# NCT_API_ROUTER_v2.md
# Fuente de verdad — Sonnet / Opus / FABLES
# Version: 2.0 | Checkpoint: DOC3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — API ROUTER / DIAGRAMA COMPLETO
NCT API ROUTER v0.2 — Repositorio independiente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPÓSITO
El Router es el administrador de recursos del sistema.
El Orquestador decide la lógica y la coordinación.
El Router decide con qué modelo y con qué API ejecutar cada tarea.
Ningún agente conoce ninguna API key ni ningún provider.
Repositorio completamente independiente del resto del sistema.

DIAGRAMA COMPLETO

Orquestador / Team Agent / Micro-Agents / Ejecutores
        │
        │  POST /v1/complete (siempre la misma llamada)
        ▼
┌─────────────────────────────────────────────────────┐
│                 API ROUTER (VPS independiente)       │
│                                                      │
│  [R1] AUTH & API KEY MANAGER                        │
│       ├── Todas las keys cifradas (AES-256)         │
│       ├── Rotación automática de keys               │
│       ├── BYOK (bring your own key) soportado       │
│       └── Ningún agente ve ninguna key jamás        │
│       ▼                                             │
│  [R2] MODEL SELECTOR (el cerebro del Router)        │
│       ├── Señales: task_type + budget + latency_sla │
│       ├── Señales: capability + provider_health     │
│       ├── Señales: cost_per_token + license         │
│       ├── Reglas en capability.json (sin código)    │
│       └── Si provider saturado → siguiente auto     │
│       ▼                                             │
│  [R3] SCHEDULER + LOAD BALANCER                     │
│       ├── Cola 1-1000 requests simultáneos          │
│       ├── 200+ tareas continuas → batches           │
│       ├── batch_size: 20 configurable               │
│       ├── overlap: 5 (solapamiento entre batches)   │
│       ├── Priority queue: critical>normal>background│
│       └── FIFO estricto dentro de cada prioridad   │
│       ▼                                             │
│  [R4] HEALTH CHECK (cada 30s interno)               │
│       ├── Estado real de cada provider              │
│       ├── Métricas: p95_latencia + error_rate       │
│       ├── Alerta si p95 > SLA definido             │
│       ├── Alerta si costo/hora > threshold          │
│       └── Provider caído → redirige automáticamente │
│       ▼                                             │
│  [R5] RETRY ENGINE                                  │
│       ├── Reintento automático si provider falla    │
│       ├── Backoff exponencial: base 2s, max 5min    │
│       ├── Max 3 reintentos por request              │
│       └── Después de 3 → fallback siguiente provider│
│       ▼                                             │
│  [R6] CIRCUIT BREAKER por provider                  │
│       ├── Umbral: 3 fallos consecutivos → OPEN      │
│       ├── Cooldown: 30s antes de re-intentar        │
│       ├── Half-open: 1 request de prueba            │
│       └── Pass → CLOSE (vuelve a operar normal)    │
│       ▼                                             │
│  [R7] PROVIDER POOL                                 │
│       ├── PROVIDER_A: primary (el más capaz)        │
│       ├── PROVIDER_B: secondary (balance costo)     │
│       ├── PROVIDER_C: especializado código          │
│       ├── PROVIDER_D: fast (tareas simples/rápidas) │
│       └── LOCAL_GGUF: offline (sin internet)        │
│       ▼                                             │
│  [R8] SEMANTIC CACHE                                │
│       ├── Request similar respondido antes → cache  │
│       ├── TTL configurable por task_type            │
│       ├── Cache invalidation por project_hash change│
│       └── Ahorra tokens en requests repetitivos     │
│       ▼                                             │
│  [R9] AUDIT LOGGER                                  │
│       ├── timestamp / provider_usado / tokens       │
│       ├── costo_usd / latencia_ms / request_id      │
│       ├── NUNCA guarda contenido de las llamadas    │
│       └── Solo metadata para auditoría y costos     │
│       ▼                                             │
│  [R10] MONITORING + ALERTS                          │
│        ├── Dashboard: uso por agente y task_type    │
│        ├── Alert: p95 latencia > SLA                │
│        ├── Alert: costo/hora > threshold            │
│        └── Alert: error_rate > 5% en 5 min         │
└─────────────────────────────────────────────────────┘
        │
        ▼
Respuesta al agente (nunca sabe qué provider respondió)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COST_OPTIMIZER (nuevo — debate aprobado)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El costo es una restricción primera clase, no un afterthought.

REGLAS DEL COST_OPTIMIZER:
  task_simple + provider_A_caro → provider_D automático
  task_critical → provider_A SIEMPRE (sin importar costo)
  presupuesto_bajo → LOCAL_GGUF automático
  costo/hora > threshold → LOCAL_GGUF + alerta Director
  cache_hit=true → respuesta directa sin llamar a ningún provider

MÉTRICAS DE APRENDIZAJE:
  QUALITY_SCORE → ajusta qué provider usar por task_type
  EFFICIENCY_SCORE → ajusta batch_size y paralelismo
  RELIABILITY_SCORE → ajusta max_reintentos y circuit_breaker
  El Router aprende con cada ciclo completado.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLUJO CON 50 REQUESTS SIMULTÁNEOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
50 requests entran → [R3] Scheduler encola por prioridad
[R2] Model Selector evalúa cada uno (task_type + budget + SLA)
[R4] Health Check: PROVIDER_A ocupado → usa PROVIDER_B
PROVIDER_B también lleno → usa PROVIDER_C
Todos ocupados → cola espera liberación de capacidad
[R6] Circuit Breaker monitorea errores por provider
COST_OPTIMIZER: si presupuesto bajo → redirige a LOCAL_GGUF
Para el agente: siempre igual → Router → respuesta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERFACE DE LOS AGENTES (siempre la misma)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUEST:
{
  "task_type": "code_generation|research|analysis|critical_decision|...",
  "priority": "critical|normal|background",
  "budget": "low|medium|high",
  "latency_sla_ms": 5000,
  "messages": [...],
  "max_tokens": 4000,
  "stream": false
}

RESPONSE:
{
  "request_id": "uuid",
  "result": {...},
  "tokens_used": int,
  "latency_ms": int,
  "cache_hit": bool
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGLAS DE SELECCIÓN (capability.json)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
task=code_generation + budget=low      → PROVIDER_C
task=long_horizon + horizon≥24h        → PROVIDER_A
task=research_rag                      → PROVIDER_B
task=critical_decision                 → PROVIDER_A
task=simple+fast                       → PROVIDER_D
task=offline                           → LOCAL_GGUF
provider_A.health=down                 → PROVIDER_B auto
provider_B.health=down                 → PROVIDER_C auto
costo/hora > threshold                 → LOCAL_GGUF
cache_hit=true                         → respuesta directa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVOLUCIÓN → MODEL GATEWAY (futuro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPLITTING: parte tarea → PROVIDER_A / parte → PROVIDER_B en paralelo
ENSEMBLE: combina respuestas de 2 providers vía MA-RAG-SYNTH
FINE-TUNING: detecta si fine-tuned es mejor que base para la tarea
AUTO-MODEL: selecciona el modelo exacto, no solo el provider

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3 VERSIONES PARA FABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V1 BÁSICO: R1 + R2 + R5 + R9 (mínimo funcional)
V2 COMPLETO: los 10 módulos R1-R10 + COST_OPTIMIZER (recomendada)
V3 MODEL GATEWAY: R1-R10 + COST_OPTIMIZER + Splitting + Ensemble + AutoModel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUCTURA DE REPOSITORIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
github/api_router/
├── config/
│   ├── capability.json
│   └── providers/
│       ├── provider_a.config
│       ├── provider_b.config
│       ├── provider_c.config
│       ├── provider_d.config
│       └── local_gguf.config
├── modules/
│   ├── R1_auth_key_manager/
│   ├── R2_model_selector/
│   ├── R3_scheduler_lb/
│   ├── R4_health_check/
│   ├── R5_retry_engine/
│   ├── R6_circuit_breaker/
│   ├── R7_provider_pool/
│   ├── R8_semantic_cache/
│   ├── R9_audit_logger/
│   ├── R10_monitoring/
│   └── cost_optimizer/
└── README.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — NOTAS DEL ROUTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTA_R01 — SEPARACIÓN DE RESPONSABILIDADES
Orquestador → decide qué hacer (lógica y coordinación)
Team Agent → divide el trabajo en micro-tareas
Router → decide con qué modelo y API ejecutar cada tarea
Agregar 100 agentes nuevos = 0 cambios en el Router.

NOTA_R02 — CAMBIO DE PROVIDER = EDITAR UN ARCHIVO
capability.json contiene todas las reglas de routing.
Cambiar de PROVIDER_A a PROVIDER_B = 1 línea en capability.json.
El resto del sistema no se toca.

NOTA_R03 — LOS AGENTES SON CIEGOS AL PROVIDER
Ningún agente sabe qué provider respondió su request.
Ningún agente conoce ninguna API key.
Toda esa lógica vive exclusivamente en el Router.
Seguridad por diseño, no por configuración.

NOTA_R04 — HF SPACES FLEET (10-20 workers)
Los Spaces de HuggingFace se integran como backends del Router.
Protocolo: MCP via mcp-hfspace.
Selección: capability + SLA + cost (dinámico).
Circuit breaker: 3 fallos → open / 30s cooldown / half-open test.

NOTA_R05 — COST_OPTIMIZER ES PRIMERA CLASE
El costo no es un afterthought. Es una señal de routing.
El sistema aprende automáticamente qué provider
es más eficiente por task_type a lo largo del tiempo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — DOC3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "NCT_API_ROUTER_v2",
    "version": "2.0",
    "fecha": "2026-07-04",
    "fuente_de_verdad": true
  },
  "router": {
    "modulos": 10,
    "cost_optimizer": true,
    "providers": 5,
    "versiones_fables": ["V1_basico","V2_completo","V3_gateway"],
    "recomendada": "V2_completo",
    "repositorio": "github/api_router/ (independiente)"
  },
  "decisiones": {
    "agentes_ciegos_al_provider": true,
    "capability_json_es_la_unica_config": true,
    "costo_primera_clase": true,
    "cache_semantico": true,
    "circuit_breaker_por_provider": true
  }
}
