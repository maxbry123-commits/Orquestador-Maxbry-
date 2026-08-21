# ESQUELETO MAESTRO — ORQUESTADOR MAXBRY
# 3 PIPELINES · 322 FICHAS (202 ✚nuevas) · 3 CATEGORÍAS · NIVELES COGNITIVOS 0-5
# Base: diagrama 64 nodos NCT v0.4 + 29 MASTER docs + G2 v2.5 + Salidas 1-6 ya codificadas.
# Toda ficha usa Enchufe Universal v2.0. ✚ = proceso nuevo (no estaba en tus documentos).

---

## 1. ARQUITECTURA DE 3 CATEGORÍAS

```
USUARIO ──► SELECTOR DE PERFIL (nivel 0-5) ──► PLANNER_OFFLINE ──► sequence.json congelado
                                                     ▲                    │
                              ACELERADORES COGNITIVOS (A)                 ▼
                              modifican CUÁNTO razona el planner    RUNTIME DETERMINISTA 🚂
                                                                          │
        ┌────────────────────────────┬────────────────────────────┬──────┘
        ▼                            ▼                            ▼
  PIPELINE E (ENTRADA)      PIPELINE P (PROCESADOR)       PIPELINE S (SALIDA)
   72 fichas                 135 fichas                    55 fichas
        │                            │                            │
        └───────────── SERVICIOS TRANSVERSALES (T) 45 fichas ─────┘
              memoria · audit · recovery · red · métricas · dream/distill
```

**Niveles cognitivos (fichas A):** n0 Rápido · n1 Estándar · n2 Profundo · n3 Mythos · n4 Mythos Turbo · n5 Investigación Extrema. Cada nivel multiplica iteraciones/simulaciones/críticas/muestras según el campo `perfiles` del enchufe v2.0. El runtime NUNCA cambia: cambia el plan que el planner compila.

**Los 7 puntos 🔍 de re-verificación de memoria** (campo `repite_en`): INPUT · CONTEXT_LOADER · EXEC_STATE · ARTIFACT_ENGINE · MEMORY · MASTER_JSON · CONTEXT_MANAGER. **Patrón 🛂 por capa:** Sentinel (detecta) + Judge (valida con evidencia) + Sheriff (aplica política) — se instancia al cierre de cada segmento.

---

## 2. PIPELINE E — ENTRADA (72 fichas)

**Microdiagrama:** `Captura ➜ Congelar ➜ Filtrar/Seguridad ➜ Analizar semilla ➜ Clasificar ➜ Goal ➜ Compilar requirements ➜ 🛂`

### E1 · CAPTURA Y NORMALIZACIÓN
| ID | Ficha | Qué hace |
|---|---|---|
| E-001 | input_listener | Escucha multi-canal (telegram/drive/mcp/api/kanboard/webhook) |
| E-002 | normalizer_frozen | Normaliza a doc único y congela FROZEN v1.0 |
| E-003 | ack_engine | Confirma recepción al canal de origen |
| E-004 | hash_engine | SHA256 del documento completo |
| E-005 | inventory_validator | ¿Ya procesado? → skip (inventory.json) |
| E-006 ✚ | encoding_sanitizer | Limpia unicode/caracteres invisibles (bug iPad) y BOM |
| E-007 ✚ | idioma_detector | Detecta idioma y normaliza a canónico |
| E-008 ✚ | adjuntos_extractor | zip/pdf/imagen → fichas hijas con parent_id |
| E-009 ✚ | multi_doc_merger | Varios uploads → corpus único con índice |
| E-010 ✚ | delta_detector | Doc nuevo vs versión previa → procesa solo difs |
| E-011 ✚ | size_gate | Rechaza/trocea inputs que exceden límites |
| E-012 ✚ | timezone_normalizer | Fechas/horas a ISO-8601 UTC |
| E-013 ✚ | unit_normalizer | Unidades y monedas a canónico |
| E-014 ✚ | voice_to_task | Audio → transcripción → task normalizada |
| E-015 ✚ | screenshot_to_spec | Captura de pantalla → OCR+layout → spec |
| E-016 ✚ | email_parser | Email → task (asunto=goal, cuerpo=contexto) |

### E2 · SEGURIDAD Y FILTROS
| ID | Ficha | Qué hace |
|---|---|---|
| E-017 | filtros_a1 | Captura multimodal estructurada (20 checks) |
| E-018 | filtros_a2_axiomas | AX01-08 bloqueantes — 1 hit = REJECTED |
| E-019 | filtros_a3_normalizadores | Normalización semántica |
| E-020 | filtros_a4_descomponedores | Descomposición en unidades atómicas |
| E-021 | filtros_a5_coherencia | Coherencia interna del input |
| E-022 ✚ | prompt_injection_scanner | Patrones+heurística de inyección → cuarentena |
| E-023 ✚ | pii_scrubber | Datos sensibles fuera antes de tocar LLM |
| E-024 ✚ | secret_detector_input | API keys/passwords en el input → bloquea y avisa |
| E-025 ✚ | canal_firmante | Verifica firma/identidad del canal origen |
| E-026 ✚ | cuarentena_manager | Aísla inputs sospechosos hasta decisión Director |
| E-027 ✚ | rate_limiter_entrada | Límite por canal/tenant con jitter |
| E-028 ✚ | malware_flagger | Marca adjuntos con patrones peligrosos (solo flag) |
| E-029 | wake_word_engine | SYS_HALT/EXECUTE/PLAN/VERIFY/YIELD/RESUME |
| E-030 | ocr_baidu | OCR Baidu + fallback tesseract (solo P1) |
| E-031 ✚ | traductor_entrada | Traduce a idioma canónico preservando términos técnicos |
| E-032 | input_sentinel_🛂 | Integridad+completitud antes de avanzar |

### E3 · ANÁLISIS SEMILLA Y HUELLAS
| ID | Ficha | Qué hace |
|---|---|---|
| E-033 | fingerprint_l1_lexico | SHA256 texto exacto (copia) |
| E-034 | fingerprint_l2_semantico | Embedding hash (reformulación) |
| E-035 | fingerprint_l3_estructural | Árbol de secciones (reorganización) |
| E-036 | fingerprint_l4_entidades | Set canónico nombres/fechas/cifras |
| E-037 | fingerprint_l5_dependencias | Grafo de relaciones entre docs |
| E-038 | seed_s1_indexer | Indexa repo+state+RAG → seed_index.sqlite |
| E-039 | seed_s2_summarizer | Resumen por artefacto → seed_summary.json |
| E-040 | seed_s3_gap_detector | Huecos de info → seed_gaps.json |
| E-041 | seed_s4_questions | Propone preguntas → seed_questions.json |
| E-042 | seed_s5_enricher | Enriquece + evidence sufficiency (0.35/0.25/0.20/0.20) |
| E-043 ✚ | dedup_semantico_stream | Deduplicación semántica ventana 24h |
| E-044 ✚ | ner_glosario | Extrae entidades/glosario del proyecto |
| E-045 ✚ | similarity_past_tasks | Busca tareas pasadas similares → reutiliza planes |
| E-046 ✚ | contexto_historico_fetcher | Trae chats/tareas/decisiones relacionadas |
| E-047 ✚ | input_schema_inferencer | Infiere JSON schema del payload automáticamente |
| E-048 ✚ | ambiguedad_scorer | Score de ambigüedad → dispara preguntas |

### E4 · CLASIFICACIÓN, GOAL Y COMPILACIÓN
| ID | Ficha | Qué hace |
|---|---|---|
| E-049 | push_ping_30 | Tabla completa 30 clasificaciones — no avanza incompleta |
| E-050 | sid_5_preguntas | SID: qué/por qué/cómo/cuándo/con qué |
| E-051 | bis_14_categorias | Clasificación BIS del input |
| E-052 | dre_estimator | Complejidad (deps×2)+steps+ambiguo+riesgo |
| E-053 | goal_lock_builder | Congela GoalLock (goal/DoD/not_in_scope/hash) |
| E-054 | dod_generator | Genera DoD con Juez si falta — jamás inventa solo |
| E-055 | task_graph_builder | Subtareas + depends_on |
| E-056 | requirements_compiler | requirements.json → PLANNER_OFFLINE |
| E-057 | director_question_queue | Cola de preguntas al Director (paralela) |
| E-058 | batch_segmentador | 1-1000 tareas → batches 20 + overlap 5 + prioridad |
| E-059 | ficha_identidad_gen | uuid + historial + failure_registry vacío |
| E-060 | simulador_plan_x5 | Simula plan 5 veces: colisiones de estado → corrige |
| E-061 ✚ | preflight_presupuesto | Estima costo/tokens ANTES de aceptar la tarea |
| E-062 ✚ | credentials_checker | Detecta keys/permisos faltantes antes de arrancar |
| E-063 ✚ | api_quota_checker | Verifica cuotas de providers disponibles |
| E-064 ✚ | deadline_negotiator | Propone deadline realista según DRE+cola |
| E-065 ✚ | task_splitter_repo | Divide tarea por repo afectado |
| E-066 ✚ | tenant_namespacer | Etiqueta multi-proyecto (JARVIS/SPACEin/NCT) |
| E-067 ✚ | urgencia_classifier | critical/normal/background automático |
| E-068 ✚ | environment_snapshotter | Foto del entorno (versiones/deps) al aceptar |
| E-069 ✚ | form_generator_dod | Formulario dinámico al Director si falta DoD |
| E-070 ✚ | input_replay_cache | Re-procesar sin re-costo (cache por doc_id) |
| E-071 ✚ | dependency_prechecker | Fichas/servicios requeridos ¿existen y COMMITTED? |
| E-072 | goal_verifier_🛂 | Gate final E: GoalLock+requirements completos |

---

## 3. PIPELINE P — PROCESADOR DE TAREAS (135 fichas)

**Microdiagrama:** `Perfil ➜ Investigar ➜ Razonar(offline) ➜ Consenso ➜ Compilar plan ➜ 🚂 Ejecutar DAG ➜ Expertos/MA ➜ Verificar ➜ 🛂`

### P1 · PLANIFICACIÓN OFFLINE (F-1/F0)
| ID | Ficha | Qué hace |
|---|---|---|
| P-001 | planner_offline | Compila requirements→sequence.json+fallback.json (ya) |
| P-002 | perfil_selector | Lee nivel 0-5 → parametriza TODO el plan |
| P-003 | estrategia_l0_l4 | secuencial/DAG/fractal(≤5) según DRE |
| P-004 | goal_engine_25 | 25 ítems de goal management |
| P-005 | goal_queue_engine | Cola priorizada de goals |
| P-006 | schema_engine | Schemas de cada paso del plan |
| P-007 | lifecycle_engine | Estados F-1..F5 del ciclo de vida |
| P-008 | session_manager | Sesiones y continuidad |
| P-009 | discovery_engine_r1r5 | Ciclos investigación (2-5 rondas, ≥0.85 stop) |
| P-010 | hipotesis_generator | ≥3 hipótesis: estándar/extrema/inversa/híbrida/emergente |
| P-011 | research_layer | RAG+web+GitHub+papers OBLIGATORIO pre-decisión |
| P-012 | knowledge_pack_assembler | Empaqueta hallazgos para el plan |
| P-013 ✚ | plan_cache | requirements_hash → plan (reutiliza planes idénticos) |
| P-014 ✚ | plan_diff | Nuevo plan vs anterior → solo cambios al Director |
| P-015 ✚ | critical_path_analyzer | Camino crítico del DAG → prioriza |
| P-016 ✚ | parallel_group_optimizer | Re-balancea grupos paralelos por costo |
| P-017 ✚ | resource_forecaster | Predice tokens/tiempo/costo del plan por nivel |
| P-018 ✚ | curriculum_scheduler | Ordena tareas de simple→compleja cuando conviene |
| P-019 ✚ | plan_risk_scorer | Score de riesgo por paso → añade verificaciones |
| P-020 ✚ | alternative_plans_bc | Genera Plan B y C congelados junto al A |
| P-021 ✚ | context_window_packer | Empaqueta contexto óptimo por paso (sin overflow) |
| P-022 ✚ | fewshot_library | Biblioteca de ejemplos por tipo de paso |
| P-023 ✚ | prompt_compiler | Plantillas DSL → prompts sellados parseables |
| P-024 ✚ | negative_examples_injector | Inyecta ejemplos de lo que NO hacer |
| P-025 ✚ | template_rigido_enforcer | Plantilla rígida por tipo de salida |

### P2 · RAZONAMIENTO Y CONSENSO (offline, intensidad por nivel)
| ID | Ficha | Qué hace |
|---|---|---|
| P-026 | mythos_40_pasos | Perfil n3: PRELUDE+RRL+GOAL-STOP+CODA (40 pasos) |
| P-027 | max_mode | K muestras paralelas + majority + best-of-N |
| P-028 | reasoning_swarm | Paralelo técnico/usuario/seguridad |
| P-029 | critic_swarm | Crítica adversarial multi-perspectiva |
| P-030 | self_reflection | ¿Resuelvo el problema correcto? |
| P-031 | failure_analysis | Modos de fallo conocidos+desconocidos |
| P-032 | simulation_engine | Normal+edge+extremo antes de elegir |
| P-033 | edge_case_generator | Inputs vacíos/nulos/extremos |
| P-034 | consenso_5_agentes | Creative/Innovation/Critic/Selection/Architecture |
| P-035 | devil_agent | Ataca la ganadora antes de aprobar |
| P-036 | anti_groupthink | Todos iguales → re-gen con temp alta |
| P-037 | skyner_consenso | 17 modelos G7+G8, veto power (perfil n4-n5) |
| P-038 | csa_10_jueces | Consejo Supremo Auditoría: 5 fases + veto (offline) |
| P-039 | decision_fusion | Combina perspectivas → decisión única |
| P-040 | confidence_scoring | 0-100, umbral 70 |
| P-041 | solution_ranking | Tabla comparativa objetiva |
| P-042 | ensemble_fusion | Combina mejores elementos de varias soluciones |
| P-043 | goal_stop_check | ≥0.85 evidencia → stop investigación |
| P-044 ✚ | auto_consistencia_x5 | 3-5 corridas independientes → mayoría (tu método) |
| P-045 ✚ | self_refutacion | Pasada que intenta refutar la propia respuesta |
| P-046 ✚ | contraste_forzado | Obliga ángulos opuestos antes de fusionar |
| P-047 ✚ | panel_roles_opuestos | Panel con roles enfrentados (tu método) |
| P-048 ✚ | verificador_separado | Verificador ≠ generador SIEMPRE |
| P-049 ✚ | descomposicion_recursiva | Divide hasta unidad atómica verificable |
| P-050 ✚ | rubric_grader | Rúbrica numérica por criterio → score reproducible |

### P3 · EXPERTOS Y MÉTODO DE TRABAJO
| ID | Ficha | Qué hace |
|---|---|---|
| P-051 | expert_pool | 500 disponibles, activa por fase/nivel (ya) |
| P-052 | cognitive_engine | 1 motor + N YAML 0-LOC (ya) |
| P-053 | fusion_engine | Consolida con fórmula ponderada (ya) |
| P-054 | enjambre_executor | asyncio.gather con semáforo 25 (ya) |
| P-055 | expert_spawner_tdag | Crea experto ad-hoc si falta (draft) |
| P-056 | jueces_3_niveles | Local→Capa→Central (E296) |
| P-057 ✚ | expert_accuracy_decay | Accuracy decae con el tiempo → re-prueba |
| P-058 ✚ | expert_bootstrapper | Arranque en frío: calibra expertos nuevos |
| P-059 ✚ | knowledge_distiller | Destila lecciones → nuevos YAML de expertos |
| P-060 ✚ | panel_weights_tuner | Ajusta pesos de la fórmula por dominio |
| P-061 ✚ | expert_ab_selector | A/B testing offline entre configs de experto |
| P-062 ✚ | temperature_scheduler | Temperatura por paso según tipo de operación |
| P-063 ✚ | anti_echo_guard | Ventana anti-eco <30% (ya en motor, ficha propia) |
| P-064 ✚ | metodo_ok_recibido | FSM de tu método chat: OK→INVESTIGO→…→RECOMENDACIONES |
| P-065 ✚ | goal_look_paso0 | PASO 0 GOAL LOOK antes de toda cadena (tu constitución) |
| P-066 ✚ | contrato_de_borde | Declara límites/interfaces antes de ejecutar (tu método) |
| P-067 ✚ | verificar_encaje | Verifica coherencia + encaje al final (tu método) |
| P-068 ✚ | lista_tareas_funciones | Genera LISTA TAREAS + LISTA FUNCIONES estructuradas |
| P-069 ✚ | panel_300_expertos | Panel masivo por muestreo estratificado (n5) |
| P-070 ✚ | expert_conflict_court | Tribunal para contradicciones persistentes |

### P4 · EJECUCIÓN DETERMINISTA 🚂
| ID | Ficha | Qué hace |
|---|---|---|
| P-071 | graph_runtime_dag | Ejecuta sequence.json congelado (transductor, ya) |
| P-072 | dependency_resolver | Resuelve depends_on en runtime |
| P-073 | executor_lve | Loader/Verifier/Executor de fichas |
| P-074 | escritor | LLM_ESCRITOR bajo Juez (ya) |
| P-075 | runtime_bvw | Builder/Validator/Witness L1-L4 (ya) |
| P-076 | juez_pipeline_16 | P-DISCOVER→P13, anti-humo (ya) |
| P-077 | loop_engine_9fases | Cognitivo aislado, escala 20-1000 (ya) |
| P-078 | loops_infra_10 | Heartbeat/signals/DLQ/meta-loop (ya) |
| P-079 | handoff_builder | Sobre firmado orq→team (ya) |
| P-080 | team_core | Cerebro team ≤300 LOC (ya) |
| P-081 | ma_dispatcher | Despacha los 15+12 micro-agentes |
| P-082..P-093 | ma_codegen/lint/test/ragsearch/ragsynth/docwrite/archplan/verify3cap/repair5/resweb/resgh/emit | Los 12 MA del diagrama (spawn→run→emit→die ≤200 LOC) |
| P-094 | skill_manager | 3-10 skills por tarea + capability.json |
| P-095 | manifest_reader | Lee SOLO manifest.json, nunca código |
| P-096 | role_engine | Asigna rol por TM+DRE |
| P-097 | protocol_engine | Protocolos de comunicación entre nodos |
| P-098 | environment_manager | Entornos/sandboxes por paso |
| P-099 | llm_capsula | LLM provider-ciego vía Router (ya) |
| P-100 | subagent_manager | Ciclo de vida de subagentes |
| P-101 ✚ | worktree_sandbox | Git worktrees + Docker por tarea paralela |
| P-102 ✚ | speculative_prefetch | Precarga fichas COMMITTED (ETag) |
| P-103 ✚ | deadline_scheduler_edf | Earliest-deadline-first en colas |
| P-104 ✚ | backpressure_controller | Frena entrada si colas saturan |
| P-105 ✚ | retry_budget_global | Presupuesto global de reintentos por task |
| P-106 ✚ | priority_inversion_detector | Detecta bloqueos por prioridad invertida |
| P-107 ✚ | canary_executor | Ejecuta plan en muestra pequeña primero |
| P-108 ✚ | chaos_injector_staging | Inyección controlada de fallos (solo staging) |
| P-109 ✚ | idempotency_keys | Claves de idempotencia por paso |
| P-110 ✚ | cost_governor | Corta pasos que exceden presupuesto por nivel |

### P5 · CALIDAD DE CÓDIGO (para tareas de software)
| ID | Ficha | Qué hace |
|---|---|---|
| P-111 ✚ | tdd_enforcer | Test primero, código después (TDFlow) |
| P-112 ✚ | review_5_lentes | Correctitud/seguridad/perf/estilo/arquitectura en paralelo |
| P-113 ✚ | mutation_testing | Mata mutantes → calidad real de tests |
| P-114 ✚ | type_gate_mypy | mypy strict como gate |
| P-115 ✚ | complexity_linter | Complejidad ciclomática máxima |
| P-116 ✚ | loc_budget_enforcer | ≤400 LOC por archivo, duro |
| P-117 ✚ | secret_scanner_code | Keys en código → REJECTED |
| P-118 ✚ | sbom_licencias | Auditoría OSS/licencias de deps |
| P-119 ✚ | dependency_pinner | Lockfiles + versiones fijadas |
| P-120 ✚ | cve_watcher | Vulnerabilidades en deps → alerta |
| P-121 ✚ | api_diff_breaking | Detecta breaking changes de API |
| P-122 ✚ | semver_bumper | Sube versión según cambios |
| P-123 ✚ | changelog_compiler | CHANGELOG desde commits/fichas |
| P-124 ✚ | coverage_gate | Cobertura mínima por módulo |
| P-125 ✚ | flaky_test_detector | Tests intermitentes → cuarentena |
| P-126 ✚ | test_impact_analysis | Solo corre tests afectados por el diff |
| P-127 ✚ | benchmark_harness | Benchmarks por ficha con baseline |
| P-128 ✚ | regression_baseline_mgr | baseline_output.json versionado |
| P-129 ✚ | merge_resolver_3way | Resolución 3-way asistida |
| P-130 ✚ | auto_refactor_proposer | Propone (nunca aplica) refactors/dead code |
| P-131 ✚ | docstring_enforcer | Docstrings obligatorios en públicos |
| P-132 ✚ | contract_fuzzer | Fuzzing de enchufes entre fichas |
| P-133 ✚ | git_bisect_auto | Bisect automático ante regresión |
| P-134 ✚ | i18n_extractor | Extrae strings para traducción |
| P-135 | capa4_sentinel_🛂 | Gate de cierre del procesador |

---

## 4. PIPELINE S — SALIDA (55 fichas)

**Microdiagrama:** `Contrato ➜ Construir ➜ CHEF FINAL(anti-síntesis) ➜ 10 checks ➜ Reparar ➜ Diff goal ➜ Sellar ➜ Distribuir ➜ 🛂`

### S1 · CONTRATO Y CONSTRUCCIÓN
| ID | Ficha | Qué hace |
|---|---|---|
| S-001 | output_contract | Declara formato/secciones/límites ANTES de generar |
| S-002 | output_planner | Plan de la salida por secciones |
| S-003 | output_builder | Construye desde el consolidado de Fusion |
| S-004 | checks_eout_10 | E-OUT-001..010 binarios, 10/10 o no sale |
| S-005 | repair_1retry | 1 solo retry dirigido por checks fallidos |
| S-006 | output_diff_goal | Diff semántico vs GoalLock.DoD (% cobertura) |
| S-007 | final_judge_gate | Veredicto final del Juez |
| S-008 | formatter_multi | MD/JSON/HTML/PDF según contrato |

### S2 · CHEF FINAL v2 — CONSOLIDACIÓN ANTI-SÍNTESIS (mejora 1000x)
**El problema que resolvemos:** Sonnet/Opus sintetizan y omiten al consolidar proyectos grandes. **La solución:** la consolidación deja de ser "redacción LLM" y pasa a ser un proceso CONTABLE: censo → libro mayor → fusión por lotes → verificación por conteo. El Juez bloquea si 1 solo ítem queda sin mapear.
| ID | Ficha | Qué hace |
|---|---|---|
| S-009 ✚ | chef_inventory | CENSO: asigna ID a CADA ítem fuente (párrafo/regla/función) |
| S-010 ✚ | chef_coverage_ledger | LIBRO MAYOR: mapa item_id → ubicación en salida. Incompleto = FAIL |
| S-011 ✚ | chef_chunk_merger | Fusiona por lotes pequeños (≤30 ítems) con verificación por lote |
| S-012 | chef_arrastre | Memoria acumulada entre pasadas (3 pasadas) |
| S-013 | chef_3_pasadas | Lista Total → Arrastre → Diseño de Entrega (×3 c/u) |
| S-014 ✚ | chef_anti_sintesis_guard | Compara conteos fuente vs salida: pérdida >0 = REJECTED |
| S-015 ✚ | chef_citation_backmap | Cada bloque de salida referencia sus item_ids fuente |
| S-016 | chef_delivery_designer | Diseña formato/orden de la entrega final |
| S-017 ✚ | chef_sintesis_ejecutiva | Resumen ejecutivo APARTE (jamás sustituye lo completo) |
| S-018 ✚ | chef_split_800 | Divide salidas grandes en docs ≤800 líneas encadenados |
| S-019 ✚ | chef_orphan_hunter | Busca ítems fuente sin destino (0 huérfanos o no cierra) |
| S-020 ✚ | chef_juez_gate | El Juez audita ledger+conteos ANTES del formatter |

### S3 · VALIDACIÓN Y SELLADO
| ID | Ficha | Qué hace |
|---|---|---|
| S-021 | oos_14 | Output Organization System (14 reglas) |
| S-022 | ovfs | Validación de formato de salida |
| S-023 | provenance_sealer | Cadena de procedencia completa firmada |
| S-024 | hash_chain_final | Sellado hash de la respuesta |
| S-025 | artifact_engine | Event sourcing de artefactos + fingerprint L1-L5 |
| S-026 ✚ | gpg_signer | Firma GPG del paquete final |
| S-027 ✚ | checksum_manifest | manifest.json con hash de cada archivo entregado |
| S-028 ✚ | coverage_report_dod | % cumplimiento por ítem del DoD |
| S-029 ✚ | diff_visual_html | HTML de difs para revisar desde el móvil |
| S-030 ✚ | snapshot_final_archiver | Archivo firmado inmutable de la entrega |
| S-031 ✚ | rollback_package | Paquete de reversión listo por si falla |
| S-032 | output_sentinel_🛂 | Gate de cierre de salida |

### S4 · DISTRIBUCIÓN
| ID | Ficha | Qué hace |
|---|---|---|
| S-033 | output_connector | Kanboard/Obsidian/Graphiti/GitHub |
| S-034 | multi_destino_publisher | Publica vía Red Universal (rutas declarativas) |
| S-035 | telegram_notifier | Notifica + solicita aprobación (default NO_GO) |
| S-036 ✚ | atlas_regenerator | Regenera atlas DSL tras cada entrega |
| S-037 ✚ | release_notes_gen | Notas de versión desde ledger+changelog |
| S-038 ✚ | deploy_manifest | Manifiesto de deploy + healthgate post-deploy |
| S-039 ✚ | docs_site_gen | Sitio de docs desde los MD (estático) |
| S-040 ✚ | api_docs_from_schema | Docs de API desde los schemas del enchufe |
| S-041 ✚ | zip_packager | .zip con manifest y orden de construcción |
| S-042 ✚ | entrega_multitamano | Versión completa/media/mini de la misma entrega |
| S-043 ✚ | print_pdf | PDF imprimible de documentos clave |
| S-044 ✚ | cdn_pusher | Publica artefactos estáticos (HF/GH Pages) |
| S-045 ✚ | link_shortener_movil | Enlaces cortos/QR para acceso móvil |
| S-046 ✚ | retention_policy | Aplica TTL/archivado a entregas viejas |

### S5 · POST-ENTREGA
| ID | Ficha | Qué hace |
|---|---|---|
| S-047 | feedback_loop_storage | Guarda feedback para el próximo ciclo |
| S-048 | self_improvement_scores | calidad/eficiencia/precisión vs ciclo anterior |
| S-049 ✚ | postmortem_generator | Si FAIL: causa raíz + lecciones → registry |
| S-050 ✚ | sla_reporter | Cumplimiento de tiempos/presupuesto |
| S-051 ✚ | usage_analytics | Qué fichas se usaron, cuánto costaron |
| S-052 ✚ | gdpr_eraser_hooks | Borrado bajo demanda de datos del usuario |
| S-053 ✚ | satisfaction_probe | Pregunta corta al Director (1 tap) |
| S-054 ✚ | next_actions_suggester | Propone siguientes pasos con evidencia |
| S-055 | session_close_p13 | Cierre formal: crazy_wall snapshot + COMMITTED |

---

## 5. SERVICIOS TRANSVERSALES T (45 fichas)

| ID | Ficha | Qué hace |
|---|---|---|
| T-001..T-010 | state_engine · wal_dual · crazy_wall · fusion · memoria_4tiers · faiss_brain · shared_knowledge · kg_sqlite · event_sourcing · checkpoint_rebuild | Ya codificados (Salidas 3/3.1/S12) — normalizados a enchufe v2.0 |
| T-011 | dream_loop | Cron semanal: consolida sesiones → Tier3 dream.md |
| T-012 | distill_loop | Cron diario: destila lecciones, dedup, enriquece Tier2 |
| T-013 | writer_subagent | Contexto >70% → compacta sin pérdida (ficha invocable) |
| T-014..T-022 | audit_bus · obsidian_writer · graphiti_writer · hallucination_check · recovery_engine · watchdog · heartbeat · dlq_infra · failure_registry | Ya codificados (S2/S13/S15) |
| T-023 | red_universal | Router de conexiones (ya) — nodos GGUF/API como conectores |
| T-024 | enchufe_registry_v2 | Registro central de fichas v2.0 |
| T-025 | sentinela_metodo | Mejora método, nunca cerebro (S14) |
| T-026 ✚ | metrics_timeseries | Serie temporal de métricas (sqlite) |
| T-027 ✚ | anomaly_detector | Detección de anomalías sobre métricas |
| T-028 ✚ | budget_alarms | Alarmas 70/85/95% de presupuesto |
| T-029 ✚ | key_rotation | Rotación programada de credenciales |
| T-030 ✚ | backup_restore | Backup/restore de runtime/ completo |
| T-031 ✚ | cold_archiver | Archivado frío de tasks viejas |
| T-032 ✚ | migration_runner | Migraciones de schemas versionadas |
| T-033 ✚ | schema_registry | Registro versionado de todos los datatypes |
| T-034 ✚ | feature_flags | Flags centralizados (nunca borrar código) |
| T-035 ✚ | kill_switch | Apagado selectivo por ficha/categoría |
| T-036 ✚ | quota_tenant | Cuotas por proyecto/tenant |
| T-037 ✚ | uptime_prober | Sondas de disponibilidad externas |
| T-038 ✚ | incident_manager | Incidentes: abrir/escalar/cerrar con timeline |
| T-039 ✚ | oncall_notifier | Rutas de aviso según severidad |
| T-040 ✚ | resource_monitor | CPU/RAM/disco del host (móvil-aware) |
| T-041 ✚ | otel_exporter | Spans/traces OpenTelemetry |
| T-042 ✚ | log_compactor | Rotación/compresión de JSONL |
| T-043 ✚ | secrets_manager | Bóveda env→runtime (jamás en código) |
| T-044 ✚ | chaos_schedule | Ventanas aprobadas de caos (staging) |
| T-045 ✚ | config_versioner | Versiona config_runtime con difs firmados |

---

## 6. ACELERADORES COGNITIVOS A (15 fichas)

| ID | Ficha | Qué hace |
|---|---|---|
| A-001 | nivel_0_rapido | 1 iteración, 0 simulaciones, MYTHOS off |
| A-002 | nivel_1_estandar | Config base |
| A-003 | nivel_2_profundo | ×2 iteraciones, +críticas, +1 simulación |
| A-004 | nivel_3_mythos | 40 pasos completos + 3 hipótesis + GOAL-STOP |
| A-005 | nivel_4_mythos_turbo | ×K muestras + majority + consenso 5+Devil |
| A-006 | nivel_5_investigacion_extrema | SKYNER 17 + CSA + panel 300 + simulación ×5 |
| A-007 | perfil_consenso_devil | Activa consenso 5+Devil en cualquier nivel |
| A-008 | perfil_skyner | Activa SKYNER standalone |
| A-009 | perfil_deep_research | Discovery R1-R5 extendido (máx rondas ×2) |
| A-010 | perfil_dream_mode | Usa memoria Dream/Distill como contexto extra |
| A-011 ✚ | perfil_chef_estricto | CHEF anti-síntesis con lotes ≤15 y doble conteo |
| A-012 ✚ | perfil_auto_consistencia | ×5 corridas + mayoría en pasos marcados |
| A-013 ✚ | perfil_simulacion_x5 | Simula el plan 5 veces antes de congelar |
| A-014 ✚ | perfil_bajo_costo | Recorta a mínimos: para saldo bajo del plan |
| A-015 ✚ | perfil_movil | Salidas ≤800 líneas, HTML móvil, links cortos |

---

## 7. ESTRUCTURA RAÍZ (dónde vive cada cosa)

```
repo 6  fichas/entrada/E-001..E-072/          (ficha.py + ficha.contract.json + meta.md)
repo 5  fichas/procesador/P-001..P-135/
repo 6  fichas/salida/S-001..S-055/
repo 11 transversales/T-001..T-045/
repo 2  aceleradores/A-001..A-015/  (solo YAML de perfil, 0 LOC)
repo 12 contracts-schemas/universal_module_contract.v2.0.json
```

---

## 8. PLAN DE SALIDAS RESTANTES (pocas, por tu saldo)

| Salida | Contenido | Docs |
|---|---|---|
| ✅ HOY | Enchufe v2.0 + este esqueleto | 2 |
| SALIDA E | Pipeline ENTRADA: 72 fichas con código completo | 3-4 docs ≤800 líneas |
| SALIDA P | Pipeline PROCESADOR: 135 fichas con código completo | 5-6 docs |
| SALIDA S+T+A | SALIDA (con CHEF 1000x) + transversales nuevas + perfiles | 3-4 docs |

Fichas ya codificadas (Salidas 1-6) se referencian con su raíz — no se regeneran.

**VALIDACIÓN FINAL ×3:** ① 64 nodos del diagrama → todos mapeados a fichas ② corpus MASTER 01-29 → CSA/SKYNER/SID/BIS/OOS/OVFS/Loop v6/LOP/Mythos/CHEF presentes ③ tus métodos (constitución análisis, OK/RECIBIDO, panel opuesto) → fichas P-044..P-068. Nuevas ✚ = 202. Sin huérfanos.
