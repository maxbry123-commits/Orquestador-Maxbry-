# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 6)

> **Continuación**: Contiene MAPA riesgos, gaps cerrados, ejemplo completo y archivos restantes.


## DOC FUSIÓN 9723851c (cont.) — VEREDICTO FINAL DE PRESERVACIÓN

### 4 Preguntas del Veredicto

```yaml
1_arquitectura_original_preservada: >
  SI_Ninguna_fase_eliminada_Ninguna_responsabilidad_perdida

2_capacidad_original_desaparecio: >
  NO_Toda_capacidad_del_doc_base_existe_en_v4.4
  NOTA: "Fallback_Model_o_Agent"_de_F8_fue_eliminado_intencionalmente
  porque_requeria_LLM_adicional_para_repair_violando_el_objetivo
  de_reducir_LLM_Reemplazado_por_metricas_duras_+_aborto_determinista

3_fase_simplificada_en_exceso: >
  NO_F5_metricas_emocionales_renombradas_a_tecnicas_pero_funcionalidad_preservada
  F6_verificacion_LLM_reemplazada_por_codigo_puro_+_capa_transitoria
  pero_cobertura_igual_o_superior_con_DSL_expandido_por_dominio

4_nueva_arquitectura_estrictamente_superior: >
  SI_en_los_3_objetivos_del_Director
  1_Menos_LLM_de_~20%_a_~3%_amortizado
  2_Mejor_estructura_DAG_determinista_DSL_jerarquico_EROS_formalizado
  3_Multi_modal_MODE_CODE_+_MODE_MULTI_+_MODE_MIXTO_diferenciados

5_riesgos_arquitectonicos: >
  SI_20_identificados_ver_bloques_individuales
  DSL_corrupto_mitigado_AST_+_sandbox_+_aprobacion
  domain_registry_inconsistente_mitigado_validacion_jsonschema
  falso_positivo_F6_mitigado_3_capas_+_jerarquia_DSL
  loops_F8_mitigado_5_metricas_+_aborto_duro
  clasificacion_erronea_F0_mitigado_boost_rules_+_default_MIXTO
  dependencia_circular_F2_mitigado_networkx_+_aborto
  y_15_mas_documentados_en_fichas_tecnicas
```


## DOC FUSIÓN a5377cb5 — BLOQUE 2: MOTOR DE EJECUCIÓN F4 (Worker Pool + Team Engine)

### F4: Ejecución (Worker Pool + Team Engine)

```yaml
fase_F4:
  nombre_original: Fase_4_Ejecucion_Worker_Pool_+_Team_Engine
  estado_v44:
    preservado: true
    modificado: true    # Bifurcacion_por_modo_+_limites_duros_+_perfiles
    ampliado: true
  cambios:
    - "Mantiene_Worker_Pool_asyncio_hasta_100_workers"
    - "Mantiene_semaforo_maximo_10_workers_LLM_simultaneos"
    - "Añade_bifurcacion_MODE_CODE_o_MODE_MULTI_o_MODE_MIXTO"
    - "MODE_CODE_Qwen_arquitectura_a_Llama4_escritura"
    - "MODE_MULTI_Gemma4_ejecuta_DSL_predefinido"
    - "MODE_MIXTO_subtareas_CODE_a_Qwen_o_Llama4_subtareas_MULTI_a_Gemma4"
    - "Añade_limite_32K_tokens_/_30s_por_worker_con_pre_estimacion_F2"
    - "Team_Engine_3_rondas_a_opcional_segun_verification_profile"

3_modos:
  MODE_CODE_Qwen_+_Llama4:
    Worker_1_Qwen:
      perfil: architecture_generation
      input: requerimiento_+_constraints
      output: estructura_proyecto_json_schema_validado
      limite: 32K_tokens_/_30s

    Worker_2_Llama4:
      perfil: code_generation
      input: estructura_proyecto_json_+_dsl_codigo_py
      output: archivos_codigo_+_tests_schema_validado
      limite: 32K_tokens_/_30s

    Team_Engine_opcional:
      ronda_1: worker_genera_codigo
      ronda_2: verifier_revisa_con_tests_automaticos
      ronda_3: leader_aprueba_o_rechaza
      si_rechaza_a_retry_automatico_contador_F8

  MODE_MULTI_Gemma4_ejecuta_DSL:
    Worker_N_Gemma4:
      perfil: domain_specific
      input: datos_+_dsl_lt_dominio_gt_py_predefinido
      output: resultado_estructurado_schema_validado
      limite: 32K_tokens_/_30s
      NO_PIENSA: solo_ejecuta_funciones_DSL
    ejemplo_resumir_50_noticias:
      dsl_resumen_py_define:
        paso_1: extraer_titulo(texto)
        paso_2: extraer_fecha(texto)
        paso_3: resumir_parrafo(texto_max_eq_100)
      Gemma4_ejecuta_cada_funcion_no_decide

  MODE_MIXTO_Hibrido:
    subtarea_A_CODE_Crear_API_REST:
      Qwen_diseña_estructura
      Llama4_escribe_codigo
    subtarea_B_MULTI_Documentar_endpoints:
      Gemma4_ejecuta_dsl_documentar_py

limites_generales:
  - 32K_tokens_/_30s_por_worker
  - semaforo_10_workers_LLM
  - hasta_100_workers_asyncio
  - pipeline_7_pasos_por_worker

aborto: NINGUNO_en_F4_siempre_intenta_ejecutar
checkpoint: state.json["f4"]
```


### F4 Worker Pool — Ficha Técnica Completa

```python
# f4_worker_pool.py — asyncio.gather con semáforo
async def ejecutar_workers(workers_listos, grupos_paralelos, execution_profile, verification_profile):
    semaforo = asyncio.Semaphore(10)
    
    for grupo in grupos_paralelos:
        await asyncio.gather(*[ejecutar_worker(w, semaforo) for w in grupo])

async def ejecutar_worker(worker, semaforo):
    async with semaforo:
        if worker.tokens_budget_restante < 100:
            raise TokenLimitError
        
        # Llamada al modelo asignado según execution_profile
        if execution_profile == "code_generation":
            output = await llamar_qwen_o_llama4(worker.input)
        elif execution_profile == "task_execution":
            output = await llamar_gemma4_ejecutar_dsl(worker.input)
        else:  # hybrid
            output = await decidir_por_subtarea(worker.input)
        
        # Validar output contra schema
        jsonschema.validate(output, worker.schema)
        
        # Escribir a eros_memory.tier3_raw_log
        worker.eros_memory.tier3_raw_log.append({...})
```

```yaml
limites_F4:
  semaforo: asyncio_Semaphore(10)_workers_LLM
  timeout: 30s_por_worker_asyncio_wait_for
  token_budget: 32K_por_worker_pre_estimado_en_F2
  max_workers: 100_asyncio

errores_posibles:
  TimeoutError: worker_excedio_30s_a_SIGKILL_+_retry_F8
  TokenLimitError: excedio_32K_a_aborta_subtarea_especifica
  SchemaValidationError: output_no_cumple_schema_a_fail_+_F8
  LLMError: modelo_no_respondio_a_retry_con_backoff

aborto: SI_timeout_token_excedido_error_LLM
checkpoint: state.json["f4"] = {outputs, failed, tokens_total, duration_total}
salida: {outputs_por_worker, failed_workers, tokens_total, status: OK_o_PARTIAL_o_FAILED}
```

### F4 MODE_CODE (Qwen + Llama4)

```yaml
objetivo: generar_codigo_nuevo_arquitectura_de_proyecto_o_refactorizacion

flujo:
  1_Qwen_recibe: requerimiento_+_constraints_+_dsl_codigo_py_template
  2_Qwen_genera: estructura_proyecto_json_esquema_de_archivos
  3_Python_valida: estructura_contra_schema
  4_Llama4_recibe: estructura_+_dsl_codigo_py_+_archivos_a_generar
  5_Llama4_genera: codigo_fuente_+_tests_unitarios
  6_Python_valida:
    - syntax_check_compile()
    - schema_de_salida_jsonschema
    - tests_pasan_pytest_en_sandbox

limites:
  Qwen: 32K_tokens_maximo
  Llama4: 32K_tokens_maximo
  si_estructura_excede_a_F2_ya_aborto_en_pre_estimacion
  si_codigo_excede_a_divide_en_archivos_mas_pequenos_F2_DAG

verificacion_inmediata:
  - syntax_check_Python_compile
  - schema_jsonschema
  - tests_pytest_sandbox_Docker_si_disponible
  - si_falla_a_marca_failed_a_F8_Repair

pct_LLM: 60%_Qwen_+_Llama4_generan
pct_CODIGO: 40%_Python_orquesta_valida
```

### F4 MODE_MULTI (Gemma4 Ejecuta DSL)

```yaml
objetivo: ejecutar_tareas_de_dominio_con_DSL_predefinido
Gemma4_NO_GENERA_codigo_nuevo_NO_TOMA_DECISIONES
Solo_ejecuta_funciones_Python_ya_escritas_en_dsl_lt_dominio_gt_py

flujo:
  1_Gemma4_recibe: datos_+_dsl_lt_dominio_gt_py_+_schema_salida_json
  2_Gemma4_ejecuta_paso_a_paso_las_funciones_del_DSL
  3_cada_paso_produce_output_intermedio
  4_Python_valida_output_contra_schema_despues_de_cada_paso
  5_si_schema_fail_a_retry_mismo_paso_max_3_veces
  6_si_3_fallos_a_marca_failed_a_F8_Repair

dsl_resumen_py_ejemplo:
  paso_1_extraer_titulo(texto)_a_str_a_list  # regex_o_BeautifulSoup_codigo_puro
  paso_2_extraer_fecha(texto)_a_str_a_list  # dateparser_o_regex_codigo_puro
  paso_3_resumir_parrafo(texto_max_palabras)_a_str  # algoritmo_extractivo_codigo_puro

Gemma4_ejecuta_estas_funciones_No_las_inventa
Si_DSL_no_tiene_funcion_necesaria_a_aborta_con_DSL_INCOMPLETO
  a_activa_F5.5_generacion_DSL_puntual

pct_LLM: 30%_Gemma4_ejecuta_no_genera
pct_CODIGO: 70%_Python_orquesta_DSL_funciones
```

### F4 MODE_MIXTO (Híbrido)

```yaml
objetivo: ejecutar_tareas_hibridas_donde_parte_requiere_codigo_nuevo_y_parte_requiere_ejecucion_DSL

flujo:
  1_F1_etiqueto_subtareas: CODE_o_MULTI
  2_F2_construyo_DAG_con_dependencias
  3_F4_ejecuta_por_grupos_paralelos:

  grupo_1_paralelo:
    subtarea_A_CODE: Qwen_genera_estructura_API
    subtarea_B_MULTI: Gemma4_resume_requerimientos

  grupo_2_secuencial_depende_de_grupo_1:
    subtarea_C_CODE: Llama4_escribe_codigo_API_necesita_estructura_de_A
    subtarea_D_MULTI: Gemma4_documenta_endpoints_necesita_codigo_de_C

  4_DAG_decide_paralelismo:
    - sin_aristas_entre_A_y_B_a_asyncio_gather_A_B
    - arista_A_a_C_a_C_espera_A
    - arista_C_a_D_a_D_espera_C

pct_LLM: variable_segun_proporcion_CODE_vs_MULTI
```


## DOC NCT-LOP-100X — Loop Multi-Level + Fusión MiniMax/Kimi K (v100.0.0)

### 6 Niveles de Autonomía (L1-L6)

```yaml
L1_MANUAL:
  horizonte: pasos_discretos
  IA_en_orquestador: 0%
  memoria: volatil
  reparacion: manual
  verificacion: humana
  uso_tipico: micro_tareas_depuracion_fina

L2_SEMI_MANUAL:
  horizonte: minutos
  IA_en_orquestador: 0%
  memoria: opcional
  reparacion: manual_asistida
  verificacion: humana_+_regla
  uso_tipico: scripting_one_shots

L3_SCHEDULED_AUTOMATIC:
  horizonte: horas
  IA_en_orquestador: 0%
  memoria: persistente
  reparacion: reintentos_limitados
  verificacion: regla_+_log
  uso_tipico: cron_ETL_polling

L4_SUPERVISED_AUTONOMOUS:
  horizonte: horas_a_24h
  IA_en_orquestador: 0%
  memoria: persistente
  reparacion: pipeline_5_pasos
  verificacion: adversarial_3_capas
  uso_tipico: features_completas_refactors

L5_CONTINUOUS_AUTONOMOUS_72H_PLUS:
  horizonte: 72h_a_mes
  IA_en_orquestador: 0%
  memoria: jerarquica_EROS_3_tier
  reparacion: rollback_+_fallback_modelo
  verificacion: multicapa_+_drift
  uso_tipico: proyectos_largos_multi_sprint

L6_EVOLUTIONARY_AUTONOMOUS:
  horizonte: indefinido
  IA_en_orquestador: 0%
  memoria: meta_memoria
  reparacion: auto_mejora
  verificacion: autoevaluacion
  uso_tipico: self_improve_self_tune
```

### Mejora 100× — Qué se Multiplica

```yaml
factor_100x:
  1_fase_de_ejecucion_x10: 10_fases_FSM
  1_tipo_de_worker_x10: 12_modelos_de_tarea
  1_nivel_de_autonomia_x6: 6_niveles_1_a_6
  0_loops_anidados_x3: 3_anidaciones_loop_in_loop_in_loop
  1_capa_de_verificacion_x3: 3_capas_adversariales
  0%_trazabilidad_x100: 100%_event_sourcing_+_snapshots
  1_plan_estatico_x5: 5_versiones_avanzadas_de_loop
  0_auto_mejora_x1: nivel_6_evolutivo
  1_modo_de_fallo_x5: pipeline_repair_de_5_pasos
  1_idioma_de_salida_x1: multi_idioma_controlado_por_schema

producto_aproximado: 10_x_10_x_6_x_3_x_3_x_100_x_5_x_1_x_5_x_1_eq_13_500_000
normalizado_a: 100x_para_evitar_sobre_venta
```

### Fusión MiniMax + Kimi K — Conflictos Resueltos

```yaml
aporte_MiniMax:
  dual_classification_intent_plus_tasktype
  team_engine_leader_worker_verifier
  verifier_adversarial_3_layer
  structured_summaries_isolated_context
  coordinator_consolidator_hub

aporte_Kimi_K:
  ok_computer_skills_swarm_routing
  frozen_subagent_spawning
  async_gather_worker_pool
  pad_arousal_pleasure_dominance
  anxiety_circle_detection_l1_l2_l3
  anti_drift_kl_divergence
  eros_3_tier_consolidation
  repair_pipeline_5_steps

nativo_NCT:
  10_phase_fsm
  event_sourcing_state_json
  deterministic_orchestrator_0_percent_ia
  ia_only_phase4_phase6
  6_levels_of_loop_autonomy
  12_task_models_10_plus_steps_each

conflictos_resueltos:
  - "MiniMax_1_agente_grande_vs_Kimi_100_workers_pequeños_a_granularidad_adaptativa_por_router_py"
  - "MiniMax_verifica_al_final_vs_Kimi_verifica_cada_paso_a_verificacion_multicapa_intercalada"
  - "Kimi_cancela_por_ansiedad_SIGKILL_vs_MiniMax_espera_confirmacion_a_escalado_gradual_L1_log_L2_pause_L3_SIGKILL"
  - "EROS_comprime_95%_vs_structured_summaries_aislan_a_EROS_sobre_summaries_doble_compactacion"
  - "Memoria_Kimi_event_sourcing_vs_MiniMax_jerarquica_a_memoria_hibrida_jerarquica_+_journaling"
```

### 12 Task Models (TM01-TM12, ≥10 Pasos Cada Uno)

```yaml
TM01_ARCHITECTURE_DESIGN: 14_pasos  # classify_intent_classify_tasktype_select_blocks_gather_requirements_research_patterns_research_resources_decompose_design_design_data_model_select_stack_validate_consistency_document_adversarial_verify_deliver
TM02_CODE_GENERATION: 14_pasos     # parse_spec_detect_stack_select_blocks_scaffold_gen_models_gen_services_gen_apis_gen_tests_lint_format_static_analysis_security_scan_run_tests_adversarial_review_commit
TM03_RAG_RESEARCH: 14_pasos        # parse_query_expand_select_corpora_embed_retrieve_rerank_chunk_extract_citations_draft_fact_check_dedup_summary_adversarial_verify_deliver
TM04_VALIDATION_QA: 14_pasos       # load_target_oracles_static_lint_static_types_unit_tests_integration_mutation_fuzz_security_sast_dep_audit_adversarial_regression_report_gate
TM05_REPAIR_REFACTOR: 14_pasos     # detect_smell_classify_propose_branch_apply_keep_behavior_verify_update_docs_commit_pr_review_merge_or_revert_learn_deliver
TM06_TEST_SUITE: 14_pasos          # parse_module_enumerate_paths_prioritize_gen_unit_gen_edge_gen_property_gen_contract_gen_integration_gen_e2e_gen_perf_run_parallel_flaky_coverage_report
TM07_DEPLOY_RELEASE: 14_pasos      # select_artifact_verify_sig_sbom_policy_stage_deploy_smoke_load_chaos_metrics_canary_5_canary_25_canary_100_tag_notify
TM08_DOCUMENTATION: 14_pasos       # parse_audience_select_template_outline_draft_sections_code_examples_diagrams_glossary_cross_links_readability_translation_es_translation_en_review_publish_feedback
TM09_DATA_PIPELINE: 14_pasos       # parse_source_parse_sink_contract_diff_select_tool_extract_validate_schema_transform_dedup_enrich_quality_load_lineage_publish_observe_metrics_sla_check
TM10_SECURITY_AUDIT: 14_pasos      # parse_target_enumerate_assets_sast_secret_sca_license_container_infra_dast_threat_model_prioritize_cves_remediation_adversarial_redteam_deliver
TM11_LONG_HORIZON_72H_PLUS: ...
TM12_EVOLUTIONARY_SELF_IMPROVEMENT: ...
```

### 5 Advanced Loop Versions (ALV)

```yaml
ALV_LOP_GENESIS_BASELINE
ALV_LOP_TITANIUM_PARALLEL_GRAPH
ALV_LOP_QUANTUM_FRACTAL_NESTED
ALV_LOP_SINGULARITY_EVOLUTIONARY
ALV_LOP_NEXUS_FUSION_FULL
```

### Contrato JSON Canónico por Nivel

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


### TM11 — Long Horizon 72H+

```yaml
1_global_goal: meta_de_alto_nivel  # usuario
2_strategic_plan: horizonte_72h  # planner
3_milestones: checkpoints  # planner
4_resource_alloc: agentes_+_modelos  # router
5_parallel_execute: N_workers  # worker_pool
6_pad_monitor: arousal_pleasure_dominance  # monitor
7_anxiety_monitor: L1_L2_L3  # monitor
8_drift_monitor: KL_plan_actual  # monitor
9_checkpoint_save: cada_30_min  # state
10_auto_repair: 5_pasos  # repair
11_eros_consolidate: 3_tier  # consolidator
12_replan_if_drift: ajustar_plan  # planner
13_report_progress: pulse_cada_hora  # deliver
14_finalize: cierre  # deliver
```

### TM12 — Evolutionary Self-Improvement

```yaml
1_collect_metrics: KPIs_del_propio_NCT  # Telemetry
2_mine_failures: repair_logs  # SelfTuner
3_cluster_failures: embeddings  # SelfTuner
4_propose_patches: prompts_+_planes  # SelfTuner
5_sandbox_apply: branch_efimero  # Ejecutor
6_benchmark: suite_canonica  # Test
7_compare_metrics: antes_despues  # Validador
8_promote_or_revert: decision  # router
9_update_skill_library: nuevo_SKILL_md  # SelfTuner
10_update_resource_db: resources_yaml  # SelfTuner
11_update_router_weights: refuerzo  # router
12_meta_verify: 3_capas  # Verifier
13_release_meta_version: tag_semver  # deliver
14_restart_cycle: encolar_siguiente  # SelfTuner
```

### 12 Propuestas (PROP-01 a PROP-12) — Detalles Técnicos

```yaml
PROP-01_Orquestador_FSM_100_determinista:
  fase_objetivo: P0_a_P9_todas
  descripcion: FSM_como_tabla_de_transiciones_inmutable_cargada_desde_nct_config_yaml
  contratos:
    input: {state, event, guard}
    output: {state, side_effects}
  KPIs: transiciones_por_segundo_guard_failures_auditability_eq_1.0
  riesgo: sobre_restriccion_a_mitigacion_level_le_L4

PROP-02_WorkerPool_asincrono_con_gather_y_semaphore:
  fase_objetivo: P4
  descripcion: asyncio_gather_con_semaforo_K_eq_10_configurable
  contratos: "async def run_workers(jobs: list[Job], k: int) -> list[Result]"
  KPIs: throughput_jobs_por_min_p99_latency_context_isolation_violations_eq_0

PROP-03_Monitor_triple_PAD_Ansiedad_Drift:
  fase_objetivo: P5
  3_modulos_concurrentes:
    PAD: arousal_pleasure_dominance_por_worker
    Ansiedad: detecta_bucles_mismo_prompt_3x_a_L1_5x_a_L2_8x_a_L3_a_SIGKILL
    Anti_drift: KL_plan_actual_gt_0.02_a_rollback
  KPIs: false_positive_rate_mean_time_to_detect

PROP-04_Verifier_adversarial_3_capas:
  fase_objetivo: P6
  3_capas:
    Capa_1: adversarial_busca_errores_intencionales
    Capa_2: cruzada_manda_output_de_A_a_verificador_B_y_viceversa
    Capa_3: maker_checker_con_contrato_JSON_Schema
  KPIs: detection_rate_false_accept_rate_latency_p99

PROP-05_EROS_3_tier_consolidation:
  fase_objetivo: P7
  flujo: Tier_3_crudo_100%_a_Tier_2_pulses_20%_a_Tier_1_le_5%_JSON
  KPIs: compression_ratio_information_loss_reconstrunction_f1

PROP-06_Repair_Pipeline_5_pasos:
  fase_objetivo: P8
  flujo: fail_a_retry_3_a_compress_L1_o_L2_a_fallback_model_a_restore_checkpoint_a_escalate
  KPIs: recovery_rate_time_to_recover_escalation_rate

PROP-07_Memoria_hibrida_jerarquica_journaling:
  fase_objetivo: transversal
  flujo: journaling_event_sourcing_mas_memoria_jerarquica_EROS_3_tier
  KPIs: durability_replay_throughput_storage_growth_por_cycle

PROP-08_Router_adaptativo_multi_senal:
  fase_objetivo: P1
  senales: intencion_tipo_nivel_presupuesto_historico
  salida: terna_modo_ruta_agentes
  KPIs: routing_accuracy_mode_match_score_budget_overrun_rate

PROP-09_SelfTuner_evolutivo_L6:
  fase_objetivo: P9_+_L6
  flujo: P9_a_metrics_a_cluster_failures_a_propose_patch_a_sandbox_a_benchmark_a_promote_o_revert
  KPIs: mean_quality_gain_por_cycle_revert_rate

PROP-10_DSL_declarativo_para_Task_Models:
  fase_objetivo: transversal
  esquema: TM_id_level_steps_contracts_kpis
  KPIs: schema_violations_eq_0_parse_throughput

PROP-11_Circuit_breaker_backoff_exponencial:
  fase_objetivo: transversal
  flujo: ok_a_closed_fail_x_N_a_open_a_half_open_a_closed_backoff_eq_base_x_2_a_attempts
  KPIs: mttr_false_open_rate_request_loss

PROP-12_Observabilidad_OpenTelemetry:
  fase_objetivo: transversal
  flujo: traces_metrics_logs_a_OTLP_a_collector
  KPIs: trace_completeness_cardinality_budget_SLO_compliance
```

### Flujo Global con las 12 Propuestas Integradas

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
                       [PROP-07 memoria]                   │
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


## DOC NCT-LOP-200X — ADDENDUM: MiMo Code + Open-Source Agents + HF Spaces + Micro-Agents (v200.0.0)

### MiMo Code — Datos Clave

```yaml
origen: Xiaomi_MiMo_Team
base_project: OpenCode
license: MIT
first_release: 2026-06-11_V0.1.0
tech_stack: [Bun, TypeScript, Effect, SolidJS, Tauri]

3_pilares_arquitectonicos:
  compute: [Max_Mode, Goal-Stop, Dynamic_Workflow]
  memory: [Checkpoint_o_Rebuild, Writer_subagent, 4_tier_memory]
  evolution: [Dream, Distill, project_memory]

benchmarks_vs_Claude_Code:
  SWE-Bench_Pro_V2: +5%
  Terminal_Bench_2: +5%
  ultra_long_200_plus_steps: beats_Claude_Code

modelos_compatibles: [MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM]
```

### 7 Loops Internos de MiMo Code

```yaml
decision_loop: cada_turno  # tool_call_o_respuesta  # persistencia_solo_conversacion
checkpoint_loop: cada_N_turnos_configurable  # snapshot_firmado  # state_jsonl
writer_loop: cuando_contexto_gt_70%  # resumen_estructurado  # memory_tier-N_md
max_mode_loop: en_decisiones_criticas  # K_muestras_a_voto  # efermero
dream_loop: cada_7_dias  # memoria_consolidada  # memory_dream_md
repair_loop: en_error  # plan_de_recuperacion  # state_jsonl
evolution_loop: al_cierre_de_sesion  # skill_o_proc_o_prompt_nuevo  # skills_
```

### Adaptaciones MiMo → NCT (regla: nada copiar literal)

```yaml
Max_Mode: worker_pool_py_con_k_samples_por_decision_critica
Goal-Stop: nueva_fase_P9.5_goal-check_antes_de_deliver
Dynamic_Workflow: ALV_LOP_QUANTUM_FRACTAL_NESTED_ya_propuesto_en_v100
Checkpoint_o_Rebuild: state_o_engine_py_con_replay_to_checkpoint_t
Writer_subagent: nuevo_MA-RAG-SYNTH
4_tier_memory: extender_EROS_3_tier_a_4_tiers_tier0_raw_tier1_session_tier2_strategic_tier3_project
Dream: nuevo_job_cron_weekly_a_MA-DREAM
Distill: nuevo_job_cron_daily_a_MA-DISTILL
project_memory: state_o_project_memory_sqlite
```

### Catálogo Open-Source Clones (15 Backends)

```yaml
tier_s_plus:
  - OpenCode 154.5K_stars_TypeScript_75+_LLMs_MCP-first
  - Gemini_CLI 103.1K_stars_TypeScript_Gemini_free
  - OpenHands 72.6K_stars_Python_varios
  - Open_Interpreter 63.4K_stars_Python_local
  - Aider 44.3K_stars_Python_100+_LLMs
  - Goose 43.7K_stars_Rust_varios_MCP-first

tier_a:
  - Qwen_Code 24.1K_stars_TypeScript_Qwen3-Coder_MCP-first
  - Crush 23.8K_stars_Go_varios_MCP-first
  - Kimi_CLI 8.4K_stars_Python_Kimi_K2
  - Forge_Code 7.2K_stars_Rust_300+_modelos
  - MiMo_Code_TypeScript_MiMo-V2.5_+_otros

tier_b:
  - BLXCode  # MCP-first
  - Open_Design  # 16_CLIs_integrados_router
  - OpenClaw  # OpenRouter_+_MiMo-V2
  - KiloCode  # Kilo_Gateway_MCP-first
  - Cline  # 100+_modelos_MCP-first

lenguajes: [TypeScript, Python, Rust, Go]
```

### Regla Selección Router

```yaml
router:
  signals: [cost, latency, capability, license, mcp_native]
  rules:
    - if_task_type_eq_code_generation_and_budget_eq_low:
        backend: opencode_model_deepseek-coder
    - if_task_type_eq_long_horizon_and_horizon_h_ge_24:
        backend: mimo_code_model_mimo-v2.5
    - if_task_type_eq_research_rag:
        backend: openhands_model_qwen3-coder
    - if_task_type_eq_ui_design:
        backend: open_design_model_sonnet-4.6
    - default:
        backend: goose_model_claude-sonnet-4.6
```

### Contrato Común de Invocación

```yaml
backend_invocation:
  transport: [stdio, http, mcp]
  input_schema: nct.task.v1.json
  output_schema: nct.result.v1.json
  timeout_s: 600
  cancel_token: true
  auth:
    type: byok_or_proxy
    proxy_url: http://nct-proxy/api/proxy/{provider}/stream
```

### 12 Micro-Agentes Especializados (MA-)

```yaml
MA-CODE-GEN: code_generator_a_desde_spec  # input_spec_md_stack_json_a_code_zip_+_diff_patch_a_5_a_30s
MA-CODE-LINT: linter_a_lint_+_format_+_type_check  # input_code_zip_a_report_json_a_2_a_10s
MA-CODE-TEST: tester_a_unit_+_integration_+_mutation  # input_code_zip_tests_a_junit_xml_+_coverage_json_a_10_a_60s
MA-RAG-SEARCH: web_o_gh_search_a_busqueda_vectorial_+_rerank  # input_query_k_a_chunks_json_con_citas_a_3_a_15s
MA-RAG-SYNTH: synthesizer_a_sintetiza_respuesta_con_citas  # input_chunks_json_a_answer_md_a_5_a_20s
MA-DOC-WRITE: doc_writer_a_documenta_arquitectura_o_decisiones  # input_artifacts_audience_a_doc_md_a_5_a_15s
MA-ARCH-PLAN: architect_planner_a_planifica_arquitectura_y_stack  # input_requirements_json_a_arch_yaml_a_5_a_30s
MA-VERIFY-3CAPAS: verifier_a_verificacion_adversarial_3_capas  # input_artifact_rubric_a_verdict_json_a_10_a_60s
MA-REPAIR-5STEP: repairer_a_pipeline_5_pasos_de_reparacion  # input_failure_json_a_repaired_json_o_escalate_a_30_a_120s
MA-RESEARCH-WEB: web_researcher_a_crawling_+_extraccion  # input_urls_depth_a_pages_jsonl_a_30_a_300s
MA-RESEARCH-GH: github_researcher_a_busqueda_en_github_via_api  # input_query_lang_stars_min_a_repos_json_a_10_a_60s
MA-EMIT-REPORT: report_emitter_a_empaqueta_resultado_final  # input_state_json_a_report_md_+_manifest_json_a_1_a_5s

diseno_regla: single_responsibility_le_200_LOC_core_single_output_schema
execution_model: spawn_a_run_a_emit_JSON_a_die
```

### Ejemplo MA-VERIFY-3CAPAS (90% código / 10% LLM)

```python
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

### 3 Patrones de Encadenamiento

```yaml
a_secuencial:
  patron: A_a_B_a_C_a_D
  config: chain_linear
  caso_ETL_refactor

b_DAG_paralelo:
  patron: A_a_B_y_A_a_C_en_paralelo_a_D
  config: chain_dag_con_parallel_groups
  caso_investigacion_+_diseno

c_fractal_anidado:
  patron: A_a_B_y_A_a_C_en_paralelo_a_D_anidado
  config: chain_fractal_con_depth_le_5
  caso_arquitectura_multi_modulo
```

### Ejemplo Cadena Completa E-commerce Microservice

```yaml
chain:
  id: ecommerce_microservice_v1
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget:
    max_tokens: 2000000
    max_runtime_h: 24
  steps:
    - {id: MA-ARCH-PLAN, parallel_group: g1}
    - {id: MA-RESEARCH-WEB, parallel_group: g1, input_from: ctx.arch.questions}
    - {id: MA-RESEARCH-GH, parallel_group: g1, input_from: ctx.arch.stack}
    - {id: MA-RAG-SYNTH, parallel_group: g2, input_from: [ctx.web, ctx.repos]}
    - {id: MA-CODE-GEN, parallel_group: g3, input_from: ctx.arch}
    - {id: MA-CODE-LINT, parallel_group: g4, input_from: ctx.code}
    - {id: MA-CODE-TEST, parallel_group: g4, input_from: ctx.code}
    - {id: MA-VERIFY-3CAPAS, parallel_group: g5, input_from: [ctx.code, ctx.tests]}
```


### Pipeline Pre-Análisis Semilla (5 Pasos)

```yaml
S1_indexar: indexar_repo_+_state_+_RAG  # MA-INDEX_a_seed_index_sqlite
S2_resumir: resumir_cada_artefacto  # MA-SUMMARIZE_a_seed_summary_json
S3_detectar_gaps: detectar_huecos_de_informacion  # MA-GAP-DETECT_a_seed_gaps_json
S4_proponer_preguntas: proponer_preguntas_de_investigacion  # MA-QUESTION-GEN_a_seed_questions_json
S5_enriquecer: enriquecer_seed_con_respuestas_iniciales  # MA-RESEARCH-WEB_+_MA-RESEARCH-GH_a_seed_enriched_json
```

### Métrica Suficiencia Evidencia

```python
evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
)

if score >= 0.85: proceed_sin_mas_investigacion
else: entrar_ciclo_investigacion_seccion_6
```

### Ciclo de Investigación (5 Pasos R1-R5)

```yaml
R1_query: query
R2_fetch: fetch
R3_filter: filter
R4_eval: eval  # si_score_lt_0.85_replan
R5_refine: refine  # new_query_o_stop_si_score_ge_0.85

politica:
  minimo_2_rondas: por_tarea
  maximo_5_rondas: anti_bucle
  cada_ronda_consume_le_50K_tokens
  salida_consolidada: MA-RAG-SYNTH

fuentes_prioritarias:
  web: [Wikipedia, OWASP, MDN, arXiv, blogs_oficiales, documentacion_oficial_stacks]
  github: [MiMo_Code, OpenCode, awesome_lists, issues_PRs_discussions, releases_changelogs]
```

### Flota HuggingFace Spaces (10-20 Workers)

```yaml
1_evalstate_FLUX.1_schnell: generacion_imagenes_T4_5_a_15s
2_hf_audio_whisper_large_v3_turbo: STT_T4_1_a_5s
3_microsoft_OmniParser: vision_o_parsing_UI_A10G_2_a_8s
4_Qwen2_VL_72B_smolagents_E2B: VLM_reasoning_A100_5_a_20s
5_gradio_llm_router: LLM_generico_T4_2_a_10s
6_nct_rag_search: busqueda_vectorial_CPU_1_a_3s
7_nct_code_runner: ejecucion_de_codigo_CPU_1_a_5s
8_nct_lint_fmt: lint_+_format_CPU_0.5_a_2s
9_nct_test_runner: test_+_coverage_CPU_5_a_30s
10_nct_security_scan: sast_+_secrets_CPU_10_a_60s
11_nct_dream: consolidacion_memoria_CPU_60_a_300s
12_nct_distill: destilacion_memoria_CPU_60_a_300s
13_a_20: reservados_para_picos_failover_mixto_variable

seleccion_router:
  select_worker(capability, sla_ms):
    alive = [c for c in candidates if c.health_eq_ok]
    feasible = [c for c in alive if c.p95_ms_le_sla_ms]
    return min(feasible, key=c.cost)

resiliencia:
  circuit_breaker: por_Space_umbral_3_fallos_consecutivos
  backoff_exponencial: base_2s_max_5_min
  failover: al_siguiente_Space_disponible_de_misma_capability
  degradacion_elegante: si_todos_caen_a_paso_se_marca_como_skipped_y_cadena_continua
```

### DSL Determinista (90% Código / 10% LLM)

```yaml
regla_presupuesto:
  90%_codigo_determinista:
    - parseo_validacion_transformacion_routing
    - verificacion_mecanica_formatting
    - retry_fallback_circuit_breaker
    - EROS_compression_checkpoint_o_restore_schema_validation
  10%_LLM_solo_en:
    - MA-RAG-SYNTH
    - MA-ARCH-PLAN_parte_creativa
    - Max_Mode_en_decisiones_criticas
    - llm_adversarial_review_cuando_3_capas_mecanicas_fallan
```

```yaml
# dsl/step.yaml
step:
  id: MA-VERIFY-3CAPAS
  type: deterministic_with_llm_fallback
  budget:
    code_pct: 90
    llm_pct: 10
    max_tokens: 50000
  inputs: {artifact: object, rubric: object}
  outputs: {decision: enum, issues: array}
  code_steps:
    - parse_artifact
    - schema_validate
    - cap1_adversarial
    - cap2_cruzada
    - cap3_maker_checker
  llm_steps:
    - when: any(cap.issues)
      call: llm_adversarial_review
      max_tokens: 4000
      temperature: 0.0
```

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


### 8 Nuevas Propuestas (PROP-13 a PROP-20)

```yaml
PROP-13_micro_agents_catalog: 12_micro_agentes_especializados
  inputs: {task, k_concurrency}
  outputs: {results, audit}
  invariants: [single_responsibility_true, max_loc_core_200, schema_io_unico_true]
  kpis: [p99_latency_ms, success_rate, cost_per_call]

PROP-14_chain_patterns: 3_patrones_secuencial_DAG_fractal
  inputs: {tasks}
  outputs: {execution_plan}
  invariants: [acyclic_dag_true, max_depth_5]

PROP-15_seed_pre_analysis: 5_pasos_de_pre_analisis
  inputs: {repo, state, rag}
  outputs: {seed_index_sqlite, gaps, questions}
  invariants: [reproducible_true]

PROP-16_research_cycle: 2_a_5_rondas_stop_por_evidencia
  inputs: {question, sources}
  outputs: {synthesized, score}
  invariants: [min_rounds_2, max_rounds_5, early_stop_threshold_0.85]

PROP-17_hf_spaces_fleet: 10_a_20_workers_remotos_MCP
  inputs: {capability, sla_ms}
  outputs: {worker_id, fallback_chain}
  invariants: [min_workers_10, max_workers_20, circuit_breaker_true]

PROP-18_dsl_90_10_budget: 90%_codigo_/_10%_LLM
  inputs: {pipeline}
  outputs: {budget_report}
  invariants: [llm_pct_le_10_true]
  kpis: [llm_pct, cost_per_cycle]

PROP-19_mimo_integration: componentes_de_MiMo_Max_Mode_Goal-Stop_Writer_Dream_Distill_Checkpoint
  inputs: {mimo_feature}
  outputs: {enabled, config}

PROP-20_oss_backends_router: router_entre_15_backends_OSS
  inputs: {task}
  outputs: {backend, model, transport}
  invariants: [byok_or_proxy_true, mcp_first_preferred_true]
```

### Integración con Documento Padre v100

```yaml
seccion_v100_a_complemento_v200:
  0_indice: nuevo_bloque_JSON_con_scope_additions
  1_niveles: level_L5_o_L6_ahora_pueden_usar_HF_Spaces
  2_fusion_MiniMax_Kimi_K: se_añade_MiMo_Code_como_tercer_polo
  3_task_models: cada_TM_puede_invocar_micro_agentes
  4_ALV_loops: el_QUANTUM_FRACTAL_usa_la_cadena_de_micro_agentes
  5_propuestas: nuevas_propuestas_PROP_13_a_PROP_20
  6_diagramas: diagrama_adicional_de_la_flotta_HF
  7_contratos_YAML: contratos_extendidos_para_micro_agentes
  9_entrega: nuevo_subpaquete_lop_v200
```

### Árbol de Entrega Actualizado

```yaml
nct_coordinator/:
  lop_v100/  # documento_padre_ya_entregado
    __init__.py
    levels.py
    alvs.py
    task_models/...
    proposals/PROP-01..12.yaml
    schemas/...

  lop_v200/  # NUEVO_este_addendum
    __init__.py
    micro_agents/  # 12_micro_agentes
      ma_code_gen_py
      ma_code_lint_py
      ma_code_test_py
      ma_rag_search_py
      ma_rag_synth_py
      ma_doc_write_py
      ma_arch_plan_py
      ma_verify_3capas_py
      ma_repair_5step_py
      ma_research_web_py
      ma_research_gh_py
      ma_emit_report_py
    pipelines/  # DSL_declarativos
      p_ma_chain_yaml
      ecommerce_microservice_yaml
      saas_tasks_api_v1_yaml
    backends/  # routers_a_OSS_clones
      opencode_adapter_py
      goose_adapter_py
      qwen_code_adapter_py
      mimo_code_adapter_py
      forge_code_adapter_py
    hf_spaces/  # cliente_de_la_flotta_HF
      fleet_client_py
      circuit_breaker_py
      selector_py
    dsl/
      step_yaml
      pipeline_yaml
      budget_py
    seed/
      pre_analysis_py
      gap_detector_py
    research/
      cycle_py
      web_gh_sources_yaml
    proposals/PROP-13..20.yaml
    schemas/
      micro-agent.schema.json
      pipeline.schema.json
      hf-fleet.schema.json
```


## DOC MASTER 16 (80ce5f95): MiMoCode / Lop v200 / Investigación

### MiMo Code Resumen (Master 16)

```yaml
tipo: agente_de_programacion_para_terminal
license: MIT
origen: Xiaomi_MiMo_Team
base_project: OpenCode
horizonte: decenas_a_200+_pasos_continuos

3_pilares:
  compute: [Max_Mode, Goal-Stop, Dynamic_Workflow]
  memory: [Checkpoint_o_Rebuild, Writer_subagent, 4_tier_memory]
  evolution: [Dream, Distill, project_memory]

stack: [Bun, TypeScript, Effect, SolidJS_TUI, Tauri_desktop]

benchmarks_vs_Claude_Code:
  SWE-Bench_Pro_V2: +5%
  Terminal_Bench_2: +5%
  ultra_long_200_plus_steps: beats_Claude_Code

modelos_compatibles: [MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM]
```

### 7 Loops Internos MiMo (Repetidos como referencia)

```yaml
decision_loop: cada_turno
checkpoint_loop: cada_N_turnos
writer_loop: cuando_contexto_gt_70%
max_mode_loop: en_decisiones_criticas
dream_loop: cada_7_dias
repair_loop: en_error
evolution_loop: al_cierre_de_sesion
```

### Tabla Maestra de Proyectos Open-Source

```yaml
OpenCode: 154.5K_TypeScript_75+_LLMs_MCP-first
Gemini_CLI: 103.1K_TypeScript_Gemini_free_parcial_MCP
OpenHands: 72.6K_Python_varios_parcial_MCP
Open_Interpreter: 63.4K_Python_local_no_MCP
Aider: 44.3K_Python_100+_LLMs_parcial_MCP
Goose: 43.7K_Rust_varios_MCP-first
Qwen_Code: 24.1K_TypeScript_Qwen3-Coder_MCP-first
Crush: 23.8K_Go_varios_MCP-first
Kimi_CLI: 8.4K_Python_Kimi_K2_parcial_MCP
Forge_Code: 7.2K_Rust_300+_modelos_parcial_MCP
MiMo_Code: TypeScript_MiMo-V2.5_+_otros_parcial_MCP
Open_Design: 16_CLIs_integrados_MCP-first
OpenClaw: OpenRouter_+_MiMo-V2_parcial_MCP
KiloCode: TypeScript_Kilo_Gateway_MCP-first
Cline: TypeScript_100+_modelos_MCP-first

lenguajes: [TypeScript, Python, Rust, Go]
MCP-first: [Goose, Open_Design, BLXCode]
```


## DOC MASTER 16 (01657536): DSL + UNIVERSAL PLUG v1.5

### DSL — Domain Specific Language

```yaml
que_es: lenguaje_estructurado_que_usa_NCT_para_definir_tareas_workflows_pipelines_y_configuraciones
nunca_es_prompt_libre

reglas:
  estructura_cerrada_no_free_form
  validado_contra_schema
  parseable_deterministicamente
  versionado_semver
  schema_first

tipos_DSL:
  DSL_Task: definir_tarea_task_v1_json
  DSL_Pipeline: definir_pipeline_pipeline_v1_json
  DSL_Agent: definir_agente_agent_v1_json
  DSL_Skill: definir_skill_skill_v1_json
  DSL_Project: definir_proyecto_project_v1_json
  DSL_Workflow: definir_workflow_workflow_v1_json
  DSL_DAG: definir_DAG_dag_v1_json
```

### DSL TASK (Ejemplo)

```yaml
task:
  id: task-2026-06-28-001
  type: simple
  level: L2_SUPERVISED
  input:
    source: telegram
    raw: "crear API REST para tareas"
  goals:
    primary: "API funcional"
    secondary: "Con tests"
    success: "Tests pasan + API responde"
    failure: "Tests fallan o API no responde"
    restriction: "No usar frameworks pesados"
  steps:
    - {id: s1, action: parse_input}
    - {id: s2, action: validate_schema}
    - {id: s3, action: generate_plan}
    - {id: s4, action: execute}
    - {id: s5, action: validate}
    - {id: s6, action: deliver}
  budget: {max_tokens: 100000, max_runtime_s: 600}
```

### DSL DAG Validación

```yaml
dag:
  id: dag-001
  nodes: [{id: A, type: task, agent: MA-01}, ...]
  edges: [{from: A, to: B}, ...]
  groups: [{id: g1, nodes: [A, B], parallel: true}]

validacion:
  no_ciclos
  topological_sort_valido
  cada_nodo_tiene_agente
  cada_edge_tiene_origen_y_destino_validos
```

### Universal Module Contract JSON Schema v1.5

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MAXBRY Module Contract",
  "version": "1.5",
  "type": "object",
  "required": ["module_id", "version", "interface"],
  "properties": {
    "module_id": {"type": "string", "pattern": "^[a-z][a-z0-9_]*$"},
    "version": {"type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$"},
    "interface": {
      "type": "object",
      "required": ["inputs", "outputs"],
      "properties": {
        "inputs": {"type": "array"},
        "outputs": {"type": "array"}
      }
    },
    "dependencies": {"type": "array", "items": {"type": "string"}},
    "capabilities": {"type": "array"},
    "limits": {"type": "object"},
    "metadata": {"type": "object"}
  }
}

campos_obligatorios: [module_id, version, interface_inputs, interface_outputs]
campos_opcionales: [dependencies, capabilities, limits, metadata, tags, author]

validacion:
  schema_valido_contra_Draft_07
  module_id_unico
  version_semver
  interface_tipado
  dependencies_resolubles
```

### Sistema Validación Cruzada DSL DAG

```yaml
cross_validation:
  node: MASTER-XX
  references_to: [MASTER-YY, MASTER-ZZ]
  referenced_by: [MASTER-WW]
  consistency_check:
    no_contradictions: true
    terms_aligned: true
    versions_match: true
    schema_compatible: true

garantias:
  cada_documento_referencia_al_menos_2_docs_mas
  referencias_son_validas
  no_hay_contradicciones_entre_docs
  dependencias_son_resolubles

ejecucion:
  def cross_validate(doc_a, doc_b):
    if contradiction(doc_a, doc_b): return {valid: False, reason: contradiction}
    if not terms_aligned(doc_a, doc_b): return {valid: False, reason: term_misalignment}
    if not versions_match(doc_a, doc_b): return {valid: False, reason: version_mismatch}
    return {valid: True}
```


## DOC MASTER 26 (0386e27d): NOMBRES ESPECÍFICOS + ARCHIVOS + ESQUEMAS

### 8 Schemas Aprobados

```yaml
TASK_json: define_una_tarea_individual
TASK_HISTORY_json: historial_de_cambios_de_una_tarea
STATE_json: estado_global_del_sistema
BLACKBOARD_json: memoria_compartida_entre_agentes
INBOX_json: entrada_de_mensajes
OUTBOX_json: salida_de_mensajes
EVENTS_json: log_de_eventos
PROJECT_ROOT_por_proyecto: root_de_cada_proyecto
```

### 12 Estados y Listas de Trabajo

```yaml
INBOX_json: recibe_entrada
OUTBOX_json: entrega_salida
STATE_json: estado_actual
HISTORY_json: acumulativo_NUNCA_se_borra
TASKS_json: lista_de_tareas
lista_tareas_pendientes_json: cola_FIFO
lista_tareas_en_curso_json: en_ejecucion
lista_tareas_completadas_json: terminadas_OK
lista_tareas_fallidas_json: con_error
BLACKBOARD_json: memoria_compartida
REPORT_FOR_M3_md: reporte_a_M3
TELEGRAM_LOG_txt: log_de_Telegram
```

### 8 Archivos del Coordinador NCT + 5 Soporte

```yaml
8_principales:
  fsm_py: orquestador_10_fases
  classifier_py: clasificacion_dual
  router_py: modo_o_ruta
  planner_py: descomposicion
  context_isolator_py: contexto_aislado
  worker_pool_py: workers_UNICA_CON_IA
  monitor_py: PAD_+_Ansiedad_+_Drift
  verifier_py: 3_capas

5_soporte:
  consolidator_py: consolida_resultados
  repair_py: repair_pipeline_5_pasos
  deliver_py: multi_target_delivery
  state_o_engine_py: engine_de_estado
  state_o_telemetry_py: telemetria
```

### G6 Staff — 5 Agentes Principales (Versión Específica)

```yaml
MiniMax_M3: 
  via: NVIDIA_NIM
  rol: lider_del_G5_SKYNER_arquitecto

MiMo_Code:
  ubicacion: HF_aparte
  rol: code_agent_paralelo_tareas_horizonte_largo

OpenCLAW:
  rol: agente_adicional_multi_canal_308k_stars_GitHub

Smolagents:
  rol: agente_adicional_tareas_generales_HuggingFace

Hermes_Agent:
  rol: archivist_+_memoria_149k_stars_GitHub_learning_loop_L1+L2+L3

Code_Agent_CLI_Aider_o_Cline:
  rol: code_generation_local_fallback_para_MiMo
```

### 3 Monitores con Umbrales Específicos

```yaml
PAD_Monitor:
  Pleasure_Arousal_Dominance
  umbral: Arousal_gt_0.8_AND_Pleasure_lt_0.2_a_SIGKILL_+_Respawn

Ansiedad_Monitor:
  3_niveles:
    bajo: confirma
    medio: confirma_+_alerta
    alto: respawn

Anti_Drift_Monitor:
  umbral: KL_divergence_gt_0.02_a_halt_+_rollback
  comparacion: contra_baseline
```

### 14 Parches Operacionales

```yaml
14.1_CIRCUIT_BREAKER:
  estados: CLOSED_o_OPEN_o_HALF_OPEN
  failure_threshold: 5_fallos_en_60s
  recovery_timeout: 30s
  libreria: pybreaker
  por_servicio: NVIDIA_NIM_Cerebras_Groq_HF_local

14.2_FREE_TIER_cost_target_$0:
  HF_Spaces_CPU_Basic: 16GB_RAM
  APIs: NVIDIA_NIM_free_Cerebras_free_Groq_free
  tecnicas: cache_fallback_batch_monitor_circuit_breaker_por_costo

14.3_TELEGRAM_1_bot_multi_topic:
  topics: [#nct-fase0, #interfaz-fusionada, #crazy-wall, #consenso, #consensus-log]

14.4_CHROMADB_vector_DB_principal:
  coleccion: nct_memory
  metric: cosine
  index: hnsw
  persistencia: disco

14.5_BGE_SMALL_EN_V1_5_embedding:
  HF: BAAI_o_bge-small-en-v1.5
  dim: 384
  size: 24MB
  alt: all-MiniLM-L6-v2

14.6_EMBEDDING_proceso:
  cada_documento_nuevo_a_bge-small_a_384-dim_a_ChromaDB
  retrieval_top_k_por_similitud_cosine
```

### 16 Mejores Prácticas EROSTAS + 4 Adicionales = 20

```yaml
originales_16:
  1_cache_de_inferencia
  2_fallback_entre_modelos
  3_checkpoint_por_commit
  4_retry_automatico_2x
  5_rollback_atomico
  6_auditoria_paralela
  7_preview_antes_de_commit
  8_notificacion_solo_cuando_hay_cambios
  9_cola_con_prioridad_urgente
  10_timeout_por_tipo
  11_workers_paralelos_5_hilos
  12_sandbox_pre_commit
  13_rollback_atomico_refuerzo
  14_trazabilidad_total
  15_metrics
  16_alertas_por_desviacion

adicionales_4:
  17_auto_optimizacion_del_loop
  18_aprendizaje_de_errores
  19_dashboard_visual
  20_export_reportes
```

