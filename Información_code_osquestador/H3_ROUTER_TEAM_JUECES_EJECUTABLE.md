# SISTEMA H — ROUTER + TEAM AGENT + SISTEMA DE JUECES (3/4)
# Router y Team: código real de FABLES, sin modificar
# Sistema de Jueces 3 niveles: GAP resuelto por Sonnet (código
# nuevo — GRUPO_H solo lo tenía conceptual, nunca en Python real)
# Versión: 1.0 | Fecha: 2026-07-12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ARCHIVO — `router/router_core.py` (~280 LOC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
"""ROUTER — dispatcher determinista SIN IA. Match por tags y
capability. Ciego al provider: los expertos piden 'necesito X', el
router resuelve quién. Pools por runtime_type + circuit breaker +
failover chain. Contract: contracts/router.contract.json
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. ARCHIVO — `team-agente/team_core.py` (~300 LOC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ARCHIVO — `expertos/sistema_jueces.py` (~250 LOC)
   GAP RESUELTO POR SONNET: GRUPO_H definía el Sistema de Jueces
   3 niveles solo conceptualmente (sección 9). Nunca existió en
   código Python real en ningún documento de FABLES recibido.
   Se construye aquí, usando el FusionEngine (H1) y el patrón
   de fichas-juez ya definidas en H2 (E189, E240, E296).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
"""SISTEMA DE JUECES — 3 niveles, jerarquía de autoridad creciente.
NIVEL 1 Local: ¿este enjambre cumplió su objetivo puntual?
NIVEL 2 Capa: resuelve lo que el Local no pudo (conflictos entre
              expertos de la misma capa).
NIVEL 3 Central (E296): única autoridad sobre checkpoints y status
              global — ES el mismo LLM_JUEZ de GRUPO_F operando
              en su rol de cierre (P13 SESSION_CLOSE).
Ningún nivel se salta: Local→Capa→Central, cada uno solo escala
si el nivel inferior no resuelve con confianza suficiente.
Contract: contracts/sistema_jueces.contract.json
"""
from __future__ import annotations
import time
from dataclasses import dataclass, field
from enum import Enum

from cognitive_engine import CognitiveEngine, ConfigExperto, ObjetoCognitivo


class Veredicto(Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    RETRY = "RETRY"


@dataclass
class ResultadoJuicio:
    nivel: str                    # "local" | "capa" | "central"
    veredicto: Veredicto
    razon: str
    escalado_a: str | None = None  # siguiente nivel si no resolvió
    duracion_ms: int = 0


UMBRAL_CONFIANZA_LOCAL = 0.70    # bajo esto, escala a Capa
UMBRAL_CONFIANZA_CAPA = 0.60     # bajo esto, escala a Central


class SistemaJueces:
    def __init__(self, engine: CognitiveEngine,
                 juez_local_cfg: ConfigExperto,
                 juez_capa_cfgs: dict[str, ConfigExperto],  # {"B1":E189,...}
                 juez_central_cfg: ConfigExperto) -> None:  # E296
        self.engine = engine
        self.juez_local = juez_local_cfg
        self.jueces_capa = juez_capa_cfgs
        self.juez_central = juez_central_cfg

    async def juzgar_enjambre(self, obj: ObjetoCognitivo,
                              resultado_enjambre: dict,
                              capa: str) -> ResultadoJuicio:
        """Entrada del flujo: SIEMPRE empieza en NIVEL 1 Local."""
        t0 = time.time()
        r_local = await self.engine.ejecutar(
            self.juez_local, obj, resultado_enjambre)
        confianza = self._extraer_confianza(r_local)
        veredicto = self._extraer_veredicto(r_local)

        if confianza >= UMBRAL_CONFIANZA_LOCAL:
            return ResultadoJuicio(
                nivel="local", veredicto=veredicto,
                razon=f"resuelto en Local, confianza={confianza:.2f}",
                duracion_ms=int((time.time() - t0) * 1000))

        # NIVEL 2: escala a Juez de Capa (solo si Local no logró confianza)
        return await self._juzgar_capa(obj, resultado_enjambre, capa, t0)

    async def _juzgar_capa(self, obj: ObjetoCognitivo, resultado: dict,
                           capa: str, t0: float) -> ResultadoJuicio:
        cfg_capa = self.jueces_capa.get(capa)
        if cfg_capa is None:
            # sin juez de capa configurado → escala directo a Central
            return await self._juzgar_central(obj, resultado, t0,
                                               escalado_desde="capa_ausente")

        r_capa = await self.engine.ejecutar(cfg_capa, obj, resultado)
        confianza = self._extraer_confianza(r_capa)
        veredicto = self._extraer_veredicto(r_capa)

        if confianza >= UMBRAL_CONFIANZA_CAPA:
            return ResultadoJuicio(
                nivel="capa", veredicto=veredicto,
                razon=f"resuelto en Capa({capa}), confianza={confianza:.2f}",
                duracion_ms=int((time.time() - t0) * 1000))

        # NIVEL 3: escala a Juez Central (E296, máxima autoridad)
        return await self._juzgar_central(obj, resultado, t0,
                                          escalado_desde=f"capa_{capa}")

    async def _juzgar_central(self, obj: ObjetoCognitivo, resultado: dict,
                              t0: float, escalado_desde: str
                              ) -> ResultadoJuicio:
        """E296 CentralJudge_Final — equivale a P13 SESSION_CLOSE
        del pipeline JUEZ de GRUPO_F. Máxima autoridad, sin escalar más."""
        r_central = await self.engine.ejecutar(
            self.juez_central, obj, resultado)
        veredicto = self._extraer_veredicto(r_central)
        return ResultadoJuicio(
            nivel="central", veredicto=veredicto,
            razon=f"decisión final E296, escalado_desde={escalado_desde}",
            escalado_a=None,
            duracion_ms=int((time.time() - t0) * 1000))

    @staticmethod
    def _extraer_confianza(r) -> float:
        if not r.proposals:
            return 0.0
        return max(p.get("confidence", 0.0) for p in r.proposals)

    @staticmethod
    def _extraer_veredicto(r) -> Veredicto:
        for p in r.proposals:
            v = p.get("value", {})
            if isinstance(v, dict) and "veredicto" in v:
                try:
                    return Veredicto(v["veredicto"])
                except ValueError:
                    pass
            if isinstance(v, dict) and "status" in v:
                mapa = {"COMMITTED": Veredicto.APPROVED,
                       "REJECTED": Veredicto.REJECTED,
                       "RETRY_CAPA_B": Veredicto.RETRY}
                if v["status"] in mapa:
                    return mapa[v["status"]]
        return Veredicto.RETRY   # default seguro: nunca aprobar por defecto
```

REGLA DE ESCALADO (por qué nunca se salta un nivel): un juez de
nivel inferior con BAJA confianza no es "está mal" — es "no sé
con certeza". El sistema nunca fuerza una decisión de baja
confianza; escala a quien tiene más contexto/autoridad. El default
de `_extraer_veredicto` es siempre `RETRY`, nunca `APPROVED` — el
sistema nunca aprueba por ausencia de evidencia (mismo principio
que RA-01 de GRUPO_F: "Nunca acepta evidencia verbal").

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIGUIENTE: H4_ENSAMBLAJE_FINAL_Y_TESTS.md
(sequence.json real, estructura final, instrucciones Claude Code)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
