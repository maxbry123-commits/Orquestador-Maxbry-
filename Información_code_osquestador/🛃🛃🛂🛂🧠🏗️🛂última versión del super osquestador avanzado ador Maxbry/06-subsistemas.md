# DOCUMENTO 6: SUBSISTEMAS DEL ORQUESTADOR
## Extraído del historial del chat

---

## 1. SYSTEM PROMPT MYTHOS (15 SECCIONES)

El System Prompt raíz tiene 15 secciones que definen la identidad y comportamiento del orquestador.

### Las 15 secciones:
```
S01 · Identidad del Orquestador
S02 · Principios Fundamentales
S03 · Objetivos Primarios
S04 · Restricciones Absolutas
S05 · Forma de Comunicación
S06 · Manejo de Decisiones
S07 · Gestión de Recursos
S08 · Trabajo en Equipo
S09 · Validación de Outputs
S10 · Manejo de Errores
S11 · Memoria y Aprendizaje
S12 · Interacción con MAX
S13 · Manejo de Tiempos
S14 · Optimización Continua
S15 · Filosofía General
```

### Características:
- Es LEY (no negociable)
- Aplica a TODOS los agentes
- Cargado en cada sesión
- Auditado por CSA J5

---

## 2. SKILLS SYSTEM (13 CRITERIOS + DEBATE 4 ESPECIALISTAS)

Sistema de Skills con 13 criterios de evaluación y debate entre 4 especialistas.

### Los 13 criterios:
```
1.  Relevancia
2.  Efectividad comprobada
3.  Costo de aplicación
4.  Compatibilidad
5.  Mantenibilidad
6.  Documentación
7.  Reusabilidad
8.  Seguridad
9.  Performance
10. Escalabilidad
11. Compliance
12. Test coverage
13. Comunidad / Soporte
```

### Versiones:
```
v1 · Inicial (básica)
v2 · Mejorada (con debate)
v3 · Avanzada (con productor + consumidor)
```

### Debate 4 Especialistas:
```
1. Productor    → quien la creó
2. Consumidor   → quien la usa
3. Auditor      → quien valida
4. Crítico      → quien busca fallas
```

---

## 3. MULTI-SOURCE INVESTIGATION (5 AGENTES)

5 agentes que investigan en paralelo desde diferentes fuentes.

### Los 5 agentes:
```
1. GitHub Agent
   - Repos públicos
   - Stars, issues, PRs
   - Patrones de uso
   - Código de referencia
   - Proyectos similares

2. HuggingFace Agent
   - Modelos GGUF disponibles
   - Datasets relevantes
   - Spaces con código útil
   - Papers referenciados
   - Versiones y updates

3. Web Agent
   - Búsqueda general
   - Documentación oficial
   - Artículos técnicos
   - Tutoriales
   - Best practices
   - Comparativas

4. YouTube Agent
   - Tutoriales paso a paso
   - Demos de productos
   - Conferencias técnicas
   - Comparativas visuales
   - Casos de estudio

5. MCP Agent
   - Model Context Protocol
   - Tools disponibles
   - Integraciones oficiales
   - Smithery catálogo
   - Composio integraciones
```

### Coordinación:
- Investigación en paralelo
- Resultados consolidados
- Deduplicación automática
- Conflicto → escalar a MAX

---

## 4. UNIVERSAL PLUG v1.5

Contrato JSON estándar (MAXBRY Module Contract) que cualquier módulo debe implementar para ser compatible.

### ESTRUCTURA
```json
{
  "module_id": "string único",
  "version": "semver",
  "type": "input|output|loop|skill|agente",
  "inputs": [...],
  "outputs": [...],
  "dependencies": [...],
  "config": {...},
  "metadata": {...}
}
```

### Características:
- Universal: cualquier módulo lo implementa
- Versionado: semver estricto
- Validado: por CSA
- Intercambiable: hot-swap sin downtime
- Documentado: schema en JSON Schema

### Uso:
```
Cada módulo nuevo:
  1. Implementa Universal Plug v1.5
  2. Se registra en BIS
  3. CSA valida
  4. Entra al swarm
```

### Concepto:
```
Este JSON es el enchufe universal de MAXBRY, YAIWES y NCT Neuronas Code Turbo.

Su función es convertir cualquier pieza de código, prompt DSL, agente IA, API, MCP, herramienta o base de datos en una ficha conectable.

Cada ficha indica:
- Qué información recibe
- Qué información entrega
- Cómo se ejecuta
- Qué permisos necesita
- Con qué otras fichas puede conectarse

Gracias a este contrato, el sistema puede unir automáticamente módulos de Python, DSL, LLMs locales o externos, APIs y MCP para formar redes de neuronas funcionales y pipelines completos sin depender de un lenguaje específico.

En una frase:
Es el estándar que permite conectar todas las neuronas de software de MAXBRY como bloques LEGO inteligentes, independientemente de si son código, prompts DSL o capas externas de IA. 🧠⚡
```

---

## 5. MINI-MAX M3 + KIMI K2.7-CODE (JEFE/EMPLEADO)

División de roles: MiniMax M3 actúa como jefe/arquitecto, Kimi K2.7-Code como empleado/ejecutor.

### M3 (JEFE)
```
- Rol: arquitecto, estratega
- Decide: qué hacer
- Tareas:
  - Diseño de alto nivel
  - Toma de decisiones
  - Interacción con MAX
  - Supervisión
- NO ejecuta código directo
```

### KIMI K2.7-CODE (EMPLEADO)
```
- Rol: ejecutor, implementador
- Decide: cómo hacerlo (siguiendo instrucciones)
- Tareas:
  - Implementación de código
  - Testing
  - Debugging
  - Documentación
- SÍ ejecuta código
```

### División de trabajo:
```
MAX → M3 (jefe)
       ↓
M3 planifica → Kimi ejecuta
       ↓
Kimi reporta → M3 valida
       ↓
M3 presenta → MAX aprueba
```

---

## 6. SISTEMA DE RAZONAMIENTO EXTERNO (URS)

Sistema universal de razonamiento:
- **STANDARD** (5+12): para tareas simples a medianas
- **TURBO** (12+45): para tareas críticas

---

## 7. FUSIÓN MiniMax + KIMI K (TAREAS LARGAS)

### Aportes MiniMax:
- Dual classification (intent + tasktype)
- Team engine (leader/worker/verifier, 3 rondas)
- Verifier adversarial (3 capas)
- Structured summaries (context aislado)
- Coordinator consolidator (hub)

### Aportes Kimi:
- OK Computer / Skills / Swarm routing
- Frozen subagent spawning
- Async gather worker pool
- PAD (arousal/pleasure/dominance)
- Anxiety circle detection (L1/L2/L3)
- Anti-drift (KL divergence)
- EROS 3-tier consolidation
- Repair pipeline 5 pasos

### Mejoras que la fusión habilita:
1. Doble watchdog (PAD + Anti-drift)
2. Triaje emocional + triaje estructural
3. Verificación cruzada cruzada
4. Compactación jerárquica con resúmenes estructurados
5. Repair con reintentos + fallback modelo + checkpoint + compresión + escalado
6. Memoria de aprendizaje
7. Orquestador 100% determinista

---

## 8. CONFLICTOS RESUELTOS POR EL FUSIONADOR

| Conflicto | Resolución NCT |
|---|---|
| MiniMax "1 agente grande" vs Kimi "100 workers pequeños" | Granularidad adaptativa por router.py |
| MiniMax verifica al final vs Kimi cada paso | Verificación multicapa intercalada |
| Kimi cancela por ansiedad vs MiniMax espera | Escalado gradual: ansiedad L1=log, L2=pause, L3=SIGKILL |
| EROS vs structured summaries | EROS sobre summaries: doble compactación |
| Memoria: Kimi event-sourcing vs MiniMax jerárquica | Memoria híbrida (jerárquica + journaling) |

---

## 9. NUEVO MODELO DE SISTEMA KIMI + MiniMax PARA NCT

Sistema de trabajo automático tipo Kimi K y MiniMax para NCT:

### FASE 0: CLASIFICACIÓN DUAL
- Intención (Kimi): Simple/Media/Compleja
- Tipo tarea (MiniMax): Simple/Batch/Complex + Tipo proyecto
- → Clasificación unificada

### FASE 1: SELECCIÓN DE MODO Y RUTA
- Modo agente (Kimi): OK Computer/Skills/Swarm
- Ruta ejecución (MiniMax): Directa/Batch/Agentes especializ.
- → Decisión unificada

### FASE 2: SKILLS Y DESCOMPOSICIÓN
- Carga Skills (Kimi): SKILL.md
- Planificación (MiniMax): todo_write + agentes
- → Plan unificado: subtareas + agentes + orden

### FASE 3: AISLAMIENTO Y PREPARACIÓN
- Spawn subagentes congelados (Kimi)
- Structured Summaries (MiniMax): Contexto aislado
- → Workers listos con contexto aislado y tools

### FASE 4: EJECUCIÓN (Única que usa IA)
- Worker Pool (Kimi): Hasta 100 workers simultáneos, asyncio.gather()
- Team Engine (MiniMax) dentro de c/worker: Leader → Worker → Verifier (3 rondas)

### FASE 5: MONITOREO SIMULTÁNEO (3 sistemas)
- PAD (Kimi): Arousal >0.8 Y Pleasure <0.2 → SIGKILL+Respawn
- Ansiedad (MiniMax): ¿Duda en círculos? Nivel 1/2/3
- Anti-Drift (Kimi): KL(plan || actual) >0.02? Halt→Rollback

### FASE 6: VERIFICACIÓN 3-CAPAS
- CAPA 1: Adversarial (MiniMax): Verifier busca errores → 3 rondas
- CAPA 2: Cruzada (Kimi): Executor B valida output de A
- CAPA 3: Maker-Checker (Ambos): Módulo A produce, Módulo B verifica

### FASE 7: CONSOLIDACIÓN JERÁRQUICA
- EROS 3-Tier (Kimi): Tier 3 (logs crudos) → Tier 2 (Strategic Pulses) → Tier 1 (<5% contexto)
- Coordinator (MiniMax): Recibe outputs, integra, maneja escalados

### FASE 8: REPAIR PIPELINE (si algo falló)
- Paso 1: Retry simple (3 intentos)
- Paso 2: Context Compression (L1/L2)
- Paso 3: Fallback Model / Agent
- Paso 4: Restore Checkpoint
- Paso 5: Escalate (Coordinator decide)

### FASE 9: CONSOLIDACIÓN FINAL Y ENTREGA
- Merge resultados + Consistencia global
- Empaquetado (KIMI_REF + archivos + URLs)
- State.json final: trazabilidad completa

---

## 10. MÓDULO NCT COORDINATOR (ADICIONAL)

```
UBICACIÓN: /nct_coordinator/ (nueva carpeta, no toca nada existente)

ARCHIVOS NUEVOS: 13 (8 coordinador + 2 state + config + main.py + __init__)

PRINCIPIO: El módulo NCT es un ORQUESTADOR que invoca los 25 bloques
existentes como workers. No los modifica, no los reescribe, no los
reemplaza. Solo les asigna tareas y recoge resultados.

COMUNICACIÓN: state.json + API interna de cada bloque

MODOS: Manual | Semi-Auto | Continuo (selector en main.py)

IA: Solo en Fase 4 (worker_pool) y Fase 6 (verifier), siempre bajo
schema estricto. El coordinador es 100% Python determinista.
```

### Archivos del NCT Coordinator:
```
nct_coordinator/
├── __init__.py
├── fsm.py                       # Orquestador 10 fases
├── classifier.py                # Clasificación dual (Fase 0)
├── router.py                    # Selección modo/ruta (Fase 1)
├── planner.py                   # Descomposición (Fase 2)
├── context_isolator.py          # Aislamiento (Fase 3)
├── worker_pool.py               # Pool de workers (Fase 4)
├── monitor.py                   # PAD + Ansiedad + Drift (Fase 5)
├── verifier.py                  # 3-capas (Fase 6)
├── consolidator.py              # EROS + Coordinator (Fase 7)
├── repair.py                    # Pipeline 5 pasos (Fase 8)
└── deliver.py                   # Empaquetado final (Fase 9)

state/
├── engine.py                    # Event sourcing + snapshots
└── telemetry.py                 # Métricas PAD

config/
└── nct_config.yaml              # Config del coordinador
```

---

## 11. SELECTOR DE MODOS (main.py)

```
1. MODO MANUAL
   → Usuario controla cada bloque directamente
   → Sin intervención del coordinador NCT

2. MODO SEMI-AUTOMÁTICO
   → Software sugiere, usuario aprueba cada fase
   → NCT asiste pero no toma decisiones finales

3. MODO CONTINUO (NCT)
   → Usuario describe la tarea, NCT coordina todo automáticamente
   → 10 fases: Clasificar → Planificar → Ejecutar → Verificar → Entregar
   → Sin supervisión humana durante la ejecución
```
</content>