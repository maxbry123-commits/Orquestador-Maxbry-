# DOCUMENTO 11: MYTHOS, FABLES Y ARQUITECTURA DE CAPAS
## Extraído del historial del chat

---

## 1. MYTHOS 40 PASOS (CADENA COMPLETA)

```
PASO 01: INPUT
PASO 02: INTENT PARSING
PASO 03: PROBLEM FRAMING
PASO 04: DOMAIN DETECTION
PASO 05: CONTEXT BUILDING
PASO 06: CONSTRAINT EXTRACTION
PASO 07: GOAL DECOMPOSITION
PASO 08: COMPLEXITY ESTIMATION
PASO 09: RISK SCORING
PASO 10: STRATEGY SELECTION
PASO 11: ARCHITECTURE DESIGN
PASO 12: PLAN GENERATION
PASO 13: SUBTASK BREAKDOWN
PASO 14: DEPENDENCY GRAPH BUILD
PASO 15: HYPOTHESIS GENERATION (MÚLTIPLE)
PASO 16: ALTERNATIVE PATH GENERATION
PASO 17: SEARCH EXPANSION
PASO 18: REASONING SWARM (PARALELO)
PASO 19: CONTRADICTION DETECTION
PASO 20: CRITIC SWARM (MULTI-PERSPECTIVA)
PASO 21: SELF REFLECTION LOOP
PASO 22: FAILURE MODE ANALYSIS
PASO 23: SIMULATION ENGINE (ESCENARIOS x N)
PASO 24: EDGE CASE GENERATION
PASO 25: VALIDATION LAYER
PASO 26: KNOWLEDGE RETRIEVAL / EXTERNAL CONTEXT
PASO 27: INSIGHT EXTRACTION
PASO 28: MEMORY WRITE (SHORT TERM)
PASO 29: MEMORY WRITE (LONG TERM)
PASO 30: REPLANNER LOOP
PASO 31: OPTIMIZATION PASS
PASO 32: DECISION ENGINE
PASO 33: CONFIDENCE SCORING
PASO 34: SOLUTION RANKING
PASO 35: FUSION / ENSEMBLE SOLUTION
PASO 36: SAFETY / CONSISTENCY CHECK
PASO 37: FINAL SYNTHESIS
PASO 38: OUTPUT GENERATION
PASO 39: POST OUTPUT AUDIT
PASO 40: FEEDBACK LOOP STORAGE
```

---

## 2. MYTHOS DESCRIPCIÓN CORTA (12 PASOS)

```
INPUT
  ↓
INTENT PARSING — interpreta intención real
  ↓
FRAMING — define problema real
  ↓
DECOMPOSE — divide en partes
  ↓
HYPOTHESES — genera soluciones múltiples
  ↓
SWARM — razona en paralelo
  ↓
CRITIC — detecta errores y contradicciones
  ↓
SIMULATION — prueba escenarios
  ↓
MEMORY — guarda aprendizajes
  ↓
REPLANNER — ajusta estrategia
  ↓
DECISION — elige mejor solución
  ↓
SYNTHESIS — construye respuesta final
  ↓
AUDIT — revisa calidad final
```

---

## 3. CAPAS EXTERNAS DE MYTHOS

### Arquitectura de Control Alto:

```
MYTHOS
  ↓
FSM
  ↓
ROUTER
  ↓
SHERIFF
  ↓
SENTINEL
  ↓
VERIFIER
  ↓
CRITIC
  ↓
JUDGE
  ↓
POLICY ENGINE
  ↓
PYDANTICAI
  ↓
RETRY ENGINE
  ↓
LLM
```

### Nombre de la Capa Externa:

Una capa externa de código encima de una LLM suele llamarse:
- Orchestrator
- Agent Framework
- Cognitive Layer
- Reasoning Engine

Si coordina varios agentes: Multi-Agent System.
Si cambia la forma de razonar: Reasoning Engine.

Para este diseño: **Mythos Cognitive Layer** o **Mythos Reasoning Engine** encaja bastante bien porque define cómo trabaja el modelo y no el modelo en sí.

---

## 4. STACK TÉCNICO (4 LENGUAJES)

```
JSON     → Define reglas
Python   → Ejecuta lógica
DSL      → Define workflows
YAML     → Configuración
```

Cadena técnica del sistema:
```
MYTHOS → PYTHON → FSM → ROUTER → LLM
```

---

## 5. PYDANTICAI

```
LLM
  ↓
JSON válido
  ↓
Schema válido
  ↓
Python válido
```

PydanticAI convierte la salida del LLM en estructuras de datos Python validadas y tipadas. Garantiza que el output del LLM sea procesable por código determinista.

---

## 6. FSM FINITE STATE MACHINE

```
PLAN
  ↓
CODE
  ↓
TEST
  ↓
CRITIC
  ↓
REPLAN
  ↓
FIN
```

El FSM define en qué estado está el sistema en cada momento y qué transiciones son válidas. No permite saltar estados arbitrariamente.

---

## 7. SEPARACIÓN DE CAPAS (5 NIVELES)

```
PENSAMIENTO
  ↓
CONTROL
  ↓
EJECUCIÓN
  ↓
PERSISTENCIA
  ↓
AUTOCORRECCIÓN
```

Cada capa tiene una responsabilidad única. No se mezclan entre sí.

- **PENSAMIENTO**: cómo se analiza y resuelve (MYTHOS)
- **CONTROL**: qué ejecutar, cuándo validar (FSM/Router)
- **EJECUCIÓN**: cómo se ejecuta el código (Coder/Sandbox)
- **PERSISTENCIA**: cómo se guarda el estado (DB/JSON)
- **AUTOCORRECCIÓN**: cómo se repara un fallo (Repairer)

---

## 8. FICHA DE COMPONENTE

Cada componente del sistema tiene una ficha con estos campos:

```
OBJETIVO:
Qué hace este componente.

UBICACIÓN:
En qué capa del sistema vive.
Ejemplo: 2.3_ROUTER vive en 2.0_CONTROL

JUSTIFICACIÓN:
Por qué existe este componente.
Qué problema resuelve.

DEPENDENCIAS:
De qué otros componentes depende.

ENTRADAS:
Qué recibe este componente.

SALIDAS:
Qué produce este componente.

IMPLEMENTACIÓN:
Qué tecnología usa (DSL / JSON / Python / etc).

EDITABLE:
SI o NO — si se puede cambiar sin romper el sistema.

CRÍTICO:
SI o NO — si falla, el sistema se detiene.
```

---

## 9. EJEMPLO DE FICHA: 2.3_ROUTER

```
OBJETIVO:
Seleccionar flujo y recursos adecuados.

UBICACIÓN:
📂 2.0_CONTROL

JUSTIFICACIÓN:
Evita lógica dispersa y centraliza decisiones.

DEPENDENCIAS:
FSM
Policy Engine

ENTRADAS:
Task
Contexto

SALIDAS:
Ruta seleccionada

IMPLEMENTACIÓN:
DSL + JSON + Python

EDITABLE:
SI

CRÍTICO:
SI
```

---

## 10. DISTINCIÓN RAZONAMIENTO VS CONTROL

Los pasos de pensamiento y las capas de control NO son lo mismo.

**PENSAMIENTO (MYTHOS/FABLES):**
- Define cómo se analiza y resuelve un problema
- Genera estrategias y soluciones
- Pertenece al RAZONAMIENTO

**CONTROL (FSM / Router / PydanticAI):**
- Decide qué ejecutar, cuándo validar y cuándo reintentar
- Garantiza que el proceso se ejecute correctamente
- Pertenece al CONTROL

Un sistema avanzado suele tener AMBOS.

---

## 11. 5 FASES FABLES (VERSIÓN CORTA)

### FASE 0 — ORQUESTACIÓN:
```
INPUT
  ↓
DESCOMPOSICIÓN EN 25 A 100 TAREAS
  ↓
ASIGNACIÓN A FASES (1 a 5)
  ↓
CREACIÓN DE LISTA_GLOBAL INICIAL
```

Salida:
- Mapa completo de tareas
- Estructura de fases asignadas
- LISTA_GLOBAL v0 inicializada

Reglas:
- Mínimo 25 tareas, máximo 100
- Cada tarea va a exactamente una fase
- LISTA_GLOBAL se crea aquí y nunca se reinicia

### FASE 1 — COMPRENSIÓN (Tareas 1 a 5):
- Entender el objetivo real
- Reformular el problema
- Construir el contexto completo
- Identificar restricciones
- Detectar recursos disponibles

### FASE 2 — PLANIFICACIÓN (Tareas 6 a 10):
- Elegir estrategia de resolución
- Diseñar arquitectura de la solución
- Descomponer en sub-tareas atómicas
- Construir grafo de dependencias
- Generar roadmap con criterios de éxito

### FASE 3 — EXPLORACIÓN + INVESTIGACIÓN (Tareas 11 a 16):
- Generar múltiples hipótesis de solución
- Explorar caminos alternativos
- Simular escenarios y edge cases
- Detectar modos de fallo
- Investigación externa

### FASE 4 — VALIDACIÓN (Tareas 17 a 21):
- Detectar errores y contradicciones
- Generar edge cases que rompan la solución
- Validación global contra todos los criterios
- Aplicar correcciones necesarias
- Score de confianza (si score < 70: regresar a Fase 2)

### FASE 5 — SÍNTESIS CRUDA (Tareas 22 a 25):
- Consolidar todas las salidas anteriores
- Integrar hallazgos de todas las fases
- Generar solución completa cruda
- Preparar para el CHEF FINAL

---

## 12. CHEF FINAL 4 PASOS

### 🔵 PASO 1 — LISTA TOTAL (3 PASADAS):
SALIDA CRUDA → 3 PASADAS → LISTA COMPLETA DE TODO
Función: reconstruir TODO el contenido generado, no resumir, no perder información.

### 🟡 PASO 2 — ARRASTRE + ACTUALIZACIÓN (3 PASADAS):
INPUT: LISTA P1 → 3 PASADAS → ARRASTRAR P1 + ACTUALIZAR + COMPLETAR + CORREGIR
Función: mantener memoria acumulada, no reiniciar contexto, mejorar consistencia.

### 🟠 PASO 3 — DISEÑO DE ENTREGA (3 PASADAS):
INPUT: P1 + P2 → 3 PASADAS → DISEÑO DE FORMATO FINAL
Función: estructurar presentación, definir cómo se entrega.

### 🔴 PASO 4 — SÍNTESIS FINAL (ANÁLISIS TOTAL):
INPUT: P1 + P2 + P3 → ANÁLISIS GLOBAL COMPLETO → VERSIÓN FINAL OPTIMIZADA
Función: revisar todo el sistema completo, cerrar inconsistencias, producir OUTPUT FINAL.

---

## 13. OPENMYTHOS

OpenMythos es un sistema de razonamiento recurrente de código abierto. Implementa un Recurrent-Depth Transformer con tres etapas:

### PRELUDE:
- Bloques transformer estándar
- Pre-procesa el input antes del loop recurrente
- Equivalente a las Fases 0-1 (comprensión)

### RECURRENT BLOCK (en loop hasta max_loop_iters):
- El núcleo de razonamiento recurrente
- Cada iteración del loop es el equivalente funcional de un paso de chain-of-thought en espacio latente continuo
- Más bucles en inferencia = cadenas de razonamiento más profundas = problemas más difíciles resueltos
- Equivalente a las Fases 2-4

### CODA:
- Refinamiento final de la salida
- Transforma el razonamiento latente en output
- Equivalente a la Fase 5 + CHEF FINAL

### CONCEPTO CLAVE:
El sistema puede dedicar más cómputo a problemas más difíciles ajustando el número de iteraciones del Recurrent Block. Esto es razonamiento escalado en inferencia (inference-time scaling).

### Integrado con el sistema FABLES:
```
FABLES (5 fases)
  ↓
PRELUDE (comprensión Fase 0-1)
  ↓
RECURRENT LOOP (razonamiento Fases 2-4)
controlado por DRE COMPLEXITY_ESTIMATOR
  ↓
CODA (síntesis Fase 5 + CHEF FINAL)
```

---

## 14. DRE PIPELINE (9 PASOS)

```
INPUT
  ↓
COMPLEXITY ESTIMATOR
  ↓
PLANNER
  ↓
REASONER
  ↓
SELF CHECK
  ↓
REASONER
  ↓
SELF CHECK
  ↓
SYNTHESIS
  ↓
OUTPUT
```

### Fórmula del score:
```
score = (dependencias × 2) + pasos_estimados
        + (5 si ambiguo) + (5 si alto riesgo)
```

### Niveles y acción:
- **LOW** (score 0-3): 0 ciclos, ejecución directa
- **MEDIUM** (score 4-8): 1 ciclo Reasoner → Verifier
- **HIGH** (score 9-15): 2 ciclos, motor completo
- **EXTREME** (score 16+): 3+ ciclos + simulaciones múltiples

---

## 15. MICRO-CICLO POR PASO (7 PASOS)

```
objetivo
  ↓
plan
  ↓
subplan
  ↓
ejecución
  ↓
verificación
  ↓
corrección
  ↓
resultado
```

Aplicado internamente en cada paso del razonamiento.

---

## 16. LOS 7 VALIDADORES Y SU ORDEN ÓPTIMO

Los validadores disponibles en el sistema:
- Verifier
- Critic
- Judge
- Sentinel
- Sheriff
- Policy Engine
- PydanticAI

**Pregunta pendiente:** ¿Cuál es el orden óptimo de estos validadores?

---

## 17. CORE PLANTILLA FIJA + ADAPTADORES

**MYTHOS CORE (plantilla fija — nunca cambia):**
- Los 40 pasos base
- Las 5 fases
- La LISTA_GLOBAL
- El CHEF FINAL (4 pasos)
- El DRE (estimador de complejidad)

**ADAPTADOR (cambia según el caso de uso):**
- Qué pasos activar según el escenario
- Cuántas iteraciones del Recurrent Loop
- Qué herramientas externas usar
- Qué formato de salida generar

### Casos de uso:
- Código → Adaptador_Code
- Investigación → Adaptador_Research
- Análisis → Adaptador_Analysis
- Diseño → Adaptador_Design

### Flujo:
```
FABLES CORE (fijo)
  ↓
Adaptador (intercambiable)
  ↓
Caso de uso detectado
  ↓
Ejecución configurada
```

---

## 18. OPTIMIZAR PARA (8 CRITERIOS)

1. Calidad
2. Robustez
3. Recuperación
4. Persistencia
5. Escalabilidad
6. Auditoría
7. Control
8. Evolución futura

### NO OPTIMIZAR PARA:
- NO para velocidad
- NO para simplicidad

---

## 19. CÓMO DISEÑAR UN CORE ESTABLE

El núcleo de control y razonamiento debe ser FIJO.
Los adaptadores deben ser INTERCAMBIABLES.

Así puedes cambiar todo el comportamiento sin tocar el código central.

Es más fácil de:
- mantener
- probar
- mejorar

---

## 20. DETERMINISTA VS PROBABILÍSTICO

**Determinista (código duro):**
- Output siempre igual dado el mismo input
- Se puede testear con unit tests
- No requiere LLM
- Ejemplos: FSM, grafo dependencias, score de confianza, persistencia

**Probabilístico (LLM):**
- Output varía según contexto
- Requiere capacidad de razonamiento semántico
- No se puede predecir exactamente
- Ejemplos: reformulación del problema, generación de hipótesis, síntesis final

---

## 21. RESPUESTA DE FABLE SOBRE STRUCTURED COT

Esta fue la única respuesta recibida de FABLE antes de que el servidor dejara de funcionar.

### Diagrama:
```
ENTRADA (prompt + contexto)
  ↓
┌─────────────────────┐
│ FASE DE PENSAMIENTO │ ← tokens internos, no visibles
│ 1. Entender tarea   │
│ 2. Descomponer      │
│ 3. Explorar opciones│
│ 4. Auto-verificar   │
│ 5. Corregir errores │
└─────────────────────┘
  ↓
RESPUESTA FINAL (visible)
```

### Punto clave:
Todo eso es el mismo proceso de generación de texto.
No hay módulos separados.
El modelo aprendió durante el entrenamiento a "razonar en borrador" antes de responder.

### JSON:
```json
{
  "instrucciones": "Antes de responder, ejecuta estas fases en orden",
  "fases": [
    {"f1": "Reformula la tarea en tus palabras"},
    {"f2": "Lista los sub-problemas"},
    {"f3": "Resuelve cada uno"},
    {"f4": "Verifica: ¿contradicciones? ¿falta algo?"},
    {"f5": "Respuesta final en formato X"}
  ],
  "regla": "Marca cada fase con su etiqueta antes de avanzar"
}
```

### Importancia:
Esto se llama **structured chain-of-thought**.
Mejora mucho los modelos pequeños que tienden a saltar directo a la respuesta.
Es totalmente legítimo, es ingeniería de prompts estándar.

---

## 22. WORKFLOW DE CADA PASO

```
planner()
  ↓
tester()
  ↓
critic()
```

Cada paso es código real. No son prompts abstractos. Son funciones Python que se ejecutan en secuencia.

---

## 23. PREGUNTAS DE SEPARACIÓN

**¿Qué partes deberían ser código?**
- Lógica ejecutable, transformaciones de datos, validaciones deterministas

**¿Qué partes deberían ser workflow?**
- Flujos de trabajo, secuencias de pasos

**¿Qué partes deberían ser configuración?**
- Settings, parámetros, constantes

**¿Qué partes deberían ser razonamiento?**
- Decisiones complejas, análisis semántico

---

## 24. RESTRICCIONES / RECURSOS / CUELLOS / RIESGOS / SUPUESTOS FALSOS

**RESTRICCIONES:**
- ¿Qué no puede cambiar?
- ¿Qué límites son inamovibles?
- ¿Qué dependencias externas existen?

**RECURSOS:**
- ¿Qué tiene el sistema disponible?
- ¿Qué tokens tiene por ciclo?
- ¿Qué memoria puede usar?
- ¿Qué herramientas externas puede llamar?

**CUELLOS DE BOTELLA:**
- ¿Dónde se va a atascar el sistema?
- ¿Qué pasos son los más lentos?
- ¿Qué pasos consumen más tokens?
- ¿Dónde puede romperse la cadena?

**RIESGOS:**
- ¿Qué puede fallar silenciosamente?
- ¿Qué fallo tiene mayor impacto?
- ¿Qué es difícil de recuperar?

**SUPUESTOS FALSOS:**
- ¿Qué estamos asumiendo que puede no ser cierto?
- ¿Qué funciona en teoría pero no en producción?
- ¿Qué asumimos del LLM que no siempre se cumple?

---

## 25. REFUTACIÓN (BLOQUE X)

### Desafiar la Arquitectura

```
DESAFIAR LA ARQUITECTURA
  ↓
CRITIC
  ↓
¿Qué está mal en esta arquitectura?
¿Qué supuestos son falsos?
¿Qué está sobre-diseñado?
¿Qué está sub-diseñado?
  ↓
COUNTER CRITIC
  ↓
¿Cuáles de las críticas anteriores son válidas?
¿Cuáles son exageradas?
¿Cuáles se resuelven con cambios menores?
¿Cuáles requieren rediseño completo?
  ↓
FAILURE SIMULATOR
  ↓
Simula cómo falla esta arquitectura en:
- uso normal (tarea simple)
- uso extremo (tarea compleja de 30-50 pasos)
- fallo de un componente crítico
- pérdida de contexto a mitad del proceso
- modelo LLM que alucina en el paso 20 de 40
- saturación de memoria en proceso de 24 horas
  ↓
ARQUITECTURA MEJORADA
  ↓
Con base en Critic + Counter Critic + Failure Simulator,
proponer la arquitectura mejorada que sobrevive
todos los escenarios de fallo.
```

### Regla:
No asumir que MYTHOS está correcto.
Hacer refutación contra el mismo antes de decidir.

---

## 26. V1/V2/V3 → COMPARADOR → JUDGE → GANADOR

```
VERSIÓN 1:
Primera propuesta sin filtros.
Lo que naturalmente se diseñaría.

VERSIÓN 2:
Una arquitectura alternativa radicalmente diferente.
Si la V1 es secuencial, la V2 es paralela.
Si la V1 es jerárquica, la V2 es plana.

VERSIÓN 3:
Una arquitectura híbrida que tome lo mejor de V1 y V2
y elimine sus debilidades.

COMPARADOR:
Tabla comparativa objetiva con métricas:
- complejidad de implementación (1-10)
- robustez ante fallos (1-10)
- capacidad de recuperación (1-10)
- escalabilidad (1-10)
- mantenibilidad (1-10)
- control sobre el LLM (1-10)

JUDGE:
Con base en el COMPARADOR, el Judge decide:
- cuál versión gana en cada criterio
- cuál es la ganadora global
- qué elementos de las perdedoras conservar

GANADOR:
La arquitectura ganadora con todas las mejoras
integradas y el código ejecutable completo.
```

---

## 27. ARQUITECTURA MAXBRY

```
USUARIO
  ↓
MAXBRY
  ↓
Control Layer
  ↓
Workflow Layer
  ↓
Memory Layer
  ↓
Tool Layer
  ↓
LLM Layer
```

**MAXBRY NO es una nueva LLM.**
MAXBRY NO es un modelo fundacional.
MAXBRY NO compite con Claude, GPT, Gemini, Qwen.

**MAXBRY es una CAPA EXTERNA DE ORQUESTACIÓN, CONTROL Y ORGANIZACIÓN.**
MAXBRY vive fuera de los modelos.
MAXBRY coordina modelos, herramientas, proyectos y objetivos.
</content>