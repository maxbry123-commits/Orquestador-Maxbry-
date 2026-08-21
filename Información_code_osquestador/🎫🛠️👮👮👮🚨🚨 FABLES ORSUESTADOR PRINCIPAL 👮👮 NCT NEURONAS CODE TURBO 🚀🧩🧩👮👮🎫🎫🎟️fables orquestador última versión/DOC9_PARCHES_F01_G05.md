# DOCUMENTO 9 — PARCHES F01-F06 + G01-G05
# 11 PARCHES COMPLEMENTARIOS
# VERSION FINAL

## F01 — CAPABILITY GRAPH JSON EJECUTABLE
UBICACIÓN: Bloque 0 | Archivo: capability_graph.json | Carpeta: A11_documentation/

```json
{
  "capability_graph": {
    "version": "1.0",
    "capabilities": [
      {"id":"CAP-01","name":"PLANIFICAR","component":"PLANNER_OFFLINE","layer":"KERNEL","inputs":["objetivo","restricciones"],"outputs":["sequence.json","task_list"],"enables":["CAP-02","CAP-03"],"status":"MVP","file":"planner_offline.py"},
      {"id":"CAP-02","name":"EJECUTAR","component":"RUNTIME","layer":"RUNTIME","inputs":["artifact_id","input_data"],"outputs":["resultado","execution_log"],"depends_on":["CAP-04","CAP-05"],"status":"MVP","file":"executor.py"},
      {"id":"CAP-03","name":"VERIFICAR","component":"VERIFIER","layer":"VERIFICATION","inputs":["artifact_code","artifact_contract"],"outputs":["validation_report","pass_fail"],"depends_on":["CAP-05"],"enables":["CAP-02"],"status":"MVP","file":"verifier.py"},
      {"id":"CAP-04","name":"RECUPERAR","component":"RECOVERY_CORE","layer":"STATE","inputs":["checkpoint","wal_log"],"outputs":["estado_restaurado"],"depends_on":["CAP-05"],"status":"MVP","file":"recovery_core.py"},
      {"id":"CAP-05","name":"MEMORIZAR","component":"STATE_MANAGER","layer":"STATE","inputs":["evento","datos"],"outputs":["estado_actualizado","hash_chain"],"enables":["CAP-02","CAP-03","CAP-04"],"status":"MVP","file":"state_manager.py"},
      {"id":"CAP-06","name":"AUDITAR","component":"AUDIT_SYSTEM","layer":"VERIFICATION","inputs":["ejecucion_log","artifact_manifest"],"outputs":["audit_report","findings"],"depends_on":["CAP-05"],"status":"MVP","file":"audit_system.py"},
      {"id":"CAP-07","name":"OBSERVAR","component":"OBSERVABILITY","layer":"VERIFICATION","inputs":["eventos_sistema"],"outputs":["metrics","traces","logs"],"depends_on":["CAP-05"],"enables":["CAP-06"],"status":"MVP","file":"observability.py"}
    ],
    "dependency_order": ["CAP-05","CAP-04","CAP-03","CAP-07","CAP-06","CAP-02","CAP-01"]
  }
}
```

---

## F02 — 12 MAPAS ADICIONALES
UBICACIÓN: Bloque 0 | Archivo: MAPS_INDEX.md | Carpeta: A11_documentation/

MVP (construir ahora):
- MAPA 01: VISIÓN GLOBAL — North Star + objetivos 1/3/5 años
- MAPA 02: CAPABILITY MAP — CAP-01 a CAP-07 con dependencias
- MAPA 03: COMPONENT MAP — 25 componentes + capa
- MAPA 04: DEPENDENCY MAP — DEPENDENCY_REGISTRY.json
- MAPA 05: DATA FLOW MAP — entrada→procesamiento→salida
- MAPA 06: GOVERNANCE MAP — CONSTITUCIÓN→ADR→DECISIONES→CONTRATOS→CÓDIGO
- MAPA 07: STATE MAP — FSM diagrama + estados artifact + tarea

POST-MVP:
- MAPA 08: COST FLOW MAP — CPU/memoria/tiempo por componente
- MAPA 09: SECURITY MAP — GPG + permisos + sandbox por artifact
- MAPA 10: RECOVERY MAP — ERR_XX → política de recovery
- MAPA 11: TESTING MAP — Unit/Integration/E2E por componente
- MAPA 12: ROADMAP TEMPORAL — Fase 0→5 con milestones

---

## F03 — SELF_AUDIT_ENGINE + PATCH_ENGINE
UBICACIÓN: Bloque 15-B | Carpeta: A09_validators/

### SELF_AUDIT_ENGINE
Archivo: self_audit_engine.py | Capa: VERIFICATION
Trigger: cada 10 artifacts COMMITTED
Frecuencia: automático + manual con comando AUDIT
Output: audit_report.json
Escala al Director si criticidad = HIGH y hallazgo > 48h

### PATCH_ENGINE
Archivo: patch_engine.py | Capa: VERIFICATION
10 pasos: leer→validar→identificar→verificar compat→backup→aplicar→validar→CHANGELOG→decision_registry→notificar
Output: patch_report.json | Rollback: automático si falla paso 7

Total componentes actualizado: 25 → 27

---

## F04 — INTEGRATION TESTS IT01-IT06
UBICACIÓN: Bloque 4 | Archivo: integration_tests.json | Carpeta: A12_tests_control_plane/

IT01: Loader carga artifact correcto desde Storage
IT02: Pipeline Verifier N0-N5 completo
IT03: Executor invoca Space correctamente
IT04: Recovery desde fallo completo
IT05: DAG ejecuta secuencia completa en orden
IT06: GCL v1.0 bloquea artifacts inválidos + rollback

---

## F05 — G3 REGLA UNIVERSAL
UBICACIÓN: Bloque 0 | Archivo: CONSTITUTION.md | Sección: Constitución

"Ningún modelo construye sin pre-diagrama previo"

PROHIBIDO sin:
- ✅ Pre-diagrama 15 dominios aprobado
- ✅ Bloque 0 completo
- ✅ system_manifest.json presente
- ✅ project_index.json presente
- ✅ template_completeness_check = COMPLETO

Si falta cualquiera → STOP → [PENDIENTE_DIRECTOR]
Aplica a: Claude, GPT, Kimi, Gemini — cualquier modelo
Nivel: CONSTITUCIÓN — no puede anularse por prompt de usuario

---

## F06 — JSON CAPA 2
UBICACIÓN: Bloque 15-B | Carpeta: memoria/registros/

### version_registry.json
Propósito: historial inmutable de versiones por artifact
Regla: append-only — nada se borra

### event_log.jsonl
Propósito: log de todos los eventos del sistema
Regla: hash chain — cada evento referencia el anterior
Tipos: COMMIT | EXECUTE | FAIL | RECOVER | AUDIT

### evidence_registry.json
Propósito: prueba de que cada paso ocurrió
Tipos: TEST_PASS | VERIFIER_PASS | COMMIT | DEPLOY
Regla: sin evidencia = no cuenta como hecho

### risk_log.json
Propósito: registro activo de riesgos detectados
Estados: OPEN | MITIGATED | CLOSED
Regla: revisar en cada gate de calidad

### roles_registry.json
Roles definidos:
- ROL-01 DIRECTOR: puede_aprobar=true / puede_construir=false / puede_ejecutar=false
- ROL-02 IA_CONSTRUCTORA: puede_aprobar=false / puede_construir=true / puede_ejecutar=false
- ROL-03 SISTEMA: puede_aprobar=false / puede_construir=false / puede_ejecutar=true

---

## G01 — MOTOR DECISIONES (kernel.py)
UBICACIÓN: Bloque 0 | Archivo: kernel.py | Carpeta: raíz brain | Tarea: T001

FSM en Python con tabla de transiciones:
IDLE→PARSE→ROUTE→EXECUTE→VERIFY→COMMIT→IDLE

NUNCA usar LLM para decidir transiciones.
Determinista: misma entrada = misma decisión siempre.

---

## G02 — CLASIFICADOR INTENCIONES (dispatcher.py)
UBICACIÓN: Bloque 0 | Archivo: router/dispatcher.py | Tarea: T003

Keywords ponderados — O(n) — sin ML — determinista.
Salida: {"modo":"CONSTRUIR","confianza":0.90,"keywords_detectados":["construye"]}
Empate → preguntar al Director (1 pregunta máx).

---

## G03 — VALIDADOR N0-N5 (verifier.py)
UBICACIÓN: Bloque 15-B | Archivo: ejecucion/verifier.py | Tareas: T014-T019

N0: gnupg GPG sig
N1: hashlib SHA256
N2: jsonschema schema
N3: semver version
N4: ast import whitelist
N5: ast LLM ratio ≤ 0.10

Pipeline: N0→N1→N2→N3→N4→N5 — falla uno → STOP

---

## G04 — MANEJADOR ERRORES (error_handler.py)
UBICACIÓN: Bloque 15-B | Archivo: ejecucion/error_handler.py | Tarea: T020 NUEVA

ERR_SCHEMA→REJECT | ERR_HASH→RELOAD×3 | ERR_TIMEOUT→RETRY+5s×3
ERR_MEMORY→REJECT+escalar | ERR_IMPORT→REJECT | ERR_RUNTIME→RETRY×2
ERR_COMPAT→REJECT+ADR | ERR_NOT_FOUND→RELOAD×1 | ERR_NOT_COMMITTED→REJECT | ERR_VERSION→REJECT+actualizar

Todo registrado en REGISTRO_EVENTOS. Sin LLM para decidir política.

---

## G05 — MEMORIA VIVA (state_manager.py)
UBICACIÓN: Bloque 15-B | Archivo: ejecucion/state_manager.py | Tarea: T028

Hash chain: cada entrada referencia hash de la anterior.
Operaciones: READ | WRITE (append-only) | VERIFY | REPLAY

Triggers automáticos:
- Cada COMMIT → escribe
- Cada EXECUTE → escribe
- Cada FAIL → escribe
- Cada RECOVER → escribe

Reglas: append-only | timestamp | autor | hash verificable
❌ nunca delete ❌ nunca update de entradas existentes

---

## RESUMEN PARCHES

F01 ✅ Capability Graph JSON → Bloque 0
F02 ✅ 12 Mapas adicionales → Bloque 0
F03 ✅ self_audit + patch → Bloque 15-B
F04 ✅ Integration Tests IT01-IT06 → Bloque 4
F05 ✅ G3 Regla Universal → Bloque 0 Constitución
F06 ✅ JSON Capa 2 → Bloque 15-B
G01 ✅ Motor decisiones → Bloque 0 KERNEL
G02 ✅ Clasificador intenciones → Bloque 0 KERNEL
G03 ✅ Validador N0-N5 → Bloque 15-B
G04 ✅ Manejador errores → Bloque 15-B (T020 NUEVA)
G05 ✅ Memoria viva → Bloque 15-B STATE
