# GUÍA INTERNA A.1 — PARCHE DE AUDITORÍA (4 pasadas)
# Cierra gaps detectados en GUÍA A+B+C
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GAP 1 — UNIVERSAL MODULE CONTRACT COMPLETO (enchufe Opus)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este es EL contrato que conecta TODO: fichas de código,
prompts DSL, agentes, APIs, MCP, DB, tools. Cada módulo del
sistema (Loop Engine, expertos G2, micro-agentes MA-*,
Router) DEBE emitir este contrato para ser conectable.

SCHEMA COMPLETO (de la bandeja, v1.5, campos obligatorios):
```json
{
  "artifact_id": "reasoning.loop_engine.run",
  "artifact_version": "1.0.0",
  "contract_version": "1.5",
  "contract_hash": "sha256:...",
  "hash_algorithm": "sha256",
  "estado": "draft|testing|active|deprecated|blocked",
  "ciclo_vida": {
    "creado": "ISO-8601",
    "deployed_at": null,
    "deprecated_at": null,
    "blocked_at": null,
    "replaces": []
  },
  "registry_metadata": {
    "slot": "reasoning.loop",
    "priority": 10,
    "domain": "cognitive_processing",
    "capa": "KERNEL|RUNTIME|VERIFICATION|STATE"
  },
  "contrato": {
    "rol": "transform|source|sink",
    "consume": {
      "datatype": {"family": "task", "type": "goal_lock", "version": 1},
      "schema_uri": "contracts/task.schema.json",
      "intent": ["reasoning_request"],
      "required": ["goal_lock", "dre_score"]
    },
    "expone": {
      "datatype": {"family": "task", "type": "loop_result", "version": 1},
      "schema_uri": "contracts/loop_result.schema.json"
    },
    "errores": {
      "E001": {"code": "E001", "retryable": true, "max_retries": 3},
      "E002": {"code": "E002", "retryable": false, "fatal": true}
    },
    "restricciones": {
      "requires_preceding": [{"family": "goal_lock"}],
      "cannot_follow": [{"family": "aborted_pipeline"}]
    }
  },
  "naturaleza": {
    "determinista": false,
    "idempotente": false,
    "puro": false,
    "efectos": {"escribe_db": true, "llama_api": true, "irreversible": false}
  },
  "seguridad": {
    "permisos": ["read:oc", "write:checkpoint"],
    "limites": {"timeout_ms": 300000, "deadline_ms": 600000,
                "memoria_max_mb": 512, "cpu_max_percent": 80},
    "sandbox": "process"
  },
  "ejecucion": {
    "kind": "code",
    "transport": "importlib",
    "config": {"module": "reasoning.loop_engine.core", "fn": "run_loop_engine"},
    "healthcheck": {"interval_ms": 30000}
  },
  "resultado": {
    "success_schema_uri": "contracts/loop_result.schema.json",
    "error_schema_uri": "contracts/error.schema.json",
    "trace_id_format": "uuid"
  },
  "dependencias": {"runtime_min": "3.11"},
  "versioning": {"min": "1.0.0", "max": "1.99.99", "mode": "semver_strict"},
  "gobernanza_ref": {
    "build_id": "BUILD-...",
    "ledger": {"artifact_id": "reasoning.loop_engine.run", "version": "1.0.0"}
  }
}
```

REGLA DE ORO: TODO módulo nuevo (experto G2, micro-agente MA-*,
nodo del Kernel, Loop Engine) EMITE este contrato antes de
poder registrarse en el Capability Registry [18] de DOC1.
Sin contrato válido → el módulo no existe para el sistema.

UBICACIÓN: contracts/universal_module_contract.schema.json
(raíz contracts/, ya existente en las 13 raíces de DOC1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GAP 2 — CONTENIDO DE policies/gcl_rules.yaml
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reglas GCL mínimas para el MVP (expandibles después):

```yaml
# policies/gcl_rules.yaml
rules:
  - id: R001_presupuesto_excedido
    guard: "estado.presupuesto_usado > estado.presupuesto_max"
    command: "HALT_escalar_director"
    severity: block

  - id: R002_consenso_insuficiente
    guard: "estado.task_level == 'critical' and estado.consenso_quorum < 3"
    command: "CONSENSUS_BLOCKED"
    severity: block

  - id: R003_hash_corrupto
    guard: "estado.hash_actual != estado.hash_esperado"
    command: "RECOVERY_nivel_3_checkpoint"
    severity: block

  - id: R004_deadline_proximo
    guard: "estado.tiempo_restante_ms < 60000"
    command: "WARN_deadline_proximo"
    severity: warn

  - id: R005_agente_sin_heartbeat
    guard: "estado.ultimo_heartbeat_s > 60"
    command: "RECOVERY_nivel_2_rollback"
    severity: block

  - id: R006_scope_creep_detectado
    guard: "estado.output_excede_not_in_scope == true"
    command: "REJECTED_escritor_retry"
    severity: block

  - id: R007_max_reintentos_agotados
    guard: "estado.intento_actual >= estado.max_intentos"
    command: "ESCALATE_nivel_5_director"
    severity: escalate
```

Estas 7 reglas cubren los casos ya definidos en DOC1
(Recovery Engine 5 niveles, GOAL_LOCK, max_intentos) —
GCL las hace VERIFICABLES formalmente en vez de solo
lógica dispersa en el código.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GAP 3 — TEAM AGENT: CEREBRO PEQUEÑO DETERMINISTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Respuesta 8 del Director: "no capas de 200-500 LOC en el
agente... cerebro más determinista pequeño inspirado un poco
en el orquestador pero con diferentes PIPELINES para ejecutar
métodos de trabajo... trabajar múltiples tareas al mismo
tiempo en modo loops y bucles"

ESTRUCTURA RESUELTA:
```
team_agente/
├── cerebro_ta/              (≤300 LOC total, inspirado en Kernel)
│   ├── core.py              # ≤100 LOC: recibe orden de MAXBRY
│   │                          Orquestador, decide qué pipeline usar
│   ├── pipeline_selector.py # ≤80 LOC: elige entre N pipelines
│   │                          según tipo de tarea (capability match)
│   └── multitask_scheduler.py # ≤120 LOC: asyncio.gather() para
│                                correr M tareas simultáneas
├── pipelines/                (intercambiables, cada uno un método)
│   ├── pipeline_code_gen.py  # usa staff: Claude Code/Open Code
│   ├── pipeline_research.py  # usa staff: agentes de investigación
│   ├── pipeline_refactor.py  # usa staff: Aider/Open Claw
│   └── pipeline_generic.py   # fallback: usa micro-agentes MA-*
└── staff_registry.json       # qué agente externo cumple qué capability
```

FLUJO:
```python
# cerebro_ta/core.py
async def recibir_orden(orden_de_maxbry_orquestador: dict):
    pipeline = pipeline_selector.elegir(orden_de_maxbry_orquestador)
    # multitask: si hay N sub-tareas independientes, correr en paralelo
    resultados = await multitask_scheduler.ejecutar_paralelo(
        [pipeline.run(sub) for sub in orden_de_maxbry_orquestador["subtareas"]]
    )
    return consolidar(resultados)
```

REGLA DE CREACIÓN DE MICRO-AGENTE (ya definida, ratificada):
```python
def pipeline_selector.elegir(orden):
    capability_requerida = orden["capability"]
    if capability_requerida in staff_registry:
        return pipelines[staff_registry[capability_requerida]]
    else:
        # no hay agente de staff → construir micro-agente DSL/DAG
        return pipeline_generic.crear_micro_agente(capability_requerida)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GAP 4 — MAPEO 300 EXPERTOS (GRUPO_H) ↔ 9 FASES (GUÍA C)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Los 300 expertos de GRUPO_H y las 9 FASES del Loop Engine
NO son sistemas paralelos — los expertos SON quienes ejecutan
el contenido de cada fase cuando el Loop Engine corre a
NIVEL_AVANZADO o NIVEL_TURBO (donde se justifica su costo).
En NIVEL_RAPIDO/BASICO, fases más simples usan MYTHOS directo
(sin invocar el catálogo completo de 300 fichas).

MAPEO EXACTO:
```
FASE_0 (Inicialización/Constitución) → CAPA A, célula A2
        (Filtros axiomáticos E021-E040, bloqueante)
FASE_1 (Comprensión/extracción/OCR)   → CAPA A, células A1+A3
        (E001-E020 captura + E041-E060 normalización)
FASE_2 (Análisis/descomposición)      → CAPA A, célula A4 +
        CAPA B, célula B1 (E061-E080 + E101-E120)
FASE_3 (Planificación multiobjetivo)  → CAPA B, célula B3
        (E141-E160 planificación)
FASE_4 (Debate/refutaciones)          → CAPA B, célula B4
        (E161-E180 razonamiento profundo + Devil Agent DOC1)
FASE_5 (Verificación/consistencia)    → CAPA A, célula A5 +
        CAPA B, célula B5 (E081-E100 + E181-E200)
FASE_6 (Optimización/fusión)          → CAPA B, célula B2
        (E121-E140 síntesis)
FASE_7 (Autoevaluación/confianza)     → CAPA B, célula B5
        (E181-E200, mismo que verificación, 2da pasada)
FASE_8 (Síntesis final/documentación) → CAPA C, células C1-C5
        (E201-E300 construcción→emisión completo)
```

REGLA DE ACTIVACIÓN POR NIVEL:
```
NIVEL_RAPIDO/BASICO: solo usa MYTHOS (DOC1 [7.1]) directo,
                      NO invoca fichas de expertos individuales
                      (sería sobre-ingeniería para tarea simple)
NIVEL_AVANZADO:       invoca expertos de las células CRÍTICAS
                      por fase (1-3 expertos representativos)
NIVEL_TURBO:          invoca el enjambre completo de la célula
                      correspondiente (hasta 20 expertos/célula)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA A.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_A1_PARCHE_AUDITORIA","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno","fuente_de_verdad":true,
    "pasadas_auditoria": 4},
  "gaps_cerrados": [
    "universal_module_contract_completo_en_contracts/",
    "gcl_rules_yaml_7_reglas_iniciales",
    "team_agent_cerebro_pequeno_estructura_completa",
    "mapeo_300_expertos_a_9_fases_por_nivel"
  ],
  "regla_activacion_expertos_por_nivel": {
    "rapido_basico": "solo_mythos_directo",
    "avanzado": "1-3_expertos_representativos_por_fase",
    "turbo": "enjambre_completo_celula_hasta_20"
  },
  "siguiente_documento": "GUIA_D_ESTRUCTURA_REPOS_EXPANDIDA"
}
