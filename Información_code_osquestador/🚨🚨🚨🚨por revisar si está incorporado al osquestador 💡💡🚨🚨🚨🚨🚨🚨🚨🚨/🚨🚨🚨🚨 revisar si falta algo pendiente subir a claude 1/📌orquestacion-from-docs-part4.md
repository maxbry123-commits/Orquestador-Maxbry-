# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 4)

> **Continuación** de part1, part2 y part3. Algunos archivos grandes y específicos.


## DOC 4: SISTEMAS DE RAZONAMIENTO (EURS + Mythos + OpenMythos)

### EURS — External Universal Reasoning System

```yaml
modo_Standard_5_capas_+_12_pasos:
  5_capas:
    C1_Analisis_del_problema
    C2_Generacion_de_hipotesis
    C3_Evaluacion_de_hipotesis
    C4_Sintesis_de_solucion
    C5_Verificacion_final
  12_pasos:
    P01_parsear_input
    P02_identificar_conceptos_clave
    P03_establecer_relaciones
    P04_generar_3_hipotesis
    P05_buscar_evidencia
    P06_evaluar_cada_hipotesis
    P07_combinar_resultados
    P08_construir_solucion
    P09_validar_coherencia
    P10_verificar_completitud
    P11_formatear_output
    P12_reportar
  cuando_se_usa: tareas_simples_a_medianas_recursos_limitados_respuesta_rapida

modo_Turbo_12_capas_+_45_pasos:
  12_capas:
    C01_parsing_profundo
    C02_descomposicion
    C03_contextualizacion
    C04_generacion_exhaustiva_de_hipotesis
    C05_busqueda_multi_fuente
    C06_evaluacion_rigurosa
    C07_sintesis_avanzada
    C08_diseno_de_solucion
    C09_implementacion
    C10_validacion_multiple
    C11_refinamiento
    C12_certificacion
  45_pasos: distribucion_entre_12_capas_3_a_4_pasos_promedio_por_capa
  cuando_se_usa: tareas_criticas_decisiones_arquitectonicas_problemas_complejos_cuando_MAX_pide_maxima_calidad

comparacion: |
  STANDARD: 5_capas_+_12_pasos_a_rapido_80%_cobertura
  TURBO: 12_capas_+_45_pasos_a_lento_99%_cobertura
```

### Micro-Ciclo por Paso (7 Pasos)

```yaml
aplicado_internamente_en_cada_paso_del_razonamiento:
  objetivo → plan → subplan → ejecucion → verificacion → correccion → resultado

proposito: cada_paso_individual_sea_verificable_y_corregible_antes_de_avanzar_al_siguiente
```

### Capa Externa — Nombre

```yaml
capa_externa_de_codigo_sobre_una_LLM_suele_llamarse:
  - Orchestrator
  - Agent_Framework
  - Cognitive_Layer
  - Reasoning_Engine

coordinando_varios_agentes: Multi_Agent_System
cambiando_forma_de_razonar: Reasoning_Engine

para_este_diseno: Mythos_Cognitive_Layer_o_Mythos_Reasoning_Engine  # define_como_trabaja_el_modelo_no_el_modelo_en_si
```

### Arquitectura de Control Alto (Cadena Completa)

```
MYTHOS → FSM → ROUTER → SHERIFF → SENTINEL → VERIFIER → CRITIC → JUDGE → POLICY_ENGINE → PYDANTICAI → RETRY_ENGINE → LLM
```

### Stack Técnico (4 Lenguajes + Roles)

```yaml
JSON: define_reglas
Python: ejecuta_logica
DSL: define_workflows
YAML: configuracion

cadena_tecnica: MYTHOS_a_PYTHON_a_FSM_a_ROUTER_a_LLM
```

### PydanticAI (Cadena Completa)

```
LLM_a_JSON_valido_a_Schema_valido_a_Python_valido

proposito: convierte_la_salida_del_LLM_en_estructuras_de_datos_Python_validadas_y_tipadas  # garantiza_que_el_output_del_LLM_sea_procesable_por_codigo_determinista
```

### FSM Finite State Machine

```yaml
estados: PLAN_a_CODE_a_TEST_a_CRITIC_a_REPLAN_a_FIN

proposito: define_en_que_estado_esta_el_sistema_en_cada_momento_y_que_transiciones_son_validas_no_permite_saltar_estados_arbitrariamente
```

### Separación de Capas (5 Niveles)

```yaml
PENSAMIENTO: como_se_analiza_y_resuelve  # MYTHOS
CONTROL: que_ejecutar_cuando_validar  # FSM_o_Router
EJECUCION: como_se_ejecuta_el_codigo  # Coder_o_Sandbox
PERSISTENCIA: como_se_guarda_el_estado  # DB_o_JSON
AUTOCORRECCION: como_se_repara_un_fallo  # Repairer

cada_capa_tiene_una_responsabilidad_unica_no_se_mezclan_entre_si
```

### DRE Pipeline (9 Pasos)

```yaml
INPUT_a_COMPLEXITY_ESTIMATOR_a_PLANNER_a_REASONER_a_SELF_CHECK_a_REASONER_a_SELF_CHECK_a_SYNTHESIS_a_OUTPUT

COMPLEXITY_ESTIMATOR_evalua:
  - dependencias
  - ambiguedad
  - pasos_estimados
  - riesgo_de_error
```

### OpenMythos (Prelude → Loop → Coda)

```yaml
tipo: sistema_de_razonamiento_recurrente_de_codigo_abierto_con_Recurrent-Depth_Transformer_y_tres_etapas

PRELUDE:
  - bloques_transformer_estandar
  - pre_procesa_el_input_antes_del_loop_recurrente
  - equivalente_a_las_Fases_0-1_comprension

RECURRENT_BLOCK_en_loop_hasta_max_loop_iters:
  - nucleo_de_razonamiento_recurrente
  - cada_iteracion_del_loop_es_el_equivalente_funcional_de_un_paso_de_chain_of_thought_en_espacio_latente_continuo
  - mas_bucles_en_inferencia_eq_cadenas_de_razonamiento_mas_profundas
  - mas_bucles_eq_problemas_mas_dificiles_resueltos
  - equivalente_a_las_Fases_2-4_planificacion_exploracion_validacion

CODA:
  - refinamiento_final_de_la_salida
  - transforma_el_razonamiento_latente_en_output
  - equivalente_a_la_Fase_5_+_CHEF_FINAL

concepto_clave: el_sistema_puede_dedicar_mas_computo_a_problemas_mas_dificiles_ajustando_el_numero_de_iteraciones_del_Recurrent_Block  # razonamiento_escalado_en_inferencia_inference_time_scaling
```

### Optimizar Para (Lista 8 Criterios)

```yaml
1_calidad
2_robustez
3_recuperacion
4_persistencia
5_escalabilidad
6_auditoria
7_control
8_evolucion_futura

NO_optimizar_para:
  - velocidad
  - simplicidad
```

### Core Plantilla Fija + Adaptadores

```yaml
MYTHOS_CORE_plantilla_fija_nunca_cambia:
  - los_40_pasos_base
  - las_5_fases
  - la_LISTA_GLOBAL
  - el_CHEF_FINAL_4_pasos
  - el_DRE_estimador_de_complejidad

ADAPTADOR_cambia_segun_el_caso_de_uso:
  - que_pasos_activar_segun_el_escenario
  - cuantas_iteraciones_del_Recurrent_Loop
  - que_herramientas_externas_usar
  - que_formato_de_salida_generar

casos_de_uso:
  - Codigo_a_Adaptador_Code
  - Investigacion_a_Adaptador_Research
  - Analisis_a_Adaptador_Analysis
  - Diseno_a_Adaptador_Design

ejecucion: FABLES_CORE_+_Adaptador_[tipo]_a_comportamiento_especifico_para_cada_caso_sin_tocar_el_nucleo_central
```

### Distinción Razonamiento vs Control

```yaml
PENSAMIENTO_MYTHOS_o_FABLES:
  - define_como_se_analiza_y_resuelve_un_problema
  - genera_estrategias_y_soluciones
  - pertenece_al_RAZONAMIENTO

CONTROL_FSM_o_Router_o_PydanticAI:
  - decide_que_ejecutar_cuando_validar_y_cuando_reintentar
  - garantiza_que_el_proceso_se_ejecute_correctamente
  - pertenece_al_CONTROL

sistema_avanzado_tiene_AMBOS:
  - el_pensamiento_genera_estrategias_y_soluciones
  - el_control_garantiza_que_el_proceso_se_ejecute_correctamente
  
son_capas_DIFERENTES_que_trabajan_juntas_no_se_mezclan_no_se_reemplazan_entre_si
```

### Restricciones / Recursos / Cuellos / Riesgos / Supuestos Falsos

```yaml
RESTRICCIONES:
  - ¿qué_no_puede_cambiar?
  - ¿qué_limites_son_inamovibles?
  - ¿qué_dependencias_externas_existen?

RECURSOS:
  - ¿qué_tiene_el_sistema_disponible?
  - ¿qué_tokens_tiene_por_ciclo?
  - ¿qué_memoria_puede_usar?
  - ¿qué_herramientas_externas_puede_llamar?

CUELLOS_DE_BOTELLA:
  - ¿dónde_se_va_a_atascar_el_sistema?
  - ¿qué_pasos_son_los_más_lentos?
  - ¿qué_pasos_consumen_más_tokens?
  - ¿dónde_puede_romperse_la_cadena?

RIESGOS:
  - ¿qué_puede_fallar_silenciosamente?
  - ¿qué_fallo_tiene_mayor_impacto?
  - ¿qué_es_difícil_de_recuperar?

SUPUESTOS_FALSOS:
  - ¿qué_estamos_asumiendo_que_puede_no_ser_cierto?
  - ¿qué_funciona_en_teoría_pero_no_en_producción?
  - ¿qué_asumimos_del_LLM_que_no_siempre_se_cumple?
```

### 7 Validadores y su Orden Óptimo (Pregunta Pendiente)

```yaml
validadores_disponibles:
  - Verifier
  - Critic
  - Judge
  - Sentinel
  - Sheriff
  - Policy_Engine
  - PydanticAI

pregunta_pendiente: ¿cuál_es_el_orden_óptimo_de_estos_validadores?
```


## DOC 11: MYTHOS 40 PASOS + FABLES 5 FASES + Arquitectura de Capas

### MYTHOS 40 Pasos (Cadena Completa)

```yaml
PASO_01: INPUT
PASO_02: INTENT_PARSING
PASO_03: PROBLEM_FRAMING
PASO_04: DOMAIN_DETECTION
PASO_05: CONTEXT_BUILDING
PASO_06: CONSTRAINT_EXTRACTION
PASO_07: GOAL_DECOMPOSITION
PASO_08: COMPLEXITY_ESTIMATION
PASO_09: RISK_SCORING
PASO_10: STRATEGY_SELECTION
PASO_11: ARCHITECTURE_DESIGN
PASO_12: PLAN_GENERATION
PASO_13: SUBTASK_BREAKDOWN
PASO_14: DEPENDENCY_GRAPH_BUILD
PASO_15: HYPOTHESIS_GENERATION_multiple
PASO_16: ALTERNATIVE_PATH_GENERATION
PASO_17: SEARCH_EXPANSION
PASO_18: REASONING_SWARM_paralelo
PASO_19: CONTRADICTION_DETECTION
PASO_20: CRITIC_SWARM_multi_perspectiva
PASO_21: SELF_REFLECTION_LOOP
PASO_22: FAILURE_MODE_ANALYSIS
PASO_23: SIMULATION_ENGINE_escenarios_x_N
PASO_24: EDGE_CASE_GENERATION
PASO_25: VALIDATION_LAYER
PASO_26: KNOWLEDGE_RETRIEVAL_external_context
PASO_27: INSIGHT_EXTRACTION
PASO_28: MEMORY_WRITE_short_term
PASO_29: MEMORY_WRITE_long_term
PASO_30: REPLANNER_LOOP
PASO_31: OPTIMIZATION_PASS
PASO_32: DECISION_ENGINE
PASO_33: CONFIDENCE_SCORING
PASO_34: SOLUTION_RANKING
PASO_35: FUSION_o_ENSEMBLE_SOLUTION
PASO_36: SAFETY_o_CONSISTENCY_CHECK
PASO_37: FINAL_SYNTHESIS
PASO_38: OUTPUT_GENERATION
PASO_39: POST_OUTPUT_AUDIT
PASO_40: FEEDBACK_LOOP_STORAGE
```

### MYTHOS Descripción Corta (12 Pasos)

```yaml
INPUT → INTENT_PARSING → FRAMING → DECOMPOSE → HYPOTHESES → SWARM →
CRITIC → SIMULATION → MEMORY → REPLANNER → DECISION → SYNTHESIS → AUDIT

INPUT: entrada
INTENT_PARSING: interpreta_intencion_real
FRAMING: define_problema_real
DECOMPOSE: divide_en_partes
HYPOTHESES: genera_soluciones_multiples
SWARM: razona_en_paralelo
CRITIC: detecta_errores_y_contradicciones
SIMULATION: prueba_escenarios
MEMORY: guarda_aprendizajes
REPLANNER: ajusta_estrategia
DECISION: elige_mejor_solucion
SYNTHESIS: construye_respuesta_final
AUDIT: revisa_calidad_final
```

### Ficha de Componente

```yaml
campos_de_ficha:
  OBJETIVO: que_hace_este_componente
  UBICACION: en_que_capa_vive  # ejemplo: 2.3_ROUTER_vive_en_2.0_CONTROL
  JUSTIFICACION: por_que_existe_este_componente_que_problema_resuelve
  DEPENDENCIAS: de_que_otros_componentes_depende
  ENTRADAS: que_recibe_este_componente
  SALIDAS: que_produce_este_componente
  IMPLEMENTACION: que_tecnologia_usa  # DSL_o_JSON_o_Python_etc
  EDITABLE: SI_o_NO  # si_se_puede_cambiar_sin_romper_el_sistema
  CRITICO: SI_o_NO  # si_falla_el_sistema_se_detiene
```

### Ejemplo de Ficha: 2.3_ROUTER

```yaml
OBJETIVO: seleccionar_flujo_y_recursos_adecuados
UBICACION: 2.0_CONTROL  # 📂
JUSTIFICACION: evita_logica_dispersa_y_centraliza_decisiones
DEPENDENCIAS: [FSM, Policy_Engine]
ENTRADAS: [Task, Contexto]
SALIDAS: ruta_seleccionada
IMPLEMENTACION: DSL_+_JSON_+_Python
EDITABLE: SI
CRITICO: SI
```

### 5 Fases FABLES (Versión Corta)

```yaml
FASE_0_Orquestacion:
  patron: INPUT_a_DESCOMPOSICION_EN_25_A_100_TAREAS_a_ASIGNACION_A_FASES_1_a_5_a_CREACION_DE_LISTA_GLOBAL_INICIAL
  salida:
    - mapa_completo_de_tareas
    - estructura_de_fases_asignadas
    - LISTA_GLOBAL_v0_inicializada
  reglas:
    - minimo_25_tareas_maximo_100
    - cada_tarea_va_a_exactamente_una_fase
    - LISTA_GLOBAL_se_crea_aqui_y_nunca_se_reinicia

FASE_1_Comprension_tareas_1_a_5:
  - entender_objetivo_real
  - reformular_problema
  - construir_contexto_completo
  - identificar_restricciones
  - detectar_recursos_disponibles

FASE_2_Planificacion_tareas_6_a_10:
  - elegir_estrategia_de_resolucion
  - disenar_arquitectura_de_la_solucion
  - descomponer_en_sub_tareas_atomicas
  - construir_grafo_de_dependencias
  - generar_roadmap_con_criterios_de_exito

FASE_3_Exploracion_Investigacion_tareas_11_a_16:
  - generar_multiples_hipotesis_de_solucion
  - explorar_caminos_alternativos
  - simular_escenarios_y_edge_cases
  - detectar_modos_de_fallo
  - investigacion_externa

FASE_4_Validacion_tareas_17_a_21:
  - detectar_errores_y_contradicciones
  - generar_edge_cases_que_rompan_la_solucion
  - validacion_global_contra_todos_los_criterios
  - aplicar_correcciones_necesarias
  - score_de_confianza_si_score_lt_70_regresar_a_Fase_2

FASE_5_Sintesis_cruda_tareas_22_a_25:
  - consolidar_todas_las_salidas_anteriores
  - integrar_hallazgos_de_todas_las_fases
  - generar_solucion_completa_cruda
  - preparar_para_CHEF_FINAL
```

### CHEF FINAL 4 Pasos

```yaml
PASO_1_Lista_Total_3_pasadas: SALIDA_CRUDA_a_3_PASADAS_a_LISTA_COMPLETA_DE_TODO  # reconstruir_TODO_no_resumir_no_perder_informacion
PASO_2_Arrastre_Actualizacion_3_pasadas: LISTA_P1_a_3_PASADAS_a_ARRASTRAR_P1_+_ACTUALIZAR_+_COMPLETAR_+_CORREGIR  # mantener_memoria_acumulada_no_reiniciar_contexto_mejorar_consistencia
PASO_3_Diseno_de_Entrega_3_pasadas: P1_+_P2_a_3_PASADAS_a_DISENO_DE_FORMATO_FINAL  # estructurar_presentacion_definir_como_se_entrega
PASO_4_Sintesis_Final_Analisis_Total: P1_+_P2_+_P3_a_ANALISIS_GLOBAL_COMPLETO_a_VERSION_FINAL_OPTIMIZADA  # revisar_todo_el_sistema_completo_cerrar_inconsistencias_producir_OUTPUT_FINAL
```

### V1 / V2 / V3 → Comparador → Judge → Ganador

```yaml
VERSIÓN_1:
  primera_propuesta_sin_filtros_lo_que_naturalmente_se_disenaria

VERSIÓN_2:
  una_arquitectura_alternativa_radicalmente_diferente
  si_V1_es_secuencial_V2_es_paralela
  si_V1_es_jerarquica_V2_es_plana

VERSIÓN_3:
  una_arquitectura_hibrida_que_tome_lo_mejor_de_V1_y_V2_y_elimine_sus_debilidades

COMPARADOR:
  tabla_comparativa_objetiva_con_metricas:
    - complejidad_de_implementacion_1_a_10
    - robustez_ante_fallos_1_a_10
    - capacidad_de_recuperacion_1_a_10
    - escalabilidad_1_a_10
    - mantenibilidad_1_a_10
    - control_sobre_el_LLM_1_a_10

JUDGE:
  con_base_en_COMPARADOR_decide:
    - cual_version_gana_en_cada_criterio
    - cual_es_la_ganadora_global
    - que_elementos_de_las_perdedoras_conservar

GANADOR:
  arquitectura_ganadora_con_todas_las_mejoras_integradas_y_el_codigo_ejecutable_completo
```

### Refutación (Bloque X — Desafiar la Arquitectura)

```yaml
DESAFIAR_LA_ARQUITECTURA_a_CRITIC:
  - ¿Qué_está_mal_en_esta_arquitectura?
  - ¿Qué_supuestos_son_falsos?
  - ¿Qué_está_sobre_disenado?
  - ¿Qué_está_sub_disenado?

COUNTER_CRITIC:
  - ¿Cuáles_de_las_críticas_anteriores_son_válidas?
  - ¿Cuáles_son_exageradas?
  - ¿Cuáles_se_resuelven_con_cambios_menores?
  - ¿Cuáles_requieren_rediseno_completo?

FAILURE_SIMULATOR:
  simula_como_falla_esta_arquitectura_en:
    - uso_normal_tarea_simple
    - uso_extremo_tarea_compleja_de_30_a_50_pasos
    - fallo_de_un_componente_critico
    - perdida_de_contexto_a_mitad_del_proceso
    - modelo_LLM_que_alucina_en_el_paso_20_de_40
    - saturacion_de_memoria_en_proceso_de_24_horas

ARQUITECTURA_MEJORADA:
  con_base_en_Critic_+_Counter_Critic_+_Failure_Simulator_proponer_la_arquitectura_mejorada_que_sobrevive_todos_los_escenarios_de_fallo

REGLA: no_asumir_que_MYTHOS_esta_correcto_hacer_refutacion_contra_el_mismo_antes_de_decidir
```

### Determinista vs Probabilístico

```yaml
determinista_codigo_duro:
  - output_siempre_igual_dado_el_mismo_input
  - se_puede_testear_con_unit_tests
  - no_requiere_LLM
  ejemplos: FSM_grafo_dependencias_score_de_confianza_persistencia

probabilistico_LLM:
  - output_varia_segun_contexto
  - requiere_capacidad_de_razonamiento_semantico
  - no_se_puede_predecir_exactamente
  ejemplos: reformulacion_del_problema_generacion_de_hipotesis_sintesis_final
```

### Preguntas de Separación (Código vs Workflow vs Config vs Razonamiento)

```yaml
que_partes_deberian_ser_codigo:
  - logica_ejecutable
  - transformaciones_de_datos
  - validaciones_deterministas

que_partes_deberian_ser_workflow:
  - flujos_de_trabajo
  - secuencias_de_pasos

que_partes_deberian_ser_configuracion:
  - settings
  - parametros
  - constantes

que_partes_deberian_ser_razonamiento:
  - decisiones_complejas
  - analisis_semantico
```

### Cómo Diseñar un Core Estable

```yaml
principio: el_nucleo_de_control_y_razonamiento_debe_ser_FIJO_los_adaptadores_deben_ser_INTERCAMBIABLES

asi_puedes_cambiar_todo_el_comportamiento_sin_tocar_el_codigo_central

es_mas_facil_de:
  - mantener
  - probar
  - mejorar
```

### OpenMythos Integrado con FABLES

```yaml
flujo:
  FABLES_5_fases_a_PRELUDE_comprension_Fase_0-1_a_RECURRENT_LOOP_razonamiento_Fases_2-4_controlado_por_DRE_COMPLEXITY_ESTIMATOR_a_CODA_sintesis_Fase_5_+_CHEF_FINAL
```

### Respuesta de FABLE sobre Structured CoT

```yaml
diagrama: |
  ENTRADA_prompt_+_contexto
       ↓
  ┌─────────────────────┐
  │ FASE_DE_PENSAMIENTO │ ← tokens_internos_no_visibles
  │ 1. Entender_tarea    │
  │ 2. Descomponer       │
  │ 3. Explorar_opciones │
  │ 4. Auto_verificar    │
  │ 5. Corregir_errores  │
  └─────────────────────┘
       ↓
  RESPUESTA_FINAL_visible

punto_clave: todo_eso_es_el_mismo_proceso_de_generacion_de_texto_no_hay_modulos_separados_el_modelo_aprendio_durante_el_entrenamiento_a_razonar_en_borrador_antes_de_responder

json_formato: |
  {
    "instrucciones": "Antes_de_responder_ejecuta_estas_fases_en_orden",
    "fases": [
      {"f1": "Reformula_la_tarea_en_tus_palabras"},
      {"f2": "Lista_los_sub_problemas"},
      {"f3": "Resuelve_cada_uno"},
      {"f4": "Verifica_contradicciones_falta_algo"},
      {"f5": "Respuesta_final_en_formato_X"}
    ],
    "regla": "Marca_cada_fase_con_su_etiqueta_antes_de_avanzar"
  }

importancia: esto_se_llama_structured_chain_of_thought_mejora_mucho_los_modelos_pequenos_que_tienden_a_saltar_directo_a_la_respuesta_es_totalmente_legitimo_es_ingenieria_de_prompts_estandar
```

### Arquitectura MAXBRY

```yaml
USUARIO_a_MAXBRY_a_Control_Layer_a_Workflow_Layer_a_Memory_Layer_a_Tool_Layer_a_LLM_Layer

MAXBRY_NO_es_una_nueva_LLM
MAXBRY_NO_es_un_modelo_fundacional
MAXBRY_NO_compite_con_Claude_GPT_Gemini_Qwen

MAXBRY_es_una_CAPA_EXTERNA_DE_ORQUESTACION_CONTROL_Y_ORGANIZACION
MAXBRY_vive_fuera_de_los_modelos
MAXBRY_coordina_modelos_herramientas_proyectos_y_objetivos
```


## DOC MASTER 26: NOMBRES ESPECÍFICOS + ARCHIVOS + ESQUEMAS (Detalle Esquemas + Archivos)

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

### Ubicaciones y Sincronización

```yaml
paths:
  - /workspace/orquestador/* → git_push → nct-consensus-log/main/orquestador/
  - /workspace/compartido/* → git_push → nct-consensus-log/main/compartido/

sincronizacion:
  - git_pull_cada_30_segundos
  - git_push_cada_5_minutos
  - o_cuando_hay_commit_importante
```

### 8 Archivos del Coordinador NCT + 5 Soporte

```yaml
los_8_principales:
  fsm_py: orquestador_10_fases
  classifier_py: clasificacion_dual
  router_py: modo_o_ruta
  planner_py: descomposicion
  context_isolator_py: contexto_aislado
  worker_pool_py: workers_unica_con_IA
  monitor_py: PAD_+_Ansiedad_+_Drift
  verifier_py: 3_capas

los_5_archivos_soporte:
  consolidator_py: consolida_resultados
  repair_py: repair_pipeline_5_pasos
  deliver_py: multi_target_delivery
  state/engine_py: engine_de_estado
  state/telemetry_py: telemetria
```

### G6 Staff — 5 Agentes Principales (Versión 6 con Code Agent CLI)

```yaml
5.1_MiniMax_M3_LLM_principal:
  via: NVIDIA_NIM
  cargo: lider_del_G5_SKYNER
  rol: arquitecto

5.2_MiMo_Code:
  ubicacion: HF_aparte
  funcion: code_agent_paralelo_tareas_horizonte_largo

5.3_OpenCLAW:
  rol: agente_adicional_multi_canal
  stars: 308K

5.4_Smolagents:
  rol: agente_adicional_tareas_generales
  ubicacion: HuggingFace

5.5_Hermes_Agent:
  rol: archivist_+_memoria
  stars: 149K
  learning_loop: L1+L2+L3

5.6_Code_Agent_CLI:
  variantes: [Aider, Cline]
  instalado: true
  fallback_para_MiMo: true
```

### 3 Monitores con Umbrales Específicos

```yaml
PAD_Monitor:
  pleasure_arousal_dominance:
    arousal_gt_0.8_AND_pleasure_lt_0.2: SIGKILL_+_Respawn

Ansiedad_Monitor:
  niveles:
    bajo: confirma
    medio: confirma_+_alerta
    alto: respawn

Anti_Drift_Monitor:
  KL_divergence_gt_0.02: halt_+_rollback_compara_con_baseline
```

### Fases del Orquestador (KIMI K + MINIMAX)

```yaml
FASE_0: Clasificacion_Dual_intencion_+_tipo_de_tarea_primera_lectura
FASE_1: Seleccion_de_Modo_y_Ruta_manual_semi_continuo_identifica_ruta_optima
FASE_2: Skills_y_Descomposicion_BIS_lookup_descomposicion_de_tareas
FASE_3: Aislamiento_y_Preparacion_contexto_aislado_estado_limpio
FASE_4: Ejecucion_Unica_con_IA_ejecuta_tareas_worker_pool_activo
FASE_5: Monitoreo_Simultaneo_PAD_Ansiedad_Anti_Drift
FASE_6: Verificacion_3_Capas_Adversarial_Cruzada_Maker_Checker
FASE_7: Consolidacion_Jerarquica_EROS_3_tier_tier_1_inmediato_tier_2_sesion_tier_3_proyecto
FASE_8: Repair_Pipeline_5_pasos_retry_compression_fallback_restore_escalate
FASE_9: Consolidacion_Final_y_Entrega_multi_target_delivery_reporte_a_MAX
```

### 16 Mejores Prácticas de EROSTAS

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
  9_cola_con_prioridad_Urgente
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

### 20 Propuestas de Mejora 100X

```yaml
1_encryption_de_keys_vault
2_backup_automatico_cada_1h
3_health_checks_cada_60s
4_logs_centralizados
5_webhooks_para_notificaciones_externas
6_versionado_de_prompts
7_A_o_B_testing_de_modelos
8_cost_monitoring_real_time
9_rate_limiting_por_key
10_auto_scaling_si_API_saturada
11_retry_policy_configurable
12_modo_dry-run
13_modo_test
14_dashboard_web_para_MAX
15_export_reportes_PDF_o_MD
16_alertas_Telegram_criticas
17_modo_pause
18_historial_de_decisiones
19_sistema_de_roles_o_permisos
20_sandbox_para_codigo_pre_commit
```

### Keys Separadas por Archivo

```yaml
estructura_secretos:
  /workspace/secrets/:
    nvidia-nim-01.json
    nvidia-nim-02.json
    nvidia-nim-03.json
    nvidia-nim-04.json
    cerebras-01.json
    "..."
    groq-01.json
    "..."
    loader.py

principio: cada_API_key_en_archivo_individual_con_loader.py_para_cambiar_una_key_no_se_toca_el_orquestador
```

### Parches Operacionales

```yaml
14.1_CIRCUIT_BREAKER:
  estados: CLOSED_o_OPEN_o_HALF_OPEN
  failure_threshold: 5_fallos_en_60s
  recovery_timeout: 30s
  libreria: pybreaker
  por_servicio: [NVIDIA_NIM, Cerebras, Groq, HF_local]

14.2_FREE_TIER_cost_target_$0:
  HF_Spaces_CPU_Basic: 16GB_RAM
  APIs: NVIDIA_NIM_free, Cerebras_free, Groq_free
  tecnicas: cache_fallback_batch_monitor_circuit_breaker_por_costo

14.3_TELEGRAM_1_bot_multi_topic:
  topics:
    - "#nct-fase0"
    - "#interfaz-fusionada"
    - "#crazy-wall"
    - "#consenso"
    - "#consensus-log"

14.4_CHROMADB_vector_DB_principal:
  coleccion: nct_memory
  metric: cosine
  index: hnsw
  persistencia: disco

14.5_BGE_SMALL_EN_V1_5_embedding:
  HF: BAAI/bge-small-en-v1.5
  dim: 384
  size: 24MB
  alt: all-MiniLM-L6-v2

14.6_EMBEDDING_proceso:
  cada_documento_nuevo_a_bge-small_a_384-dim_a_ChromaDB
  retrieval_top-k_por_similitud_cosine
```


## DOC 2: ESTRUCTURA INTERNA DEL ORQUESTADOR (Detalle Versión Historial)

### 30 Micro-Agentes (Versión Original del Historial)

```yaml
categorias:
  1_5_Analisis: [input_parsing, intent, context, etc.]
  6_10_Planificacion: [task_breakdown, scheduling, etc.]
  11_15_Ejecucion: [delegacion, monitoring, retries, etc.]
  16_20_Validacion: [CSA_jueces_subset, quality, etc.]
  21_25_Aprendizaje: [memory, patterns, optimization, etc.]
  26_30_Meta: [orquestacion_de_orquestadores, recovery, etc.]

caracteristicas:
  - cada_uno_con_rol_especifico
  - trabajan_en_paralelo_sobre_bus_de_eventos
  - capacidad_de_invocarce_entre_si
  - auto_descubrimiento_de_capacidades
```

### 11 Roles Internos

```yaml
los_11_roles_internos:
  1_Director_de_Proyecto
  2_Planificador_Estrategico
  3_Asignador_de_Recursos
  4_Monitor_de_Estado
  5_Coordinador_de_Agentes
  6_Gestor_de_Dependencias
  7_Reconciliador_de_Conflictos
  8_Optimizador_de_Costos
  9_Gestor_de_Memoria
  10_Auditor_de_Procesos
  11_Gestor_de_Conocimiento
```

### 10 Colas Paralelas

```yaml
Q1_CRITICAL: emergencias_rollback
Q2_HIGH: tareas_de_MAX_directo
Q3_USER: inputs_del_usuario
Q4_VALIDATION: CSA_quality_checks
Q5_EXECUTION: tareas_activas
Q6_MONITORING: supervision
Q7_LEARNING: aprendizaje
Q8_MAINTENANCE: housekeeping
Q9_BACKGROUND: tareas_de_baja_prioridad
Q10_RESERVED: para_picos_de_carga

caracteristicas: procesamiento_paralelo_priorizacion_dinamica_auto_balanceo_dead_letter_queue
```

### 12 Task Models (Versión Original del Historial — TM01-TM12)

```yaml
TM01_Analisis: entender_input
TM02_Diseno: arquitectura_de_solucion
TM03_Implementacion: codigo
TM04_Testing: pruebas
TM05_Debug: encontrar_y_arreglar_bugs
TM06_Refactor: mejorar_codigo_existente
TM07_Documentacion: escribir_docs
TM08_Investigacion: buscar_informacion
TM09_Validacion: ejecutar_CSA
TM10_Aprendizaje: actualizar_memoria
TM11_Despliegue: publicar_o_rollback
TM12_Coordinacion: multiples_tareas
```

### 5 Loop Versions (Versión Original del Historial)

```yaml
ALV_LOP_MIN: minimo_1_ciclo_1_agente
ALV_LOP_STD: estandar_3_ciclos_A_B_C_paralelos
ALV_LOP_ENHANCED: mas_learning_loop_meta_learning
ALV_LOP_TURBO: maximo_paralelismo_todos_los_recursos
ALV_LOP_ADAPTIVE: se_adapta_al_contexto_automaticamente

caracteristicas:
  MIN: recursos_minimos_baja_latencia
  STD: balance_estandar
  ENHANCED: mas_lento_pero_aprende
  TURBO: maxima_velocidad_maximo_costo
  ADAPTIVE: elige_segun_tarea
```

### Notas Adicionales del Chat (Contexto)

```yaml
M3_chat_ne_SKYNER:
  - M3_es_el_arquitecto_que_trabaja_con_MAX
  - SKYNER_es_el_orquestador_interno
  - SKYNER_eq_1x_NVIDIA_en_el_liderazgo_del_orquestador
BIS_raiz_unica: una_sola_raiz_para_todas_las_skills
pregunta_correcta:
  cuantos_sub_agentes_en_paralelo  # no_total
  workers_jueces_colas_en_paralelo_no_secuencial
```

