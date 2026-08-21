# NCT_TEAM_AGENT_v2.md
# Fuente de verdad — Sonnet / Opus / FABLES
# Version: 2.0 | Checkpoint: DOC2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — TEAM AGENT / DIAGRAMA COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[AG1.01] OBJETIVO Y FUNCIÓN
Coordina un enjambre de micro-agentes especializados
para tareas complejas que ningún agente único puede resolver.
Existe porque las tareas reales requieren paralelismo,
especialización simultánea y síntesis coordinada de resultados.
Casos de uso: arquitectura multi-módulo, investigación profunda,
validación adversarial compleja, refactoring masivo 72h+.

[AG1.02] ANÁLISIS Y CONSENSO PREVIO
Antes de asignar cualquier tarea el Team Agent ejecuta
el Decision Engine v2 completo:
5 agentes votan qué micro-agentes activar, en qué orden,
con qué patrón (secuencial|DAG|fractal) y con qué presupuesto.
Sin consenso → CONSENSUS_BLOCKED → escala al Orquestador.

[AG1.03] GOALS (mínimo 7 justificados)
G1: Descomponer tareas complejas en unidades atómicas verificables
G2: Asignar cada unidad al micro-agente más adecuado por capability
G3: Coordinar ejecución paralela sin colisiones de estado compartido
G4: Sintetizar resultados parciales en output coherente y firmado
G5: Detectar y recuperar micro-agentes fallidos sin detener el swarm
G6: Garantizar que ninguna unidad del DAG quede sin ejecutar
G7: Mantener contexto compartido íntegro entre todos los agentes

[AG1.04] INVESTIGACIÓN WEB PREVIA
Antes de planificar ejecuta 2-5 rondas de investigación:
Fuentes: patrones de orquestación / benchmarks multi-agent /
         papers de swarm coordination / repos de referencia
Umbral de suficiencia: evidence_score ≥ 0.85 antes de avanzar.

[AG1.05] PLANIFICACIÓN
Descarga 3-10 skills según el tipo de tarea detectado.
Genera el task graph (DAG) completo con todas las dependencias.
Estima: tokens / tiempo / costo antes de comprometer recursos.
Valida: no hay ciclos en el DAG, no hay dependencias imposibles.
SIMULACIÓN: el DAG se simula 5 veces antes de ejecutar.
Si 3 de 5 simulaciones fallan → bloquear ejecución real.

[AG1.06] ORGANIZACIÓN DE TAREAS
Agrupa micro-agentes por parallel_group (g1, g2...gN).
Cada grupo puede ejecutar en paralelo internamente.
Los grupos tienen orden de dependencia entre sí (DAG de grupos).
Priority queue: critical > normal > background dentro de cada grupo.

[AG1.07] DIVISIÓN DE TAREAS
Cada tarea → un solo micro-agente con responsabilidad única.
Regla: ≤200 LOC de núcleo por micro-agente.
Cada micro-agente tiene: input_schema + output_schema cerrados.
Estado del micro-agente: efímero (spawn→run→emit→die).
Selección por CAPABILITY no por nombre:
  "necesito: refactoring_python + test_gen"
  El registry devuelve cuál micro-agente lo cumple.

[AG1.08] TRABAJA EN ENJAMBRE
spawn() → todos los micro-agentes del grupo activo en paralelo.
async gather() → espera resultados del grupo completo.
Agente muerto/timeout → spawn() del agente de respaldo.
Resultado parcial de agente → MA-REPAIR-5STEP automático.

SWARM SIZING por DRE:
  LOW:    1-3 micro-agentes en secuencia
  MEDIUM: 4-8 agentes en DAG paralelo
  HIGH:   8-15 agentes en DAG+fractal
  EXTREME: 15-50 agentes, horizon 24h-72h+

[AG1.09] PASOS A EJECUTAR (10 pasos)
PASO 01: Discovery de la tarea (Seed Analysis S1→S5)
PASO 02: Consenso del plan (Decision Engine v2, 5 agentes)
PASO 03: Generación del DAG de micro-agentes con dependencias
PASO 04: Validación del DAG (sin ciclos, dependencias factibles)
PASO 05: Simulación 5x del DAG antes de ejecutar
PASO 06: spawn() del primer parallel_group
PASO 07: async gather() + validación de resultados del grupo
PASO 08: spawn() del siguiente grupo con resultados previos como input
PASO 09: Síntesis final (MA-EMIT-REPORT)
PASO 10: Verificación 3 capas (MA-VERIFY-3CAPAS)
PASO 11: Checkpoint + output firmado al Orquestador principal

[AG1.10] REVISIÓN DE CONTEXTO
Antes de cada parallel_group: verificar state.json integridad.
Si hash chain falla → Recovery Engine nivel 3 (checkpoint).
🔍 activo en cada transición entre grupos del DAG.
Token Budget: si >70% → Writer Subagent compacta antes de continuar.

[AG1.11] REPLANIFICACIÓN DE OBJETIVOS
Si un grupo falla 3 veces → re-ejecutar el Planner completo.
Nuevas hipótesis generadas por Recurrent Reasoning Loop.
Discovery adicional si evidence_score < 0.85 en el nuevo plan.

[AG1.12] CONSENSO REPLANIFICACIÓN — 10 PASOS
P01: Presentar el fallo al Decision Engine v2 con contexto completo
P02: Research Layer busca alternativas (RAG + web + GitHub)
P03: Creative Agent genera nuevas estrategias sin filtro
P04: Innovation Agent mejora cada estrategia a su mejor versión
P05: Critic Agent las ataca adversarialmente
P06: Devil Agent destruye la candidata más fuerte
P07: Selection Agent elige la superviviente (score ≥ 0.6)
P08: Architecture Agent convierte en plan ejecutable concreto
P09: Validator verifica el nuevo plan contra restricciones
P10: Director Loop aprueba (V1) o Auto-gate pasa (V2)

[AG1.13] LOOPS ACTIVOS
decision_loop: cada turno de coordinación del Team Agent
worker_loop: monitoreo continuo de micro-agentes activos
validation_loop: verificación continua de outputs recibidos
memory_loop: escritura periódica a los 4 tiers de memoria
health_loop: detección de agentes caídos o sin respuesta (30s)

[AG1.14] BUCLE PRINCIPAL
```
while (tareas_pendientes AND NOT timeout AND NOT SYS_HALT):
    grupo_activo = DAG.next_group()
    if not simular_5x(grupo_activo):
        recovery_engine.activar(nivel=4)  # REPLAN
        continue
    spawn(grupo_activo)
    resultados = async_gather(grupo_activo, timeout=300s)
    for resultado in resultados:
        if resultado.estado == FAILED:
            MA-REPAIR-5STEP(resultado)
        elif resultado.estado == PARTIAL:
            transformar_antes_de_continuar(resultado)
        elif resultado.estado == ESCALATE:
            decision_engine_v2.evaluar(resultado)
    if todos_pasaron_validacion_3_capas():
        checkpoint_save()
        continuar_siguiente_grupo()
    else:
        recovery_engine.activar(nivel_apropiado)
```

[AG1.15] VALIDACIÓN (3 capas obligatorias)
MA-VERIFY-3CAPAS en cada output de micro-agente:
CAP1: adversarial_check (código determinista 90%)
CAP2: cross_check (código determinista 90%)
CAP3: maker_checker (código determinista 90%)
CAP4_LLM: solo si CAP1-3 detectan issues (LLM 10%)
Resultado: {decision:pass|fail, issues:[], evidence:{c1,c2,c3}}

[AG1.16] HIPÓTESIS
Hypothesis Engine genera N hipótesis de solución al inicio.
Team Agent asigna cada hipótesis a micro-agentes en paralelo.
La que produce mejor score en validación gana.
Mínimo 3 hipótesis antes de seleccionar estrategia.

[AG1.17] REFUTACIONES
Devil Agent ataca cada hipótesis superviviente del Critic.
Si el score de una hipótesis cae por debajo de 0.6 → eliminada.
Solo pasan hipótesis que sobreviven ataque adversarial completo.
Sin hipótesis superviviente → nuevo ciclo de Discovery.

[AG1.18] REPLANIFICACIÓN + CONSENSO LLM (14.1)
Si todas las hipótesis mueren → nuevo ciclo de Discovery completo.
Evidence sufficiency mide si hay info suficiente para replantear.
Si score < 0.85 → más rondas de investigación antes de replantear.
Evaluación final con LLM temperature:0.0 (máximo determinismo).
Los 10 pasos de consenso se repiten con el nuevo contexto.

[AG1.19] 12 PREGUNTAS DE OBJETIVOS (verificación)
Q01: ¿El output cumple el goal primario exactamente como se definió?
Q02: ¿Los goals secundarios (G1-G7) están satisfechos?
Q03: ¿El resultado es verificable con evidencia observable?
Q04: ¿Algún micro-agente produjo output sin verificación de 3 capas?
Q05: ¿El hash chain de memoria está intacto en todos los tiers?
Q06: ¿El DAG se completó sin pasos saltados ni dependencias rotas?
Q07: ¿El score de la solución ganadora es ≥ 0.6?
Q08: ¿El Evidence Sufficiency Score fue ≥ 0.85 antes de ejecutar?
Q09: ¿El Devil Agent ejecutó su refutación completa?
Q10: ¿El artifact tiene provenance chain completa y firmada?
Q11: ¿El checkpoint fue guardado correctamente en state.jsonl?
Q12: ¿El Director aprobó (V1) o el auto-gate pasó (V2)?

[AG1.20] CAMBIO DE ESTRATEGIA
Si > 3 preguntas de objetivos responden NO:
→ Cambiar patrón: Secuencial → DAG → Fractal anidado
→ Cambiar modelos en capability.json (sin tocar código)
→ Aumentar max_rounds del consenso (+2 rondas)
→ Reducir batch_size (mayor control, menor paralelismo)

[AG1.21] NUEVO LOOP
Después del cambio de estrategia:
Reiniciar el bucle principal desde el último checkpoint válido.
No desde el inicio: replay_to_checkpoint(t) exacto.
Actualizar state.json con nueva estrategia y nuevo plan.

[AG1.22] MEMORIA CONTINUA
Cada ciclo escribe a los 4 tiers de memoria.
Tier 0: inputs crudos del ciclo actual (efímero)
Tier 1: contexto activo de la sesión
Tier 2: decisiones estratégicas del ciclo
Tier 3: resultado final + lecciones permanentes
Writer Subagent: compacta cuando >70% del contexto ocupado.
Distill diario + Dream semanal mantienen Tier 2 y Tier 3 limpios.

[AG1.23] CLASIFICACIÓN DE RESULTADOS
Cada output de micro-agente recibe clasificación:
PASS → avanza al siguiente paso del DAG
FAIL → activa MA-REPAIR-5STEP automáticamente
PARTIAL → transformar antes de continuar
ESCALATE → Decision Engine v2 evalúa qué hacer
SKIP → el paso puede saltarse (definido en dependency graph)

[AG1.24] TRANSFORMACIÓN DE RESULTADOS PARCIALES
Los outputs PARTIAL pasan por transformación antes de continuar:
1. Extraer lo válido del resultado parcial
2. Documentar qué parte faltó y por qué
3. Actualizar el contexto del siguiente agente con lo extraído
4. Marcar en el DAG que el paso fue completado parcialmente
5. Continuar con advertencia en el state.json

[AG1.25] FORMATO DE SALIDA ESTRUCTURADA
{
  "team_id": "uuid",
  "tarea_id": "uuid",
  "timestamp_inicio": "ISO-8601",
  "timestamp_fin": "ISO-8601",
  "resultado": {...},
  "score_final": float,
  "artifacts": [{id, tipo, hash, ruta}],
  "provenance_chain": [{evento, actor, timestamp, hash}],
  "checkpoint_ref": "sha256",
  "clasificacion": "PASS|FAIL|PARTIAL|ESCALATE",
  "micro_agentes_usados": [{id, rol, tiempo_s, tokens}],
  "hipotesis_evaluadas": int,
  "consenso_rondas": int,
  "recovery_activado": bool,
  "simulaciones_previas": 5,
  "tiempo_total_s": int,
  "tokens_totales": int
}

[AG1.26] MEMORIA PERSISTENTE (post-ciclo)
Tier 3 PROJECT: resultado guardado indefinidamente
Knowledge Graph: aristas nuevas añadidas al grafo
Corrections DB: si Director itera, se guarda como few-shot
Skills DB: nuevas skills aprendidas disponibles
Failure Registry: causa raíz de fallos para evitar repetir

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PLAN AGENT (complementario al TEAM AGENT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[AG2.01] OBJETIVO
Separa el PENSAMIENTO de la EJECUCIÓN.
Diseña, valida y firma el plan ANTES de que cualquier
executor o Team Agent toque una sola línea de código.
Sin Plan Agent aprobado: ningún executor puede iniciar.

[AG2.02] GOALS
G1: Diseñar el DAG completo con todas las dependencias antes de ejecutar
G2: Validar que el plan es técnicamente factible con los recursos disponibles
G3: Detectar dependencias circulares antes de cualquier spawn
G4: Estimar tokens/tiempo/costo antes de comprometer presupuesto
G5: Producir execution_package validado por auditores y listo para usar

[AG2.03] FLUJO
Input task → Research (3-10 skills descargadas) → Plan draft
→ Simulación 5x del DAG propuesto
→ Feasibility check (¿es implementable con lo que tenemos?)
→ Consensus v2 (5 agentes validan el plan)
→ Auditor_1 + Auditor_2 verifican
→ execution_package firmado por Architecture Agent
→ GOAL_LOCK activado por LLM_JUEZ
→ Handoff al Team Agent o Executor

[AG2.04] FORMATO DE SALIDA
{
  "plan_id": "uuid",
  "dag": {nodes:[], edges:[], critical_path:[]},
  "estimacion": {tokens_total:int, tiempo_h:float, costo_usd:float},
  "riesgos": [{componente, modo, probabilidad, impacto, mitigacion}],
  "dependencias": [{id, tipo, obligatorio:bool}],
  "execution_package": {pasos:[], agentes:[], skills:[]},
  "firmado_por": "ARCHITECTURE_AGENT",
  "aprobado_por": "DIRECTOR|AUTO_GATE",
  "goal_lock_activo": true,
  "simulaciones_exitosas": 5,
  "timestamp_aprobacion": "ISO-8601"
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — NOTAS DEL AGENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTA_A01 — DIFERENCIA TEAM vs PLAN AGENT
PLAN AGENT: piensa y diseña el plan (antes de ejecutar)
TEAM AGENT: coordina la ejecución del plan aprobado
Sin PLAN AGENT aprobado → TEAM AGENT no inicia.
Son complementarios, no intercambiables.

NOTA_A02 — AGENTES SON PROCESOS REALES
No son LLMs simulando roles. Son procesos Python en Antigravity.
El LLM es una herramienta que usa el proceso, no el proceso mismo.
Comunicación entre agentes: JSON sobre HTTP o Message Queue.
El orquestador llama a cada proceso por su endpoint real.

NOTA_A03 — MICRO-AGENTES SON DESECHABLES
Cada micro-agente nace, ejecuta su única tarea y muere.
Estado efímero: no guarda nada entre ejecuciones.
Toda la persistencia va al state.json y a la memoria por tiers.
La reutilización viene del Knowledge Graph, no del agente mismo.

NOTA_A04 — RECOVERY DE AGENTES CAÍDOS
Detección: health_loop cada 30s detecta agente sin respuesta
Timeout: 5min sin respuesta → agente declarado caído
Acción: spawn() del agente de respaldo con mismo manifest
Context: el nuevo agente recibe el handoff_package del anterior
Límite: max 3 respawns del mismo agente antes de ESCALATE

NOTA_A05 — BUDGET DSL 90/10
90% del trabajo del Team Agent es código determinista:
routing, scheduling, validation, checkpoint, retry, logging.
Solo 10% usa LLM: síntesis de resultados, decisiones creativas,
evaluación adversarial cuando las 3 capas mecánicas fallan.

NOTA_A06 — SIMULACIÓN OBLIGATORIA
El DAG se simula 5 veces con variación aleatoria antes de ejecutar.
Si 3 de 5 simulaciones fallan → bloquear ejecución real.
El simulador usa el mismo DAG real pero con mocks.
Detecta colisiones de estado antes de que ocurran en producción.

NOTA_A07 — CAPABILITY-BASED, NO NAME-BASED
El Team Agent no dice "usa MA-CODE-GEN".
Dice "necesito: python_code_generation + ast_validation".
El Capability Registry devuelve qué micro-agente lo cumple.
Si mañana aparece uno mejor → se registra → funciona solo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 3 — MICRO-AGENTES (12 MA-*)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REGLA UNIVERSAL: spawn→run→emit JSON→die (≤200 LOC núcleo)
Cada uno tiene: manifest.json + input_schema + output_schema + 1 test

MA-CODE-GEN
  Capability: python_code_generation, js_code_gen, rust_code_gen
  Input: spec.md + stack.json
  Output: code.py|js|rs + imports.json
  LOC: ≤200

MA-CODE-LINT
  Capability: lint, format, type_check
  Input: code.py|js|rs
  Output: report.json {issues:[], severity, fixed:bool}
  LOC: ≤150

MA-CODE-TEST
  Capability: unit_test, integration_test, mutation_test
  Input: code.py + spec.md
  Output: junit.xml + coverage.json
  LOC: ≤180

MA-RAG-SEARCH
  Capability: vector_search, semantic_rerank
  Input: query.str + collection.str
  Output: chunks.json [{text, score, source}]
  LOC: ≤150

MA-RAG-SYNTH
  Capability: synthesis_with_citations
  Input: chunks.json + question.str
  Output: answer.md con citas inline
  LOC: ≤150

MA-DOC-WRITE
  Capability: architecture_documentation
  Input: arch.yaml + decisions.json
  Output: doc.md autocontenido
  LOC: ≤180

MA-ARCH-PLAN
  Capability: architecture_planning, stack_selection
  Input: requirements.json + constraints.json
  Output: arch.yaml + adr.md
  LOC: ≤200

MA-VERIFY-3CAP
  Capability: adversarial_verification
  Input: artifact.json + schema.json
  Output: verdict.json {pass:bool, issues:[], evidence:{c1,c2,c3}}
  CAP1: adversarial_check (determinista)
  CAP2: cross_check (determinista)
  CAP3: maker_checker (determinista)
  CAP4_LLM: solo si CAP1-3 detectan issues
  LOC: ≤200

MA-REPAIR-5STEP
  Capability: code_repair, error_fix
  Input: failed_artifact.json + error.json
  Output: repaired.json + diff.patch
  Pasos: diagnose→hypothesize→fix→test→verify
  LOC: ≤200

MA-RESEARCH-WEB
  Capability: web_crawling, content_extraction
  Input: query.str + max_pages.int
  Output: pages.jsonl [{url, content, relevance}]
  LOC: ≤150

MA-RESEARCH-GH
  Capability: github_search, repo_analysis
  Input: query.str + filters.json
  Output: repos.json [{name, stars, relevant_files}]
  LOC: ≤150

MA-EMIT-REPORT
  Capability: result_packaging, report_generation
  Input: all_artifacts.json + metadata.json
  Output: report.md + manifest.json + summary.json
  LOC: ≤180

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — DOC2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "NCT_TEAM_AGENT_v2",
    "version": "2.0",
    "fecha": "2026-07-04",
    "fuente_de_verdad": true
  },
  "team_agent": {
    "secciones": 26,
    "preguntas_objetivos": 12,
    "micro_agentes": 12,
    "simulacion_previa": 5,
    "swarm_max": 50,
    "horizon_max": "72h+"
  },
  "plan_agent": {
    "goals": 5,
    "simulacion_dag": true,
    "flujo_pasos": 7
  },
  "micro_agentes_MA": {
    "total": 12,
    "LOC_max_cada_uno": 200,
    "seleccion": "capability_based_no_name_based"
  },
  "decisiones": {
    "agentes_procesos_reales": true,
    "estado_efimero": true,
    "persistencia_en_tiers": true,
    "budget_dsl_90_llm_10": true,
    "simulacion_5x_obligatoria": true
  }
}
