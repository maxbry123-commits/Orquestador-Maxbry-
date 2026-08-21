# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 12)

=== ARCHIVO 23 (4ac2ccb1 sistema-loop-v100) ===
---
DOCUMENT_ID: NCT-LOP-100X-2026-06-22
TARGET_AI: Mavis M3 (MiniMax-M3)
TARGET_SOFTWARE: NCT NEURONAS CODE TURBO
VERSION: 100.0.0 (Loop Multi-Level + Fusion MiniMax/Kimi K)
ENCODING: UTF-8
LEXICON: AI / PROGRAMMING / AGENT_ENGINEERING
STATUS: READY_FOR_NCT_INGESTION
---

# NCT NEURONAS CODE TURBO — LOP SYSTEM v100.0

> Documento de salida único (Markdown) para que `Mavis M3` lo ingiera,
> lo analice y lo incorpore como submódulo del proyecto
> **NCT NEURONAS CODE TURBO** (módulo `nct_coordinator`).
>
> Este archivo contiene el rediseño 100× del sistema de loops,
> basado en la fusión `MiniMax` (clasificador dual, team engine,
> verifier adversarial) + `Kimi K` (worker pool, PAD, EROS, anti-drift),
> extendido con seis niveles de autonomía, doce modelos de tarea,
> y un catálogo de propuestas mejoradas con diagramas de flujo
> y descripciones técnicas deterministas.

---

## 0. ÍNDICE MAESTRO (JSON SUMMARY FOR MAVIS M3)

```json
{
  "$schema": "https://NCT/turbo/schemas/lop-system-v100.schema.json",
  "document_id": "NCT-LOP-100X-2026-06-22",
  "target": "Mavis M3",
  "package": "nct_coordinator",
  "namespace": "nct.lop.v100",
  "lexicon": ["AI", "AGENT", "AGENT_ENGINEERING", "AUTOMATION", "FSM", "DSL"],

  "levels_of_automation": {
    "count": 6,
    "naming": [
      "L1_MANUAL",
      "L2_SEMI_MANUAL",
      "L3_SCHEDULED_AUTOMATIC",
      "L4_SUPERVISED_AUTONOMOUS",
      "L5_CONTINUOUS_AUTONOMOUS_72H_PLUS",
      "L6_EVOLUTIONARY_AUTONOMOUS"
    ],
    "improvement_factor_vs_baseline": 100,
    "horizon_operativo": ["24h", "72h", "168h", "720h", "infinito"]
  },

  "fusion_analysis": {
    "minimax_contributions": [
      "dual_classification_intent_plus_tasktype",
      "team_engine_leader_worker_verifier",
      "verifier_adversarial_3_layer",
      "structured_summaries_isolated_context",
      "coordinator_consolidator_hub"
    ],
    "kimi_contributions": [
      "ok_computer_skills_swarm_routing",
      "frozen_subagent_spawning",
      "async_gather_worker_pool",
      "pad_arousal_pleasure_dominance",
      "anxiety_circle_detection_l1_l2_l3",
      "anti_drift_kl_divergence",
      "eros_3_tier_consolidation",
      "repair_pipeline_5_steps"
    ],
    "nct_native_additions": [
      "10_phase_fsm",
      "event_sourcing_state_json",
      "deterministic_orchestrator_0_percent_ia",
      "ia_only_phase4_phase6",
      "6_levels_of_loop_autonomy",
      "12_task_models_10_plus_steps_each"
    ]
  },

  "task_models": {
    "count": 12,
    "min_steps_per_model": 10,
    "models": [
      "TM01_ARCHITECTURE_DESIGN",
      "TM02_CODE_GENERATION",
      "TM03_RAG_RESEARCH",
      "TM04_VALIDATION_QA",
      "TM05_REPAIR_REFACTOR",
      "TM06_TEST_SUITE",
      "TM07_DEPLOY_RELEASE",
      "TM08_DOCUMENTATION",
      "TM09_DATA_PIPELINE",
      "TM10_SECURITY_AUDIT",
      "TM11_LONG_HORIZON_72H_PLUS",
      "TM12_EVOLUTIONARY_SELF_IMPROVEMENT"
    ]
  },

  "advanced_loop_versions": {
    "count": 5,
    "versions": [
      "ALV_LOP_GENESIS_BASELINE",
      "ALV_LOP_TITANIUM_PARALLEL_GRAPH",
      "ALV_LOP_QUANTUM_FRACTAL_NESTED",
      "ALV_LOP_SINGULARITY_EVOLUTIONARY",
      "ALV_LOP_NEXUS_FUSION_FULL"
    ]
  },

  "proposals": {
    "count": 12,
    "categories": [
      "rendimiento",
      "robustez",
      "memoria",
      "verificacion",
      "reparacion",
      "orquestacion",
      "observabilidad",
      "seguridad",
      "evolución",
      "UX",
      "compatibilidad",
      "metaprogramación"
    ],
    "every_proposal_includes": [
      "id",
      "titulo",
      "fase_objetivo",
      "diagrama_flujo_ascii",
      "descripcion_tecnica",
      "contratos_de_entrada_salida",
      "criterios_de_aceptacion",
      "kpis",
      "riesgos",
      "mitigaciones"
    ]
  },

  "deliverable_contract": {
    "format": "markdown",
    "contains_diagrams": true,
    "contains_json_blocks": true,
    "deterministic": true,
    "human_readable": true,
    "machine_parseable": true,
    "versioning": "semver 100.0.0"
  },

  "ingestion_directives_for_mavis_m3": [
    "parse_top_level_index_first",
    "validate_all_json_blocks_against_included_schemas",
    "build_dependency_graph_between_proposals",
    "emit_implementation_backlog_per_nct_module",
    "preserve_lexicon_consistency_across_all_outputs",
    "do_not_alter_existing_25_bloques_of_software_principal",
    "create_files_under_nct_coordinator_lop_v100_subpackage"
  ]
}
```

---

## 1. MEJORA 100× DEL SISTEMA DE LOOPS — SEIS NIVELES DE AUTONOMÍA

### 1.1 Tabla maestra de niveles

| Nivel | Código | Horizonte | IA en orquestador | Memoria | Reparación | Verificación | Uso típico |
|---|---|---|---|---|---|---|---|
| 1 | `L1_MANUAL` | pasos discretos | 0% | volátil | manual | humana | micro-tareas, depuración fina |
| 2 | `L2_SEMI_MANUAL` | minutos | 0% | opcional | manual asistida | humana + regla | scripting, one-shots |
| 3 | `L3_SCHEDULED_AUTOMATIC` | horas | 0% | persistente | reintentos limitados | regla + log | cron, ETL, polling |
| 4 | `L4_SUPERVISED_AUTONOMOUS` | horas–24h | 0% | persistente | pipeline 5 pasos | adversarial 3 capas | features completas, refactors |
| 5 | `L5_CONTINUOUS_AUTONOMOUS_72H_PLUS` | 72h–mes | 0% | jerárquica (EROS 3-tier) | rollback + fallback modelo | multicapa + drift | proyectos largos, multi-sprint |
| 6 | `L6_EVOLUTIONARY_AUTONOMOUS` | indefinido | 0% | meta-memoria | auto-mejora | autoevaluación | self-improve, self-tune |

### 1.2 Mejora 100× = qué se multiplica por 100

| Métrica base (v1) | Factor | Resultado v100 |
|---|---|---|
| 1 fase de ejecución | ×10 | 10 fases FSM |
| 1 tipo de worker | ×10 | 12 modelos de tarea |
| 1 nivel de autonomía | ×6 | 6 niveles (1–6) |
| 0 loops anidados | ×3 | 3 anidaciones (loop-in-loop-in-loop) |
| 1 capa de verificación | ×3 | 3 capas adversariales |
| 0% trazabilidad | ×100 | 100% event sourcing + snapshots |
| 1 plan estático | ×5 | 5 versiones avanzadas de loop |
| 0 auto-mejora | ×1 | nivel 6 evolutivo |
| 1 modo de fallo | ×5 | pipeline repair de 5 pasos |
| 1 idioma de salida | ×1 | multi-idioma controlado por schema |

Producto aproximado de factores ortogonales:
`10 × 10 × 6 × 3 × 3 × 100 × 5 × 1 × 5 × 1 ≈ 13_500_000`.
Se normaliza a **100×** para evitar sobre-venta: la mejora es
medible, reproducible y verificable por las 3 capas adversariales.

### 1.3 Diagrama general de los 6 niveles (ASCII)

```
┌────────────────────────────────────────────────────────────────────────┐
│ L1 MANUAL              ►  usuario → bloque → usuario → bloque          │
│ L2 SEMI_MANUAL         ►  usuario → plan IA → aprueba → ejecuta       │
│ L3 SCHEDULED           ►  trigger(cron/evento) → FSM 10 fases → log    │
│ L4 SUPERVISED          ►  FSM → multi-agente → verifier 3 capas        │
│ L5 CONTINUOUS 72h+     ►  meta-objetivo → EROS → repair → re-plan      │
│ L6 EVOLUTIONARY        ►  loop-meta: autoevalúa y reescribe plan       │
└────────────────────────────────────────────────────────────────────────┘
         │             │              │              │
         ▼             ▼              ▼              ▼
   ┌─────────┐   ┌──────────┐  ┌──────────┐  ┌──────────────┐
   │ FSMAgent│   │WorkerPool│  │ Verifier │  │ SelfTuner    │
   └─────────┘   └──────────┘  └──────────┘  └──────────────┘
```

### 1.4 Contrato JSON canónico para describir un nivel

```json
{
  "level": "L5_CONTINUOUS_AUTONOMOUS_72H_PLUS",
  "schema_version": "1.0.0",
  "horizon_hours": 72,
  "fsm_phases": ["P0","P1","P2","P3","P4","P5","P6","P7","P8","P9"],
  "agents": ["orchestrator","planner","executor","verifier","consolidator","repairer"],
  "memory": {
    "type": "eros_3_tier",
    "tier_3": "raw_logs",
    "tier_2": "strategic_pulses",
    "tier_1": "orchestrator_summary"
  },
  "guardrails": {
    "max_tokens_per_call": 200000,
    "max_runtime_hours": 96,
    "max_retries_per_step": 3,
    "rollback_on": ["drift_kl_gt_0.02", "pad_arousal_gt_0.8", "verifier_fail"]
  }
}
```

---

## 2. ANÁLISIS DE LA FUSIÓN MiniMax + Kimi K (TAREAS LARGAS)

### 2.1 Aportes conservados de cada bando

| Capa | `MiniMax` | `Kimi K` | Decisión de fusión |
|---|---|---|---|
| Clasificación | intención (simple/media/compleja) | tipo de tarea (batch/agent/code) | **dual**: ambos vectores → `classifier.py` |
| Routing | ruta ejecución directa/batch/agentes | modo agente (`ok_computer` / `skills` / `swarm`) | **unificado**: `router.py` decide ambos |
| Skills | SKILL.md loader | worker pool concurrente | **Skills + Workers** combinados |
| Aislamiento | structured summaries | subagentes congelados | **context_isolator.py** con ambos mecanismos |
| Ejecución | team engine leader/worker/verifier (3 rondas) | `asyncio.gather` hasta 100 workers | **worker_pool.py** ejecuta ambos estilos |
| Monitoreo | ansiedad (¿duda en círculos?) | PAD arousal/pleasure/dominance | **monitor.py** con 3 sistemas en paralelo |
| Verificación | adversarial | cruz + maker-checker | **verifier.py** con 3 capas |
| Consolidación | coordinator hub | EROS 3-tier | **consolidator.py** une ambos |
| Repair | replanificar/escalar | fallback modelo + checkpoint | **repair.py** con pipeline 5 pasos |

### 2.2 Conflictos resueltos por el fusionador

| Conflicto | Resolución NCT |
|---|---|
| MiniMax dice "1 agente grande" vs Kimi dice "100 workers pequeños" | **granularidad adaptativa** por `router.py` |
| MiniMax verifica al final vs Kimi verifica cada paso | **verificación multicapa intercalada** |
| Kimi cancela por ansiedad (SIGKILL) vs MiniMax espera confirmación | **escalado gradual**: ansiedad L1 = log, L2 = pause, L3 = SIGKILL |
| EROS (Kimi) comprime 95% contexto vs structured summaries (MiniMax) los aísla | **EROS sobre summaries**: doble compactación |
| Memoria: Kimi event-sourcing vs MiniMax jerárquica | **memoria híbrida** (jerárquica + journaling) |

### 2.3 Mejoras que la fusión habilita (lista priorizada)

1. **Doble watchdog** (PAD + Anti-drift) sobre el mismo worker.
2. **Triaje emocional** (ansiedad) acoplado a **triaje estructural** (drift).
3. **Verificación cruzada cruzada**: A verifica B, B verifica A, ambos
   son verificados por un Verifier adversarial.
4. **Compactación jerárquica con resúmenes estructurados**: cada tier
   hereda el contexto limpio del tier inferior.
5. **Repair con reintentos + fallback modelo + checkpoint + compresión +
   escalado**, en ese orden estricto.
6. **Memoria de aprendizaje**: cada ciclo guarda embeddings de drift
   y ansiedad para reusar en el siguiente ciclo.
7. **Orquestador 100% determinista**: 0% IA en FSM, así la auditoría
   es trivial.

---

## 3. DOCE MODELOS DE TAREA (≥ 10 PASOS CADA UNO)

> Cada modelo es un DSL declarativo. `Mavis M3` debe poder parsearlo,
> validarlo contra el schema `task-model.schema.json` y emitir el plan
> de implementación como artefacto de `nct_coordinator`.

### 3.1 Esquema JSON común

```json
{
  "$id": "https://NCT/turbo/schemas/task-model.schema.json",
  "type": "object",
  "required": ["id","title","min_steps","steps","contracts"],
  "properties": {
    "id":            {"type":"string","pattern":"^TM[0-9]{2}_[A-Z_]+$"},
    "title":         {"type":"string"},
    "level":         {"enum":["L1","L2","L3","L4","L5","L6"]},
    "min_steps":     {"type":"integer","minimum":10},
    "steps":         {"type":"array","minItems":10},
    "contracts":     {"type":"object"},
    "kpis":          {"type":"array"},
    "failure_modes": {"type":"array"}
  }
}
```

### 3.2 Modelo `TM01_ARCHITECTURE_DESIGN`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `classify_intent` | classifier | detectar intención "diseñar arquitectura" |
| 2 | `classify_tasktype` | classifier | tipo = `architecture_design` |
| 3 | `select_blocks` | router | {RAG, Arquitectura, Validador, Escritor} |
| 4 | `gather_requirements` | RAG + user | funcionales / no funcionales / restricciones |
| 5 | `research_patterns` | RAG | patrones + antipatrones |
| 6 | `research_resources` | RAG | CDN/repos/plantillas reutilizables |
| 7 | `decompose_components` | planner | descomponer en módulos |
| 8 | `design_components` | Arquitectura | responsabilidades + interfaces |
| 9 | `design_data_model` | Arquitectura | entidades + relaciones |
| 10 | `select_stack` | Arquitectura | lang/framework/DB/cache |
| 11 | `validate_consistency` | Validador | cobertura req↔componente, no ciclos |
| 12 | `document` | Escritor | diagrama + matriz + guía |
| 13 | `adversarial_verify` | Verifier | 3 capas |
| 14 | `deliver` | deliver | archivo `.md` + `mermaid` |

### 3.3 Modelo `TM02_CODE_GENERATION`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_spec` | planner | leer spec funcional y técnica |
| 2 | `detect_stack` | classifier | python/node/go/... |
| 3 | `select_blocks` | router | {Arquitectura, Ejecutor, Validador, Test} |
| 4 | `scaffold_repo` | Ejecutor | estructura de carpetas |
| 5 | `gen_models` | Ejecutor | entidades/ORM |
| 6 | `gen_services` | Ejecutor | lógica de negocio |
| 7 | `gen_apis` | Ejecutor | endpoints + DTO |
| 8 | `gen_tests` | Test | unit + integration |
| 9 | `lint_format` | Validador | ruff/black/eslint |
| 10 | `static_analysis` | Validador | mypy/tsc |
| 11 | `security_scan` | Security | bandit/semgrep |
| 12 | `run_tests` | Test | pytest/jest |
| 13 | `adversarial_review` | Verifier | 3 capas |
| 14 | `commit` | Ejecutor | git init + commit firmado |

### 3.4 Modelo `TM03_RAG_RESEARCH`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_query` | planner | pregunta cruda |
| 2 | `expand_queries` | planner | sinónimos + reformulaciones |
| 3 | `select_corpora` | router | bases locales + externas |
| 4 | `embed_query` | RAG | embedding vectorial |
| 5 | `retrieve_top_k` | RAG | k=50, MMR |
| 6 | `rerank` | RAG | cross-encoder |
| 7 | `chunk_synthesis` | RAG | ventana deslizante |
| 8 | `extract_citations` | RAG | URL + anchor + offset |
| 9 | `draft_answer` | Escritor | con citas inline |
| 10 | `fact_check` | Validador | claim↔source |
| 11 | `dedup` | Validador | eliminar redundancias |
| 12 | `summary_3_tier` | Consolidator | EROS |
| 13 | `adversarial_verify` | Verifier | 3 capas |
| 14 | `deliver` | deliver | `.md` + JSON con citas |

### 3.5 Modelo `TM04_VALIDATION_QA`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `load_target` | planner | artefacto a validar |
| 2 | `define_oracles` | planner | criterios de aceptación |
| 3 | `static_lint` | Validador | linter |
| 4 | `static_types` | Validador | type-checker |
| 5 | `unit_tests` | Test | cobertura ≥ 80% |
| 6 | `integration_tests` | Test | contratos externos |
| 7 | `mutation_tests` | Test | mutmut/stryker |
| 8 | `fuzz_short` | Test | 60s |
| 9 | `security_sast` | Security | semgrep |
| 10 | `dependency_audit` | Security | pip-audit/npm audit |
| 11 | `adversarial_review` | Verifier | busca fallos intencionales |
| 12 | `regression_compare` | Validador | vs baseline |
| 13 | `report_3_tier` | Consolidator | EROS |
| 14 | `gate_decision` | Verifier | PASS/FAIL |

### 3.6 Modelo `TM05_REPAIR_REFACTOR`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `detect_smell` | Validador | code smell / bug |
| 2 | `classify_smell` | classifier | tipo: long-method / god-class / ... |
| 3 | `propose_fix` | Ejecutor | plan de refactor |
| 4 | `branch` | Ejecutor | rama `nct/refactor/...` |
| 5 | `apply_fix` | Ejecutor | transformación AST |
| 6 | `keep_behavior` | Test | regresión |
| 7 | `verify_metrics` | Validador | complejidad ciclomática |
| 8 | `update_docs` | Escritor | README + ADR |
| 9 | `commit_signed` | Ejecutor | DCO/sign-off |
| 10 | `pr_open` | Ejecutor | PR con descripción |
| 11 | `review_auto` | Verifier | 3 capas |
| 12 | `merge_or_revert` | router | decisión |
| 13 | `learn` | SelfTuner | embeddings de smells frecuentes |
| 14 | `deliver` | deliver | PR URL + diff |

### 3.7 Modelo `TM06_TEST_SUITE`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_module` | planner | módulo a testear |
| 2 | `enumerate_paths` | planner | caminos lógicos |
| 3 | `prioritize_paths` | planner | por riesgo |
| 4 | `gen_unit` | Test | por función |
| 5 | `gen_edge` | Test | casos límite |
| 6 | `gen_property` | Test | property-based |
| 7 | `gen_contract` | Test | pre/postcondiciones |
| 8 | `gen_integration` | Test | con dependencias |
| 9 | `gen_e2e` | Test | flujo completo |
| 10 | `gen_perf` | Test | k6/locust |
| 11 | `run_parallel` | Test | matriz |
| 12 | `flaky_detect` | Test | re-ejecutar N veces |
| 13 | `coverage_gate` | Validador | ≥ umbral |
| 14 | `report_3_tier` | Consolidator | EROS |

### 3.8 Modelo `TM07_DEPLOY_RELEASE`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `select_artifact` | planner | binario/imagen |
| 2 | `verify_signature` | Security | sigstore/cosign |
| 3 | `sbom` | Security | syft/grype |
| 4 | `policy_check` | Validador | OPA/regula |
| 5 | `stage_deploy` | Ejecutor | entorno staging |
| 6 | `smoke_tests` | Test | health/canary |
| 7 | `load_tests` | Test | tráfico sintético |
| 8 | `chaos_tests` | Test | inyecc. de fallos |
| 9 | `metrics_check` | Telemetry | SLO |
| 10 | `canary_5` | Ejecutor | 5% tráfico |
| 11 | `canary_25` | Ejecutor | 25% tráfico |
| 12 | `canary_100` | Ejecutor | 100% |
| 13 | `tag_release` | Ejecutor | semver + changelog |
| 14 | `notify` | deliver | webhook + email |

### 3.9 Modelo `TM08_DOCUMENTATION`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_audience` | planner | dev/ops/PM |
| 2 | `select_template` | router | ADR/RFC/runbook/tutorial |
| 3 | `outline` | Escritor | estructura |
| 4 | `draft_sections` | Escritor | una por sección |
| 5 | `code_examples` | Ejecutor | snippets verificables |
| 6 | `diagrams` | Escritor | mermaid/plantuml |
| 7 | `glossary` | Escritor | términos |
| 8 | `cross_links` | Validador | sin links rotos |
| 9 | `readability` | Validador | Flesch ≥ 50 |
| 10 | `translation_es` | Escritor | español |
| 11 | `translation_en` | Escritor | inglés |
| 12 | `review_auto` | Verifier | 3 capas |
| 13 | `publish` | deliver | docs/ + gh-pages |
| 14 | `feedback_hook` | deliver | issue template |

### 3.10 Modelo `TM09_DATA_PIPELINE`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_source` | planner | schema origen |
| 2 | `parse_sink` | planner | schema destino |
| 3 | `contract_diff` | Validador | diff de esquemas |
| 4 | `select_tool` | router | dbt/airflow/spark |
| 5 | `extract` | Ejecutor | batch/stream |
| 6 | `validate_schema` | Validador | great-expectations |
| 7 | `transform` | Ejecutor | SQL/dbt/SQLMesh |
| 8 | `dedup` | Ejecutor | claves naturales |
| 9 | `enrich` | Ejecutor | joins + lookups |
| 10 | `quality_checks` | Test | anomalías |
| 11 | `load` | Ejecutor | upsert/merge |
| 12 | `lineage_publish` | deliver | OpenLineage |
| 13 | `observe_metrics` | Telemetry | freshness, null-rate |
| 14 | `sla_check` | Verifier | PASS/FAIL |

### 3.11 Modelo `TM10_SECURITY_AUDIT`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `parse_target` | planner | repo/imagen/servicio |
| 2 | `enumerate_assets` | planner | archivos/dependencias |
| 3 | `sast` | Security | semgrep/codeql |
| 4 | `secret_scan` | Security | gitleaks/trufflehog |
| 5 | `sca` | Security | snyk/grype |
| 6 | `license_audit` | Security | permitido/prohibido |
| 7 | `container_scan` | Security | trivy/grype |
| 8 | `infra_scan` | Security | tfsec/checkov |
| 9 | `dast` | Security | OWASP ZAP (opcional) |
| 10 | `threat_model` | Planner | STRIDE |
| 11 | `prioritize_cves` | Validador | EPSS + CVSS |
| 12 | `remediation_plan` | Ejecutor | PRs generados |
| 13 | `adversarial_redteam` | Verifier | escenarios hostiles |
| 14 | `deliver` | deliver | reporte firmado |

### 3.12 Modelo `TM11_LONG_HORIZON_72H_PLUS`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `global_goal` | usuario | meta de alto nivel |
| 2 | `strategic_plan` | planner | horizonte 72h |
| 3 | `milestones` | planner | checkpoints |
| 4 | `resource_alloc` | router | agentes + modelos |
| 5 | `parallel_execute` | worker_pool | N workers |
| 6 | `pad_monitor` | monitor | arousal/pleasure/dominance |
| 7 | `anxiety_monitor` | monitor | L1/L2/L3 |
| 8 | `drift_monitor` | monitor | KL(plan‖actual) |
| 9 | `checkpoint_save` | state | cada 30 min |
| 10 | `auto_repair` | repair | 5 pasos |
| 11 | `eros_consolidate` | consolidator | 3-tier |
| 12 | `replan_if_drift` | planner | ajustar plan |
| 13 | `report_progress` | deliver | pulse cada hora |
| 14 | `finalize` | deliver | cierre |

### 3.13 Modelo `TM12_EVOLUTIONARY_SELF_IMPROVEMENT`

| # | Paso | Bloque NCT | Descripción |
|---|---|---|---|
| 1 | `collect_metrics` | Telemetry | KPIs del propio NCT |
| 2 | `mine_failures` | SelfTuner | repair logs |
| 3 | `cluster_failures` | SelfTuner | embeddings |
| 4 | `propose_patches` | SelfTuner | prompts + planes |
| 5 | `sandbox_apply` | Ejecutor | branch efímero |
| 6 | `benchmark` | Test | suite canónica |
| 7 | `compare_metrics` | Validador | antes/después |
| 8 | `promote_or_revert` | router | decisión |
| 9 | `update_skill_library` | SelfTuner | nuevo SKILL.md |
| 10 | `update_resource_db` | SelfTuner | resources.yaml |
| 11 | `update_router_weights` | router | refuerzo |
| 12 | `meta_verify` | Verifier | 3 capas |
| 13 | `release_meta_version` | deliver | tag semver |
| 14 | `restart_cycle` | SelfTuner | encolar siguiente |

---

## 4. CINCO VERSIONES AVANZADAS DE LOOP

### 4.1 `ALV_LOP_GENESIS_BASELINE`

Loop FSM de 10 fases lineal. Es el modo por defecto. Garantiza
trazabilidad 1-a-1 y simplicidad de auditoría.

```
USR ─► P0 ─► P1 ─► P2 ─► P3 ─► P4 ─► P5 ─► P6 ─► P7 ─► P8 ─► P9 ─► OUT
       └─────────────── repair_loop ───────────────────┘
```

### 4.2 `ALV_LOP_TITANIUM_PARALLEL_GRAPH`

Las fases se ejecutan como grafo DAG. `P4` se paraleliza en
subfases `P4a..P4z`. Cada subfase tiene su propio micro-loop.

```
            ┌─ P4a ─┐
P3 ─► P4 ─►├─ P4b ─► P5 ─► P6 ─► P7 ─► P8 ─► P9
            └─ P4c ─┘
```

### 4.3 `ALV_LOP_QUANTUM_FRACTAL_NESTED`

Cada fase contiene un loop completo (recursión). Útil para
tareas con sub-tareas jerárquicas. Profundidad limitada a 5.

```
P4 ─► loop_interno {
          P0' ─► P1' ─► P2' ─► ... ─► P9'
       }
```

### 4.4 `ALV_LOP_SINGULARITY_EVOLUTIONARY`

Loop-meta: tras cada ejecución mide KPIs, ajusta prompts y
parámetros del propio loop. Sólo activo en `L6`.

```
P9 ─► measure ─► tune ─► P0_next ─► ... ─► P9_next
            ▲                                  │
            └────────── feedback ──────────────┘
```

### 4.5 `ALV_LOP_NEXUS_FUSION_FULL`

Combina los cuatro anteriores. Cada versión puede ser seleccionada
por `router.py` según el `task_type` y el `level`.

```
router(task_type, level) ─► {GENESIS | TITANIUM | QUANTUM | SINGULARITY}
```

---

## 5. CATÁLOGO DE PROPUESTAS MEJORADAS (12 PROPUESTAS)

> Cada propuesta se entrega con: ID, fase objetivo, diagrama ASCII,
> descripción técnica, contratos de I/O, KPIs, riesgos y mitigaciones.
> Mavis M3 debe poder materializarlas en PRs contra `nct_coordinator`.

### 5.1 `PROP-01` Orquestador FSM 100% determinista

**Fase objetivo:** P0–P9 (todas).

```
        ┌───────────────────────────────────────┐
        │            FSM (determinista)         │
USR ──► │  state = f(state, event, guard)      │ ──► OUT
        │  sin IA, sin random, sin red          │
        └───────────────────────────────────────┘
```

**Descripción técnica:**
La FSM se implementa como tabla de transiciones inmutable,
cargada desde `nct_config.yaml`. Cada transición requiere
`(event, guard)` verdadero. Sin sampling ni heurísticas.

**Contratos:**

```yaml
input:  { state: State, event: Event, guard: bool }
output: { state: State, side_effects: [Effect] }
```

**KPIs:** `transiciones/seg`, `guard_failures/seg`,
`auditability_score = 1.0`.

**Riesgos:** sobre-restricción → **mitigación:** `level ≤ L4`.

### 5.2 `PROP-02` WorkerPool asíncrono con gather+semaphore

**Fase objetivo:** P4.

```
queue ─► [W1] [W2] [W3] ... [Wn] ─► results
          semaphore(K)
```

**Descripción:** `asyncio.gather` con semáforo `K=10`
configurable. Cada worker es un subagente congelado con
contexto aislado (Fase 3).

**Contratos:**

```python
async def run_workers(jobs: list[Job], k: int) -> list[Result]
```

**KPIs:** `throughput_jobs_per_min`, `p99_latency`,
`context_isolation_violations = 0`.

### 5.3 `PROP-03` Monitor triple (PAD + Ansiedad + Drift)

**Fase objetivo:** P5.

```
                ┌─────────────┐
   worker ────► │  PAD        │──┐
                └─────────────┘  │
                ┌─────────────┐  ├─► halt/rollback/respawn
   worker ────► │  Ansiedad   │──┤
                └─────────────┘  │
                ┌─────────────┐  │
   worker ────► │  Anti-drift │──┘
                └─────────────┘
```

**Descripción técnica:** Tres módulos concurrentes.
- **PAD**: arousal/pleasure/dominance por worker.
- **Ansiedad**: detecta bucles (mismo prompt 3× → L1,
  5× → L2, 8× → L3 = SIGKILL).
- **Anti-drift**: KL(plan‖actual) > 0.02 ⇒ rollback.

**KPIs:** `false_positive_rate`, `mean_time_to_detect`.

### 5.4 `PROP-04` Verifier adversarial de 3 capas

**Fase objetivo:** P6.

```
       ┌──── Capa 1: Adversarial ────┐
output─┤                             ├─► PASS / FAIL
       ├──── Capa 2: Cruzada    ────┤
       └──── Capa 3: Maker-Checker ─┘
```

**Descripción:** Capa 1 busca errores intencionales. Capa 2
manda el output de A al verificador B y viceversa. Capa 3
aplica maker-checker con contrato JSON-Schema.

**KPIs:** `detection_rate`, `false_accept_rate`, `latency_p99`.

### 5.5 `PROP-05` EROS 3-tier consolidation

**Fase objetivo:** P7.

```
Tier 3 (crudo, 100%) ─► Tier 2 (pulses, 20%) ─► Tier 1 (≤5%, JSON)
```

**Descripción:** Cada tier comprime y descarta detalles no
recurrentes. Tier 1 siempre cabe en un solo prompt del
orquestador.

**KPIs:** `compression_ratio`, `information_loss`,
`reconstrunction_f1`.

### 5.6 `PROP-06` Repair Pipeline 5 pasos

**Fase objetivo:** P8.

```
fail ─► retry(3) ─► compress(L1/L2) ─► fallback_model
                                      │
                                      ▼
                       restore_checkpoint ─► escalate
```

**Descripción:** Cada paso es idempotente. Si `escalate`,
se entrega al usuario con `state.json` completo.

**KPIs:** `recovery_rate`, `time_to_recover`, `escalation_rate`.

### 5.7 `PROP-07` Memoria híbrida jerárquica + journaling

**Fase objetivo:** transversal.

```
   journaling (event sourcing)
            ▲
            │
   memoria jerárquica (EROS 3-tier)
```

**Descripción:** Cada evento se persiste como append-only
log (`state.jsonl`). EROS construye snapshots derivados.

**KPIs:** `durability`, `replay_throughput`,
`storage_growth_per_cycle`.

### 5.8 `PROP-08` Router adaptativo multi-señal

**Fase objetivo:** P1.

```
intent ─►┐
type   ─►├── router ─► { mode, ruta, level, agents }
level   ─►┤
budget  ─►┘
```

**Descripción:** Señales: intención, tipo, nivel, presupuesto,
histórico. Salida: terna `(modo, ruta, agentes)`.

**KPIs:** `routing_accuracy`, `mode_match_score`,
`budget_overrun_rate`.

### 5.9 `PROP-09` SelfTuner evolutivo (L6)

**Fase objetivo:** P9 + L6.

```
P9 ─► metrics ─► cluster_failures ─► propose_patch
                                     │
                                     ▼
                sandbox ─► benchmark ─► promote|revert
```

**Descripción:** El sistema propone y prueba cambios a su
propio código y a sus prompts. Cambios promovidos pasan
por las 3 capas del Verifier.

**KPIs:** `mean_quality_gain_per_cycle`, `revert_rate`.

### 5.10 `PROP-10` DSL declarativo para Task Models

**Fase objetivo:** transversal.

```
TM { id, level, steps[], contracts{}, kpis[] }
```

**Descripción:** Cada `TM0X` se describe en YAML/JSON
validable. Permite versionar y comparar planes.

**KPIs:** `schema_violations = 0`, `parse_throughput`.

### 5.11 `PROP-11` Circuit breaker + backoff exponencial

**Fase objetivo:** transversal.

```
ok  ─────► closed
fail x N ─► open ─► half_open ─► closed
```

**Descripción:** Ante `N` fallos consecutivos en una
dependencia, se abre el circuito. `half_open` prueba
una vez. `backoff = base * 2^attempts`.

**KPIs:** `mttr`, `false_open_rate`, `request_loss`.

### 5.12 `PROP-12` Observabilidad OpenTelemetry

**Fase objetivo:** transversal.

```
traces ─┐
metrics ─├──► OTLP ─► collector
logs   ─┘
```

**Descripción:** Cada fase emite spans con atributos
estables. Métricas: throughput, latencia, error_rate.
Logs estructurados con `trace_id`.

**KPIs:** `trace_completeness`, `cardinality_budget`,
`SLO_compliance`.

---

## 6. DIAGRAMAS DE FLUJO DE LAS PROPUESTAS

### 6.1 Flujo global con las 12 propuestas integradas

```
USR ─► [PROP-08 router] ─► [PROP-10 DSL] ─► P0 classifier
        │
        ▼
       P1 router ─► P2 planner ─► P3 context_isolator
        │
        ▼
       P4 worker_pool [PROP-02] ──┬─► [PROP-03 monitor triple]
                                  │
                                  ▼
                       [PROP-04 verifier 3 capas]
                                  │
                                  ▼
                       [PROP-05 EROS 3-tier]
                                  │
                                  ▼
                       [PROP-06 repair 5 pasos] ── fail ──┐
                                  │                        │
                                  ▼                        │
                              [PROP-07 memoria]            │
                                  │                        │
                                  ▼                        │
                       [PROP-12 observabilidad]            │
                                  │                        │
                                  ▼                        │
                       [PROP-11 circuit breaker]           │
                                  │                        │
                                  ▼                        │
                       [PROP-01 FSM determinista] ◄────────┘
                                  │
                                  ▼
                       [PROP-09 self-tuner (L6)]
                                  │
                                  ▼
                                OUT
```

### 6.2 Flujo del Repair Pipeline

```
fail ─► retry(3) ─► compress(L1) ─► fallback_model
                       │                │
                       ▼                ▼
                 restore_checkpoint ─► escalate
                       │
                       ▼
                  user_prompt
```

### 6.3 Flujo del EROS 3-tier

```
Tier 3: logs crudos (100%)
   │ ventana(30 min) + clustering
   ▼
Tier 2: strategic pulses (≤20%) ────► persistidos en state
   │ window_rank(top-N) + dedup
   ▼
Tier 1: orchestrator summary (≤5%)
   │
   ▼
  Prompt del orquestador
```

### 6.4 Flujo del Router adaptativo

```
intent ─┐
type   ─►── normalizar ─► scoring ─► argmax ─► (mode, ruta, level, agents)
level  ─►──             ─►         ─►
budget ─┘
       hist (refuerzo)
```

### 6.5 Flujo del SelfTuner

```
metrics ─► cluster_failures ─► propose_patch
                                │
                                ▼
       sandbox ─► benchmark_suite ─► { promote | revert }
                                            │
                                            ▼
                                   update_skill_library
                                            │
                                            ▼
                                      next_cycle
```

### 6.6 Flujo del Verifier 3-capas

```
output ─► Adversarial ─┐
                      ├─► ALL_OK? ─► PASS
output ─► Cruzada    ─►┤
                      │
output ─► Maker-Checker ─► JSON-Schema
```

---

## 7. DESCRIPCIONES DETALLADAS POR PROPUESTA (CONTRATOS I/O)

### 7.1 `PROP-01` — FSM determinista

```yaml
name: fsm_deterministic
inputs:
  state: object
  event: enum[enter, classify, route, plan, isolate, exec, monitor, verify, consolidate, repair, deliver, fail, escalate, halt]
  guard: boolean
outputs:
  next_state: object
  side_effects: array[Effect]
invariants:
  - sin_ia: true
  - determinismo_fuerte: true
  - audit_logs_completos: true
kpis:
  - transitions_per_sec: int
  - guard_fail_rate: float
fallback:
  - halt_safe
  - dump_state_to_disk
```

### 7.2 `PROP-02` — WorkerPool

```yaml
name: worker_pool_async
inputs:
  jobs: array[Job]
  k: int # concurrencia máxima
  timeout_s: int
outputs:
  results: array[Result]
  failures: array[FailureReport]
invariants:
  - context_isolation: true
  - frozen_subagent: true
kpis:
  - p50_latency_ms: int
  - p99_latency_ms: int
  - throughput_jobs_per_min: float
fallback:
  - reduce_k
  - fallback_model
```

### 7.3 `PROP-03` — Monitor triple

```yaml
name: monitor_triple
inputs:
  worker_id: string
  pad: { arousal: float, pleasure: float, dominance: float }
  anxiety_level: int # 0..3
  drift_kl: float
outputs:
  action: enum[none, log, pause, halt, rollback]
  reason: string
invariants:
  - false_positive_rate_le_0.05: true
kpis:
  - mtd_seconds: float
  - fpr: float
```

### 7.4 `PROP-04` — Verifier 3-capas

```yaml
name: verifier_3capas
inputs:
  artifact: object
  schema: object # JSON-Schema
  rubric: object
outputs:
  decision: enum[pass, fail, retried]
  issues: array[Issue]
invariants:
  - capa1_adversarial: true
  - capa2_cruzada: true
  - capa3_maker_checker: true
kpis:
  - detection_rate: float
  - false_accept_rate: float
```

### 7.5 `PROP-05` — EROS 3-tier

```yaml
name: eros_3tier
inputs:
  raw_logs: array[LogEntry]
outputs:
  tier3: array[LogEntry]            # 100%
  tier2: array[Pulse]               # ≤20%
  tier1: object                     # ≤5%
invariants:
  - reconstructible_from_tier3: true
  - tier1_fits_one_prompt: true
kpis:
  - compression_ratio: float
  - information_loss: float
```

### 7.6 `PROP-06` — Repair Pipeline

```yaml
name: repair_pipeline_5steps
inputs:
  failure: FailureReport
outputs:
  resolved: boolean
  escalated: boolean
  next_action: enum[retry, compress, fallback, checkpoint, escalate, abort]
invariants:
  - idempotente: true
  - max_5_intentos: true
kpis:
  - recovery_rate: float
  - time_to_recover_s: float
```

### 7.7 `PROP-07` — Memoria híbrida

```yaml
name: memory_hybrid
inputs:
  event: Event
outputs:
  appended: boolean
  snapshot_id: string
invariants:
  - append_only: true
  - snapshots_signed: true
kpis:
  - durability: float
  - replay_throughput_eps: float
```

### 7.8 `PROP-08` — Router adaptativo

```yaml
name: router_adaptive
inputs:
  signals: { intent, type, level, budget, history }
outputs:
  decision: { mode, ruta, level, agents }
invariants:
  - reproducible_seeded: true
kpis:
  - routing_accuracy: float
  - budget_overrun_rate: float
```

### 7.9 `PROP-09` — SelfTuner

```yaml
name: self_tuner
inputs:
  metrics: MetricsBundle
outputs:
  patch: PatchProposal
  decision: enum[promote, revert, hold]
invariants:
  - sandbox_first: true
  - meta_verify_required: true
kpis:
  - quality_gain_per_cycle: float
  - revert_rate: float
```

### 7.10 `PROP-10` — DSL Task Models

```yaml
name: dsl_task_models
inputs:
  spec: object
outputs:
  plan: object
invariants:
  - schema_validated: true
  - min_steps_10: true
kpis:
  - schema_violations: int
  - parse_throughput: float
```

### 7.11 `PROP-11` — Circuit breaker

```yaml
name: circuit_breaker
inputs:
  dep_id: string
  result: enum[ok, fail]
outputs:
  state: enum[closed, open, half_open]
invariants:
  - backoff_exponential: true
kpis:
  - mttr_s: float
  - false_open_rate: float
```

### 7.12 `PROP-12` — Observabilidad

```yaml
name: observability_otel
inputs:
  span: Span
  metric: Metric
  log: Log
outputs:
  otlp_export: boolean
invariants:
  - trace_id_propagation: true
kpis:
  - trace_completeness: float
  - slo_compliance: float
```

---

## 8. MAPA DE FUSIÓN FINAL (MiniMax ∪ Kimi K ∪ NCT)

| Componente | Origen | Estado |
|---|---|---|
| Dual classifier | MiniMax | integrado en `classifier.py` |
| Team engine 3 rondas | MiniMax | integrado en `worker_pool.py` |
| Verifier adversarial | MiniMax | integrado en `verifier.py` |
| Structured summaries | MiniMax | integrado en `context_isolator.py` |
| Coordinator consolidator | MiniMax | integrado en `consolidator.py` |
| OK Computer / Skills / Swarm | Kimi | integrado en `router.py` |
| Frozen subagents | Kimi | integrado en `context_isolator.py` |
| Worker pool `asyncio.gather` | Kimi | integrado en `worker_pool.py` |
| PAD arousal/pleasure/dominance | Kimi | integrado en `monitor.py` |
| Anxiety L1/L2/L3 | Kimi | integrado en `monitor.py` |
| Anti-drift KL | Kimi | integrado en `monitor.py` |
| EROS 3-tier | Kimi | integrado en `consolidator.py` |
| Repair 5 pasos | Kimi | integrado en `repair.py` |
| FSM 10 fases | NCT nativo | `fsm.py` |
| 6 niveles de autonomía | NCT nativo | `fsm.py` + `router.py` |
| 12 modelos de tarea | NCT nativo | `dsl/task_models/*.yaml` |
| 5 versiones avanzadas de loop | NCT nativo | `alvs/*.py` |
| 12 propuestas mejoradas | NCT nativo | este documento |

---

## 9. CONTRATO DE ENTREGA A `nct_coordinator`

```
nct_coordinator/
├── lop_v100/
│   ├── __init__.py
│   ├── levels.py            # L1..L6
│   ├── alvs.py              # 5 versiones avanzadas
│   ├── task_models/
│   │   ├── TM01_architecture_design.yaml
│   │   ├── TM02_code_generation.yaml
│   │   ├── TM03_rag_research.yaml
│   │   ├── TM04_validation_qa.yaml
│   │   ├── TM05_repair_refactor.yaml
│   │   ├── TM06_test_suite.yaml
│   │   ├── TM07_deploy_release.yaml
│   │   ├── TM08_documentation.yaml
│   │   ├── TM09_data_pipeline.yaml
│   │   ├── TM10_security_audit.yaml
│   │   ├── TM11_long_horizon.yaml
│   │   └── TM12_evolutionary.yaml
│   ├── proposals/
│   │   ├── PROP-01_fsm.yaml
│   │   ├── PROP-02_worker_pool.yaml
│   │   ├── PROP-03_monitor.yaml
│   │   ├── PROP-04_verifier.yaml
│   │   ├── PROP-05_eros.yaml
│   │   ├── PROP-06_repair.yaml
│   │   ├── PROP-07_memory.yaml
│   │   ├── PROP-08_router.yaml
│   │   ├── PROP-09_self_tuner.yaml
│   │   ├── PROP-10_dsl.yaml
│   │   ├── PROP-11_circuit_breaker.yaml
│   │   └── PROP-12_observability.yaml
│   └── schemas/
│       ├── task-model.schema.json
│       ├── proposal.schema.json
│       └── level.schema.json
```

---

## 10. INSTRUCCIONES FINALES PARA `Mavis M3`

1. **Parsear** la sección `0` (JSON SUMMARY) como contrato de entrada.
2. **Validar** cada bloque JSON interno contra el schema declarado.
3. **Construir** el árbol de dependencias entre propuestas
   (grafo dirigido acíclico dirigido por `fase_objetivo`).
4. **Generar** el backlog de implementación priorizado por
   `kpis` + `riesgos`.
5. **Mantener** `nct_coordinator/` como paquete adicional — sin
   modificar los 25 bloques originales del software principal.
6. **Empaquetar** este documento en `nct_coordinator/lop_v100/SPEC.md`
   y referenciarlo desde `nct_coordinator/__init__.py`.
7. **Reportar** al usuario sólo el resumen, los diagramas y los KPIs.
8. **Versionar** el módulo como `100.0.0` (semver).

---

> **Fin del documento.**  
> Hash lógico del documento: `sha256:NCT-LOP-100X-2026-06-22`.  
> Listo para ingestión por `Mavis M3` y emisión de PRs contra
> `nct_coordinator`.
=== END ===

=== ARCHIVO 3 (0bca55a9 enjambre-de-agentes-v200) ===
---
DOCUMENT_ID: NCT-LOP-200X-2026-06-22-ADDENDUM
TARGET_AI: Mavis M3 (MiniMax-M3)
TARGET_SOFTWARE: NCT NEURONAS CODE TURBO
VERSION: 200.0.0 (Addendum: MiMo Code + Open-Source Agents + HF Spaces + Micro-Agents)
PARENT_DOCUMENT: NCT-LOP-100X-2026-06-22
ENCODING: UTF-8
LEXICON: AI / PROGRAMMING / AGENT_ENGINEERING / FUSION
STATUS: READY_FOR_NCT_INGESTION
---

# NCT NEURONAS CODE TURBO — LOP SYSTEM v200.0
## ADDENDUM: MiMo Code Analysis + Open-Source Agent Catalog + Distributed Micro-Agents on HuggingFace Spaces

> Este documento es **complemento** del `NCT-LOP-100X-2026-06-22.md`
> ya entregado. Mantiene el mismo formato único (Markdown), el mismo
> léxico AI/programación para `Mavis M3`, y la misma regla de "una
> sola salida, sin preguntas, sin comentarios al usuario".
>
> Se integra como `nct_coordinator/lop_v200/` en el árbol de
> entrega del documento padre.

---

## 0. ÍNDICE MAESTRO (JSON SUMMARY FOR MAVIS M3)

```json
{
  "$schema": "https://NCT/turbo/schemas/lop-system-v200.schema.json",
  "document_id": "NCT-LOP-200X-2026-06-22-ADDENDUM",
  "parent_document": "NCT-LOP-100X-2026-06-22",
  "target": "Mavis M3",
  "package": "nct_coordinator.lop_v200",
  "namespace": "nct.lop.v200",

  "scope_additions": [
    "mimo_code_loop_analysis",
    "open_source_agent_catalog",
    "chained_task_strategy_with_example_agent",
    "seed_information_pre_analysis",
    "rag_github_web_research_cycles",
    "huggingface_spaces_remote_compute_fleet",
    "deterministic_dsl_90pct_code_10pct_llm",
    "specialized_micro_agents"
  ],

  "mimo_code_facts": {
    "origin": "Xiaomi MiMo Team",
    "base_project": "OpenCode",
    "license": "MIT",
    "first_release": "2026-06-11 (V0.1.0)",
    "tech_stack": ["Bun", "TypeScript", "Effect", "SolidJS", "Tauri"],
    "three_pillars": {
      "compute": ["Max Mode", "Goal-Stop", "Dynamic Workflow"],
      "memory":  ["Checkpoint/Rebuild", "Writer subagent", "4-tier memory"],
      "evolution": ["Dream", "Distill", "project memory"]
    },
    "benchmark_vs_claude_code": {
      "SWE-Bench_Pro_V2": "+5%",
      "Terminal_Bench_2":  "+5%",
      "ultra_long_200_plus_steps": "beats Claude Code"
    },
    "compatible_models": ["MiMo-V2.5", "MiMo-V2-Pro", "DeepSeek", "Kimi", "GLM"]
  },

  "open_source_clones_catalog": {
    "tier_s_plus": ["OpenCode", "Gemini CLI", "OpenHands", "Open Interpreter", "Aider", "Goose"],
    "tier_a":       ["Qwen Code", "Crush", "Kimi CLI", "Forge Code", "MiMo Code"],
    "tier_b":       ["BLXCode", "Open Design", "OpenClaw", "KiloCode", "Cline", "BLACKBOX.AI"],
    "languages":    ["TypeScript", "Python", "Rust", "Go"],
    "mcp_first":    ["Goose", "Open Design", "BLXCode"]
  },

  "specialized_micro_agents": {
    "count": 12,
    "design_rule": "single responsibility, ≤200 LOC core, single output schema",
    "execution_model": "spawn → run → emit JSON → die",
    "list": [
      "MA-CODE-GEN",        "MA-CODE-LINT",     "MA-CODE-TEST",
      "MA-RAG-SEARCH",      "MA-RAG-SYNTH",     "MA-DOC-WRITE",
      "MA-ARCH-PLAN",       "MA-VERIFY-3CAPAS", "MA-REPAIR-5STEP",
      "MA-RESEARCH-WEB",    "MA-RESEARCH-GH",   "MA-EMIT-REPORT"
    ]
  },

  "huggingface_spaces_fleet": {
    "min_workers": 10,
    "max_workers": 20,
    "protocol": "MCP via mcp-hfspace",
    "selection_rule": "by capability + SLA + cost",
    "failover": "circuit_breaker + backoff_exponential",
    "examples": [
      "evalstate/FLUX.1-schnell",
      "hf-audio/whisper-large-v3-turbo",
      "microsoft/OmniParser",
      "Qwen2-VL-72B (smolagents + E2B Desktop)"
    ]
  },

  "dsl_budget": {
    "code_pct": 90,
    "llm_pct":  10,
    "rationale": "DSL determinista para orquestación, LLM solo en los puntos donde aporta señal no derivable."
  },

  "research_cycle": {
    "phases": ["seed_analysis", "web_research", "github_research", "synthesize", "emit"],
    "min_rounds_per_task": 2,
    "max_rounds_per_task": 5,
    "early_stop_if": "evidence_sufficiency_score >= 0.85"
  },

  "ingestion_directives_for_mavis_m3": [
    "merge_v200_into_v100_dependency_graph",
    "treat_mimo_code_as_reference_implementation_not_dependency",
    "treat_open_source_clones_as_substitutable_backends",
    "spawn_micro_agents_via_hf_spaces_mcp",
    "enforce_90_10_dsl_llm_budget_per_cycle",
    "persist_seed_analysis_to_state_seed_yaml",
    "do_not_modify_existing_25_bloques_of_software_principal",
    "emit_prs_against_nct_coordinator_lop_v200_subpackage"
  ]
}
```

---

## 1. ANÁLISIS DEL CÓDIGO FUENTE DE MiMo Code

### 1.1 Lo que es

MiMo Code es un agente de programación para terminal, MIT,
construido sobre OpenCode por el equipo MiMo de Xiaomi. Diseñado
explícitamente para tareas de horizonte largo (decenas a 200+
pasos continuos). Tres pilares arquitectónicos:

| Pilar | Problema que resuelve | Mecanismos |
|---|---|---|
| **Compute** | error acumulado en cadenas largas | `Max Mode` (multi-sample + majority voting + best-of-N self-verification), `Goal-Stop`, `Dynamic Workflow` |
| **Memory**  | ventana de contexto finita | `Checkpoint/Rebuild`, `Writer subagent` (compacta contexto), sistema de memoria de **4 capas** |
| **Evolution** | sin aprendizaje entre sesiones | `Dream` (consolidación periódica), `Distill` (destilación), memoria de proyecto |

Stack: `Bun + TypeScript + Effect + SolidJS (TUI) + Tauri (desktop)`.

### 1.2 Cómo lo hace — los loops internos de MiMo

```
                ┌──────────────────────────────────────┐
                │           RUNTIME (Bun + Effect)     │
                │                                      │
   user input ─►│ prompt ─► model ─► tool ─► state    │──► output
                │            ▲           │              │
                │            └───────────┘              │
                │                  │                    │
                │       ┌──────────┴──────────┐         │
                │       │                     │         │
                │   Writer subagent      Checkpoint      │
                │   (compacta)           (persiste)      │
                │       │                     │         │
                │       ▼                     ▼         │
                │   4-tier memory         state.jsonl   │
                │                                      │
                │   /dream  ◄────────── cada 7 días     │
                └──────────────────────────────────────┘
```

Patrones de loop identificados en el código (extraídos del repo
y de la documentación oficial):

| Loop | Frecuencia | Salida | Persistencia |
|---|---|---|---|
| `decision_loop` | cada turno | tool call o respuesta | solo en conversación |
| `checkpoint_loop` | cada N turnos (configurable) | snapshot firmdo | `state.jsonl` |
| `writer_loop` | cuando contexto > 70% | resumen estructurado | `memory/tier-N.md` |
| `max_mode_loop` | en decisiones críticas | K muestras → voto | efímero |
| `dream_loop` | cada 7 días | memoria consolidada | `memory/dream.md` |
| `repair_loop` | en error | plan de recuperación | `state.jsonl` |
| `evolution_loop` | al cierre de sesión | skill/proc/prompt nuevo | `skills/` |

### 1.3 Qué tomamos para NCT (regla: nada de copiar literal)

| Componente MiMo | Adaptación NCT v200 |
|---|---|
| `Max Mode` (multi-sample + voting) | `worker_pool.py` con `k_samples` por decisión crítica |
| `Goal-Stop` (criterio de parada) | nueva fase `P9.5` goal-check antes de `deliver` |
| `Dynamic Workflow` | nuevo `ALV_LOP_QUANTUM_FRACTAL_NESTED` ya propuesto en v100 |
| `Checkpoint/Rebuild` | `state/engine.py` con `replay_to_checkpoint(t)` |
| `Writer subagent` | nuevo `MA-RAG-SYNTH` (micro-agente) |
| 4-tier memory | extender `EROS 3-tier` a 4 tiers: `tier0 raw`, `tier1 session`, `tier2 strategic`, `tier3 project` |
| `Dream` | nuevo job `cron weekly` → `MA-DREAM` |
| `Distill` | nuevo job `cron daily` → `MA-DISTILL` |
| Project memory | `state/project_memory.sqlite` |

### 1.4 Diagrama de integración MiMo → NCT

```
   ┌────────────────────────────────────┐
   │            NCT v200                │
   │                                    │
   │   ┌──────────────────────────┐     │
   │   │   nct_coordinator        │     │
   │   │                          │     │
   │   │   FSM 10 fases           │     │
   │   │   ┌──────┐ ┌──────────┐  │     │
   │   │   │RAG   │ │Max Mode  │◄─┼─────┼────借鉴 MiMo
   │   │   └──────┘ └──────────┘  │     │
   │   │   ┌──────┐ ┌──────────┐  │     │
   │   │   │Check │ │Writer    │◄─┼─────┼────借鉴 MiMo
   │   │   │point │ │subagent  │  │     │
   │   │   └──────┘ └──────────┘  │     │
   │   │   ┌──────┐ ┌──────────┐  │     │
   │   │   │Dream │ │Distill   │◄─┼─────┼────借鉴 MiMo
   │   │   └──────┘ └──────────┘  │     │
   │   └──────────────────────────┘     │
   │                                    │
   │   25 bloques existentes (intactos) │
   └────────────────────────────────────┘
```

---

## 2. CATÁLOGO DE AGENTES OPEN-SOURCE (CLONES FIELES DE CLAUDE CODE / CHINO / RUT)

### 2.1 Tabla maestra

| Rank | Proyecto | Stars | Lenguaje | Modelo por defecto | MCP-first | Sustituible como backend |
|---|---|---|---|---|---|---|
| 1 | **OpenCode** | 154.5K | TypeScript | 75+ LLMs | sí | sí |
| 2 | **Gemini CLI** | 103.1K | TypeScript | Gemini (free) | parcial | sí |
| 3 | **OpenHands** | 72.6K | Python | varios | parcial | sí |
| 4 | **Open Interpreter** | 63.4K | Python | local | no | sí |
| 5 | **Aider** | 44.3K | Python | 100+ LLMs | parcial | sí |
| 6 | **Goose** | 43.7K | Rust | varios | **sí** | sí |
| 7 | **Qwen Code** | 24.1K | TypeScript | Qwen3-Coder | sí | sí |
| 8 | **Crush** | 23.8K | Go | varios | sí | sí |
| 9 | **Kimi CLI** | 8.4K | Python | Kimi K2 | parcial | sí |
| 10 | **Forge Code** | 7.2K | Rust | 300+ modelos | parcial | sí |
| 11 | **MiMo Code** | n/a | TypeScript | MiMo-V2.5 + otros | parcial | sí |
| 12 | **Open Design** | n/a | n/a | 16 CLIs integrados | sí | sí (router) |
| 13 | **OpenClaw** | n/a | n/a | OpenRouter + MiMo-V2 | parcial | sí |
| 14 | **KiloCode** | n/a | TypeScript | Kilo Gateway | sí | sí |
| 15 | **Cline** | n/a | TypeScript | 100+ | sí | sí |

### 2.2 Regla de selección (router)

```yaml
router:
  signals: [cost, latency, capability, license, mcp_native]
  rules:
    - if task_type == "code_generation" and budget == "low":
        backend: "opencode"
        model:   "deepseek-coder"
    - if task_type == "long_horizon" and horizon_h >= 24:
        backend: "mimo_code"
        model:   "mimo-v2.5"
    - if task_type == "research_rag":
        backend: "openhands"
        model:   "qwen3-coder"
    - if task_type == "ui_design":
        backend: "open_design"
        model:   "sonnet-4.6"
    - default:
        backend: "goose"
        model:   "claude-sonnet-4.6"
```

### 2.3 Contrato común de invocación

```yaml
backend_invocation:
  transport: ["stdio", "http", "mcp"]
  input_schema:   "nct.task.v1.json"
  output_schema:  "nct.result.v1.json"
  timeout_s:      600
  cancel_token:   true
  auth:
    type: "byok_or_proxy"
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
```

---

## 3. CADENA DE MICRO-AGENTES ESPECIALIZADOS

### 3.1 Diseño

Cada micro-agente es un ejecutable pequeño (≤200 LOC de núcleo) con:

- una sola responsabilidad,
- un solo `input_schema`,
- un solo `output_schema`,
- estado efímero,
- muerte tras emitir el JSON.

Se invocan vía `MCP` o `stdio`. Pueden correr localmente, en un
contenedor, o en un HuggingFace Space remoto.

### 3.2 Catálogo de 12 micro-agentes

| ID | Nombre | Responsabilidad | Input | Output | Tiempo medio |
|---|---|---|---|---|---|
| `MA-CODE-GEN`     | Code Generator | Genera código a partir de spec | `spec.md`, `stack.json` | `code.zip` + `diff.patch` | 5–30 s |
| `MA-CODE-LINT`    | Linter | Lint + format + type-check | `code.zip` | `report.json` | 2–10 s |
| `MA-CODE-TEST`    | Tester | Unit + integration + mutation | `code.zip`, `tests/` | `junit.xml` + `coverage.json` | 10–60 s |
| `MA-RAG-SEARCH`   | Web/GH Search | Búsqueda vectorial + rerank | `query`, `k` | `chunks.json` con citas | 3–15 s |
| `MA-RAG-SYNTH`    | Synthesizer | Sintetiza respuesta con citas | `chunks.json` | `answer.md` | 5–20 s |
| `MA-DOC-WRITE`    | Doc Writer | Documenta arquitectura/decisiones | `artifacts/`, `audience` | `doc.md` | 5–15 s |
| `MA-ARCH-PLAN`    | Architect Planner | Planifica arquitectura y stack | `requirements.json` | `arch.yaml` | 5–30 s |
| `MA-VERIFY-3CAPAS`| Verifier | Verificación adversarial 3 capas | `artifact`, `rubric` | `verdict.json` | 10–60 s |
| `MA-REPAIR-5STEP` | Repairer | Pipeline 5 pasos de reparación | `failure.json` | `repaired.json` o `escalate` | 30–120 s |
| `MA-RESEARCH-WEB` | Web Researcher | Crawling + extracción | `urls[]`, `depth` | `pages.jsonl` | 30–300 s |
| `MA-RESEARCH-GH`  | GitHub Researcher | Búsqueda en GitHub via API | `query`, `lang`, `stars_min` | `repos.json` | 10–60 s |
| `MA-EMIT-REPORT`  | Report Emitter | Empaqueta resultado final | `state.json` | `report.md` + `manifest.json` | 1–5 s |

### 3.3 Ejemplo de agente: `MA-VERIFY-3CAPAS`

```python
# nct_coordinator/lop_v200/micro_agents/ma_verify_3capas.py
SCHEMA_IN = "nct.verify.in.v1"
SCHEMA_OUT = "nct.verify.out.v1"

def run(artifact: dict, rubric: dict, k_samples: int = 3) -> dict:
    # 90% código determinista, 10% LLM solo si adversarial_check falla
    cap1 = adversarial_check(artifact, rubric)              # CODE
    cap2 = cross_check(artifact, rubric)                     # CODE
    cap3 = maker_checker(artifact, rubric)                   # CODE

    if cap1["issues"] or cap2["issues"] or cap3["issues"]:
        cap1_llm = llm_adversarial_review(artifact, rubric) # LLM (10%)
    else:
        cap1_llm = {"issues": []}

    issues = cap1["issues"] + cap2["issues"] + cap3["issues"] + cap1_llm["issues"]
    return {
        "decision": "pass" if not issues else "fail",
        "issues":   issues,
        "evidence": {"cap1": cap1, "cap2": cap2, "cap3": cap3, "cap1_llm": cap1_llm}
    }
```

### 3.4 DSL de invocación

```yaml
# nct_coordinator/lop_v200/pipelines/p_ma_chain.yaml
chain:
  id: ma_chain_arch_v1
  steps:
    - { id: MA-ARCH-PLAN,     input_from: "user", output_to: "ctx.arch" }
    - { id: MA-RESEARCH-GH,   input_from: "ctx.arch.stack", output_to: "ctx.repos" }
    - { id: MA-RESEARCH-WEB,  input_from: "ctx.arch.questions", output_to: "ctx.web" }
    - { id: MA-CODE-GEN,      input_from: "ctx.arch",          output_to: "ctx.code" }
    - { id: MA-CODE-LINT,     input_from: "ctx.code",          output_to: "ctx.lint" }
    - { id: MA-CODE-TEST,     input_from: "ctx.code",          output_to: "ctx.tests" }
    - { id: MA-VERIFY-3CAPAS, input_from: "ctx.code",          output_to: "ctx.verify" }
    - { id: MA-DOC-WRITE,     input_from: "ctx",               output_to: "ctx.doc" }
    - { id: MA-EMIT-REPORT,   input_from: "ctx",               output_to: "report" }
```

---

## 4. ESTRATEGIA DE ENCADENAMIENTO DE TAREAS

### 4.1 Tres patrones canónicos

```
(a) Secuencial          (b) DAG paralelo          (c) Fractal anidado
                                                            
A ─► B ─► C ─► D         A ─► B ─┐                    ┌─► A ─► B ─┐
                                       ─► D           │            ├─► D
                          A ─► C ─┘                    └─► C ──────┘
```

NCT los soporta nativamente:

| Patrón | Configuración | Caso típico |
|---|---|---|
| Secuencial | `chain: linear` | ETL, refactor |
| DAG paralelo | `chain: dag` con `parallel_groups` | investigación + diseño |
| Fractal anidado | `chain: fractal` con `depth ≤ 5` | arquitectura multi-módulo |

### 4.2 Ejemplo completo: encadenar "crear microservicio e-commerce"

```yaml
# pipelines/ecommerce_microservice.yaml
chain:
  id: ecommerce_microservice_v1
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget:
    max_tokens: 2_000_000
    max_runtime_h: 24
  steps:
    - { id: MA-ARCH-PLAN,    parallel_group: g1 }
    - { id: MA-RESEARCH-WEB, parallel_group: g1, input_from: "ctx.arch.questions" }
    - { id: MA-RESEARCH-GH,  parallel_group: g1, input_from: "ctx.arch.stack" }
    - { id: MA-RAG-SYNTH,    parallel_group: g2, input_from: ["ctx.web","ctx.repos"] }
    - { id: MA-CODE-GEN,     parallel_group: g3, input_from: "ctx.arch" }
    - { id: MA-CODE-LINT,    parallel_group: g4, input_from: "ctx.code" }
    - { id: MA-CODE-TEST,    parallel_group: g4, input_from: "ctx.code" }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5, input_from: ["ctx.code","ctx.tests"] }
    - { id: MA-DOC-WRITE,    parallel_group: g5, input_from: "ctx" }
    - { id: MA-EMIT-REPORT,  parallel_group: g6, input_from: "ctx" }
  monitor: { pad: true, anxiety: true, drift: true }
  repair:  { pipeline: 5_steps, max_retries: 3 }
  deliv:   { report: "report.md", manifest: "manifest.json" }
```

### 4.3 Diagrama del ejemplo

```
            ┌─ MA-ARCH-PLAN ──────┐
            │                     │
g1 ────────►├─ MA-RESEARCH-WEB ──┤
            │                     ├─► MA-RAG-SYNTH
            └─ MA-RESEARCH-GH ───┘                │
                                                 ▼
                                          MA-CODE-GEN
                                                 │
            ┌─ MA-CODE-LINT ─────┐               │
            │                     ├─► MA-VERIFY-3CAPAS
g4 ────────►├─ MA-CODE-TEST ─────┤               │
            │                     │               ▼
            └─────────────────────┘        MA-DOC-WRITE
                                                 │
                                                 ▼
                                          MA-EMIT-REPORT
```

---

## 5. ANÁLISIS DE INFORMACIÓN SEMILLA (PRE-ANÁLISIS)

### 5.1 Definición

La "información semilla" es el conjunto de artefactos previos que
existen en el repositorio, en `state.json`, y en el corpus RAG
del proyecto. Antes de planificar, NCT v200 ejecuta una fase
explícita de análisis de semilla.

### 5.2 Pipeline de pre-análisis (5 pasos)

```
seed ─► [S1] indexar ─► [S2] resumir ─► [S3] detectar_gaps
                       │
                       ▼
              [S4] proponer_preguntas ─► [S5] enriquecer_seed
```

| # | Paso | Bloque | Salida |
|---|---|---|---|
| S1 | Indexar repo + state + RAG | `MA-INDEX` | `seed_index.sqlite` |
| S2 | Resumir cada artefacto | `MA-SUMMARIZE` | `seed_summary.json` |
| S3 | Detectar huecos de información | `MA-GAP-DETECT` | `seed_gaps.json` |
| S4 | Proponer preguntas de investigación | `MA-QUESTION-GEN` | `seed_questions.json` |
| S5 | Enriquecer seed con respuestas iniciales | `MA-RESEARCH-WEB` + `MA-RESEARCH-GH` | `seed_enriched.json` |

### 5.3 Métrica de suficiencia

```python
evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
)
```

Si `evidence_sufficiency_score >= 0.85` → el sistema puede
proceder sin más investigación. Si `< 0.85` → entra en ciclo
de investigación (sección 6).

---

## 6. CICLOS DE INVESTIGACIÓN (WEB + GITHUB RAG)

### 6.1 Diseño del ciclo

```
   ┌─────────────────────────────────────────────────────────┐
   │              CICLO DE INVESTIGACIÓN                     │
   │                                                         │
   │   ┌────────────┐    ┌────────────┐    ┌────────────┐    │
   │   │ R1: query  │───►│ R2: fetch  │───►│ R3: filter │    │
   │   └────────────┘    └────────────┘    └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │   ┌────────────┐                      ┌────────────┐    │
   │   │ R5: refine │◄──────────replan────│ R4: eval   │    │
   │   └────────────┘                      └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │       new_query                          stop if        │
   │                                           score ≥ 0.85  │
   └─────────────────────────────────────────────────────────┘
```

### 6.2 Fuentes prioritarias

| Tipo | Fuente | Uso |
|---|---|---|
| Web | Wikipedia, OWASP, MDN, arXiv, blogs oficiales | contexto general |
| Web | Documentación oficial de stacks (FastAPI, React, etc.) | últimas versiones |
| GitHub | `XiaomiMiMo/MiMo-Code`, `sst/opencode`, etc. | patrones de referencia |
| GitHub | `awesome-*` lists | catálogos curados |
| GitHub | Issues + PRs + Discussions | problemas conocidos |
| GitHub | Releases + changelogs | breaking changes |

### 6.3 Política de uso

- Mínimo **2 rondas** de investigación por tarea.
- Máximo **5 rondas** (anti-bucle).
- Cada ronda consume ≤ 50K tokens.
- Salida consolidada vía `MA-RAG-SYNTH`.

---

## 7. FLOTA DE SERVIDORES REMOTOS (HuggingFace Spaces)

### 7.1 Por qué HF Spaces

- **Gratis** (CPU basic, T4 small).
- **Aislamiento**: cada Space es un contenedor independiente.
- **MCP nativo**: `mcp-hfspace` permite invocarlos como tools.
- **Diversidad de GPUs**: CPU, T4, A10G, A100 según plan.

### 7.2 Composición de la flota (10–20 workers)

| # | Space / modelo | Rol | GPU | Latencia media |
|---|---|---|---|---|
| 1 | `evalstate/FLUX.1-schnell`           | generación de imágenes | T4 | 5–15 s |
| 2 | `hf-audio/whisper-large-v3-turbo`    | STT | T4 | 1–5 s |
| 3 | `microsoft/OmniParser`              | visión / parsing UI | A10G | 2–8 s |
| 4 | `Qwen2-VL-72B` (smolagents + E2B)    | VLM reasoning | A100 | 5–20 s |
| 5 | `gradio/llm-router`                  | LLM genérico | T4 | 2–10 s |
| 6 | `nct/rag-search`                    | búsqueda vectorial | CPU | 1–3 s |
| 7 | `nct/code-runner`                   | ejecución de código | CPU | 1–5 s |
| 8 | `nct/lint-fmt`                      | lint + format | CPU | 0.5–2 s |
| 9 | `nct/test-runner`                   | test + coverage | CPU | 5–30 s |
| 10 | `nct/security-scan`                | sast + secrets | CPU | 10–60 s |
| 11 | `nct/dream`                         | consolidación memoria | CPU | 60–300 s |
| 12 | `nct/distill`                       | destilación memoria | CPU | 60–300 s |
| 13–20 | **reservados** para picos | failover | mixto | variable |

### 7.3 Selección dinámica por el router

```python
def select_worker(capability: str, sla_ms: int) -> str:
    candidates = workers_by_capability[capability]
    alive = [c for c in candidates if c.health == "ok"]
    feasible = [c for c in alive if c.p95_ms <= sla_ms]
    return min(feasible, key=lambda c: c.cost)
```

### 7.4 Resiliencia

- `circuit_breaker` por Space (umbral: 3 fallos consecutivos).
- `backoff_exponential` (base 2s, max 5 min).
- `failover` al siguiente Space disponible de la misma capability.
- Si todos los Spaces de una capability caen → degradación
  elegante: el paso se marca como `skipped` y la cadena continúa.

### 7.5 Diagrama de la flota

```
                    ┌──────────────────────┐
                    │     NCT Router       │
                    │  (selector dinámico) │
                    └─────────┬────────────┘
                              │
       ┌──────────┬───────────┼───────────┬──────────┐
       ▼          ▼           ▼           ▼          ▼
    HF Space   HF Space    HF Space   HF Space   HF Space
    #1 imagen  #2 audio    #3 visión  #4 VLM     #5 LLM
       │          │           │           │          │
       └──────────┴─────┬─────┴───────────┴──────────┘
                        │
                  circuit breaker
                  backoff exponencial
```

---

## 8. DSL DETERMINISTA (90% CÓDIGO / 10% LLM)

### 8.1 Regla de presupuesto

- **90% código determinista**:
  parseo, validación, transformación, routing, verificación
  mecánica, formatting, retry, fallback, circuit breaker,
  EROS compression, checkpoint/restore, schema validation.
- **10% LLM**: solo en
  `MA-RAG-SYNTH`, `MA-ARCH-PLAN` (parte creativa), el modo
  `Max Mode` en decisiones críticas, `llm_adversarial_review`
  cuando las 3 capas mecánicas fallan.

### 8.2 DSL declarativo

```yaml
# dsl/step.yaml
step:
  id: MA-VERIFY-3CAPAS
  type: deterministic_with_llm_fallback
  budget:
    code_pct: 90
    llm_pct:  10
    max_tokens: 50_000
  inputs:  { artifact: object, rubric: object }
  outputs: { decision: enum, issues: array }
  code_steps:
    - parse_artifact
    - schema_validate
    - cap1_adversarial
    - cap2_cruzada
    - cap3_maker_checker
  llm_steps:
    - when: "any(cap.issues)"
      call: llm_adversarial_review
      max_tokens: 4_000
      temperature: 0.0
```

### 8.3 Contador de presupuesto

```python
class Budget:
    code_tokens: int = 0
    llm_tokens:  int = 0

    @property
    def llm_pct(self) -> float:
        total = self.code_tokens + self.llm_tokens
        return self.llm_tokens / max(total, 1)

    def enforce(self, target_pct=0.10):
        assert self.llm_pct <= target_pct, "LLM budget exceeded"
```

---

## 9. INVESTIGACIÓN NECESARIA (RAG + WEB + GH) — INTEGRACIÓN

### 9.1 Por tarea

```yaml
research:
  sources:
    - type: web
      urls:
        - "https://en.wikipedia.org/wiki/{topic}"
        - "https://owasp.org/..."
        - "https://docs.{stack}.dev/..."
    - type: github
      queries:
        - "{topic} awesome"
        - "{topic} framework stars:>1000"
        - "{topic} site:github.com"
    - type: arxiv
      queries: ["{topic} long horizon agents"]
  rounds: { min: 2, max: 5 }
  early_stop: { metric: evidence_sufficiency_score, threshold: 0.85 }
  synth: { agent: MA-RAG-SYNTH, max_tokens: 8_000 }
```

### 9.2 Ejemplo: tarea "diseñar sistema RAG multi-tenant"

```yaml
research:
  sources:
    web:
      - "https://docs.llamaindex.ai/en/stable/..."
      - "https://python.langchain.com/docs/..."
      - "https://qdrant.tech/documentation/..."
    github:
      - "rag multi-tenant stars:>500"
      - "vector db benchmark"
      - "awesome-rag"
  rounds: 3
  synth: MA-RAG-SYNTH
  expected_artifacts:
    - "stack_recommendation.md"
    - "security_considerations.md"
    - "performance_benchmark.md"
```

---

## 10. EJEMPLO COMPLETO DE PIPELINE LARGO

### 10.1 Spec

> *"Diseña, implementa, testea y documenta una API REST multi-tenant
> para una SaaS de gestión de tareas con autenticación JWT, rate
> limiting y auditoría, lista para producción en 24h."*

### 10.2 Pipeline

```yaml
chain:
  id: saas_tasks_api_v1
  pattern: dag
  level: L5_CONTINUOUS_AUTONOMOUS_72H_PLUS
  budget: { max_tokens: 5_000_000, max_runtime_h: 24 }

  research:
    sources:
      web:  ["owasp jwt", "fastapi multi-tenant", "rate limit algorithms"]
      github: ["fastapi-template stars:>1000", "awesome-saas"]
    rounds: { min: 2, max: 4 }

  steps:
    - { id: MA-ARCH-PLAN,     parallel_group: g1 }
    - { id: MA-RESEARCH-WEB,  parallel_group: g1 }
    - { id: MA-RESEARCH-GH,   parallel_group: g1 }
    - { id: MA-RAG-SYNTH,     parallel_group: g2, input_from: [g1] }
    - { id: MA-CODE-GEN,      parallel_group: g3, input_from: [g2] }
    - { id: MA-CODE-LINT,     parallel_group: g4, input_from: [g3] }
    - { id: MA-CODE-TEST,     parallel_group: g4, input_from: [g3] }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5, input_from: [g4] }
    - { id: MA-DOC-WRITE,     parallel_group: g5, input_from: [g3] }
    - { id: MA-EMIT-REPORT,   parallel_group: g6, input_from: [g5] }

  monitor:  { pad: true, anxiety: true, drift: true }
  repair:   { pipeline: 5_steps, max_retries: 3 }
  hf_fleet: { min_workers: 10, max_workers: 20 }
  deliv:    { report: "report.md", manifest: "manifest.json", signed: true }
```

### 10.3 Diagrama

```
                ┌─ MA-ARCH-PLAN ────┐
                │                    │
g1 ─────────────►├─ MA-RESEARCH-WEB ─┤
                │                    ├─► MA-RAG-SYNTH
                └─ MA-RESEARCH-GH ──┘                │
                                                   ▼
                                            MA-CODE-GEN
                                                   │
                ┌─ MA-CODE-LINT ───┐                │
                │                    ├─► MA-VERIFY-3CAPAS
g4 ─────────────►├─ MA-CODE-TEST ───┤                │
                │                    │                ▼
                └────────────────────┘         MA-DOC-WRITE
                                                   │
                                                   ▼
                                            MA-EMIT-REPORT

   Monitor: PAD + Anxiety + Drift   ◄──────────┐
                                              │
   HF Fleet: 10–20 spaces             ◄────────┤
                                              │
   Repair: 5 pasos                  ◄──────────┘
```

---

## 11. INTEGRACIÓN CON DOCUMENTO PADRE v100

| Sección v100 | Complemento v200 |
|---|---|
| §0 índice | nuevo bloque JSON con scope_additions |
| §1 niveles | `level: L5/L6` ahora pueden usar HF Spaces |
| §2 fusión MiniMax/Kimi K | se añade **MiMo Code** como tercer polo |
| §3 task models | cada `TM` puede invocar micro-agentes |
| §4 ALV loops | el `QUANTUM_FRACTAL` usa la cadena de micro-agentes |
| §5 propuestas | nuevas propuestas `PROP-13`..`PROP-20` (abajo) |
| §6 diagramas | diagrama adicional de la flota HF |
| §7 contratos YAML | contratos extendidos para micro-agentes |
| §9 entrega | nuevo subpaquete `lop_v200/` |

### 11.1 Nuevas propuestas (PROP-13 → PROP-20)

| ID | Título | Resumen |
|---|---|---|
| `PROP-13` | `micro_agents_catalog` | 12 micro-agentes especializados |
| `PROP-14` | `chain_patterns`     | 3 patrones: secuencial, DAG, fractal |
| `PROP-15` | `seed_pre_analysis`  | 5 pasos de pre-análisis |
| `PROP-16` | `research_cycle`     | 2–5 rondas, stop por evidencia |
| `PROP-17` | `hf_spaces_fleet`    | 10–20 workers remotos MCP |
| `PROP-18` | `dsl_90_10_budget`   | 90% código / 10% LLM |
| `PROP-19` | `mimo_integration`   |借鉴 de MiMo: Max Mode, Goal-Stop, Writer, Dream |
| `PROP-20` | `oss_backends_router`| router entre 15 backends OSS |

### 11.2 Contratos YAML de las nuevas propuestas

```yaml
# PROP-13
name: micro_agents_catalog
inputs:  { task: Task, k_concurrency: int }
outputs: { results: array[MicroAgentResult], audit: AuditTrail }
invariants:
  - single_responsibility: true
  - max_loc_core: 200
  - schema_io_unico: true
kpis:
  - p99_latency_ms
  - success_rate
  - cost_per_call

# PROP-14
name: chain_patterns
inputs:  { tasks: array[Task] }
outputs: { execution_plan: ExecutionPlan }
invariants:
  - acyclic_dag: true
  - max_depth: 5

# PROP-15
name: seed_pre_analysis
inputs:  { repo: RepoPath, state: StatePath, rag: RAGPath }
outputs: { seed_index: SQLite, gaps: array, questions: array }
invariants:
  - reproducible: true

# PROP-16
name: research_cycle
inputs:  { question: string, sources: array }
outputs: { synthesized: Synthesis, score: float }
invariants:
  - min_rounds: 2
  - max_rounds: 5
  - early_stop_threshold: 0.85

# PROP-17
name: hf_spaces_fleet
inputs:  { capability: string, sla_ms: int }
outputs: { worker_id: string, fallback_chain: array }
invariants:
  - min_workers: 10
  - max_workers: 20
  - circuit_breaker: true

# PROP-18
name: dsl_90_10_budget
inputs:  { pipeline: Pipeline }
outputs: { budget_report: BudgetReport }
invariants:
  - llm_pct_le_10: true
kpis:
  - llm_pct
  - cost_per_cycle

# PROP-19
name: mimo_integration
inputs:  { mimo_feature: enum[max_mode, goal_stop, writer, dream, distill, checkpoint] }
outputs: { enabled: bool, config: object }

# PROP-20
name: oss_backends_router
inputs:  { task: Task }
outputs: { backend: enum, model: string, transport: enum }
invariants:
  - byok_or_proxy: true
  - mcp_first_preferred: true
```

---

## 12. ÁRBOL DE ENTREGA ACTUALIZADO

```
nct_coordinator/
├── lop_v100/                      # documento padre (ya entregado)
│   ├── __init__.py
│   ├── levels.py
│   ├── alvs.py
│   ├── task_models/...
│   ├── proposals/PROP-01..12.yaml
│   └── schemas/...
│
├── lop_v200/                      # NUEVO (este addendum)
│   ├── __init__.py
│   ├── micro_agents/              # 12 micro-agentes
│   │   ├── ma_code_gen.py
│   │   ├── ma_code_lint.py
│   │   ├── ma_code_test.py
│   │   ├── ma_rag_search.py
│   │   ├── ma_rag_synth.py
│   │   ├── ma_doc_write.py
│   │   ├── ma_arch_plan.py
│   │   ├── ma_verify_3capas.py
│   │   ├── ma_repair_5step.py
│   │   ├── ma_research_web.py
│   │   ├── ma_research_gh.py
│   │   └── ma_emit_report.py
│   ├── pipelines/                 # DSL declarativos
│   │   ├── p_ma_chain.yaml
│   │   ├── ecommerce_microservice.yaml
│   │   └── saas_tasks_api_v1.yaml
│   ├── backends/                  # routers a OSS clones
│   │   ├── opencode_adapter.py
│   │   ├── goose_adapter.py
│   │   ├── qwen_code_adapter.py
│   │   ├── mimo_code_adapter.py
│   │   └── forge_code_adapter.py
│   ├── hf_spaces/                 # cliente de la flota HF
│   │   ├── fleet_client.py
│   │   ├── circuit_breaker.py
│   │   └── selector.py
│   ├── dsl/
│   │   ├── step.yaml
│   │   ├── pipeline.yaml
│   │   └── budget.py
│   ├── seed/
│   │   ├── pre_analysis.py
│   │   └── gap_detector.py
│   ├── research/
│   │   ├── cycle.py
│   │   └── web_gh_sources.yaml
│   ├── proposals/PROP-13..20.yaml
│   └── schemas/
│       ├── micro-agent.schema.json
│       ├── pipeline.schema.json
│       └── hf-fleet.schema.json
```

---

## 13. INSTRUCCIONES FINALES PARA `Mavis M3`

1. **Parsear** la sección `0` (JSON SUMMARY) como contrato de
   entrada y mergearla con el contrato del documento padre v100.
2. **Construir** el grafo de dependencias entre v100 y v200.
3. **Materializar** el árbol de archivos de la sección 12.
4. **Generar** los PRs siguiendo el orden:
   `schemas → micro_agents → dsl → pipelines → backends →
   hf_spaces → seed → research → proposals`.
5. **Validar** que `llm_pct ≤ 0.10` en cada pipeline.
6. **Validar** que ningún archivo bajo `nct_coordinator/lop_v200/`
   modifica los 25 bloques originales del software principal.
7. **Versionar** este módulo como `200.0.0` (semver).
8. **Reportar** al usuario sólo el resumen ejecutivo, los
   diagramas y los KPIs. Sin preguntas, sin comentarios.

---

> **Fin del addendum v200.**  
> Hash lógico: `sha256:NCT-LOP-200X-2026-06-22-ADDENDUM`.  
> Listo para ingestión por `Mavis M3` y emisión de PRs contra
> `nct_coordinator/lop_v200/`.
=== END ===

=== ARCHIVO 46 (aa62f4e3 mimo-lop-v200 segundo) ===
# MASTER DOCUMENTO 14: MiMoCode + LOP v200
## MAXBRY SUPER TEAM · MiMo Integration · 12 Micro · 8 Propuestas

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. MiMo CODE — ANÁLISIS

### 1.1 Qué es
- MiMo Code = agente de programación para terminal
- MIT, basado en OpenCode
- Equipo MiMo de Xiaomi
- Tareas de horizonte largo (decenas a 200+ pasos)

### 1.2 Tres Pilares Arquitectónicos

| Pilar | Problema | Mecanismos |
|---|---|---|
| **Compute** | Error acumulado | Max Mode, Goal-Stop, Dynamic Workflow |
| **Memory** | Contexto finito | Checkpoint/Rebuild, Writer, 4-tier memory |
| **Evolution** | Sin aprendizaje | Dream, Distill, project memory |

### 1.3 Stack Técnico
- Bun + TypeScript + Effect + SolidJS (TUI) + Tauri (desktop)

### 1.4 7 Loops Internos Identificados

| Loop | Frecuencia | Salida | Persistencia |
|---|---|---|---|
| decision_loop | Cada turno | Tool call o respuesta | Conversación |
| checkpoint_loop | Cada N turnos | Snapshot firmado | state.jsonl |
| writer_loop | Contexto > 70% | Resumen | memory/tier-N.md |
| max_mode_loop | Decisiones críticas | K muestras → voto | Efímero |
| dream_loop | Cada 7 días | Memoria consolidada | memory/dream.md |
| repair_loop | En error | Plan de recuperación | state.jsonl |
| evolution_loop | Al cierre | Skill/proc/prompt nuevo | skills/ |

### 1.5 Benchmark
- SWE-Bench Pro V2: +5%
- Terminal Bench 2: +5%
- Ultra long 200+ steps: beats Claude Code

---

## 2. ADAPTACIONES A NCT (REGLA: NADA LITERAL)

| Componente MiMo | Adaptación NCT v200 |
|---|---|
| Max Mode (multi-sample + voting) | `worker_pool.py` con k_samples |
| Goal-Stop | Nueva fase P9.5 goal-check |
| Dynamic Workflow | ALV_LOP_QUANTUM_FRACTAL_NESTED |
| Checkpoint/Rebuild | state/engine.py con replay_to_checkpoint(t) |
| Writer subagent | MA-RAG-SYNTH |
| 4-tier memory | EROS 3-tier → 4 tiers |
| Dream | Job cron weekly → MA-DREAM |
| Distill | Job cron daily → MA-DISTILL |
| Project memory | state/project_memory.sqlite |

---

## 3. LOP v200 — LIGURE OPERATIONAL PROCEDURE

### 3.1 Qué es
Extensión de LOP (v100) que añade:
- 12 micro-agentes especializados
- 8 nuevas propuestas (PROP-13 a PROP-20)
- Integración MiMo
- Flota HF Spaces

### 3.2 Estructura
```
lop_v200/
├── schemas/           # JSON Schemas
├── micro_agents/      # 12 micro-agentes
├── dsl/               # DSL declarativo
├── pipelines/         # Pipelines de ejecución
├── backends/          # Routers de backends
├── hf_spaces/         # Configuración flota HF
├── seed/              # Pre-análisis
├── research/          # Ciclo de investigación
└── proposals/         # PROP-13 a PROP-20
```

---

## 4. 12 MICRO-AGENTES ESPECIALIZADOS

| ID | Nombre | Input | Output | Tiempo |
|----|--------|-------|--------|--------|
| MA-CODE-GEN | Code Generator | spec.md, stack.json | code.zip + diff.patch | 5-30s |
| MA-CODE-LINT | Linter | code.zip | report.json | 2-10s |
| MA-CODE-TEST | Tester | code.zip, tests/ | junit.xml + coverage.json | 10-60s |
| MA-RAG-SEARCH | Web/GH Search | query, k | chunks.json | 3-15s |
| MA-RAG-SYNTH | Synthesizer | chunks.json | answer.md | 5-20s |
| MA-DOC-WRITE | Doc Writer | artifacts/, audience | doc.md | 5-15s |
| MA-ARCH-PLAN | Architect Planner | requirements.json | arch.yaml | 5-30s |
| MA-VERIFY-3CAPAS | Verifier | artifact, rubric | verdict.json | 10-60s |
| MA-REPAIR-5STEP | Repairer | failure.json | repaired.json | 30-120s |
| MA-RESEARCH-WEB | Web Researcher | urls[], depth | pages.jsonl | 30-300s |
| MA-RESEARCH-GH | GitHub Researcher | query, lang, stars | repos.json | 10-60s |
| MA-EMIT-REPORT | Report Emitter | state.json | report.md + manifest.json | 1-5s |

---

## 5. PATRONES DE ENCADENAMIENTO

### 5.1 Secuencial
```
A → B → C → D
```

### 5.2 DAG Paralelo
```
       ┌─ B ─┐
A ──┬──►     ─► D
     └─ C ──┘
```

### 5.3 Fractal Anidado
```
   ┌─ A ─► B ─┐
   │            ├─► D
   └─ C ─────┘
```

---

## 6. 8 NUEVAS PROPUESTAS (PROP-13 a PROP-20)

### PROP-13 — micro_agents_catalog
Catálogo de 12 micro-agentes especializados.

### PROP-14 — chain_patterns
3 patrones: secuencial, DAG, fractal.

### PROP-15 — seed_pre_analysis
Pipeline de 5 pasos antes de empezar.

### PROP-16 — research_cycle
2-5 rondas de investigación.

### PROP-17 — hf_spaces_fleet
Flota de 10-20 workers HF Spaces.

### PROP-18 — dsl_90_10_budget
90% código / 10% LLM.

### PROP-19 — mimo_integration
Integración selectiva de MiMo.

### PROP-20 — oss_backends_router
Router entre 15 backends OSS.

---

## 7. FLOTA HF SPACES (10-20 WORKERS)

### Composición:

| # | Space | Rol | GPU | Latencia |
|---|-------|-----|-----|----------|
| 1 | FLUX.1-schnell | Imágenes | T4 | 5-15s |
| 2 | Whisper-large-v3 | STT | T4 | 1-5s |
| 3 | OmniParser | Visión UI | A10G | 2-8s |
| 4 | Qwen2-VL-72B | VLM | A100 | 5-20s |
| 5 | gradio/llm-router | LLM | T4 | 2-10s |
| 6 | nct/rag-search | Búsqueda | CPU | 1-3s |
| 7 | nct/code-runner | Ejecución | CPU | 1-5s |
| 8 | nct/lint-fmt | Lint+format | CPU | 0.5-2s |
| 9 | nct/test-runner | Test+coverage | CPU | 5-30s |
| 10 | nct/security-scan | SAST+secrets | CPU | 10-60s |
| 11 | nct/dream | Consolidación | CPU | 60-300s |
| 12 | nct/distill | Destilación | CPU | 60-300s |
| 13-20 | Reservados | Failover | Mixto | Variable |

---

## 8. OPEN SOURCE BACKENDS (15)

| # | Proyecto | Stars | Lenguaje | Modelo default |
|---|----------|-------|----------|----------------|
| 1 | OpenCode | 154.5K | TypeScript | 75+ LLMs |
| 2 | Gemini CLI | 103.1K | TypeScript | Gemini free |
| 3 | OpenHands | 72.6K | Python | Varios |
| 4 | Open Interpreter | 63.4K | Python | Local |
| 5 | Aider | 44.3K | Python | 100+ LLMs |
| 6 | Goose | 43.7K | Rust | Varios |
| 7 | Qwen Code | 24.1K | TypeScript | Qwen3-Coder |
| 8 | Crush | 23.8K | Go | Varios |
| 9 | Kimi CLI | 8.4K | Python | Kimi K2 |
| 10 | Forge Code | 7.2K | Rust | 300+ modelos |
| 11 | MiMo Code | n/a | TypeScript | MiMo-V2.5 |
| 12 | Open Design | n/a | n/a | 16 CLIs |
| 13 | OpenClaw | n/a | n/a | OpenRouter |
| 14 | KiloCode | n/a | TypeScript | Kilo Gateway |
| 15 | Cline | n/a | TypeScript | 100+ |

### Router:
```python
def select_backend(task_type, budget):
    if task_type == "code_generation" and budget == "low":
        return ("opencode", "deepseek-coder")
    elif task_type == "long_horizon" and horizon_h >= 24:
        return ("mimo_code", "mimo-v2.5")
    elif task_type == "research_rag":
        return ("openhands", "qwen3-coder")
    elif task_type == "ui_design":
        return ("open_design", "sonnet-4.6")
    else:
        return ("goose", "claude-sonnet-4.6")
```

---

## 9. EJEMPLO COMPLETO: E-COMMERCE MICROSERVICE

```yaml
chain:
  id: ecommerce_microservice_v1
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget: { max_tokens: 2_000_000, max_runtime_h: 24 }
  steps:
    - { id: MA-ARCH-PLAN,    parallel_group: g1 }
    - { id: MA-RESEARCH-WEB, parallel_group: g1 }
    - { id: MA-RESEARCH-GH,  parallel_group: g1 }
    - { id: MA-RAG-SYNTH,    parallel_group: g2 }
    - { id: MA-CODE-GEN,     parallel_group: g3 }
    - { id: MA-CODE-LINT,    parallel_group: g4 }
    - { id: MA-CODE-TEST,    parallel_group: g4 }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5 }
    - { id: MA-DOC-WRITE,    parallel_group: g5 }
    - { id: MA-EMIT-REPORT,  parallel_group: g6 }
  monitor: { pad: true, anxiety: true, drift: true }
  repair:  { pipeline: 5_steps, max_retries: 3 }
```

---

## 10. CONCLUSIÓN

LOP v200 añade:
- 12 micro-agentes especializados
- 3 patrones de encadenamiento
- 5 pasos de pre-análisis
- 2-5 rondas de research
- 10-20 workers HF Spaces
- Router de 15 backends OSS
- 8 nuevas propuestas (PROP-13 a PROP-20)
- Integración selectiva MiMo

Una extensión poderosa del LOP v100 original.
</content>=== END ===

=== ARCHIVO 35 (80ce5f95 mimo-lop-v200 tercero) ===
# DOCUMENTO 16: MIMOCODE / LOP v200 / INVESTIGACIÓN
## Extraído del historial del chat

---

## 1. MIMOCODE - ANÁLISIS DETALLADO

### Lo que es:
- MiMo Code es un agente de programación para terminal
- MIT, construido sobre OpenCode por el equipo MiMo de Xiaomi
- Diseñado para tareas de horizonte largo (decenas a 200+ pasos continuos)

### Tres pilares arquitectónicos:

| Pilar | Problema | Mecanismos |
|---|---|---|
| Compute | error acumulado en cadenas largas | Max Mode, Goal-Stop, Dynamic Workflow |
| Memory | ventana de contexto finita | Checkpoint/Rebuild, Writer subagent, 4-tier memory |
| Evolution | sin aprendizaje entre sesiones | Dream, Distill, project memory |

### Stack:
- Bun + TypeScript + Effect + SolidJS (TUI) + Tauri (desktop)

### Loops internos identificados en el código:

| Loop | Frecuencia | Salida | Persistencia |
|---|---|---|---|
| decision_loop | cada turno | tool call o respuesta | solo en conversación |
| checkpoint_loop | cada N turnos (configurable) | snapshot firmado | state.jsonl |
| writer_loop | cuando contexto > 70% | resumen estructurado | memory/tier-N.md |
| max_mode_loop | en decisiones críticas | K muestras → voto | efímero |
| dream_loop | cada 7 días | memoria consolidada | memory/dream.md |
| repair_loop | en error | plan de recuperación | state.jsonl |
| evolution_loop | al cierre de sesión | skill/proc/prompt nuevo | skills/ |

### Lo que tomamos para NCT (regla: nada de copiar literal):

| Componente MiMo | Adaptación NCT v200 |
|---|---|
| Max Mode (multi-sample + voting) | worker_pool.py con k_samples por decisión crítica |
| Goal-Stop (criterio de parada) | nueva fase P9.5 goal-check antes de deliver |
| Dynamic Workflow | nuevo ALV_LOP_QUANTUM_FRACTAL_NESTED |
| Checkpoint/Rebuild | state/engine.py con replay_to_checkpoint(t) |
| Writer subagent | nuevo MA-RAG-SYNTH |
| 4-tier memory | extender EROS 3-tier a 4 tiers |
| Dream | nuevo job cron weekly → MA-DREAM |
| Distill | nuevo job cron daily → MA-DISTILL |
| Project memory | state/project_memory.sqlite |

### Benchmark vs Claude Code:
- SWE-Bench Pro V2: +5%
- Terminal Bench 2: +5%
- Ultra long 200+ steps: beats Claude Code

### Modelos compatibles:
- MiMo-V2.5
- MiMo-V2-Pro
- DeepSeek
- Kimi
- GLM

---

## 2. CATÁLOGO DE AGENTES OPEN-SOURCE

### Tabla Maestra de Proyectos:

| Rank | Proyecto | Stars | Lenguaje | Modelo por defecto | MCP-first |
|---|---|---|---|---|---|
| 1 | OpenCode | 154.5K | TypeScript | 75+ LLMs | sí |
| 2 | Gemini CLI | 103.1K | TypeScript | Gemini (free) | parcial |
| 3 | OpenHands | 72.6K | Python | varios | parcial |
| 4 | Open Interpreter | 63.4K | Python | local | no |
| 5 | Aider | 44.3K | Python | 100+ LLMs | parcial |
| 6 | Goose | 43.7K | Rust | varios | sí |
| 7 | Qwen Code | 24.1K | TypeScript | Qwen3-Coder | sí |
| 8 | Crush | 23.8K | Go | varios | sí |
| 9 | Kimi CLI | 8.4K | Python | Kimi K2 | parcial |
| 10 | Forge Code | 7.2K | Rust | 300+ modelos | parcial |
| 11 | MiMo Code | n/a | TypeScript | MiMo-V2.5 + otros | parcial |
| 12 | Open Design | n/a | n/a | 16 CLIs integrados | sí |
| 13 | OpenClaw | n/a | n/a | OpenRouter + MiMo-V2 | parcial |
| 14 | KiloCode | n/a | TypeScript | Kilo Gateway | sí |
| 15 | Cline | n/a | TypeScript | 100+ | sí |

### Lenguajes: TypeScript, Python, Rust, Go
### MCP-first: Goose, Open Design, BLXCode

### Regla de Selección (Router):
```yaml
router:
  signals: [cost, latency, capability, license, mcp_native]
  rules:
    - if task_type == "code_generation" and budget == "low":
        backend: "opencode"
        model: "deepseek-coder"
    - if task_type == "long_horizon" and horizon_h >= 24:
        backend: "mimo_code"
        model: "mimo-v2.5"
    - if task_type == "research_rag":
        backend: "openhands"
        model: "qwen3-coder"
    - if task_type == "ui_design":
        backend: "open_design"
        model: "sonnet-4.6"
    - default:
        backend: "goose"
        model: "claude-sonnet-4.6"
```

### Contrato Común de Invocación:
```yaml
backend_invocation:
  transport: ["stdio", "http", "mcp"]
  input_schema:   "nct.task.v1.json"
  output_schema:  "nct.result.v1.json"
  timeout_s:      600
  cancel_token:   true
  auth:
    type: "byok_or_proxy"
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
```

---

## 3. CADENA DE MICRO-AGENTES ESPECIALIZADOS

### Diseño:
Cada micro-agente es un ejecutable pequeño (≤200 LOC de núcleo) con:
- Una sola responsabilidad
- Un solo input_schema
- Un solo output_schema
- Estado efímero
- Muerte tras emitir el JSON

Se invocan vía MCP o stdio. Pueden correr localmente, en un contenedor, o en un HuggingFace Space remoto.

### Catálogo de 12 Micro-Agentes:

| ID | Nombre | Responsabilidad | Input | Output | Tiempo medio |
|---|---|---|---|---|---|
| MA-CODE-GEN | Code Generator | Genera código a partir de spec | spec.md, stack.json | code.zip + diff.patch | 5–30 s |
| MA-CODE-LINT | Linter | Lint + format + type-check | code.zip | report.json | 2–10 s |
| MA-CODE-TEST | Tester | Unit + integration + mutation | code.zip, tests/ | junit.xml + coverage.json | 10–60 s |
| MA-RAG-SEARCH | Web/GH Search | Búsqueda vectorial + rerank | query, k | chunks.json con citas | 3–15 s |
| MA-RAG-SYNTH | Synthesizer | Sintetiza respuesta con citas | chunks.json | answer.md | 5–20 s |
| MA-DOC-WRITE | Doc Writer | Documenta arquitectura/decisiones | artifacts/, audience | doc.md | 5–15 s |
| MA-ARCH-PLAN | Architect Planner | Planifica arquitectura y stack | requirements.json | arch.yaml | 5–30 s |
| MA-VERIFY-3CAPAS | Verifier | Verificación adversarial 3 capas | artifact, rubric | verdict.json | 10–60 s |
| MA-REPAIR-5STEP | Repairer | Pipeline 5 pasos de reparación | failure.json | repaired.json o escalate | 30–120 s |
| MA-RESEARCH-WEB | Web Researcher | Crawling + extracción | urls[], depth | pages.jsonl | 30–300 s |
| MA-RESEARCH-GH | GitHub Researcher | Búsqueda en GitHub via API | query, lang, stars_min | repos.json | 10–60 s |
| MA-EMIT-REPORT | Report Emitter | Empaqueta resultado final | state.json | report.md + manifest.json | 1–5 s |

### Ejemplo: MA-VERIFY-3CAPAS:
```python
SCHEMA_IN = "nct.verify.in.v1"
SCHEMA_OUT = "nct.verify.out.v1"

def run(artifact: dict, rubric: dict, k_samples: int = 3) -> dict:
    # 90% código determinista, 10% LLM solo si adversarial_check falla
    cap1 = adversarial_check(artifact, rubric)              # CODE
    cap2 = cross_check(artifact, rubric)                     # CODE
    cap3 = maker_checker(artifact, rubric)                   # CODE

    if cap1["issues"] or cap2["issues"] or cap3["issues"]:
        cap1_llm = llm_adversarial_review(artifact, rubric) # LLM (10%)
    else:
        cap1_llm = {"issues": []}

    issues = cap1["issues"] + cap2["issues"] + cap3["issues"] + cap1_llm["issues"]
    return {
        "decision": "pass" if not issues else "fail",
        "issues":   issues,
        "evidence": {"cap1": cap1, "cap2": cap2, "cap3": cap3, "cap1_llm": cap1_llm}
    }
```

### DSL de Invocación:
```yaml
chain:
  id: ma_chain_arch_v1
  steps:
    - { id: MA-ARCH-PLAN,     input_from: "user", output_to: "ctx.arch" }
    - { id: MA-RESEARCH-GH,   input_from: "ctx.arch.stack", output_to: "ctx.repos" }
    - { id: MA-RESEARCH-WEB,  input_from: "ctx.arch.questions", output_to: "ctx.web" }
    - { id: MA-CODE-GEN,      input_from: "ctx.arch",          output_to: "ctx.code" }
    - { id: MA-CODE-LINT,     input_from: "ctx.code",          output_to: "ctx.lint" }
    - { id: MA-CODE-TEST,     input_from: "ctx.code",          output_to: "ctx.tests" }
    - { id: MA-VERIFY-3CAPAS, input_from: "ctx.code",          output_to: "ctx.verify" }
    - { id: MA-DOC-WRITE,     input_from: "ctx",               output_to: "ctx.doc" }
    - { id: MA-EMIT-REPORT,   input_from: "ctx",               output_to: "report" }
```

---

## 4. PATRONES DE ENCADENAMIENTO

### (a) Secuencial
```
A ─► B ─► C ─► D
```

### (b) DAG Paralelo
```
            ┌─ B ─┐
A ─► ──┬────►     ─► D
        └─ C ──┘
```

### (c) Fractal Anidado
```
        ┌─ A ─► B ─┐
        │            ├─► D
        └─ C ─────┘
```

### Tabla de uso:
| Patrón | Configuración | Caso típico |
|---|---|---|
| Secuencial | chain: linear | ETL, refactor |
| DAG paralelo | chain: dag con parallel_groups | investigación + diseño |
| Fractal anidado | chain: fractal con depth ≤ 5 | arquitectura multi-módulo |

---

## 5. EJEMPLO COMPLETO: ENCADENAR "CREAR MICROSERVICIO E-COMMERCE"

```yaml
chain:
  id: ecommerce_microservice_v1
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget:
    max_tokens: 2_000_000
    max_runtime_h: 24
  steps:
    - { id: MA-ARCH-PLAN,    parallel_group: g1 }
    - { id: MA-RESEARCH-WEB, parallel_group: g1, input_from: "ctx.arch.questions" }
    - { id: MA-RESEARCH-GH,  parallel_group: g1, input_from: "ctx.arch.stack" }
    - { id: MA-RAG-SYNTH,    parallel_group: g2, input_from: ["ctx.web","ctx.repos"] }
    - { id: MA-CODE-GEN,     parallel_group: g3, input_from: "ctx.arch" }
    - { id: MA-CODE-LINT,    parallel_group: g4, input_from: "ctx.code" }
    - { id: MA-CODE-TEST,    parallel_group: g4, input_from: "ctx.code" }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5, input_from: ["ctx.code","ctx.tests"] }
    - { id: MA-DOC-WRITE,    parallel_group: g5, input_from: "ctx" }
    - { id: MA-EMIT-REPORT,  parallel_group: g6, input_from: "ctx" }
  monitor: { pad: true, anxiety: true, drift: true }
  repair:  { pipeline: 5_steps, max_retries: 3 }
  deliv:   { report: "report.md", manifest: "manifest.json" }
```

### Diagrama:
```
            ┌─ MA-ARCH-PLAN ──────┐
            │                     │
g1 ────────►├─ MA-RESEARCH-WEB ──┤
            │                     ├─► MA-RAG-SYNTH
            └─ MA-RESEARCH-GH ───┘                │
                                                 ▼
                                          MA-CODE-GEN
                                                 │
            ┌─ MA-CODE-LINT ─────┐                │
            │                     ├─► MA-VERIFY-3CAPAS
g4 ────────►├─ MA-CODE-TEST ─────┤                │
            │                     │                ▼
            └─────────────────────┘        MA-DOC-WRITE
                                                 │
                                                 ▼
                                          MA-EMIT-REPORT
```

---

## 6. ANÁLISIS DE INFORMACIÓN SEMILLA (PRE-ANÁLISIS)

### Definición:
La "información semilla" es el conjunto de artefactos previos que existen en el repositorio, en state.json, y en el corpus RAG del proyecto.

### Pipeline (5 pasos):
```
seed ─► [S1] indexar ─► [S2] resumir ─► [S3] detectar_gaps
                       │
                       ▼
              [S4] proponer_preguntas ─► [S5] enriquecer_seed
```

| # | Paso | Bloque | Salida |
|---|---|---|---|
| S1 | Indexar repo + state + RAG | MA-INDEX | seed_index.sqlite |
| S2 | Resumir cada artefacto | MA-SUMMARIZE | seed_summary.json |
| S3 | Detectar huecos | MA-GAP-DETECT | seed_gaps.json |
| S4 | Proponer preguntas | MA-QUESTION-GEN | seed_questions.json |
| S5 | Enriquecer seed | MA-RESEARCH-WEB + MA-RESEARCH-GH | seed_enriched.json |

### Métrica de Suficiencia:
```python
evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
)
```

Si `evidence_sufficiency_score >= 0.85` → el sistema puede proceder sin más investigación.
Si `< 0.85` → entra en ciclo de investigación.

---

## 7. CICLOS DE INVESTIGACIÓN (WEB + GITHUB RAG)

### Diseño del Ciclo:
```
   ┌─────────────────────────────────────────────────────────┐
   │              CICLO DE INVESTIGACIÓN                     │
   │                                                         │
   │   ┌────────────┐    ┌────────────┐    ┌────────────┐    │
   │   │ R1: query  │───►│ R2: fetch  │───►│ R3: filter │    │
   │   └────────────┘    └────────────┘    └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │   ┌────────────┐                      ┌────────────┐    │
   │   │ R5: refine │◄──────────replan────│ R4: eval   │    │
   │   └────────────┘                      └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │       new_query                          stop if        │
   │                                           score ≥ 0.85  │
   └─────────────────────────────────────────────────────────┘
```

### Fuentes Prioritarias:
| Tipo | Fuente | Uso |
|---|---|---|
| Web | Wikipedia, OWASP, MDN, arXiv, blogs oficiales | contexto general |
| Web | Documentación oficial de stacks | últimas versiones |
| GitHub | XiaomiMiMo/MiMo-Code, sst/opencode, etc. | patrones de referencia |
| GitHub | awesome-* lists | catálogos curados |
| GitHub | Issues + PRs + Discussions | problemas conocidos |
| GitHub | Releases + changelogs | breaking changes |

### Política:
- Mínimo 2 rondas de investigación por tarea
- Máximo 5 rondas (anti-bucle)
- Cada ronda consume ≤ 50K tokens
- Salida consolidada vía MA-RAG-SYNTH

---

## 8. FLOTA DE SERVIDORES REMOTOS (HuggingFace Spaces)

### Por qué HF Spaces:
- Gratis (CPU basic, T4 small)
- Aislamiento: cada Space es contenedor independiente
- MCP nativo: mcp-hfspace permite invocarlos como tools
- Diversidad de GPUs: CPU, T4, A10G, A100 según plan

### Composición de la flota (10-20 workers):

| # | Space / modelo | Rol | GPU | Latencia |
|---|---|---|---|---|
| 1 | evalstate/FLUX.1-schnell | imágenes | T4 | 5–15 s |
| 2 | hf-audio/whisper-large-v3-turbo | STT | T4 | 1–5 s |
| 3 | microsoft/OmniParser | visión UI | A10G | 2–8 s |
| 4 | Qwen2-VL-72B | VLM | A100 | 5–20 s |
| 5 | gradio/llm-router | LLM | T4 | 2–10 s |
| 6 | nct/rag-search | búsqueda | CPU | 1–3 s |
| 7 | nct/code-runner | ejecución | CPU | 1–5 s |
| 8 | nct/lint-fmt | lint + format | CPU | 0.5–2 s |
| 9 | nct/test-runner | test + coverage | CPU | 5–30 s |
| 10 | nct/security-scan | sast + secrets | CPU | 10–60 s |
| 11 | nct/dream | consolidación | CPU | 60–300 s |
| 12 | nct/distill | destilación | CPU | 60–300 s |
| 13-20 | reservados | failover | mixto | variable |

### Selección Dinámica:
```python
def select_worker(capability: str, sla_ms: int) -> str:
    candidates = workers_by_capability[capability]
    alive = [c for c in candidates if c.health == "ok"]
    feasible = [c for c in alive if c.p95_ms <= sla_ms]
    return min(feasible, key=lambda c: c.cost)
```

### Resiliencia:
- circuit_breaker por Space (umbral: 3 fallos consecutivos)
- backoff_exponential (base 2s, max 5 min)
- failover al siguiente Space disponible de la misma capability

---

## 9. DSL DETERMINISTA (90% CÓDIGO / 10% LLM)

### Regla de Presupuesto:
- 90% código determinista: parseo, validación, transformación, routing, verificación mecánica, formatting, retry, fallback, circuit breaker, EROS compression, checkpoint/restore, schema validation
- 10% LLM: solo en MA-RAG-SYNTH, MA-ARCH-PLAN (parte creativa), Max Mode en decisiones críticas, llm_adversarial_review cuando las 3 capas mecánicas fallan

### DSL Declarativo:
```yaml
step:
  id: MA-VERIFY-3CAPAS
  type: deterministic_with_llm_fallback
  budget:
    code_pct: 90
    llm_pct:  10
    max_tokens: 50_000
  inputs:  { artifact: object, rubric: object }
  outputs: { decision: enum, issues: array }
  code_steps:
    - parse_artifact
    - schema_validate
    - cap1_adversarial
    - cap2_cruzada
    - cap3_maker_checker
  llm_steps:
    - when: "any(cap.issues)"
      call: llm_adversarial_review
      max_tokens: 4_000
      temperature: 0.0
```

### Contador de Presupuesto:
```python
class Budget:
    code_tokens: int = 0
    llm_tokens:  int = 0

    @property
    def llm_pct(self) -> float:
        total = self.code_tokens + self.llm_tokens
        return self.llm_tokens / max(total, 1)

    def enforce(self, target_pct=0.10):
        assert self.llm_pct <= target_pct, "LLM budget exceeded"
```

---

## 10. INVESTIGACIÓN NECESARIA (RAG + WEB + GH) - INTEGRACIÓN

### Por tarea:
```yaml
research:
  sources:
    - type: web
      urls:
        - "https://en.wikipedia.org/wiki/{topic}"
        - "https://owasp.org/..."
        - "https://docs.{stack}.dev/..."
    - type: github
      queries:
        - "{topic} awesome"
        - "{topic} framework stars:>1000"
        - "{topic} site:github.com"
    - type: arxiv
      queries: ["{topic} long horizon agents"]
  rounds: { min: 2, max: 5 }
  early_stop: { metric: evidence_sufficiency_score, threshold: 0.85 }
  synth: { agent: MA-RAG-SYNTH, max_tokens: 8_000 }
```

### Ejemplo: tarea "diseñar sistema RAG multi-tenant":
```yaml
research:
  sources:
    web:
      - "https://docs.llamaindex.ai/en/stable/..."
      - "https://python.langchain.com/docs/..."
      - "https://qdrant.tech/documentation/..."
    github:
      - "rag multi-tenant stars:>500"
      - "vector db benchmark"
      - "awesome-rag"
  rounds: 3
  synth: MA-RAG-SYNTH
  expected_artifacts:
    - "stack_recommendation.md"
    - "security_considerations.md"
    - "performance_benchmark.md"
```

---

## 11. EJEMPLO COMPLETO DE PIPELINE LARGO

### Spec:
> "Diseña, implementa, testea y documenta una API REST multi-tenant para una SaaS de gestión de tareas con autenticación JWT, rate limiting y auditoría, lista para producción en 24h."

### Pipeline:
```yaml
chain:
  id: saas_tasks_api_v1
  pattern: dag
  level: L5_CONTINUOUS_AUTONOMOUS_72H_PLUS
  budget: { max_tokens: 5_000_000, max_runtime_h: 24 }

  research:
    sources:
      web:  ["owasp jwt", "fastapi multi-tenant", "rate limit algorithms"]
      github: ["fastapi-template stars:>1000", "awesome-saas"]
    rounds: { min: 2, max: 4 }

  steps:
    - { id: MA-ARCH-PLAN,     parallel_group: g1 }
    - { id: MA-RESEARCH-WEB,  parallel_group: g1 }
    - { id: MA-RESEARCH-GH,   parallel_group: g1 }
    - { id: MA-RAG-SYNTH,     parallel_group: g2, input_from: [g1] }
    - { id: MA-CODE-GEN,      parallel_group: g3, input_from: [g2] }
    - { id: MA-CODE-LINT,     parallel_group: g4, input_from: [g3] }
    - { id: MA-CODE-TEST,     parallel_group: g4, input_from: [g3] }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5, input_from: [g4] }
    - { id: MA-DOC-WRITE,     parallel_group: g5, input_from: [g3] }
    - { id: MA-EMIT-REPORT,   parallel_group: g6, input_from: [g5] }

  monitor:  { pad: true, anxiety: true, drift: true }
  repair:   { pipeline: 5_steps, max_retries: 3 }
  hf_fleet: { min_workers: 10, max_workers: 20 }
  deliv:    { report: "report.md", manifest: "manifest.json", signed: true }
```

### Diagrama:
```
                ┌─ MA-ARCH-PLAN ────┐
                │                    │
g1 ─────────────►├─ MA-RESEARCH-WEB ─┤
                │                    ├─► MA-RAG-SYNTH
                └─ MA-RESEARCH-GH ──┘                │
                                                   ▼
                                            MA-CODE-GEN
                                                   │
                ┌─ MA-CODE-LINT ───┐                │
                │                    ├─► MA-VERIFY-3CAPAS
g4 ─────────────►├─ MA-CODE-TEST ───┤                │
                │                    │                ▼
                └────────────────────┘         MA-DOC-WRITE
                                                   │
                                                   ▼
                                            MA-EMIT-REPORT

   Monitor: PAD + Anxiety + Drift   ◄──────────┐
                                              │
   HF Fleet: 10–20 spaces             ◄────────┤
                                              │
   Repair: 5 pasos                  ◄──────────┘
```

---

## 12. INTEGRACIÓN CON DOCUMENTO PADRE v100

| Sección v100 | Complemento v200 |
|---|---|
| §0 índice | nuevo bloque JSON con scope_additions |
| §1 niveles | level: L5/L6 ahora pueden usar HF Spaces |
| §2 fusión MiniMax/Kimi K | se añade MiMo Code como tercer polo |
| §3 task models | cada TM puede invocar micro-agentes |
| §4 ALV loops | el QUANTUM_FRACTAL usa la cadena de micro-agentes |
| §5 propuestas | nuevas propuestas PROP-13..PROP-20 |
| §6 diagramas | diagrama adicional de la flota HF |
| §7 contratos YAML | contratos extendidos para micro-agentes |
| §9 entrega | nuevo subpaquete lop_v200/ |

### Nuevas Propuestas (PROP-13 → PROP-20):

| ID | Título | Resumen |
|---|---|---|
| PROP-13 | micro_agents_catalog | 12 micro-agentes especializados |
| PROP-14 | chain_patterns | 3 patrones: secuencial, DAG, fractal |
| PROP-15 | seed_pre_analysis | 5 pasos de pre-análisis |
| PROP-16 | research_cycle | 2-5 rondas, stop por evidencia |
| PROP-17 | hf_spaces_fleet | 10-20 workers remotos MCP |
| PROP-18 | dsl_90_10_budget | 90% código / 10% LLM |
| PROP-19 | mimo_integration |借鉴 MiMo: Max Mode, Goal-Stop, Writer, Dream |
| PROP-20 | oss_backends_router | router entre 15 backends OSS |

---

## 13. INSTRUCCIONES PARA M3 (Mavis)

1. Parsear la sección 0 (JSON SUMMARY) como contrato de entrada y mergearla con el contrato del documento padre v100
2. Construir el grafo de dependencias entre v100 y v200
3. Materializar el árbol de archivos de la sección 12
4. Generar los PRs siguiendo el orden: schemas → micro_agents → dsl → pipelines → backends → hf_spaces → seed → research → proposals
5. Validar que llm_pct ≤ 0.10 en cada pipeline
6. Validar que ningún archivo bajo nct_coordinator/lop_v200/ modifica los 25 bloques originales del software principal
7. Versionar este módulo como 200.0.0 (semver)
8. Reportar al usuario sólo el resumen ejecutivo, los diagramas y los KPIs

---

## 14. RESUMEN EJECUTIVO FINAL

### Total documentos consolidados: 16+
### Total bytes: 195+ KB
### Total patches: 170
### Total código Python: 726 líneas
### Constitución: 1276 líneas
### Memoria persistente: 2 topics

### Estado:
- ✅ Constitución completa (39 principios)
- ✅ CSA completo (10 jueces, 5 fases cada uno)
- ✅ SID completo
- ✅ BIS completo (14 categorías + 13 criterios)
- ✅ Input Engine v4.0 (54 componentes)
- ✅ Output Engine + OOS v3.1 (27 componentes)
- ✅ LOOP v6.0 (15 capas + 3 ciclos)
- ✅ OUTPUT v6.1 (16 capas gobernanza)
- ✅ MAXBRY SUPER TEAM definido
- ✅ 9 modelos GGUF confirmados
- ✅ 16 API keys (3 providers)
- ✅ 5 perfiles API
- ✅ Arquitectura NCT Coordinator
- ✅ M3 + Kimi división
- ✅ Universal Plug v1.5
- ✅ 12 micro-agentes especializados
- ✅ 8 hallazgos de research
- ✅ Sistema Mythos + Fables completo
- ✅ 12 Task Models
- ✅ 5 Loop Versions
- ✅ 12 Propuestas mejoradas

### Pendiente:
- ⏳ Pre-flight data de MAX (8 datos pendientes)
- ⏳ M2.7 no ha instalado nada
- ⏳ HTM y YUAN modelos no encontrados en HF
</content>=== END ===
