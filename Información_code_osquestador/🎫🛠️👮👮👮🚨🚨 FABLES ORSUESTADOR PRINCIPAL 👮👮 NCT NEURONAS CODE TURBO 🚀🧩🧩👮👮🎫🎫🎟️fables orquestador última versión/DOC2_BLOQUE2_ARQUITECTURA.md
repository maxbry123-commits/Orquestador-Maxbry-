# DOCUMENTO 2 — BLOQUE 2: PECP Y ARQUITECTURA GENERAL
# VERSION FINAL

## PECP — Plataforma Estructura de Construcción de Proyecto

### KERNEL (decide)
- Responsabilidad: router, DAG, índice, constitución, config
- Restricción: NO usa LLM para decidir
- Garantía: mismas entradas = misma decisión siempre

### RUNTIME (ejecuta)
- Responsabilidad: spaces, agentes, fichas, DAG engine, planner_offline
- Restricción: solo ejecuta lo que KERNEL autoriza

### VERIFICATION (verifica)
- Responsabilidad: CEF, VSE, GCL, audit
- Restricción: verifica SIEMPRE antes de ejecutar
- Garantía: ningún artifact se ejecuta sin pasar N0-N5

### STATE (recuerda)
- Responsabilidad: recovery core, registros, WAL, Crazy Wall
- Restricción: única fuente de verdad del estado
- Garantía: recovery completa desde cualquier fallo

---

## ARQUITECTURA GENERAL

REPO 1: [PROYECTO]-brain (protegido)
DB XATA: catálogo/índice (NO guarda código)
OBJECT STORAGE: código real de fichas
SPACES HF: ejecutan Python real (50-100 paralelos)
  - ComputePool: 80
  - HybridPool: 15
  - LLMPool: 5

---

## ESTRUCTURA REPO 1 (BRAIN)

```
📂 github.com/[PROYECTO]-brain/
├── system_manifest.json
├── project_index.json
├── project_manifest.json
├── orquestador.py
├── 📂 schemas/
│   ├── sequence.schema.json
│   ├── state.schema.json
│   └── contract.schema.json
├── 📂 flujo/
│   ├── sequence.json
│   ├── state.json
│   └── fallback.json
├── 📂 router/
│   └── dispatcher.py
├── 📂 dag/
│   └── dag.py
├── 📂 ejecucion/
│   ├── loader.py
│   ├── verifier.py
│   ├── executor.py
│   └── space_client.py
├── 📂 observabilidad/
│   ├── logger.py
│   └── tracer.py
├── 📂 memoria/
│   ├── 📂 recovery_core/
│   │   ├── tier_0_constitution.json
│   │   ├── tier_1_blueprints.json
│   │   ├── tier_2_artifacts.json
│   │   ├── tier_3_states.json
│   │   └── tier_4_metadata.json
│   └── 📂 registros/
│       ├── APPROVED_REGISTRY.json
│       ├── INTEGRATION_MAP.json
│       ├── PASS_KPI_SIGMA.json
│       ├── APPROVAL_LEDGER.json
│       ├── PUZZLE_MAP_GLOBAL.json
│       └── DEPENDENCY_REGISTRY.json
├── 📂 instructions/
│   ├── README.md
│   ├── 📂 _agent_guide/
│   ├── 📂 identity/
│   ├── 📂 behavior/
│   ├── 📂 contracts/
│   ├── 📂 validation/
│   ├── 📂 recovery/
│   └── 📂 instructions_1/ ... instructions_5/
├── 📂 A06_artifact_contracts/[ficha_id]/artifact_contract.json
├── 📂 A07_artifact_specs/[ficha_id]/artifact_spec.md
├── 📂 A08_schemas/
├── 📂 A09_validators/validators.py
├── 📂 A10_approval_ledger/APPROVAL_LEDGER.json
├── 📂 A11_documentation/
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── BLUEPRINT.md
│   ├── TASKS.md
│   ├── DECISIONS.md
│   ├── ARTIFACT_STANDARD.md
│   ├── VERSIONING_POLICY.md
│   ├── ERROR_CODES.md
│   ├── LOADER_CONTRACT.md
│   ├── CHANGELOG.md
│   ├── OUTPUT_FORMAT_STANDARD.md
│   ├── decision_registry.json
│   ├── interface_catalog.json
│   ├── integration_checklist.md
│   ├── release_standard.md
│   ├── document_authority_map.json
│   ├── quality_gates.json
│   ├── audit_findings.json
│   ├── risk_registry.json
│   ├── contract_template.json
│   ├── artifact_spec_template.md
│   ├── adr_template.md
│   ├── kpi_standard.json
│   ├── acceptance_protocol.md
│   ├── template_completeness_check.md
│   └── 📂 tasks/TASK_001.md ... TASK_XXX.md
├── 📂 A12_tests_control_plane/
└── 📂 A13_artifact_manifests/[ficha_id]/artifact_manifest.json
```

---

## DB XATA

```json
{
  "master_index": "ficha_id: {archivo, space, invocacion, tags, prioridad}",
  "semantic_index": "búsqueda por intención",
  "artifact_contracts": "[ficha_id].json"
}
```
Regla: Solo COMMITTED es visible para el cerebro.

---

## REPO 2 (MODULES)

```
📂 github.com/[PROYECTO]-modules/
├── 📂 agentes/
│   ├── agent_A.py + permissions.json
│   ├── agent_B.py + permissions.json
│   └── agent_C.py + permissions.json
├── 📂 propuestas/
├── 📂 instrucciones_1/
├── 📂 instrucciones_2/
└── 📂 instrucciones_3/
```
Regla: Agentes NUNCA tocan el cerebro.

---

## OBJECT STORAGE

```
📂 object_storage/[PROYECTO]/
├── 📂 B01_artifact_code/[ficha_id]/artifact_code.py
├── 📂 B02_artifact_internal/[ficha_id]/internal/
├── 📂 B03_artifact_tests/
├── 📂 B04_artifact_versions/
├── 📂 B05_artifact_packages/[ficha_id]_bundle.zip
├── 📂 B06_execution_logs/
├── 📂 B07_traces/traces.jsonl
├── 📂 B08_runtime_outputs/
├── 📂 B09_checkpoints/
└── 📂 B10_cache/
```
