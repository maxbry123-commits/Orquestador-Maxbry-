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
