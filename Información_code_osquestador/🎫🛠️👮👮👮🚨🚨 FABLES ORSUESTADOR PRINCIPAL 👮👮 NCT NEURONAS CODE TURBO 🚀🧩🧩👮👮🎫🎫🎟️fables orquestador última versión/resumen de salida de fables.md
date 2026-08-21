Fables análisis del orquestador MAXBRY y agente TEAM 

# ✅ ANÁLISIS COMPLETO — 3 PASADAS × 30 DOCUMENTOS

**PASADA 1 (inventario literal):** 33 archivos leídos. 3 duplicados exactos detectados (`03-LOOPS-1`=`03-LOOPS`, `04-INSTRUCCIONES-1`=`04`, `paso2_etapa1-1`=`paso2_etapa1`) → 30 únicos.

**PASADA 2 (coherencia cruzada) — 8 conflictos detectados y resueltos:**

| # | Conflicto | Resolución (fuente ganadora) |
|---|---|---|
| 1 | Repos: 13 raíces vs 8 vs 14 | **15 repos** (GUÍA_D + Sentinela). Doc 02 (8 repos) aporta el detalle interno de auditor/Obsidian/Graphiti que GUÍA_D no tenía → se fusiona |
| 2 | Escala DRE fija vs escalable | **20-50/100-300/300-800/800-1000** (CHECKPOINT + GUÍA_C) |
| 3 | MYTHOS vs Capa B expertos | **Doble vía:** RAPIDO/BASICO=MYTHOS directo; AVANZADO/TURBO=expertos G2 (GUÍA_A1 GAP4) |
| 4 | Micro-agentes 12 vs 15 | **15** (GRUPO_F añade MA-BUILD/BUILD-EXEC/RUNTIME-CHECK) |
| 5 | Executor [24]: trío Escritor/Runtime vs Loader/Verifier/Executor | **Ambos:** Loader/Verifier/Executor = motor de fichas; Escritor+Runtime = vía de código nuevo |
| 6 | Loops 10 niveles vs Loop Engine 4 niveles | **Coexisten:** LOOPS-INFRA (10 niveles: heartbeat/DLQ/signals) ≠ LOOP-ENGINE (cognitivo 4×9 fases) |
| 7 | 3 etapas en `fichas/` vs 3 Cognitive Fabrics | **Convergen:** son la misma división P1/P2/P3 — se unifica como principio organizador |
| 8 | Pipeline JUEZ P09/P10/P13 | Ya cerrado en PARCHE (14 pasos) |

**PASADA 3 (gaps abiertos):** schema completo de `state.json` · formato CRAZY WALL · Fusion Engine · Snapshot→Commit de memoria · compilador DSL→Python · generador del atlas HTML (10-50 docs) · Control Plane config · wiring cerebro→loop→expertos.

---

# 🎯 MEJORAS 100X (integradas al diseño)

1. **1 fuente de verdad ejecutable:** el DSL DAG genera automáticamente los 10-50 HTML + MD + Mermaid. Editas el DSL → se regenera todo el atlas. Cero desincronización diseño/docs/código.
2. **Kernel de 6 responsabilidades** (~3.000 LOC): recibir → activar pipeline → crear expertos → compartir estado → consolidar → emitir. No investiga, no programa, no valida.
3. **1 Cognitive Engine + N expertos de 0 LOC:** expertos = archivos YAML (config) que instancian el mismo motor. Mejoras el motor → mejoran los 300.
4. **Expert Pool dinámico (MoE software):** router activa 15 o 300 según DRE, nunca números fijos.
5. **Expertos nunca llaman agentes:** emiten `{"necesito": [...]}` → Router+Registry resuelven por capability.
6. **Memoria transaccional:** Snapshot → expertos escriben solo `proposals` → Fusion Engine → Commit único. 1000 expertos en paralelo sin colisión.
7. **Salida como subsistema:** OutputContract declarado antes de generar + 10 checks binarios (E-OUT-001..010) + 1 retry de reparación + Output Diff vs goal. Nada sale sin 10/10 PASS.
8. **Audit Bus transversal** con puntos marcados: OCR-Baidu (solo INPUT) · Graphiti (todas las fases) · Obsidian (PROCESS→salida) · Hallucination-check con sampling (PROCESS→salida) · log hash-chained.
9. **Sheriff formal:** GCL-lite O(1) en cada paso + SlotContract SC1-SC6 + Z3 gate final P13.
10. **Grafo condicional (LangGraph-style):** edges con condición `confidence<0.6 → escalar`; no pipeline lineal.
11. **Spawning TDAG:** si falta un experto, el pool lo genera ad-hoc desde plantilla DSL.
12. **TDD obligatorio en ejecución** (TDFlow) + review 5-lentes paralelo + sandbox Docker/worktrees.

---

# 🧠 DISEÑO KERNEL v3 (estructura en texto libre)

```
MAXBRY KERNEL v3 (microkernel ~3.000 LOC)
│
├─ IDENTIDAD (inmutable): ADN 14 reglas · Guardian 6 checks · LLM_JUEZ (P-DISCOVER→P13)
│
├─ FASE 1 — INPUT COGNITIVE FABRIC (hasta 100 expertos dinámicos)
│   Anchor(clasifica+pregunta+investiga en paralelo) → PUSH_PING 30
│   → OCR Baidu → Filtros axiomáticos A2 (bloqueante) → Normalización
│   → Descomposición → GOAL_LOCK → Task Graph + Knowledge Pack
│   AUDIT: 🔍 OCR+Graphiti | SHERIFF: GCL-lite | LOOPS: FASE_0-2 | GOALS: lock
│
├─ FASE 2 — EXECUTION COGNITIVE FABRIC (hasta 300 expertos dinámicos)
│   PipelineController elige modo: RAPIDO(MYTHOS)|BASICO|AVANZADO|TURBO(enjambres G2)
│   → Loop Engine aislado (repo 3, escalado dinámico)
│   → Consenso 5+Devil → Escritor+Runtime (código) / Loader+Verifier+Executor (fichas)
│   → Team Agente en paralelo (asyncio.gather, staff externo primero)
│   AUDIT: Graphiti+Obsidian+Hallucination | SHERIFF: SC1-SC5+Z3(goal_lock)
│   PARALELO: parallel_groups DAG | EXPERTOS: pool | SENTINELA: observa métricas
│
├─ FASE 3 — OUTPUT COGNITIVE FABRIC (hasta 100 expertos dinámicos)
│   OutputContract → Planner → Builder → 10 checks binarios E-OUT
│   → Repair(1 retry) → Output Diff vs goal → Final Judge → Formatter
│   AUDIT: Obsidian+Graphiti+hash-chain | SHERIFF: SC6+GCL v1.0 Z3 gate final
│
└─ TRANSVERSALES (sobre las 3 fases)
    CEREBRO: state.json+crazy_wall+checkpoints (hash chain)
    ROUTER: repo 10, capability-based, ciego al provider
    COMUNICACIÓN: Event Bus 3 canales + Enchufe Universal v1.5 + DLQ
    MEMORIA: Global(RO)→Snapshot→Local→Fusion→Commit + 4 tiers
    LOOPS-INFRA: 10 niveles (heartbeat/signals/DLQ/escalation)
    SENTINELA: repo 15, mejora método, nunca cerebro, aprueba Director
```

**TEAM AGENTE:** mismo esquema 3 fases en miniatura. Cerebro ≤300 LOC (core+pipeline_selector+multitask_scheduler) → INPUT recibe handoff firmado → PROCESS ejecuta staff en paralelo (micro-agente MA-* solo si falta capability) → OUTPUT valida con Witness (Evidence L1-L4) y devuelve firmado.

---

# 🔧 SISTEMA DE EXPERTOS (diseño)

```
EXPERT_POOL (500 disponibles, 0 activos en reposo)
├─ cognitive_engine.py      ← EL único cerebro (1.500-3.000 LOC)
├─ expert_contract v1.0     ← schema-in/schema-out, non_scope, anti-echo <30%
├─ experts/*.yaml           ← E001-E300 = solo configuración (0 LOC)
│    expert_id: E017 | pipeline: planning | temperature: 0.4 | skills: [...]
├─ router_experts.py        ← activa por operación cognitiva, no por dominio
├─ spawner.py               ← TDAG: crea experto ad-hoc si no existe
├─ fusion_engine.py         ← dedup + contradicciones + confianza + síntesis
└─ jueces 3 niveles         ← Local(enjambre)→Capa→Central(E296=LLM_JUEZ)
Consenso ponderado: 0.35·accuracy + 0.30·evidencia + 0.20·contexto + 0.15·recencia
```

---

# 📦 CÓDIGO: DSL DAG SCHEMA SHERIFF (estructura, agentes eliminados)

Tomo tu `diagrama_dsl_pipeline.py` (base aprobada), **quito el campo `agentes`**, integro los prompts/métodos como nodos y lo extiendo así:

```
maxbry_dsl/
├── schema.py        # @dataclass Nodo (patrón árbol ejecutable, 7 preguntas):
│     id, nombre, tipo(Enum), fase(P1|P2|P3),
│     que_hace: str            # 2-3 líneas
│     microflujo: list[str]    # Entrada➜Evaluar➜Ejecutar➜Verificar➜Salir
│     programacion: list[str]  # [AsyncIO, FSM, DAG, Pydantic, Scheduler...]
│     raiz: dict               # {"📂": "/input/loops/", files:[loop_manager.py,...]}
│     dependencias: list[str]  # [EventBus, Goals, Sentinela, EstadoGlobal]
│     consume / produce: dict  # schemas (enchufe v1.5)
│     audit_points: list       # [OCR|GRAPHITI|OBSIDIAN|HALLUCINATION]
│     metricas: list           # [tiempo, errores, reintentos]
│   @dataclass Arista: desde, hacia, condicion  # "CONF>=0.6", "FALLA→REPAIR"
│   @dataclass Fase: id(P1|P2|P3), nodos[], overlays{cerebro,router,comunicacion}
├── sheriff.py       # valida: DAG acíclico + jsonschema strict + GCL-lite
│                    # + SC1-SC6 + toda arista con condición válida
├── pipeline_p1.py   # DAG INPUT   (Anchor→PushPing→OCR→Axiomas→GoalLock)
├── pipeline_p2.py   # DAG PROCESS (Controller→LoopEngine→Consenso→Ejecución)
├── pipeline_p3.py   # DAG OUTPUT  (Contract→Builder→10 checks→Repair→Judge)
├── pipeline_team.py # DAG Team Agente (mini 3 fases)
├── exporters.py     # render_texto() + mermaid() + html_atlas() + md_atlas()
│                    # ← genera los 10-50 HTML automáticamente desde el DAG
└── run.py           # compila, valida con sheriff, exporta atlas completo
```

Cada rama del árbol (Router, Goals, Loops, Sentinela, Expertos, Memoria, Auditoría, OCR, Graphiti, Obsidian, EventBus, Scheduler, Retry, CircuitBreaker, Cache, Logging) = 1 `Nodo` con las 7 respuestas. El atlas HTML se **genera**, no se escribe a mano.

---

# 📋 PLAN DE SALIDAS PARA SONNET (10 documentos de instrucciones)

| Salida | Contenido | Repos |
|---|---|---|
| S1 | Enchufe Universal v1.5 + todos los contracts/schemas + state.json + crazy_wall | 12 |
| S2 | Kernel v3: 6 responsabilidades + ADN/Guardian/Juez/Recovery | 1 |
| S3 | **DSL DAG Schema Sheriff completo** + generador atlas HTML/MD | 2 |
| S4 | FASE 1 Input Fabric (Anchor+PushPing+A1-A5+OCR) | 6 |
| S5 | FASE 2: Cognitive Engine + Expert Pool + Fusion + consenso + wiring Loop Engine | 5,6,3 |
| S6 | FASE 3 Output Fabric (OutputContract + 10 E-OUT + Repair + Diff) | 6 |
| S7 | Team Agente (cerebro ≤300 LOC + pipelines + staff + 15 MA-*) + Escritor/Runtime | 7,8,9 |
| S8 | Memoria (4 tiers + Snapshot→Fusion→Commit + event sourcing + KG) | 11 |
| S9 | Audit Bus (Obsidian+Graphiti+Baidu OCR+hash chain) + Sheriff (GCL/Z3/SC) | 4,1 |
| S10 | Sentinela + Loops-Infra 10 niveles + integración Router | 15,10 |

Cada salida incluirá: goals, árbol de archivos con LOC máx, contratos I/O, orden de construcción, tests de aceptación y prohibiciones — listo para pegar a Sonnet/Claude Code.

**SÍ O NO:** ¿genero SALIDA 1 (Enchufe + Contracts + state.json + crazy_wall)?

# 📏 LOC DEL CEREBRO (con separación modular máxima)

**ORQUESTADOR — Kernel/cerebro: ~2.000-3.000 LOC**

| Módulo | LOC |
|---|---|
| core.py (6 responsabilidades: recibir→activar→crear→estado→consolidar→emitir) | ~300 |
| ADN + Guardian (14 reglas + 6 checks) | ~350 |
| LLM_JUEZ (estados + pipeline P-DISCOVER→P13) | ~600 |
| Auto-Recovery (watchdog + replay checkpoint) | ~400 |
| Loader de pipelines DSL + dispatcher | ~300 |
| State reader/writer (hash chain) | ~250 |
| Enchufes/wiring a módulos externos | ~300 |

**TEAM AGENTE — cerebro: ~300 LOC** (ya confirmado)
- core.py ≤100 · pipeline_selector ≤80 · multitask_scheduler ≤120

**Lo que crece SIN tocar el cerebro:**

| Fuera del cerebro | LOC crece hasta |
|---|---|
| Expertos (YAML config, 0 código) | ∞ (300→500→1000) |
| Pipelines DSL/DAG (archivos declarativos) | ilimitado |
| Fichas + micro-agentes MA-* (≤200 c/u) | ~8.000+ |
| Loop Engine aislado | ~1.500 |
| Cognitive Engine (1 solo, mejora a todos) | ~2.500 |
| Router / Memoria / Audit / GCL | ~8.000 |

**Total sistema: ~34.000 LOC. Cerebro: solo ~7-9% del total.**

Clave: el cerebro nunca crece — crecen los archivos de configuración, pipelines y fichas que él carga. Mejorar el sistema = añadir YAML/DSL, no editar el kernel.

¿Genero SALIDA 1?

**SALIDA 1/6 lista** — Kernel núcleo: `adn_system.py` (150) + `guardian_layer.py` (180) + `kernel_core.py` (380). Cerebro con las 6 responsabilidades exactas, enchufes por `Protocol` (cero imports lejanos), snapshot→commit, retry+checkpoint por fase.

**Plan confirmado (19 salidas, todas MD):**

| Código (6) | Contenido |
|---|---|
| ✅ S1 | ADN + Guardian + Kernel Core |
| S2 | LLM_JUEZ + Auto-Recovery 5 niveles |
| S3 | State Engine (state.json + crazy_wall + hash chain + snapshot/commit) |
| S4 | DSL DAG Schema Sheriff + pipelines P1/P2/P3 |
| S5 | Cognitive Engine + Expert Pool + Fusion Engine |
| S6 | Team Agente completo (cerebro ≤300 + pipelines + staff) |

Luego S7-S19: instrucciones Sonnet (contracts/enchufe, Input Fabric, Output Fabric, Escritor/Runtime, memoria 4 tiers, audit bus Obsidian/Graphiti/OCR, GCL/Z3/SC, Router, Sentinela, loops-infra, micro-agentes, atlas HTML, integración final).

¿Continúo con SALIDA 2?


**SALIDA 2/6 lista** — `juez_core.py` (390: pipeline 16 pasos, anti-humo determinista, verificación Evidence Report con recálculo de hash) + `failure_registry.py` (200: JSONL hash-chained, few-shot para Escritor) + `recovery_engine.py` (380: watchdog 30s, Causal Engine declarativo, escalera 5 niveles con Guardian).

¿Continúo con SALIDA 3 (State Engine: state.json + crazy_wall + snapshot→fusion→commit)?




