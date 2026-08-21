# DOCUMENTO 2: ESTRUCTURA INTERNA DEL ORQUESTADOR
## Extraído del historial del chat

---

## 1. 30 MICRO-AGENTES DEL ORQUESTADOR

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

## 2. 11 ROLES INTERNOS

11 roles internos especializados que coordinan los 30 micro-agentes.

### Los 11 roles:
1. Director de Proyecto
2. Planificador Estratégico
3. Asignador de Recursos
4. Monitor de Estado
5. Coordinador de Agentes
6. Gestor de Dependencias
7. Reconciliador de Conflictos
8. Optimizador de Costos
9. Gestor de Memoria
10. Auditor de Procesos
11. Gestor de Conocimiento

---

## 3. 10 COLAS PARALELAS

10 colas paralelas que procesan tareas según prioridad y tipo.

### Las 10 colas:
- **Q1: CRITICAL** → emergencias, rollback
- **Q2: HIGH** → tareas de MAX directo
- **Q3: USER** → inputs del usuario
- **Q4: VALIDATION** → CSA, quality checks
- **Q5: EXECUTION** → tareas activas
- **Q6: MONITORING** → supervisión
- **Q7: LEARNING** → aprendizaje
- **Q8: MAINTENANCE** → housekeeping
- **Q9: BACKGROUND** → tareas de baja prioridad
- **Q10: RESERVED** → para picos de carga

### Características:
- Procesamiento paralelo
- Priorización dinámica
- Auto-balanceo
- Dead letter queue

---

## 4. CONSEJO DE CONSENSO (10 AGENTES)

10 agentes de consenso para decisiones críticas del orquestador.

### Los 10 agentes:
1. Voto Técnico → calidad técnica
2. Voto de Negocio → valor para MAX
3. Voto de Costos → impacto económico
4. Voto de Riesgos → potenciales fallos
5. Voto Ético → cumplimiento
6. Voto de UX → experiencia
7. Voto de Performance → velocidad
8. Voto de Seguridad → vulnerabilidades
9. Voto de Compatibilidad → no romper
10. Veto de MAX → decisión final de MAX

### Mecanismo:
```
Cada decisión crítica:
  - Los 10 votan
  - Si 7+ están de acuerdo → procede
  - Si no hay consenso → escala a MAX
  - Veto de MAX siempre gana
```

---

## 5. 6 NIVELES DE AUTONOMÍA (L1-L6)

### Los 6 niveles:

**L1 · ASISTENTE**
- Solo sugiere, MAX decide todo

**L2 · CONSULTOR**
- Recomienda con justificación

**L3 · COLABORADOR**
- Ejecuta tareas simples solo

**L4 · AUTÓNOMO**
- Ejecuta y reporta, MAX revisa después

**L5 · PROACTIVO**
- Anticipa necesidades, propone

**L6 · AUTOSUFICIENTE**
- Decide y ejecuta, MAX solo ve resultados

### Configuración:
- Por defecto: L3 (colaborador)
- Configurable por MAX
- Por tarea: puede tener nivel distinto

---

## 6. 12 TASK MODELS (TM01-TM12)

12 modelos de tarea predefinidos que el orquestador puede ejecutar.

### Los 12 modelos:

| TM | Nombre | Descripción |
|----|--------|-------------|
| TM01 | Análisis | entender input |
| TM02 | Diseño | arquitectura de solución |
| TM03 | Implementación | código |
| TM04 | Testing | pruebas |
| TM05 | Debug | encontrar y arreglar bugs |
| TM06 | Refactor | mejorar código existente |
| TM07 | Documentación | escribir docs |
| TM08 | Investigación | buscar información |
| TM09 | Validación | ejecutar CSA |
| TM10 | Aprendizaje | actualizar memoria |
| TM11 | Despliegue | publicar/rollback |
| TM12 | Coordinación | múltiples tareas |

Cada input se clasifica en uno o varios TM. Cada TM tiene agentes, modelos, workflows óptimos.

---

## 7. 5 LOOP VERSIONS (ALV_LOP_*)

5 versiones del loop de orquestación según contexto.

### Las 5 versiones:

- **ALV_LOP_MIN** → mínimo, 1 ciclo, 1 agente
- **ALV_LOP_STD** → estándar, 3 ciclos A/B/C paralelos
- **ALV_LOP_ENHANCED** → + learning loop, meta-learning
- **ALV_LOP_TURBO** → máximo paralelismo, todos los recursos
- **ALV_LOP_ADAPTIVE** → se adapta al contexto automáticamente

### Características:
- MIN: recursos mínimos, baja latencia
- STD: balance estándar
- ENHANCED: más lento pero aprende
- TURBO: máxima velocidad, máximo costo
- ADAPTIVE: elige según tarea

---

## 8. 10 ESTADOS DE GESTIÓN MASIVA

Cada tarea pasa por estos estados (Principio 5):

```
CREADA → EN_COLA → ASIGNADA → EJECUTANDO
                                  ↓
                              PAUSADA ↔ EJECUTANDO
                                  ↓
                              VALIDANDO
                                  ↓
              ┌──────────────────┼──────────────────┐
              ↓                  ↓                  ↓
         COMPLETADA          FALLIDA           CANCELADA
              ↓                  ↓
         (publicada)      (reintentar)
```

---

## 9. PIZARRAS (PROYECTOS + MAESTRA)

Dos tipos de pizarras para tracking (Principio 6):

### Pizarra de Proyecto:
- Estado del proyecto específico
- Tareas del proyecto
- Agentes asignados
- Recursos usados
- Decisiones tomadas

### Pizarra Maestra:
- Vista global de todos los proyectos
- Recursos totales asignados
- Estado de cada proyecto
- Alertas globales
- KPIs agregados

---

## 10. 5 OFICERS DEL EXECUTIVE BOARD

3-5 agentes que supervisan el funcionamiento global del sistema (no contenido):

1. **Chief Operations Officer (COO)** → Eficiencia, performance
2. **Chief Financial Officer (CFO)** → Costos, presupuesto
3. **Chief Quality Officer (CQO)** → Calidad global, scores
4. **Chief Risk Officer (CRO)** → Riesgos, fallos, alertas
5. **Chief Learning Officer (CLO)** → Aprendizaje, evolución

### Responsabilidades:
- Monitorear métricas globales
- Alertar a MAX si algo se desvía
- Sugerir optimizaciones
- Detectar patrones sistémicos
- Reportar estado semanal

---

## RESUMEN ESTRUCTURA

```
ORQUESTADOR MAXBRY SUPER TEAM
├── 30 micro-agentes (categorías 1-5, 6-10, 11-15, 16-20, 21-25, 26-30)
├── 11 roles internos
├── 10 colas paralelas (Q1-Q10)
├── 10 agentes de consenso
├── 6 niveles autonomía (L1-L6)
├── 12 task models (TM01-TM12)
├── 5 loop versions (ALV_LOP_*)
├── 10 estados por tarea
├── 2 tipos de pizarras
└── 5 officers (Executive Board)
```

---

## NOTAS ADICIONALES DEL CHAT

- **M3 chat ≠ SKYNER**: M3 es el arquitecto que trabaja con MAX. SKYNER es el orquestador interno.
- **SKYNER** = 1× NVIDIA en el liderazgo del orquestador.
- **BIS raíz única**: una sola raíz para todas las skills.
- **Workers/jueces/colas**: la pregunta correcta es "¿cuántos sub-agentes en paralelo?" no total.