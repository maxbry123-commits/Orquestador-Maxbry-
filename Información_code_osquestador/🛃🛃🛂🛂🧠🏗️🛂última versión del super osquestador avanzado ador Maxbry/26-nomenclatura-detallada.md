# MASTER DOCUMENTO 26: NOMBRES ESPECÍFICOS + ARCHIVOS + ESQUEMAS
## MAXBRY SUPER TEAM · Nombres Aprobados · 8 Archivos NCT · 5 ALV · 12 TM · Schemas

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO (rellena gap)

---

## 1. SCHEMAS APROBADOS (8 ARCHIVOS)

Todos los archivos JSON del sistema:

| Schema | Propósito |
|--------|-----------|
| **TASK.json** | Define una tarea individual |
| **TASK_HISTORY.json** | Historial de cambios de una tarea |
| **STATE.json** | Estado global del sistema |
| **BLACKBOARD.json** | Memoria compartida entre agentes |
| **INBOX.json** | Entrada de mensajes |
| **OUTBOX.json** | Salida de mensajes |
| **EVENTS.json** | Log de eventos |
| **PROJECT_ROOT** (por proyecto) | Root de cada proyecto |

---

## 2. ESTADOS Y LISTAS DE TRABAJO (12 ARCHIVOS)

| Archivo | Propósito |
|---------|-----------|
| INBOX.json | Recibe entrada |
| OUTBOX.json | Entrega salida |
| STATE.json | Estado actual |
| HISTORY.json | Acumulativo, NUNCA se borra |
| TASKS.json | Lista de tareas |
| lista_tareas_pendientes.json | Cola FIFO |
| lista_tareas_en_curso.json | En ejecución |
| lista_tareas_completadas.json | Terminadas OK |
| lista_tareas_fallidas.json | Con error |
| BLACKBOARD.json | Memoria compartida |
| REPORT_FOR_M3.md | Reporte a M3 |
| TELEGRAM_LOG.txt | Log de Telegram |

---

## 3. UBICACIONES Y SINCRONIZACIÓN

### 3.1 Paths
- `/workspace/orquestador/*` → git push → `nct-consensus-log/main/orquestador/`
- `/workspace/compartido/*` → git push → `nct-consensus-log/main/compartido/`

### 3.2 Sincronización
- `git pull` cada 30 segundos
- `git push` cada 5 minutos
- O cuando hay commit importante

---

## 4. 8 ARCHIVOS DEL COORDINADOR NCT

### 4.1 Los 8 principales
| Archivo | Responsabilidad |
|---------|-----------------|
| `fsm.py` | Orquestador 10 fases |
| `classifier.py` | Clasificación dual |
| `router.py` | Modo/ruta |
| `planner.py` | Descomposición |
| `context_isolator.py` | Contexto aislado |
| `worker_pool.py` | Workers (única con IA) |
| `monitor.py` | PAD + Ansiedad + Drift |
| `verifier.py` | 3 capas |

### 4.2 Los 5 archivos soporte
| Archivo | Responsabilidad |
|---------|-----------------|
| `consolidator.py` | Consolida resultados |
| `repair.py` | Repair pipeline 5 pasos |
| `deliver.py` | Multi-target delivery |
| `state/engine.py` | Engine de estado |
| `state/telemetry.py` | Telemetría |

---

## 5. G6 STAFF — 5 AGENTES PRINCIPALES

### 5.1 MiniMax M3 (LLM principal)
- Vía NVIDIA NIM
- Líder del G5 (SKYNER)
- Arquitecto

### 5.2 MiMo Code
- En HF aparte
- Code agent paralelo
- Tareas de horizonte largo

### 5.3 OpenCLAW
- Agente adicional
- Multi-canal
- 308k stars en GitHub

### 5.4 Smolagents
- Agente adicional
- Tareas generales
- HuggingFace

### 5.5 Hermes Agent
- Archivist + memoria
- 149k stars en GitHub
- Learning loop L1+L2+L3

### 5.6 Code Agent CLI (Aider/Cline)
- Instalado
- Code generation local
- Fallback para MiMo

---

## 6. 12 MODELOS DE TAREA (NOMBRES ESPECÍFICOS)

| TM | Nombre completo |
|----|-----------------|
| TM01 | TM01_ARCHITECTURE_DESIGN |
| TM02 | TM02_CODE_GENERATION |
| TM03 | TM03_RAG_RESEARCH |
| TM04 | TM04_VALIDATION_QA |
| TM05 | TM05_REPAIR_REFACTOR |
| TM06 | TM06_TEST_SUITE |
| TM07 | TM07_DEPLOY_RELEASE |
| TM08 | TM08_DOCUMENTATION |
| TM09 | TM09_DATA_PIPELINE |
| TM10 | TM10_SECURITY_AUDIT |
| TM11 | TM11_LONG_HORIZON_72H_PLUS |
| TM12 | TM12_EVOLUTIONARY_SELF_IMPROVEMENT |

---

## 7. 5 VERSIONES DE LOOP (NOMBRES ESPECÍFICOS)

| ALV | Nombre completo |
|-----|-----------------|
| 1 | ALV_LOP_GENESIS_BASELINE |
| 2 | ALV_LOP_TITANIUM_PARALLEL_GRAPH |
| 3 | ALV_LOP_QUANTUM_FRACTAL_NESTED |
| 4 | ALV_LOP_SINGULARITY_EVOLUTIONARY |
| 5 | ALV_LOP_NEXUS_FUSION_FULL |

---

## 8. 3 MONITORES (CON UMBRALES ESPECÍFICOS)

### 8.1 PAD Monitor
- **P**leasure, **A**rousal, **D**ominance
- Arousal > 0.8 AND Pleasure < 0.2 → **SIGKILL + Respawn**

### 8.2 Ansiedad Monitor
- 3 niveles:
  - Bajo: confirma
  - Medio: confirma + alerta
  - Alto: respawn

### 8.3 Anti-Drift Monitor
- KL divergence > 0.02 → halt + rollback
- Compara con baseline

---

## 9. FASES DEL ORQUESTADOR (KIMI K + MINIMAX)

### FASE 0 — Clasificación Dual
- Intención + tipo de tarea
- Primera lectura

### FASE 1 — Selección de Modo y Ruta
- Manual / Semi / Continuo
- Identifica ruta óptima

### FASE 2 — Skills y Descomposición
- BIS lookup
- Descomposición de tareas

### FASE 3 — Aislamiento y Preparación
- Contexto aislado
- Estado limpio

### FASE 4 — Ejecución (ÚNICA CON IA)
- Ejecuta tareas
- Worker pool activo
- Esta es la ÚNICA fase con IA

### FASE 5 — Monitoreo Simultáneo
- PAD monitor
- Ansiedad monitor
- Anti-Drift monitor

### FASE 6 — Verificación 3-Capas
- Adversarial
- Cruzada
- Maker-Checker

### FASE 7 — Consolidación Jerárquica (EROS 3-tier)
- Tier 1: inmediato
- Tier 2: sesión
- Tier 3: proyecto

### FASE 8 — Repair Pipeline (5 pasos)
- Retry
- Compression
- Fallback
- Restore
- Escalate

### FASE 9 — Consolidación Final y Entrega
- Multi-target delivery
- Reporte a MAX

---

## 10. 6 NIVELES DE AUTONOMÍA (CON DETALLES)

### L1 · MANUAL
- Pasos discretos
- IA 0%
- Memoria volátil

### L2 · SEMI_MANUAL
- Minutos
- IA 0%

### L3 · SCHEDULED_AUTOMATIC
- Horas
- IA 0%

### L4 · SUPERVISED_AUTONOMOUS
- Horas a 24h
- IA 0%
- Repair pipeline 5 pasos

### L5 · CONTINUOUS_AUTONOMOUS_72H_PLUS
- 72h a mes
- IA 0%
- Memoria EROS 3-tier

### L6 · EVOLUTIONARY_AUTONOMOUS
- Indefinido
- IA 0%
- Meta-memoria
- Auto-mejora

---

## 11. 16 MEJORES PRÁCTICAS DE EROSTAS

### Originales (16):
1. Cache de inferencia
2. Fallback entre modelos
3. Checkpoint por commit
4. Retry automático (2x)
5. Rollback atómico
6. Auditoría paralela
7. Preview antes de commit
8. Notificación solo cuando hay cambios
9. Cola con prioridad Urgente
10. Timeout por tipo
11. Workers paralelos (5 hilos)
12. Sandbox pre-commit
13. Rollback atómico (refuerzo)
14. Trazabilidad total
15. Metrics
16. Alertas por desviación

### Adicionales (4):
17. Auto-optimización del loop
18. Aprendizaje de errores
19. Dashboard visual
20. Export reportes

---

## 12. 20 PROPUESTAS DE MEJORA 100X

1. Encryption de keys (vault)
2. Backup automático cada 1h
3. Health checks cada 60s
4. Logs centralizados
5. Webhooks para notificaciones externas
6. Versionado de prompts
7. A/B testing de modelos
8. Cost monitoring real-time
9. Rate limiting por key
10. Auto-scaling si API saturada
11. Retry policy configurable
12. Modo "dry-run"
13. Modo "test"
14. Dashboard web para MAX
15. Export reportes PDF/MD
16. Alertas Telegram críticas
17. Modo "pause"
18. Historial de decisiones
19. Sistema de roles/permisos
20. Sandbox para código pre-commit

---

## 13. KEYS SEPARADAS POR ARCHIVO

Cada API key en archivo individual (.json) con `loader.py`. Para cambiar una key no se toca el orquestador.

### Estructura:
```
/workspace/secrets/
├── nvidia-nim-01.json
├── nvidia-nim-02.json
├── nvidia-nim-03.json
├── nvidia-nim-04.json
├── cerebras-01.json
├── ...
├── groq-01.json
├── ...
└── loader.py
```

---

## 14. PARCHES OPERACIONALES

### 14.1 CIRCUIT BREAKER
```
Estados: CLOSED / OPEN / HALF_OPEN
failure_threshold: 5 fallos en 60s
recovery_timeout: 30s
Librería: pybreaker
Por servicio: NVIDIA NIM, Cerebras, Groq, HF local
```

### 14.2 FREE TIER (cost target $0)
```
HF Spaces CPU Basic: 16GB RAM
APIs: NVIDIA NIM free, Cerebras free, Groq free
Técnicas: cache, fallback, batch, monitor, circuit breaker por costo
```

### 14.3 TELEGRAM (1 bot, multi-topic)
```
Topics:
- #nct-fase0
- #interfaz-fusionada
- #crazy-wall
- #consenso
- #consensus-log
```

### 14.4 CHROMADB (vector DB principal)
```
colección: nct_memory
metric: cosine
index: hnsw
persistencia: disco
```

### 14.5 BGE-SMALL-EN-V1.5 (embedding)
```
HF: BAAI/bge-small-en-v1.5
dim: 384
size: 24MB
alt: all-MiniLM-L6-v2
```

### 14.6 EMBEDDING (proceso)
```
cada documento nuevo → bge-small → 384-dim → ChromaDB
retrieval top-k por similitud cosine
```

---

## 15. CONCLUSIÓN

Este documento llena los gaps de nomenclatura específica, archivos del coordinador, schemas, listas de trabajo, ubicaciones, agentes principales G6, fases, niveles de autonomía, prácticas EROSTAS, propuestas 100X y parches operacionales que estaban dispersos en el proyecto.
</content>