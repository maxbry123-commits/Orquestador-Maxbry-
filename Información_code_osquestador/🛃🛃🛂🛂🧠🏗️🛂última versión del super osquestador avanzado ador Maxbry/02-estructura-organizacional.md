# MASTER DOCUMENTO 02: ESTRUCTURA ORGANIZACIONAL
## MAXBRY SUPER TEAM · 30 Micro-Agentes · 11 Roles · 10 Colas · 6 Niveles

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. VISIÓN DE LA ORGANIZACIÓN

MAXBRY SUPER TEAM se organiza como una **empresa digital** con:

- **30 micro-agentes** = empleados especializados
- **11 internal roles** = roles de coordinación
- **10 colas paralelas** = líneas de trabajo
- **6 niveles de autonomía** = permisos escalonados
- **12 task models** = plantillas de tarea
- **5 loop versions** = estilos de iteración
- **3 monitores** = vigilancia continua
- **10 agentes consejo** = decisiones críticas

---

## 2. LOS 30 MICRO-AGENTES

### 2.1 Categorías (6 categorías × 5 agentes)

```
[1-5]   ANÁLISIS (Input parsing, intent, context)
[6-10]  PLANIFICACIÓN (Task breakdown, scheduling)
[11-15] EJECUCIÓN (Delegación, monitoring, retries)
[16-20] VALIDACIÓN (CSA jueces subset, quality)
[21-25] APRENDIZAJE (Memory, patterns, optimization)
[26-30] META (Orquestación de orquestadores, recovery)
```

### 2.2 Características comunes

- Cada uno ≤ 200 LOC de núcleo
- Una sola responsabilidad
- Un input_schema
- Un output_schema
- Estado efímero
- Muerte tras emitir el JSON
- Se invocan vía MCP o stdio

### 2.3 Tabla de los 30

| ID | Nombre | Categoría | Responsabilidad |
|----|--------|-----------|-----------------|
| MA-01 | Input Parser | Análisis | Parsea DSL/DAG/JSON/YAML/MD |
| MA-02 | Intent Classifier | Análisis | Clasifica intención |
| MA-03 | Context Builder | Análisis | Construye contexto del task |
| MA-04 | Entity Extractor | Análisis | Extrae entidades |
| MA-05 | Semantic Analyzer | Análisis | Analiza semántica |
| MA-06 | Task Decomposer | Planificación | Descompone tareas |
| MA-07 | Scheduler | Planificación | Agenda ejecuciones |
| MA-08 | Resource Allocator | Planificación | Asigna recursos |
| MA-09 | Priority Manager | Planificación | Gestiona prioridades |
| MA-10 | Plan Validator | Planificación | Valida planes |
| MA-11 | Code Generator | Ejecución | Genera código |
| MA-12 | Code Linter | Ejecución | Lint + format |
| MA-13 | Code Tester | Ejecución | Tests + coverage |
| MA-14 | Worker Pool | Ejecución | K samples paralelo |
| MA-15 | Executor | Ejecución | Ejecuta tareas |
| MA-16 | Verifier 3-Capas | Validación | Adversarial+cross+maker |
| MA-17 | Critic | Validación | Análisis crítico |
| MA-18 | Judge | Validación | Juzga outputs |
| MA-19 | Sentinel | Validación | Vigila anomalías |
| MA-20 | Quality Assurance | Validación | QA final |
| MA-21 | Memory Writer | Aprendizaje | Escribe en memoria |
| MA-22 | Pattern Detector | Aprendizaje | Detecta patrones |
| MA-23 | Optimizer | Aprendizaje | Optimiza rendimiento |
| MA-24 | Skill Curator | Aprendizaje | Auto-curación BIS |
| MA-25 | Metrics Collector | Aprendizaje | Recolecta métricas |
| MA-26 | Meta-Orchestrator | Meta | Orquesta orquestadores |
| MA-27 | Recovery Agent | Meta | Recupera fallos |
| MA-28 | Self-Improver | Meta | Auto-mejora |
| MA-29 | Health Monitor | Meta | Salud del sistema |
| MA-30 | Lifecycle Manager | Meta | Nacimiento/muerte |

---

## 3. LOS 11 INTERNAL ROLES

### 3.1 Listado de roles

| # | Rol | Responsabilidad |
|---|-----|-----------------|
| R1 | **CEO Virtual** | Director del G5 |
| R2 | **COO** | Operaciones |
| R3 | **CTO** | Tecnología y modelos |
| R4 | **CFO** | Recursos y costos |
| R5 | **CHRO** | Agentes y roles |
| R6 | **CSO** | Seguridad |
| R7 | **CMO** | Comunicación con MAX |
| R8 | **Chief Auditor** | CSA coordination |
| R9 | **Chief Architect** | Diseño y patrones |
| R10 | **Chief Skeptic** | Contrarian thinking |
| R11 | **Chief Historian** | Memoria y estado |

### 3.2 Asignación de roles

```
CEO Virtual     → SKYNER (NVIDIA)
COO             → Cerebras
CTO             → Cerebras
CFO             → Groq
CHRO            → GGUF local
CSO             → GGUF API
CMO             → Groq
Chief Auditor   → CSA J1-J10
Chief Architect → GGUF API
Chief Skeptic   → Cerebras
Chief Historian → Groq
```

---

## 4. LAS 10 COLAS PARALELAS

### 4.1 Listado

| Cola | Nombre | Tipo | Capacidad |
|------|--------|------|-----------|
| Q1 | Critical Path | Blocking | 100 |
| Q2 | High Priority | Fast | 500 |
| Q3 | Normal | Standard | 1000 |
| Q4 | Background | Async | 2000 |
| Q5 | Research | Multi-source | 200 |
| Q6 | Code | Compilation | 300 |
| Q7 | Test | Quality | 400 |
| Q8 | Documentation | Text | 150 |
| Q9 | Review | Human-like | 100 |
| Q10 | Recovery | Healer | 50 |

### 4.2 Scheduling

- Round-robin dentro de cada cola
- Priority boost para Q1
- Preemption Q1 > Q2 > resto
- Q4, Q10 pueden tomar prestado tiempo de Q3

---

## 5. LOS 6 NIVELES DE AUTONOMÍA

### 5.1 L1 · Manual
- Cada paso requiere aprobación humana
- MAX aprueba cada acción

### 5.2 L2 · Supervised
- Sistema propone, MAX aprueba
- 1 aprobación cada 5 acciones

### 5.3 L3 · Assisted Autonomous
- Sistema ejecuta, MAX revisa
- 1 revisión cada 10 acciones

### 5.4 L4 · Supervised Autonomous
- Sistema ejecuta y reporta
- MAX solo en puntos críticos

### 5.5 L5 · Continuous Autonomous
- Sistema autónomo hasta 72h
- Solo reporte final

### 5.6 L6 · Full Autonomous
- Sistema totalmente autónomo
- Reporta anomalías graves
- Self-evolution enabled

---

## 6. LOS 12 TASK MODELS (TM)

### 6.1 Listado

| TM | Nombre | Nivel | Pasos |
|----|--------|-------|-------|
| TM01 | Simple Task | L1-L2 | 3-5 |
| TM02 | Code Refactor | L2-L3 | 5-10 |
| TM03 | New Feature | L3-L4 | 10-15 |
| TM04 | Bug Fix | L3-L4 | 5-12 |
| TM05 | API Design | L3-L4 | 8-12 |
| TM06 | Microservice | L4-L5 | 12-20 |
| TM07 | Full App | L4-L5 | 20-30 |
| TM08 | Research Report | L3-L5 | 8-15 |
| TM09 | Migration | L4-L5 | 15-25 |
| TM10 | Multi-System | L5-L6 | 25-40 |
| TM11 | Critical Recovery | L4-L6 | 5-15 |
| TM12 | Self-Improvement | L6 | 20-30 |

### 6.2 Cada TM tiene 14 pasos

```
PASO 1-3: Pre-análisis (input, seed, gaps)
PASO 4-6: Research (web, github, rag)
PASO 7-9: Plan + consensus
PASO 10-12: Execute + monitor
PASO 13: Verify (3 capas)
PASO 14: Deliver
```

---

## 7. LAS 5 LOOP VERSIONS (ALV)

### 7.1 ALV_LOP_SIMPLE
- Secuencial
- 1 agente principal
- 1 iteración

### 7.2 ALV_LOP_PARALLEL
- DAG paralelo
- 2-3 agentes en paralelo
- 1-2 iteraciones

### 7.3 ALV_LOP_FRACTAL
- Fractal anidado
- depth ≤ 5
- 3-5 iteraciones

### 7.4 ALV_LOP_QUANTUM_FRACTAL_NESTED
- Quantum + fractal + nested
- depth adaptativo
- 5-10 iteraciones

### 7.5 ALV_LOP_SELF_IMPROVING
- Self-improving
- Modifica parámetros en cada iteración
- 10+ iteraciones
- Solo L6

---

## 8. LOS 3 MONITORES

### 8.1 PAD Monitor
- **P** - Performance (latencia, throughput)
- **A** - Accuracy (calidad)
- **D** - Drift (deriva semántica)

### 8.2 Anxiety Monitor
- Detecta ansiedad operativa
- Mide: retries, fallos, timeouts
- Trigger si ansiedad > umbral

### 8.3 Drift Monitor
- Detecta deriva semántica
- Compara con baseline
- Trigger si drift > 0.15

---

## 9. EL CONSEJO DE CONSENSO (10 AGENTES)

### 9.1 Los 10 votantes

| # | Voto | Pregunta |
|---|------|----------|
| 1 | Técnico | ¿Es técnicamente correcto? |
| 2 | Negocio | ¿Aporta valor? |
| 3 | Costos | ¿Es costo-efectivo? |
| 4 | Riesgos | ¿Tiene riesgos inaceptables? |
| 5 | Ético | ¿Es ético? |
| 6 | UX | ¿Tiene buena UX? |
| 7 | Performance | ¿Es rápido? |
| 8 | Seguridad | ¿Es seguro? |
| 9 | Compatibilidad | ¿Rompe algo? |
| 10 | Veto MAX | ¿MAX lo aprobaría? |

### 9.2 Mecanismo

```
7+ de acuerdo → Procede
5-6 de acuerdo → Escala a MAX
< 5 de acuerdo → Bloquea
Veto MAX → Siempre bloquea
```

---

## 10. ESTADOS DE TAREA

### 10.1 Los 10 estados

```
CREADA → EN_COLA → ASIGNADA → EJECUTANDO
                                  ↓
                              PAUSADA ↔ EJECUTANDO
                                  ↓
                              VALIDANDO
                                  ↓
        ┌─────────────────────┼────────────────────┐
        ↓                     ↓                    ↓
   COMPLETADA              FALLIDA              CANCELADA
        ↓                     ↓
   (publicada)          (reintentar)
```

### 10.2 Transiciones válidas

- CREADA → EN_COLA ✓
- EN_COLA → ASIGNADA ✓
- ASIGNADA → EJECUTANDO ✓
- EJECUTANDO → PAUSADA → EJECUTANDO ✓
- EJECUTANDO → VALIDANDO ✓
- VALIDANDO → COMPLETADA ✓
- VALIDANDO → FALLIDA ✓
- EJECUTANDO → CANCELADA ✓
- Cualquier → CREADA (reapertura)

---

## 11. INTERACCIÓN CON MAXBRY

### 11.1 Canales de entrada

- Telegram Bot
- API REST
- Dashboard Web
- CLI local
- Voice (opcional)

### 11.2 Canales de salida

- 23 destinos en Multi-Target Delivery
- Adaptive (aprende preferencia de MAX)
- Auto-formato

---

## 12. ARTEFACTOS PRINCIPALES

### 12.1 Archivos producidos

- state.json (estado actual)
- events.log (event sourcing)
- memories/*.md (tier 1-4)
- skills/*.json (skills activas)
- artifacts/ (outputs)
- projects/ (proyectos por workspace)
- checkpoints/ (snapshots firmados)

### 12.2 Estructura de carpetas

```
/workspace/nct-proyecto/
├── CONSOLIDADO-FINAL/ (18 docs)
├── MASTER-FINAL/ (20+ docs)
├── CONSTITUCION-ORQUESTADOR.md
├── PARCHE-v14 a PARCHE-v17
├── PARCHES-ORQUESTADOR/
├── PATCHES-INPUT-V40/
├── PATCHES-LOOP-V60/
├── PATCHES-OUTPUT-V61/
└── PARCHES-INFRA/

/workspace/maxbry/
├── g1-infra/
├── g2-core/
├── g3-ui/
├── g4-audit/
├── g5-orquestador/ ⭐
└── g6-asistentes/
```

---

## 13. CONCLUSIONES

MAXBRY SUPER TEAM cuenta con:
- **30 micro-agentes** especializados
- **11 roles** de coordinación
- **10 colas** paralelas
- **6 niveles** de autonomía
- **12 task models** (TM01-TM12)
- **5 loop versions** (ALV)
- **3 monitores** (PAD, Anxiety, Drift)
- **10 agentes** en consejo consenso
- **10 estados** de tarea

Una organización digital completa con:
- Separación clara de responsabilidades
- Auto-coordinación
- Auto-monitoreo
- Auto-recuperación
- Auto-mejora
</content>