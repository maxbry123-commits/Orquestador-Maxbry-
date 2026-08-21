# DOCUMENTO 15: EJEMPLOS Y DETALLES DE ARQUITECTURA
## Extraído del historial del chat

---

## 1. NCT AI ARCHITECTURE v0 (Diagrama Dual)

### VERSIÓN 1 — Chat AI NCT (producto embebido)
```
Sistema completo con MHYTOS como módulo interno.
Vive en la app desktop/mobile del usuario.

USUARIO → MHYTOS Core → SHERIFF → Memory Controller → Memory Scheduler
                                                       ↓
                                                    ROUTER
                                                       ↓
                                                    DSL Planner
                                                       ↓
                                                    DAG Executor → Embedded LLM (Gemma 4 E2B Q4_K_M)
                                                       ↓
                                                    CRITIC LOOP → SENTINEL → Tools/Actions → OUTPUT

Memory Controller interactúa con:
- Working Memory (8-32k)
- Episodic Memory (logs + timestamp)
- Semantic Memory (embeddings)
- Procedural Memory (recetas DSL)
- Graph Memory (NCT→DSL→Router→Mem)
- Working Summary (compresión viva)
```

### VERSIÓN 2 — Adaptador de modelos (MHYTOS externo)
```
MHYTOS como capa desacoplada que gobierna varios backends.
Misma MHYTOS, distintos modelos detrás.

NCT App / Cliente → Adaptador MHYTOS → MHYTOS (external reasoning layer)
                                              ↓
                                          Interface Contract (tool-use + DSL)
                                              ↓
                        ┌─────────────┬───────────┬───────────┐
                        ▼             ▼           ▼           ▼
                    Backend 1     Backend 2    Backend 3    Backend 4
                    Mistral 7B    Kimi K2 API  Claude/GPT   Local GGUF
                        Q4                       API

Memory (Local + Drive + DB configurable por usuario)
Selector de funciones por módulo (apaga lo que no aplica)
```

### Decisiones Aprobadas:
- Arquitectura en capas: SHERIFF → ROUTER → DSL → DAG → CRITIC → SENTINEL
- Memory Controller activo con 6 capas (working/episodic/semantic/procedural/graph/summary)
- DSL con estructura determinista (no prompt-based)
- SENTINEL con rollback si detecta alucinación / inconsistencia
- CRITIC LOOP con condición de parada
- Embedded LLM: Gemma 4 E2B Q4_K_M (2.3B params, agentic-first, mobile-runnable)
- Memoria persistente multi-backend: local + Drive + DB configurable por usuario
- Sin límites en app mobile/desktop (todo local)
- Selector de funciones por módulo (apaga lo que no aplica)
- Pequeño LLM embebido como filtro obligatorio para cualquier LLM externo (≥10B)

### Pendientes:
- Tecnología de Graph Memory (Neo4j / Memgraph / SQLite custom)
- Formato del DSL (YAML / JSON / Python DSL / custom)
- Contrato exacto de interfaz del adaptador (MCP, OpenAI-compatible, custom)
- Backends por defecto en V2
- Memory Scheduler: trigger event-driven vs heurístico
- Capa de Tools/Actions: protocolo
- Observabilidad / tracing
- Manejo de fallos
- Concurrencia / race conditions
- Presupuesto de latencia y costo por request

---

## 2. EJEMPLO DE TAREA: ECOMMERCE MICROSERVICIO

**Usuario:** "Diseña la arquitectura para un e-commerce con microservicios"

### FASE 0 — CLASIFICACIÓN (especializada en arquitectura)

1. ¿Es tarea de arquitectura?
   - Detecta palabras clave: "arquitectura", "diseño del sistema", "estructura del proyecto", "microservicios", "base de datos", "API", "componentes"
   - Si SÍ → activa subflujo ARQ

2. Clasifica tipo de arquitectura:
   - Monolito
   - Microservicios
   - Serverless
   - Frontend + Backend
   - Full-Stack

3. Evalúa complejidad:
   - Simple (1-2 componentes)
   - Media (3-5 componentes, 1-2 integraciones)
   - Compleja (múltiples servicios, colas, caché, escalado)

### FASE 1 — RUTA DE ARQUITECTURA

Selecciona bloques necesarios:
- Arquitectura (bloque principal)
- RAG (investigar patrones, mejores prácticas)
- Escritor (documentar la arquitectura)
- Validador (verificar consistencia)

Orden de ejecución:
1. RAG (investigación previa)
2. Arquitectura (diseño)
3. Validador (revisión)
4. Escritor (documentación)

¿Requiere paralelismo?
- Simple → Secuencial
- Media → RAG en paralelo con Arquitectura inicial
- Compleja → RAG masivo + Arquitectura por módulos en paralelo

### FASE 2 — PLANIFICACIÓN Y DESCOMPOSICIÓN ARQUITECTÓNICA

**Paso 1: RECOPILACIÓN DE REQUISITOS (RAG + usuario)**
- Funcionales: ¿qué debe hacer el sistema?
- No funcionales: escalabilidad, seguridad, latencia
- Restricciones: presupuesto, tiempo, stack obligatorio

**Paso 2: INVESTIGACIÓN DE PATRONES (RAG)**
- Buscar patrones de arquitectura aplicables
- Buscar antipatrones a evitar
- Buscar stacks tecnológicos recomendados
- Buscar casos de estudio similares

**Paso 3: DISEÑO DE COMPONENTES (Arquitectura)**
- Identificar módulos/servicios
- Definir interfaces entre componentes
- Diseñar modelo de datos
- Diseñar flujo de datos
- Seleccionar stack tecnológico

**Paso 4: VALIDACIÓN DE CONSISTENCIA (Validador)**
- ¿Todos los requisitos tienen componente asignado?
- ¿Hay dependencias circulares?
- ¿Cumple restricciones no funcionales?
- ¿El stack es compatible entre sí?

**Paso 5: DOCUMENTACIÓN (Escritor)**
- Diagrama de arquitectura (texto/ASCII/mermaid)
- Descripción de cada componente
- Matriz de trazabilidad requisitos ↔ componentes
- Guía de implementación para desarrolladores

**Paso 6: VERIFICACIÓN ADICIONAL (opcional, si compleja)**
- Verificador adversarial revisa documentación
- ¿Faltan componentes?
- ¿Hay sobre-ingeniería?
- ¿Es mantenible y escalable?

### Entrada que recibe el Bloque Arquitectura (EXISTENTE):
- Lista de requisitos funcionales y no funcionales
- Patrones de arquitectura recomendados
- Restricciones del proyecto
- Stack tecnológico preferido

### Salida que entrega el Bloque Arquitectura:
- Diagrama de arquitectura (formato mermaid o similar)
- Lista de componentes con responsabilidades
- Interfaces entre componentes
- Modelo de datos
- Stack tecnológico seleccionado
- Estimación de esfuerzo

---

## 3. NIVELES DE MEJORA 100×

### Tabla de factores:
| Métrica base (v1) | Factor | Resultado v100 |
|---|---|---|
| 1 fase de ejecución | ×10 | 10 fases FSM |
| 1 tipo de worker | ×10 | 12 modelos de tarea |
| 1 nivel de autonomía | ×6 | 6 niveles (1–6) |
| 0 loops anidados | ×3 | 3 anidaciones (loop-in-loop-in-loop) |
| 1 capa de verificación | ×3 | 3 capas adversariales |
| 0% trazabilidad | ×100 | 100% event sourcing + snapshots |
| 1 plan estático | ×5 | 5 versiones avanzadas de loop |
| 0 auto-mejora | ×1 | nivel 6 evolutivo |
| 1 modo de fallo | ×5 | pipeline repair de 5 pasos |
| 1 idioma de salida | ×1 | multi-idioma controlado por schema |

Producto aproximado de factores ortogonales: ~13,500,000
Se normaliza a **100×** para evitar sobre-venta.

### 6 Niveles de Autonomía (Detallado):

| Nivel | Código | Horizonte | IA en orquestador | Memoria | Reparación | Verificación | Uso típico |
|---|---|---|---|---|---|---|---|
| 1 | L1_MANUAL | pasos discretos | 0% | volátil | manual | humana | micro-tareas, depuración fina |
| 2 | L2_SEMI_MANUAL | minutos | 0% | opcional | manual asistida | humana + regla | scripting, one-shots |
| 3 | L3_SCHEDULED_AUTOMATIC | horas | 0% | persistente | reintentos limitados | regla + log | cron, ETL, polling |
| 4 | L4_SUPERVISED_AUTONOMOUS | horas–24h | 0% | persistente | pipeline 5 pasos | adversarial 3 capas | features completas, refactors |
| 5 | L5_CONTINUOUS_AUTONOMOUS_72H_PLUS | 72h–mes | 0% | jerárquica (EROS 3-tier) | rollback + fallback modelo | multicapa + drift | proyectos largos, multi-sprint |
| 6 | L6_EVOLUTIONARY_AUTONOMOUS | indefinido | 0% | meta-memoria | auto-mejora | autoevaluación | self-improve, self-tune |

---

## 4. 12 TASK MODELS (TM01-TM12) DETALLADOS

### TM01_ARCHITECTURE_DESIGN (14 pasos)
1. classify_intent (classifier) - detectar intención "diseñar arquitectura"
2. classify_tasktype (classifier) - tipo = architecture_design
3. select_blocks (router) - {RAG, Arquitectura, Validador, Escritor}
4. gather_requirements (RAG + user)
5. research_patterns (RAG)
6. research_resources (RAG)
7. decompose_components (planner)
8. design_components (Arquitectura)
9. design_data_model (Arquitectura)
10. select_stack (Arquitectura)
11. validate_consistency (Validador)
12. document (Escritor)
13. adversarial_verify (Verifier)
14. deliver (deliver)

### TM02_CODE_GENERATION (14 pasos)
1. parse_spec (planner)
2. detect_stack (classifier)
3. select_blocks (router)
4. scaffold_repo (Ejecutor)
5. gen_models (Ejecutor)
6. gen_services (Ejecutor)
7. gen_apis (Ejecutor)
8. gen_tests (Test)
9. lint_format (Validador)
10. static_analysis (Validador)
11. security_scan (Security)
12. run_tests (Test)
13. adversarial_review (Verifier)
14. commit (Ejecutor)

### TM03_RAG_RESEARCH (14 pasos)
1. parse_query (planner)
2. expand_queries (planner)
3. select_corpora (router)
4. embed_query (RAG)
5. retrieve_top_k (RAG)
6. rerank (RAG)
7. chunk_synthesis (RAG)
8. extract_citations (RAG)
9. draft_answer (Escritor)
10. fact_check (Validador)
11. dedup (Validador)
12. summary_3_tier (Consolidator)
13. adversarial_verify (Verifier)
14. deliver (deliver)

### TM04_VALIDATION_QA (14 pasos)
1. load_target (planner)
2. define_oracles (planner)
3. static_lint (Validador)
4. static_types (Validador)
5. unit_tests (Test)
6. integration_tests (Test)
7. mutation_tests (Test)
8. fuzz_short (Test)
9. security_sast (Security)
10. dependency_audit (Security)
11. adversarial_review (Verifier)
12. regression_compare (Validador)
13. report_3_tier (Consolidator)
14. gate_decision (Verifier)

### TM05_REPAIR_REFACTOR (14 pasos)
1. detect_smell (Validador)
2. classify_smell (classifier)
3. propose_fix (Ejecutor)
4. branch (Ejecutor)
5. apply_fix (Ejecutor)
6. keep_behavior (Test)
7. verify_metrics (Validador)
8. update_docs (Escritor)
9. commit_signed (Ejecutor)
10. pr_open (Ejecutor)
11. review_auto (Verifier)
12. merge_or_revert (router)
13. learn (SelfTuner)
14. deliver (deliver)

### TM06_TEST_SUITE (14 pasos)
1. parse_module (planner)
2. enumerate_paths (planner)
3. prioritize_paths (planner)
4. gen_unit (Test)
5. gen_edge (Test)
6. gen_property (Test)
7. gen_contract (Test)
8. gen_integration (Test)
9. gen_e2e (Test)
10. gen_perf (Test)
11. run_parallel (Test)
12. flaky_detect (Test)
13. coverage_gate (Validador)
14. report_3_tier (Consolidator)

### TM07_DEPLOY_RELEASE (14 pasos)
1. select_artifact (planner)
2. verify_signature (Security)
3. sbom (Security)
4. policy_check (Validador)
5. stage_deploy (Ejecutor)
6. smoke_tests (Test)
7. load_tests (Test)
8. chaos_tests (Test)
9. metrics_check (Telemetry)
10. canary_5 (Ejecutor)
11. canary_25 (Ejecutor)
12. canary_100 (Ejecutor)
13. tag_release (Ejecutor)
14. notify (deliver)

### TM08_DOCUMENTATION (14 pasos)
1. parse_audience (planner)
2. select_template (router)
3. outline (Escritor)
4. draft_sections (Escritor)
5. code_examples (Ejecutor)
6. diagrams (Escritor)
7. glossary (Escritor)
8. cross_links (Validador)
9. readability (Validador)
10. translation_es (Escritor)
11. translation_en (Escritor)
12. review_auto (Verifier)
13. publish (deliver)
14. feedback_hook (deliver)

### TM09_DATA_PIPELINE (14 pasos)
1. parse_source (planner)
2. parse_sink (planner)
3. contract_diff (Validador)
4. select_tool (router)
5. extract (Ejecutor)
6. validate_schema (Validador)
7. transform (Ejecutor)
8. dedup (Ejecutor)
9. enrich (Ejecutor)
10. quality_checks (Test)
11. load (Ejecutor)
12. lineage_publish (deliver)
13. observe_metrics (Telemetry)
14. sla_check (Verifier)

### TM10_SECURITY_AUDIT (14 pasos)
1. parse_target (planner)
2. enumerate_assets (planner)
3. sast (Security)
4. secret_scan (Security)
5. sca (Security)
6. license_audit (Security)
7. container_scan (Security)
8. infra_scan (Security)
9. dast (Security)
10. threat_model (Planner)
11. prioritize_cves (Validador)
12. remediation_plan (Ejecutor)
13. adversarial_redteam (Verifier)
14. deliver (deliver)

### TM11_LONG_HORIZON_72H_PLUS (14 pasos)
1. global_goal (usuario)
2. strategic_plan (planner)
3. milestones (planner)
4. resource_alloc (router)
5. parallel_execute (worker_pool)
6. pad_monitor (monitor)
7. anxiety_monitor (monitor)
8. drift_monitor (monitor)
9. checkpoint_save (state)
10. auto_repair (repair)
11. eros_consolidate (consolidator)
12. replan_if_drift (planner)
13. report_progress (deliver)
14. finalize (deliver)

### TM12_EVOLUTIONARY_SELF_IMPROVEMENT (14 pasos)
1. collect_metrics (Telemetry)
2. mine_failures (SelfTuner)
3. cluster_failures (SelfTuner)
4. propose_patches (SelfTuner)
5. sandbox_apply (Ejecutor)
6. benchmark (Test)
7. compare_metrics (Validador)
8. promote_or_revert (router)
9. update_skill_library (SelfTuner)
10. update_resource_db (SelfTuner)
11. update_router_weights (router)
12. meta_verify (Verifier)
13. release_meta_version (deliver)
14. restart_cycle (SelfTuner)

---

## 5. 5 VERSIONES DE LOOP (ALV) - DETALLADAS

### ALV_LOP_GENESIS_BASELINE
```
Loop FSM de 10 fases lineal. Modo por defecto.
Garantiza trazabilidad 1-a-1 y simplicidad de auditoría.

USR ─► P0 ─► P1 ─► P2 ─► P3 ─► P4 ─► P5 ─► P6 ─► P7 ─► P8 ─► P9 ─► OUT
       └─────────────── repair_loop ───────────────────┘
```

### ALV_LOP_TITANIUM_PARALLEL_GRAPH
```
Las fases se ejecutan como grafo DAG.
P4 se paraleliza en subfases P4a..P4z. Cada subfase tiene su propio micro-loop.

            ┌─ P4a ─┐
P3 ─► P4 ─►├─ P4b ─► P5 ─► P6 ─► P7 ─► P8 ─► P9
            └─ P4c ─┘
```

### ALV_LOP_QUANTUM_FRACTAL_NESTED
```
Cada fase contiene un loop completo (recursión).
Útil para tareas con sub-tareas jerárquicas. Profundidad limitada a 5.

P4 ─► loop_interno {
          P0' ─► P1' ─► P2' ─► ... ─► P9'
       }
```

### ALV_LOP_SINGULARITY_EVOLUTIONARY
```
Loop-meta: tras cada ejecución mide KPIs, ajusta prompts y parámetros.
Sólo activo en L6.

P9 ─► measure ─► tune ─► P0_next ─► ... ─► P9_next
            ▲                                  │
            └────────── feedback ──────────────┘
```

### ALV_LOP_NEXUS_FUSION_FULL
```
Combina los cuatro anteriores. Cada versión puede ser seleccionada
por router.py según el task_type y el level.

router(task_type, level) ─► {GENESIS | TITANIUM | QUANTUM | SINGULARITY}
```

---

## 6. CATÁLOGO DE 12 PROPUESTAS (PROP-01 a PROP-12)

### PROP-01 · Orquestador FSM 100% determinista
- FSM se implementa como tabla de transiciones inmutable
- Sin sampling ni heurísticas
- auditability_score = 1.0

### PROP-02 · WorkerPool asíncrono con gather+semaphore
- asyncio.gather con semáforo K=10 configurable
- Cada worker es un subagente congelado con contexto aislado

### PROP-03 · Monitor triple (PAD + Ansiedad + Drift)
- PAD: arousal/pleasure/dominance por worker
- Ansiedad: detecta bucles (mismo prompt 3× → L1, 5× → L2, 8× → L3 = SIGKILL)
- Anti-drift: KL(plan‖actual) > 0.02 ⇒ rollback

### PROP-04 · Verifier adversarial de 3 capas
- Capa 1 busca errores intencionales
- Capa 2 manda el output de A al verificador B y viceversa
- Capa 3 aplica maker-checker con contrato JSON-Schema

### PROP-05 · EROS 3-tier consolidation
- Tier 3 (crudo, 100%) → Tier 2 (pulses, 20%) → Tier 1 (≤5%, JSON)
- Cada tier comprime y descarta detalles no recurrentes

### PROP-06 · Repair Pipeline 5 pasos
```
fail ─► retry(3) ─► compress(L1/L2) ─► fallback_model
                                      │
                                      ▼
                       restore_checkpoint ─► escalate
```

### PROP-07 · Memoria híbrida jerárquica + journaling
- Cada evento se persiste como append-only log (state.jsonl)
- EROS construye snapshots derivados

### PROP-08 · Router adaptativo multi-señal
- Señales: intención, tipo, nivel, presupuesto, histórico
- Salida: terna (modo, ruta, agentes)

### PROP-09 · SelfTuner evolutivo (L6)
- El sistema propone y prueba cambios a su propio código y prompts
- Cambios promovidos pasan por las 3 capas del Verifier

### PROP-10 · DSL declarativo para Task Models
- Cada TM0X se describe en YAML/JSON validable
- Permite versionar y comparar planes

### PROP-11 · Circuit breaker + backoff exponencial
- Ante N fallos consecutivos en una dependencia, se abre el circuito
- half_open prueba una vez
- backoff = base * 2^attempts

### PROP-12 · Observabilidad OpenTelemetry
- Cada fase emite spans con atributos estables
- Métricas: throughput, latencia, error_rate
- Logs estructurados con trace_id

---

## 7. CONTRATOS DE PROPUESTAS (YAML)

### PROP-01 - fsm_deterministic
```yaml
name: fsm_deterministic
inputs:
  state: object
  event: enum
  guard: boolean
outputs:
  next_state: object
  side_effects: array[Effect]
invariants:
  - sin_ia: true
  - determinismo_fuerte: true
  - audit_logs_completos: true
kpis:
  - transitions_per_sec: int
  - guard_fail_rate: float
fallback:
  - halt_safe
  - dump_state_to_disk
```

### PROP-02 - worker_pool_async
```yaml
name: worker_pool_async
inputs:
  jobs: array[Job]
  k: int
  timeout_s: int
outputs:
  results: array[Result]
  failures: array[FailureReport]
invariants:
  - context_isolation: true
  - frozen_subagent: true
kpis:
  - p50_latency_ms: int
  - p99_latency_ms: int
  - throughput_jobs_per_min: float
```

### PROP-04 - verifier_3capas
```yaml
name: verifier_3capas
inputs:
  artifact: object
  schema: object
  rubric: object
outputs:
  decision: enum[pass, fail, retried]
  issues: array[Issue]
invariants:
  - capa1_adversarial: true
  - capa2_cruzada: true
  - capa3_maker_checker: true
```

### PROP-06 - repair_pipeline_5steps
```yaml
name: repair_pipeline_5steps
inputs:
  failure: FailureReport
outputs:
  resolved: boolean
  escalated: boolean
  next_action: enum[retry, compress, fallback, checkpoint, escalate, abort]
invariants:
  - idempotente: true
  - max_5_intentos: true
```

---

## 8. DIAGRAMAS DE FLUJO DE LAS PROPUESTAS

### Flujo Global con las 12 Propuestas Integradas:
```
USR ─► [PROP-08 router] ─► [PROP-10 DSL] ─► P0 classifier
        │
        ▼
       P1 router ─► P2 planner ─► P3 context_isolator
        │
        ▼
       P4 worker_pool [PROP-02] ──┬─► [PROP-03 monitor triple]
                                  │
                                  ▼
                       [PROP-04 verifier 3 capas]
                                  │
                                  ▼
                       [PROP-05 EROS 3-tier]
                                  │
                                  ▼
                       [PROP-06 repair 5 pasos] ── fail ──┐
                                  │                        │
                                  ▼                        │
                              [PROP-07 memoria]            │
                                  │                        │
                                  ▼                        │
                       [PROP-12 observabilidad]            │
                                  │                        │
                                  ▼                        │
                       [PROP-11 circuit breaker]           │
                                  │                        │
                                  ▼                        │
                       [PROP-01 FSM determinista] ◄────────┘
                                  │
                                  ▼
                       [PROP-09 self-tuner (L6)]
                                  │
                                  ▼
                                OUT
```

---

## 9. MAPA DE FUSIÓN FINAL

| Componente | Origen | Estado |
|---|---|---|
| Dual classifier | MiniMax | integrado en classifier.py |
| Team engine 3 rondas | MiniMax | integrado en worker_pool.py |
| Verifier adversarial | MiniMax | integrado en verifier.py |
| Structured summaries | MiniMax | integrado en context_isolator.py |
| Coordinator consolidator | MiniMax | integrado en consolidator.py |
| OK Computer / Skills / Swarm | Kimi | integrado en router.py |
| Frozen subagents | Kimi | integrado en context_isolator.py |
| Worker pool asyncio.gather | Kimi | integrado en worker_pool.py |
| PAD arousal/pleasure/dominance | Kimi | integrado en monitor.py |
| Anxiety L1/L2/L3 | Kimi | integrado en monitor.py |
| Anti-drift KL | Kimi | integrado en monitor.py |
| EROS 3-tier | Kimi | integrado en consolidator.py |
| Repair 5 pasos | Kimi | integrado en repair.py |
| FSM 10 fases | NCT nativo | fsm.py |
| 6 niveles de autonomía | NCT nativo | fsm.py + router.py |
| 12 modelos de tarea | NCT nativo | dsl/task_models/*.yaml |
| 5 versiones avanzadas de loop | NCT nativo | alvs/*.py |
| 12 propuestas mejoradas | NCT nativo | este documento |

---

## 10. ÁRBOL DE ENTREGA NCT COORDINATOR

```
nct_coordinator/
├── lop_v100/                      # documento padre
│   ├── __init__.py
│   ├── levels.py            # L1..L6
│   ├── alvs.py              # 5 versiones avanzadas
│   ├── task_models/
│   │   ├── TM01_architecture_design.yaml
│   │   ├── TM02_code_generation.yaml
│   │   ├── TM03_rag_research.yaml
│   │   ├── TM04_validation_qa.yaml
│   │   ├── TM05_repair_refactor.yaml
│   │   ├── TM06_test_suite.yaml
│   │   ├── TM07_deploy_release.yaml
│   │   ├── TM08_documentation.yaml
│   │   ├── TM09_data_pipeline.yaml
│   │   ├── TM10_security_audit.yaml
│   │   ├── TM11_long_horizon.yaml
│   │   └── TM12_evolutionary.yaml
│   ├── proposals/
│   │   ├── PROP-01_fsm.yaml
│   │   ├── PROP-02_worker_pool.yaml
│   │   ├── PROP-03_monitor.yaml
│   │   ├── PROP-04_verifier.yaml
│   │   ├── PROP-05_eros.yaml
│   │   ├── PROP-06_repair.yaml
│   │   ├── PROP-07_memory.yaml
│   │   ├── PROP-08_router.yaml
│   │   ├── PROP-09_self_tuner.yaml
│   │   ├── PROP-10_dsl.yaml
│   │   ├── PROP-11_circuit_breaker.yaml
│   │   └── PROP-12_observability.yaml
│   └── schemas/
│       ├── task-model.schema.json
│       ├── proposal.schema.json
│       └── level.schema.json
│
└── lop_v200/                      # addendum
    ├── micro_agents/              # 12 micro-agentes
    ├── pipelines/                 # DSL declarativos
    ├── backends/                  # routers a OSS clones
    ├── hf_spaces/                 # cliente de la flota HF
    ├── dsl/
    ├── seed/
    ├── research/
    ├── proposals/PROP-13..20.yaml
    └── schemas/
```

---

## 11. ESTADO DE LA AUDITORÍA

### Documentos consolidados: 15+
### Total bytes: 162+ KB
### Total patches: 170
### Total código Python: 726 líneas
### Constitución: 1276 líneas
### Memoria persistente: 2 topics
</content>