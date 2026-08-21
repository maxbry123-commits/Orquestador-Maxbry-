```json
{
  "checkpoint_id": "DIAGRAMA-PASO-2-PRELIMINAR",
  "tipo": "diagrama_preliminar_integrado + 5_simulaciones",
  "estilo": "identico al documento 30 (deepseck): cajas ASCII verticales, fase por fase, 0% IA en coordinador",
  "regla_90_10": "IA solo en F4 (ejecucion) y F6 (verificacion nivel juez). Todo lo demas = codigo determinista.",
  "estado": "PRELIMINAR — espera aprobacion del Director antes de la version final en 8 salidas"
}
```

# DIAGRAMA PRELIMINAR — ORQUESTADOR MAXBRY/NCT INTEGRADO

```
DIRECTOR (texto natural / comando GO)
           │
           ▼
┌─────────────────────────────────────────────────┐
│ F0: CLASIFICACIÓN DUAL + CONTEXTO               │
│ ┌─────────────────┐  ┌──────────────────────┐   │
│ │ PUSH_PING       │  │ Clasificador dual    │   │
│ │ 30 campos +     │  │ intención (simple/   │   │
│ │ filtros A1-A5   │  │ media/compleja) +    │   │
│ │ + GOAL_LOCK     │  │ tipo (batch/agent/   │   │
│ │ (sha256, freeze)│  │ code)                │   │
│ └────────┬────────┘  └──────────┬───────────┘   │
│          └──────────┬───────────┘               │
│  Sin GOAL_LOCK → pipeline BLOQUEADO             │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F1: FSM KERNEL + ROUTER (0% IA)                 │
│  IDLE→PARSE→ROUTE→EXECUTE→VERIFY→COMMIT         │
│  ADN 6 leyes + Guardian 6 booleanos             │
│  (cualquier true → RECHAZO inmediato)           │
│  Router: keywords ponderados, empate → pregunta │
│  Nivel: RAPIDO 20-50 / BASICO / AVANZADO /      │
│         TURBO 800-1000 loops                    │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F2: PLANNER OFFLINE (0% IA)                     │
│  requirements.json → TopologicalSorter →        │
│  sequence.json INMUTABLE + hash                 │
│  (único lugar donde se decide el orden;         │
│   runtime solo EJECUTA lo congelado)            │
│  + Capability Registry (¿quién sabe hacer qué?) │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F3: AISLAMIENTO + HANDOFF (0% IA)               │
│  Handoff firmado SHA256 → sin firma NO trabajo  │
│  goal_lock_hash dentro del sobre                │
│  Contexto aislado por worker (subagente         │
│  congelado + structured summary)                │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F4: EJECUCIÓN — ÚNICA FASE CON IA PLENA         │
│ ┌─────────────────────────────────────────────┐ │
│ │ MYTHOS (razonamiento, sub-fase FM)          │ │
│ │ 5 arquetipos → estructura el problema       │ │
│ └──────────────────┬──────────────────────────┘ │
│ ┌──────────────────▼──────────────────────────┐ │
│ │ LOOP ENGINE (9 fases, escalado dinámico)    │ │
│ │ dentro: ExpertPool activa N expertos YAML   │ │
│ │ (20-500 según nivel) → enjambre paralelo →  │ │
│ │ proposals (append-only, NADIE escribe       │ │
│ │ directo) → FusionEngine → 1 COMMIT único    │ │
│ └──────────────────┬──────────────────────────┘ │
│ ┌──────────────────▼──────────────────────────┐ │
│ │ TRABAJO PARALELO EXTERNO (opcional)         │ │
│ │ Execution Pipeline DSL (OpenClaw, 15 nodos) │ │
│ │ corre como orquestador paralelo — recibe    │ │
│ │ orden DSL, devuelve resultado firmado       │ │
│ └─────────────────────────────────────────────┘ │
│  Escritor NUNCA dice "funciona" — solo propone  │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F5: MONITOREO SIMULTÁNEO (0% IA, 3 sistemas)    │
│ ┌──────────┐ ┌──────────────┐ ┌─────────────┐  │
│ │ GUARDIAN │ │ WATCHDOG 30s │ │ PAD+Ansiedad│  │
│ │ 6 leyes  │ │ ¿responde?   │ │ +Anti-Drift │  │
│ │ booleano │ │ ¿hash OK?    │ │ KL>0.02 →   │  │
│ │ →RECHAZO │ │ ¿estancado?  │ │ halt+rollbck│  │
│ └──────────┘ └──────────────┘ └─────────────┘  │
│  Detectores: estancamiento/repetición/deriva    │
│  → rota estrategia del pool, no repite la misma │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F6: VERIFICACIÓN 3 CAPAS + ADUANA G2            │
│ CAPA A (0% IA): Verifier N0-N5                  │
│   gpg→sha256→schema→semver→AST imports→         │
│   AST llm_ratio≤0.10 — falla uno → STOP         │
│ CAPA B (0% IA): GCL+Z3+SlotContract SC1-SC6     │
│   verificación formal SAT/UNSAT                 │
│ CAPA C (IA solo aquí): LLM_JUEZ 3 niveles       │
│   Local(0.70)→Capa(0.60)→Central(E296)          │
│   default = RETRY, nunca APPROVED sin evidencia │
│ + WITNESS: Evidence L1-L4 real (build+run+test) │
│   evidence_hash — tampering → abort             │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F7: CONSOLIDACIÓN + MEMORIA (0% IA)             │
│  Postgres+pgvector (1 sola DB, 66% menos costo) │
│  Tier0 RAW→Tier1 SESSION→Tier2 STRATEGIC→       │
│  Tier3 PROJECT (event sourcing, hash chain)     │
│  boot_sequence() SQL arma contexto en 1 query   │
│  Dream Loop semanal + Distill Loop diario       │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F8: REPARACIÓN (0% IA en la escalera)           │
│  RETRY→ROLLBACK→CHECKPOINT→REPLAN→ESCALATE      │
│  (5 niveles, código confirmado)                 │
│  + on_failure por paso: fallback|abort|compensate│
│  FailureRegistry hash-chain → alimenta Sentinela│
│  Sentinela propone parche → SOLO config_runtime │
│  → firma del Director en ledger → aplica        │
└─────────────────────┬───────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────┐
│ F9: ENTREGA + DESPLIEGUE (0% IA)                │
│  Artifact: 3 archivos ([x].py + [x].meta.md +   │
│  location_plan.json) → bundle.zip               │
│  Sheriff SH01-SH07 valida → Atlas automático    │
│  → organizador.py clasifica → desplegador.py    │
│  git commit real → detector_version.py semver   │
│  → subir_a_github.sh push                       │
│  CIERRE: 18 checks — un FAIL|WARNING → reabre   │
└─────────────────────────────────────────────────┘
```

---

# 5 SIMULACIONES END-TO-END

### SIM 1 — Tarea simple: "corrige el typo en el README del repo X"
```
F0: clasifica SIMPLE/code → GOAL_LOCK ok → F1: nivel RAPIDO (20-50 loops)
F2: sequence.json de 1 paso → F3: Handoff a 1 worker
F4: SIN Mythos (nivel rápido lo omite), 1 experto, edición directa
F5: sin eventos → F6: N0-N5 pasa, Juez Local aprueba (0.85>0.70)
F7: memoria Tier1 → F8: no aplica → F9: 3 archivos+push. FIN.
```
**Resultado: 0 fricción, ~30 loops, IA usada solo 2 veces (edición + juicio).** ✅

### SIM 2 — Tarea compleja: "construye el módulo de pagos completo"
```
F0: COMPLEJA/code → F1: TURBO (800-1000) → F2: DAG de 14 pasos, 3 en paralelo
F3: 3 Handoffs firmados → F4: Mythos estructura, 120 expertos en enjambre,
    Execution Pipeline DSL corre tests en paralelo (orquestador externo)
F5: detector nota estancamiento en paso 9 → rota estrategia del pool
F6: N4 detecta import no permitido → STOP → F8: RETRY con fix → F6 pasa
F7: consolida → F9: entrega. FIN.
```
**Resultado: el fallo de import se detecta por CÓDIGO (N4/AST), no por juicio del LLM — el sistema se corrige sin intervención del Director.** ✅

### SIM 3 — Fallo de infraestructura: sandbox muere a mitad de F4
```
F5: watchdog 30s no recibe heartbeat → marca sandbox DEAD
F8: nivel 3 CHECKPOINT → estado se recupera de Postgres (workflows.current_step)
    → sandbox backup (multi-sandbox) monta memoria → resume desde último step
F4: continúa desde paso 8/14, NO desde cero. FIN normal.
```
**Resultado: pérdida = solo el paso en curso. Sin multi-sandbox+Postgres esto perdía todo.** ✅

### SIM 4 — Intento de violación: un agente intenta escribir fuera de su scope
```
F4: agente externo devuelve resultado que incluye modificación a adn/
F6 CAPA A: N2 schema detecta ruta fuera de allowed_paths → STOP
F5 GUARDIAN: booleano NINGUN_AGENTE_MODIFICA_ADN = true → RECHAZO + log
F8: no es fallo técnico → registro en FailureRegistry con causa
Sentinela observa (≥3 repeticiones del patrón → propone regla causal nueva)
```
**Resultado: doble barrera (schema + Guardian), ambas 0% IA — no depende de que un LLM "se dé cuenta".** ✅

### SIM 5 — El Juez duda: evidencia insuficiente en tarea crítica
```
F6 CAPA C: Juez Local score 0.55 < 0.70 → escala a Juez de Capa
    Juez de Capa 0.58 < 0.60 → escala a Central (E296)
    Central pide evidencia adicional → veredicto RETRY (default, nunca aprueba sin más)
F8: RETRY → F4 re-ejecuta con instrucción RETRY_INSTRUCTION del Juez
    (máx 3 intentos) → 3er intento falla → ESCALATE al Director
```
**Resultado: el sistema NUNCA aprueba por cansancio — o hay evidencia o llega al Director.** ✅

---

## LO QUE ESTE PRELIMINAR INTEGRA (trazabilidad)
- Esqueleto: doc 30 (deepseck) — 10 fases, 0% IA coordinador ✔
- Fusión Kimi+MiniMax: clasificación dual, worker pool, PAD/Ansiedad/Drift, EROS, verificación 3 capas ✔
- Código real: ADN/Guardian/Kernel, Juez/Recovery(5), DSL-DAG-Sheriff, Motor 300 expertos, Loop Engine, GCL/Z3, Witness ✔
- Gaps de cierre: Hatchet/Postgres+pgvector, boot_sequence, multi-sandbox, batching (F4), cadena Mythos→control (F4→F5) ✔
- Despliegue determinista: organizador/desplegador/detector/push ✔

**Pendiente de tu aprobación. Si apruebas → Paso 3: versión final en 8 salidas, mismo estilo, fase por fase con micro-diagramas.**
