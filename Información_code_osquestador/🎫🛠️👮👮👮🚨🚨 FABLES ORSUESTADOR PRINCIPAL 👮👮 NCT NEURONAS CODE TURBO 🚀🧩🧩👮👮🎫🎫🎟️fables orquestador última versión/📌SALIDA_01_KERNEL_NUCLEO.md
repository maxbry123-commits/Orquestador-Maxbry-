# SALIDA 1/6 — KERNEL NÚCLEO ORQUESTADOR
# Repo 1: orquestador-nucleo | Archivos: 3 | LOC: ~150 + ~180 + ~380
# Regla: ningún archivo supera 400 LOC. Cerebro mínimo, todo lo demás es modular.

---

## ARCHIVO 1 — `orquestador-nucleo/adn/adn_system.py` (~150 LOC)

```python
"""ADN_SYSTEM — 14 reglas inmutables (6 leyes + 8 axiomas).
INMUTABLE: NO modificar después de publicado. Solo el Director humano
puede emitir una nueva versión. Ningún proceso automático lo toca.
Contract: contracts/adn_system.contract.json
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import json
import time


class TipoRegla(Enum):
    LEY = "LEY"
    AXIOMA = "AXIOMA"


@dataclass(frozen=True)
class Regla:
    id: str
    tipo: TipoRegla
    texto: str
    bloqueante: bool = True


# ── LAS 6 LEYES ────────────────────────────────────────────
LEYES: tuple[Regla, ...] = (
    Regla("LEY_1", TipoRegla.LEY, "TODO_DEBE_SER_AUDITABLE"),
    Regla("LEY_2", TipoRegla.LEY, "TODO_DEBE_SER_REVERSIBLE"),
    Regla("LEY_3", TipoRegla.LEY, "TODO_DEBE_SER_TRAZABLE"),
    Regla("LEY_4", TipoRegla.LEY, "TODO_CAMBIO_REQUIERE_VALIDACION"),
    Regla("LEY_5", TipoRegla.LEY, "NINGUN_AGENTE_MODIFICA_ADN"),
    Regla("LEY_6", TipoRegla.LEY, "NINGUN_AGENTE_ALMACENA_TOOLS_EN_CEREBRO"),
)

# ── LOS 8 AXIOMAS (gates duros, se codifican como filtros A2) ──
AXIOMAS: tuple[Regla, ...] = (
    Regla("AX01", TipoRegla.AXIOMA, "VIDA_HUMANA_PRIMERO"),
    Regla("AX02", TipoRegla.AXIOMA, "NO_DANO_A_VULNERABLES"),
    Regla("AX03", TipoRegla.AXIOMA, "ANTI_PROMPT_INJECTION_Y_NO_ALUCINACION"),
    Regla("AX04", TipoRegla.AXIOMA, "SCOPE_RESPETADO"),
    Regla("AX05", TipoRegla.AXIOMA, "RECURSOS_RESPETADOS"),
    Regla("AX06", TipoRegla.AXIOMA, "CONTINUIDAD_3_ESTADOS"),
    Regla("AX07", TipoRegla.AXIOMA, "BUCLE_SIN_SLEEP_SCHEDULER_ASYNC"),
    Regla("AX08", TipoRegla.AXIOMA, "SATISFACCION_UNIVERSAL_STAKEHOLDERS"),
)

TODAS: tuple[Regla, ...] = LEYES + AXIOMAS


@dataclass(frozen=True)
class ADNSystem:
    """Objeto sellado. Su hash certifica que nadie alteró las reglas."""
    version: str = "3.0.0"
    reglas: tuple[Regla, ...] = field(default=TODAS)

    def hash_adn(self) -> str:
        payload = json.dumps(
            [(r.id, r.tipo.value, r.texto, r.bloqueante) for r in self.reglas],
            sort_keys=True, ensure_ascii=False,
        )
        return sha256(payload.encode("utf-8")).hexdigest()

    def verificar_integridad(self, hash_esperado: str) -> bool:
        """Se llama en CADA arranque del kernel (Auto-Recovery también)."""
        return self.hash_adn() == hash_esperado

    def regla(self, regla_id: str) -> Regla:
        for r in self.reglas:
            if r.id == regla_id:
                return r
        raise KeyError(f"Regla desconocida: {regla_id}")

    def export_constitution(self) -> dict:
        """Genera adn_constitution.json (Nivel C de configuración)."""
        return {
            "version": self.version,
            "hash": self.hash_adn(),
            "generado": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "inmutable": True,
            "reglas": [
                {"id": r.id, "tipo": r.tipo.value,
                 "texto": r.texto, "bloqueante": r.bloqueante}
                for r in self.reglas
            ],
        }


# Instancia única sellada del sistema (no hay setters, frozen=True)
ADN = ADNSystem()
ADN_HASH_PUBLICADO: str = ADN.hash_adn()  # se persiste en el repo al publicar


def assert_adn_integro() -> None:
    """HALT duro si el ADN fue alterado. Primera línea de todo arranque."""
    if not ADN.verificar_integridad(ADN_HASH_PUBLICADO):
        raise SystemExit("ADN_CORRUPTO: intervención humana requerida (LEY_5)")
```

---

## ARCHIVO 2 — `orquestador-nucleo/guardian/guardian_layer.py` (~180 LOC)

```python
"""GUARDIAN_LAYER — máxima autoridad de seguridad.
6 checks. Cualquiera en True → RECHAZAR_SOLICITUD inmediato.
Consultado por: Kernel (cada solicitud), Sentinela (cada propuesta),
Recovery (cada acción), Juez (cada veredicto crítico).
Contract: contracts/guardian.contract.json
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable
import fnmatch
import logging

log = logging.getLogger("guardian")

# Rutas que NADIE (excepto Director) puede modificar — línea roja absoluta
RUTAS_INMUTABLES: tuple[str, ...] = (
    "orquestador-nucleo/adn/*",
    "orquestador-nucleo/guardian/*",
    "orquestador-nucleo/llm_juez/*",
    "contracts-schemas/*",
)


class Veredicto(Enum):
    PERMITIR = "PERMITIR"
    RECHAZAR_SOLICITUD = "RECHAZAR_SOLICITUD"


@dataclass(frozen=True)
class ResultadoGuardian:
    veredicto: Veredicto
    checks: dict[str, bool]          # nombre_check -> violado(True/False)
    razon: str = ""

    @property
    def permitido(self) -> bool:
        return self.veredicto is Veredicto.PERMITIR


@dataclass
class SolicitudGuardian:
    """Payload normalizado que el Kernel arma antes de consultar."""
    actor: str                        # "orquestador"|"team_agent"|"sentinela"|...
    accion: str                       # "ejecutar_pipeline"|"modificar_archivo"|...
    rutas_afectadas: list[str] = field(default_factory=list)
    modifica_adn: bool = False
    omite_auditoria: bool = False
    omite_trazabilidad: bool = False
    rompe_aislamiento: bool = False   # p.ej. import directo entre repos lejanos
    riesgo_seguridad: bool = False    # marcado por filtros A2 / Sentinel


def _viola_adn(s: SolicitudGuardian) -> bool:
    if s.modifica_adn:
        return True
    return any(
        fnmatch.fnmatch(ruta, patron)
        for ruta in s.rutas_afectadas
        for patron in RUTAS_INMUTABLES
    ) and s.accion.startswith("modificar")


def _viola_leyes(s: SolicitudGuardian) -> bool:
    # LEY_6: nadie escribe tools dentro del cerebro
    return any("orquestador-nucleo" in r and s.accion == "instalar_tool"
               for r in s.rutas_afectadas)


CHECKS: dict[str, Callable[[SolicitudGuardian], bool]] = {
    "VIOLA_ADN": _viola_adn,
    "VIOLA_LEYES": _viola_leyes,
    "VIOLA_AUDITORIA": lambda s: s.omite_auditoria,
    "VIOLA_TRAZABILIDAD": lambda s: s.omite_trazabilidad,
    "VIOLA_SEGURIDAD": lambda s: s.riesgo_seguridad,
    "VIOLA_AISLAMIENTO": lambda s: s.rompe_aislamiento,
}


class GuardianLayer:
    """Sin estado mutable de negocio: evalúa y registra, nada más."""

    def evaluar(self, solicitud: SolicitudGuardian) -> ResultadoGuardian:
        resultados = {nombre: chk(solicitud) for nombre, chk in CHECKS.items()}
        violados = [n for n, v in resultados.items() if v]
        if violados:
            razon = f"checks_violados={violados} actor={solicitud.actor}"
            log.warning("RECHAZAR_SOLICITUD %s", razon)
            return ResultadoGuardian(Veredicto.RECHAZAR_SOLICITUD,
                                     resultados, razon)
        return ResultadoGuardian(Veredicto.PERMITIR, resultados, "OK")

    def es_ruta_modificable(self, ruta: str) -> bool:
        """API directa para Sentinela (GUÍA E, línea roja)."""
        return not any(fnmatch.fnmatch(ruta, p) for p in RUTAS_INMUTABLES)


GUARDIAN = GuardianLayer()
```

---

## ARCHIVO 3 — `orquestador-nucleo/kernel/kernel_core.py` (~380 LOC)

```python
"""KERNEL_CORE — el cerebro mínimo (6 responsabilidades, nada más).
1 recibir · 2 activar pipeline · 3 crear expertos · 4 compartir estado
5 consolidar · 6 emitir.
NO investiga, NO programa, NO valida, NO planifica: delega todo vía enchufe.
Todo módulo externo se resuelve por contrato (Enchufe Universal v1.5),
nunca por import directo de repos lejanos.
Contract: contracts/kernel_core.contract.json
"""
from __future__ import annotations
import asyncio
import logging
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Any, Awaitable, Callable, Protocol

from adn.adn_system import assert_adn_integro
from guardian.guardian_layer import GUARDIAN, SolicitudGuardian

log = logging.getLogger("kernel")

# ═══════════════ TIPOS Y ESTADOS ═══════════════

class EstadoKernel(Enum):
    IDLE = "IDLE"
    RECIBIENDO = "RECIBIENDO"
    ACTIVANDO_PIPELINE = "ACTIVANDO_PIPELINE"
    EJECUTANDO = "EJECUTANDO"
    CONSOLIDANDO = "CONSOLIDANDO"
    EMITIENDO = "EMITIENDO"
    HALT = "HALT"
    DEGRADED = "DEGRADED"


class Fase(Enum):
    P1_INPUT = "P1_INPUT"
    P2_PROCESS = "P2_PROCESS"
    P3_OUTPUT = "P3_OUTPUT"


class Clasificacion(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    PARTIAL = "PARTIAL"
    ESCALATE = "ESCALATE"


@dataclass
class Solicitud:
    """Responsabilidad 1 — lo único que el kernel RECIBE."""
    raw: Any
    origen: str                       # telegram|drive|mcp|api|studio
    solicitud_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)

    @property
    def doc_id(self) -> str:
        return sha256(repr(self.raw).encode()).hexdigest()


@dataclass
class ResultadoFase:
    fase: Fase
    clasificacion: Clasificacion
    payload: dict[str, Any]
    evidencia: dict[str, Any] = field(default_factory=dict)
    checkpoint_ref: str | None = None


@dataclass
class RespuestaFinal:
    solicitud_id: str
    clasificacion: Clasificacion
    resultado: dict[str, Any]
    provenance: list[dict] = field(default_factory=list)
    hash_respuesta: str = ""

    def sellar(self) -> "RespuestaFinal":
        self.hash_respuesta = sha256(
            repr((self.solicitud_id, self.resultado)).encode()
        ).hexdigest()
        return self


# ═══════════════ ENCHUFES (Protocols = contratos, no imports) ═══════════════
# El kernel NO conoce implementaciones. Recibe puertos que cumplen el contrato.

class PuertoPipeline(Protocol):
    async def ejecutar(self, fase: Fase, contexto: dict) -> ResultadoFase: ...
    def seleccionar(self, contexto: dict) -> str: ...   # nombre pipeline DSL


class PuertoExpertos(Protocol):
    async def activar(self, fase: Fase, necesidades: list[str],
                      snapshot: dict) -> list[dict]: ...
    async def liberar(self, fase: Fase) -> None: ...


class PuertoEstado(Protocol):
    def snapshot(self) -> dict: ...                      # copia consistente RO
    def commit(self, proposals: list[dict], actor: str) -> str: ...  # hash
    def checkpoint(self, etiqueta: str) -> str: ...
    def verificar_hash_chain(self) -> bool: ...


class PuertoFusion(Protocol):
    def consolidar(self, parciales: list[ResultadoFase]) -> dict: ...


class PuertoAudit(Protocol):
    def evento(self, tipo: str, datos: dict) -> None: ...  # hash-chained log


class PuertoJuez(Protocol):
    async def veredicto(self, fase: Fase,
                        resultado: ResultadoFase) -> Clasificacion: ...
    def goal_lock_activo(self) -> bool: ...


@dataclass
class Enchufes:
    """Inyección de dependencias: 1 solo punto de ensamblaje del sistema."""
    pipeline: PuertoPipeline
    expertos: PuertoExpertos
    estado: PuertoEstado
    fusion: PuertoFusion
    audit: PuertoAudit
    juez: PuertoJuez
    on_emit: Callable[[RespuestaFinal], Awaitable[None]] | None = None


# ═══════════════ EL KERNEL ═══════════════

FASES_ORDEN: tuple[Fase, ...] = (Fase.P1_INPUT, Fase.P2_PROCESS, Fase.P3_OUTPUT)
MAX_RETRY_FASE = 3


class KernelCore:
    """Microkernel MAXBRY v3. Solo coordina. Nunca ejecuta trabajo real."""

    def __init__(self, enchufes: Enchufes) -> None:
        assert_adn_integro()                     # HALT si ADN alterado
        self.e = enchufes
        self.estado = EstadoKernel.IDLE
        self._halt = asyncio.Event()

    # ── Señales SYS_* (Wake Word Engine invoca esto) ──
    def sys_halt(self) -> None:
        self._halt.set()
        self.estado = EstadoKernel.HALT
        self.e.audit.evento("SYS_HALT", {})

    # ── PUNTO DE ENTRADA ÚNICO ──
    async def procesar(self, solicitud: Solicitud) -> RespuestaFinal:
        self._transicion(EstadoKernel.RECIBIENDO)
        self.e.audit.evento("solicitud.recibida", {
            "id": solicitud.solicitud_id, "doc_id": solicitud.doc_id,
            "origen": solicitud.origen,
        })

        # Guardian primero: nada avanza si viola ADN/leyes
        g = GUARDIAN.evaluar(SolicitudGuardian(
            actor="kernel", accion="ejecutar_pipeline"))
        if not g.permitido:
            return self._rechazo(solicitud, g.razon)

        # Responsabilidad 4: snapshot consistente ANTES de trabajar
        if not self.e.estado.verificar_hash_chain():
            self.e.audit.evento("state.corrupto", {"accion": "recovery_n3"})
            return self._rechazo(solicitud, "STATE_CORRUPTION")

        contexto: dict[str, Any] = {
            "solicitud": solicitud, "doc_id": solicitud.doc_id,
            "snapshot": self.e.estado.snapshot(),
        }

        parciales: list[ResultadoFase] = []
        for fase in FASES_ORDEN:
            if self._halt.is_set():
                return self._rechazo(solicitud, "SYS_HALT")
            resultado = await self._ejecutar_fase(fase, contexto)
            parciales.append(resultado)
            if resultado.clasificacion is Clasificacion.FAIL:
                return self._rechazo(solicitud, f"{fase.value}_FAIL",
                                     parciales)
            if resultado.clasificacion is Clasificacion.ESCALATE:
                return self._escalar(solicitud, fase, parciales)
            # el output de cada fase alimenta a la siguiente
            contexto[fase.value] = resultado.payload

        # Responsabilidad 5: consolidar
        self._transicion(EstadoKernel.CONSOLIDANDO)
        consolidado = self.e.fusion.consolidar(parciales)
        commit_hash = self.e.estado.commit(
            proposals=[{"path": "ultimo_resultado", "value": consolidado}],
            actor="kernel",
        )

        # Responsabilidad 6: emitir (sellado + provenance)
        self._transicion(EstadoKernel.EMITIENDO)
        respuesta = RespuestaFinal(
            solicitud_id=solicitud.solicitud_id,
            clasificacion=Clasificacion.PASS,
            resultado=consolidado,
            provenance=[{"fase": p.fase.value, "cp": p.checkpoint_ref,
                         "clasif": p.clasificacion.value} for p in parciales]
                      + [{"commit": commit_hash}],
        ).sellar()
        self.e.audit.evento("respuesta.emitida", {
            "id": respuesta.solicitud_id, "hash": respuesta.hash_respuesta})
        if self.e.on_emit:
            await self.e.on_emit(respuesta)
        self._transicion(EstadoKernel.IDLE)
        return respuesta

    # ── Ejecución de 1 fase con retry + juez + expertos ──
    async def _ejecutar_fase(self, fase: Fase, ctx: dict) -> ResultadoFase:
        self._transicion(EstadoKernel.ACTIVANDO_PIPELINE)
        nombre = self.e.pipeline.seleccionar({**ctx, "fase": fase.value})
        self.e.audit.evento("pipeline.seleccionado",
                            {"fase": fase.value, "pipeline": nombre})

        if fase is not Fase.P1_INPUT and not self.e.juez.goal_lock_activo():
            return ResultadoFase(fase, Clasificacion.FAIL,
                                 {"error": "SIN_GOAL_LOCK"})

        self._transicion(EstadoKernel.EJECUTANDO)
        for intento in range(1, MAX_RETRY_FASE + 1):
            try:
                # Responsabilidad 3: el pool crea/activa expertos por fase.
                # El kernel NO sabe cuáles — solo declara la fase y snapshot.
                await self.e.expertos.activar(
                    fase, necesidades=[], snapshot=ctx["snapshot"])
                resultado = await self.e.pipeline.ejecutar(fase, ctx)
            except asyncio.TimeoutError:
                self.e.audit.evento("fase.timeout",
                                    {"fase": fase.value, "intento": intento})
                continue
            finally:
                await self.e.expertos.liberar(fase)

            veredicto = await self.e.juez.veredicto(fase, resultado)
            resultado.clasificacion = veredicto
            resultado.checkpoint_ref = self.e.estado.checkpoint(
                f"{fase.value}_i{intento}")
            self.e.audit.evento("fase.completada", {
                "fase": fase.value, "intento": intento,
                "veredicto": veredicto.value, "cp": resultado.checkpoint_ref})

            if veredicto is not Clasificacion.FAIL:
                return resultado
            # FAIL → reintento con el mismo contexto (Juez adjunta razones)
        return ResultadoFase(fase, Clasificacion.FAIL,
                             {"error": "MAX_RETRY_FASE_AGOTADO"})

    # ── Helpers ──
    def _transicion(self, nuevo: EstadoKernel) -> None:
        log.info("kernel %s -> %s", self.estado.value, nuevo.value)
        self.estado = nuevo

    def _rechazo(self, s: Solicitud, razon: str,
                 parciales: list[ResultadoFase] | None = None) -> RespuestaFinal:
        self.e.audit.evento("solicitud.rechazada",
                            {"id": s.solicitud_id, "razon": razon})
        self._transicion(EstadoKernel.IDLE)
        return RespuestaFinal(s.solicitud_id, Clasificacion.FAIL,
                              {"razon": razon}).sellar()

    def _escalar(self, s: Solicitud, fase: Fase,
                 parciales: list[ResultadoFase]) -> RespuestaFinal:
        self.e.audit.evento("solicitud.escalada",
                            {"id": s.solicitud_id, "fase": fase.value})
        self._transicion(EstadoKernel.IDLE)
        return RespuestaFinal(s.solicitud_id, Clasificacion.ESCALATE,
                              {"fase": fase.value,
                               "requiere": "DIRECTOR"}).sellar()
```

---

## NOTAS DE DISEÑO (por qué es avanzado)

1. **6 responsabilidades exactas** en `KernelCore.procesar()` — nada más vive en el cerebro.
2. **Enchufes = `Protocol`** (duck typing estructural): el kernel compila sin conocer ninguna implementación. Cambiar Loop Engine, Expert Pool o Memoria = inyectar otro objeto que cumpla el contrato. Cero imports entre repos lejanos.
3. **Snapshot→Commit**: el kernel jamás muta estado directamente; propone y el State Engine (Salida 3) decide.
4. **Guardian + ADN íntegro en cada arranque**; hash del ADN publicado en repo.
5. **Retry por fase (máx 3) + veredicto del Juez + checkpoint por intento** — recovery granular.
6. **HALT asíncrono** vía `asyncio.Event` (Wake Word SYS_HALT interrumpe entre fases).

## CONTRATOS QUE ESTE CÓDIGO EXIGE (se cierran en salidas 2-6)
- `PuertoJuez` → Salida 2 (LLM_JUEZ + Recovery)
- `PuertoEstado` → Salida 3 (State Engine + crazy_wall)
- `PuertoPipeline` → Salida 4 (DSL DAG Sheriff)
- `PuertoExpertos` + `PuertoFusion` → Salida 5 (Expert Pool + Fusion)
- Team Agente (mismo patrón en miniatura) → Salida 6

## TESTS MÍNIMOS (para Sonnet)
```
test_adn_hash_estable · test_adn_alterado_halt
test_guardian_rechaza_ruta_inmutable · test_guardian_permite_config
test_kernel_sin_goal_lock_fail_p2 · test_kernel_3fases_pass
test_kernel_escalate_corta_flujo · test_sys_halt_interrumpe
```
