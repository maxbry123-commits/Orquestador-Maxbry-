# DOCUMENTO 9: REGLAS, COSTOS Y CAPACIDADES
## Extraído del historial del chat

---

## 1. OBJETIVO: INFRAESTRUCTURA $0

### Cómo se logra:
```
HuggingFace Free Tier:
- 7 Spaces con 16GB RAM c/u
- CPU básico gratis
- Storage limitado

API Free Tiers:
- 4 NVIDIA NIM keys (free tier)
- 6 Cerebras keys (free tier)
- 6 Groq keys (free tier)

GGUF Local:
- 9 modelos cuantizados
- 0.6GB - 3GB cada uno
- Sin costo de inferencia

Total: $0/mes
```

### Límites a respetar:
- HF Spaces pueden dormirse por inactividad
- Rate limits de APIs
- Memoria limitada por Space (16GB c/u)
- Cold starts posibles
- HH ≠ A100 (solo CPU/T4)

---

## 2. CAPACIDADES DEL SISTEMA

### Objetivo:
```
- 2000+ agentes simultáneos (CAPACIDAD, no reales)
- 1000+ tareas simultáneas
- 7 HF Spaces con 16GB c/u = 112GB RAM
- ~13.5GB usados por modelos
- 87% margen libre
```

### Cálculo de líneas y memoria:
```
~53,400 líneas totales de código
336 archivos Python
~14 MB código fuente
~500 MB RAM runtime sin modelos
~13.5 GB RAM con modelos G6
7 HF Spaces × 16GB = 112 GB disponibles (87% margen libre)
```

### Escalabilidad:
- Horizontal: agregar HF Spaces
- Vertical: upgrade a Spaces larger
- Sin redesign del código

---

## 3. MÁXIMA CAPACIDAD (NO IMPLEMENTAR TODAVÍA)

Diseño CAPACIDAD, no implementación:
- 10 → 2000 agentes sin redesign
- 1000 tareas simultáneas
- Stateless design
- Comunicación bus de eventos

---

## 4. RESTRICCIONES DE MAX (CONFIRMADAS)

### Hardware:
- MAX solo tiene smartphones + iPad Pro
- Sin PC para servidores
- Sin GPU dedicada
- Todo debe correr en HF

### Reglas operacionales:
- "NUNCA crear ni cambiar nada sin mi APROBADO"
- "SOLO AGREGO capas, NUNCA reemplazo"
- "MANTENER todos los nombres originales"
- "Estructura <200 líneas por archivo — M2.7 puede editar sin romper"

---

## 5. 30 MICRO-AGENTES DEL ORQUESTADOR (DETALLE)

30 micro-agentes especializados que componen el orquestador MAXBRY SUPER TEAM.

### Categorías:
```
1-5:   Análisis (input parsing, intent, context, etc.)
6-10:  Planificación (task breakdown, scheduling, etc.)
11-15: Ejecución (delegación, monitoring, retries, etc.)
16-20: Validación (CSA jueces subset, quality, etc.)
21-25: Aprendizaje (memory, patterns, optimization, etc.)
26-30: Meta (orquestación de orquestadores, recovery, etc.)
```

### Características:
- Cada uno con rol específico
- Trabajan en paralelo sobre bus de eventos
- Capacidad de invocarse entre sí
- Auto-descubrimiento de capacidades

---

## 6. REGLAS DEL SISTEMA (CONFIRMADAS EN CHAT)

### Reglas de operación:
- 5 GOALS + 12 PASOS obligatorios en cada salida
- Cada salida empieza con "APLICANDO SYSTEM PROMPT"
- Cada salida termina con "AUDIT FINAL (PASO 12)"
- 3 separate inventories: Tools ≠ Agents ≠ AI Models
- Orquestador INDEPENDIENTE — no mezclar con GGUF/AI keys/proyectos
- NO inventar datos — preguntar si falta info
- NO alucinar
- MVP first, anti-overengineering
- No inventar nuevas categorías
- Cada salida validar antes de patchear
- Mostrar PENDIENTE si algo no está aprobado
- STATE JSON actualizado siempre

### Reglas de aprobación:
- NUNCA crear/cambiar nada sin "APROBADO" explícito
- SOLO AGREGO capas, NUNCA reemplazo
- MANTENER todos los nombres, roles, cantidades originales

### Reglas técnicas:
- Input is sacred — Input Block nunca modifica/resume/parafrese/reinterpreta
- DSL/DAG nunca prompt libre — solo estructurado
- G5 gestiona agentes (no al revés)
- Orquestador confirma proyecto antes de ejecutar (Fase 0.5)
- APIs intercambiables (3 profiles: conservador/equilibrado/agresivo)
- Structure <200 líneas por archivo
- Cada HF Space per group = aislado, con own token
- Cada proyecto = separate root en GitHub
- Cada Docker container por proyecto

---

## 7. PROMPT DSL CERRADO (DETERMINISMO)

### Por qué:
- Misma calidad de razonamiento en cada consenso
- Mismo formato de respuesta (parseable)
- Auditoría fácil (qué prompt usó cada agente)

### Estructura:
```
[SISTEMA]
Eres el {AGENT_ROLE} en el sistema de consenso de NEURONA CODE TURBO.
Tu misión: {MISSION_TEXT}
Tu personalidad: {PERSONALITY_TEXT}
Tus restricciones: {RESTRICTIONS}
Responde SOLO en el formato JSON especificado. No agregues prosa.

[CONTEXTO]
Proyecto: {PROJECT_NAME}
Stack: {STACK}
Presupuesto: {BUDGET}
Tiempo: {TIME}
Restricciones adicionales: {EXTRA}

[PROBLEMA]
{USER_PROBLEM}

[INPUT_PREVIO]
{PREVIOUS_AGENT_OUTPUT}

[FORMATO_DE_SALIDA]
{OUTPUT_SCHEMA_JSON}

[IMPORTANTE]
- No inventes features que no estén en el stack.
- Sé conciso.
- Si dudas, di "no tengo suficiente información".
```

---

## 8. DETERMINISMO EN EL ORQUESTADOR (90/10)

### 90% código determinista:
- Parseo
- Validación
- Transformación
- Routing
- Verificación mecánica
- Formatting
- Retry
- Fallback
- Circuit breaker
- EROS compression
- Checkpoint/restore
- Schema validation

### 10% LLM (solo donde aporta señal):
- MA-RAG-SYNTH (síntesis)
- MA-ARCH-PLAN (parte creativa)
- Max Mode (decisiones críticas)
- llm_adversarial_review (cuando 3 capas mecánicas fallan)

### Contador de presupuesto:
```python
class Budget:
    code_tokens: int = 0
    llm_tokens:  int = 0

    @property
    def llm_pct(self) -> float:
        total = self.code_tokens + self.llm_tokens
        return self.llm_tokens / max(total, 1)

    def enforce(self, target_pct=0.10):
        assert self.llm_pct <= target_pct, "LLM budget exceeded"
```

---

## 9. CICLOS DE INVESTIGACIÓN

### Diseño del ciclo:
```
   ┌─────────────────────────────────────────────────────────┐
   │              CICLO DE INVESTIGACIÓN                     │
   │                                                         │
   │   ┌────────────┐    ┌────────────┐    ┌────────────┐    │
   │   │ R1: query  │───►│ R2: fetch  │───►│ R3: filter │    │
   │   └────────────┘    └────────────┘    └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │   ┌────────────┐                      ┌────────────┐    │
   │   │ R5: refine │◄──────────replan────│ R4: eval   │    │
   │   └────────────┘                      └────────────┘    │
   │           │                                   │         │
   │           ▼                                   ▼         │
   │       new_query                          stop if        │
   │                                           score ≥ 0.85  │
   └─────────────────────────────────────────────────────────┘
```

### Política:
- Mínimo 2 rondas de investigación por tarea
- Máximo 5 rondas (anti-bucle)
- Cada ronda consume ≤ 50K tokens
- Salida consolidada vía MA-RAG-SYNTH

---

## 10. SEMILLA DE INFORMACIÓN (PRE-ANÁLISIS)

### Pipeline de pre-análisis (5 pasos):
```
seed ─► [S1] indexar ─► [S2] resumir ─► [S3] detectar_gaps
                       │
                       ▼
              [S4] proponer_preguntas ─► [S5] enriquecer_seed
```

| # | Paso | Bloque | Salida |
|---|---|---|---|
| S1 | Indexar repo + state + RAG | MA-INDEX | seed_index.sqlite |
| S2 | Resumir cada artefacto | MA-SUMMARIZE | seed_summary.json |
| S3 | Detectar huecos de información | MA-GAP-DETECT | seed_gaps.json |
| S4 | Proponer preguntas de investigación | MA-QUESTION-GEN | seed_questions.json |
| S5 | Enriquecer seed con respuestas iniciales | MA-RESEARCH-WEB + MA-RESEARCH-GH | seed_enriched.json |

### Métrica de suficiencia:
```python
evidence_sufficiency_score = (
    0.35 * coverage_requirements +
    0.25 * consistency_score    +
    0.20 * source_diversity     +
    0.20 * recency_score
)
```

Si `evidence_sufficiency_score >= 0.85` → el sistema puede proceder sin más investigación. Si `< 0.85` → entra en ciclo de investigación.

---

## 11. PATRONES DE ENCADENAMIENTO

### 3 patrones canónicos:

```
(a) Secuencial          (b) DAG paralelo          (c) Fractal anidado

A ─► B ─► C ─► D         A ─► B ─┐                    ┌─► A ─► B ─┐
                                       ─► D           │            ├─► D
                          A ─► C ─┘                    └─► C ──────┘
```

| Patrón | Configuración | Caso típico |
|---|---|---|
| Secuencial | `chain: linear` | ETL, refactor |
| DAG paralelo | `chain: dag` con `parallel_groups` | investigación + diseño |
| Fractal anidado | `chain: fractal` con `depth ≤ 5` | arquitectura multi-módulo |

---

## 12. ESTADO DEL PROYECTO

### Done:
- ✅ 100 patches con documentación individual
- ✅ 19 archivos Python reales (726 líneas)
- ✅ Constitución 1276 líneas
- ✅ Memoria persistente: 2 topics
- ✅ 8 documentos consolidados (72 KB)

### In Progress:
- ⏳ 9 documentos consolidados más (este en curso)
- ⏳ Verificación cruzada final

### Blocked:
- ⏳ MAX confirma arquitectura final
- ⏳ M2.7 no ha instalado nada (espera GO de MAX)
- ⏳ Datos pre-flight pendientes:
  - GitHub username + PAT
  - HF username + 6 tokens
  - 16 API keys con labels
  - Turso DB credentials
  - Visibility preference (public/private)
  - Telegram bot token
  - HTM model name (no encontrado en HF)
  - YUAN model name (no encontrado en HF)

---

## 13. CÓDIGO REAL CREADO

19 archivos Python en `/workspace/maxbry/g7/output_engine/v2/`:

### Estructura:
```
g7/output_engine/v2/
├── __init__.py                                (47 líneas)
├── pre_mortem/pre_mortem_analyzer.py           (70 líneas)
├── auto_rollback/rollback_monitor.py            (62 líneas)
├── meta_learning/cross_release_analyzer.py     (56 líneas)
├── personalization/style_learner.py            (64 líneas)
├── multi_stakeholder/stakeholder_detector.py   (79 líneas)
├── causal_tracing/causal_chain_builder.py      (75 líneas)
├── marketplace/output_cataloger.py             (84 líneas)
├── self_improving/quality_analyzer.py          (99 líneas)
└── production_monitoring/usage_tracker.py      (88 líneas)
+ 10 __init__.py
Total: 726 líneas de código
```

### Sin output_sandbox (RECHAZADO por MAX):
No se creó carpeta `output_sandbox/` porque MAX rechazó esa propuesta.

---

## 14. DOCUMENTACIÓN PRINCIPAL EN /workspace/nct-proyecto/

### Documentos de diseño:
- 01-FASE-0-FROZEN.md (651 líneas)
- 02-SYSTEM-PROMPT-MYTHOS.md (672 líneas)
- ANALISIS-LOOPS-v100.md (192 líneas)
- BIS-v1-MAXBRY.md (143 líneas)
- BORRADOR-LISTA-APROBADOS.md (1456 líneas)
- CONSENSO-MEJORADO-10X.md (4465 líneas)
- CONSTITUCION-ORQUESTADOR.md (1276 líneas)
- MI-SYSTEM-PROMPT-OPERATIVO.md (136 líneas)
- ORQUESTADOR-G5-DISENO.md (2928 líneas)
- PARCHE-v14 a PARCHE-v17 (4 parches)
- PARCHES-MAXBRY-SUPER-TEAM.md (847 líneas)
- SISTEMA-RAZONAMIENTO-EXTERNO.md (3126 líneas)
- STATE-AUDIT.md (455 líneas)
- VALIDACION-POR-SALIDA.md (2667 bytes)
- RESUMEN-OUTPUT-V61.md

### Documentos consolidados (en /workspace/nct-proyecto/CONSOLIDADO-FINAL/):
- 01 a 09 documentos sobre orquestador y agentes
</content>