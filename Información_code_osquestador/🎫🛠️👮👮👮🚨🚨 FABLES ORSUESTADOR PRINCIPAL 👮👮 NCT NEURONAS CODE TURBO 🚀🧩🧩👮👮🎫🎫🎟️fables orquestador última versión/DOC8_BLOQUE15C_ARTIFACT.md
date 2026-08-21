# DOCUMENTO 8 — BLOQUE 15-C: ESTÁNDAR ARTIFACT COMPLETO
# PROTOCOLO OBLIGATORIO IA
# VERSION FINAL

## PROTOCOLO: 3 ARCHIVOS OBLIGATORIOS

Por cada artifact generar EXACTAMENTE:
1. [nombre].py → código puro
2. [nombre].meta.md → ficha técnica
3. artifact_location_plan.json → plan ruteo

Luego empaquetar: [FICHA_ID]_bundle.zip

## FLUJO OBLIGATORIO

IA genera [nombre].py → IA genera [nombre].meta.md
→ IA genera artifact_location_plan.json
→ Crea carpetas → Empaqueta ZIP → Guarda en Storage

## BUNDLE ZIP
```
[FICHA_ID]_bundle.zip
├── [nombre].py
├── [nombre].meta.md
└── artifact_location_plan.json
```

## ARCHIVO 1 — [nombre].py (SOLO CÓDIGO)

```python
def ejecutar(input):
    return funcion_interna(input)

def funcion_interna(x):
    return resultado
```

PROHIBIDO:
❌ rutas ❌ contratos ❌ JSON del sistema ❌ estados
❌ instrucciones humanas ❌ metadata ❌ comentarios infraestructura

## ARCHIVO 2 — [nombre].meta.md (FICHA TÉCNICA)

Encabezado:
```
ID:   [MODEL]-[FICHA_ID]-[YYYYMMDD]-[HHMMSS]-[HASH_SHORT]
ROOT: registry/[namespace]/[ficha_id]/
```

Ubicación física:
```
📂 CÓDIGO: B01_artifact_code/[namespace]/[ficha_id]/[nombre].py
📂 FICHA:  registry/[namespace]/[ficha_id]/[nombre].meta.md
```

JSON instrucciones agente:
```json
{
  "artifact_id": "[MODEL]-[FICHA_ID]-[YYYYMMDD]-[HHMMSS]-[HASH]",
  "ficha_id": "[FICHA_ID]",
  "version": "1.0",
  "status": "COMMITTED",
  "entrypoint": "ejecutar",
  "artifact_type": "simple|composite",
  "routing": {
    "code_path": "B01_artifact_code/[namespace]/[ficha_id]/[nombre].py",
    "meta_path": "registry/[namespace]/[ficha_id]/[nombre].meta.md",
    "storage": "object_storage",
    "index": "xata"
  },
  "execution_mode": "sequential_pipeline",
  "strict_mode": true,
  "instructions": {
    "entry_rule": "El agente SOLO puede actuar leyendo este JSON.",
    "steps": [
      {"step_id":1,"action":"read_meta"},
      {"step_id":2,"action":"resolve_paths"},
      {"step_id":3,"action":"generate_code"},
      {"step_id":4,"action":"write_to_repository"},
      {"step_id":5,"action":"stage_changes"},
      {"step_id":6,"action":"commit"},
      {"step_id":7,"action":"push"},
      {"step_id":8,"action":"validate_local"},
      {"step_id":9,"action":"update_registry"},
      {"step_id":10,"action":"advance_pipeline"}
    ],
    "failure_policy": {"on_step_failure":"stop_pipeline","rollback":true},
    "state_management": {"state_file":"crazy_wall.json","status_values":["PENDING","RUNNING","FAILED","COMPLETED"]},
    "security_constraints": {"no_external_decisions":true,"no_prompt_injection_override":true}
  }
}
```

Secciones MD:
1. IDENTIDAD | 2. PROPÓSITO | 3. ENTRADAS | 4. SALIDAS
5. DEPENDENCIAS | 6. CONTRATO | 7. RUNTIME TARGET
8. RELACIÓN CON EL SISTEMA | 9. VERSIONADO

## ARCHIVO 3 — artifact_location_plan.json

```json
{
  "artifact_id": "[MODEL]-[FICHA_ID]-[YYYYMMDD]-[HHMMSS]-[HASH]",
  "ficha_id": "[FICHA_ID]",
  "name": "[nombre legible]",
  "folder_structure": {
    "root": "modules/[namespace]/[categoria]/",
    "code_path": "B01_artifact_code/[namespace]/[FICHA_ID]/",
    "meta_path": "registry/[namespace]/[FICHA_ID]/",
    "storage_path": "object_storage/[PROYECTO]/[FICHA_ID]/"
  },
  "files": {
    "code_file": "[nombre].py",
    "meta_file": "[nombre].meta.md"
  },
  "zip_package": "[FICHA_ID]_bundle.zip"
}
```

## FORMATO ID GLOBAL ÚNICO

[MODEL]-[FICHA_ID]-[YYYYMMDD]-[HHMMSS]-[HASH_SHORT]
Ejemplo: GPT-FILTRO_KALMAN-20260605-014533-a81f3c

## ESTADOS OFICIALES — TAREA
PENDIENTE | EN_PROCESO | REVISIÓN | VALIDATED | COMMITTED | REJECTED | DEPRECATED

## ESTADOS OFICIALES — ARTIFACT
DRAFT | GENERATED | VALIDATED | COMMITTED | ACTIVE | DEPRECATED | ARCHIVED

## DEFINITION OF DONE (8 criterios)
✓ Código generado | ✓ Tests pasan | ✓ Verifier N0-N5 pasa
✓ BUILD_REGISTRY actualizado | ✓ Estado tarea = COMMITTED
✓ Estado artifact = ACTIVE | ✓ artifact_manifest.json generado
✓ DEPENDENCY_REGISTRY actualizado

## PROJECT_STATUS.md
Control del siguiente paso:
T001 ✅ COMMITTED | T002 ✅ COMMITTED | T003 🚧 EN_PROCESO | T004 ⏳ PENDIENTE
Regla: siguiente paso = primer ⏳ PENDIENTE

## BUILD_REGISTRY.md
Registro inmutable append-only. Nada se borra.

## 5 FASES ANTES DEL CÓDIGO

FASE 0: FUNDACIÓN (ya hecho) — G2 cerrado, Bloques aprobados
FASE 1: BLUEPRINT — ARCHITECTURE.md + BLUEPRINT.md + DEPENDENCY_REGISTRY
FASE 2: BACKLOG — T001-T031 con owner + dependencias
FASE 3: CONTRATOS — artifact_contract.json + artifact_spec.md por tarea
FASE 4: CONSTRUCCIÓN — artifact_code.py + Verifier N0-N5
FASE 5: INTEGRACIÓN — MAXBRY ejecuta + GCL v1.0 gate F4

## REGLAS ABSOLUTAS
✅ código y ficha tienen el MISMO nombre base
✅ artifact_code.py → solo lógica pura
✅ [nombre].meta.md → GPS + pasaporte + contrato
✅ artifact_location_plan.json → plan ruteo automático
✅ bundle ZIP = unidad completa de entrega
❌ NUNCA mezclar código + ubicación
❌ NUNCA mezclar ejecución + sistema
❌ NUNCA guardar rutas dentro del código
❌ NUNCA inferir pasos externos al JSON
