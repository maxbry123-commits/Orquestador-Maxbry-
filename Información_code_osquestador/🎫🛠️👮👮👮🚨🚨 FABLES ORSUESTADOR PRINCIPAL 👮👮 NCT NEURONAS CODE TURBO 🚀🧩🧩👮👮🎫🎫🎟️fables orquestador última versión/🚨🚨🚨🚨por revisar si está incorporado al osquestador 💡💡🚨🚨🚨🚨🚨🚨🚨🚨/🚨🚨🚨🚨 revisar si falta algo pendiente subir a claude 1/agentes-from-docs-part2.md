# AGENTES — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 2)

> **Continuación del Parte 1** (`agentes-from-docs-part1.md`).
>
> **Reglas aplicadas**:
> - Solo contenido citado literalmente.
> - Separado del orquestador.
> - Sin repetir entre partes.


## DOC MASTER 21: SUBSISTEMAS DETALLADOS (Agentes + Razonamiento)

### System Prompt Mythos (15 Secciones)

```yaml
mythos_15_secciones:
  S1_Identidad: "MAXBRY_SUPER_TEAM_es_el_orquestador_universal_distribuido_para_IA"
  S2_Mision: "Coordinar_agentes_herramientas_proyectos_y_objetivos_para_MAX"
  S3_Valores:
    - determinismo
    - trazabilidad
    - resiliencia
    - auto_mejora
    - costo_$0
  S4_Principios: 39_principios_de_la_Constitucion
  S5_Arquitectura_capas:
    - USUARIO
    - MAXBRY
    - Control_Layer
    - Workflow_Layer
    - Memory_Layer
    - Tool_Layer
    - LLM_Layer
  S6_Capacidades:
    - 2000+_agentes
    - 1000+_tareas
    - multi_modelo
    - auto_evolucion
  S7_Limites:
    - costo_$0
    - HF_free_tier
    - 16GB_RAM_por_Space
  S8_Interaccion:
    - Telegram
    - API_REST
    - Dashboard
    - CLI
  S9_Outputs:
    - 23_destinos
    - adaptive_format
    - multi_target
  S10_Validacion:
    - 5_GOALS_+_12_PASOS
    - confidence_scoring_ge_95%
    - CSA_audit
  S11_Seguridad:
    - secretos_encriptados
    - audit_log
    - OWASP_compliance
  S12_Operacion:
    - 90%_codigo_/_10%_LLM
    - multi_modelo
    - 3_perfiles_API
  S13_Aprendizaje:
    - meta_learning
    - self_improving
    - counterfactual_reasoning
  S14_Reporte:
    - estado
    - metricas
    - alertas
  S15_Cierre: "Reporto_a_MAX_Escala_a_MAX_si_es_critico"
```

### Skills System — 13 Criterios Individuales

```yaml
C1_Nombre_Claro:
  - identifica_la_skill
  - patron: snake_case
  - ejemplo: code_generator
C2_Descripcion_Concisa:
  - 1_a_2_oraciones
  - QUE_hace_no_COMO
C3_Categoria_Valida:
  - una_de_A_a_N_BIS
C4_Inputs_Tipados:
  - schema_JSON
  - required_vs_optional
C5_Outputs_Tipados:
  - schema_JSON
  - siempre_definido
C6_Tiempo_Medio:
  - estimacion_realista
  - p50_p95_p99
C7_Recursos:
  - CPU_o_RAM_o_disk
  - modelo_si_requiere_LLM
C8_Dependencias:
  - skills_que_requiere
  - versiones
C9_Tests:
  - minimo_3_unit_tests
  - coverage_ge_80%
C10_Documentacion:
  - README_md
  - ejemplos
C11_Ejemplos:
  - minimo_2_ejemplos
  - real_world_use_cases
C12_Version_Semver:
  - MAJOR.MINOR.PATCH
  - ejemplo: 1.2.3
C13_Mantenedor:
  - owner_asignado
  - contacto
```

### Skills Debate — 4 Especialistas

```yaml
especialistas_4:
  Arquitecto: ¿es_coherente_con_la_arquitectura?
  Implementador: ¿es_implementable_con_recursos_actuales?
  Tester: ¿es_testeable_como_se_prueba?
  Critico: ¿vale_la_pena_el_costo_o_beneficio?

voto:
  4_a_0: skill_excelente
  3_a_1: skill_aprobada_con_notas
  2_a_2: escala_a_MAX
  1_a_3: skill_rechazada
  0_a_4: skill_prohibida
```

### Multi-Source Investigation (5 Agentes Investigadores)

```yaml
4.1_GitHub_Researcher:
  agent: github_researcher
  sources: [github.com_repos, github_API]
  queries: ["awesome-{topic}", "{topic}_stars:>1000"]
  outputs: [repos.json, stars_issues_PRs]

4.2_HuggingFace_Researcher:
  agent: hf_researcher
  sources: [huggingface.co_models_datasets_spaces]
  queries: ["{topic}_model_dataset_space"]
  outputs: [models.json, downloads_likes]

4.3_Web_Researcher:
  agent: web_researcher
  sources: [Wikipedia, MDN, OWASP, documentacion_oficial, arXiv]
  queries: ["{topic}_best_practices", "{topic}_documentation"]
  outputs: [pages.jsonl]

4.4_YouTube_Researcher:
  agent: youtube_researcher
  sources: [YouTube_tecnicos]
  queries: ["{topic}_tutorial", "{topic}_conference_talk"]
  outputs: [videos.json, transcripts]

4.5_MCP_Researcher:
  agent: mcp_researcher
  sources: [mcp_servers, smithery, Composio]
  queries: ["{topic}_mcp_server"]
  outputs: [mcp_servers.json]
```

### Universal Plug v1.5 (Detalles del Conector Universal)

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
  capabilities:
    - code_generation
    - web_search
    - rag_query
    - file_read
    - file_write
    - api_call
    - test_run
    - deploy
  nexus: "punto_central_de_conexion_entre_modulos"
  nexus_funciones:
    - descubre_modulos_disponibles
    - registra_capabilities
    - enruta_requests
    - monitorea_health
```

### M3 + Kimi División

```yaml
M3_jefe:
  funcion: arquitecto
  trabaja_con: MAX_directamente
  decide: QUE_hacer
  NO_ejecuta: codigo_directo
  entrega: plan_+_validacion

Kimi_K2.7_Code_empleado:
  funcion: implementador
  trabaja_para: M3
  decide: COMO_hacerlo
  SI_ejecuta: codigo
  entrega: implementacion_+_tests

flujo:
  MAX → M3_jefe → M3_planifica → Kimi_implementa → Kimi_reporta → M3_valida → M3_presenta → MAX_aprueba
```

### Fusión Kimi + MiniMax

```yaml
fusion_protocol:
  input: spec_de_M3
  output: implementacion_de_Kimi
  handoff:
    M3 → Kimi: plan_+_acceptance_criteria
    Kimi → M3: implementacion_+_tests
  validation: M3_valida_contra_acceptance_criteria
  feedback: M3 → Kimi_correcciones_si_necesario

garantias:
  M3_nunca_ejecuta_codigo_directo
  Kimi_nunca_habla_con_MAX
  handoff_siempre_con_schemas
```

### NCT Coordinator — 13 Archivos (Detalle)

```yaml
nct_coordinator_py: coordinador_principal_inicializa_sistema
nct_modes_py: selector_de_modo_Manual/Semi/Continuo
nct_flows_py: definicion_de_flujos_continuos
nct_phases_py: implementacion_de_F0_a_F9
nct_inputs_py: recepcion_y_procesamiento_de_inputs
nct_outputs_py: generacion_y_entrega_de_outputs
nct_state_py: estado_global_state_json
nct_memory_py: sistema_de_memoria_4_tier
nct_skills_py: integracion_con_BIS
nct_agents_py: gestion_de_agentes
nct_audit_py: integracion_con_CSA
nct_metrics_py: recoleccion_de_metricas
nct_delivery_py: multi_target_delivery
```

---

## DOC MASTER 11: RAZONAMIENTO + MYTHOS (40 Pasos + FABLES)

### EURS — External Universal Reasoning System

```yaml
EURS_STANDARD_5_+_12:
  5_Niveles:
    1_Literal_Read: lee_literal_el_input
    2_Intent_Detection: detecta_intencion
    3_Context_Loading: carga_contexto
    4_Hypothesis_Generation: genera_hipotesis
    5_Validation: valida_respuesta
  12_Pasos:
    1_parse_input
    2_validate_schema
    3_extract_intent
    4_load_context
    5_generate_hypotheses
    6_test_hypotheses
    7_synthesize_answer
    8_validate_answer
    9_check_consistency
    10_format_output
    11_add_citations
    12_emit_output

EURS_TURBO_12_+_45:
  12_Niveles:
    1_Literal_Read
    2_Intent_Detection
    3_Context_Loading
    4_Hypothesis_Generation
    5_Validation
    6_Synthesis
    7_Critique
    8_Refinement
    9_Cross_validation
    10_Meta_validation
    11_Final_Check
    12_Delivery
  45_Pasos: detalle_para_razonamiento_profundo
```

### MYTHOS — System Prompt Avanzado (40 Pasos)

```yaml
mythos_40_pasos:
  Categoria_A_Inicializacion_5_pasos:
    1: inicializar_contexto
    2: cargar_system_prompt
    3: validar_entrada
    4: verificar_permisos
    5: iniciar_sesion
  
  Categoria_B_Analisis_5_pasos:
    6: parsear_input
    7: clasificar_intencion
    8: extraer_entidades
    9: construir_contexto
    10: detectar_ambiguedades
  
  Categoria_C_Investigacion_5_pasos:
    11: buscar_en_web
    12: buscar_en_github
    13: buscar_en_RAG
    14: buscar_en_memoria
    15: sintetizar_hallazgos
  
  Categoria_D_Planificacion_5_pasos:
    16: generar_plan
    17: validar_plan
    18: optimizar_plan
    19: asignar_recursos
    20: programar_tareas
  
  Categoria_E_Ejecucion_5_pasos:
    21: iniciar_ejecucion
    22: monitorear_progreso
    23: manejar_errores
    24: aplicar_reparaciones
    25: validar_resultados
  
  Categoria_F_Verificacion_5_pasos:
    26: verificacion_tecnica
    27: verificacion_de_negocio
    28: verificacion_de_seguridad
    29: verificacion_de_calidad
    30: verificacion_de_compliance
  
  Categoria_G_Entrega_5_pasos:
    31: formatear_output
    32: validar_formato
    33: seleccionar_destino
    34: enviar
    35: confirmar_recepcion
  
  Categoria_H_Cierre_5_pasos:
    36: recolectar_feedback
    37: actualizar_memoria
    38: aprender_lecciones
    39: cerrar_sesion
    40: emitir_reporte
```

### Arquitectura de Control Alto

```
MYTHOS(control) → LLM(razonamiento) → OUTPUT
regla: "MYTHOS_controla_LLM_razona"
```

### FABLES — Framework for Adversarial Battle of Logical Evaluation and Synthesis

```yaml
FABLES_5_fases:
  FASE_1_Inicializacion:
    - recibe_pregunta
    - carga_contexto
    - define_criterios_de_exito
  
  FASE_2_Generacion_Adversarial:
    - genera_N_soluciones
    - cada_solucion_intenta_superar_a_las_anteriores
    - adversarial_search
  
  FASE_3_Critica_Multi_Agente:
    - 5_agentes_critican
    - cada_uno_busca_problemas_diferentes
    - compilan_issues
  
  FASE_4_Refinamiento_Iterativo:
    - soluciona_issues
    - regenera
    - repite_hasta_score_ge_95%
  
  FASE_5_Sintesis_Final:
    - combina_mejores_partes
    - valida_output_completo
    - emite_respuesta
```

### CHEF FINAL (4 Pasos)

```yaml
paso_1_Revision_Final: revisa_el_output_completo
paso_2_Validacion_Cruzada: cruza_con_todos_los_criterios
paso_3_Refinamiento_Cosmetico: mejoras_finales_de_estilo
paso_4_Emision: emite_output_final_con_firma
```

### Micro-Ciclo (7 Pasos)

```yaml
1_receive: recibe_input
2_decompose: descompone
3_distribute: distribuye_a_agentes
4_execute: ejecuta
5_aggregate: agrega_resultados
6_verify: verifica
7_emit: emite_output
```

### DRE Pipeline (9 Pasos)

```yaml
DRE: Deep_Reasoning_Engine
1_parse: parse
2_analyze: analyze
3_hypothesize: hypothesize
4_research: research
5_synthesize: synthesize
6_critique: critique
7_refine: refine
8_validate: validate
9_emit: emit
```

---

## DOC MASTER 18: PATCHES EXTRAS + HALLAZGOS RESEARCH (170 Patches)

### Resumen Patches por Categoría

```yaml
total: 170_patches_documentados

por_categoria:
  ORQUESTADOR: 51
  INPUT_V4.0: 9
  LOOP_V6.0: 15
  OUTPUT_V6.1: 9
  OUTPUT_V6.1_gobernanza: 16
  PROPUESTAS_INPUT/LOOP: 10
  INFRA: 8
  EXTRAS: 37
  PARCHES_v14_a_v17: 4+
```

### Patches Output V6.1 (9 Propuestas M3)

```yaml
PATCH-OUTPUT-V61-01_pre_mortem: pre_mortem_analysis_antes_output_simula_que_podria_fallar_reduce_fallos_70%
PATCH-OUTPUT-V61-02_auto_rollback: rollback_automatico_si_degrada_restauracion_al_ultimo_bueno
PATCH-OUTPUT-V61-03_meta_learning: aprende_de_outputs_pasados_mejora_continua
PATCH-OUTPUT-V61-04_personalization: adapta_a_preferencias_de_MAX_formato_personalizado
PATCH-OUTPUT-V61-05_multi_stakeholder: versiones_para_diferentes_audiencias_mismo_contenido_diferentes_vistas
PATCH-OUTPUT-V61-06_causal_tracing: cadena_causal_completa_trazabilidad_causa_efecto
PATCH-OUTPUT-V61-07_marketplace: outputs_compartibles_como_skills_marketplace_interno
PATCH-OUTPUT-V61-08_self_improving: cada_output_mejora_al_siguiente_similar_optimizacion_continua
PATCH-OUTPUT-V61-09_production_monitoring: monitorea_outputs_en_produccion_detecta_degradacion
RECHAZADO_PATCH-OUTPUT-V61-10_sandbox: output_sandbox_NO_se_implementa
```

### Patches Output V6.1 Gobernanza (16 Capas A-P)

```yaml
A_Pre_Output_Audit
B_Confidence_Check
C_Compliance_Check
D_Security_Scan
E_Consistency_Verification
F_Provenance_Embedding
G_Version_Locking
H_Multi_Channel_Validation
I_Rollback_Preparation
J_Output_Score_Calculation
K_Adaptive_Format_Selection
L_Delivery_Path_Selection
M_Recipient_Verification
N_Delivery_Confirmation
O_Post_Delivery_Monitoring
P_Feedback_Loop_Trigger
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

### Patches LOOP V6.0 (15 Propuestas)

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

### Patches EXTRAS (37) — Agentes

```yaml
8.1_CSA_fases_10:
  - CSA-F1_a_CSA-F10  # uno_por_juez
  - detalle_de_5_fases_por_juez

8.2_Skills_criterios_13:
  - criterios_BIS_detallados
  - debate_4_especialistas
  - v1_v2_v3_skills

8.3_Investigacion_agentes_5:
  - GitHub_researcher
  - HF_researcher
  - Web_researcher
  - YouTube_researcher
  - MCP_researcher

8.4_Hallazgos_research_8:
  - DeerFlow_2.0
  - LiteLLM
  - Microsoft_Agent_Framework
  - AgentOrchestra
  - OpenCLAW
  - Hermes_Agent
  - LangGraph
  - CrewAI

8.5_Delivery_destinos_1:
  - 23_destinos_multi_target
```

### 8 Hallazgos Research (Aprobados)

```yaml
1_DeerFlow_2.0_ByteDance:
  stars: 46K
  patron: Super_Agent_Harness_investigacion_multi_agente
2_LiteLLM:
  descripcion: unifica_100+_LLMs_en_1_API_open_source
```

---

## DOC MASTER 20: VALIDACIÓN CRUZADA FINAL

### Propósito

```yaml
proposito: validacion_cruzada_final_de_los_19_Master_Documentos_previos
garantiza:
  - toda_la_informacion_del_orquestador_esta_cubierta
  - no_hay_contradicciones_entre_docs
  - las_referencias_cruzadas_son_validas
  - el_DSL_DAG_de_validacion_pasa
```

### Inventario 20 Master Documentos

```yaml
20_Master_Documentos_creados:
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
  20-validacion-cruzada-final: este_doc
total: ~120914_bytes_en_20_documentos
```

### DSL DAG de Validación

```yaml
dag_validation_nodos_y_dependencias:
  MASTER-01: []  # sin_deps
  MASTER-02: [MASTER-01]
  MASTER-03: [MASTER-01]
  MASTER-04: [MASTER-01, MASTER-03]
  MASTER-05: [MASTER-01, MASTER-03]
  MASTER-06: [MASTER-01, MASTER-02]
  MASTER-07: [MASTER-01, MASTER-02]
  MASTER-08: [MASTER-02, MASTER-03]
  MASTER-09: [MASTER-02, MASTER-03, MASTER-04]
  MASTER-10: [MASTER-02, MASTER-17]
  MASTER-11: [MASTER-01, MASTER-02]
  MASTER-12: [MASTER-02, MASTER-08]
  MASTER-13: [MASTER-01, MASTER-02]
  MASTER-14: [MASTER-02, MASTER-08]
  MASTER-15: [MASTER-01, MASTER-03]
  MASTER-16: [MASTER-01, MASTER-15]
  MASTER-17: [MASTER-01, MASTER-10]
  MASTER-18: [MASTER-01, MASTER-02]
  MASTER-19: [MASTER-01, MASTER-17]
  MASTER-20: [MASTER-01..MASTER-19]

validation_rules:
  no_cycles: true
  all_deps_resolve: true
  all_docs_complete: true
  size_limits_respected: true
  no_contradictions: true
```

### Cross-References (Mapa)

```yaml
MASTER-01_a_otros:
  MASTER-02_Estructura
  MASTER-03_Constitucion
  MASTER-13_Arquitectura_NCT
  MASTER-15_Reglas
MASTER-02_a_otros:
  MASTER-06_Input_Engine
  MASTER-07_Output_Engine
  MASTER-08_Loop
  MASTER-09_Agentes
  MASTER-14_MiMo_LOP_v200
MASTER-03_a_otros:
  MASTER-04_CSA
  MASTER-05_SID_BIS
  MASTER-15_Reglas
MASTER-04_a_otros:
  MASTER-09_Agentes
MASTER-05_a_otros:
  MASTER-09_Agentes
MASTER-06_a_otros:
  MASTER-12_Pipeline
MASTER-07_a_otros:
  MASTER-08_Loop
MASTER-08_a_otros:
  MASTER-12_Pipeline
MASTER-09_a_otros:
  MASTER-18_Patches
MASTER-10_a_otros:
  MASTER-17_Configuraciones
MASTER-11_a_otros:
  MASTER-12_Pipeline
MASTER-12_a_otros:
  MASTER-13_Arquitectura
MASTER-13_a_otros:
  MASTER-19_Pre_flight
MASTER-14_a_otros:
  MASTER-18_Patches
MASTER-15_a_otros:
  MASTER-16_DSL
MASTER-16_a_otros:
  MASTER-20_Validacion
MASTER-17_a_otros:
  MASTER-19_Pre_flight
MASTER-18_a_otros:
  MASTER-19_Pre_flight
MASTER-19_a_otros:
  MASTER-20_Validacion
```

---

## DOC 8: MODELOS GGUF Y APIs (Agentes G6)

### 9 Modelos GGUF Confirmados

```yaml
modelos_GGUF_confirmados:
  1_HRM_Text-1B: [Sapient_Inc, 1B, 0.6GB_GGUF, arxiv_2504.12345, sapientinc/HRM-Text-1B]
  2_Qwen2.5_Coder-1.5B: [Alibaba, 1.5B, code_specialist]
  3_Granite_4.1-3B: [IBM, 3B, general]
  4_Granite_3.2-2B: [IBM, 2B, bajo_consumo]
  5_LFM2.5-1.2B_Thinking: [Liquid, 1.2B, modo_thinking_razonamiento_explicito]
  6_Gemma_4-E4B: [Google, MoE_4B, backup_alto_rendimiento]
  7_Gemma_4-E2B: [Google, MoE_2B, bajo_consumo_MoE]
  8_GPT_OSS-20B: [OpenAI, 21B_total_3.6B_active, MXFP4, openai/gpt-oss-20b]
  9_Nemotron_3_Nano-4B: [NVIDIA, 4B, integracion_NVIDIA_NIM]
```

### Uso Recomendado por Modelo

```yaml
HRM_Text-1B:
  - razonamiento_profundo
  - analisis_complejo
  - tareas_que_requieren_pensar

Qwen2.5_Coder-1.5B:
  - generacion_de_codigo
  - code_review
  - refactoring
  - debugging

Granite_4.1-3B:
  - tareas_generales
  - balance_rendimiento_costo
  - produccion

Granite_3.2-2B:
  - bajo_consumo
  - tareas_simples
  - inferencia_rapida

LFM2.5-1.2B_Thinking:
  - razonamiento_explicito
  - mostrar_pasos_de_pensamiento
  - decisiones_que_requieren_transparencia

Gemma_4-E4B:
  - tareas_multimodales
  - razonamiento_general
  - backup_de_alto_rendimiento

Gemma_4-E2B:
  - bajo_consumo
  - tareas_MoE_ligeras
  - inferencia_eficiente

GPT_OSS-20B_MXFP4:
  - tareas_criticas
  - maxima_calidad
  - cuando_se_necesita_el_mejor_modelo_disponible

Nemotron_3_Nano-4B:
  - integracion_NVIDIA_NIM
  - backup_de_NVIDIA
  - inferencia_optimizada
```

### 16 API Keys (3 Providers)

```yaml
4_NVIDIA_NIM_keys:
  KEY-1: principal
  KEY-2: backup_#1
  KEY-3: backup_#2
  KEY-4: emergencias

6_Cerebras_keys:
  KEY-1_a_KEY-6: cerebras_inference

6_Groq_keys:
  KEY-1_a_KEY-6: groq_LPU_inference
```

### Uso de APIs por Perfil

```yaml
CONSERVADOR:
  - NVIDIA_NIM: 4_keys_alta_calidad
  - Cerebras: 1_a_2_keys_verificacion
  - Groq: 1_a_2_keys_emergencias

EQUILIBRADO_DEFAULT:
  - NVIDIA_NIM: 1_key
  - Cerebras: 6_keys_mayor_uso
  - Groq: 4_a_6_keys_complemento

AGRESIVO:
  - NVIDIA_NIM: 1_key_solo_critico
  - Cerebras: todas_las_keys
  - Groq: todas_las_keys
```

### Modelo Router Inteligente

```yaml
criterios_de_seleccion:
  1_tipo_de_tarea: codigo_a_Qwen_Coder, razonamiento_a_HRM-Text, general_a_Granite
  2_costo: minimizar_tokens_consumidos
  3_latencia: Cerebras_gt_Groq_gt_NVIDIA_gt_Local
  4_calidad_requerida: definida_por_Definition_Score
  5_disponibilidad: rate_limits_caidas
  6_perfil_activo: Conservador_o_Equilibrado_o_Agresivo
```

### SKYNER (NVIDIA NIM) — Modelo Principal del Orquestador

```yaml
SKYNER:
  via: NVIDIA_NIM
  rol: modelo_principal_del_orquestador
  cargo: lider_del_grupo_G5

router_signals: [cost, latency, capability, license, mcp_native]
reglas:
  - if_task_type_eq_code_generation_and_budget_eq_low:
      backend: opencode
      model: deepseek-coder
  - if_task_type_eq_long_horizon_and_horizon_h_ge_24:
      backend: mimo_code
      model: mimo-v2.5
  - if_task_type_eq_research_rag:
      backend: openhands
      model: qwen3-coder
  - if_task_type_eq_ui_design:
      backend: open_design
      model: sonnet-4.6
  - default:
      backend: goose
      model: claude-sonnet-4.6
```

### MiMo Code

```yaml
origen: Xiaomi_MiMo_Team
base: OpenCode
license: MIT
first_release: 2026-06-11_V0.1.0
stack: [Bun, TypeScript, Effect, SolidJS, Tauri]
3_pilares:
  compute: [Max_Mode, Goal_Stop, Dynamic_Workflow]
  memory: [Checkpoint/Rebuild, Writer_subagent, 4_tier_memory]
  evolution: [Dream, Distill, project_memory]
benchmark_vs_Claude_Code:
  SWE_Bench_Pro_V2: +5%
  Terminal_Bench_2: +5%
  ultra_long_200_plus_steps: beats_Claude_Code
compatible_models: [MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM]
```

### GPT-OSS-20B

```yaml
params: 21B_total_/_3.6B_active_MoE
quantization: MXFP4
HF: openai/gpt-oss-20b
```

### HRM-Text-1B

```yaml
autor: Sapient_Inc
tamano: 0.6GB_GGUF
paper: arxiv_2504.12345
HF: sapientinc/HRM-Text-1B
especialidad: razonamiento
```

---
