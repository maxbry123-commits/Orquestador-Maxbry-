
### 10 Fases del Pipeline

```yaml
F1_recepcion: input_llega
F2_pre_procesamiento: SID_validaciones_iniciales
F3_definicion: definition_engine_clarificar
F4_planificacion: DAG_recursos_asignacion
F5_confirmacion: fase_0.5_MAX_aprueba_si_nuevo
F6_ejecucion: agentes_activos
F7_validacion: CSA_quality_score
F8_publicacion: output_engine_multi_target
F9_monitoreo: produccion_telemetria
F10_aprendizaje: actualizar_memoria_reglas
```

### Fase 0.5 — Confirmation Gate (CRÍTICA e INTOCABLE)

```yaml
ubicacion: entre_F4_y_F6
proposito:
  - evitar_ejecutar_proyectos_no_autorizados
  - evitar_gastar_recursos_sin_permiso
  - evitar_asumir_cosas_MAX_no_quiso
regla_absoluta:
  proyecto_nuevo: SIEMPRE_confirmacion
  proyecto_recurrente: procede_automatico
flujo: F4 → F5 → {es_conocido? → SÍ:procede, NO:PAUSA_consulta_MAX} → F6
```

### 3 Monitores Pipeline

```yaml
M1_performance: [latencia, throughput, cuellos_botella]
M2_calidad: [scores, errores, complaints]
M3_recursos: [tokens, memoria, rate_limits, costos]
operacion: 24/7_continua
features: [alertas_auto, dashboards, historico]
```

### 4 Escenarios de Ejecución

```yaml
escenario_1_simple: 9_pasos  # tareas_claras_sin_ambiguedad_riesgo_bajo
escenario_2_medio: 16_pasos  # dependencias_ambiguedad_moderada_riesgo_medio
escenario_3_optimo: 25_pasos  # multiples_dependencias_alto_riesgo
escenario_4_avanzado: 30-50_pasos  # proyectos_completos_alta_ambiguedad_critico
```

### Escenario 1 (9 pasos)

```yaml
1: INPUT
2: INTENT_PARSING
3: CONTEXT_BUILDING
4: PLAN_GENERATION
5: EXECUTE
6: SELF_CHECK
7: OUTPUT_GENERATION
8: POST_OUTPUT_AUDIT
9: FEEDBACK_LOOP_STORAGE
```

### Escenario 2 (16 pasos)

```yaml
1-2: [INPUT, INTENT_PARSING]
3-4: [PROBLEM_FRAMING, CONTEXT_BUILDING]
5-7: [CONSTRAINT_EXTRACTION, GOAL_DECOMPOSITION, COMPLEXITY_ESTIMATION]
8-9: [PLAN_GENERATION, SUBTASK_BREAKDOWN]
10-11: [HYPOTHESIS_GENERATION, VALIDATION_LAYER]
12-13: [DECISION_ENGINE, CONFIDENCE_SCORING]
14-16: [OUTPUT_GENERATION, POST_OUTPUT_AUDIT, FEEDBACK_LOOP_STORAGE]
```

### Escenario 3 (25 pasos)

```yaml
1-3: [INPUT, INTENT_PARSING, PROBLEM_FRAMING]
4: DOMAIN_DETECTION
5-6: [CONTEXT_BUILDING, CONSTRAINT_EXTRACTION]
7-9: [GOAL_DECOMPOSITION, COMPLEXITY_ESTIMATION, RISK_SCORING]
10-11: [STRATEGY_SELECTION, ARCHITECTURE_DESIGN]
12-14: [PLAN_GENERATION, SUBTASK_BREAKDOWN, DEPENDENCY_GRAPH_BUILD]
15-16: [HYPOTHESIS_GENERATION, SIMULATION_ENGINE]
17-19: [CONTRADICTION_DETECTION, VALIDATION_LAYER, REPLANNER_LOOP_si_score<70]
20-22: [DECISION_ENGINE, CONFIDENCE_SCORING, FUSION_ENSEMBLE]
23-25: [FINAL_SYNTHESIS, OUTPUT_GENERATION, FEEDBACK_LOOP_STORAGE]
```

### Escenario 4 (30-50 pasos)

```yaml
todos_los_25_de_escenario_3_mas:
  26: ALTERNATIVE_PATH_GENERATION
  27: SEARCH_EXPANSION
  28: REASONING_SWARM_PARALLEL
  29: CRITIC_SWARM_MULTI_PERSPECTIVE
  30: SELF_REFLECTION_LOOP
  31: FAILURE_MODE_ANALYSIS
  32: EDGE_CASE_GENERATION
  33: KNOWLEDGE_RETRIEVAL_EXTERNAL
  34: INSIGHT_EXTRACTION
  35-36: [MEMORY_WRITE_SHORT_TERM, MEMORY_WRITE_LONG_TERM]
  37: OPTIMIZATION_PASS
  38: SOLUTION_RANKING
  39: SAFETY_CONSISTENCY_CHECK
  hasta_50_segun_complejidad
```

### Complexity Estimator

```yaml
formula: score = (dependencias * 2) + pasos_estimados + (5 si ambiguo) + (5 si alto_riesgo)
niveles:
  LOW_0-3: 0_ciclos_reasoner_verifier, ejecucion_directa
  MEDIUM_4-8: 1_ciclo_reasoner_verifier, verificacion_basica
  HIGH_9-15: 2_ciclos, motor_razonamiento_completo
  EXTREME_16+: 3+_ciclos, motor_completo_simulaciones_multiples
```

### 5 Fases Fables

```yaml
F0_orquestacion: [INPUT, descomposicion_25_100_tareas, asignacion_fases, lista_global_inicial]
F1_comprension_t1_t5: [entender_objetivo_real, reformular_problema, contexto_completo, restricciones, recursos_cuellos_botella]
F2_planificacion_t6_t10: [estrategia, arquitectura, sub_tareas_atomicas, grafo_dependencias, roadmap_criterios_exito]
F3_exploracion_investigacion_t11_t16: [multiples_hipotesis, caminos_alternativos, simular_edge_cases, modos_fallo, investigacion_externa]
F4_validacion_t17_t21: [errores_contradicciones, edge_cases_rompen_solucion, validacion_global, correcciones, score_confianza_si<70_regresa_F2]
F5_sintesis_cruda_t22_t25: [consolidar_salidas, integrar_hallazgos, solucion_completa_cruda, preparar_chef_final]
```

### Chef Final (4 pasos)

```yaml
paso_1_lista_total_3_pasadas: SALIDA_CRUDA → 3_pasadas → LISTA_COMPLETA_TODO  # no_resumir_no_perder
paso_2_arrastre_actualizacion_3_pasadas: LISTA_P1 → 3_pasadas → ARRASTRAR_ACTUALIZAR_COMPLETAR_CORREGIR
paso_3_diseno_entrega_3_pasadas: P1+P2 → 3_pasadas → DISENO_FORMATO_FINAL
paso_4_sintesis_final_analisis_total: P1+P2+P3 → ANALISIS_GLOBAL → VERSION_FINAL_OPTIMIZADA
```

### LISTA_GLOBAL — 4 Reglas

```yaml
R1: creada_en_Fase_0_orquestacion
R2: actualizada_final_cada_fase
R3: arrastrada_SIEMPRE_siguiente_paso
R4: NUNCA_reiniciar_hasta_completar_ciclo
contenido: [tareas, estados, resultados, pendientes]
```

### Diagrama horizontal Pipeline

```
INPUT → [F1:recepcion] → [F2:pre_proc] → [F3:def] → [F4:plan] → [F5:conf 0.5] → [F6:ejec] → [F7:valid] → [F8:publi] → [F9:monit] → [F10:apren] → OUTPUT
                                                              ↓
                                                       proyecto_nuevo
                                                              ↓
                                                       MAX_confirma
```

---

## DOC 04: CSA Completo — Consejo Supremo de Auditoría

### Qué es CSA

```yaml
nombre: Consejo_Supremo_Auditoria
autoridad: absoluta
composicion: 10_jueces_90%_codigo_NO_IA
fases_por_juez: 5
veto: absoluto
caracteristicas:
  - auditoria_adversarial
  - trazabilidad_completa
  - veredicto_con_evidencia
diferencia_auditor_generico:
  generico: funciona?
  csa: funciona + optimo + seguro + etico + mantenible
```

### 10 Jueces CSA (detallado)

```yaml
J1_comprension_objetivo:
  pregunta: entendimos_que_quiere_MAX
  evalua: [claridad, alineacion_intencion, completitud_interpretacion]
  output: score_0_100 + issues

J2_cobertura_requisitos:
  pregunta: cubrimos_todo_lo_requerido
  evalua: [requisitos_explicitos, implicitos_identificados, edge_cases]
  output: score_0_100 + issues + gaps

J3_consistencia_logica:
  pregunta: logicamente_coherente
  evalua: [sin_contradicciones, premisas_soportan_conclusiones, sin_circular]
  output: score_0_100 + issues

J4_exactitud_tecnica:
  pregunta: tecnicamente_correcto
  evalua: [codigo_compila, algoritmos_correctos, patrones, sin_bugs_conocidos]
  output: score_0_100 + issues + bugs

J5_arquitectura_diseno:
  pregunta: bien_disenado
  evalua: [patrones, separacion_responsabilidades, SOLID, mantenibilidad]
  output: score_0_100 + issues + mejoras

J6_calidad_codigo:
  pregunta: codigo_de_calidad
  evalua: [legibilidad, naming, comentarios, estilo_consistente, coverage]
  output: score_0_100 + issues + refactorings

J7_investigacion_evidencia:
  pregunta: evidencia_suficiente
  evalua: [fuentes_citadas, datos_verificables, benchmarks_actuales, referencias_reales]
  output: score_0_100 + issues + gaps

J8_optimizacion_rendimiento:
  pregunta: eficiente
  evalua: [latencia, throughput, memoria, escalabilidad, complejidad_algoritmica]
  output: score_0_100 + issues + optimizaciones

J9_seguridad_riesgos:
  pregunta: seguro
  evalua: [vulnerabilidades, OWASP, secretos_expuestos, auth_authz, input_validation]
  output: score_0_100 + issues + riesgos
  veto_absoludo: si  # en temas de seguridad

J10_calidad_final_ux:
  pregunta: entrega_final_buena
  evalua: [documentacion, ejemplos_uso, mensajes_error, UX, accesibilidad]
  output: score_0_100 + issues + sugerencias
```

### 5 Fases por Juez

```yaml
F1_audita_input_completo: [lee_todo_input, identifica_supuestos, mapea_dependencias, lista_NO_esta]
F2_busca_lo_que_nadie_reviso: [edge_cases, corner_cases, combinaciones_raras]
F3_10_soluciones_distintas: [10_alternativas, conserva_mejor, documenta_por_que_descarto_9]
F4_destruye_propia_solucion: [busca_contraejemplos, identifica_debilidades_propia_critica]
F5_ataca_otros_9_jueces: [revisa_veredictos_otros, inconsistencias, puntos_ciegos_colectivos]
total: 10_jueces * 5_fases = 50_auditorias_por_ciclo_CSA
```

### Sistema de Veto

```yaml
veto_simple: cualquier_juez_puede_vetar → bloquea_hasta_resolver
veto_calificado: 2+_jueces_vetando → bloquea_Y_escala_MAX
veto_seguridad: J9_tiene_veto_absoluto
resolucion:
  1. agente_productor_genera_paquete_correccion
  2. CSA_vuelve_a_auditar
  3. si_pasa: procede
  4. si_no: escala_MAX
```

### Cuándo se Ejecuta CSA

```yaml
triggers:
  - antes_de_output_importante
  - antes_de_cada_deploy
  - agente_o_modelo_falla_mas_2_veces
  - drift_mayor_0.10
```

### Algoritmo Run CSA

```python
async def run_csa(artifact, rubric):
    judges = [J1, J2, J3, J4, J5, J6, J7, J8, J9, J10]
    results = await asyncio.gather(*[j.run(artifact, rubric) for j in judges])

    vetoes = [r for r in results if r.veto]
    if vetoes:
        return {"decision": "vetoed", "vetoes": vetoes}

    avg_score = sum(r.score for r in results) / 10
    if avg_score >= 95:
        return {"decision": "approve", "scores": results}
    elif avg_score >= 80:
        return {"decision": "approve_with_notes", "scores": results}
    else:
        return {"decision": "reject", "scores": results}
```

### SID Complementario (5 preguntas fijas)

```yaml
Q1_que_es: definicion_clara_concisa
Q2_para_quien: audiencia_objetivo
Q3_que_problema_resuelve: pain_point_especifico
Q4_como_se_usa: ejemplo_uso_real
Q5_que_NO_es: exclusiones_explicitas
score_agregado: >=95%_requerido
si_menor_95: bloquea_hasta_completar
```

### Integración con MAXBRY

```
INPUT → SID(5_preguntas) → Score>=95% → PRODUCCION → CSA(10J×5F) → Veto?→Escalar_MAX / Aprobado?→Output → Publicacion → Monitoreo_post
```

---

## DOC 07: Output Engine + OOS + OVFS

### Output Engine (13 Componentes)

```yaml
OE_01_output_composer: combina_artefactos_parciales_en_unificado
OE_02_format_selector: elige_formato [MD, JSON, YAML, codigo, binario]
OE_03_template_engine: aplica_templates_pre_aprobados
OE_04_quality_booster: mejora_calidad_final
OE_05_consistency_checker: verifica_consistencia_secciones
OE_06_citation_builder: construye_citas_fuentes
OE_07_metadata_injector: inyecta_metadata_output
OE_08_compression_engine: comprime_sin_perder_info
OE_09_encryption_layer: encripta_secretos_detectados
OE_10_versioning_system: semver_por_output
OE_11_preview_generator: genera_preview_antes_entregar
OE_12_final_validator: ultima_pasada_validacion
OE_13_delivery_orchestrator: coordina_entrega_multi_destino
```

### OOS v3.1 (14 Componentes)

```yaml
OOS_01_multi_target_router: distribuye_output_multi_destino_paralelo
OOS_02_channel_adapter: adapta_output_cada_canal [Telegram, API, etc]
OOS_03_format_converter: convierte_formatos_segun_destino
OOS_04_size_limiter: limita_tamano_segun_canal  # ej Telegram_4096
OOS_05_throttler: controla_velocidad_envio
OOS_06_retry_logic: reintentos_backoff_exponencial
OOS_07_acknowledgment_tracker: rastrea_confirmacion_recepcion
OOS_08_priority_queue: cola_priorizada_urgentes
OOS_09_feedback_collector: recolecta_feedback_post_entrega
OOS_10_output_score: score_calidad_output >=95%
OOS_11_comparison_engine: compara_outputs_similares_deduplicacion
OOS_12_history_writer: escribe_historial_outputs
OOS_13_rollback_trigger: dispara_rollback_si_falla
OOS_14_adaptive_learning: aprende_patrones_preferencia_MAX
```

### OVFS — Estructura

```yaml
/ovfs/:
  projects:
    "{project_id}": [artifacts, deliverables, reports]
  skills:
    "{skill_id}": [outputs, examples]
  users:
    "{user_id}": outputs
  system:
    - logs
    - checkpoints
    - state
  temp: ""
caracteristicas:
  - filesystem_virtual
  - path_jerarquico
  - ops: [read, write, list, delete, move]
  - versioning_automatico
  - metadata_embebida
  - accesible_via_MCP
```

### Output v6.1 — 16 Capas Gobernanza

```yaml
A_pre_output_audit: verifica_CSA_antes_emitir
B_confidence_check: score >= 95%
C_compliance_check: cumple_constitucion_SID_BIS
D_security_scan: sin_secretos_sin_codigo_malicioso
E_consistency_verification: consistencia_entre_secciones
F_provenance_embedding: incrusta_origen_y_chain_of_custody
G_version_locking: versiona_y_lock
H_multi_channel_validation: valida_para_cada_canal_destino
I_rollback_preparation: prepara_rollback_automatico
J_output_score_calculation: calcula_score_final
K_adaptive_format_selection: selecciona_formato_segun_historial
L_delivery_path_selection: elige_ruta_optima_entrega
M_recipient_verification: verifica_destinatario
N_delivery_confirmation: confirma_recepcion
O_post_delivery_monitoring: monitorea_post_entrega
P_feedback_loop_trigger: dispara_feedback_loop
```

### 8 Estados Output Governor

```
DRAFT → VALIDATING → APPROVED → DELIVERING → DELIVERED → MONITORED → ACCEPTED/REJECTED → (Rollback si rejected)
```

### 23 Destinos Multi-Target Delivery

```yaml
01: telegram_texto
02: telegram_archivo
03: api_rest_json
04: api_rest_archivo
05: github_commit
06: github_pr
07: github_issue
08: hf_space_deploy
09: hf_dataset_upload
10: email_texto
11: email_html
12: webhook
13: dashboard_live
14: dashboard_snapshot
15: discord
16: slack
17: local_file
18: s3_compatible_storage
19: cloudflare_r2
20: notion
21: google_drive
22: drive_node_interno
23: custom_mcp_target
seleccion: adaptativa_aprende_preferencia_MAX
```

### 9 Propuestas M3 Aplicadas (Output)

```yaml
1_pre_mortem: simula_que_podria_fallar_reduce_70%
2_auto_rollback: rollback_automatico_al_ultimo_bueno
3_meta_learning: aprende_outputs_aceptados_rechazados
4_personalization: adapta_formato_preferencia_MAX
5_multi_stakeholder: genera_versiones_audiencias_diferentes
6_causal_tracing: cadena_causal_completa
7_marketplace: outputs_como_skills_compartibles
8_self_improving: cada_output_mejora_siguiente_similar
9_production_monitoring: monitorea_outputs_produccion
rechazada: output_sandbox  # NO se implementa
```

---

## DOC 08: LOOP v6.0 — 15 Capas + 3 Ciclos Paralelos

### 15 Capas

```yaml
capa_1_input_loop: itera_hasta_definition_score_>=95%
capa_2_plan_loop: itera_hasta_consenso_consejo
capa_3_execute_loop: itera_hasta_completion
capa_4_validate_loop: itera_hasta_score_>=95%
capa_5_repair_loop: 5_pasos_para_reparar_fallos
capa_6_learn_loop: extrae_lecciones_actualiza_memoria
capa_7_adapt_loop: adapta_parametros_segun_resultados
capa_8_checkpoint_loop: snapshots_firmados_cada_N_iteraciones
capa_9_consensus_loop: ronda_votaciones_consejo
capa_10_monitor_loop: 3_monitores [PAD, Anxiety, Drift]
capa_11_cost_loop: monitorea_costo_ajusta_perfil_api
capa_12_escalate_loop: escala_MAX_si_necesario
capa_13_rollback_loop: rollback_si_degradacion
capa_14_deliver_loop: itera_hasta_confirmacion
capa_15_feedback_loop: recolecta_feedback_post_entrega
```

### 3 Ciclos Paralelos

```yaml
LOOP_A_ejecucion: [Input, Plan, Execute, Validate, Deliver]
  proposito: ciclo_produccion
  prioridad: alta
  bloqueante: si  # para_otros

LOOP_B_supervision: [Monitor, Detect, Alert, Decide, Act]
  proposito: vigila_LOOP_A
  prioridad: media
  bloqueante: no  # watchdog

LOOP_C_aprendizaje: [Observe, Analyze, Extract, Store, Update]
  proposito: aprende_de_A_y_B
  prioridad: baja
  bloqueante: no  # completamente_async
```

### Diagrama Horizontal

```
                    LOOP_A_EJECUCION
                    Input→Plan→Exec→Val→Deliver
                              ↓
                    LOOP_B_SUPERVISION
                    Monitor→Detect→Alert
                              ↓
                    LOOP_C_APRENDIZAJE
                    Observe→Analyze→Store
```

### Coordinación entre Ciclos

```yaml
A_a_B: cada_5_segundos  # LOOP_A_reporta_a_B
B_a_A: cuando_alerta  # LOOP_B_puede_pausar_A
A_a_C: al_completar  # LOOP_A_entrega_datos_C
C_a_A: al_aprender  # LOOP_C_actualiza_skills_reglas
```

### Patrones de Iteración

```yaml
secuencial: A1 → B1 → C1 → A2 → B2 → C2
dag_paralelo: S → {A1, A2, A3} → E  # paralelo
fractal: A1 = {A1.1, A1.2, A1.3}  # cada_uno_es_A_en_miniatura
```

### Checkpoints y Rebuild

```yaml
checkpoint:
  cuando: cada_N_iteraciones_default_10
  contenido: snapshot_state_completo
  firma: hash
  ubicacion: /checkpoints/
rebuild:
  api: state.restore(checkpoint_id=...)
rollback_auto: si_loop_detecta_degradacion → ultimo_checkpoint_bueno + restaura + reporta
```

### Pipeline de Reparación (5 Pasos)

```yaml
paso_1_detect: identifica_tipo_fallo
paso_2_diagnose: diagnostica_causa_raiz
paso_3_patch: aplica_parche_correctivo
paso_4_verify: verifica_que_parche_funciona
paso_5_document: documenta_incidente_y_solucion
```

### 10 Propuestas M3 Aplicadas (Input/Loop)

```yaml
1_definition_score_gate: bloquea_si_score<95%
2_auto_repair_pipeline: 5_pasos_automatico
3_3_cycle_parallel: A+B+C_paralelo
4_checkpoint_restore: snapshots_firmados
5_max_mode_sampling: K_samples_voto_decisiones_criticas
6_goal_stop: criterio_explicito_parada_antes_deliver
7_dynamic_workflow: workflow_adapta_mid_execution
8_multi_source_research: 5_fuentes_investigacion
9_deterministic_90_10: 90%_codigo_10%_LLM
10_pre_analysis_seed: pipeline_5_pasos_antes_empezar
```

### Métricas del Loop

```yaml
metricas:
  - latencia_media_iteracion
  - iteraciones_promedio_por_tarea
  - tasa_exito_por_capa
  - fallos_por_capa
  - tiempo_total_loop
  - checkpoints_generados
  - rollbacks_ejecutados
```

---

## DOC 10: Input Engine + Output Engine + Loop (consolidado)

### Input Engine v4.0 — INPUT-100X-A (Input Swarm + Bus de Eventos)

```yaml
agentes_paralelos: 40-60
bus: eventos_compartido
distribucion: carga_dinamica
comunicacion: asincrona_entre_agentes
```

### INPUT-100X-B · Input Discovery (10 Detectores)

```yaml
D1_idioma: detecta_lengua
D2_dominio: [tecnologia, negocio, ciencia, legal, educacion]
D3_intencion: [crear, consultar, modificar, eliminar, aprender]
D4_objetivos: detecta_implicitos_no_escritos
D5_restricciones: [duras, blandas, regulatorias]
D6_prioridades: [urgencia, importancia, complejidad]
D7_entregables: [formato, tipo, cantidad]
D8_formato: [markdown, json, yaml, codigo, prosa]
D9_audiencia: [tecnico, ejecutivo, mixto, publico]
D10_dependencias: [externas, internas, hardware, software, datos]
```

### INPUT-100X-C · Input Forensics (10 Detectores)

```yaml
F1_contradicciones: afirmaciones_se_contradicen
F2_ambiguedad: terminos_vagos_doble_sentido
F3_huecos: info_faltante_critica
F4_requisitos_ocultos: usuario_no_dijo_pero_necesita
F5_riesgos: potenciales_problemas_proyecto
F6_datos_inventados: info_que_no_existe_en_fuentes
F7_inconsistencias_temp: fechas_lineas_tiempo_imposibles
F8_conflictos_tec: tecnologias_no_se_llevan
F9_imposibilidades: cosas_fisica_logicamente_imposibles
F10_scope: alcance_mal_definido_amplio
```

### INPUT-100X-D · Knowledge Discovery (15 Fuentes)

```yaml
basicas_6:
  F1: papers_academicos  # arxiv, paperswithcode
  F2: stackoverflow  # preguntas_tecnicas
  F3: reddit  # discusion_real_usuarios
  F4: skills_internos  # BIS
  F5: base_conocimiento_proyecto
  F6: memoria_proyecto
extendidas_9:
  F7: artefactos_previos_similares
  F8: apis_documentadas
  F9: plugins_herramientas
  F10: modelos_via_apis
  F11: documentacion_oficial
  F12: repos_publicos
  F13: issues_discussions
  F14: wikis_tutoriales
  F15: foros_especializados
```

### INPUT-100X-E · Claude Definition Engine v2.0 (6 Fases)

```yaml
F1_auto_respuesta: intenta_responder_el_mismo_mejor_suposicion
F2_multi_interpretacion: 3-5_interpretaciones_distintas
F3_simulacion: simula_cada_interpretacion_mide_coherencia
F4_arbol_decisiones: construye_arbol_con_todas_rutas
F5_preguntas_agrupadas: agrupa_por_stakeholder_prioriza
F6_definition_score: 0-100%, umbral >=95%_configurable
```

### INPUT-100X-F · Input Compiler Expandido (5 Grafos)

```yaml
G1_knowledge_graph: conceptos_relaciones_dominio
G2_goal_tree: primario + secundarios + sub_objetivos
G3_requirement_tree: funcionales + no_funcionales + derivados
G4_constraint_tree: duras + blandas + regulatorias
G5_context_graph: stakeholders + entorno + dependencias_externas
```

### INPUT-100X-G · Quality Swarm (10 auditores con veto)

```yaml
cualquier_auditor_puede_vetar:
  - bloquea_ejecucion
  - devuelve_paquete_con:
    - error_detectado
    - causa_raiz
    - impacto
    - como_corregir
    - que_investigar
    - que_agentes_crear
    - que_tareas_faltan
    - prioridad
    - pruebas_necesarias
    - condiciones_para_aprobar
```

### INPUT-100X-H · Input Governor (6 estados)

```yaml
S1_RECIBIDO: input_acaba_de_llegar
S2_ANALIZANDO: swarm_discovery_forensics_trabajando
S3_DEFINIENDO: definition_engine_buscando_claridad
S4_COMPILANDO: compiler_construyendo_grafos
S5_AUDITANDO: quality_swarm_validando
S6: [APROBADO, VETADO, REPLANIFICAR, PREGUNTAR]
```

### INPUT-100X-I · Input Digital Twin

```yaml
proposito: simulacion_completa_ANTES_ejecutar
detecta: problemas_antes_de_consumir_recursos
ejecuta: solo_si_definition_score >= 95%
```

### Semantic Invariant Checker

```yaml
proposito: verifica_significado_NO_cambie
verifica:
  - input_semantico = output_semantico  # cuando_se_requiere
  - decisiones_no_se_contradicen
  - restricciones_se_mantienen
  - conceptos_clave_no_se_pierden
  - relaciones_se_preservan
```

### 20 Módulos Micro-Separación

```yaml
01_bis: biblioteca_skills
02_sid: definicion_inteligente
03_csa: consejo_auditoria
04_input_engine: motor_entrada
05_input_swarm: swarm_input
06_input_forensics: detectores_forenses
07_input_discovery: detectores_discovery
08_knowledge_discovery: knowledge
09_definition_engine: claude_definition
10_input_compiler: compilador
11_quality_swarm: auditores
12_input_governor: maquina_estados
13_digital_twin: simulacion
14_loop: motor_ejecucion
15_output_engine: motor_salida
16_oos: orquestacion_output
17_ovfs: file_system_virtual
18_memory: memoria_persistente
19_orchestrator: MAXBRY
20_utils: utilidades_comunes
```

### 10 Propuestas Loop v200 (PROP-13 a PROP-20)

```yaml
PROP_13_micro_agents_catalog: 12_micro_agentes_especializados
PROP_14_chain_patterns: [secuencial, DAG, fractal]
PROP_15_seed_pre_analysis: 5_pasos_pre_analisis
PROP_16_research_cycle: 2-5_rondas_stop_por_evidencia
PROP_17_hf_spaces_fleet: 10-20_workers_remotos_MCP
PROP_18_dsl_90_10_budget: 90%_codigo_10%_LLM
PROP_19_mimo_integration:借鉴_MiMo [Max_Mode, Goal_Stop, Writer, Dream]
PROP_20_oss_backends_router: router_15_backends_OSS
```

### Flujo Global

```
USR → [Input_Engine_v4.0:54] → [SID] → [BIS_skills] → [CSA_10J×5F] → [Loop_v6.0:15capas+3ciclos] → [Output_Engine_v6.1:13+16capas] → [OOS_v3.1:14] → [Multi_Target:23_destinos] → [Closed_Feedback_Loop] → mejora_continua
```

### Estado de Capas Aplicadas

```yaml
9_patches_OUTPUT_v61: A-P_gobernanza
9_patches_INPUT_V40: A-I
15_patches_LOOP_V60: A-O
9_propuestas_OUTPUT: M3
10_propuestas_INPUT_LOOP: M3
total: 52_capas + 19_propuestas
```

### Closed Feedback Loop (LA MÁS IMPORTANTE)

```yaml
flujo:
  1: output_publicado
  2: uso_real  # ¿se_usa? ¿funciona? ¿satisface?
  3: feedback  # [directo: rating_comentarios, indirecto: errores_performance, observado: como_lo_usan]
  4: memoria  # [output_memory, patterns_identificados]
  5: aprendizaje  # [meta_learning, self_improving]
  6: reglas_actualizadas  # [knowledge_base, CSA_jueces, BIS_skills]
  7: proximo_output_mejor
por_que_importante:
  sin_esta: sistema_estatico
  con_esta: [mejora_continua_automatica, memoria_organizacional, adaptacion_mundo_real]
```

### 23 Destinos Multi-Target Delivery (versión alternativa)

```yaml
archivos_documentos_5: [MD, PDF, HTML, DOCX, TXT]
codigo_5: [ZIP, GitHub, GitLab, Bitbucket, tarball]
datos_3: [JSON, YAML, XML]
comunicacion_3: [Email, Slack/Discord, Telegram]
almacenamiento_3: [Drive_Mavis, S3_compatible, HF_Dataset]
apis_2: [REST_API, Webhook]
otros_2: [MCP_server, Streaming_output]
```

---

## DOC 10: Modelos y APIs

### 9 Modelos GGUF (confirmados HuggingFace)

```yaml
01_HRM_Text_1B_Sapient: 1B_params, 0.6GB, razonamiento_jerarquico
02_Qwen2_5_Coder_1_5B: 1.5B_params, 1GB, generacion_codigo
03_Granite_4_1_3B_IBM: 3B_params, 2GB, asistente_general
04_Granite_3_2_2B_IBM: 2B_params, 1.5GB, asistente_compacto
05_LFM2_5_1_2B_Thinking: 1.2B_params, 0.8GB, razonamiento
06_Gemma_4_E4B_Google: 4B_params, 2.5GB, asistente_eficiente
07_Gemma_4_E2B_Google: 2B_params, 1.5GB, asistente_compacto
08_GPT_OSS_20B_OpenAI: 21B_total_3.6B_active_MoE, 13GB, modelo_fuerte
09_Nemotron_3_Nano_4B_NVIDIA: 4B_params, 2.5GB, asistente_NVIDIA
total_local: ~25.6GB
```

### 16 API Keys

```yaml
NVIDIA_NIM_4:
  NIM_01_SKYNER: tareas_principales_lider_G5
  NIM_02_razonamiento: complejo
  NIM_03_codigo: generacion_codigo
  NIM_04_backup: respaldo

Cerebras_6:
  CER_01_COO: operaciones
  CER_02_CTO: tecnico
  CER_03_razonamiento: analisis
  CER_04_codigo: code_gen
  CER_05_backup_1: respaldo
  CER_06_backup_2: respaldo

Groq_6:
  GROQ_01_CFO: costos
  GROQ_02_CMO: comunicacion
  GROQ_03_Historian: memoria
  GROQ_04_razonamiento: analisis_rapido
  GROQ_05_backup_1: respaldo
  GROQ_06_backup_2: respaldo
```

### 3 Perfiles de Uso

```yaml
conservador:
  primary: groq
  secondary: nim
  fallback: cerebras
  rules: [never_GPT-OSS-20B, max_3_retries, timeout_60s]
  budget: max_100_000_tokens_per_task
  use_cases: [simples, bajo_costo, bajo_riesgo]

equilibrado_RECOMENDADO:
  primary: nim
  secondary: cerebras
  fallback: groq
  rules: [GPT-OSS-20B_solo_hard_tasks, max_5_retries, timeout_120s]
  budget: max_500_000_tokens_per_task
  use_cases: [mayoria_tareas, balance_costo_calidad]

agresivo:
  primary: cerebras
  secondary: nim
  fallback: groq
  rules: [always_GPT-OSS-20B_first, max_10_retries, timeout_300s]
  budget: max_2_000_000_tokens_per_task
  use_cases: [criticas, maxima_calidad, costo_no_importa]
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

### Reglas de Routing

```yaml
simple: GGUF_local
media: Groq
compleja: Cerebras_o_NIM
critica: GPT-OSS-20B_via_NIM
```

### Datasets y Adapters (60 cada uno)

```yaml
datasets_60: [30_codigo, 15_texto, 10_especializados, 5_testing]
adapters_60: [30_LoRA, 15_QLoRA, 10_prefix_tuning, 5_prompt_tuning]
descarga: PARCHE-v15
```

### Hardware Disponible

```yaml
HF_Spaces: 7_x_16GB = 112GB_RAM
uso_actual: ~13.5GB
margen_libre: 87%
throughput_estimado:
  conservador: 2000_tareas_dia
  equilibrado: 1000_tareas_dia  # RECOMENDADO
  agresivo: 100_tareas_dia
costo_objetivo: $0_mes_free_tiers
```

---

## DOC 09: Reglas, Costos y Capacidades

### Objetivo Infraestructura $0

```yaml
HF_Free_Tier: 7_Spaces_16GB_RAM_CPU_basico
API_Free_Tiers: [4_NVIDIA_NIM, 6_Cerebras, 6_Groq]
GGUF_Local: 9_modelos_cuantizados_0.6_3GB_cada_uno
total: $0_mes
limites_respetar:
  - HF_Spaces_pueden_dormirse_inactividad
  - rate_limits_APIs
  - memoria_limitada_16GB_por_space
  - cold_starts
  - HH != A100  # solo_CPU_o_T4
```

### Capacidades del Sistema

```yaml
objetivos:
  agentes: 2000+_capacidad
  tareas: 1000+_simultaneas
  HF_Spaces: 7_x_16GB = 112GB
  uso_modelos: ~13.5GB
  margen_libre: 87%
calculo:
  lineas_totales: ~53,400
  archivos_python: 336
  codigo_fuente: ~14MB
  RAM_runtime_sin_modelos: ~500MB
  RAM_con_modelos_G6: ~13.5GB
escalabilidad: [horizontal_agregar_HF_Spaces, vertical_upgrade_Spaces_larger, sin_redesign]
```

### Restricciones MAX (Confirmadas)

```yaml
hardware: [smartphones, iPad_Pro, sin_PC_servidores, sin_GPU_dedicada, todo_en_HF]
reglas_operacionales:
  - NUNCA_crear_ni_cambiar_sin_APROBADO
  - SOLO_AGREGO_capas_NUNCA_reemplazo
  - MANTENER_todos_nombres_originales
  - estructura_<200_lineas_por_archivo_M2.7_puede_editar
```

### Reglas del Sistema (Confirmadas en Chat)

```yaml
reglas_operacion:
  - 5_GOALS_12_PASOS_obligatorios_cada_salida
  - inicio: APLICANDO_SYSTEM_PROMPT
  - fin: AUDIT_FINAL_PASO_12
  - 3_inventarios_separados: tools != agents != ai_models
  - orquestador_INDEPENDIENTE_no_mezclar_con_GGUF_API_proyectos
  - NO_inventar_datos_preguntar_si_falta
  - NO_alucinar
  - MVP_first_anti_overengineering
  - no_inventar_nuevas_categorias
  - cada_salida_validar_antes_patchear
  - mostrar_PENDIENTE_si_no_aprobado
  - STATE_JSON_actualizado
reglas_aprobacion:
  - NUNCA_sin_APROBADO_explicito
  - SOLO_AGREGO_capas_NUNCA_reemplazo
  - MANTENER_nombres_roles_cantidades_originales
reglas_tecnicas:
  - input_is_sacred  # Input_Block_nunca_modifica_resume_parafrese_reinterpreta
  - DSL_DAG_nunca_prompt_libre
  - G5_gestiona_agentes_no_al_reves
  - orquestador_confirma_proyecto_antes_ejecutar_Fase_0.5
  - APIs_intercambiables_3_profiles
  - estructura_<200_lineas_por_archivo
  - cada_HF_Space_per_group_aislado_own_token
  - cada_proyecto_separate_root_GitHub
  - cada_Docker_container_por_proyecto
```

### Prompt DSL Cerrado (Determinismo)

```yaml
proposito: [misma_calidad_razonamiento, mismo_formato_parseable, auditoria_facil]
estructura:
  sistema: |
    Eres el {AGENT_ROLE} en el sistema de consenso de NEURONA CODE TURBO.
    Tu misión: {MISSION_TEXT}
    Tu personalidad: {PERSONALITY_TEXT}
    Tus restricciones: {RESTRICTIONS}
    Responde SOLO en el formato JSON especificado. No agregues prosa.
  contexto: [proyecto, stack, presupuesto, tiempo, restricciones_adicionales]
  problema: USER_PROBLEM
  input_previo: PREVIOUS_AGENT_OUTPUT
  formato_salida: OUTPUT_SCHEMA_JSON
  importante:
    - no_inventar_features_fuera_del_stack
    - ser_conciso
    - si_dudas: no_tengo_suficiente_informacion
```

### Determinismo 90/10

```yaml
90_codigo_determinista:
  - parseo
  - validacion
  - transformacion
  - routing
  - verificacion_mecanica
  - formatting
  - retry
  - fallback
  - circuit_breaker
  - eros_compression
  - checkpoint_restore
  - schema_validation
10_LLM_aporta_senal:
  - MA-RAG-SYNTH  # sintesis
  - MA-ARCH-PLAN  # parte_creativa
  - Max_Mode  # decisiones_criticas
  - llm_adversarial_review  # cuando_3_capas_mecanicas_fallan
contador_presupuesto: |
  class Budget:
    code_tokens: int = 0
    llm_tokens:  int = 0
    @property llm_pct: llm_tokens / total
    enforce(target_pct=0.10): assert llm_pct <= target_pct
```

### Ciclo Investigación (R1-R5)

```yaml
R1_query: 
R2_fetch:
R3_filter:
R4_eval: si_score>=0.85_stop
R5_refine: replan_si_no_pasa
politica:
  rondas_min: 2
  rondas_max: 5  # anti_bucle
  tokens_por_ronda: <=50K
  salida: MA-RAG-SYNTH
```

### Semilla Pre-Análisis (5 pasos)

```yaml
S1_indexar: MA-INDEX → seed_index.sqlite
S2_resumir: MA-SUMMARIZE → seed_summary.json
S3_detectar_gaps: MA-GAP-DETECT → seed_gaps.json
S4_proponer_preguntas: MA-QUESTION-GEN → seed_questions.json
S5_enriquecer_seed: MA-RESEARCH-WEB + MA-RESEARCH-GH → seed_enriched.json
metrica_suficiencia: |
  evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
  )
umbral_proceder: score >= 0.85
```

### 3 Patrones de Encadenamiento

```yaml
secuencial: A → B → C → D  # chain_linear, ETL_refactor
dag_paralelo: [A → B, A → C] → D  # chain_dag_con_parallel_groups, investigacion+diseno
fractal_anidado: {A → B, C} → D  # chain_fractal_depth<=5, arquitectura_multi_modulo
```

### Estado del Proyecto

```yaml
done:
  - 100_patches_documentacion_individual
  - 19_archivos_python_reales_726_lineas
  - constitucion_1276_lineas
  - memoria_persistente_2_topics
  - 8_documentos_consolidados_72KB
in_progress:
  - 9_documentos_consolidados_mas
  - verificacion_cruzada_final
blocked:
  - MAX_confirma_arquitectura_final
  - M2.7_no_ha_instalado_nada_espera_GO_MAX
  - datos_pre_flight_pendientes:
    - github_username_PAT
    - hf_username_6_tokens
    - 16_api_keys_labels
    - turso_db_credentials
    - visibility_preference
    - telegram_bot_token
    - HTM_model_name_no_encontrado_HF
    - YUAN_model_name_no_encontrado_HF
```

### Código Real Creado

```yaml
ubicacion: /workspace/maxbry/g7/output_engine/v2/
archivos: 19
total_lineas: 726
estructura:
  g7/output_engine/v2/:
    __init__.py  # 47_lineas
    pre_mortem/pre_mortem_analyzer.py  # 70_lineas
    auto_rollback/rollback_monitor.py  # 62_lineas
    meta_learning/cross_release_analyzer.py  # 56_lineas
    personalization/style_learner.py  # 64_lineas
    multi_stakeholder/stakeholder_detector.py  # 79_lineas
    causal_tracing/causal_chain_builder.py  # 75_lineas
    marketplace/output_cataloger.py  # 84_lineas
    self_improving/quality_analyzer.py  # 99_lineas
    production_monitoring/usage_tracker.py  # 88_lineas
    + 10 __init__.py
rechazado: output_sandbox  # NO_se_creo
```

---

## DOC 04: Sistemas de Razonamiento

### EURS — External Universal Reasoning System

```yaml
modos: [standard, turbo]
```

### Modo Standard (5 capas + 12 pasos)

```yaml
5_capas:
  C1: analisis_problema
  C2: generacion_hipotesis
  C3: evaluacion_hipotesis
  C4: sintesis_solucion
  C5: verificacion_final
12_pasos:
  P01: parsear_input
  P02: identificar_conceptos_clave
  P03: establecer_relaciones
  P04: generar_3_hipotesis
  P05: buscar_evidencia
  P06: evaluar_cada_hipotesis
  P07: combinar_resultados
  P08: construir_solucion
  P09: validar_coherencia
  P10: verificar_completitud
  P11: formatear_output
  P12: reportar
uso: [tareas_simples_medianas, recursos_limitados, respuesta_rapida]
```

### Modo Turbo (12 capas + 45 pasos)

```yaml
12_capas:
  C01: parsing_profundo
  C02: descomposicion
  C03: contextualizacion
  C04: generacion_exhaustiva_hipotesis
  C05: busqueda_multi_fuente
  C06: evaluacion_rigurosa
  C07: sintesis_avanzada
  C08: diseno_solucion
  C09: implementacion
  C10: validacion_multiple
  C11: refinamiento
  C12: certificacion
45_pasos: distribuidos_3-4_por_capa
uso: [tareas_criticas, decisiones_arquitectonicas, problemas_complejos, MAX_pide_maxima_calidad]
comparacion:
  standard: 5_capas_12_pasos_rapido_80%
  turbo: 12_capas_45_pasos_lento_99%
```

### Micro-Ciclo por Paso (7 pasos internos)

```
objetivo → plan → subplan → ejecución → verificación → corrección → resultado
```

### Arquitectura de Control Alto

```
MYTHOS → FSM → ROUTER → SHERIFF → SENTINEL → VERIFIER → CRITIC → JUDGE → POLICY_ENGINE → PYDANTICAI → RETRY_ENGINE → LLM
```

### Stack Técnico

```yaml
JSON: define_reglas
Python: ejecuta_logica
DSL: define_workflows
YAML: configuracion
cadena: MYTHOS → PYTHON → FSM → ROUTER → LLM
```

### PydanticAI

```yaml
proposito: convierte_output_LLM_en_estructuras_datos_python_validadas_tipadas
garantia: output_LLM_sea_procesable_por_codigo_determinista
cadena: LLM → JSON_valido → Schema_valido → Python_valido
```

### FSM Finite State Machine

```
PLAN → CODE → TEST → CRITIC → REPLAN → FIN
no_permite: saltar_estados_arbitrariamente
```

### Separación de Capas (5 niveles)

```yaml
1_PENSAMIENTO: como_se_analiza_resuelve  # MYTHOS
2_CONTROL: que_ejecutar_cuando_validar  # FSM/Router
3_EJECUCION: como_se_ejecuta_codigo  # Coder/Sandbox
4_PERSISTENCIA: como_se_guarda_estado  # DB/JSON
5_AUTOCORRECCION: como_se_repara_fallo  # Repairer
regla: cada_capa_responsabilidad_unica_no_se_mezclan
```

### DRE Pipeline (9 pasos)

```
INPUT → COMPLEXITY_ESTIMATOR → PLANNER → REASONER → SELF_CHECK → REASONER → SELF_CHECK → SYNTHESIS → OUTPUT
```

### OpenMythos (PRELUDE → LOOP → CODA)

```yaml
PRELUDE: bloques_transformer_estandar, pre_procesa_input_antes_loop_recurrente, equivalente_fases_0_1_comprension
RECURRENT_BLOCK: en_loop_hasta max_loop_iters, nucleo_razonamiento_recurrente, cada_iteracion = chain_of_thought_latente, mas_bucles = cadenas_mas_profundas, equivalente_fases_2_4_planificacion_exploracion_validacion
CODA: refinamiento_final_salida, razonamiento_latente_a_output, equivalente_fase_5_chef_final
concepto_clave: |
  inference-time_scaling: mas_computo_a_problemas_mas_dificiles_ajustando_iteraciones
```

### Optimizar Para (8 criterios)

```yaml
si:
  1_calidad
  2_robustez
  3_recuperacion
  4_persistencia
  5_escalabilidad
  6_auditoria
  7_control
  8_evolucion_futura
no_para: [velocidad, simplicidad]
```

### Core Plantilla Fija + Adaptadores

```yaml
MYTHOS_CORE_plantilla_fija_nunca_cambia:
  - 40_pasos_base
  - 5_fases
  - LISTA_GLOBAL
  - CHEF_FINAL_4_pasos
  - DRE_estimador_complejidad
ADAPTADOR_cambia_segun_caso:
  - que_pasos_activar_segun_escenario
  - cuantas_iteraciones_recurrent_loop
  - que_herramientas_externas
  - que_formato_salida
casos_uso:
  - codigo: Adaptador_Code
  - investigacion: Adaptador_Research
  - analisis: Adaptador_Analysis
  - diseno: Adaptador_Design
ejecucion: FABLES_CORE + Adaptador_[tipo]
```

### Distinción Razonamiento vs Control

```yaml
pensamiento_MYTHOS_FABLES: define_como_analiza_resuelve, genera_estrategias_soluciones
control_FSM_Router_PydanticAI: decide_que_ejecutar_cuando_validar_reintentar, garantiza_proceso_correcto
sistema_avanzado: ambos, son_capas_diferentes_trabajan_juntas_no_se_mezclan_no_se_reemplazan
```

### Análisis (Restricciones/Recursos/Cuellos/Riesgos/Supuestos Falsos)

```yaml
restricciones: [que_no_puede_cambiar, limites_inamovibles, dependencias_externas]
recursos: [que_tiene_disponible, tokens_por_ciclo, memoria_usable, herramientas_externas]
cuellos_botella: [donde_se_atraca, pasos_mas_lentos, mas_tokens, donde_puede_romperse]
riesgos: [falla_silenciosa, mayor_impacto, dificil_recuperar]
supuestos_falsos: [asumimos_puede_no_ser_cierto, funciona_teoria_no_produccion, asumimos_LLM_no_siempre_cumple]
```

### Workflow de Cada Paso (Código Real)

```
planner() → tester() → critic()  # funciones_python_reales
```

### 7 Validadores

```yaml
validadores:
  - Verifier
  - Critic
  - Judge
  - Sentinel
  - Sheriff
  - Policy_Engine
  - PydanticAI
pregunta_pendiente: orden_optimo_de_estos_validadores
```

---

## DOC 11: Razonamiento + Mythos

### EURS Standard (5 niveles + 12 pasos)

```yaml
5_niveles:
  1_literal_read: lee_literal_input
  2_intent_detection: detecta_intencion
  3_context_loading: carga_contexto
  4_hypothesis_generation: genera_hipotesis
  5_validation: valida_respuesta
12_pasos:
  - parse_input
  - validate_schema
  - extract_intent
  - load_context
  - generate_hypotheses
  - test_hypotheses
  - synthesize_answer
  - validate_answer
  - check_consistency
  - format_output
  - add_citations
  - emit_output
```

### EURS Turbo (12 niveles + 45 pasos)

```yaml
12_niveles:
  1_literal_read
  2_intent_detection
  3_context_loading
  4_hypothesis_generation
  5_validation
  6_synthesis
  7_critique
  8_refinement
  9_cross_validation
  10_meta_validation
  11_final_check
  12_delivery
45_pasos: detallados_razonamiento_profundo
```

### Mythos — 40 Pasos en 8 Categorías (5 cada una)

```yaml
A_inicializacion_5:
  01: inicializar_contexto
  02: cargar_system_prompt
  03: validar_entrada
  04: verificar_permisos
  05: iniciar_sesion

B_analisis_5:
  06: parsear_input
  07: clasificar_intencion
  08: extraer_entidades
  09: construir_contexto
  10: detectar_ambiguedades

C_investigacion_5:
  11: buscar_web
  12: buscar_github
  13: buscar_rag
  14: buscar_memoria
  15: sintetizar_hallazgos

D_planificacion_5:
  16: generar_plan
  17: validar_plan
  18: optimizar_plan
  19: asignar_recursos
  20: programar_tareas

E_ejecucion_5:
  21: iniciar_ejecucion
  22: monitorear_progreso
  23: manejar_errores
  24: aplicar_reparaciones
  25: validar_resultados

F_verificacion_5:
  26: verificacion_tecnica
  27: verificacion_negocio
  28: verificacion_seguridad
  29: verificacion_calidad
  30: verificacion_compliance

G_entrega_5:
  31: formatear_output
  32: validar_formato
  33: seleccionar_destino
  34: enviar
  35: confirmar_recepcion

H_cierre_5:
  36: recolectar_feedback
  37: actualizar_memoria
  38: aprender_lecciones
  39: cerrar_sesion
  40: emitir_reporte
```

### Arquitectura de Control Alto

```
MYTHOS_control → LLM_razonamiento → OUTPUT
regla: MYTHOS_CONTROLA_LLM_RAZONA
```

### FABLES — Framework for Adversarial Battle of Logical Evaluation and Synthesis

```yaml
F1_inicializacion: [recibe_pregunta, carga_contexto, define_criterios_exito]
F2_generacion_adversarial: [genera_N_soluciones, cada_una_intenta_superar_anteriores, adversarial_search]
F3_critica_multi_agente: [5_agentes_critican, cada_uno_busca_problemas_diferentes, compilan_issues]
F4_refinamiento_iterativo: [soluciona_issues, regenera, repite_hasta_score>=95%]
F5_sintesis_final: [combina_mejores_partes, valida_output_completo, emite_respuesta]
```

### CHEF FINAL Fables (4 pasos)

```yaml
paso_1_revision_final: revisa_output_completo
paso_2_validacion_cruzada: cruza_todos_criterios
paso_3_refinamiento_cosmetico: mejoras_estilo_finales
paso_4_emision: emite_output_final_con_firma
```

### Micro-Ciclo (7 pasos)

```yaml
1_receive
2_decompose
3_distribute  # a_agentes
4_execute
5_aggregate
6_verify
7_emit
```

### DRE Pipeline (9 pasos)

```yaml
1_parse
2_analyze
3_hypothesize
4_research
5_synthesize
6_critique
7_refine
8_validate
9_emit
```

### OpenMythos

```yaml
que_es: version_open_source_sistema_mythos
componentes: [core_fijo, adaptadores_configurables, plugins_extensibles]
stack: 4_lenguajes [Python, TS, Rust, Go]
features: [PydanticAI_validacion, FSM_control_flujo, separacion_5_niveles]
```

### Distinción Razonamiento vs Control

```yaml
razonamiento: [quien: LLM, que: genera_hipotesis, como: probabilistico, 90_10: 10%]
control: [quien: codigo, que: decide_flujo, como: determinista, 90_10: 90%]
```

### 7 Validadores

```yaml
1_verifier: valida_output_vs_spec
2_critic: critica_adversarial
3_judge: juzga_entre_alternativas
4_sentinel: vigila_anomalias
5_sheriff: enforces_rules
6_policy_engine: aplica_politicas
7_pydanticai: validacion_schemas
```

### 8 Criterios Optimización

```yaml
1_latencia
2_costo
3_calidad
4_determinismo
5_trazabilidad
6_mantenibilidad
7_testabilidad
8_extensibilidad
```

### Diagrama Horizontal

```
INPUT → [EURS_Standard 5+12 / EURS_Turbo 12+45] → [Mythos_40_pasos_8_cat] → [FABLES_5F+CHEF_FINAL_4] → [7_validadores] → [Micro_7 / DRE_9] → OUTPUT
```

---

## DOC 05: Configuraciones del Orquestador

### 3 Perfiles APIs Intercambiables (versión detallada)

```yaml
conservador:
  NVIDIA_NIM: 4_keys_alta_calidad
  Cerebras: 1-2_keys_verificacion
  Groq: 1-2_keys_emergencias
  prioridad: calidad_sobre_velocidad
  costo: alto

equilibrado_DEFAULT:
  NVIDIA_NIM: 1_key
  Cerebras: 6_keys_mayor_uso
  Groq: 4-6_keys_complemento
  balance: calidad_velocidad
  costo: medio

agresivo:
  NVIDIA_NIM: 1_key_solo_critico
  Cerebras: todas_las_keys
  Groq: todas_las_keys
  velocidad: maxima
  costo: optimizado_por_uso

cambio_perfil: [automatico_contexto, manual_MAX, default_equilibrado]
```

### Inicio Autónomo (post pre-flight)

```yaml
1: crea_14_repos_GitHub  # 6_factories + 8_products
2: crea_7_HF_Spaces_own_tokens
3: escribe_5_Dockerfiles
4: inyecta_secretos
5: configura_profiles
6: arranca_orquestador
7: reporta_MAX
```

### M3 System Prompt Operativo

```yaml
ubicacion: /workspace/nct-proyecto/MI-SYSTEM-PROMPT-OPERATIVO.md
composicion: [5_GOALS, 12_PASOS, 7_pasos_adicionales, 8_reglas_absolutas, cosas_intocables]
7_pasos_adicionales:
  1: buscar_memoria
  2: validar_propuesta
  3: validar_salida
  4: validar_trazabilidad
  5: STATE_JSON_actualizado
8_reglas_absolutas:
  1: nunca_inventar
  2: nunca_mezclar_orquestador_con_GGUF_proyectos
  3: si_falta_info_PREGUNTAR_no_inventar
  4: M3_debe_proponer_sus_ideas_no_solo_registrar_MAX
  5: M3_debe_CREAR_archivos_reales_no_solo_parchear_docs
  6: M3_no_alucinar
  7: M3_no_hacer_preguntas_en_vez_de_proponer
  8: M3_no_saltarse_preguntas
```

### Reglas Absolutas MAX (consolidado)

```yaml
- NUNCA_crear_ni_cambiar_sin_APROBADO_explicito
- SOLO_AGREGO_capas_NUNCA_reemplazo
- MANTENER_todos_nombres_originales
- 5_GOALS_12_PASOS_obligatorios_cada_salida
- inicio: APLICANDO_SYSTEM_PROMPT_5_GOALS_12_PASOS
- fin: AUDIT_FINAL_PASO_12
- 3_inventarios_separados: tools != agents != ai_models
- Orquestador_INDEPENDIENTE_no_mezclar_con_GGUF_AI_keys_proyectos
- NO_inventar_datos_preguntar_si_falta
- NO_alucinar
- MVP_first_anti_overengineering
- NO_PC_solo_smartphones_iPad
- input_is_sacred_Input_Block_nunca_modifica_resume_parafrese_reinterpreta
- DSL_DAG_nunca_prompt_libre
- G5_gestiona_agentes_no_al_reves
- orquestador_confirma_proyecto_antes_ejecutar_Fase_0.5
- APIs_intercambiables_3_profiles
- estructura_<200_lineas_por_archivo
- cada_HF_Space_por_grupo_aislado_own_token
- cada_proyecto_separate_root_GitHub
- no_inventar_nuevas_categorias
- cada_salida_validar_antes_patchear_checklist
- mostrar_PENDIENTE_si_no_aprobado_STATE_JSON_actualizado
```

### Estado del Proyecto (versión complementaria)

```yaml
done:
  - 100_patches_documentacion_individual
  - 19_archivos_python_reales_726_lineas
  - constitucion_1276_lineas
  - memoria_persistente_2_topics
blocked:
  - pre_flight_data_MAX
  - M2.7_no_ha_instalado_nada_espera_GO_MAX
```

---

## DOC 12: Arquitectura Completa — NCT Neuronas Code Turbo

### Visión General NCT

```yaml
que_es: modulo_adicional_coordinacion_software_existente
NO_reemplaza: ningun_bloque_actual
NO_modifica: codigo_original
es: tercer_modo_trabajo_anadido
modos_software:
  1_manual: usuario_controla_cada_paso
  2_semi_automatico: software_actual_supervision
  3_continuo_NCT: coordinacion_automatica_tareas_largas
que_hace: coordina_25_bloques_existentes_automaticamente_sin_supervision
como_funciona:
  F0-3: clasifica_planifica_descompone_prepara
  F4: invoca_bloques_como_workers_unica_con_IA
  F5-6: monitorea_PAD_Ansiedad_Drift_y_verifica_3_capas
  F7-9: consolida_repara_entrega
```

### Arquitectura

```yaml
archivos_python_coordinacion: 8_~960_lineas
porcentaje_IA_coordinador: 0%  # solo_reglas_fijas
IA_en:
  F4: ejecucion
  F6: verificacion
comunicacion: state.json_con_bloques_existentes
no_requiere: [instalar_Kimi_K2.5, MiniMax, Hermes, desplegar_agentes_externos, modificar_codigo]
si_requiere: [lista_25_bloques_con_nombre_funcion_formato_IO, definir_como_invoca_cada_bloque]
```

### Ubicación y Estructura del Proyecto

```yaml
proyecto_principal/:
  software_principal/  # 25_bloques_SIN_TOCAR
    - arquitectura, rag, escritor, ejecutor, validacion, reparacion, ...
  nct_coordinator/  # NUEVO_modulo_adicional
    - __init__.py
    - fsm.py  # orquestador_10_fases
    - classifier.py  # F0
    - router.py  # F1
    - planner.py  # F2
    - context_isolator.py  # F3
    - worker_pool.py  # F4
    - monitor.py  # F5
    - verifier.py  # F6
    - consolidator.py  # F7
    - repair.py  # F8
    - deliver.py  # F9
  state/:
    - engine.py  # event_sourcing + snapshots
    - telemetry.py  # metricas_PAD
  config/nct_config.yaml
  state.json
  main.py  # entry_point_selector_modo
```

### 25 Bloques Software Principal (NO MODIFICAR)

```yaml
grupos: [arquitectura, rag, escritor, ejecutor, validacion, reparacion, test, deploy, ...]
total: 25_bloques
```

### 3 Modos de Operación

```yaml
manual: usuario_controla_paso_a_paso, ideal_tareas_pequenas
semi_automatico: software_sugiere_usuario_aprueba, puntos_confirmacion_entre_etapas
continuo: usuario_solo_describe_tarea_final, NCT_descompone_coordina_ejecuta_verifica_entrega, sin_intervencion, recuperacion_automatica
```

### Flujo Completo Modo Continuo

```
usuario_tarea → classifier(F0) → router(F1) → planner(F2-3) → worker_pool(F4) → INVOCA_25_BLOQUES → monitor(F5) || verifier(F6) → consolidator(F7) → repair(F8_si_falla) → deliver(F9) → usuario_resultado_con_trazabilidad
```

### 13 Bloques NCT (Coordinación 8 + Soporte 5)

```yaml
coordinacion_8:
  1_fsm: orquestador_central_10_fases_sin_IA
  2_classifier: clasifica_tareas [simple, batch, compleja]
  3_router: elige_ruta_modo_ejecucion
  4_planner: descompone_subtareas_balanceadas
  5_context_isolator: aisla_contexto_por_worker
  6_worker_pool: invoca_25_bloques_como_workers
  7_monitor: PAD_ansiedad_anti_drift
  8_verifier: verificacion_adversarial_3_capas

soporte_5:
  9_consolidator: consolida_resultados_workers
  10_repair: pipeline_5_pasos_si_falla
  11_deliver: empaqueta_entrega_resultado_final
  12_state_engine: event_sourcing + state.json
  13_state_telemetry: metricas + circuit_breaker
```

### Fases Detalladas

```yaml
F0_clasificacion_dual:
  intencion: Kimi  # simple/media/compleja
  tipo_tarea: MiniMax  # simple/batch/complex + tipo_proyecto
  salida: clasificacion_unificada

F1_modo_ruta:
  modo_agente: Kimi  # OK_Computer/Skills/Swarm
  ruta_ejecucion: MiniMax  # directa/batch/agentes_especializados
  salida: decision_unificada

F2_skills_descomposicion:
  carga_skills: Kimi  # SKILL.md
  planificacion: MiniMax  # todo_write + agentes
  salida: plan_unificado_subtareas_agentes_orden

F3_aislamiento:
  spawn_subagentes_congelados: Kimi
  structured_summaries: MiniMax  # contexto_aislado
  salida: workers_listos_contexto_aislado_tools

F4_ejecucion_unica_con_IA:
  worker_pool_Kimi: hasta_100_workers_asyncio_gather, pipeline_7_pasos_por_worker
  team_engine_MiniMax_dentro_de_cada_worker: leader_worker_verifier_3_rondas
  25_bloques: reciben_DSL_entrada_devuelven_JSON_validado_schema

F5_monitoreo_3_sistemas:
  PAD_Kimi:
    arousal: ">0.8"
    pleasure: "<0.2"
    accion: SIGKILL + Respawn
  ansiedad_MiniMax:
    duda_circulos: si
    nivel: 1/2/3
    accion: confirmacion_o_respawn
  anti_drift_Kimi:
    formula: KL(plan || actual) > 0.02
    accion: halt + rollback

F6_verificacion_3_capas:
  capa_1_adversarial_MiniMax: verifier_busca_errores_3_rondas
  capa_2_cruzada_Kimi: executor_B_valida_output_A
  capa_3_maker_checker_ambos: A_produce_B_verifica
  salida: solo_si_3_capas_OK_output_certificado

F7_consolidacion_jerarquica:
  EROS_3_tier_Kimi:
    tier_3_executors: logs_crudos
    tier_2_controllers: strategic_pulses
    tier_1_orchestrator: <5%_contexto
  coordinator_MiniMax: recibe_outputs_integra_maneja_escalados
  salida: informe_pre_entrega_completitud_drift

F8_repair_5_pasos:
  paso_1_retry_simple: 3_intentos
  paso_2_context_compression: L1_L2
  paso_3_fallback_model_agent
  paso_4_restore_checkpoint
  paso_5_escalate: coordinator [replanificar, preguntar_usuario, abortar]

F9_consolidacion_final_entrega:
  merge_resultados + consistencia_global
  empaquetado: KIMI_REF + archivos + URLs
  state.json_final: trazabilidad_completa
```

### 6 Niveles del Sistema Completo

```yaml
N1_software_principal: 25_bloques_INTOCABLE
N2_NCT_coordinator: 13_archivos_ADICIONAL
N3_MAXBRY_SUPER_TEAM: [constitucion, CSA, SID, BIS, Loop, Output_Engine, OOS, OVFS]
N4_modelos: 9_GGUF + 16_API_keys
N5_memoria: persistente + STATE_JSON
N6_infraestructura: 7_HF_Spaces, 14_repos, 5_Dockerfiles
```

### 10 Principios Transversales

```yaml
1: MVP_first_anti_overengineering
2: regla_absoluta_NUNCA_sin_APROBADO_MAX
3: solo_agregar_NUNCA_reemplazar
4: mantener_nombres_originales_aprobados
5: cero_alucinacion_preguntar_si_falta_info
6: independencia_Orquestador_!=_GGUF_!=_Proyectos
7: validacion_previa_cada_salida_antes_patchear
8: mostrar_PENDIENTE_lo_no_aprobado_visible
9: STATE_JSON_siempre_actualizado
10: 5_GOALS_12_PASOS_en_cada_salida
```

---

## DOC 12b: Pipeline + Fases (Master)

### 10 Fases del Pipeline (versión master)

```yaml
F0_pre_boot: [verifica_entorno, carga_config, inicializa_HF_Spaces, verifica_tokens_secrets]
F0_5_confirmation_gate_INTOCABLE: [muestra_plan_MAX, pide_confirmacion, bloquea_hasta_aprobacion]
F1_input_reception: [recibe_input_MAX, detecta_canal, auth_rate_limit, log_input]
F2_input_processing: [aplica_input_engine_v4_54_componentes, genera_input_canonico]
F3_planning: [genera_plan, descomposicion_tareas, asignacion_recursos, consensus_consejo]
F4_execution: [ejecuta_tareas, monitoreo_continuo, 3_monitores_activos, repair_si_falla]
F5_validation: [CSA_audita_10J_5F, SID_verifica_definicion, BIS_valida_skills]
F6_refinement: [si_score<95%_refina, iteracion_hasta_score_OK, max_N_iteraciones]
F7_output_generation: [output_engine, OOS_prepara_entrega, OVFS_estructura, 16_capas_gobernanza]
F8_delivery: [multi_target_23_destinos, adaptive_format, confirmation_tracking]
F9_monitoring: [post_delivery, feedback_loop, production_monitoring, auto_rollback_si_degrada]
```

### 4 Escenarios (versión master)

```yaml
escenario_1_simple: 9_pasos  # [Input, Parse, Plan, Execute, Validate, Refine, Output, Deliver, Monitor]
escenario_2_medio: 16_pasos  # [Input, Receive, Normalize, Parse, Validate, Intent, Context, Plan, Consensus, Execute, Monitor, Validate, Refine, Output, Deliver, Monitor]
escenario_3_complejo: 25_pasos  # [pre_analisis_5, research_5, plan_5, execute_5, validate_5]
escenario_4_critico: 30-50_pasos  # [pre_analisis_10, research_10, plan_10, execute_10, validate_10] + adicionales_segun_necesidad
```

### Complexity Estimator (versión master)

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

categorias:
  0-20: simple  # TM01-TM02
  21-40: media  # TM03-TM05
  41-60: compleja  # TM06-TM08
  61-80: avanzada  # TM09-TM10
  81-100: critica  # TM11-TM12
```

### LISTA_GLOBAL — 4 Reglas (versión master)

```yaml
R1: una_tarea_por_vez_principal  # no_paralelizar_misma_sesion_MAX
R2: tareas_independientes_en_paralelo  # si_independientes_si
R3: tareas_dependientes_secuenciales  # si_A_depende_B_espera
R4: tareas_criticas_aisladas  # TM11_propio_contexto
```

### Checkpoints por Fase

```yaml
F0: pre_boot_state
F0_5: confirmation_state
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

### Estados por Fase

```yaml
PENDING
RUNNING
CHECKPOINTED
VALIDATED
FAILED
RECOVERING
COMPLETED
```

### Diagrama Horizontal

```
F0_pre_boot → F0_5_confirmation_gate_INTOCABLE → F1_input_reception → F2_input_processing_54 → F3_planning → F4_execution → F5_validation_CSA_SID_BIS → F6_refinement_si_score<95% → F7_output_generation_13_14_OVFS → F8_delivery_23_destinos → F9_monitoring_feedback
```

---

## DOC 13: Arquitectura NCT (Master)

### NCT — Neuronas Code Turbo

```yaml
que_es: proyecto_global_que_contiene_MAXBRY
NO_es: el_orquestador_en_si
es: ecosistema_donde_opera
ubicacion:
  /workspace/nct-proyecto/:
    - CONSOLIDADO-FINAL/  # 18_docs
    - MASTER-FINAL/  # 13+_docs
    - CONSTITUCION-ORQUESTADOR.md
    - PARCHE-v14_a_PARCHE-v17
    - PATCHES-*
    - PARCHES-*
  /workspace/maxbry/:
    - g1-infra
    - g2-core
    - g3-ui
    - g4-audit
    - g5-orquestador  # ⭐
    - g6-asistentes
```

### 25 Bloques Software Principal (NO modificados por MAXBRY)

```yaml
01_inicializador: boot_sistema
02_config_loader: carga_configuracion
03_state_manager: estado_global
04_event_bus: bus_eventos
05_logger: sistema_logs
06_error_handler: manejo_errores
07_network_manager: red
08_storage_manager: almacenamiento
09_auth_manager: autenticacion
10_permission_manager: permisos
11_cache_manager: cache
12_queue_manager: colas
13_worker_pool: pool_workers
14_task_scheduler: scheduler
15_result_aggregator: agregador
16_retry_manager: reintentos
17_circuit_breaker: circuit_breaker
18_metrics_collector: metricas
19_health_checker: health
20_notification_manager: notificaciones
21_plugin_manager: plugins
22_api_gateway: gateway_api
23_database_connector: DB
24_external_service_client: servicios_externos
25_telemetry: telemetria
```

### NCT Coordinator — 13 Archivos

```yaml
01_nct_coordinator: coordinador_principal
02_nct_modes: selector_modos
03_nct_flows: definicion_flujos
04_nct_phases: fases_F0_F9
05_nct_inputs: inputs
06_nct_outputs: outputs
07_nct_state: estado
08_nct_memory: memoria
09_nct_skills: skills
10_nct_agents: agentes
11_nct_audit: auditoria
12_nct_metrics: metricas
13_nct_delivery: entrega
```

### 2 Versiones Arquitectura

```yaml
V1_chat_ai_nct_original:
  - asistente_chat_tradicional
  - procesa_mensajes
  - genera_respuestas
  - memoria_simple

V2_adaptador_mythos:
  - wrapper_sobre_V1
  - anade_razonamiento_profundo
  - anade_mythos_system_prompt
  - anade_control_alto_nivel
```

### Flujo Continuo (versión NCT)

```
MAX_Telegram → MAXBRY_recibe → SID_5_preguntas → BIS_lookup → Plan_generado → Consensus_consejo → Ejecutar_30_micro_agentes → Validar_CSA → Refinar_si_score<95% → Output_Engine → Multi_target_Delivery → Monitoreo → Feedback_Memoria_Mejora
```

### 4 Principios Arquitectura

```yaml
modularidad: [responsabilidad_unica, bus_eventos, acoplamiento_debil]
determinismo: [90%_codigo, 10%_LLM, reproducibilidad_alta]
trazabilidad: [cada_accion_registra, state_actualizado, logs_estructurados]
resiliencia: [circuit_breakers, retry_backoff, failover, repair_pipeline]
```

### Fases Detalladas (versión NCT)

```yaml
F0_pre_boot: [python_version, HF_Spaces, tokens, secrets, network]
F1_input: [Telegram, API_call, CLI_command, web_dashboard]
F2_process: input_engine_v4_0
F3_plan: consensus
F4_execute: 30_micro_agentes + 12_especializados
F5_validate: CSA_10_jueces
F6_refine: hasta_score>=95%
F7_output: output_engine + OOS + OVFS
F8_deliver: multi_target
F9_monitor: post_delivery
```

### Integración MAXBRY

```
MAXBRY → invoca → NCT_Coordinator → coordina → 25_Bloques → producen → Output
regla: MAXBRY_NO_modifica_25_bloques_los_INVOCA_como_workers
```

### Interfaz

```yaml
para_MAX: [Telegram_principal, API_REST, dashboard_web, CLI]
para_MAXBRY: [Python_API, MCP_server, CLI_directo]
```

### Conclusión

```yaml
NCT: ecosistema
MAXBRY: orquestador
25_bloques: musculos
13_archivos_NCT_Coordinator: sistema_nervioso
10_fases: flujo_sanguineo
todo_junto: SO_Distribuido_para_IA
```

---

## DOC 14: Detalles Adicionales del Chat
