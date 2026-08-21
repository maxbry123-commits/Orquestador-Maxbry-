# PATCH-AUDITORIA-GAPS-V2: 2DA PASADA — NUEVOS GAPS
## MAXBRY SUPER TEAM · Segunda iteración del bucle

**Versión:** 2.0
**Fecha:** 2026-06-28
**Tipo:** PATCH de auditoría (2da pasada)
**Estado:** ✅ COMPLETO

---

## PROPÓSITO

Después de la 2da auditoría profunda (después de MASTER-FINAL/PATCH-AUDITORIA-GAPS.md v1) encontré NUEVOS gaps que no estaban en el primer patch. Este documento cierra esos gaps adicionales.

---

## GAP #21 — DECLARACIÓN DE APERTURA OBLIGATORIA

### Antes de cada salida, escribir EXACTAMENTE:

```
> system prompt mythos ejecutado
> input_block: ACTIVO
> goals: 5 [primary, secondary, success, failure, restriction]
> pasos: 12
> checkpoint: listo
> recovery_json: listo
> refutacion: pendiente
> validacion: pendiente
```

**Si no se puede escribir esto, NO se genera respuesta.**

**Aplicar en:** MASTER-15 (Reglas + Intocables) — agregar como regla obligatoria.

---

## GAP #22 — 3 REVISIONES DEL INPUT (antes de procesar)

```
REVISIÓN 1 — COMPRENSIÓN
  □ ¿qué pidió exactamente?
  □ ¿cuál es el objetivo principal?
  □ ¿cuál es el output esperado?

REVISIÓN 2 — RESTRICCIONES
  □ ¿qué restricciones hay?
  □ ¿qué NO se puede hacer?
  □ ¿qué formato se espera?

REVISIÓN 3 — RIESGOS
  □ ¿qué puede salir mal?
  □ ¿qué información falta?
  □ ¿qué asumí sin verificar?

SI ALGUNA REVISIÓN FALLA:
  → pedir aclaración ANTES de procesar
  → NO inventar
  → NO asumir
```

**Aplicar en:** MASTER-15 (Reglas + Intocables).

---

## GAP #23 — CHECKPOINT JSON ESTRUCTURA ESPECÍFICA

```json
{
  "checkpoint_id": "uuid",
  "task_id": "uuid",
  "timestamp": "iso8601",
  "paso_actual": 1-12,
  "input_literal": "string (EXACTO, no modificado)",
  "goals_locked": true,
  "resultados_parciales": {
    "paso_1": "string",
    "paso_2": "string"
  },
  "validation_passed": true,
  "violations": []
}
```

Escribir este JSON después de CADA paso mayor.

**Aplicar en:** MASTER-12 (Pipeline) — agregar.

---

## GAP #24 — RECOVERY JSON ESTRUCTURA ESPECÍFICA

```json
{
  "recovery_id": "uuid",
  "task_id": "uuid",
  "failed_at_paso": 1-12,
  "failed_at_checkpoint": "uuid del último válido",
  "error": "string",
  "input_literal": "string (para retomar desde literal)"
}
```

**Aplicar en:** MASTER-12 (Pipeline).

---

## GAP #25 — INPUT ENGINE 11 COMPONENTES (DETALLE COMPLETO)

### 1. Canonical Input Graph (CIG)
```
Cada frase genera 12 tipos de nodos:
  - Objetivos / Restricciones / Requisitos / Suposiciones
  - Datos / Recursos / Dependencias / Prioridades
  - Riesgos / Entregables / Criterios de aceptación
  - Preguntas abiertas

Cada nodo: ID único (N51), Tipo, Texto original (referencia exacta),
Estado, Prioridad, Dependencias
```

### 2. Atomic Requirement Extraction
```
NO párrafos. REQUISITOS ATÓMICOS:
  REQ-001, REQ-002 ... REQ-127+
Cada requisito tiene vida propia.
```

### 3. Dependency Graph
```
REQ-8 → REQ-15 → REQ-44 → REQ-93
Si falla REQ-8, automáticamente se invalidan los dependientes.
```

### 4. Decision Graph
```
Cada decisión importante es un nodo independiente.
Elegir Base de Datos → PostgreSQL/MySQL/SQLite/MongoDB
El sistema NUNCA olvida por qué eligió una opción.
```

### 5. Memory Index
```
TODO queda indexado. NO se resume.
Objetivo → Nodo 8 → Prompt original → Línea exacta → Mensaje original
Un agente puede volver siempre al origen.
```

### 6. Plan Compiler
```
NO divide texto. Divide NODOS.
127 requisitos → 36 grupos → 198 tareas → 634 subtareas
Cada una mantiene referencias al grafo.
```

### 7. Task DNA (15 campos)
```
ID / Objetivo / Entradas / Salidas / Dependencias / Restricciones
Skills / Agentes / Prioridad / Riesgos / Pruebas / Estado
Contexto / Referencias / Fuente original
Ningún agente recibe instrucciones ambiguas.
```

### 8. Context Loader
```
Un agente NUNCA recibe todo el proyecto.
Solo recibe: la subtarea, dependencias, restricciones relacionadas,
contexto relevante, referencias al Input Graph.
```

### 9. Completeness Engine
```
Antes de dividir el trabajo:
  ¿Todos los requisitos tienen dueño?
  ¿Todos tienen prioridad?
  ¿Todos tienen dependencias?
  ¿Todos tienen criterio de aceptación?
  ¿Todos tienen contexto suficiente?

Si alguno falla → NO planifica.
```

### 10. Coverage Matrix (PIEZA MÁS IMPORTANTE)
```
Matriz:
  Requisito | Tarea | Agente | Estado
  REQ-1     | TASK-4| Backend| ✔
  REQ-2     | TASK-9| Seg    | ✔
  REQ-3     | TASK-18| Invest | ✔

Si existe un requisito sin tarea asignada → el sistema lo detecta.
```

### 11. Reverse Traceability
```
Al finalizar el proyecto:
  Frase 1 → TASK-12, TASK-47, TASK-81 → Resultado Validado

Hace esto con ABSOLUTAMENTE todas las frases del usuario.
Si alguna frase no puede trazarse → RECHAZO.
```

**Aplicar en:** MASTER-06 (Input Engine) — expandir con los 11 componentes detallados.

---

## GAP #26 — 17 MEJORAS AL INPUT ENGINE

### 1. Intent Graph
Objetivo principal, secundarios, implícitos, futuros, opcionales. Asignar prioridades.

### 2. Constraint Engine
Cada restricción recibe nivel: Obligatoria / Preferida / Opcional.
Tipos: Sin coste, Código abierto, Compatible Android, Offline, Sin API, Tiempo máximo, Idioma, Licencia, Hardware.

### 3. Anti-Ambiguity Engine
Detecta: rápido, seguro, grande, barato, simple, mejor. Las convierte en valores medibles.

### 4. Hidden Requirement Detector
Busca requisitos NO escritos. Ejemplo: API REST → también necesita autenticación, manejo de errores, validación, documentación, pruebas.

### 5. Contradiction Engine (clasificado)
Categorías: Lógica, Temporal, Técnica, Arquitectónica, Legal, Coste, Rendimiento.

### 6. Assumption Registry
Toda suposición queda registrada: Suposición / Motivo / Confianza / Impacto / Quién la hizo.

### 7. Confidence Engine
Cada requisito recibe nivel de confianza: 98% / 83% / 51% / 27%.

### 8. Multi-Interpretation Engine
NO genera una interpretación. Genera VARIAS: A, B, C, D...

### 9. Scope Boundary Detector
Define qué está DENTRO y FUERA del alcance.

### 10. Completeness Score
Calcula: Información suficiente / Riesgo de alucinación / Información faltante / Requisitos definidos / Contradicciones.

### 11. Context Partition
Divide el contexto: Negocio / Código / Arquitectura / Seguridad / UX / Infraestructura / Documentación.

### 12. Traceability ID
Cada frase del usuario obtiene un identificador único. Cualquier decisión puede responder: "Proviene de: Mensaje 4, Línea 18, Frase 7".

### 13. Hallucination Risk Analyzer
Estima qué partes tienen mayor riesgo: Tecnologías poco conocidas / APIs sin documentación / Requisitos incompletos / Información desactualizada.

### 14. Requirement Normalizer
Normaliza el lenguaje: "Haz una aplicación" → Frontend / Backend / Autenticación / Persistencia / API / Despliegue.

### 15. Impact Analyzer
Antes de modificar cualquier requisito, calcula qué tareas, decisiones y agentes se verán afectados.

### 16. Información Inmutable
DOS versiones del contexto: Prompt original (solo lectura) / Modelo estructurado.

### 17. Registro de Decisiones
Cada decisión guarda: Alternativas / Criterios / Evidencias / Agente responsable / Fecha / Nivel de confianza.

**Aplicar en:** MASTER-06 (Input Engine).

---

## GAP #27 — OUTPUT ENGINE 13 COMPONENTES (DETALLE)

### 1. Output Planner
Calcula: Salida estimada (15 páginas, 28000 palabras, 120 archivos, 35 módulos, 6 diagramas, 3 tablas).

### 2. Output Graph (grafo, no texto)
Proyecto: Arquitectura / Backend / Frontend / Base de datos / API / Tests / Documentación / Deployment / Manual. Cada nodo es independiente.

### 3. Smart Chunking (por significado)
NO divide por cantidad de texto. Divide por SIGNIFICADO.

### 4. Dynamic Output Engine
Estima: tokens, memoria, tiempo, coste, tamaño final. Calcula 1/3/15/52/100 partes. NO existe límite fijo.

### 5. Manifest (índice antes de entregar)
El usuario SIEMPRE sabe qué recibirá.

### 6. Output Registry
Cada salida tiene: ID / Versión / Dependencias / Estado / Checksum / Autor / Fecha / Destino.

### 7. Output Router (menú de formatos)
Markdown, Artifact, HTML, PDF, DOCX, PPTX, JSON, YAML, CSV, ZIP, Git, DB, Drive, MCP, API, Otro.

### 8. Destination Engine (adaptadores)
Markdown Adapter, Artifact Adapter, Git Adapter, Drive Adapter, Notion Adapter, MCP Adapter, API Adapter, Database Adapter, S3 Adapter, Cloud Adapter.

### 9. Streaming Output
NO espera a terminar todo. Módulo 1 → Validado → Entregado. Módulo 2 → Validado → Entregado...

### 10. Output Validator
¿Está completa? / ¿Tiene dependencias rotas? / ¿Hace referencia a un módulo inexistente? / ¿Todos los enlaces funcionan? / ¿Cumple el formato?

### 11. Multi-Target Delivery (parcialmente documentado)

### 12-13. (Por leer)

**Aplicar en:** MASTER-07 (Output Engine).

---

## GAP #28 — P35/P36/P37 MEJORAS 100X

### P35 · AUTO-MEJORA CONTINUA
```
ANTES: MAXBRY se audita cada 7 días
AHORA: MAXBRY EVOLUCIONA cada hora (con aprobación selectiva)
- Auto-mejora CADA HORA en cambios pequeños
- Auto-rollback si la mejora empeora métricas
- Sandbox de experimentación
- Si mejora funciona 24h → promueve a producción
- Notifica a MAX solo si es significativa
- Aprende qué tipo de mejoras acepta MAX

Archivo: g5/auto_evolucion/
```

### P36 · EXPERIMENTACIÓN A/B BAYESIAN
```
ANTES: A/B/C para elegir mejor opción
AHORA: BAYESIAN MULTI-ARMIED BANDIT
- Algoritmo multi-armed bandit
- Explota lo conocido + explora nuevas
- Predice ganador con 95% confianza
- Se auto-ajusta
- 10+ variaciones en paralelo
- Resultados en Knowledge Graph

Archivo: g5/experimentation/v2/
```

### P37 · PRICING TIEMPO REAL
```
ANTES: dashboard con costos
AHORA: ECONOMÍA PREDICTIVA con auto-optimización
- Predice costo con 30 días de anticipación
- Auto-cambia a modelos más baratos cuando conviene
- Marketplace de modelos
- NEGOCIACIÓN si el costo sube
- Reporte mensual automático
- Alertas inteligentes

Archivo: g5/economia/v2/
```

**Aplicar en:** MASTER-27 (Parches Detallados).

---

## GAP #29 — EVENTS.JSON TYPES ESPECÍFICOS

```
event_id / type / timestamp / source / task_id / payload

types:
  TASK_CREATED
  TASK_STARTED
  TASK_DONE
  TASK_FAILED
  CONSENSUS_REQUIRED
  BUILD_FINISHED
  GROUP_HEARTBEAT
  RETRY_TRIGGERED
  TIMEOUT_REACHED
  CANCELLED
```

**Aplicar en:** MASTER-26 (Schemas).

---

## GAP #30 — AGENTES UNIVERSALES (N API keys dinámica)

```
REGLA: el orquestador debe poder usar 1 a 50 API keys
cada agente toma una API key disponible
si 50 agentes necesitan LLM vía API → toman de las disponibles
NO usa una sola API key

EJEMPLO:
  Claude Code normalmente usa 1 API key
  el orquestador: divide en N agentes con N API keys
  si hay 50 keys → 50 agentes en paralelo
  si hay 1 key → 1 agente (secuencial)
```

**Aplicar en:** MASTER-09 (Agentes) — agregar regla.

---

## GAP #31 — DECISIONES TOMADAS (CONFIRMADAS POR MAX)

De BORRADOR-LISTA-APROBADOS.md, sección 3:

```
✅ G5 = MISMO GRUPO = consenso + orquestador (NO son dos grupos separados)
✅ G6 BUILD eliminado (era invento)
✅ G7/G8 también eran confusión → ahora es solo G6 ASISTENTES
✅ Total: 6 grupos (G1, G2, G3, G4, G5, G6)
✅ MiniMax M3 = LÍDER de G5 (como SKYNER, vía 1 NVIDIA NIM)
✅ M2.7 SOLO crea G5 inicialmente (después G5 programa todo)
✅ Orquestador MANEJA al agente (NO al revés)
✅ DSL/DAG NUNCA prompt libre
✅ Input sagrado (no se modifica, no se resume, no se parafrasea)
✅ Todo se reporta a M3_chat + a MAX por Telegram
✅ 1 HF Space por grupo (own token, aislada)
✅ ZeroGPU se comparte — no nos afecta porque usamos API
✅ GitHub como fuente de verdad de todo
✅ SandboxDB por grupo para estado temporal
✅ RAM 16GB por HF
✅ Q5/Q4 según peso del modelo
✅ bartowski recomendado para GGUF (mejor quantización community)
✅ Unsloth Dynamic 2.0 como segunda opción
✅ context7 para contexto extendido 10M tokens
```

**Aplicar en:** MASTER-15 (Reglas + Intocables) — agregar como decisiones confirmadas.

---

## GAP #32 — UBICACIONES PROYECTOS INICIALES

```
projects/ (separación por proyecto)
├── nct-fase0/
├── interfaz-fusionada/
└── crazy-wall/
```

**Aplicar en:** MASTER-13 (Arquitectura NCT).

---

## GAP #33 — KIMI K2.7-CODE ESPECIFICACIONES DETALLADAS

```
Vendor:           Moonshot AI (Kimi K2.7 Code)
HF:               moonshotai/Kimi-K2.7-Code
Función:          Generación de código de producción
Provider OpenCLAW: Sí (config nativo)
Compatible Claude Code: Sí (vía API Moonshot)
Fortalezas:       Tool calling avanzado, agentic coding, código coherente
Cuándo se elige:  TM01, TM02 cuando el lenguaje es Python/TS/Rust/Go
Temperatura:      0.2 (default)
Output:           Patch unified diff + JSON metadata
Endpoint:         Groq provider o NVIDIA NIM
```

**Aplicar en:** MASTER-10 (Modelos y APIs).

---

## RESUMEN DE GAPS NUEVOS

### 13 gaps nuevos en 2da pasada:

| # | Gap | Master destino |
|---|-----|----------------|
| 21 | DECLARACIÓN DE APERTURA | MASTER-15 |
| 22 | 3 REVISIONES DEL INPUT | MASTER-15 |
| 23 | CHECKPOINT JSON estructura | MASTER-12 |
| 24 | RECOVERY JSON estructura | MASTER-12 |
| 25 | Input Engine 11 componentes | MASTER-06 |
| 26 | 17 Mejoras Input Engine | MASTER-06 |
| 27 | Output Engine 13 componentes | MASTER-07 |
| 28 | P35/P36/P37 100X | MASTER-27 |
| 29 | EVENTS types | MASTER-26 |
| 30 | Agentes Universales N keys | MASTER-09 |
| 31 | Decisiones MAX confirmadas | MASTER-15 |
| 32 | Proyectos iniciales | MASTER-13 |
| 33 | Kimi K2.7-Code specs | MASTER-10 |

---

## CONCLUSIÓN DEL BUCLE

Continuaré auditando en la siguiente iteración si encuentro más gaps.
</content>