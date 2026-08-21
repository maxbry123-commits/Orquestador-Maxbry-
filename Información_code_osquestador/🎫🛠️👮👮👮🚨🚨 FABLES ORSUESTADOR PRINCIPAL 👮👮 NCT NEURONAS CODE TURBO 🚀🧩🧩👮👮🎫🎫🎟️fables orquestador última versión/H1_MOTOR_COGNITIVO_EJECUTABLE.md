# SISTEMA H — MOTOR COGNITIVO EJECUTABLE (1/4)
# 300 expertos MoE-software — código real, listo para Claude Code
# Fuente: código de FABLES (cognitive_engine.py + expert_pool.py, sin
# modificar) + fusion_engine.py (gap resuelto por Sonnet, ver sección 3)
# Versión: 1.0 | Fecha: 2026-07-12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. QUÉ ES ESTO Y CÓMO SE ENSAMBLA (leer primero)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este es el REPO 5 (motor-cognitivo-g2) de GUÍA D, completo y
ejecutable. 3 archivos Python reales + estructura de carpetas.
NO son 300 archivos de código — son 1 motor + 300 fichas YAML
de 0 LOC cada una (ver H2_FICHAS_YAML_EJEMPLOS.md).

PRINCIPIO NO NEGOCIABLE (AX03 del ADN, ya definido en el proyecto):
El LLM es una CALCULADORA AISLADA que recibe schema, devuelve
schema. NUNCA decide arquitectura, NUNCA decide siguiente paso.
Eso lo decide el Motor (código determinista) y el sequence.json
pre-compilado por PLANNER_OFFLINE (ver H4).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ARCHIVO — `expertos/cognitive_engine.py` (~350 LOC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. ARCHIVO — `expertos/expert_pool.py` (~300 LOC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ARCHIVO — `expertos/fusion_engine.py` (~220 LOC)
   GAP RESUELTO POR SONNET: el archivo original de FABLES no
   estaba entre los documentos recibidos — solo un parche que
   lo modifica ("AÑADIR task_id en consolidar()"). Se reconstruye
   aquí completo, usando: la fórmula de consenso ponderado ya
   definida en GRUPO_H, el patrón Snapshot→proposals→Fusion→
   Commit del resumen de FABLES, y el campo task_id que pide
   el parche de alineación G2.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
"""FUSION ENGINE — consolida N respuestas de expertos en 1 Objeto
Cognitivo actualizado. Único punto de escritura real (Commit).
Los expertos SOLO proponen (proposals); nunca escriben directo al OC
— eso evita colisiones con cientos de expertos en paralelo (memoria
transaccional: Snapshot → proposals → Fusion → Commit único).
Fórmula de consenso ponderado (ya definida en GRUPO_H sección 8):
  score = accuracy_historica×0.35 + evidencia×0.30 +
          contexto×0.20 + recencia×0.15
Contract: contracts/fusion_engine.contract.json
"""
from __future__ import annotations
import json
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

from cognitive_engine import ObjetoCognitivo, RespuestaExperto

PESO_ACCURACY = 0.35
PESO_EVIDENCIA = 0.30
PESO_CONTEXTO = 0.20
PESO_RECENCIA = 0.15


@dataclass
class Contradiccion:
    path: str
    valores: list[tuple[str, Any]] = field(default_factory=list)  # (expert_id, value)
    resuelto_por: str = ""                 # expert_id ganador
    razon: str = ""


@dataclass
class ResultadoFusion:
    task_id: str
    bloque_destino: str                    # analisis|sintesis|plan|salida...
    aplicadas: int
    descartadas: int
    contradicciones: list[Contradiccion]
    duracion_ms: int = 0


class FusionEngine:
    def __init__(self, snapshot_accuracy: dict[str, float] | None = None) -> None:
        # inyectado por ExpertPool.snapshot_accuracy() antes de fusionar
        self.accuracy_historica = snapshot_accuracy or {}

    def consolidar(self, obj: ObjetoCognitivo, bloque_destino: str,
                   respuestas: list[RespuestaExperto],
                   contexto_relevancia: dict[str, float] | None = None
                   ) -> ResultadoFusion:
        t0 = time.time()
        contexto_relevancia = contexto_relevancia or {}

        # 1) DEDUP + agrupar propuestas por path (posible contradicción)
        por_path: dict[str, list[dict]] = defaultdict(list)
        for r in respuestas:
            for p in r.proposals:
                por_path[p["path"]].append({**p, "expert_id": r.expert_id})

        aplicadas, descartadas = 0, 0
        contradicciones: list[Contradiccion] = []
        datos_finales: dict = {}

        for path, props in por_path.items():
            valores_unicos = {json.dumps(p["value"], sort_keys=True, default=str)
                              for p in props}
            if len(valores_unicos) == 1:
                # sin contradicción: aplica la de mayor confidence
                mejor = max(props, key=lambda p: p["confidence"])
                datos_finales[path] = mejor["value"]
                aplicadas += 1
                continue

            # 2) CONTRADICCIÓN: resolver por score ponderado
            scored = [(p, self._score(p, contexto_relevancia)) for p in props]
            scored.sort(key=lambda t: t[1], reverse=True)
            ganador, score_ganador = scored[0]
            datos_finales[path] = ganador["value"]
            aplicadas += 1
            descartadas += len(scored) - 1
            contradicciones.append(Contradiccion(
                path=path,
                valores=[(p["expert_id"], p["value"]) for p, _ in scored],
                resuelto_por=ganador["expert_id"],
                razon=f"score={score_ganador:.3f} (accuracy+evidencia+"
                      f"contexto+recencia)"))

        # 3) COMMIT único al Objeto Cognitivo (único punto de escritura)
        obj.evolucionar(bloque_destino, datos_finales)

        return ResultadoFusion(
            task_id=obj.task_id, bloque_destino=bloque_destino,
            aplicadas=aplicadas, descartadas=descartadas,
            contradicciones=contradicciones,
            duracion_ms=int((time.time() - t0) * 1000))

    def _score(self, proposal: dict, contexto_relevancia: dict[str, float]) -> float:
        eid = proposal["expert_id"]
        accuracy = self.accuracy_historica.get(eid, 0.5)
        evidencia = min(1.0, len(proposal.get("evidencia_refs", [])) / 3)
        contexto = contexto_relevancia.get(eid, 0.5)
        # recencia: si el proposal trae timestamp, más reciente = más peso;
        # si no trae, neutral (0.5)
        recencia = proposal.get("recencia_score", 0.5)
        return (accuracy * PESO_ACCURACY + evidencia * PESO_EVIDENCIA +
                contexto * PESO_CONTEXTO + recencia * PESO_RECENCIA)
```

REGLA DE ORO DE LA FUSIÓN (por qué evita colisiones con 300
expertos en paralelo): ningún experto escribe directo al Objeto
Cognitivo. Todos escriben a `proposals` (una lista, append-only,
sin conflicto posible). El FusionEngine es el ÚNICO que llama
`obj.evolucionar()`. Esto es "memoria transaccional: Snapshot →
proposals → Fusion → Commit único" — 1000 expertos en paralelo
sin colisión porque nadie escribe directo, todos proponen.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. ESTRUCTURA DE CARPETAS (repo 5, motor-cognitivo-g2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
motor-cognitivo-g2/
├── expertos/
│   ├── cognitive_engine.py      ← sección 1 (código real FABLES)
│   ├── expert_pool.py           ← sección 2 (código real FABLES)
│   ├── fusion_engine.py         ← sección 3 (reconstruido, gap cerrado)
│   └── configs/                 ← las 300 fichas YAML (ver H2)
│       ├── E001.yaml … E100.yaml   (Capa A)
│       ├── E101.yaml … E200.yaml   (Capa B)
│       └── E201.yaml … E300.yaml   (Capa C)
├── contracts/
│   ├── cognitive_engine.contract.json
│   ├── expert_pool.contract.json
│   └── fusion_engine.contract.json
└── tests/
    ├── test_cognitive_engine.py
    ├── test_expert_pool.py
    └── test_fusion_engine.py
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIGUIENTE: H2_FICHAS_YAML_EJEMPLOS.md
(formato exacto + 15 fichas reales completas, listas para copiar)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
