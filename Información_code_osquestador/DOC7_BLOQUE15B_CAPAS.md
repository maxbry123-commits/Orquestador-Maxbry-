# DOCUMENTO 7 — BLOQUE 15-B: CAPAS + COMPONENTES + ESTÁNDARES
# VERSION FINAL

## 4 CAPAS DEL SISTEMA

### KERNEL (decide)
Constitution | Router | Triage | CCL | Modos | Config

### RUNTIME (ejecuta) ← DAG Engine vive aquí
Loader | Executor | DAG Engine | Spaces Connector | Planner Offline | Context Builder | Artifact Registry | Commit Pipeline

### VERIFICATION (verifica)
Verifier N0-N5 | GCL Lite | GCL v1.0 | Audit System | FAG | Observability
+ self_audit_engine | patch_engine

### STATE (recuerda)
WAL | Recovery Core | Crazy Wall | Memory Manager FAISS | Shared Knowledge | Registry (5) | Schema Migration

REGLA: DAG Engine = RUNTIME. NO aparece en KERNEL.

## 27 COMPONENTES REALES

KERNEL: 01.Brain 02.Planner Offline 03.Router 04.Session Manager 05.CLI
RUNTIME: 06.DAG Engine 07.Loader 08.Executor 09.Spaces Connector 10.Context Builder 11.Artifact Registry 12.Commit Pipeline
VERIFICATION: 13.Verifier N0-N5 14.GCL Lite 15.GCL v1.0 16.Audit System 17.FAG 18.Observability 19.self_audit_engine 20.patch_engine
STATE: 21.WAL 22.Recovery Core 23.Crazy Wall 24.Memory Manager FAISS 25.Shared Knowledge 26.Registry(5) 27.Schema Migration

## ORDEN DE CONSTRUCCIÓN
STATE → VERIFICATION → RUNTIME → KERNEL

## MAPA CAPA → COMPONENTE → TAREA

### KERNEL
T001 Brain (orquestador FSM) | T002 Planner Offline | T003 Router/Dispatcher | T004 Session Manager | T005 CLI

### RUNTIME
T006 DAG Engine | T007 DAG Validator | T008 Loader | T009 Executor | T010 Spaces Connector | T011 Context Builder | T012 Artifact Registry | T013 Commit Pipeline

### VERIFICATION
T014 Verifier N0 (GPG) | T015 Verifier N1 (hash) | T016 Verifier N2 (schema) | T017 Verifier N3 (version) | T018 Verifier N4 (compat) | T019 Verifier N5 (AST ratio) | T020 GCL Lite | T021 GCL v1.0 | T022 Audit System | T023 Observability

### STATE
T024 WAL | T025 Checkpoint | T026 Replay | T027 Recovery Core | T028 Crazy Wall | T029 Memory Manager FAISS | T030 Shared Knowledge | T031 Schema Migration

## VALIDADOR N0-N5 (verifier.py)

N0: GPG sig | N1: SHA256 hash | N2: jsonschema | N3: semver | N4: import whitelist (AST) | N5: LLM ratio ≤ 0.10 (AST)
Pipeline: N0→N1→N2→N3→N4→N5 — falla uno → STOP

## MANEJADOR ERRORES (error_handler.py) — T020 NUEVA

ERR_SCHEMA → REJECT
ERR_HASH → RELOAD×3 → REJECT
ERR_TIMEOUT → RETRY+5s×3 → REJECT
ERR_MEMORY → REJECT + escalar Director
ERR_IMPORT → REJECT
ERR_RUNTIME → RETRY×2 → REJECT
ERR_COMPAT → REJECT + ADR obligatorio
ERR_NOT_FOUND → RELOAD×1 → REJECT
ERR_NOT_COMMITTED → REJECT
ERR_VERSION → REJECT + actualizar DEPENDENCY_REGISTRY

## MEMORIA VIVA (state_manager.py) — T028

Hash chain: cada entrada referencia hash de la anterior.
Reglas: append-only | timestamp | autor | hash verificable
Triggers: cada COMMIT/EXECUTE/FAIL/RECOVER → escribe automáticamente

## ARTIFACT_MANIFEST.json (7 SECCIONES)

```json
{
  "artifact_identity": {"artifact_id":"ART-0001","ficha_id":"","name":"","version":"1.0","status":"COMMITTED"},
  "identity": {"artifact_id":"","ficha_id":"","namespace":"","type":"atomic_function"},
  "location": {"repo":"","branch":"main","path":"","storage_path":"","hash_path":""},
  "execution": {"entrypoint":"ejecutar","runtime":"python3.11","timeout_ms":30000,"memory_mb":512,"space":""},
  "dependencies": {"hard":[],"soft":[],"runtime":[],"artifacts":[]},
  "interface": {"input_schema":"","output_schema":""},
  "integrity": {"hash_sha256":"","signature":"","version_lock":true},
  "lifecycle": {"created_at":"","updated_at":"","deprecated":false,"replacement_artifact":null}
}
```

## VERSIONING_POLICY
PATCH x.x.1 → bugfix | MINOR x.1.x → nueva funcionalidad | MAJOR 1.x.x → rompe compatibilidad
Cambio MAJOR → ADR obligatorio

## LIFECYCLE ARTIFACT
DRAFT → GENERATED → VALIDATED → COMMITTED → ACTIVE → DEPRECATED → ARCHIVED

## LIFECYCLE TAREA
PENDIENTE → EN_PROCESO → REVISIÓN → VALIDATED → COMMITTED → REJECTED → DEPRECATED

## LOADER_CONTRACT
REQUEST: {artifact_id, version}
RESPONSE: {status, entrypoint, location, code_hash, manifest}
FLUJO: recibe → lee manifest → resuelve ubicación → verifica hash → carga código → retorna

## JSON CAPA 2

Archivos en memoria/registros/:
- version_registry.json → historial inmutable de versiones (append-only)
- event_log.jsonl → log con hash chain de todos los eventos
- evidence_registry.json → prueba de que cada paso ocurrió
- risk_log.json → riesgos activos con mitigación
- roles_registry.json → DIRECTOR / IA_CONSTRUCTORA / SISTEMA con permisos

## SELF_AUDIT_ENGINE
Archivo: self_audit_engine.py | Capa: VERIFICATION
Trigger: cada 10 artifacts COMMITTED
Detecta: hallazgos abiertos > 48h → escala al Director

## PATCH_ENGINE
Archivo: patch_engine.py | Capa: VERIFICATION
10 pasos: leer→validar→identificar destino→verificar compat→backup→aplicar→validar→CHANGELOG→decision_registry→notificar
Rollback: automático si falla paso 7
