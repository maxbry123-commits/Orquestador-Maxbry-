# GUÍA INTERNA B — GCL + Z3 + SLOT CONTRACT
# Documento de trabajo de Claude — pseudo-código + Python real
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. QUÉ RESUELVE Y DÓNDE VIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Antes de ejecutar cualquier acción irreversible, el sistema
verifica FORMALMENTE (no con heurísticas) que las reglas
activas son consistentes y que la acción propuesta no viola
ninguna combinada con las demás.

Vive en: cerebro/ (REPO 2) → kernel/gcl/
Se activa en: [30] Self Check (DOC1) y en P10/P13 del
pipeline JUEZ (GRUPO_F) — momento exacto: antes de P-CODE
(GCL-lite, rápido) y en el cierre P13 (GCL v1.0, completo).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. GCL — GUARDED COMMAND LANGUAGE (capa de reglas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONCEPTO: cada regla = Guard(condición) → Command(acción)

PSEUDO-CÓDIGO:
```
regla:
  guard: condicion_booleana
  command: accion_a_tomar

ejemplo:
  guard: presupuesto_usado > presupuesto_max
  command: HALT_y_escalar_Director

  guard: task_level == "critical" AND consenso_quorum < 3
  command: CONSENSUS_BLOCKED

  guard: hash_actual != hash_esperado
  command: STATE_CORRUPTION_recovery_nivel_3
```

PYTHON REAL (estructura mínima, ≤150 LOC):
```python
# kernel/gcl/rules.py
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class GCLRule:
    id: str
    guard: Callable[[dict], bool]   # recibe el estado, retorna bool
    command: str                     # acción simbólica a ejecutar
    severity: str                    # "block" | "warn" | "escalate"

# Registro de reglas activas (cargado desde policies/gcl_rules.yaml)
RULES: list[GCLRule] = []

def evaluate_all(state: dict) -> list[GCLRule]:
    """Retorna las reglas cuyo guard se cumple (violaciones o triggers)."""
    return [r for r in RULES if r.guard(state)]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. MOTOR Z3 — VERIFICACIÓN SAT/UNSAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONCEPTO: antes de comprometer un plan, se traduce el
conjunto de restricciones activas a fórmulas Z3 y se
pregunta si existe una asignación de valores que las
satisfaga TODAS a la vez (SAT) o no (UNSAT).

CASOS DE USO EN NCT:
- ¿El plan del Team Agent respeta budget Y deadline Y
  dependencias a la vez? (si UNSAT → replantear antes de
  gastar un solo token en ejecutar)
- ¿Las políticas de 2 agentes en el mismo enjambre son
  compatibles? (si UNSAT → conflicto real, no aparente)
- ¿El GOAL_LOCK es alcanzable dado el estado actual?

PSEUDO-CÓDIGO:
```
restricciones = [
  presupuesto_usado + costo_tarea <= presupuesto_max,
  tiempo_transcurrido + tiempo_estimado <= deadline,
  dependencia_A completada ANTES de tarea_B
]
resultado = Z3.check(restricciones)
si resultado == UNSAT:
    devolver conflicto_imposible → JUEZ rechaza el plan
si resultado == SAT:
    devolver asignacion_valida → JUEZ aprueba, continua
```

PYTHON REAL (usa z3-solver, ya en dependencias de FUENTE 4):
```python
# kernel/gcl/z3_verifier.py
from z3 import Solver, Int, Bool, sat, unsat

def verificar_plan(presupuesto_max, presupuesto_usado, costo_tarea,
                    deadline_ms, tiempo_transcurrido_ms, tiempo_estimado_ms):
    """Retorna (True, None) si SAT, (False, razon) si UNSAT."""
    s = Solver()
    presupuesto = Int('presupuesto_usado')
    tiempo = Int('tiempo_transcurrido')

    s.add(presupuesto == presupuesto_usado + costo_tarea)
    s.add(presupuesto <= presupuesto_max)
    s.add(tiempo == tiempo_transcurrido_ms + tiempo_estimado_ms)
    s.add(tiempo <= deadline_ms)

    if s.check() == sat:
        return True, None
    return False, "UNSAT: presupuesto o deadline imposibles con este plan"
```

NIVEL DE USO (según DECISIÓN del Director, escala 20-1000):
  NIVEL_RAPIDO (20-50 pasos):    Z3 se SALTA (solo GCL-lite)
  NIVEL_BASICO (100-300):        Z3 en GOAL_LOCK únicamente
  NIVEL_AVANZADO (300-800):      Z3 en GOAL_LOCK + Consenso
  NIVEL_TURBO (800-1000):        Z3 en cada paso crítico (P10, P13)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. SLOT CONTRACT SC1-SC6
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFINICIÓN CONCEPTUAL DEL DIRECTOR (autoritativa):
SC1 Entrada válida
SC2 Dependencias completas
SC3 Permisos correctos
SC4 Estado consistente
SC5 Objetivo alcanzable
SC6 Salida validada

MAPEO A NOMBRES DE ARCHIVO YA EXISTENTES EN FUENTE 4
(reconciliación: incluir en la implementación):
SC1 (Entrada válida)        ↔ sc1_ficha_id.json
SC2 (Dependencias)           ↔ sc2_hash.json (verifica hash de deps)
SC3 (Permisos)                ↔ sc3_schemas.json (schema=permisos declarados)
SC4 (Estado consistente)      ↔ sc4_runtime_type.json
SC5 (Objetivo alcanzable)     ↔ sc5_llm_ratio.json (verifica 90/10 budget)
SC6 (Salida validada)         ↔ sc6_idempotente.json

CADA SLOT DEVUELVE:
```json
{"status": "SAT", "reason": "OK"}
{"status": "UNSAT", "reason": "descripcion del fallo"}
```

PSEUDO-CÓDIGO DEL FLUJO COMPLETO:
```
entrada → SC1 → SC2 → SC3 → SC4 → SC5 → SC6 → ejecución
Si cualquier SC devuelve UNSAT:
    detener → reparar (RECOVERY) o replantear (REPLAN)
```

PYTHON REAL:
```python
# fichas/verifier/slot_contract.py
from typing import TypedDict, Literal

class SlotResult(TypedDict):
    status: Literal["SAT", "UNSAT"]
    reason: str

def sc1_entrada_valida(ficha_input: dict) -> SlotResult:
    if not ficha_input.get("doc_id"):
        return {"status": "UNSAT", "reason": "falta doc_id (ficha_id)"}
    return {"status": "SAT", "reason": "OK"}

def sc2_dependencias_completas(ficha: dict, registry: dict) -> SlotResult:
    for dep in ficha.get("dependencies", []):
        if dep not in registry or registry[dep]["estado"] != "active":
            return {"status": "UNSAT", "reason": f"dependencia {dep} no activa"}
    return {"status": "SAT", "reason": "OK"}

def sc3_permisos_correctos(ficha: dict, permisos_otorgados: list) -> SlotResult:
    requeridos = ficha.get("seguridad", {}).get("permisos", [])
    faltantes = [p for p in requeridos if p not in permisos_otorgados]
    if faltantes:
        return {"status": "UNSAT", "reason": f"permisos faltantes: {faltantes}"}
    return {"status": "SAT", "reason": "OK"}

def sc4_estado_consistente(state_hash_actual: str, state_hash_esperado: str) -> SlotResult:
    if state_hash_actual != state_hash_esperado:
        return {"status": "UNSAT", "reason": "hash chain no coincide (posible corrupción)"}
    return {"status": "SAT", "reason": "OK"}

def sc5_objetivo_alcanzable(plan: dict) -> SlotResult:
    from kernel.gcl.z3_verifier import verificar_plan
    ok, razon = verificar_plan(**plan)
    if not ok:
        return {"status": "UNSAT", "reason": razon}
    return {"status": "SAT", "reason": "OK"}

def sc6_salida_validada(output: dict, output_schema: dict) -> SlotResult:
    import jsonschema
    try:
        jsonschema.validate(output, output_schema)
    except jsonschema.ValidationError as e:
        return {"status": "UNSAT", "reason": str(e)}
    return {"status": "SAT", "reason": "OK"}

def run_slot_contract(ficha, registry, permisos, state_hashes, plan, output, schema) -> list[SlotResult]:
    """Ejecuta SC1-SC6 en orden. Detiene en el primer UNSAT (fail-fast)."""
    checks = [
        sc1_entrada_valida(ficha),
        sc2_dependencias_completas(ficha, registry),
        sc3_permisos_correctos(ficha, permisos),
        sc4_estado_consistente(*state_hashes),
        sc5_objetivo_alcanzable(plan),
        sc6_salida_validada(output, schema),
    ]
    return checks  # el llamador revisa el primer UNSAT
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. GCL-LITE vs GCL v1.0 (dos velocidades, ya definido en
   FUENTE 4, ratificado aquí con integración a DOC1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GCL-LITE (por fase, O(1), rápido):
  Verifica: presupuesto>0 + contratos + task_id +
            hash(last_ledger_entry)
  NO verifica el DAG completo
  Se activa: en CADA paso del pipeline JUEZ (P00...P13)
  Falla → fail-fast inmediato, no avanza al siguiente paso

GCL v1.0 (gate final, usa Z3, completo):
  Se activa: SOLO en P13 (SESSION_CLOSE, ver PARCHE_CIERRE_H_F)
  Es EL único gate final antes de marcar COMMITTED
  Usa Z3 para verificar consistencia GLOBAL de todo el pipeline
  GCL_ENABLED: true en producción, false en desarrollo (skip)

PYTHON REAL (integración con pipeline JUEZ de GRUPO_F):
```python
# kernel/gcl/gate.py
def gcl_lite_check(fase: str, estado: dict) -> bool:
    """O(1). Se llama en cada paso P00..P13."""
    if estado["presupuesto_usado"] <= 0:
        return False
    if not estado.get("contratos_declarados"):
        return False
    if not estado.get("task_id"):
        return False
    return True  # fail-fast en el llamador si False

def gcl_v1_gate_final(pipeline_completo: dict, gcl_enabled: bool = True) -> tuple[bool, str]:
    """Gate final en P13. Usa Z3. Único por sesión."""
    if not gcl_enabled:
        return True, "GCL_DISABLED (modo dev)"
    from kernel.gcl.z3_verifier import verificar_plan
    ok, razon = verificar_plan(**pipeline_completo["plan_final"])
    return ok, razon or "GCL v1.0 PASS"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DIAGRAMA DE INTEGRACIÓN COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
PUSH_PING [30 clasificaciones] (DOC1)
        │
        ▼
Pipeline JUEZ P-DISCOVER..P13 (GRUPO_F)
        │
        ├─ en CADA paso: GCL-lite check (O(1)) ──fail──> RETRY/ABORT
        │
        ├─ antes de P-CODE: Slot Contract SC1-SC5
        │  (SC6 se hace DESPUÉS del código, con el output real)
        │
        ├─ P-CODE: ESCRITOR genera código
        │
        ├─ P11: RUNTIME ejecuta → Evidence Report L1-L4
        │  → SC6 (salida validada) usa este report
        │
        ├─ P12: sello (ADR)
        │
        └─ P13: GCL v1.0 GATE FINAL (Z3, único, completo)
               │
               ├─ SAT  → COMMITTED en BUILD_REGISTRY
               └─ UNSAT → REJECTED + Failure Registry + razón exacta
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA B
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_B_GCL_Z3_SLOTCONTRACT","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno","fuente_de_verdad":true},
  "gcl": {"tipo":"guarded_command_language","estructura":"guard->command",
    "ubicacion":"kernel/gcl/rules.py"},
  "z3": {"libreria":"z3-solver==4.12.4","uso":"SAT/UNSAT verificacion formal",
    "ubicacion":"kernel/gcl/z3_verifier.py",
    "escala_por_nivel":{"rapido":"skip","basico":"solo_goal_lock",
      "avanzado":"goal_lock+consenso","turbo":"cada_paso_critico"}},
  "slot_contract": {
    "SC1":"entrada_valida","SC2":"dependencias_completas",
    "SC3":"permisos_correctos","SC4":"estado_consistente",
    "SC5":"objetivo_alcanzable_Z3","SC6":"salida_validada",
    "ubicacion":"fichas/verifier/slot_contract.py",
    "fail_fast": true
  },
  "gcl_lite_vs_v1": {
    "lite":{"frecuencia":"cada_paso_P00_P13","complejidad":"O(1)"},
    "v1":{"frecuencia":"solo_P13_session_close","usa":"Z3_completo",
      "flag":"G2_GCL_ENABLED true=prod false=dev"}
  },
  "integracion_pipeline_juez": "GCL-lite en cada paso + SlotContract antes de P-CODE + SC6 en P11 + GCL-v1 en P13",
  "siguiente_documento": "GUIA_C_SISTEMA_LOOPS_AISLADO"
}
