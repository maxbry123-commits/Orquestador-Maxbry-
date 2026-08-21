# DOCUMENTO 4: SISTEMAS DE RAZONAMIENTO
## Extraído del historial del chat

---

## 1. EXTERNAL UNIVERSAL REASONING SYSTEM (EURS)

Sistema de razonamiento externo que opera en dos modos.

---

## 2. MODO STANDARD (5 CAPAS + 12 PASOS)

### Las 5 Capas:
- **C1 · Análisis del problema**
- **C2 · Generación de hipótesis**
- **C3 · Evaluación de hipótesis**
- **C4 · Síntesis de solución**
- **C5 · Verificación final**

### Los 12 Pasos:
```
P01 · Parsear input
P02 · Identificar conceptos clave
P03 · Establecer relaciones
P04 · Generar 3 hipótesis
P05 · Buscar evidencia
P06 · Evaluar cada hipótesis
P07 · Combinar resultados
P08 · Construir solución
P09 · Validar coherencia
P10 · Verificar completitud
P11 · Formatear output
P12 · Reportar
```

### Cuándo se usa:
- Tareas simples a medianas
- Recursos limitados
- Respuesta rápida

---

## 3. MODO TURBO (12 CAPAS + 45 PASOS)

### Las 12 Capas:
```
C01 · Parsing profundo
C02 · Descomposición
C03 · Contextualización
C04 · Generación exhaustiva de hipótesis
C05 · Búsqueda multi-fuente
C06 · Evaluación rigurosa
C07 · Síntesis avanzada
C08 · Diseño de solución
C09 · Implementación
C10 · Validación múltiple
C11 · Refinamiento
C12 · Certificación
```

### Los 45 Pasos:
Distribución entre las 12 capas, 3-4 pasos promedio por capa.

### Cuándo se usa:
- Tareas críticas
- Decisiones arquitectónicas
- Problemas complejos
- Cuando MAX pide máxima calidad

### Comparación:
```
STANDARD: 5 capas + 12 pasos → rápido, 80% cobertura
TURBO:    12 capas + 45 pasos → lento, 99% cobertura
```

---

## 4. MICRO-CICLO POR PASO (7 PASOS)

Aplicado internamente en cada paso del razonamiento:

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

Este micro-ciclo se aplica internamente en cada paso del razonamiento para que cada paso individual sea verificable y corregible antes de avanzar al siguiente.

---

## 5. CAPA EXTERNA · NOMBRE

Una capa externa de código encima de una LLM suele llamarse:
- **Orchestrator**
- **Agent Framework**
- **Cognitive Layer**
- **Reasoning Engine**

Si coordina varios agentes: Multi-Agent System.
Si cambia la forma de razonar: Reasoning Engine.

Para este diseño: **Mythos Cognitive Layer** o **Mythos Reasoning Engine** encaja bastante bien porque define cómo trabaja el modelo y no el modelo en sí.

---

## 6. ARQUITECTURA DE CONTROL ALTO (CADENA COMPLETA)

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

---

## 7. STACK TÉCNICO (4 LENGUAJES + SUS ROLES)

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

## 8. PYDANTICAI (CADENA COMPLETA)

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

## 9. FSM FINITE STATE MACHINE

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

## 10. SEPARACIÓN DE CAPAS (5 NIVELES)

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

## 11. DRE PIPELINE (9 PASOS)

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

El COMPLEXITY_ESTIMATOR evalúa:
- Dependencias
- Ambigüedad
- Pasos estimados
- Riesgo de error

---

## 12. OPENMYTHOS (PRELUDE → LOOP → CODA)

OpenMythos es un sistema de razonamiento recurrente de código abierto. Implementa un Recurrent-Depth Transformer con tres etapas:

### PRELUDE:
- Bloques transformer estándar
- Pre-procesa el input antes del loop recurrente
- Equivalente a las Fases 0-1 (comprensión)

### RECURRENT BLOCK (en loop hasta max_loop_iters):
- El núcleo de razonamiento recurrente
- Cada iteración del loop es el equivalente funcional de un paso de chain-of-thought en espacio latente continuo
- Más bucles en inferencia = cadenas de razonamiento más profundas = problemas más difíciles resueltos
- Equivalente a las Fases 2-4 (planificación, exploración, validación)

### CODA:
- Refinamiento final de la salida
- Transforma el razonamiento latente en output
- Equivalente a la Fase 5 + CHEF FINAL

### CONCEPTO CLAVE:
El sistema puede dedicar más cómputo a problemas más difíciles ajustando el número de iteraciones del Recurrent Block. Esto es razonamiento escalado en inferencia (inference-time scaling).

---

## 13. OPTIMIZAR PARA (LISTA 8 CRITERIOS)

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

## 14. CORE PLANTILLA FIJA + ADAPTADORES

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

### CASO DE USO:
- Código → Adaptador_Code
- Investigación → Adaptador_Research
- Análisis → Adaptador_Analysis
- Diseño → Adaptador_Design

### EJECUCIÓN:
FABLES_CORE + Adaptador_[tipo]
↓
Comportamiento específico para cada caso sin tocar el núcleo central

---

## 15. DISTINCIÓN RAZONAMIENTO VS CONTROL

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
- El pensamiento genera estrategias y soluciones
- El control garantiza que el proceso se ejecute correctamente

Son capas DIFERENTES que trabajan juntas. No se mezclan. No se reemplazan entre sí.

---

## 16. RESTRICCIONES / RECURSOS / CUELLOS / RIESGOS / SUPUESTOS FALSOS

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

## 17. WORKFLOW DE CADA PASO (CÓDIGO REAL)

```
planner()
  ↓
tester()
  ↓
critic()
```

Cada paso es código real. No son prompts abstractos. Son funciones Python que se ejecutan en secuencia.

---

## 18. LOS 7 VALIDADORES Y SU ORDEN ÓPTIMO

Los validadores disponibles en el sistema:
- Verifier
- Critic
- Judge
- Sentinel
- Sheriff
- Policy Engine
- PydanticAI

Pregunta pendiente: ¿Cuál es el orden óptimo de estos validadores?