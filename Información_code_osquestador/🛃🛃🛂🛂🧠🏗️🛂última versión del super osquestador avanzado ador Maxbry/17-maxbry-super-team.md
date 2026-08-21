# DOCUMENTO 17: MAXBRY SUPER TEAM - DETALLES COMPLETOS
## Extraído del historial del chat

---

## 1. NOMBRE Y UBICACIÓN

**MAXBRY SUPER TEAM** es el nuevo nombre que reemplaza "Orquestador M3" / "G5".

**Ubicación:** G5 = ORQUESTADOR + CONSENSO (SAME GROUP)

### Regla:
M3 chat ≠ SKYNER. M3 chat es el arquitecto que trabaja con MAX. SKYNER es el orquestador interno.

---

## 2. LIDERAZGO DEL G5

Liderado por:
- 1× NVIDIA SKYNER (líder)
- 2× Cerebras
- 2× Groq
- 4 GGUF local
- 4 GGUF vía API

---

## 3. SISTEMA DE PRODUCCIÓN

### Modos del software:
1. Modo Manual → El usuario controla cada paso
2. Modo Semi-automático → El software actual opera con supervisión
3. Modo Continuo (NCT) → Coordinación automática para tareas largas

### Reglas de operación:
- 0% IA en el coordinador (solo reglas fijas)
- IA solo como motor en Fase 4 (ejecución) y Fase 6 (verificación)
- Comunicación vía state.json con los bloques existentes

---

## 4. CAPAS DE MAXBRY (NO ES UNA LLM)

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

### Aclaraciones:
- MAXBRY NO es una nueva LLM
- MAXBRY NO es un modelo fundacional
- MAXBRY NO compite con Claude, GPT, Gemini, Qwen
- MAXBRY es una CAPA EXTERNA DE ORQUESTACIÓN, CONTROL Y ORGANIZACIÓN
- MAXBRY vive fuera de los modelos
- MAXBRY coordina modelos, herramientas, proyectos y objetivos

---

## 5. SKILLS INDEX (BIS) - 14 CATEGORÍAS

### Detalle de cada categoría:

### A · ARQUITECTURA
Diseño de sistemas, patrones, decisiones arquitectónicas.

### B · GESTIÓN
Gestión de proyectos, planificación, recursos.

### C · FRONTEND
HTML, CSS, JS, frameworks UI/UX.

### D · BACKEND
APIs, servidores, lógica de negocio.

### E · MÓVIL
iOS, Android, React Native, Flutter.

### F · ESCRITORIO
Aplicaciones desktop, Electron, Tauri.

### G · BASES DE DATOS
SQL, NoSQL, vectoriales, migraciones.

### H · APIs
REST, GraphQL, gRPC, webhooks.

### I · DEVOPS
CI/CD, contenedores, infraestructura.

### J · IA
LLMs, ML, agentes, RAG, fine-tuning.

### K · TESTING
Unit, integration, E2E, performance.

### L · SEGURIDAD
Auth, encryption, vulnerabilities, OWASP.

### M · AUTOMATIZACIÓN
Scripts, workflows, RPA, schedulers.

### N · LENGUAJES
Python, JS, Go, Rust, Java, etc.

---

## 6. APROVISIONAMIENTO AUTOMÁTICO

### Cuando MAX da datos pre-flight:

El sistema automáticamente:

1. **Crea 14 repos en GitHub:**
   - 6 repos para grupos (G1-G6)
   - 8 repos para productos

2. **Crea 7 HF Spaces:**
   - 1 por cada grupo G1-G6
   - 1 adicional para extras

3. **Escribe 5 Dockerfiles:**
   - Cada grupo tiene su Dockerfile
   - Configuración de runtime

4. **Inyecta secretos:**
   - API keys
   - Tokens
   - Credenciales

5. **Configura profiles:**
   - Conservador
   - Equilibrado
   - Agresivo

6. **Arranca el orquestador:**
   - Inicialización automática
   - Reporte a MAX

7. **Reporta a MAX:**
   - Estado de instalación
   - URLs de acceso
   - Comandos útiles

---

## 7. SISTEMA DE ESTADOS DEL G5

### 10 estados posibles para cada tarea:

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

### Transiciones válidas:
- CREADA → EN_COLA
- EN_COLA → ASIGNADA
- ASIGNADA → EJECUTANDO
- EJECUTANDO → PAUSADA → EJECUTANDO
- EJECUTANDO → VALIDANDO
- VALIDANDO → COMPLETADA
- VALIDANDO → FALLIDA
- EJECUTANDO → CANCELADA

---

## 8. AUTOEVOLUCIÓN DEL G5

El G5 evoluciona solo a través de:

1. **Meta-Learning entre releases**
2. **Self-Improving Output Quality**
3. **Auto-Curación de skills** (BIS)
4. **Counterfactual reasoning**
5. **Causalidad (no correlación)**
6. **Self-Tuner evolutivo (L6)**

---

## 9. 30 MICRO-AGENTES DEL G5 (Categorías)

```
1-5:   Análisis (input parsing, intent, context, etc.)
6-10:  Planificación (task breakdown, scheduling, etc.)
11-15: Ejecución (delegación, monitoring, retries, etc.)
16-20: Validación (CSA jueces subset, quality, etc.)
21-25: Aprendizaje (memory, patterns, optimization, etc.)
26-30: Meta (orquestación de orquestadores, recovery, etc.)
```

### Características de los 30:
- Cada uno con rol específico
- Trabajan en paralelo sobre bus de eventos
- Capacidad de invocarse entre sí
- Auto-descubrimiento de capacidades
- ≤200 LOC por archivo (regla de estructura)

---

## 10. INTEGRACIÓN CON OTROS GRUPOS

### G1 INFRAESTRUCTURA
- 7 HF Spaces (uno por grupo + extras)
- 14 repositorios GitHub
- 5 Dockerfiles
- Secrets management
- Networking entre HF Spaces
- Rate limit handling
- Monitoring de infraestructura

### G2 CORE
- BIS (Biblioteca Inteligente de Skills)
- SID (Sistema Inteligente de Definición)
- Input Engine v4.0
- Output Engine v6.1
- OOS v3.1
- OVFS

### G3 UI
- Telegram Bot (chat con MAX)
- API REST (integración con sistemas externos)
- Dashboard web (métricas, monitoring)
- CLI local (para debugging)
- Voice interface (opcional)
- Mobile-friendly (MAX usa smartphones)

### G4 AUDIT (CSA)
- 10 Jueces CSA con autoridad absoluta
- 5 fases por juez
- Sistema de veto
- Auditor SID 5 preguntas fijas

### G5 ORQUESTADOR + CONSENSO (MAXBRY SUPER TEAM)
- MAXBRY SUPER TEAM (el orquestador)
- 30 micro-agentes
- 11 internal roles
- 10 colas paralelas
- Consejo de consenso
- 6 niveles autonomía
- 12 task models
- 5 loop versions
- SKYNER interno

### G6 ASISTENTES
- 9 modelos GGUF
- 16 API keys
- Model Router Inteligente

---

## 11. RECURSOS DEL G5

### 7 HF Spaces:
- Cada uno con su propio token
- Aislados (sin compartir secretos)
- Comunicación vía API

### 14 repositorios GitHub:
- Cada proyecto = separate root
- Cada grupo = repositorio separado
- Productos adicionales en repos separados

### 5 Dockerfiles:
- Cada grupo con su Dockerfile
- Runtime consistente

---

## 12. CAPACIDADES DEL G5

### Diseño CAPACIDAD (no implementación):
- 2000+ agentes simultáneos
- 1000+ tareas simultáneas
- Sin redesign al escalar

### Recursos disponibles:
- 7 HF Spaces × 16GB = 112GB RAM
- ~13.5GB usados por modelos G6
- 87% margen libre

### Escalabilidad:
- Horizontal: agregar HF Spaces
- Vertical: upgrade a Spaces larger
- Sin rediseñar el código

---

## 13. VERIFICACIÓN DEL G5

### 5 niveles de validación por salida:
1. Buscar memoria (revisar si ya existe)
2. Validar propuesta (es correcta?)
3. Validar salida (cumple formato?)
4. Validar trazabilidad (registrable?)
5. STATE JSON actualizado

### Checklist de validación:
- 5 GOALS presentes
- 12 PASOS presentes
- AUDIT FINAL al final
- 3 inventarios separados
- Sin mezclas con GGUF/proyectos
- Sin alucinaciones

---

## 14. INTEGRACIÓN CON M3 + KIMI

### M3 (JEFE - Arquitecto)
- MiniMax M3 como arquitecto
- Decide QUÉ hacer
- Diseña de alto nivel
- Interactúa con MAX
- NO ejecuta código directo

### Kimi K2.7-Code (EMPLEADO - Ejecutor)
- Kimi K2.7-Code como implementador
- Decide CÓMO hacerlo
- Implementa código
- Testing
- Debugging

### Flujo:
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

## 15. HERRAMIENTAS RECOMENDADAS PARA MAXBRY

### WORKFLOW (5):
- Temporal
- Kestra
- Airflow
- Structurizr
- C4 Model

### ARQUITECTURA (4):
- arc42
- PlantUML
- Mermaid
- diagrams.net

### AGENTES (5):
- LangGraph
- CrewAI
- OpenAI Agents SDK
- LlamaIndex
- Mem0

### MCP / INTEGRACIÓN (3):
- MCP
- Smithery
- Composio

### GESTIÓN (3):
- Plane
- OpenProject
- Taiga

---

## 16. RELACIÓN CON EL SOFTWARE PRINCIPAL (25 BLOQUES)

### REGLA INTOCABLE:
MAXBRY SUPER TEAM NO modifica los 25 bloques del software principal.

### Lo que hace:
- Los INVOCA como workers
- Les pasa tareas
- Recoge resultados
- Los coordina

### Lo que NO hace:
- Reescribir
- Reemplazar
- Eliminar
- Combinar sin permiso

---

## 17. CONSENSO DEL G5 (Consejo de 10 Agentes)

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
- Los 10 votan en decisiones críticas
- Si 7+ están de acuerdo → procede
- Si no hay consenso → escala a MAX
- Veto de MAX siempre gana

---

## 18. AUDITORÍA Y RENDICIÓN DE CUENTAS

### 10 Judges CSA con autoridad absoluta:
1. J1 Comprensión objetivo
2. J2 Cobertura requisitos
3. J3 Consistencia lógica
4. J4 Exactitud técnica
5. J5 Arquitectura y diseño
6. J6 Calidad código
7. J7 Investigación y evidencia
8. J8 Optimización y rendimiento
9. J9 Seguridad y riesgos
10. J10 Calidad final y UX

### 5 Fases por juez:
- F1 Audita input completo
- F2 Busca lo que NADIE revisó
- F3 10 soluciones distintas (conserva mejor)
- F4 Destruye propia solución
- F5 Ataca otros 9 jueces

### Veto:
Cualquier juez puede VETAR → bloquea output → entrega paquete de corrección

---

## 19. COSAS INTOCABLES (Resumen)

NUNCA se modifican:
- 10 Jueces CSA (J1-J10) con 5 fases
- Auditor SID 5 preguntas fijas
- Constitución 39 principios
- 14 categorías BIS
- 30 micro-agentes
- 11 internal roles
- 10 parallel queues
- 10-agent consensus council
- 6 autonomy levels L1-L6
- 12 task models TM01-TM12
- 5 loop versions ALV_LOP_*
- 3 monitors
- 9 GGUF models confirmados
- 16 API keys
- 4 NVIDIA NIM
- 6 Cerebras
- 6 Groq
- 60 datasets (PARCHE-v15)
- 60 adapters (PARCHE-v15)

---

## 20. ESTADO ACTUAL DE MAXBRY SUPER TEAM

### APLICADO:
- ✅ 9 patches OUTPUT v6.1 (propuestas M3)
- ✅ 16 patches OUTPUT v6.1 gobernanza
- ✅ 9 patches INPUT v4.0
- ✅ 15 patches LOOP v6.0
- ✅ 9 propuestas M3 OUTPUT aplicadas
- ✅ 10 propuestas M3 INPUT/LOOP aplicadas
- ✅ 170 patches totales con documentación

### PENDIENTE:
- ⏳ MAX da datos pre-flight
- ⏳ M2.7 instala todo
- ⏳ M3 aprueba cada paso

### RECHAZADO:
- ❌ Output Sandbox (no se creó)

---

## 21. DETALLES DE IMPLEMENTACIÓN

### Sistema de nombres de archivos:
- Cada parche tiene su propio archivo .md
- Formato: PATCH-[CATEGORÍA]-[NÚMERO]-[NOMBRE].md
- Ejemplo: PATCH-OUTPUT-V61-01-pre-mortem.md

### Estructura de carpetas:
- /workspace/nct-proyecto/CONSTITUCION-ORQUESTADOR.md
- /workspace/nct-proyecto/PARCHE-v14 a PARCHE-v17
- /workspace/nct-proyecto/PARCHES-MAXBRY-SUPER-TEAM.md
- /workspace/nct-proyecto/PARCHES-ORQUESTADOR/
- /workspace/nct-proyecto/PATCHES-INPUT-V40/
- /workspace/nct-proyecto/PATCHES-LOOP-V60/
- /workspace/nct-proyecto/PATCHES-OUTPUT-V61/
- /workspace/nct-proyecto/PATCHES-OUTPUT-V61-GOBERNANZA/
- /workspace/nct-proyecto/PATCHES-PROPUESTAS-INPUT-LOOP/
- /workspace/nct-proyecto/PARCHES-INFRA/
- /workspace/nct-proyecto/PARCHES-EXTRAS/
- /workspace/nct-proyecto/CONSOLIDADO-FINAL/  ← nuevos docs consolidados

---

## 22. RESUMEN EJECUTIVO

MAXBRY SUPER TEAM es:
- El orquestador universal distribuido para IA
- Diseñado para 2000+ agentes y 1000+ tareas
- Costo $0 (HF free + API free tiers)
- Sin PC (solo smartphones + iPad)
- Basado en Constitución de 39 principios
- Con CSA 10 jueces con autoridad absoluta
- Con BIS 14 categorías de skills
- Con 30 micro-agentes internos
- Con Loop de 15 capas + 3 ciclos paralelos
- Con Output Engine de 27 componentes
- Con Input Engine de 54 componentes
- Con 9 modelos GGUF + 16 API keys
- 100% trazabilidad con STATE JSON
- Auto-evolución continua
</content>