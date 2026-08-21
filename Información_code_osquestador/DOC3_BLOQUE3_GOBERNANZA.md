# DOCUMENTO 3 — BLOQUE 3: GOBERNANZA (COMPLEMENTOS)
# VERSION FINAL

## P3-01 — project_manifest.json
```json
{
  "project_id": "",
  "project_name": "",
  "project_version": "",
  "architecture_version": "",
  "template_version": "",
  "constitution_version": "",
  "current_phase": "",
  "current_status": "",
  "north_star": "",
  "owner": "",
  "created_at": "",
  "updated_at": ""
}
```
UBICACIÓN: raíz del brain
DIFERENCIA: system_manifest=técnico / project_manifest=identidad global

## P3-02 — CHANGELOG.md
Formato: VERSIÓN | FECHA | AUTOR | CAMBIO | IMPACTO | ADR_RELACIONADO
Regla: Nada puede modificarse sin registro en CHANGELOG.

## P3-03 — decision_registry.json
```json
{
  "decision_id": "",
  "title": "",
  "status": "APPROVED",
  "date": "",
  "owner": "",
  "affected_components": [],
  "adr": ""
}
```

## P3-04 — interface_catalog.json
```json
{
  "interface_id": "",
  "component": "",
  "entrypoint": "",
  "input_schema": "",
  "output_schema": "",
  "version": ""
}
```

## P3-05 — dependency_registry.json
```json
{
  "dependency_id": "",
  "source": "",
  "target": "",
  "type": "hard|soft|runtime|optional",
  "criticality": "high|medium|low"
}
```
UBICACIÓN ÚNICA: memoria/registros/DEPENDENCY_REGISTRY.json

## P3-06 — integration_checklist.md
- □ Contrato válido
- □ Spec válida
- □ Tests pasan
- □ Verifier N0-N5 pasa
- □ Registro actualizado
- □ Interface Catalog actualizado
- □ Dependency Registry actualizado
- □ Build Registry actualizado
- □ artifact_manifest.json generado
- □ Estado = COMMITTED

## P3-07 — release_standard.md
Estados: DRAFT → RC → STABLE → DEPRECATED
Requisitos mínimos: sin errores críticos, todos COMMITTED, Verifier pasa, CHANGELOG actualizado.

## P3-08 — document_authority_map.json
```json
{
  "authority_hierarchy": [
    "constitution","adr","architecture",
    "contracts","schemas","tasks","code"
  ],
  "conflict_rule": "Si dos documentos se contradicen, gana el nivel superior."
}
```

## UBICACIÓN DOCUMENTOS
📂 github.com/[PROYECTO]-brain/A11_documentation/
- project_manifest.json → raíz
- CHANGELOG.md
- decision_registry.json
- interface_catalog.json
- integration_checklist.md
- release_standard.md
- document_authority_map.json
