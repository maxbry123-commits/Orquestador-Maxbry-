```json
{
  "checkpoint_id": "DIAGRAMA-FINAL-PARTE-3-de-3",
  "fases_cubiertas": "F7 (memoria/consolidación), F8 (reparación), F9 (entrega) + POST (despliegue determinista) + CAPA TRANSVERSAL (gobernanza)",
  "pasadas": "3 (inventario + comparación vs Partes 1-2 + validación cruzada)",
  "estilo": "documento 30 (deepseck)",
  "estado": "CIERRE DEL DIAGRAMA COMPLETO — espera aprobación del Director"
}
```

# VERSIÓN FINAL — PARTE 3/3 (F7 → F9 + DESPLIEGUE + GOBERNANZA)

```
                 [VIENE DE PARTE 2: F6 certificó con evidence_hash]
                            │
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F7: CONSOLIDACIÓN + MEMORIA (0% IA)                           │
│                                                               │
│ ┌───────────────────────────────────────────────────────────┐ │
│ │ CONSOLIDACIÓN JERÁRQUICA (EROS 3-tier, Kimi + doc 30)     │ │
│ │  Tier 3 Executors → logs crudos                           │ │
│ │  Tier 2 Controllers → Strategic Pulses                    │ │
│ │  Tier 1 Orchestrator → <5% del contexto                   │ │
│ │  + Coordinator (MiniMax): integra outputs, escala dudas   │ │
│ │  doble compactación: EROS SOBRE structured summaries      │ │
│ └─────────────────────────┬─────────────────────────────────┘ │
│ ┌─────────────────────────▼─────────────────────────────────┐ │
│ │ MEMORIA UNIFICADA — Postgres + pgvector (1 sola DB)       │ │
│ │  tablas: agent_memory (embedding 1536, importance 1-10,   │ │
│ │  tipo episodic/semantic/procedural/preference) +          │ │
│ │  workflows (current_step, resume) + sandboxes +           │ │
│ │  idempotency_keys (TTL 7d) + outbox (CDC)                 │ │
│ │  boot_sequence() SQL: identidad + recientes + críticas    │ │
│ │  (importance≥7) en 1 query — implementa el PUSH_PING      │ │
│ │  4 TIERS LÓGICOS: T0 RAW efímero → T1 SESSION →           │ │
│ │  T2 STRATEGIC → T3 PROJECT permanente                     │ │
│ │  Event Sourcing puro: hash chain sha256, time-travel,     │ │
│ │  rollback granular a cualquier punto ≤10s                 │ │
│ │  KNOWLEDGE GRAPH lateral: aristas tipadas (version_de/    │ │
│ │  contradice/refina/depende_de/cita_a/autoridad_sobre) —   │ │
│ │  detección de contradicciones O(grado), no O(n²)          │ │
│ │  MEMORIA POR CAPAS (añadir_1): workflow(Temporal-lite)/   │ │
│ │  operational(PG)/semantic(pgvector)/artifact(S3-B01..B10) │ │
│ │  CRON: Dream Loop semanal (consolida→T3) +                │ │
│ │  Distill Loop diario (lecciones, dedup)                   │ │
│ │  + aprendizaje de fallos: embeddings de drift/ansiedad    │ │
│ │  se guardan y reusan en el ciclo siguiente (doc 30)       │ │
│ └───────────────────────────────────────────────────────────┘ │
└───────────────────────────┬───────────────────────────────────┘
                            ▼ (solo si algo falló en cualquier fase)
┌───────────────────────────────────────────────────────────────┐
│ F8: REPARACIÓN (0% IA en la escalera de decisión)             │
│                                                               │
│  ESCALERA 5 NIVELES (código real SALIDA_02, confirmado):      │
│  1 RETRY único → 2 ROLLBACK a estado estable →                │
│  3 CHECKPOINT replay (resume desde workflows.current_step)    │
│  → 4 REPLAN completo → 5 ESCALATE ("no puedo solo")           │
│  + on_failure POR PASO en sequence.json:                      │
│    fallback | abort | compensate (saga por paso, no nivel 6)  │
│                                                               │
│  REPAIR PIPELINE (doc 30, orden estricto): reintento →        │
│  fallback de modelo → checkpoint → compresión → escalado      │
│                                                               │
│  RT-80 RECOVERY_GATE (UOOS): clasifica auto_recuperable       │
│  vs requiere_Director — nunca escala lo que puede solo        │
│                                                               │
│  CATÁLOGO 200 ESTRATEGIAS (SHERIFF_V7): rotación de           │
│  tácticas por tipo de fallo (redescubrir, limpiar caché,      │
│  bisección binaria de causa, consultar múltiples IA y         │
│  cruzar...) — se rota/combina ANTES de escalar                │
│                                                               │
│  FAILURE REGISTRY (hash-chain verificable):                   │
│  causas_frecuentes() alimenta al SENTINELA:                   │
│  patrón ≥3 repeticiones → observer detecta → proposer         │
│  genera propuesta (SOLO config_runtime.* y reglas YAML,       │
│  NUNCA adn/guardian/juez/contracts) → gatekeeper valida       │
│  contra Guardian → firma del Director en ledger → aplica      │
│  ERR_* 10 códigos con política 1:1 (ERR_HASH→RELOAD×3→        │
│  REJECT, ERR_TIMEOUT→RETRY+5s×3→REJECT...)                    │
│  + P0 robustez (INPUT_BLOCK bloque 7): atomic_write_json,     │
│  graceful shutdown SIGTERM, CircuitBreaker 3 estados,         │
│  exponential_backoff, DeadLetterQueue, HealthChecker          │
└───────────────────────────┬───────────────────────────────────┘
                            ▼ (todos los nodos done)
┌───────────────────────────────────────────────────────────────┐
│ F9: ENTREGA + SELLO (0% IA)                                   │
│                                                               │
│  PROTOCOLO 3 ARCHIVOS por pieza (DOC8, obligatorio):          │
│  [nombre].py (código puro) + [nombre].meta.md (ficha con      │
│  JSON de 10 pasos) + artifact_location_plan.json (ruteo)      │
│  → bundle.zip → ID global [MODEL]-[FICHA]-[FECHA]-[HORA]-     │
│  [HASH] → B01_artifact_code (Storage) + registry (brain)      │
│  REGLA: GitHub=cerebro / Storage=músculos, nunca mezclar      │
│                                                               │
│  QUALITY GATES QG-01..QG-08: contrato/schema/tests/verifier/  │
│  integración/documentación/registro/auditoría —               │
│  falla un gate = NO avanza                                    │
│                                                               │
│  SHERIFF SH01-SH07 valida el grafo final (ciclos,             │
│  compatibilidad enchufe por datatype, coherencia audit×fase)  │
│  → EXPORTERS genera ATLAS AUTOMÁTICO (texto + Mermaid +       │
│  HTML por fase + MD por nodo) desde el grafo con hash         │
│                                                               │
│  DEFINITION OF DONE (8 criterios DOC8 + S19):                 │
│  CI: pytest + AX01 (0 llamadas LLM directas en orquestador,   │
│  AST) + AX02 (llm_ratio≤0.10) + N5 + IT01-IT06                │
│  CIERRE 18 CHECKS (SHERIFF_V7): existe FAIL|WARNING|          │
│  BLOCKED|DEGRADED|UNKNOWN|PENDING|PARTIAL → NO termina,       │
│  reabre el nodo | solo 18/18 → CERTIFIED                      │
│  P12 sello + ADR │ P13 session_close (NUNCA se omite)         │
│  RT-90: BACKLOG.md + reporte final al Director                │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ POST: DESPLIEGUE DETERMINISTA (0% LLM — sin agente)           │
│                                                               │
│  organizador.py → clasifica archivos en 5 repos por REGLAS    │
│  fijas (+ regla nueva: agentes_externos/ → nct-backend)       │
│  → desplegador.py → git init/add/commit real                  │
│  → detector_version.py → compara hashes, sube semver SOLO     │
│    si algo cambió (idempotente)                               │
│  → subir_a_github.sh → crea repos + push                      │
│  INFRA: VPS primary (Contabo/Hetzner, Docker+bind mount) +    │
│  backup región B + snapshots S3/15min + Cloudflare LB/DNS     │
│  failover + Hatchet (Postgres-only) como motor durable        │
│  cuando se necesite | 3 vías de comunicación (normal/         │
│  dirección/emergencia OpenClaw), todas registradas por Router │
└───────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════╗
║ CAPA TRANSVERSAL (activa en TODAS las fases): GOBERNANZA      ║
║                                                               ║
║  CAPA 9 GOBERNANZA (última_versión_1, debate Claude↔Fables):  ║
║  matriz de decisiones — requiere_humano / auto_aprobada /     ║
║  bloqueada_siempre + audit trail de cada decisión             ║
║  DOCUMENT AUTHORITY MAP: jerarquía documental, conflicto →    ║
║  gana el nivel superior | decision_registry.json +            ║
║  CHANGELOG formato fijo + interface_catalog +                 ║
║  dependency_registry (ubicación única) + release standard     ║
║  DRAFT→RC→STABLE→DEPRECATED                                   ║
║  MÉTRICAS: QUALITY/EFFICIENCY/RELIABILITY_SCORE por ciclo →   ║
║  alimentan Model Selector automáticamente | 8 KPIs op         ║
║  (build_success_rate, rollback_rate, mean_recovery_time...)   ║
║  SELF-IMPROVEMENT: mejora→conserva | regresión→rollback de    ║
║  reglas | estancamiento→muta estrategia o modelo              ║
║  SELF_AUDIT_ENGINE: cada 10 artifacts, hallazgo >48h escala   ║
║  PATCH_ENGINE: 10 pasos, rollback automático si falla paso 7  ║
║  HASH CHAIN EN TODO: DSL, skills, schemas, policies, config — ║
║  rollback a cualquier punto ≤10s                              ║
║  RÚBRICA 13 CRITERIOS (serie MAXBRY, rescatada) para evaluar  ║
║  cualquier herramienta OSS antes de integrarla                ║
║  EVENT BUS 3 tipos: SYSTEM/TASK/COGNITIVE, cada uno con       ║
║  canal y política de retry propia                             ║
║  INTERFACE (NCT_INTERFACE_v2): Centro de Control Cognitivo,   ║
║  9 capas, 3 modos headless/studio/embedded + pinned bar 🔒 +  ║
║  modales de confirmación + "frontend abierto": cada botón     ║
║  de la UI = función MCP invocable por otros agentes           ║
║  SIMULACIÓN 5x obligatoria con variación aleatoria antes de   ║
║  ejecutar planes complejos — 3 de 5 fallos → bloquea          ║
╚═══════════════════════════════════════════════════════════════╝
```

## RESUMEN AMPLIO — PARTE 3

**F7 convierte el trabajo en conocimiento sin gastar IA.** La consolidación jerárquica (EROS) garantiza que el orquestador nunca vea más del 5% del ruido: los ejecutores producen logs crudos, los controladores los destilan en pulsos estratégicos, y solo la esencia llega arriba. Todo vive en UNA base (Postgres+pgvector, 66% menos costo que 3 DBs separadas), donde la misma query puede cruzar estado de workflow con memoria semántica. Los 4 tiers lógicos + event sourcing con hash chain hacen que cualquier estado pasado sea recuperable en segundos, y el Knowledge Graph con aristas tipadas detecta contradicciones entre memorias de forma barata (por grado, no comparando todo contra todo). Los dos crones (Dream semanal, Distill diario) son el equivalente a dormir: consolidan, destilan lecciones y borran duplicados. Y el detalle fino del doc 30: los embeddings de los fallos (drift, ansiedad) se guardan — el sistema literalmente recuerda cómo se sintió fallar para reconocerlo antes la próxima vez.

**F8 repara con una escalera fija, no con improvisación.** Cinco niveles confirmados en código (la discrepancia "¿5 o 6?" quedó resuelta en la auditoría: compensate es atributo por paso, no un sexto nivel). Antes de escalar al Director, el sistema rota entre 200 estrategias catalogadas — la regla anti-estancamiento aplicada a la reparación misma. El FailureRegistry con hash-chain no solo registra: alimenta al Sentinela, el único componente autorizado a proponer cambios al método (nunca al cerebro), siempre con firma humana en ledger. Los 10 códigos ERR_* con política 1:1 y los 8 patrones P0 de robustez (escritura atómica, circuit breaker, DLQ, shutdown limpio) hacen que el sistema aguante caídas de infraestructura sin corromper estado.

**F9 sella con burocracia útil y el POST despliega sin cerebro.** Nada sale sin sus 3 archivos, su ID global con hash, sus 8 gates de calidad, la validación del Sheriff sobre el grafo completo y el atlas regenerado automáticamente (el sistema se auto-documenta — nadie dibuja diagramas a mano). El cierre es binario: 18/18 checks o se reabre; no existe "casi terminado". Y el despliegue final es la demostración del principio 90/10 llevado al extremo: 0% LLM — cuatro scripts deterministas clasifican, versionan por hash, commitean y suben. Un agente pudo escribir el código, pero ningún agente decide cómo se despliega.

**La capa transversal es el gobierno.** La CAPA 9 (nacida del debate Claude↔Fables) define qué decisiones requieren humano, cuáles se auto-aprueban y cuáles están bloqueadas siempre — con rastro auditable. Las 3 métricas por ciclo cierran el lazo de auto-mejora con una regla honesta: si empeora, se revierten las reglas nuevas; si se estanca, se muta. Y la interfaz no es decoración: el pinned bar con candado y los modales son la garantía visual de que el input se leyó literal, y el "frontend abierto" convierte cada botón en una función MCP — humanos y agentes usan la misma puerta.

**Gaps integrados en esta parte** (adicionales a Partes 1-2): doc30 EROS+Coordinator+doble compactación+embeddings de fallos, GAP-CIERRE-009/010 (boot_sequence+Postgres unificado), GAP-P3-017 (4 tiers+Dream/Distill+Knowledge Graph+Event Sourcing), GAP-P2-057 (memoria por capas), GAP-P3-018+P3-043 (recovery 5 niveles+compensate por paso reconciliado), GAP-P2-029 (200 estrategias), GAP-P2-022 (ERR_* 10 códigos), GAP-P2-027 (8 P0 robustez), GAP-P3-029 (Sentinela 3 archivos+ledger), GAP-P2-025 (3 archivos+ID global), GAP-P2-011 (QG-01..08), SALIDA_04 (Sheriff SH01-07+atlas), GAP-P3-030 (S19 criterio cierre+AX01/AX02), GAP-P2-030 (18 checks), GAP-P3-012 (P12/P13), GAP-P2-035 (RT-80/RT-90), despliegue completo (organizador/desplegador/detector/push + GAP-CIERRE-002), GAP-CIERRE-007/011 (Hatchet+multi-sandbox), GAP-P3-041 (3 vías comunicación), CAPA 9+authority map+DOC3 completo (gobernanza), GAP-P3-015 (Event Bus+métricas+simulación 5x+hash chain todo), GAP-P2-023 (self_audit+patch_engine), GAP-P3-045 (rúbrica 13 criterios rescatada), NCT_INTERFACE_v2+GAP-P3-034/036 (interfaz+pinned bar+frontend abierto MCP).

---

# EL DIAGRAMA ESTÁ COMPLETO (3/3)

Cobertura final: F0→F9 + despliegue + gobernanza transversal, integrando los 6 linajes del proyecto (MAXBRY serie→rescatado como métodos/rúbricas · NCT Kernel v2→esqueleto de control · Sistema H→motor cognitivo real · UOOS→disciplina runtime · doc30/fusión Kimi-MiniMax→paralelismo y monitoreo · PECP/DOC1-9→contratos y verificación) + los 123 gaps documentados + el código real existente (~12 piezas que se copian, no se regeneran).

**Espera tu aprobación para cerrar el prototipo del orquestador.**
