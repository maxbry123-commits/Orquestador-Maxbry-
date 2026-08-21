```json
{
  "checkpoint_id": "DIAGRAMA-FINAL-PARTE-1-de-3",
  "fases_cubiertas": "F0, F1, F2, F3 (entrada, kernel, planificación, aislamiento)",
  "integra": "documentos del chat + bandeja de proyecto + 123 gaps documentados",
  "estilo": "documento 30 (deepseck)",
  "regla": "0% IA en F0-F3. Todo determinista."
}
```

# VERSIÓN FINAL — PARTE 1/3 (F0 → F3)

```
DIRECTOR (comandos: GO/OK/FIX/PAUSA/ESTADO/SALTAR/UNLOCK/ABORT)
           │  ← vocabulario cerrado de 8 comandos (UOOS)
           ▼
┌───────────────────────────────────────────────────────────────┐
│ F0: INPUT FABRIC — CLASIFICACIÓN + CONTEXTO (0% IA)           │
│                                                               │
│ ┌───────────────┐  ┌────────────────┐  ┌──────────────────┐  │
│ │ INPUT_BLOCK   │  │ ANCHOR +       │  │ CLASIFICADOR DUAL│  │
│ │ inmutable     │  │ PUSH_PING      │  │ Kimi: intención  │  │
│ │ raw_hash      │  │ 30 campos con  │  │ simple/media/    │  │
│ │ sha256, hash- │  │ "si_falta" por │  │ compleja         │  │
│ │ chain SQLite  │  │ campo — no     │  │ MiniMax: tipo    │  │
│ │ + pre_tool_   │  │ avanza sin los │  │ batch/agent/code │  │
│ │ use hook:     │  │ 30 resueltos   │  │ + clase pushping │  │
│ │ bloquea agente│  │                │  │                  │  │
│ │ que no leyó   │  │                │  │                  │  │
│ └───────┬───────┘  └───────┬────────┘  └────────┬─────────┘  │
│         └──────────────────┼────────────────────┘            │
│                            ▼                                 │
│ ┌────────────────────────────────────────────────────────┐   │
│ │ FILTROS A1-A5 + OCR (solo aquí, vigilado SH05)         │   │
│ │ + detector de negaciones ("no","nunca","excepto")      │   │
│ │ + detector de énfasis (MAYÚSCULAS/! = prioridad alta)  │   │
│ └───────────────────────────┬────────────────────────────┘   │
│                             ▼                                │
│ ┌────────────────────────────────────────────────────────┐   │
│ │ GOAL_LOCK (sha256, congelado por LLM_JUEZ)             │   │
│ │ + SEED PRE-ANALYSIS S1-S5 (repo+state+RAG → seed_index │   │
│ │   SQLite + gaps + preguntas) + Repo RAG Agent          │   │
│ │   ("¿qué existe YA en el repo?" — anti-inventar)       │   │
│ │ CONTRATO SALIDA F0: {goal_lock_hash, task_graph,       │   │
│ │   knowledge_pack, clase_pushping}                      │   │
│ │ SIN GOAL_LOCK → PIPELINE BLOQUEADO SIN EXCEPCIÓN       │   │
│ └────────────────────────────────────────────────────────┘   │
│ MODOS: MANUAL | SEMI-AUTO | CONTINUO (doc 30) — el Director  │
│ elige cuánta supervisión; CONTINUO = sin intervención humana │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F1: FSM KERNEL + ADN + GUARDIAN + ROUTER (0% IA)              │
│                                                               │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ ADN_SYSTEM — 6 leyes INMUTABLES (solo Director modifica) │ │
│ │ AUDITABLE·REVERSIBLE·TRAZABLE·EVIDENCIA·JERARQUÍA·       │ │
│ │ NINGUN_AGENTE_MODIFICA_ADN                               │ │
│ └────────────────────────┬─────────────────────────────────┘ │
│ ┌────────────────────────▼─────────────────────────────────┐ │
│ │ GUARDIAN_LAYER — 6 booleanos, cualquier true → RECHAZO   │ │
│ └────────────────────────┬─────────────────────────────────┘ │
│ ┌────────────────────────▼─────────────────────────────────┐ │
│ │ FSM: IDLE→PARSE→ROUTE→EXECUTE→VERIFY→COMMIT→IDLE         │ │
│ │ NUNCA un LLM decide transiciones                         │ │
│ │ ROUTER: keywords ponderados O(n), empate → 1 pregunta    │ │
│ │ NIVEL: RAPIDO 20-50 | BASICO 100-300 | AVANZADO 300-800  │ │
│ │        | TURBO 800-1000 loops (nivel 0 = autodetección)  │ │
│ │ JERARQUÍA: N0 Director → N1 Orquestador → N2 Consejo(5)  │ │
│ │            → N3 Auditores(3 capas) → N4 Ejecutores       │ │
│ └──────────────────────────────────────────────────────────┘ │
│ ARCHIVOS RAÍZ (leídos ANTES de todo): system_manifest.json + │
│ project_manifest.json + project_index.json + connections.yaml│
│ (providers viven aquí, no en código) + state.json (CrazyWall)│
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F2: PLANNER OFFLINE + CAPABILITY (0% IA)                      │
│                                                               │
│ requirements.json → graphlib.TopologicalSorter (detecta       │
│ ciclos) → sequence.json INMUTABLE + hash                      │
│   schema por step: {step_id, tipo:secuencial|paralelo,        │
│   fichas[], depends_on[], critico, condition(safe_eval AST,   │
│   sin Call/Import — anti-inyección), timeout_seg,             │
│   on_failure: fallback|abort|compensate}                      │
│ REGLA DE ORO: único lugar donde se decide el orden.           │
│ En runtime el kernel solo EJECUTA lo congelado.               │
│                                                               │
│ CAPABILITY REGISTRY: capability-based, NO name-based          │
│ ("necesito refactoring_python", no "usa Aider")               │
│ + consulta a resources.yaml (DeepSeek): "¿existe OSS que ya   │
│   cubra esto?" antes de construir ficha nueva                 │
│ + 325 fichas mapeadas (30 con código, 295 planeadas)          │
│ + regla ficha: 1 ficha = 1 función, ≤200 LOC, PROHIBIDO       │
│   runtime/orquestador/DAG/FSM dentro de una ficha             │
│ PIPELINE JUEZ pre-código: P-DISCOVER→P00..P10 (simple omite   │
│ P03-P06+P09-P10; critical corre 14 completos; P13 nunca       │
│ se omite) + presupuesto: P09 declara, P10 aprueba             │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F3: AISLAMIENTO + HANDOFF + SANDBOX (0% IA)                   │
│                                                               │
│ HANDOFF firmado SHA256 (sin firma válida NO se trabaja)       │
│   contiene: goal_lock_hash + criterios aprobación/rechazo +   │
│   output_schema + max_intentos:3                              │
│   Escritor solo recibe del Juez, nunca del Director directo   │
│                                                               │
│ CONTEXTO AISLADO por worker:                                  │
│   subagente congelado (Kimi) + structured summary (MiniMax)   │
│   Writer Subagent compacta si contexto >70%                   │
│   + reload-after-compaction (input se re-inyecta, no se       │
│     "olvida" en conversaciones largas)                        │
│                                                               │
│ SANDBOX POOL dinámico (1-10, asignación por proyecto):        │
│   sandbox = SOLO entorno de ejecución, nunca el cerebro       │
│   muere → marca DEAD → guarda estado → nuevo sandbox →        │
│   monta memoria → resume desde checkpoint                     │
│   PRIMARY (Contabo, Docker+bind mount) + BACKUP (Hetzner/DO)  │
│   + snapshots S3 cada 15 min + LB/DNS failover (Cloudflare)   │
│   Scheduler asigna por recursos (CPU/RAM/tiempo estimado)     │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
                    [PARTE 2/3: F4-F6]
```

## MICRO-RESUMEN PARTE 1
F0 garantiza que NADA entra sin leerse literal (InputBlock con hook que bloquea), sin contexto completo (30 campos) y sin objetivo congelado (GOAL_LOCK). F1 es el control puro: leyes inmutables + FSM donde ningún LLM decide. F2 congela el plan ANTES de ejecutar (orden inmutable con hash). F3 blinda la entrega de trabajo (firma criptográfica) y hace los sandboxes desechables sin perder memoria.

**Gaps integrados en esta parte**: GAP-P3-032/033 (InputBlock+hook+detectores), GAP-P3-016 (PUSH_PING 30), GAP-P2-039 (modos A/B/C→Manual/Semi/Continuo), GAP-P3-003 (ADN/Guardian), GAP-P2-004/005 (FSM+Router), GAP-P3-011 (jerarquía+escala loops), GAP-P2-001/044 (archivos raíz+connections.yaml), GAP-P2-052 (planner offline), GAP-P3-044 (sequence schema+safe_eval), GAP-CIERRE-004 (resources.yaml DeepSeek), GAP-P3-042 (325 fichas), GAP-P2-015 (regla ficha), GAP-P3-012 (Pipeline Juez 14 pasos), GAP-P3-049 (Handoff), GAP-P2-050 origen (Witness llega en P2), GAP-P2-063 (sandbox pool), GAP-CIERRE-011 (multi-sandbox), GAP-P3-017 parcial (Writer Subagent).

¿OK para Parte 2/3 (F4-F6: ejecución, monitoreo, verificación)?
