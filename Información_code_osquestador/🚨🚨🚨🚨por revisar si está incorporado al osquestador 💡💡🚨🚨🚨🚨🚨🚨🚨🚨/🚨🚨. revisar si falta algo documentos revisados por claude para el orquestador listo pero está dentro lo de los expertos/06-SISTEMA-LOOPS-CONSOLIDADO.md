# DOCUMENTO 06 — SISTEMA DE LOOPS AVANZADO CONSOLIDADO
## V1.0 — Para implementación programática

Fuentes integradas:
- 03-LOOPS-10-NIVELES.md (NCT jerarquía operacional)
- 04-MHYTOS-6-FASES.md (motor de pensamiento paralelo)
- 12 Agentic Harness Patterns de Bilgin Ibryam (Claude Code leak 2026)
- Experience Graphs Trellis (Meta arxiv 2606.29823)
- EXG (arxiv 2605.17721), ExpGraph (arxiv 2605.30712)
- Gödel Agent (arxiv 2410.04444), SICA (arxiv 2504.15228)
- ACE Framework (arxiv 2510.04618, ICLR 2026)
- ICML 2026 "Recognize Your Orchestrator" (Nanjing University)
- LangGraph orchestrator-worker pattern
- Bilevel Autoresearch (arxiv 2603.23420)
- claude-code-router, Hermes Agent, Open Claw
- 100 simulaciones previas del vault
- 250+ fuentes de inventario-codigo-real.md

---

## 1. VISIÓN UNIFICADA

El sistema integra 4 capas independientes pero conectadas:

| Capa | Función | Inspiración |
|---|---|---|
| Harness (12 patterns) | Hacer al modelo confiable | Bilgin Ibryam sobre Claude Code |
| Memory (5 patterns + experience graph) | Recordar entre sesiones y aprender | EXG, Trellis, ACE |
| Workflow (3 patterns) | Orquestar tareas | LangGraph orchestrator-worker, explore-plan-act |
| Loops (10 niveles + 6 fases) | Operar 24/7 con auto-mejora | NCT + MHYTOS propios |

Ecuación: **Agente = Modelo + Harness + Memory + Workflow + Loops**

---

## 2. LOS 12 HARNESS PATTERNS (Bilgin Ibryam)

### 2.1 Memoria y Contexto (5 patterns)

**Pattern 1: Persistent Instruction File**
- Archivo `CLAUDE.md` o equivalente a nivel proyecto
- Se carga automáticamente en cada sesión
- Contiene: convenciones de código, comandos de build, reglas arquitectónicas, restricciones
- Versionado junto al codebase
- Para MHYTOS: un CLAUDE.md por scope (A/B/C/D) más uno raíz

**Pattern 2: Scoped Context Assembly**
- Instrucciones fragmentadas por scope: organización → proyecto → subdirectorio
- El agente carga solo las relevantes según directorio actual
- Imports modularizados para evitar duplicación
- Para MHYTOS: `cerebro/phases/f1/CLAUDE.md`, `cerebro/phases/f2/CLAUDE.md`, etc.

**Pattern 3: Tiered Memory**
- 3 niveles: índice lean en contexto, detalles bajo demanda, historial en disco
- Nivel 1 (core): identidad, reglas activas, estado de tarea actual
- Nivel 2 (recall): últimas N conversaciones indexadas, búsqueda on-demand
- Nivel 3 (archival): todo el historial, vector store + knowledge graph
- Para MHYTOS: la base de las 4 work groups, cada uno con su tier

**Pattern 4: Dream Consolidation**
- Proceso background que corre en idle
- Evalúa, deduplica, poda y optimiza memoria
- Trigger: cuando CPU < 20% o cada N minutos sin tarea
- Output: memoria más limpia sin intervención del agente
- Para MHYTOS: F4 Mejoras Continuas en su forma más pura

**Pattern 5: Progressive Context Compaction**
- Compresión multinivel según antigüedad
- Reciente: texto completo
- Antiguo: resumen
- Muy antiguo: compresión fuerte
- Trigger: cuando context window > 80%
- Para MHYTOS: evita que F5 Revisión se quede sin contexto

### 2.2 Workflow y Orquestación (3 patterns)

**Pattern 6: Explore-Plan-Act Loop**
- Separación explícita de 3 fases
- Explore: solo lectura, búsqueda, análisis
- Plan: propuesta de solución, sin modificar
- Act: solo cuando se aprueba el plan, modificar
- Para MHYTOS: F2 Planificación = Plan, F3 Ejecución = Act, F1 Investigación = Explore
- Beneficio: previene ediciones prematuras, mejora calidad 23-36% según benchmark Claude Code

**Pattern 7: Context-Isolated Subagents**
- Cada subagente tiene su propio context window, prompt, tools limitadas
- Main agent recibe solo el resumen final, no el proceso
- Previene contaminación de contexto
- Para MHYTOS: cada fase es un subagente con scope específico
- Implementación: Claude Code Task tool con `run_in_background: true`, límite 10 paralelos

**Pattern 8: Fork-Join Parallelism**
- Subagentes paralelos en worktrees independientes
- Comparten cache del proceso padre (ahorro de tokens)
- Join cuando todos terminan
- Para MHYTOS: 6 fases en paralelo cada una en su contexto aislado
- Implementación: git worktree + Claude Code Task tool paralelo

### 2.3 Herramientas y Permisos (3 patterns)

**Pattern 9: Progressive Tool Expansion**
- Empezar con <20 herramientas default
- Agregar especializadas solo cuando se necesitan
- Reduce ruido en selección, mejora precisión
- Para MHYTOS: router decide qué tools exponer a cada fase

**Pattern 10: Command Risk Classification**
- Clasificador de riesgo de comandos shell antes de ejecutar
- 3 niveles: safe (auto-aprueba), warning (loguea), danger (requiere confirmación)
- Implementación: lista de patrones regex + LLM-as-judge para casos ambiguos
- Para MHYTOS: F3 Ejecución antes de cada bash call

**Pattern 11: Single-Purpose Tool Design**
- Herramientas dedicadas con input validado en lugar de shell genérico
- Ejemplo: `FileReadTool(path)` en vez de `cat $path`
- Boundaries claras, validables, auditables
- Para MHYTOS: MCP servers con schemas JSON estrictos

### 2.4 Automatización (1 pattern)

**Pattern 12: Deterministic Lifecycle Hooks**
- Acciones automáticas en puntos fijos del ciclo de vida
- `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Notification`, `Stop`, `SubagentStop`, `PreCompact`
- Independiente del prompt, no se puede saltar
- Ejemplo: formatear código después de cada edit, validar comandos antes de ejecutar
- Para MHYTOS: triggers automáticos de F5 Revisión, sync Graphiti, refutación cada 10 pasos

---

## 3. SISTEMA DE MEMORIA CON EXPERIENCE GRAPH

### 3.1 Tres Tiers (Pattern 3 + Experience Graph)

```
TIER 1: Core Memory
├── Identidad del agente (quién soy)
├── Reglas activas (qué reglas me aplican)
├── Estado de tarea actual
├── Skills activas (qué sé hacer)
└── Permisos scope actual (qué puedo tocar)
Persistencia: en prompt, RAM
Latencia: 0
Modificación: tool calls explícitos

TIER 2: Recall Memory
├── Últimas N conversaciones (10-100)
├── Resúmenes comprimidos
├── Índices por timestamp, topic, outcome
└── Searchable via semantic similarity
Persistencia: SQLite o Postgres
Latencia: <50ms
Modificación: append-only + rotación

TIER 3: Archival Memory (Experience Graph)
├── Cada trajectory = nodo con (task, action, outcome, reward)
├── Edges: similitud semántica, secuencia causal, corrección
├── Abstracted principles separados de trajectories
├── Cross-session query: "¿qué funcionó en tareas similares?"
└── Trust boundary: solo writers autorizados
Persistencia: FalkorDB o Neo4j (graph) + vector store
Latencia: 100-500ms
Modificación: governed, versionado
```

### 3.2 Experience Graph Schema (Trellis-style)

```json
{
  "nodes": {
    "trajectory_id": {
      "task": "string",
      "actions": ["action1", "action2", ...],
      "outcome": "success|failure|partial",
      "reward": 0.0-1.0,
      "timestamp": "ISO8601",
      "session_id": "string",
      "parent_trajectory": "trajectory_id|null"
    },
    "principle_id": {
      "abstraction": "string",
      "supporting_trajectories": ["trajectory_id", ...],
      "confidence": 0.0-1.0,
      "applicability": "string",
      "last_validated": "ISO8601"
    }
  },
  "edges": {
    "semantic_similarity": {weight: 0.0-1.0},
    "causal_sequence": {parent: "id", child: "id"},
    "error_correction": {original: "id", corrected: "id"},
    "abstraction_link": {trajectory: "id", principle: "id"}
  }
}
```

### 3.3 Sincronización cada 10 pasos

1. Recolectar trajectories de los últimos 10 steps
2. Detectar patterns repetidos (semantic clustering)
3. Generar o actualizar principles abstractas
4. Validar principles contra held-out tasks
5. Podar trajectories redundantes
6. Actualizar indices
7. Escribir a vault markdown con wikilinks

---

## 4. WORKFLOW PATTERNS INTEGRADOS

### 4.1 Orchestrator-Worker con Entropy Management

El patrón dominante 2026 según ICML 2026. Estructura:

```
ORCHESTRATOR (main agent)
├── Sostiene contrato con usuario
├── Mantiene task-level state
├── Decide decomposition dinámica
├── Monitorea "entropy" (cuán fuera de control está)
├── Re-sincroniza si entropy > threshold
└── Sintetiza outputs de workers

WORKERS (subagentes context-isolated)
├── Reciben brief estrecho
├── Context window aislado
├── Tools específicas a su rol
├── Devuelven solo final + artifact refs
└── No comparten conversational history
```

Implementación LangGraph:
- `StateGraph` con `Send` API para fork dinámico de workers
- `interrupt()` para re-sincronización cuando entropy sube
- `PostgresSaver` checkpointer para resumability
- Thread ID para session isolation

### 4.2 Explore-Plan-Act (Pattern 6) en cada fase

```
EXPLORE (read-only)
├── Read archivos relevantes
├── Grep patrones
├── Glob estructura
└── Output: mapa de contexto

PLAN (no-modify)
├── Sintetizar findings
├── Proponer approach
├── Listar risks
└── Output: plan.md

ACT (con permisos)
├── Ejecutar cambios
├── Validar cada cambio
├── Reportar outcome
└── Output: resultado + delta
```

Trigger entre fases: validación humana o auto-aprobación con threshold.

### 4.3 Fork-Join (Pattern 8) para 6 fases paralelas

```
MAIN SPAWN:
├── git worktree f1_investigacion
├── git worktree f2_planificacion
├── git worktree f3_ejecucion
├── git worktree f4_mejoras
├── git worktree f5_revision
└── git worktree f6_estrategia

PARALLEL EXECUTION (cada worktree):
├── Claude Code con scope permissions
├── Tier 1 memory compartido (read-only del core)
├── Tier 2 memory compartido (read-write)
└── Tier 3 memory individual (read-write)

JOIN:
├── Cada worker vuelca a shared state
├── Orchestrator sintetiza
├── Commit a main
└── Cleanup worktrees
```

---

## 5. SISTEMA DE LOOPS (10 NIVELES + 6 FASES)

### 5.1 10 Niveles NCT (de tu documento 03)

Nivel 0: Meta-Loop Open Claw (cada 10s)
- Heartbeat, poll 4 grupos, re-priorizar, decidir siguiente acción
- Combina LangGraph Supervisor + BabyAGI + Temporal

Nivel 1: Bucle Open Claw (30s)
- Receive signals, poll grupos, detect recovery needed

Nivel 2: Bucle de Grupo (por task)
- Saga Pattern + Circuit Breaker + Exponential Backoff
- MAX_STEPS=20, delay = 2^ronda + random(0,1)
- Fases 0-8: init saga → claude loop → mimo loop → auditor → circuit breaker → commit/compensate → notify → update state

Nivel 3: Bucle Interno Claude (ReAct mejorado)
- 0: Receive task
- 1: Generate hypotheses (min 3)
- 2: Self-reflection
- 3-5: Investigate / Design / Alternatives
- 6: Implement (ReAct Thought→Action→Obs)
- 7: Self-check 3 niveles
- 8: Prepare handoff

Nivel 4: Bucle Mimo (3 capas paralelas con asyncio.gather)
- Cache check → parallel validation → aggregate → classify → generate feedback → update log

Nivel 5: Bucle Auditor (N0-N5 paralelos + SC1-SC6 secuencial)
- Parallel verification, slot contract, fingerprint 5 layers, provenance, Obsidian+Graphiti write

Nivel 6: Self-Improvement (cron 1h)
- Collect metrics → compare baseline → decide mejora/regresión/estancamiento → 3 ciclos validación → merge

Nivel 7: Signal Handlers (always listening)
- HALT, PAUSE/RESUME, SCALE_UP/DOWN, ROLLBACK, EMERGENCY

Nivel 8: Heartbeat (cada 10s)
- state.X.heartbeat, watchdog cada 30s, recovery levels

Nivel 9: Dead Letter Queue con retry inteligente
- 5min → 30min → 2h → 24h, nuevas hipótesis en cada reintento

Nivel 10: Escalation Hierarchy (5 niveles)
- SELF → PARENT → SIBLING → AUDITOR → DIRECTOR

### 5.2 6 Fases MHYTOS (de tu documento 04)

FASE 1: Investigación
- Sub-loop: generate_query, search multi-source, curate, diff
- Sources: arxiv, HF, GitHub, web
- Output: investigation.jsonl con hallazgos rankeados
- Patterns aplicados: Karpathy autoresearch, gpt-researcher, open_deep_research

FASE 2: Planificación
- Sub-loop: read F1 findings, decompose, qualify, prioritize, assign
- Output: plan.json con tasks jerárquicos + metric criteria
- Patterns aplicados: BabyAGI, HTN planning, DSPy GEPA, Gödel Agent

FASE 3: Ejecución
- Sub-loop: pull task, route (simple/dynamic), execute, eval, retry 3x o buscar alternativas
- Output: execution_log.jsonl + feedback.jsonl
- Patterns aplicados: ReAct, Reflexion, Temporal Signals, Plan-and-Solve

FASE 4: Mejoras Continuas (async)
- Sub-loop: observe → propose → simulate → sandbox_apply → measure (10min window) → persist/revert
- Output: improvements.jsonl + metrics.jsonl + auto-PRs
- Patterns aplicados: Factory.ai Signals, Bilevel Autoresearch

FASE 5: Revisión
- Sub-loop: aggregate F1-F4 outputs, eval vs gold_standard, find_gaps, propose, finalize o restart
- Output: review.json + restart_plan.json + HITL flag
- Patterns aplicados: A-MEM, MetaReflection, Quality control loops

FASE 6: Estrategia
- Sub-loop: aggregate F1-F5, generate 10 hipótesis, simulate vs world_model, portfolio select, emit_to_F2
- Output: hypotheses.json + simulation_results.json + strategy_evolution.jsonl
- Patterns aplicados: ReTreVal, MCTS, Bayesian Optimization, Monte Carlo

### 5.3 Cross-Phase Sync (cada 10 pasos)

1. Refutation Engine: 50 preguntas en 7 categorías, score 0.0-1.0 por fase
2. Graphiti Sync: extrae entities + relations, persiste FalkorDB + vault
3. Obsidian Commit: cada fase escribe _phase_state.md
4. Memory Sync: Generator+Reflector+Curator actualizan ACE playbook
5. Interrupt Decision: si refutation_score < 0.4 → HITL, si 3 contradicciones → consolidation

### 5.4 Categorías de Refutación (50 preguntas)

| Categoría | Count | Propósito |
|---|---|---|
| adversarial_data | 7 | contradice el prompt |
| safety_bypass | 10 | intenta saltarse restricciones |
| hallucination_check | 10 | detecta fabricaciones |
| contradiction_scan | 7 | lógica circular |
| scope_creep | 5 | excede objetivo |
| bias_detect | 5 | sesgos sistemáticos |
| determinism_check | 5 | ejecuciones no reproducibles |
| misc | 1 | cierre |

---

## 6. SISTEMA DE LOOPS AUTO-MEJORANTES (Recursive Self-Improvement)

### 6.1 Tres niveles de RSI

Nivel 1 (inner loop): mejora outputs en tarea específica
- Mecanismo: prompt iteration, tool selection, memory retrieval
- Métrica: outcome quality, latency, cost

Nivel 2 (outer loop): mejora los mecanismos del Nivel 1
- Mecanismo: Bilevel Autoresearch, meta-prompt optimization
- Métrica: mejora sostenida en Nivel 1

Nivel 3 (recursivo): modifica su propio código/harness
- Mecanismo: Gödel Agent (monkey patching), SICA (auto-edición)
- Métrica: mejora en Nivel 2 + safety constraints

### 6.2 Implementación de RSI (basado en Bilevel Autoresearch)

```
INNER LOOP (cada task):
1. Run task con mechanism M_i
2. Eval outcome score s_i
3. Keep/revert
4. Repeat

OUTER LOOP (cada N inner iterations):
1. Explore: review failure modes de inner loop
2. Critique: analyze why M_i failed
3. Specify: design new mechanism M_{i+1}
4. Generate: produce code/config para M_{i+1}
5. Test: validate M_{i+1} on held-out tasks
6. Adopt: if M_{i+1} > M_i, replace

SAFETY:
- Resource bounds (max code size, max test time)
- Reversibility (snapshot before change)
- Human-in-loop para cambios estructurales
```

### 6.3 Self-Diagnosis (clave del RSI según AEL arxiv 2604.21725)

AEL demostró que "self-diagnosis is the key enabler". Memoria sola mejora modestamente, reflexión produce salto cualitativo (27% Sharpe), pero cada mecanismo adicional degrada performance. La conclusión: hacer menos, hacer bien lo fundamental.

### 6.4 EvolveR Cognitive Skills (ICML 2026)

Agente destila experiencias en skills cognitivas:
- Online: agent ejecuta tarea, genera trajectory
- Offline self-distillation: revisa successes/failures, extrae patterns
- Library maintenance: dedup semántico, merge, score dinámico
- Strategy evolution: RL para aprender cuándo usar qué skill

---

## 7. ORQUESTADOR INTERNO (Trellis + 4 Work Groups)

### 7.1 4 Work Groups Aislados (estilo Claude Tag)

| Group | Scope | Permissions | Memory | Token Budget |
|---|---|---|---|---|
| A (Ingeniería) | GitHub + n8n + Linear + Datadog | default | A-Mem0 | 50K/día |
| B (Producto) | Notion + Figma + analytics + CRM | acceptEdits | B-Mem0 | 30K/día |
| C (Operaciones) | Slack + Jira + PagerDuty + observabilidad | auto | C-Mem0 | 40K/día |
| D (Estrategia) | research tools + datasets + benchmarks | plan | D-Mem0 | 60K/día |

Comunicación cross-scope: A2A protocol (JSON-RPC 2.0, Agent Cards)
Tools: MCP (filesystem, git, memory, sequential thinking, time)
Sandbox: Bubblewrap subprocess env scrub, sandbox.credentials

### 7.2 Permission Modes (6 Claude Code modes)

| Mode | Uso en MHYTOS |
|---|---|
| default | F5 Revisión (production) |
| acceptEdits | F3 Ejecución (coding iterativo) |
| plan | F1 Investigación, F6 Estrategia (exploración) |
| auto | F4 Mejoras (background async) |
| dontAsk | F4 cron jobs, scripts |
| bypassPermissions | Solo sandbox aislado, CI/CD |

### 7.3 Anti-Loop Guards (3 obligatorios)

1. MAX_STEPS=20 hard cap (por agente, por workflow)
2. Action dedup MD5 hash (tool_name, json_args con sort_keys)
3. External completion verifier (maker-checker pattern)

Extras producción:
- Per-tool quotas
- Server-side token budget (no confiar en agent)
- Structured error envelopes (status: no_results/error/ok)
- Tool-call entropy tracking
- Adversarial prompt testing

---

## 8. MODE ENVIRONMENT + MODE AMBIENT (Claude Code 2026)

### 8.1 Mode Environment (control runtime)

Plan Mode: read-only, Shift+Tab toggle, default para exploración
Background Tasks: /bg, /sessions, /switch ID, /end ID, /loop cron
Background Sessions: ctrl+B background, ctrl+F kill
Env Vars: CLAUDE_CODE_SUBPROCESS_ENV_SCRUB, CLAUDE_CODE_DISABLE_BACKGROUND_TASKS, CLAUDE_CODE_FORK_SUBAGENT, CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS
sandbox.credentials: v2.1.187, limita qué credenciales ve cada scope

### 8.2 Mode Ambient (proactividad)

Tres implementaciones:
1. Claude Tag Slack: surface info sin etiquetado, vigila umbrales
2. Claude Code ambient flag (v2.1.51+): habla por iniciativa en sesión
3. Background sessions detached: /bg manda a Agent View, sigue ejecutando

Para MHYTOS: F4 Mejoras Continuas opera en modo ambient. Trigger cuando threshold se cruza (test falla, métrica degrada, PR de Anthropic cambia formato). Aplica fix, mide 10min, persiste o revierte.

### 8.3 Subagents y Agent Teams

Subagent: instancia Claude con propio context window, system prompt, tools específicas, permisos. Built-in: Explore (Haiku, read-only), Plan (en plan mode, read-only), General-purpose (todas las tools). Límite: 10 paralelos. Foreground bloquea, background async.

Agent Teams: múltiples instancias que se comunican entre sí vía SendMessage({to: name}). Patrón "proyecto colaborativo" vs Subagents "jefe-empleado". Útil para discusión/debate.

---

## 9. ESTÁNDARES DE COMUNICACIÓN 2026

### 9.1 MCP (Model Context Protocol)

Anthropic, late 2024. JSON-RPC sobre stdio o HTTP+SSE. Tools: filesystem, git, memory, sequential thinking, time. 1899+ servers en producción. SDKs: TypeScript, Python, Rust, Swift, Kotlin, Go, C#.

### 9.2 A2A (Agent2Agent)

Google abril 2025, Linux Foundation junio 2025. JSON-RPC 2.0 sobre HTTPS. Agent Cards en /.well-known/agent.json. Tasks con lifecycle: submitted → working → input-required → completed/failed. Streaming con SSE. Multimodal. 100+ empresas. ACP de IBM se fusionó con A2A agosto 2025.

### 9.3 SKILL.md (cross-vendor, enero 2026)

YAML frontmatter (name, description, license, metadata, allowed-tools). 3 niveles de carga: metadatos al startup (30 tokens), instrucciones al activar (<5000 tokens), recursos solo cuando referenciados. Adoptantes: Claude Code, Cursor, VS Code Copilot v1.109, Gemini CLI, OpenAI Codex, LM-Kit.NET.

### 9.4 JSON Agents / PAM

JSON Schema 2020-12. Manifest universal para agent, capabilities, tools, runtimes, governance.

---

## 10. ADAPTIVE COMPLEXITY GATE (cierra el gap del 38% trivial)

### 10.1 Clasificación pre-loop

```
INPUT: task description, expected outcome, constraints
↓
CLASSIFIER (LLM + heuristics):
- TRIVIAL: <100 LOC, 1 tool, <5min human review
- SIMPLE: <500 LOC, 2-3 tools, 15min review
- COMPLEX: >500 LOC, multi-file, >1h review
- CRITICAL: production deploy, security, financial
↓
ROUTE TO:
- TRIVIAL → 1 fase (F3 directa), no sync
- SIMPLE → 3 fases (F2-F3-F5), sync cada 25
- COMPLEX → 6 fases, sync cada 10
- CRITICAL → 6 fases + meta-observer + bias, sync cada 5
```

### 10.2 Métrica Fija por Tarea

Cada plan (F2) debe incluir:
- success_criteria (qué indica que está terminado)
- measurement_method (cómo se mide)
- threshold (cuándo es aceptable)
- rollback_trigger (cuándo revertir)

Sin métrica fija, la tarea no se ejecuta.

---

## 11. ANTI-PATRONES Y BUGS CONOCIDOS

| Issue | Descripción | Workaround |
|---|---|---|
| langgraph #5790 | langgraph dev pierde memoria | Usar AsyncSqliteSaver en script directo |
| LangGraph no persiste en nodos | Solo entre nodos | External state store para in-node |
| Claude Code Read tool v2.1.127 | No sandboxed, lee /proc/self/environ | v2.1.128+ parchea, sandbox.credentials |
| $47K runaway loop (Tianpan) | Sin budget server-side | BUDGET server-side obligatorio |
| Mem0 vs Letta benchmark dispute | Benchmark quality cuestionada | No confiar en un solo benchmark |
| ACP deprecated agosto 2025 | Fusionado con A2A | Usar A2A directo |
| Reflection contamination | 17x amplificación errores | Reflector SEPARADO del Executor |
| Subagent infinite recursion | Subagente llama subagente | Max depth=1, hard limit |

---

## 12. STACK TECNOLÓGICO RECOMENDADO

| Componente | Librería | Versión | Justificación |
|---|---|---|---|
| State graph | langgraph | >=0.2 | cycles, persistence, interrupts, subgraphs |
| Durable execution | temporalio | >=1.5 | workflows, signals, activities, retry |
| Router | LiteLLM | >=1.5 | multi-model routing, fallback, A/B |
| Memory tier 1 | in-context (Claude prompt) | - | zero latency |
| Memory tier 2 | LangMem | latest | episodic + semantic memory |
| Memory tier 3 | graphiti-core + FalkorDB | >=0.5 | temporal knowledge graph |
| Vector store | faiss-cpu | >=1.7 | semantic search |
| Sandbox | RestrictedPython + AST | - | código execution |
| API | FastAPI | >=0.100 | async, type-safe |
| Queue | Redis | >=7 | tasks, cache, ephemeral state |
| DB | Postgres | >=15 | checkpointer, persistent state |
| Observability | OpenTelemetry + OpenLLMetry | latest | genai semantic conventions |
| Protocols | MCP SDK | >=0.5 | tool access |
| Protocols | A2A SDK | latest | agent-to-agent |
| Skills | SKILL.md format | - | cross-vendor portability |

### 12.1 Dependencias pip mínimas para MVP

```
langgraph>=0.2
langchain>=0.3
langchain-openai>=0.2
langchain-anthropic>=0.3
temporalio>=1.5
litellm>=1.5
graphiti-core>=0.5
falkordb>=0.4
langmem>=0.0.1
faiss-cpu>=1.7
fastapi>=0.100
redis>=5
psycopg>=3.1
sqlalchemy>=2.0
pydantic>=2.0
pydantic-ai>=0.1
asyncio>=3.10
opentelemetry-api>=1.20
opentelemetry-sdk>=1.20
traceloop-sdk>=0.1
restrictedpython>=7
```

---

## 13. ESTRUCTURA DE DIRECTORIOS OBJETIVO

```
/workspace/sistema-orquestador/
├── orquestador-auditor/              # CAPAS 0, 1, 6, 8
│   ├── harness/                      # 12 patterns implementation
│   │   ├── persistent_instruction.py
│   │   ├── scoped_context.py
│   │   ├── tiered_memory.py
│   │   ├── dream_consolidation.py
│   │   ├── progressive_compaction.py
│   │   ├── explore_plan_act.py
│   │   ├── subagent_manager.py
│   │   ├── fork_join.py
│   │   ├── tool_expansion.py
│   │   ├── risk_classifier.py
│   │   ├── single_tool.py
│   │   └── lifecycle_hooks.py
│   ├── langgraph/                     # CAPA 1
│   ├── temporal/                      # CAPA 0
│   ├── refutation/                    # CAPA 6
│   ├── meta_observer/                 # CAPA 8
│   └── bias_injector/
├── cerebro/                          # CAPAS 3, 4, 5
│   ├── mhydos_engine.py              # coordinator
│   ├── maxbry.py                     # ya existe (brain)
│   ├── pecp.py                       # ya existe (spec)
│   ├── phases/
│   │   ├── f1_investigacion.py
│   │   ├── f2_planificacion.py
│   │   ├── f3_ejecucion.py
│   │   ├── f4_mejoras.py
│   │   ├── f5_revision.py
│   │   └── f6_estrategia.py
│   ├── memory/                        # CAPA 4
│   │   ├── core.py
│   │   ├── recall.py
│   │   └── archival.py
│   ├── experience_graph/             # CAPA 5
│   │   ├── trellis.py
│   │   ├── trajectories.py
│   │   ├── principles.py
│   │   └── queries.py
│   └── adaptive_gate.py              # complexity classifier
├── fichas/                           # estado persistente
│   ├── playbook/                     # ACE-style
│   ├── grafo.py                      # graphiti wrapper
│   ├── slot_contracts/                # ya existe
│   └── state.db
├── router/                           # CAPA 2
│   ├── moe_selector.py
│   ├── cooldown.py
│   └── litellm_router.py
├── frontend/
├── comunicacion-externa/
│   ├── mcp_servers/                   # filesystem, git, memory, sequential-thinking
│   ├── a2a/                          # inter-agent protocol
│   └── claude_tag/                    # ambient mode integration
├── mejoras-continuas/                # CAPA 7
│   ├── bilevel.py
│   ├── evolve_r.py
│   └── auto_pr.py
├── observability/
│   ├── opentelemetry/
│   ├── langfuse/
│   └── genai_semantic/
├── agentes/                          # 9 agentes (4 Claude + 4 Mimo + Open Claw)
│   ├── claude/
│   ├── mimo/
│   ├── open_claw/
│   └── hermes/
├── skills/                           # SKILL.md files
│   ├── core/
│   ├── domain/
│   └── procedures/
└── investigacion-loops/              # investigación previa
    ├── vault/
    ├── grafos/
    ├── scripts/
    └── simulaciones/
```

---

## 14. CONTRACTS DE INTERFAZ (para programación)

### 14.1 Orchestrator Interface

```python
class Orchestrator(Protocol):
    async def classify_complexity(self, task: Task) -> Complexity
    async def plan(self, task: Task) -> Plan
    async def execute(self, plan: Plan) -> ExecutionResult
    async def review(self, result: ExecutionResult) -> Review
    async def improve(self, observations: list[Observation]) -> Improvement
    async def sync_experience_graph(self) -> None
    async def refutate(self, output: PhaseOutput) -> RefutationScore
    async def meta_observe(self) -> MetaObservation
```

### 14.2 Phase Interface (las 6 fases MHYTOS)

```python
class Phase(Protocol):
    name: str
    tier_1_state: CoreMemory
    tier_2_state: RecallMemory
    tier_3_state: ArchivalMemory

    async def run(self, input: PhaseInput) -> PhaseOutput
    def metrics(self) -> dict[str, float]
    def is_healthy(self) -> bool
```

### 14.3 Harness Pattern Interface

```python
class HarnessPattern(Protocol):
    name: str
    category: Literal["memory", "workflow", "tools", "automation"]

    def apply(self, context: HarnessContext) -> HarnessContext
    def validate(self) -> bool
    def metrics(self) -> dict[str, float]
```

### 14.4 Experience Graph Interface

```python
class ExperienceGraph(Protocol):
    async def record_trajectory(self, traj: Trajectory) -> None
    async def record_principle(self, p: Principle) -> None
    async def query_similar(self, task: Task) -> list[Trajectory]
    async def consolidate(self) -> None  # dream consolidation
    async def validate_principles(self) -> None
    def stats(self) -> GraphStats
```

### 14.5 Loops Interface

```python
class Loop(Protocol):
    name: str
    max_steps: int
    dedup_strategy: DedupStrategy
    completion_check: Callable[[State], bool]

    async def run(self, state: State) -> State
    async def step(self, state: State) -> State
    def should_continue(self, state: State) -> bool
```

---

## 15. MÉTRICAS DE ÉXITO (para evaluar el sistema implementado)

### 15.1 Loop Efficiency

- Iteraciones productive/wasted: target ≥90% (cerrar el gap del 38% trivial)
- Iteraciones con repeat detection: <5%
- Iteraciones con HITL trigger: <10%

### 15.2 Cost & Time

- Cost per consensus decision: track server-side
- Time to first useful output: <5min (F1-F3)
- Mean iterations to completion: <3

### 15.3 Memory

- Memory hit rate: ≥80% facts retrieved correctly from archival
- Experience graph query latency: <500ms p99
- Cross-scope isolation: 0 leaks en 100 simulaciones

### 15.4 Ambient Mode

- Response latency desde threshold trigger hasta fix: <30s
- Background session uptime: 99.9% over 7-day continuous run
- Auto-improvement gain: ≥10% en 4h window

### 15.5 RSI (Recursive Self-Improvement)

- Inner loop improvement rate: ≥5% per 100 iterations
- Outer loop adoption rate: ≥30% proposals accepted
- Safety: 0 irreversible regressions

---

## 16. COMANDOS OPERATIVOS (referencia para testing)

```bash
# Arranque del sistema
./start-mhytos.sh --scope=engineering --mode=ambient --permission=default --memory-tier=full

# Iteración de fase específica
./iterate.sh --phase=research --iterations=10 --max-cost=20

# Auditoría
./audit.sh --role=refutador --questions=50 --output=markdown

# Simulación de escenarios
./simulate.sh --scenarios=100 --output=json

# Escalación de work groups
./scale.sh --scopes=A,B,C,D --sync-interval=10

# Validación de experience graph
./validate-graph.sh --trellis --principles --trajectories
```

---

## 17. ESTADO HONESTO (qué existe vs qué falta)

### Existe
- 7 documentos markdown en vault (diseño)
- 1 grafo JSON con 51 entidades, 59 relaciones
- 4 inventarios de librerías reales
- 100 simulaciones documentadas
- 1 script validador (3/4 checks)
- 5 documentos finales
- 9 skills (definidos, no implementados)
- 250+ fuentes reales verificadas

### No existe (gaps)
- Código ejecutable de las 6 fases
- LangGraph StateGraph compilado
- graphiti-core conectado en vivo (FalkorDB no instalado)
- Refutation engine con LLM-as-judge real
- 11 perfiles de agentes (simulaciones de Mavis, la única real)
- 90 SKILL.md files (definidos 9, faltan 81)
- Bilevel Meta-Loop funcional
- Dynamic Workflows de Claude Code
- Experience Graph Trellis-style en producción

### Verificable en industria
- 12 Harness Patterns de Bilgin Ibryam
- LangGraph orchestrator-worker + Send API + interrupt
- MCP servers (filesystem, git, memory, sequential thinking)
- A2A protocol (Linux Foundation)
- SKILL.md cross-vendor
- Memory tier 1/2/3 (Claude, Letta, Mem0, Zep/Graphiti)
- 6 permission modes de Claude Code
- Anti-loop guards (MAX_STEPS, dedup MD5, external verifier)

---

## 18. RESUMEN EJECUTIVO

El sistema es programable en 4 capas independientes:

1. **Harness (12 patterns)**: el modelo solo no es confiable. Necesita Persistent Instruction File, Scoped Context, Tiered Memory, Dream Consolidation, Progressive Compaction, Explore-Plan-Act, Context-Isolated Subagents, Fork-Join, Progressive Tool Expansion, Command Risk Classification, Single-Purpose Tool Design, Deterministic Lifecycle Hooks. Estos 12 patterns son bloques constructivos con interfaces claras.

2. **Memory (3 tiers + Experience Graph)**: Core en contexto (RAM), Recall con índice (cache), Archival como grafo relacional de trajectories + principles. El grafo se construye online durante ejecución y se consolida offline entre sesiones. Trust boundary estricto en writers.

3. **Workflow (Orchestrator-Worker)**: Main agent sostiene contrato, workers context-isolated ejecutan en paralelo, fork-join para concurrencia, explore-plan-act para separación de responsabilidades, entropy management para mantener al orchestrator en control.

4. **Loops (10 niveles + 6 fases)**: Jerarquía operacional que vigila, ejecuta, valida y recupera. 6 fases de pensamiento paralelo que investigan, planifican, ejecutan, mejoran, revisan y generan estrategia. Anti-loop guards obligatorios: MAX_STEPS, dedup MD5, external verifier.

Para programación: cada pattern es un módulo, cada fase es una async function, cada nivel es un nodo LangGraph, el experience graph es una tabla en FalkorDB con schema fijo. Los contratos de interfaz (sección 14) son la API que conecta todo.

Honestidad: 11 perfiles son simulaciones de Mavis, la única real. Bugs conocidos documentados (langgraph #5790, Claude Code Read tool, reflection contamination). Benchmarks disputados (Mem0 vs Letta). Lo que no se ha medido: si el RSI 100x se mantiene en producción real, no en simulación.
