# INSTRUCCIONES SONNET — PARTE 2/2 (S14-S19)
# Mismo formato. Con esto quedan cubiertas las 13 salidas de instrucciones.

---

## S14 — SENTINELA (repo 15, GUÍA E literal)
**OBJETIVO:** mejora el MÉTODO, nunca el cerebro. Nivel D (observa, propone, Director aprueba).
**ARCHIVOS:**
- `sentinela/observer.py` ~250 — lee métricas (FailureRegistry.causas_frecuentes, accuracy del pool, tiempos por fase); detecta patrones ≥3 repeticiones
- `sentinela/proposer.py` ~250 — genera propuesta estructurada `{problema, evidencia, cambio_propuesto, riesgo, rollback}`; SOLO puede apuntar a `config_runtime.*` y reglas causales YAML
- `sentinela/gatekeeper.py` ~150 — valida contra Guardian (`es_ruta_modificable`), encola para Director, aplica solo tras firma en ledger
**TESTS:** `test_propuesta_a_ruta_inmutable_rechazada`, `test_sin_firma_no_aplica`.
**PROHIBIDO:** tocar ADN/Guardian/Juez/contratos; auto-aplicar; proponer sin evidencia ≥3 casos.

---

## S15 — LOOPS-INFRA (10 niveles) + WIRING LOOP ENGINE (repo 3)
**OBJETIVO:** los 2 sistemas de loops coexistiendo: INFRA (heartbeat/señales/DLQ/meta-loop, doc 03) + ENGINE cognitivo (4 niveles × 9 fases, GUÍA C) aislado en repo 3.
**ARCHIVOS:**
- `loops_infra/heartbeat.py` ~150 — latido por componente cada 30s → alimenta `heartbeat_fn` del RecoveryEngine (Salida 2)
- `loops_infra/signals.py` ~150 — SYS_HALT/PAUSE/RESUME/STATUS (Wake Word) → `kernel.sys_halt()`
- `loops_infra/dlq.py` ~200 — dead letter queue: mensajes fallidos con retry+jitter, 3 intentos → escalate
- `loops_infra/meta_loop.py` ~150 — vigila los loops (loop de loops): detecta loop sin avance → sintoma `sin_avance`
- `loop_engine/engine.py` ~380 — 9 fases (FASE_0 setup → FASE_8 cierre); escala dinámica 20-50/100-300/300-800/800-1000 iteraciones según nivel; presupuesto por fase; conecta con `ExpertPool.ejecutar_enjambre`
- `loop_engine/policies.yaml` — condiciones de salida por nivel (declarativo)
**TESTS:** `test_meta_loop_detecta_estancado`, `test_escala_por_nivel`, `test_dlq_3_intentos`.
**PROHIBIDO:** sleep en bucles (AX07: usar asyncio+scheduler); loops sin condición de salida; contadores fijos DRE.

---

## S16 — MICRO-AGENTES MA-* + AGENTES CATEGORÍA B (repo 7, PATCH-001 literal)
**OBJETIVO:** los 15 MA-* locales (≤200 LOC c/u) + soporte runtime_type=agent.
**ARCHIVOS:**
- `ma/` 15 archivos: MA-SEARCH, MA-FETCH, MA-PARSE, MA-DIFF, MA-TEST, MA-LINT, MA-DOC, MA-ZIP, MA-GIT, MA-SCHED, MA-NOTIF, MA-OCR, MA-EMBED, MA-BUILD, MA-BUILD-EXEC — cada uno: `async def ejecutar(payload)->dict`, 1 función, sin clases, sin estado
- `agentes_b/agent_wrapper.py` ~300 — envuelve agente externo bajo contrato: `max_steps` (HALT al superar), `allowed_actions` (whitelist dura, acción fuera → REJECTED), `environment`, `requires_approval` (pausa→Director), registra cada paso en Audit Bus
- `agentes_b/failover.py` ~150 — cadena de 9: mimo→openhands→smollagents→claude→opencode→codex→cline→goose→aider
**TESTS:** `test_max_steps_halt`, `test_accion_fuera_whitelist`, `test_approval_pausa`.
**PROHIBIDO:** crear agente donde basta ficha llm; agente sin max_steps/allowed_actions; requires_approval=false sin ledger.

---

## S17 — EXECUTION LAYER / SPACES (repos 13-14)
**OBJETIVO:** runners unificados `ejecutar_ficha(ficha,input)→TypedResult` + pools + autoscaling.
**ARCHIVOS:**
- `exec/typed_result.py` ~80 — `Ok[T] | Err[Exception]`, match/case
- `exec/runner_local.py` ~200 — importlib + asyncio.wait_for(timeout por runtime_type: 5/15/30/120)
- `exec/runner_hf.py` ~250 — httpx.AsyncClient POST Bearer HF_API_TOKEN (env); tabla HTTP: 429→reduce+retry, 503→CB OPEN, timeout→CB cuenta, 500→REJECTED+alternate; puerto 7860
- `exec/pools.py` ~250 — ComputePool 80 / HybridPool 15 / LLMPool 5; PoolRouter.route por runtime_type; round_robin+health 5s
- `exec/autoscaler.py` ~150 — up: queue>10 por 60s; down: queue<2 por 300s; límites 3-20 activos, pool máx 100
- `exec/speculative.py` ~150 — precarga fichas COMMITTED + ETag check antes de ejecutar
**TESTS:** IT01 falla 3×→alternate, `test_429_reduce_rate`, `test_scale_up_down`.
**PROHIBIDO:** tokens en código (solo env/Railway); ejecutar ficha no COMMITTED; ignorar ETag.

---

## S18 — ATLAS DSL POBLADO + CONTROL PLANE (repo 2, usa Salida 4)
**OBJETIVO:** poblar el GrafoDSL con los ~40 nodos reales del orquestador + ~12 del Team y generar el atlas completo (~50 docs). Añadir Control Plane.
**ARCHIVOS:**
- `atlas/nodos_orquestador.py` ~380 — declara los nodos P1 (Anchor, PushPing, FiltrosA, OCR, GoalLock, TaskGraph), P2 (Planner, LoopEngine, ExpertPool, Consenso, Escritor, Runtime), P3 (Contract, Builder, ChecksEOUT, Repair, Diff, Formatter), TRANSVERSAL (Kernel, Juez, Recovery, State, Wall, Fusion, Router, AuditBus, Sentinela, DLQ...) — cada nodo con sus 7 preguntas REALES (raíz = rutas de las Salidas 1-6)
- `atlas/nodos_team.py` ~150 — TeamCore, Selector, Scheduler, Witness, MA-*
- `control_plane/profiles.yaml` — Fast/Deep/Research/Autonomous/Custom → nivel, expertos máx, presupuesto, timeouts
- `control_plane/loader.py` ~120 — carga perfil → `config_runtime` (vía commit, nunca directo)
**ORDEN:** nodos → `generar_atlas()` → verificar 50 archivos → commit del hash del grafo.
**TESTS:** `test_atlas_50_docs`, `test_sheriff_pass_grafo_real`, `test_perfil_a_config_runtime`.
**PROHIBIDO:** editar HTML del atlas a mano (solo regenerar); nodo sin ficha_id.

---

## S19 — INTEGRACIÓN FINAL + MVP + CI/CD
**OBJETIVO:** ensamblar todo y arrancar.
**ARCHIVOS:**
- `main.py` ~150 — ensamblaje (Enchufes de Salida 5+6) + watchdog + health loops + señales
- `mvp_plan.md` — 5 pasos G2: (1) runner local+sequence→DAG→state.json (2) 1 ficha real+1 fallo intencional (3) orquestador mínimo+fallback (4) /artifacts (5) trace_id+JSONL
- `.github/workflows/ci.yml` — pytest completo + AX01 (AST scan: 0 llamadas LLM en orquestador) + AX02 (ratio≤0.10) + AX05 (sin Planner con estado en runtime) + N5 en CI + IT01-IT06
- `config.py` — TODOS los flags (CHAT_FASE1_ENABLED etc.), env solo para secretos
**CRITERIO DE CIERRE:** IT01-06 PASS + AX PASS + atlas regenerado + MVP paso 1 corriendo.
**PROHIBIDO:** merge a main sin CI verde; ficha sin los 3 archivos (py+meta.md+location_plan); borrar código (feature flags).

---

# ✅ ESTADO GLOBAL DEL PROYECTO
| Bloque | Estado |
|---|---|
| Kernel código (S1-S6) | ✅ HECHO |
| Parche G2 (3.1) | ✅ HECHO |
| Instrucciones S7-S19 | ✅ ESTE DOC + PARTE 1 |
| Router Universal | → siguiente documento |
