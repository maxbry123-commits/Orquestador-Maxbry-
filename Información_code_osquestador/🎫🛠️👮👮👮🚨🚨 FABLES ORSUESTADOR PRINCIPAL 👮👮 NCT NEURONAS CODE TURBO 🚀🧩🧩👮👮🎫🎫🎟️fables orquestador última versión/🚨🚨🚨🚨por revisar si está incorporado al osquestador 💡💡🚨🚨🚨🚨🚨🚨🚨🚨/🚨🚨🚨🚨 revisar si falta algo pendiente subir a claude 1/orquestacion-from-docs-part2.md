# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 2)

> **Continuación del Parte 1** (`orquestacion-from-docs-part1*.md`).
> 
> Esta es la extracción **literal** (no inventada) de toda la información relacionada con el **ORQUESTADOR** encontrada en los 57 documentos fuente en `/workspace/attachments/`. Formato AI-friendly (YAML/DSL/código + diagramas horizontales).
>
> **Reglas aplicadas**:
> - Solo contenido citado literalmente de los documentos fuente.
> - Separación estricta: orquestador ≠ agentes.
> - Sin repetir información entre partes.
> - Cada diagrama es horizontal y compacto.

# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 2)

> **Continuación del Parte 1** (`orquestacion-from-docs-part1.md`).
> 
> Esta es la extracción **literal** (no inventada) de toda la información relacionada con el **ORQUESTADOR** encontrada en los 57 documentos fuente en `/workspace/attachments/`. Formato AI-friendly (YAML/DSL/código + diagramas horizontales).
>
> **Reglas aplicadas**:
> - Solo contenido citado literalmente de los documentos fuente.
> - Separación estricta: orquestador ≠ agentes.
> - Sin repetir información entre partes.
> - Cada diagrama es horizontal y compacto.


## DOC BLOQUE_4_F7_F8_F9_CONSOLIDACION_REPAIR_ENTREGA: Verificación Cruzada

### Diagrama F7 → F8 → F9 (Transversal)

```
F6 ─► [F7 consolidador EROS 3-Tier] ─► [F8 repair 5-pasos métricas-duras] ─► [F9 deliver empaquetado+reporte] ─► USR
       │                                  │                                       │
    certified_outputs                  rejected_outputs                       empaquetado
    eros_memory per worker             failed_workers                         reporte_automático
    schemas                            metricas_flags                         state_final_FINAL
```

### F7 — Consolidación Jerárquica EROS 3-Tier

```yaml
estado: PRESERVADA_MEJORADA_algoritmo_especificado
herencia_original:
  nombre: "Fase 7: Consolidación Jerárquica (EROS 3-Tier + Coordinator)"
  MiniMax_coordinator: recibe_outputs_integra_maneja_escalados
cambios_v44:
  - EROS_3_Tier_codigo_puro_estadistica
  - Tier3_a_Tier2: resumen_estadistico [count, mean, success_rate]
  - Tier2_a_Tier1: solo_metricas_criticas_lt_5%_contexto
  - Coordinator_merge_determinista_por_tipo_tarea
  - añade_completitud_check: X_de_Y_subtareas_listas
  - añade_drift_detection: divergence_kl_residual
riesgo_estructural: NINGUNO

fases_internas_F7:
  tier3_a_tier2_por_worker:
    logs: worker.eros_memory.tier3_raw_log
    pulse: {total_events, ok_events, error_events, duration_ms}
  tier2_a_tier1_global:
    all_pulses: [w.tier2 for w in workers]
    summary:
      ok: success_rate_ge_0.9
      critical_errors: errors[:3]
      avg_duration_ms: mean(durations)
      completitud: len(certified)/len(workers)
  merge_determinista:
    CODE: concat_codigo_+_tests_+_docs
    MULTI: merge_json_estructurados
    MIXTO: merge_by_subtask_type

input: [certified_outputs_de_F6, eros_memory_por_worker, state_json_completo]
proceso: 100%_Python_puro
output: {merged_output, tier1_summary, informe_pre_entrega}
checkpoint: state.json.f7
aborto: completitud_lt_50%
decisiones_python: 2  # compresion_estadistica, merge
decisiones_llm: 0
archivo: f7_consolidador.py
```

### F8 — Repair Pipeline 5 Pasos + Métricas Duras

```yaml
estado: PRESERVADA_MEJORADA_DSL_jerarquico_metricas
herencia_original:
  nombre: "Fase 8: Repair Pipeline (5 pasos)"
  5_pasos_originales:
    1_retry_simple_3_intentos: preservado
    2_context_compression_L1/L2: modificado_a_DSL_jerarquico_v3_a_v2_a_v1
    3_fallback_model/agent: ELIMINADO_requeria_LLM_adicional
    4_restore_checkpoint: preservado
    5_escalate_coordinator: modificado_a_5_metricas_duras_deciden_aborto

v44_5_pasos:
  1_retry_x3_mismo_DSL: re_ejecuta_worker_DSL_original mismo_contexto, contador_retry
     exito: reemplaza_output_rechazado
     falla_3_veces: paso_2
  2_DSL_jerarquico:
     jerarquia: v3_completo_todos_campos -> v2_medio_campos_criticos -> v1_minimo_solo_critico
     intenta_v2: si_falla_intenta_v1
     v1_falla: paso_3
  3_reduce_contexto_50%_re_ejecuta: trunca_input_data_mitad, re_ejecuta_DL_simple, degradado
     exito: output_parcial_degradado
     falla: paso_4
  4_restore_checkpoint: recupera_state_json_checkpoint_anterior, re_ejecuta_desde_F3_datos_originales
     exito: output_restaurado
     falla: paso_5
  5_evalua_aborto_5_metricas:
     schema_compliance_rate: valid_fields/total_fields
     output_divergence_index: levenshtein(plan, actual)/len(plan)
     dsl_execution_failure_rate: failed_executions/total_attempts
     repair_pattern_stability: mismo_error_2_reparaciones
     token_budget_deviation: abs(tokens_usados-budget)/budget
     flags:
       condition: metric_status_eq_CORRUPT
       decisión:
         2+_flags: ABORTA_reporta_usuario
         1_flag: DEGRADED_retry_alternativo
         0_flags: CONTINUA_improbable

umbral_cada_metric:
  schema_compliance_rate: lt_0.5_es_CORRUPT
  output_divergence_index: gt_0.3_es_CORRUPT
  dsl_execution_failure_rate: gt_0.4_es_CORRUPT
  repair_pattern_stability: true_es_CORRUPT
  token_budget_deviation: gt_3.0_es_CORRUPT

input: [rejected_outputs_de_F6, failed_workers_de_F4/F5, domain_registry_dict_dsl_jerarquico]
proceso: 100%_Python_puro
output: {repaired_outputs, aborted, metrics, status: OK|PARTIAL|ABORTED}
checkpoint: state.json.f8
decisiones_python: 3  # repair, evaluacion_metricas, decision_aborto
decisiones_llm: 0
archivo: f8_repair.py
config: config/dsl_hierarchy.yaml
```

### F9 — Entrega Final + Reporte Automático

```yaml
estado: PRESERVADO_sin_cambios
herencia_original:
  nombre: "Fase 9: Consolidación Final y Entrega"
  original: merge_resultados_consistencia_global_empaquetado_KIMI_REF_archivos_URLs_state_json_final

input: [merged_output_de_F7, repaired_outputs_de_F8, state_json_completo_F-1_a_F9]
proceso_100_python_puro:
  1_empaquetado_segun_modo:
    MODE_CODE: zip_codigo_+_tests_+_docs_+_README
    MODE_MULTI: json_estructurado_+_resumen_md
    MODE_MIXTO: zip_combinado
  2_reporte_automatico_python_no_LLM:
    campos: {modo, modelo_principal, llm_pensó, errores_llm, errores_codigo_puro, calidad_score, tiempo_total_ms, tokens_total, dominios_f55, metricas_f5, metricas_f8, trazabilidad_completa}
    modelo_principal_mapping:
      CODE: Qwen
      MULTI: Gemma4
      MIXTO: Mixto
    llm_usado: si_F4_usado_else_false
    metricas_f5_agregadas:
      max_stress: max(s.get("stress", 0) for s in state.values())
      max_anxiety: max(s.get("anxiety", 0) for s in state.values())
      max_divergence: max(s.get("divergence", 0) for s in state.values())
    metricas_f8: {repairs, aborts}
  3_state_json_final: añade_f9_con_timestamp_reporte_paths_entrega

decisiones_python: 3  # empaquetado_zipfile_json_os, reporte_formateo_estructurado, trazabilidad_recorrido_state
decisiones_llm: 0
archivos: f9_deliver.py
checkpoint: state.json.f9_INMUTABLE_FINAL
aborto: NINGUNO_última_fase
rollback: NINGUNO

usuario_recibe:
  - resultado_empaquetado  # zip/json/md
  - reporte_ejecucion_completo
  - state_json_trazabilidad
```

### Ruta Diseño F6 → F7 → F8 → F9 (Contratos Transiciones)

```yaml
F6_a_F7:
  datos: {certified_outputs, eros_memory_workers, schemas}
  validaciones: certified_no_vacio_si_vacio_F8_repair
  abortos: NINGUNO_F8_maneja_rechazados
  rollback: SI_checkpoint_F6_re_verificar

F7_a_F8:
  datos: {rejected_outputs, failed_workers, informe_pre_entrega}
  validaciones: rejected_no_vacio_si_vacio_salta_F8_F9_directo
  abortos: NINGUNO
  rollback: SI_checkpoint_F7_re_consolidar

F8_a_F9:
  datos: {repaired_outputs, merged_output_F7, state_json_completo}
  validaciones: state_json_todas_fases_F-1_a_F8
  abortos: NINGUNO_F9_entrega_lo_que_tenga
  rollback: NINGUNO

F9_a_USER:
  datos: {empaquetado, reporte, state_final}
  validaciones: empaquetado_no_vacio_reporte_campos_obligatorios
  abortos: NINGUNO
  rollback: NINGUNO
```

### Conclusión Bloque 4

```yaml
total_riesgos_estructurales: 0  # NINGUNO en F7, F8, F9
fase_mas_estable_pipeline: F9  # sin_modificaciones
cambios_v44:
  F7: [algoritmo_EROS_definido, completitud_check, drift_detection]
  F8: [DSL_jerarquico, 5_metricas_duras, aborto_determinista]
  F9: [reporte_estructurado_python_puro, MODE_entrega_adaptativo]
preservado_totalmente:
  - F7_capacidad_comprimir_logs_consolidar
  - F8_capacidad_reparar_outputs_fallidos
  - F9_capacidad_entregar_resultado_usuario
```

---

## DOC BLOQUE_2_F4_EJECUCION: Verificación Cruzada F4 vs Doc Base

### Diagrama F3 → F4 → F5 (Transversal con bifurcación por modo)

```
F3 ─► [F4 worker_pool asyncio.semaphore(10)]
       ├── MODE_CODE: [Qwen arquitectura] ─► [Llama4 escritura] ─► LLM_pensó=true
       ├── MODE_MULTI: [Gemma4 ejecuta_DSL_predefinido] ───────► LLM_ejecuta_no_pensa
       └── MODE_MIXTO: [subtareas_CODE_a_Qwen/Llama4] + [subtareas_MULTI_a_Gemma4] ─► DAG_decide_paralelismo
   ─► [F5 monitoreo_3_sistemas]
```

### F4 — Worker Pool + Team Engine

```yaml
estado: PRESERVADA_MEJORADA_bifurcacion_modo_limites_duros
herencia_original:
  nombre: "Fase 4: Ejecución (Worker Pool + Team Engine)"
  patron_dual_Kimi_MiniMax:
    Kimi: worker_pool_asyncio_gather_hasta_100_workers
    MiniMax: team_engine_leader_worker_verifier_3_rondas_por_worker
cambios_v44:
  - mantiene_worker_pool_asyncio_hasta_100_workers
  - mantiene_semaforo_maximo_10_workers_LLM_simultaneos
  - añade_bifurcacion_MODE_CODE/MODE_MULTI/MODE_MIXTO
  - MODE_CODE: Qwen_arquitectura_a_Llama4_escritura
  - MODE_MULTI: Gemma4_ejecuta_DSL_predefinido
  - MODE_MIXTO: subtareas_CODE_a_Qwen_Llama4, subtareas_MULTI_a_Gemma4
  - limite_32K_tokens/30s_por_worker_pre_estimado_F2
  - team_engine_3_rondas_a_opcional_segun_verification_profile
riesgo_estructural: NINGUNO

submodos:
  MODE_CODE:
    LLMs_activas: [Qwen_arquitectura, Llama4_escritura]
    patron: Qwen_recibe_requerimiento_+_constraints_+_dsl_template -> genera_estructura_proyecto_json -> Llama4_recibe_estructura_+_dsl_codigo_py -> genera_archivos_codigo_+_tests -> validacion_python_syntax_compile_schema_jsonschema_pytest_sandbox
    verificacion_inmediata: [syntax_check_compile, schema_jsonschema, tests_pytest_sandbox]
    fallo: marca_failed_a_F8_Repair
    %_LLM: 60
    %_CODIGO: 40
  MODE_MULTI:
    LLMs_activas: [Gemma4_ejecuta_no_pensa]
    patron: Gemma4_recibe_datos_+_dsl_dominio_py_+_schema_salida_json -> ejecuta_paso_a_paso_funciones_DSL -> output_intermedio -> validacion_post_cada_paso
    retry: si_schema_falla_max_3_intentos
    fallo_3_intentos: marca_failed_a_F8_Repair
    DSL_incompleto: aborta_DSL_INCOMPLETO_a_activa_F5.5_generacion_puntual
    %_LLM: 30
    %_CODIGO: 70
  MODE_MIXTO:
    patron: F1_etiqueta_subtareas_CODE_o_MULTI -> F2_construye_DAG_dependencias -> F4_ejecuta_por_grupos_paralelos
    ejemplo:
      Grupo_1_paralelo:
        - Subtarea_A_CODE: Qwen_estructura_API
        - Subtarea_B_MULTI: Gemma4_resume_requerimientos
      Grupo_2_secuencial_depende_Grupo_1:
        - Subtarea_C_CODE: Llama4_codigo_API  # depende_A
        - Subtarea_D_MULTI: Gemma4_documenta_endpoints  # depende_C
    sin_aristas: asyncio_gather_paralelo
    con_aristas: secuencial
    %_LLM: variable_segun_proporcion
    %_CODIGO: variable_python_orquesta

config_semaforo_y_limites:
  asyncio_Semaphore: 10_workers_LLM_simultaneos
  asyncio_wait_for_timeout: 30s_por_worker
  token_budget_per_worker: 32000
  pre_estimado_en: F2_F2

limites_qwen_llama4:
  tokens_max: 32000
  si_estructura_excede: F2_ya_aborto_pre_estimacion
  si_codigo_excede: divide_archivos_mas_pequenos_F2_DAG

input: [workers_listos_F3, grupos_paralelos_F2, execution_profile_F1, verification_profile_F1]
proceso: Python_+_LLM
output: {outputs_por_worker: [{id, output, status, tokens}], tokens_total, duration_total}
checkpoint: state.json.f4
aborto: SI_timeout_token_excedido_error_LLM
decisiones_python: 4  # semaforo_scheduling, validation_post_ejecucion_jsonschema, timeout_enforcement_wait_for, token_accounting
decisiones_llm_per_mode: [CODE_60, MULTI_30, MIXTO_variable]
archivos: [f4_worker_pool.py, config/worker_limits.yaml]
errores:
  - TimeoutError: excedio_30s_a_SIGKILL_retry_F8
  - TokenLimitError: excedio_32K_a_aborta_subtarea_especifica
  - SchemaValidationError: output_no_comple_schema_a_fail_F8
  - LLMError: modelo_no_responde_a_retry_con_backoff
```

### Transiciones F3 → F4 → F5 (Contratos)

```yaml
F3_a_F4:
  llama: f3_aislamiento.py
  recibe: f4_worker_pool.py
  datos: {workers_listos, grupos_paralelos, execution_profile, verification_profile}
  validaciones: [workers_no_vacio, dsl_validado, schema_validado, modelo_en_Qwen_Llama4_Gemma4]
  abortos: [WORKERS_LISTOS_VACIO, DSL_NO_VALIDADO]
  rollback: SI_checkpoint_F3

F4_a_F5:
  llama: f4_worker_pool.py
  recibe: f5_monitor.py
  datos: {outputs_por_worker, failed_workers, tokens_total, duration_total_ms, eros_memory.tier3_raw_log}
  validaciones: [outputs_no_vacio_aunque_parcial, state_json_actualizado]
  abortos: [OUTPUTS_VACIO_TOTAL]
  rollback: SI_checkpoint_F4
```

### Conclusión Bloque 2

```yaml
riesgos_estructurales: 0  # NINGUNO
team_engine_opcional: si_segun_verification_profile
nuevos_llms_introducidos: Qwen_arquitectura, Llama4_escritura (CODE); Gemma4_ejecuta_DSL (MULTI)
preservado:
  - worker_pool_asyncio
  - team_engine_3_rondas (opcional)
  - context_aislado (viene de F3)
```

## DOC BLOQUE_3_F5_F5.5_F6_CONTROL_VERIFICACION: Verificación Cruzada

### Diagrama F4 → F5 → F5.5 ↔ F6 → F7 (Transversal)

```
F4 ─► [F5 monitoring 3-sistemas simultaneos] ─► outputs_filtrados_a_F6
       │                                          │
       ├── system_stress (cpu+memory+queue)/3 > 0.8 → SIGKILL + respawn
       ├── anxiety_level errores_consecutivos >= 3 → confirma_o_respawn  
       └── divergence_kl levenshtein(plan, actual) > 0.02 → rollback F3

       [F5.5 generador_DSL nuevo dominio] ↔ [F6 detecta DSL_INCOMPLETO]
       ├── Gate 1 AST parse syntax + imports peligrosos
       ├── Gate 2 Docker sandbox tests 60s sin_red
       └── Gate 3 aprobacion humana → f55_cubierto=true

F6 ─► [verificacion 3-capas]
       ├── Capa 1: jsonschema Python puro
       ├── Capa 2A: diff+checksum hashlib python puro (default)
       ├── Capa 2B: LLM anclado (SOLO si MODE_CODE AND f55_cubierto=false) ── transitoria
       └── Capa 3: pytest/unittest Python puro
   ─► [F7 consolidador]
```

### F5 — Monitoreo Simultáneo 3-Sistemas

```yaml
estado: PRESERVADA_MEJORADA_metricas_renombradas_a_tecnicas_duras
herencia_original:
  nombre: "Fase 5: Monitoreo Simultáneo (PAD + Ansiedad + Anti-Drift)"
  3_sistemas_originales:
    PAD_arousal_pleasure: arousal_gt_0.8_AND_pleasure_lt_0.2_a_SIGKILL_+_respawn
    ansiedad_duda_circulos: nivel_1_a_confirmar_o_respawn
    anti_drift_KL_divergence: KL_plan_actual_gt_0.02_a_halt_+_rollback
renombrado_v44:
  PAD_a_system_stress: (cpu_+_memory_+_queue/25)/3_gt_0.8_a_SIGKILL_+_respawn
  pleasure_a_success_rate: passed/total_lt_0.2_a_SIGKILL
  ansiedad_a_anxiety_level: errores_consecutivos_ge_3_a_confirmar_o_respawn
  anti_drift_a_divergence_kl: levenshtein(plan_output_actual_output)/len(plan)_gt_0.02_a_rollback

3_sistemas_simultaneos_nuevo_diseno:
  SISTEMA_1_system_stress_ex_PAD:
    metricas: [cpu_percent_gt_80, memory_percent_gt_80, queue_depth_gt_20]
    formula: stress = (cpu_+_memory_+_queue/25)/3
    umbral: stress_gt_0.8_a_SIGKILL_+_respawn
    accion: asyncio_create_task(respawn_worker(id))
  SISTEMA_2_anxiety_level_ex_Ansiedad:
    metricas: [errores_consecutivos_por_worker, retries_sin_exito, schema_validation_fails]
    niveles:
      nivel_1: 1_error_a_log_warning
      nivel_2: 2_errores_a_retry_automatico
      nivel_3: ge_3_errores_a_confirmar_o_respawn
    accion: si_nivel_3_a_marca_worker_para_F8_Repair
  SISTEMA_3_divergence_kl_ex_Anti_Drift:
    formula_KL: KL(plan_output_parallel_actual_output) = sum plan_i_*_log(plan_i/actual_i)
    simplificacion_codigo: diff_ratio = levenshtein(plan, actual)/len(plan)
    umbral: diff_ratio_gt_0.02_a_ROLLBACK
    accion: restore_checkpoint_F3_+_re_ejecutar_worker

input: [outputs_por_worker_F4, state_json_global, metricas_sistema_cpu_memory_queue]
loop: asyncio_each_500ms
proceso: 100%_Python_puro_psutil_asyncio
output: {actions: [SIGKILL, ROLLBACK, RETRY], workers_afectados: list, state_updates: dict}
checkpoint: state.json.f5
aborto: SI_stress_critico_multiple_workers
decisiones_python: 3  # calculo_metricas_psutil_asyncio, comparacion_umbrales, acciones_control_asyncio_create_task_os_kill
decisiones_llm: 0
archivos: [f5_monitor.py, config/monitor_thresholds.yaml]

errores:
  - stress_critico_global: SIGKILL_multiples_workers
  - divergencia_masiva: rollback_completo_a_F3
  - loop_anxiety: mismo_worker_falla_3_veces_a_F8_Repair
```

### F5.5 — Generación DSL Dominio Nuevo (transitoria)

```yaml
estado: NUEVA_ADITIVA
descripcion: >-
  Cuando F6 detecta dominio sin reglas de verificación, generar DSL,
  template, tests UNA SOLA VEZ con 3 gates de seguridad.
existencia_en_doc_base: NO_EXISTIA

activacion:
  - F6_Capa_3_detecta: dominio_X_no_tiene_verify_X_py
  - consulta_domain_registry: f55_cubierto_eq_false
  - si_usuario_configuro_auto_generate_true: activa_F5.5
  - si_auto_generate_false: aborta_con_DSL_INCOMPLETO

proceso_una_sola_vez_Llama4:
  1: Llama4_recibe = brief_del_dominio_+_ejemplos_de_otros_verify_py
  2: Llama4_genera:
     - dsl_<dominio>_v1.yaml: reglas_verificacion
     - template_<dominio>.py: estructura_de_tarea
     - tests_<dominio>.py: tests_unitarios
  3: GATE_1_AST_estatico:
     - ast.parse()_verifica_syntax
     - detecta: os_system, eval, exec, __import__
     - detecta: imports_no_declarados
     - resultado: PASS_o_FAIL
  4: GATE_2_Docker_sandbox:
     - ejecuta_tests_en_contenedor_aislado
     - timeout: 60s
     - sin_red, sin_filesystem_host, sin_variables_entorno
     - resultado: PASS_o_FAIL
  5: GATE_3_aprobacion_humana:
     - muestra_DSL_generado_al_usuario
     - usuario_aprueba_o_rechaza_o_modifica
     - si_aprueba: copia_a_config_dsl_+_domain_registry_f55_cubierto=true
     - si_rechaza: descarta_+_reporta_DSL_INCOMPLETO

post_aprobacion:
  - F6_Capa_2_cambia_a_codigo_puro_para_este_dominio
  - futuras_tareas_de_este_dominio: 0%_LLM_en_verificacion
  - DSL_añade_a_config_dsl_permanentemente

%_LLM: Puntual_una_sola_vez_por_dominio
%_CODIGO: 100%_en_Gate_1_y_Gate_2
checkpoint: state.json.f5.5
aborto: SI_Gate_1_2_3_falla
decisiones_python: 4  # activacion_consulta_domain_registry, Gate_1_ast_parse, Gate_2_subprocess_docker, Gate_3_interfaz_usuario
decisiones_llm: 1  # generacion_DSL_Llama4_una_sola_vez
archivos: [f5_5_generador_dsl.py, config_dsl/, config/domain_registry.yaml]
errores:
  - Gate_1_FAIL_syntax_invalida: retry_generacion_max_3
  - Gate_2_FAIL_tests_fallan: retry_con_mas_ejemplos
  - Gate_3_RECHAZO: f55_cubierto_permanece_false

output: {dominio: str, dsl_path: str, tests_path: str, approved: bool}
```

### F6 — Verificación 3-Capas

```yaml
estado: PRESERVADA_MEJORADA_3_capas_LLM_a_2_capas_puras_+_1_transitoria
herencia_original:
  nombre: "Fase 6: Verificación 3-Capas (Adversarial + Cruzada + Maker-Checker)"
  original_3_capas_LLM:
    capa_1_adversarial_MiniMax: verifier_busca_errores_3_rondas
    capa_2_cruzada_Kimi: executor_B_valida_output_de_A
    capa_3_maker_checker: modulo_A_produce_modulo_B_verifica

cambios_v44:
  - Capa_1: jsonschema_Python_puro_reemplaza_LLM_adversarial
  - Capa_2A: diff_+_checksum_hashlib_python_puro_reemplaza_LLM_cruzada
  - Capa_3: pytest_unittest_python_puro_reemplaza_Maker_Checker_LLM
  - añade: Capa_2B_LLM_anclado_SOLO_en_MODE_CODE_Y_SOLO_si_f55_cubierto_false
  - añade: DSL_de_verificacion_expandible_por_dominio
  - 5_dominios_base_cubiertos: web, datos, texto, codigo, imagenes

3_capas_nuevo_diseno:
  CAPA_1_schema_validation_python_puro:
    - jsonschema.validate(output, schema_json)
    - todos_campos_obligatorios_presentes
    - tipos_correctos_str_int_list_dict
    - formatos_validos_email_URL_fecha_ISO
    - resultado: PASS_o_FAIL_con_lista_errores
    - FAIL_a_marca_SCHEMA_INVALIDO
  CAPA_2A_diff_checksum_python_puro_default:
    - hashlib.sha256(output.encode()).hexdigest()
    - compara_contra_expected_pattern_si_existe
    - levenshtein(output, expected)/len(expected)
    - resultado: PASS_o_DIVERGENCE_DETECTED
  CAPA_2B_LLM_anclado_condicional:
    condicion_activacion: execution_profile_eq_MODE_CODE_AND_domain_registry_dominio_f55_cubierto_eq_false
    LLM_recibe: brief_original_+_output_generado
    pregunta: "¿Este output contradice el brief?"
    respuesta: SI/NO_+_razon
    si_SI: marca_CONTRADICCION_BRIEF_a_F8_Repair
    si_NO: pasa
    nota: capa_2B_es_TRANSITORIA_una_vez_F5.5_cubre_dominio_a_se_desactiva
  CAPA_3_tests_automaticos_python_puro:
    - pytest tests_<dominio>.py (generados_en_F5.5)
    - unittest_para_validaciones_especificas
    - si_codigo: compile()_+_syntax_check
    - si_web: BeautifulSoup_checks_SEO_responsive
    - si_datos: pandas_schema_validation
    - si_texto: longitud_+_formato_+_encoding
    - si_imagenes: dimensiones_+_formato_+_checksum
    - resultado: PASS_o_FAIL_con_logs_detallados

logica_decision:
  Capa_1_FAIL_a_F8_Repair  # schema_invalido
  Capa_2A_FAIL_a_F8_Repair  # divergencia_detectada
  Capa_2B_CONTRADICCION_a_F8_Repair  # brief_violado
  Capa_3_FAIL_a_F8_Repair  # tests_no_pasan
  TODAS_PASS_a_output_certificado_a_F7

5_dominios_base_cubiertos_DSL:
  verify_web: SEO, responsive, accesibilidad, performance
  verify_datos: schema, tipos, nulos, rangos
  verify_texto: longitud, formato, encoding, idioma
  verify_codigo: syntax, tests, imports, seguridad
  verify_imagen: dimensiones, formato, checksum, metadata

input: [outputs_por_worker_F4, schemas_F3, domain_registry, execution_profile]
proceso: jsonschema_+_hashlib_+_difflib_+_pytest_+_unittest
output: {certified_outputs: list, rejected: list, capa2b_usada: bool, f55_cubierto: bool}
checkpoint: state.json.f6
aborto: SI_todos_outputs_rechazados
decisiones_python: 4  # seleccion_capa_2A_vs_2B_if_else_domain_registry, validation_schema_jsonschema, diff_checksum_hashlib_difflib, tests_pytest_unittest
decisiones_llm: 1  # Capa_2B_Llama4_anclado_solo_cold_start_dominio_AND_MODE_CODE
archivos: [f6_verificador.py, verify_<dominio>.py_uno_por_dominio]

riesgo_estructural: NINGUNO
```

### Loop Condicional F5.5 ↔ F6

```yaml
F5.5_a_F6_loop_condicional:
  quien_llama: f6_verificador.py  # detecta_DSL_INCOMPLETO
  quien_recibe: f5_5_generador_dsl.py
  datos: {dominio, brief, ejemplos_dsl}
  validaciones: [dominio_no_en_registry_o_f55_cubierto_false, usuario_autorizo_auto_generate]
  abortos: SI_usuario_rechaza_Gate_3
  rollback: NINGUNO_F5.5_aditivo_no_destructivo
```

### Transiciones F4 → F5 → F6 → F7

```yaml
F4_a_F5: {datos_outputs_por_worker_failed_workers_tokens_total_duration_total_eros_memory_tier3_raw_log, validaciones_outputs_no_vacio_state_json_actualizado, abortos_OUTPUTS_VACIO_TOTAL, rollback_SI_checkpoint_F4}
F5_a_F6: {datos_outputs_filtrados_solo_OK_no_failed_schemas_F3_acciones_control_aplicadas, validaciones_outputs_validados_F5_stress_anxiety_divergence_OK, abortos_NINGUNO_F5_ya_filtro, rollback_NINGUNO}
F6_a_F7: {datos_certified_outputs_schemas_verification_results, validaciones_certified_no_vacio_si_vacio_F8_repair_todo, abortos_NINGUNO_F8_maneja_rechazados, rollback_SI_checkpoint_F6_re_verificar}
```

### Conclusión Bloque 3

```yaml
riesgos_estructurales: 0  # los 3 NINGUNO
cambios_v44_resumen:
  F5: metricas_emocionales_a_tecnicas_duras_3_sistemas_mantenidos
  F5.5: NUEVA_ADITIVA_3_gates_seguridad_cold_start_dominio
  F6: 3_capas_LLM_a_2_puras_+_1_transitoria_5_dominios_base
preservacion_total:
  - F5_monitorear_y_tomar_acciones_de_control
  - F6_verificar_outputs_y_certificarlos
nuevos_archivos_per_dominio: verify_<dominio>.py
```

---

## DOC PARTE_4_INTEGRACION_COMPLETA: Pipeline v4.4 — F-1 → F9

### Diagrama Global Pipeline (Transversal Horizontal)

```
USR ─► [BLOQUE_1 100%CODIGO: F-1→F0→F1→F2→F3] ─► workers_listos_a_F4
     ─► [BLOQUE_2 LLM: F4 worker_pool] ─► outputs_a_F5
       ├── MODE_CODE: Qwen_arquitectura_+_Llama4_escritura_60%LLM
       ├── MODE_MULTI: Gemma4_ejecuta_DSL_30%LLM
       └── MODE_MIXTO: variable
     ─► [BLOQUE_3 100%CODIGO: F5→F5.5↔F6] ─► certified_a_F7
     ─► [BLOQUE_4 100%CODIGO: F7→F8→F9] ─► USR_resultado
```

### Auditoría Completa Decisiones (Quién Decide Qué)

```yaml
total_decisiones_por_tipo:
  PYTHON_orquestacion: 50+  # F-1, F0, F1, F2, F3, F5, F7, F8, F9
  PYTHON_workers_F4: 5  # semaforo, scheduling, wait_for, jsonschema, token_accounting
  LLM_generacion:
    F4_CODE_Qwen_arquitectura: genera_estructura_proyecto_json
    F4_CODE_Llama4_escritura: genera_codigo_fuente_+_tests
    F4_MULTI_Gemma4_ejecuta: ejecuta_funciones_DSL_no_genera
    F4_MIXTO: variable_segun_subtarea
    F5_5_Llama4_DSL: genera_DSL_dominio_nuevo_una_sola_vez_3_gates
    F6_Capa2B_Llama4: verifica_si_output_contradice_brief_solo_cold_start
  USUARIO:
    F5.5_Gate_3: aprueba_o_rechaza_DSL_generado
    F2: confirma_si_presupuesto_excede_32K_o_30s
    F8: recibe_reporte_aborto_si_2_metricas_CORRUPT
    F9: recibe_resultado_final_+_reporte_completo

categorias_decisiones:
  ORQUESTACION_Y_SCHEDULING: PYTHON
  VALIDACIONES_Y_MONITOREO: PYTHON
  CONTROL_DECISIONES_SIGKILL_ROLLBACK: PYTHON
  MERGE_EMPAQUETADO_REPORTE: PYTHON
  GATES_F5.5_AST_SANDBOX: PYTHON
  CAPAS_1_2A_3_F6: PYTHON
  EJECUCION_DSL_NO_DECISION: GEMMA4_solo_ejecuta
  GENERACION_CODIGO_NUEVO: QWEN_+_LLAMA4
  GENERACION_DSL_NUEVO: LLAMA4_una_vez_por_dominio
  VERIFICACION_BRIEF: LLAMA4_transitorio
```

### Auditoría Consumo LLM (Por Fase)

```yaml
tabla_llm_por_fase:
  F-1: [false, --, 0%]
  F0: [false, --, 0%]
  F1: [false, --, 0%]
  F2: [false, --, 0%]
  F3: [false, --, 0%]
  F4_CODE: [true, Qwen/Llama4, 60%]
  F4_MULTI: [true, Gemma4, 30%]
  F4_MIXTO: [true, Mixto, variable]
  F5: [false, --, 0%]
  F5.5: [true, Llama4, 0%_amortizado_una_sola_vez_por_dominio]
  F6_CAPA1: [false, --, 0%]
  F6_CAPA2A: [false, --, 0%]
  F6_CAPA2B: [true_solo_cold_start_AND_MODE_CODE, Llama4, 0-5%]
  F6_CAPA3: [false, --, 0%]
  F7: [false, --, 0%]
  F8: [false, --, 0%]
  F9: [false, --, 0%]

promedios_por_modo:
  MODE_CODE: ~93%_codigo_a_~7%_LLM  # F4_60%_+_F6_Capa2B_5-7%
  MODE_MULTI: ~99%_codigo_a_~1%_LLM  # F4_30%_+_F6_0%
  MODE_MIXTO: variable_ponderado_CODE_vs_MULTI
  GLOBAL: ~97%_codigo_a_~3%_LLM  # amortizado
```

### Mapa Responsabilidades por Capa

```yaml
PYTHON_SISTEMA:
  fases: [F-1, F0, F1, F2, F3, F5, F7, F8, F9]
  responsabilidades:
    - todas_las_decisiones_de_orquestacion
    - scheduling_validacion_monitoreo
    - control_SIGKILL_respawn_rollback_aborto
    - merge_empaquetado_reporte_trazabilidad
    - gates_1_y_2_de_F5.5_ast_sandbox
    - capas_1_2A_3_de_F6_jsonschema_hashlib_pytest

GEMMA4_ejecutor_DSL:
  fase: F4_MODE_MULTI
  rol: ejecuta_funciones_predefinidas_en_dsl_py
  restricciones:
    NO_genera_codigo_nuevo: true
    NO_toma_decisiones: true
    NO_interpreta_briefs: true
  input: [datos, DSL, schema]
  output: resultado_estructurado

QWEN_arquitecto:
  fase: F4_MODE_CODE
  rol: diseña_estructura_de_proyectos_de_codigo
  output: estructura_proyecto_json
  restricciones:
    NO_escribe_codigo_final: eso_es_Llama4
    NO_verifica_outputs: eso_es_F6

LLAMA4_escritor_y_generador_DSL:
  usos:
    - F4_MODE_CODE: escribe_codigo_fuente_+_tests
    - F5.5: genera_DSL_de_verificacion_para_dominios_nuevos_UNA_SOLO_VEZ
    - F6_Capa_2B_transitorio: verifica_si_output_contradice_brief
  restricciones:
    NO_toma_decisiones_de_control: SIGKILL_aborto
    NO_decide_rutas: eso_es_F1
    NO_decide_paralelismo: eso_es_F2

DSL_reglas_predefinidas:
  ciclo_vida:
    F3: precargadas_antes_de_ejecucion
    F4: ejecutadas_por_Gemma4_MODE_MULTI
    F5.5: generadas_UNA_SOLO_VEZ_por_Llama4_aprobadas_por_usuario
    F6: aplicadas_por_Python_para_verificacion
    F8: degradadas_jerarquicamente_v3_a_v2_a_v1
  jerarquia_repair_F8:
    v3_completo: todos_campos_validacion_estricta
    v2_medio: campos_criticos_validacion_media
    v1_minimo: solo_campo_critico_no_vacio

DOMAIN_REGISTRY_configuracion_central:
  files_y_usos:
    F-1: signals_yaml_pesos_contextuales
    F0_F1: keywords_execution_profiles_worker_profiles
    F2: limits_tokens_runtime_workers
    F5.5_F6: f55_cubierto_flags_por_dominio
    F6: verification_profiles_por_dominio
    F8: dsl_hierarchy_v3_v2_v1

EROS_memoria_jerarquica:
  3_tiers:
    F3: prepara_tier3_raw_log_tier2_pulse_buffer_tier1_summary_slot
    F4: escribe_tier3_raw_log_durante_ejecucion
    F5: lee_tier3_calcula_tier2_comprime_tier1
    F7: usa_tier1_para_decision_de_merge
```

### Veredicto Final Preservación

```yaml
arquitectura_original_preservada: SI
capacidad_original_desaparecio: NO
  nota: "Fallback Model/Agent de F8 eliminado intencionalmente porque requería LLM adicional para repair, violando objetivo de reducir LLM. Reemplazado por métricas duras + aborto determinista."
fase_simplificada_en_exceso: NO
  nota: "F5 métricas emocionales renombradas a técnicas, pero funcionalidad preservada. F6 verificación LLM reemplazada por código puro + capa transitoria, pero cobertura igual o superior con DSL expandido por dominio."

arquitectura_nueva_estrictamente_superior:
  1: "Menos LLM: de ~20% a ~3% amortizado"
  2: "Mejor estructura: DAG determinista, DSL jerárquico, EROS formalizado"
  3: "Multi-modal: MODE_CODE + MODE_MULTI + MODE_MIXTO diferenciados"

riesgos_arquitectonicos: 20_identificados
  mitigaciones_resumen:
    DSL_corrupto: AST_+_sandbox_+_aprobacion
    domain_registry_inconsistente: validacion_jsonschema
    falso_positivo_F6: 3_capas_+_jerarquia_DSL
    loops_F8: 5_metricas_+_aborto_duro
    clasificacion_erronea_F0: boost_rules_+_default_MIXTO
    dependencia_circular_F2: networkx_+_aborto
```

### F9 — Campos Obligatorios Reporte Final (12 campos)

```yaml
campos_obligatorios_reporte_F9:
  - modo
  - modelo_principal
  - llm_pensó
  - errores_llm
  - errores_codigo_puro
  - calidad_score
  - tiempo_total_ms
  - tokens_total
  - dominios_f55
  - metricas_f5
  - metricas_f8
  - trazabilidad_completa
```

---

## DOC NCT-LOP-200X-2026-06-22-ADDENDUM: MiMo Code + Open-Source Agents + HF Spaces + Micro-Agents

### JSON Summary

```yaml
$schema: https://NCT/turbo/schemas/lop-system-v200.schema.json
document_id: NCT-LOP-200X-2026-06-22-ADDENDUM
parent_document: NCT-LOP-100X-2026-06-22
target: Mavis_M3
package: nct_coordinator.lop_v200
namespace: nct.lop.v200
version: 200.0.0
scope_additions:
  - mimo_code_loop_analysis
  - open_source_agent_catalog
  - chained_task_strategy_with_example_agent
  - seed_information_pre_analysis
  - rag_github_web_research_cycles
  - huggingface_spaces_remote_compute_fleet
  - deterministic_dsl_90pct_code_10pct_llm
  - specialized_micro_agents
```

### MiMo Code — Análisis del Código Fuente

```yaml
descripcion: agente_programacion_terminal_MIT_construido_sobre_OpenCode_por_equipo_MiMo_Xiaomi
disenado_para: tareas_horizonte_largo_200_plus_pasos_continuos
primera_release: 2026-06-11_v0.1.0
stack_tecnologico: [Bun, TypeScript, Effect, SolidJS_TUI, Tauri_desktop]
modelos_compatibles: [MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM]

3_pilares_arquitectonicos:
  compute:
    patron: Max_Mode_multi_sample_+_majority_voting_+_best_of_N_self_verification
    goal_stop: criterio_de_parada_nuevo_p9.5
    dynamic_workflow: ALV_LOP_QUANTUM_FRACTAL_NESTED
  memory:
    checkpoint_rebuild: state_jsonl_con_replay_to_checkpoint_t
    writer_subagent: MA-RAG-SYNTH
    4_tier_memory:
      tier0_raw: raw_logs
      tier1_session: session_resumen
      tier2_strategic: strategic_pulses
      tier3_project: project_memory_sqlite
  evolution:
    dream: consolidacion_periodica_7_dias_cron
    distill: destilacion_diaria_cron
    project_memory: state/project_memory.sqlite

benchmarks_vs_claude_code:
  SWE-Bench_Pro_V2: +5%
  Terminal_Bench_2: +5%
  ultra_long_200_plus_steps: beats_Claude_Code

7_loops_internos_MiMo_identificados:
  decision_loop: cada_turno_output_tool_call_o_respuesta_solo_conversacion
  checkpoint_loop: cada_N_turnos_snapshot_firmado_state_jsonl
  writer_loop: cuando_contexto_gt_70%_resumen_estructurado_memory_tier-N_md
  max_mode_loop: decisiones_criticas_K_muestras_voto_efimero
  dream_loop: cada_7_dias_memoria_consolidada_memory_dream_md
  repair_loop: en_error_plan_de_recuperacion_state_jsonl
  evolution_loop: al_cierre_sesion_skill_proc_prompt_nuevo_skills
```

### Adaptación MiMo → NCT v200

```yaml
componente_MiMo_a_NCT:
  Max_Mode:
    MiMo: multi_sample_+_voting_+_best_of_N
    NCT: worker_pool_py_con_k_samples_por_decision_critica
  Goal_Stop:
    MiMo: criterio_de_parada
    NCT: nueva_fase_P9.5_goal_check_antes_de_deliver
  Dynamic_Workflow:
    MiMo: workflow_dinamico
    NCT: ALV_LOP_QUANTUM_FRACTAL_NESTED_ya_propuesto_v100
  Checkpoint_Rebuild:
    MiMo: persistencia_con_replay
    NCT: state_engine_py_con_replay_to_checkpoint_t
  Writer_subagent:
    MiMo: compactador_de_contexto
    NCT: MA-RAG-SYNTH_nuevo_micro_agente
  4_tier_memory:
    MiMo: 4_capas_memoria
    NCT: extender_EROS_3_tier_a_4_tiers_tier0_raw_tier1_session_tier2_strategic_tier3_project
  Dream:
    MiMo: consolidacion_periodica
    NCT: nuevo_job_cron_weekly_a_MA-DREAM
  Distill:
    MiMo: destilacion
    NCT: nuevo_job_cron_daily_a_MA-DISTILL
  Project_Memory:
    MiMo: project_memory
    NCT: state/project_memory.sqlite

regla: nada_de_copiar_literal
```

### Catálogo Open-Source Clones (15 backends)

```yaml
tier_s_plus:
  OpenCode: [154.5K_stars, TypeScript, 75+_LLMs, MCP_first_true]
  Gemini_CLI: [103.1K_stars, TypeScript, Gemini_free, parcial]
  OpenHands: [72.6K_stars, Python, varios, parcial]
  Open_Interpreter: [63.4K_stars, Python, local, false]
  Aider: [44.3K_stars, Python, 100+_LLMs, parcial]
  Goose: [43.7K_stars, Rust, varios, MCP_first_true]

tier_a:
  Qwen_Code: [24.1K_stars, TypeScript, Qwen3-Coder, MCP_first_true]
  Crush: [23.8K_stars, Go, varios, MCP_first_true]
  Kimi_CLI: [8.4K_stars, Python, Kimi_K2, parcial]
  Forge_Code: [7.2K_stars, Rust, 300+_modelos, parcial]
  MiMo_Code: [n/a_stars, TypeScript, MiMo-V2.5+_otros, parcial]

tier_b:
  BLXCode: [n/a, TypeScript, MCP_first_true]
  Open_Design: [n/a, 16_CLIs_integrados, MCP_first_true]
  OpenClaw: [n/a, OpenRouter+MiMo-V2, parcial]
  KiloCode: [n/a, TypeScript, Kilo_Gateway, MCP_first_true]
  Cline: [n/a, TypeScript, 100+_modelos, MCP_first_true]
  BLACKBOX_AI: [n/a, ?]

languages: [TypeScript, Python, Rust, Go]
mcp_first_obligatorio: [Goose, Open_Design, BLXCode]
```

### Regla Selección Router (15 backends)

```yaml
signals: [cost, latency, capability, license, mcp_native]

reglas:
  - if task_type_eq_code_generation and budget_eq_low:
      backend: opencode
      model: deepseek-coder
  - if task_type_eq_long_horizon and horizon_h_ge_24:
      backend: mimo_code
      model: mimo-v2.5
  - if task_type_eq_research_rag:
      backend: openhands
      model: qwen3-coder
  - if task_type_eq_ui_design:
      backend: open_design
      model: sonnet-4.6
  - default:
      backend: goose
      model: claude-sonnet-4.6
```

### Contrato Común de Invocación (todos los backends)

```yaml
backend_invocation:
  transports: [stdio, http, mcp]
  input_schema: nct.task.v1.json
  output_schema: nct.result.v1.json
  timeout_s: 600
  cancel_token: true
  auth:
    type: byok_or_proxy
    proxy_url: http://nct-proxy/api/proxy/{provider}/stream
```

### Catálogo 12 Micro-Agentes Especializados (MA-*)

```yaml
MA-CODE-GEN:
  responsabilidad: genera_codigo_a_partir_de_spec
  input: [spec.md, stack.json]
  output: [code.zip, diff.patch]
  tiempo: 5-30s
MA-CODE-LINT:
  responsabilidad: lint_+_format_+_type_check
  input: code.zip
  output: report.json
  tiempo: 2-10s
MA-CODE-TEST:
  responsabilidad: unit_+_integration_+_mutation
  input: [code.zip, tests/]
  output: [junit.xml, coverage.json]
  tiempo: 10-60s
MA-RAG-SEARCH:
  responsabilidad: busqueda_vectorial_+_rerank
  input: [query, k]
  output: chunks.json_con_citas
  tiempo: 3-15s
MA-RAG-SYNTH:
  responsabilidad: sintetiza_respuesta_con_citas
  input: chunks.json
  output: answer.md
  tiempo: 5-20s
MA-DOC-WRITE:
  responsabilidad: documenta_arquitectura/decisiones
  input: [artifacts/, audience]
  output: doc.md
  tiempo: 5-15s
MA-ARCH-PLAN:
  responsabilidad: planifica_arquitectura_y_stack
  input: requirements.json
  output: arch.yaml
  tiempo: 5-30s
MA-VERIFY-3CAPAS:
  responsabilidad: verificacion_adversarial_3_capas
  input: [artifact, rubric]
  output: verdict.json
  tiempo: 10-60s
MA-REPAIR-5STEP:
  responsabilidad: pipeline_5_pasos_de_reparacion
  input: failure.json
  output: [repaired.json_o_escalate]
  tiempo: 30-120s
MA-RESEARCH-WEB:
  responsabilidad: crawling_+_extraccion
  input: [urls, depth]
  output: pages.jsonl
  tiempo: 30-300s
MA-RESEARCH-GH:
  responsabilidad: busqueda_en_github_via_api
  input: [query, lang, stars_min]
  output: repos.json
  tiempo: 10-60s
MA-EMIT-REPORT:
  responsabilidad: empaqueta_resultado_final
  input: state.json
  output: [report.md, manifest.json]
  tiempo: 1-5s

regla_diseno:
  single_responsibility: true
  max_loc_core: 200
  single_input_schema: true
  single_output_schema: true
  estado_efimero: true
  muerte_tras_emitir: true

modelo_ejecucion: spawn → run → emit_json → die
locaciones: localma_contenedorHF_space_remoto
invocacion: MCP_o_stdio
```

### Ejemplo Agente MA-VERIFY-3CAPAS

```python
SCHEMA_IN = "nct.verify.in.v1"
SCHEMA_OUT = "nct.verify.out.v1"

def run(artifact: dict, rubric: dict, k_samples: int = 3) -> dict:
    cap1 = adversarial_check(artifact, rubric)              # CODE_puro
    cap2 = cross_check(artifact, rubric)                     # CODE_puro
    cap3 = maker_checker(artifact, rubric)                   # CODE_puro

    if cap1["issues"] or cap2["issues"] or cap3["issues"]:
        cap1_llm = llm_adversarial_review(artifact, rubric) # LLM_10%
    else:
        cap1_llm = {"issues": []}

    issues = cap1["issues"] + cap2["issues"] + cap3["issues"] + cap1_llm["issues"]
    return {
        "decision": "pass" if not issues else "fail",
        "issues":   issues,
        "evidence": {"cap1": cap1, "cap2": cap2, "cap3": cap3, "cap1_llm": cap1_llm}
    }
```

### 3 Patrones Encadenamiento (Secuencial / DAG / Fractal)

```yaml
a_secuencial:
  patron: chain_linear
  caso: ETL_refactor
b_dag_paralelo:
  patron: chain_dag_con_parallel_groups
  caso: investigacion_+_diseno
c_fractal_anidado:
  patron: chain_fractal_con_depth_le_5
  caso: arquitectura_multi_modulo
```

### Pre-Análisis Información Semilla (5 pasos S1-S5)

```yaml
S1_indexar: 
  bloque: MA-INDEX
  input: [repo, state, RAG]
  output: seed_index.sqlite
S2_resumir:
  bloque: MA-SUMMARIZE
  output: seed_summary.json
S3_detectar_gaps:
  bloque: MA-GAP-DETECT
  output: seed_gaps.json
S4_proponer_preguntas:
  bloque: MA-QUESTION-GEN
  output: seed_questions.json
S5_enriquecer_seed:
  bloque: MA-RESEARCH-WEB_+_MA-RESEARCH-GH
  output: seed_enriched.json

metric_suficiencia:
  formula: 0.35_coverage_+_0.25_consistency_+_0.20_source_diversity_+_0.20_recency
  threshold: 0.85
  decision: si_score_ge_0.85_procede_sin_mas_investigacion_else_ciclo_investigacion
```

### Ciclo Investigación (5 rondas máximo)

```yaml
fases:
  R1_query: 
  R2_fetch: 
  R3_filter: 
  R4_eval: eval_score
  R5_refine: replan

min_rondas: 2
max_rondas: 5
tokens_por_ronda: le_50K
stop_if: evidence_sufficiency_score_ge_0.85
synth: MA-RAG-SYNTH

fuentes_priorizadas:
  web_general: [Wikipedia, OWASP, MDN, arXiv, blogs_oficiales]
  web_stack: documentacion_oficial_fastapi_react_etc
  github_repos_referencia: [XiaomiMiMo_MiMo-Code, sst_opencode, ...]
  github_awesome_lists: catalogos_curados
  github_issues_prs_discussions: problemas_conocidos
  github_releases_changelogs: breaking_changes
```

### Flota HuggingFace Spaces (10-20 workers)

```yaml
min_workers: 10
max_workers: 20
protocolo: MCP_via_mcp-hfspace
selection_rule: by_capability_+_SLA_+_cost
failover: circuit_breaker_+_backoff_exponential

composicion_flota_10_a_20:
  1_evalstate_FLUX.1-schnell: [generacion_imagenes, T4, 5-15s]
  2_hf-audio_whisper-large-v3-turbo: [STT, T4, 1-5s]
  3_microsoft_OmniParser: [vision_parsing_UI, A10G, 2-8s]
  4_Qwen2-VL-72B_smolagents_E2B: [VLM_reasoning, A100, 5-20s]
  5_gradio_llm-router: [LLM_generico, T4, 2-10s]
  6_nct_rag-search: [busqueda_vectorial, CPU, 1-3s]
  7_nct_code-runner: [ejecucion_codigo, CPU, 1-5s]
  8_nct_lint-fmt: [lint_+_format, CPU, 0.5-2s]
  9_nct_test-runner: [test_+_coverage, CPU, 5-30s]
  10_nct_security-scan: [sast_+_secrets, CPU, 10-60s]
  11_nct_dream: [consolidacion_memoria, CPU, 60-300s]
  12_nct_distill: [destilacion_memoria, CPU, 60-300s]
  13_a_20_reservados: [failover, mixto, variable]

selector_dinamico:
  criterion: feasibility_p95_ms_le_sla + min_cost

resiliencia:
  circuit_breaker_umbral: 3_fallos_consecutivos
  backoff_exponential: [base_2s, max_5min]
  failover_al_siguiente_space: misma_capability
  if_todos_fallan: degraded_elegant_paso_skipped_cadena_continua
```

### DSL Determinista 90% Código / 10% LLM

```yaml
presupuesto:
  90%_codigo_determinista:
    - parseo_validacion_transformacion
    - routing_verificacion_mecanica
    - formatting_retry_fallback
    - circuit_breaker_EROS_compression
    - checkpoint_restore_schema_validation
  10%_LLM:
    - MA-RAG-SYNTH
    - MA-ARCH-PLAN_parte_creativa
    - Max_Mode_decisiones_criticas
    - llm_adversarial_review_si_3_capas_mecanicas_fallan

contador_presupuesto:
  code_tokens: int
  llm_tokens: int
  llm_pct: float = llm_tokens/max(total, 1)
  enforce: assert_llm_pct_le_0.10
```

### Investigación RAG+Web+GH Integración por Tarea

```yaml
research:
  sources:
    web:
      - https://en.wikipedia.org/wiki/{topic}
      - https://owasp.org/...
      - https://docs.{stack}.dev/...
    github:
      - "{topic} awesome"
      - "{topic} framework stars:>1000"
      - "{topic} site:github.com"
    arxiv:
      - "{topic} long horizon agents"
  rounds: {min: 2, max: 5}
  early_stop: {metric: evidence_sufficiency_score, threshold: 0.85}
  synth: {agent: MA-RAG-SYNTH, max_tokens: 8000}
```

### 8 Propuestas Nuevas (PROP-13 a PROP-20)

```yaml
PROP-13_micro_agents_catalog: 12_micro_agentes_especializados single_responsibility max_loc_core_200 schema_io_unico
PROP-14_chain_patterns: 3_patrones_secuencial_DAG_fractal acyclic_dag max_depth_5
PROP-15_seed_pre_analysis: 5_pasos_pre_analisis reproducible seed_index_sqlite_gaps_questions
PROP-16_research_cycle: 2_a_5_rondas_stop_por_evidencia early_stop_threshold_0.85
PROP-17_hf_spaces_fleet: 10_a_20_workers_remotos_MCP min_workers_10 max_workers_20 circuit_breaker
PROP-18_dsl_90_10_budget: llm_pct_le_10 code_pct_ge_90 kpis_llm_pct_cost_per_cycle
PROP-19_mimo_integration: patrones_MiMo max_mode_goal_stop_writer_dream_distill_checkpoint
PROP-20_oss_backends_router: 15_backends_OSS router byok_or_proxy mcp_first_preferred
```

### Estructura de Archivos Addendum v200

```yaml
nct_coordinator/lop_v200/:
  __init__.py
  micro_agents/  # 12_agentes
    ma_code_gen.py
    ma_code_lint.py
    ma_code_test.py
    ma_rag_search.py
    ma_rag_synth.py
    ma_doc_write.py
    ma_arch_plan.py
    ma_verify_3capas.py
    ma_repair_5step.py
    ma_research_web.py
    ma_research_gh.py
    ma_emit_report.py
  pipelines/  # DSL_declarativos
    p_ma_chain.yaml
    ecommerce_microservice.yaml
    saas_tasks_api_v1.yaml
  backends/  # routers_a_OSS_clones
    opencode_adapter.py
    goose_adapter.py
    qwen_code_adapter.py
    mimo_code_adapter.py
    forge_code_adapter.py
  hf_spaces/  # cliente_de_la_flota
    fleet_client.py
    circuit_breaker.py
    selector.py
  dsl/  # declarativos
    step.yaml
    pipeline.yaml
    budget.py
  seed/pre_analysis.py
  seed/gap_detector.py
  research/cycle.py
  research/web_gh_sources.yaml
  proposals/PROP-13..20.yaml
  schemas/  # micro-agent, pipeline, hf-fleet
```

### Ingestion Directives para Mavis M3

```yaml
1_parsear_seccion_0_JSON_SUMMARY_como_contrato_entrada_mergear_con_padre_v100
2_construir_grafo_dependencias_entre_v100_y_v200
3_materializar_arbol_archivos_seccion_12
4_generar_PRs_orden:
  schemas → micro_agents → dsl → pipelines → backends → hf_spaces → seed → research → proposals
5_validar_llm_pct_le_0.10_en_cada_pipeline
6_validar_ningun_archivo_bajo_nct_coordinator_lop_v200_modifica_25_bloques_originales
7_versionar_este_modulo_como_200.0.0_semver
8_reportar_usuario_solo_resumen_ejecutivo_diagramas_KPIs_sin_preguntas_sin_comentarios
```

---

## DOC PATCH-AUDITORIA-GAPS-V5: 12 Gaps Únicos 5ta Pasada

### Gaps #69-#80

```yaml
GAP_69_Input_Governor_6_estados:
  descripcion: estados_RECIBIDO_ANALIZANDO_DEFINIENDO_COMPILANDO_AUDITANDO_APROBADO/VETADO/REPLANIFICAR/PREGUNTAR
  aplicar: MASTER-06_Input_Engine_agregar_Input_Governor
  accion_especial: si_PREGUNTAR_bloquea_hasta_respuesta_de_MAX

GAP_70_Executive_Board_5_oficiales:
  nombres_oficiales:
    1_Chief_Operations_Officer_COO: eficiencia_performance
    2_Chief_Financial_Officer_CFO: costos_presupuesto
    3_Chief_Quality_Officer_CQO: calidad_global_scores
    4_Chief_Risk_Officer_CRO: riesgos_fallos_alertas
    5_Chief_Learning_Officer_CLO: aprendizaje_evolucion
  aplicar: MASTER-09_Agentes_corregir_nombres_oficiales

GAP_71_23_destinos_especificos_oficiales:
  archivos_documentos_5: [md, pdf, html, docx, txt]
  codigo_5: [zip, github, gitlab, bitbucket, tarball]
  datos_3: [json, yaml, xml]
  comunicacion_3: [email, slack/discord, telegram]
  almacenamiento_3: [drive_mavis, s3_compatible, hf_dataset]
  apis_2: [rest_api, webhook]
  otros_2: [mcp_server, streaming_output]
  total: 23_destinos
  aplicar: MASTER-18_Patches_Extras_corregir_lista_oficial

GAP_72_Inteligencia_Colectiva_Emergente:
  patron: agente_tiene_conocimiento_local → comparte_en_bus_eventos → lee_compartido_otros
  emergencia: >suma_partes_soluciones_no_anticipadas
  usa: Bus_de_Eventos_INPUT-A
  complementa: Swarm
  aplicar: MASTER-09_Agentes_agregar

GAP_73_Output_Governor_8_estados:
  estados: [APROBAR, CORREGIR, REGENERAR, REPLANIFICAR, DIVIDIR, INVESTIGAR_MAS, PREGUNTAR_USUARIO, CANCELAR]
  controla: flujo_entre_16_componentes_Output_v6.1
  reporta: al_Orquestador_G5
  si_PREGUNTAR_USUARIO: bloquea_hasta_respuesta
  aplicar: MASTER-07_Output_Engine_expandir_Output_Governor

GAP_74_Closed_Feedback_Loop:
  fases:
    1_OUTPUT_PUBLICADO → 2_USO_REAL → 3_FEEDBACK_DIRECTO_INDIRECTO_OBSERVADO → 4_MEMORIA_OUTPUT_MEMORY → 5_APRENDIZAJE_META_LEARNING_SELF_IMPROVING → 6_REGLAS_ACTUALIZADAS_KB_CSA_BIS → 7_PROXIMO_OUTPUT_MEJOR
  importancia: "pegamento_entre_los_otros_9_patches_OUTPUT.cierra_ciclo_vida_completo"
  aplicar: MASTER-10_Input_Output_Loop_agregar_detalle

GAP_75_Pre_Mortem_detalle:
  pipeline:
    1_recibe_salida_candidata
    2_genera_10_escenarios_de_fracaso
    3_para_cada_escenario_probabilidad_impacto
    4_propone_mitigaciones
    5_si_riesgo_promedio_alto_no_publica
  metricas:
    - 10_escenarios_por_analisis
    - probabilidad_base: 15%_por_escenario
    - impacto_escala_1_a_10
    - mitigacion_automatica_por_escenario
  aplicar: MASTER-07_o_MASTER-10

GAP_76_Trust_Engine_umbrales:
  rango: 0_a_100
  por_elemento:
    agentes: tasa_exito_historica
    modelos: coherencia_respuestas
    datos: fuente_verificacion
    skills: resultados_aplicadas
    CSA_jueces: acuerdos_otros_jueces
  umbrales:
    - trust_lt_30: rechazar_o_pedir_segunda_opinion
    - trust_30_a_70: usar_con_cautela
    - trust_gt_70: usar_con_confianza
    - trust_gt_90: usar_sin_verificar
  integracion:
    usado_por_Model_Router_LOOP-G
    alimenta_Causal_Tracing_OUTPUT-PATCH-7
  aplicar: MASTER-08_LOOP_agregar_Trust_Engine_umbrales

GAP_77_Workflow_DAG_vs_Pipeline:
  pipeline: A→B→C→D→E_secuencial
  dag: A→B→D ↘C↗ ↘E paralelo_ramificado
  ventajas_DAG:
    - paralelismo_real
    - manejo_dependencias_complejas
    - no_bloqueos_lineales
    - reintentos_parciales
  reemplaza: concepto_pipeline_en_Loop_v6.0
  base_para: Runtime_Kernel_LOOP-B
  usado_por: 3_ciclos_paralelos_A/B/C
  aplicar: MASTER-08_LOOP

GAP_78_19_archivos_Python_especificos:
  path: /workspace/maxbry/g7/output_engine/v2/
  archivos_creados:
    - __init__.py: 1316_bytes
    - pre_mortem/pre_mortem_analyzer.py: 2436_bytes_70_lineas
    - auto_rollback/rollback_monitor.py: 2211_bytes_62_lineas
    - meta_learning/cross_release_analyzer.py: 1991_bytes_56_lineas
    - personalization/style_learner.py: 2165_bytes_64_lineas
    - multi_stakeholder/stakeholder_detector.py: 2913_bytes_79_lineas
    - causal_tracing/causal_chain_builder.py: 2812_bytes_75_lineas
    - marketplace/output_cataloger.py: 3010_bytes_84_lineas
    - self_improving/quality_analyzer.py: 3606_bytes_99_lineas
    - production_monitoring/usage_tracker.py: 3052_bytes_88_lineas
  total: 19_archivos_726_lineas
  aplicar: MASTER-23_Implementacion

GAP_79_9_propuestas_aplicadas_+_1_rechazada:
  1_Pre_Mortem_Analysis: ✅_APLICADO
  2_Output_Sandbox: ❌_RECHAZADO_POR_MAX
  3_Auto_Rollback_Inteligente: ✅_APLICADO
  4_Meta_Learning_entre_Releases: ✅_APLICADO
  5_Output_Personalization: ✅_APLICADO
  6_Multi_Stakeholder_Output: ✅_APLICADO
  7_Causal_Output_Tracing: ✅_APLICADO
  8_Output_Marketplace_Interno: ✅_APLICADO
  9_Self_Improving_Output_Quality: ✅_APLICADO
  10_Production_Monitoring: ✅_APLICADO
  aplicar: MASTER-18_Patches_Extras

GAP_80_Constitucion_maestra:
  path: /workspace/nct-proyecto/CONSTITUCION-ORQUESTADOR.md
  lineas: 1276
  capas_totales: ~80
  principios: 39
  agentes_paralelos: 200+
  HF_Spaces: 7
  aplicar: MASTER-03_Constitucion_Completa
```

### Resumen Total 80 Gaps

```yaml
1er_patch_V1: 20
2do_patch_V2: 13
3er_patch_V3: 17
4to_patch_V4: 18
5to_patch_V5: 12_unicos
total: 80_gaps_identificados
```

## DOC PATCH-AUDITORIA-GAPS-V3: 17 Gaps 3ra Pasada

```yaml
GAP_34_Estructura_completa_336_archivos:
  00_raiz: 6_archivos_metadata
  01_bootstrap: 5_archivos_instalacion
  02_core: 7_archivos_nucleo
  03_input_engine: 28_archivos_P28-29_+_17_mejoras
  04_sid: 10_archivos_P27
  05_sub_orquestadores: 26_archivos_P19_20_SO_+_SO-ARQ
  06_csa: 17_archivos_P26
  07_output_engine: 25_archivos_P31+P34
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
  total: 336_archivos_python_~40800_lineas_python_~53400_lineas_totales

GAP_35_Calculos_recursos:
  lineas_codigo_estimadas:
    python_puro: ~40800
    yaml_configs: ~2500
    json_schemas: ~1800
    shell_scripts: ~300
    markdown_docs: ~8000
    total: ~53400_lineas
  tamaño_disco:
    codigo_fuente: ~2.0MB
    configs_schemas: ~0.3MB
    docs: ~12MB
    total: ~14MB
  memoria_ejecucion:
    python_runtime: ~130MB
    litellm_gateway: ~50MB
    dramatiq: ~30MB
    fastapi: ~20MB
    chromadb: ~80MB
    bge_small: ~100MB
    pybreaker: ~10MB
    redis_client: ~20MB
    telegram_bot: ~30MB
    mcp_server: ~30MB
    total_runtime: ~500MB_RAM
  con_modelos_G6: ~13GB_RAM
  recursos_totales:
    "7_HF_Spaces_x_16GB_eq_112GB"
    "usados: ~13.5GB"
    "margen_libre: 87%"

GAP_36_OOS_14_componentes:
  componentes:
    - Output_Planner
    - Output_Compiler_AST_salida
    - Output_Graph
    - Semantic_Chunk_Engine  # no_corta_por_tokens_calcula_dependencias
    - Adaptive_Chunk_Size  # tamaño_dinamico
    - Predictive_Output_Planner  # calcula_salida_estimada_antes
    - Auto_Format_Negotiation  # recomienda_formato_inteligente
    - Intelligent_Packaging  # paquetes_por_tipo
    - Multi_Delivery_Pipeline  # 15+_destinos_en_paralelo
    - Intelligent_Compression  # optimiza_antes_de_comprimir
    - Smart_Version_Control  # v1.0.0_v1.0.1
    - Incremental_Publishing
    - Intelligent_Resume
    - Output_Verification
  plus:
    - Universal_Output_Model
    - Delivery_Policy_Engine

GAP_37_15+_destinos_OOS:
  misma_salida_a_15_destinos_simultaneos:
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
  todo_en_paralelo

GAP_38_20_Sub_Orquestadores_SO_01_a_SO_20:
  - SO-01_analista_objetivos
  - SO-02_organizador
  - SO-03_planificador
  - SO-04_validador_plan
  - SO-05_investigador
  - SO-06_replanificador
  - SO-07_mapa_mental
  - SO-08_clasificador
  - SO-09_divisor_tareas
  - SO-10_disenador_pasos
  - SO-11_constructor_bucles
  - SO-12_gestor_dependencias
  - SO-13_calculador_recursos
  - SO-14_asignador
  - SO-15_creador_loops
  - SO-16_validador_calidad
  - SO-17_verificador_cruzado
  - SO-18_auditor_trazabilidad
  - SO-19_reportador
  - SO-20_memoria_sistema
  plus: SO-ARQ_arquitectura

GAP_39_6_Colmenas:
  - colmena_programacion: sa_diseno_ma_01_30
  - colmena_investigacion: github_hf_web_youtube_mcp
  - colmena_memoria: chromadb_bge_embedder_trazabilidad
  - colmena_seguridad: sheriff_sentinel_auditor
  - colmena_documentacion: escritor_generador_validador
  - colmena_testing: runner_coverage_benchmark

GAP_40_SA-DISENO:  # Sub-Agente-Diseñador-P23
GAP_41_Kimi_K2_detalles:
  vendor: Moonshot_AI
  HF: moonshotai/Kimi-K2.7-Code
  GitHub: github.com/MoonshotAI/Kimi-K2.5
  funcion: agente_de_code_del_orquestador
  provider: OpenCLAW_nativo_+_compatible_Claude_Code_via_API
  endpoint: Groq_provider_o_NVIDIA_NIM
  arquitectura: MoE_1T_params_32B_activados
  versiones: [K2.5, K2.7-Code, K2_Thinking]

GAP_42_10_instrucciones_pendientes_MAX:
  1: confirmacion_archivo_docx_con_lo_aprobado
  2: activar_M2.7_para_crear_G5_con_HF_+_Telegram_+_MCP_server
  3: nombre_exacto_de_HTM_y_YUAN_no_encontrados_en_HF
  4: autorizacion_para_finalizar_documentos_y_proceder_con_instalacion
  5: decision_sobre_visibilidad_de_repos_publico/privado
  6: decision_sobre_comunicacion_Telegram_bot_token
  7: datos_acceso_GitHub_GH_OWNER_PAT
  8: datos_acceso_HuggingFace_HF_USERNAME_token
  9: 16_API_keys_confirmadas_con_labels
  10: Turso_DB_credentials_opcional

GAP_43_Herramientas_aprobadas:
  HuggingFace:
    ZeroGPU: infraestructura_COMPARTIDA_no_nos_afecta_usamos_API
    CPU-Basic_Spaces: 16GB_RAM_cada_uno_aislados_por_contenedor
    GitHub_PAT: conexion_via_git_con_GH_PAT_como_secret
    cada_HF_Space: propia_URL_fija_en_produccion
  MCP_Model_Context_Protocol:
    - github.com/modelcontextprotocol/servers  # 2700+_servers
    - github.com/shreyaskarnik/huggingface-mcp-server
    - G8_MCP_server_expone_tools
    - G7_son_MCP_clients
  RAG_tools:
    - context7  # contexto_10M_tokens_real
    - ChromaDB  # embeddings
    - bge-small-en-v1.5  # modelo_embeddings_24MB_HF
    - LightRAG: github.com/HKUDS/LightRAG
    - Haystack: github.com/deepset-ai/haystack
  Adaptadores_cuantizacion:
    - Unsloth_Dynamic_2.0: github.com/unslothai/unsloth
    - bartowski: github.com/bartowski  # mejor_quantizacion_community
    - GGUF_format
    - llama-cpp-python: github.com/abetlen/llama-cpp-python
  Frameworks:
    - pydantic  # validacion_schemas
    - PEFT  # adapters
    - LoRA  # fine-tuning

GAP_44_Merge_Rule_snapshot_branch:
  auto_merge_when: G4_AUDIT_approved_AND_G5_CONSENSO_approved_AND_tests_pass
  if_any_fails: PR_open_+_M3_chat_notified_+_MAX_decides
  snapshot_branch: snapshot-vX.Y.Z
  versioning: semver

GAP_45_Repair_v1.0_5_pasos_detalle:
  paso_1: Retry_simple_3_intentos
  paso_2: Context_Compression_L1/L2
  paso_3: Fallback_Model/Agent
  paso_4: Restore_Checkpoint
  paso_5: Escalate_Coordinator_decide

GAP_46_Patch_log_historico:
  v1.0.0 → v1.0.5: secciones_1_a_30_originales
  v1.0.6_2026-06-28: patch_031_9_modelos_GGUF_detallados
  v1.0.7_2026-06-28: patch_032_10_agentes_del_consejo
  v1.0.8_2026-06-28: patch_033_sistema_de_Skills
  v1.0.9_2026-06-28: patch_034_Kimi_K2_como_agente
  v1.0.10_2026-06-28: patch_035_investigacion_multi_fuente

GAP_47_Adaptive_Chunk_Size:
  tamaño_dinamico_por_parte:
    parte_1: 400_lineas
    parte_2: 1500_lineas
    parte_3: 650_lineas
  no_existe_tamaño_fijo

GAP_48_Auto_Format_Negotiation:
  pregunta_inteligente_no_simple:
    "He detectado que la salida contiene:
      ✔ Código
      ✔ Diagramas
      ✔ Documentación
      ✔ Configuración
      ✔ Tests
    Recomendación:
      Artifact + ZIP + Repositorio Git
    ¿Deseas usar esta configuración?
      SÍ / MODIFICAR"

GAP_49_Agentes_Colmena_Investigacion_5:
  - github_search.py  # REST+GraphQL
  - hf_search.py  # HF_API
  - web_search.py  # DuckDuckGo+scraper
  - youtube_search.py  # YouTube_Data_API_v3_transcripts
  - mcp_search.py  # MCP_servers

GAP_50_Investigacion_multi_fuente:
  agente_github: API_github.com_REST_GraphQL_busquedas_repos_codigo_issues_stars_commits
  agente_huggingface: API_huggingface.co_REST_busquedas_modelos_datasets_spaces
  agente_web: API_duckduckgo_+_custom_scraper_busquedas_docs_oficiales_awesome_lists_papers_blogs
  agente_youtube: API_youtube-data-api_v3_busquedas_videos_transcripts_canales_verificados_uso_tutoriales
  agente_mcp: API_github.com/modelcontextprotocol/servers_busquedas_servers_tools_registries
```

---

## DOC PATCH-AUDITORIA-GAPS-V4: 18 Gaps 4ta Pasada

```yaml
GAP_51_M2.7_flujo_simplificado_5_pasos:
  1_RECIBIR:
    - leer_TASK_json
    - verificar_schema
    - output: task_recibida_ok
  2_VERIFICAR:
    - chequear_dependencias
    - chequear_keys_necesarias
    - chequear_permisos
    - output: dependencias_ok
  3_EJECUTAR:
    - ejecutar_la_tarea
    - output: ejecucion_resultado
  4_VALIDAR:
    - tests_pasan
    - output_compilado
    - secrets_detectados_no
    - output: validacion_ok
  5_REPORTAR:
    - escribir_resultado_STATE_json
    - escribir_HISTORY_json_acumulativo
    - notificar_M3_chat
    - output: reporte_enviado
  si_falla_cualquier_paso:
    - escribir_RECOVERY_JSON
    - rollback_si_necesario
    - escalar_M3_chat_si_retry_gt_2

GAP_52_Division_tareas_grandes:
  regla: si_tarea_gt_5_subtareas → dividir_en_bloques
  bloque_independiente:
    - checkpoint_separado
    - recovery_independiente
  patron: BLOQUE_1_checkpoint_1_output_1 → BLOQUE_2_checkpoint_2_output_2 → BLOQUE_3_checkpoint_3_output_3
  cada_bloque_incluye:
    - input_literal_preservado
    - 5_GOALS_fijados
    - 12_PASOS_ejecutados
    - CHECKPOINT_JSON_escrito
    - REFUTACION_pasada
    - VALIDACION_pasada
    - OUTPUT_entregado
    - RECOVERY_JSON_listo_si_falla

GAP_53_10_modulos_MAXBRY:
  M1_Bootstrap: instalador_+_actualizador_+_lanzador
  M2_Nucleo_Orquestador: planificador_+_scheduler_+_motor_decisiones
  M3_Gestor_Memoria: ChromaDB_+_bge-small_+_embeddings
  M4_Scheduler: Dramatiq_+_Redis_+_colas_paralelas
  M5_Gestor_Agentes: registry_+_colmena_+_distribucion
  M6_Gestor_Skills: catalogo_+_generador_+_versionado
  M7_Gestor_Modelos_IA: API_keys_+_profiles_+_circuit_breaker
  M8_Sistema_Seguridad: cifrado_+_auth_+_licencias
  M9_Sistema_Actualizacion: versiones_+_diffs_+_rollback
  M10_Sistema_Monitorizacion: logs_+_metricas_+_alertas_+_dashboards
  cada_modulo:
    - carpeta_independiente
    - API_publica_clara
    - actualizable_sin_reinstalar
    - tests_propios
    - version_propia
    - metadata_versionada

GAP_54_Sistema_seguridad_6_capas:
  capa_1_CIFRADO_COMUNICACION: HTTPS_TLS
  capa_2_AUTENTICACION: API_keys_con_tokens_1h_OAuth2_opcional
  capa_3_FIRMAS_DIGITALES: cada_solicitud_firmada_criptograficamente
  capa_4_RATE_LIMITING: 100_req/min_1000_req/h
  capa_5_LICENCIAS: cada_instalacion_unica_servidor_valida_cada_arranque
  capa_6_RESPUESTAS_MINIMAS: API_solo_devuelve_lo_necesario_nunca_paths_internos

GAP_55_Nucleo_via_API_cliente_ligero:
  cliente_M3: local_5_MB  # lo_que_usuario_tiene
  API_Orquestador: servidor  # lo_que_NO_se_descarga
    - planificador
    - memoria_global
    - scheduler
    - motor_decisiones
    - agentes
    - modelos_IA
  ventajas:
    - usuario_NO_recibe_codigo_nucleo
    - NO_puede_copiar_planificador
    - actualizaciones_sin_usuario_reinstale
    - puedes_revocar_accesos
    - codigo_importante_NUNCA_sale_del_servidor

GAP_56_P8_Bootstrap_instalacion_autonoma:
  responsabilidades:
    - detectar_OS_Linux/Mac/Windows
    - detectar_arquitectura_x86_64/arm64
    - verificar_recursos_CPU_RAM_disco_red
    - comprobar_dependencias_necesarias
    - instalar_automaticamente
    - crear_estructura_directorios
    - inicializar_base_datos
    - generar_configuraciones_iniciales
    - generar_claves_criptograficas
    - descargar_solo_componentes_necesarios
    - iniciar_orquestador
  caracteristicas:
    - tamaño_maximo: 5_MB
    - NO_contiene_logica_orquestador
    - solo_instalador_+_actualizador_+_lanzador
    - descarga_componentes_bajo_demanda
    - verificacion_criptografica_integridad

GAP_57_8_Principios_Rectores_Sistema_Razonamiento:
  1_INPUT_SAGRADO: input_NUNCA_se_modifica_resume_parafrasea_reinterpreta
  2_DSL_DAG_NUNCA_PROMPT_LIBRE: salida_siempre_JSON_estructurado
  3_DETERMINISMO: mismo_input_+_config_+_LLM_=_misma_forma_de_razonamiento
  4_UNIVERSALIDAD: cualquier_LLM_puede_usarlo
  5_EXTERNALIDAD: vive_en_reasoning_system_no_en_orquestador
  6_EDITABILIDAD_POR_ARCHIVOS: cambiar_goal/step_=_editar_archivo_no_codigo
  7_AUDITABILIDAD: cada_ejecucion_produce_log_auditable
  8_AISLAMIENTO: sistema_no_contamina_al_orquestador_ni_al_LLM

GAP_58_INPUT_BLOCK_estructura_JSON:
  input_block:
    raw: "<<input_EXACTO_del_usuario_sin_tocar>>"
    received_at: "<<timestamp_ISO_8601>>"
    source: "<<nombre_del_llamador>>"
    checks:
      preserve_verbatim: true
      no_summarize: true
      no_paraphrase: true
      no_modify: true
    status: ACCEPTED|REJECTED

GAP_59_7_Prohibiciones_explicitas_INPUT_BLOCK:
  1_resumir_el_input:  # usuario_pidio_algo_especifico_no_resumen
  2_parafrasear_el_input:  # cambia_matiz_semantico
  3_mejorar_la_redaccion_del_input:  # usuario_escribio_como_quiso
  4_agregar_contexto_que_no_estaba:  # contamina_intencion_original
  5_quitar_partes_irrelevantes:  # LLM_decidira_que_es_relevante
  6_traducir_el_input:  # cambia_idioma_cambia_semantica
  7_reordenar_las_ideas_del_input:  # estructura_sintactica_porta_significado

GAP_60_12_pasos_standard_con_prompts_especificos:
  01_literal_read:
    prompt: "INSTRUCCION_SAGRADA_NO_INTERPRETAR_NO_RESUMIR_NO_MODIFICAR"
    output: {input_accepted: true, raw_acknowledged: ...}
    conexion: entrada_a_02_think_si_falla_a_REJECTED
  02_think:
    prompt: "Considerando_los_goals_y_el_input_verbatim_que_estas_entendiendo"
    output: {thinking: [obs1, obs2, obs3]}
  03_plan:
    prompt: "Genera_un_plan_de_3_a_7_pasos_para_cumplir_goal_primary"
    output: {plan: [{step, action, expected_output}]}
  04_decompose:
    prompt: "Para_cada_paso_del_plan_identifica_las_subtareas_atomicas"
    output: {decomposition: [{plan_step, atomic_tasks}]}
  05_hypotheses:
    prompt: "Para_cada_atomic_task_propon_2_a_4_hipotesis_de_solucion_alternativas"
    output: {hypotheses: [{task_id, alternatives}]}
  06_swarm:
    prompt: "Para_cada_hipotesis_evalua_esfuerzo_riesgo_alineamiento"
    output: {swarm_results: [{h_id, effort, ...}]}
  07_critic:
    prompt: "Como_critico_que_falla_en_cada_hipotesis"
    output: {critiques: [{h_id, weakness, severity}]}
  08_simulate:
    prompt: "Simula_paso_a_paso_la_ejecucion_de_la_hipotesis_ganadora"
    output: {simulation: [{phase, result, issues}]}
  09_validate:
    prompt: "La_simulacion_cumple_goal_success_respeta_goal_restriction"
    output: {validation: {meets_success, respects_restriction}}
  10_consensus:
    prompt: "Considerando_thinker_critic_simulator_validator_cual_es_la_decision"
    output: {consensus: {decision, confidence, votes}}
  11_report:
    prompt: "Genera_el_reporte_final_en_formato_DSL"
    output: {report: <DSL_final>}
  12_audit:
    prompt: "Auditoria_se_respeto_input_sagrado_se_ejecutaron_los_12_pasos"
    output: {audit: {input_respected, verdict, notes}}

GAP_61_M3_formato_salida:
  antes_de_cada_salida:
    - system_prompt_mythos_ejecutado
    - goals_lista
    - pasos_completados_1_a_12
    - checkpoints_uuid
    - refutacion_ok_fail
    - validacion_ok_fail
  despues_de_cada_salida:
    - self_audit_ok_fail
    - input_preserved_true
    - output_validated_true

GAP_62_M2.7_log_ejecucion:
  log_en_STATE_json:
    - system_prompt_mythos_executed
    - paso_actual_1_a_5
    - checkpoint_id_uuid

GAP_63_Refutacion_5_preguntas_obligatorias:
  obligatorias_antes_output_final:
    - que_asumi_sin_verificar
    - que_puede_romper_esta_salida
    - que_restriccion_viole
    - que_informacion_invente
    - que_dependencias_no_chequee
  si_alguna_problematica:
    - volver_al_paso_1
    - NO_presentar_output_refutado

GAP_64_Estructura_sistema_razonamiento:
  reasoning_system/:
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

GAP_65_Validacion_obligatoria_checks:
  obligatorios_antes_output_final:
    - input_preservado_verbatim
    - output_no_resume_input
    - output_no_parafrasea_input
    - output_responde_5_GOALS
    - output_cumple_restriccion_inegociable
    - checkpoints_escritos
    - refutacion_pasada
    - consensus_aplicado_si_aplica
  si_alguna_falla: REJECTED_+_recovery

GAP_66_Protocolo_recuperacion:
  si_tarea_falla:
    1_escribir_RECOVERY_JSON_inmediatamente
    2_identificar_ultimo_CHECKPOINT_valido
    3_si_retry_count_lt_2: rollback_checkpoint_retry
    4_si_retry_count_ge_2: escalar_a_M3_chat
    5_M3_chat_decide_mas_retries_redesign_o_cancelar
  NUNCA:
    - inventar_output_cuando_falla
    - saltarse_pasos_para_avanzar
    - ignorar_violaciones
    - borrar_checkpoints_validos

GAP_67_Uso_memoria_M3_y_M2.7:
  M3_chat_MEMORIA:
    - memory_topic_append_despues_cada_sesion_importante
    - leer_memory_topic_read_al_inicio_cada_sesion_nueva
    - BORRADOR-LISTA-APROBADOS_md_fuente_de_verdad_visible
  M2.7_MEMORIA:
    - leer_BORRADOR-LISTA-APROBADOS_md_al_iniciar
    - STATE_json_estado_actual
    - HISTORY_json_historico_completo_nunca_borrar
  BORRADOR-LISTA-APROBADOS_md:
    - actualizado_con_CADA_cambio_aprobado
    - actualizado_con_CADA_nueva_propuesta
    - actualizado_con_CADA_tarea_completada
    - fuente_de_verdad_para_todo

GAP_68_Integracion_system_prompt_mythos_+_razonamiento_externo:
  diferencia:
    system_prompt_mythos: reglas_y_procedimiento_visible
    reasoning_system: libreria_Python_con_funciones
  ambos_deben_usarse:
    M3_lee_system_prompt_mythos_al_inicio
    M3_usa_reasoning_system_reason_para_tareas_complejas
    M2.7_lee_system_prompt_mythos_al_inicio
    M2.7_usa_reasoning_system_reason_si_necesita_razonar
  integracion:
    system_prompt_mythos_=_capa_comportamiento
    reasoning_system_=_capa_ejecucion
    juntos_=_sistema_completo
```

### Resumen Total 80 Gaps Acumulados

```yaml
patch_V1: 20_gaps
patch_V2: 13_gaps
patch_V3: 17_gaps
patch_V4: 18_gaps
patch_V5: 12_unicos
total: 80_gaps_identificados
```

---

## DOC PATCH-AUDITORIA-GAPS (V1): 20 Gaps Originales — Auditoría 55X

### GAP #1 — INCONSISTENCIA MAYOR: 6 GRUPOS vs 8 GRUPOS

```yaml
criticidad: ALTA
problema:
  - 01-FASE-0-FROZEN_md: define_8_GRUPOS_G1_a_G8
  - ORQUESTADOR-G5-DISENO_md: tambien_8_GRUPOS
  - CONSTITUCION-ORQUESTADOR_md_y_STATE-AUDIT_md: 6_GRUPOS
  - los_29_Master_Documents: 6_GRUPOS

version_A_8_grupos_FASE_0_FROZEN:
  G1_INFRA: runtime_scheduler_sheriff_sentinel_watcher
  G2_CORE: cerebro_cognitivo_planner_DSL_DAG_memoria
  G3_UI: interfaces_frontend
  G4_AUDIT: fichas_documentacion_LightRAG_Haystack
  G5_CONSENSO: SKYNER_validacion_arbitraje
  G6_BUILD: assemble_compile_test_package_publish
  G7_ASISTENTES: 9_modelos_GGUF_locales_staff
  G8_ORQUESTADOR: router_Telegram_bridge_MCP_server_consensus_orchestrator

version_B_6_grupos_MASTER_DOCS:
  G1_INFRA: HF_Spaces_GitHub_Docker
  G2_CORE: BIS_SID_Input_Output_Engine
  G3_UI: Telegram_API_REST_Dashboard
  G4_AUDIT: CSA
  G5_ORQUESTADOR_CONSENSO_mismo_grupo: MAXBRY_SUPER_TEAM
  G6_ASISTENTES: 9_modelos_GGUF_+_16_API_keys

recomendacion: CONSERVAR_6_GRUPOS_y_tratar_G7-G8_como_sub_grupos_dentro_G5+G6
```

### GAP #2 — ACTIVATION COMMANDS (Telegram)

```yaml
ORQUESTADOR: solo_G8_responde_version_8_grupos_o_G5_version_6
ASISTENTE: solo_G7_responde_o_G6
ASISTENTE_ORQUESTADOR: ambos_responden_parallel
ORQUESTADOR_CONSENSO: G8_o_G5_pregunta_5_o_12_modelos
```

### GAP #3 — 13 CRITERIOS SKILLS (Versión OFICIAL)

```yaml
lista_correcta_ORQUESTADOR-G5-DISENO:
  01_calidad_del_codigo: lint_type_check_complexity
  02_licencia: compatible_MIT_Apache_2.0_BSD
  03_mantenimiento_reciente: ultimo_commit_lt_6_meses
  04_estrellas_github: senal_no_criterio_unico
  05_issues_abiertos_vs_cerrados: ratio
  06_uso_por_comunidad: descargas_HF_cites
  07_compatibilidad_con_arquitectura_NCT
  08_dependencias: minimas_y_mantenidas
  09_seguridad: sin_CVEs_conocidos
  10_rendimiento: latencia_throughput
  11_tamano: cabe_en_16GB_RAM
  12_facilidad_de_integracion: API_estable
  13_pruebas_propias: tests_incluidos
```

### GAP #4 — SHERIFF + SENTINEL + WATCHER + JUDGE + VALIDATOR + ORCHESTRATOR

```yaml
SHERIFF_v1.0:
  ID: sheriff
  grupo: G1_INFRA
  tipo: deterministic_no_LLM
  frequency: every_5min
  checks: [process_alive, progress_moved, errors, timeout, rate_limit, api_fail, commit_fail, dependency_broken]
  classify:
    INFO: log
    WARNING: BLACKBOARD
    ERROR: retry_+_BLACKBOARD
    CRITICAL: G5_+_MAX
  blocks:
    no_events_30min
    no_progress_30min
    no_commit_30min
    no_state_write_15min
    no_heartbeat_5min
  input_block_violation: detected_if_input_ne_output_semantically
  loops_protection: [retry_max_2, consensus_max_2, audit_max_2, repair_max_2]

SENTINEL_v1.0:
  ID: sentinel
  grupo: G1_INFRA
  tipo: deterministic
  frequency: 1min_resources_/_5min_costs_security
  monitors: [tokens_per_min, rate_limits, latency, HF_spaces_uptime, GH_API_remaining, daily_cost, security_commits]
  supervised_by: sheriff_heartbeat_5min_if_silent_10min_a_GH_Action_restart

WATCHER_v1.0:
  ID: watcher
  grupo: G1_INFRA
  tipo: deterministic
  frequency: 60s
  monitors: [group_heartbeat_window_5min, HF_space_state, GH_actions_runs, last_STATE_write]
  supervised_by: sentinel

JUDGE_v1.0_SKYNER_ALGORITHM:
  ID: judge
  grupo: SKYNER
  via: MiniMax-M3-via-NVIDIA-NIM
  formula: confidence = 0.40_semantic_match + 0.30_consistency_BLACKBOARD + 0.20_model_self_confidence + 0.10_historical_accuracy
  thresholds:
    ge_0.85: APPROVED
    0.60_a_0.85: RE_INVOKE_max_2
    lt_0.60: REJECTED
  veto_conditions:
    - contradicts_BLACKBOARD
    - violates_rules
    - security_implication
  output_fields: [consensus_status, confidence, reason, veto_reason, requires_human]

VALIDATOR_v1.0:
  validates: [compiles, tests_pass, linting, type_check, docs, STATE_schema, no_secrets, no_breaking_changes]
  rejects_if: any_check_fails_or_STATE_invalid_or_secret_detected
  max_iterations: 2

ORCHESTRATOR_v1.0:
  inputs: [TASK_json, BLACKBOARD_json]
  priorities: Urgente_gt_Alta_gt_Media_gt_Baja_fifo_within_level
  recovery:
    silent_5min: check_heartbeat
    silent_10min: sheriff_alert
    silent_30min: reassign
```

### GAP #5 — CONSENSUS 5 vs CONSENSUS 12 (Modelos Específicos)

```yaml
consensus_5_rapido:
  - HRM-Text-1B
  - Qwen2.5-Coder-1.5B
  - Granite-Code-3B
  - Liquid-LFM2.5-1.2B-Thinking
  - Gemma-4-E2B

consensus_12_completo:
  - 4_NVIDIA_NIM_keys
  - 6_Cerebras_keys
  - GPT-OSS-20B_local
  - OpenCodeReasoning-Nemotron-7B
  - DeepHermes-3-3B
  - SmolLM3-3B
```

### GAP #6 — 10 LOOPS CONTRACTS

```yaml
tabla_loops:
  Planning:
    inicia: M3_chat
    termina_cuando: DAG_armado
    max: 3
    escala_a: MAX
  Execution:
    inicia: scheduler
    termina_cuando: done_true_or_failed
    max: "1+2"
    escala_a: retry_a_G5
  Review:
    inicia: scheduler
    termina_cuando: approved_or_rejected
    max: 2
    escala_a: G5
  Critic:
    inicia: AUTO_BOTH
    termina_cuando: acuerdo_entre_par
    max: 3
    escala_a: SKYNER
  Repair:
    inicia: G4_or_scheduler
    termina_cuando: errores_fixed
    max: 2
    escala_a: G5
  Validation:
    inicia: REQUEST_REVIEW
    termina_cuando: consensus_status_emit
    max: 2
    escala_a: MAX
  Consensus:
    inicia: any_group
    termina_cuando: decision_emitida
    max: 3
    escala_a: MAX
  Build:
    inicia: scheduler
    termina_cuando: release_publicado
    max: 2
    escala_a: MAX
  Release:
    inicia: G6
    termina_cuando: tag_+_ZIP_+_informe
    max: 1
    escala_a: MAX
  Monitoring:
    inicia: cron_5min
    termina_cuando: incidente_cerrado
    max: infinito
    escala_a: MAX
```

### GAP #7 — MEMORY PROTOCOL v1 (3 Tiers)

```yaml
FUENTE_DE_VERDAD: GitHub_nct-consensus-log
INDICE_RAPIDO: ChromaDB_en_HF_MEMORIA
CONTEXTO_10M: context7_retrieval_por_proyecto
JERARQUIA:
  tier_1: ultimos_32K_tokens_texto_completo
  tier_2: 32K_a_2M_chunks_ChromaDB
  tier_3: 2M_a_10M_resumenes_retrieval_on_demand
EMBEDDINGS: bge-small-en-v1.5_24MB_HF
CHAT_MEMORY: M3_chat_guarda_en_memory_topic_append_despues_de_cada_sesion
```

### GAP #8 — STORAGE STRATEGY

```yaml
GitHub_versionado_+_auditoria:
  - fichas
  - code
  - artifacts
  - master_project
  - Indice
  - TEAMS_MAP_md

SandboxDB_alta_frecuencia:
  - STATE
  - BLACKBOARD
  - EVENTS
  - INBOX
  - OUTBOX
  - Cola
  - Heartbeats
  - Cache
  - Logs

export_a_GitHub_solo_en:
  - cierre_de_tarea
  - error
  - auditoria
```

### GAP #9 — MERGE RULE + PRIORIDADES + KEEPALIVE

```yaml
MERGE_RULE:
  auto_merge_when: G4_AUDIT_approved_AND_G5_CONSENSO_approved_AND_tests_pass
  if_any_fails: PR_open_+_M3_chat_notified_+_MAX_decides

PRIORIDADES:
  Urgente: [SLA_60min, retries_3]
  Alta:    [SLA_240min, retries_2]
  Media:   [SLA_1440min, retries_2]
  Baja:    [SLA_4320min, retries_1]

KEEPALIVE:
  GitHub_Actions_cron_20min: /health_per_space
  alert_on: 2_consecutive_failures
```

### GAP #10 — MiniMax M3 Atributos Específicos

```yaml
atributo: valor
modelo: MiniMax-M3_MiniMaxAI/MiniMax-M3_en_HF
endpoint: 1x_NVIDIA_NIM_dedicado_slot_reservado
api_style: OpenAI-compatible_/v1/chat/completions
context_window: 1048576_tokens_1M
throughput: ge_80_tok/s_sostenidos
latencia_p50: le_350ms_primer_token
latencia_p95: le_900ms_primer_token
roles_permitidos: [FASE_4_Ejecucion, FASE_6_Verificacion_capa_3]
system_prompt: orquestador/system_prompt_json
politica_retries: 3_reintentos_backoff_1s_3s_7s_fallback_Kimi_K2
logging: request_id_UUIDv7_en_reportes_llm_calls
```

### GAP #11 — DSL reasoning_chain.py (Enforced)

```python
@enforced  # decorador obligatorio — no se puede saltar
def reasoning_chain(task_input):
    # STEP 1 — LITERAL READ
    raw_input = task_input  # texto sagrado, no se toca
    assert no_modification(raw_input, task_input)

    # STEP 2 — THINK (entender qué pide sin reescribir)
    understood = think(raw_input)
    assert understood.refers_to_input(raw_input)

    # STEP 3 — PLAN (construir DAG)
    dag = plan(understood)
    assert dag.is_valid()

    # STEP 4 — EXECUTE
    result = execute(dag)

    # STEP 5 — VALIDATE
    assert result.makes_sense(raw_input)
    assert result.did_not_summarize(raw_input)

    # STEP 6 — REPORT
    report(result)
```

```yaml
INPUT_BLOCK_RULE:
  condicion_1: SI_input_ne_output_en_cualquier_token_a_REJECTED
  condicion_2: SI_modelo_hace_paraphrasis_o_sintesis_o_reinterpretacion_a_VIOLATION
  efecto: violation_eq_tarea_se_reinicia_desde_literal_input_+_Sheriff_registra
```

### GAP #12 — FASE 0.5 Confirmation Ejemplo Completo

```yaml
escenario:
  user_input: "crea el panel de crazy wall"
  g5_respuesta: "Detecte que puede ir a:
    1. nct-fase0
    2. interfaz-fusionada
    3. crazy-wall
    ¿A cuales va? (1, 2, 3, todos, ninguno)"
  user_respuesta_3: solo_crazy-wall
  user_respuesta_los_3: a_los_3_proyectos
```

### GAP #13 — SID Pre-Procesador (10 Pasos) + Panel Inteligente

```yaml
pre_procesador_10_pasos:
  1: comprension_del_objetivo
  2: extraccion_de_requisitos
  3: deteccion_de_ambiguedades
  4: deteccion_de_contradicciones
  5: deteccion_de_informacion_faltante
  6: recuperacion_de_contexto
  7: consulta_de_memoria
  8: consulta_de_documentacion
  9: generacion_de_hipotesis
  10: calculo_de_confianza
  if_confianza_ge_umbral: continua_automaticamente
  if_confianza_lt_umbral: abre_Panel_Inteligente_de_Definicion

panel_inteligente_ejemplo:
  falta_definir: base_de_datos
  impacto: arquitectura_rendimiento_costes
  opciones: [PostgreSQL_recomendada, MySQL, SQLite, Otro]
  default_si_no_elige: PostgreSQL

clasificacion_incertidumbre:
  Critica: bloquea_la_ejecucion
  Alta: puede_cambiar_la_arquitectura
  Media: afecta_la_calidad
  Baja: se_puede_asumir_valor_razonable
  bloquean_proceso: solo_las_criticas

motor_hipotesis:
  genera_varias_interpretaciones:
    Hipotesis_A: 72%
    Hipotesis_B: 18%
    Hipotesis_C: 10%
  if_una_supera_95%_confianza: continua_sin_preguntar

detector_contradicciones_ejemplos:
  hazlo_rapido_+_optimiza_al_maximo
  sin_coste_+_usa_servicios_premium
  solo_local_+_usa_APIs_en_la_nube
```

### GAP #14 — DATASETS/ADAPTERS URLs Verificados (60+60)

```yaml
master_doc_destino: MASTER-10_Modelos_y_APIs
aplicar: agregar_URLs_reales_de_HF_para_los_60_datasets_y_60_adapters_que_PARCHE-v15_confirmo
```

### GAP #15 — CSA Estructura de Carpetas

```yaml
g5/csa/:
  __init__.py
  consejo.py  # coordina_los_10_jueces
  jueces/:
    __init__.py
    j1_comprension.py
    j2_cobertura.py
    j3_consistencia.py
    j4_exactitud.py
    j5_arquitectura.py
    j6_calidad_codigo.py
    j7_investigacion.py
    j8_optimizacion.py
    j9_seguridad.py
    j10_calidad_final.py
  fases/:
    __init__.py
    fase1_audita_input.py
    fase2_busca_huecos.py
    fase3_10_soluciones.py
    fase4_destruye.py
    fase5_ataca_otros.py
  sistema_veto.py
  paquete_rechazo.py
  ciclo_infinito.py
```

### GAP #16 — PATCHES-MAXBRY-SUPER-TEAM P1-P14 (Resumen)

```yaml
P1: Redis_compartido_solo_G5+G6
P2: Capacidad_2000_agentes_/_1000_tareas
P3: Generador_Skills_o_Agentes_auto_evolucion
P3.2: Skills_NO_se_borran_van_a_GitHub
P3.3: Raiz_para_Skills_MAXBRY_ROOT
P4: Juez_Supervisor_Validador_JSV_8_reglas
P5: AUTO-RUN_+_Interface_de_configuracion_inicial
P6: Sistema_de_cifrado_y_seguridad
P7: Nucleo_del_orquestador_solo_via_API
P8: Bootstrap_de_instalacion_autonoma
P9: Arquitectura_modular_10_modulos_independientes
P10: Principio_de_cero_configuracion
P11: Descarga_inteligente_de_componentes
P12: Inicio_autonomo
P13: Escalabilidad_horizontal
P14: Renombramiento_MAXBRY_SUPER_TEAM
```

### GAP #17 — AUTO-RUN Interface (Primera Instalación)

```yaml
interfaz_visual:
  titulo: MAXBRY_SUPER_TEAM_Configuracion_Inicial
  seleccion_modelos_IA_a_usar:
    - MiniMax_M3_jefe_validador: true
    - Kimi_K2.7-Code_programador: true
    - Hermes_Agent: true
    - OpenCLAW: true
    - Smolagents: true
    - MiMo_Code: true
    - "..."
  boton: CONTINUAR
```

### GAP #18 — Dependencias entre Grupos (DAG)

```yaml
DAG_dependencias:
  G1_INFRA: []
  G2_CORE: [G1_INFRA]
  G3_UI: [G1_INFRA, G2_CORE]
  G4_AUDIT: [G2_CORE, G3_UI]
  G5_CONSENSO: [G4_AUDIT]
  G6_BUILD: [G5_CONSENSO]
  G7_ASISTENTES: [G5_CONSENSO, G8_ORQUESTADOR]
  G8_ORQUESTADOR: [G5_CONSENSO]
```

### GAP #19 — PARCHE-v16 Mejoras 100X (8 Inputs)

```yaml
INPUT_1: Skills_Predictivos
INPUT_2: Memoria_Cuantica_Distribuida
INPUT_3: Interfaz_Multimodal  # texto_voz_imagen_video_archivo_WebRTC_gestos_biometricos_contexto_ambiental
INPUT_4: MAXBRY_como_Super_Orquestrador_Universal  # protocolo_abierto
INPUT_5: Ecosistema_de_Inteligencia_Distribuida  # auditores_dinamicos
INPUT_6: "?"
INPUT_7: "?"
INPUT_8: "?"
```

### GAP #20 — FUSIÓN KIMI + M3 (Ficha Ejecutable)

```yaml
lo_que_mantiene:
  - 10_fases_Fase_0_a_9
  - 8_archivos_coordinador
  - 5_archivos_soporte
  - 3_modos_Manual_Semi_Auto_Continuo
  - principios_90%_code_+_10%_LLM

mejoras_100x:
  estructura_lt_200_lineas: cada_archivo_editable_sin_romper_otros
  10_agentes_del_consejo: consenso_mas_robusto_no_1_juez
  investigacion_multi_fuente: 5_fuentes_en_paralelo
  youtube_agent: tutoriales_visuales
  MiniMax_M3_+_Kimi_K2: division_de_roles_clara
  APIs_intercambiables: profiles_en_config_json
  mini_interface_multi_canal: 5_canales_de_entrada
  confirmacion_de_proyecto: preguntar_antes_de_ejecutar
  enchufe_universal_v1.5: conecta_cualquier_cosa
  sistema_externo_de_razonamiento: universal_para_cualquier_LLM
  ficha_ejecutable: diseno_es_codigo_ejecutable
```

### Resumen de Acciones

```yaml
gap_a_master_doc_destino:
  1_6_vs_8_grupos: MASTER-02_mantener_6_aclaracion
  2_activation_commands: MASTER-09_agregar_seccion
  3_13_criterios_skills: MASTER-05_27_corregir_lista
  4_sheriff_sentinel_watcher: MASTER-09_agregar_protocolos
  5_consensus_5_12: MASTER-25_agregar_detalle
  6_10_loops: MASTER-08_agregar_tabla
  7_memory_protocol_v1: MASTER-21_agregar_tiers
  8_storage_strategy: MASTER-12_agregar
  9_merge_prioridades_keepalive: MASTER-12_agregar
  10_M3_atributos: MASTER-10_agregar
  11_DSL_reasoning_chain_py: MASTER-16_agregar_codigo
  12_FASE_0.5_ejemplo: MASTER-12_agregar_ejemplo
  13_SID_pre_procesador: MASTER-05_agregar
  14_URLs_datasets_adapters: MASTER-10_agregar_URLs
  15_CSA_estructura: MASTER-13_agregar
  16_P1_a_P14_MAXBRY: MASTER-17_agregar
  17_auto_run_interface: MASTER-23_agregar
  18_dependencias_DAG: MASTER-13_agregar
  19_mejoras_100X: MASTER-27_agregar_INPUT_1_a_5
  20_fusion_Kimi_M3: MASTER-13_agregar

conclusion:
  - 20_gaps_criticos_encontrados
  - 17_ya_parcialmente_documentados_en_master_docs
  - 3_requieren_actualizacion_mayor: 1_inconsistencia_grupos, 3_lista_criterios, 11_DSL_enforcement
```


## DOC 9: REGLAS + COSTOS + CAPACIDADES (Full Extracción)

### Objetivo Infraestructura $0

```yaml
como_se_logra:
  HuggingFace_Free_Tier:
    - 7_Spaces_con_16GB_RAM_c/u
    - CPU_basico_gratis
    - Storage_limitado
  API_Free_Tiers:
    - 4_NVIDIA_NIM_keys_free_tier
    - 6_Cerebras_keys_free_tier
    - 6_Groq_keys_free_tier
  GGUF_Local:
    - 9_modelos_cuantizados
    - "0.6GB_a_3GB_cada_uno"
    - sin_costo_de_inferencia

total: $0/mes

limites_a_respetar:
  - HF_Spaces_pueden_dormirse_por_inactividad
  - rate_limits_de_APIs
  - memoria_limitada_por_Space_16GB_c/u
  - cold_starts_posibles
  - HH_ne_A100_solo_CPU/T4
```

### Capacidades del Sistema

```yaml
objetivo:
  - 2000+_agentes_simultaneos_CAPACIDAD_no_reales
  - 1000+_tareas_simultaneas
  - 7_HF_Spaces_con_16GB_c/u_eq_112GB_RAM
  - "~13.5GB_usados_por_modelos"
  - "87%_margen_libre"

calculo_de_lineas_y_memoria:
  - "~53,400_lineas_totales_de_codigo"
  - "336_archivos_Python"
  - "~14_MB_codigo_fuente"
  - "~500_MB_RAM_runtime_sin_modelos"
  - "~13.5_GB_RAM_con_modelos_G6"
  - "7_HF_Spaces_x_16GB_eq_112_GB_disponibles_87%_margen_libre"

escalabilidad:
  horizontal: agregar_HF_Spaces
  vertical: upgrade_a_Spaces_larger
  "sin_redesign_del_codigo"
```

### Máxima Capacidad (No Implementar Todavía)

```yaml
diseno_CAPACIDAD_no_implementacion:
  - 10_a_2000_agentes_sin_redesign
  - 1000_tareas_simultaneas
  - stateless_design
  - comunicacion_bus_de_eventos
```

### Restricciones de MAX (Confirmadas)

```yaml
hardware:
  - MAX_solo_tiene_smartphones_+_iPad_Pro
  - sin_PC_para_servidores
  - sin_GPU_dedicada
  - todo_debe_correr_en_HF

reglas_operacionales:
  - NUNCA_crear_ni_cambiar_nada_sin_mi_APROBADO
  - SOLO_AGREGO_capas_NUNCA_reemplazo
  - MANTENER_todos_los_nombres_originales
  - estructura_lt_200_lineas_por_archivo  # M2.7_puede_editar_sin_romper
```

### Reglas del Sistema (Confirmadas en Chat)

```yaml
reglas_de_operacion:
  - 5_GOALS_+_12_PASOS_obligatorios_en_cada_salida
  - cada_salida_empieza_con_APLICANDO_SYSTEM_PROMPT
  - cada_salida_termina_con_AUDIT_FINAL_PASO_12
  - 3_separate_inventories: Tools_ne_Agents_ne_AI_Models
  - Orquestador_INDEPENDIENTE_no_mezclar_con_GGUF/AI_keys/proyectos
  - NO_inventar_datos_preguntar_si_falta_info
  - NO_alucinar
  - MVP_first_anti_overengineering
  - no_inventar_nuevas_categorias
  - cada_salida_validar_antes_de_patchear
  - mostrar_PENDIENTE_si_algo_no_esta_aprobado
  - STATE_JSON_actualizado_siempre

reglas_de_aprobacion:
  - NUNCA_crear_o_cambiar_nada_sin_APROBADO_explicito
  - SOLO_AGREGO_capas_NUNCA_reemplazo
  - MANTENER_todos_los_nombres_roles_cantidades_originales

reglas_tecnicas:
  - Input_is_sacred_Input_Block_nunca_modifica_o_resume_o_parafrese_o_reinterpreta
  - DSL/DAG_nunca_prompt_libre_solo_estructurado
  - G5_gestiona_agentes_no_al_reves
  - Orquestador_confirma_proyecto_antes_de_ejecutar_Fase_0.5
  - APIs_intercambiables_3_profiles_conservador_equilibrado_agresivo
  - Structure_lt_200_lineas_por_archivo
  - cada_HF_Space_per_group_eq_aislado_con_own_token
  - cada_proyecto_eq_separate_root_en_GitHub
  - cada_Docker_container_por_proyecto
```

### Determinismo en el Orquestador (90/10)

```yaml
90%_codigo_determinista:
  - Parseo
  - Validacion
  - Transformacion
  - Routing
  - Verificacion_mecanica
  - Formatting
  - Retry
  - Fallback
  - Circuit_breaker
  - EROS_compression
  - Checkpoint_restore
  - Schema_validation

10%_LLM_solo_donde_aporta_senal:
  - MA-RAG-SYNTH_sintesis
  - MA-ARCH-PLAN_parte_creativa
  - Max_Mode_decisiones_criticas
  - llm_adversarial_review_cuando_3_capas_mecanicas_fallan
```

### Estado del Proyecto

```yaml
done:
  - 100_patches_con_documentacion_individual
  - 19_archivos_Python_reales_726_lineas
  - Constitucion_1276_lineas
  - Memoria_persistente_2_topics
  - 8_documentos_consolidados_72_KB

in_progress:
  - 9_documentos_consolidados_mas_en_curso
  - verificacion_cruzada_final

blocked:
  - MAX_confirma_arquitectura_final
  - M2.7_no_ha_instalado_nada_espera_GO_de_MAX
  - datos_pre_flight_pendientes:
    - GitHub_username_+_PAT
    - HF_username_+_6_tokens
    - 16_API_keys_con_labels
    - Turso_DB_credentials
    - Visibility_preference_public/privado
    - Telegram_bot_token
    - HTM_model_name_no_encontrado_en_HF
    - YUAN_model_name_no_encontrado_en_HF

codigo_real_creado: 19_archivos_Python_en_/workspace/maxbry/g7/output_engine/v2/
estructura:
  __init__.py: 47_lineas
  pre_mortem/pre_mortem_analyzer.py: 70_lineas
  auto_rollback/rollback_monitor.py: 62_lineas
  meta_learning/cross_release_analyzer.py: 56_lineas
  personalization/style_learner.py: 64_lineas
  multi_stakeholder/stakeholder_detector.py: 79_lineas
  causal_tracing/causal_chain_builder.py: 75_lineas
  marketplace/output_cataloger.py: 84_lineas
  self_improving/quality_analyzer.py: 99_lineas
  production_monitoring/usage_tracker.py: 88_lineas
  +_10___init___.py
  total: 726_lineas_de_codigo

sin_output_sandbox: RECHAZADO_por_MAX_no_se_creo_carpeta_output_sandbox
```

### Documentación Principal en /workspace/nct-proyecto/

```yaml
documentos_de_diseno:
  01-FASE-0-FROZEN.md: 651_lineas
  02-SYSTEM-PROMPT-MYTHOS.md: 672_lineas
  ANALISIS-LOOPS-v100.md: 192_lineas
  BIS-v1-MAXBRY.md: 143_lineas
  BORRADOR-LISTA-APROBADOS.md: 1456_lineas
  CONSENSO-MEJORADO-10X.md: 4465_lineas
  CONSTITUCION-ORQUESTADOR.md: 1276_lineas
  MI-SYSTEM-PROMPT-OPERATIVO.md: 136_lineas
  ORQUESTADOR-G5-DISENO.md: 2928_lineas
  PARCHE-v14_a_PARCHE-v17: 4_parches
  PARCHES-MAXBRY-SUPER-TEAM.md: 847_lineas
  SISTEMA-RAZONAMIENTO-EXTERNO.md: 3126_lineas
  STATE-AUDIT.md: 455_lineas
  VALIDACION-POR-SALIDA.md: 2667_bytes
  RESUMEN-OUTPUT-V61.md
documentos_consolidados:
  directorio: /workspace/nct-proyecto/CONSOLIDADO-FINAL/
  contenido: 01_a_09_documentos_sobre_orquestador_y_agentes
```

---

## DOC MASTER 19: PRE-FLIGHT + DEPENDENCIAS

### 8 Datos Pre-Flight Pendientes

```yaml
github:
  username: pendiente
  personal_access_token_PAT_scopes: [repo_full_control, workflow_update_workflows, admin:org_si_aplica]

huggingface:
  username: pendiente
  tokens: 6_pendientes  # uno_por_Space_principal

api_keys_16_total:
  - 4_NVIDIA_NIM_keys
  - 6_Cerebras_keys
  - 6_Groq_keys
  formato_recomendado: provider-numero-uso

database:
  turso_db_url: pendiente
  turso_db_token: pendiente

otros:
  visibility_preference: public_or_private_pendiente
  telegram_bot_token_de_BotFather: pendiente
  HTM_model_name_hipotetico_en_HF: no_encontrado
  YUAN_model_name_hipotetico_en_HF: no_encontrado
```

### Aprovisionamiento Automático (7 Pasos)

```yaml
paso_1_crear_14_repos_en_GitHub:
  repos_de_grupos_6:
    - nct-g1-infra
    - nct-g2-core
    - nct-g3-ui
    - nct-g4-audit
    - nct-g5-orquestador  # estrella
    - nct-g6-asistentes
  repos_de_productos_8: nct-product-01_a_nct-product-08

paso_2_crear_7_HF_Spaces:
  - mavis/g1-infra
  - mavis/g2-core
  - mavis/g3-ui
  - mavis/g4-audit
  - mavis/g5-orquestador  # estrella
  - mavis/g6-asistentes
  - mavis/extras
  cada_con_su_propio_token

paso_3_escribir_5_Dockerfiles:
  - Dockerfile.g1
  - Dockerfile.g2
  - Dockerfile.g3
  - Dockerfile.g4
  - Dockerfile.g5

paso_4_inyectar_secretos:
  - API_keys_como_GitHub_Secrets
  - Tokens_como_HF_Secrets
  - Credenciales_encriptadas

paso_5_configurar_profiles:
  - Conservador
  - Equilibrado_recomendado
  - Agresivo

paso_6_arrancar_orquestador:
  - Bootstrap_autonomo
  - Conexion_a_G1-G6
  - Reporte_a_MAX

paso_7_reporte_a_MAX:
  - URLs_de_acceso
  - Comandos_utiles
  - Estado_de_cada_Space
  - Estado_de_cada_repo
```

### Responsable de Instalación: M2.7

```yaml
quien_es_M2.7: sesion_dedicada_a_instalacion  # NO_disena_arquitectura_eso_es_M3

lo_que_M2.7_hace:
  - lee_CONSTITUCION-ORQUESTADOR_md
  - lee_los_18_master_docs
  - lee_los_patches_aprobados
  - ejecuta_aprovisionamiento_automatico
  - reporta_a_MAX

lo_que_M2.7_NO_hace:
  - no_modifica_arquitectura
  - no_inventa
  - no_reemplaza_originales
  - no_crea_nuevas_categorias_sin_aprobacion

bloqueos_de_M2.7:
  - si_encuentra_datos_faltantes: escala_a_MAX
  - si_encuentra_inconsistencias: escala_a_MAX
```

### Dependencias entre Grupos

```yaml
DAG:
  G1_INFRA → G2_CORE → G3_UI
       ↓         ↓        ↓
       └───► G4_AUDIT ◄──┘
                ↓
          G5_ORQUESTADOR  # estrella
                ↓
          G6_ASISTENTES

secuencia_instalacion:
  1_G1_INFRA: primero  # crea_HF_Spaces_GitHub_Docker
  2_G6_ASISTENTES: segundo  # carga_modelos
  3_G2_CORE: tercero  # BIS_SID_Input_Output
  4_G4_AUDIT: cuarto  # CSA
  5_G5_ORQUESTADOR: quinto  # MAXBRY
  6_G3_UI: ultimo  # interfaz_con_MAX
```

### Estado de M2.7

```yaml
actual:
  - M2.7_NO_ha_instalado_nada
  - espera_datos_pre_flight_de_MAX
  - espera_aprobacion_de_arquitectura_final

cuando_arranque:
  1: verifica_entorno_Python_network_secrets
  2: crea_estructura_de_carpetas
  3: clona_template_base
  4: configura_profiles
  5: crea_recursos_externos_con_pre_flight
  6: inyecta_secretos
  7: arranca_servicios
  8: reporta
```

### Checklist Pre-Arquitectura

```yaml
ya_completado:
  - Constitucion_v3.0_completa_39_principios
  - CSA_10_jueces_con_5_fases
  - SID_con_5_preguntas
  - BIS_con_14_categorias_+_13_criterios
  - Input_Engine_v4.0_54_componentes
  - Output_Engine_+_OOS_v3.1_27_componentes
  - LOOP_v6.0_15_capas_+_3_ciclos
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

pendiente:
  - 8_datos_pre_flight_de_MAX
  - aprobacion_final_de_MAX
  - M2.7_orden_de_instalacion
```

### Recomendaciones para MAX

```yaml
perfil_recomendado: Equilibrado  # balance_costo_calidad
canales_prioritarios: [Telegram, API_REST]  # Telegram_chat_directo, API_REST_integracion
lista_inicial_de_proyectos: Pendiente_decision  # MAX_decide_los_8_productos
visibilidad: Decision_pendiente  # MAX_decide_si_public_o_private

conclusion:
  el_sistema_esta_100%_disenado
  falta_solo:
    1: los_8_datos_pre_flight_de_MAX
    2: aprobacion_final
    3: orden_de_instalacion_a_M2.7
  cuando_MAX_dé_GO_M2.7_ejecuta_aprovisionamiento_automatico_y_reporta
```

## DOC MASTER 15: REGLAS + COSAS INTOCABLES (Detalle Completo)

### Regla de Oro

```yaml
regla_de_oro: "NUNCA_crear_ni_cambiar_nada_sin_APROBADO_explicito_de_MAX"
categoria: regla_absoluta
cualquier_desviacion_requiere: aprobacion_explicita
```

### Cosas Intocables (Nunca Modificar)

```yaml
CSA_Consejo_Supremo_de_Auditoria:
  - 10_Jueces_CSA_J1-J10
  - 5_fases_por_juez_F1-F5
  - Sistema_de_veto
  - Sistema_de_puntuacion
  - Auditor_SID_5_preguntas_fijas

Constitucion: 39_principios_totales_v1.0_v2.0_v3.0

BIS_Biblioteca_Inteligente_de_Skills:
  - 14_categorias_A-N
  - 13_criterios_de_skills
  - 3_versiones_v1_v2_v3
  - Debate_de_4_especialistas

Estructura_MAXBRY_SUPER_TEAM:
  - 30_micro_agentes_MA-01_a_MA-30
  - 11_internal_roles_R1-R11
  - 10_parallel_queues_Q1-Q10
  - 10_agent_consensus_council
  - 6_autonomy_levels_L1-L6
  - 12_task_models_TM01-TM12
  - 5_loop_versions_ALV_LOP_*
  - 3_monitors_PAD_Anxiety_Drift
  - 5_officers_CEO_CTO_COO_CSO_CMO

Modelos_y_APIs:
  - 9_GGUF_modelos_confirmados
  - 16_API_keys_4_NIM_+_6_Cerebras_+_6_Groq
  - 60_datasets_PARCHE-v15
  - 60_adapters_PARCHE-v15

Outputs_rechazados:
  - Output_Sandbox  # no_se_implementa
```

### 10 Reglas de Operación

```yaml
R1_capas: SOLO_AGREGO_capas_NUNCA_reemplazo
R2_nombres: MANTENER_todos_los_nombres_originales  # J1-J10_SID_5_preguntas_39_principios_14_categorias_BIS_A-N
R3_cantidades: Mantener_cantidades_exactas  # 10_jueces_5_fases_30_micro_agentes_11_internal_roles
R4_validacion: Cada_salida_valida_antes_de_patchear
R5_PENDIENTE: Mostrar_PENDIENTE_si_algo_no_esta_aprobado  # NO_inventar
R6_inventarios: 3_inventarios_separados_Tools_ne_Agents_ne_AI_Models
R7_Orquestador_independiente: No_mezclar_con_GGUF/AI_keys/proyectos
R8_no_inventar: NO_inventar_datos  # preguntar_si_falta_info
R9_no_alucinar: NO_alucinar  # mejor_decir_no_se_que_inventar
R10_MVP_first: Empezar_simple_iterar
```

### 5 GOALS Obligatorios en Cada Salida

```yaml
cada_salida_debe_tener_explicitamente:
  G1_goal_primary: objetivo_principal
  G2_goal_secondary: objetivo_secundario
  G3_goal_success: que_es_exito
  G4_goal_failure: que_es_fracaso
  G5_goal_restriction: que_NO_hacer
```

### 12 PASOS Obligatorios en Cada Salida

```yaml
cada_salida_sigue_12_pasos:
  01_literal_read
  02_think
  03_plan
  04_decompose
  05_hypotheses
  06_swarm
  07_critic
  08_simulate
  09_validate
  10_consensus
  11_report
  12_audit
```

### Formato de Salida

```yaml
inicio_obligatorio: "APLICANDO_SYSTEM_PROMPT_5_GOALS_+_12_PASOS"
final_obligatorio: "AUDIT_FINAL_PASO_12"
```

### 5 Pasos de Validación por Salida

```yaml
1_buscar_memoria: ya_existe
2_validar_propuesta: es_correcta
3_validar_salida: cumple_formato
4_validar_trazabilidad: registrable
5_STATE_JSON_actualizado: sincronizado
```

### 8 Reglas del Juez Supervisor

```yaml
1_nombre_correcto: usa_nombres_aprobados
2_formato_valido: cumple_formato_esperado
3_aprobado_por_MAX: tiene_visto_bueno
4_sin_reemplazo: no_sustituye_originales
5_STATE_JSON_actualizado: refleja_cambios
6_trazabilidad: acciones_registradas
7_audit_completo: AUDIT_FINAL_presente
8_compatible_con_Constitucion: no_viola_principios
```

### Confidence Scoring

```yaml
umbrales:
  ge_95%: APROBADO_procede
  80_a_94%: APROBADO_CON_NOTAS_procede_con_advertencias
  lt_80%: RECHAZADO_bloquea

aplicado_a:
  - Tasks_Task_Score
  - Agents_Agent_Score
  - Models_Model_Score
  - Outputs_Output_Score
```

### Roles M3 vs SKYNER

```yaml
M3_chat_arquitecto:
  - interactua_con_MAX
  - decide_QUE_hacer
  - NO_ejecuta_codigo_directo
  - disena_alto_nivel

SKYNER_interno:
  - ejecuta
  - NO_chatea_con_MAX
  - decide_COMO_hacerlo
  - reporta_a_M3

conclusion: las_reglas_y_cosas_intocables_son_el_marco_respetarlas_garantiza_crecimiento_sin_romperse_la_regla_de_oro_APROBADO_de_MAX_es_la_mas_importante
```

