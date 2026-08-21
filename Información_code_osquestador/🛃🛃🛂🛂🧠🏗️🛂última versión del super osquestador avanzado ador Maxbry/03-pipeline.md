# DOCUMENTO 3: PIPELINE Y FASES DEL ORQUESTADOR
## Extraído del historial del chat

---

## 1. 10 FASES DEL PIPELINE

10 fases del pipeline principal del orquestador.

### Las 10 fases:
```
F1  · Recepción        → input llega
F2  · Pre-procesamiento → SID, validaciones iniciales
F3  · Definición       → Definition Engine, clarificar
F4  · Planificación    → DAG, recursos, asignación
F5  · Confirmación     → Fase 0.5, MAX aprueba si es nuevo
F6  · Ejecución        → agentes activos
F7  · Validación       → CSA, quality, score
F8  · Publicación      → output engine, multi-target
F9  · Monitoreo        → producción, telemetría
F10 · Aprendizaje      → actualizar memoria, reglas
```

---

## 2. FASE 0.5 · CONFIRMATION GATE (CRÍTICA E INTOCABLE)

Fase CRÍTICA entre planificación y ejecución. El orquestador DEBE confirmar con MAX antes de ejecutar proyectos nuevos.

### Por qué existe:
```
Evitar que el orquestador:
  - Ejecute proyectos no autorizados
  - Gaste recursos sin permiso
  - Asuma cosas que MAX no quiso
```

### Cómo funciona:
```
F4 · Planificación completa
       ↓
F5 · FASE 0.5 · Confirmación
       ↓
    ¿Es proyecto conocido?
       ↓
   SÍ → procede automático
       ↓
   NO → PAUSA y consulta a MAX
       ↓
    MAX aprueba o modifica
       ↓
F6 · Ejecución inicia
```

### REGLA ABSOLUTA:
```
Proyecto nuevo = SIEMPRE confirmación
Proyecto recurrente = procede automático
```

---

## 3. 3 MONITORES DEL PIPELINE

3 monitores que supervisan el pipeline en tiempo real.

### Los 3 monitores:

**M1 · MONITOR DE PERFORMANCE**
- Latencia, throughput, cuellos de botella

**M2 · MONITOR DE CALIDAD**
- Scores, errores, complaints

**M3 · MONITOR DE RECURSOS**
- Tokens, memoria, rate limits, costos

### Características:
- Operación continua 24/7
- Alertas automáticas
- Dashboards para MAX
- Histórico para análisis

---

## 4. MODELOS DE EJECUCIÓN SEGÚN COMPLEJIDAD

### 4 Escenarios (9 / 16 / 25 / 30-50 PASOS):

**ESCENARIO 1 — TAREA SIMPLE (9 pasos mínimos):**
Para tareas claras, sin ambigüedad, dependencias mínimas y riesgo bajo.

1. INPUT
2. INTENT_PARSING
3. CONTEXT_BUILDING
4. PLAN_GENERATION
5. EXECUTE
6. SELF_CHECK
7. OUTPUT_GENERATION
8. POST_OUTPUT_AUDIT
9. FEEDBACK_LOOP_STORAGE

**ESCENARIO 2 — TAREA MEDIA (16 pasos):**
Para tareas con algunas dependencias, cierto nivel de ambigüedad y riesgo moderado.

1. INPUT
2. INTENT_PARSING
3. PROBLEM_FRAMING
4. CONTEXT_BUILDING
5. CONSTRAINT_EXTRACTION
6. GOAL_DECOMPOSITION
7. COMPLEXITY_ESTIMATION
8. PLAN_GENERATION
9. SUBTASK_BREAKDOWN
10. HYPOTHESIS_GENERATION
11. VALIDATION_LAYER
12. DECISION_ENGINE
13. CONFIDENCE_SCORING
14. OUTPUT_GENERATION
15. POST_OUTPUT_AUDIT
16. FEEDBACK_LOOP_STORAGE

**ESCENARIO 3 — TAREA ÓPTIMA (25 pasos):**
Para tareas complejas con múltiples dependencias, ambigüedad significativa y riesgo alto.

1. INPUT
2. INTENT_PARSING
3. PROBLEM_FRAMING
4. DOMAIN_DETECTION
5. CONTEXT_BUILDING
6. CONSTRAINT_EXTRACTION
7. GOAL_DECOMPOSITION
8. COMPLEXITY_ESTIMATION
9. RISK_SCORING
10. STRATEGY_SELECTION
11. ARCHITECTURE_DESIGN
12. PLAN_GENERATION
13. SUBTASK_BREAKDOWN
14. DEPENDENCY_GRAPH_BUILD
15. HYPOTHESIS_GENERATION
16. SIMULATION_ENGINE
17. CONTRADICTION_DETECTION
18. VALIDATION_LAYER
19. REPLANNER_LOOP (si score menor a 70)
20. DECISION_ENGINE
21. CONFIDENCE_SCORING
22. FUSION_ENSEMBLE
23. FINAL_SYNTHESIS
24. OUTPUT_GENERATION
25. FEEDBACK_LOOP_STORAGE

**ESCENARIO 4 — TAREA AVANZADA (30 a 50 pasos):**
Para proyectos completos, sistemas de múltiples módulos, alta ambigüedad y riesgo crítico.

Incluye los 25 pasos del Escenario 3 más:
26. ALTERNATIVE_PATH_GENERATION
27. SEARCH_EXPANSION
28. REASONING_SWARM_PARALLEL
29. CRITIC_SWARM_MULTI_PERSPECTIVE
30. SELF_REFLECTION_LOOP
31. FAILURE_MODE_ANALYSIS
32. EDGE_CASE_GENERATION
33. KNOWLEDGE_RETRIEVAL_EXTERNAL
34. INSIGHT_EXTRACTION
35. MEMORY_WRITE_SHORT_TERM
36. MEMORY_WRITE_LONG_TERM
37. OPTIMIZATION_PASS
38. SOLUTION_RANKING
39. SAFETY_CONSISTENCY_CHECK
(hasta 50 según complejidad detectada)

---

## 5. COMPLEXITY ESTIMATOR

El COMPLEXITY_ESTIMATOR evalúa:
- Dependencias
- Ambigüedad
- Pasos estimados
- Riesgo de error

### Fórmula del score:
```
score = (dependencias × 2) + pasos_estimados
        + (5 si ambiguo) + (5 si alto riesgo)
```

### Niveles y acción:

**LOW (score 0-3):**
- 0 ciclos Reasoner/Verifier
- Ejecución directa sin loops
- Ahorra tokens para tareas simples

**MEDIUM (score 4-8):**
- 1 ciclo Reasoner → Verifier
- Verificación básica

**HIGH (score 9-15):**
- 2 ciclos Reasoner → Verifier
- Motor de razonamiento completo

**EXTREME (score 16+):**
- 3 ciclos o más
- Motor completo + simulaciones múltiples

---

## 6. 5 FASES PRINCIPALES (FABLES)

### FASE 0 — ORQUESTACIÓN:
- INPUT
- DESCOMPOSICIÓN EN 25 A 100 TAREAS
- ASIGNACIÓN A FASES (1 a 5)
- CREACIÓN DE LISTA_GLOBAL INICIAL

### FASE 1 — COMPRENSIÓN (Tareas 1 a 5):
INPUT + LISTA_GLOBAL
Procesos:
- Entender el objetivo real
- Reformular el problema en términos solucionables
- Construir el contexto completo
- Identificar restricciones explícitas e implícitas
- Detectar recursos disponibles y cuellos de botella

### FASE 2 — PLANIFICACIÓN (Tareas 6 a 10):
INPUT + LISTA_GLOBAL (v1)
Procesos:
- Elegir estrategia de resolución
- Diseñar arquitectura de la solución
- Descomponer en sub-tareas atómicas
- Construir grafo de dependencias
- Generar roadmap con criterios de éxito

### FASE 3 — EXPLORACIÓN + INVESTIGACIÓN (Tareas 11 a 16):
INPUT + LISTA_GLOBAL (v2)
Procesos:
- Generar múltiples hipótesis de solución
- Explorar caminos alternativos
- Simular escenarios y edge cases
- Detectar modos de fallo
- Investigación externa

### FASE 4 — VALIDACIÓN (Tareas 17 a 21):
INPUT + LISTA_GLOBAL (v3)
Procesos:
- Detectar errores y contradicciones internas
- Generar edge cases que rompan la solución
- Validación global contra todos los criterios
- Aplicar correcciones necesarias
- Score de confianza (si score menor a 70: regresar a Fase 2)

### FASE 5 — SÍNTESIS CRUDA (Tareas 22 a 25):
INPUT + LISTA_GLOBAL (v4)
Procesos:
- Consolidar todas las salidas anteriores
- Integrar hallazgos de todas las fases
- Generar solución completa cruda
- Preparar para el CHEF FINAL

---

## 7. CHEF FINAL (4 PASOS)

### PASO 1 — LISTA TOTAL (3 PASADAS):
- SALIDA CRUDA → 3 PASADAS → LISTA COMPLETA DE TODO
- Función: reconstruir TODO el contenido generado, no resumir, no perder información

### PASO 2 — ARRASTRE + ACTUALIZACIÓN (3 PASADAS):
- INPUT: LISTA P1 → 3 PASADAS → ARRASTRAR P1 + ACTUALIZAR + COMPLETAR + CORREGIR
- Función: mantener memoria acumulada, no reiniciar contexto, mejorar consistencia

### PASO 3 — DISEÑO DE ENTREGA (3 PASADAS):
- INPUT: P1 + P2 → 3 PASADAS → DISEÑO DE FORMATO FINAL
- Función: estructurar presentación, definir cómo se entrega

### PASO 4 — SÍNTESIS FINAL (ANÁLISIS TOTAL):
- INPUT: P1 + P2 + P3 → ANÁLISIS GLOBAL COMPLETO → VERSIÓN FINAL OPTIMIZADA
- Función: revisar todo el sistema completo, cerrar inconsistencias, producir OUTPUT FINAL

---

## 8. LISTA_GLOBAL — 4 REGLAS

La LISTA_GLOBAL es la memoria estructural del sistema.

- **REGLA 1**: Se crea en la Fase 0 (orquestación)
- **REGLA 2**: Se actualiza al final de cada fase
- **REGLA 3**: Se arrastra SIEMPRE al siguiente paso
- **REGLA 4**: NUNCA se reinicia hasta completar el ciclo

Contiene: tareas / estados / resultados / pendientes