# DOCUMENTO 12: ARQUITECTURA COMPLETA DEL SISTEMA
## Extraído del historial del chat

---

## 1. NCT NEURONAS CODE TURBO — VISIÓN GENERAL

**Qué es:** Un MÓDULO ADICIONAL de coordinación para el software existente.
NO reemplaza ningún bloque actual. NO modifica el código original.
Es un tercer modo de trabajo que se añade a los ya existentes.

**Modos del software:**
1. Modo Manual → El usuario controla cada paso
2. Modo Semi-automático → El software actual opera con supervisión
3. Modo Continuo (NCT) → Coordinación automática para tareas largas

**Qué hace NCT:**
Coordina los 25 bloques existentes para ejecutar tareas complejas de forma automática y continua, sin supervisión humana.

**Cómo funciona:**
- Fase 0-3: Clasifica, planifica, descompone y prepara
- Fase 4: Invoca los bloques existentes como workers (única fase con IA)
- Fase 5-6: Monitorea (PAD/Ansiedad/Drift) y verifica (3-capas)
- Fase 7-9: Consolida, repara si falla, y entrega

**Arquitectura:**
- 8 archivos Python de coordinación (~960 líneas)
- 0% IA en el coordinador (solo reglas fijas)
- IA solo en Fase 4 (ejecución) y Fase 6 (verificación)
- Comunicación vía state.json con los bloques existentes

**No requiere:**
- No instalar Kimi K2.5, MiniMax, ni Hermes
- No desplegar agentes externos
- No modificar el código existente

**Sí requiere:**
- Lista de los 25 bloques con: nombre, función, formato entrada/salida
- Definir cómo se invoca cada bloque (API, CLI, función directa)

---

## 2. UBICACIÓN Y ESTRUCTURA DEL PROYECTO

```
proyecto_principal/                  # Tu proyecto actual
│
├── software_principal/              # Tus 25 bloques (SIN TOCAR)
│   ├── arquitectura/
│   ├── rag/
│   ├── escritor/
│   ├── ejecutor/
│   ├── validacion/
│   ├── reparacion/
│   └── ... (20 bloques más)
│
├── nct_coordinator/                 # ← NUEVO MÓDULO (adicional)
│   ├── __init__.py
│   ├── fsm.py                       # Orquestador 10 fases
│   ├── classifier.py                # Clasificación dual (Fase 0)
│   ├── router.py                    # Selección modo/ruta (Fase 1)
│   ├── planner.py                   # Descomposición (Fase 2)
│   ├── context_isolator.py          # Aislamiento (Fase 3)
│   ├── worker_pool.py               # Pool de workers (Fase 4)
│   ├── monitor.py                   # PAD + Ansiedad + Drift (Fase 5)
│   ├── verifier.py                  # 3-capas (Fase 6)
│   ├── consolidator.py              # EROS + Coordinator (Fase 7)
│   ├── repair.py                    # Pipeline 5 pasos (Fase 8)
│   └── deliver.py                   # Empaquetado final (Fase 9)
│
├── state/                           # ← NUEVO (gestión de estado)
│   ├── engine.py                    # Event sourcing + snapshots
│   └── telemetry.py                 # Métricas PAD
│
├── config/
│   └── nct_config.yaml              # Config del coordinador
│
├── state.json                       # Estado compartido (runtime)
│
└── main.py                          # Entry point con selector de modo
```

---

## 3. 25 BLOQUES DEL SOFTWARE PRINCIPAL (NO MODIFICAR)

```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│Arquitect.│ │   RAG    │ │ Escritor │ │  Ejecutor    │
└──────────┘ └──────────┘ └──────────┘ └──────────────┘
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│Validación│ │Reparación│ │  Test    │ │   Deploy     │
└──────────┘ └──────────┘ └──────────┘ └──────────────┘
              ... (25 bloques)
```

---

## 4. INTERFAZ PRINCIPAL DEL SOFTWARE

### Selección de Modo:

```
┌─────────────┐  ┌─────────────────┐  ┌───────────────────┐
│             │  │                 │  │                   │
│   MANUAL    │  │  SEMI-AUTOMÁTICO│  │    CONTINUO       │
│             │  │                 │  │    (Automático)   │
└─────────────┘  └─────────────────┘  └───────────────────┘
```

### Modo Manual:
- El usuario decide qué bloque usar, cuándo y en qué orden
- Interfaz paso a paso
- Ideal para tareas pequeñas o específicas

### Modo Semi-Automático:
- El software sugiere bloques y orden
- El usuario aprueba o modifica cada fase
- Puntos de confirmación entre etapas

### Modo Continuo:
- El usuario solo describe la tarea final
- NCT descompone, coordina, ejecuta, verifica y entrega
- Sin intervención humana durante la ejecución
- Recuperación automática ante fallos

---

## 5. FLUJO COMPLETO (MODO CONTINUO)

```
Usuario describe tarea
    │
    ▼
classifier.py (Fase 0) ─► router.py (Fase 1) ─► planner.py (Fase 2-3)
    │
    ▼
worker_pool.py (Fase 4) ─► INVOCA TUS 25 BLOQUES ORIGINALES
    │
    ├─► monitor.py (Fase 5) — PAD + Ansiedad + Anti-Drift
    ├─► verifier.py (Fase 6) — 3 capas de verificación
    │
    ▼
consolidator.py (Fase 7) ─► repair.py (Fase 8, si falla) ─► deliver.py (Fase 9)
    │
    ▼
Usuario recibe resultado final con trazabilidad completa
```

---

## 6. PRINCIPIOS CLAVE DE NCT

- 100% Python determinista (sin IA en el coordinador)
- IA solo como motor en Fase 4 (ejecución) y Fase 6 (verificación)
- Comunicación vía state.json (event sourcing)
- Los 25 bloques originales NO se modifican
- Recuperación automática ante fallos (5 pasos de repair)
- Trazabilidad completa de cada decisión y ejecución

---

## 7. INTERFAZ DE USUARIO DEL SOFTWARE

```
┌─────────────────────────────────────────────────────────────────┐
│                    SELECCIÓN DE MODO                          │
│                                                               │
│  ┌─────────────┐  ┌─────────────────┐  ┌───────────────────┐  │
│  │             │  │                 │  │                   │  │
│  │   MANUAL    │  │  SEMI-AUTOMÁTICO│  │    CONTINUO       │  │
│  │             │  │                 │  │    (Automático)   │  │
│  └─────────────┘  └─────────────────┘  └───────────────────┘  │
│                                                               │
│  Usuario controla   Software opera        Software trabaja    │
│  cada paso          con supervisión       sin supervisión     │
│                     del usuario           (NCT coordina)      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. NUEVOS BLOQUES NCT (13 ARCHIVOS)

### BLOQUES DE COORDINACIÓN (8)

1. **fsm.py** — Orquestador central, 10 fases, sin IA
2. **classifier.py** — Clasifica tareas (simple/batch/compleja)
3. **router.py** — Elige ruta y modo de ejecución
4. **planner.py** — Descompone en subtareas balanceadas
5. **context_isolator.py** — Aísla contexto por worker
6. **worker_pool.py** — Invoca tus 25 bloques como workers
7. **monitor.py** — PAD + Ansiedad + Anti-Drift
8. **verifier.py** — Verificación adversarial 3-capas

### BLOQUES DE SOPORTE (5)

9. **consolidator.py** — Consolida resultados de workers
10. **repair.py** — Pipeline 5 pasos si algo falla
11. **deliver.py** — Empaqueta y entrega resultado final
12. **state/engine.py** — Event sourcing + state.json
13. **state/telemetry.py** — Métricas y circuit breaker

---

## 9. MODOS Y FLUJOS

### FLUJO MODO CONTINUO (MÁS IMPORTANTE)

```
USUARIO
  │
  ▼
main.py (selector de modo)
  │
  └─► Modo Continuo ─► nct_coordinator toma el control
       │
       ▼
   fsm.py (orquestador)
       │
       ▼
   classifier.py → router.py → planner.py → context_isolator.py
       │
       ▼
   worker_pool.py ──► INVOCA TUS 25 BLOQUES (API/CLI/función)
       │
       ▼
   monitor.py (paralelo a la ejecución)
       │
       ▼
   verifier.py (valida outputs de tus bloques)
       │
       ▼
   consolidator.py → repair.py (si falla) → deliver.py
       │
       ▼
   USUARIO RECIBE RESULTADO
```

---

## 10. ARQUITECTURA DETALLADA DE NCT COORDINATOR

```
┌─────────────────────────────────────────────────────────────────┐
│              SOFTWARE ORIGINAL (25 BLOQUES) — SIN MODIFICAR    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NUEVOS BLOQUES NCT (13 archivos)             │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ BLOQUES DE COORDINACIÓN (8)                               │ │
│  │                                                           │ │
│  │ 1. fsm.py            Orquestador central, 10 fases, sin IA   │ │
│  │ 2. classifier.py     Clasifica tareas (simple/batch/compleja) │ │
│  │ 3. router.py         Elige ruta y modo de ejecución          │ │
│  │ 4. planner.py        Descompone en subtareas balanceadas     │ │
│  │ 5. context_isolator.py  Aísla contexto por worker            │ │
│  │ 6. worker_pool.py    Invoca tus 25 bloques como workers      │ │
│  │ 7. monitor.py        PAD + Ansiedad + Anti-Drift             │ │
│  │ 8. verifier.py       Verificación adversarial 3-capas        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ BLOQUES DE SOPORTE (5)                                    │ │
│  │                                                           │ │
│  │ 9.  consolidator.py   Consolida resultados de workers         │ │
│  │ 10. repair.py         Pipeline 5 pasos si algo falla          │ │
│  │ 11. deliver.py        Empaqueta y entrega resultado final    │ │
│  │ 12. state/engine.py   Event sourcing + state.json             │ │
│  │ 13. state/telemetry.py  Métricas y circuit breaker            │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. UBICACIÓN EN EL PROYECTO: NTC_COORDINATOR/

```
nct_coordinator/   ← NUEVO (8 archivos + 2 state + config + main.py)
   ├── fsm.py
   ├── classifier.py
   ├── router.py
   ├── planner.py
   ├── context_isolator.py
   ├── worker_pool.py
   ├── monitor.py
   ├── consolidator.py
   └── repair.py
```

---

## 12. ARQUITECTURA MÓDULO NCT — ADICIONAL AL SOFTWARE PRINCIPAL

**UBICACIÓN:** /nct_coordinator/ (nueva carpeta, no toca nada existente)

**ARCHIVOS NUEVOS:** 13 (8 coordinador + 2 state + config + main.py + __init__)

**PRINCIPIO:** El módulo NCT es un ORQUESTADOR que invoca los 25 bloques existentes como workers. No los modifica, no los reescribe, no los reemplaza. Solo les asigna tareas y recoge resultados.

**COMUNICACIÓN:** state.json + API interna de cada bloque

**MODOS:** Manual | Semi-Auto | Continuo (selector en main.py)

**IA:** Solo en Fase 4 (worker_pool) y Fase 6 (verifier), siempre bajo schema estricto. El coordinador es 100% Python determinista.

---

## 13. FLUJO DETALLADO POR FASE

### Fase 0 - Clasificación:
```
FASE 0 — CLASIFICACIÓN DUAL
┌─────────────────┐  ┌──────────────────────┐
│ Intención (Kimi) │  │ Tipo tarea (MiniMax) │
│ Simple/Media/    │  │ Simple/Batch/Complex │
│ Compleja         │  │ + Tipo proyecto      │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
           Clasificación unificada
```

### Fase 1 - Modo y Ruta:
```
FASE 1 — SELECCIÓN DE MODO Y RUTA
┌─────────────────┐  ┌──────────────────────┐
│ Modo agente     │  │ Ruta ejecución       │
│ (Kimi)          │  │ (MiniMax)            │
│ OK Computer/    │  │ Directa/Batch/       │
│ Skills/Swarm    │  │ Agentes especializ.  │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
           Decisión unificada
```

### Fase 2 - Skills y Descomposición:
```
FASE 2 — SKILLS Y DESCOMPOSICIÓN
┌─────────────────┐  ┌──────────────────────┐
│ Carga Skills    │  │ Planificación        │
│ (Kimi)          │  │ (MiniMax)            │
│ SKILL.md        │  │ todo_write + agentes │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
Plan unificado: subtareas + agentes + orden
```

### Fase 3 - Aislamiento:
```
FASE 3 — AISLAMIENTO Y PREPARACIÓN
┌─────────────────┐  ┌──────────────────────┐
│ Spawn subagentes│  │ Structured Summaries │
│ congelados      │  │ (MiniMax)            │
│ (Kimi)          │  │ Contexto aislado     │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
Workers listos con contexto aislado y tools
```

### Fase 4 - Ejecución (ÚNICA CON IA):
```
FASE 4 — EJECUCIÓN (Única que usa IA)
┌─────────────────────────────────────────────┐
│ Worker Pool (Kimi)                         │
│ • Hasta 100 workers simultáneos             │
│ • asyncio.gather()                          │
│ • Pipeline 7 pasos por worker               │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Team Engine (MiniMax) — dentro de c/worker  │
│ Leader → Worker → Verifier (3 rondas)       │
└─────────────────────────────────────────────┘
Tus 25 bloques reciben DSL de entrada
y devuelven JSON validado contra schema
```

### Fase 5 - Monitoreo:
```
FASE 5 — MONITOREO SIMULTÁNEO (3 sistemas)
┌──────────┐  ┌──────────────┐  ┌────────────┐
│ PAD      │  │ Ansiedad     │  │ Anti-Drift │
│ (Kimi)   │  │ (MiniMax)    │  │ (Kimi)     │
│          │  │              │  │            │
│ Arousal  │  │ ¿Duda en     │  │ KL(plan || │
│ >0.8 Y   │  │ círculos?    │  │ actual)    │
│ Pleasure │  │              │  │ >0.02?     │
│ <0.2?    │  │ Nivel 1/2/3  │  │            │
│          │  │              │  │            │
│ SIGKILL  │  │ Confirmación │  │ Halt →     │
│ +Respawn │  │ o Respawn    │  │ Rollback   │
└────┬─────┘  └──────┬───────┘  └─────┬──────┘
     └───────────────┬────────────────┘
                     ▼
           State.json actualizado
```

### Fase 6 - Verificación 3-Capas:
```
FASE 6 — VERIFICACIÓN 3-CAPAS
CAPA 1: Adversarial (MiniMax)
   Verifier busca errores → 3 rondas
                ↓
CAPA 2: Cruzada (Kimi)
   Executor B valida output de A
                ↓
CAPA 3: Maker-Checker (Ambos)
   Módulo A produce, Módulo B verifica
                ↓
Solo si 3 capas OK → output certificado
```

### Fase 7 - Consolidación:
```
FASE 7 — CONSOLIDACIÓN JERÁRQUICA
┌─────────────────────────────────────────────┐
│ EROS 3-Tier (Kimi)                         │
│ Tier 3 (Executors) → logs crudos            │
│ Tier 2 (Controllers) → Strategic Pulses     │
│ Tier 1 (Orchestrator) → <5% contexto        │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Coordinator (MiniMax)                       │
│ Recibe outputs, integra, maneja escalados   │
└─────────────────────────────────────────────┘
                      ↓
Informe pre-entrega: completitud, drift, etc.
```

### Fase 8 - Repair Pipeline:
```
FASE 8 — REPAIR PIPELINE (si algo falló)
Paso 1: Retry simple (3 intentos)
   ↓ falló
Paso 2: Context Compression (L1/L2)
   ↓ falló
Paso 3: Fallback Model / Agent
   ↓ falló
Paso 4: Restore Checkpoint
   ↓ falló
Paso 5: Escalate (Coordinator decide)
   → Replanificar / Preguntar usuario / Abortar
```

### Fase 9 - Entrega:
```
FASE 9 — CONSOLIDACIÓN FINAL Y ENTREGA
┌─────────────────────────────────────────────┐
│ Merge resultados + Consistencia global      │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Empaquetado (KIMI_REF + archivos + URLs)    │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ State.json final: trazabilidad completa     │
└─────────────────────────────────────────────┘
              ↓
      USUARIO RECIBE RESULTADO
```

---

## 14. RESUMEN DEL SISTEMA COMPLETO

**Nivel 1:** Software Principal (25 bloques) - INTOCABLE

**Nivel 2:** NCT Coordinator (13 archivos) - ADICIONAL

**Nivel 3:** MAXBRY SUPER TEAM (orquestador con Constitución, CSA, SID, BIS, Loop, Output Engine, OOS, OVFS)

**Nivel 4:** Modelos GGUF (9) + APIs (16 keys)

**Nivel 5:** Memoria persistente + STATE JSON

**Nivel 6:** Infraestructura (7 HF Spaces, 14 repos, 5 Dockerfiles)

---

## 15. PRINCIPIOS TRANSVERSALES

1. **MVP first** - anti-overengineering
2. **Regla absoluta** - NUNCA sin APROBADO de MAX
3. **Solo agregar** - NUNCA reemplazar
4. **Mantener nombres** - originales aprobados
5. **Cero alucinación** - preguntar si falta info
6. **Independencia** - Orquestador ≠ GGUF ≠ Proyectos
7. **Validación previa** - cada salida valida antes de patchear
8. **Mostrar PENDIENTE** - lo no aprobado es visible
9. **STATE JSON** - siempre actualizado
10. **5 GOALS + 12 PASOS** - en cada salida
</content>