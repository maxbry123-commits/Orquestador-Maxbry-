# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 3)

> **Continuación** de `orquestacion-from-docs-part1*.md` y `part2.md`.
> Quinta pasada — extractos individuales de archivos específicos.


## DOC MASTER 10: MODELOS Y APIs — 9 GGUF + 16 API Keys + 3 Perfiles

### 9 Modelos GGUF Confirmados en HF

```yaml
modelo_01_HRM-Text-1B:
  params: 1B
  gguf_size: 0.6GB
  uso: razonamiento_jerarquico
modelo_02_Qwen2.5-Coder-1.5B:
  params: 1.5B
  gguf_size: 1GB
  uso: generacion_de_codigo
modelo_03_Granite-4.1-3B_IBM:
  params: 3B
  gguf_size: 2GB
  uso: asistente_general
modelo_04_Granite-3.2-2B_IBM:
  params: 2B
  gguf_size: 1.5GB
  uso: asistente_compacto
modelo_05_LFM2.5-1.2B-Thinking:
  params: 1.2B
  gguf_size: 0.8GB
  uso: razonamiento
modelo_06_Gemma-4-E4B_Google:
  params: 4B
  gguf_size: 2.5GB
  uso: asistente_eficiente
modelo_07_Gemma-4-E2B_Google:
  params: 2B
  gguf_size: 1.5GB
  uso: asistente_compacto
modelo_08_GPT-OSS-20B_OpenAI:
  params: 21B_total_/_3.6B_active_MoE
  gguf_size: 13GB
  uso: modelo_fuerte
modelo_09_Nemotron-3-Nano-4B_NVIDIA:
  params: 4B
  gguf_size: 2.5GB
  uso: asistente_NVIDIA

total_local: ~25.6GB
```

### 16 API Keys (con Labels Sugeridos)

```yaml
NVIDIA_NIM_4_keys:
  NIM-01: [SKYNER_lider_G5, tareas_principales]
  NIM-02: [Razonamiento, razonamiento_complejo]
  NIM-03: [Codigo, generacion_de_codigo]
  NIM-04: [Backup, respaldo]

Cerebras_6_keys:
  CER-01: [COO, operaciones]
  CER-02: [CTO, tecnico]
  CER-03: [Razonamiento, analisis]
  CER-04: [Codigo, code_gen]
  CER-05: [Backup-1, respaldo]
  CER-06: [Backup-2, respaldo]

Groq_6_keys:
  GROQ-01: [CFO, costos]
  GROQ-02: [CMO, comunicacion]
  GROQ-03: [Historian, memoria]
  GROQ-04: [Razonamiento, analisis_rapido]
  GROQ-05: [Backup-1, respaldo]
  GROQ-06: [Backup-2, respaldo]
```

### 3 Perfiles de Uso

```yaml
conservador:
  primary: groq
  secondary: nim
  fallback: cerebras
  reglas:
    - never_use_GPT-OSS-20B_too_heavy
    - max_3_retries
    - timeout: 60s
  budget:
    max_tokens_per_task: 100_000
  casos: tareas_simples_bajo_costo_bajo_riesgo

equilibrado_RECOMENDADO:
  primary: nim
  secondary: cerebras
  fallback: groq
  reglas:
    - GPT-OSS-20B_only_for_hard_tasks
    - max_5_retries
    - timeout: 120s
  budget:
    max_tokens_per_task: 500_000
  casos: mayoria_tareas_balance_costo_calidad

agresivo:
  primary: cerebras
  secondary: nim
  fallback: groq
  reglas:
    - always_try_GPT-OSS-20B_first
    - max_10_retries
    - timeout: 300s
  budget:
    max_tokens_per_task: 2_000_000
  casos: tareas_criticas_maxima_calidad_costo_no_importa
```

### Router Inteligente

```python
def select_model(task, profile):
    candidates = MODELS_BY_CAPABILITY[task.type]
    if profile == "conservador":
        return cheapest(candidates)
    elif profile == "equilibrado":
        return best_quality_per_dollar(candidates)
    else:  # agresivo
        return best_quality(candidates)
```

```yaml
reglas_de_routing:
  - tarea_simple_a_GGUF_local
  - tarea_media_a_Groq
  - tarea_compleja_a_Cerebras_o_NIM
  - tarea_critica_a_GPT-OSS-20B_via_NIM
```

### Datasets (60) y Adapters (60)

```yaml
datasets_con_PARCHE-v15:
  - 30_datasets_de_codigo
  - 15_datasets_de_texto
  - 10_datasets_especializados
  - 5_datasets_de_testing
  total: 60_datasets_con_URLs_verificadas

adapters_con_PARCHE-v15:
  - 30_LoRA_adapters
  - 15_QLoRA_adapters
  - 10_prefix_tuning
  - 5_prompt_tuning
  total: 60_adapters_con_URLs_verificadas
```

### Capacidades Finales

```yaml
hardware_disponible:
  - 7_HF_Spaces_x_16GB_eq_112GB_RAM
  - "~13.5GB_usados_por_modelos_G6"
  - "87%_margen_libre"

throughput_estimado:
  - 1000+_tareas_dia_perfil_equilibrado
  - 2000+_tareas_dia_perfil_conservador
  - 100+_tareas_dia_perfil_agresivo

conclusion_G6_Asistentes:
  - 9_modelos_GGUF_locales
  - 16_API_keys_4_NIM_+_6_Cerebras_+_6_Groq
  - 3_perfiles_de_uso
  - router_inteligente
  - 60_datasets
  - 60_adapters
  - capacidad_para_1000+_tareas_dia
  - costo_$0/mes_con_free_tiers
```

## DOC MASTER 16: DSL + UNIVERSAL PLUG v1.5

### 1. DSL — Domain Specific Language

```yaml
que_es: lenguaje_estructurado_que_usa_NCT_para_tareas_workflows_pipelines_configuraciones  # NUNCA_prompt_libre

reglas:
  - estructura_cerrada_no_free_form
  - validado_contra_schema
  - parseable_deterministicamente
  - versionado_semver
  - schema_first

tipos_soportados:
  DSL_Task: [definir_tarea, task.v1.json]
  DSL_Pipeline: [definir_pipeline, pipeline.v1.json]
  DSL_Agent: [definir_agente, agent.v1.json]
  DSL_Skill: [definir_skill, skill.v1.json]
  DSL_Project: [definir_proyecto, project.v1.json]
  DSL_Workflow: [definir_workflow, workflow.v1.json]
  DSL_DAG: [definir_DAG, dag.v1.json]
```

### 2. DSL Task (Ejemplo)

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
    - { id: s1, action: parse_input }
    - { id: s2, action: validate_schema }
    - { id: s3, action: generate_plan }
    - { id: s4, action: execute }
    - { id: s5, action: validate }
    - { id: s6, action: deliver }
  budget:
    max_tokens: 100_000
    max_runtime_s: 600
```

### 3. DSL Pipeline (Ejemplo)

```yaml
pipeline:
  id: pipeline-001
  name: "Crear API REST"
  pattern: dag
  steps:
    - { id: parse, agent: MA-01, input_from: user, output_to: ctx.parsed }
    - { id: plan, agent: MA-06, input_from: ctx.parsed, output_to: ctx.plan, depends_on: parse }
    - { id: execute, agent: MA-15, input_from: ctx.plan, output_to: ctx.executed, depends_on: plan }
    - { id: verify, agent: MA-16, input_from: ctx.executed, output_to: ctx.verified, depends_on: execute }
  consensus: required
  audit: full_csa
```

### 4. DSL DAG

```yaml
dag:
  id: dag-001
  nodes:
    - { id: A, type: task, agent: MA-01 }
    - { id: B, type: task, agent: MA-06 }
    - { id: C, type: task, agent: MA-15 }
  edges:
    - { from: A, to: B }
    - { from: B, to: C }
  groups:
    - { id: g1, nodes: [A, B], parallel: true }

validacion:
  - no_ciclos
  - topological_sort_valido
  - cada_nodo_tiene_agente
  - cada_edge_tiene_origen_y_destino_validos
```

### 5. Universal Plug v1.5 — Module Contract JSON Schema

```yaml
descripcion: define_como_los_modulos_se_conectan_entre_si
version: 1.5
schema:
  $schema: http://json-schema.org/draft-07/schema#
  title: MAXBRY_Module_Contract
  type: object
  required: [module_id, version, interface]
  properties:
    module_id:
      type: string
      pattern: ^[a-z][a-z0-9_]*$
    version:
      type: string
      pattern: ^\d+\.\d+\.\d+$
    interface:
      type: object
      required: [inputs, outputs]
      properties:
        inputs: { type: array }
        outputs: { type: array }
    dependencies:
      type: array
      items: { type: string }
    capabilities:
      type: array
    limits:
      type: object
    metadata:
      type: object

campos_obligatorios:
  - module_id
  - version
  - interface.inputs
  - interface.outputs

campos_opcionales:
  - dependencies
  - capabilities
  - limits
  - metadata
  - tags
  - author

validacion:
  - schema_valido_contra_Draft-07
  - module_id_unico
  - version_semver
  - interface_tipado
  - dependencies_resolubles
```

### 6. Ejemplo de Módulo

```yaml
ejemplo_ma_code_gen:
  module_id: ma_code_gen
  version: 1.0.0
  interface:
    inputs:
      - { name: spec, type: string, required: true }
      - { name: stack, type: object, required: true }
    outputs:
      - { name: code, type: file }
      - { name: diff, type: file }
  dependencies: [ma_arch_plan]
  capabilities: [code_generation, diff_creation]
  limits:
    max_tokens: 50000
    max_runtime_s: 120
  metadata:
    owner: g5-orquestador
    category: J-IA
    license: MIT
```

### 7. Sistema de Validación Cruzada (DSL DAG)

```yaml
concepto: DSL_DAG_de_validacion_cruzada_garantiza_que_cada_documento_referencia_al_menos_2_docs_mas_las_referencias_sean_validas_no_hay_contradicciones_las_dependencias_sean_resolubles

estructura:
  cross_validation:
    node: MASTER-XX
    references_to: [MASTER-YY, MASTER-ZZ]
    referenced_by: [MASTER-WW]
    consistency_check:
      no_contradictions: true
      terms_aligned: true
      versions_match: true
      schema_compatible: true

ejecucion_python: |
  def cross_validate(doc_a, doc_b):
      # Check no contradictions
      if contradiction(doc_a, doc_b):
          return {"valid": False, "reason": "contradiction"}
      
      # Check term alignment
      if not terms_aligned(doc_a, doc_b):
          return {"valid": False, "reason": "term_misalignment"}
      
      # Check version compatibility
      if not versions_match(doc_a, doc_b):
          return {"valid": False, "reason": "version_mismatch"}
```


## DOC 3: PIPELINE Y FASES DEL ORQUESTADOR (10 Fases Detalle)

### 10 Fases del Pipeline

```yaml
F1_Recepcion: input_llega
F2_Pre_procesamiento: SID_validaciones_iniciales
F3_Definicion: Definition_Engine_clarificar
F4_Planificacion: DAG_recursos_asignacion
F5_Confirmacion: Fase_0.5_MAX_aprueba_si_es_nuevo
F6_Ejecucion: agentes_activos
F7_Validacion: CSA_quality_score
F8_Publicacion: output_engine_multi_target
F9_Monitoreo: produccion_telemetria
F10_Aprendizaje: actualizar_memoria_reglas
```

### FASE 0.5 — Confirmation Gate (CRÍTICA E INTOCABLE)

```yaml
por_que_existe:
  evitar_que_orquestador:
    - ejecute_proyectos_no_autorizados
    - gaste_recursos_sin_permiso
    - asuma_cosas_que_MAX_no_quiso

como_funciona:
  F4_Planificacion_completa
  F5_Fase_0.5_Confirmacion
  "¿Es_proyecto_conocido?"
    SI_a_procede_automatico
    NO_a_PAUSA_y_consulta_a_MAX
  MAX_aprueba_o_modifica
  F6_Ejecucion_inicia

REGLA_ABSOLUTA:
  proyecto_nuevo_eq_SIEMPRE_confirmacion
  proyecto_recurrente_eq_procede_automatico
```

### 3 Monitores del Pipeline

```yaml
M1_Performance: latencia_throughput_cuellos_de_botella
M2_Calidad: scores_errores_complaints
M3_Recursos: tokens_memoria_rate_limits_costos

caracteristicas:
  - operacion_continua_24_7
  - alertas_automaticas
  - dashboards_para_MAX
  - historico_para_analisis
```

### Modelos de Ejecución Según Complejidad (4 Escenarios)

```yaml
ESCENARIO_1_TAREA_SIMPLE_9_pasos:
  1_INPUT
  2_INTENT_PARSING
  3_CONTEXT_BUILDING
  4_PLAN_GENERATION
  5_EXECUTE
  6_SELF_CHECK
  7_OUTPUT_GENERATION
  8_POST_OUTPUT_AUDIT
  9_FEEDBACK_LOOP_STORAGE

ESCENARIO_2_TAREA_MEDIA_16_pasos:
  1_INPUT
  2_INTENT_PARSING
  3_PROBLEM_FRAMING
  4_CONTEXT_BUILDING
  5_CONSTRAINT_EXTRACTION
  6_GOAL_DECOMPOSITION
  7_COMPLEXITY_ESTIMATION
  8_PLAN_GENERATION
  9_SUBTASK_BREAKDOWN
  10_HYPOTHESIS_GENERATION
  11_VALIDATION_LAYER
  12_DECISION_ENGINE
  13_CONFIDENCE_SCORING
  14_OUTPUT_GENERATION
  15_POST_OUTPUT_AUDIT
  16_FEEDBACK_LOOP_STORAGE

ESCENARIO_3_TAREA_OPTIMA_25_pasos:
  1_INPUT
  2_INTENT_PARSING
  3_PROBLEM_FRAMING
  4_DOMAIN_DETECTION
  5_CONTEXT_BUILDING
  6_CONSTRAINT_EXTRACTION
  7_GOAL_DECOMPOSITION
  8_COMPLEXITY_ESTIMATION
  9_RISK_SCORING
  10_STRATEGY_SELECTION
  11_ARCHITECTURE_DESIGN
  12_PLAN_GENERATION
  13_SUBTASK_BREAKDOWN
  14_DEPENDENCY_GRAPH_BUILD
  15_HYPOTHESIS_GENERATION
  16_SIMULATION_ENGINE
  17_CONTRADICTION_DETECTION
  18_VALIDATION_LAYER
  19_REPLANNER_LOOP_si_score_menor_70
  20_DECISION_ENGINE
  21_CONFIDENCE_SCORING
  22_FUSION_ENSEMBLE
  23_FINAL_SYNTHESIS
  24_OUTPUT_GENERATION
  25_FEEDBACK_LOOP_STORAGE

ESCENARIO_4_TAREA_AVANZADA_30_a_50_pasos:
  incluye_los_25_del_escenario_3_mas:
    26_ALTERNATIVE_PATH_GENERATION
    27_SEARCH_EXPANSION
    28_REASONING_SWARM_PARALLEL
    29_CRITIC_SWARM_MULTI_PERSPECTIVE
    30_SELF_REFLECTION_LOOP
    31_FAILURE_MODE_ANALYSIS
    32_EDGE_CASE_GENERATION
    33_KNOWLEDGE_RETRIEVAL_EXTERNAL
    34_INSIGHT_EXTRACTION
    35_MEMORY_WRITE_SHORT_TERM
    36_MEMORY_WRITE_LONG_TERM
    37_OPTIMIZATION_PASS
    38_SOLUTION_RANKING
    39_SAFETY_CONSISTENCY_CHECK
  hasta_50_segun_complejidad_detectada
```

### COMPLEXITY ESTIMATOR

```yaml
evalua:
  - dependencias
  - ambiguedad
  - pasos_estimados
  - riesgo_de_error

formula_score: "(dependencias_x_2)_+_pasos_estimados_+_(5_si_ambiguo)_+_(5_si_alto_riesgo)"

niveles_y_accion:
  LOW_score_0_3:
    - 0_ciclos_Reasoner_o_Verifier
    - ejecucion_directa_sin_loops
    - ahorra_tokens_para_tareas_simples
  MEDIUM_score_4_8:
    - 1_ciclo_Reasoner_a_Verifier
    - verificacion_basica
  HIGH_score_9_15:
    - 2_ciclos_Reasoner_a_Verifier
    - motor_de_razonamiento_completo
  EXTREME_score_16_plus:
    - 3_ciclos_o_mas
    - motor_comleto_+_simulaciones_multiples
```

### 5 Fases Principales (FABLES)

```yaml
FASE_0_Orquestacion:
  - INPUT
  - DESCOMPOSICION_EN_25_A_100_TAREAS
  - ASIGNACION_A_FASES_1_a_5
  - CREACION_DE_LISTA_GLOBAL_INICIAL

FASE_1_Comprension_tareas_1_a_5:
  INPUT_LISTA_GLOBAL
  procesos:
    - entender_objetivo_real
    - reformular_problema_en_terminos_solucionables
    - construir_contexto_completo
    - identificar_restricciones_explicitas_e_implicitas
    - detectar_recursos_disponibles_y_cuellos_de_botella

FASE_2_Planificacion_tareas_6_a_10:
  INPUT_LISTA_GLOBAL_v1
  procesos:
    - elegir_estrategia_de_resolucion
    - disenar_arquitectura_de_la_solucion
    - descomponer_en_sub_tareas_atomicas
    - construir_grafo_de_dependencias
    - generar_roadmap_con_criterios_de_exito

FASE_3_Exploracion_Investigacion_tareas_11_a_16:
  INPUT_LISTA_GLOBAL_v2
  procesos:
    - generar_multiples_hipotesis_de_solucion
    - explorar_caminos_alternativos
    - simular_escenarios_y_edge_cases
    - detectar_modos_de_fallo
    - investigacion_externa

FASE_4_Validacion_tareas_17_a_21:
  INPUT_LISTA_GLOBAL_v3
  procesos:
    - detectar_errores_y_contradicciones_internas
    - generar_edge_cases_que_rompan_la_solucion
    - validacion_global_contra_todos_los_criterios
    - aplicar_correcciones_necesarias
    - score_de_confianza_si_score_menor_70_regresar_a_Fase_2

FASE_5_Sintesis_cruda_tareas_22_a_25:
  INPUT_LISTA_GLOBAL_v4
  procesos:
    - consolidar_todas_las_salidas_anteriores
    - integrar_hallazgos_de_todas_las_fases
    - generar_solucion_completa_cruda
    - preparar_para_el_CHEF_FINAL
```

### CHEF FINAL (4 Pasos)

```yaml
PASO_1_LISTA_TOTAL_3_pasadas:
  SALIDA_CRUDA_a_3_PASADAS_a_LISTA_COMPLETA_DE_TODO
  funcion: reconstruir_TODO_el_contenido_generado_no_resumir_no_perder_informacion

PASO_2_ARRastre_actualizacion_3_pasadas:
  INPUT_LISTA_P1_a_3_PASADAS_a_ARRASTRAR_P1_+_ACTUALIZAR_+_COMPLETAR_+_CORREGIR
  funcion: mantener_memoria_acumulada_no_reiniciar_contexto_mejorar_consistencia

PASO_3_Diseno_de_entrega_3_pasadas:
  INPUT_P1_+_P2_a_3_PASADAS_a_DISENO_DE_FORMATO_FINAL
  funcion: estructurar_presentacion_definir_como_se_entrega

PASO_4_Sintesis_final_analisis_total:
  INPUT_P1_+_P2_+_P3_a_ANALISIS_GLOBAL_COMPLETO_a_VERSION_FINAL_OPTIMIZADA
  funcion: revisar_todo_el_sistema_completo_cerrar_inconsistencias_producir_OUTPUT_FINAL
```

### LISTA_GLOBAL — 4 Reglas

```yaml
LISTA_GLOBAL: memoria_estructural_del_sistema

REGLA_1: se_crea_en_la_Fase_0_orquestacion
REGLA_2: se_actualiza_al_final_de_cada_fase
REGLA_3: se_arrastra_SIEMPRE_al_siguiente_paso
REGLA_4: NUNCA_se_reinicia_hasta_completar_el_ciclo

contiene: [tareas, estados, resultados, pendientes]
```


## DOC MASTER 12: PIPELINE + FASES (10 Fases — Detalle con FASE 0.5)

### Las 10 Fases del Pipeline (con FASE 0.5 ⭐)

```yaml
FASE_0_Pre_Boot:
  - verifica_entorno
  - carga_configuracion
  - inicializa_HF_Spaces
  - verifica_tokens_y_secrets

FASE_0.5_Confirmation_Gate_INTOCABLE:
  - muestra_plan_a_MAX
  - pide_confirmacion
  - bloquea_hasta_aprobacion
  REGLA_INTOCABLE: no_proceder_sin_aprobacion

FASE_1_Input_Reception:
  - recibe_input_de_MAX
  - detecta_canal
  - auth_-+_rate_limit
  - log_input

FASE_2_Input_Processing:
  - aplica_Input_Engine_v4.0
  - 54_componentes
  - genera_input_canonico

FASE_3_Planning:
  - genera_plan
  - descomposicion_de_tareas
  - asignacion_de_recursos
  - consensus_del_consejo

FASE_4_Execution:
  - ejecuta_tareas
  - monitoreo_continuo
  - 3_monitores_activos
  - repair_pipeline_si_falla

FASE_5_Validation:
  - CSA_audita_10_jueces_x_5_fases
  - SID_verifica_definicion
  - BIS_valida_skills

FASE_6_Refinement:
  - si_score_lt_95%_refina
  - iteracion_hasta_score_OK
  - maximo_N_iteraciones

FASE_7_Output_Generation:
  - aplica_Output_Engine
  - OOS_prepara_entrega
  - OVFS_estructura
  - 16_capas_gobernanza

FASE_8_Delivery:
  - multi_target_23_destinos
  - adaptive_format
  - confirmation_tracking

FASE_9_Monitoring:
  - post_delivery
  - feedback_loop
  - production_monitoring
  - auto_rollback_si_degrada
```

### 4 Escenarios de Ejecución

```yaml
Escenario_1_Tarea_Simple_9_pasos: Input_a_Parse_a_Plan_a_Execute_a_Validate_a_Refine_a_Output_a_Deliver_a_Monitor
Escenario_2_Tarea_Media_16_pasos: Input_a_Receive_a_Normalize_a_Parse_a_Validate_a_Intent_a_Context_a_Plan_a_Consensus_a_Execute_a_Monitor_a_Validate_a_Refine_a_Output_a_Deliver_a_Monitor
Escenario_3_Tarea_Compleja_25_pasos:
  pre_analisis_5_+_research_5_+_plan_5_+_execute_5_+_validate_5
Escenario_4_Tarea_Critica_30_a_50_pasos:
  pre_analisis_10_+_research_10_+_plan_10_+_execute_10_+_validate_10_+_pasos_adicionales_segun_necesidad
```

### COMPLEXITY ESTIMATOR (Categórico)

```python
def estimate_complexity(task):
    factors = {
        "length": len(task.input),
        "novelty": task.novelty_score,
        "dependencies": len(task.dependencies),
        "ambiguity": task.ambiguity_score,
        "risk": task.risk_score
    }
    return weighted_sum(factors)
```

```yaml
categorias:
  - 0_a_20: Simple  # TM01-TM02
  - 21_a_40: Media  # TM03-TM05
  - 41_a_60: Compleja  # TM06-TM08
  - 61_a_80: Avanzada  # TM09-TM10
  - 81_a_100: Critica  # TM11-TM12
```

### LISTA_GLOBAL — 4 Reglas

```yaml
regla_1: una_tarea_por_vez_principal  # no_paralelizar_tareas_de_la_misma_sesion_MAX
regla_2: tareas_independientes_en_paralelo
regla_3: tareas_dependientes_secuenciales  # si_A_depende_de_B_A_espera_a_B
regla_4: tareas_criticas_aisladas  # TM11_en_su_propio_contexto
```

### Checkpoints por Fase

```yaml
F0: pre_boot_state
F0.5: confirmation_state
F1: raw_input
F2: canonical_input
F3: plan_approved
F4: execution_log
F5: CSA_verdict
F6: refined_output
F7: output_sealed
F8: delivery_state
F9: post_delivery_state
```

### Diagrama Pipeline (Transversal)

```
F0_Pre_Boot
   ↓
F0.5_Confirmation_Gate_INTOCABLE  # bloquea_sin_aprobacion
   ↓
F1_Input_Reception
   ↓
F2_Input_Processing_54_componentes
   ↓
F3_Planning
   ↓
F4_Execution
   ↓
F5_Validation_CSA_+_SID_+_BIS
   ↓
F6_Refinement_si_score_lt_95%
   ↓
F7_Output_Generation_13_+_14_+_OVFS
   ↓
F8_Delivery_23_destinos
   ↓
F9_Monitoring_+_Feedback
```

### Estados por Fase

```yaml
estados_posibles:
  - PENDING
  - RUNNING
  - CHECKPOINTED
  - VALIDATED
  - FAILED
  - RECOVERING
  - COMPLETED
```

## DOC MASTER 08: LOOP v6.0 — 15 Capas + 3 Ciclos Paralelos

### 15 Capas del Loop

```yaml
Capa_01_Input_Loop: itera_hasta_Definition_Score_ge_95%
Capa_02_Plan_Loop: itera_hasta_consenso_del_consejo
Capa_03_Execute_Loop: itera_hasta_completion
Capa_04_Validate_Loop: itera_hasta_score_ge_95%
Capa_05_Repair_Loop: pipeline_5_pasos_para_reparar_fallos
Capa_06_Learn_Loop: extrae_lecciones_y_actualiza_memoria
Capa_07_Adapt_Loop: adapta_parametros_basado_en_resultados
Capa_08_Checkpoint_Loop: snapshots_firmados_cada_N_iteraciones
Capa_09_Consensus_Loop: ronda_de_votaciones_del_consejo
Capa_10_Monitor_Loop: 3_monitores_activos_PAD_Anxiety_Drift
Capa_11_Cost_Loop: monitorea_costo_y_ajusta_perfil_API
Capa_12_Escalate_Loop: escala_a_MAX_cuando_necesario
Capa_13_Rollback_Loop: rollback_automatico_si_degradacion
Capa_14_Deliver_Loop: itera_hasta_confirmacion
Capa_15_Feedback_Loop: recolecta_feedback_post_entrega
```

### 3 Ciclos Paralelos

```yaml
LOOP_A_Ejecucion_Principal:
  patron: Input_a_Plan_a_Execute_a_Validate_a_Deliver
  funcion: ciclo_de_produccion
  prioridad: alta
  bloqueante_para_otros: true

LOOP_B_Supervision_Watchdog:
  patron: Monitor_a_Detect_a_Alert_a_Decide_a_Act
  funcion: vigila_LOOP_A
  prioridad: media
  bloqueante: false

LOOP_C_Aprendizaje_Background:
  patron: Observe_a_Analyze_a_Extract_a_Store_a_Update
  funcion: aprende_de_LOOP_A_y_B
  prioridad: baja
  async: true
```

### Diagrama 3 Ciclos

```
            ┌─────────────────────────────┐
            │     LOOP A — EJECUCIÓN      │
            │  Input → Plan → Exec → Val  │
            └─────────────┬───────────────┘
                          │
            ┌─────────────▼───────────────┐
            │     LOOP B — SUPERVISIÓN    │
            │  Monitor → Detect → Alert   │
            └─────────────┬───────────────┘
                          │
            ┌─────────────▼───────────────┐
            │     LOOP C — APRENDIZAJE    │
            │  Observe → Analyze → Store  │
            └─────────────────────────────┘
```

### Coordinación entre Ciclos

```yaml
A_a_B_cada_5_segundos: LOOP_A_reporta_estado_a_LOOP_B
B_a_A_cuando_alerta: LOOP_B_puede_pausar_LOOP_A_si_detecta_problema
A_a_C_al_completar: LOOP_A_entrega_datos_a_LOOP_C_al_terminar
C_a_A_al_aprender: LOOP_C_actualiza_skills_o_reglas_que_LOOP_A_usa
```

### Patrones de Iteración

```yaml
secuencial: A1_a_B1_a_C1_a_A2_a_B2_a_C2
dag_paralelo: |
  ┌─ A1 ─┐
S ─►├─ A2 ─┤──► E
  └─ A3 ─┘
fractal: A1_eq_{A1.1, A1.2, A1.3_cada_uno_es_A_en_miniatura}
```

### Checkpoints y Rebuild

```yaml
checkpoint: cada_N_iteraciones_configurable_default_10
  - snapshot_del_state_completo
  - firmado_con_hash
  - almacenado_en_checkpoints/

rebuild: |
  state.restore(checkpoint_id="cp-2026-06-28-001")

rollback_automatico: si_loop_detecta_degradacion
  - encuentra_ultimo_checkpoint_bueno
  - restaura
  - reporta_incidente
```

### Pipeline Reparación (5 Pasos)

```yaml
paso_1_detect: identifica_tipo_de_fallo
paso_2_diagnose: diagnostica_causa_raiz
paso_3_patch: aplica_parche_correctivo
paso_4_verify: verifica_que_el_parche_funciona
paso_5_document: documenta_el_incidente_y_la_solucion
```

### 10 Propuestas M3 INPUT/LOOP Aplicadas

```yaml
1_Definition_Score_Gate: bloquea_si_lt_95%
2_Auto_Repair_Pipeline: pipeline_5_pasos
3_3_Cycle_Parallel: LOOP_A_+_B_+_C_en_paralelo
4_Checkpoint_Restore: sistema_de_checkpoints_firmados
5_Max_Mode_Sampling: K_samples_+_voto_en_decisiones_criticas
6_Goal_Stop: criterio_explicito_de_parada_antes_de_deliver
7_Dynamic_Workflow: workflow_que_se_adapta_mid_execution
8_Multi_Source_Research: investigacion_con_5_fuentes
9_Deterministic_90_10: 90%_codigo_/_10%_LLM
10_Pre_Analysis_Seed: pipeline_5_pasos_antes_de_empezar
```

### Métricas del Loop

```yaml
metricas:
  - latencia_media_por_iteracion
  - iteraciones_promedio_por_tarea
  - tasa_de_exito_por_capa
  - fallos_por_capa
  - tiempo_total_de_loop
  - checkpoints_generados
  - rollbacks_ejecutados
```


## DOC MASTER 07: OUTPUT ENGINE + OOS v3.1 + OVFS + 16 Capas Gobernanza

### Output Engine (13 Componentes)

```yaml
1_Output_Composer: combina_artefactos_parciales_en_output_unificado
2_Format_Selector: elige_formato_MD_JSON_YAML_codigo_binario
3_Template_Engine: aplica_templates_pre_aprobados
4_Quality_Booster: mejora_calidad_final_del_output
5_Consistency_Checker: verifica_consistencia_entre_secciones
6_Citation_Builder: construye_citas_a_fuentes
7_Metadata_Injector: inyecta_metadata_al_output
8_Compression_Engine: comprime_si_necesario_sin_perder_info
9_Encryption_Layer: encripta_secretos_detectados
10_Versioning_System: versiona_cada_output_semver
11_Preview_Generator: genera_preview_antes_de_entregar
12_Final_Validator: ultima_pasada_de_validacion
13_Delivery_Orchestrator: coordina_entrega_a_multiples_destinos
```

### OOS — Output Orchestration System v3.1 (14 Componentes)

```yaml
OOS-01_Multi_Target_Router: distribuye_output_a_multiples_destinos_en_paralelo
OOS-02_Channel_Adapter: adapta_output_a_cada_canal_Telegram_API_etc
OOS-03_Format_Converter: convierte_entre_formatos_segun_destino
OOS-04_Size_Limiter: limita_tamano_segun_canal_Telegram_4096_chars
OOS-05_Throttler: controla_velocidad_de_envio
OOS-06_Retry_Logic: reintentos_con_backoff_exponencial
OOS-07_Acknowledgment_Tracker: rastrea_confirmacion_de_recepcion
OOS-08_Priority_Queue: cola_priorizada_para_outputs_urgentes
OOS-09_Feedback_Collector: recolecta_feedback_post_entrega
OOS-10_Output_Score: score_de_calidad_del_output_ge_95%_requerido
OOS-11_Comparison_Engine: compara_outputs_similares_deduplicacion
OOS-12_History_Writer: escribe_historial_de_outputs
OOS-13_Rollback_Trigger: dispara_rollback_si_output_falla
OOS-14_Adaptive_Learning: aprende_patrones_de_preferencia_de_MAX
```

### OVFS — Output Virtual File System

```yaml
proposito: capa_de_abstraccion_que_permite_tratar_todos_los_outputs_como_archivos_en_un_filesystem_virtual

estructura:
  /ovfs/:
    projects/:
      "{project_id}/":
        artifacts/
        deliverables/
        reports/
    skills/:
      "{skill_id}/":
        outputs/
        examples/
    users/:
      "{user_id}/":
        outputs/
    system/:
      logs/
      checkpoints/
      state/
    temp/

caracteristicas:
  - sistema_de_archivos_virtual
  - path_jerarquico
  - operaciones: [read, write, list, delete, move]
  - versioning_automatico
  - metadata_embebida
  - accesible_via_MCP
```

### OUTPUT v6.1 — 16 Capas de Gobernanza

```yaml
A_Pre_Output_Audit: verifica_CSA_antes_de_emitir
B_Confidence_Check: score_ge_95%_requerido
C_Compliance_Check: cumple_constitucion_+_SID_+_BIS
D_Security_Scan: sin_secretos_sin_codigo_malicioso
E_Consistency_Verification: consistencia_entre_secciones
F_Provenance_Embedding: incrusta_origen_y_chain_of_custody
G_Version_Locking: versiona_y_lock_el_output
H_Multi_Channel_Validation: valida_para_cada_canal_destino
I_Rollback_Preparation: prepara_rollback_automatico
J_Output_Score_Calculation: calcula_score_final
K_Adaptive_Format_Selection: selecciona_formato_segun_historial
L_Delivery_Path_Selection: elige_ruta_optima_de_entrega
M_Recipient_Verification: verifica_destinatario
N_Delivery_Confirmation: confirma_recepcion
O_Post_Delivery_Monitoring: monitorea_post_entrega
P_Feedback_Loop_Trigger: dispara_feedback_loop
```

### Estados del Output Governor (8 Estados)

```yaml
flujo: |
  DRAFT → VALIDATING → APPROVED → DELIVERING
            ↓                          ↓
          (rechaza)               DELIVERED → MONITORED
                                         ↓
                                   ACCEPTED_o_REJECTED
                                          ↓
                                  (Rollback_si_rejected)
```

### 9 Propuestas M3 Aplicadas (OUTPUT)

```yaml
6.1_Pre_Mortem_Analysis: antes_de_output_simula_que_podria_fallar_reduce_fallos_70%
6.2_Auto_Rollback: si_output_falla_rollback_automatico_al_ultimo_bueno
6.3_Meta_Learning_Output: aprende_que_outputs_fueron_aceptados_o_rechazados
6.4_Personalization: adapta_formato_segun_preferencia_de_MAX
6.5_Multi_Stakeholder_Output: genera_versiones_para_diferentes_audiencias
6.6_Causal_Tracing: cada_output_tiene_cadena_causal_completa
6.7_Marketplace_Output: outputs_pueden_ser_compartidos_como_skills
6.8_Self_Improving_Output: cada_output_mejora_al_siguiente_similar
6.9_Production_Monitoring_Output: monitorea_outputs_en_produccion
RECHAZADA_Output_Sandbox: no_se_implementa
```

### Multi-Target Delivery (23 Destinos)

```yaml
destinos_principales:
  1_Telegram_texto
  2_Telegram_archivo
  3_API_REST_JSON
  4_API_REST_archivo
  5_GitHub_commit
  6_GitHub_PR
  7_GitHub_issue
  8_HF_Space_deploy
  9_HF_Dataset_upload
  10_Email_texto
  11_Email_HTML
  12_Webhook
  13_Dashboard_live
  14_Dashboard_snapshot
  15_Discord
  16_Slack
  17_Local_file
  18_S3_compatible_storage
  19_Cloudflare_R2
  20_Notion
  21_Google_Drive
  22_Drive_node_interno
  23_Custom_MCP_target

seleccion_adaptativa: el_sistema_aprende_cual_destino_prefiere_MAX_para_cada_tipo_de_output
```

