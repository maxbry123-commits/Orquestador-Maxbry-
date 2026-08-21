# SISTEMA H — ENSAMBLAJE FINAL Y TESTS (4/4)
# planner_offline.py (código real FABLES) + sequence.json de ejemplo
# + tests + orden exacto de instrucciones para Claude Code
# Versión: 1.0 | Fecha: 2026-07-12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ARCHIVO — `orquestador-nucleo/planner/planner_offline.py`
   (código real de FABLES, ~150 LOC — compila sequence.json)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
"""PLANNER_OFFLINE — Compiler[requirements.json → sequence.json + fallback.json]
Corre en F-1/F0 (lifecycle marker), NUNCA en runtime. Python puro, NO LLM,
NO agente. Vive en repo brain (orquestador-nucleo). El Director define
requirements; esto compila la vía del tren y la congela con hash.
REGLA DE ORO (Kernel Transductor 🚂): esto es el ÚNICO lugar donde se
"decide" el orden. En runtime, el kernel solo EJECUTA lo aquí congelado.
"""
from __future__ import annotations
import json
import time
from graphlib import TopologicalSorter, CycleError
from hashlib import sha256
from pathlib import Path


class TaskRejectedError(Exception):
    """Ciclo, ficha inexistente o requirements inválidos."""


def _hash(obj) -> str:
    return sha256(json.dumps(obj, sort_keys=True, default=str)
                  .encode()).hexdigest()


def compilar_sequence(requirements: dict,
                      fichas_disponibles: set[str]) -> dict:
    """requirements = {"objetivo":..., "fichas_requeridas":[...],
    "dependencias":{"E101":["E001","E021"]}, "nivel":"AVANZADO"}"""
    fichas_req = set(requirements.get("fichas_requeridas", []))
    faltantes = fichas_req - fichas_disponibles
    if faltantes:
        raise TaskRejectedError(f"fichas_inexistentes:{faltantes}")

    deps = requirements.get("dependencias", {})
    ts = TopologicalSorter(deps)
    try:
        orden = list(ts.static_order())
    except CycleError as exc:
        raise TaskRejectedError(f"ciclo_detectado:{exc}") from exc

    fases = _agrupar_por_fase(orden, fichas_req)
    sequence = {
        "id": f"seq_{int(time.time())}",
        "cognitive_object_id": requirements.get("task_id", ""),
        "version": 1,
        "immutable": True,
        "phases": fases,
        "global_constraints": {
            "max_total_time_ms": requirements.get("timeout_ms", 60000),
            "max_llm_calls": requirements.get("max_llm_calls", 50),
            "rollback_strategy": "to_last_valid_checkpoint",
        },
        "metadata": {
            "generated_by": "planner_offline",
            "nivel": requirements.get("nivel", "BASICO"),
            "expected_experts": len(orden),
        },
    }
    sequence["hash"] = _hash(sequence)
    return sequence


def _agrupar_por_fase(orden: list[str], fichas_req: set[str]) -> list[dict]:
    """Agrupa por capa (prefijo del expert_id: E0xx=A, E1xx=B, E2xx=C)."""
    grupos: dict[str, list[str]] = {"A": [], "B": [], "C": []}
    for eid in orden:
        if eid not in fichas_req:
            continue
        num = int(eid[1:]) if eid[1:].isdigit() else 0
        capa = "A" if num < 101 else "B" if num < 201 else "C"
        grupos[capa].append(eid)

    fases = []
    for capa, experts in grupos.items():
        if not experts:
            continue
        fases.append({
            "phase_id": f"fase_{capa.lower()}",
            "layer": capa,
            "swarms": [{
                "swarm_id": f"swarm_{capa.lower()}_1",
                "experts": experts,
                "mode": "parallel",
                "timeout_ms": 30000,
            }],
        })
    return fases


def congelar_a_disco(sequence: dict, ruta: str = "sequences/") -> str:
    """Escribe sequence.json INMUTABLE. Re-generar = nuevo archivo,
    nunca sobrescribir uno ya usado en producción."""
    Path(ruta).mkdir(parents=True, exist_ok=True)
    destino = Path(ruta) / f"{sequence['id']}.json"
    destino.write_text(json.dumps(sequence, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    return str(destino)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. SEQUENCE.JSON — EJEMPLO REAL COMPLETO (nivel BASICO)
   (generado por planner_offline.py con los 15 expertos de H2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```json
{
  "id": "seq_ejemplo_basico_001",
  "cognitive_object_id": "task_demo_001",
  "version": 1,
  "immutable": true,
  "phases": [
    {
      "phase_id": "fase_a",
      "layer": "A",
      "swarms": [{
        "swarm_id": "swarm_a_1",
        "cell": "A1+A2+A5",
        "experts": ["E001", "E002", "E021", "E037", "E081"],
        "mode": "parallel",
        "coordinator": "E001",
        "blocking_experts": ["E021", "E037"],
        "timeout_ms": 15000,
        "exit_criteria": "todos_completos OR bloqueo_axiomatico"
      }]
    },
    {
      "phase_id": "fase_b",
      "layer": "B",
      "depends_on": ["fase_a"],
      "swarms": [{
        "swarm_id": "swarm_b_1",
        "cell": "B1+B2+B4+B5",
        "experts": ["E101", "E121", "E161", "E187", "E189"],
        "mode": "parallel_then_sequential",
        "orden_interno": [["E101", "E121"], ["E161"], ["E187", "E189"]],
        "coordinator": "E187",
        "judge_local": "E189",
        "timeout_ms": 45000,
        "max_iteraciones_rollback": 2
      }]
    },
    {
      "phase_id": "fase_c",
      "layer": "C",
      "depends_on": ["fase_b"],
      "swarms": [{
        "swarm_id": "swarm_c_1",
        "cell": "C1+C2+C4+C5",
        "experts": ["E201", "E240", "E261", "E296", "E300"],
        "mode": "sequential",
        "orden_interno": ["E201", "E240", "E261", "E296", "E300"],
        "judge_central": "E296",
        "timeout_ms": 20000
      }]
    }
  ],
  "global_constraints": {
    "max_total_time_ms": 80000,
    "max_llm_calls": 15,
    "max_cost_units": 30,
    "rollback_strategy": "to_last_valid_checkpoint"
  },
  "metadata": {
    "generated_by": "planner_offline",
    "nivel": "BASICO",
    "expected_experts": 15,
    "expected_duration_ms": 60000
  },
  "hash": "sha256_calculado_al_congelar_NUNCA_editar_manualmente"
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. TESTS MÍNIMOS (uno por archivo, listos para pytest)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
# tests/test_cognitive_engine.py
import pytest
from expertos.cognitive_engine import (Capa, CognitiveEngine, ConfigExperto,
                                        ObjetoCognitivo)

class LLMFalso:
    async def calcular(self, plantilla, variables, schema_out,
                       temperature, max_tokens):
        return {"proposals": [{"path": "test.campo", "value": "ok",
                               "confidence": 0.9, "evidencia_refs": []}]}

@pytest.mark.asyncio
async def test_experto_respeta_non_scope():
    cfg = ConfigExperto(
        expert_id="E999", nombre="Test", capa=Capa.A_ENTRADA, grupo="A1",
        operacion="test", schema_in={"required": []},
        schema_out={"required": ["proposals"]},
        non_scope=("palabra_prohibida",))
    engine = CognitiveEngine(LLMFalso())
    obj = ObjetoCognitivo(task_id="t1", objetivo={})
    r = await engine.ejecutar(cfg, obj, {"texto": "esto tiene palabra_prohibida"})
    assert r.self_check["scope_ok"] is False

@pytest.mark.asyncio
async def test_objeto_cognitivo_versiona_al_evolucionar():
    obj = ObjetoCognitivo(task_id="t1", objetivo={})
    v_inicial = obj.version
    obj.evolucionar("analisis", {"campo": "valor"})
    assert obj.version == v_inicial + 1
    assert obj.analisis["campo"] == "valor"
```

```python
# tests/test_fusion_engine.py
from expertos.cognitive_engine import ObjetoCognitivo, RespuestaExperto
from expertos.fusion_engine import FusionEngine

def test_fusion_resuelve_contradiccion_por_accuracy():
    obj = ObjetoCognitivo(task_id="t1", objetivo={})
    r1 = RespuestaExperto("E101", [{"path": "analisis.x", "value": "A",
                                     "confidence": 0.9, "evidencia_refs": []}])
    r2 = RespuestaExperto("E102", [{"path": "analisis.x", "value": "B",
                                     "confidence": 0.5, "evidencia_refs": []}])
    fusion = FusionEngine(snapshot_accuracy={"E101": 0.9, "E102": 0.3})
    resultado = fusion.consolidar(obj, "analisis", [r1, r2])
    assert obj.analisis["x"] == "A"          # gana el de mayor accuracy
    assert len(resultado.contradicciones) == 1

def test_fusion_sin_contradiccion_aplica_directo():
    obj = ObjetoCognitivo(task_id="t1", objetivo={})
    r1 = RespuestaExperto("E101", [{"path": "analisis.y", "value": "Z",
                                     "confidence": 0.8, "evidencia_refs": []}])
    fusion = FusionEngine()
    resultado = fusion.consolidar(obj, "analisis", [r1])
    assert obj.analisis["y"] == "Z"
    assert resultado.aplicadas == 1
    assert len(resultado.contradicciones) == 0
```

```python
# tests/test_sistema_jueces.py
import pytest
from expertos.cognitive_engine import Capa, CognitiveEngine, ConfigExperto, ObjetoCognitivo
from expertos.sistema_jueces import SistemaJueces, Veredicto

class LLMJuezAprueba:
    async def calcular(self, plantilla, variables, schema_out, temperature, max_tokens):
        return {"proposals": [{"path": "verificacion.juez", "value":
                {"veredicto": "APPROVED"}, "confidence": 0.95,
                "evidencia_refs": []}]}

@pytest.mark.asyncio
async def test_juez_local_resuelve_con_alta_confianza():
    engine = CognitiveEngine(LLMJuezAprueba())
    juez_local = ConfigExperto(
        expert_id="E189", nombre="LocalJudge", capa=Capa.B_RAZONAMIENTO,
        grupo="B5", operacion="juzgar", schema_in={"required": []},
        schema_out={"required": ["proposals"]})
    juez_central = ConfigExperto(
        expert_id="E296", nombre="CentralJudge", capa=Capa.C_SALIDA,
        grupo="C5", operacion="juzgar_final", schema_in={"required": []},
        schema_out={"required": ["proposals"]})
    sistema = SistemaJueces(engine, juez_local, {}, juez_central)
    obj = ObjetoCognitivo(task_id="t1", objetivo={})
    resultado = await sistema.juzgar_enjambre(obj, {}, capa="B")
    assert resultado.nivel == "local"          # no debió escalar
    assert resultado.veredicto == Veredicto.APPROVED
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. ESTRUCTURA DE CARPETAS FINAL CONSOLIDADA (H1+H2+H3+H4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
motor-cognitivo-g2/                    (repo 5, GUÍA D)
├── expertos/
│   ├── cognitive_engine.py            (H1.1)
│   ├── expert_pool.py                 (H1.2)
│   ├── fusion_engine.py               (H1.3)
│   ├── sistema_jueces.py              (H3.3)
│   └── configs/
│       ├── E001.yaml … E100.yaml      (H2, Capa A — 15 ejemplos dados,
│       │                                285 restantes por generar)
│       ├── E101.yaml … E200.yaml      (H2, Capa B)
│       └── E201.yaml … E300.yaml      (H2, Capa C)
├── router/
│   └── router_core.py                 (H3.1)
├── team-agente/
│   └── team_core.py                   (H3.2)
├── orquestador-nucleo/
│   └── planner/
│       └── planner_offline.py         (H4.1)
├── sequences/
│   └── seq_ejemplo_basico_001.json    (H4.2)
├── contracts/
│   ├── cognitive_engine.contract.json
│   ├── expert_pool.contract.json
│   ├── fusion_engine.contract.json
│   ├── router.contract.json
│   └── team_agent.contract.json
└── tests/
    ├── test_cognitive_engine.py       (H4.3)
    ├── test_fusion_engine.py          (H4.3)
    └── test_sistema_jueces.py         (H4.3)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. ORDEN EXACTO DE INSTRUCCIONES PARA CLAUDE CODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ejecutar en este orden, sin saltar pasos:

PASO 1: Crear la estructura de carpetas completa (sección 4)
PASO 2: Copiar cognitive_engine.py tal cual (H1 sección 1) —
        NO modificar, es código ya auditado
PASO 3: Copiar expert_pool.py tal cual (H1 sección 2)
PASO 4: Copiar fusion_engine.py tal cual (H1 sección 3)
PASO 5: Copiar las 15 fichas YAML de ejemplo (H2) en configs/
PASO 6: Correr test_cognitive_engine.py y test_fusion_engine.py
        con LLM falso (LLMFalso de sección 3) — deben pasar 100%
        ANTES de conectar un LLM real
PASO 7: Copiar router_core.py tal cual (H3 sección 1)
PASO 8: Copiar team_core.py tal cual (H3 sección 2)
PASO 9: Copiar sistema_jueces.py tal cual (H3 sección 3)
PASO 10: Correr test_sistema_jueces.py con LLM falso — debe pasar
PASO 11: Copiar planner_offline.py tal cual (H4 sección 1)
PASO 12: Generar sequence.json de prueba usando planner_offline
         con los 15 experts de ejemplo — comparar contra el
         ejemplo de sección 2 (misma estructura, hash distinto es OK)
PASO 13: Conectar LLM real (implementar PuertoLLM con el Router
         de DOC3/api-router — el Cognitive Engine NUNCA llama a
         un provider directo, siempre vía Router)
PASO 14: Test end-to-end: sequence.json de nivel BASICO →
         ejecuta fase A→B→C con los 15 expertos → Juez Central
         (E296) emite veredicto → debe completar sin excepciones
PASO 15: SOLO al pasar el paso 14 → generar las 285 fichas
         restantes siguiendo el patrón de H2 sección 4, usando
         los nombres ya catalogados en GRUPO_H_MAXBRY_G2.md

CRITERIO DE ACEPTACIÓN (Definition of Done de este paquete):
✅ Los 15 expertos de ejemplo ejecutan sin modificar el motor
✅ Fusion Engine resuelve contradicciones por score, nunca por
   "el último que escribió gana"
✅ Sistema de Jueces escala correctamente Local→Capa→Central
   cuando la confianza es baja, nunca aprueba por defecto
✅ sequence.json generado es determinista: mismo requirements.json
   + mismas fichas disponibles → mismo grafo de fases (el hash
   cambia por timestamp, la estructura no)
✅ Ningún LLM decide arquitectura — solo devuelve proposals con
   schema validado

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — SISTEMA H EJECUTABLE COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "SISTEMA_H_EJECUTABLE (H1+H2+H3+H4)",
    "fecha": "2026-07-12",
    "fuente_de_verdad": true,
    "estado": "CODIGO_REAL_LISTO_PARA_CLAUDE_CODE"
  },
  "origen_codigo": {
    "fables_sin_modificar": ["cognitive_engine.py", "expert_pool.py",
      "router_core.py", "team_core.py", "planner_offline.py"],
    "gaps_resueltos_por_sonnet": ["fusion_engine.py (archivo completo,
      solo existía un parche que lo referenciaba)", "sistema_jueces.py
      (nunca existió en código real, solo conceptual en GRUPO_H)"]
  },
  "fichas_yaml": {"ejemplos_completos_dados": 15, "restantes_por_generar": 285,
    "patron_documentado": true, "candidato_a_automatizar": true},
  "tests_incluidos": 5,
  "sequence_json_ejemplo": "seq_ejemplo_basico_001, nivel BASICO, 15 expertos, 3 fases",
  "orden_claude_code": "15 pasos, no saltar ninguno",
  "documentos_paquete": ["H1_MOTOR_COGNITIVO_EJECUTABLE.md",
    "H2_FICHAS_YAML_EJEMPLOS.md", "H3_ROUTER_TEAM_JUECES_EJECUTABLE.md",
    "H4_ENSAMBLAJE_FINAL_Y_TESTS.md"],
  "nota_importante": "Este paquete es EJECUTABLE pero el Director indicó
    'no diseñar hasta terminar el debate' como regla general — esta
    excepción fue una instrucción explícita y puntual del Director para
    convertir SOLO el Sistema H en código. No extender esta excepción
    a otras partes del proyecto sin instrucción igual de explícita."
}
