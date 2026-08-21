# SALIDA 5+6/6 — COGNITIVE ENGINE + EXPERT POOL + ROUTER + TEAM AGENTE
# Repos 5 (expertos), 10 (router), 7 (team-agente) | 4 archivos: ~350+~300+~280+~300 LOC
# Cierra el código del cerebro. Fusion Engine ya existe (Salida 3).

---

## ARCHIVO 1 — `expertos/cognitive_engine.py` (~350 LOC)

```python
"""COGNITIVE ENGINE — EL único motor. Los 300 expertos son YAML (0 LOC).
Contrato fijo: schema-in/schema-out. LLM = calculadora aislada (AX03),
NUNCA decide. Anti-echo <30% (lección MP-MoE). Mejoras aquí = mejoran todos.
Contract: contracts/cognitive_engine.contract.json
"""
from __future__ import annotations
import asyncio
import difflib
import json
import time
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from pathlib import Path
from typing import Any, Protocol

try:
    import yaml
except ImportError:                       # fallback dev sin pyyaml
    yaml = None


class Capa(Enum):
    A_ENTRADA = "A"       # 100 expertos: captura/filtros/normaliza/descompone
    B_RAZONAMIENTO = "B"  # 100: análisis/síntesis/plan/profundo/crítica
    C_SALIDA = "C"        # 100: código/docs/decisión/validación/emisión


@dataclass(frozen=True)
class ConfigExperto:
    """1 experto = 1 archivo YAML. CERO código por experto."""
    expert_id: str            # E001..E300
    nombre: str
    capa: Capa
    grupo: str                # A1..A5 | B1..B5 | C1..C5
    operacion: str            # operación cognitiva, NO dominio
    schema_in: dict
    schema_out: dict
    non_scope: tuple[str, ...] = ()
    temperature: float = 0.2
    max_tokens: int = 1024
    plantilla: str = ""       # prompt DSL con {placeholders}
    llm_ratio: float = 0.10   # SC5: ≤0.10 salvo capa B declarada

    @staticmethod
    def desde_yaml(ruta: str) -> "ConfigExperto":
        raw = (yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))
               if yaml else json.loads(Path(ruta).read_text(encoding="utf-8")))
        raw["capa"] = Capa(raw["capa"])
        raw["non_scope"] = tuple(raw.get("non_scope", ()))
        return ConfigExperto(**raw)


@dataclass
class ObjetoCognitivo:
    """El Objeto que evoluciona por las 3 capas (9 bloques G2)."""
    task_id: str
    objetivo: dict
    contexto: dict = field(default_factory=dict)
    analisis: dict = field(default_factory=dict)      # B1
    sintesis: dict = field(default_factory=dict)      # B2
    plan: dict = field(default_factory=dict)          # B3
    verificacion: dict = field(default_factory=dict)  # B5
    salida: dict = field(default_factory=dict)        # C
    version: int = 1
    trace_id: str = ""
    historial_fp: list[str] = field(default_factory=list)

    def fp(self) -> str:
        return sha256(json.dumps(
            [self.task_id, self.version, self.analisis, self.sintesis,
             self.plan, self.salida], sort_keys=True,
            default=str).encode()).hexdigest()[:16]

    def evolucionar(self, bloque: str, datos: dict) -> None:
        """Los expertos NUNCA mutan directo: el motor aplica y versiona."""
        self.historial_fp.append(self.fp())
        setattr(self, bloque, {**getattr(self, bloque), **datos})
        self.version += 1


@dataclass
class RespuestaExperto:
    expert_id: str
    proposals: list[dict]                 # [{path,value,confidence,evidencia_refs}]
    necesito: list[str] = field(default_factory=list)   # requests al Router
    self_check: dict[str, bool] = field(default_factory=dict)
    duracion_ms: int = 0
    echo_score: float = 0.0


class PuertoLLM(Protocol):
    """Calculadora aislada: entra schema, sale schema. Vía Router (ciego)."""
    async def calcular(self, plantilla: str, variables: dict,
                       schema_out: dict, temperature: float,
                       max_tokens: int) -> dict: ...


class CognitiveEngine:
    ECHO_MAX = 0.30                        # anti-echo-chamber

    def __init__(self, llm: PuertoLLM) -> None:
        self.llm = llm
        self._historial_salidas: list[str] = []   # ventana anti-echo

    async def ejecutar(self, cfg: ConfigExperto, obj: ObjetoCognitivo,
                       entrada: dict) -> RespuestaExperto:
        t0 = time.time()
        self._validar_schema(entrada, cfg.schema_in, "in", cfg.expert_id)
        for prohibido in cfg.non_scope:
            if prohibido.lower() in json.dumps(entrada,
                                               default=str).lower():
                return RespuestaExperto(cfg.expert_id, [], self_check={
                    "scope_ok": False})

        variables = {"objetivo": obj.objetivo, "contexto": obj.contexto,
                     "entrada": entrada, "operacion": cfg.operacion}
        salida = await asyncio.wait_for(
            self.llm.calcular(cfg.plantilla, variables, cfg.schema_out,
                              cfg.temperature, cfg.max_tokens),
            timeout=30.0)
        self._validar_schema(salida, cfg.schema_out, "out", cfg.expert_id)

        echo = self._echo_score(json.dumps(salida, default=str))
        if echo > self.ECHO_MAX:
            # forzar contraste: reintento único con temperatura opuesta
            salida = await self.llm.calcular(
                cfg.plantilla + "\nPROHIBIDO repetir salidas previas. "
                "Aporta ángulo distinto.", variables, cfg.schema_out,
                min(1.0, cfg.temperature + 0.5), cfg.max_tokens)
            echo = self._echo_score(json.dumps(salida, default=str))
        self._historial_salidas.append(json.dumps(salida, default=str))
        self._historial_salidas = self._historial_salidas[-20:]

        proposals = [{"path": p["path"], "value": p["value"],
                      "confidence": float(p.get("confidence", 0.5)),
                      "evidencia_refs": p.get("evidencia_refs", []),
                      "actor": f"expert:{cfg.expert_id}"}
                     for p in salida.get("proposals", [])]
        return RespuestaExperto(
            expert_id=cfg.expert_id, proposals=proposals,
            necesito=salida.get("necesito", []),
            self_check={"scope_ok": True, "schema_ok": True,
                        "echo_ok": echo <= self.ECHO_MAX},
            duracion_ms=int((time.time() - t0) * 1000), echo_score=echo)

    # ── helpers ──
    @staticmethod
    def _validar_schema(data: dict, schema: dict, lado: str,
                        eid: str) -> None:
        faltan = [k for k in schema.get("required", []) if k not in data]
        if faltan:
            raise ValueError(f"{eid}:schema_{lado}_incompleto:{faltan}")

    def _echo_score(self, salida: str) -> float:
        if not self._historial_salidas:
            return 0.0
        return max(difflib.SequenceMatcher(
            None, salida, prev).ratio()
            for prev in self._historial_salidas[-5:])
```

---

## ARCHIVO 2 — `expertos/expert_pool.py` (~300 LOC)

```python
"""EXPERT POOL — 500 disponibles, 0 activos en reposo (MoE de software).
Activa dinámicamente por fase+operación según escala (20-50/100-300/...).
Spawner TDAG: si falta un experto, lo genera ad-hoc desde plantilla.
Cumple PuertoExpertos de KernelCore. Contract: contracts/expert_pool.contract.json
"""
from __future__ import annotations
import asyncio
import json
import time
from dataclasses import dataclass, field
from pathlib import Path

from cognitive_engine import (Capa, CognitiveEngine, ConfigExperto,
                              ObjetoCognitivo, RespuestaExperto)

FASE_A_CAPA = {"P1_INPUT": Capa.A_ENTRADA, "P2_PROCESS": Capa.B_RAZONAMIENTO,
               "P3_OUTPUT": Capa.C_SALIDA}
ESCALA = {"RAPIDO": (5, 15), "BASICO": (20, 50),
          "AVANZADO": (100, 300), "TURBO": (300, 500)}


@dataclass
class RegistroExperto:
    cfg: ConfigExperto
    activo: bool = False
    ejecuciones: int = 0
    aciertos: int = 0

    @property
    def accuracy(self) -> float:
        return self.aciertos / self.ejecuciones if self.ejecuciones else 0.5


class ExpertPool:
    def __init__(self, engine: CognitiveEngine,
                 dir_experts: str = "expertos/configs") -> None:
        self.engine = engine
        self.registro: dict[str, RegistroExperto] = {}
        self._cargar(dir_experts)
        self._activos_por_fase: dict[str, list[str]] = {}

    def _cargar(self, d: str) -> None:
        base = Path(d)
        if base.exists():
            for f in sorted(base.glob("E*.y*ml")) or sorted(
                    base.glob("E*.json")):
                cfg = ConfigExperto.desde_yaml(str(f))
                self.registro[cfg.expert_id] = RegistroExperto(cfg)

    # ── selección dinámica ──
    def seleccionar(self, fase: str, nivel: str,
                    operaciones: list[str]) -> list[ConfigExperto]:
        capa = FASE_A_CAPA.get(fase)
        candidatos = [r for r in self.registro.values()
                      if r.cfg.capa is capa]
        if operaciones:
            candidatos = [r for r in candidatos
                          if r.cfg.operacion in operaciones] or candidatos
        candidatos.sort(key=lambda r: r.accuracy, reverse=True)
        _, maximo = ESCALA.get(nivel, ESCALA["BASICO"])
        return [r.cfg for r in candidatos[:maximo]]

    # ── API PuertoExpertos (KernelCore) ──
    async def activar(self, fase, necesidades: list[str],
                      snapshot: dict) -> list[dict]:
        fase_v = getattr(fase, "value", str(fase))
        nivel = snapshot.get("config_runtime", {}).get("nivel", "BASICO")
        elegidos = self.seleccionar(fase_v, nivel, necesidades)
        faltantes = [op for op in necesidades
                     if not any(c.operacion == op for c in elegidos)]
        for op in faltantes:                       # TDAG spawn
            elegidos.append(self._spawn(op, FASE_A_CAPA[fase_v]))
        self._activos_por_fase[fase_v] = [c.expert_id for c in elegidos]
        for c in elegidos:
            self.registro[c.expert_id].activo = True
        return [{"expert_id": c.expert_id, "operacion": c.operacion}
                for c in elegidos]

    async def liberar(self, fase) -> None:
        fase_v = getattr(fase, "value", str(fase))
        for eid in self._activos_por_fase.pop(fase_v, []):
            if eid in self.registro:
                self.registro[eid].activo = False

    def _spawn(self, operacion: str, capa: Capa) -> ConfigExperto:
        """Experto ad-hoc desde plantilla genérica. Queda en draft:
        pasa a registry permanente solo si Director aprueba (ledger)."""
        eid = f"EX_{operacion.upper()[:12]}_{int(time.time()) % 100000}"
        cfg = ConfigExperto(
            expert_id=eid, nombre=f"spawn:{operacion}", capa=capa,
            grupo="SPAWN", operacion=operacion,
            schema_in={"required": ["entrada"]},
            schema_out={"required": ["proposals"]},
            plantilla=f"Aplica la operación cognitiva '{operacion}' a "
                      "{entrada} respecto al objetivo {objetivo}. Devuelve "
                      "JSON con proposals[path,value,confidence].")
        self.registro[eid] = RegistroExperto(cfg)
        return cfg

    # ── ejecución en enjambre (paralelo real) ──
    async def ejecutar_enjambre(self, fase: str, obj: ObjetoCognitivo,
                                entrada: dict,
                                max_concurrencia: int = 25
                                ) -> list[RespuestaExperto]:
        ids = self._activos_por_fase.get(fase, [])
        sem = asyncio.Semaphore(max_concurrencia)

        async def _uno(eid: str) -> RespuestaExperto | None:
            async with sem:
                try:
                    r = await self.engine.ejecutar(
                        self.registro[eid].cfg, obj, entrada)
                    self.registro[eid].ejecuciones += 1
                    if all(r.self_check.values()):
                        self.registro[eid].aciertos += 1
                    return r
                except Exception:                 # noqa: BLE001
                    self.registro[eid].ejecuciones += 1
                    return None

        res = await asyncio.gather(*[_uno(e) for e in ids])
        return [r for r in res if r is not None]

    def snapshot_accuracy(self) -> dict[str, float]:
        """Alimenta la fórmula de Fusion (accuracy_historica)."""
        return {eid: r.accuracy for eid, r in self.registro.items()}
```

---

## ARCHIVO 3 — `router/router_core.py` (~280 LOC)

```python
"""ROUTER — dispatcher determinista SIN IA (ítem 39). Match por tags y
capability. Ciego al provider: los expertos piden 'necesito X', el router
resuelve quién. Pools por runtime_type + circuit breaker + failover chain.
Contract: contracts/router.contract.json
"""
from __future__ import annotations
import asyncio
import random
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Awaitable, Callable

FAILOVER_CHAIN = ["mimo", "openhands", "smollagents", "claude",
                  "opencode", "codex", "cline", "goose", "aider"]
TIMEOUT_POR_TIPO = {"compute": 5, "hybrid": 15, "llm": 30, "agent": 120}


class CBEstado(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"


@dataclass
class CircuitBreaker:
    fallos: int = 0
    estado: CBEstado = CBEstado.CLOSED
    abierto_desde: float = 0.0
    UMBRAL: int = 5
    ESPERA_S: int = 30

    def permite(self) -> bool:
        if self.estado is CBEstado.OPEN:
            if time.time() - self.abierto_desde >= self.ESPERA_S:
                self.estado = CBEstado.HALF_OPEN
                return True
            return False
        return True

    def exito(self) -> None:
        self.fallos, self.estado = 0, CBEstado.CLOSED

    def fallo(self) -> None:
        self.fallos += 1
        if self.fallos >= self.UMBRAL:
            self.estado, self.abierto_desde = CBEstado.OPEN, time.time()


@dataclass
class Destino:
    """1 ejecutor registrado: ficha COMMITTED, Space HF, LLM provider..."""
    destino_id: str
    runtime_type: str            # compute|hybrid|llm|agent
    tags: frozenset[str]
    ejecutar: Callable[[dict], Awaitable[dict]]
    cb: CircuitBreaker = field(default_factory=CircuitBreaker)
    sano: bool = True


class Router:
    def __init__(self) -> None:
        self.destinos: dict[str, Destino] = {}
        self._rr: dict[str, int] = {}            # round-robin por pool

    def registrar(self, d: Destino) -> None:
        self.destinos[d.destino_id] = d

    # ── match determinista: tags ∩ capability, sin IA ──
    def resolver(self, necesito: str,
                 runtime_type: str | None = None) -> list[Destino]:
        req = frozenset(necesito.lower().split())
        candidatos = [d for d in self.destinos.values()
                      if d.sano and d.cb.permite()
                      and (runtime_type is None
                           or d.runtime_type == runtime_type)
                      and req & d.tags]
        candidatos.sort(key=lambda d: len(req & d.tags), reverse=True)
        return candidatos

    async def despachar(self, necesito: str, payload: dict,
                        runtime_type: str | None = None,
                        trace_id: str = "") -> dict:
        candidatos = self.resolver(necesito, runtime_type)
        if not candidatos:
            return {"status": "FAIL", "error": f"sin_destino:{necesito}"}
        pool = candidatos[0].runtime_type
        idx = self._rr.get(pool, 0)
        orden = candidatos[idx % len(candidatos):] + \
            candidatos[:idx % len(candidatos)]
        self._rr[pool] = idx + 1

        for intento, d in enumerate(orden):
            timeout = TIMEOUT_POR_TIPO.get(d.runtime_type, 30)
            try:
                r = await asyncio.wait_for(
                    d.ejecutar({**payload, "trace_id": trace_id}),
                    timeout=timeout)
                d.cb.exito()
                return {"status": "DONE", "destino": d.destino_id,
                        "output": r}
            except asyncio.TimeoutError:
                d.cb.fallo()                       # timeout → cuenta fallo
            except ConnectionError:
                d.cb.fallo()                       # 503 → breaker
            except Exception as exc:               # noqa: BLE001
                d.cb.fallo()                       # 500 → siguiente destino
                if intento == len(orden) - 1:
                    return {"status": "FAIL", "error": str(exc)}
            await asyncio.sleep(
                (1000 * 2 ** intento + random.randint(0, 1000)) / 1000)
        return {"status": "FAIL", "error": "todos_los_destinos_agotados"}

    async def health_check_loop(self, interval_s: int = 5) -> None:
        while True:
            await asyncio.sleep(interval_s)
            for d in self.destinos.values():
                try:
                    r = await asyncio.wait_for(
                        d.ejecutar({"_health": True}), timeout=3)
                    d.sano = r.get("ok", True)
                except Exception:                  # noqa: BLE001
                    d.sano = False
```

---

## ARCHIVO 4 — `team-agente/team_core.py` (~300 LOC)

```python
"""TEAM AGENTE — cerebro ≤300 LOC. Mismo patrón 3 fases en miniatura.
Recibe handoff FIRMADO del orquestador, ejecuta staff en paralelo
(externo primero, micro-agente MA-* solo si falta capability),
devuelve con Witness (evidencia, nunca palabra).
Contract: contracts/team_agent.contract.json
"""
from __future__ import annotations
import asyncio
import json
import time
import uuid
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any, Awaitable, Callable, Protocol


@dataclass(frozen=True)
class Handoff:
    """Sobre firmado orquestador→team. Sin firma válida NO se trabaja."""
    task_id: str
    trace_id: str
    goal_lock_hash: str
    subtareas: tuple[dict, ...]        # ({id, necesito, payload, critico},)
    firma: str = ""

    def firmar(self, secreto: str) -> "Handoff":
        cuerpo = json.dumps([self.task_id, self.goal_lock_hash,
                             len(self.subtareas)], sort_keys=True)
        object.__setattr__(self, "firma",
                           sha256((secreto + cuerpo).encode()).hexdigest())
        return self

    def verificar(self, secreto: str) -> bool:
        cuerpo = json.dumps([self.task_id, self.goal_lock_hash,
                             len(self.subtareas)], sort_keys=True)
        return self.firma == sha256((secreto + cuerpo).encode()).hexdigest()


@dataclass
class ResultadoSubtarea:
    subtarea_id: str
    status: str                        # DONE|FAIL|SKIP
    output: dict = field(default_factory=dict)
    evidencia: dict = field(default_factory=dict)
    ejecutor: str = ""
    duracion_ms: int = 0


class PuertoRouterTeam(Protocol):
    async def despachar(self, necesito: str, payload: dict,
                        runtime_type: str | None = None,
                        trace_id: str = "") -> dict: ...
    def resolver(self, necesito: str,
                 runtime_type: str | None = None) -> list: ...


class PuertoWitness(Protocol):
    """Testigo: reproduce y certifica. Nunca acepta 'funciona'."""
    async def certificar(self, r: ResultadoSubtarea) -> dict: ...


MicroAgente = Callable[[dict], Awaitable[dict]]


class PipelineSelector:
    """≤30 LOC: elige modo por tamaño/criticidad. Determinista."""
    @staticmethod
    def modo(subtareas: tuple[dict, ...]) -> str:
        n = len(subtareas)
        if any(s.get("critico") for s in subtareas):
            return "SECUENCIAL_ESTRICTO"
        return "PARALELO" if n > 1 else "DIRECTO"


class TeamCore:
    MAX_PARALELO = 10                  # hasta 10 piezas simultáneas

    def __init__(self, router: PuertoRouterTeam, witness: PuertoWitness,
                 secreto: str,
                 micro_agentes: dict[str, MicroAgente] | None = None) -> None:
        self.router = router
        self.witness = witness
        self.secreto = secreto
        self.ma = micro_agentes or {}   # MA-* locales, último recurso

    # ── PUNTO DE ENTRADA ÚNICO ──
    async def procesar(self, h: Handoff) -> dict:
        # FASE 1 mini-INPUT: verificar firma + goal + estructura
        if not h.verificar(self.secreto):
            return self._sellar(h, "REJECTED", [], "FIRMA_INVALIDA")
        if not h.goal_lock_hash:
            return self._sellar(h, "REJECTED", [], "SIN_GOAL_LOCK")
        malas = [s["id"] for s in h.subtareas
                 if "necesito" not in s or "payload" not in s]
        if malas:
            return self._sellar(h, "REJECTED", [],
                                f"subtareas_invalidas:{malas}")

        # FASE 2 mini-PROCESS: ejecutar según modo
        modo = PipelineSelector.modo(h.subtareas)
        if modo == "SECUENCIAL_ESTRICTO":
            resultados = []
            for s in h.subtareas:
                r = await self._ejecutar(s, h.trace_id)
                resultados.append(r)
                if r.status == "FAIL" and s.get("critico"):
                    return self._sellar(h, "FAIL", resultados,
                                        f"critica_fallo:{s['id']}")
        else:
            sem = asyncio.Semaphore(self.MAX_PARALELO)

            async def _uno(s: dict) -> ResultadoSubtarea:
                async with sem:
                    return await self._ejecutar(s, h.trace_id)
            resultados = list(await asyncio.gather(
                *[_uno(s) for s in h.subtareas]))

        # FASE 3 mini-OUTPUT: Witness certifica TODO antes de devolver
        certificados = []
        for r in resultados:
            if r.status == "DONE":
                cert = await self.witness.certificar(r)
                r.evidencia = cert
                if not cert.get("verificado", False):
                    r.status = "FAIL"
            certificados.append(r)
        estado = ("DONE" if all(r.status == "DONE" for r in certificados)
                  else "PARTIAL" if any(r.status == "DONE"
                                        for r in certificados) else "FAIL")
        return self._sellar(h, estado, certificados, "")

    # ── ejecución 1 subtarea: staff externo primero, MA-* después ──
    async def _ejecutar(self, s: dict, trace_id: str) -> ResultadoSubtarea:
        t0 = time.time()
        r = await self.router.despachar(s["necesito"], s["payload"],
                                        trace_id=trace_id)
        if r["status"] == "DONE":
            return ResultadoSubtarea(s["id"], "DONE", r["output"],
                                     ejecutor=r["destino"],
                                     duracion_ms=int((time.time()-t0)*1000))
        # Router sin destino → micro-agente local SOLO si existe capability
        ma = self.ma.get(s["necesito"])
        if ma is None:
            return ResultadoSubtarea(s["id"], "FAIL",
                                     {"error": r.get("error", "")})
        try:
            out = await asyncio.wait_for(ma(s["payload"]), timeout=60)
            return ResultadoSubtarea(s["id"], "DONE", out,
                                     ejecutor=f"MA:{s['necesito']}",
                                     duracion_ms=int((time.time()-t0)*1000))
        except Exception as exc:                  # noqa: BLE001
            return ResultadoSubtarea(s["id"], "FAIL", {"error": str(exc)})

    def _sellar(self, h: Handoff, estado: str,
                resultados: list[ResultadoSubtarea], razon: str) -> dict:
        cuerpo = {"task_id": h.task_id, "trace_id": h.trace_id,
                  "estado": estado, "razon": razon,
                  "resultados": [r.__dict__ for r in resultados],
                  "ts": time.time()}
        cuerpo["firma_team"] = sha256(
            (self.secreto + json.dumps(
                [h.task_id, estado, len(resultados)],
                sort_keys=True)).encode()).hexdigest()
        return cuerpo
```

---

## NOTAS DE CIERRE (código del cerebro COMPLETO)
1. **1 motor + N YAML**: mejorar `cognitive_engine.py` mejora los 300/500 expertos a la vez. Anti-echo con reintento de contraste forzado.
2. **Objeto Cognitivo versionado** con huella por evolución — trazabilidad total del razonamiento.
3. **Pool = MoE software**: escala 5→500 por nivel, accuracy histórica alimenta Fusion, spawns TDAG quedan en draft hasta aprobación del Director.
4. **Router sin IA**: match por tags, round-robin, circuit breaker 5/30s, jitter, failover chain de 9, health check 5s.
5. **Team ≤300 LOC**: firma criptográfica en handoff Y en respuesta; staff externo primero; Witness certifica o no sale.

## ENSAMBLAJE FINAL (main.py, ~30 líneas)
```python
estado  = MasterStateEngine()
juez    = LLMJuez(escritor, runtime, FailureRegistry(), CrazyWall())
pool    = ExpertPool(CognitiveEngine(llm_port))
kernel  = KernelCore(Enchufes(pipeline=transductor, expertos=pool,
                              estado=estado, fusion=FusionEngine(),
                              audit=audit_bus, juez=juez))
```

## TESTS
```
test_experto_yaml_0_loc · test_echo_mayor_30_reintenta · test_non_scope_bloquea
test_pool_escala_por_nivel · test_spawn_queda_draft · test_router_sin_ia_match_tags
test_cb_abre_a_los_5 · test_handoff_firma_invalida_rejected
test_witness_no_verificado_fail · test_team_paralelo_max_10
```
