# PATCH-AUDITORIA-GAPS-V4: 4TA PASADA
## MAXBRY SUPER TEAM · Cuarta iteración del bucle

**Versión:** 4.0
**Fecha:** 2026-06-28
**Tipo:** PATCH de auditoría (4ta pasada)
**Estado:** ✅ COMPLETO

---

## PROPÓSITO

4ta pasada de auditoría. Más gaps encontrados.

---

## GAP #51 — M2.7 FLUJO SIMPLIFICADO (5 PASOS)

```
PASO 1 — RECIBIR
  leer TASK.json
  verificar schema
  output: task_recibida_ok

PASO 2 — VERIFICAR
  chequear dependencias
  chequear keys necesarias
  chequear permisos
  output: dependencias_ok

PASO 3 — EJECUTAR
  ejecutar la tarea
  output: ejecucion_resultado

PASO 4 — VALIDAR
  tests pasan
  output compilado
  secrets detectados? no
  output: validacion_ok

PASO 5 — REPORTAR
  escribir resultado a STATE.json
  escribir a HISTORY.json (acumulativo)
  notificar a M3_chat
  output: reporte_enviado

SI FALLA EN CUALQUIER PASO:
  → escribir RECOVERY JSON
  → rollback si es necesario
  → escalar a M3_chat si retry > 2
```

**Aplicar en:** MASTER-23 (Implementación) — agregar M2.7 flow.

---

## GAP #52 — DIVISIÓN DE TAREAS GRANDES (REGLA)

```
REGLA: si tarea > 5 subtareas → dividir en bloques
cada bloque = checkpoint separado
cada bloque = recovery independiente

TAREA GRANDE → dividirse en:
  BLOQUE 1 → checkpoint_1 → output_1
  BLOQUE 2 → checkpoint_2 → output_2 (depende de output_1)
  BLOQUE 3 → checkpoint_3 → output_3 (depende de output_2)
  ...

CADA BLOQUE:
  - input_literal preservado
  - 5 GOALS fijados
  - 12 PASOS ejecutados
  - CHECKPOINT JSON escrito
  - REFUTACIÓN pasada
  - VALIDACIÓN pasada
  - OUTPUT entregado
  - RECOVERY JSON listo si falla
```

**Aplicar en:** MASTER-15 (Reglas) o MASTER-12 (Pipeline).

---

## GAP #53 — 10 MÓDULOS DE MAXBRY (P9)

```
M1  · Bootstrap (instalador + actualizador + lanzador)
M2  · Núcleo del Orquestador (planificador + scheduler + motor decisiones)
M3  · Gestor de Memoria (ChromaDB + bge-small + embeddings)
M4  · Scheduler (Dramatiq + Redis + colas paralelas)
M5  · Gestor de Agentes (registry + colmena + distribución)
M6  · Gestor de Skills (catálogo + generador + versionado)
M7  · Gestor de Modelos de IA (API keys + profiles + circuit breaker)
M8  · Sistema de Seguridad (cifrado + auth + licencias)
M9  · Sistema de Actualización (versiones + diffs + rollback)
M10 · Sistema de Monitorización (logs + métricas + alertas + dashboards)

Cada módulo:
- Carpeta independiente
- API pública clara
- Actualizable sin reinstalar
- Tests propios
- Versión propia
- Metadata versionada
```

**Aplicar en:** MASTER-13 (Arquitectura NCT) o MASTER-23 (Implementación).

---

## GAP #54 — SISTEMA DE SEGURIDAD (6 CAPAS)

```
Capa 1: CIFRADO DE COMUNICACIÓN (HTTPS/TLS)
Capa 2: AUTENTICACIÓN (API keys con tokens 1h, OAuth2 opcional)
Capa 3: FIRMAS DIGITALES (cada solicitud firmada criptográficamente)
Capa 4: RATE LIMITING (100 req/min, 1000 req/h)
Capa 5: LICENCIAS (cada instalación única, servidor valida cada arranque)
Capa 6: RESPUESTAS MÍNIMAS (API solo devuelve lo necesario, nunca paths internos)
```

**Aplicar en:** MASTER-15 (Reglas) — agregar capas seguridad.

---

## GAP #55 — NÚCLEO VÍA API (CLIENTE LIGERO vs SERVIDOR)

```
Usuario
   │
   ▼
Cliente M3 (local, 5 MB)         ← lo que el usuario tiene
   │
   ▼
API del Orquestador (servidor)    ← lo que NO se descarga
   ├── Planificador
   ├── Memoria global
   ├── Scheduler
   ├── Motor de decisiones
   ├── Agentes
   └── Modelos IA

Ventajas:
✅ Usuario NO recibe código del núcleo
✅ NO puede copiar planificador
✅ Actualizaciones sin que usuario reinstale
✅ Puedes revocar accesos
✅ El código importante NUNCA sale del servidor
```

**Aplicar en:** MASTER-13 (Arquitectura).

---

## GAP #56 — P8 BOOTSTRAP DE INSTALACIÓN AUTÓNOMA

```
Responsabilidades:
1. Detectar OS (Linux/Mac/Windows)
2. Detectar arquitectura (x86_64/arm64)
3. Verificar recursos (CPU, RAM, disco, red)
4. Comprobar dependencias necesarias
5. Instalar automáticamente
6. Crear estructura de directorios
7. Inicializar base de datos
8. Generar configuraciones iniciales
9. Generar claves criptográficas
10. Descargar solo componentes necesarios
11. Iniciar el orquestador

Características:
- Tamaño máximo: 5 MB
- NO contiene lógica del orquestador
- Solo es instalador + actualizador + lanzador
- Descarga componentes bajo demanda
- Verificación criptográfica de integridad
```

**Aplicar en:** MASTER-23 (Implementación).

---

## GAP #57 — 8 PRINCIPIOS RECTORES DEL SISTEMA RAZONAMIENTO

```
1. INPUT SAGRADO: el input NUNCA se modifica, resume, parafrasea, reinterpreta
2. DSL/DAG, NUNCA PROMPT LIBRE: salida siempre JSON estructurado
3. DETERMINISMO: mismo input + config + LLM = misma forma de razonamiento
4. UNIVERSALIDAD: cualquier LLM puede usarlo
5. EXTERNALIDAD: vive en /reasoning_system/, no en /orquestador/
6. EDITABILIDAD POR ARCHIVOS: cambiar goal/step = editar archivo, no código
7. AUDITABILIDAD: cada ejecución produce log auditable
8. AISLAMIENTO: el sistema no contamina al orquestador ni al LLM
```

**Aplicar en:** MASTER-15 (Reglas) o MASTER-11 (Razonamiento).

---

## GAP #58 — INPUT BLOCK ESTRUCTURA JSON

```json
{
  "input_block": {
    "raw": "<<input EXACTO del usuario, sin tocar>>",
    "received_at": "<<timestamp ISO 8601>>",
    "source": "<<nombre del llamador>>",
    "checks": {
      "preserve_verbatim": true,
      "no_summarize": true,
      "no_paraphrase": true,
      "no_modify": true
    },
    "status": "ACCEPTED | REJECTED"
  }
}
```

**Aplicar en:** MASTER-11 (Razonamiento).

---

## GAP #59 — 7 PROHIBICIONES EXPLÍCITAS INPUT BLOCK

```
1. Resumir el input (el usuario pidió algo específico, no un resumen)
2. Parafrasear el input (cambia el matiz semántico)
3. "Mejorar" la redacción del input (el usuario escribió como quiso)
4. Agregar contexto que no estaba (contamina la intención original)
5. Quitar partes "irrelevantes" (el LLM decidirá qué es relevante)
6. Traducir el input (cambia el idioma, cambia la semántica)
7. Reordenar las ideas del input (la estructura sintáctica porta significado)
```

**Aplicar en:** MASTER-15 (Reglas) o MASTER-11 (Razonamiento).

---

## GAP #60 — 12 PASOS STANDARD CON PROMPTS ESPECÍFICOS

```
01_literal_read (INPUT BLOCK SAGRADO)
  Prompt: "INSTRUCCIÓN SAGRADA — NO INTERPRETAR, NO RESUMIR, NO MODIFICAR..."
  Output: {"input_accepted": true, "raw_acknowledged": "..."}
  Conexión: entrada a 02_think. Si falla → REJECTED

02_think (análisis)
  Prompt: "Considerando los goals y el input verbatim, ¿qué estás entendiendo?"
  Output: {"thinking": ["obs1", "obs2", "obs3"]}

03_plan (planificación)
  Prompt: "Genera un plan de 3-7 pasos para cumplir goal_primary"
  Output: {"plan": [{"step": 1, "action": "...", "expected_output": "..."}]}

04_decompose (descomposición)
  Prompt: "Para cada paso del plan, identifica las subtareas atómicas"
  Output: {"decomposition": [{"plan_step": 1, "atomic_tasks": [...]}]}

05_hypotheses (generación hipótesis)
  Prompt: "Para cada atomic_task, propón 2-4 hipótesis de solución alternativas"
  Output: {"hypotheses": [{"task_id": "...", "alternatives": [...]}]}

06_swarm (ejecución paralela conceptual)
  Prompt: "Para cada hipótesis, evalúa: esfuerzo, riesgo, alineamiento"
  Output: {"swarm_results": [{"h_id": "h1", "effort": "low|med|high", ...}]}

07_critic (crítica adversarial)
  Prompt: "Como crítico, ¿qué falla en cada hipótesis?"
  Output: {"critiques": [{"h_id": "h1", "weakness": "...", "severity": "..."}]}

08_simulate (simulación)
  Prompt: "Simula paso a paso la ejecución de la hipótesis ganadora"
  Output: {"simulation": [{"phase": "...", "result": "...", "issues": []}]}

09_validate (validación)
  Prompt: "¿La simulación cumple goal_success? ¿Respeta goal_restriction?"
  Output: {"validation": {"meets_success": true|false, "respects_restriction": ...}}

10_consensus (consenso interno)
  Prompt: "Considerando thinker, critic, simulator, validator, ¿cuál es la decisión?"
  Output: {"consensus": {"decision": "...", "confidence": 0.0-1.0, "votes": [...]}}

11_report (reporte)
  Prompt: "Genera el reporte final en formato DSL"
  Output: {"report": {<DSL final>}}

12_audit (auditoría)
  Prompt: "Auditoría: ¿se respetó input sagrado? ¿se ejecutaron los 12 pasos?"
  Output: {"audit": {"input_respected": true, "verdict": "PASS|FAIL", "notes": "..."}}
```

**Aplicar en:** MASTER-11 (Razonamiento) — agregar los 12 pasos detallados.

---

## GAP #61 — M3 EN CADA SALIDA (FORMATO)

```
ANTES DE CADA SALIDA:
  mostrar:
    > system prompt mythos ejecutado
    > goals: [lista]
    > pasos completados: [1-12]
    > checkpoints: [uuid]
    > refutacion: [ok | fail]
    > validacion: [ok | fail]

DESPUÉS DE CADA SALIDA:
  mostrar:
    > self_audit: [ok | fail]
    > input_preserved: true
    > output_validated: true
```

**Aplicar en:** MASTER-15 (Reglas).

---

## GAP #62 — M2.7 EN CADA EJECUCIÓN (LOG)

```
log en STATE.json:
  > system_prompt_mythos: executed
  > paso_actual: [1-5]
  > checkpoint_id: [uuid]
```

**Aplicar en:** MASTER-23 (Implementación).

---

## GAP #63 — REFUTACIÓN (5 PREGUNTAS OBLIGATORIAS)

```
PREGUNTAS OBLIGATORIAS (antes de output final):
  □ ¿qué asumí sin verificar?
  □ ¿qué puede romper esta salida?
  □ ¿qué restricción violé?
  □ ¿qué información inventé?
  □ ¿qué dependencias no chequeé?

SI ALGUNA RESPUESTA ES PROBLEMÁTICA:
  → volver al paso 1
  → NO presentar output refutado
```

**Aplicar en:** MASTER-11 (Razonamiento).

---

## GAP #64 — ESTRUCTURA SISTEMA RAZONAMIENTO

```
/reasoning_system/
├── README.md
├── config.json
├── goals/ (5 goals standard)
├── goals_turbo/ (7 goals extra)
├── steps/ (12 pasos standard)
├── steps_turbo/ (33 pasos extra)
├── prompts/
│   ├── standard_dsl.json
│   ├── turbo_dsl.json
│   └── input_block_rule.json
├── runner.py
├── loader.py
└── api.py
```

**Aplicar en:** MASTER-11 (Razonamiento) o MASTER-13 (Arquitectura).

---

## GAP #65 — VALIDACIÓN OBLIGATORIA (CHECKS)

```
CHECKS OBLIGATORIOS (antes de output final):
  □ input preservado verbatim
  □ output no resume el input
  □ output no parafrasea el input
  □ output responde a los 5 GOALS
  □ output cumple restricción innegociable
  □ checkpoints escritos
  □ refutación pasada
  □ consensus aplicado (si aplica)

SI ALGUNA FALLA:
  → REJECTED
  → recovery
```

**Aplicar en:** MASTER-15 (Reglas).

---

## GAP #66 — PROTOCOLO DE RECUPERACIÓN

```
SI TAREA FALLA:
  1. escribir RECOVERY JSON inmediatamente
  2. identificar último CHECKPOINT válido
  3. si retry_count < 2 → rollback al checkpoint, retry
  4. si retry_count >= 2 → escalar a M3_chat
  5. M3_chat decide: más retries, redesign, o cancelar

NUNCA:
  - inventar output cuando falla
  - saltarse pasos para "avanzar"
  - ignorar violaciones
  - borrar checkpoints válidos
```

**Aplicar en:** MASTER-08 (Loop) o MASTER-12 (Pipeline).

---

## GAP #67 — USO DE MEMORIA M3 Y M2.7

```
M3_chat MEMORIA:
  - memory_topic_append después de cada sesión importante
  - leer memory_topic_read al inicio de cada sesión nueva
  - BORRADOR-LISTA-APROBADOS.md = fuente de verdad visible

M2.7 MEMORIA:
  - leer BORRADOR-LISTA-APROBADOS.md al iniciar
  - STATE.json = estado actual
  - HISTORY.json = histórico completo (nunca borrar)

BORRADOR-LISTA-APROBADOS.md:
  - se actualiza con CADA cambio aprobado
  - se actualiza con CADA nueva propuesta
  - se actualiza con CADA tarea completada
  - es la fuente de verdad para todo
```

**Aplicar en:** MASTER-12 (Pipeline) o MASTER-23 (Implementación).

---

## GAP #68 — INTEGRACIÓN SYSTEM PROMPT MYTHOS + RAZONAMIENTO EXTERNO

```
DIFERENCIA:
  system prompt mythos → reglas y流程 visible (este doc)
  /reasoning_system/ → librería Python con funciones

AMBOS DEBEN USARSE:
  M3 lee system prompt mythos al inicio
  M3 usa reasoning_system.reason() para tareas complejas
  M2.7 lee system prompt mythos al inicio
  M2.7 usa reasoning_system.reason() si necesita razonar

INTEGRACIÓN:
  system prompt mythos = capa de comportamiento
  reasoning_system = capa de ejecución
  juntos = sistema completo
```

**Aplicar en:** MASTER-11 (Razonamiento).

---

## RESUMEN DE GAPS NUEVOS

### 18 gaps nuevos en 4ta pasada:

| # | Gap | Master destino |
|---|-----|----------------|
| 51 | M2.7 flujo simplificado 5 pasos | MASTER-23 |
| 52 | División de tareas grandes (regla) | MASTER-15 |
| 53 | 10 módulos MAXBRY | MASTER-13 |
| 54 | 6 capas de seguridad | MASTER-15 |
| 55 | Núcleo vía API (cliente ligero) | MASTER-13 |
| 56 | P8 Bootstrap instalación | MASTER-23 |
| 57 | 8 Principios Rectores | MASTER-15 |
| 58 | INPUT BLOCK estructura JSON | MASTER-11 |
| 59 | 7 Prohibiciones explícitas | MASTER-15 |
| 60 | 12 pasos con prompts específicos | MASTER-11 |
| 61 | M3 formato salida | MASTER-15 |
| 62 | M2.7 log ejecución | MASTER-23 |
| 63 | Refutación 5 preguntas | MASTER-11 |
| 64 | Estructura sistema razonamiento | MASTER-11 |
| 65 | Validación obligatoria checks | MASTER-15 |
| 66 | Protocolo de recuperación | MASTER-08 |
| 67 | Uso de memoria M3/M2.7 | MASTER-12 |
| 68 | Integración system prompt + razonamiento | MASTER-11 |

---

## TOTAL ACUMULADO

```
1er patch (V1): 20 gaps
2do patch (V2): 13 gaps
3er patch (V3): 17 gaps
4to patch (V4): 18 gaps
─────────────────────
TOTAL:          68 gaps identificados
```

---

## CONCLUSIÓN

Continuaré auditando si encuentro más gaps en próxima iteración.
</content>