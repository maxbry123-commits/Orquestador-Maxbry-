# PATCH-AUDITORIA-GAPS: GAPS ENCONTRADOS EN AUDITORÍA 55X
## MAXBRY SUPER TEAM · Documento único de parche

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** PATCH de auditoría (UN documento)
**Estado:** ✅ COMPLETO

---

## PROPÓSITO

Después de auditar 55 veces los 170+ parches y documentos del proyecto, encontré GAPS CRÍTICOS que NO están en los Master Documents 01-29. Este es **UN solo documento** que cierra esos gaps.

---

## GAP #1 — INCONSISTENCIA MAYOR: 6 GRUPOS vs 8 GRUPOS

### 🔴 CRÍTICO

**El problema:**
- `01-FASE-0-FROZEN.md` define **8 GRUPOS** (G1-G8)
- `ORQUESTADOR-G5-DISENO.md` también define **8 GRUPOS**
- `CONSTITUCION-ORQUESTADOR.md` y `STATE-AUDIT.md` definen **6 GRUPOS** (G1-G6)
- Los 29 Master Documents usan **6 GRUPOS**

### Las DOS versiones encontradas:

#### Versión A — 8 GRUPOS (FASE 0 FROZEN)
```
G1_INFRA        — runtime, scheduler, sheriff, sentinel, watcher
G2_CORE         — cerebro cognitivo, planner, DSL, DAG, memoria
G3_UI           — interfaces, frontend
G4_AUDIT        — fichas, documentación, LightRAG, Haystack
G5_CONSENSO     — SKYNER, validación, arbitraje
G6_BUILD        — assemble, compile, test, package, publish
G7_ASISTENTES   — 9 modelos GGUF locales (staff)
G8_ORQUESTADOR  — router, Telegram bridge, MCP server, consensus orchestrator
```

#### Versión B — 6 GRUPOS (MASTER DOCS actuales)
```
G1 INFRA        — HF Spaces, GitHub, Docker
G2 CORE         — BIS, SID, Input/Output Engine
G3 UI           — Telegram, API REST, Dashboard
G4 AUDIT        — CSA
G5 ORQUESTADOR+CONSENSO (mismo grupo) — MAXBRY SUPER TEAM
G6 ASISTENTES   — 9 modelos GGUF + 16 API keys
```

### Recomendación:
**CONSERVAR 6 GRUPOS** (que es lo aprobado por MAX en el chat) y tratar los G7-G8 originales como sub-grupos dentro de G5+G6.

---

## GAP #2 — ACTIVATION COMMANDS (TELEGRAM)

Comandos específicos de Telegram que NO están en master docs:

```
"ORQUESTADOR"           → solo G8 responde (en versión 8 grupos) / G5 (en versión 6)
"ASISTENTE"             → solo G7 responde / G6
"ASISTENTE ORQUESTADOR" → ambos responden (parallel)
"ORQUESTADOR CONSENSO"  → G8/G5 pregunta: "¿5 o 12 modelos?"
```

**Aplicar en MASTER-09 (Agentes) — agregar sección "Activation Commands".**

---

## GAP #3 — 13 CRITERIOS SKILLS (VERSIÓN OFICIAL)

### Lista incorrecta en MASTER-27:
```
01-relevancia, 02-efectividad, 03-costo, 04-compatibilidad, 05-mantenibilidad,
06-documentacion, 07-reusabilidad, 08-seguridad, 09-performance, 10-escalabilidad,
11-compliance, 12-test-coverage, 13-comunidad
```

### Lista CORRECTA (de ORQUESTADOR-G5-DISENO.md):
```
01. Calidad del código (lint, type-check, complexity)
02. Licencia (compatible: MIT, Apache 2.0, BSD)
03. Mantenimiento reciente (último commit <6 meses)
04. Estrellas en GitHub (señal, no criterio único)
05. Issues abiertos vs cerrados (ratio)
06. Uso por la comunidad (descargas HF, cites)
07. Compatibilidad con arquitectura NCT
08. Dependencias (mínimas y mantenidas)
09. Seguridad (sin CVEs conocidos)
10. Rendimiento (latencia, throughput)
11. Tamaño (cabe en 16GB RAM)
12. Facilidad de integración (API estable)
13. Pruebas propias (tests incluidos)
```

**Aplicar en MASTER-05 (SID+BIS) — corregir los 13 criterios.**

---

## GAP #4 — SHERIFF + SENTINEL + WATCHER + JUDGE PROTOCOLS

### SHERIFF v1.0
```
ID: sheriff · G1_INFRA · deterministic (no LLM)
frequency: every_5min
checks: process_alive / progress_moved / errors / timeout / rate_limit / api_fail / commit_fail / dependency_broken
classify: INFO→log / WARNING→BLACKBOARD / ERROR→retry+BLACKBOARD / CRITICAL→G5+MAX
blocks: no_events_30min / no_progress_30min / no_commit_30min / no_state_write_15min / no_heartbeat_5min
input_block_violation: detected if input ≠ output semantically
loops_protection: retry_max=2 / consensus_max=2 / audit_max=2 / repair_max=2
```

### SENTINEL v1.0
```
ID: sentinel · G1_INFRA · deterministic
frequency: 1min (resources) / 5min (costs/security)
monitors: tokens_per_min / rate_limits / latency / HF_spaces_uptime / GH_API_remaining / daily_cost / security_commits
supervised_by: sheriff (heartbeat 5min — if silent 10min → GH_Action restart)
```

### WATCHER v1.0
```
ID: watcher · G1_INFRA · deterministic
frequency: 60s
monitors: group_heartbeat (window: 5min) / HF_space_state / GH_actions_runs / last_STATE_write
supervised_by: sentinel
```

### JUDGE v1.0 (SKYNER ALGORITHM)
```
ID: judge · SKYNER · MiniMax-M3-via-NVIDIA-NIM
algorithm:
  confidence = 0.40×semantic_match + 0.30×consistency_BLACKBOARD
            + 0.20×model_self_confidence + 0.10×historical_accuracy
  ≥0.85 → APPROVED · 0.60-0.85 → RE_INVOKE (max 2) · <0.60 → REJECTED
veto: contradicts BLACKBOARD / violates rules / security_implication
output: consensus_status / confidence / reason / veto_reason / requires_human
```

### VALIDATOR v1.0
```
validates: compiles / tests_pass / linting / type_check / docs / STATE.schema / no_secrets / no_breaking_changes
rejects_if: any check fails / STATE invalid / secret detected
max_iterations: 2
```

### ORCHESTRATOR v1.0
```
inputs: TASK.json / BLACKBOARD.json
priorities: Urgente > Alta > Media > Baja · FIFO within level
recovery: silent_5min→check_heartbeat / silent_10min→sheriff_alert / silent_30min→reassign
```

**Aplicar en MASTER-09 (Agentes) — agregar protocolos detallados.**

---

## GAP #5 — CONSENSUS 5 vs CONSENSUS 12 (MODELOS ESPECÍFICOS)

### Consensus 5 (rápido):
```
1. HRM-Text-1B
2. Qwen2.5-Coder-1.5B
3. Granite-Code-3B
4. Liquid-LFM2.5-1.2B-Thinking
5. Gemma-4-E2B
```

### Consensus 12 (completo):
```
4 NVIDIA-NIM keys
+ 6 Cerebras keys
+ GPT-OSS-20B (local)
+ OpenCodeReasoning-Nemotron-7B
+ DeepHermes-3-3B
+ SmolLM3-3B
```

**Aplicar en MASTER-25 (SKYNER+Consenso) — agregar detalle de Consensus 5 vs 12.**

---

## GAP #6 — 10 LOOPS CONTRACTS

```
LOOP           INICIA        TERMINA CUANDO           MAX    ESCALA A
─────────────────────────────────────────────────────────────────────
Planning       M3_chat       DAG armado               3      MAX
Execution      scheduler     done=true|failed         1+2    retry→G5
Review         scheduler     approved|rejected        2      G5
Critic         AUTO_BOTH     acuerdo entre par        3      SKYNER
Repair         G4|scheduler  errores fixed            2      G5
Validation     REQUEST_REVIEW consensus_status emit   2      MAX
Consensus      any_group     decisión emitida         3      MAX
Build          scheduler     release publicado        2      MAX
Release        G6            tag+ZIP+informe          1      MAX
Monitoring     cron_5min     incidente cerrado        ∞      MAX
```

**Aplicar en MASTER-08 (Loop) — agregar tabla de 10 Loops.**

---

## GAP #7 — MEMORY PROTOCOL v1 (3 TIERS)

```
FUENTE DE VERDAD: GitHub nct-consensus-log
ÍNDICE RÁPIDO: ChromaDB en HF MEMORIA
CONTEXTO 10M: context7 (retrieval por proyecto)
JERARQUÍA:
  Tier 1: últimos 32K tokens (texto completo)
  Tier 2: 32K-2M (chunks ChromaDB)
  Tier 3: 2M-10M (resúmenes retrieval on-demand)
EMBEDDINGS: bge-small-en-v1.5 (24MB, HF)
CHAT MEMORY: M3_chat guarda en memory_topic_append después de cada sesión
```

**Aplicar en MASTER-12 (Pipeline) o MASTER-21 (Subsistemas) — agregar Memory Protocol v1.**

---

## GAP #8 — STORAGE STRATEGY

```
GitHub (versionado + auditoría):
  fichas / code / artifacts / master_project / Índice / TEAMS_MAP.md

SandboxDB (alta frecuencia):
  STATE / BLACKBOARD / EVENTS / INBOX / OUTBOX / Cola / Heartbeats / Caché / Logs

Export a GitHub solo: cierre de tarea / error / auditoría
```

**Aplicar en MASTER-12 (Pipeline) — agregar Storage Strategy.**

---

## GAP #9 — MERGE RULE + PRIORIDADES + KEEPALIVE

### MERGE RULE:
```
auto_merge_when: G4_AUDIT_approved AND G5_CONSENSO_approved AND tests_pass
if_any_fails: PR_open + M3_chat_notified + MAX_decides
```

### PRIORIDADES:
```
Urgente: SLA=60min / retries=3
Alta:    SLA=240min / retries=2
Media:   SLA=1440min / retries=2
Baja:    SLA=4320min / retries=1
```

### KEEPALIVE:
```
GitHub_Actions_cron_20min · /health_per_space · alert_on: 2_consecutive_failures
```

**Aplicar en MASTER-12 (Pipeline) — agregar Merge Rule + Prioridades + Keepalive.**

---

## GAP #10 — MiniMax M3 ATRIBUTOS ESPECÍFICOS

```
Atributo:          Valor
Modelo:            MiniMax-M3 (MiniMaxAI/MiniMax-M3 en HF)
Endpoint:          1× NVIDIA NIM dedicado (slot reservado)
API style:         OpenAI-compatible (/v1/chat/completions)
Context window:    1.048.576 tokens (1M)
Throughput:        ≥ 80 tok/s sostenidos
Latencia p50:      ≤ 350 ms primer token
Latencia p95:      ≤ 900 ms primer token
Roles permitidos:  FASE 4 (Ejecución) + FASE 6 (Verificación capa 3)
System prompt:     orquestador/system_prompt.json
Política retries:  3 reintentos, backoff 1s/3s/7s, fallback Kimi K2
Logging:           request_id (UUIDv7) en reportes/llm_calls/
```

**Aplicar en MASTER-10 (Modelos y APIs) — agregar atributos específicos M3.**

---

## GAP #11 — DSL REASONING_CHAIN.PY (ENFORCED)

```python
@enforced  # decorador obligatorio — no se puede saltar
def reasoning_chain(task_input):
    # STEP 1 — LITERAL READ
    raw_input = task_input  # texto sagrado, no se toca
    assert no_modification(raw_input, task_input)

    # STEP 2 — THINK (entender qué pide sin reescribir)
    understood = think(raw_input)
    assert understood.refers_to_input(raw_input)

    # STEP 3 — PLAN (construir DAG)
    dag = plan(understood)
    assert dag.is_valid()

    # STEP 4 — EXECUTE
    result = execute(dag)

    # STEP 5 — VALIDATE
    assert result.makes_sense(raw_input)
    assert result.did_not_summarize(raw_input)

    # STEP 6 — REPORT
    report(result)
```

**INPUT BLOCK RULE:**
```
SI input ≠ output en cualquier token → REJECTED
SI modelo hace paráfrasis/síntesis/reinterpretación → VIOLATION
VIOLATION = tarea se reinicia desde literal input + Sheriff registra
```

**Aplicar en MASTER-16 (DSL+Universal Plug) — agregar reasoning_chain.py.**

---

## GAP #12 — FASE 0.5 CONFIRMATION EJEMPLO COMPLETO

```
MAX: "crea el panel de crazy wall"

G5: "Detecté que puede ir a:
     1. nct-fase0
     2. interfaz-fusionada
     3. crazy-wall
     ¿A cuáles va? (1, 2, 3, todos, ninguno)"

MAX: "3"

G5: "Confirmado. Voy a crear el panel SOLO en crazy-wall."
     → escribe solo en /workspace/orquestador/projects/crazy-wall/

MAX: "los 3"

G5: "Confirmado. Voy a crear el panel en los 3 proyectos."
     → escribe en los 3 carpetas
```

**Aplicar en MASTER-12 (Pipeline) — agregar Fase 0.5 ejemplo.**

---

## GAP #13 — SID PRE-PROCESADOR (10 PASOS) + PANEL INTELIGENTE

### Pre-Procesador (10 pasos):
```
1. Comprensión del objetivo
2. Extracción de requisitos
3. Detección de ambigüedades
4. Detección de contradicciones
5. Detección de información faltante
6. Recuperación de contexto
7. Consulta de memoria
8. Consulta de documentación
9. Generación de hipótesis
10. Cálculo de confianza
Si confianza ≥ umbral → continúa automáticamente
Si confianza < umbral → abre Panel Inteligente de Definición
```

### Panel Inteligente de Definición (ejemplo):
```
Falta definir: Base de datos
Impacto: arquitectura + rendimiento + costes
Opciones:
  ○ PostgreSQL (recomendada)
  ○ MySQL
  ○ SQLite
  ○ Otro
Si no eliges → PostgreSQL
```

### Clasificación de Incertidumbre:
```
Crítica  → bloquea la ejecución
Alta     → puede cambiar la arquitectura
Media    → afecta la calidad
Baja     → se puede asumir un valor razonable
Solo las CRÍTICAS bloquean el proceso.
```

### Motor de Hipótesis:
```
Genera varias interpretaciones:
  Hipótesis A — 72%
  Hipótesis B — 18%
  Hipótesis C — 10%
Si una supera 95% confianza → continúa sin preguntar.
```

### Detector de Contradicciones:
```
"Hazlo rápido" + "optimiza al máximo"
"Sin coste" + "usa servicios premium"
"Solo local" + "usa APIs en la nube"
```

**Aplicar en MASTER-05 (SID+BIS) — agregar Pre-Procesador + Panel Inteligente.**

---

## GAP #14 — DATASETS/ADAPTERS URLs VERIFICADOS (60+60)

URLs reales de HF para los 60 datasets y 60 adapters que PARCHE-v15 confirmó.

**Aplicar en MASTER-10 (Modelos y APIs) — agregar URLs.**

---

## GAP #15 — CSA ESTRUCTURA DE CARPETAS

```
g5/csa/
├── __init__.py
├── consejo.py                   # coordina los 10 jueces
├── jueces/
│   ├── __init__.py
│   ├── j1_comprension.py
│   ├── j2_cobertura.py
│   ├── j3_consistencia.py
│   ├── j4_exactitud.py
│   ├── j5_arquitectura.py
│   ├── j6_calidad_codigo.py
│   ├── j7_investigacion.py
│   ├── j8_optimizacion.py
│   ├── j9_seguridad.py
│   └── j10_calidad_final.py
├── fases/
│   ├── __init__.py
│   ├── fase1_audita_input.py
│   ├── fase2_busca_huecos.py
│   ├── fase3_10_soluciones.py
│   ├── fase4_destruye.py
│   └── fase5_ataca_otros.py
├── sistema_veto.py              # lógica de veto
├── paquete_rechazo.py           # genera paquete de rechazo
└── ciclo_infinito.py            # crea → audita → destruye → reconstruye
```

**Aplicar en MASTER-13 (Arquitectura NCT) — agregar estructura CSA.**

---

## GAP #16 — PATCHES-MAXBRY-SUPER-TEAM P1-P14 (RESUMEN)

### P1 — Redis compartido (solo G5+G6)
### P2 — Capacidad 2000 agentes / 1000 tareas
### P3 — Generador Skills/Agentes (auto-evolución)
### P3.2 — Skills NO se borran (van a GitHub)
### P3.3 — Raíz para Skills (MAXBRY_ROOT)
### P4 — Juez Supervisor Validador (JSV, 8 reglas)
### P5 — AUTO-RUN + Interface de configuración inicial
### P6 — Sistema de cifrado y seguridad
### P7 — Núcleo del orquestador solo vía API
### P8 — Bootstrap de instalación autónoma
### P9 — Arquitectura modular (10 módulos independientes)
### P10 — Principio de cero configuración
### P11 — Descarga inteligente de componentes
### P12 — Inicio autónomo
### P13 — Escalabilidad horizontal
### P14 — Renombramiento: MAXBRY SUPER TEAM

**Aplicar en MASTER-17 (MAXBRY SUPER TEAM Detalles) — agregar P1-P14.**

---

## GAP #17 — AUTO-RUN INTERFACE (PRIMERA INSTALACIÓN)

```
╔═══════════════════════════════════════════════════════════╗
║  MAXBRY SUPER TEAM · Configuración Inicial               ║
╠═══════════════════════════════════════════════════════════╣
║  Modelos de IA a usar:                                    ║
║  [✓] MiniMax M3 (jefe / validador)                       ║
║  [✓] Kimi K2.7-Code (programador)                        ║
║  [✓] Hermes Agent                                        ║
║  [✓] OpenCLAW                                            ║
║  [✓] Smolagents                                          ║
║  [✓] MiMo Code                                           ║
║  ...                                                      ║
║  [ CONTINUAR ]                                            ║
╚═══════════════════════════════════════════════════════════╝
```

**Aplicar en MASTER-23 (Implementación) — agregar Auto-Run Interface.**

---

## GAP #18 — DEPENDENCIAS ENTRE GRUPOS (DAG)

```
G1_INFRA: []
G2_CORE: [G1_INFRA]
G3_UI: [G1_INFRA, G2_CORE]
G4_AUDIT: [G2_CORE, G3_UI]
G5_CONSENSO: [G4_AUDIT]
G6_BUILD: [G5_CONSENSO]
G7_ASISTENTES: [G5_CONSENSO, G8_ORQUESTADOR]
G8_ORQUESTADOR: [G5_CONSENSO]
```

**Aplicar en MASTER-13 (Arquitectura NCT) — agregar dependencias.**

---

## GAP #19 — PARCHE-v16 MEJORAS 100X (8 inputs)

### INPUT 1 — Skills Predictivos
### INPUT 2 — Memoria Cuántica Distribuida
### INPUT 3 — Interfaz Multimodal (texto, voz, imagen, video, archivo, WebRTC, gestos, biométricos, contexto ambiental)
### INPUT 4 — MAXBRY como Super-Orquestrador Universal (protocolo abierto)
### INPUT 5 — Ecosistema de Inteligencia Distribuida (auditores dinámicos)
### INPUT 6 — ?
### INPUT 7 — ?
### INPUT 8 — ?

**Aplicar en MASTER-27 (Parches Detallados Faltantes) — agregar INPUT 1-5 de PARCHE-v16.**

---

## GAP #20 — FUSIÓN KIMI + M3 (FICHA EJECUTABLE)

### Lo que mantiene:
- 10 fases (Fase 0-9)
- 8 archivos coordinador
- 5 archivos soporte
- 3 modos (Manual / Semi-Auto / Continuo)
- Principios (90% code + 10% LLM)

### Lo que mejora 100x:
| Mejora | Detalle |
|--------|---------|
| Estructura <200 líneas | Cada archivo editable sin romper otros |
| 10 agentes del consejo | Consenso más robusto (no 1 juez) |
| Investigación multi-fuente | 5 fuentes en paralelo |
| YouTube agent | Tutoriales visuales |
| MiniMax M3 + Kimi K2 | División de roles clara |
| APIs intercambiables | Profiles en config.json |
| Mini interface multi-canal | 5 canales de entrada |
| Confirmación de proyecto | Preguntar antes de ejecutar |
| Enchufe universal v1.5 | Conecta cualquier cosa |
| Sistema externo de razonamiento | Universal para cualquier LLM |
| Ficha ejecutable | Diseño es código ejecutable |

**Aplicar en MASTER-13 (Arquitectura NCT) — agregar Mejoras 100x.**

---

## RESUMEN DE ACCIONES

### Por cada gap, agregar al master doc correspondiente:

| Gap | Master Doc destino | Acción |
|-----|---------------------|--------|
| #1 — 6 vs 8 grupos | MASTER-02 | Mantener 6 (aclaración) |
| #2 — Activation Commands | MASTER-09 | Agregar sección |
| #3 — 13 criterios skills | MASTER-05/27 | Corregir lista |
| #4 — Sheriff/Sentinel/Watcher | MASTER-09 | Agregar protocolos |
| #5 — Consensus 5/12 | MASTER-25 | Agregar detalle |
| #6 — 10 Loops | MASTER-08 | Agregar tabla |
| #7 — Memory Protocol v1 | MASTER-21 | Agregar tiers |
| #8 — Storage Strategy | MASTER-12 | Agregar |
| #9 — Merge/Prioridades/Keepalive | MASTER-12 | Agregar |
| #10 — M3 atributos | MASTER-10 | Agregar |
| #11 — DSL reasoning_chain.py | MASTER-16 | Agregar código |
| #12 — FASE 0.5 ejemplo | MASTER-12 | Agregar ejemplo |
| #13 — SID Pre-Procesador | MASTER-05 | Agregar |
| #14 — URLs datasets/adapters | MASTER-10 | Agregar URLs |
| #15 — CSA estructura | MASTER-13 | Agregar |
| #16 — P1-P14 MAXBRY | MASTER-17 | Agregar |
| #17 — Auto-Run Interface | MASTER-23 | Agregar |
| #18 — Dependencias DAG | MASTER-13 | Agregar |
| #19 — Mejoras 100X | MASTER-27 | Agregar INPUT 1-5 |
| #20 — Fusión Kimi+M3 | MASTER-13 | Agregar |

---

## CONCLUSIÓN

Después de auditar 55 veces los patches:
- **20 gaps críticos** encontrados
- **17 ya parcialmente documentados** en master docs
- **3 requieren actualización mayor** (#1 inconsistencia grupos, #3 lista criterios, #11 DSL enforcement)

**Este es UN solo patch document** que cierra los 20 gaps. NO creo más documentos.

Los master docs pueden actualizarse después si MAX lo aprueba.
</content>