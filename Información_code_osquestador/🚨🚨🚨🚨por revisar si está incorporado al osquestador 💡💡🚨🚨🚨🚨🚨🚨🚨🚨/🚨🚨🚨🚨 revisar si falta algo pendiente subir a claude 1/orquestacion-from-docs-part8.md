# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 8)

> **Continuación de las 5 pasadas**: Contiene PATCH V2-V4, 01-constitucion, csa-completo, y archivos restantes.


## PATCH-AUDITORIA-GAPS-V2 (98beb746): 13 Gaps Nuevos (2da Pasada)

### GAP #21 — Declaración de Apertura Obligatoria

```yaml
antes_de_cada_salida_escribir_EXACTAMENTE:
  > system_prompt_mythos_ejecutado
  > input_block: ACTIVO
  > goals: 5_primary_secondary_success_failure_restriction
  > pasos: 12
  > checkpoint: listo
  > recovery_json: listo
  > refutacion: pendiente
  > validacion: pendiente

si_NO_se_puede_escribir_esto_a_NO_se_genera_respuesta
```

### GAP #22 — 3 Revisiones del Input (Antes de Procesar)

```yaml
REVISION_1_Comprension:
  - que_pidio_exactamente
  - cual_es_el_objetivo_principal
  - cual_es_el_output_esperado

REVISION_2_Restricciones:
  - que_restricciones_hay
  - que_NO_se_puede_hacer
  - que_formato_se_espera

REVISION_3_Riesgos:
  - que_puede_salir_mal
  - que_informacion_falta
  - que_asumi_sin_verificar

si_alguna_revisin_falla:
  - pedir_aclaracion_ANTES_de_procesar
  - NO_inventar
  - NO_asumir
```

### GAP #23 — Checkpoint JSON Estructura Específica

```json
{
  "checkpoint_id": "uuid",
  "task_id": "uuid",
  "timestamp": "iso8601",
  "paso_actual": "1_a_12",
  "input_literal": "string_EXACTO_no_modificado",
  "goals_locked": true,
  "resultados_parciales": {
    "paso_1": "string",
    "paso_2": "string"
  },
  "validation_passed": true,
  "violations": []
}
```

### GAP #24 — Recovery JSON Estructura Específica

```json
{
  "recovery_id": "uuid",
  "task_id": "uuid",
  "failed_at_paso": "1_a_12",
  "failed_at_checkpoint": "uuid_del_ultimo_valido",
  "error": "string",
  "input_literal": "string_para_retomar_desde_literal"
}
```

### GAP #25 — Input Engine 11 Componentes (Detalle Completo)

```yaml
1_Canonical_Input_Graph_CIG:
  cada_frase_genera_12_tipos_de_nodos:
    objetivos_restricciones_requisitos_suposiciones_datos_recursos_dependencias_prioridades_riesgos_entregables_criterios_de_aceptacion_preguntas_abiertas
  cada_nodo: ID_unico_N51_tipo_texto_original_referencia_exacta_estado_prioridad_dependencias

2_Atomic_Requirement_Extraction:
  NO_parrafos_REQUISITOS_ATOMICOS
  REQ_001_a_REQ_127_plus
  cada_requisito_tiene_vida_propia

3_Dependency_Graph:
  REQ_8_a_REQ_15_a_REQ_44_a_REQ_93
  si_falla_REQ_8_a_automaticamente_se_invalidan_los_dependientes

4_Decision_Graph:
  cada_decision_importante_es_un_nodo_independiente
  elegir_Base_de_Datos_a_PostgreSQL_o_MySQL_o_SQLite_o_MongoDB
  el_sistema_NUNCA_olvida_por_que_eligio_una_opcion

5_Memory_Index:
  TODO_queda_indexado_NO_se_resume
  Objetivo_a_Nodo_8_a_Prompt_original_a_Linea_exacta_a_Mensaje_original

6_Plan_Compiler:
  NO_divide_texto_divide_NODOS
  127_requisitos_a_36_grupos_a_198_tareas_a_634_subtareas
  cada_uno_mantiene_referencias_al_grafo

7_Task_DNA_15_campos:
  ID_objetivo_entradas_salidas_dependencias_restricciones_skills_agentes_prioridad_riesgos_pruebas_estado_contexto_referencias_fuente_original
  ningun_agente_recibe_instrucciones_ambiguas

8_Context_Loader:
  un_agente_NUNCA_recibe_todo_el_proyecto
  solo_recibe: la_subtarea_dependencias_restricciones_relacionadas_contexto_relevante_referencias_al_Input_Graph

9_Completeness_Engine:
  antes_de_dividir_el_trabajo:
    todos_los_requisitos_tienen_dueno
    todos_tienen_prioridad
    todos_tienen_dependencias
    todos_tienen_criterio_de_aceptacion
    todos_tienen_contexto_suficiente
  si_alguno_falla_a_NO_planifica

10_Coverage_Matrix_PIEZA_MAS_IMPORTANTE:
  matriz: Requisito_o_Tarea_o_Agente_o_Estado
  REQ_1_a_TASK_4_a_Backend_a_✔
  REQ_2_a_TASK_9_a_Seg_a_✔
  REQ_3_a_TASK_18_a_Invest_a_✔
  si_existe_un_requisito_sin_tarea_asignada_a_el_sistema_lo_detecta

11_Reverse_Traceability:
  al_finalizar_el_proyecto:
    Frase_1_a_TASK_12_TASK_47_TASK_81_a_Resultado_Validado
  hace_esto_con_ABSOLUTAMENTE_todas_las_frases_del_usuario
  si_alguna_frase_no_puede_trazarse_a_RECHAZO
```

### GAP #26 — 17 Mejoras al Input Engine

```yaml
1_Intent_Graph: objetivo_principal_secundarios_implicitos_futuros_opcionales_asignar_prioridades
2_Constraint_Engine: cada_restriccion_recibe_nivel_obligatoria_preferida_opcional
3_Anti_Ambiguity_Engine: >
  detecta_rapido_seguro_grande_barato_simple_mejor
  las_convierte_en_valores_medibles
4_Hidden_Requirement_Detector: busca_requisitos_NO_escritos
5_Contradiction_Engine_clasificado: logica_temporal_tecnica_arquitectonica_legal_coste_rendimiento
6_Assumption_Registry: toda_suposicion_queda_registrada_suposicion_motivo_confianza_impacto_quien_la_hizo
7_Confidence_Engine: cada_requisito_recibe_nivel_de_confianza_98%_83%_51%_27%
8_Multi_Interpretation_Engine: NO_genera_una_interpretacion_genera_VARIAS_A_B_C_D
9_Scope_Boundary_Detector: define_que_esta_DENTRO_y_FUERA_del_alcance
10_Completeness_Score: calcula_informacion_suficiente_riesgo_de_alucinacion_informacion_faltante_requisitos_definidos_contradicciones
11_Context_Partition: divide_el_contexto_negocio_codigo_arquitectura_seguridad_ux_infraestructura_documentacion
12_Traceability_ID: cada_frase_del_usuario_obtiene_un_identificador_unico
13_Hallucination_Risk_Analyzer: estima_que_partes_tienen_mayor_riesgo
14_Requirement_Normalizer: normaliza_el_lenguaje_haz_una_aplicacion_a_Frontend_Backend_etc
15_Impact_Analyzer: antes_de_modificar_cualquier_requisito_calcula_que_tareas_decisiones_y_agentes_se_veran_afectados
16_Informacion_Inmutable: DOS_versiones_del_contexto_prompt_original_solo_lectura_modelo_estructurado
17_Registro_de_Decisiones: cada_decision_guarda_alternativas_criterios_evidencias_agente_responsable_fecha_nivel_de_confianza
```

### GAP #27 — Output Engine 13 Componentes (Detalle)

```yaml
1_Output_Planner: calcula_salida_estimada_15_paginas_28000_palabras_120_archivos_35_modulos_6_diagramas_3_tablas
2_Output_Graph_grafo_no_texto: proyecto_arquitectura_backend_frontend_base_de_datos_api_tests_documentacion_deployment_manual_cada_nodo_es_independiente
3_Smart_Chunking_por_significado: NO_divide_por_cantidad_de_texto_divide_por_SIGNIFICADO
4_Dynamic_Output_Engine: >
  estima_tokens_memoria_tiempo_coste_tamano_final
  calcula_1_3_15_52_100_partes
  NO_existe_limite_fijo
5_Manifest_indice_antes_de_entregar: el_usuario_SIEMPRE_sabe_que_recibira
6_Output_Registry: cada_salida_tiene_id_version_dependencias_estado_checksum_autor_fecha_destino
7_Output_Router_menu_de_formatos: >
  markdown_artifact_html_pdf_docx_pptx_json_yaml_csv_zip_git_db_drive_mcp_api_otro
8_Destination_Engine_adaptadores: markdown_artifact_git_drive_notion_mcp_api_database_s3_cloud_adapter
9_Streaming_Output: NO_espera_a_terminar_todo_modulo_1_a_validado_a_entregado_modulo_2_a_validado_a_entregado
10_Output_Validator: completa_dependencias_rotas_referencia_a_modulo_inexistente_enlaces_funcionan_cumple_formato
11_Multi_Target_Delivery_parcialmente_documentado
12_pendiente
13_pendiente
```

### GAP #28 — P35/P36/P37 Mejoras 100X

```yaml
P35_Auto_Mejora_Continua:
  ANTES: MAXBRY_se_audita_cada_7_dias
  AHORA: MAXBRY_EVOLUCIONA_cada_hora_con_aprobacion_selectiva
  - auto_mejora_CADA_HORA_en_cambios_pequenos
  - auto_rollback_si_la_mejora_empeora_metricas
  - sandbox_de_experimentacion
  - si_mejora_funciona_24h_a_promueve_a_produccion
  - notifica_a_MAX_solo_si_es_significativa
  - aprende_que_tipo_de_mejoras_acepta_MAX
  archivo: g5_o_auto_evolucion_o

P36_Experimentacion_A_o_B_Bayesian:
  ANTES: A_o_B_o_C_para_elegir_mejor_opcion
  AHORA: BAYESIAN_MULTI_ARMED_BANDIT
  - algoritmo_multi_armed_bandit
  - explota_lo_conocido_ mas_ explora_nuevas
  - predice_ganador_con_95%_confianza
  - se_auto_ajusta
  - 10+_variaciones_en_paralelo
  - resultados_en_Knowledge_Graph
  archivo: g5_o_experimentacion_o_v2_o

P37_Pricing_Tiempo_Real:
  ANTES: dashboard_con_costos
  AHORA: ECONOMIA_PREDICTIVA_con_auto_optimizacion
  - predice_costo_con_30_dias_de_anticipacion
  - auto_cambia_a_modelos_mas_baratos_cuando_conviene
  - marketplace_de_modelos
  - NEGOCIACION_si_el_costo_sube
  - reporte_mensual_automatico
  - alertas_inteligentes
  archivo: g5_o_economia_o_v2_o
```

### GAP #29 — EVENTS.json Types Específicos

```yaml
event_id_o_type_o_timestamp_o_source_o_task_id_o_payload

types:
  TASK_CREATED
  TASK_STARTED
  TASK_DONE
  TASK_FAILED
  CONSENSUS_REQUIRED
  BUILD_FINISHED
  GROUP_HEARTBEAT
  RETRY_TRIGGERED
  TIMEOUT_REACHED
  CANCELLED
```

### GAP #30 — Agentes Universales (N API Keys Dinámica)

```yaml
REGLA: el_orquestador_debe_poder_usar_1_a_50_API_keys
cada_agente_toma_una_API_key_disponible
si_50_agentes_necesitan_LLM_via_API_a_toman_de_las_disponibles
NO_usa_una_sola_API_key

EJEMPLO:
  Claude_Code_normalmente_usa_1_API_key
  el_orquestador: divide_en_N_agentes_con_N_API_keys
  si_hay_50_keys_a_50_agentes_en_paralelo
  si_hay_1_key_a_1_agente_secuencial
```

### GAP #31 — Decisiones Tomadas (Confirmadas por MAX)

```yaml
✅ G5_eq_MISMO_GRUPO_eq_consenso_ mas_ orquestador_NO_son_dos_grupos_separados
✅ G6_BUILD_eliminado_era_invento
✅ G7_o_G8_tambien_eran_confusion_a_ahora_es_solo_G6_ASISTENTES
✅ Total: 6_grupos_G1_G2_G3_G4_G5_G6
✅ MiniMax_M3_eq_LIDER_de_G5_como_SKYNER_via_1_NVIDIA_NIM
✅ M2.7_SOLO_crea_G5_inicialmente_despues_G5_programa_todo
✅ Orquestador_MANEJA_al_agente_NO_al_reves
✅ DSL_o_DAG_NUNCA_prompt_libre
✅ Input_sagrado_no_se_modifica_no_se_resume_no_se_parafrasea
✅ Todo_se_reporta_a_M3_chat_ mas_ a_MAX_por_Telegram
✅ 1_HF_Space_por_grupo_own_token_aislada
✅ ZeroGPU_se_comparte_no_nos_afecta_porque_usamos_API
✅ GitHub_como_fuente_de_verdad_de_todo
✅ SandboxDB_por_grupo_para_estado_temporal
✅ RAM_16GB_por_HF
✅ Q5_o_Q4_segun_peso_del_modelo
✅ bartowski_recomendado_para_GGUF_mejor_quantizacion_community
✅ Unsloth_Dynamic_2.0_como_segunda_opcion
✅ context7_para_contexto_extendido_10M_tokens
```

### GAP #32 — Ubicaciones Proyectos Iniciales

```yaml
projects_separacion_por_proyecto:
  nct_fase0_o
  interfaz_fusionada_o
  crazy_wall_o
```

### GAP #33 — Kimi K2.7-Code Especificaciones Detalladas

```yaml
vendor: Moonshot_AI_Kimi_K2.7_Code
HF: moonshotai_o_Kimi_K2.7_Code
funcion: generacion_de_codigo_de_produccion
provider_OpenCLAW: si_config_nativo
compatible_Claude_Code: si_via_API_Moonshot
fortalezas: tool_calling_avanzado_agentic_coding_codigo_coherente
cuando_se_elige: TM01_TM02_cuando_el_lenguaje_es_Python_o_TS_o_Rust_o_Go
temperatura: 0.2_default
output: patch_unified_diff_ mas_ JSON_metadata
endpoint: Groq_provider_o_NVIDIA_NIM
```


## PATCH-AUDITORIA-GAPS-V3 (854d3ba4): 17 Gaps Nuevos (3ra Pasada)

### GAP #34 — Estructura Completa MAXBRY (336 Archivos)

```yaml
00_raiz_o: 6_archivos_metadata
01_bootstrap_o: 5_archivos_instalacion
02_core_o: 7_archivos_nucleo
03_input_engine_o: 28_archivos_P28_P29_ mas_ 17_mejoras
04_sid_o: 10_archivos_P27
05_sub_orquestadores_o: 26_archivos_P19_20_SO_ mas_ SO-ARQ
06_csa_o: 17_archivos_P26
07_output_engine_o: 25_archivos_P31_P34
08_ovfs_o: 6_archivos_P32
09_agentes_o: 40_archivos_colmenas
10_invariantes_o: 3_archivos_P30
11_datasets_o: 60_archivos
12_adapters_o: 60_archivos
13_seguridad_o: 7_archivos_P6
14_canales_o: 6_archivos
15_modelos_o: 9_archivos
16_scheduler_o: 4_archivos
17_storage_o: 5_archivos
18_estado_o: 4_archivos
19_testing_o: 4_archivos
20_logs_o: 4_archivos
total: 336_archivos_Python_~40.800_lineas_~53.400_lineas_totales
```

### GAP #35 — Cálculos de Recursos

```yaml
lineas_de_codigo_estimadas:
  Python_puro: ~40.800
  YAML_configs: ~2.500
  JSON_schemas: ~1.800
  Shell_scripts: ~300
  Markdown_docs: ~8.000
  total: ~53.400_lineas

tamano_en_disco:
  codigo_fuente: ~2.0_MB
  configs_o_schemas: ~0.3_MB
  docs: ~12_MB
  total: ~14_MB

memoria_en_ejecucion:
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
  7_HF_Spaces_x_16GB_eq_112GB
  usados: ~13.5GB
  margen_libre: 87%
```

### GAP #36 — OOS 14 Componentes (Diferente de Output Engine)

```yaml
1_Output_Planner
2_Output_Compiler_AST_de_salida
3_Output_Graph
4_Semantic_Chunk_Engine_no_corta_por_tokens_calcula_dependencias
5_Adaptive_Chunk_Size_tamano_dinamico
6_Predictive_Output_Planner_calcula_salida_estimada_antes
7_Auto_Format_Negotiation_recomienda_formato_inteligente
8_Intelligent_Packaging_paquetes_por_tipo
9_Multi_Delivery_Pipeline_15_plus_destinos_en_paralelo
10_Intelligent_Compression_optimiza_antes_de_comprimir
11_Smart_Version_Control_v1.0.0_v1.0.1
12_Incremental_Publishing
13_Intelligent_Resume
14_Output_Verification
mas_Universal_Output_Model
mas_Delivery_Policy_Engine
```

### GAP #37 — 15+ Destinos OOS

```yaml
la_misma_salida_puede_ir_SIMULTANEAMENTE_a:
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

TODO_EN_PARALELO
```

### GAP #38 — 20 Sub-Orquestadores (SO-01 a SO-20)

```yaml
SO-01_analista_objetivos
SO-02_organizador
SO-03_planificador
SO-04_validador_plan
SO-05_investigador
SO-06_replanificador
SO-07_mapa_mental
SO-08_clasificador
SO-09_divisor_tareas
SO-10_disenador_pasos
SO-11_constructor_bucles
SO-12_gestor_dependencias
SO-13_calculador_recursos
SO-14_asignador
SO-15_creador_loops
SO-16_validador_calidad
SO-17_verificador_cruzado
SO-18_auditor_trazabilidad
SO-19_reportador
SO-20_memoria_sistema
mas_SO_ARQ_arquitectura
```

### GAP #39 — 6 Colmenas

```yaml
09_agentes_o:
  colmena_programacion_o: sa_diseno_ma_01_30_etc
  colmena_investigacion_o: github_hf_web_youtube_mcp
  colmena_memoria_o: chromadb_bge_embedder_trazabilidad
  colmena_seguridad_o: sheriff_sentinel_auditor
  colmena_documentacion_o: escritor_generador_validador
  colmena_testing_o: runner_coverage_benchmark
```

### GAP #41 — Kimi K2 Detalles Específicos

```yaml
vendor: Moonshot_AI
HF: moonshotai_o_Kimi_K2.7_Code
GitHub: github_com_o_MoonshotAI_o_Kimi_K2.5
funcion: agente_de_code_del_orquestador
provider: OpenCLAW_nativo_ mas_ compatible_Claude_Code_via_API
endpoint: Groq_provider_o_NVIDIA_NIM
arquitectura: MoE_1T_params_32B_activados
versiones: K2.5_K2.7_Code_K2_Thinking
```

### GAP #42 — 10 Instrucciones Pendientes de MAX

```yaml
1_confirmacion_sobre_archivo_docx_con_lo_aprobado
2_activar_M2.7_para_crear_G5_con_HF_ mas_ Telegram_ mas_ MCP_server
3_nombre_exacto_de_HTM_y_YUAN_no_encontrados_en_HF
4_autorizacion_para_finalizar_documentos_y_proceder_con_instalacion
5_decision_sobre_visibilidad_de_repos_publico_o_privado
6_decision_sobre_comunicacion_Telegram_bot_token
7_datos_de_acceso_a_GitHub_GH_OWNER_PAT
8_datos_de_acceso_a_Hugging_Face_HF_USERNAME_token
9_16_API_keys_confirmadas_con_labels
10_Turso_DB_credentials_opcional
```

### GAP #43 — Herramientas Aprobadas

```yaml
HuggingFace:
  ZeroGPU: infraestructura_COMPARTIDA_no_nos_afecta_usamos_API
  CPU_Basic_Spaces: 16GB_RAM_cada_uno_aislados_por_contenedor
  GitHub_PAT: conexion_via_git_con_GH_PAT_como_secret
  Cada_HF_Space: propia_URL_fija_en_produccion

MCP_Model_Context_Protocol:
  github_com_o_modelcontextprotocol_o_servers: 2700+_servers
  github_com_o_shreyaskarnik_o_huggingface_mcp_server
  G8_MCP_server_expone_tools
  G7_son_MCP_clients

RAG_tools:
  context7: contexto_10M_tokens_real
  ChromaDB: embeddings
  bge_small_en_v1.5: modelo_embeddings_24MB_HF
  LightRAG: github_com_o_HKUDS_o_LightRAG
  Haystack: github_com_o_deepset_ai_o_haystack

Adaptadores_cuantizacion:
  Unsloth_Dynamic_2.0: github_com_o_unslothai_o_unsloth
  bartowski: github_com_o_bartowski_mejor_quantizacion_community
  GGUF_format
  llama_cpp_python: github_com_o_abetlen_o_llama_cpp_python

Frameworks:
  pydantic: validacion_schemas
  PEFT: adapters
  LoRA: fine_tuning
```

### GAP #44 — Merge Rule con Snapshot_Branch

```yaml
auto_merge_when: G4_AUDIT_approved_AND_G5_CONSENSO_approved_AND_tests_pass
if_any_fails: PR_open_ mas_ M3_chat_notified_ mas_ MAX_decides
snapshot_branch: snapshot_vX.Y.Z
versioning: semver
```

### GAP #45 — Repair v1.0 (5 Pasos Detallados)

```yaml
Paso_1: Retry_simple_3_intentos
Paso_2: Context_Compression_L1_o_L2
Paso_3: Fallback_Model_o_Agent
Paso_4: Restore_Checkpoint
Paso_5: Escalate_Coordinator_decide
```

### GAP #46 — Patch Log Histórico

```yaml
v1.0.0_a_v1.0.5: secciones_1_a_30_originales
v1.0.6_2026-06-28: patch_031_a_9_modelos_GGUF_detallados
v1.0.7_2026-06-28: patch_032_a_10_agentes_del_consejo
v1.0.8_2026-06-28: patch_033_a_sistema_de_Skills
v1.0.9_2026-06-28: patch_034_a_Kimi_K2_como_agente
v1.0.10_2026-06-28: patch_035_a_investigacion_multi_fuente
```

### GAP #47 — Adaptive Chunk Size (OOS)

```yaml
el_tamano_de_cada_parte_cambia_DINAMICAMENTE

ejemplo:
  Parte_1: 400_lineas
  Parte_2: 1500_lineas
  Parte_3: 650_lineas

NO_existe_un_tamano_fijo
```

### GAP #48 — Auto Format Negotiation (OOS)

```yaml
NO_pregunta_simplemente_¿Markdown_o_ZIP

pregunta_INTELIGENTEMENTE:

he_detectado_que_la_salida_contiene:
  ✔_codigo
  ✔_diagramas
  ✔_documentacion
  ✔_configuracion
  ✔_tests

recomendacion:
  Artifact_ mas_ ZIP_ mas_ Repositorio_Git

deseas_usar_esta_configuracion:
  SI_o_MODIFICAR
```

### GAP #49 — Agentes Colmena Investigación (5 Específicos)

```yaml
09_agentes_o_colmena_investigacion_o:
  github_search_py: REST_ mas_ GraphQL
  hf_search_py: HF_API
  web_search_py: DuckDuckGo_ mas_ scraper
  youtube_search_py: YouTube_Data_API_v3_transcripts
  mcp_search_py: MCP_servers
```

### GAP #50 — Investigación Multi-Fuente Detalles

```yaml
agente_github_py:
  API: github_com_REST_ mas_ GraphQL
  busquedas: repos_codigo_issues_stars_commits

agente_huggingface_py:
  API: huggingface_co_REST
  busquedas: modelos_datasets_spaces

agente_web_py:
  API: duckduckgo_ mas_ custom_scraper
  busquedas: docs_oficiales_awesome_lists_papers_blogs

agente_youtube_py_NUEVO:
  API: youtube_data_api_v3
  busquedas: videos_transcripts_canales_verificados
  uso: tutoriales_explicaciones_visuales

agente_mcp_py:
  API: github_com_o_modelcontextprotocol_o_servers
  busquedas: servers_tools_registries
```

### Total Acumulado de Gaps

```yaml
1er_patch_GAPS_V1: 20_gaps
2do_patch_GAPS_V2: 13_gaps_nuevos_total_33
3er_patch_GAPS_V3: 17_gaps_nuevos_total_50
```


## PATCH-AUDITORIA-GAPS-V4 (f638ecfb): 18 Gaps Nuevos (4ta Pasada)

### GAP #51 — M2.7 Flujo Simplificado (5 Pasos)

```yaml
PASO_1_RECIBIR:
  leer_TASK_json
  verificar_schema
  output: task_recibida_ok

PASO_2_VERIFICAR:
  chequear_dependencias
  chequear_keys_necesarias
  chequear_permisos
  output: dependencias_ok

PASO_3_EJECUTAR:
  ejecutar_la_tarea
  output: ejecucion_resultado

PASO_4_VALIDAR:
  tests_pasan
  output_compilado
  secrets_detectados_no
  output: validacion_ok

PASO_5_REPORTAR:
  escribir_resultado_a_STATE_json
  escribir_a_HISTORY_json_acumulativo
  notificar_a_M3_chat
  output: reporte_enviado

si_falla_en_cualquier_paso:
  - escribir_RECOVERY_JSON
  - rollback_si_es_necesario
  - escalar_a_M3_chat_si_retry_gt_2
```

### GAP #52 — División de Tareas Grandes (Regla)

```yaml
REGLA: si_tarea_gt_5_subtareas_a_dividir_en_bloques
cada_bloque_eq_checkpoint_separado
cada_bloque_eq_recovery_independiente

TAREA_GRANDE_a_dividirse_en:
  BLOQUE_1_a_checkpoint_1_a_output_1
  BLOQUE_2_a_checkpoint_2_a_output_2_depende_de_output_1
  BLOQUE_3_a_checkpoint_3_a_output_3_depende_de_output_2

CADA_BLOQUE:
  - input_literal_preservado
  - 5_GOALS_fijados
  - 12_PASOS_ejecutados
  - CHECKPOINT_JSON_escrito
  - REFUTACION_pasada
  - VALIDACION_pasada
  - OUTPUT_entregado
  - RECOVERY_JSON_listo_si_falla
```

### GAP #53 — 10 Módulos de MAXBRY

```yaml
M1_Bootstrap: instalador_actualizador_lanzador
M2_Nucleo_del_Orquestador: planificador_scheduler_motor_decisiones
M3_Gestor_de_Memoria: ChromaDB_bge_small_embeddings
M4_Scheduler: Dramatiq_Redis_colas_paralelas
M5_Gestor_de_Agentes: registry_colmena_distribucion
M6_Gestor_de_Skills: catalogo_generador_versionado
M7_Gestor_de_Modelos_de_IA: API_keys_profiles_circuit_breaker
M8_Sistema_de_Seguridad: cifrado_auth_licencias
M9_Sistema_de_Actualizacion: versiones_diffs_rollback
M10_Sistema_de_Monitorizacion: logs_metricas_alertas_dashboards

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
Capa_1_Cifrado_de_Comunicacion: HTTPS_o_TLS
Capa_2_Autenticacion: API_keys_con_tokens_1h_OAuth2_opcional
Capa_3_Firmas_Digitales: cada_solicitud_firmada_criptograficamente
Capa_4_Rate_Limiting: 100_req_por_min_1000_req_por_h
Capa_5_Licencias: cada_instalacion_unica_servidor_valida_cada_arranque
Capa_6_Respuestas_Minimas: API_solo_devuelve_lo_necesario_nunca_paths_internos
```

### GAP #55 — Núcleo Vía API (Cliente Ligero vs Servidor)

```yaml
Usuario
   ↓
Cliente_M3_local_5_MB  # lo_que_el_usuario_tiene
   ↓
API_del_Orquestador_servidor  # lo_que_NO_se_descarga
   ├── Planificador
   ├── Memoria_global
   ├── Scheduler
   ├── Motor_de_decisiones
   ├── Agentes
   └── Modelos_IA

ventajas:
  ✅_Usuario_NO_recibe_codigo_del_nucleo
  ✅_NO_puede_copiar_planificador
  ✅_Actualizaciones_sin_que_usuario_reinstale
  ✅_Puedes_revocar_accesos
  ✅_El_codigo_importante_NUNCA_sale_del_servidor
```

### GAP #56 — P8 Bootstrap de Instalación Autónoma

```yaml
responsabilidades:
  1_detectar_OS_Linux_o_Mac_o_Windows
  2_detectar_arquitectura_x86_64_o_arm64
  3_verificar_recursos_CPU_RAM_disco_red
  4_comprobar_dependencias_necesarias
  5_instalar_automaticamente
  6_crear_estructura_de_directorios
  7_inicializar_base_de_datos
  8_generar_configuraciones_iniciales
  9_generar_claves_criptograficas
  10_descargar_solo_componentes_necesarios
  11_iniciar_el_orquestador

caracteristicas:
  tamano_maximo_5_MB
  NO_contiene_logica_del_orquestador
  solo_es_instalador_actualizador_lanzador
  descarga_componentes_bajo_demanda
  verificacion_criptografica_de_integridad
```

### GAP #57 — 8 Principios Rectores del Sistema Razonamiento

```yaml
1_INPUT_SAGRADO: el_input_NUNCA_se_modifica_resume_parafrasea_reinterpreta
2_DSL_o_DAG_NUNCA_PROMPT_LIBRE: salida_siempre_JSON_estructurado
3_DETERMINISMO: mismo_input_ mas_ config_ mas_ LLM_eq_misma_forma_de_razonamiento
4_UNIVERSALIDAD: cualquier_LLM_puede_usarlo
5_EXTERNALIDAD: vive_en_o_reasoning_system_o_no_en_o_orquestador_o
6_EDITABILIDAD_POR_ARCHIVOS: cambiar_goal_o_step_eq_editar_archivo_no_codigo
7_AUDITABILIDAD: cada_ejecucion_produce_log_auditable
8_AISLAMIENTO: el_sistema_no_contamina_al_orquestador_ni_al_LLM
```

### GAP #58 — INPUT_BLOCK Estructura JSON

```json
{
  "input_block": {
    "raw": "input_EXACTO_del_usuario_sin_tocar",
    "received_at": "timestamp_ISO_8601",
    "source": "nombre_del_llamador",
    "checks": {
      "preserve_verbatim": true,
      "no_summarize": true,
      "no_paraphrase": true,
      "no_modify": true
    },
    "status": "ACCEPTED_o_REJECTED"
  }
}
```

### GAP #59 — 7 Prohibiciones Explícitas INPUT_BLOCK

```yaml
1_resumir_el_input: el_usuario_pidio_algo_especifico_no_un_resumen
2_parafrasear_el_input: cambia_el_matiz_semantico
3_mejorar_la_redaccion_del_input: el_usuario_escribio_como_quiso
4_agregar_contexto_que_no_estaba: contamina_la_intencion_original
5_quitar_partes_irrelevantes: el_LLM_decidira_que_es_relevante
6_traducir_el_input: cambia_el_idioma_cambia_la_semantica
7_reordenar_las_ideas_del_input: la_estructura_sintactica_porta_significado
```

### GAP #60 — 12 Pasos Standard con Prompts Específicos

```yaml
01_literal_read_INPUT_BLOCK_SAGRADO:
  prompt: "INSTRUCCION_SAGRADA_NO_INTERPRETAR_NO_RESUMIR_NO_MODIFICAR"
  output: {input_accepted: true, raw_acknowledged: string}
  conexion: entrada_a_02_think_si_falla_a_REJECTED

02_think_analisis:
  prompt: "Considerando_los_goals_y_el_input_verbatim_que_estas_entendiendo"
  output: {thinking: [obs1, obs2, obs3]}

03_plan_planificacion:
  prompt: "Genera_un_plan_de_3_a_7_pasos_para_cumplir_goal_primary"
  output: {plan: [{step: 1, action, expected_output}]}

04_decompose_descomposicion:
  prompt: "Para_cada_paso_del_plan_identifica_las_subtareas_atomicas"
  output: {decomposition: [{plan_step: 1, atomic_tasks: list}]}

05_hypotheses_generacion_hipotesis:
  prompt: "Para_cada_atomic_task_propon_2_a_4_hipotesis_de_solucion_alternativas"
  output: {hypotheses: [{task_id, alternatives: list}]}

06_swarm_ejecucion_paralela_conceptual:
  prompt: "Para_cada_hipotesis_evalua_esfuerzo_riesgo_alineamiento"
  output: {swarm_results: [{h_id, effort: low_o_med_o_high}]}

07_critic_critica_adversarial:
  prompt: "Como_critico_que_falla_en_cada_hipotesis"
  output: {critiques: [{h_id, weakness, severity}]}

08_simulate_simulacion:
  prompt: "Simula_paso_a_paso_la_ejecucion_de_la_hipotesis_ganadora"
  output: {simulation: [{phase, result, issues: list}]}

09_validate_validacion:
  prompt: "La_simulacion_cumple_goal_success_Respeta_goal_restriction"
  output: {validation: {meets_success, respects_restriction}}

10_consensus_consenso_interno:
  prompt: "Considerando_thinker_critic_simulator_validator_cual_es_la_decision"
  output: {consensus: {decision, confidence: 0_a_1, votes: list}}

11_report_reporte:
  prompt: "Genera_el_reporte_final_en_formato_DSL"
  output: {report: DSL_final}

12_audit_auditoria:
  prompt: "Auditoria_se_respeto_input_sagrado_se_ejecutaron_los_12_pasos"
  output: {audit: {input_respected, verdict: PASS_o_FAIL, notes}}
```

### GAP #61 — M3 en Cada Salida (Formato)

```yaml
ANTES_DE_CADA_SALIDA_mostrar:
  > system_prompt_mythos_ejecutado
  > goals: list
  > pasos_completados: 1_a_12
  > checkpoints: list_uuid
  > refutacion: ok_o_fail
  > validacion: ok_o_fail

DESPUES_DE_CADA_SALIDA_mostrar:
  > self_audit: ok_o_fail
  > input_preserved: true
  > output_validated: true
```

### GAP #62 — M2.7 en Cada Ejecución (Log)

```yaml
log_en_STATE_json:
  > system_prompt_mythos: executed
  > paso_actual: 1_a_5
  > checkpoint_id: uuid
```

### GAP #63 — Refutación (5 Preguntas Obligatorias)

```yaml
PREGUNTAS_OBLIGATORIAS_antes_de_output_final:
  - que_asumi_sin_verificar
  - que_puede_romper_esta_salida
  - que_restriccion_viole
  - que_informacion_invent
  - que_dependencias_no_cheque

si_alguna_respuesta_es_problematica:
  - volver_al_paso_1
  - NO_presentar_output_refutado
```

### GAP #64 — Estructura Sistema Razonamiento

```yaml
o_reasoning_system_o:
  README_md
  config_json
  goals_o: 5_goals_standard
  goals_turbo_o: 7_goals_extra
  steps_o: 12_pasos_standard
  steps_turbo_o: 33_pasos_extra
  prompts_o:
    standard_dsl_json
    turbo_dsl_json
    input_block_rule_json
  runner_py
  loader_py
  api_py
```

### GAP #65 — Validación Obligatoria (Checks)

```yaml
CHECKS_OBLIGATORIOS_antes_de_output_final:
  - input_preservado_verbatim
  - output_no_resume_el_input
  - output_no_parafrasea_el_input
  - output_responde_a_los_5_GOALS
  - output_cumple_restriccion_innegociable
  - checkpoints_escritos
  - refutacion_pasada
  - consensus_aplicado_si_aplica

si_alguna_falla:
  - REJECTED
  - recovery
```

### GAP #66 — Protocolo de Recuperación

```yaml
SI_TAREA_FALLA:
  1_escribir_RECOVERY_JSON_inmediatamente
  2_identificar_ultimo_CHECKPOINT_valido
  3_si_retry_count_lt_2_a_rollback_al_checkpoint_retry
  4_si_retry_count_ge_2_a_escalar_a_M3_chat
  5_M3_chat_decide_mas_retries_redesign_o_cancelar

NUNCA:
  - inventar_output_cuando_falla
  - saltarse_pasos_para_avanzar
  - ignorar_violaciones
  - borrar_checkpoints_validos
```

### GAP #67 — Uso de Memoria M3 y M2.7

```yaml
M3_chat_MEMORIA:
  - memory_topic_append_despues_de_cada_sesion_importante
  - leer_memory_topic_read_al_inicio_de_cada_sesion_nueva
  - BORRADOR_LISTA_APROBADOS_md_eq_fuente_de_verdad_visible

M2.7_MEMORIA:
  - leer_BORRADOR_LISTA_APROBADOS_md_al_iniciar
  - STATE_json_eq_estado_actual
  - HISTORY_json_eq_historico_completo_nunca_borrar

BORRADOR_LISTA_APROBADOS_md:
  - se_actualiza_con_CADA_cambio_aprobado
  - se_actualiza_con_CADA_nueva_propuesta
  - se_actualiza_con_CADA_tarea_completada
  - es_la_fuente_de_verdad_para_todo
```

### GAP #68 — Integración System Prompt Mythos + Razonamiento Externo

```yaml
DIFERENCIA:
  system_prompt_mythos_a_reglas_y_proceso_visible
  o_reasoning_system_o_a_libreria_Python_con_funciones

AMBOS_DEBEN_USARSE:
  M3_lee_system_prompt_mythos_al_inicio
  M3_usa_reasoning_system_reason_para_tareas_complejas
  M2.7_lee_system_prompt_mythos_al_inicio
  M2.7_usa_reasoning_system_reason_si_necesita_razonar

INTEGRACION:
  system_prompt_mythos_eq_capa_de_comportamiento
  reasoning_system_eq_capa_de_ejecucion
  juntos_eq_sistema_completo
```

### Total Acumulado Final

```yaml
1er_patch_V1: 20_gaps
2do_patch_V2: 13_gaps
3er_patch_V3: 17_gaps
4to_patch_V4: 18_gaps
total: 68_gaps_identificados
```

