
```yaml
total: 170_patches

categoria_cantidad_carpeta:
  ORQUESTADOR_51: /PARCHES-ORQUESTADOR/
  INPUT_V40_9: /PATCHES-INPUT-V40/
  LOOP_V60_15: /PATCHES-LOOP-V60/
  OUTPUT_V61_9: /PATCHES-OUTPUT-V61/
  OUTPUT_V61_gobernanza_16: /PATCHES-OUTPUT-V61-GOBERNANZA/
  PROPUESTAS_INPUT_LOOP_10: /PATCHES-PROPUESTAS-INPUT-LOOP/
  INFRA_8: /PARCHES-INFRA/
  EXTRAS_37: /PARCHES-EXTRAS/
  PARCHES_v14_v17: 4+_raiz
```

### Patches Input V4.0 (9 Propuestas)

```yaml
1_Definition_Score_Gate
2_Semantic_Invariant_Checker
3_Input_Digital_Twin
4_Input_Swarm
5_Confidence_Scoring_Input
6_Multi_Modal_Input
7_Provenance_Chain
8_Auto_Enrichment
9_Input_Drift_Detector
```

### Patches Loop V6.0 (15 Propuestas)

```yaml
1_Repair_Pipeline_5_Steps
2_3_Cycle_Parallel_ABC
3_Checkpoint_Restore
4_Max_Mode_Sampling
5_Goal_Stop
6_Dynamic_Workflow
7_Multi_Source_Research
8_Deterministic_90_10
9_Pre_Analysis_Seed
10_PAD_Monitor
11_Anxiety_Monitor
12_Drift_Monitor
13_Adaptive_Loop
14_Quantum_Fractal
15_Self_Improving_Loop
```

### Patches Infra (8)

```yaml
- 7_HF_Spaces_configuration
- 14_repos_configuration
- 5_Dockerfiles
- Secrets_management
- Networking
- Rate_limit_handling
- Monitoring_infra
- Backup_recovery
```

### Patches Extras (37) — Desglose

```yaml
CSA_fases_10: CSA-F1_a_CSA-F10_uno_por_juez
skills_criterios_13: [criterios_BIS_detallados, debate_4_especialistas, v1_v2_v3_skills]
investigacion_agentes_5: [GitHub, HF, Web, YouTube, MCP_researcher]
hallazgos_research_8: [DeerFlow_2.0, LiteLLM, MAF, AgentOrchestra, OpenCLAW, Hermes, LangGraph, CrewAI]
delivery_destinos_1: 23_destinos_multi_target
```

---

## DOC 14: MiMoCode + LOP v200

### MiMo Code Análisis

```yaml
que_es: [agente_programacion_terminal, MIT, OpenCode, Xiaomi_MiMo, tareas_horizonte_largo_200+_pasos]

3_pilares_arquitectonicos:
  compute:
    problema: error_acumulado
    mecanismos: [Max_Mode, Goal_Stop, Dynamic_Workflow]
  memory:
    problema: contexto_finito
    mecanismos: [Checkpoint_Rebuild, Writer, 4_tier_memory]
  evolution:
    problema: sin_aprendizaje
    mecanismos: [Dream, Distill, project_memory]

stack_tecnico: [Bun, TypeScript, Effect, SolidJS_TUI, Tauri_desktop]
```

### 7 Loops Internos MiMo

```yaml
decision_loop: [cada_turno, tool_call_o_respuesta, conversacion]
checkpoint_loop: [cada_N_turnos, snapshot_firmado, state.jsonl]
writer_loop: [contexto_mayor_70%, resumen, memory_tier-N_md]
max_mode_loop: [decisiones_criticas, K_muestras_voto, efimero]
dream_loop: [cada_7_dias, memoria_consolidada, memory_dream_md]
repair_loop: [en_error, plan_recuperacion, state.jsonl]
evolution_loop: [al_cierre, skill_proc_prompt_nuevo, skills/]
```

### Benchmark MiMo

```yaml
SWE_Bench_Pro_V2: +5%
Terminal_Bench_2: +5%
Ultra_long_200+_steps: beats_Claude_Code
```

### Adaptaciones NCT (Regla: NADA LITERAL)

```yaml
Max_Mode_multi_sample_voting: worker_pool.py_con_k_samples
Goal_Stop: nueva_fase_P9.5_goal_check
Dynamic_Workflow: ALV_LOP_QUANTUM_FRACTAL_NESTED
Checkpoint_Rebuild: state/engine.py_con_replay_to_checkpoint(t)
Writer_subagent: MA-RAG-SYNTH
4_tier_memory: EROS_3_tier_a_4_tiers
Dream: job_cron_weekly_a_MA-DREAM
Distill: job_cron_daily_a_MA-DISTILL
Project_memory: state/project_memory.sqlite
```

### LOP v200 — Ligure Operational Procedure

```yaml
que_es: extension_LOP_v100_que_annade
componentes:
  - 12_micro_agentes_especializados
  - 8_nuevas_propuestas_PROP-13_a_PROP-20
  - integracion_MiMo
  - flota_HF_Spaces

estructura:
  lop_v200/:
    schemas/  # JSON_Schemas
    micro_agents/  # 12_micro_agentes
    dsl/  # DSL_declarativo
    pipelines/  # pipelines_ejecucion
    backends/  # routers_backends
    hf_spaces/  # configuracion_flota_HF
    seed/  # pre_analisis
    research/  # ciclo_investigacion
    proposals/  # PROP-13_a_PROP-20
```

### 12 Micro-Agentes Especializados (Input/Output/Tiempo)

```yaml
MA-CODE-GEN: [spec.md_stack.json, code.zip_+_diff.patch, 5-30s]
MA-CODE-LINT: [code.zip, report.json, 2-10s]
MA-CODE-TEST: [code.zip_tests, junit.xml_+_coverage.json, 10-60s]
MA-RAG-SEARCH: [query_k, chunks.json, 3-15s]
MA-RAG-SYNTH: [chunks.json, answer.md, 5-20s]
MA-DOC-WRITE: [artifacts_audience, doc.md, 5-15s]
MA-ARCH-PLAN: [requirements.json, arch.yaml, 5-30s]
MA-VERIFY-3CAPAS: [artifact_rubric, verdict.json, 10-60s]
MA-REPAIR-5STEP: [failure.json, repaired.json, 30-120s]
MA-RESEARCH-WEB: [urls_depth, pages.jsonl, 30-300s]
MA-RESEARCH-GH: [query_lang_stars, repos.json, 10-60s]
MA-EMIT-REPORT: [state.json, report.md_+_manifest.json, 1-5s]
```

### 8 Nuevas Propuestas (PROP-13 a PROP-20)

```yaml
PROP-13_micro_agents_catalog: catalogo_12_micro_agentes_especializados
PROP-14_chain_patterns: 3_patrones [secuencial, DAG, fractal]
PROP-15_seed_pre_analysis: pipeline_5_pasos_antes_empezar
PROP-16_research_cycle: 2-5_rondas_investigacion
PROP-17_hf_spaces_fleet: flota_10-20_workers_HF_Spaces
PROP-18_dsl_90_10_budget: 90%_codigo_10%_LLM
PROP-19_mimo_integration: integracion_selectiva_MiMo
PROP-20_oss_backends_router: router_15_backends_OSS
```

### Flota HF Spaces (10-20 workers)

```yaml
01_FLUX_1_schnell: [imagenes, T4, 5-15s]
02_whisper_large_v3: [STT, T4, 1-5s]
03_OmniParser: [vision_UI, A10G, 2-8s]
04_Qwen2_VL_72B: [VLM, A100, 5-20s]
05_gradio_llm_router: [LLM, T4, 2-10s]
06_nct_rag_search: [busqueda, CPU, 1-3s]
07_nct_code_runner: [ejecucion, CPU, 1-5s]
08_nct_lint_fmt: [lint_format, CPU, 0.5-2s]
09_nct_test_runner: [test_coverage, CPU, 5-30s]
10_nct_security_scan: [SAST_secrets, CPU, 10-60s]
11_nct_dream: [consolidacion, CPU, 60-300s]
12_nct_distill: [destilacion, CPU, 60-300s]
13-20: [reservados_failover, mixto, variable]
```

### 15 Open Source Backends (OSS)

```yaml
01_OpenCode: 154.5K_stars_TypeScript_75+_LLMs
02_Gemini_CLI: 103.1K_stars_TypeScript_Gemini_free
03_OpenHands: 72.6K_stars_Python_varios
04_Open_Interpreter: 63.4K_stars_Python_local
05_Aider: 44.3K_stars_Python_100+_LLMs
06_Goose: 43.7K_stars_Rust_varios
07_Qwen_Code: 24.1K_stars_TypeScript_Qwen3-Coder
08_Crush: 23.8K_stars_Go_varios
09_Kimi_CLI: 8.4K_stars_Python_Kimi_K2
10_Forge_Code: 7.2K_stars_Rust_300+_modelos
11_MiMo_Code: n_a_TypeScript_MiMo-V2.5
12_Open_Design: n_a_n_a_16_CLIs
13_OpenClaw: n_a_n_a_OpenRouter
14_KiloCode: n_a_TypeScript_Kilo_Gateway
15_Cline: n_a_TypeScript_100+
```

### Router Backends

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

### Ejemplo Completo: E-commerce Microservice

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
  repair: { pipeline: 5_steps, max_retries: 3 }
```

### Conclusión LOP v200

```yaml
annade:
  - 12_micro_agentes_especializados
  - 3_patrones_encadenamiento
  - 5_pasos_pre_analisis
  - 2-5_rondas_research
  - 10-20_workers_HF_Spaces
  - router_15_backends_OSS
  - 8_propuestas_nuevas
  - integracion_selectiva_MiMo
extension: poderosa_del_LOP_v100_original
```

---

## DOC 16: MiMoCode / LOP v200 / Investigación

### Información Semilla — Pipeline Pre-Análisis (5 pasos)

```yaml
seed_pipeline_5_pasos:
  S1_indexar: MA-INDEX → seed_index.sqlite  # repo + state + RAG
  S2_resumir: MA-SUMMARIZE → seed_summary.json
  S3_detectar_gaps: MA-GAP-DETECT → seed_gaps.json
  S4_proponer_preguntas: MA-QUESTION-GEN → seed_questions.json
  S5_enriquecer: MA-RESEARCH-WEB + MA-RESEARCH-GH → seed_enriched.json

metrica_suficiencia: |
  evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
  )
umbral_proceder: score >= 0.85
```

### Ciclo Investigación Detallado

```yaml
fases:
  R1_query
  R2_fetch
  R3_filter
  R4_eval: si_score >= 0.85_stop
  R5_refine: replan_si_no_pasa

fuentes_prioritarias:
  web: [Wikipedia, OWASP, MDN, arXiv, blogs_oficiales, documentacion_oficial_stacks]
  github: [XiaomiMiMo_MiMo-Code, sst_opencode, awesome_lists, issues_PRs_discussions, releases_changelogs]

politica:
  rondas_min: 2
  rondas_max: 5  # anti_bucle
  tokens_por_ronda: menor_igual_50K
  sintesis_final: MA-RAG-SYNTH
```

### Catálogo 12 Micro-Agentes — Tabla Maestra

```yaml
MA-CODE-GEN: [genera_codigo_desde_spec, spec.md_stack.json → code.zip_+_diff.patch, 5-30s]
MA-CODE-LINT: [lint_format_type_check, code.zip → report.json, 2-10s]
MA-CODE-TEST: [unit_integration_mutation, code.zip_tests → junit.xml_+_coverage.json, 10-60s]
MA-RAG-SEARCH: [busqueda_vectorial_+_rerank, query_k → chunks.json_con_citas, 3-15s]
MA-RAG-SYNTH: [sintetiza_respuesta_citas, chunks.json → answer.md, 5-20s]
MA-DOC-WRITE: [documenta_arquitectura_decisiones, artifacts_audience → doc.md, 5-15s]
MA-ARCH-PLAN: [planifica_arquitectura_stack, requirements.json → arch.yaml, 5-30s]
MA-VERIFY-3CAPAS: [verificacion_adversarial_3_capas, artifact_rubric → verdict.json, 10-60s]
MA-REPAIR-5STEP: [pipeline_5_pasos_reparacion, failure.json → repaired.json_o_escalate, 30-120s]
MA-RESEARCH-WEB: [crawling_+_extraccion, urls_depth → pages.jsonl, 30-300s]
MA-RESEARCH-GH: [busqueda_github_API, query_lang_stars_min → repos.json, 10-60s]
MA-EMIT-REPORT: [empaqueta_resultado_final, state.json → report.md_+_manifest.json, 1-5s]
```

### Ejemplo MA-VERIFY-3CAPAS

```python
SCHEMA_IN = "nct.verify.in.v1"
SCHEMA_OUT = "nct.verify.out.v1"

def run(artifact, rubric, k_samples=3):
    # 90% codigo determinista, 10% LLM solo si adversarial_check falla
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
        "issues": issues,
        "evidence": {"cap1": cap1, "cap2": cap2, "cap3": cap3, "cap1_llm": cap1_llm}
    }
```

### DSL Invocación Cadena Micro-Agentes

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

### 3 Patrones de Encadenamiento

```yaml
secuencial: A → B → C → D
dag_paralelo: A → {B, C} → D
fractal_anidado: {A→B, C} → D  # depth <= 5

uso:
  - secuencial: chain_linear, ETL_refactor
  - dag_paralelo: chain_dag_con_parallel_groups, investigacion_diseño
  - fractal_anidado: chain_fractal_con_depth_<=5, arquitectura_multi_modulo
```

### DSL Determinista (90/10)

```yaml
regla_presupuesto:
  90%_codigo_determinista: [parseo, validacion, transformacion, routing, verificacion_mecanica, formatting, retry, fallback, circuit_breaker, EROS_compression, checkpoint_restore, schema_validation]
  10%_LLM: [MA-RAG-SYNTH, MA-ARCH-PLAN_parte_creativa, Max_Mode_decisiones_criticas, llm_adversarial_review_cuando_3_capas_mecanicas_fallan]

step_yaml_ejemplo: |
  step:
    id: MA-VERIFY-3CAPAS
    type: deterministic_with_llm_fallback
    budget: { code_pct: 90, llm_pct: 10, max_tokens: 50_000 }
    inputs: { artifact: object, rubric: object }
    outputs: { decision: enum, issues: array }
    code_steps: [parse_artifact, schema_validate, cap1_adversarial, cap2_cruzada, cap3_maker_checker]
    llm_steps:
      - when: "any(cap.issues)"
        call: llm_adversarial_review
        max_tokens: 4_000
        temperature: 0.0

contador_presupuesto: |
  class Budget:
    code_tokens: int = 0
    llm_tokens:  int = 0
    @property llm_pct: llm_tokens / total
    enforce(target_pct=0.10): assert llm_pct <= target_pct
```

### Investigación por Tarea

```yaml
research:
  sources:
    - type: web
      urls: [wikipedia, owasp, docs_stacks, blogs_oficiales]
    - type: github
      queries: [topic_awesome, topic_framework_stars_>1000, topic_site_github]
    - type: arxiv
      queries: [topic_long_horizon_agents]
  rounds: { min: 2, max: 5 }
  early_stop: { metric: evidence_sufficiency_score, threshold: 0.85 }
  synth: { agent: MA-RAG-SYNTH, max_tokens: 8_000 }

ejemplo_tarea_RAG_multi_tenant:
  sources:
    web: [docs_llamaindex, docs_langchain, qdrant_docs]
    github: [rag_multi_tenant_stars_>500, vector_db_benchmark, awesome_rag]
  rounds: 3
  synth: MA-RAG-SYNTH
  expected_artifacts: [stack_recommendation.md, security_considerations.md, performance_benchmark.md]
```

### Ejemplo Completo Pipeline Largo: SaaS API

```yaml
chain:
  id: saas_tasks_api_v1
  pattern: dag
  level: L5_CONTINUOUS_AUTONOMOUS_72H_PLUS
  budget: { max_tokens: 5_000_000, max_runtime_h: 24 }
  research:
    sources:
      web: [owasp_jwt, fastapi_multi_tenant, rate_limit_algorithms]
      github: [fastapi-template_stars_>1000, awesome_saas]
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
  monitor: { pad: true, anxiety: true, drift: true }
  repair: { pipeline: 5_steps, max_retries: 3 }
  hf_fleet: { min_workers: 10, max_workers: 20 }
  deliv: { report: report.md, manifest: manifest.json, signed: true }
```

### Diagrama SaaS API

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
   Monitor: PAD+Anxiety+Drift ←──┐
   HF Fleet: 10-20 spaces ←───────┤
   Repair: 5 pasos ←─────────────┘
```

### Integración v100 → v200

```yaml
v100_seccion_a_v200_complemento:
  s0_indice: nuevo_bloque_JSON_scope_additions
  s1_niveles: level_L5_L6_pueden_usar_HF_Spaces
  s2_fusion: añade_MiMo_Code_como_tercer_polo
  s3_task_models: cada_TM_puede_invocar_micro_agentes
  s4_ALV_loops: QUANTUM_FRACTAL_usa_cadena_micro_agentes
  s5_propuestas: nuevas_PROP-13_a_PROP-20
  s6_diagramas: adicional_flota_HF
  s7_contratos_YAML: extendidos_para_micro_agentes
  s9_entrega: nuevo_subpaquete_lop_v200
```

### Instrucciones para M3

```yaml
1: parsear_seccion_0_JSON_SUMMARY_como_contrato_entrada_mergear_con_contrato_padre_v100
2: construir_grafo_dependencias_v100_v200
3: materializar_arbol_archivos_seccion_12
4: generar_PRs_orden: [schemas, micro_agents, dsl, pipelines, backends, hf_spaces, seed, research, proposals]
5: validar_llm_pct_menor_igual_0.10_en_cada_pipeline
6: validar_ningun_archivo_nct_coordinator_lop_v200_modifica_25_bloques_originales
7: versionar_este_modulo_como_200.0.0_semver
8: reportar_usuario_solo_resumen_ejecutivo_diagramas_KPIs
```

### Resumen Ejecutivo Final

```yaml
documentos_consolidados: 16+
bytes: 195+_KB
patches: 170
codigo_python: 726_lineas
constitucion: 1276_lineas
memoria_persistente: 2_topics
aplicado:
  - constitucion_39_principios
  - CSA_10J_5F
  - SID
  - BIS_14_categorias_13_criterios
  - Input_Engine_v4_54
  - Output_Engine_+_OOS_v3.1_27
  - LOOP_v6_15_capas_3_ciclos
  - OUTPUT_v6.1_16_capas_gobernanza
  - MAXBRY_SUPER_TEAM
  - 9_GGUF
  - 16_API_keys
  - 5_perfiles_API
  - Arquitectura_NCT_Coordinator
  - M3_Kimi_division
  - Universal_Plug_v1.5
  - 12_micro_agentes
  - 8_hallazgos_research
  - Mythos_Fables
  - 12_Task_Models
  - 5_Loop_Versions
  - 12_Propuestas_mejoradas
pendiente:
  - pre_flight_8_datos_MAX
  - M2.7_no_ha_instalado
  - HTM_YUAN_modelos_no_encontrados_HF
```

---

## DOC 29: Auditoría Final Definitiva

### 20 Gaps Encontrados y Cerrados

```yaml
gap_1_skyner_consenso: SKYNER_17_modelos_G7+G8_veto_AUTO_BOTH_multi_round → cerrado en MASTER-25
gap_2_nombres_especificos: TM01_ARCHITECTURE_DESIGN_ALV_LOP_GENESIS_BASELINE → cerrado en MASTER-26
gap_3_8_archivos_coordinador: fsm_classifier_router_planner_context_isolator_worker_pool_monitor_verifier → cerrado en MASTER-26
gap_4_G6_staff: MiniMax_M3_MiMo_Code_OpenCLAW_Smolagents_Hermes_Code_Agent_CLI → cerrado en MASTER-26
gap_5_8_schemas: TASK_TASK_HISTORY_STATE_BLACKBOARD_INBOX_OUTBOX_EVENTS_PROJECT_ROOT → cerrado en MASTER-26
gap_6_12_estados_listas: INBOX_OUTBOX_STATE_HISTORY_TASKS_4_listas_BLACKBOARD_REPORT_TELEGRAM_LOG → cerrado en MASTER-26
gap_7_ubicaciones_sync: /workspace/orquestador/*_a_nct-consensus-log_git_pull_30s_push_5min → cerrado en MASTER-26
gap_8_3_monitores_umbrales: PAD_Arousal>0.8_Pleasure<0.2_SIGKILL_Ansiedad_3_niveles_Anti_Drift_KL>0.02 → cerrado en MASTER-26
gap_9_10_fases: F0_a_F9_Kimi_MiniMax → cerrado en MASTER-26_y_28
gap_10_6_niveles_detalle: L1_a_L6_con_IA_y_memoria_y_repair → cerrado en MASTER-26
gap_11_16_practicas_EROSTAS_+_4: cache_fallback_checkpoint_retry_rollback_auditoria_preview_notificacion + 4 → cerrado en MASTER-26
gap_12_20_propuestas_100X: encryption_vault_backup_1h_health_60s_logs_centralizados_webhooks + 14 → cerrado en MASTER-26
gap_13_parches_operacionales: Circuit_Breaker_pybreaker_Free_Tier_Telegram_5_topics_ChromaDB_BGE_small → cerrado en MASTER-26
gap_14_parches_loop_V60_detalle: A-O_15_patches → cerrado en MASTER-27
gap_15_parches_output_V61_gobernanza: A-P_16_patches → cerrado en MASTER-27
gap_16_parches_input_V40: A-I_9_patches → cerrado en MASTER-27
gap_17_13_criterios_skills: 01_relevancia_a_13_comunidad → cerrado en MASTER-27
gap_18_10_propuestas_avanzadas: meta_agentes_causalidad_counterfactual_auto_modificacion + 6 → cerrado en MASTER-27
gap_19_30_skills_recomendados: workflow_5_arquitectura_4_agentes_5_MCP_3_gestion_3 → cerrado en MASTER-27
gap_20_razonamiento_externo: 16_etapas_35_pasos_67_pasos_40_MYTHOS_5_FABLES_9_DRE_4_escenarios → cerrado en MASTER-28
```

### Inventario 29 Master Docs (con bytes)

```yaml
01_vision_general: 12701
02_estructura_organizacional: 9892
03_constitucion_completa: 8170
04_csa_completo: 7093
05_sid_bis: 7308
06_input_engine: 5326
07_output_engine: 5805
08_loop: 4803
09_agentes: 5570
10_modelos_apis: 4273
11_razonamiento_mythos: 5195
12_pipeline_fases: 4518
13_arquitectura_nct: 5639
14_mimo_lop_v200: 7797
15_reglas_intocables: 5133
16_dsl_universal_plug: 6386
17_configuraciones_costos: 4968
18_patches_extras: 5443
19_pre_flight_pendientes: 4894
20_validacion_cruzada_final: 9249
21_subsistemas_detallados: 7650
22_ejemplos_paso_a_paso: 9671
23_implementacion_deploy: 9359
24_auditoria_final: 12336
25_skyner_consenso_detallado: 8257_nuevo
26_nomenclatura_detallada: 8298_nuevo
27_parches_detallados_faltantes: 9138_nuevo
28_razonamiento_externo_detallado: 7460_nuevo
29_auditoria_final_definitiva: este_doc
total: 210231_bytes / 29_documentos
```

### Cobertura Final Verificada

```yaml
constitucional: [39_principios_v1.0_v2.0_v3.0, 10_jueces_CSA_5_fases, 5_preguntas_SID, 14_BIS_+_13_criterios]

engines: [Input_Engine_v4_54, Output_Engine_13_+_OOS_14_+_OVFS, LOOP_v6_15_capas_3_ciclos, OUTPUT_v6.1_16_gobernanza]

agentes: [30_micro, 11_internal_roles, 10_parallel_queues, 6_niveles_autonomia, 12_TM_nombres_especificos, 5_loop_versions_nombres_especificos, 3_monitores_umbrales, 5_consenso, 5_investigacion, 5_officers, 10_consejo, 12_especializados_v200, G6_staff_MiMo_OpenCLAW_Smolagents_Hermes_Aider_Cline]

razonamiento: [EURS_Standard_5+12, EURS_Turbo_12+45, Mythos_40, FABLES_5, CHEF_FINAL_4, DRE_9, OpenMythos, 16_etapas_cadena_estructurada, 35_pasos_metodo_v2, 67_pasos_MASTER_STRUCTURE, Bloque_X_Refutacion, EROS_3_tier]

infraestructura: [SKYNER_17_modelos_G7+G8, confidence_scoring_veto, AUTO_BOTH, multi_round_re_invocation, fallback_auto, 9_GGUF, 16_API_keys, 3_perfiles, 7_HF_Spaces, 14_repos, 5_Dockerfiles]

pipeline: [10_fases_Kimi+MiniMax, fase_0.5_confirmation_gate, 4_escenarios_9/16/25/30-50_pasos, 8_archivos_NCT_Coordinator, 5_archivos_soporte]

parches: [170+_documentados, 9_OUTPUT_M3_aplicadas, 1_OUTPUT_rechazada, 10_INPUT/LOOP_M3_aplicadas, 10_propuestas_avanzadas, 16_EROSTAS_+_4, 20_propuestas_100X, 13_criterios_skills, parches_operacionales, 30_skills_recomendados]

reglas: [regla_absoluta_MAX, cosas_intocables, 5_GOALS_12_PASOS, 7_pasos_adicionales, validacion_por_salida, MI-SYSTEM-PROMPT-OPERATIVO]

memoria_estado: [8_schemas_JSON, 12_archivos_estado_listas, ubicaciones_sync, ChromaDB_nct_memory, BGE-small-en-v1.5_embedding]

universal_plug: [DSL_DAG, Universal_Plug_v1.5, Universal_Module_Contract_JSON_Schema, Nexus, 23_destinos_multi_target]
```

### Métricas Finales

```yaml
total_master_docs: 29
total_bytes: ~210_KB
constitucion_principios: 39
CSA_jueces: 10
CSA_fases_por_juez: 5
SID_preguntas: 5
BIS_categorias: 14
BIS_criterios_skills: 13
Input_Engine_componentes: 54
Output_Engine_+_OOS: 27
LOOP_capas: 15
LOOP_ciclos: 3
OUTPUT_gobernanza: 16
micro_agentes: 30
internal_roles: 11
colas_paralelas: 10
niveles_autonomia: 6
task_models: 12
loop_versions: 5
monitores: 3
modelos_GGUF: 9
modelos_SKYNER_G7+G8: 17
API_keys: 16
perfiles_API: 3
agentes_staff_G6: 6
agentes_principales_5+5+10+5: 25
agentes_consenso: 5
agentes_investigacion: 5
officers: 5
destinos_multi_target: 23
HF_Spaces: 7
repos_GitHub: 14
Dockerfiles: 5
parches_documentados: 170+
propuestas_M3_aplicadas: 19
propuestas_M3_rechazadas: 1
propuestas_avanzadas: 10
mejores_practicas_EROSTAS: 20
propuestas_100X: 20
skills_recomendados: 30
schemas_JSON: 8
archivos_estado_listas: 12
archivos_NCT_Coordinator: 13
MYTHOS_pasos: 40
EURS_Standard: 5+12
EURS_Turbo: 12+45
cadena_estructurada_etapas: 16
metodo_v2_pasos: 35
MASTER_STRUCTURE_pasos: 67
FABLES_fases: 5
DRE_pasos: 9
LISTA_GLOBAL_reglas: 4
CHEF_FINAL_pasos: 4
EROS_tiers: 3
```

### Estado Final

```yaml
cobertura: 100%
sin_contradicciones: yes
tamanos_respetados: yes  # cada_doc_menor_igual_60K
referencias_validas: yes
```

### Lo que Falta (NO es info del orquestador)

```yaml
- 8_datos_pre_flight_MAX_credenciales
- confirmacion_HTM_YUAN_modelos
- aprobacion_final_MAX
- orden_M2.7_instalar
```

### Conclusión Definitiva

```yaml
MAXBRY_SUPER_TEAM: 100%_documentado_en_29_Master_Docs_+_18_Consolidados_=_47_documentos
conocimiento_capturado:
  - arquitectura
  - constitucion
  - engines
  - agentes
  - modelos_APIs
  - razonamiento
  - pipeline
  - parches
  - reglas
  - memoria_estado
  - universal_plug
  - pre_flight
  - implementacion
  - auditoria
listo_implementacion: cuando_MAX_de_GO
```

---

## DOC 27: Parches Detallados Faltantes

### 15 Parches Loop V60 (Detallados)

```yaml
A_workflow_dag: [workflow_como_DAG_explicito, cada_nodo=paso, edges=dependencias, topological_sort, validacion_sin_ciclos]
B_runtime_kernel: [runtime_como_kernel_SO, process_management, memory_management, IPC, scheduling]
C_event_sourcing: [fuente_de_verdad, cada_cambio=evento, estado=replay_eventos, auditoria_completa, time_travel_debugging]
D_state_machine: [FSM_control_flujo, estados_explicitos, transiciones_validadas, eventos_disparan, visualizacion]
E_prediction_engine: [prediccion_outcomes, basado_en_historico, predice_exito_fallo, predice_duracion, predice_costo]
F_dynamic_replanning: [detecta_desviacion, genera_plan_alternativo, aplica_si_score_cae]
G_model_router: [router_inteligente, por_capacidad, por_costo, por_latencia, fallback_automatico]
H_trust_engine: [motor_confianza, cada_dato_agente_modelo_tiene_score, score_0-100, se_actualiza_con_feedback, afecta_decisiones]
I_goal_monitor: [verifica_output_cumple_goals, alerta_si_diverge, trigger_replanning]
J_contract_engine: [motor_contratos, define_contratos_input_output, valida_cumplimiento, genera_evidencia]
K_resource_economy: [economia_recursos, presupuesto_por_tarea, contador_tiempo_real, throttling_si_excede]
L_semantic_diff: [diff_semantico_no_syntax, detecta_cambios_sutiles, trigger_si_semantic_drift>0.10]
M_universal_artifact_graph: [grafo_universal_artefactos, todos_outputs_son_nodos, relaciones_entre_artefactos, tracking_completo]
N_failure_recovery: [recuperacion_fallos, detecta_tipo, aplica_estrategia, 5_pasos]
O_executive_board: [5_officers, supervisan_funcionamiento_global, reportan_MAX]
```

### 16 Parches Output V6.1 Gobernanza (Detallados)

```yaml
A_output_governor: [gobierna_output, decide_cuando_emitir, decide_formato, decide_destino]
B_output_digital_twin: [gemelo_digital, simula_antes_emitir, detecta_problemas, reduce_fallos_70%]
C_multi_version_generator: [genera_N_versiones, diferentes_audiencias, compara_selecciona]
D_output_fusion: [combina_mejores_partes, elimina_redundancia, sintesis_final]
E_acceptance_test: [verifica_contra_criterios, score_aceptacion, go_no_go]
F_coverage_map: [que_cubre, que_NO_cubre, gaps_identificados]
G_explainability: [por_que_generado_asi, que_info_usó, cadena_razonamiento]
H_output_provenance: [origen_datos, cadena_custodia, hash_firmado]
I_consistency_swarm: [multiples_agentes_verifican, detectan_inconsistencias, corrigen]
J_artifact_graph: [relaciones_entre_outputs, versiones, dependencias]
K_release_manager: [decide_cuando_liberar, versiona_output, gestiona_rollout]
L_output_memory: [guarda_outputs_pasados, permite_re_emision, auditoria_historica]
M_output_score: [calcula_score_0-100, umbral_95%_requerido, multiples_dimensiones]
N_human_approval: [MAX_aprueba, workflow_aprobacion, tracking]
O_adaptive_delivery: [aprende_patron_MAX, decide_formato_destino_optimo]
P_closed_feedback_loop: [publicar_uso_real_feedback_memoria_reglas, mejora_continua]
```

### 9 Parches Input V40 (Detallados)

```yaml
A_input_swarm_bus: [40-60_agentes_paralelo, bus_eventos_compartido, distribucion_carga_dinamica, comunicacion_asincrona]
B_input_discovery: [10_detectores, idioma_dominio_intencion_objetivos_restricciones_prioridades_entregables_formato_audiencia_dependencias]
C_input_forensics: [10_detectores, contradicciones_ambiguedad_huecos_requisitos_ocultos_riesgos_datos_inventados_inconsistencias_conflictos_imposibilidades_scope]
D_knowledge_discovery: [15_fuentes, papers_stackoverflow_reddit_skills_internos_base_conocimiento_memoria_artefactos_APIs_plugins_modelos_docs_repos_issues_wikis_foros]
E_claude_definition_engine: [6_fases, auto_respuesta_multi_interpretacion_simulacion_arbol_decisiones_preguntas_agrupadas_definition_score_>=95%]
F_input_compiler: [5_grafos, knowledge_graph_goal_tree_requirement_tree_constraint_tree_context_graph]
G_quality_swarm: [10_auditores_con_veto, bloquea_si_vetan, devuelve_paquete_correccion]
H_input_governor: [6_estados, RECIBIDO_ANALIZANDO_DEFINIENDO_COMPILANDO_AUDITANDO_APROBADO_VETADO_REPLANIFICAR_PREGUNTAR]
I_input_digital_twin: [simulacion_completa_antes_ejecutar, detecta_problemas_antes_consumir_recursos, solo_si_definition_score>=95%]
```

### Capacidades Detalladas

```yaml
capacidad_actual_HF_Spaces:
  spaces: 7_x_16GB = 112GB
  uso_modelos: ~13.5GB
  margen_libre: 87%

capacidad_objetivo:
  agentes: 2000+_capacidad
  tareas_simultaneas: 1000+
  tareas_dia: 1000-2000+

limitaciones:
  - HF_Spaces_pueden_dormirse
  - rate_limits_APIs
  - cold_starts
  - 16GB_max_por_Space
```

### 30 Skills Recomendados (Categorías)

```yaml
workflow_5:
  - Temporal
  - Kestra
  - Airflow
  - Dagster
  - Prefect

arquitectura_6:
  - Structurizr
  - C4_Model
  - arc42
  - PlantUML
  - Mermaid
  - diagrams_net

agentes_10:
  - LangGraph
  - CrewAI
  - OpenAI_Agents_SDK
  - LlamaIndex
  - Mem0
  - LangMem
  - AutoGen
  - MAF
  - DSPy
  - Haystack

MCP_integracion_3:
  - MCP
  - Smithery
  - Composio

gestion_3:
  - Plane
  - OpenProject
  - Taiga
```

### 13 Criterios Skills (Puntuación)

```yaml
01_relevancia: [es_relevante_dominio, resuelve_problema_real, score_0-10]
02_efectividad: [resuelve_problema, tasa_exito, score_0-10]
03_costo: [costo_ejecucion, costo_efectivo, score_0-10]
04_compatibilidad: [compatible_stack, compatible_skills, score_0-10]
05_mantenibilidad: [facil_mantener, facil_actualizar, score_0-10]
06_documentacion: [README, ejemplos, score_0-10]
07_reusabilidad: [reusable, contextos_multiples, score_0-10]
08_seguridad: [seguro, sin_vulnerabilidades, score_0-10]
09_performance: [rapido, p50_p95_p99, score_0-10]
10_escalabilidad: [escala, tareas_simultaneas, score_0-10]
11_compliance: [cumple_regulaciones, GDPR_HIPAA, score_0-10]
12_test_coverage: [tiene_tests, coverage_mayor_igual_80%, score_0-10]
13_comunidad: [comunidad, maintained, score_0-10]
```

### 10 Propuestas Avanzadas Input/Loop

```yaml
01_meta_agentes: [agentes_orquestan_otros_agentes, nivel_meta, auto_gestion]
02_causalidad: [razonamiento_causal_no_correlacional, identifica_causa_raiz, predice_efectos]
03_counterfactual: [que_hubiera_pasado_si, analisis_contrafactual, aprendizaje_decisiones]
04_auto_modificacion: [sistema_se_modifica_si_mismo, basado_en_feedback, con_aprobacion]
05_memoria_episodica: [memoria_episodios_especificos, contexto_completo, retrieval_similitud]
06_zero_shot_transfer: [transferir_conocimiento_dominios, sin_entrenamiento, generalizacion]
07_nas: [neural_architecture_search, busca_arquitectura_optima, automaticamente, por_tarea]
08_time_travel: [volver_estado_anterior, debugging_temporal, auditoria]
09_inteligencia_colectiva: [multiples_agentes_colaboran, inteligencia_emergente, swarm_intelligence]
10_auto_curriculum: [sistema_disena_propio_curriculum, aprende_progresivamente, adaptativo]
```

---

## DOC 19: Pre-Flight + Dependencias

### 8 Datos Pre-Flight Pendientes

```yaml
github:
  username: pendiente
  PAT_scopes: [repo, workflow, admin_org_si_aplica]

huggingface:
  username: pendiente
  tokens: 6  # uno_por_Space_principal

API_keys_16_total:
  NVIDIA_NIM: 4
  Cerebras: 6
  Groq: 6
  formato: provider-numero-uso

database:
  turso_URL: pendiente
  turso_token: pendiente

otros:
  visibility: public_o_private
  telegram_bot_token: BotFather
  HTM_model_name: no_encontrado_HF
  YUAN_model_name: no_encontrado_HF
```

### Aprovisionamiento Automático (7 Pasos)

```yaml
paso_1: crear_14_repos_GitHub  # 6_grupos + 8_productos
paso_2: crear_7_HF_Spaces  # 1_por_grupo + extras, cada_uno_propio_token
paso_3: escribir_5_Dockerfiles
paso_4: inyectar_secretos  # API_keys_GitHub_Secrets, tokens_HF_Secrets, credenciales_encriptadas
paso_5: configurar_profiles  # conservador_equilibrado_agresivo
paso_6: arrancar_orquestador  # bootstrap_autonomo, conexion_G1-G6, reporte_MAX
paso_7: reporte_MAX  # URLs_acceso, comandos_utiles, estado_Space_repos
```

### 14 Repos GitHub

```yaml
grupos_6:
  - nct-g1-infra
  - nct-g2-core
  - nct-g3-ui
  - nct-g4-audit
  - nct-g5-orquestador  # ⭐
  - nct-g6-asistentes

productos_8:
  - nct-product-01
  - nct-product-02
  - nct-product-03
  - nct-product-04
  - nct-product-05
  - nct-product-06
  - nct-product-07
  - nct-product-08
```

### 7 HF Spaces

```yaml
- mavis/g1-infra
- mavis/g2-core
- mavis/g3-ui
- mavis/g4-audit
- mavis/g5-orquestador  # ⭐
- mavis/g6-asistentes
- mavis/extras
```

### M2.7 (Responsable de Instalación)

```yaml
quien_es: sesion_dedicada_instalacion  # NO_diseña_arquitectura

hace:
  - lee_CONSTITUCION-ORQUESTADOR_md
  - lee_18_master_docs
  - lee_patches_aprobados
  - ejecuta_aprovisionamiento_automatico
  - reporta_MAX

NO_hace:
  - modificar_arquitectura
  - inventar
  - reemplazar_originales
  - crear_nuevas_categorias_sin_aprobacion

bloqueos: si_datos_faltantes_escala_MAX  # si_inconsistencias_escala_MAX
```

### Dependencias entre Grupos (Secuencia de Instalación)

```yaml
G1_INFRA ← G2_CORE ← G3_UI
   ↓           ↓         ↓
   └───► G4_AUDIT ◄─────┘
              ↓
        G5_ORQUESTADOR  # ⭐
              ↓
        G6_ASISTENTES

orden_instalacion:
  1_G1_INFRA: crea_HF_Spaces_GitHub_Docker
  2_G6_ASISTENTES: carga_modelos
  3_G2_CORE: BIS_SID_Input_Output
  4_G4_AUDIT: CSA
  5_G5_ORQUESTADOR: MAXBRY
  6_G3_UI: interfaz_MAX
```

### Estado M2.7

```yaml
actual:
  - NO_ha_instalado_nada
  - espera_datos_pre_flight_MAX
  - espera_aprobacion_arquitectura_final

cuando_arranque:
  1: verifica_entorno_python_network_secrets
  2: crea_estructura_carpetas
  3: clona_template_base
  4: configura_profiles
  5: crea_recursos_externos_con_pre_flight
  6: inyecta_secretos
  7: arranca_servicios
  8: reporta
```

### Checklist Pre-Arquitectura

```yaml
completado_18_items:
  - Constitucion_v3.0_39_principios
  - CSA_10_jueces_5_fases
  - SID_5_preguntas
  - BIS_14_categorias_13_criterios
  - Input_Engine_v4.0_54_componentes
  - Output_Engine_+_OOS_v3.1_27_componentes
  - LOOP_v6.0_15_capas_3_ciclos
  - OUTPUT_v6.1_16_capas_gobernanza
  - MAXBRY_SUPER_TEAM_definido
  - 30_micro_agentes_11_roles_10_colas_6_niveles
  - 12_Task_Models
  - 5_Loop_Versions
  - 3_Monitores
  - 9_modelos_GGUF
  - 16_API_keys
  - 19_propuestas_M3_aplicadas_1_rechazada
  - 170_patches_documentados
  - 18_Master_Documentos_completos

pendiente_3_items:
  - 8_datos_pre_flight_MAX
  - aprobacion_final_MAX
  - M2.7_orden_instalacion
```

### Recomendaciones para MAX

```yaml
perfil_recomendado: equilibrado  # balance_costo_calidad
canales_prioritarios: [Telegram, API_REST]
proyectos_iniciales: pendiente_decision
visibilidad: pendiente_decision
```

---

## DOC 21: Subsistemas Detallados

### System Prompt Mythos (15 Secciones)

```yaml
s1_identidad: "MAXBRY SUPER TEAM es el orquestador universal distribuido para IA"
s2_mision: "Coordinar agentes, herramientas, proyectos y objetivos para MAX"
s3_valores: [determinismo, trazabilidad, resiliencia, auto_mejora, costo_$0]
s4_principios: 39_principios_Constitucion
s5_arquitectura: [USUARIO, MAXBRY, Control_Layer, Workflow_Layer, Memory_Layer, Tool_Layer, LLM_Layer]
s6_capacidades: [2000+_agentes, 1000+_tareas, multi_modelo, auto_evolucion]
s7_limites: [costo_$0, HF_free_tier, 16GB_RAM_por_Space]
s8_interaccion: [Telegram, API_REST, Dashboard, CLI]
s9_outputs: [23_destinos, adaptive_format, multi_target]
s10_validacion: [5_GOALS_12_PASOS, confidence_scoring_>=95%, CSA_audit]
s11_seguridad: [secretos_encriptados, audit_log, OWASP_compliance]
s12_operacion: [90%_codigo_10%_LLM, multi_modelo, 3_perfiles_API]
s13_aprendizaje: [Meta_Learning, Self_Improving, Counterfactual_reasoning]
s14_reporte: [estado, metricas, alertas]
s15_cierre: "Reporto a MAX. Escala a MAX si es crítico"
```

### 13 Criterios Skills Individuales

```yaml
criterio_1_nombre_claro: [identifica_skill, patron_snake_case, ejemplo_code_generator]
criterio_2_descripcion_concisa: 1-2_oraciones_que_no_como
criterio_3_categoria_valida: una_de_A-N_BIS
criterio_4_inputs_tipados: schema_JSON_required_optional
criterio_5_outputs_tipados: schema_JSON_siempre_definido
criterio_6_tiempo_medio: estimacion_realista_p50_p95_p99
criterio_7_recursos: [CPU, RAM, disk, modelo_si_LLM]
criterio_8_dependencias: [skills_requeridas, versiones]
criterio_9_tests: minimo_3_unit_tests_coverage_>=80%
criterio_10_documentacion: [README.md, ejemplos]
criterio_11_ejemplos: minimo_2_real_world_use_cases
criterio_12_version_semver: MAJOR_MINOR_PATCH_1.2.3
criterio_13_mantenedor: [owner_asignado, contacto]
```

### 4 Especialistas Debate Skills

```yaml
arquitecto_pregunta: es_coherente_con_arquitectura
implementador_pregunta: es_implementable_con_recursos_actuales
tester_pregunta: es_testeable_como_se_prueba
critico_pregunta: vale_la_pena_costo_beneficio

voto:
  4-0: skill_excelente
  3-1: skill_aprobada_con_notas
  2-2: escala_MAX
  1-3: skill_rechazada
  0-4: skill_prohibida
```

### 5 Agentes Multi-Source Investigation (Detallados)

```yaml
github_researcher:
  sources: [github.com, github_API]
  queries: [awesome-{topic}, {topic}_stars_>1000]
  outputs: [repos.json, stars_issues_PRs]

hf_researcher:
  sources: [huggingface.co_models_datasets_spaces]
  queries: [{topic}_model_dataset_space]
  outputs: [models.json, downloads_likes]

web_researcher:
  sources: [Wikipedia, MDN, OWASP, documentacion_oficial, arXiv]
  queries: [{topic}_best_practices, {topic}_documentation]
  outputs: [pages.jsonl]

youtube_researcher:
  sources: [YouTube_tecnicos]
  queries: [{topic}_tutorial, {topic}_conference_talk]
  outputs: [videos.json, transcripts]

mcp_researcher:
  sources: [mcp_servers, smithery, Composio]
  queries: [{topic}_mcp_server]
  outputs: [mcp_servers.json]
```

### Universal Plug v1.5 Detalle

```yaml
universal_plug:
  version: 1.5
  interface: MCP
  transport: [stdio, http, mcp]
  input_schema: nct.task.v1.json
  output_schema: nct.result.v1.json
  auth:
    type: byok_or_proxy
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
  capabilities: [code_generation, web_search, rag_query, file_read, file_write, api_call, test_run, deploy]

nexus:
  funcion: punto_central_conexion_modulos
  hace: [descubre_modulos, registra_capabilities, enruta_requests, monitorea_health]
```

### M3 + Kimi División

```yaml
M3_jefe:
  funcion: arquitecto
  trabaja_con: MAX_directamente
  decide: QUE_hacer
  NO_ejecuta: codigo_directo
  entrega: plan_validacion

Kimi_K2_7_Code_empleado:
  funcion: implementador
  trabaja_para: M3
  decide: COMO_hacerlo
  SI_ejecuta: codigo
  entrega: implementacion_tests

flujo: MAX → M3_jefe → M3_planifica → Kimi_implementa → Kimi_reporta → M3_valida → M3_presenta → MAX_aprueba
```

### Fusión Kimi + MiniMax

```yaml
punto_fusion: donde_M3_chat_architect_encuentra_Kimi_ejecutor

protocolo_fusion:
  input: spec_from_M3
  output: implementation_from_Kimi
  handoff:
    M3_a_Kimi: plan_acceptance_criteria
    Kimi_a_M3: implementation_tests
  validation:
    M3_validates_against_acceptance_criteria
  feedback:
    M3_a_Kimi: corrections_if_needed

garantias:
  - M3_nunca_ejecuta_codigo_directo
  - Kimi_nunca_habla_con_MAX
  - handoff_siempre_con_schemas
```

### NCT Coordinator — 13 Archivos Detallados

```yaml
01_nct_coordinator: coordinador_principal_inicializa_sistema
02_nct_modes: selector_modo_manual_semi_continuo
03_nct_flows: definicion_flujos_continuos
04_nct_phases: implementacion_F0-F9
05_nct_inputs: recepcion_procesamiento_inputs
06_nct_outputs: generacion_entrega_outputs
07_nct_state: estado_global_state_json
08_nct_memory: sistema_memoria_4_tier
09_nct_skills: integracion_BIS
10_nct_agents: gestion_agentes
11_nct_audit: integracion_CSA
12_nct_metrics: recoleccion_metricas
13_nct_delivery: multi_target_delivery
```

### Selector de Modos (UI)

```
┌─────────────────────────────────────┐
│      NCT — SELECCIÓN DE MODO        │
├─────────────────────────────────────┤
│                                     │
│  1. Manual                          │
│     • Cada paso requiere aprobación │
│                                     │
│  2. Semi-automático                 │
│     • Sistema propone, MAX aprueba  │
│                                     │
│  3. Continuo (NCT)                  │
│     • Coordinación automática       │
│     • Tareas largas (24h+)          │
│                                     │
│  Selecciona modo [1/2/3]: ___       │
└─────────────────────────────────────┘
```

---

## DOC 22: Ejemplos Completos Paso a Paso

### Ejemplo 1: Crear Microservicio E-Commerce

```yaml
spec_MAX: "Microservicio para gestionar productos y stock de tienda online con REST API, JWT auth, deploy en HF Spaces"

SID_5_preguntas:
  Q1_que_es: "Microservicio REST para gestión de productos y stock con autenticación JWT"
  Q2_para_quien: "Desarrolladores e-commerce que necesitan backend simple para tienda pequeña/mediana"
  Q3_que_problema_resuelve: "Crear backend desde cero toma 2-4 semanas, este lo entrega en 24h con features básicas"
  Q4_como_se_usa: |
    1. POST /auth/register → crear usuario
    2. POST /auth/login → JWT
    3. POST /products (con JWT) → crear producto
    4. GET /products → listar
    5. PUT /products/{id}/stock → actualizar stock
    6. GET /products/{id} → ver detalle
  Q5_que_NO_es: [NO_marketplace_completo, NO_pasarela_pago, NO_UI_web, NO_procesa_imagenes, NO_escala_millones_productos]
  score: 96/100_aprobado

BIS_lookup:
  categorias_relevantes: [H_APIs, D_Backend, G_Bases_datos, L_Seguridad, K_Testing]
  skills_seleccionadas: 6

plan_generado: |
  plan:
    id: plan-ecommerce-001
    pattern: dag
    level: L4_SUPERVISED_AUTONOMOUS
    steps:
      - id: research, parallel_group: g1, agents: [MA-RESEARCH-WEB, MA-RESEARCH-GH]
      - id: architecture, parallel_group: g1, agent: MA-ARCH-PLAN
      - id: synth, parallel_group: g2, agent: MA-RAG-SYNTH, input_from: g1
      - id: code, parallel_group: g3, agent: MA-CODE-GEN, input_from: g2
      - id: lint, parallel_group: g4, agent: MA-CODE-LINT, input_from: g3
      - id: test, parallel_group: g4, agent: MA-CODE-TEST, input_from: g3
      - id: verify, parallel_group: g5, agent: MA-VERIFY-3CAPAS, input_from: g4
      - id: doc, parallel_group: g5, agent: MA-DOC-WRITE, input_from: g3
      - id: deliver, parallel_group: g6, agent: MA-EMIT-REPORT, input_from: g5

ejecucion:
  duracion: 18h_23min
  tokens: 1.2M
  resultado: PASS_CSA_score_96/100

outputs:
  codigo: 8_archivos_Python
  tests: 24_unit_+_8_integration
  docs: [README.md, ARCHITECTURE.md]
  deploy: HF_Space_mavis_ecommerce-microservice
```

### Ejemplo 2: SaaS API Multi-Tenant

```yaml
spec_MAX: "API REST multi-tenant para SaaS de gestión de tareas con autenticación JWT, rate limiting y auditoría, lista para producción en 24h"

SID_5_preguntas:
  Q1: "API REST multi-tenant para SaaS de gestión de tareas"
  Q2: "Equipos de 5-50 personas"
  Q3: "SaaS comerciales cuestan $500+/mes, alternativa económica con control"
  Q4: |
    1. POST /tenants → crear tenant
    2. POST /auth → JWT
    3. POST /tasks → crear tarea
    4. GET /tasks → listar
    5. Rate limit 1000 req/h
    6. Audit log de todo
  Q5: [NO_mayor_1000_usuarios, NO_UI_web, NO_reemplaza_Jira]
  score: 97/100_aprobado

pipeline_completo: |
  chain:
    id: saas_tasks_api_v1
    pattern: dag
    level: L5_CONTINUOUS_AUTONOMOUS_72H_PLUS
    budget: { max_tokens: 5_000_000, max_runtime_h: 24 }
    research:
      sources:
        web: [owasp_jwt, fastapi_multi_tenant, rate_limit_algorithms]
        github: [fastapi-template_stars_>1000, awesome-saas]
      rounds: { min: 2, max: 4 }
    steps:
      - { id: MA-ARCH-PLAN, parallel_group: g1 }
      - { id: MA-RESEARCH-WEB, parallel_group: g1 }
      - { id: MA-RESEARCH-GH, parallel_group: g1 }
      - { id: MA-RAG-SYNTH, parallel_group: g2 }
      - { id: MA-CODE-GEN, parallel_group: g3 }
      - { id: MA-CODE-LINT, parallel_group: g4 }
      - { id: MA-CODE-TEST, parallel_group: g4 }
      - { id: MA-VERIFY-3CAPAS, parallel_group: g5 }
      - { id: MA-DOC-WRITE, parallel_group: g5 }
      - { id: MA-EMIT-REPORT, parallel_group: g6 }
    monitor: { pad: true, anxiety: true, drift: true }
    repair: { pipeline: 5_steps, max_retries: 3 }
    hf_fleet: { min_workers: 10, max_workers: 20 }

resultado:
  duracion: 22h_47min
  tests: 47_unit_+_12_integration_+_8_E2E
  coverage: 87%
  CSA_score: 97/100
  output: listo_produccion
```

### Contratos YAML

```yaml
contrato_skill:
  skill_id: code_generator
  version: 1.2.0
  category: J-IA
  interface:
    inputs: [{ name: spec, type: string, required: true }, { name: stack, type: object, required: true }, { name: constraints, type: array, required: false }]
    outputs: [{ name: code, type: file, format: zip }, { name: diff, type: file, format: patch }]
  capabilities: [code_generation, multi_language]
  limits: { max_tokens: 50000, max_runtime_s: 120, max_files: 50 }
  dependencies: [arch_planner, rag_search]
  tests: { unit: 5, integration: 2, coverage: 85% }
  owner: g5-orquestador
  license: MIT

contrato_agente: |
  agent_contract:
    agent_id: MA-VERIFY-3CAPAS
    type: deterministic_with_llm_fallback
    budget: { code_pct: 90, llm_pct: 10, max_tokens: 50_000 }
    inputs: { artifact: object, rubric: object }
    outputs: { decision: enum, issues: array }
    code_steps: [parse_artifact, schema_validate, cap1_adversarial, cap2_cruzada, cap3_maker_checker]
    llm_steps:
      - when: "any(cap.issues)"
        call: llm_adversarial_review
        max_tokens: 4_000
        temperature: 0.0

contrato_pipeline:
  pipeline_id: ecommerce_v1
  version: 1.0.0
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget: { max_tokens: 2_000_000, max_runtime_h: 24 }
  steps: [...]
  consensus: required
  audit: full_csa
  delivery: { targets: [github, hf_space, telegram], format: adaptive }
```

### Árbol de Entrega NCT Coordinator

```yaml
NCT/:
  Coordinator_nct_coordinator_py:
    Modes_nct_modes_py: [Manual, Semi-automatico, Continuo]
    Flows_nct_flows_py: [Flow_F0-F9, Custom_flows]
    Phases_nct_phases_py: [Phase_0_Pre-Boot, Phase_0.5_Confirmation, Phase_1-9]
  Core/:
    Inputs_nct_inputs_py: Input_Engine_v4.0
    Outputs_nct_outputs_py: Output_Engine_+_OOS
    State_nct_state_py: state.json
    Memory_nct_memory_py: 4_tier_memory
  Skills_nct_skills_py: BIS
    - 14_categorias
    - 13_criterios
    - debate_4_especialistas
  Agents_nct_agents_py:
    - 30_micro_agentes
    - 11_internal_roles
    - 10_agent_council
  Audit_nct_audit_py: CSA
    - 10_jueces
    - 5_fases
  Metrics_nct_metrics_py: [PAD, Anxiety, Drift]
  Delivery_nct_delivery_py:
    - 23_destinos
    - adaptive_format
```

### Mapa Fusión Final

```
MAX → MAXBRY_SUPER_TEAM
        ├── SID_5_preguntas
        ├── BIS_skills_lookup
        ├── plan_generation
        ├── consensus_10_agentes
        ├── execution_30_micro_agentes
        ├── CSA_audit_10_jueces
        ├── output_engine
        ├── multi_target_delivery
        └── feedback_loop

G6_ASISTENTES → 9_GGUF_+_16_API_keys
G1-G4_INFRA_CORE_UI_AUDIT → workers
```

---

## DOC 17: Configuraciones + Costos

### Objetivo Costo $0/mes

```yaml
HF_Spaces_free_tier
API_free_tiers
GGUF_local_sin_costo
sin_servers_dedicados
sin_bases_datos_caras
```

### 3 Perfiles de Uso de API

```yaml
conservador:
  description: bajo_costo_baja_capacidad
  primary: groq
  secondary: nim
  fallback: cerebras
  rules: [no_gpt_oss_20b, max_retries_3, timeout_60s]
  budget: max_tokens_per_task_100_000
  expected_throughput: 2000+_tasks_dia
  use_cases: [simples, bajo_riesgo, bajo_costo]

equilibrado_RECOMENDADO:
  description: balance_costo_calidad
  primary: nim
  secondary: cerebras
  fallback: groq
  rules: [gpt_oss_20b_for_hard_tasks, max_retries_5, timeout_120s]
  budget: max_tokens_per_task_500_000
  expected_throughput: 1000+_tasks_dia
  use_cases: [mayoria_tareas, balance_costo_calidad]

agresivo:
  description: maxima_calidad
  primary: cerebras
  secondary: nim
  fallback: groq
  rules: [always_try_gpt_oss_20b_first, max_retries_10, timeout_300s]
  budget: max_tokens_per_task_2_000_000
  expected_throughput: 100+_tasks_dia
  use_cases: [criticas, maxima_calidad, costo_no_importa]
```

### Arranque Autónomo (Pasos)

```yaml
1: crea_14_repos_GitHub  # 6_grupos + 8_productos
2: crea_7_HF_Spaces  # 1_por_grupo + extras
3: escribe_5_Dockerfiles  # cada_grupo_Dockerfile
4: inyecta_secretos  # API_keys_tokens_credenciales
5: configura_profiles  # conservador_equilibrado_agresivo
6: arranca_orquestador  # inicializacion_automatica_reporte_MAX
```

### Capacidades Objetivo

```yaml
cantidad:
  agentes: 2000+_simultaneos_capacidad
  tareas: 1000+_simultaneas

hardware:
  HF_Spaces: 7_x_16GB = 112GB
  uso_modelos: ~13.5GB
  margen_libre: 87%

throughput_por_perfil:
  conservador: 2000+_tasks_dia
  equilibrado: 1000+_tasks_dia
  agresivo: 100+_tasks_dia
```

### 7 HF Spaces (Propósito + RAM)

```yaml
g1_infra: [infraestructura, 16GB]
g2_core: [BIS, SID, Input/Output, 16GB]
g3_ui: [Telegram, API, Dashboard, 16GB]
g4_audit: [CSA, 16GB]
g5_orquestador: [MAXBRY, 16GB]
g6_asistentes: [9_modelos_GGUF, 16GB]
extras: [reservas, 16GB]
```

### Limitaciones

```yaml
HF_Spaces: [pueden_dormirse_inactividad, rate_limits, cold_starts, 16GB_RAM_max_por_Space]
APIs_free_tier: [rate_limits, cuotas_mensuales, latencia_variable]
GGUF_local: [carga_RAM, inferencia_mas_lenta_que_API, modelos_mas_pequenos]
```

### Reglas de Costo

```yaml
nunca_exceder_presupuesto: cada_task_max_tokens_y_max_runtime_s
perfil_default: equilibrado
cambio_dinamico: [MAX_solicita, presupuesto_se_agota, tarea_critica]
monitoreo: [tokens_usados, tiempo_inferencia, costo_estimado_en_tiempo_no_dinero]
```

---

## DOC 18b: Verificación Cruzada (versión inicial)

### Cobertura Verificada 100%

```yaml
constitucional: [39_principios_v1_v2_v3, 10_CSA_5_fases, SID_5_preguntas, BIS_14_categorias_13_criterios]
engines: [Input_Engine_v4_54, Output_Engine_+_OOS_27, LOOP_v6_15+3, OUTPUT_v6.1_16_gobernanza]
estructura: [30_micro, 11_roles, 10_colas, 6_niveles, 12_TM, 5_loop_versions, 3_monitores]
pipeline: [10_fases, fase_0.5, FABLES_5, CHEF_FINAL_4]
razonamiento: [STANDARD_5+12, TURBO_12+45, micro_ciclo_7, DRE_9, OpenMythos]
mythos_fables: [40_pasos, 12_cortos, OpenMythos, arquitectura_control]
subsistemas: [System_Prompt_15, Skills_13, investigation_5, Universal_Plug_v1.5, M3_Kimi_division, razonamiento_externo, NCT_Coordinator, Universal_Module_Contract]
configuraciones: [3_perfiles_API, pre_flight, costos, $0]
reglas: [regla_absoluta_MAX, cosas_intocables, validacion, 5_GOALS_12_PASOS]
agentes: [5_consenso, 5_investigacion, 12_especializados, 10_CSA, 10_consejo, 5_officers, 9_OUTPUT_M3, 10_INPUT_LOOP_M3, 8_hallazgos_research, OSS_clones]
modelos: [9_GGUF, 16_API_keys, 3_perfiles, 60_datasets, 60_adapters]
arquitectura: [V1_Chat_AI_NCT, V2_Adaptador_MHYTOS, decisiones_aprobadas, diagrama_V1_V2, NCT_AI_Architecture]
mimo_lop_v200: [analisis_MiMo, 3_pilares, loops_internos, adaptaciones, 12_micro_agentes, 8_propuestas, flota_HF_Spaces]
```

### Temas Mencionados en Chat No Profundizados

```yaml
1_validacion_por_salida_md: mencionado_pero_no_extraido_completamente
2_MI_SYSTEM_PROMPT_OPERATIVO_md: mencionado_pero_no_extraido_completamente
3_BORRADOR_LISTA_APROBADOS_md: mencionado_pero_no_extraido_completamente
4_STATE_AUDIT_md: mencionado_pero_no_extraido_completamente
5_detalles_validacion_por_salida: mencionado_en_doc_05_pero_puede_profundizarse
6_Mi_System_Prompt_Operativo_M3: mencionado_en_doc_06_pero_puede_profundizarse
```

### Resumen Ejecutivo

```yaml
total_documentos: 17
total_bytes: 209185
total_temas_cubiertos: 80+
total_verificaciones_cruzadas: 100%

faltante_en_MAX_no_en_documentos:
  - 8_datos_pre_flight_pendientes
  - confirmacion_HTM_YUAN_model_names
  - aprobacion_final_para_M2.7
```

### Parches Indexados (170)

```yaml
9_patches_OUTPUT_v6.1
16_patches_OUTPUT_v6.1_gobernanza
9_patches_INPUT_V40
15_patches_LOOP_V60
10_patches_PROPUESTAS_INPUT_LOOP
51_parches_ORQUESTADOR
23_parches_INFRA
37_parches_EXTRAS  # CSA_criterios_agentes_research_delivery
total: 170
```

### Archivos Relacionados

```yaml
workspace_attachments/: 12_archivos_misc
workspace_nct_proyecto/:
  - 01-FASE-0-FROZEN.md
  - 02-SYSTEM-PROMPT-MYTHOS.md
  - ANALISIS-LOOPS-v100.md
  - BIS-v1-MAXBRY.md
  - BORRADOR-LISTA-APROBADOS.md
  - CONSENSO-MEJORADO-10X.md
  - CONSTITUCION-ORQUESTADOR.md
  - MI-SYSTEM-PROMPT-OPERATIVO.md
  - ORQUESTADOR-G5-DISENO.md
  - PARCHE-v14_a_PARCHE-v17
  - PARCHES-MAXBRY-SUPER-TEAM.md
  - SISTEMA-RAZONAMIENTO-EXTERNO.md
  - STATE-AUDIT.md
  - VALIDACION-POR-SALIDA.md

workspace_maxbry/: 19_archivos_python_726_lineas
```

### Credenciales

```yaml
documentadas: [16_API_keys, 6_tokens_HF_pendientes, 14_repos_pendientes, 5_Dockerfiles_pendientes, Telegram_bot_token_pendiente, Turso_DB_credentials_pendientes, GitHub_username_PAT_pendientes]
reales_NO_en_docs: claves_reales_las_tiene_MAX
estos_docs_son: ARQUITECTURA
```

---

## DOC NCT-LOP-200X-2026-06-22-ADDENDUM: MiMo Code v200

### JSON Summary for Mavis M3

```yaml
$schema: https://NCT/turbo/schemas/lop-system-v200.schema.json
document_id: NCT-LOP-200X-2026-06-22-ADDENDUM
parent_document: NCT-LOP-100X-2026-06-22
target: Mavis_M3
package: nct_coordinator.lop_v200
namespace: nct.lop.v200

scope_additions: [mimo_code_loop_analysis, open_source_agent_catalog, chained_task_strategy, seed_information_pre_analysis, rag_github_web_research_cycles, huggingface_spaces_remote_compute_fleet, deterministic_dsl_90_10, specialized_micro_agents]
```

### MiMo Code Facts

```yaml
origin: Xiaomi_MiMo_Team
base_project: OpenCode
license: MIT
first_release: 2026-06-11_v0.1.0
tech_stack: [Bun, TypeScript, Effect, SolidJS, Tauri]
three_pillars:
  compute: [Max_Mode, Goal_Stop, Dynamic_Workflow]
  memory: [Checkpoint_Rebuild, Writer_subagent, 4_tier_memory]
  evolution: [Dream, Distill, project_memory]
benchmark_vs_claude_code: { SWE-Bench_Pro_V2: +5%, Terminal_Bench_2: +5%, ultra_long_200+_steps: beats_Claude_Code }
compatible_models: [MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM]
```

### Open Source Clones Catalog

```yaml
tier_s_plus: [OpenCode, Gemini_CLI, OpenHands, Open_Interpreter, Aider, Goose]
tier_a: [Qwen_Code, Crush, Kimi_CLI, Forge_Code, MiMo_Code]
tier_b: [BLXCode, Open_Design, OpenClaw, KiloCode, Cline, BLACKBOX.AI]
languages: [TypeScript, Python, Rust, Go]
mcp_first: [Goose, Open_Design, BLXCode]
```

### Specialized Micro-Agents (12)

```yaml
count: 12
design_rule: single_responsibility_menor_igual_200_LOC_core_single_output_schema
execution_model: spawn_run_emit_JSON_die
list: [MA-CODE-GEN, MA-CODE-LINT, MA-CODE-TEST, MA-RAG-SEARCH, MA-RAG-SYNTH, MA-DOC-WRITE, MA-ARCH-PLAN, MA-VERIFY-3CAPAS, MA-REPAIR-5STEP, MA-RESEARCH-WEB, MA-RESEARCH-GH, MA-EMIT-REPORT]
```

### HF Spaces Fleet

```yaml
min_workers: 10
max_workers: 20
protocol: MCP_via_mcp-hfspace
selection_rule: by_capability_+_SLA_+_cost
failover: circuit_breaker_+_backoff_exponential
examples: [evalstate_FLUX.1-schnell, hf-audio_whisper-large-v3-turbo, microsoft_OmniParser, Qwen2-VL-72B_smolagents_E2B]
```

### DSL Budget

```yaml
code_pct: 90
llm_pct: 10
rationale: DSL_determinista_para_orquestacion_LLM_solo_donde_aporta_senal_no_derivable
```

### Research Cycle

```yaml
phases: [seed_analysis, web_research, github_research, synthesize, emit]
min_rounds_per_task: 2
max_rounds_per_task: 5
early_stop_if: evidence_sufficiency_score >= 0.85
```

### Ingestion Directives for Mavis M3

```yaml
- merge_v200_into_v100_dependency_graph
- treat_mimo_code_as_reference_implementation_not_dependency
- treat_open_source_clones_as_substitutable_backends
- spawn_micro_agents_via_hf_spaces_mcp
- enforce_90_10_dsl_llm_budget_per_cycle
- persist_seed_analysis_to_state_seed_yaml
- do_not_modify_existing_25_bloques_of_software_principal
- emit_prs_against_nct_coordinator_lop_v200_subpackage
```

### Integración MiMo → NCT (Diagrama)

```
NCT_v200:
  nct_coordinator:
    FSM_10_fases:
      RAG + Max_Mode ←借鉴_MiMo
      Checkpoint + Writer_subagent ←借鉴_MiMo
      Dream + Distill ←借鉴_MiMo
  25_bloques_existentes_intactos
```

### 8 Nuevas Propuestas (PROP-13 a PROP-20) — Contratos

```yaml
PROP-13_micro_agents_catalog:
  inputs: { task: Task, k_concurrency: int }
  outputs: { results: array, audit: AuditTrail }
  invariants: [single_responsibility, max_loc_core_200, schema_io_unico]
  kpis: [p99_latency_ms, success_rate, cost_per_call]

PROP-14_chain_patterns:
  inputs: { tasks: array }
  outputs: { execution_plan: ExecutionPlan }
  invariants: [acyclic_dag, max_depth_5]

PROP-15_seed_pre_analysis:
  inputs: { repo: RepoPath, state: StatePath, rag: RAGPath }
  outputs: { seed_index: SQLite, gaps: array, questions: array }
  invariants: [reproducible]

PROP-16_research_cycle:
  inputs: { question: string, sources: array }
  outputs: { synthesized: Synthesis, score: float }
  invariants: [min_rounds_2, max_rounds_5, early_stop_threshold_0.85]

PROP-17_hf_spaces_fleet:
  inputs: { capability: string, sla_ms: int }
  outputs: { worker_id: string, fallback_chain: array }
  invariants: [min_workers_10, max_workers_20, circuit_breaker]

PROP-18_dsl_90_10_budget:
  inputs: { pipeline: Pipeline }
  outputs: { budget_report: BudgetReport }
  invariants: [llm_pct_le_10]
  kpis: [llm_pct, cost_per_cycle]

PROP-19_mimo_integration:
  inputs: { mimo_feature: enum[max_mode, goal_stop, writer, dream, distill, checkpoint] }
  outputs: { enabled: bool, config: object }

PROP-20_oss_backends_router:
  inputs: { task: Task }
  outputs: { backend: enum, model: string, transport: enum }
  invariants: [byok_or_proxy, mcp_first_preferred]
```

### Árbol de Entrega Actualizado

```yaml
nct_coordinator/:
  lop_v100/  # documento padre ya entregado
    __init__.py
    levels.py
    alvs.py
    task_models/...
    proposals/PROP-01..12.yaml
    schemas/...
  lop_v200/  # NUEVO este addendum
    __init__.py
    micro_agents/  # 12_micro_agentes
    pipelines/  # DSL_declarativos
    backends/  # routers_OSS_clones
    hf_spaces/  # cliente_flota_HF
    dsl/
    seed/
    research/
    proposals/PROP-13..20.yaml
    schemas/
```

### Instrucciones Finales para M3

```yaml
1: parsear_seccion_0_JSON_SUMMARY_como_contrato_entrada_mergear_con_contrato_padre_v100
2: construir_grafo_dependencias_v100_v200
3: materializar_arbol_archivos_seccion_12
4: generar_PRs_orden [schemas, micro_agents, dsl, pipelines, backends, hf_spaces, seed, research, proposals]
5: validar_llm_pct_menor_igual_0.10_en_cada_pipeline
6: validar_ningun_archivo_nct_coordinator_lop_v200_modifica_25_bloques_originales
7: versionar_este_modulo_como_200.0.0_semver
8: reportar_usuario_solo_resumen_ejecutivo_diagramas_KPIs  # sin_preguntas_sin_comentarios
```

### 3 Patrones de Encadenamiento (Soportados Nativamente)

```yaml
secuencial: chain_linear  # caso_ETL_refactor
dag_paralelo: chain_dag_con_parallel_groups  # caso_investigacion_diseño
fractal_anidado: chain_fractal_con_depth_<=5  # caso_arquitectura_multi_modulo
```

### Selección Dinámica Worker

```python
def select_worker(capability, sla_ms):
    candidates = workers_by_capability[capability]
    alive = [c for c in candidates if c.health == "ok"]
    feasible = [c for c in alive if c.p95_ms <= sla_ms]
    return min(feasible, key=lambda c: c.cost)
```

### Resiliencia

```yaml
circuit_breaker: por_Space_umbral_3_fallos_consecutivos
backoff_exponential: base_2s_max_5min
failover: al_siguiente_Space_disponible_misma_capability
degradacion_elegante: si_todos_Spaces_caen_paso_se_marca_skipped_cadena_continua
```

---

## PATCH-AUDITORIA-GAPS-V5: 12 Gaps Únicos

### Resumen 80 Gaps Totales (5 Pasadas)

```yaml
1er_patch_V1: 20_gaps
2do_patch_V2: 13_gaps
3er_patch_V3: 17_gaps
4to_patch_V4: 18_gaps
5to_patch_V5: 12_gaps_unicos
total: 80_gaps_identificados
```

### GAP #69 — Input Governor 6 Estados (Detalle)

```yaml
1_RECIBIDO: input_acaba_llegar_sistema
2_ANALIZANDO: swarm_discovery_forensics_trabajando
3_DEFINIENDO: definition_engine_buscando_claridad
4_COMPILANDO: compiler_construyendo_grafos
5_AUDITANDO: quality_swarm_validando
6_DECISION: [APROBADO, VETADO, REPLANIFICAR, PREGUNTAR]
regla: si_PREGUNTAR_bloquea_hasta_respuesta_MAX
```

### GAP #70 — Executive Board 5 Nombres Específicos

```yaml
COO: eficiencia_performance
CFO: costos_presupuesto
CQO: calidad_global_scores
CRO: riesgos_fallos_alertas
CLO: aprendizaje_evolucion
responsabilidades: [monitorear_metricas_globales, alertar_MAX_si_desvia, sugerir_optimizaciones, detectar_patrones_sistemicos, reportar_estado_semanal]
```

### GAP #71 — 23 Destinos Delivery (Lista Oficial)

```yaml
archivos_documentos_5: [MD, PDF, HTML, DOCX, TXT]
codigo_5: [ZIP, GitHub, GitLab, Bitbucket, tarball]
datos_3: [JSON, YAML, XML]
comunicacion_3: [Email, Slack_Discord, Telegram]
almacenamiento_3: [Drive_Mavis, S3_compatible, HF_Dataset]
apis_2: [REST_API, Webhook]
otros_2: [MCP_server, Streaming_output]
```

### GAP #72 — Inteligencia Colectiva Emergente

```yaml
cada_agente: [conocimiento_local, comparte_en_bus_eventos, lee_que_otros_comparten]
patrones_emergen: [agentes_colaboran_sin_programacion_explicita, soluciones_no_anticipadas, comportamiento_enjambre]
surge: inteligencia_superior_a_suma
usa: bus_de_eventos_INPUT-A
complementa: Swarm
mejora_con: escala
```

### GAP #73 — Output Governor 8 Estados (Detalle)

```yaml
1_APROBAR: output_cumple_criterios_publicar
2_CORREGIR: errores_menores_corregir_republicar
3_REGENERAR: problemas_serios_generar_de_nuevo
4_REPLANIFICAR: enfoque_incorrecto_cambiar_estrategia
5_DIVIDIR: output_demasiado_grande_partir
6_INVESTIGAR_MAS: falta_informacion_investigar
7_PREGUNTAR_USUARIO: decision_humana_necesaria_consultar_MAX
8_CANCELAR: no_tiene_sentido_continuar_terminar
controla: flujo_entre_16_componentes_Output_v6.1
reporta: a_Orquestador_G5
regla: si_PREGUNTAR_USUARIO_bloquea_hasta_respuesta
```

### GAP #74 — Closed Feedback Loop (Detalle)

```yaml
flujo:
  1: output_publicado
  2: uso_real  # se_usa_funciona_satisface
  3: feedback  # [directo_rating_comentarios, indirecto_errores_performance, observado_como_lo_usan]
  4: memoria  # [output_memory, patterns_identificados]
  5: aprendizaje  # [meta_learning, self_improving]
  6: reglas_actualizadas  # [knowledge_base, CSA_jueces, BIS_skills]
  7: proximo_output_mejor

por_que_mas_importante:
  - mejora_continua_automatica
  - memoria_organizacional
  - adaptacion_mundo_real
  - pegamento_entre_otros_9_patches_OUTPUT
  - cierra_ciclo_vida_completo
```

### GAP #75 — Pre-Mortem Detalle

```yaml
1: recibe_salida_candidata
2: genera_10_escenarios_fracaso_posibles
3: para_cada_escenario_calcula_probabilidad_impacto
4: propone_mitigaciones_especificas
5: si_riesgo_promedio_alto_no_publica

metricas:
  escenarios: 10_por_analisis
  probabilidad_base: 15%_por_escenario
  impacto: escala_1-10
  mitigacion: automatica_por_escenario
```

### GAP #76 — Trust Engine Umbrales Específicos

```yaml
rango: 0-100
por_elemento:
  agentes: tasa_exito_historica
  modelos: coherencia_respuestas
  datos: fuente_y_verificacion
  skills: resultados_al_aplicarlas
  CSA_jueces: acuerdos_con_otros_jueces

umbrales:
  trust_menor_30: rechazar_o_pedir_segunda_opinion
  trust_30-70: usar_con_cautela
  trust_mayor_70: usar_con_confianza
  trust_mayor_90: usar_sin_verificar

integracion:
  - usado_por_Model_Router_LOOP-G
  - alimenta_Causal_Tracing_OUTPUT-PATCH-7
```

### GAP #77 — Workflow DAG vs Pipeline

```yaml
pipeline: A→B→C→D→E  # lineal_secuencial
DAG: A→B→D, A→C→D, D→E  # paralelo_ramificado

ventajas_DAG:
  - paralelismo_real
  - manejo_dependencias_complejas
  - sin_bloqueos_lineales
  - permite_reintentos_parciales

reemplaza: concepto_pipeline_en_Loop_v6.0
base_para: Runtime_Kernel_LOOP-B
usado_por: 3_ciclos_paralelos_A_B_C
```

### GAP #78 — 19 Archivos Python Específicos

```yaml
/workspace/maxbry/g7/output_engine/v2/:
  __init__.py: 1316_bytes
  pre_mortem/:
    __init__.py
    pre_mortem_analyzer.py: 2436_bytes_70_lineas
  auto_rollback/:
    __init__.py
    rollback_monitor.py: 2211_bytes_62_lineas
  meta_learning/:
    __init__.py
    cross_release_analyzer.py: 1991_bytes_56_lineas
  personalization/:
    __init__.py
    style_learner.py: 2165_bytes_64_lineas
  multi_stakeholder/:
    __init__.py
    stakeholder_detector.py: 2913_bytes_79_lineas
  causal_tracing/:
    __init__.py
    causal_chain_builder.py: 2812_bytes_75_lineas
  marketplace/:
    __init__.py
    output_cataloger.py: 3010_bytes_84_lineas
  self_improving/:
    __init__.py
    quality_analyzer.py: 3606_bytes_99_lineas
  production_monitoring/:
    __init__.py
    usage_tracker.py: 3052_bytes_88_lineas

total: 19_archivos_Python_726_lineas
```

### GAP #79 — 9 Propuestas Aplicadas + 1 Rechazada

```yaml
1_Pre_Mortem_Analysis: aplicado
2_Output_Sandbox: RECHAZADO_POR_MAX
3_Auto_Rollback_Inteligente: aplicado
4_Meta_Learning_entre_Releases: aplicado
5_Output_Personalization: aplicado
6_Multi_Stakeholder_Output: aplicado
7_Causal_Output_Tracing: aplicado
8_Output_Marketplace_Interno: aplicado
9_Self_Improving_Output_Quality: aplicado
10_Production_Monitoring: aplicado
```

### GAP #80 — Constitución Maestra 1276 Líneas

```yaml
/workspace/nct-proyecto/CONSTITUCION-ORQUESTADOR.md: 1276_lineas
capas_totales: ~80
principios: 39
agentes_paralelos: 200+
HF_Spaces: 7
```

---

## PATCH-AUDITORIA-GAPS-V3: 17 Gaps Nuevos

### GAP #34 — Estructura Completa MAXBRY (336 Archivos)

```yaml
00_raiz: 6_archivos_metadata
01_bootstrap: 5_archivos_instalacion
02_core: 7_archivos_nucleo
03_input_engine: 28_archivos_P28-P29_+_17_mejoras
04_sid: 10_archivos_P27
05_sub_orquestadores: 26_archivos  # 20_SO_+_SO-ARQ
06_csa: 17_archivos_P26
07_output_engine: 25_archivos  # P31+P34
08_ovfs: 6_archivos_P32
09_agentes: 40_archivos_colmenas
10_invariantes: 3_archivos_P30
11_datasets: 60_archivos
12_adapters: 60_archivos
13_seguridad: 7_archivos_P6
14_canales: 6_archivos
15_modelos: 9_archivos
16_scheduler: 4_archivos
17_storage: 5_archivos
18_estado: 4_archivos
19_testing: 4_archivos
20_logs: 4_archivos
total: 336_archivos_Python_40800_lineas_python_53400_lineas_totales
```

### GAP #35 — Cálculos de Recursos

```yaml
lineas_codigo_estimadas:
  Python_puro: ~40800
  YAML_configs: ~2500
  JSON_schemas: ~1800
  Shell_scripts: ~300
  Markdown_docs: ~8000
  total: ~53400_lineas

tamano_disco:
  codigo_fuente: ~2_MB
  configs_schemas: ~0.3_MB
  docs: ~12_MB
  total: ~14_MB

memoria_ejecucion:
  Python_runtime: ~130_MB
  LiteLLM_gateway: ~50_MB
  Dramatiq: ~30_MB
  FastAPI: ~20_MB
  ChromaDB: ~80_MB
  bge_small: ~100_MB
  Pybreaker: ~10_MB
  Redis_client: ~20_MB
  Telegram_bot: ~30_MB
  MCP_server: ~30_MB
  total_runtime: ~500_MB_RAM
con_modelos_G6: ~13_GB_RAM
recursos_totales:
  HF_Spaces: 7_x_16GB = 112GB
  usados: ~13.5GB
  margen_libre: 87%
```

### GAP #36 — OOS 14 Componentes (Diferente de Output Engine)

```yaml
OOS_14_componentes:
  - Output_Planner
  - Output_Compiler_AST_de_salida
  - Output_Graph
  - Semantic_Chunk_Engine  # no_corta_por_tokens_calcula_dependencias
  - Adaptive_Chunk_Size  # tamaño_dinamico
  - Predictive_Output_Planner  # calcula_salida_estimada_antes
  - Auto_Format_Negotiation  # recomienda_formato_inteligente
  - Intelligent_Packaging  # paquetes_por_tipo
  - Multi_Delivery_Pipeline  # 15+_destinos_en_paralelo
  - Intelligent_Compression  # optimiza_antes_comprimir
  - Smart_Version_Control  # v1.0.0_v1.0.1
  - Incremental_Publishing
  - Intelligent_Resume
  - Output_Verification
  - Universal_Output_Model  # extra
  - Delivery_Policy_Engine  # extra
```

### GAP #37 — 15+ Destinos OOS (en paralelo)

```yaml
destinos_paralelo:
  - Artifact
  - Markdown
  - GitHub
  - Google_Drive
  - Dropbox
  - OneDrive
  - Base_SQL
  - Vector_DB
  - Notion
  - Obsidian
  - MCP
  - REST_API
  - WebSocket
  - S3
  - NAS
  - Servidor_privado
regla: TODO_EN_PARALELO
```

### GAP #38 — 20 Sub-Orquestadores (SO-01 a SO-20)

```yaml
SO-01: analista_objetivos
SO-02: organizador
SO-03: planificador
SO-04: validador_plan
SO-05: investigador
SO-06: replanificador
SO-07: mapa_mental
SO-08: clasificador
SO-09: divisor_tareas
SO-10: disenador_pasos
SO-11: constructor_bucles
SO-12: gestor_dependencias
SO-13: calculador_recursos
SO-14: asignador
SO-15: creador_loops
SO-16: validador_calidad
SO-17: verificador_cruzado
SO-18: auditor_trazabilidad
SO-19: reportador
SO-20: memoria_sistema
mas: SO-ARQ_arquitectura
```

### GAP #39 — 6 Colmenas

```yaml
09_agentes/:
  colmena_programacion: [sa_diseno, ma_01_30, etc]
  colmena_investigacion: [github, hf, web, youtube, mcp]
  colmena_memoria: [chromadb, bge_embedder, trazabilidad]
  colmena_seguridad: [sheriff, sentinel, auditor]
  colmena_documentacion: [escritor, generador, validador]
  colmena_testing: [runner, coverage, benchmark]
```

### GAP #41 — Kimi K2 Detalles Específicos

```yaml
vendor: Moonshot_AI
HF: moonshotai/Kimi-K2.7-Code
GitHub: github.com/MoonshotAI/Kimi-K2.5
funcion: agente_de_code_del_orquestador
provider: OpenCLAW_nativo_+_compatible_Claude_Code_via_API
endpoint: Groq_provider_o_NVIDIA_NIM
arquitectura: MoE_1T_params_32B_activados
versiones: [K2.5, K2.7-Code, K2_Thinking]
```

### GAP #42 — 10 Instrucciones Pendientes de MAX

```yaml
1: confirmacion_archivo_docx_con_aprobado
2: activar_M2.7_para_crear_G5_con_HF_Telegram_MCP_server
3: nombre_exacto_HTM_YUAN_no_encontrados_HF
4: autorizacion_finalizar_documentos_proceder_instalacion
5: decision_visibilidad_repos_publico_privado
6: decision_comunicacion_Telegram_bot_token
7: datos_acceso_GitHub_GH_OWNER_PAT
8: datos_acceso_HuggingFace_HF_USERNAME_token
9: 16_API_keys_confirmadas_con_labels
10: Turso_DB_credentials_opcional
```

### GAP #43 — Herramientas Aprobadas

```yaml
huggingface:
  - ZeroGPU: infraestructura_COMPARTIDA_no_nos_afecta
  - CPU-Basic_Spaces: 16GB_RAM_cada_uno_aislados_por_contenedor
  - GitHub_PAT: conexion_via_git_con_GH_PAT_como_secret
  - cada_HF_Space_propia_URL_fija_produccion

mcp_model_context_protocol:
  - github.com/modelcontextprotocol/servers  # 2700+_servers
  - github.com/shreyaskarnik/huggingface-mcp-server
  - G8_MCP_server_expone_tools
  - G7_son_MCP_clients

rag_tools:
  - context7: contexto_10M_tokens_real
  - ChromaDB: embeddings
  - bge-small-en-v1.5: modelo_embeddings_24MB_HF
  - LightRAG: github.com/HKUDS/LightRAG
  - Haystack: github.com/deepset-ai/haystack

adaptadores_cuantizacion:
  - Unsloth_Dynamic_2_0: github.com/unslothai/unsloth
  - bartowski: github.com/bartowski  # mejor_cuantizacion_community
  - GGUF_format
  - llama-cpp-python: github.com/abetlen/llama-cpp-python

frameworks:
  - pydantic: validacion_schemas
  - PEFT: adapters
  - LoRA: fine_tuning
```

### GAP #44 — Merge Rule con snapshot_branch

```yaml
auto_merge_when: [G4_AUDIT_approved, G5_CONSENSO_approved, tests_pass]
if_any_fails: [PR_open, M3_chat_notified, MAX_decides]
snapshot_branch: snapshot-vX.Y.Z
versioning: semver
```

### GAP #45 — Repair v1.0 (5 Pasos Detallados)

```yaml
paso_1: retry_simple  # 3_intentos
paso_2: context_compression  # L1/L2
paso_3: fallback_model_agent
paso_4: restore_checkpoint
paso_5: escalate  # coordinator_decide
```

### GAP #46 — Patch Log Histórico

```yaml
v1_0_0_a_v1_0_5: secciones_1-30_originales
v1_0_6_2026-06-28: patch_031_9_modelos_GGUF_detallados
v1_0_7_2026-06-28: patch_032_10_agentes_consejo
v1_0_8_2026-06-28: patch_033_sistema_Skills
v1_0_9_2026-06-28: patch_034_Kimi_K2_como_agente
v1_0_10_2026-06-28: patch_035_investigacion_multi_fuente
```

### GAP #47 — Adaptive Chunk Size (OOS)

```yaml
caracteristica: tamaño_de_cada_parte_cambia_DINAMICAMENTE
ejemplo:
  parte_1: 400_lineas
  parte_2: 1500_lineas
  parte_3: 650_lineas
regla: NO_existe_tamano_fijo
```

### GAP #48 — Auto Format Negotiation (OOS)

```yaml
NO_pregunta_simplemente: markdown_o_zip
pregunta_INTELIGENTEMENTE:
  detectado_en_salida: [codigo, diagramas, documentacion, configuracion, tests]
  recomendacion_automatica: Artifact_+_ZIP_+_Repositorio_Git
  pregunta: deseas_usar_esta_configuracion_SI_MODIFICAR
```

### GAP #49 — Agentes Colmena Investigación (5 específicas)

```yaml
09_agentes/colmena_investigacion/:
  github_search.py: REST_+_GraphQL
  hf_search.py: HF_API
  web_search.py: DuckDuckGo_+_scraper
  youtube_search.py: YouTube_Data_API_v3_transcripts
  mcp_search.py: MCP_servers
```

### GAP #50 — Investigación Multi-Fuente Detalles

```yaml
agente_github: API_github.com_REST_+_GraphQL_busquedas_repos_codigo_issues_stars_commits
agente_huggingface: API_huggingface.co_REST_busquedas_modelos_datasets_spaces
agente_web: API_duckduckgo_+_scraper_busquedas_docs_oficiales_awesome_lists_papers_blogs
agente_youtube_NUEVO: API_youtube-data-api_v3_busquedas_videos_transcripts_canales_verificados_uso_tutoriales_visualizaciones
agente_mcp: API_github_modelcontextprotocol_servers_busquedas_servers_tools_registries
```

### Resumen Total Gaps Acumulados

```yaml
1er_patch_V1: 20
2do_patch_V2: 13_nuevos_total_33
3er_patch_V3: 17_nuevos_total_50
```

---

## PATCH-AUDITORIA-GAPS-V2: 13 Gaps Nuevos (2da Pasada)

### GAP #21 — Declaración de Apertura Obligatoria

```yaml
cada_salida_debe_empezar_con: |
  > system_prompt_mythos_ejecutado
  > input_block: ACTIVO
  > goals: 5 [primary, secondary, success, failure, restriction]
  > pasos: 12
  > checkpoint: listo
  > recovery_json: listo
  > refutacion: pendiente
  > validacion: pendiente

regla: si_no_puede_escribir_esto_NO_genera_respuesta
```

### GAP #22 — 3 Revisiones del Input

```yaml
revision_1_comprension:
  - que_pidio_exactamente
  - objetivo_principal
  - output_esperado

revision_2_restricciones:
  - que_restricciones_hay
  - que_NO_puede_hacer
  - que_formato_espera

revision_3_riesgos:
  - que_puede_salir_mal
  - que_informacion_falta
  - que_asumi_sin_verificar

si_falla: pedir_aclaracion_antes_de_procesar_NO_inventar_NO_asumir
```

### GAP #23 — Checkpoint JSON Estructura

```json
{
  "checkpoint_id": "uuid",
  "task_id": "uuid",
  "timestamp": "iso8601",
  "paso_actual": 1-12,
  "input_literal": "string (EXACTO, no modificado)",
  "goals_locked": true,
  "resultados_parciales": {"paso_1": "string", "paso_2": "string"},
  "validation_passed": true,
  "violations": []
}
```

### GAP #24 — Recovery JSON Estructura

```json
{
  "recovery_id": "uuid",
  "task_id": "uuid",
  "failed_at_paso": 1-12,
  "failed_at_checkpoint": "uuid del último válido",
  "error": "string",
  "input_literal": "string (para retomar desde literal)"
}
```

### GAP #25 — Input Engine 11 Componentes (Detalle)

```yaml
01_canonical_input_graph_CIG:
  cada_frase_genera_12_nodos:
    - objetivos_restricciones_requisitos_suposiciones
    - datos_recursos_dependencias_prioridades
    - riesgos_entregables_criterios_aceptacion
    - preguntas_abiertas
  nodo: ID_unico_N51, tipo, texto_original, estado, prioridad, dependencias

02_atomic_requirement_extraction:
  NO_parrafos_REQUISITOS_ATOMICOS
  REQ-001_a_REQ-127+
  cada_requisito_tiene_vida_propia

03_dependency_graph:
  REQ-8 → REQ-15 → REQ-44 → REQ-93
  si_falla_invalida_dependientes

04_decision_graph:
  cada_decision_importante_nodo_independiente
  PostgreSQL_MySQL_SQLite_MongoDB
  NUNCA_olvida_por_que_eligio

05_memory_index:
  TODO_indexado_NO_resumido
  objetivo → nodo_8 → prompt_original → linea_exacta → mensaje_original
  siempre_volver_al_origen

06_plan_compiler:
  NO_divide_texto_divide_nodos
  127_requisitos → 36_grupos → 198_tareas → 634_subtareas

07_task_DNA_15_campos:
  - ID_objetivo_entradas_salidas_dependencias_restricciones
  - skills_agentes_prioridad_riesgos_pruebas_estado
  - contexto_referencias_fuente_original
  sin_instrucciones_ambiguas

08_context_loader:
  agente_NUNCA_recibe_todo
  solo_subtarea_dependencias_restricciones_contexto_referencias

09_completeness_engine:
  antes_de_dividir:
    - todos_requisitos_tienen_duenho
    - todos_tienen_prioridad
    - todos_tienen_dependencias
    - todos_tienen_criterio_aceptacion
    - todos_tienen_contexto_suficiente
  si_alguno_falla_NO_planifica

10_coverage_matrix_PIEZA_MAS_IMPORTANTE:
  matriz: requisito | tarea | agente | estado
  si_existe_requisito_sin_tarea_asignada_sistema_detecta

11_reverse_traceability:
  al_finalizar:
    frase_1 → TASK-12, TASK-47, TASK-81 → resultado_validado
  con_TODAS_las_frases_usuario
  si_alguna_NO_puede_trazarse_RECHAZO
```

### GAP #26 — 17 Mejoras al Input Engine

```yaml
01_intent_graph: objetivo_principal_secundarios_implicitos_futuros_opcionales_asignar_prioridades
02_constraint_engine: cada_restriccion_nivel [obligatoria, preferida, opcional] tipos [sin_coste, codigo_abierto, compatible_android, offline, sin_api, tiempo_max, idioma, licencia, hardware]
03_anti_ambiguity_engine: detecta_rapido_seguro_grande_barato_simple_mejor_convierte_valores_medibles
04_hidden_requirement_detector: busca_requisitos_NO_escritos
05_contradiction_engine_clasificado: [logica, temporal, tecnica, arquitectonica, legal, coste, rendimiento]
06_assumption_registry: suposicion_motivo_confianza_impacto_quien_la_hizo
07_confidence_engine: cada_requisito_nivel_confianza [98%, 83%, 51%, 27%]
08_multi_interpretation_engine: NO_genera_una_genera_VARIAS [A, B, C, D]
09_scope_boundary_detector: que_esta_dentro_fuera_alcance
10_completeness_score: [informacion_suficiente, riesgo_alucinacion, informacion_faltante, requisitos_definidos, contradicciones]
11_context_partition: divide [negocio, codigo, arquitectura, seguridad, ux, infraestructura, documentacion]
12_traceability_ID: cada_frase_identificador_unico_decision_responde_proviene_de_mensaje_4_linea_18_frase_7
13_hallucination_risk_analyzer: estima_partes_mayor_riesgo
14_requirement_normalizer: "haz_una_aplicacion" → [frontend, backend, autenticacion, persistencia, api, despliegue]
15_impact_analyzer: antes_de_modificar_requisito_calcula_que_tareas_decisiones_agentes_se_veran_afectados
16_informacion_inmutable: DOS_versiones [prompt_original_solo_lectura, modelo_estructurado]
17_registro_decisiones: [alternativas, criterios, evidencias, agente_responsable, fecha, nivel_confianza]
```

### GAP #27 — Output Engine 13 Componentes (Detalle)

```yaml
01_output_planner: calcula_salida_estimada [15_paginas, 28000_palabras, 120_archivos, 35_modulos, 6_diagramas, 3_tablas]
02_output_graph: proyecto_nodos_independientes [arquitectura, backend, frontend, BD, API, tests, docs, deployment, manual]
03_smart_chunking: divide_por_SIGNIFICADO_NO_cantidad_texto
04_dynamic_output_engine: estima [tokens, memoria, tiempo, coste, tamano_final] calcula_1_3_15_52_100_partes
05_manifest: indice_antes_de_entregar_usuario_siempre_sabe_que_recibira
06_output_registry: cada_salida_tiene [ID, version, dependencias, estado, checksum, autor, fecha, destino]
07_output_router_menu_formatos: [markdown, artifact, html, pdf, docx, pptx, json, yaml, csv, zip, git, db, drive, mcp, api, otro]
08_destination_engine_adaptadores: [markdown_artifact_git_drive_notion_mcp_api_db_s3_cloud]
09_streaming_output: modulo_1_validado_entregado_luego_modulo_2
10_output_validator: [completa, sin_dependencias_rotas, modulos_existentes, enlaces_funcionan, cumple_formato]
11_multi_target_delivery: parcialmente_documentado
12_13: por_leer
```

### GAP #28 — P35/P36/P37 Mejoras 100X

```yaml
P35_auto_mejora_continua:
  antes: audita_cada_7_dias
  ahora: EVOLUCIONA_cada_hora_con_aprobacion_selectiva
  - auto_mejora_cada_hora_cambios_pequenos
  - auto_rollback_si_empeora_metricas
  - sandbox_experimentacion
  - si_mejora_funciona_24h_promueve_produccion
  - notifica_MAX_solo_si_significativa
  - aprende_que_tipo_mejoras_acepta_MAX
  archivo: g5/auto_evolucion/

P36_experimentacion_AB_bayesian:
  antes: AB_para_elegir_mejor
  ahora: BAYESIAN_MULTI_ARMED_BANDIT
  - multi_armed_bandit
  - explota_conocido_explora_nuevas
  - predice_ganador_95%_confianza
  - se_auto_ajusta
  - 10+_variaciones_paralelo
  - resultados_Knowledge_Graph
  archivo: g5/experimentation/v2/

P37_pricing_tiempo_real:
  antes: dashboard_costos
  ahora: ECONOMIA_PREDICTIVA_auto_optimizacion
  - predice_costo_30_dias_anticipacion
  - auto_cambia_modelos_mas_baratos
  - marketplace_modelos
  - NEGOCIACION_si_costo_sube
  - reporte_mensual_automatico
  - alertas_inteligentes
  archivo: g5/economia/v2/
```

### GAP #29 — EVENTS.JSON Types Específicos

```yaml
campos: [event_id, type, timestamp, source, task_id, payload]

types:
  - TASK_CREATED
  - TASK_STARTED
  - TASK_DONE
  - TASK_FAILED
  - CONSENSUS_REQUIRED
  - BUILD_FINISHED
  - GROUP_HEARTBEAT
  - RETRY_TRIGGERED
  - TIMEOUT_REACHED
  - CANCELLED
```

### GAP #30 — Agentes Universales (N API keys dinámica)

```yaml
regla: orquestador_puede_usar_1_a_50_API_keys
cada_agente_toma_API_key_disponible
si_50_agentes_necesitan_LLM_via_API_toman_disponibles
NO_usa_una_sola_key

ejemplo:
  Claude_Code: 1_API_key
  orquestador: N_agentes_con_N_API_keys
  50_keys → 50_agentes_paralelo
  1_key → 1_agente_secuencial
```

### GAP #31 — Decisiones Confirmadas por MAX

```yaml
de_BORRADOR_LISTA_APROBADOS_seccion_3:
  G5 = mismo_grupo = consenso_+_orquestador  # NO_dos_grupos_separados
  G6_BUILD_eliminado  # era_invento
  G7/G8_confusion → ahora_solo_G6_ASISTENTES
  total: 6_grupos_G1_G2_G3_G4_G5_G6
  MiniMax_M3 = LIDER_de_G5_como_SKYNER_via_1_NVIDIA_NIM
  M2.7_solo_crea_G5_inicialmente_despues_G5_programa_todo
  orquestador_MANEJA_agente_NO_al_reves
  DSL_DAG_nunca_prompt_libre
  input_sagrado_NO_modifica_NO_resume_NO_parafrafrasea
  todo_se_reporta_M3_chat_+_MAX_por_Telegram
  1_HF_Space_por_grupo_own_token_aislada
  ZeroGPU_comparte_no_nos_afecta_usamos_API
  GitHub_fuente_de_verdad
  SandboxDB_por_grupo_estado_temporal
  RAM_16GB_por_HF
  Q5_Q4_segun_peso_modelo
  bartowski_recomendado_GGUF_mejor_cuantizacion_community
  Unsloth_Dynamic_2_0_segunda_opcion
  context7_contexto_extendido_10M_tokens
```

### GAP #32 — Ubicaciones Proyectos Iniciales

```yaml
projects/:
  nct-fase0/
  interfaz-fusionada/
  crazy-wall/
```

### GAP #33 — Kimi K2.7-Code Especificaciones

```yaml
vendor: Moonshot_AI_Kimi_K2.7_Code
HF: moonshotai/Kimi-K2.7-Code
funcion: generacion_codigo_produccion
provider_OpenCLAW: si_config_nativo
compatible_Claude_Code: si_via_API_Moonshot
fortalezas: [tool_calling_avanzado, agentic_coding, codigo_coherente]
cuando_se_elige: [TM01, TM02 cuando_lenguaje_python_ts_rust_go]
temperatura: 0.2_default
output: [patch_unified_diff, JSON_metadata]
endpoint: Groq_provider_o_NVIDIA_NIM
```

---

## PATCH-AUDITORIA-GAPS-V4: 18 Gaps Nuevos (4ta Pasada)

### GAP #51 — M2.7 Flujo Simplificado (5 Pasos)

```yaml
paso_1_recibir:
  - leer_TASK_json
  - verificar_schema
  - output: task_recibida_ok

paso_2_verificar:
  - chequear_dependencias
  - chequear_keys_necesarias
  - chequear_permisos
  - output: dependencias_ok

paso_3_ejecutar:
  - ejecutar_tarea
  - output: ejecucion_resultado

paso_4_validar:
  - tests_pasan
  - output_compilado
  - secrets_detectados_no
  - output: validacion_ok

paso_5_reportar:
  - escribir_resultado_STATE_json
  - escribir_HISTORY_json_acumulativo
  - notificar_M3_chat
  - output: reporte_enviado

si_falla_cualquier_paso:
  - escribir_RECOVERY_JSON
  - rollback_si_necesario
  - escalar_M3_chat_si_retry_mayor_2
```

### GAP #52 — División de Tareas Grandes (Regla)

```yaml
regla: si_tarea_mayor_5_subtareas → dividir_en_bloques
cada_bloque = checkpoint_separado
cada_bloque = recovery_independiente

tarea_grande → divide:
  bloque_1 → checkpoint_1 → output_1
  bloque_2 → checkpoint_2 → output_2_depende_output_1
  bloque_3 → checkpoint_3 → output_3_depende_output_2

cada_bloque:
  - input_literal_preservado
  - 5_GOALS_fijados
  - 12_PASOS_ejecutados
  - CHECKPOINT_JSON_escrito
  - REFUTACION_pasada
  - VALIDACION_pasada
  - OUTPUT_entregado
  - RECOVERY_JSON_listo_si_falla
```

### GAP #53 — 10 Módulos MAXBRY (P9)

```yaml
M1_bootstrap: instalador_+_actualizador_+_lanzador
M2_nucleo_orquestador: planificador_+_scheduler_+_motor_decisiones
M3_gestor_memoria: ChromaDB_+_bge-small_+_embeddings
M4_scheduler: Dramatiq_+_Redis_+_colas_paralelas
M5_gestor_agentes: registry_+_colmena_+_distribucion
M6_gestor_skills: catalogo_+_generador_+_versionado
M7_gestor_modelos_IA: API_keys_+_profiles_+_circuit_breaker
M8_sistema_seguridad: cifrado_+_auth_+_licencias
M9_sistema_actualizacion: versiones_+_diffs_+_rollback
M10_sistema_monitorizacion: logs_+_metricas_+_alertas_+_dashboards

cada_modulo:
  - carpeta_independiente
  - API_publica_clara
  - actualizable_sin_reinstalar
  - tests_propios
  - version_propia
  - metadata_versionada
```

### GAP #54 — Sistema de Seguridad (6 Capas)

```yaml
capa_1_cifrado_comunicacion: HTTPS/TLS
capa_2_autenticacion: API_keys_tokens_1h_OAuth2_opcional
capa_3_firmas_digitales: cada_solicitud_firmada_criptograficamente
capa_4_rate_limiting: 100_req/min_1000_req/h
capa_5_licencias: cada_instalacion_unica_servidor_valida_arranque
capa_6_respuestas_minimas: API_solo_devuelve_necesario_nunca_paths_internos
```

### GAP #55 — Núcleo Vía API (Cliente Ligero vs Servidor)

```
USUARIO → Cliente_M3_local_5MB  # lo_que_usuario_tiene
                                    ↓
                              API_Orquestador_servidor  # lo_que_NO_se_descarga
                                ├── planificador
                                ├── memoria_global
                                ├── scheduler
                                ├── motor_decisiones
                                ├── agentes
                                └── modelos_IA

ventajas:
  - usuario_NO_recibe_codigo_nucleo
  - NO_puede_copiar_planificador
  - actualizaciones_sin_reinstalar
  - revocar_accesos
  - codigo_importante_NUNCA_sale_servidor
```

### GAP #56 — P8 Bootstrap Instalación Autónoma

```yaml
responsabilidades:
  1: detectar_OS [Linux, Mac, Windows]
  2: detectar_arquitectura [x86_64, arm64]
  3: verificar_recursos [CPU, RAM, disco, red]
  4: comprobar_dependencias_necesarias
  5: instalar_automaticamente
  6: crear_estructura_directorios
  7: inicializar_base_datos
  8: generar_configuraciones_iniciales
  9: generar_claves_criptograficas
  10: descargar_solo_componentes_necesarios
  11: iniciar_orquestador

caracteristicas:
  - tamano_maximo: 5_MB
  - NO_contiene_logica_orquestador
  - solo_instalador_+_actualizador_+_lanzador
  - descarga_componentes_bajo_demanda
  - verificacion_criptografica_integridad
```

### GAP #57 — 8 Principios Rectores Sistema Razonamiento

```yaml
1_INPUT_SAGRADO: input_NUNCA_modifica_resume_parafrafrasea_reinterpreta
2_DSL_DAG_NUNCA_PROMPT_LIBRE: salida_siempre_JSON_estructurado
3_DETERMINISMO: mismo_input_+_config_+_LLM = misma_forma_razonamiento
4_UNIVERSALIDAD: cualquier_LLM_puede_usarlo
5_EXTERNALIDAD: vive_en_/reasoning_system/_NO_en_/orquestador/
6_EDITABILIDAD_POR_ARCHIVOS: cambiar_goal_step = editar_archivo_NO_codigo
7_AUDITABILIDAD: cada_ejecucion_produce_log_auditable
8_AISLAMIENTO: sistema_NO_contamina_orquestador_ni_LLM
```

### GAP #58 — INPUT BLOCK Estructura JSON

```json
{
  "input_block": {
    "raw": "<<input EXACTO del usuario, sin tocar>>",
    "received_at": "<<timestamp ISO 8601>>",
    "source": "<<nombre del llamador>>",
    "checks": {
      "preserve_verbatim": true,
      "no_summarize": true,
      "no_paraphrase": true,
      "no_modify": true
    },
    "status": "ACCEPTED | REJECTED"
  }
}
```

### GAP #59 — 7 Prohibiciones Explícitas Input Block

```yaml
1_resumir_input: usuario_pidio_algo_especifico_NO_resumen
2_parafrafrasear_input: cambia_matiz_semantico
3_mejorar_redaccion_input: usuario_escribio_como_quiso
4_agregar_contexto_NO_esta: contamina_intencion_original
5_quitar_partes_irrelevantes: LLM_decide_que_es_relevante
6_traducir_input: cambia_idioma_cambia_semantica
7_reordenar_ideas_input: estructura_sintactica_porta_significado
```

### GAP #60 — 12 Pasos Standard con Prompts Específicos

```yaml
01_literal_read:
  prompt: "INSTRUCCION_SAGRADA_NO_INTERPRETAR_NO_RESUMIR_NO_MODIFICAR"
  output: { input_accepted: true, raw_acknowledged: "..." }
  si_falla: REJECTED

02_think:
  prompt: "Considerando goals e input verbatim, que estas entendiendo"
  output: { thinking: [obs1, obs2, obs3] }

03_plan:
  prompt: "Genera plan 3-7 pasos para cumplir goal_primary"
  output: { plan: [{step, action, expected_output}] }

04_decompose:
  prompt: "Para cada paso plan identifica subtareas atomicas"
  output: { decomposition: [{plan_step, atomic_tasks}] }

05_hypotheses:
  prompt: "Para cada atomic_task propone 2-4 hipotesis alternativas"
  output: { hypotheses: [{task_id, alternatives}] }

06_swarm:
  prompt: "Para cada hipotesis evalua esfuerzo_riesgo_alineamiento"
  output: { swarm_results: [{h_id, effort_low_med_high}] }

07_critic:
  prompt: "Como critico que falla en cada hipotesis"
  output: { critiques: [{h_id, weakness, severity}] }

08_simulate:
  prompt: "Simula paso a paso ejecucion hipotesis ganadora"
  output: { simulation: [{phase, result, issues}] }

09_validate:
  prompt: "La simulacion cumple goal_success respeta goal_restriction"
  output: { validation: {meets_success, respects_restriction} }

10_consensus:
  prompt: "Considerando thinker_critic_simulator_validator cual es la decision"
  output: { consensus: {decision, confidence_0-1, votes} }

11_report:
  prompt: "Genera reporte final en formato DSL"
  output: { report: {<DSL_final>} }

12_audit:
  prompt: "Auditoria se respeto input sagrado se ejecutaron 12 pasos"
  output: { audit: {input_respected, verdict_PASS_FAIL, notes} }
```

### GAP #61 — M3 en Cada Salida (Formato)

```yaml
antes_de_cada_salida_mostrar: |
  > system_prompt_mythos_ejecutado
  > goals: [lista]
  > pasos_completados: [1-12]
  > checkpoints: [uuid]
  > refutacion: [ok_fail]
  > validacion: [ok_fail]

despues_de_cada_salida_mostrar: |
  > self_audit: [ok_fail]
  > input_preserved: true
  > output_validated: true
```

### GAP #62 — M2.7 en Cada Ejecución (Log)

```yaml
log_en_STATE_json:
  > system_prompt_mythos: executed
  > paso_actual: 1-5
  > checkpoint_id: uuid
```

### GAP #63 — Refutación (5 Preguntas Obligatorias)

```yaml
preguntas_obligatorias_antes_de_output_final:
  - que_asumi_sin_verificar
  - que_puede_romper_esta_salida
  - que_restriccion_viole
  - que_informacion_invente
  - que_dependencias_NO_chequee

si_alguna_problematica:
  - volver_paso_1
  - NO_presentar_output_refutado
```

### GAP #64 — Estructura Sistema Razonamiento

```yaml
/reasoning_system/:
  README.md
  config.json
  goals/  # 5_goals_standard
  goals_turbo/  # 7_goals_extra
  steps/  # 12_pasos_standard
  steps_turbo/  # 33_pasos_extra
  prompts/:
    standard_dsl.json
    turbo_dsl.json
    input_block_rule.json
  runner.py
  loader.py
  api.py
```

### GAP #65 — Validación Obligatoria (Checks)

```yaml
checks_obligatorios_antes_output_final:
  - input_preservado_verbatim
  - output_NO_resume_input
  - output_NO_parafrafrasea_input
  - output_responde_5_GOALS
  - output_cumple_restriccion_innegociable
  - checkpoints_escritos
  - refutacion_pasada
  - consensus_aplicado_si_aplica

si_alguna_falla: REJECTED_recovery
```

### GAP #66 — Protocolo de Recuperación

```yaml
si_tarea_falla:
  1: escribir_RECOVERY_JSON_inmediatamente
  2: identificar_ultimo_CHECKPOINT_valido
  3: si_retry_count_menor_2: rollback_checkpoint_retry
  4: si_retry_count_mayor_igual_2: escalar_M3_chat
  5: M3_chat_decide: mas_retries, redesign, cancelar

NUNCA:
  - inventar_output_cuando_falla
  - saltarse_pasos_para_avanzar
  - ignorar_violaciones
  - borrar_checkpoints_validos
```

### GAP #67 — Uso de Memoria M3 y M2.7

```yaml
M3_chat_memoria:
  - memory_topic_append_despues_cada_sesion_importante
  - leer_memory_topic_read_al_inicio_cada_sesion_nueva
  - BORRADOR_LISTA_APROBADOS_md = fuente_de_verdad_visible

M2_7_memoria:
  - leer_BORRADOR_LISTA_APROBADOS_md_al_iniciar
  - STATE_json = estado_actual
  - HISTORY_json = historico_completo_NUNCA_borrar

BORRADOR_LISTA_APROBADOS_md:
  - se_actualiza_con_CADA_cambio_aprobado
  - se_actualiza_con_CADA_nueva_propuesta
  - se_actualiza_con_CADA_tarea_completada
  - es_la_fuente_de_verdad_para_todo
```

### GAP #68 — Integración System Prompt Mythos + Razonamiento Externo

```yaml
diferencia:
  system_prompt_mythos: reglas_y_flujo_visible
  /reasoning_system/: libreria_Python_con_funciones

ambos_deben_usarse:
  M3_lee_system_prompt_mythos_al_inicio
  M3_usa_reasoning_system_reason_para_tareas_complejas
  M2_7_lee_system_prompt_mythos_al_inicio
  M2_7_usa_reasoning_system_reason_si_necesita_razonar

integracion:
  system_prompt_mythos = capa_comportamiento
  reasoning_system = capa_ejecucion
  juntos = sistema_completo
```

---

## DOC NCT-LOP-100X-2026-06-22: Loop Multi-Level + Fusión MiniMax/Kimi K

### JSON Summary for Mavis M3

```yaml
$schema: https://NCT/turbo/schemas/lop-system-v100.schema.json
document_id: NCT-LOP-100X-2026-06-22
target: Mavis_M3
package: nct_coordinator
namespace: nct.lop.v100
lexicon: [AI, AGENT, AGENT_ENGINEERING, AUTOMATION, FSM, DSL]
version: 100.0.0
```

### 6 Niveles de Autonomía (Tabla Maestra)

```yaml
L1_MANUAL: [pasos_discretos, IA_0%, memoria_volatil, reparacion_manual, verificacion_humana, micro_tareas_depuracion_fina]
L2_SEMI_MANUAL: [minutos, IA_0%, memoria_opcional, manual_asistida, humana+regla, scripting_one_shots]
L3_SCHEDULED_AUTOMATIC: [horas, IA_0%, memoria_persistente, reintentos_limitados, regla+log, cron_ETL_polling]
L4_SUPERVISED_AUTONOMOUS: [horas_a_24h, IA_0%, persistente, pipeline_5_pasos, adversarial_3_capas, features_completas_refactors]
L5_CONTINUOUS_AUTONOMOUS_72H_PLUS: [72h_a_mes, IA_0%, jerarquica_EROS_3_tier, rollback+fallback_modelo, multicapa+drift, proyectos_largos_multi_sprint]
L6_EVOLUTIONARY_AUTONOMOUS: [indefinido, IA_0%, meta_memoria, auto_mejora, autoevaluacion, self_improve_self_tune]
```

### Mejora 100× = Qué se Multiplica por 100

```yaml
1_fase_ejecucion ×10: 10_fases_FSM
1_tipo_worker ×10: 12_modelos_tarea
1_nivel_autonomia ×6: 6_niveles
0_loops_anidados ×3: 3_anidaciones
1_capa_verificacion ×3: 3_capas_adversariales
0%_trazabilidad ×100: 100%_event_sourcing_snapshots
1_plan_estatico ×5: 5_versiones_avanzadas_loop
0_auto_mejora ×1: nivel_6_evolutivo
1_modo_fallo ×5: pipeline_repair_5_pasos
1_idioma_salida ×1: multi_idioma_controlado_schema

producto_ortogonales: ~13_500_000
normalizado: 100x_para_evitar_sobre_venta
medible_reproducible_verificable: por_3_capas_adversariales
```

### Diagrama General 6 Niveles (ASCII)

```
L1_MANUAL              ►  usuario → bloque → usuario → bloque
L2_SEMI_MANUAL         ►  usuario → plan_IA → aprueba → ejecuta
L3_SCHEDULED           ►  trigger_cron_evento → FSM_10_fases → log
L4_SUPERVISED          ►  FSM → multi_agente → verifier_3_capas
L5_CONTINUOUS_72h+     ►  meta_objetivo → EROS → repair → re_plan
L6_EVOLUTIONARY        ►  loop_meta: autoevalúa_reescribe_plan
```

### Contrato JSON Canónico para Describir un Nivel

```json
{
  "level": "L5_CONTINUOUS_AUTONOMOUS_72H_PLUS",
  "schema_version": "1.0.0",
  "horizon_hours": 72,
  "fsm_phases": ["P0","P1","P2","P3","P4","P5","P6","P7","P8","P9"],
  "agents": ["orchestrator","planner","executor","verifier","consolidator","repairer"],
  "memory": {"type": "eros_3_tier", "tier_3": "raw_logs", "tier_2": "strategic_pulses", "tier_1": "orchestrator_summary"},
  "guardrails": {"max_tokens_per_call": 200000, "max_runtime_hours": 96, "max_retries_per_step": 3, "rollback_on": ["drift_kl_gt_0.02", "pad_arousal_gt_0.8", "verifier_fail"]}
}
```

### Fusión MiniMax + Kimi K — Conflictos Resueltos

```yaml
conflicto_1_agente_grande_vs_100_workers: granularidad_adaptativa_por_router
conflicto_2_verifica_final_vs_cada_paso: verificacion_multicapa_intercalada
conflicto_3_ansiedad_SIGKILL_vs_espera_confirmacion: escalado_gradual [L1_log, L2_pause, L3_SIGKILL]
conflicto_4_EROS_comprime_vs_summaries_aisla: EROS_sobre_summaries_doble_compactacion
conflicto_5_memoria_event_sourcing_vs_jerarquica: memoria_hibrida_jerarquica_journaling
```

### 7 Mejoras que la Fusión Habilita

```yaml
1_doble_watchdog: PAD + Anti-drift_sobre_mismo_worker
2_triage_emocional_y_estructural: ansiedad_acoplado_a_drift
3_verificacion_cruzada_cruzada: A_verifica_B_B_verifica_A_verifier_adversarial
4_compactacion_jerarquica_resumenes_estructurados: cada_tier_hereda_contexto_limpio_inferior
5_repair_reintentos_fallback_checkpoint_compresion_escalado: orden_estricto
6_memoria_aprendizaje: cada_ciclo_guarda_embeddings_drift_ansiedad_para_reusar
7_orquestador_100_determinista: 0%_IA_en_FSM_auditoria_trivial
```

### Esquema JSON Común Task Model

```json
{
  "$id": "https://NCT/turbo/schemas/task-model.schema.json",
  "type": "object",
  "required": ["id","title","min_steps","steps","contracts"],
  "properties": {
    "id": {"type":"string","pattern":"^TM[0-9]{2}_[A-Z_]+$"},
    "title": {"type":"string"},
    "level": {"enum":["L1","L2","L3","L4","L5","L6"]},
    "min_steps": {"type":"integer","minimum":10},
    "steps": {"type":"array","minItems":10},
    "contracts": {"type":"object"},
    "kpis": {"type":"array"},
    "failure_modes": {"type":"array"}
  }
}
```

### 5 Loop Versions Avanzadas (ALV)

```yaml
ALV_LOP_GENESIS_BASELINE: |
  USR → P0 → P1 → P2 → P3 → P4 → P5 → P6 → P7 → P8 → P9 → OUT
         └─────────────── repair_loop ───────────────────┘

ALV_LOP_TITANIUM_PARALLEL_GRAPH: |
         ┌─ P4a ─┐
  P3 → P4 →├─ P4b → P5 → P6 → P7 → P8 → P9
         └─ P4c ─┘

ALV_LOP_QUANTUM_FRACTAL_NESTED: |
  P4 → loop_interno { P0' → P1' → P2' → ... → P9' }
  profundidad_maxima: 5

ALV_LOP_SINGULARITY_EVOLUTIONARY: |
  P9 → measure → tune → P0_next → ... → P9_next
       ▲                                  │
       └────────── feedback ──────────────┘
  solo_L6

ALV_LOP_NEXUS_FUSION_FULL: |
  router(task_type, level) → {GENESIS | TITANIUM | QUANTUM | SINGULARITY}
```

### 12 Propuestas Mejoradas (PROP-01 a PROP-12)

```yaml
PROP-01_FSM_determinista: tabla_transiciones_inmutable, sin_IA, sin_random, sin_red, auditability_score_1.0
PROP-02_WorkerPool_async: asyncio.gather_con_semaforo_K=10, context_isolation, frozen_subagent
PROP-03_Monitor_triple: PAD_arousal_pleasure_dominance + Ansiedad_L1_L2_L3 + Anti_drift_KL_gt_0.02_rollback
PROP-04_Verifier_3_capas: capa1_adversarial + capa2_cruzada + capa3_maker_checker_JSON_Schema
PROP-05_EROS_3_tier: tier3_raw_logs_100% + tier2_strategic_pulses_<=20% + tier1_orchestrator_summary_<=5%
PROP-06_Repair_5_pasos: fail → retry(3) → compress(L1_L2) → fallback_model → restore_checkpoint → escalate
PROP-07_Memoria_hibrida: journaling_event_sourcing + memoria_jerarquica_EROS, append_only, snapshots_firmados
PROP-08_Router_adaptativo: señales [intent, type, level, budget, history] → terna [modo, ruta, level, agents]
PROP-09_SelfTuner_evolutivo_L6: propone_prueba_cambios_propio_codigo_prompts, sandbox_first, meta_verify_required
PROP-10_DSL_Task_Models: cada_TM_descrito_YAML_JSON_validable, min_steps_10, schema_validated
PROP-11_Circuit_breaker: N_fallos → open, half_open_prueba_1, backoff_base_2^attempts
PROP-12_Observabilidad_OTel: cada_fase_spans_atributos_estables, trace_id_propagation, slo_compliance
```

### 12 Modelos de Tarea (TM01-TM12)

```yaml
TM01_ARCHITECTURE_DESIGN: 14_pasos_classify_intent_research_decompose_design_validate_document
TM02_CODE_GENERATION: 14_pasos_parse_spec_scaffold_gen_models_apis_tests_lint_security_commit
TM03_RAG_RESEARCH: 14_pasos_parse_expand_embed_retrieve_rerank_synthesize_fact_check_dedup_deliver
TM04_VALIDATION_QA: 14_pasos_load_define_oracles_static_lint_types_unit_integration_mutation_fuzz_security_adversarial_gate
TM05_REPAIR_REFACTOR: 14_pasos_detect_classify_propose_branch_apply_keep_behavior_verify_update_pr_review_merge_learn
TM06_TEST_SUITE: 14_pasos_parse_enumerate_prioritize_gen_unit_edge_property_contract_integration_e2e_perf_run_flaky_coverage
TM07_DEPLOY_RELEASE: 14_pasos_select_verify_signature_sbom_policy_stage_smoke_load_chaos_metrics_canary_5_25_100_tag_notify
TM08_DOCUMENTATION: 14_pasos_parse_audience_select_template_outline_draft_code_diagrams_glossary_links_readability_translation_review_publish_feedback
TM09_DATA_PIPELINE: 14_pasos_parse_source_sink_contract_diff_select_extract_validate_transform_dedup_enrich_quality_load_lineage_observe_sla
TM10_SECURITY_AUDIT: 14_pasos_parse_target_assets_sast_secret_sca_license_container_infra_dast_threat_prioritize_remediation_adversarial_deliver
TM11_LONG_HORIZON_72H_PLUS: 14_pasos_global_strategic_milestones_resource_parallel_pad_anxiety_drift_checkpoint_repair_eros_replan_report_finalize
TM12_EVOLUTIONARY_SELF_IMPROVEMENT: 14_pasos_collect_metrics_mine_cluster_propose_sandbox_benchmark_compare_promote_update_skill_resource_router_meta_verify_release_restart
```

### Mapa de Fusión Final

```yaml
origen_MiniMax_en_nct_coordinator:
  - dual_classifier → classifier_py
  - team_engine_3_rondas → worker_pool_py
  - verifier_adversarial → verifier_py
  - structured_summaries → context_isolator_py
  - coordinator_consolidator → consolidator_py

origen_Kimi_K_en_nct_coordinator:
  - OK_Computer_Skills_Swarm → router_py
  - frozen_subagents → context_isolator_py
  - worker_pool_asyncio_gather → worker_pool_py
  - PAD_arousal_pleasure_dominance → monitor_py
  - anxiety_L1_L2_L3 → monitor_py
  - anti_drift_KL → monitor_py
  - EROS_3_tier → consolidator_py
  - repair_5_pasos → repair_py

NCT_nativo:
  - FSM_10_fases → fsm_py
  - 6_niveles_autonomia → fsm_py_+_router_py
  - 12_modelos_tarea → dsl_task_models_yaml
  - 5_versiones_avanzadas_loop → alvs_py
  - 12_propuestas_mejoradas → este_documento
```

### Contrato de Entrega a nct_coordinator

```yaml
nct_coordinator/:
  lop_v100/:
    __init__.py
    levels.py  # L1..L6
    alvs.py  # 5_versiones_avanzadas
    task_models/  # 12_TM_yaml
    proposals/  # 12_PROP_yaml
    schemas/  # task-model, proposal, level
```

### Ingestion Directives for Mavis M3

```yaml
- parsear_seccion_0_JSON_SUMMARY_como_contrato_entrada
- validar_cada_bloque_JSON_interno_contra_schema_declarado
- construir_arbol_dependencias_entre_propuestas_DAG_dirigido_por_fase_objetivo
- generar_backlog_implementacion_priorizado_por_kpis_riesgos
- mantener_nct_coordinator_como_paquete_adicional_sin_modificar_25_bloques_originales
- empaquetar_documento_en_nct_coordinator_lop_v100_SPEC_md_referenciar_desde_init_py
- reportar_usuario_solo_resumen_diagramas_KPIs
- versionar_modulo_como_100.0.0_semver
```

---

## DOC BLOQUE_1_F-1_F3_MOTOR_PREPARACION: Pipeline v4.4 (Consenso Claude + Kimi K + GPT)
