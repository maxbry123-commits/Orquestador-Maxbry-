# DOCUMENTO 03 — SISTEMA DE LOOPS DE 10 NIVELES
## V1.0 — Completo

Inspirado en: LangGraph Supervisor, BabyAGI, Celery + Exponential Backoff con Jitter, Saga Pattern, Circuit Breaker, Temporal.io (signals + heartbeats + cancellation).

---

## NIVEL 0 — META-LOOP (Open Claw)

Combina 3 patrones: LangGraph Supervisor + BabyAGI + Temporal.

```
META-LOOP OPEN CLAW (cada 10s):
    1. Heartbeat interno
    2. Poll estado de los 4 grupos (asyncio.gather)
    3. Re-priorizar tasks (critical > normal > bg)
    4. Decidir siguiente acción (como Supervisor)
    5. Hacer handoff al grupo (como LangGraph)
    6. Chequear signals externos (Director, métricas)
    7. Publicar evento al event bus
    8. Self-healing check
```

---

## NIVEL 1 — BUCLE OPEN CLAW (30s)

```
1. Receive signals (non-blocking)
2. Heartbeat tick
3. Poll all grupos (parallel)
4. Detect recovery needed
5. Update task queue
6. Assign next task
7. Emit metrics
8. Self-healing check
```

---

## NIVEL 2 — BUCLE DE GRUPO (por task)

Combina: Saga Pattern + Circuit Breaker + Exponential Backoff.

```
FASE 0: Wait for task (timeout 1h)
FASE 1: Init saga
FASE 2: Claude loop (max 3 rondas + exponential backoff + jitter)
FASE 3: Mimo loop (3 capas paralelas)
FASE 4: Auditor loop (N0-N5 + SC1-SC6 paralelos)
FASE 5: Circuit breaker check
FASE 6: Commit or compensate (saga)
FASE 7: Notify Open Claw
FASE 8: Update local state
```

**Exponential backoff:** `delay = (2 ** ronda) + random.uniform(0, 1)`
**Saga compensation:** si falla, rollback cambios parciales en orden inverso

---

## NIVEL 3 — BUCLE INTERNO CLAUDE (ReAct)

```
FASE 0: Receive task
FASE 1: Generate hypotheses (mín 3)
FASE 2: Self-reflection
FASE 3: Investigate (P01-P05)
FASE 4: Design (P06-P10)
FASE 5: Alternative paths
FASE 6: Implement (ReAct: Thought → Action → Observation)
FASE 7: Self-check 3 niveles
FASE 8: Prepare handoff
```

---

## NIVEL 4 — BUCLE INTERNO MIMO (3 capas paralelas)

```
FASE 0: Receive archivos
FASE 1: Cache check
FASE 2: Parallel validation (CAPA 1, 2, 3 en asyncio.gather)
FASE 3: Aggregate results
FASE 4: Classify issues (critical / warning / info)
FASE 5: Generate feedback
FASE 6: Update audit log
```

---

## NIVEL 5 — BUCLE AUDITOR (N0-N5 + SC1-SC6 paralelos)

```
FASE 0: Receive validated files
FASE 1: Parallel verification (N0, N1, N2, N3, N4, N5)
FASE 2: Slot Contract (SC1-SC6 secuencial)
FASE 3: Fingerprint 5 layers
FASE 4: Provenance chain
FASE 5: Write to Obsidian + Graphiti
FASE 6: Commit or reject
```

---

## NIVEL 6 — SELF-IMPROVEMENT LOOP (cron 1h)

```
1. Collect metrics de todos los loops
2. Compare con baseline
3. Decide: MEJORA / REGRESION / ESTANCAMIENTO
4. Apply changes en rama improve/*
5. Await 3 ciclos consecutivos de MEJORA
6. Merge a main + notify Director
```

---

## NIVEL 7 — SIGNAL HANDLERS (always listening)

```
- HALT (from Director) → emergency stop
- PAUSE / RESUME
- SCALE_UP / SCALE_DOWN
- ROLLBACK
- EMERGENCY (from watchdog)
```

---

## NIVEL 8 — HEARTBEAT SYSTEM (cada 10s)

```
Open Claw + 4 grupos → state.X.heartbeat (cada 10s)
Watchdog (cada 30s):
  - Open Claw sin heartbeat > 60s → RECOVERY nivel 5
  - Grupo sin heartbeat > 5min → RECOVERY nivel 3
```

---

## NIVEL 9 — DEAD LETTER QUEUE CON RETRY INTELIGENTE

```
Tarea fallida → DLQ
Retry policy: 5min → 30min → 2h → 24h
Cada reintento:
  - Genera nuevas hipótesis
  - Investiga qué cambió
  - Reintenta con backoff
Si todo falla → ESCALATE al Director
```

---

## NIVEL 10 — ESCALATION HIERARCHY (5 niveles)

```
NIVEL 1: SELF_RECOVERY (el loop se recupera solo)
NIVEL 2: PARENT_LOOP (escala al loop padre)
NIVEL 3: SIBLING_LOOP (otro grupo toma el task)
NIVEL 4: AUDITOR (Obsidian/Graphiti registran)
NIVEL 5: DIRECTOR (humano, autoridad final)
```

---

## INTERACCIÓN COMPLETA

```
NIVEL 0 (Meta-Loop, 10s) ─┐
NIVEL 1 (Open Claw, 30s) ─┤
NIVEL 2 (Grupo, por task) ┤
NIVEL 3 (Claude, interno) ┤
NIVEL 4 (Mimo, paralelo) ─┤
NIVEL 5 (Auditor) ───────┤
NIVEL 6 (Self-Improve, 1h)┤
NIVEL 7 (Signals, always) ┤
NIVEL 8 (Heartbeat, 10s) ─┤
NIVEL 9 (DLQ, async) ─────┤
NIVEL 10 (Escalation) ────┘
```

---

## CRITERIOS DE ACEPTACIÓN

- [x] 10 niveles de loops definidos
- [x] Cada nivel con fases claras
- [x] Combinación de 3 patrones en Meta-Loop
- [x] Saga + circuit breaker + backoff en nivel 2
- [x] ReAct en nivel 3
- [x] 3 capas paralelas en nivel 4
- [x] N0-N5 paralelos en nivel 5
- [x] Self-improvement con 3 ciclos de validación
- [x] Signal handlers definidos
- [x] Heartbeat con watchdog
- [x] DLQ con retry inteligente
- [x] Escalation hierarchy de 5 niveles

DOCUMENTO 03 COMPLETO V1.0
