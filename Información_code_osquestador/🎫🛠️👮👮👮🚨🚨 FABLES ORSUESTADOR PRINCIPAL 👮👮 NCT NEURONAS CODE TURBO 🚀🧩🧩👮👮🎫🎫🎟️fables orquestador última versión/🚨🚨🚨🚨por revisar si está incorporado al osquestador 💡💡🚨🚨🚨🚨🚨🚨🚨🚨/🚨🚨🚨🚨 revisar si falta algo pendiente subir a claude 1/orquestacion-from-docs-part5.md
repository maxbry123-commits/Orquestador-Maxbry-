# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 5)

> **Continuación**: Contiene documentos verificados (verificación cruzada + patches faltantes + estructura + agentes dedup)


## DOC 18: VERIFICACIÓN CRUZADA — 17 Documentos Consolidados

### Resumen Lo Consolidado (Total: 209,185 bytes)

```yaml
17_documentos:
  01-constitucion: 17407_bytes
  02-estructura: 6599_bytes
  03-pipeline: 7316_bytes
  04-razonamiento: 7872_bytes
  05-configuraciones: 5752_bytes
  06-subsistemas: 10449_bytes
  07-agentes: 10995_bytes
  08-modelos-apis: 6474_bytes
  09-reglas-costos: 10708_bytes
  10-input-output-loop: 12227_bytes
  11-mythos-fables: 16104_bytes
  12-arquitectura-completa: 16519_bytes
  13-patches-extras: 11230_bytes
  14-extras-y-detalles: 11676_bytes
  15-ejemplos-y-arquitectura-detalles: 22426_bytes
  16-mimo-lop-v200: 22751_bytes
  17-maxbry-super-team: 11680_bytes
total: 209185_bytes_en_17_documentos
```

### Análisis de Cobertura por Categoría

```yaml
A_Constitucion_39_principios:
  v1.0_13_principios: Doc_01
  v2.0_13_principios: Doc_01
  v3.0_13_componentes: Doc_01_y_12

B_CSA_10_Jueces:
  10_jueces_definidos: Doc_01
  5_fases_por_juez: Doc_13
  sistema_de_veto: Doc_01

C_SID:
  componentes: Doc_01
  auditor_5_preguntas_fijas: Doc_01

D_BIS_14_categorias:
  14_categorias: Doc_02_y_13
  13_criterios_de_skills: Doc_13
  3_versiones_v1_v2_v3: Doc_06

E_Input_Engine_v4.0_54_componentes:
  originales_45: Doc_10
  nuevos_9_A_a_I: Doc_10

F_Output_Engine_+_OOS_v3.1_27_componentes:
  13_Output_Engine: Doc_10
  14_OOS: Doc_10
  OVFS: Doc_10

G_LOOP_v6.0_15_capas_+_3_ciclos:
  15_capas: Doc_10
  3_ciclos_ABC: Doc_10

H_OUTPUT_v6.1_16_capas_gobernanza:
  16_capas_A_a_P: Doc_10
  Output_Governor_8_estados: Doc_10

I_Estructura_MAXBRY_SUPER_TEAM:
  30_micro_agentes: Doc_02_y_17
  11_internal_roles: Doc_02
  10_parallel_queues: Doc_02
  6_niveles_autonomia: Doc_02
  12_task_models: Doc_15
  5_loop_versions: Doc_15
  3_monitors: Doc_03

J_Pipeline:
  10_fases: Doc_03
  Fase_0.5_confirmation_gate: Doc_03
  5_fases_FABLES: Doc_11
  CHEF_FINAL_4_pasos: Doc_11

K_Razonamiento:
  STANDARD_5_+_12: Doc_04
  TURBO_12_+_45: Doc_04
  Micro_ciclo_7_pasos: Doc_04
  DRE_9_pasos: Doc_04
  OpenMythos: Doc_11

L_Mythos_Fables:
  40_pasos: Doc_11
  12_pasos_cortos: Doc_11
  OpenMythos: Doc_11
  Arquitectura_de_control: Doc_11

M_Subsistemas:
  System_Prompt_Mythos_15_secciones: Doc_06
  Skills_System_13_criterios: Doc_06
  Multi_source_investigation_5_agentes: Doc_06
  Universal_Plug_v1.5: Doc_06
  M3_+_Kimi_division: Doc_06
  Sistema_de_razonamiento_externo: Doc_06
  NCT_Coordinator: Doc_12
  Universal_Module_Contract_JSON_Schema: Doc_14

N_Configuraciones:
  3_perfiles_API: Doc_05
  Datos_pre_flight_pendientes: Doc_05
  Costos_y_capacidades: Doc_09
  $0_infraestructura: Doc_09

O_Reglas:
  Regla_absoluta_MAX: Doc_05
  Cosas_intocables: Doc_01_y_09
  Validacion_por_salida: Doc_05
  5_GOALS_+_12_PASOS: Doc_05

P_Agentes:
  5_agentes_de_consenso: Doc_07
  5_agentes_de_investigacion: Doc_07
  12_micro_agentes_especializados: Doc_07
  10_jueces_CSA: Doc_07
  10_agentes_consejo_de_consenso: Doc_07
  5_officers_Executive_Board: Doc_07
  9_propuestas_M3_OUTPUT: Doc_07
  10_propuestas_M3_INPUT_o_LOOP: Doc_07
  8_hallazgos_de_research: Doc_13
  Open_Source_Clones_Catalog: Doc_16

Q_Modelos_y_APIs:
  9_GGUF_modelos: Doc_08
  16_API_keys: Doc_08
  3_perfiles_de_uso: Doc_05
  60_datasets_PARCHE-v15: Doc_08
  60_adapters_PARCHE-v15: Doc_08

R_Arquitectura_completa:
  Version_1_Chat_AI_NCT: Doc_15
  Version_2_Adaptador_MHYTOS: Doc_15
  Decisiones_aprobadas: Doc_15
  Diagrama_V1_vs_V2: Doc_15
  NCT_AI_Architecture: Doc_15

S_MiMoCode_Lop_v200:
  Analisis_de_MiMo_Code: Doc_16
  3_pilares_arquitectonicos: Doc_16
  Loops_internos: Doc_16
  Adaptaciones_a_NCT: Doc_16
  Catalogo_12_micro_agentes: Doc_16
  8_nuevas_propuestas_PROP-13_a_PROP-20: Doc_16
  Flota_HF_Spaces: Doc_16
```

### Temas Mencionados en Chat pero No Profundizados

```yaml
1_validacion_por_salida_md_contenido_completo: mencionado_pero_no_extraido_completamente
2_MI-SYSTEM-PROMPT-OPERATIVO_md_contenido: mencionado_pero_no_extraido_completamente
3_BORRADOR-LISTA-APROBADOS_md_contenido: mencionado_pero_no_extraido_completamente
4_STATE-AUDIT_md_contenido: mencionado_pero_no_extraido_completamente
5_detalles_especificos_validacion_por_salida: mencionado_en_Doc_05_pero_podria_profundizarse
6_Mi_System_Prompt_Operativo_de_M3: mencionado_en_Doc_06_pero_podria_profundizarse
```

### Resumen Ejecutivo Final

```yaml
total_documentos: 17
total_bytes: 209185
total_temas_cubiertos: 80+
total_verificaciones_cruzadas: 100%

lo_que_NO_falta_verificado:
  1_Constitucion_completa_39_principios
  2_CSA_completo_10_jueces_x_5_fases
  3_SID_completo_con_5_preguntas
  4_BIS_completo_14_categorias_+_13_criterios
  5_Input_Engine_completo_54_componentes
  6_Output_Engine_completo_27_componentes_+_OVFS
  7_LOOP_completo_15_capas_+_3_ciclos
  8_OUTPUT_v6.1_completo_16_capas_gobernanza
  9_MAXBRY_SUPER_TEAM_completo
  10_Modelos_y_APIs_completos
  11_Reglas_y_cosas_intocables
  12_Agentes_consenso_investigacion_micro
  13_Pipeline_completo_10_fases_+_Fase_0.5
  14_Razonamiento_completo_Standard_+_Turbo_+_DRE
  15_Mythos_o_Fables_completo
  16_Subsistemas_completos
  17_Arquitectura_NCT_completa
  18_MiMoCode_+_Lop_v200
  19_Universal_Plug_v1.5
  20_Universal_Module_Contract

lo_que_falta_en_MAX_no_en_los_documentos:
  - 8_datos_pre_flight_pendientes
  - confirmacion_de_HTM_y_YUAN_model_names
  - aprobacion_final_para_M2.7
```

### Conclusión

```yaml
los_17_documentos_contienen_TODA_la_informacion_sobre_orquestador_y_agentes_que_fue_aprobada_en_el_historial_del_chat

las_19_propuestas_M3_estan_documentadas:
  - 9_propuestas_OUTPUT_aplicadas
  - 1_propuesta_OUTPUT_rechazada  # Output_Sandbox
  - 10_propuestas_INPUT_o_LOOP_aplicadas

los_170_patches_estan_indexados:
  - 9_patches_OUTPUT_v6.1
  - 16_patches_OUTPUT_v6.1_gobernanza
  - 9_patches_INPUT_V4.0
  - 15_patches_LOOP_V6.0
  - 10_patches_PROPUESTAS_INPUT_o_LOOP
  - 51_parches_ORQUESTADOR
  - 23_parches_INFRA
  - 37_parches_EXTRAS  # CSA_criterios_agentes_research_delivery

total: 170_patches_documentados
```


## DOC MASTER 09 (Segunda Versión): 87+ Agentes — Visión General (Versión Deduplicada)

### 5 Officers — Versión CEO/CTO/COO/CSO/CMO

```yaml
7.1_CEO_Officer:
  - coordina_toda_la_operacion
  - reporta_a_MAX

7.2_CTO_Officer:
  - decisiones_tecnicas
  - seleccion_de_modelos

7.3_COO_Officer:
  - operaciones
  - monitoreo

7.4_CSO_Officer:
  - seguridad_global
  - compliance

7.5_CMO_Officer:
  - comunicacion_con_MAX
  - reportes
```

### 12 Micro-Agentes MiMo-Aligned (Loops Internos)

```yaml
inspirados_en: loops_internos_de_MiMo_Code

decision_loop: cada_turno
checkpoint_loop: cada_N_turnos
writer_loop: cuando_contexto_gt_70%
max_mode_loop: decisiones_criticas
dream_loop: semanal
repair_loop: en_error
evolution_loop: al_cierre
resto_hasta_12: extensiones_para_lograr_12
```

### Conclusión 87+ Agentes

```yaml
MAXBRY_orquesta_87+_agentes_distribuidos_en:
  - 30_micro_agentes_operativos
  - 5_agentes_de_consenso
  - 5_agentes_de_investigacion
  - 10_jueces_CSA
  - 10_consejo
  - 5_officers  # CEO_CTO_COO_CSO_CMO
  - 12_especializados_v200
  - 12_MiMo_aligned

cada_uno_con_responsabilidad_especifica_formando_un_sistema_completo_de_auto_gobierno
```


## DOC MASTER 27: PARCHES DETALLADOS FALTANTES (Trust Engine + Contract + 13 Criterios Skills)

### Parches Loop V60 Detallados (15)

```yaml
A_workflow_dag:
  concepto: Workflow_como_DAG_explicito
  cada_nodo_eq_un_paso
  edges_eq_dependencias
  topological_sort_al_ejecutar
  validacion: no_ciclos

B_runtime_kernel:
  concepto: Runtime_como_kernel_del_SO
  process_management
  memory_management
  IPC_inter_process_communication
  scheduling

C_event_sourcing:
  concepto: Event_sourcing_como_fuente_de_verdad
  cada_cambio_eq_un_evento
  estado_eq_replay_de_eventos
  auditoria_completa
  time_travel_debugging

D_state_machine:
  concepto: FSM_para_control_de_flujo
  estados_explicitos
  transiciones_validadas
  eventos_disparan_transiciones
  visualizacion_de_flujo

E_prediction_engine:
  concepto: Prediccion_de_outcomes
  basado_en_historico
  predice_exito_o_fallo
  predice_duracion
  predice_costo

F_dynamic_replanning:
  concepto: Replanning_dinamico
  detecta_desviacion
  genera_plan_alternativo
  aplica_si_score_cae

G_model_router_estrella:
  concepto: Router_inteligente_de_modelos
  seleccion_por_capacidad
  seleccion_por_costo
  seleccion_por_latencia
  fallback_automatico

H_trust_engine_NUEVO_DETALLE:
  concepto: Motor_de_confianza
  cada_dato_o_agente_o_modelo_tiene_score_de_confianza
  score_0_a_100
  se_actualiza_con_feedback
  afecta_decisiones

I_goal_monitor:
  concepto: Monitor_de_objetivos
  verifica_que_el_output_cumple_goals
  alerta_si_diverge
  trigger_de_replanning

J_contract_engine_NUEVO_DETALLE:
  concepto: Motor_de_contratos
  define_contratos_input_o_output
  valida_cumplimiento
  genera_evidencia

K_resource_economy_NUEVO_DETALLE:
  concepto: Economia_de_recursos
  presupuesto_por_tarea
  contador_en_tiempo_real
  throttling_si_excede

L_semantic_diff_NUEVO_DETALLE:
  concepto: Diff_semantico
  compara_significado_no_syntax
  detecta_cambios_sutiles
  trigger_si_semantic_drift_gt_0.10

M_universal_artifact_graph_NUEVO_DETALLE:
  concepto: Grafo_universal_de_artefactos
  todos_los_outputs_son_nodos
  relaciones_entre_artefactos
  tracking_completo

N_failure_recovery_NUEVO_DETALLE:
  concepto: Recuperacion_de_fallos
  detecta_tipo_de_fallo
  aplica_estrategia_de_recovery
  5_pasos

O_executive_board_DETALLE:
  concepto: Executive_Board
  5_officers
  supervisan_funcionamiento_global
  reportan_a_MAX
```

### Parches Output V6.1 Gobernanza Detallados (16)

```yaml
A_output_governor:
  concepto: Gobernador_del_output
  decide_cuando_se_emite
  decide_formato
  decide_destino

B_output_digital_twin:
  concepto: Gemelo_digital_del_output
  simula_antes_de_emitir
  detecta_problemas
  reduce_fallos_70%

C_multi_version_generator:
  concepto: Generador_multi_version
  genera_N_versiones
  para_diferentes_audiencias
  compara_y_selecciona

D_output_fusion:
  concepto: Fusion_de_outputs
  combina_mejores_partes
  elimina_redundancia
  sintesis_final

E_acceptance_test:
  concepto: Test_de_aceptacion
  verifica_contra_criterios
  score_de_aceptacion
  go_o_no_go

F_coverage_map:
  concepto: Mapa_de_cobertura
  que_cubre_el_output
  que_NO_cubre
  gaps_identificados

G_explainability:
  concepto: Explicabilidad
  por_que_se_genero_asi
  que_informacion_uso
  cadena_de_razonamiento

H_output_provenance:
  concepto: Provenance_del_output
  origen_de_cada_dato
  cadena_de_custodia
  hash_firmado

I_consistency_swarm:
  concepto: Swarm_de_consistencia
  multiples_agentes_verifican
  detectan_inconsistencias
  corrigen

J_artifact_graph:
  concepto: Grafo_de_artefactos
  relaciones_entre_outputs
  versiones
  dependencias

K_release_manager_NUEVO_DETALLE:
  concepto: Release_manager
  decide_cuando_se_libera
  versiona_el_output
  gestiona_el_rollout

L_output_memory_NUEVO_DETALLE:
  concepto: Memoria_del_output
  guarda_outputs_pasados
  permite_re_emision
  auditoria_historica

M_output_score:
  concepto: Score_del_output
  calcula_score_0_a_100
  umbral_95%_requerido
  multiples_dimensiones

N_human_approval_NUEVO_DETALLE:
  concepto: Aprobacion_humana
  cuando_MAX_debe_aprobar
  workflow_de_aprobacion
  tracking

O_adaptive_delivery: ✅_YA_DOCUMENTADO
P_closed_feedback_loop: ✅_YA_DOCUMENTADO
```

### Parches Input V40 Detallados (9)

```yaml
A_Definition_Score_Gate: bloquea_si_lt_95%
B_input_discovery:
  concepto: Descubrimiento_de_inputs
  detecta_fuentes
  lista_inputs_disponibles
  enriquece_input
C_input_forensics:
  concepto: Forensics_del_input
  analisis_profundo
  deteccion_de_anomalias
  tracing
D_knowledge_discovery:
  concepto: Descubrimiento_de_conocimiento
  encuentra_info_relevante
  indexa
  prepara_para_uso
E_claude_definition:
  concepto: Definicion_tipo_Claude
  5_preguntas_fijas_SID
  Definition_Score
  Gate_keeper
F_input_compiler:
  concepto: Compilador_de_input
  convierte_a_formato_canonico
  optimiza
  normaliza
G_quality_swarm:
  concepto: Swarm_de_calidad
  multiples_agentes_evaluan_input
  score_de_calidad
  feedback
H_input_governor:
  concepto: Gobernador_del_input
  decide_si_proceder
  bloquea_si_score_bajo
  reporta
```

### 13 Criterios Skills Detallados (Originales vs Corregidos)

```yaml
criterio_01_relevancia:
  "¿es_relevante_para_el_dominio?"
  "¿resuelve_un_problema_real?"
  score_0_a_10

criterio_02_efectividad:
  "¿resuelve_el_problema?"
  "¿con_que_tasa_de_exito?"
  score_0_a_10

criterio_03_costo:
  "¿cuanto_cuesta_ejecutar?"
  "¿es_costo_efectivo?"
  score_0_a_10

criterio_04_compatibilidad:
  "¿es_compatible_con_el_stack?"
  "¿con_otras_skills?"
  score_0_a_10

criterio_05_mantenibilidad:
  "¿es_facil_de_mantener?"
  "¿es_facil_de_actualizar?"
  score_0_a_10

criterio_06_documentacion:
  "¿tiene_README?"
  "¿tiene_ejemplos?"
  score_0_a_10

criterio_07_reusabilidad:
  "¿se_puede_reusar?"
  "¿en_cuantos_contextos?"
  score_0_a_10

criterio_08_seguridad:
  "¿es_seguro?"
  "¿sin_vulnerabilidades?"
  score_0_a_10

criterio_09_performance:
  "¿que_tan_rapido?"
  "p50_p95_p99"
  score_0_a_10

criterio_10_escalabilidad:
  "¿escala?"
  "¿a_cuantas_tareas_simultaneas?"
  score_0_a_10

criterio_11_compliance:
  "¿cumple_regulaciones?"
  "¿GDPR_HIPAA?"
  score_0_a_10

criterio_12_test_coverage:
  "¿tiene_tests?"
  "¿coverage_ge_80%?"
  score_0_a_10

criterio_13_comunidad:
  "¿tiene_comunidad?"
  "¿esta_maintained?"
  score_0_a_10
```

### 10 Propuestas Avanzadas Input/Loop

```yaml
01_meta_agentes:
  agentes_que_orquestan_otros_agentes_nivel_meta_auto_gestion
02_causalidad:
  razonamiento_causal_no_correlacional_identifica_causa_raiz_predice_efectos
03_counterfactual:
  que_hubiera_pasado_si_analisis_contrafactual_aprendizaje_de_decisiones
04_auto_modificacion:
  el_sistema_se_modifica_a_si_mismo_basado_en_feedback_con_aprobacion
05_memoria_episodica:
  memoria_de_episodios_especificos_contexto_completo_retrieval_por_similitud
06_zero_shot_transfer:
  transferir_conocimiento_entre_dominios_sin_entrenamiento_especifico_generalizacion
07_NAS_Neural_Architecture_Search:
  buscar_arquitectura_optima_automaticamente_por_tarea
08_time_travel:
  volver_a_estado_anterior_debugging_temporal_auditoria
09_inteligencia_colectiva:
  multiples_agentes_colaboran_inteligencia_emergente_swarm_intelligence
10_auto_curriculum:
  el_sistema_disena_su_propio_curriculum_aprende_progresivamente_adaptativo
```

### Capacidades Detalladas

```yaml
capacidad_actual_HF_Spaces:
  - 7_HF_Spaces_x_16GB_RAM_eq_112GB
  - "~13.5GB_usados_por_modelos"
  - "87%_margen_libre"

capacidad_objetivo:
  - 2000+_agentes_capacidad
  - 1000+_tareas_simultaneas
  - 1000_a_2000+_tareas_dia

limitaciones:
  - HF_Spaces_pueden_dormirse
  - rate_limits_de_APIs
  - cold_starts
  - 16GB_max_por_Space
```

### Skills Recomendados (30)

```yaml
workflow_5:
  - Temporal
  - Kestra
  - Airflow
  - Dagster
  - Prefect

arquitectura_4_a_6:
  - Structurizr
  - C4_Model
  - arc42
  - PlantUML
  - Mermaid
  - diagrams_net

agentes_5_a_10:
  - LangGraph
  - CrewAI
  - OpenAI_Agents_SDK
  - LlamaIndex
  - Mem0
  - LangMem
  - AutoGen
  - MAF_Microsoft_Agent_Framework
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

total: 30_skills_recomendados
```


## DOC MASTER 28: SISTEMA RAZONAMIENTO EXTERNO DETALLADO (16 Etapas + 35 Pasos + 67 Pasos + EROS 3-tier)

### Cadena de Razonamiento Estructurada (16 Etapas)

```yaml
1_GOAL_LOCK: congelar_objetivo_antes_de_razonar
2_CONTRACT_LOCK: contrato_de_bordes_que_entra_que_sale
3_PROBLEM_DECOMPOSITION: descomposicion_del_problema
4_MULTI_HYPOTHESIS_GENERATOR: generar_multiples_hipotesis
5_CONTRAST_ENGINE: contraste_forzado_entre_hipotesis
6_FIRST_PRINCIPLES_REBUILD: reconstruccion_desde_primeros_principios
7_ARCHITECTURE_COMPETITION: competencia_entre_arquitecturas
8_MULTI_LAYER_REASONING: 10_niveles_de_razonamiento
9_SELF_REFUTATION_ENGINE: auto_refutacion_de_la_propuesta
10_ADVERSARIAL_REVIEW_PANEL: panel_de_revision_adversarial
11_CONSENSUS_ENGINE: punto_de_integracion_con_SKYNER ⭐
12_VERIFIER_INDEPENDIENTE: verificador_separado_del_razonador
13_FAILURE_SIMULATION: simulacion_de_fallos
14_RECOVERY_ENGINE: motor_de_recuperacion
15_SELF_IMPROVEMENT_LOOP: bucle_de_auto_mejora
16_FINAL_DECISION_GATE: puerta_de_decision_final
```

### Método de Razonamiento V2 (35 Pasos + 10 GOAL)

```yaml
10_GOAL_fijados_ANTES_de_razonar:
  1_objetivo_primario
  2_objetivos_secundarios
  3_criterios_de_exito
  4_criterios_de_fallo
  5_restricciones
  6_alcance
  7_vecinos
  8_riesgo
  9_resultado_esperado
  10_fuente_de_verdad

35_pasos_agrupados:
  pasos_1_a_7: comprension_y_setup
  pasos_8_a_14: investigacion_y_descubrimiento
  pasos_15_a_21: generacion_de_hipotesis
  pasos_22_a_28: validacion_y_refutacion
  pasos_29_a_35: sintesis_y_decision
```

### MASTER_STRUCTURE V1 (67 Pasos en 5 Bloques)

```yaml
BLOQUE_A_pasos_01_a_15_preparacion_y_comprension:
  setup_inicial
  comprension_del_problema
  definicion_de_objetivos

BLOQUE_B_pasos_16_a_30_investigacion_y_descubrimiento:
  research_multi_fuente
  synthesis
  hallazgos

BLOQUE_C_pasos_31_a_45_generacion_de_soluciones:
  swarm
  red_team
  alternativas

BLOQUE_D_pasos_46_a_56_autoevaluacion:
  consenso
  auditoria
  veredicto

BLOQUE_E_pasos_57_a_67_chef_final:
  post_check
  output_final
  cierre
```

### MYTHOS 40 Pasos (Reorganizado en 4 Fases)

```yaml
pasos_1_a_10_comprension:
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

pasos_11_a_20_planificacion:
  11_ARCHITECTURE_DESIGN
  12_PLAN_GENERATION
  13_SUBTASK_BREAKDOWN
  14_DEPENDENCY_GRAPH_BUILD
  15_HYPOTHESIS_GENERATION
  16_ALTERNATIVE_PATH_GENERATION
  17_SEARCH_EXPANSION
  18_REASONING_SWARM
  19_CONTRADICTION_DETECTION
  20_CRITIC_SWARM

pasos_21_a_30_validacion:
  21_SELF_REFLECTION_LOOP
  22_FAILURE_MODE_ANALYSIS
  23_SIMULATION_ENGINE
  24_EDGE_CASE_GENERATION
  25_VALIDATION_LAYER
  26_KNOWLEDGE_RETRIEVAL
  27_INSIGHT_EXTRACTION
  28_MEMORY_WRITE_SHORT_o_LONG_TERM
  29_REPLANNER_LOOP
  30_transicion_a_sintesis

pasos_31_a_40_sintesis:
  31_OPTIMIZATION_PASS
  32_DECISION_ENGINE
  33_CONFIDENCE_SCORING  # ⭐
  34_SOLUTION_RANKING
  35_FUSION_o_ENSEMBLE
  36_SAFETY_CHECK
  37_FINAL_SYNTHESIS
  38_OUTPUT_GENERATION
  39_POST_OUTPUT_AUDIT
  40_FEEDBACK_LOOP_STORAGE
```

### 4 Escenarios Según Complejidad

```yaml
Escenario_1_9_pasos: tareas_simples  # TM01_TM02
Escenario_2_16_pasos: tareas_medias  # TM03_TM04_TM05
Escenario_3_25_pasos: tareas_complejas  # TM06_TM07_TM08
Escenario_4_30_a_50_pasos: tareas_criticas  # TM11_TM12
```

### EROS 3-Tier (Consolidación Jerárquica)

```yaml
Tier_1_Inmediato:
  - estado_actual
  - en_RAM
  - volatil

Tier_2_Sesion:
  - estado_de_sesion
  - persistente_durante_sesion
  - en_disco

Tier_3_Proyecto:
  - estado_del_proyecto
  - persistente_siempre
  - en_DB

proposito: tracking_completo_persistencia_entre_fases_anti_perdida_de_informacion
```


## DOC MASTER 13: ARQUITECTURA NCT (NCT Coordinator + 25 Bloques + V1+V2)

### Los 25 Bloques del Software Principal

```yaml
01_Inicializador: boot_del_sistema
02_Config_Loader: carga_configuracion
03_State_Manager: estado_global
04_Event_Bus: bus_de_eventos
05_Logger: sistema_de_logs
06_Error_Handler: manejo_de_errores
07_Network_Manager: red
08_Storage_Manager: almacenamiento
09_Auth_Manager: autenticacion
10_Permission_Manager: permisos
11_Cache_Manager: cache
12_Queue_Manager: colas
13_Worker_Pool: pool_de_workers
14_Task_Scheduler: scheduler
15_Result_Aggregator: agregador
16_Retry_Manager: reintentos
17_Circuit_Breaker: circuit_breaker
18_Metrics_Collector: metricas
19_Health_Checker: health
20_Notification_Manager: notificaciones
21_Plugin_Manager: plugins
22_API_Gateway: gateway_api
23_Database_Connector: db
24_External_Service_Client: servicios_externos
25_Telemetry: telemetria
```

### NCT Coordinator — 13 Archivos

```yaml
1_nct_coordinator_py: coordinador_principal
2_nct_modes_py: selector_de_modos  # Manual_Semi_Continuo
3_nct_flows_py: definicion_de_flujos
4_nct_phases_py: fases_F0_a_F9
5_nct_inputs_py: inputs
6_nct_outputs_py: outputs
7_nct_state_py: estado
8_nct_memory_py: memoria
9_nct_skills_py: skills
10_nct_agents_py: agentes
11_nct_audit_py: auditoria
12_nct_metrics_py: metricas
13_nct_delivery_py: entrega
```

### Dos Versiones de Arquitectura

```yaml
Version_1_Chat_AI_NCT_original:
  - asistente_de_chat_tradicional
  - procesa_mensajes
  - genera_respuestas
  - memoria_simple

Version_2_Adaptador_MYTHOS:
  - wrapper_sobre_V1
  - añade_razonamiento_profundo
  - añade_Mythos_system_prompt
  - añade_control_de_alto_nivel

Diagrama_V1_vs_V2:
  V1_chat_AI_NCT ──────► LLMs
  V2_MYTHOS_control ──► Adaptador_MYTHOS ──► LLMs
```

### Flujo Continuo MAXBRY

```
MAX → Telegram
   ↓
MAXBRY recibe
   ↓
SID (5 preguntas)
   ↓
BIS lookup
   ↓
Plan generado
   ↓
Consensus consejo
   ↓
Ejecutar (30 micro-agentes)
   ↓
Validar (CSA)
   ↓
Refinar si score < 95%
   ↓
Output Engine
   ↓
Multi-target Delivery
   ↓
Monitoreo
   ↓
Feedback → Memoria → Mejora
```

### Fases Detalladas (F0-F9)

```yaml
F0_Pre_Boot:
  verifica: [python_version, HF_Spaces, tokens, secrets, network]
F1_Input:
  recibe: [telegram_message, API_call, CLI_command, web_dashboard]
F2_Process: aplica_Input_Engine_v4.0
F3_Plan: genera_plan_con_consensus
F4_Execute: 30_micro_agentes_+_12_especializados
F5_Validate: CSA_10_jueces
F6_Refine: hasta_score_ge_95%
F7_Output: Output_Engine_+_OOS_+_OVFS
F8_Deliver: multi_target
F9_Monitor: post_delivery
```

### Integración MAXBRY ↔ NCT Coordinator

```yaml
MAXBRY_NO_modifica_los_25_bloques_los_INVOCA_como_workers

MAXBRY ─invoca─► NCT_Coordinator ─coordina─► 25_Bloques ─producen─► Output
```

### Interfaces

```yaml
para_MAX:
  - telegram_principal
  - API_REST
  - dashboard_web
  - CLI

para_MAXBRY:
  - Python_API
  - MCP_server
  - CLI_directo
```

### Principios Arquitectónicos

```yaml
Modularidad:
  - cada_bloque_responsabilidad_unica
  - comunicacion_via_bus_de_eventos
  - acoplamiento_debil

Determinismo:
  - 90%_codigo_determinista
  - 10%_LLM_donde_aporta
  - reproducibilidad_alta

Trazabilidad:
  - cada_accion_se_registra
  - state_siempre_actualizado
  - logs_estructurados

Resiliencia:
  - circuit_breakers
  - retry_con_backoff
  - failover_automatico
  - repair_pipeline
```


## DOC MASTER 23: IMPLEMENTACIÓN Y DEPLOY (Estructura + Código + Tests + Deployment)

### Reglas de Estructura de Archivos

```yaml
regla_general:
  maximo_200_lineas_por_archivo
  una_responsabilidad_por_archivo
  naming_snake_case_para_Python
  type_hints_obligatorios
```

### Estructura Completa MAXBRY / g5-orquestador

```yaml
/workspace/maxbry/g5-orquestador/:
  - README.md
  - pyproject.toml
  - Dockerfile
  - src/core/:
      constitution_py: 39_principios
      csa_py: 10_jueces
      sid_py: 5_preguntas
      bis_py: 14_categorias
  - src/agents/:
      micro_30_py: 30_micro_agentes
      consensus_5_py: 5_consenso
      investigation_5_py: 5_investigacion
      officers_5_py: 5_officers
      council_10_py: 10_consejo
  - src/engines/:
      input_engine_py: 54_componentes
      output_engine_py: 13_componentes
      oos_py: 14_componentes_OOS
      ovfs_py: Output_Virtual_FS
      loop_engine_py: 15_capas_+_3_ciclos
  - src/state/:
      state_py: state_json
      events_py: event_log
      memory_py: 4_tier_memory
      checkpoints_py: snapshots_firmados
  - src/orchestration/:
      skyner_py: lider
      task_models_py: 12_TM
      loop_versions_py: 5_ALV
      monitors_py: 3_monitores
  - src/delivery/:
      multi_target_py: 23_destinos
      adaptive_py: adaptive_format
      feedback_py: feedback_loop
  - tests/:
      unit/: 100+_tests
      integration/: 30+_tests
      e2e/: 10+_tests
  - scripts/:
      bootstrap_sh
      health_check_py
      report_py
  - config/:
      profile_conservador_yaml
      profile_equilibrado_yaml
      profile_agresivo_yaml
```

### Código de Ejemplo (Constitution, SID, CSA)

```python
# constitution.py (extracto)
class ConstitutionPrinciple:
    def __init__(self, number: int, version: str, title: str, description: str):
        self.number = number
        self.version = version
        self.title = title
        self.description = description

class Constitution:
    PRINCIPLES = [
        ConstitutionPrinciple(1, "v1.0", "FILOSOFÍA",
            "El Orquestador opera como Director de Empresa, no como IA."),
        ConstitutionPrinciple(2, "v1.0", "OBJETIVOS DE ESCALA",
            "Soporta 2000+ agentes y 1000+ tareas simultáneas."),
        # ... 37 más
    ]
    
    @classmethod
    def get(cls, number): ...
    @classmethod
    def all(cls): ...
    @classmethod
    def by_version(cls, version): ...
```

```python
# sid.py
SID_QUESTIONS = [
    "What is this?",
    "Who is it for?",
    "What problem does it solve?",
    "How is it used?",
    "What is it NOT?"
]

async def run_sid(task: str) -> dict:
    # 5 preguntas + score total
    ...
```

```python
# csa.py (10 jueces con 5 fases cada uno)
class CSAJudge:
    async def run(self, artifact, rubric):
        phase_1_F1 = self.audit_input(artifact, rubric)
        phase_2_F2 = self.find_unreviewed(artifact)
        phase_3_F3 = self.generate_alternatives(artifact)
        phase_4_F4 = self.destroy_self(artifact)
        phase_5_F5 = self.attack_others(artifact)
        
        score = max(0, 100 - len(issues) * 5)
        return {"judge": self.id, "score": score, ...}

CSA_JUDGES = [
    CSAJudge("J1", "COMPRENSIÓN", "¿Entendimos QUÉ quiere MAX?", eval_j1),
    CSAJudge("J2", "COBERTURA", "¿Cubrimos TODO?", eval_j2),
    # ... 8 más
]
```

### Tests

```yaml
unit_tests:
  test_constitution:
    test_principles_count_eq_39
    test_v1_has_13_principles
    test_v2_has_13_principles
    test_v3_has_13_principles
    test_get_principle_by_number
    test_sid_questions_fixed_eq_5
    test_csa_has_10_judges

integration_tests:
  test_sid_to_csa_flow:
    sid_result_pass
    csa_10_jueces_en_paralelo
    avg_ge_80
```

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git curl wget && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/src/
COPY config/ /app/config/
COPY scripts/ /app/scripts/
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python scripts/health_check.py || exit 1
CMD ["python", "-m", "src.core.constitution"]
```

### HF Spaces Deployment

```yaml
estructura_HF_Space:
  mavis_o_g5-orquestador/:
    - README_md: SDK_metadata
    - requirements_txt
    - Dockerfile
    - app_py: entry_point_Gradio_o_Streamlit
    - src/

SDK_metadata_header:
  title: G5_Orquestador_MAXBRY
  emoji: 🧠
  colorFrom: blue
  colorTo: purple
  sdk: docker
  app_port: 7860
  pinned: true
  license: mit

Secrets_HF_Space_settings:
  - NVIDIA_NIM_KEY_01_a_04
  - CEREBRAS_KEY_01_a_06
  - GROQ_KEY_01_a_06
  - HF_TOKEN
  - GITHUB_TOKEN
  - TURSO_URL_y_TURSO_TOKEN
  - TELEGRAM_BOT_TOKEN
```

### Bootstrap Script

```bash
#!/bin/bash
# bootstrap.sh
set -e
echo "🚀 MAXBRY SUPER TEAM Bootstrap"

# 1. Verificar entorno
python --version || (echo "Python 3.11+ requerido" && exit 1)

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Verificar secrets
python scripts/verify_secrets.py

# 4. Health check
python scripts/health_check.py

# 5. Inicializar state
python scripts/init_state.py

# 6. Cargar skills BIS
python scripts/load_bis.py

# 7. Iniciar orquestador
echo "✅ Bootstrap completo"
echo "📊 Report:"
python scripts/report.py
```

### Monitoring — Métricas Clave

```python
METRICS = {
    "tasks_total": Counter(),
    "tasks_success": Counter(),
    "tasks_failed": Counter(),
    "agents_active": Gauge(),
    "consensus_score": Histogram(),
    "csa_scores": Histogram(),
    "llm_tokens_used": Counter(),
    "loop_iterations": Histogram(),
    "drift_score": Gauge(),
    "anxiety_level": Gauge(),
}

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "agents_active": METRICS["agents_active"].value,
        "tasks_total": METRICS["tasks_total"].value,
        "uptime": get_uptime(),
        "version": "1.0.0"
    }
```


## DOC FUSIÓN 31e85428 — BLOQUE 4: F7 + F8 + F9 (Consolidación + Repair + Entrega)

### F7 Consolidación Jerárquica (EROS 3-Tier)

```yaml
fase_F7:
  nombre_original: Fase_7_Consolidacion_Jerarquica_EROS_3-Tier_+_Coordinator
  responsabilidad_original: >
    EROS_3-Tier: Tier_3_Executors_logs_crudos_Tier_2_Controllers_Strategic_Pulses
    Tier_1_Orchestrator_menos_5%_contexto
    Coordinator_MiniMax_recibe_outputs_integra_maneja_escalados
  estado_v44:
    preservado: true
    modificado: true
    ampliado: true
  cambios:
    - "EROS_3-Tier_implementado_en_codigo_puro_estadistica"
    - "Tier_3_a_tier2_resumen_estadistico_count_mean_success_rate"
    - "Tier_2_a_tier1_solo_metricas_criticas_menos_5%_contexto"
    - "Coordinator_merge_determinista_por_tipo_de_tarea"
    - "Añade_completitud_check_X_de_Y_subtareas_listas"
    - "Añade_drift_detection_divergence_kl_residual"

F7_proceso_100_Python_puro:
  1_TIER_3_a_TIER_2_por_worker:
    logs = worker["eros_memory"]["tier3_raw_log"]
    pulse = {
      total_events: len(logs),
      ok_events: sum(1 for l in logs if l["status"] == "OK"),
      error_events: [l for l in logs if l["status"] != "OK"],
      duration_ms: logs[-1]["timestamp"] - logs[0]["timestamp"]
    }
    worker["eros_memory"]["tier2_pulse_buffer"] = pulse

  2_TIER_2_a_TIER_1_global:
    all_pulses = [w["tier2"] for w in workers]
    summary = {
      ok: sum(p["ok_events"] for p in all_pulses) / sum(p["total_events"]) >= 0.9,
      critical_errors: [e for p in all_pulses for e in p["error_events"]][:3],
      avg_duration_ms: sum(p["duration_ms"] for p in all_pulses) / len(all_pulses),
      completitud: len(certified_outputs) / len(workers)
    }

  3_MERGE_DETERMINISTA:
    CODE: concat_code_files(certified_outputs)
    MULTI: merge_json_outputs(certified_outputs)
    MIXTO: merge_by_subtask_type(certified_outputs)

F7_checkpoints: state.json["f7"] = {tier1, merged, informe}
F7_salida: {merged_output, tier1_summary, informe_pre_entrega}
F7_aborto: SI_completitud_lt_50%
```

### F8 Repair Pipeline (5 Pasos + Métricas Duras)

```yaml
fase_F8:
  nombre_original: Fase_8_Repair_Pipeline_5_pasos
  estado_v44:
    preservado: true
    modificado: true
    ampliado: true
  cambios:
    - "Paso_1_Retry_mismo_DSL_3_intentos_preservado"
    - "Paso_2_Cambia_a_DSL_mas_simple_jerarquia_v3_v2_v1"
    - "Paso_3_Reduce_contexto_50%_re_ejecuta_DSL"
    - "Paso_4_Restore_checkpoint_snapshot_previo_preservado"
    - "Paso_5_Aborto_duro_con_5_metricas_context_integrity_score"
    - "Elimina_Fallback_Model_o_Agent_requeria_LLM_adicional"
    - "Añade_metricas_duras_para_decision_aborto"

5_pasos_repair:
  Paso_1_retry_x3:
    re_ejecuta_mismo_DSL_mismo_contexto
    si_exito_reemplaza_output
    si_falla_x3_paso_2
  Paso_2_DSL_jerarquico:
    intenta_v2_medio_menos_campos_obligatorios
    si_falla_intenta_v1_minimo_solo_campo_critico
    si_falla_paso_3
  Paso_3_reduce_contexto_50%:
    trunca_input_data_a_la_mitad
    re_ejecuta_DSL_mas_simple
    si_exito_output_parcial_calidad_degradada
    si_falla_paso_4
  Paso_4_restore_checkpoint:
    recupera_state_json_de_checkpoint_F3
    re_ejecuta_pipeline_desde_F3
    si_exito_output_restaurado
    si_falla_paso_5
  Paso_5_evalua_aborto_5_metricas:
    schema_compliance_rate_lt_0.5_a_CORRUPT
    output_divergence_index_gt_0.3_a_CORRUPT
    dsl_execution_failure_rate_gt_0.4_a_CORRUPT
    repair_pattern_stability_true_a_CORRUPT
    token_budget_deviation_gt_3.0_a_CORRUPT
    2_plus_flags_CORRUPT_a_ABORTA_reporta_usuario
    1_flag_a_DEGRADED_retry_alternativo
    0_flags_a_CONTINUA_improbable

F8_checkpoints: state.json["f8"] = {repaired, aborted, metrics}
F8_salida: {repaired_outputs, aborted, status: OK|PARTIAL|ABORTED}
```

### F9 Entrega Final y Reporte Automático

```yaml
fase_F9:
  nombre_original: Fase_9_Consolidacion_Final_y_Entrega
  estado_v44:
    preservado: true    # 100%_codigo_puro_preservado
    modificado: false
    ampliado: false
  conclusion: >
    Responsabilidad_preservada_entregar_resultado_al_usuario
    Proceso_preservado_merge_empaquetado_state_final
    Sin_modificaciones_Fase_mas_estable_del_pipeline

F9_proceso_100_Python_puro:
  1_empaquetado_segun_modo:
    MODE_CODE: zip_codigo_tests_docs_README
    MODE_MULTI: JSON_estructurado_resumen_md
    MODE_MIXTO: zip_combinado

  2_reporte_automatico_Python_genera_no_LLM:
    reporte = {
      modo: execution_profile,
      modelo_principal: "Qwen_si_CODE_si_no_Gemma4_si_MULTI_si_no_Mixto",
      llm_penso: True_si_F4_usado_si_no_False,
      errores_llm: len([e for e in state if e.get("llm_error")]),
      errores_codigo_puro: len([e for e in state if e.get("code_error")]),
      calidad_score: calcular_calidad(state),
      tiempo_total_ms: state["f9"]["timestamp"] - state["f-1"]["timestamp"],
      tokens_total: sum(s.get("tokens", 0) for s in state.values()),
      dominios_f55: [d for d in domain_registry if d.get("f55_cubierto")],
      metricas_f5: {max_stress, max_anxiety, max_divergence},
      metricas_f8: {repairs, aborts},
      trazabilidad_completa: True
    }

  3_state_json_final:
    añade_f9_con_timestamp_reporte_paths_entrega

F9_salida_al_usuario:
  - resultado_empaquetado_zip_o_json_o_md
  - reporte_ejecucion_completo
  - state_json_con_trazabilidad

F9_aborto: NINGUNO_ultima_fase_entrega_lo_que_tenga
```

### Ruta de Diseño F6 → F7 → F8 → F9

```yaml
F6_a_F7:
  quien_llama: f6_verificador_py
  quien_recibe: f7_consolidador_py
  datos: [certified_outputs, eros_memory_workers, schemas]
  validaciones: certified_outputs_no_vacio_si_vacio_a_F8_Repair_todo
  rollback: SI_checkpoint_F6

F7_a_F8:
  quien_llama: f7_consolidador_py
  quien_recibe: f8_repair_py
  datos: [rejected_outputs, failed_workers, informe_pre_entrega]
  validaciones: rejected_no_vacio_si_vacio_salta_F8_a_F9
  rollback: SI_checkpoint_F7

F8_a_F9:
  quien_llama: f8_repair_py
  quien_recibe: f9_deliver_py
  datos: [repaired_outputs_puede_vacio, merged_output_F7, state_json_completo]
  validaciones: state_json_tiene_F-1_a_F8
  rollback: NINGUNO

F9_a_USUARIO:
  quien_llama: f9_deliver_py
  quien_recibe: usuario_interfaz
  datos: [empaquetado, reporte, state_final]
  validaciones: empaquetado_no_vacio_reporte_campos_obligatorios
  rollback: NINGUNO
```


## DOC FUSIÓN 357d97be — BLOQUE 1: F-1 a F3 (Motor de Preparación) Pipeline v4.4

### Header JSON Obligatorio

```json
{
  "document_id": "BLOQUE_1_F-1_F3_MOTOR_PREPARACION",
  "version": "v4.4",
  "status": "PRE-APROBADO",
  "autor": "Panel Arquitectos MAXBRY (Kimi K + Claude + GPT)",
  "fecha": "2026-06-02",
  "pieza_rompecabezas": true,
  "ledger_v": "DEBATE_NCT_FUSION_2026_06_02",
  "checksum": "SHA256_BLOQUE1",
  "dependencias": ["config/signals.yaml", "config/domain_registry.yaml", "config/isolation_policy.yaml"],
  "puzzle_coords": {"x": 1, "y": 1, "z": "preparacion"}
}
```

### Verificación Cruzada de Preservación

```yaml
| Fase | Existe en Doc Base | Estado v4.4 | Responsabilidad Preservada | Riesgo Estructural |
|------|-------------------|-------------|---------------------------|-------------------|
| F-1  | NO_nueva          | NUEVA_ADITIVA | Pre_estimar_tokens_y_pesos_contextuales | NINGUNO |
| F0   | SI                | PRESERVADA_MEJORADA | Clasificar_modo_CODE_o_MULTI_o_MIXTO | NINGUNO |
| F1   | SI                | PRESERVADA_MEJORADA | Seleccionar_ruta_y_workers | NINGUNO |
| F2   | SI                | PRESERVADA_MEJORADA | Planificar_DAG_detectar_ciclos | NINGUNO |
| F3   | SI                | PRESERVADA_MEJORADA | Aislar_contexto_precargar_DSL | NINGUNO |

veredicto: >
  Ninguna_fase_eliminada_Ninguna_responsabilidad_perdida
  1_fase_nueva_aditiva_F-1_4_fases_mejoradas_F0_a_F3
```

### F-1: MYTHOS PREP LOOP (NUEVA, 100% Python)

```yaml
objetivo: pre_estimar_complejidad_y_tokens_antes_de_clasificar
evitar: lanzar_F4_con_tareas_que_exceden_budget_sin_aviso

proceso_100_python:
  1_cargar_config_yaml: yaml.safe_load(open(config_path))
  2_tokens_estimados: len(texto_raw) // 4
  3_peso_code: sum(signals.code.get(t, 0) for t in tokens)
  4_peso_multi: sum(signals.multi.get(t, 0) for t in tokens)
  5_aplicar_boost_rules:
    - trigger: ['python', 'script'] multiplier: 2.5  # Script Python = código con alta certeza
    - trigger: ['docker', 'kubernetes'] multiplier: 2.2  # Infraestructura containerizada = código
    - trigger: ['api', 'rest'] multiplier: 1.8  # API implica desarrollo backend
    - trigger: ['microservicio', 'deploy'] multiplier: 2.0  # Arquitectura distribuida = código complejo
  6_diff: abs(peso_code - peso_multi)
  7_umbral: thresholds.modo_unico  # 1.5
  8_modo_preliminar:
    - diff_gt_umbral: CODE_si_peso_code_gt_peso_multi_si_no_MULTI
    - else: MIXTO

config_signals_yaml_ejemplo:
  code:
    python: 1.0
    script: 1.0
    api: 1.5
    funcion: 1.0
    clase: 1.2
    test: 1.3
    deploy: 1.4
    refactor: 1.3
    docker: 1.2
    kubernetes: 1.3
    microservicio: 1.4
    backend: 1.1
    frontend: 1.1
  multi:
    resumen: 1.0
    informe: 1.0
    traduce: 0.8
    analiza: 0.3
    investiga: 0.9
    planifica: 0.7
    redacta: 0.8
    clasifica: 0.6
    email: 0.5
    noticia: 0.7
    articulo: 0.8
    documento: 0.6
  thresholds:
    modo_unico: 1.5
    default_mixto: true

errores_posibles_F-1:
  texto_vacio_len_eq_0: tokens_eq_0_modo_preliminar_MIXTO
  keyword_desconocida_peso_eq_0: ignora_no_aborta
  config_no_encontrada_FileNotFoundError: aborta_ERROR_F1_CONFIG_INVALIDA

checkpoint: state.json["f-1"] = {tokens_estimados, peso_code, peso_multi, diff, modo_preliminar, keywords_detectados}
```

### F0: CLASIFICACIÓN DUAL → UNIFICADA (100% Python)

```yaml
objetivo: determinar_modo_final_CODE_o_MULTI_o_MIXTO_con_fuente_unica_de_verdad

proceso:
  1_cargar_domain_registry_yaml
  2_assert_f1_result.diff_ge_0
  3_tokens_lower_split
  4_code_hits: [t for t in tokens if t in clasificacion.keywords.code_indicators]
  5_multi_hits: [t for t in tokens if t in clasificacion.keywords.multi_indicators]
  6_diff: f1_result.diff
  7_umbral: clasificacion.thresholds.modo_unico  # 1.5
  8_modo_final:
    - diff_gt_umbral: CODE_si_peso_code_gt_peso_multi_si_no_MULTI
    - else: MIXTO
  9_confianza: diff_div_umbral_x_2_si_diff_lt_umbral_x_2_si_no_1.0

boost_pairs:
  - [python, script]
  - [docker, kubernetes]
  - [api, rest]
  - [microservicio, deploy]

errores_posibles_F0:
  ambiguedad_total_diff_eq_0: default_MIXTO
  config_inconsistente_signals_source_no_existe: aborta_ERROR_F0_CONFIG_INVALIDA

checkpoint: state.json["f0"] = {modo_final, confianza, code_hits, multi_hits, tokens_estimados}
```

### F1: RUTEO POR TABLA DE VERDAD + PERFILES (100% Python)

```yaml
objetivo: producir_perfiles_ejecucion_verificacion_y_worker_NO_seleccionar_implementaciones_concretas

execution_profiles:
  CODE:
    type: code_generation
    verification_profile: code_verification
    worker_profile: architecture_generation
    f6_capa2: llm_anclado_condicional
    description: 'Genera_codigo_nuevo_arquitectura_de_proyecto_refactor'
  MULTI:
    type: task_execution
    verification_profile: task_verification
    worker_profile: domain_specific
    f6_capa2: codigo_puro
    description: 'Ejecuta_tareas_de_dominio_con_DSL_predefinido'
  MIXTO:
    type: hybrid
    verification_profile: hybrid_verification
    worker_profile: mixed
    f6_capa2: codigo_puro
    description: 'Hibrido_parte_codigo_parte_tarea'

worker_profiles:
  architecture_generation:
    description: 'Disena_estructura_de_proyectos_de_codigo'
    capabilities: [code_structure, tests_design, docs_technical]
  code_generation:
    description: 'Escribe_codigo_fuente_y_tests_unitarios'
    capabilities: [code_write, tests_write, syntax_check]
  domain_specific:
    description: 'Ejecuta_tareas_de_dominio_con_DSL_predefinido'
    capabilities: [dsl_execution, schema_validation, format_output]
  mixed:
    description: 'Hibrido_parte_codigo_parte_tarea'
    capabilities: [code_structure, dsl_execution]

router_code_steps: [design_architecture, write_code, write_tests, verify_code]
router_multi_steps: [load_dsl, execute_dsl, validate_output]
router_mixto_steps: [classify_subtasks, route_code_subtasks, route_multi_subtasks, merge_results]

errores_posibles_F1:
  modo_invalido_not_in_profiles: aborta_ERROR_F1_MODO_INVALIDO
  config_no_encontrada: aborta_ERROR_F1_CONFIG_INVALIDA

checkpoint: state.json["f1"] = {execution_profile, verification_profile, worker_profile, f6_capa2_config, ruta_config, modo}
```

### F2: PLAN DAG DETERMINISTA + PRESUPUESTO OPERATIVO

```yaml
objetivo: >
  Ordenar_subtareas_en_grafo_dirigido_detectar_ciclos
  Validar_presupuesto_tokens_o_runtime_antes_de_aprobar_DAG

# Continúa en el doc, depende de DAGs
```


### F2: PLAN DAG DETERMINISTA + PRESUPUESTO OPERATIVO (Detalle Completo)

```python
# f2_plan_dag.py — Topological sort + presupuesto + detección ciclos
def f2_plan_dag(subtareas: list, registry_path='config/domain_registry.yaml') -> dict:
    G = nx.DiGraph()
    
    # 1. Añadir nodos con presupuesto
    for s in subtareas:
        G.add_node(s['id'],
            estimated_tokens=s.get('estimated_tokens', len(str(s.get('dsl', ''))) // 4),
            estimated_runtime=s.get('estimated_runtime', 5.0),
            worker_profile=s.get('worker_profile'),
            dsl_file=s.get('dsl'),
            schema_file=s.get('schema'))
    
    # 2. Añadir aristas (dependencias)
    for s in subtareas:
        for dep in s.get('dependencies', []):
            if dep in G.nodes():
                G.add_edge(dep, s['id'])
    
    # 3. VALIDAR PRESUPUESTO ANTES de topological sort
    total_tokens = sum(G.nodes[n]['estimated_tokens'] for n in G.nodes())
    total_runtime = sum(G.nodes[n]['estimated_runtime'] for n in G.nodes())
    
    if total_tokens > 32000:
        return {status: PRESUPUESTO_EXCEDIDO, accion: solicitar_confirmacion_usuario}
    if total_runtime > 30:
        return {status: RUNTIME_EXCEDIDO, accion: solicitar_confirmacion_usuario}
    
    # 4. Topological sort + detección ciclos
    orden = list(nx.topological_sort(G))
    ciclo = nx.find_cycle(G, orientation='original')  # aborta si hay
    
    # 5. Agrupar paralelos por niveles
    niveles = {}
    for n in orden:
        nivel = max(niveles.get(pred, 0) + 1 for pred in G.predecessors(n))
        niveles[n] = nivel
    grupos = {nivel: [] for nivel in set(niveles.values())}
    for n, nivel in niveles.items():
        grupos[nivel].append(n)
    
    # 6. Generar execution_manifest
    manifest = [{
        node_id, worker_profile, dependencies,
        context_budget: {tokens, runtime_seconds},
        dsl_profile: {dsl_file, schema_file, output_schema},
        execution_profile, verification_profile, parallel_group
    } for node_id in orden]
    
    return {status: OK, orden_ejecucion, grupos_paralelos, total_tokens, total_runtime, presupuesto_aprobado: True, execution_manifest}
```

```yaml
limits:
  max_tokens: 32000
  max_runtime_seconds: 30
  max_workers: 100
  max_llm_workers: 10

errores_F2:
  ciclo_detectado: ABORTA_reporta_usuario_con_nodos_involucrados
  presupuesto_excedido_tokens_gt_32000: solicita_confirmacion_usuario
  runtime_excedido_gt_30s: solicita_confirmacion_usuario
  dependencia_a_nodo_inexistente: ignora_arista_log_warning

checkpoint: state.json["f2"] = {status, orden_ejecucion, grupos_paralelos, total_tokens, total_runtime, presupuesto_aprobado, execution_manifest}
```

### F3: AISLAMIENTO + PRECARGA DSL + BUFFERS EROS (Detalle Completo)

```python
# f3_aislamiento.py — Prepara workers con memoria aislada
def f3_aislar_workers(manifest: list, policy_path='config/isolation_policy.yaml') -> dict:
    workers = []
    for item in manifest:
        worker = {
            id: item['node_id'],
            profile: item['worker_profile'],
            local_context: {input_data: None, dsl_loaded: False, schema_validated: False, output_buffer: None, execution_start: None, execution_end: None},
            eros_memory: {
                tier3_raw_log: [],
                tier2_pulse_buffer: {start_time, end_time, status: pending, tokens_used: 0, errors: [], events: []},
                tier1_summary_slot: None
            },
            context_budget: item['context_budget'],
            dsl_profile: item['dsl_profile'],
            isolation_policy: {
                blackboard_access: policy.worker.blackboard,
                local_context_access: policy.worker.local_context,
                orchestrator_channel: policy.worker.orchestrator_channel,
                other_workers: policy.worker.other_workers
            }
        }
        
        dsl_valid = validar_dsl(worker)  # AST parse + detecta imports peligrosos os/sys/subprocess/socket
        schema_valid = validar_schema(worker)  # jsonschema.Draft7Validator.check_schema
        
        workers.append(worker)
    
    return {workers_listos: workers, manifest, total_workers: len(workers)}

def validar_dsl(worker: dict) -> bool:
    ast.parse(dsl_content)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in ['os', 'sys', 'subprocess', 'socket']:
                    return False  # IMPORT_PELIGROSO_DETECTADO
    return True
```

```yaml
isolation_policy_yaml:
  worker:
    local_context: read_write
    blackboard: read_only
    orchestrator_channel: write_only
    other_workers: forbidden
  orchestrator:
    local_context: read_write
    blackboard: read_write
    all_workers: read_only
    system_state: read_write
  blackboard:
    scope: global
    write_policy: orchestrator_only
    read_policy: all_workers
    data_types: [system_state, shared_config, progress_summary]
  worker_to_worker:
    direct_communication: forbidden
    indirect_via_orchestrator: allowed
    data_passing: through_blackboard_only
  memory_limits:
    max_local_context_mb: 512
    max_blackboard_read_mb: 64
    max_orchestrator_write_kb: 16

errores_F3:
  DSL_no_encontrado_FileNotFoundError: aborta_subtarea_no_todo_pipeline
  schema_invalido_jsonschema_SchemaError: aborta_subtarea
  DSL_con_imports_peligrosos_os_sys_subprocess: aborta_subtarea_log_seguridad
  memoria_insuficiente_excede_max_local_context_mb: escala_a_modo_secuencial_degradacion

checkpoint: state.json["f3"] = {workers: [{id, profile, local_context, eros_memory, dsl_profile, isolation_policy}], total_workers, dsl_validados, schemas_validados}
```


### Ruta de Diseño — Transiciones F-1 a F3

```yaml
USUARIO_a_F-1:
  quien_llama: main_py
  quien_recibe: f-1_mythos_py
  datos: texto_raw
  validaciones: texto_no_None_len_gt_0
  abortos: NINGUNO_texto_vacio_default_MIXTO
  rollback: NINGUNO

F-1_a_F0:
  quien_llama: f-1_mythos_py
  quien_recibe: f0_clasificador_py
  datos: {texto_raw, tokens_estimados, peso_code, peso_multi, diff, modo_preliminar}
  validaciones: pesos_finitos_diff_ge_0
  abortos: NINGUNO
  rollback: NINGUNO

F0_a_F1:
  quien_llama: f0_clasificador_py
  quien_recibe: f1_router_py
  datos: {modo_final, confianza, code_hits, multi_hits, tokens_estimados}
  validaciones: modo_final_in_[CODE_MULTI_MIXTO]
  abortos: ERROR_F1_MODO_INVALIDO
  rollback: NINGUNO

F1_a_F2:
  quien_llama: f1_router_py
  quien_recibe: f2_plan_dag_py
  datos: {subtareas_tagged, ruta, workers, f6_capa2_config}
  validaciones: subtareas_no_vacias_IDs_unicos
  abortos: NINGUNO
  rollback: NINGUNO

F2_a_F3:
  quien_llama: f2_plan_dag_py
  quien_recibe: f3_aislamiento_py
  datos: {execution_manifest, orden_ejecucion, grupos_paralelos}
  validaciones: execution_manifest_no_vacio_cada_item_dsl_profile_completo_presupuesto_aprobado
  abortos: PRESUPUESTO_EXCEDIDO_ya_aborto_en_F2
  rollback: NINGUNO

F3_a_F4:
  quien_llama: f3_aislamiento_py
  quien_recibe: f4_worker_pool_py
  datos: {workers_listos, grupos_paralelos, execution_profile, verification_profile}
  validaciones: workers_listos_no_vacio_dsl_y_schema_validados_modelo_en_[Qwen_Llama4_Gemma4]
  abortos: WORKERS_LISTOS_VACIO_aborta_pipeline_DSL_NO_VALIDADO_aborta_subtarea
  rollback: SI_checkpoint_F3_permite_re_preparar
```

### Auditoría Decisiones Bloque 1

```yaml
TOTAL_DECISIONES_PYTHON: 28
TOTAL_DECISIONES_LLM: 0
TOTAL_DECISIONES_USUARIO: 0

por_fase:
  F-1: 5_PYTHON
  F0: 4_PYTHON
  F1: 5_PYTHON
  F2: 7_PYTHON
  F3: 7_PYTHON
```

### Consumo LLM Bloque 1

```yaml
BLOQUE_1_TOTAL: 100%_CODIGO_PURO_/_0%_LLM

por_fase:
  F-1: 0%
  F0: 0%
  F1: 0%
  F2: 0%
  F3: 0%
```

### 20 Riesgos Arquitectónicos del Bloque 1

```yaml
R01_signals_yaml_corrupto: ALTA_BAJA_jsonschema_valida_YAML_backup_automatico
R02_domain_registry_inconsistente: ALTA_BAJA_validacion_jsonschema_checksum
R03_F-1_estimacion_tokens_imprecisa: MEDIA_MEDIA_F2_re_valida_presupuesto_real
R04_clasificacion_erronea_F0_modo_equivocado: MEDIA_BAJA_default_MIXTO_si_diff_eq_0_usuario_override
R05_router_YAML_no_encontrado: ALTA_BAJA_validacion_existencia_archivo_antes_de_usar
R06_ciclo_no_detectado_en_F2: ALTA_MUY_BAJA_networkx_find_cycle_+_topological_sort_doble
R07_presupuesto_tokens_subestimado: MEDIA_MEDIA_F2_calcula_suma_real_F4_monitorea
R08_DSL_con_syntax_invalida: MEDIA_BAJA_AST_parse_en_F3_aborta_subtarea
R09_schema_JSON_invalido: MEDIA_BAJA_jsonschema_check_schema_en_F3
R10_DSL_con_imports_peligrosos: ALTA_BAJA_AST_walk_detecta_os_sys_subprocess
R11_memoria_insuficiente_para_workers: MEDIA_MEDIA_degradacion_a_secuencial_limites_configurables
R12_aislamiento_violado_worker_lee_otro_worker: ALTA_MUY_BAJA_politica_YAML_validacion_runtime
R13_F3_no_prepara_EROS_buffers_correctamente: BAJA_BAJA_F7_valida_existencia_tier3_tier2_tier1
R14_execution_manifest_incompleto: MEDIA_BAJA_F3_valida_campos_obligatorios_por_schema
R15_configuracion_de_limites_inconsistente: MEDIA_BAJA_validacion_cruzada_F-1_vs_F2_vs_F4
R16_worker_profile_no_mapea_a_modelo_valido: ALTA_BAJA_lookup_tabla_en_F3_valida_lista_blanca
R17_F1_produce_perfiles_que_F4_no_puede_ejecutar: MEDIA_BAJA_F3_valida_dsl_file_existe
R18_subtareas_sin_dependencias_explicitas_corren_paralelo: MEDIA_MEDIA_DAG_construido_por_F2_usuario_puede_forzar
R19_F-1_boost_rules_con_multiplicador_excesivo: BAJA_BAJA_limites_config_max_multiplier_3.0
R20_keywords_en_signals_yaml_se_solapan: BAJA_BAJA_auditoria_periodica_F0_logea_hits
```

### Veredicto Preservación Bloque 1

```yaml
arquitectura_original_preservada: SI
capacidad_original_desaparecida: NO
fase_simplificada_en_exceso: NO
nueva_arquitectura_estrictamente_superior: SI_en_los_3_objetivos_del_Director

3_objetivos_del_Director:
  1_menos_LLM: Bloque_1_pasa_de_~20%_a_0%
  2_mejor_estructura: Config_centralizada_fuente_unica_DAG_determinista_aislamiento_verificable
  3_multi_modal: F1_ya_diferencia_CODE_o_MULTI_o_MIXTO_con_perfiles_desacoplados
```

### Archivos del Bloque 1

```yaml
f-1_mythos_py: pre_estimacion_tokens_+_pesos_contextuales
f0_clasificador_py: clasificacion_modo_final
f1_router_py: ruteo_por_perfiles
f2_plan_dag_py: planificacion_DAG_+_presupuesto
f3_aislamiento_py: aislamiento_+_precarga_DSL_+_EROS_buffers
config_signals_yaml: pesos_contextuales_keywords
config_domain_registry_yaml: fuente_unica_perfiles_limites_dominios
config_isolation_policy_yaml: politicas_de_aislamiento_memoria
config_router_code_yaml: pasos_modo_CODE
config_router_multi_yaml: pasos_modo_MULTI
config_router_mixto_yaml: pasos_modo_MIXTO
```

### 8 Reparaciones Post-Auditoría GPT

```yaml
A-01_pesos_embebidos_a_configuracion_YAML: signals_yaml_fuente_unica_sin_duplicacion
A-02_fuentes_duplicadas_a_repositorio_central: eliminados_keywords_txt_unica_domain_registry_yaml
A-03_F1_implementaciones_concretas_a_perfiles_desacoplados: F1_produce_worker_profile_F4_resuelve_implementacion
A-04_F2_sin_presupuesto_a_validacion_tokens_runtime_antes_de_DAG: F2_calcula_total_antes_de_topological_sort
A-05_F2_a_F3_handoff_incompleto_a_execution_manifest_formal: manifest_con_8_campos_obligatorios
A-06_F3_sin_EROS_buffers_a_preparacion_nativa: F3_inicializa_tier3_tier2_tier1
A-07_aislamiento_ambiguo_a_politica_YAML_verificable: isolation_policy_yaml_con_permisos_explicitos
A-08_sin_evidencia_preservacion_a_matriz_formal: seccion_1_matriz_por_fase_con_estado_responsabilidad_riesgo
```

### 20 Gaps Detectados y Cerrados (Anexo B)

```yaml
TOTAL_GAPS_DETECTADOS: 20
TOTAL_GAPS_CERRADOS: 20
GAPS_ABIERTOS: 0

G01_a_G20: 20_gaps_todos_cerrados  # Ver detalles en Seccion_15_del_doc
```

### Mapa Responsabilidades Bloque 1

```yaml
Python_Sistema:
  F-1_a_F3: 28_decisiones_todas_python
  archivos: [f-1_mythos_py, f0_clasificador_py, f1_router_py, f2_plan_dag_py, f3_aislamiento_py]

Gemma4_en_bloque_1: NINGUNA  # Solo_en_F4_como_ejecutor_DSL
Qwen_en_bloque_1: NINGUNA     # Solo_en_F4_como_arquitecto_codigo
Llama4_en_bloque_1: NINGUNA   # Solo_en_F4_escritor_y_F5.5_generador_DSL_puntual

DSL_en_bloque_1:
  F3_precargados_desde_disco
  validados_con_AST
  Schema_JSON_validado
  archivos: dsl_resumen_py_dsl_codigo_py_dsl_investigar_py_etc

Domain_Registry:
  signals_yaml_F-1
  domain_registry_yaml_F0_F1_F2_F3
  isolation_policy_yaml_F3
  router_code_yaml_F1
  nota: fuente_unica_de_verdad_para_todo_el_pipeline

EROS_Memoria_Jerarquica:
  F3_inicializa_tier3_raw_log
  F3_inicializa_tier2_pulse_buffer
  F3_inicializa_tier1_summary_slot
  nota: EROS_se_llena_en_F4_F5_se_comprime_en_F7

Usuario_Director:
  F2_confirma_presupuesto_excede_32K_o_30s
  F5.5_Gate_3_aprueba_DSL_fuera_de_Bloque_1
  F8_recibe_reporte_aborto_si_2_plus_metricas_CORRUPT
```


## DOC FUSIÓN 779ccf3b — BLOQUE 3: F5 + F5.5 + F6 (Monitoreo + Generación DSL + Verificación)

### F5: Monitoreo Simultáneo 3-Sistemas (100% Python)

```yaml
fase_F5:
  nombre_original: Fase_5_Monitoreo_Simultaneo_PAD_Ansiedad_Anti-Drift
  estado_v44:
    preservado: true
    modificado: true    # Metricas_emocionales_a_tecnicas_duras
    ampliado: true
  cambios:
    - "Renombra_metricas_emocionales_a_tecnicas_duras"
    - "PAD_a_system_stress_cpu_plus_memory_plus_queue_sobre_3_gt_0.8_a_SIGKILL"
    - "Pleasure_a_success_rate_passed_sobre_total_lt_0.2_a_SIGKILL"
    - "Ansiedad_a_anxiety_level_errores_consecutivos_ge_3_a_confirmar_o_respawn"
    - "Anti-Drift_a_divergence_kl_KL_plan_output_actual_output_gt_0.02_a_rollback"
    - "Mantiene_3_sistemas_simultaneos_ahora_100%_codigo_puro"
    - "Añade_jsonschema_validation_+_timeout_checks_+_pytest"

3_sistemas:
  1_SYSTEM_STRESS_ex_PAD:
    metricas: [cpu_percent_gt_80, memory_percent_gt_80, queue_depth_gt_20]
    formula: stress_eq_cpu_plus_memory_plus_queue_sobre_25_sobre_3
    umbral: stress_gt_0.8_a_SIGKILL_+_respawn
    accion: asyncio.create_task(respawn_worker(id))

  2_ANXIETY_LEVEL_ex_Ansiedad:
    metricas: [errores_consecutivos_por_worker, retries_sin_exito, schema_validation_fails]
    niveles:
      1: 1_error_a_log_warning
      2: 2_errores_a_retry_automatico
      3: ge_3_errores_a_confirmar_o_respawn
    accion: si_nivel_3_a_marca_worker_para_F8_Repair

  3_DIVERGENCE_KL_ex_Anti-Drift:
    formula: KL(plan_output_||_actual_output)_eq_SUM_plan_i_x_log_plan_i_sobre_actual_i
    simplificacion_codigo_puro: diff_ratio_eq_levenshtein(plan_actual)_sobre_len(plan)
    umbral: si_diff_ratio_gt_0.02_a_ROLLBACK
    accion: restore_checkpoint_F3_+_re_ejecutar_worker

frecuencia: cada_500ms_asyncio_loop
checkpoint: state.json["f5"]
aborto: SI_stress_critico_en_multiples_workers
```

### F5.5: Generación DSL para Dominio Nuevo (NUEVA, TRANSITORIA)

```yaml
fase_F5_5:
  estado_v44: NUEVA_ADITIVA
  responsabilidad: >
    Generar_DSL_de_verificacion_para_dominios_nuevos_no_cubiertos
    Llama4_genera_reglas_UNA_SOLA_VEZ_con_3_gates_de_seguridad

activacion:
  F6_detecta: DSL_INCOMPLETO_para_dominio_X
  condicion: domain_registry[dominio][f55_cubierto]_eq_false
  permiso: usuario_aprueba_generacion_configurable

proceso_Llama4_UNA_SOLA_VEZ:
  - Llama4_genera_dsl_lt_dominio_gt_v1_yaml
  - Llama4_genera_template_lt_dominio_gt_py
  - Llama4_genera_tests_lt_dominio_gt_py

3_gates_obligatorios:
  GATE_1_AST_ESTATICO:
    - Python_ast_parse_verifica_syntax_valida
    - Detecta_os_system_eval_exec___import__
    - Detecta_imports_no_declarados
    - Resultado: PASS_o_FAIL
  GATE_2_DOCKER_SANDBOX:
    - Ejecuta_tests_en_contenedor_aislado
    - Timeout_60s
    - Sin_acceso_red_filesystem_host_variables_entorno
    - Resultado: PASS_o_FAIL
  GATE_3_APROBACION_HUMANA:
    - Usuario_revisa_DSL_generado
    - Usuario_aprueba_o_rechaza
    - Si_aprueba_a_domain_registry[dominio][f55_cubierto]_eq_true
    - Si_rechaza_a_aborta_+_reporta

post_aprobar:
  - F6_Capa_2_cambia_a_codigo_puro_para_este_dominio
  - Futuras_tareas_de_este_dominio: 0%_LLM_en_verificacion
  - DSL_se_añade_a_config_o_dsl_o_permanentemente

pct_LLM: Puntual_una_sola_vez_por_dominio
pct_CODIGO: 100%_en_gates_1_y_2
checkpoint: state.json["f5.5"]
aborto: SI_Gate_1_o_2_o_3_falla
```

### F6: Verificación 3-Capas (MEJORADA, Mayoría Python)

```yaml
fase_F6:
  nombre_original: Fase_6_Verificacion_3-Capas_Adversarial_Cruzada_Maker-Checker
  estado_v44:
    preservado: true
    modificado: true    # 3_capas_LLM_a_2_python_+_1_LLM_transitoria
    ampliado: true
  cambios:
    - "Capa_1_jsonschema_Python_puro_reemplaza_LLM_adversarial"
    - "Capa_2_diff_+_checksum_hashlib_Python_puro_reemplaza_LLM_cruzada"
    - "Capa_3_pytest_o_unittest_Python_puro_reemplaza_Maker-Checker_LLM"
    - "Añade_Capa_2_LLM_anclado_SOLO_en_MODE_CODE_y_SOLO_si_f55_cubierto_eq_false"
    - "Añade_DSL_de_verificacion_expandible_por_dominio"
    - "5_dominios_base_cubiertos_web_datos_texto_codigo_imagenes"

3_capas:
  CAPA_1_SCHEMA_VALIDATION_Python_puro:
    jsonschema.validate(output, schema_json)
    ¿todos_campos_obligatorios_presentes?
    ¿tipos_correctos_str_int_list_dict?
    ¿formatos_validos_email_URL_fecha_ISO?
    Resultado: PASS_o_FAIL_con_lista_de_errores

  CAPA_2A_DIFF_CHECKSUM_Python_puro_DEFAULT:
    hashlib.sha256(output.encode()).hexdigest()
    compara_contra_expected_pattern_si_existe
    levenshtein(output, expected)_sobre_len(expected)
    Resultado: PASS_o_DIVERGENCE_DETECTED

  CAPA_2B_LLM_ANCLADO_conditional:
    SOLO_SI:
      - execution_profile_eq_MODE_CODE
      - domain_registry[dominio][f55_cubierto]_eq_false
    LLM_recibe: brief_original_+_output_generado
    pregunta: "¿este_output_contradice_el_brief?"
    respuesta: SI_o_NO_+_razon
    si_SI_a_marca_CONTRADICCION_BRIEF_a_F8_Repair
    si_NO_a_pasa
    NOTA: Capa_2B_es_TRANSITORIA_una_vez_F5.5_cubre_dominio_a_Capa_2B_se_desactiva

  CAPA_3_TESTS_AUTOMATICOS_Python_puro:
    pytest_tests_lt_dominio_gt_py_generados_en_F5.5
    unittest_para_validaciones_especificas
    si_codigo: compile()_+_syntax_check
    si_web: BeautifulSoup_checks_SEO_responsive
    si_datos: pandas_schema_validation
    si_texto: longitud_+_formato_+_encoding
    si_imagenes: dimensiones_+_formato_+_checksum
    Resultado: PASS_o_FAIL_con_logs_detallados

logica_decision:
  Capa_1_FAIL_a_F8_Repair_schema_invalido
  Capa_2A_FAIL_a_F8_Repair_divergencia_detectada
  Capa_2B_CONTRADICCION_a_F8_Repair_brief_violado
  Capa_3_FAIL_a_F8_Repair_tests_no_pasan
  TODAS_PASS_a_output_certificado_a_F7

DSL_verificacion_por_dominio_ejemplos:
  verify_web_py: SEO_responsive_accesibilidad_performance
  verify_datos_py: schema_tipos_nulos_rangos
  verify_texto_py: longitud_formato_encoding_idioma
  verify_codigo_py: syntax_tests_imports_seguridad
  verify_imagen_py: dimensiones_formato_checksum_metadata

checkpoint: state.json["f6"]
aborto: SI_todos_outputs_rechazados
```


## DOC FUSIÓN 9723851c — PARTE 4: INTEGRACIÓN COMPLETA — Ruta F-1 → F9

### Diagrama Global del Pipeline v4.4

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    PIPELINE v4.4 — CONSENSO CLAUDE + KIMI K + GPT             ║
║                         NCT + MAXBRY AGI — BLOQUES 1-4                      ║
╚═══════════════════════════════════════════════════════════════════════════════╝

USUARIO (texto natural)
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 1: MOTOR DE PREPARACIÓN (100% CÓDIGO)                            │
│  F-1 Mythos Prep → F0 Clasificación → F1 Ruteo → F2 Plan DAG → F3 Aislar  │
│  Salida: workers_listos + execution_profile + grupos_paralelos              │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 💡 BLOQUE 2: MOTOR DE EJECUCIÓN (LLM ACTIVA)                               │
│  F4 Worker Pool: MODE_CODE / MODE_MULTI / MODE_MIXTO                        │
│  MODE_CODE: Qwen (arquitectura) + Llama4 (escritura) — 60% LLM / 40% CÓDIGO│
│  MODE_MULTI: Gemma4 (ejecuta DSL) — 30% LLM / 70% CÓDIGO                  │
│  MODE_MIXTO: Variable según subtarea                                        │
│  Límite: 32K tokens / 30s por worker. Semáforo 10 workers LLM.              │
│  Salida: outputs_por_worker + failed_workers + tokens_total               │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 3: CONTROL + VERIFICACIÓN (100% CÓDIGO + F5.5 transitorio)       │
│  F5 Monitoreo (3 sistemas: stress + anxiety + divergence)                   │
│  F5.5 Generación DSL (Llama4 UNA VEZ por dominio nuevo + 3 gates)          │
│  F6 Verificación 3-Capas (2 código puro + 1 LLM transitoria condicional)   │
│  Salida: certified_outputs + domain_registry actualizado                   │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 4: CONSOLIDACIÓN + ENTREGA (100% CÓDIGO)                         │
│  F7 Consolidación EROS 3-Tier (Tier3→Tier2→Tier1)                           │
│  F8 Repair Pipeline (5 pasos + 5 métricas duras)                            │
│  F9 Entrega Final (empaquetado + reporte + state.json inmutable)            │
│  Salida: resultado al usuario con trazabilidad completa                     │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
🎯 USUARIO RECIBE: RESULTADO + REPORTE + STATE.JSON
```

### Tabla Resumen del Pipeline (4 Bloques, F-1 a F9)

```yaml
bloque_1_motor_preparacion_100_codigo:
  fases: [F-1, F0, F1, F2, F3]
  LLM: 0%
  salida: workers_listos + execution_profile + grupos_paralelos

bloque_2_motor_ejecucion_LLM_activa:
  fases: [F4]
  MODE_CODE: Qwen_arquitectura_+_Llama4_escritura  # 60%_LLM_/_40%_CODIGO
  MODE_MULTI: Gemma4_ejecuta_DSL_predefinido        # 30%_LLM_/_70%_CODIGO
  MODE_MIXTO: variable_segun_subtarea
  limites: 32K_tokens_/_30s_por_worker._semaforo_10_workers_LLM
  salida: outputs_por_worker + failed_workers + tokens_total

bloque_3_control_verificacion_100_codigo_mas_F5.5_transitorio:
  fases: [F5, F5.5, F6]
  F5_monitoreo: 3_sistemas_stress_anxiety_divergence
  F5.5_generacion_DSL: Llama4_UNA_VEZ_por_dominio_nuevo_+_3_gates
  F6_verificacion: 3_capas_2_python_+_1_LLM_transitoria_condicional
  salida: certified_outputs + domain_registry_actualizado

bloque_4_consolidacion_entrega_100_codigo:
  fases: [F7, F8, F9]
  F7_consolidacion_EROS_3-Tier: Tier3_a_Tier2_a_Tier1
  F8_repair_pipeline: 5_pasos_+_5_metricas_duras
  F9_entrega_final: empaquetado_+_reporte_+_state_json_inmutable
  salida: resultado_al_usuario_con_trazabilidad_completa
```


### Transiciones F-1 a F9 Detalladas (12 Transiciones)

```yaml
USUARIO_a_F-1:
  quien_llama: main_py
  quien_recibe: f-1_mythos_py
  datos: texto_raw, config_signals_yaml, domain_registry_yaml
  validaciones: texto_no_None_len_gt_0_config_files_existen_parseables
  abortos: NINGUNO_texto_vacio_default_MIXTO
  rollback: NINGUNO

F-1_a_F0:
  quien_llama: f-1_mythos_py
  quien_recibe: f0_clasificador_py
  datos: {texto_raw, tokens_estimados, peso_codigo, peso_multi, diff, modo_preliminar}
  validaciones: pesos_finitos_diff_ge_0_modo_preliminar_in_[CODE_MULTI_MIXTO]
  abortos: NINGUNO
  rollback: NINGUNO

F0_a_F1:
  quien_llama: f0_clasificador_py
  quien_recibe: f1_router_py
  datos: {modo_final, confianza, keywords_detectados, execution_profiles, worker_profiles}
  validaciones: modo_final_en_execution_profiles_execution_profiles_no_vacio
  abortos: ERROR_F1_MODO_INVALIDO
  rollback: NINGUNO

F1_a_F2:
  quien_llama: f1_router_py
  quien_recibe: f2_plan_dag_py
  datos: {subtareas_tagged, execution_profile, verification_profile, f6_capa2_config, limits}
  validaciones: subtareas_no_vacias_IDs_unicos_dependencies_refs_IDs_existentes
  abortos: NINGUNO
  rollback: NINGUNO

F2_a_F3:
  quien_llama: f2_plan_dag_py
  quien_recibe: f3_aislamiento_py
  datos: {execution_manifest, orden_ejecucion, grupos_paralelos, presupuesto_aprobado}
  validaciones: execution_manifest_no_vacio_cada_item_dsl_profile_completo
  abortos: PRESUPUESTO_EXCEDIDO_ya_aborto_en_F2
  rollback: NINGUNO

F3_a_F4:
  quien_llama: f3_aislamiento_py
  quien_recibe: f4_worker_pool_py
  datos: {workers_listos, grupos_paralelos, execution_profile, verification_profile}
  validaciones: workers_listos_no_vacio_dsl_y_schema_validados_modelo_in_[Qwen_Llama4_Gemma4]
  abortos: WORKERS_LISTOS_VACIO_a_aborta_pipeline_DSL_NO_VALIDADO_a_aborta_subtarea
  rollback: SI_checkpoint_F3_permite_re_preparar

F4_a_F5:
  quien_llama: f4_worker_pool_py
  quien_recibe: f5_monitor_py
  datos: {outputs_por_worker, failed_workers, tokens_total, duration_total_ms, eros_memory_tier3_raw_log}
  validaciones: outputs_no_vacio_aunque_parcial_state_json_actualizado
  abortos: OUTPUTS_VACIO_TOTAL_a_aborta_pipeline
  rollback: SI_checkpoint_F4_permite_re_ejecutar

F5_a_F6:
  quien_llama: f5_monitor_py
  quien_recibe: f6_verificador_py
  datos: {outputs_por_worker_filtrados_OK, schemas, acciones_control, domain_registry, execution_profile}
  validaciones: outputs_validados_por_F5_stress_anxiety_divergence_OK
  abortos: NINGUNO_F5_ya_filtro
  rollback: NINGUNO

F6_F5.5_LOOP_CONDICIONAL:
  quien_llama: f6_verificador_py_detecta_DSL_INCOMPLETO
  quien_recibe: f5_5_generador_dsl_py
  datos: {dominio, brief, ejemplos_dsl, execution_profile, domain_registry, auto_generate}
  validaciones: dominio_no_en_registry_o_f55_cubierto_eq_false_auto_generate_eq_True
  abortos: GATE_1_FAIL_GATE_2_FAIL_GATE_3_RECHAZO
  rollback: NINGUNO_F5.5_es_aditivo_no_destructivo

F5.5_a_F6_post_aprobacion:
  quien_llama: f5_5_generador_dsl_py_Gate_3_aprobado
  quien_recibe: f6_verificador_py
  datos: {dsl_nuevo, tests_nuevo, domain_registry_actualizado_f55_cubierto_eq_true}
  validaciones: dsl_nuevo_existe_parseable_AST_tests_nuevo_pasan_en_sandbox
  abortos: NINGUNO_ya_paso_3_gates
  rollback: NINGUNO

F6_a_F7:
  quien_llama: f6_verificador_py
  quien_recibe: f7_consolidador_py
  datos: {certified_outputs, rejected_outputs, schemas, verification_results, capa2b_usada, domain_registry, eros_memory_workers, execution_profile}
  validaciones: certified_outputs_no_vacio_si_vacio_a_F8_Repair_todo
  abortos: NINGUNO_F8_maneja_rechazados
  rollback: SI_checkpoint_F6_permite_re_verificar

F7_a_F8:
  quien_llama: f7_consolidador_py
  quien_recibe: f8_repair_py
  datos: {rejected_outputs, failed_workers, informe_pre_entrega, merged_output, domain_registry, dsl_hierarchy, repair_limits}
  validaciones: dsl_hierarchy_tiene_v3_v2_v1_definidos
  abortos: NINGUNO
  rollback: SI_checkpoint_F7_permite_re_consolidar

F8_a_F9:
  quien_llama: f8_repair_py
  quien_recibe: f9_deliver_py
  datos: {repaired_outputs, merged_output, state_json_completo, reporte_parcial, delivery_formats}
  validaciones: state_json_tiene_F-1_a_F8_state_json_f9_no_existe_evita_doble_entrega
  abortos: NINGUNO_F9_es_ultima_fase
  rollback: NINGUNO

F9_a_USUARIO:
  quien_llama: f9_deliver_py
  quien_recibe: usuario_interfaz
  datos: {empaquetado, reporte, state_final_inmutable}
  validaciones: empaquetado_no_vacio_reporte_tiene_campos_obligatorios_12_campos
  abortos: NINGUNO
  rollback: NINGUNO
```

### Auditoría Decisiones Pipeline Completo

```yaml
F-1: pre_estimar_tokens_asignar_pesos_contextuales_pre_clasificar_modo  # 3_PYTHON
F0:  regex_matching_sumar_pesos_comparar_umbral_seleccionar_modo_final  # 4_PYTHON
F1:  seleccionar_router_YAML_asignar_execution_verification_worker_perfiles_configurar_F6_capa2  # 5_PYTHON
F2:  construir_grafo_orden_topologico_detectar_ciclos_validar_presupuesto_decidir_paralelismo  # 5_PYTHON
F3:  spawn_workers_aislar_memoria_cargar_DSL_validar_schema_asignar_modelo_preparar_EROS  # 6_PYTHON
F4:  semaforo_workers_LLM_scheduling_paralelo_timeout_validar_schema_token_accounting  # 6_PYTHON
F4:  generar_codigo_nuevo_ejecutar_DSL_predefinido  # 2_LLM_Llama4_Qwen_Gemma4
F5:  calcular_stress_calcular_anxiety_calcular_divergence_decidir_SIGKILL_respawn_rollback  # 6_PYTHON
F5.5: decidir_activacion_generar_DSL_validar_AST_ejecutar_sandbox  # 4_PYTHON_+_1_LLM_+_1_USUARIO
F6:  validar_schema_calcular_diff_checksum_seleccionar_capa_ejecutar_tests_decidir_certificar  # 6_PYTHON
F6:  verificar_brief_capa_2B  # 1_LLM_transitorio
F7:  compresion_Tier3_a_Tier2_compresion_Tier2_a_Tier1_merge_determinista_calcular_completitud  # 4_PYTHON
F8:  retry_mismo_DSL_cambiar_DSL_jerarquico_reducir_contexto_restore_checkpoint_evaluar_5_metricas_decidir_aborto  # 6_PYTHON
F9:  empaquetar_generar_reporte_escribir_state_final  # 3_PYTHON
```

### Consumo LLM por Fase

```yaml
F-1: 0%
F0:  0%
F1:  0%
F2:  0%
F3:  0%
F4_CODE: 60%_Qwen_+_Llama4
F4_MULTI: 30%_Gemma4
F4_MIXTO: variable_segun_subtarea
F5:  0%
F5.5: 0%_amortizado_una_vez_por_dominio
F6_CAPA1: 0%
F6_CAPA2A: 0%
F6_CAPA2B: 0_a_5%_transitorio_solo_si_f55_cubierto_eq_false
F6_CAPA3: 0%
F7:  0%
F8:  0%
F9:  0%

PROMEDIOS_POR_MODO:
  MODE_CODE: ~93%_codigo_/_~7%_LLM  # F4_60%_mas_F6_Capa2B_5_a_7%
  MODE_MULTI: ~99%_codigo_/_~1%_LLM  # F4_30%_mas_F6_0%
  MODE_MIXTO: variable_ponderado_por_subtareas_CODE_vs_MULTI
  GLOBAL: ~97%_codigo_/_~3%_LLM_amortizado
```

