# DOCUMENTO 4 — BLOQUE 4: ESTÁNDARES Y CALIDAD
# VERSION FINAL

## P4-01 — quality_gates.json
Gates mínimos: QG-01 Contrato | QG-02 Schema | QG-03 Tests | QG-04 Verifier N0-N5 | QG-05 Integración | QG-06 Documentación | QG-07 Registro | QG-08 Auditoría
Regla: falla un gate obligatorio = no avanza.

## P4-02 — audit_findings.json
```json
{
  "finding_id": "",
  "severity": "critical|high|medium|low",
  "description": "",
  "component": "",
  "status": "OPEN|IN_PROGRESS|RESOLVED|REJECTED",
  "resolution": ""
}
```

## P4-03 — risk_registry.json
```json
{
  "risk_id": "",
  "description": "",
  "probability": "high|medium|low",
  "impact": "high|medium|low",
  "mitigation": "",
  "owner": ""
}
```

## P4-04 — contract_template.json
```json
{
  "artifact_id": "ART-XXXX",
  "ficha_id": "",
  "version": "1.0",
  "entrypoint": "ejecutar",
  "public_api": ["ejecutar"],
  "artifact_type": "simple|composite",
  "language": "python",
  "runtime_type": "compute|hybrid|llm",
  "llm_ratio_max": 0.10,
  "input_schema": {},
  "output_schema": {},
  "allowed_imports": [],
  "test_cases": [],
  "dependencies": [],
  "failure_modes": [],
  "fallback": "",
  "side_effects": [],
  "idempotente": true,
  "sandbox": "strict|relaxed|none",
  "limits": {"timeout_seg": 30, "memory_mb": 512, "cpu_cores": 1},
  "url_codigo": "object_storage://...",
  "space": "",
  "causa": [],
  "habilita": [],
  "efecto_si_falla": [],
  "sustituible_por": [],
  "schema_version": "1.0"
}
```

## P4-05 — artifact_spec_template.md
Secciones: OBJETIVO | ENTRADAS + EJEMPLO | SALIDAS + ESPERADA | CASOS NORMALES | CASOS BORDE | ERRORES | EJEMPLOS | PERFORMANCE | RESTRICCIONES | DEFINICIÓN DE ÉXITO

Restricciones obligatorias:
- Una sola función pública: ejecutar(input)
- Sin clases
- Sin fases internas
- Sin subpipelines
- Sin estado global
- Determinista

## P4-06 — adr_template.md
Campos: ADR-ID | Título | Fecha | Estado | Contexto | Problema | Opciones | Decisión | Consecuencias | Componentes afectados

## P4-07 — kpi_standard.json
KPIs: KPI-01 build_success_rate | KPI-02 integration_success_rate | KPI-03 test_pass_rate | KPI-04 verifier_pass_rate | KPI-05 rollback_rate | KPI-06 mean_recovery_time | KPI-07 artifact_growth_rate | KPI-08 audit_resolution_rate

## P4-08 — acceptance_protocol.md
Resultado: APPROVED | REJECTED | CONDITIONAL_APPROVAL

## P4-09 — template_completeness_check.md
19 ítems: Constitution | Manifest | Architecture | Blueprint | ADR Registry | Decision Registry | Tasks | Status | Build Registry | Contract Templates | Spec Templates | KPI Standard | Risk Registry | Quality Gates | Acceptance Protocol | Document Authority Map | Dependency Registry | Interface Catalog | Changelog

Si falta alguno → INCOMPLETO → no construir.

## P4-10 — REGLA MAESTRA
VISIÓN → OBJETIVOS → CONSTITUCIÓN → ARQUITECTURA → BLUEPRINT → COMPONENTES → BACKLOG → CONTRATOS → SPECS → VALIDACIÓN → CÓDIGO → INTEGRACIÓN → AUDITORÍA → COMMITTED

PROHIBIDO: VISIÓN → CÓDIGO directamente.

## INTEGRATION TESTS IT01-IT06

### IT01 — TEST LOADER
Verifica: Loader carga artifact correcto desde Storage
Falla si: hash no coincide / artifact no existe

### IT02 — TEST VERIFIER N0-N5
Verifica: pipeline completo N0 a N5
Falla si: cualquier N falla

### IT03 — TEST EXECUTOR
Verifica: Executor invoca Space correctamente
Falla si: timeout / schema mismatch / Space down

### IT04 — TEST RECOVERY
Verifica: sistema se recupera desde fallo
Falla si: estado post-recovery ≠ estado pre-fallo

### IT05 — TEST DAG END-TO-END
Verifica: DAG ejecuta secuencia completa
Falla si: orden incorrecto / artifact skipeado

### IT06 — TEST GCL GATE F4
Verifica: GCL v1.0 bloquea artifacts inválidos
Falla si: artifact inválido pasa el gate

## ESTÁNDAR FICHA — 1 FICHA = 1 FUNCIÓN

### REGLA DE CORTE simple vs composite
- simple: 2-5 pasos relacionados, no reutilizable
- composite: reutilizable, necesita auditoría individual

### PROHIBIDO dentro de ficha
❌ Runtime ❌ Orquestador ❌ DAG ❌ FSM ❌ Cache Manager ❌ Router ❌ Planner ❌ Fases internas
