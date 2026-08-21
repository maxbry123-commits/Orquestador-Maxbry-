---
doc_id: MAXBRY-ORQUESTACION-FROM-DOCS
fecha: 2026-07-04
fuente: 57 documentos de /workspace/attachments/
formato: AI-FRIENDLY (lenguaje de programación, no prosa)
regla: Solo lo que dice TEXTUALMENTE cada doc. Sin inventar.
separación: ORQUESTACIÓN aquí. AGENTES en doc aparte.
---

# ORQUESTACIÓN — Extraída textualmente de los 57 docs

## DOC 16: DSL + Universal Plug v1.5

```yaml
dsl_tipos: [task, pipeline, agent, skill, project, workflow, dag]
schemas: [task.v1.json, pipeline.v1.json, agent.v1.json, skill.v1.json, project.v1.json, workflow.v1.json, dag.v1.json]
contrato_modulo:
  obligatorios: [module_id, version, interface.inputs, interface.outputs]
  opcionales: [dependencies, capabilities, limits, metadata, tags, author]
  validacion: [schema_draft_07, module_id_unico, version_semver, interface_tipado, dependencies_resolubles]
modulo_ejemplo: ma_code_gen  # category J-IA, owner g5-orquestador
flujo_dsl: parse→validate→generate_plan→execute→validate→deliver
flujo_pipeline: parse(MA-01)→plan(MA-06)→execute(MA-15)→verify(MA-16)
validacion_cruzada: cada_doc_refs_min_2_otros
```

### Diagrama horizontal
```
USER → [MA-01:parse] → [MA-06:plan] → [MA-15:execute] → [MA-16:verify] → DELIVER
```

---

## DOC 01: Constitución del Orquestador (G5)

### Principios constitucionales v1.0 (1-13)

```yaml
P1_filosofia: Director_de_Empresa_no_IA
P2_escala: [2000_agentes_capacidad, 1000_tareas_simultaneas, no_disenar_2000_reales]
P3_no_ia_codigo: 90%_codigo_determinista + 10%_LLM
P4_director_empresa: [planifica, asigna, contrata, despide, supervisa, reporta, decide]
P5_10_estados_tarea: [CREADA, EN_COLA, ASIGNADA, EJECUTANDO, PAUSADA, VALIDANDO, COMPLETADA, FALLIDA, CANCELADA, REPLANIFICADA]
P6_pizarras: [proyecto, maestra]
P7_escalado_horizontal: agregar_nodos_no_poder
P8_colmenas: [codigo, testing, investigacion, auditoria, output, investigacion_hf, aprendizaje, meta]
P9_multi_modelo: intercambiable_por_tarea_costo_calidad
P10_minima_infra: $0_objetivo
P11_escala_10_2000: sin_redesign
P12_organizacion_absoluta: nada_se_pierde_nada_se_duplica
P13_so_distribuido: [kernel, process_manager, file_system, scheduler, ipc, memory, io]
```

### v2.0 (14-26)

```yaml
P14_auto_evolucion: [meta_learning, self_improving, auto_curacion, counterfactual, causalidad]
P15_skills_persistentes: [persistencia, respaldo, versionado, replicacion]
P16_raiz_unica_skills: BIS
P17_juez_supervisor: 8_reglas_validan_todo
P18_auto_run_primera_ejecucion: 6_pasos
P19_cifrado_total: nada_texto_plano
P20_nucleo_solo_api
P21_bootstrap_autonomo
P22_10_modulos_independientes: [Input, SID, BIS, Loop, CSA, Output, OOS, OVFS, Memoria, Orquestador]
P23_cero_configuracion
P24_descarga_inteligente
P25_inicio_autonomo
P26_escalabilidad_horizontal
```

### v3.0 (27-39)

```yaml
P27_csa_10_jueces_5_fases_veto
P28_sid_sistema_inteligente_definicion
P29_input_engine_v4_54_componentes
P30_semantic_invariant_checker
P31_output_engine_ovfs
P32_micro_separacion_20_carpetas
P33_39: restantes_definidos_parches
```

### CSA — 10 Jueces con 5 Fases

```yaml
jueces:
  J1: comprension_objetivo
  J2: cobertura_requisitos
  J3: consistencia_logica
  J4: exactitud_tecnica
  J5: arquitectura_diseno
  J6: calidad_codigo
  J7: investigacion_evidencia
  J8: optimizacion_rendimiento
  J9: seguridad_riesgos
  J10: calidad_final_ux
fases_por_juez: [F1_audita_input, F2_busca_lo_que_nadie_reviso, F3_10_soluciones, F4_destruye_propia, F5_ataca_otros_9]
veto: cualquier_juez_puede_vetar
regla_intocable: 10_jueces_NO_se_reemplazan_NO_se_modifican
```

### SID — 5 Preguntas Fijas

```yaml
Q1: objetivo_real
Q2: restricciones_aplican
Q3: recursos_disponibles
Q4: criterio_exito
Q5: riesgos
regla: intocables
```

### Input Engine v4.0 — 54 Componentes (45 originales + 9 nuevos 100X)

```yaml
originales_45: [sid_9, input_base_11, mejoras_17, auditores_3, capas_4]
nuevos_9_100X:
  A: input_swarm_bus_eventos  # 40-60 agentes
  B: input_discovery  # 10 detectores (idioma, dominio, intencion, objetivos_implicitos, restricciones, prioridades, entregables, formato, audiencia, dependencias_externas)
  C: input_forensics  # 10 detectores (contradicciones, ambiguedad, huecos, requisitos_ocultos, riesgos, datos_inventados, inconsistencias_temporales, conflictos_tecnologicos, imposibilidades, scope)
  D: knowledge_discovery  # 15 fuentes (papers, stackoverflow, reddit, skills_internos, base_conocimiento, memoria_proyecto, artefactos, apis, plugins, modelos_apis, documentacion, repos_publicos, issues, wikis, foros)
  E: claude_definition_engine_v2  # 6 fases (auto_respuesta, multi_interpretacion, simulacion, arbol_decisiones, preguntas_agrupadas, definition_score_>=95)
  F: input_compiler_expandido  # (knowledge_graph, goal_tree, requirement_tree, constraint_tree, context_graph)
  G: quality_swarm  # 10 auditores con veto
  H: input_governor  # 6 estados (RECIBIDO, ANALIZANDO, DEFINIENDO, COMPILANDO, AUDITANDO, APROBADO|VETADO|REPLANIFICAR|PREGUNTAR)
  I: input_digital_twin  # simulacion completa antes de ejecutar
```

### Output Engine (13) + OOS v3.1 (14) + OVFS

```yaml
output_engine_13: [planner, compiler_ast, graph, smart_chunking, dynamic_output, manifest, registry, router, destination_engine, streaming, validator, multi_target_delivery, reanudacion]
oos_v31_14: [contrato_salida, uom, semantic_chunk, adaptive_chunk_size, predictive_planner, auto_format_negotiation, intelligent_packaging, multi_delivery_pipeline, intelligent_compression, smart_version_control, incremental_publishing, intelligent_resume, output_verification, delivery_policy_engine]
ovfs_estructura: [README.md, docs/, backend/, frontend/, tests/, diagrams/, prompts/, metadata/]
```

### Output v6.1 Gobernanza — 16 Capas + 8 Estados

```yaml
estados_gobernador: [APROBAR, CORREGIR, REGENERAR, REPLANIFICAR, DIVIDIR, INVESTIGAR_MAS, PREGUNTAR_USUARIO, CANCELAR]
capas_16:
  A: output_governor
  B: output_digital_twin
  C: multi_version_generator  # 5 versiones (calidad, velocidad, minimo_consumo, documentacion, codigo_optimizado)
  D: output_fusion_engine
  E: acceptance_test_engine
  F: output_coverage_map
  G: explainability_engine
  H: output_provenance
  I: consistency_swarm  # 20 microagentes
  J: artifact_relationship_graph
  K: release_manager
  L: output_memory
  M: output_score  # minimo 95% configurable
  N: human_approval_layer
  O: adaptive_delivery
  P: closed_feedback_loop  # LA_MAS_IMPORTANTE
```

### LOOP v6.0 — 15 Capas + 3 Ciclos Paralelos

```yaml
capas_15:
  A: workflow_dag  # no_pipeline
  B: runtime_kernel  # tipo_os
  C: event_sourcing
  D: state_machine_por_tarea
  E: prediction_engine
  F: dynamic_replanning
  G: model_router_inteligente
  H: trust_engine
  I: goal_monitor_permanente
  J: contract_engine
  K: resource_economy
  L: semantic_diff
  M: universal_artifact_graph
  N: failure_recovery_engine
  O: executive_board  # 3-5 agentes
ciclos_paralelos_3:
  A_ejecucion: [CREAR, VALIDAR, CORREGIR, ENTREGAR]
  B_supervision: [MONITORIZAR, MEDIR, REPLANIFICAR]
  C_aprendizaje: [REGISTRAR, ANALIZAR, OPTIMIZAR, ACTUALIZAR_REGLAS]
comunicacion: bus_de_eventos
```

### BIS — 14 Categorías + 13 Criterios + 3 Versiones

```yaml
categorias_14: [ARQUITECTURA, GESTION, FRONTEND, BACKEND, MOVIL, ESCRITORIO, BASES_DE_DATOS, APIs, DEVOPS, IA, TESTING, SEGURIDAD, AUTOMATIZACION, LENGUAJES]
criterios_13: [relevancia, efectividad, costo, compatibilidad, mantenibilidad, documentacion, reusabilidad, seguridad, performance, escalabilidad, compliance, test_coverage, comunidad]
versiones_3: [v1_inicial, v2_mejorada_con_debate, v3_avanzada_productor_consumidor]
debate_4_especialistas: [productor, consumidor, auditor, critico]
mejoras_100X:
  F: 5_investigadores_paralelos
  G: renovacion_cada_15_dias
  H: detector_intencion
  I: pre_descarga_inteligente
```

### 10 Propuestas M3 Output (9 aprobadas + 1 rechazada)

```yaml
aprobadas: [pre_mortem, auto_rollback, meta_learning, output_personalization, multi_stakeholder, causal_tracing, output_marketplace, self_improving_quality, production_monitoring]
rechazada: [output_sandbox]  # por MAX
```

### 10 Propuestas M3 Input/Loop (todas aprobadas)

```yaml
aprobadas: [meta_agentes, causalidad, counterfactual, auto_modificacion_codigo, memoria_episodica, zero_shot_transfer, neural_architecture_search, time_travel_debugging, inteligencia_colectiva_emergente, auto_curriculum]
```

### Regla absoluta MAX

```yaml
regla: NUNCA_crear_ni_cambiar_nada_sin_APROBADO_explicito
regla2: SOLO_AGREGO_capas_NUNCA_reemplazo
regla3: MANTENER_todos_los_nombres_originales
```

### Cosas Intocables

```yaml
intocables: [10_Jueces_CSA, Auditor_SID_5_preguntas, Constitucion_39_principios, 14_categorias_BIS, 30_micro_agentes, 11_internal_roles, 10_parallel_queues, 10_agent_consensus_council, 6_autonomy_levels_L1_L6, 12_task_models_TM01_TM12, 5_loop_versions_ALV_LOP, 3_monitors, 9_GGUF_models_confirmados, 16_API_keys]
```

### Diagrama horizontal Constitución

```
INPUT → [SID:5Q] → [INPUT_ENGINE:54] → [BIS:14cat] → [CSA:10J×5F] → [LOOP:15capas+3ciclos] → [OUTPUT_ENGINE:13] → [OOS:14] → [OVFS] → DELIVERY
```

---

## DOC 03: Constitución Completa — 39 Principios Detallados

### v1.0 — 13 originales (Artículos 1-13)
(ya cubiertos en DOC 01)

### v2.0 — 13 adicionales (Artículos 14-26)

```yaml
A14_auto_evolucion: meta_learning + counterfactual
A15_skills_persistentes: respaldo + versionado
A16_raiz_unica_BIS
A17_juez_supervisor_8_reglas:
  - nombre_correcto
  - formato_valido
  - aprobado_MAX
  - sin_reemplazo_originales
  - STATE_JSON_actualizado
  - trazabilidad
  - audit_completo
  - compatible_constitucion
A18_auto_run_primera_ejecucion
A19_cifrado_total: secretos_reposo + comunicacion_cifrada + audit_log
A20_nucleo_solo_api
A21_bootstrap_autonomo
A22_10_modulos_independientes: cada_uno_con [responsabilidad, test, version, fallo_no_tumba]
A23_cero_configuracion: defaults_sensatos
A24_descarga_inteligente: solo_necesario
A25_inicio_autonomo: con_pre_flight
A26_escalabilidad_horizontal: mas_nodos
```

### v3.0 — 13 avanzados (Artículos 27-39)

```yaml
A27_csa_10_jueces_5_fases_veto
A28_sid_5_preguntas_fijas:
  - que_es
  - para_quien
  - que_problema_resuelve
  - como_se_usa
  - que_NO_es
  umbral: definition_score >= 95%
A29_input_engine_v4_54_componentes
A30_semantic_invariant_checker: trigger_si semantic_drift > 0.10
A31_output_engine_ovfs: 13 + 14 + OVFS
A32_micro_separacion_20_modulos: <=200_LOC_cada_uno
A33_closed_feedback_loop: publicar → uso_real → feedback → memoria → reglas
A34_multi_target_delivery: 23_destinos_paralelos
A35_adaptive_delivery: aprende_patrones_MAX
A36_confidence_scoring: umbral_95% por [tarea, agente, modelo]
A37_auto_rollback: si_degrada_sistema
A38_meta_learning: aprende_de_releases_pasados
A39_production_monitoring: post_publicacion_deteccion_regresiones
```

### Reglas Derivadas

```yaml
regla_oro: NUNCA_crear_ni_cambiar_nada_sin_APROBADO_MAX
intocables: [10_Jueces_CSA_5_fases_veto, Auditor_SID_5_preguntas, 39_principios, 14_categorias_BIS, nombres_originales_aprobados]
regla_capas: SOLO_AGREGO_capas_NUNCA_reemplazo
regla_validacion: cada_salida_valida_antes_patchear
```

### Aplicación por Salida

```yaml
cada_output_debe:
  - citar_principios_aplicables
  - verificar_cumplimiento
  - documentar_desviaciones
  - actualizar_STATE_JSON
  - registrar_AUDIT_FINAL
```

---

## DOC 00: Visión General MAXBRY SUPER TEAM

### Niveles de Arquitectura (G1-G6)

```yaml
G1_infraestructura: [HF_Spaces, GitHub, Docker]
G2_core: [BIS, SID, Input_Output_Engine, OOS, OVFS]
G3_ui: [Telegram, API_REST, Dashboard]
G4_audit: [CSA_10_jueces, Auditor_SID]
G5_orquestador: MAXBRY_SUPER_TEAM ⭐  # = ORQUESTADOR + CONSENSO
G6_asistentes: [9_GGUF, 16_API_keys]
```

### Nombres Clave

```yaml
MAXBRY_SUPER_TEAM: orquestador_G5
SKYNER: lider_interno_G5_NVIDIA
M3: arquitecto_que_trabaja_con_MAX
Kimi_K27_Code: implementador
NCT: Neuronas_Code_Turbo_proyecto
CSA: Consejo_Supremo_Auditoria_10_jueces
SID: Sistema_Inteligente_Definicion
BIS: Biblioteca_Inteligente_Skills
OOS: Output_Orchestration_System_v31
OVFS: Output_Virtual_File_System
distincion_critica: M3_chat != SKYNER
```

### Capacidades Objetivo

```yaml
agentes: 2000+_capacidad_no_implementacion
tareas: 1000+_simultaneas
costo: $0_mes
hardware: smartphones_iPad_sin_PC
multi_modelo: intercambiable
auto_recuperacion: si
trazabilidad: 100%
```

### 5 GOALS (cada salida)

```yaml
G1: goal_primary
G2: goal_secondary
G3: goal_success
G4: goal_failure
G5: goal_restriction
```

### 12 PASOS (cada salida)

```yaml
P01: literal_read
P02: think
P03: plan
P04: decompose
P05: hypotheses
P06: swarm
P07: critic
P08: simulate
P09: validate
P10: consensus
P11: report
P12: audit
```

### 5 Pasos Validación Obligatoria

```yaml
V1: buscar_memoria  # ¿ya existe?
V2: validar_propuesta  # ¿correcta?
V3: validar_salida  # ¿cumple_formato?
V4: validar_trazabilidad  # ¿registrable?
V5: STATE_JSON_actualizado
```

### Resiliencia

```yaml
circuit_breaker: por_dependencia
backoff_exponencial: base_2s_max_5min
failover_automatico: si
retry_policy: si
repair_pipeline: 5_pasos
```

### Multi-modelo

```yaml
gguf_local: 9
gguf_api: 4
nvidia_nim: 4
cerebras: 6
groq: 6
perfiles: [conservador, equilibrado, agresivo]
cambio: dinamico_por_tarea
```

### Agentes (resumen numérico)

```yaml
micro_agentes: 30
internal_roles: 11
parallel_queues: 10
niveles_autonomia: 6  # L1-L6
task_models: 12  # TM01-TM12
loop_versions: 5  # ALV_LOP_*
monitores: 3
consejo_consenso: 10_voto
```

### Diagrama horizontal

```
INPUT → [SID:5Q] → [INPUT_ENGINE:54] → [BIS:14cat] → [CSA:10J×5F] → [LOOP:15capas+3ciclos] → [OUTPUT_ENGINE:13] → [OOS:14] → [OVFS] → DELIVERY
```

### Pendiente (datos pre-flight)

```yaml
pendientes:
  - github_username_PAT
  - hf_username_6_tokens
  - 16_api_keys_labels
  - turso_db_credentials
  - visibility_preference
  - telegram_bot_token
  - htm_model_name
  - yuan_model_name
rechazado: output_sandbox
```

---

## DOC 02: Estructura Organizacional — 30 Micro-Agentes, 11 Roles, 10 Colas, 6 Niveles

### 30 Micro-Agentes (6 categorías × 5)

```yaml
categoria_1_analisis: [MA-01, MA-02, MA-03, MA-04, MA-05]
categoria_2_planificacion: [MA-06, MA-07, MA-08, MA-09, MA-10]
categoria_3_ejecucion: [MA-11, MA-12, MA-13, MA-14, MA-15]
categoria_4_validacion: [MA-16, MA-17, MA-18, MA-19, MA-20]
categoria_5_aprendizaje: [MA-21, MA-22, MA-23, MA-24, MA-25]
categoria_6_meta: [MA-26, MA-27, MA-28, MA-29, MA-30]
```

### 30 Micro-Agentes (detallado)

```yaml
MA-01: input_parser  # DSL/DAG/JSON/YAML/MD
MA-02: intent_classifier
MA-03: context_builder
MA-04: entity_extractor
MA-05: semantic_analyzer
MA-06: task_decomposer
MA-07: scheduler
MA-08: resource_allocator
MA-09: priority_manager
MA-10: plan_validator
MA-11: code_generator
MA-12: code_linter  # lint + format
MA-13: code_tester  # tests + coverage
MA-14: worker_pool  # K samples paralelo
MA-15: executor
MA-16: verifier_3_capas  # adversarial + cross + maker
MA-17: critic
MA-18: judge
MA-19: sentinel  # vigila anomalias
MA-20: quality_assurance  # QA final
MA-21: memory_writer
MA-22: pattern_detector
MA-23: optimizer
MA-24: skill_curator  # auto-curacion BIS
MA-25: metrics_collector
MA-26: meta_orchestrator  # orquesta orquestadores
MA-27: recovery_agent
MA-28: self_improver
MA-29: health_monitor
MA-30: lifecycle_manager  # nacimiento/muerte
```

### Características micro-agentes

```yaml
max_loc: 200
responsabilidad: una_sola
input_schema: uno
output_schema: uno
estado: efimero
muerte: tras_emitir_JSON
invocacion: [MCP, stdio]
```

### 11 Internal Roles (R1-R11)

```yaml
R1_CEO_Virtual: SKYNER_NVIDIA
R2_COO: Cerebras
R3_CTO: Cerebras
R4_CFO: Groq
R5_CHRO: GGUF_local
R6_CSO: GGUF_API
R7_CMO: Groq
R8_Chief_Auditor: CSA_J1_J10
R9_Chief_Architect: GGUF_API
R10_Chief_Skeptic: Cerebras
R11_Chief_Historian: Groq
```

### 10 Colas Paralelas (Q1-Q10)

```yaml
Q1_critical_path: blocking_100
Q2_high_priority: fast_500
Q3_normal: standard_1000
Q4_background: async_2000
Q5_research: multi_source_200
Q6_code: compilation_300
Q7_test: quality_400
Q8_documentation: text_150
Q9_review: human_like_100
Q10_recovery: healer_50
scheduling:
  - round_robin_interna
  - priority_boost_Q1
  - preemption: Q1 > Q2 > resto
  - Q4_Q10_pueden_tomar_tiempo_de_Q3
```

### 6 Niveles de Autonomía (L1-L6)

```yaml
L1_manual: cada_paso_aprobacion_humana
L2_supervised: 1_aprobacion_cada_5_acciones
L3_assisted_autonomous: 1_revision_cada_10_acciones
L4_supervised_autonomous: solo_puntos_criticos
L5_continuous_autonomous: autonomo_72h_solo_reporte_final
L6_full_autonomous: self_evolution_enabled
```

### 12 Task Models (TM01-TM12)

```yaml
TM01_simple_task: L1_L2, 3-5_pasos
TM02_code_refactor: L2_L3, 5-10_pasos
TM03_new_feature: L3_L4, 10-15_pasos
TM04_bug_fix: L3_L4, 5-12_pasos
TM05_api_design: L3_L4, 8-12_pasos
TM06_microservice: L4_L5, 12-20_pasos
TM07_full_app: L4_L5, 20-30_pasos
TM08_research_report: L3_L5, 8-15_pasos
TM09_migration: L4_L5, 15-25_pasos
TM10_multi_system: L5_L6, 25-40_pasos
TM11_critical_recovery: L4_L6, 5-15_pasos
TM12_self_improvement: L6, 20-30_pasos
cada_TM_14_pasos:
  - 1-3: pre_analisis [input, seed, gaps]
  - 4-6: research [web, github, rag]
  - 7-9: plan + consensus
  - 10-12: execute + monitor
  - 13: verify_3_capas
  - 14: deliver
```

### 5 Loop Versions (ALV)

```yaml
ALV_LOP_SIMPLE: secuencial_1agente_1iter
ALV_LOP_PARALLEL: dag_2-3agentes_1-2iter
ALV_LOP_FRACTAL: fractal_anidado_depth<=5_3-5iter
ALV_LOP_QUANTUM_FRACTAL_NESTED: quantum_fractal_nested_adaptativo_5-10iter
ALV_LOP_SELF_IMPROVING: modifica_params_10+iter_solo_L6
```

### 3 Monitores

```yaml
PAD_monitor:
  P: performance  # latencia, throughput
  A: accuracy  # calidad
  D: drift  # deriva semantica
anxiety_monitor:
  mide: [retries, fallos, timeouts]
  trigger: ansiedad > umbral
drift_monitor:
  compara: baseline
  trigger: drift > 0.15
```

### Consejo Consenso (10 votantes)

```yaml
voto_1_tecnico: tecnicamente_correcto
voto_2_negocio: aporta_valor
voto_3_costos: costo_efectivo
voto_4_riesgos: riesgos_inaceptables
voto_5_etico: etico
voto_6_ux: buena_ux
voto_7_performance: rapido
voto_8_seguridad: seguro
voto_9_compatibilidad: rompe_algo
voto_10_veto_MAX: MAX_aprobria
mecanismo:
  7+_acuerdo: procede
  5-6_acuerdo: escala_a_MAX
  menos_5: bloquea
  veto_MAX: siempre_bloquea
```

### Estados Tarea (10)

```yaml
estados: [CREADA, EN_COLA, ASIGNADA, EJECUTANDO, PAUSADA, VALIDANDO, COMPLETADA, FALLIDA, CANCELADA, REAPERTURA]
transiciones_validas:
  CREADA → EN_COLA
  EN_COLA → ASIGNADA
  ASIGNADA → EJECUTANDO
  EJECUTANDO ↔ PAUSADA
  EJECUTANDO → VALIDANDO
  VALIDANDO → COMPLETADA
  VALIDANDO → FALLIDA
  EJECUTANDO → CANCELADA
  cualquier → CREADA  # reapertura
```

### Canales de Entrada/Salida

```yaml
entrada: [Telegram, API_REST, Dashboard_Web, CLI_local, Voice_opcional]
salida: 23_destinos_multi_target_delivery + adaptive
```

### Artefactos

```yaml
archivos:
  - state.json
  - events.log
  - memories/*.md  # tier 1-4
  - skills/*.json
  - artifacts/
  - projects/
  - checkpoints/  # snapshots firmados
carpetas_workspace:
  - /workspace/nct-proyecto/  # CON 18 docs + MASTER 20+ docs + parches
  - /workspace/maxbry/  # g1-g6
```

---

## DOC 02b: Estructura Interna (versión complementaria)

### 11 Roles Internos (versión alternativa nombres)

```yaml
R01: director_proyecto
R02: planificador_estrategico
R03: asignador_recursos
R04: monitor_estado
R05: coordinador_agentes
R06: gestor_dependencias
R07: reconciliador_conflictos
R08: optimizador_costos
R09: gestor_memoria
R10: auditor_procesos
R11: gestor_conocimiento
```

### 10 Colas Paralelas (versión alternativa)

```yaml
Q1_critical: emergencias_rollback
Q2_high: tareas_MAX_directo
Q3_user: inputs_usuario
Q4_validation: CSA_quality_checks
Q5_execution: tareas_activas
Q6_monitoring: supervision
Q7_learning: aprendizaje
Q8_maintenance: housekeeping
Q9_background: baja_prioridad
Q10_reserved: picos_carga
```

### 6 Niveles Autonomía (versión alternativa)

```yaml
L1_asistente: solo_sugiere_MAX_decide
L2_consultor: recomienda_con_justificacion
L3_colaborador: ejecuta_simples_solo
L4_autonomo: ejecuta_reporta_MAX_revisa_despues
L5_proactivo: anticipa_necesidades_propoue
L6_autosuficiente: decide_ejecuta_MAX_ve_resultados
default: L3
configurable: por_MAX_y_por_tarea
```

### 12 Task Models (versión alternativa)

```yaml
TM01_analisis: entender_input
TM02_diseno: arquitectura_solucion
TM03_implementacion: codigo
TM04_testing: pruebas
TM05_debug: encontrar_arreglar_bugs
TM06_refactor: mejorar_codigo_existente
TM07_documentacion: escribir_docs
TM08_investigacion: buscar_informacion
TM09_validacion: ejecutar_CSA
TM10_aprendizaje: actualizar_memoria
TM11_despliegue: publicar_rollback
TM12_coordinacion: multiples_tareas
```

### 5 Loop Versions (versión alternativa)

```yaml
ALV_LOP_MIN: 1_ciclo_1_agente_minimo_baja_latencia
ALV_LOP_STD: 3_ciclos_ABC_paralelos_balance
ALV_LOP_ENHANCED: +learning_loop_meta_learning
ALV_LOP_TURBO: maximo_paralelismo_maximo_costo
ALV_LOP_ADAPTIVE: adapta_segun_contexto_auto
```

### 5 Officers Executive Board

```yaml
COO: eficiencia_performance
CFO: costos_presupuesto
CQO: calidad_global_scores
CRO: riesgos_fallos_alertas
CLO: aprendizaje_evolucion
responsabilidades:
  - monitorear_metricas_globales
  - alertar_MAX_si_desvia
  - sugerir_optimizaciones
  - detectar_patrones_sistemicos
  - reportar_estado_semanal
```

---

## DOC 03: Pipeline y Fases del Orquestador

## DOC 1: CONSTITUCIÓN DEL ORQUESTADOR (Detalle Completo — Extracto)

### Constitución v1.0 — 13 Principios Originales

```yaml
P1_Filosofia: Director_de_Empresa_no_IA  # gestiona_delegá_supervisa_NO_improvisa
P2_Objetivos_Escala:
  - 2000+_agentes_CAPACIDAD_no_diseno_de_2000_agentes_reales
  - 1000+_tareas_simultaneas
P3_No_es_IA_Es_Codigo: 90%_codigo_determinista_+_10%_LLM
  porque: predecible_auditable_confiable_bajo_costo_sin_alucinaciones_en_decisiones
  uso_LLM_solo_en:
    - razonamiento_complejo
    - generacion_de_texto
    - interpretacion_de_input
  NUNCA: para_decisiones_de_control
P4_Director_de_Empresa_responsabilidades:
  - planifica
  - asigna_recursos
  - contrata_crea_agentes
  - despide_elimina_agentes
  - supervisa
  - reporta_al_CEO_MAX
  - decide_bajo_incertidumbre
P5_Gestion_Masiva_10_estados:
  1_CREADA: recien_solicitada
  2_EN_COLA: esperando_recursos
  3_ASIGNADA: agente_asignado
  4_EJECUTANDO: en_proceso
  5_PAUSADA: temporalmente_detenida
  6_VALIDANDO: en_revision
  7_COMPLETADA: terminada_con_exito
  8_FALLIDA: error
  9_CANCELADA: detenida_por_MAX
  10_REPLANIFICADA: cambiando_enfoque
P6_Pizarras:
  Pizarra_de_Proyecto:
    - estado_del_proyecto_especifico
    - tareas_del_proyecto
    - agentes_asignados
    - recursos_usados
    - decisiones_tomadas
  Pizarra_Maestra:
    - vista_global_de_todos_los_proyectos
    - recursos_totales_asignados
    - estado_de_cada_proyecto
    - alertas_globales
    - KPIs_agregados
P7_Escalado_Horizontal:
  como: agregar_HF_Spaces_cada_Space_eq_nodo_nodos_comunican_via_bus_sin_single_point_of_failure
  ventajas: costo_controlado_sin_limites_teoricos_resiliencia_mantenimiento_sin_downtime
P8_Colmenas_por_Especialidad:
  - Colmena_de_Codigo
  - Colmena_de_Testing
  - Colmena_de_Investigacion
  - Colmena_de_Auditoria
  - Colmena_de_Output
  - Colmena_de_Investigacion_HF
  - Colmena_de_Aprendizaje
  - Colmena_de_Meta_crear_agentes
P9_Multi_Modelo_Intercambiable:
  disponibles:
    - GGUF_local: [HRM-Text-1B, Qwen2.5-Coder-1.5B, Granite-4.1-3B, LFM2.5-1.2B-Thinking]
    - APIs: [4_NVIDIA_NIM, 6_Cerebras, 6_Groq, GPT-OSS-20B]
  cambio_dinamico_por: [tarea, disponibilidad, costo, calidad_requerida]
P10_Minima_Infraestructura:
  objetivo: $0  # HF_Spaces_free_tier_API_free_tiers_GGUF_local_sin_servers_dedicados
  restricciones_MAX:
    - solo_smartphones_+_iPad
    - sin_PC_para_servidores
    - todo_debe_correr_en_HF
P11_Escalabilidad_10_a_2000:
  como: diseno_stateless_sin_estado_compartido_comunicacion_via_bus_de_eventos_configuracion_dinamica_sin_acoplamiento_fuerte
P12_Organizacion_Absoluta:
  reglas:
    - cada_archivo_en_su_lugar
    - cada_skill_en_su_categoria
    - cada_agente_en_su_colmena
    - cada_evento_en_su_log
    - cada_decision_documentada
    - cada_version_etiquetada
P13_SO_Distribuido_para_IA:
  componentes_tipo_OS:
    - Kernel_Runtime_Kernel
    - Process_Manager_State_Machine
    - File_System_OVFS
    - Scheduler_10_colas
    - IPC_Bus_de_eventos
    - Memory_Manager_Output_Memory
    - I-O_Manager_Multi_Delivery
```

### Constitución v2.0 — 13 Principios Adicionales (Total 26)

```yaml
P14_Auto_Evolucion:
  mecanismos: [Meta_Learning_entre_releases, Self_Improving_Output_Quality, Auto_Curacion_de_skills, Counterfactual_reasoning, Causalidad_no_correlacion]
P15_Skills_Persistentes_requisitos: [persistencia, respaldo_cifrado, versionado, replicacion]
P16_Raiz_Unica_de_Skills: BIS  # evitar_duplicacion_consistencia_auditoria
P17_Juez_Supervisor_Validador_8_reglas:
  R1: cumple_constitucion
  R2: cumple_fase_0.5_confirmacion
  R3: tiene_recursos_asignados
  R4: CSA_aprobado
  R5: Auditor_SID_aprobado
  R6: definition_score_ge_95%
  R7: no_viola_restricciones
  R8: MAX_dio_luz_verde
P18_Auto_Run_primera_ejecucion:
  pasos:
    1_detecta_entorno
    2_descarga_dependencias
    3_configura_secretos
    4_inicializa_estado
    5_arranca_orquestador
    6_reporta_a_MAX
P19_Cifrado_y_Seguridad:
  que_cifrar: [API_keys, tokens_HF_GitHub, memoria_outputs_sensibles, comunicaciones_entre_agentes, respaldos]
P20_Nucleo_solo_via_API: control_acceso_auditoria_versionado_testing_aislado_seguridad
P21_Bootstrap_Autonomo: arranca_solo_desde_cero_sin_intervencion
P22_10_Modulos_Independientes:
  1: Input_Engine
  2: SID_definicion
  3: BIS_skills
  4: Loop_ejecucion
  5: CSA_auditoria
  6: Output_Engine
  7: OOS_orquestacion_output
  8: OVFS_file_system
  9: Memoria
  10: Orquestador_MAXBRY
P23_Cero_Configuracion: sistema_funciona_con_configuracion_por_defecto  # MAX_no_debe_configurar_nada
P24_Descarga_Inteligente: descarga_solo_lo_necesario_cuando_lo_necesita
P25_Inicio_Autonomo:
  lo_que_MAX_da: [GitHub_username_+_PAT, HF_username_+_6_tokens, 16_API_keys_4_NIM_6_Cerebras_6_Groq, Turso_DB, Telegram_bot_token]
P26_Escalabilidad_Horizontal: reafirma_el_principio_7
```

### Constitución v3.0 — 13 Principios Adicionales (Total 39)

```yaml
P27_CSA_10_Jueces_con_5_Fases_+_Veto:
P28_SID_Sistema_Inteligente_de_Definicion:
P29_Input_Engine_11_componentes_+_17_mejoras:
P30_Semantic_Invariant_Checker: verifica_que_significado_NO_cambie_al_pasar_por_sistema
P31_Output_Engine_13_componentes_+_OVFS:
P32_Micro_Separacion_de_Carpetas_20_modulos:
  1_bis
  2_sid
  3_csa
  4_input_engine
  5_input_swarm
  6_input_forensics
  7_input_discovery
  8_knowledge_discovery
  9_definition_engine
  10_input_compiler
  11_quality_swarm
  12_input_governor
  13_digital_twin
  14_loop
  15_output_engine
  16_oos
  17_ovfs
  18_memory
  19_orchestrator
  20_utils
P33_a_P39: mas_principios_definidos_en_PARCHES-ORQUESTADOR/constitucion/v3/
```

### SID — Sistema Inteligente de Definición (Componentes)

```yaml
componentes:
  - Pre_procesador_10_pasos
  - Panel_de_Definicion_Inteligente
  - Clasificador_de_Incertidumbre: critica_alta_media_baja
  - Motor_de_Hipotesis
  - Detector_de_Contradicciones
  - Simulador_Previo
  - Plan_Preliminar_con_nivel_confianza
  - Aprendizaje
  - Preguntas_Adaptativas_arbol_de_decision
  - Auditor_de_Entrada_5_preguntas_fijas

auditor_de_entrada_5_preguntas_fijas_INTOCABLES:
  1: "¿Cual_es_el_objetivo_real?"
  2: "¿Que_restricciones_aplican?"
  3: "¿Que_recursos_estan_disponibles?"
  4: "¿Cual_es_el_criterio_de_exito?"
  5: "¿Que_riesgos_hay?"
```

### Input Engine v4.0 (54 Componentes)

```yaml
originales_45:
  SID: 9_componentes
  Input_Engine_base: 11_componentes
  17_mejoras_adicionales
  3_auditores_de_entrada
  4_capas_adicionales

nuevos_9_capa_34_en_adelante:
  INPUT-100X-A: Input_Swarm_+_Bus_de_Eventos  # 40_a_60_agentes
  INPUT-100X-B: Input_Discovery  # 10_detectores_idioma_dominio_intencion_objetivos_implicitos_restricciones_prioridades_entregables_formato_audiencia_dependencias_externas
  INPUT-100X-C: Input_Forensics  # 10_detectores_contradicciones_ambiguedad_huecos_requisitos_ocultos_riesgos_datos_inventados_inconsistencias_temporales_conflictos_tecnologicos_imposibilidades_scope
  INPUT-100X-D: Knowledge_Discovery  # 15_fuentes_papers_StackOverflow_Reddit_Skills_internos_Base_conocimiento_Memoria_proyecto_Artefactos_APIs_Plugins_Modelos_via_APIs_Documentacion_Repos_publicos_Issues_Wikis_Foros
  INPUT-100X-E: Claude_Definition_Engine_v2.0  # 6_fases_auto_respuesta_multi_interpretacion_simulacion_arbol_decisiones_preguntas_agrupadas_definition_score_ge_95%
  INPUT-100X-F: Input_Compiler_Expandido  # Knowledge_Graph_Goal_Tree_Requirement_Tree_Constraint_Tree_Context_Graph
  INPUT-100X-G: Quality_Swarm  # 10_auditores_con_veto
  INPUT-100X-H: Input_Governor  # 6_estados_RECIBIDO_ANALIZANDO_DEFINIENDO_COMPILANDO_AUDITANDO_APROBADO_o_VETADO_o_REPLANIFICAR_o_PREGUNTAR
  INPUT-100X-I: Input_Digital_Twin  # simulacion_completa_antes_de_ejecutar
```

### OOS v3.1 (14 Componentes)

```yaml
1_contrato_de_salida
2_UOM_Universal_Output_Model
3_Semantic_Chunk_Engine
4_Adaptive_Chunk_Size
5_Predictive_Planner
6_Auto_Format_Negotiation
7_Intelligent_Packaging
8_Multi_Delivery_Pipeline
9_Intelligent_Compression
10_Smart_Version_Control
11_Incremental_Publishing
12_Intelligent_Resume
13_Output_Verification
14_Delivery_Policy_Engine
```

### OVFS — Output Virtual File System

```yaml
estructura:
  /root:
    README_md: descripcion_del_output
    docs/: documentacion
    backend/: codigo_backend
    frontend/: codigo_frontend
    tests/: tests
    diagrams/: diagramas
    prompts/: prompts_usados
    metadata/: metadata_del_output
```

### Output v6.1 Gobernanza (16 Capas)

```yaml
output_governor_8_estados:
  1_APROBAR
  2_CORREGIR
  3_REGENERAR
  4_REPLANIFICAR
  5_DIVIDIR
  6_INVESTIGAR_MAS
  7_PREGUNTAR_USUARIO
  8_CANCELAR

16_capas_A_a_P:
  A: Output_Governor_8_estados
  B: Output_Digital_Twin
  C: Multi_Version_Generator_5_versiones: [calidad, velocidad, minimo_consumo, documentacion, codigo_optimizado]
  D: Output_Fusion_Engine
  E: Acceptance_Test_Engine
  F: Output_Coverage_Map
  G: Explainability_Engine
  H: Output_Provenance
  I: Consistency_Swarm  # 20_microagentes
  J: Artifact_Relationship_Graph
  K: Release_Manager
  L: Output_Memory
  M: Output_Score  # minimo_95%_configurable
  N: Human_Approval_Layer
  O: Adaptive_Delivery
  P: Closed_Feedback_Loop  # LA_MAS_IMPORTANTE_publicacion_a_uso_real_a_feedback_a_memoria_a_actualizacion_de_reglas
```

### LOOP v6.0 (15 Capas + 3 Ciclos Paralelos)

```yaml
15_capas:
  A: Workflow_DAG_no_pipeline
  B: Runtime_Kernel_tipo_OS
  C: Event_Sourcing
  D: State_Machine_por_tarea
  E: Prediction_Engine
  F: Dynamic_Replanning
  G: Model_Router_Inteligente
  H: Trust_Engine_confianza
  I: Goal_Monitor_Permanente
  J: Contract_Engine
  K: Resource_Economy
  L: Semantic_Diff
  M: Universal_Artifact_Graph
  N: Failure_Recovery_Engine
  O: Executive_Board  # 3_a_5_agentes

3_ciclos_paralelos:
  CICLO_A_Ejecucion: CREAR_a_VALIDAR_a_CORREGIR_a_ENTREGAR
  CICLO_B_Supervision: MONITORIZAR_a_MEDIR_a_REPLANIFICAR
  CICLO_C_Aprendizaje: REGISTRAR_a_ANALIZAR_a_OPTIMIZAR_a_ACTUALIZAR_REGLAS
  comunicacion_entre_ciclos: bus_de_eventos
```

### BIS — Biblioteca Inteligente de Skills (14 Categorías + 13 Criterios)

```yaml
14_categorias:
  A: ARQUITECTURA
  B: GESTION
  C: FRONTEND
  D: BACKEND
  E: MOVIL
  F: ESCRITORIO
  G: BASES_DE_DATOS
  H: APIs
  I: DEVOPS
  J: IA
  K: TESTING
  L: SEGURIDAD
  M: AUTOMATIZACION
  N: LENGUAJES

13_criterios_de_skills:
  - relevancia
  - efectividad_comprobada
  - costo_de_aplicacion
  - compatibilidad
  - mantenibilidad
  - documentacion
  - reusabilidad
  - seguridad
  - performance
  - escalabilidad
  - compliance
  - test_coverage
  - comunidad_soporte

3_versiones:
  v1: inicial_basica
  v2: mejorada_con_debate
  v3: avanzada_con_productor_y_consumidor

debate_4_especialistas:
  - Productor_quien_la_creo
  - Consumidor_quien_la_usa
  - Auditor_quien_valida
  - Critico_quien_busca_fallas

BIS-100X_mejoras:
  BIS-100X-F: 5_investigadores_paralelos
  BIS-100X-G: renovacion_cada_15_dias
  BIS-100X-H: detector_de_intencion
  BIS-100X-I: pre_descarga_inteligente
```

### Regla Absoluta de MAX

```yaml
regla_absoluta_de_MAX: NUNCA_crear_ni_cambiar_nada_sin_mi_APROBADO_explicito
regla_de_capas: SOLO_AGREGO_capas_NUNCA_reemplazo
regla_de_nombres: MANTENER_todos_los_nombres_originales
```

