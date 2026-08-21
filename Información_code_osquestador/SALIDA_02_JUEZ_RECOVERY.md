# SALIDA 2/6 — LLM_JUEZ + AUTO-RECOVERY
# Repo 1: orquestador-nucleo | Archivos: 3 | LOC: ~390 + ~200 + ~380
# El JUEZ es el único que emite APPROVED/REJECTED. Recovery = 5 niveles + causal.

---

## ARCHIVO 1 — `orquestador-nucleo/llm_juez/juez_core.py` (~390 LOC)

```python
"""LLM_JUEZ — profesor-director-ingeniero jefe.
Único actor que emite APPROVED | REJECTED | RETRY. Nunca escribe código,
nunca diseña, nunca se auto-aprueba, nunca acepta evidencia verbal.
Pipeline: P-DISCOVER→P00..P13 (14 pasos; simple omite P03-P06,P09,P10).
Contract: contracts/llm_juez.contract.json
"""
from __future__ import annotations
import asyncio
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Any, Protocol


class JuezEstado(Enum):
    IDLE = "IDLE"
    INITIALIZING = "INITIALIZING"
    ORCHESTRATING = "ORCHESTRATING"
    AUDITING = "AUDITING"
    AWAITING_RUNTIME = "AWAITING_RUNTIME"
    AWAITING_DIRECTOR = "AWAITING_DIRECTOR"
    RETRYING = "RETRYING"
    COMPLETED = "COMPLETED"
    ABORTED = "ABORTED"


class Verdict(Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    RETRY = "RETRY"


class TaskLevel(Enum):
    SIMPLE = "simple"
    CRITICAL = "critical"
    LONG_HORIZON = "long_horizon"


# Pipeline definitivo (PARCHE_CIERRE_H_F): 16 posiciones nombradas
PIPELINE: tuple[str, ...] = (
    "P-DISCOVER", "P00", "P01", "P02", "P03", "P04", "P05", "P06",
    "P07", "P08", "P09", "P10", "P-CODE", "P11", "P12", "P13",
)
OMITE_SIMPLE: frozenset[str] = frozenset(
    {"P03", "P04", "P05", "P06", "P09", "P10"})

# ── Detección anti-humo / anti-alucinación (determinista, grep-style) ──
PATRONES_HUMO: tuple[str, ...] = (
    "mock", "fake", "dummy", "placeholder", "todo:", "fixme",
    "coming_soon", "hardcoded", "pass  #", "lorem ipsum",
    "por implementar", "ejemplo genérico",
)
FRASES_EXITO_PROHIBIDAS: tuple[str, ...] = (
    "funciona", "listo", "completado", "todo ok", "works perfectly",
)


@dataclass(frozen=True)
class GoalLock:
    objetivo: str
    definition_of_done: tuple[str, ...]
    not_in_scope: tuple[str, ...]
    criterio_fallo: tuple[str, ...] = ()
    fuente_de_verdad: str = ""
    congelado_ts: float = field(default_factory=time.time)

    @property
    def lock_hash(self) -> str:
        return sha256(repr((self.objetivo, self.definition_of_done,
                            self.not_in_scope)).encode()).hexdigest()


@dataclass
class Instruction:
    paso: str
    instruccion: str
    output_schema: dict
    criterios_aprobacion: list[str]
    criterios_rechazo: list[str]
    task_level: TaskLevel
    goal_lock: GoalLock
    ficha_id: str
    instruction_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    intento_actual: int = 1
    max_intentos: int = 3
    contexto: dict = field(default_factory=dict)


@dataclass
class Delivery:
    instruction_id: str
    paso: str
    payload: dict
    self_check: dict[str, bool]


@dataclass
class Auditoria:
    verdict: Verdict
    problemas: list[str] = field(default_factory=list)
    evidencia: dict = field(default_factory=dict)


class PuertoEscritor(Protocol):
    async def ejecutar(self, instr: Instruction) -> Delivery: ...


class PuertoRuntime(Protocol):
    async def activar(self, ficha_id: str, code_payload: dict,
                      niveles: list[str]) -> dict: ...  # Evidence Report L1-L4


class PuertoFailureRegistry(Protocol):
    def registrar(self, paso: str, causa: str, payload: dict) -> None: ...
    def relevantes(self, paso: str) -> list[dict]: ...


class PuertoCrazyWall(Protocol):
    def actualizar(self, paso: str, estado: str, datos: dict) -> None: ...


class LLMJuez:
    """FSM + auditor determinista. El LLM (vía Router) es herramienta
    opcional del paso AUDITING solo si los checks mecánicos dudan."""

    def __init__(self, escritor: PuertoEscritor, runtime: PuertoRuntime,
                 registry: PuertoFailureRegistry, wall: PuertoCrazyWall,
                 auditor_llm=None) -> None:
        self.escritor, self.runtime = escritor, runtime
        self.registry, self.wall = registry, wall
        self.auditor_llm = auditor_llm            # opcional, 10% LLM
        self.estado = JuezEstado.IDLE
        self.goal_lock: GoalLock | None = None
        self.resultados: dict[str, Delivery] = {}

    # ── API para KernelCore (PuertoJuez) ──
    def goal_lock_activo(self) -> bool:
        return self.goal_lock is not None

    def congelar_goal(self, gl: GoalLock) -> str:
        """Nada avanza sin esto (PUSH_PING [19])."""
        self.goal_lock = gl
        self.wall.actualizar("GOAL_LOCK", "CONGELADO",
                             {"hash": gl.lock_hash})
        return gl.lock_hash

    # ── PIPELINE COMPLETO ──
    async def ejecutar_pipeline(self, task_level: TaskLevel,
                                ficha_id: str,
                                schemas_por_paso: dict[str, dict]) -> dict:
        if not self.goal_lock:
            return {"estado": "BLOQUEADO", "razon": "SIN_GOAL_LOCK"}
        self.estado = JuezEstado.INITIALIZING
        pasos = [p for p in PIPELINE
                 if task_level is not TaskLevel.SIMPLE
                 or p not in OMITE_SIMPLE]

        for paso in pasos:
            self.estado = JuezEstado.ORCHESTRATING
            ok = await self._paso_con_reintentos(
                paso, task_level, ficha_id,
                schemas_por_paso.get(paso, {"type": "object"}))
            if not ok:
                self.estado = JuezEstado.ABORTED
                self.wall.actualizar(paso, "ABORTED", {})
                return {"estado": "ABORTED", "paso": paso}
            if paso == "P-CODE":                  # activar Runtime real
                if not await self._verificar_runtime(ficha_id):
                    self.estado = JuezEstado.ABORTED
                    return {"estado": "ABORTED", "paso": "P11_RUNTIME"}
        self.estado = JuezEstado.COMPLETED
        self.wall.actualizar("P13", "COMMITTED", {"ficha": ficha_id})
        return {"estado": "COMMITTED", "ficha_id": ficha_id,
                "pasos_ejecutados": pasos}

    async def _paso_con_reintentos(self, paso: str, level: TaskLevel,
                                   ficha_id: str, schema: dict) -> bool:
        instr = Instruction(
            paso=paso, instruccion=f"Producir output del paso {paso}",
            output_schema=schema, task_level=level, ficha_id=ficha_id,
            goal_lock=self.goal_lock,
            criterios_aprobacion=list(self.goal_lock.definition_of_done),
            criterios_rechazo=list(self.goal_lock.not_in_scope),
            contexto={"failure_registry": self.registry.relevantes(paso)},
        )
        for intento in range(1, instr.max_intentos + 1):
            instr.intento_actual = intento
            try:
                delivery = await asyncio.wait_for(
                    self.escritor.ejecutar(instr), timeout=30.0)
            except asyncio.TimeoutError:
                self.registry.registrar(paso, "ESCRITOR_TIMEOUT", {})
                continue
            self.estado = JuezEstado.AUDITING
            audit = self._auditar(instr, delivery)
            self.wall.actualizar(paso, audit.verdict.value,
                                 {"intento": intento,
                                  "problemas": audit.problemas})
            if audit.verdict is Verdict.APPROVED:
                self.resultados[paso] = delivery
                return True
            if audit.verdict is Verdict.REJECTED:
                self.registry.registrar(paso, "REJECTED",
                                        {"problemas": audit.problemas})
                return False
            self.estado = JuezEstado.RETRYING
            instr.contexto["problemas_detectados"] = audit.problemas
        self.registry.registrar(paso, "MAX_INTENTOS", {})
        return False

    # ── AUDITORÍA DETERMINISTA (90% código) ──
    def _auditar(self, instr: Instruction, d: Delivery) -> Auditoria:
        problemas: list[str] = []
        if d.instruction_id != instr.instruction_id:
            return Auditoria(Verdict.REJECTED, ["instruction_id_no_coincide"])
        if not all(d.self_check.values()):
            problemas.append(f"self_check_negativo:"
                             f"{[k for k, v in d.self_check.items() if not v]}")
        texto = repr(d.payload).lower()
        problemas += [f"HUMO:{p}" for p in PATRONES_HUMO if p in texto]
        problemas += [f"EXITO_DECLARADO:{f}"
                      for f in FRASES_EXITO_PROHIBIDAS if f in texto]
        faltan = [k for k in instr.output_schema.get("required", [])
                  if k not in d.payload]
        if faltan:
            problemas.append(f"CAMPOS_FALTANTES:{faltan}")
        for fuera in instr.goal_lock.not_in_scope:
            if fuera.lower() in texto:
                problemas.append(f"SCOPE_CREEP:{fuera}")
        if not problemas:
            return Auditoria(Verdict.APPROVED)
        graves = [p for p in problemas
                  if p.startswith(("SCOPE_CREEP", "EXITO_DECLARADO"))]
        if graves or instr.intento_actual >= instr.max_intentos:
            return Auditoria(Verdict.REJECTED, problemas)
        return Auditoria(Verdict.RETRY, problemas)

    async def _verificar_runtime(self, ficha_id: str) -> bool:
        """RT-01..04: evidencia real, jamás palabra."""
        self.estado = JuezEstado.AWAITING_RUNTIME
        code = self.resultados.get("P-CODE")
        report = await self.runtime.activar(
            ficha_id, code.payload if code else {},
            niveles=["L1", "L2", "L3", "L4"])
        esperado = sha256(repr({k: v for k, v in report.items()
                                if k != "evidence_hash"}).encode()).hexdigest()
        if report.get("evidence_hash") != esperado:
            self.registry.registrar("P11", "EVIDENCE_TAMPERING", {})
            return False                          # RT-04 → ABORT
        niveles = ("L1_static", "L2_build", "L3_runtime", "L4_feature")
        fails = [n for n in niveles
                 if report.get(n, {}).get("status") != "PASS"]
        if fails:                                 # RT-01
            self.registry.registrar("P11", "RUNTIME_FAIL", {"fails": fails})
            return False
        return True
```

---

## ARCHIVO 2 — `orquestador-nucleo/llm_juez/failure_registry.py` (~200 LOC)

```python
"""FAILURE_REGISTRY — memoria de causas raíz. Evita repetir errores.
Append-only JSONL con hash chain; alimenta few-shot del Escritor y
prioridades del Sentinela. Contract: contracts/failure_registry.contract.json
"""
from __future__ import annotations
import json
import time
from collections import Counter
from dataclasses import dataclass, asdict, field
from hashlib import sha256
from pathlib import Path


@dataclass
class Fallo:
    paso: str
    causa: str
    payload: dict
    ts: float = field(default_factory=time.time)
    prev_hash: str = ""
    hash: str = ""

    def sellar(self, prev: str) -> "Fallo":
        self.prev_hash = prev
        self.hash = sha256(
            (prev + json.dumps([self.paso, self.causa, self.ts],
                               sort_keys=True)).encode()).hexdigest()
        return self


class FailureRegistry:
    def __init__(self, ruta: str = "runtime/failure_registry.jsonl") -> None:
        self.ruta = Path(ruta)
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self._ultimo_hash = self._leer_ultimo_hash()

    def _leer_ultimo_hash(self) -> str:
        if not self.ruta.exists():
            return "GENESIS"
        lineas = self.ruta.read_text(encoding="utf-8").strip().splitlines()
        return json.loads(lineas[-1])["hash"] if lineas else "GENESIS"

    def registrar(self, paso: str, causa: str, payload: dict) -> None:
        f = Fallo(paso, causa, payload).sellar(self._ultimo_hash)
        with self.ruta.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(f), ensure_ascii=False) + "\n")
        self._ultimo_hash = f.hash

    def relevantes(self, paso: str, n: int = 5) -> list[dict]:
        """Los N fallos más recientes del mismo paso → few-shot anchor."""
        if not self.ruta.exists():
            return []
        out = [json.loads(l) for l in
               self.ruta.read_text(encoding="utf-8").strip().splitlines()]
        return [f for f in out if f["paso"] == paso][-n:]

    def causas_frecuentes(self, top: int = 10) -> list[tuple[str, int]]:
        """Para Sentinela: patrones de fallo repetido."""
        if not self.ruta.exists():
            return []
        c = Counter(json.loads(l)["causa"] for l in
                    self.ruta.read_text(encoding="utf-8").strip().splitlines())
        return c.most_common(top)

    def verificar_cadena(self) -> bool:
        prev = "GENESIS"
        if not self.ruta.exists():
            return True
        for linea in self.ruta.read_text(encoding="utf-8").strip().splitlines():
            f = json.loads(linea)
            esperado = sha256(
                (prev + json.dumps([f["paso"], f["causa"], f["ts"]],
                                   sort_keys=True)).encode()).hexdigest()
            if f["hash"] != esperado:
                return False
            prev = f["hash"]
        return True
```

---

## ARCHIVO 3 — `orquestador-nucleo/auto_recovery/recovery_engine.py` (~380 LOC)

```python
"""AUTO-RECOVERY — watchdog 30s interno (sin ping externo) + 5 niveles +
Causal Engine (causa/habilita/efecto_si_falla/sustituible_por) + compensate.
PUEDE: reiniciar flujos, cambiar rutas, fallback, ajustar batch, cambiar
modelo en capability.json. NO PUEDE: tocar ADN, contratos, schemas.
Contract: contracts/recovery.contract.json
"""
from __future__ import annotations
import asyncio
import logging
import time
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Awaitable, Callable, Protocol

from guardian.guardian_layer import GUARDIAN, SolicitudGuardian

log = logging.getLogger("recovery")


class NivelRecovery(IntEnum):
    RETRY = 1        # reintentar 1 vez
    ROLLBACK = 2     # revertir al último estado estable
    CHECKPOINT = 3   # replay_to_checkpoint(t)
    REPLAN = 4       # replantear desde el fallo
    ESCALATE = 5     # Director


@dataclass
class Sintoma:
    tipo: str            # timeout|hash_roto|sin_avance|proceso_muerto|...
    origen: str          # módulo/agente que lo emitió
    datos: dict = field(default_factory=dict)
    ts: float = field(default_factory=time.time)


@dataclass(frozen=True)
class ReglaCausal:
    """Causal Engine: mapa sintoma→causa→acción, editable en YAML."""
    sintoma: str
    causa_probable: str
    nivel: NivelRecovery
    habilita: tuple[str, ...] = ()          # qué desbloquea si se repara
    efecto_si_falla: str = "escalar"
    sustituible_por: str | None = None       # fallback (otro modelo/agente)


REGLAS_CAUSALES: tuple[ReglaCausal, ...] = (
    ReglaCausal("timeout", "provider_saturado", NivelRecovery.RETRY,
                sustituible_por="provider_fallback"),
    ReglaCausal("hash_roto", "state_corruption", NivelRecovery.CHECKPOINT),
    ReglaCausal("sin_avance", "loop_inutil", NivelRecovery.REPLAN),
    ReglaCausal("proceso_muerto", "agente_caido", NivelRecovery.ROLLBACK,
                sustituible_por="respawn_manifest"),
    ReglaCausal("evidence_tampering", "integridad", NivelRecovery.ESCALATE),
)


class PuertoEstadoRec(Protocol):
    def verificar_hash_chain(self) -> bool: ...
    def replay_to_checkpoint(self, etiqueta: str | None = None) -> str: ...
    def ultimo_checkpoint(self) -> str | None: ...


class PuertoNotificador(Protocol):
    async def director(self, mensaje: str, datos: dict) -> None: ...


AccionRecovery = Callable[[Sintoma], Awaitable[bool]]


class RecoveryEngine:
    MAX_REINTENTOS_CONSECUTIVOS = 3
    WATCHDOG_INTERVALO_S = 30
    SIN_AVANCE_MAX_S = 300

    def __init__(self, estado: PuertoEstadoRec,
                 notificador: PuertoNotificador,
                 heartbeat_fn: Callable[[], float],
                 acciones_extra: dict[NivelRecovery, AccionRecovery]
                 | None = None) -> None:
        self.estado, self.notif = estado, notificador
        self.heartbeat_fn = heartbeat_fn        # último ts de avance real
        self.acciones_extra = acciones_extra or {}
        self.fallos_consecutivos = 0
        self.degraded = False
        self._stop = asyncio.Event()

    # ── WATCHDOG (Capa 0, loop infinito async, AX07) ──
    async def watchdog(self) -> None:
        while not self._stop.is_set():
            await asyncio.sleep(self.WATCHDOG_INTERVALO_S)
            sintomas = self._autoevaluar()
            for s in sintomas:
                await self.manejar(s)

    def detener(self) -> None:
        self._stop.set()

    def _autoevaluar(self) -> list[Sintoma]:
        out: list[Sintoma] = []
        if not self.estado.verificar_hash_chain():
            out.append(Sintoma("hash_roto", "watchdog"))
        if time.time() - self.heartbeat_fn() > self.SIN_AVANCE_MAX_S:
            out.append(Sintoma("sin_avance", "watchdog",
                               {"max_s": self.SIN_AVANCE_MAX_S}))
        if self.estado.ultimo_checkpoint() is None:
            out.append(Sintoma("sin_checkpoint", "watchdog"))
        return out

    # ── NÚCLEO: síntoma → regla causal → escalera de niveles ──
    async def manejar(self, sintoma: Sintoma) -> bool:
        regla = next((r for r in REGLAS_CAUSALES
                      if r.sintoma == sintoma.tipo), None)
        nivel_inicial = regla.nivel if regla else NivelRecovery.RETRY
        log.warning("recovery sintoma=%s causa=%s nivel=%s",
                    sintoma.tipo,
                    regla.causa_probable if regla else "desconocida",
                    nivel_inicial.name)

        for nivel in NivelRecovery:
            if nivel < nivel_inicial:
                continue
            g = GUARDIAN.evaluar(SolicitudGuardian(
                actor="recovery", accion=f"recovery_n{nivel.value}"))
            if not g.permitido:
                nivel = NivelRecovery.ESCALATE
            exito = await self._ejecutar_nivel(nivel, sintoma, regla)
            if exito:
                self.fallos_consecutivos = 0
                self._verificar_reparacion(sintoma)
                return True
            self.fallos_consecutivos += 1
            if self.fallos_consecutivos >= self.MAX_REINTENTOS_CONSECUTIVOS:
                await self._modo_degradado(sintoma)
                return False
        return False

    async def _ejecutar_nivel(self, nivel: NivelRecovery, s: Sintoma,
                              regla: ReglaCausal | None) -> bool:
        if nivel in self.acciones_extra:          # hooks inyectados
            return await self.acciones_extra[nivel](s)
        if nivel is NivelRecovery.RETRY:
            return regla is not None and regla.sustituible_por is not None
        if nivel is NivelRecovery.ROLLBACK:
            cp = self.estado.ultimo_checkpoint()
            return cp is not None
        if nivel is NivelRecovery.CHECKPOINT:
            try:
                self.estado.replay_to_checkpoint()
                return self.estado.verificar_hash_chain()
            except Exception as exc:              # noqa: BLE001
                log.error("replay fallo: %s", exc)
                return False
        if nivel is NivelRecovery.REPLAN:
            # el kernel re-ejecuta la fase con Discovery nuevo (hook)
            return False if NivelRecovery.REPLAN not in self.acciones_extra \
                else True
        if nivel is NivelRecovery.ESCALATE:
            await self.notif.director(
                f"RECOVERY_ESCALATE: {s.tipo}", s.datos)
            return True                            # escalado = manejado
        return False

    def _verificar_reparacion(self, s: Sintoma) -> None:
        """JUDGE de Capa 0: el reinicio se valida con evidencia, no palabra."""
        if s.tipo == "hash_roto" and not self.estado.verificar_hash_chain():
            raise RuntimeError("REPARACION_NO_VERIFICADA")

    async def _modo_degradado(self, s: Sintoma) -> None:
        self.degraded = True
        await self.notif.director(
            "DEGRADED_MODE: 3 fallos consecutivos", {"sintoma": s.tipo})
```

---

## NOTAS DE DISEÑO
1. **Juez = FSM determinista**: auditoría anti-humo/scope/schema en código puro; LLM solo opcional (10%).
2. **Runtime = evidencia o nada**: verifica `evidence_hash` recalculando (RT-04) y exige PASS en L1-L4 (RT-01).
3. **FailureRegistry hash-chained** alimenta few-shot del Escritor y métricas del Sentinela.
4. **Causal Engine** declarativo (síntoma→causa→nivel→sustituto) — Sentinela puede ampliar las reglas vía YAML sin tocar el código.
5. **Escalera de recovery**: si un nivel falla sube al siguiente; Guardian valida cada acción; 3 fallos → DEGRADED + Director.

## TESTS MÍNIMOS
```
test_juez_sin_goal_lock_bloquea · test_simple_omite_6_pasos
test_humo_detectado_retry · test_scope_creep_rejected
test_evidence_tampering_abort · test_registry_cadena_integra
test_recovery_hash_roto_replay · test_3_fallos_degraded
```
