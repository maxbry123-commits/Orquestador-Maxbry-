# NCT NEURONAS CODE TURBO
## ORQUESTADOR AGÉNTICO — ARQUITECTURA COMPLETA v0.1
### Base para FABLES — diseño y construcción del kernel

---

## 1. CAMBIO DE PARADIGMA

**ANTES:** Capa de razonamiento → controla UNA LLM → solo pensamiento

**AHORA:** Orquestador agéntico → coordina N agentes reales
- Cada agente = proceso real en Antigravity, NO LLM simulado
- El orquestador decide quién hace qué, cuándo y con qué datos
- Los agentes se comunican via JSON sobre HTTP o Message Queue
- Estado compartido entre agentes via state.json
- Si un agente falla → recovery automático sin intervención humana

---

## 2. JERARQUÍA DE ROLES

### NIVEL 0 — DIRECTOR (humano)
- Define objetivo, prioridades, restricciones
- Define Definition of Done
- Puede omitir pasos del pipeline
- Aprueba o detiene el pipeline
- Decide cambios de modelo
- Única fuente de autoridad final

### NIVEL 1 — ORQUESTADOR (cerebro operativo)
- Planifica y divide tareas en atómicas
- Genera JSON por cada paso del pipeline
- Coordina asesores y auditores
- Mantiene state_json y crazy_wall
- Detecta desviaciones del objetivo
- Decide reintentos o fallback
- Activa RECOVERY en fallos
- NO implementa código
- NO ejecuta lógica final
- NO modifica arquitectura

### NIVEL 2 — CONSEJO DE CONSENSO (3 asesores)
- OPUS: arquitectura + análisis profundo + planificación estratégica
- DEEPSEEK R1: razonamiento estructurado + lógica + sistemas
- KIMI K: código + implementación + breakdown de tareas técnicas
- Regla de consenso: mínimo 2 de 3 deben coincidir
- Sin consenso → estado: CONSENSUS_BLOCKED
- No se avanza sin consenso en decisiones de arquitectura

### NIVEL 3 — AUDITORES (3 capas de validación)
- AUDITOR_1 (GPT): estructura + coherencia + formato JSON
  - Output: OK / RECHAZO / CAMBIOS_REQUERIDOS
- AUDITOR_2 (Gemini): validación ejecutable Antigravity
  - Valida: pipeline paso a paso, no ambigüedad, no mezcla
  - Output: OK_EXEC / FIX_REQUIRED / REJECT
- AUDITOR_3 (Gemini): validación final de arquitectura completa
  - Valida: consistencia global, riesgo de fallos, capacidad real
  - Output: APPROVED / BLOCKED

### NIVEL 4 — EJECUTORES (workers intercambiables)
- Solo implementan, no deciden arquitectura
- No modifican objetivos ni plan definido
- No seleccionan tecnologías por cuenta propia
- No redefinen el alcance
- Intercambiables según tipo de tarea
- Viven en Antigravity sandbox
- Claude Code Rust como agente ejecutor principal

---

## 3. REGLAS DE GOBERNANZA

### SEPARACIÓN DE RESPONSABILIDADES
- Builder ≠ Validator (el que construye no valida su propio trabajo)
- Validator ≠ Witness (el que valida no atestigua)
- Writer ≠ Reviewer (el que escribe no revisa su propio código)
- Ningún modelo trabaja solo — siempre: Writer → Reviewer → Approved

### REGLAS DE CÓDIGO
- all_code_requires_review: true
- minimum_reviewers: 1
- critical_components minimum_reviewers: 2

### REGLAS DE ARQUITECTURA
- all_architecture_requires_review: true
- minimum_reviewers: 2
- Ninguna arquitectura se aprueba sin consenso de 2 modelos

### REGLAS DE CONSENSO
- Menos de 2 modelos de acuerdo → CONSENSUS_BLOCKED
- No se avanza sin consenso en decisiones arquitectónicas
- Timeout de consenso: máximo 3 rondas de debate

### REGLAS DE EVIDENCIA
- Antes de cerrar tarea: verificar resultado observable
- No valen: planes bonitos, documentos bonitos, arquitecturas bonitas
- Solo valen: cuenta creada, repo creado, endpoint responde, login funciona
- RESULTADO_REQUIRED obligatorio antes de marcar tarea como DONE

### REGLAS DE RECUPERACIÓN
- DRIFT_DETECTED cuando: objetivo ≠ trabajo actual
- Proceso: Pausar → Recuperar contexto → Reemitir tarea → Continuar
- Máximo 3 reintentos antes de ESCALATE al Director

---

## 4. FLUJO DEL PIPELINE (11 PASOS)

```
PASO 01: Director define objetivo + prioridades + restricciones
         Output: objetivo_formal + definition_of_done

PASO 02: Orquestador inicia Discovery obligatorio
         Output: contexto_completo + state_json inicial + crazy_wall

PASO 03: Consejo de Consenso (Opus + DeepSeek + Kimi) debate y analiza
         Output: 3 propuestas independientes

PASO 04: Consenso Engine evalúa propuestas
         → Consenso logrado: planificación + DSL
         → Sin consenso: CONSENSUS_BLOCKED

PASO 05: Ejecutor asignado según tipo de tarea
         → Infraestructura: ejecutor infra
         → Código: Claude Code Rust / Qwen Code
         → Arquitectura: Opus

PASO 06: Implementación supervisada
         El ejecutor solo implementa — no decide, no modifica plan

PASO 07: Human Checkpoint (si requiere acción física)
         Estado: WAITING_HUMAN → HUMAN_CONFIRMED

PASO 08: Auditor_1 (GPT) verifica evidencia observable
         Output: OK | REJECT | FIX_REQUIRED

PASO 09: Orquestador valida resultado observable
         ¿Existe resultado observable? ¿Evidencia suficiente?

PASO 10: Con evidencia → DONE
         Sin evidencia → Recovery o NOT_DONE

PASO 11: Preparación Antigravity
         Dry-run de execution_package.md
         ¿Validación pasa? → Enviar a Antigravity
         ¿No pasa? → BLOCKED
```

---

## 5. MODO EXECUTION_ONLY

Cuando el plan ya existe y no hay necesidad de rediseñar:
- Saltar pasos 02-04 del pipeline
- Ir directo al paso 05 (ejecutor asignado)
- Orquestador activa flag: EXECUTION_ONLY_MODE = true
- El Auditor sigue activo en pasos 08-09

---

## 6. JSON POR PASO (ESTRUCTURA OBLIGATORIA)

Cada paso del pipeline tiene obligatoriamente estos campos:

```json
{
  "paso_id": "string",
  "input": "qué recibe este paso",
  "output": "qué produce este paso",
  "schema": "estructura de datos del output",
  "restricciones": ["qué no puede hacer este paso"],
  "modelo_asignado": "quién ejecuta este paso",
  "timeout_segundos": 300,
  "on_failure": "RETRY | ESCALATE | BLOCK",
  "max_retries": 3
}
```

---

## 7. LOS 14 ESTADOS DEL SISTEMA

```
IDLE              → sistema en espera
DISCOVERY         → buscando contexto y recursos
PLANNING          → generando plan de ejecución
CONSENSUS_ACTIVE  → asesores debatiendo
CONSENSUS_BLOCKED → no se logró consenso
EXECUTING         → ejecutor trabajando
WAITING_HUMAN     → esperando acción física del Director
HUMAN_CONFIRMED   → Director confirmó acción
AUDITING          → auditor verificando resultado
RECOVERY          → recuperando de un fallo
DRIFT_DETECTED    → objetivo ≠ trabajo actual
BLOCKED           → pipeline bloqueado, requiere intervención
NOT_DONE          → tarea fallida sin recovery posible
DONE              → tarea completada con evidencia
```

---

## 8. LOS 6 ARTEFACTOS DEL SISTEMA

```
1. state.json         → fuente de verdad del estado actual
2. crazy_wall         → mapa vivo del workflow
3. task_graph         → grafo de tareas y dependencias
4. execution_package  → paquete listo para Antigravity
5. audit_log          → registro completo de auditorías
6. recovery_json      → estado serializado para reinicio
```

---

## 9. COMPONENTES TÉCNICOS INTERNOS

### DISCOVERY ENGINE
- Tipo: exploración no lineal
- Genera hipótesis: estándar, extrema, inversa, híbrida, emergente
- Busca: contexto, dependencias, recursos disponibles, restricciones ocultas
- Loop interno: si no hay novedad → expandir / si hay novedad → escalar
- Output: knowledge_pack estructurado

### CONSENSUS ENGINE
- Recibe las 3 propuestas del Consejo
- Mide coincidencia (semántica, no solo exacta)
- Máximo 3 rondas de debate
- Si 2 de 3 coinciden → consenso logrado
- Si no hay consenso en 3 rondas → CONSENSUS_BLOCKED
- Output: approved_plan o blocked_signal

### RECOVERY ENGINE (5 NIVELES)
```
NIVEL 1 — RETRY:       reintentar la operación fallida una vez más
NIVEL 2 — ROLLBACK:    revertir al último estado estable conocido
NIVEL 3 — CHECKPOINT:  cargar último checkpoint y continuar
NIVEL 4 — REPLAN:      replantear desde el punto de fallo
NIVEL 5 — ESCALATE:    escalar al Director, sistema no puede solo
```

### SELF_IMPROVEMENT_LOOP
```
Sistema ejecuta tarea
↓
Mide resultado (score numérico: calidad + tiempo + tokens)
↓
Compara con ciclos anteriores
↓
Detecta errores del ciclo anterior
↓
Ajusta reglas del JSON de control
↓
Si nuevo ciclo es peor → rollback de reglas
Si es mejor → actualizar reglas y continuar
```

### TIME + BUDGET ENGINE
```
FAST MODE     → exploración ligera, tareas simples
STANDARD MODE → análisis equilibrado, tareas medias
DEEP MODE     → investigación avanzada, tareas complejas
EXTENDED MODE → 12-24h exploración, proyectos completos
ULTRA MODE    → N horas definidas, sin límite
INFINITE MODE → sin límite temporal, condición de parada por resultado
```

Progresión temporal inteligente:
- Fase 1 (0-25%): exploración expansiva
- Fase 2 (25-50%): generación de hipótesis
- Fase 3 (50-75%): evaluación y filtrado
- Fase 4 (75-95%): consolidación
- Fase 5 (último tramo): síntesis final

---

## 10. ARQUITECTURA E1 vs E2

### E1 — FÁBRICA ACTUAL (temporal)
```
Director (móvil/iPad)
→ Open WebUI (HF Space)
→ MCP Server (SSE/HTTP)
→ Antigravity VM Linux (sandbox)
→ script_monitor.py (24/7)
→ Claude Code Rust (HF ~25MB)
→ APIs directas (Kimi/Qwen/DeepSeek/GPT/Gemini/Cerebras/Grok)
→ GitHub (4 repos — push directo)
```

### E2 — COMMAND CENTER FINAL (objetivo)
```
Director (móvil/iPad)
→ Vercel (React+Vite+PixiJS+ReactFlow — 61 funciones)
→ Cloudflare Workers (proxy)
→ HuggingFace Spaces Docker (16GB RAM):
  → hf-langgraph-core (Supervisor Central)
  → hf-director-yaiwes + MemGPT
  → hf-agent-claude-code-rust
  → 9 agentes código separados
  → 15 modelos GGUF separados
  → 4 Labs
→ APIs externas directas
→ Supabase + Neon + Cloudflare
→ GitHub (4 repos)
```

---

## 11. LOS 4 REPOSITORIOS GITHUB

- command-center-chat
- command-center-agents
- nct-neuronas-code-turbo
- nct-neuronas-labs-mirror

---

## 12. STACK TÉCNICO APROBADO

```
Agente ejecutor:    Claude Code Rust (HF ~25MB)
LangGraph:          coordina flujos entre procesos
CrewAI:             coordina agentes entre sí
APIs directas:      Kimi K / Qwen Code / Qwen 3.7 / DeepSeek /
                    GPT / Gemini / Cerebras x4 / Grok
NO usar:            OpenRouter como hub único
Puente primario:    Telegram Bot bidireccional
Puente alternativo: Open WebUI via MCP (SSE/HTTP)
Sandbox:            Antigravity VM Linux
Monitoreo:          UptimeRobot ping 2min + Watchdog 30s
BD:                 Supabase + Neon
CDN/Proxy:          Cloudflare
```

---

## 13. MULTI-AGENTE — ROL POR FORTALEZA

```
Planificación estratégica → Claude Opus
Orquestación externa      → Claude Sonnet
Código Python/JS          → Qwen Code
Código Rust/Go            → DeepSeek
Análisis crítico          → Gemini
Replanificación           → GPT
Investigación             → Kimi K
Reparación de código      → Qwen
Auditoría                 → Claude Sonnet + Gemini
Validación final          → Claude Opus
```

---

*Documento: NCT_AGENTE_ORQUESTADOR_ARQUITECTURA.md*
*Estado: BORRADOR v0.1 — para revisión de FABLES*
*Fuente: Chat NCT + conversación DeepSeek+GPT sobre orquestador Jason*
