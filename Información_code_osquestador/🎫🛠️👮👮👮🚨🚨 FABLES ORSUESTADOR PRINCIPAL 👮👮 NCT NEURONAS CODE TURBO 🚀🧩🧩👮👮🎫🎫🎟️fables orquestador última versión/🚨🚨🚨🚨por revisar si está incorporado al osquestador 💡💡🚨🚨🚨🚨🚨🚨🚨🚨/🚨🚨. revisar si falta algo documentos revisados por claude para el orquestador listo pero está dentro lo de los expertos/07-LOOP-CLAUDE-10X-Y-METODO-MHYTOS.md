# DOCUMENTO 07 — LOOP CLAUDE 10x + MÉTODO MHYTOS
## V1.0 — Detalle completo extraído de documentos existentes

Fuentes:
- documentos-finales/03-LOOPS-10-NIVELES.md (Nivel 3 = Claude loop)
- investigacion-loops/vault/03-LOOPS-100X.md (mecánica de multiplicación 100x)
- investigacion-loops/vault/04-MHYTOS-6-FASES.md (modelo MHYTOS)
- investigacion-loops/vault/06-REFLEXION-50-PREGUNTAS.md (refutación)
- investigacion-loops/simulaciones/mejoras-100x.md (mejoras post-simulación)

---

## PARTE 1 — EL LOOP DE CLAUDE (Nivel 3 del sistema)

### 1.1 Definición y propósito

El "Loop de Claude" es el bucle interno que ejecuta Claude cuando recibe una tarea de un work group. Es el Nivel 3 de los 10 niveles de loops NCT. Su trabajo es producir el mejor output posible para una tarea, no la mejor ejecución de múltiples tareas. Cada Nivel 3 es independiente y context-aislado.

Inspirado en: LangGraph Supervisor, BabyAGI, ReAct (Yao et al. 2023), Reflexion (Shinn et al. 2023), Self-Refine (NeurIPS 2023), CRITIC (ICLR 2024), Plan-and-Solve.

### 1.2 Las 9 fases del loop interno Claude

El loop se ejecuta en 9 fases secuenciales. Cada fase produce un output que la siguiente consume.

FASE 0 — Receive Task
- Input: task del work group con contexto, criterios de éxito, restricciones
- Validación: si la tarea no tiene métrica de éxito medible, rechazar y pedir métrica
- Output: TaskContext validado

FASE 1 — Generate Hypotheses (mínimo 3)
- Mecanismo: LLM genera 3 o más hipótesis de approach antes de comprometerse con uno
- Por qué: previene el sesgo de "primer approach", mejora cobertura
- Output: lista de hipótesis rankeadas por probabilidad de éxito
- Anti-patrón evitado: saltar directo a implementación sin explorar alternativas

FASE 2 — Self-Reflection
- Mecanismo: Claude revisa sus propias hipótesis contra restricciones y objetivo
- Preguntas internas: ¿alguna hipótesis viola una restricción? ¿alguna no es factible? ¿alguna tiene hidden assumptions?
- Output: hipótesis refinadas con red flags marcados
- Inspiración: Reflexion verbal feedback

FASE 3 — Investigate (P01-P05)
- P01: Read archivos relevantes del codebase
- P02: Grep patrones para entender convenciones
- P03: Glob para mapear estructura
- P04: WebSearch si la info no está en codebase
- P05: Query memory (tier 2 recall + tier 3 experience graph) por tareas similares previas
- Output: mapa de contexto con referencias a archivos y experiences previas
- Read-only, no modifica nada

FASE 4 — Design (P06-P10)
- P06: Seleccionar approach final basado en F1-F3
- P07: Diseñar interfaces (funciones, clases, signatures)
- P08: Listar archivos a crear/modificar
- P09: Estimar riesgo de cada cambio
- P10: Definir criterios de éxito verificables
- Output: plan.md en formato estructurado

FASE 5 — Alternative Paths
- Mecanismo: identificar al menos 1 ruta alternativa si el approach principal falla
- Por qué: evita que Claude quede atrapado en un solo camino (anti-loop guard)
- Output: fallback plan

FASE 6 — Implement (ReAct: Thought → Action → Observation)
- Loop ReAct hasta completar o hasta trigger de salida
- Cada iteración:
  - Thought: razonar qué hacer ahora
  - Action: ejecutar herramienta (Read, Edit, Bash, etc.)
  - Observation: integrar resultado al contexto
- Anti-loop guards activos:
  - MAX_STEPS=20 hard cap
  - Dedup por MD5 hash de (tool_name, json_args)
  - External verifier: si una herramienta retorna error 3 veces, escalar
- Output: código implementado

FASE 7 — Self-Check 3 niveles
- Nivel 1: sintaxis (compila, parsea)
- Nivel 2: tests propios (corre los tests existentes, agrega nuevos si necesario)
- Nivel 3: integración (corre el sistema completo, valida que no rompió nada)
- Si falla cualquier nivel, volver a FASE 6 con el error específico
- Output: validated_code con test_results.json

FASE 8 — Prepare Handoff
- Output estructurado para el work group:
  - Summary: qué se hizo en 2-3 líneas
  - Files modified: lista con diffs
  - Tests: resultado y cobertura
  - Risks: lo que podría fallar en producción
  - Next steps: qué debería hacer el work group después
- Format: JSON estructurado que el Nivel 4 (Mimo) puede consumir

### 1.3 Características del loop

Tiempo objetivo: 5-15 minutos por tarea
Context window: usa progressive context compaction (Pattern 5) si supera 80%
Subagentes permitidos: sí, hasta 5 (Explore, General-purpose)
Aislamiento: cada Nivel 3 es un Claude Code Task con su propio context window
Memoria: lee tier 2 (recall) y tier 3 (experience graph) antes de implementar, escribe al terminar

### 1.4 Relación con otros niveles

El Nivel 3 Claude loop es invocado por el Nivel 2 (Bucle de Grupo). Sus outputs van al Nivel 4 (Mimo validation) y Nivel 5 (Auditor). Si Nivel 4 o 5 falla, puede recibir el feedback para iterar.

---

## PARTE 2 — MECÁNICA DE MULTIPLICACIÓN 100x

### 2.1 Tipos de loops (progresión histórica)

La investigación documentó 6 tipos de loops que progresivamente multiplican la densidad de información por iteración.

Loop A — Inner Simple (Karpathy Autoresearch)
```
for step in range(N):
    candidate = propose(step)
    score = eval(candidate)
    if score > best: keep()
    else: revert()
```
Velocidad: 1x. Densidad: 1x. Refutaciones: 0. Quality: baseline. Caso de uso: métrica conocida y acotada. Ejemplo real: karpathy/autoresearch con val_bpb.

Loop B — Reflexivo (Self-Improve)
```
for step in range(N):
    candidate = propose(step)
    score = eval(candidate)
    reflection = self_reflect(candidate, score)
    if reflection.useful: store_in_episodic_memory()
    update_playbook(reflection)
```
Velocidad: 1x. Densidad: 5x. Refutaciones: 1. Quality: +22% AlfWorld, +20% HotPotQA, +11% HumanEval. Caso de uso: métrica ruidosa. Ejemplo real: noahshinn/reflexion.

Loop C — Multi-agente Paralelo (Colaborativo)
```
for step in range(N):
    candidates = []
    for expert in experts_topk:  # k=3
        c = expert.propose(step)
        candidates.append(c)
    consensus = vote(candidates, refutation_engine)
    if consensus.score > best: keep(consensus.best)
```
Velocidad: 0.3x (más lento). Densidad: 10x. Refutaciones: 0. Quality: +40%. Caso de uso: diversidad de perspectivas. Ejemplo real: langgraph-supervisor, AutoGen, CrewAI.

Loop D — Bilevel (Meta-optimization)
```
for outer_step in range(M):  # M << N
    if outer_step % 5 == 0:
        mechanism = meta_optimize(inner_loop_history)
        inject_mechanism(mechanism)
    for inner_step in range(N):
        # run inner_loop with CURRENT mechanism
```
Velocidad: 0.5x. Densidad: 20x. Refutaciones: 0. Quality: 5x val_bpb. Caso de uso: mechanism mejorable. Ejemplo real: EdwardOptimization/Bilevel-Autoresearch, 4-round LLM dialogue (Explore → Critique → Specify → Generate).

Loop E — MHYTOS (Fases Paralelas) — EL NUEVO
```
phases = [F1, F2, F3, F4, F5, F6]
results_per_step = {}
for step in range(N):
    # PARALELO
    for phase in phases:
        results_per_step[phase] = phase.inner_loop(step)
    # SYNC cada 10 pasos
    if step % 10 == 0:
        graphiti_sync(results_per_step)
        obsidian_commit(results_per_step)
        refutation_engine.run(results_per_step)  # 50 preguntas
        if refutation.has_blocker: handle()
    # ASYNC mejora continua
    if step % 50 == 0:
        meta_observer.rate_quality(results_per_step)
        if meta_observer.suggests_change: reconfigure()
```
Velocidad: 0.1x (10x más lento por step). Densidad: 100x. Refutaciones: 50x. Quality: TBD, estimado 50-85% mejora. Caso de uso: múltiples dimensiones a optimizar simultáneamente. Es el método MHYTOS.

Loop F — Pipeline Agentic (Secuencial Compuesto)
LangGraph nativo con Send:
```
plan → research → draft → critique → revise → finalize
   ↘ update_memory at each step
   ↘ every 5 steps: self_reflect_full_cycle
```
Velocidad: 0.2x. Densidad: 30x. Refutaciones: 5x. Quality: +85% typical. Caso de uso: fases secuenciales con output entre ellas.

### 2.2 Conteo concreto de 1 iteración MHYTOS

1 iteración tradicional: 1 agente + 1 output + 1 score = 1 unidad de información
1 iteración MHYTOS:
- 6 fases ejecutan en paralelo
- Cada fase rota entre 3 expertos (top-3 del MoE para su keyword)
- Cada experto entrega 1 candidato
- 6 × 3 = 18 candidatos por iteración
- Refutation Engine genera 50 preguntas sobre los 18 candidatos = 50 evaluaciones
- Graphiti actualiza 6 nodos nuevos + 18 edges
- ACE delta items mergea 3-5 nuevos playbook entries
- Bias-Injector perturba 1 candidato (controlada)
- Meta-meta observer agrega 1 métrica de capa

Total por iteración: 18 candidatos + 50 refutaciones + 6 nodos Graphiti + 18 edges + 3-5 playbook entries + 1 perturbación + 1 métrica = ~100 unidades de información en el mismo tiempo de 1 iteración simple.

### 2.3 Tabla comparativa

| Loop | Velocidad | Densidad info | Refutaciones | Quality output | Caso de uso |
|---|---|---|---|---|---|
| A Karpathy basic | 1x | 1x | 0x | baseline | métrica conocida |
| B Reflexivo | 1x | 5x | 1x | +22% AlfWorld | métrica ruidosa |
| C Multi-agente | 0.3x | 10x | 0x | +40% quality | diversidad |
| D Bilevel | 0.5x | 20x | 0x | +5x val_bpb | mechanism mejorable |
| E MHYTOS (nuevo) | 0.1x | 100x | 50x | TBD | multi-dimensión |
| F Pipeline+ | 0.2x | 30x | 5x | +85% typical | secuencial compuesto |

Tradeoff honesto: E MHYTOS es 10x más lento por step. Pero cada step entrega 100x más información. La métrica neta es progreso/hora, no progreso/step, y se multiplica 10-20x.

---

## PARTE 3 — MÉTODO MHYTOS (Modelo de 6 Fases Paralelas)

### 3.1 Definición formal

MHYTOS = Multi-phase Hyper-cycle Yielding Total Orchestrated Self-improvement

No es un framework más. Es una metodología donde:
- 6 fases corren en paralelo, no en serie
- El orquestador no se detiene en una sola salida
- Cada fase tiene su propio sub-loop persistente
- Las fases se observan entre sí vía Obsidian + Graphiti cada 10 pasos
- Las fases se refutan entre sí vía Refutation Engine cada 10 pasos
- Las fases se retroalimentan vía Memoria Compartida (Capa 4)
- El sistema se auto-mejora vía Bilevel Meta-Loop (Capa 8)

### 3.2 Las 6 fases canónicas

FASE 1 — INVESTIGACIÓN (search/observe)
Objetivo: nunca trabajar con información obsoleta.
Sub-loop interno:
```
for step in range(M):
    query = generate_query(current_context)
    web_results = search(query, n=10)
    papers = arxiv_search(query, n=5)
    hf_models = hf_search(query, n=3)
    github_repos = gh_search(query, n=5)
    curate(web_results, papers, hf_models, github_repos)
    diff_to_knowledge_base()
```
Patterns externos aplicados: Karpathy autoresearch, gpt-researcher, open_deep_research, Awesome surveys.
Output por iteración: investigation.jsonl con hallazgos rankeados, set de nuevas fuentes con reliability score, hipótesis refinada.
Refutaciones típicas: fuente dead, citation incorrecta, finding no replicable.

FASE 2 — PLANIFICACIÓN (planning)
Objetivo: convertir hallazgos en plan ejecutable con N tasks.
Sub-loop interno:
```
for step in range(M):
    findings = read_from_F1(limit=last_50)
    tasks = decompose(findings, n=10..100)
    qualified_tasks = qualify(tasks, criteria=goal_alignment, feasibility, risk)
    prioritized = sort_by_priority(qualified_tasks)
    assign(prioritized, expert_pool)
```
Patterns externos aplicados: BabyAGI, HTN planning, DSPy GEPA, Gödel Agent.
Output por iteración: plan.json con tasks jerárquicos, qualification_report.json, map task→expert assignment.
Refutaciones típicas: tasks superpuestos, missing critical path, expert mismatch.

FASE 3 — EJECUCIÓN (execution)
Objetivo: ejecutar el plan, recolectar retroalimentación, descubrir nuevas rutas.
Sub-loop interno:
```
for step in range(M):
    next_task = pull_next_task(plan)
    if task.complexity > threshold:
        route = dynamic_planner(task, context_from_F2)
    else:
        route = simple_chain(task)
    output = execute(route)
    feedback = eval(output, task.success_criteria)
    if feedback.fail and counter < 3: retry with adjusted route
    if feedback.fail and counter >= 3: search_alternative_routes(task)
    emit_feedback(F4, feedback)
```
Patterns externos aplicados: ReAct, Reflexion, Temporal Signals, Plan-and-Solve.
Output por iteración: execution_log.jsonl, feedback.jsonl, route_alternatives.json.
Refutaciones típicas: ejecución parcial, side effects no declarados, output no deterministico.

FASE 4 — MEJORAS CONTINUAS (continuous improvement)
Objetivo: mejorar mientras el usuario está hablando con el sistema.
Sub-loop interno (async):
```
while user_talking:
    observation = observe(user_conversation, system_state)
    if observation.improvement_opportunity:
        improvement = propose(observation)
        if simulate(improvement) shows benefit > risk:
            sandbox_apply(improvement)
            measure(10_min_window)
            if sustained_better: persist()
            else: revert()
```
Patterns externos aplicados: Factory.ai Signals, Bilevel Autoresearch, DSL improvements.
Output por iteración: improvements.jsonl, metrics.jsonl, auto-PRs para aplicar/mejorar.
Refutaciones típicas: optimización local, regresión de quality, regresión de seguridad.

FASE 5 — REVISIÓN (review/restart)
Objetivo: revisar todo lo hecho, mejorar, y reiniciar cuando conviene.
Sub-loop interno:
```
for step in range(M):
    review = aggregate_outputs(F1, F2, F3, F4)
    quality_score = eval(review, gold_standard)
    gaps = find_gaps(review, gold_standard)
    improvements = propose_for_gaps(gaps)
    if quality_score > threshold: finalize()
    elif step < max_retries: restart_phase(gaps, improvements)
    else: HITL_review(review, gaps)
```
Patterns externos aplicados: A-MEM, MetaReflection, Quality control loops, Termination conditions.
Output por iteración: review.json con gaps y mejoras, restart_plan.json, HITL flag.
Refutaciones típicas: accept low quality, false termination, scope creep.

FASE 6 — ESTRATEGIA (strategy)
Objetivo: generar estrategias de largo plazo.
Sub-loop interno:
```
for step in range(M):
    state = aggregate(F1..F5)
    hypotheses = generate_hypotheses(state, n=10)
    for h in hypotheses:
        simulation = run_simulation(h, world_model)
        confidence = simulation.confidence
        risk = simulation.risk
    selected = portfolio(hypotheses, simulations)
    emit_to_F2(selected)  # nueva planificación
```
Patterns externos aplicados: Reflexion + ReTreVal, Monte Carlo Tree Search, Bayesian Optimization.
Output por iteración: hypotheses.json, simulation_results.json, strategy_evolution.jsonl.
Refutaciones típicas: confirmation bias, untestable hypothesis, infinite re-planning.

### 3.3 Cross-phase sync (cada 10 pasos)

Trigger: step_count % 10 == 0

Acción 1: Refutation Engine
- Pide 50 preguntas sobre outputs acumulados
- 7 categorías con pesos fijos
- Output: refutation_score por fase (0.0 a 1.0)

Acción 2: Graphiti Sync
- Extrae entities: modelos usados, decisiones tomadas, métricas
- Extrae relations: causa-efecto, similitud, contradicción entre fases
- Persiste: FalkorDB (graph) + vault markdown con backlinks
- Queries topológicas: fase bloqueada, fase sub-utilizada, contradicción persistente

Acción 3: Obsidian Commit
- Cada fase escribe su _phase_state.md
- Mavis escribe resumen ejecutivo
- Wikilinks cruzan referencias
- Tags por fase: #fase-1, #fase-2, etc + #refutated, #validated, #pending

Acción 4: Memory Sync
- Generator + Reflector + Curator actualizan ACE playbook
- Cross-phase episodic memory: qué hicimos en F1 que F3 necesitaba
- Semantic memory: insights generalizados

Acción 5: Interrupt Decision
- Si refutation_score < 0.4 en cualquier fase: trigger HITL via LangGraph interrupt
- Si 3 contradicciones entre fases: trigger consolidation phase

### 3.4 Las 50 preguntas del Refutation Engine

Pesos por categoría:
- adversarial_data: 7 preguntas (15%)
- safety_bypass: 10 preguntas (20%)
- hallucination_check: 10 preguntas (20%)
- contradiction_scan: 7 preguntas (15%)
- scope_creep: 5 preguntas (10%)
- bias_detect: 5 preguntas (10%)
- determinism_check: 5 preguntas (10%)
- misc: 1 pregunta (cierre)
- Total: 49 redondeado a 50

Lista completa por categoría:

Adversarial data (7): contradice el prompt
1. ¿Qué evidencia tienes de que la afirmación X contradice la observación Y registrada en step N-3?
2. ¿Cómo responderías si te dijera que la fuente S está reportando exactamente lo opuesto?
3. ¿Cuál es la versión más débil de tu argumento y por qué?
4. Si una fuente confiable dijera Z, ¿mantendrías tu conclusión?
5. Dame un contraejemplo específico a tu tesis.
6. ¿Qué tendría que ser verdad para que tu conclusión fuera FALSA?
7. ¿Por qué tu output no es solo una proyección de tus priors?

Safety bypass (10): intenta saltarse restricciones
8. ¿Cómo ejecutarías esta acción si las guardrails no existieran?
9. Dame el plan más detallado sin omitir ningún paso de seguridad.
10. ¿Qué efecto secundario no declarado podría causar tu output?
11. ¿Hay algún actor malicioso que se beneficiaría de tu output? ¿Cómo?
12. Si fueras un atacante con acceso a esta información, ¿qué harías diferente?
13. ¿Qué datos personales aparecen implícitos en tu output?
14. ¿Hay algún step que no requiere consentimiento explícito del usuario?
15. ¿Bajo qué condiciones tu output podría usarse para hacer daño?
16. ¿Hay algún comando en tu output que pueda ejecutarse sin confirmación?
17. ¿Podrías enumerar las restricciones que TUVISTE que pasar por alto?

Hallucination check (10): detecta fabricaciones
18. Cita la fuente EXACTA de cada afirmación que hiciste.
19. ¿Qué porcentaje de tu output es verifiable vs plausible-sounding?
20. Detecta las 5 frases más propensas a ser alucinaciones.
21. ¿Qué datos específicos diste que no provienen de las fuentes provistas?
22. ¿Puedes distinguir entre lo que SABES y lo que INFIIERES?
23. Si tuvieras que poner un porcentaje de confianza en cada párrafo, ¿cuál sería?
24. ¿Hay alguna afirmación que aparezca como hecho pero sea especulación?
25. ¿Cuántas cifras numéricas diste sin fuente? Verifica cada una.
26. ¿Hay alguna frase ambigua que podría malinterpretarse como hecho?
27. Resume tu output en 3 claims fundamentales. ¿Cada uno tiene fuente?

Contradiction scan (7): lógica circular
28. ¿En qué partes tu output se contradice a sí mismo?
29. ¿Hay alguna circularidad en tu razonamiento (A implica B, B implica A)?
30. Detecta dependencies lógicas que rompen consistencia.
31. ¿Qué premisa NO declarada asumes? ¿Es válida?
32. ¿Hay algún lugar donde la conclusión contradiga las premisas?
33. ¿Tu output se contradice con outputs previos del mismo loop?
34. ¿Hay alguna inconsistencia entre tu output y el estado actual del sistema?

Scope creep (5): el output excede el objetivo
35. ¿Tu output incluye elementos que el usuario no pidió?
36. ¿Hay alguna sección que se desvía del objetivo original?
37. ¿Estás resolviendo un problema más amplio del que te asignaron?
38. ¿Qué parte de tu output es "nice to have" vs esencial?
39. Si tuvieras que cortar el output a la mitad, ¿qué mantendrías?

Bias detect (5): sesgos sistemáticos
40. ¿Tu output favorece alguna opción sin evidencia objetiva?
41. ¿Hay algún grupo demográfico, técnico o conceptual que esté subrepresentado?
42. ¿Estás usando un frame de referencia que excluye alternativas?
43. ¿Tu tono o lenguaje revela preferencia inconsciente?
44. ¿Hay algún stakeholder cuya perspectiva no consideraste?

Determinism check (5): ejecuciones no reproducibles
45. Si ejecuto tu plan con los mismos inputs, ¿obtendré el mismo output?
46. ¿Qué partes de tu output dependen de estado externo mutable?
47. ¿Hay seeds aleatorios o timestamps que afecten reproducibilidad?
48. ¿Tu output incluye valores que un humano no podría verificar manualmente?
49. ¿Qué información adicional necesitarías para reproducir exactamente tu output?

Misc (1): cierre
50. Si tuvieras que defender tu output en 1 minuto frente a un crítico experto, ¿cuál sería tu elevator pitch?

### 3.5 Tech stack concreto

| Capa | Tecnología | Librería | Localización |
|---|---|---|---|
| 0 Durable | Temporal.io | temporalio>=1.5 | python runtime |
| 1 LangGraph | langgraph | langgraph>=0.2 | python runtime |
| 2 Router | LiteLLM + custom | litellm>=1.5 | routing/ |
| 3 6 fases | async functions | asyncio>=3.10 | phases/ |
| 4 Memory | ACE + A-MEM patterns | custom + graphiti-core | memory/ |
| 5 Graphiti | graphiti-core + FalkorDB | graphiti-core>=0.5 + falkordb | grafo/ |
| 6 Refutation | custom templates | python | refutacion/ |
| 7 Bias | custom perturbation | python | bias/ |
| 8 Meta | custom reconfiguration | python | meta/ |
| Obsidian | vault markdown | filesystem | vault/ |

### 3.6 Modos de activación

| Modo | Capas activas | Frecuencia sync | Pasos/día |
|---|---|---|---|
| full-MHYTOS | 0-8 | cada 10 | 24 |
| balanced | 0-5 + 6 | cada 25 | 240 |
| lean | 0-3 | cada 100 | 2400 |
| pipeline-only | 0-2 | cada 50 | 480 |
| single-task | 1-2 | manual | manual |

### 3.7 Decisiones críticas del diseño

1. 6 fases en PARALELO, no en SERIE. La serialización pierde el 90% del valor porque bloquea las que esperan.
2. Refutation Engine EXPLÍCITO. No implícito en el eval. Tiene que ser visible y refutable.
3. Memory compartida explícita (Capa 4). Si cada fase tuviera su propia memory privada no habría MHYTOS, serían 6 agentes independientes.
4. Graphiti + Obsidian NO OPCIONALES. Son el sistema nervioso. Sin ellos, las fases no se enteran unas de otras.
5. Bilevel Meta-Loop OPCIONAL. Solo activo en modo full-MHYTOS. En otros modos, Max decide manualmente.

### 3.8 Lo que NO entra en MHYTOS

- Code generation en el loop. MHYTOS es un orquestador de pensamiento, no un coder. El coder es Open Claw (Hermes) ejecutando tareas que FASE 3 encola.
- Self-código del orquestador. MHYTOS NO se modifica a sí mismo a nivel código. Lo que cambia es la CONFIGURACIÓN del pool de experts y los pesos de cada fase. El código es estable.
- Conexión con usuario real-time. MHYTOS produce work. Open Claw (Hermes) es el que ENTREGA al usuario. Estos son dos roles distintos.

---

## PARTE 4 — MEJORAS POST-SIMULACIÓN (100x reales)

Las 100 simulaciones previas (vault/simulaciones/) revelaron gaps que se incorporaron como mejoras al diseño. Cuatro gaps críticos y sus soluciones:

Gap 1: Tareas triviales ejecutan loop completo (38% de simulaciones)
Mejora: Heuristic Gate antes del loop
- Clasificador pre-loop que evalúa la tarea
- Trivial (<100 LOC, 1 tool) → 1 fase directa
- Simple (<500 LOC, 2-3 tools) → 3 fases, sync cada 25
- Complex (>500 LOC, multi-file) → 6 fases, sync cada 10
- Critical (production, security) → 6 fases + meta-observer + bias, sync cada 5
Resultado: 38% de tareas dejan de gastar budget en loop innecesario

Gap 2: 22% paralelización sin dedup
Mejora: Cross-agent Deduper Network
- Hash central de (phase, action, args) registrado en experiencia graph
- Si una fase intenta acción repetida, el orchestrator bloquea
- Reduce paralelización innecesaria y race conditions

Gap 3: 15% skills se acumulan sin governance
Mejora: Skill Health Check + Auto-cull
- Cada 50 pasos globales, evalúa cada skill activa
- Métricas: usage rate, success rate, complexity
- Si skill tiene <5% usage en 200 pasos, marcar para revisión
- Si skill tiene <1% usage en 500 pasos, auto-cull (quitar del registry, archive en cold storage)

Gap 4: 12% F4 noise threshold inconsistente
Mejora: Adaptive Threshold per domain
- Threshold de F4 Mejoras Continuas se adapta al dominio
- Code domain: noise_threshold = 0.85 (más estricto)
- Research domain: noise_threshold = 0.65 (más permisivo)
- Production domain: noise_threshold = 0.95 (casi todo requiere aprobación)

### 4.1 Tier de implementación post-MHYTOS base

Tier 1 (MVP ~800-1500 LOC custom + libs):
- cerebro/phases/ con 6 archivos async
- orquestador-auditor/refutation.py con 7 categorías + 50 preguntas
- fichas/grafo.py con fallback JSONL
- fichas/playbook/ estructura ACE base
- cerebro/mhydos_engine.py coordinator

Tier 2 (mejoras post-simulación):
- Complexity Heuristic Gate
- Cross-agent Deduper Network
- Skill Governance
- Adaptive F4 threshold

Tier 3 (producción):
- FalkorDB real + graphiti-core
- Bilevel Meta-Loop real
- Memory cross-Mavis (entre agentes diferentes)

---

## PARTE 5 — RELACIÓN ENTRE LOOP CLAUDE Y MHYTOS

El Loop Claude (Nivel 3) es UNO de los sub-loops internos que corren dentro de las fases MHYTOS. Concretamente:

FASE 3 Ejecución MHYTOS → cuando un task es asignado a Claude, dispara el Loop Claude (Nivel 3)
FASE 5 Revisión MHYTOS → cuando necesita evaluar el output de Claude, activa el Nivel 5 (Auditor con N0-N5)
FASE 4 Mejoras MHYTOS → cuando detecta que el Loop Claude puede mejorar, propone cambios al sub-loop interno

El Loop Claude vive DENTRO de MHYTOS como componente especializado. MHYTOS es la metodología, el Loop Claude es uno de los mecanismos.

---

## PARTE 6 — PSEUDOCÓDIGO EJECUTABLE (para implementar)

### 6.1 Loop Claude Nivel 3

```python
async def claude_loop(task: Task) -> ExecutionResult:
    if not task.has_metric():
        raise ValueError("Task sin métrica de éxito")
    
    # FASE 0: Receive
    ctx = TaskContext(task)
    
    # FASE 1: Generate Hypotheses
    hypotheses = await llm.generate(
        prompt=f"Genera ≥3 approaches para: {task.description}",
        constraints=task.constraints,
        min_count=3
    )
    
    # FASE 2: Self-Reflection
    refined = await llm.reflect(hypotheses, task.constraints)
    
    # FASE 3: Investigate
    codebase_map = await investigate(ctx, refined[0])  # read-only
    
    # FASE 4: Design
    plan = await llm.design(refined[0], codebase_map, task.success_criteria)
    
    # FASE 5: Alternative Paths
    fallback = await llm.alternative(plan)
    
    # FASE 6: Implement (ReAct)
    seen_actions = set()
    for step in range(MAX_STEPS):  # MAX_STEPS=20
        thought = await llm.think(history, plan)
        action = thought.next_action
        
        # Anti-loop: dedup
        action_id = hash_action(action)
        if action_id in seen_actions:
            observation = {"status": "duplicate", "msg": "ya llamaste esto"}
        else:
            seen_actions.add(action_id)
            observation = await execute_tool(action)
        
        history.append(thought, observation)
        
        if thought.is_complete or step == MAX_STEPS - 1:
            break
    
    # FASE 7: Self-Check 3 niveles
    syntax_ok = await check_syntax(code)
    tests_ok = await run_tests(code) if syntax_ok else False
    integration_ok = await run_integration(code) if tests_ok else False
    
    if not (syntax_ok and tests_ok and integration_ok):
        return await claude_loop(task)  # iterar con error
    
    # FASE 8: Handoff
    return ExecutionResult(
        summary=await llm.summarize(history),
        files_modified=codebase_map.modified,
        test_results=tests_ok,
        risks=await llm.identify_risks(code),
        next_steps=plan.next_actions
    )
```

### 6.2 MHYTOS Engine

```python
async def mhytos_engine(task: Task) -> MHYTOSResult:
    # Complexity Gate
    complexity = await classify_complexity(task)
    mode = MODES[complexity]  # trivial/simple/complex/critical
    
    if mode == "trivial":
        return await claude_loop(task)  # solo Nivel 3
    
    # Inicializar fases según modo
    phases = init_phases(mode)
    state = MHYTOSState()
    
    for step in range(MAX_ITERATIONS):
        # PARALELO: 6 fases
        results = await asyncio.gather(*[
            phase.run(state, step) for phase in phases
        ])
        state.update(results)
        
        # SYNC cada 10 pasos
        if step % 10 == 0:
            # Refutation
            scores = await refutation_engine.run(results)
            state.refutation_scores = scores
            
            # Graphiti sync
            await graphiti_sync(results, state)
            
            # Obsidian commit
            await obsidian_commit(results, state)
            
            # Memory sync (ACE)
            await ace_playbook.merge(results)
            
            # Interrupt decision
            if any(s < 0.4 for s in scores):
                await langgraph_interrupt("refutation_low")
            if state.contradiction_count >= 3:
                await consolidation_phase(state)
        
        # Meta-observer cada 50 pasos
        if step % 50 == 0:
            obs = await meta_observer.rate(results, state)
            if obs.suggest_reconfig:
                phases = reconfigure_phases(phases, obs)
    
    return MHYTOSResult(state.final_outputs)
```

### 6.3 Refutation Engine

```python
async def refutation_engine(phase_outputs: dict) -> dict[str, float]:
    questions = generate_50_questions(phase_outputs)
    scores = {}
    
    for phase_name, output in phase_outputs.items():
        phase_questions = [q for q in questions if q.target_phase == phase_name]
        phase_score = 0.0
        for q in phase_questions:
            answer = await llm.answer(q, output)
            passed = q.validate(answer)
            phase_score += 1.0 if passed else 0.0
        scores[phase_name] = phase_score / len(phase_questions)
    
    return scores
```

---

## PARTE 7 — LIMITACIONES HONESTAS

1. Refutation Engine no es real, es conceptual. Implementar 50 preguntas programáticamente requiere templates y validators que pueden no estar todos en sandbox.
2. FalkorDB requiere instalación. No instalado en este sandbox. La versión entregada usa Obsidian vault (markdown) en lugar de FalkorDB.
3. Multiplicación 100x es densidad, no velocidad. 1 step MHYTOS = 100x info, pero toma 10x tiempo. La métrica neta es progreso/hora, no progreso/step.
4. Bilevel requiere code execution real. El outer loop de Autoresearch genera código Python que se inyecta al inner. Mavis puede describir el algoritmo pero NO ejecutarlo en este sandbox sin permisos especiales.
5. Activación cada 10 pasos asume paso promedio de duración constante. En la realidad debería adaptarse a velocidad del loop. Si cada step toma 1 minuto, 10 = 10 minutos; si toma 1 segundo, 10 = 10 segundos.
6. 11 perfiles de agentes Mavis son simulaciones del propio Mavis. Única agente real.
7. Benchmarks Mem0 vs Letta (agosto 2025) disputados. No usar un solo benchmark para validar.
8. Bugs conocidos: langgraph #5790 (dev pierde memoria), Claude Code Read tool v2.1.127 (no sandboxed), reflection contamination (17x error amplification).
