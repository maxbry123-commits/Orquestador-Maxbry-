# AGENTES — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 1)

> **Separado del orquestador** (orquestacion-from-docs-*).
>
> Esta es la extracción **literal** (no inventada) de toda la información relacionada con los **AGENTES** (no orquestador) encontrada en los 57 documentos fuente en `/workspace/attachments/`. Formato AI-friendly (YAML/DSL/código + diagramas horizontales).
>
> **Reglas aplicadas**:
> - Solo contenido citado literalmente de los documentos fuente.
> - Separación estricta: agentes ≠ orquestador.
> - Sin repetir información entre partes.
> - Cada diagrama es horizontal y compacto.
> - ~100KB por archivo.

# AGENTES — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 1)

> **Separado del orquestador** (orquestacion-from-docs-*).
>
> Esta es la extracción **literal** (no inventada) de toda la información relacionada con los **AGENTES** (no orquestador) encontrada en los 57 documentos fuente en `/workspace/attachments/`. Formato AI-friendly (YAML/DSL/código + diagramas horizontales).
>
> **Reglas aplicadas**:
> - Solo contenido citado literalmente de los documentos fuente.
> - Separación estricta: agentes ≠ orquestador.
> - Sin repetir información entre partes.
> - Cada diagrama es horizontal y compacto.
> - ~100KB por archivo.


## DOC 7: AGENTES DEL ORQUESTADOR (Extraído del historial)

### 1. 5 Agentes del Consenso (APX-C)

```yaml
proposito: decisiones_de_diseño_arquitectura_o_estrategia
NO_uso_tareas_mecanicas:  # mover_archivos_generar_strings_hacer_commits

por_que_5_no_3_no_7:
  3_agentes: empates_frecuentes_sin_voto_de_calidad
  5_agentes: quorum_natural_diversidad_desempate_facil
  7_agentes: overhead_alto_sin_ganancia_proporcional
  5_especializados_gt_gt_5_genericos

los_5_agentes_consenso:
  1_CREATIVE_AGENT:
    misión: generar_mayor_numero_posible_ideas_sin_filtro
    personalidad: explorador_divergente_sin_miedo_a_lo_absurdo
    input: problema_del_usuario_1_parrafo
    output: 5_a_10_ideas_con_nombre_descripcion_riesgo
    modelo: uno_creativo_Claude_Opus_GPT-4
    temperature: 0.9
    tokens: ~2000
  2_INNOVATION_AGENT:
    misión: tomar_cada_idea_del_Creative_y_mejorarla
    personalidad: iterador_que_pasaria_si
    input: ideas_del_Creative_+_problema_original
    output: cada_idea_mejorada_con_version_evolucionada_variantes_pros_contras_score
    modelo: el_mas_fuerte_disponible
    temperature: 0.7
    tokens: ~3000
  3_CRITIC_AGENT:
    misión: destruir_todo_lo_debil_adversarial_por_diseno
    personalidad: esceptico_riguroso_sin_piedad
    input: ideas_del_Innovation
    output: para_cada_idea_3_puntos_debiles_2_riesgos_no_considerados_score_recomendacion
    modelo: uno_diferente_al_Creative_diversidad
    temperature: 0.3
    tokens: ~2500
  4_SELECTION_AGENT:
    misión: elegir_la_mejor_superviviente_o_combinacion
    personalidad: decisor_sintetizador
    input: ideas_del_Innovation_+_scores_del_Critic
    output: Ganadora_Runner_up_Justificacion_Score_final
    regla: si_score_lt_0.6_no_hay_consenso_escala_al_usuario
    modelo: el_mas_fuerte_disponible
    temperature: 0.2
    tokens: ~2000
  5_ARCHITECTURE_AGENT:
    misión: convertir_la_idea_ganadora_en_plano_ejecutable
    personalidad: arquitecto_sistematico
    input: ganadora_+_problema_original
    output: Stack_recomendado_Fichas_DSL_a_crear_Fichas_a_modificar_Talleres_involucrados_Estimacion_esfuerzo_Riesgos_tecnicos_Primer_paso_concreto
    modelo: uno_fuerte_de_codigo
    temperature: 0.3
    tokens: ~3000

flujo:
  USUARIO/M3 → CREATIVE → INNOVATION → CRITIC → SELECTION → ARCHITECTURE → RESULTADO

reglas_duras:
  cuando_si_consenso:
    - decisiones_de_arquitectura
    - decisiones_de_UX
    - decisiones_de_producto
    - decisiones_de_seguridad
    - naming_branding_propuesta_de_valor
  cuando_no_consenso:
    - tareas_mecanicas_mover_archivos_generar_strings
    - tests_automatizados
    - commits_y_deploys
    - consultas_base_de_datos
    - cualquier_cosa_100%_determinista
  cuando_escalar_usuario:
    - empate_entre_opciones
    - score_de_la_ganadora_lt_0.6
    - consenso_pide_recursos_fuera_presupuesto
    - consenso_contradice_decision_ya_aprobada

prompt_dsl_cerrado:
  SISTEMA: "Eres el {AGENT_ROLE} en el sistema de consenso de NEURONA CODE TURBO. Tu misión: {MISSION_TEXT}. Tu personalidad: {PERSONALITY_TEXT}. Tus restricciones: {RESTRICTIONS}. Responde SOLO en el formato JSON especificado. No agregues prosa."
  CONTEXTO: 
    proyecto: {PROJECT_NAME}
    stack: {STACK}
    presupuesto: {BUDGET}
    tiempo: {TIME}
    restricciones_adicionales: {EXTRA}
  PROBLEMA: {USER_PROBLEM}
  INPUT_PREVIO: {PREVIOUS_AGENT_OUTPUT}
  FORMATO_DE_SALIDA: {OUTPUT_SCHEMA_JSON}
  IMPORTANTE:
    - no_inventes_features_que_no_esten_en_stack
    - se_conciso
    - si_dudas_no_tengo_suficiente_informacion
```

### 2. 5 Agentes de Investigación (Multi-Source)

```yaml
1_GitHub_Agent:
  que_busca:
    - repos_publicos_relevantes
    - stars_forks_issues
    - patrones_de_uso
    - codigo_de_referencia
    - proyectos_similares
  outputs:
    - lista_repos_con_metadata
    - analisis_de_calidad
    - codigo_reutilizable
    - issues_recurrentes
2_HuggingFace_Agent:
  que_busca:
    - modelos_GGUF_disponibles
    - datasets_relevantes
    - spaces_con_codigo_util
    - papers_referenciados
    - versiones_y_updates
  outputs:
    - lista_modelos_con_URLs
    - datasets_descargables
    - codigo_de_Spaces
    - estado_de_APIs
3_Web_Agent:
  que_busca:
    - documentacion_oficial
    - articulos_tecnicos
    - tutoriales
    - best_practices
    - comparativas
    - precios_costos
  outputs:
    - URLs_relevantes
    - resumenes
    - comparativas
    - recomendaciones
4_YouTube_Agent:
  que_busca:
    - tutoriales_paso_a_paso
    - demos_de_productos
    - conferencias_tecnicas
    - comparativas_visuales
    - casos_de_estudio
  outputs:
    - URLs_de_videos
    - transcripciones_relevantes
    - timestamp_de_momentos_clave
    - resumenes_visuales
5_MCP_Agent:
  que_busca:
    - MCP_servers_disponibles
    - tools_registrados
    - integraciones_oficiales
    - Smithery_catalogo
    - Composio_integraciones
  outputs:
    - lista_MCP_servers
    - tools_utilizables
    - compatibilidad
    - configuracion_necesaria
```

### 3. 12 Micro-Agentes Especializados (de MiMo/Lop v200)

```yaml
MA-CODE-GEN:
  nombre: Code_Generator
  responsabilidad: genera_codigo_a_partir_de_spec
  input: [spec.md, stack.json]
  output: [code.zip, diff.patch]
MA-CODE-LINT:
  nombre: Linter
  responsabilidad: lint_+_format_+_type-check
  input: code.zip
  output: report.json
MA-CODE-TEST:
  nombre: Tester
  responsabilidad: unit_+_integration_+_mutation
  input: [code.zip, tests/]
  output: [junit.xml, coverage.json]
MA-RAG-SEARCH:
  nombre: Web/GH_Search
  responsabilidad: busqueda_vectorial_+_rerank
  input: [query, k]
  output: chunks.json_con_citas
MA-RAG-SYNTH:
  nombre: Synthesizer
  responsabilidad: sintetiza_respuesta_con_citas
  input: chunks.json
  output: answer.md
MA-DOC-WRITE:
  nombre: Doc_Writer
  responsabilidad: documenta_arquitectura/decisiones
  input: [artifacts/, audience]
  output: doc.md
MA-ARCH-PLAN:
  nombre: Architect_Planner
  responsabilidad: planifica_arquitectura_y_stack
  input: requirements.json
  output: arch.yaml
MA-VERIFY-3CAPAS:
  nombre: Verifier
  responsabilidad: verificacion_adversarial_3_capas
  input: [artifact, rubric]
  output: verdict.json
MA-REPAIR-5STEP:
  nombre: Repairer
  responsabilidad: pipeline_5_pasos_de_reparacion
  input: failure.json
  output: [repaired.json_o_escalate]
MA-RESEARCH-WEB:
  nombre: Web_Researcher
  responsabilidad: crawling_+_extraccion
  input: [urls, depth]
  output: pages.jsonl
MA-RESEARCH-GH:
  nombre: GitHub_Researcher
  responsabilidad: busqueda_en_github_via_api
  input: [query, lang, stars_min]
  output: repos.json
MA-EMIT-REPORT:
  nombre: Report_Emitter
  responsabilidad: empaqueta_resultado_final
  input: state.json
  output: [report.md, manifest.json]

diseno_reglas:
  - una_sola_responsabilidad
  - un_solo_input_schema
  - un_solo_output_schema
  - estado_efimero
  - muerte_tras_emitir_JSON
  - max_LOC_core_200
```

### 4. 10 Propuestas M3 para INPUT/LOOP

```yaml
1_meta_agentes_que_crean_otros_agentes: ✅
2_causalidad_no_correlacion: ✅
3_counterfactual_reasoning_que_habria_pasado: ✅
4_auto_modificacion_de_codigo: ✅
5_memoria_episodica: ✅
6_zero_shot_transfer_entre_proyectos: ✅
7_neural_architecture_search_NAS: ✅
8_time_travel_debugging: ✅
9_inteligencia_colectiva_emergente: ✅
10_auto_curriculum: ✅
```

### 5. 9 Propuestas M3 para OUTPUT

```yaml
1_Pre_Mortem_Analysis: ✅
2_Output_Sandbox: ❌_RECHAZADO_POR_MAX
3_Auto_Rollback_Inteligente: ✅
4_Meta_Learning_entre_Releases: ✅
5_Output_Personalization: ✅
6_Multi_Stakeholder_Output: ✅
7_Causal_Output_Tracing: ✅
8_Output_Marketplace_Interno: ✅
9_Self_Improving_Output_Quality: ✅
10_Production_Monitoring_Post_Publish: ✅
```

### 6. Hallazgos de Investigación (Referencias Aprobadas)

```yaml
tier_S_plus_excelentes:
  OpenCode: [154.5K_stars, 75+_LLMs, MCP_first]
  Gemini_CLI: [103.1K_stars, Gemini_free]
  OpenHands: [72.6K_stars, Python_multi_agente]
  Open_Interpreter: [63.4K_stars, Local]
  Aider: [44.3K_stars, 100+_LLMs]
  Goose: [43.7K_stars, MCP_first]

tier_A_muy_buenos:
  Qwen_Code: [24.1K_stars, Qwen3-Coder]
  Crush: [23.8K_stars, Go]
  Kimi_CLI: [8.4K_stars, Kimi_K2]
  Forge_Code: [7.2K_stars, 300+_modelos]
  MiMo_Code: [Xiaomi_MiMo_MIT_5%_vs_Claude_Code]

tier_B:
  - BLXCode
  - Open_Design
  - OpenClaw
  - KiloCode
  - Cline
  - BLACKBOX.AI

frameworks_de_agentes:
  LangGraph: [115K_stars, state_machine]
  CrewAI: [102K_stars, crew_+_roles]
  OpenAI_Agents_SDK: framework_oficial
  LlamaIndex: RAG
  Mem0: memoria
  LangMem: memoria_largo_plazo
  AutoGen: multi_agente_Microsoft
  DSPy: prompt_optimization
  Haystack: NLP_pipelines
  Microsoft_Agent_Framework_MAF: production_ready
  AgentOrchestra: jerarquico_83.39%_GAIA

workflow:
  - Temporal
  - Kestra
  - Airflow
  - Dagster
  - Prefect
  - Argo_Workflows

MCP_integracion:
  - MCP_Model_Context_Protocol
  - Smithery  # catalogo_MCP
  - Composio  # integraciones

investigacion_especifica:
  DeerFlow_2.0: [ByteDance_46K_stars_Super_Agent_Harness_memory_sandboxes_skills_message_gateway]
  LiteLLM: unifica_100+_LLMs_en_1_API
  Hermes_Agent: [149K_stars, learning_loop_L1+L2+L3]
  OpenCLAW: [308K_stars, gateway_channels_skills_MCP]
```

### 7. 10 Jueces del CSA (Consejo Supremo de Auditoría)

```yaml
autoridad: absoluta_sobre_TODA_decision
fases_por_juez: 5

los_10_jueces:
  J1_Comprension_objetivo: ¿el_output_realmente_Entiende_QUE_se_pidio?
  J2_Cobertura_requisitos: ¿todos_los_requisitos_estan_cubiertos?
  J3_Consistencia_logica: ¿el_output_es_logicamente_coherente?
  J4_Exactitud_tecnica: ¿el_output_es_tecnicamente_correcto?
  J5_Arquitectura_y_diseno: ¿el_diseno_es_correcto_y_mantenible?
  J6_Calidad_codigo: ¿el_codigo_sigue_buenas_practicas?
  J7_Investigacion_y_evidencia: ¿las_afirmaciones_tienen_respaldo?
  J8_Optimizacion_y_rendimiento: ¿el_output_es_eficiente?
  J9_Seguridad_y_riesgos: ¿el_output_es_seguro?
  J10_Calidad_final_y_UX: ¿el_output_es_usable_y_de_calidad?

5_fases_por_juez:
  F1_audita_input_completo
  F2_busca_lo_que_NADIE_reviso
  F3_10_soluciones_distintas
  F4_destruye_propia_solucion
  F5_ataca_otros_9_jueces
```

### 8. 10 Agentes del Consejo de Consenso

```yaml
1_Voto_Tecnico
2_Voto_de_Negocio
3_Voto_de_Costos
4_Voto_de_Riesgos
5_Voto_Etico
6_Voto_de_UX
7_Voto_de_Performance
8_Voto_de_Seguridad
9_Voto_de_Compatibilidad
10_Veto_de_MAX_decision_final
```

### 9. 5 Officers del Executive Board

```yaml
1_COO: eficiencia_performance
2_CFO: costos_presupuesto
3_CQO: calidad_global
4_CRO: riesgos_alertas
5_CLO: aprendizaje_evolucion
```

### 10. 10 Calidades del Agente Ideal

```yaml
obligatorias:
  - calidad
  - robustez
  - recuperacion
  - persistencia
  - escalabilidad
  - auditoria
  - control
  - evolucion_futura
no_objetivos:
  - velocidad
  - simplicidad
```

---

## DOC MASTER 09: AGENTES COMPLETO (30 Micro + 5 Consenso + 5 Investigación + 10 CSA + 10 Consejo + 5 Officers)

### Visión General: Tipos de Agentes

```yaml
tipos_y_cantidades:
  micro_agentes_G5: 30  # operaciones_internas
  consenso: 5  # decisiones_criticas
  investigacion: 5  # busqueda_de_info
  CSA_jueces: 10  # auditoria
  consejo: 10  # votacion
  officers: 5  # supervision_global
  micro_agentes_especializados_v200: 12  # tareas_especificas
  MiMo_aligned: 12  # memoria_evolucion
TOTAL: 87+_agentes
```

### 30 Micro-Agentes del G5

```yaml
categorias:
  1_a_5_Analisis
  6_a_10_Planificacion
  11_a_15_Ejecucion
  16_a_20_Validacion
  21_a_25_Aprendizaje
  26_a_30_Meta
```

### 5 Agentes de Consenso (Mecanismo de Votación)

```yaml
3.1_Creative:
  - genera_ideas_creativas
  - propone_soluciones_no_convencionales
  - voto: originalidad_+_viabilidad
3.2_Innovation:
  - busca_patrones_innovadores
  - recomienda_adopcion_de_nuevas_tecnicas
  - voto: innovacion_+_madurez
3.3_Critic:
  - analisis_critico_constructivo
  - busca_debilidades
  - voto: robustez
3.4_Selection:
  - selecciona_entre_alternativas
  - compara_opciones
  - voto: mejor_opcion
3.5_Architecture:
  - valida_arquitectura
  - propone_patrones
  - voto: coherencia_arquitectonica

mecanismo_consenso:
  5_agentes_deliberan
  3_o_mas_de_acuerdo: decision_tomada
  empate: escala_a_MAX
  4_a_1: fuerte_consenso_procede
  3_a_2: debil_consenso_escala
  2_a_3_o_menos: bloqueado
```

### 5 Agentes de Investigación

```yaml
4.1_GitHub_Researcher:
  - busca_codigo_en_github
  - encuentra_repos_relevantes
  - analiza_stars_issues_PRs
4.2_HuggingFace_Researcher:
  - busca_modelos_en_HF
  - encuentra_datasets
  - evalua_Spaces
4.3_Web_Researcher:
  - busqueda_web_general
  - crawling_+_extraccion
  - documentacion_oficial
4.4_YouTube_Researcher:
  - busca_videos_tecnicos
  - extrae_transcripts
  - encuentra_tutoriales
4.5_MCP_Researcher:
  - investiga_servidores_MCP
  - encuentra_tools_disponibles
  - evalua_integraciones

ciclo_investigacion:
  minimo: 2_rondas
  maximo: 5_rondas
  stop_if: evidencia_ge_85%_seg
  sintesis_final
```

### 10 Jueces CSA

```yaml
autoridad: absoluta
numeros: J1_a_J10
ver: Master_04
```

### 10 Agentes del Consejo

```yaml
votan_en_decisiones_criticas:
  1_tecnico
  2_negocio
  3_costos
  4_riesgos
  5_etico
  6_UX
  7_performance
  8_seguridad
  9_compatibilidad
  10_veto_MAX
```

### 5 Officers (Executive Board) — Versión Completa

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

### 12 Micro-Agentes Especializados (v200) Inspirados en MiMo Code

```yaml
MA-CODE-GEN: Code_Generator_genera_codigo
MA-CODE-LINT: Linter_lint_+_format
MA-CODE-TEST: Tester_tests_+_coverage
MA-RAG-SEARCH: Web/GH_Search_busqueda
MA-RAG-SYNTH: Synthesizer_sintetiza_respuestas
MA-DOC-WRITE: Doc_Writer_documenta
MA-ARCH-PLAN: Architect_Planner_planifica_arquitectura
MA-VERIFY-3CAPAS: Verifier_verificacion_adversarial
MA-REPAIR-5STEP: Repairer_pipeline_de_5_pasos
MA-RESEARCH-WEB: Web_Researcher_crawling
MA-RESEARCH-GH: GitHub_Researcher_busqueda_github
MA-EMIT-REPORT: Report_Emitter_empaqueta_resultado
```

### 12 Micro-Agentes MiMo-Aligned (Loops Internos)

```yaml
inspirados_en: loops_internos_de_MiMo_Code
cantidad: 12

7_loops_identificados:
  decision_loop: cada_turno
  checkpoint_loop: cada_N_turnos
  writer_loop: cuando_contexto_gt_70%
  max_mode_loop: decisiones_criticas
  dream_loop: semanal
  repair_loop: en_error
  evolution_loop: al_cierre
restantes_5: extensiones_para_lograr_12
```

### 8 Hallazgos de Research (MAX)

```yaml
1_DeerFlow_2.0:
  vendor: ByteDance
  stars: 46K
  descripcion: Super_Agent_Harness
2_LiteLLM:
  descripcion: unifica_100+_LLMs_en_1_API
3_Microsoft_Agent_Framework_MAF:
  descripcion: production_ready_multi_agent_workflows
4_AgentOrchestra:
  descripcion: patron_jerarquico_multi_agent_83.39%_GAIA
5_OpenCLAW:
  stars: 308K
  descripcion: gateway_+_channels_+_skills_+_MCP
6_Hermes_Agent:
  stars: 149K
  descripcion: learning_loop_L1+L2+L3
7_LangGraph:
  stars: 115K
  descripcion: state_machine_para_agents
8_CrewAI:
  stars: 102K
  descripcion: crew_+_roles_+_tasks
```

### 19 Propuestas M3 Aplicadas

```yaml
OUTPUT_9_aplicadas_+_1_rechazada:
  1_Pre_Mortem_Analysis: ✅
  2_Auto_Rollback: ✅
  3_Meta_Learning: ✅
  4_Personalization: ✅
  5_Multi_Stakeholder: ✅
  6_Causal_Tracing: ✅
  7_Marketplace: ✅
  8_Self_Improving: ✅
  9_Production_Monitoring: ✅
  10_Output_Sandbox: ❌_RECHAZADO

INPUT_LOOP_10_aplicadas:
  1_Definition_Score_Gate: ✅
  2_Auto_Repair_Pipeline: ✅
  3_3_Cycle_Parallel: ✅
  4_Checkpoint_Restore: ✅
  5_Max_Mode_Sampling: ✅
  6_Goal_Stop: ✅
  7_Dynamic_Workflow: ✅
  8_Multi_Source_Research: ✅
  9_Deterministic_90_10: ✅
  10_Pre_Analysis_Seed: ✅
```

### Conclusión

```yaml
MAXBRY_orquesta: 87+_agentes_distribuidos_en:
  - 30_micro_agentes_operativos
  - 5_agentes_de_consenso
  - 5_agentes_de_investigacion
  - 10_jueces_CSA
  - 10_consejo
  - 5_officers
  - 12_especializados_v200
  - 12_MiMo_aligned

cada_uno_con: responsabilidad_especifica
forma: sistema_completo_de_auto_gobierno
```

---

## DOC MASTER 26: NOMBRES ESPECÍFICOS + ARCHIVOS + ESQUEMAS (Agentes Relevantes)

### G6 Staff — 5 Agentes Principales

```yaml
5.1_MiniMax_M3:
  rol: LLM_principal
  via: NVIDIA_NIM
  cargo: lider_del_G5_SKYNER
  personalidad: arquitecto
5.2_MiMo_Code:
  rol: code_agent_paralelo
  ubicacion: HF_aparte
  funcion: tareas_horizonte_largo
5.3_OpenCLAW:
  rol: agente_adicional_multi_canal
  stars: 308K
5.4_Smolagents:
  rol: agente_adicional_tareas_generales
  ubicacion: HuggingFace
5.5_Hermes_Agent:
  rol: archivist_y_memoria
  stars: 149K
  Learning_Loop_L1: 149K_stars
  learning_loop: L1+L2+L3
5.6_Code_Agent_CLI:
  variantes: [Aider, Cline]
  rol: code_generation_local
  funcion: fallback_para_MiMo
```

### 5 Agents Staff from Master 26 vs 6 of Skill Catalog

```yaml
G6_staff_canonico_5_AGENTES_PRINCIPALES:
  1: MiniMax_M3_LLM_principal_NVIDIA_NIM_lider_SKYNER
  2: MiMo_Code_code_agent_paralelo_HF_tareas_horizonte_largo
  3: OpenCLAW_multi_canal_308k_stars
  4: Smolagents_HuggingFace_tareas_generales
  5: Hermes_Agent_archivist_memoria_149k_stars_learning_loop_L1_L2_L3
mas_opcional: Code_Agent_CLI_Aider_o_Cline_fallback_MiMo
```

### 6 Niveles de Autonomía (NOMBRES Exactos)

```yaml
L1_MANUAL: pasos_discretos_IA_0%_memoria_volatil
L2_SEMI_MANUAL: minutos_IA_0%
L3_SCHEDULED_AUTOMATIC: horas_IA_0%
L4_SUPERVISED_AUTONOMOUS: horas_a_24h_IA_0%_repair_pipeline_5_pasos
L5_CONTINUOUS_AUTONOMOUS_72H_PLUS: 72h_a_mes_IA_0%_memoria_EROS_3_tier
L6_EVOLUTIONARY_AUTONOMOUS: indefinido_IA_0%_meta_memoria_auto_mejora
```

---

## DOC MASTER 14: DLG DSL de NCT (Detalles Adicionales — Agentes)

### G2 ARTIFACT ENGINE — Componentes del Motor DSL

```yaml
G2_ARTIFACT_ENGINE:
  DSL: sintaxis_para_escribir_modulos
  DAG: grafo_de_dependencias_entre_modulos
  Contracts: schemas_JSON_que_validan_entradas_salidas
  Validators: funciones_que_prueban_el_contrato
  State_Machine: estados_del_modulo_idle_running_done_fail
  Memory: lectura_escritura_en_Xata_durante_ejecucion
  LLM: agente_LLM_para_la_parte_10%_con_consenso

roles_fijos:
  DSL_dice: QUE_hacer
  DAG_dice: EN_QUE_ORDEN
  Contracts_dice: QUE_FORMA_debe_tener_entrada_salida
  Validators_dice: SI_ESTA_BIEN
  State_Machine_dice: EN_QUE_PUNTO_esta
  Memory_dice: QUE_RECUERDA
  LLM_dice: QUE_DECIDE_cuando_hay_ambiguedad
```

### Estructura Módulo DSL (NCT Módulo)

```yaml
MODULO_NCT:
  id: nct.creativity.run_consensus
  version: 1.0.0
  owner_workshop: NCT-CREATIVIDAD
  description: Corre_el_consenso_de_5_agentes_sobre_una_idea
  inputs:
    idea: string
    max_agents: 5
  outputs:
    winner: object
    runner_up: object
    reasoning_log: array
  contract: { schema_de_inputs, schema_de_outputs }
  dependencies:
    - nct.creativity.creative_agent
    - nct.creativity.critic
    - "..."
  consensus:
    required: true
    agents: [Creative, Innovation, Critic, Selection, Architecture]
    tiebreaker: selection
  runtime:
    sandbox: wasm-py|docker|process
    timeout_s: 120
  memory_keys:
    - nct:project:<id>:creativity:last_run
  llm_budget:
    max_calls: 5
    max_tokens_per_call: 4000
  validators:
    - nct.validators.outputs_not_empty
    - nct.validators.winner_has_score

reglas_modulo:
  id_debe_ser_jerarquico: nct.<taller>.<verbo>
  contract_se_valida_antes_y_despues_de_ejecutar: si_falla_modulo_a_fail
  dependencies_se_resuelven_con_el_DAG
  consensus_required_true_significa_que_el_LLM_no_decide_solo
  memory_keys_punteros_a_Xata
  llm_budget_limita_uso_de_tokens_por_modulo
```

### Mapa Paso → Módulo(s) DSL

```yaml
paso_0:
  modulos:
    - nct.capture.append_turn
    - nct.capture.write_context_md
  taller: transversal
  consensus: no
paso_1:
  modulos:
    - nct.frontend.scaffold_app  # FRONTEND consensus_si
    - nct.design.apply_theme_tokens  # DISEÑO no
paso_2:
  modulos:
    - nct.history.scan_repo  # ARQUITECTURA no
    - nct.history.build_timeline  # BACKEND no
    - nct.history.bridge_to_xata  # BACKEND no
paso_3:
  modulos:
    - nct.creativity.run_consensus  # CREATIVIDAD si_5_agentes
    - nct.architecture.propose_blueprint  # ARQUITECTURA si
paso_4:
  modulos:
    - nct.config.register_api_key  # BACKEND no
    - nct.config.set_router_policy  # BACKEND no
    - nct.config.select_default_model  # FRONTEND no
paso_5:
  modulos:
    - nct.artifact.register_ficha  # ARQUITECTURA no
    - nct.artifact.execute_in_sandbox  # BACKEND no
    - nct.artifact.read_from_xata  # BACKEND no
    - nct.artifact.write_to_xata  # BACKEND no
paso_6:
  modulos:
    - nct.consensus.configure_per_agent_keys  # ARQUITECTURA no
    - nct.chat.switch_active_model  # FRONTEND no
paso_7:
  modulos:
    - nct.github.connect_repo  # DEVOPS no
    - nct.github.push_branch  # DEVOPS no
    - nct.xata.bootstrap_schema  # BACKEND no
```

### Cómo se define un módulo nuevo

```yaml
1_Nombre: elige_un_id_con_la_jerarquia_nct_taller_verbo
2_Inputs/Outputs: escribe_las_firmas
3_Contract: define_el_schema_JSON
4_Dependencies: que_otros_modulos_necesita
5_Consensus: preguntate_si_toca_diseno_seguridad_UX
6_Runtime: sandbox_preferido
7_Memory_keys: que_lee_escribe
8_LLM_budget: tope_conservador
9_Validators: al_menos_2
10_Tests: el_taller_TESTING_genera_casos
```

### DAG (Grafo de Dependencias)

```yaml
reglas:
  si_A_depende_de_B: B_corre_ANTES
  si_B_y_C_no_dependen_entre_si: corren_EN_PARALELO
  orquestador_puede_inyectar_dependencias_dinamicas
  si_DAG_tiene_ciclos: error_de_diseno
```

### State Machine del Módulo

```yaml
estados:
  idle: estado_inicial
  ready: inputs_OK_+_deps_OK
  running: ejecucion
  done: contract_OK
  fail: cualquier_error_o_timeout
transiciones:
  idle → ready: si_inputs_OK_y_deps_OK
  ready → running: ejecucion_iniciada
  running → done: contract_OK
  running → fail: timeout_o_error
  fail → ready: retry
```

### Memoria Xata — Schema Mínimo

```yaml
tablas:
  nct_modules: una_fila_por_modulo_registrado
  nct_runs: una_fila_por_ejecucion
  nct_memory: key_value_con_scope
  nct_consensus: una_fila_por_decision_de_los_5_agentes
```

### Validators (Tests Baratos)

```yaml
tipos:
  de_contrato_vienen_del_schema:
    - si_input_no_es_JSON_valido_o_falta_campo_a_fail

de_negocio_funciones_especificas:
  - nct.validators.outputs_not_empty
  - nct.validators.winner_has_score
  - nct.validators.no_secrets_in_outputs  # CRITICO
  - nct.validators.filenames_are_ascii
```

### Universal Module Contract v1.5 (JSON Schema)

```yaml
concepto: contrato_universal_de_modulos_que_permite_conectar_fichas_de_codigo_prompts_DSL_APIs_MCP_bases_de_datos_herramientas_y_LLMs_externos_mediante_interfaz_comun
funcion: cada_ficha_declara_que_consume_que_produce_como_se_ejecuta_bajo_que_reglas_puede_conectarse
conexion: [codigo, LLM, DSL_prompt, API, MCP, DB, tools]
compatibilidad: fichas_se_unen_automaticamente_si_entradas_y_salidas_son_compatibles
seguridad: define_permisos_limites_sandbox_recuperacion
resultado: construye_pipelines_DAG_donde_cada_modulo_es_una_neurona_reutilizable
ecosistemas_compatibles: [MAXBRY, YAIWES, NCT_Neuronas_Code_Turbo]

schema_principal_campos_requeridos:
  artifact_id: string
  artifact_version: semver
  contract_version: string
  contract_hash: sha256:...
  hash_algorithm: sha256
  estado: draft|testing|active|deprecated|blocked
  ciclo_vida: object
  registry_metadata: object
  contrato:
    rol: transform|source|sink
    consume: object
    expone: object
    errores: object
    restricciones: object
  naturaleza:
    determinista: bool
    idempotente: bool
    puro: bool
    efectos: object
  seguridad: object
  ejecucion:
    kind: code|llm|db|api|tool
    transport: stdio|importlib|http|sdk|prompt|mcp
    config: object
    fallback: object
  resultado:
    success_schema_uri: string
    error_schema_uri: string
    trace_id_format: uuid|ulid|snowflake
  dependencias: object
  versioning:
    min: semver
    max: semver
    mode: semver_strict|semver_loose|exact
  gobernanza_ref: object
```

### Consenso de 5 Agentes (Detalles del Flujo)

```yaml
flujo_paso_a_paso:
  1_M3_detecta_que_una_decision_necesita_consenso
  
  2_genera_el_prompt_DSL_cerrado_en_mavi_prompts_consensus_txt:
    contiene:
      - problema_del_usuario
      - contexto_del_proyecto_del_CONTEXT_md
      - restricciones_presupuesto_tiempo_stack
  
  3_M3_spawnea_5_sub_sesiones_en_paralelo_modulo_nct_consensus_run_consensus:
    cada_una_recibe:
      - el_prompt_DSL
      - su_rol_Creative_Innovation_Critic_Selection_Architecture
      - su_key_+_modelo
      - timeout_60s
  
  4_M3_espera_respuestas_timeout_global_90s:
    si_los_5_responden: sigue_a_5
    si_3_a_4_responden: sigue_con_los_que_hay_+_marca_quorum_parcial
    si_lt_3_responden: ALERTA_+_escala_al_usuario
  
  5_M3_loguea_todo_en_nct_consensus_Xata:
    campos:
      - topic
      - agents_responded
      - winner
      - runner_up
      - reasoning_log
      - decided_at
      - decided_by: consensus
  
  6_M3_presenta_al_usuario:
    - ganadora
    - runner_up_por_si_usuario_prefiere
    - razonamiento_corto_del_Critic
    - plano_de_ejecucion_del_Architecture
  
  7_usuario_aprueba_o_itera_o_cancela

visualizacion_usuario:
  durante:
    - CONSENSO_EN_CURSO_tema_agentes_estados_tiempo
  despues:
    - CONSENSO_COMPLETADO_ganadora_score_razon_plano_ejecucion_opciones

manejo_fallos_consenso:
  - un_agente_respuesta_vacia: reintentar_1_vez_si_falla_marcar_partial_quorum
  - dos_agentes_contradictorios: Critic_media_si_persiste_escala
  - todos_proponen_lo_mismo_sin_diversidad: Creative_re_genera_con_mas_temperatura
  - score_muy_bajo: escala_con_2_mejores_opciones
  - usuario_rechaza: guardar_correccion_+_ajustar_prompt_DSL

porque_es_SISTEMA_no_prompt:
  - estructura_5_agentes_definidos
  - contratos_formato_JSON
  - estado_que_respondio_cada_uno_en_que_orden
  - memoria_resultados_en_Xata
  - auditoria_todo_se_loguea
  - recuperacion_si_un_agente_falla_sigue
  - evolucion_correcciones_del_usuario_lo_mejoran
```

---

## DOC MASTER 17: MAXBRY SUPER TEAM Detalles Completos (Agentes)

### Liderazgo del G5

```yaml
liderado_por:
  - 1x_NVIDIA_SKYNER_lider
  - 2x_Cerebras
  - 2x_Groq
  - 4_GGUF_local
  - 4_GGUF_via_API
```

### MAXBRY — NO es una LLM

```yaml
definicion:
  - NO_es_una_nueva_LLM
  - NO_es_un_modelo_fundacional
  - NO_compite_con_Claude_GPT_Gemini_Qwen
  - ES_una_CAPA_EXTERNA_DE_ORQUESTACION_CONTROL_Y_ORGANIZACION
  - vive_fuera_de_los_modelos
  - coordina_modelos_herramientas_proyectos_y_objetivos

5_capas:
  USUARIO → MAXBRY → Control_Layer → Workflow_Layer → Memory_Layer → Tool_Layer → LLM_Layer
```

### 14 Categorías BIS (Biblioteca Inteligente de Skills)

```yaml
A_Arquitectura: diseno_de_sistemas_patrones_decisiones_arquitectonicas
B_Gestion: gestion_de_proyectos_planificacion_recursos
C_Frontend: HTML_CSS_JS_frameworks_UI/UX
D_Backend: APIs_servidores_logica_de_negocio
E_Movil: iOS_Android_React_Native_Flutter
F_Escritorio: aplicaciones_desktop_Electron_Tauri
G_Bases_de_Datos: SQL_NoSQL_vectoriales_migraciones
H_APIs: REST_GraphQL_gRPC_webhooks
I_DevOps: CI/CD_contenedores_infraestructura
J_IA: LLMs_ML_agentes_RAG_fine-tuning
K_Testing: Unit_integration_E2E_performance
L_Seguridad: Auth_encryption_vulnerabilities_OWASP
M_Automatizacion: Scripts_workflows_RPA_schedulers
N_Lenguajes: Python_JS_Go_Rust_Java_etc
```

### 30 Micro-Agentes del G5 — Categorías Específicas

```yaml
1_a_5_Analisis:
  - input_parsing
  - intent
  - context
  - etc
6_a_10_Planificacion:
  - task_breakdown
  - scheduling
  - etc
11_a_15_Ejecucion:
  - delegacion
  - monitoring
  - retries
  - etc
16_a_20_Validacion:
  - CSA_jueces_subset
  - quality
  - etc
21_a_25_Aprendizaje:
  - memory
  - patterns
  - optimization
  - etc
26_a_30_Meta:
  - orquestacion_de_orquestadores
  - recovery
  - etc

caracteristicas:
  - cada_uno_con_rol_especifico
  - trabajan_en_paralelo_sobre_bus_de_eventos
  - capacidad_de_invocarce_entre_si
  - auto_descubrimiento_de_capacidades
  - max_200_LOC_por_archivo_regla_de_estructura
```

### G5 — Recursos y Capacidades

```yaml
recursos:
  7_HF_Spaces:
    caracteristicas:
      - cada_uno_con_propio_token
      - aislados_sin_compartir_secretos
      - comunicacion_via_API
  14_repos_GitHub:
    - cada_proyecto_separate_root
    - cada_grupo_repositorio_separado
    - productos_adicionales_repos_separados
  5_Dockerfiles:
    - cada_grupo_con_su_Dockerfile
    - runtime_consistente

capacidades:
  - 2000+_agentes_simultaneos
  - 1000+_tareas_simultaneas
  - sin_redesign_al_escalar
  
recursos_disponibles:
  - "7_HF_Spaces_x_16GB_eq_112GB_RAM"
  - "~13.5GB_usados_por_modelos_G6"
  - "87%_margen_libre"

escalabilidad:
  horizontal: agregar_HF_Spaces
  vertical: upgrade_a_Spaces_larger
  "sin_redisenar_el_codigo"
```

### G5 — Integración con M3 + Kimi

```yaml
M3_JEFE_Arquitecto:
  rol: MiniMax_M3_como_arquitecto
  funciones:
    - decide_QUE_hacer
    - disena_de_alto_nivel
    - interactua_con_MAX
    - NO_ejecuta_codigo_directo
Kimi_K2.7_Code_EMPLEADO_Ejecutor:
  rol: Kimi_K2.7-Code_como_implementador
  funciones:
    - decide_COMO_hacerlo
    - implementa_codigo
    - testing
    - debugging

flujo:
  MAX → M3_jefe → M3_planifica → Kimi_ejecuta → Kimi_reporta → M3_valida → M3_presenta → MAX_aprueba
```

### G5 — Verificación (5 niveles por salida)

```yaml
5_niveles_validacion:
  1_buscar_memoria_revisar_si_ya_existe
  2_validar_propuesta_es_correcta
  3_validar_salida_cumple_formato
  4_validar_trazabilidad_registrable
  5_STATE_JSON_actualizado

checklist_validacion:
  - 5_GOALS_presentes
  - 12_PASOS_presentes
  - AUDIT_FINAL_al_final
  - 3_inventarios_separados
  - sin_mezclas_con_GGUF/proyectos
  - sin_alucinaciones
```

### G5 — Cosas Intocables

```yaml
NUNCA_se_modifican:
  - 10_jueces_CSA_J1-J10_con_5_fases
  - auditor_SID_5_preguntas_fijas
  - constitucion_39_principios
  - 14_categorias_BIS
  - 30_micro_agentes
  - 11_internal_roles
  - 10_parallel_queues
  - 10_agent_consensus_council
  - 6_autonomy_levels_L1-L6
  - 12_task_models_TM01-TM12
  - 5_loop_versions_ALV_LOP_*
  - 3_monitors
  - 9_GGUF_models_confirmados
  - 16_API_keys
  - 4_NVIDIA_NIM
  - 6_Cerebras
  - 6_Groq
  - 60_datasets_PARCHE-v15
  - 60_adapters_PARCHE-v15
```

### Resumen Ejecutivo

```yaml
MAXBRY_SUPER_TEAM:
  - orquestador_universal_distribuido_para_IA
  - 2000+_agentes_y_1000+_tareas
  - costo_$0_HF_free_+_API_free_tiers
  - sin_PC_solo_smartphones_iPad
  - constitucion_39_principios
  - CSA_10_jueces_autoridad_absoluta
  - BIS_14_categorias_de_skills
  - 30_micro_agentes_internos
  - loop_15_capas_+_3_ciclos_paralelos
  - output_engine_27_componentes
  - input_engine_54_componentes
  - 9_modelos_GGUF_+_16_API_keys
  - 100%_trazabilidad_con_STATE_JSON
  - auto_evolucion_continua
```

---

## DOC MASTER 24: AUDITORÍA FINAL (Cobertura Agentes 100%)

### MAXBRY SUPER TEAM en Números

```yaml
metricas:
  master_documentos: 24
  bytes_totales: ~167KB
  principios_constitucion: 39
  jueces_CSA: 10
  fases_por_juez: 5
  preguntas_SID: 5
  categorias_BIS: 14
  criterios_skills: 13
  componentes_Input_Engine: 54
  componentes_Output_Engine: 27
  capas_LOOP: 15
  ciclos_paralelos: 3
  capas_Output_Gobernanza: 16
  micro_agentes: 30
  roles_internos: 11
  colas_paralelas: 10
  niveles_autonomia: 6
  task_models: 12
  loop_versions: 5
  monitores: 3
  agentes_consenso: 5
  agentes_investigacion: 5
  officers: 5
  micro_agentes_especializados: 12
  modelos_GGUF: 9
  API_keys: 16
  perfiles_API: 3
  destinos_multi_target: 23
  patches_documentados: 170+
  propuestas_M3_aplicadas: 19
  propuestas_M3_rechazadas: 1
  hallazgos_research: 8
  archivos_python_creados: 19
  lineas_de_codigo: 726
  caracteristicas_constitucion: [v1.0, v2.0, v3.0]
```

### Cobertura 100% por Categoría — Agentes

```yaml
agentes_100%:
  - 30_micro_agentes
  - 5_consenso
  - 5_investigacion
  - 10_consejo
  - 5_officers
  - 12_especializados_v200
  - 12_MiMo_aligned

agentes_total: 87+
```

### Diagrama Completo MAXBRY (Agentes en G5)

```
MAX(CEO) ─► G3_UI ─► G5_MAXBRY_SUPER_TEAM_ORQUESTADOR
                          ├── CAPA_CONTROL(90%_codigo)
                          │   ├── Constitucion_39p
                          │   ├── CSA_10Jx5F
                          │   ├── SID_5_preg
                          │   └── BIS_14_cat
                          ├── ENGINES
                          │   ├── Input_54
                          │   ├── Output_27
                          │   ├── Loop_v6.0_15+3
                          │   └── OOS_v3.1_14
                          ├── AGENTES_87+
                          │   ├── 30_micro_+11_roles
                          │   ├── 5_consenso
                          │   ├── 5_investigacion
                          │   ├── 10_CSA_+5_off
                          │   ├── 12_v200
                          │   └── 12_MiMo_aligned
                          └── MEMORIA_Y_ESTADO
                              ├── state.json
                              ├── events.log
                              ├── memory_4_tier
                              └── checkpoints_firmados
─► G4_AUDIT_CSA_SID ─► G2_CORE_BIS_SID_InOut ─► G1_INFRA_HF_GitHub_Docker ─► G6_ASISTENTES_9_GGUF_+_16_API
```

### Lista Master Documentos (24 docs)

```yaml
01-vision-general: 12701_bytes
02-estructura-organizacional: 9892_bytes
03-constitucion-completa: 8170_bytes
04-csa-completo: 7093_bytes
05-sid-bis: 7308_bytes
06-input-engine: 5326_bytes
07-output-engine: 5805_bytes
08-loop: 4803_bytes
09-agentes: 5570_bytes
10-modelos-apis: 4273_bytes
11-razonamiento-mythos: 5195_bytes
12-pipeline-fases: 4518_bytes
13-arquitectura-nct: 5639_bytes
14-mimo-lop-v200: 7797_bytes
15-reglas-intocables: 5133_bytes
16-dsl-universal-plug: 6386_bytes
17-configuraciones-costos: 4968_bytes
18-patches-extras: 5443_bytes
19-pre-flight-pendientes: 4894_bytes
20-validacion-cruzada-final: 9249_bytes
21-subsistemas-detallados: 7650_bytes
22-ejemplos-paso-a-paso: 9671_bytes
23-implementacion-deploy: 9359_bytes
24-auditoria-final: este_doc
total: ~167KB_en_24_documentos
```

### Validación Final — Coverage 100%

```yaml
cobertura_general: 100%
sin_contradicciones: true  # todos_consistentes_entre_si
referencias_validas: true  # cross_references_resuelven
tamanos_respetados: true  # cada_doc_le_60000_chars
DSL_DAG: pasa_todos_los_checks
Sentinel_+_Judge:
  sentinel: 100%_pass
  judge_score_promedio: 94/100
```

### Entregables

```yaml
documentacion:
  - 24_master_documentos_~167KB
  - 18_documentos_consolidados_~209KB
  - 170+_patches_documentados
  - constitucion_v6.2_1276_lineas
codigo:
  - 19_archivos_python_726_lineas_en_/workspace/maxbry/g7/output_engine/v2/
  - 9_carpetas_de_modulos
  - tests_definidos
memoria_persistente:
  - 2_topics_en_agent_memory
  - "27599_+_7197_bytes"
hallazgos:
  - 13_attachments_en_/workspace/attachments/
  - 8_hallazgos_de_research_documentados
```

### Conclusión Final

```yaml
MAXBRY_SUPER_TEAM_status: 100%_documentado_y_validado
total: 24_master_+_18_consolidados_+_170+_patches_=_Cobertura_completa

listo_para_implementacion_cuando_MAX:
  1: dar_8_datos_pre_flight
  2: aprobar_arquitectura
  3: activar_M2.7_para_instalacion

no_falta_NADA_de_informacion_sobre_orquestador_y_agentes
todo_en: /workspace/nct-proyecto/MASTER-FINAL/_y_/workspace/nct-proyecto/CONSOLIDADO-FINAL/
```

---

## DOC MASTER 25: SKYNER + CONSENSO DETALLADO (Algoritmo SKYNER + 17 Modelos G7+G8)

### 1. Algoritmo SKYNER

```yaml
SKYNER: "Structured Knowledge Yielding Network for Enhanced Reasoning"
caracteristicas:
  - combina_17_modelos_en_2_grupos_G7_razonamiento_+_G8_especializados
  - confidence_scoring_ponderado_por_accuracy_historica
  - veto_power_del_orquestador_MiniMax_M3
  - re_invocacion_multi_round
  - pares_AUTO_BOTH_IA1_propone_IA2_refuta
  - fallback_automatico
  - logging_completo
mejora_10x_vs_consenso_simple:
  reduccion_alucinaciones: "~85%_en_10K_tareas"
  accuracy_promedio: 62% → 94%
  reduccion_rondas_correccion: 7x_de_8_a_1.1
  tiempo: 2.3x_mayor_pero_calidad_10x
```

### 2. Taxonomía — Grupo G7 (5 Modelos Razonamiento Profundo)

```yaml
G7-01_HRM_Hierarchical_Reasoning_Model:
  model_id: HRM-001
  provider: interno
  role: ARQUITECTO_PRINCIPAL
  specialty: razonamiento_jerarquico
  strengths: [descomposicion_profunda, meta_razonamiento, patrones_ocultos]
  weaknesses: [verbosidad_alta, latencia_alta]
  context_window: 128000
  max_output_tokens: 16000
  cost_per_1k_tokens: 0.045
  temperature_default: 0.3
  voting_weight_default: 1.0
  accuracy_history_30d: 0.967
G7-02_Qwen_2.5-72B-Instruct:
  model_id: QWEN-72B-001
  provider: Alibaba_Cloud
  role: ANALISTA_MULTI_DOMINIO
  specialty: razonamiento_multilingue
  strengths: [matematicas_avanzadas, codigo_estructurado]
  context_window: 131072
  cost_per_1k_tokens: 0.040
  voting_weight_default: 1.0
  accuracy_history_30d: 0.945
G7-03_DeepSeek-V3:
  model_id: DEEPSEEK-V3
  provider: DeepSeek
  role: ANALISTA_TECNICO
  specialty: code_generation
  strengths: [codigo_avanzado, debugging]
  voting_weight_default: 1.0
  accuracy_history_30d: 0.952
G7-04_Llama-3.1-70B:
  model_id: LLAMA-70B
  provider: Meta
  role: GENERALISTA_AVANZADO
  specialty: razonamiento_general
  voting_weight_default: 0.9
  accuracy_history_30d: 0.923
G7-05_Claude-Sonnet-4.6:
  model_id: CLAUDE-SONNET-46
  provider: Anthropic
  role: ANALISTA_NUANCIADO
  specialty: nuancing_and_refinement
  voting_weight_default: 1.0
  accuracy_history_30d: 0.961
```

### 3. Taxonomía — Grupo G8 (12 Modelos Especializados)

```yaml
G8-01: [HRM-Text-1B, Razonamiento_ligero, Quick_reasoning]
G8-02: [Qwen2.5-Coder-1.5B, Code_generation, Code]
G8-03: [Granite-Code-3B, Code, Code]
G8-04: [Granite-Doc-3B, Documentation, Docs]
G8-05: [Liquid-LFM2.5-1.2B, Thinking, Reasoning]
G8-06: [Gemma-4-E4B, Efficient_reasoning, Reasoning]
G8-07: [Gemma-4-E2B, Light_reasoning, Light]
G8-08: [GPT-OSS-20B, MoE, Heavy_reasoning]
G8-09: [Nemotron-3-Nano-4B, Lightweight, Quick]
G8-10: [MiMo-Code, Code_agent, Code_parallel]
G8-11: [Smolagents, General_agent, Tasks]
G8-12: [Hermes_Agent, Archivist_+_memory, Memory]
```

### 4. Confidence Scoring + Veto Power

```python
score_final = sum(
    model.vote * model.accuracy_history * model.voting_weight
) / sum(model.accuracy_history * model.voting_weight)
```

```yaml
veto_power:
  quien_puede_anular: MiniMax_M3
  cuando:
    score_lt_0.70: true
    hay_riesgo_de_seguridad: true
    hay_contradiccion_con_Constitucion: true
    hay_alucinacion_detectada: true

umbrales_decision:
  score_ge_0.95: APROBADO_fuerte
  score_0.85_a_0.94: APROBADO
  score_0.70_a_0.84: APROBADO_con_notas
  score_lt_0.70: RECHAZADO_o_REPLANNER
```

### 5. Schemas de Voto por Modelo

```yaml
vote_schema:
  model_id: string
  vote: enum[approve, reject, rework, abstain]
  confidence: float  # 0-1
  reasoning: string  # max_200_chars
  evidence: array
  timestamp: ISO8601
  round: int
```

### 6. Schema de Decisión Final

```yaml
decision_schema:
  consensus_id: string
  task_id: string
  models_voted: int
  approve_count: int
  reject_count: int
  rework_count: int
  abstain_count: int
  final_decision: enum[APPROVED, REJECTED, REWORK]
  confidence_score: float
  consensus_strength: float
  veto_applied: bool
  veto_reason: string
  round: int
  timestamp: ISO8601
```

### 7. Función Universal consensus()

```python
async def consensus(task: dict, models: list, rounds: int = 3) -> dict:
    for round in range(rounds):
        votes = await asyncio.gather(*[
            model.vote(task) for model in models
        ])
        
        decision = aggregate_votes(votes)
        
        if decision.confidence >= 0.95:
            return decision
        
        if decision.final_decision == "REJECTED":
            return decision
    
    # Si no hay consenso después de N rondas
    return apply_veto_or_escalate(task, votes)
```

### 8. Mecanismo de Re-Invocación Multi-Round

```yaml
cuando_se_re_invoca:
  - score_lt_0.95_despues_de_primera_ronda
  - cualquier_modelo_reporta_rework
  - detectadas_contradicciones

maximo_de_rondas:
  default: 3_rondas
  tareas_criticas: 5_rondas
  tareas_simples: 1_ronda

costo:
  - cada_ronda_suma_tokens_consumidos
  - si_excede_budget_escala_a_MAX
```

### 9. Mecanismo de Veto del Orquestador

```python
if decision.confidence < 0.70:
    veto(reason="low_confidence")
elif violates_constitution(decision):
    veto(reason="constitutional_violation")
elif has_security_risk(decision):
    veto(reason="security_risk")
elif detected_hallucination(decision):
    veto(reason="hallucination_detected")
```

```yaml
resolucion_de_veto:
  - M3_propone_correccion
  - vuelve_a_votar_con_correccion_aplicada
  - o_escala_a_MAX
```

### 10. Ponderación por Accuracy Histórica

```python
weight = model.accuracy_history_30d * model.voting_weight_default
```

```yaml
actualizacion:
  cada_30_dias: se_recalcula_accuracy_history
  basado_en: feedback_de_outputs_aceptados_o_rechazados
```

### 11. Manejo de Empates

```yaml
empate_simple_50_50:
  - escalado_a_M3_para_desempate
  - M3_decide_con_voto_de_calidad
empate_multiple_33_33_33:
  - se_pide_ronda_adicional
  - si_persiste: veto_de_M3
```

### 12. Fallback Automático entre Modelos

```yaml
cuando_se_activa:
  - modelo_retorna_error
  - modelo_retorna_resultado_degenerado
  - latencia_excede_umbral
orden_de_fallback: primario → secundario → terciario → escalar_a_MAX
```

### 13. Sistema de Logging Completo

```yaml
que_se_loggea:
  - cada_voto_individual
  - cada_re_invocacion
  - cada_decision_final
  - cada_veto_aplicado
  - cada_fallback
donde_se_guarda:
  - "/logs/consensus/{task_id}/{round}.json"
  - INDEX_global_en_ChromaDB
```

### 14. Pares AUTO_BOTH (IA1 Propone, IA2 Refuta)

```yaml
concepto:
  - dos_modelos_trabajan_en_par
  - IA1_genera_propuesta
  - IA2_busca_refutaciones
  - output_consolidado
uso:
  - decisiones_de_alto_riesgo
  - tareas_ambiguas
  - validacion_de_codigo_critico
```

### 15. Integración en Orquestador G5

```yaml
donde_se_invoca:
  - Fase_5_Validacion
  - Fase_8_Repair
  - cualquier_decision_critica

api:
  python: |
    from g5_orquestador import consensus
    result = await consensus(
        task=task_dict,
        models=["hr", "qwen", "claude"],
        rounds=3
    )
```

### 16. Integración en Sistema de Razonamiento Externo

```yaml
STANDARD_paso_10:
  modelos: 5
  rondas: 1
  score_minimo: 0.85

TURBO_paso_10_reforzado:
  modelos: 12
  rondas: 3
  score_minimo: 0.95
  aplicar: pares_AUTO_BOTH
```

### 17. Métricas y Observabilidad

```yaml
metricas_tracked:
  - consensus_total
  - consensus_approved
  - consensus_rejected
  - consensus_rework
  - average_rounds_per_task
  - average_score
  - veto_count
  - fallback_count
  - hallucination_detected
```

### 18. Conclusión SKYNER

```yaml
algoritmo_SKYNER: "corazon_del_consenso_de_MAXBRY_SUPER_TEAM"
componentes:
  - 17_modelos_distribuidos_en_G7_y_G8
  - confidence_scoring_ponderado
  - veto_power_del_orquestador
  - re_invocacion_multi_round
  - fallback_automatico
  - logging_completo
mejora: 10x_en_accuracy_vs_consenso_simple
```

---

## DOC MASTER 04: CSA COMPLETO (Consejo Supremo de Auditoría)

### 1. Qué es el CSA

```yaml
CSA: Consejo_Supremo_de_Auditoria
es: organo_de_maxima_autoridad_dentro_del_Orquestador_MAXBRY_SUPER_TEAM
proposito: auditoria_y_validacion

caracteristicas:
  autoridad_absoluta: ningun_agente_modelo_o_capa_puede_invalidar_veredicto_CSA
  5_fases: cada_juez_ejecuta_las_mismas_5_fases_en_orden
  sistema_veto: cualquier_juez_puede_vetar_bloquea_output
  auditoria_adversarial: buscan_lo_que_nadie_mas_busco
  trazabilidad_completa: cada_veredicto_se_registra_con_evidencia

diferencia_con_auditores_genericos:
  auditor_generico: funciona_si_o_no
  CSA: funciones_y_optimo_y_seguro_y_etico_y_mantenible
```

### 2. Los 10 Jueces CSA

```yaml
J1_Comprension_del_Objetivo:
  pregunta: ¿entendimos_QUE_quiere_MAX?
  evalua:
    - claridad_del_objetivo
    - alineacion_con_intencion_original
    - completitud_de_la_interpretacion
  output: Score_0_a_100_+_issues

J2_Cobertura_de_Requisitos:
  pregunta: ¿cubrimos_TODO_lo_requerido?
  evalua:
    - requisitos_explicitos_cubiertos
    - requisitos_implicitos_identificados
    - edge_cases_considerados
  output: Score_0_a_100_+_issues_+_gaps

J3_Consistencia_Logica:
  pregunta: ¿es_logicamente_coherente?
  evalua:
    - sin_contradicciones_internas
    - premisas_soportan_conclusiones
    - sin_razonamiento_circular
  output: Score_0_a_100_+_issues

J4_Exactitud_Tecnica:
  pregunta: ¿es_tecnicamente_correcto?
  evalua:
    - codigo_compila_o_ejecuta
    - algoritmos_correctos
    - patrones_correctos
    - sin_bugs_conocidos
  output: Score_0_a_100_+_issues_+_bugs

J5_Arquitectura_y_Diseno:
  pregunta: ¿esta_bien_disenado?
  evalua:
    - patrones_arquitectonicos
    - separacion_de_responsabilidades
    - SOLID_principles
    - mantenibilidad
  output: Score_0_a_100_+_issues_+_mejoras

J6_Calidad_de_Codigo:
  pregunta: ¿el_codigo_es_de_calidad?
  evalua:
    - legibilidad
    - naming
    - comentarios
    - estilo_consistente
    - coverage
  output: Score_0_a_100_+_issues_+_refactorings

J7_Investigacion_y_Evidencia:
  pregunta: ¿tenemos_evidencia_suficiente?
  evalua:
    - fuentes_citadas
    - datos_verificables
    - benchmarks_actuales
    - referencias_reales
  output: Score_0_a_100_+_issues_+_gaps

J8_Optimizacion_y_Rendimiento:
  pregunta: ¿es_eficiente?
  evalua:
    - latencia
    - throughput
    - uso_de_memoria
    - escalabilidad
    - complejidad_algoritmica
  output: Score_0_a_100_+_issues_+_optimizaciones

J9_Seguridad_y_Riesgos:
  pregunta: ¿es_seguro?
  evalua:
    - vulnerabilidades_conocidas
    - OWASP_compliance
    - secretos_expuestos
    - auth_o_authz_correcto
    - input_validation
  output: Score_0_a_100_+_issues_+_riesgos

J10_Calidad_Final_y_UX:
  pregunta: ¿la_entrega_final_es_buena?
  evalua:
    - documentacion
    - ejemplos_de_uso
    - mensajes_de_error_claros
    - UX_general
    - accesibilidad
  output: Score_0_a_100_+_issues_+_sugerencias
```

### 3. Las 5 Fases por Juez

```yaml
F1_Audita_Input_Completo:
  - lee_TODO_el_input_sin_prisa
  - identifica_supuestos_implicitos
  - mapea_dependencias
  - lista_explicitamente_lo_que_NO_esta
F2_Busca_Lo_Que_Nadie_Reviso:
  - asume_que_otros_ya_hicieron_lo_obvio
  - busca_edge_cases
  - busca_corner_cases
  - busca_combinaciones_raras
F3_10_Soluciones_Distintas:
  - genera_10_soluciones_alternativas
  - conserva_solo_la_mejor
  - documenta_por_que_descarto_las_otras_9
F4_Destruye_Propia_Solucion:
  - asume_que_su_propio_veredicto_puede_estar_mal
  - busca_contraejemplos_a_su_propio_argumento
  - identifica_debilidades_en_su_critica
F5_Ataca_Otros_9_Jueces:
  - revisa_veredictos_de_otros_jueces
  - busca_inconsistencias_entre_ellos
  - identifica_puntos_ciegos_colectivos
  - reporta_discrepancias

total_por_ciclo: 10_x_5_eq_50_auditorias
```

### 4. Sistema de Veto

```yaml
veto_simple:
  quien: cualquier_juez
  efecto: bloquea_hasta_resolver
veto_calificado:
  condicion: 2_o_mas_jueces_vetando
  efecto: bloquea_y_escala_a_MAX
veto_de_seguridad:
  juez: J9_Seguridad
  autoridad: veto_absoluto_en_temas_de_seguridad
resolucion_de_vetos:
  1: el_agente_o_productor_genera_paquete_de_correccion
  2: CSA_vuelve_a_auditar
  3: si_pasa_procede
  4: si_no_pasa_escala_a_MAX
```

### 5. Ejecución del CSA

```yaml
cuando_se_ejecuta:
  - antes_de_cada_output_importante
  - antes_de_cada_deploy
  - cuando_un_agente_o_modelo_falla_gt_2_veces
  - cuando_drift_gt_0.10

codigo_python:
  async_run_csa: |
    async def run_csa(artifact, rubric):
        judges = [J1, J2, J3, J4, J5, J6, J7, J8, J9, J10]
        results = await asyncio.gather(*[j.run(artifact, rubric) for j in judges])

        # Veto simple
        vetoes = [r for r in results if r.veto]
        if vetoes:
            return {"decision": "vetoed", "vetoes": vetoes}

        # Score agregado
        avg_score = sum(r.score for r in results) / 10

        # Consensus check
        if avg_score >= 95:
            return {"decision": "approve", "scores": results}
        elif avg_score >= 80:
            return {"decision": "approve_with_notes", "scores": results}
        else:
            return {"decision": "reject", "scores": results}
```

### 6. Auditor SID Complementario

```yaml
SID: Sistema_Inteligente_de_Definicion
cuando_trabaja: ANTES_del_CSA
proposito: define_QUE_es_el_proyecto_o_tarea

5_preguntas_fijas:
  1_Que_es_esto:
    - definicion_clara_y_concisa
  2_Para_quien_es:
    - audiencia_objetivo
  3_Que_problema_resuelve:
    - pain_point_especifico
  4_Como_se_usa:
    - ejemplo_de_uso_real
  5_Que_NO_es:
    - exclusiones_explicitas

definition_score:
  cada_respuesta_se_puntua_0_a_100
  score_agregado_minimo: 95%_para_continuar
  si_lt_95%: bloquea_hasta_que_se_complete
```

### 7. Tabla Resumen CSA

```yaml
tabla_resumen:
  J1_Comprension: [objetivo, 5_fases]
  J2_Cobertura: [requisitos, 5_fases]
  J3_Consistencia: [logica, 5_fases]
  J4_Exactitud: [tecnico, 5_fases]
  J5_Arquitectura: [diseno, 5_fases]
  J6_Calidad: [codigo, 5_fases]
  J7_Investigacion: [evidencia, 5_fases]
  J8_Optimizacion: [performance, 5_fases]
  J9_Seguridad: [riesgos, 5_fases]
  J10_Calidad_Final: [UX, 5_fases]

total: 10_x_5_eq_50_auditorias_por_ciclo
```

### 8. Integración con MAXBRY

```
INPUT → SID(5_preguntas) → Score_ge_95% → PRODUCCION
   → CSA(10_jueces_x_5_fases) → Veto? → Escalar_MAX_o_Aprobado → Output
   → Publicacion → Monitoreo_post_publicacion
```

---
