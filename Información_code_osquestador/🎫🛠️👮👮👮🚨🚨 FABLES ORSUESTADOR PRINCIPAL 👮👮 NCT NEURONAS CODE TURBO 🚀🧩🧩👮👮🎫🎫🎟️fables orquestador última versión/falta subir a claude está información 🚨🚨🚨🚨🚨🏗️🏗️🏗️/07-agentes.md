# DOCUMENTO 7: AGENTES DEL ORQUESTADOR
## Extraído del historial del chat

---

## 1. 5 AGENTES DEL CONSENSO (APX-C)

5 agentes especializados para decisiones de diseño, arquitectura o estrategia.
NO se usa para tareas mecánicas (mover archivos, generar strings, hacer commits).

### Por qué 5 agentes (no 3, no 7):
- 3 agentes → empates frecuentes, ningún "voto de calidad"
- 5 agentes → quorum natural, diversidad, desempate fácil
- 7 agentes → overhead alto sin ganancia proporcional
- 5 agentes especializados >> 5 agentes genéricos

### Los 5 Agentes:

#### 1. CREATIVE AGENT
- **Misión:** generar el mayor número posible de ideas, sin filtro
- **Personalidad:** explorador, divergente, sin miedo a lo absurdo
- **Input:** el problema del usuario (1 párrafo)
- **Output:** 5-10 ideas con nombre, descripción, riesgo
- **Modelo:** uno creativo (Claude Opus, GPT-4)
- **Temperature:** 0.9
- **Tokens:** ~2000

#### 2. INNOVATION AGENT
- **Misión:** tomar cada idea del Creative y mejorarla
- **Personalidad:** iterador, "qué pasaría si…"
- **Input:** las ideas del Creative + el problema original
- **Output:** cada idea mejorada con versión evolucionada, variantes, pros/contras, score
- **Modelo:** el más fuerte disponible
- **Temperature:** 0.7
- **Tokens:** ~3000

#### 3. CRITIC AGENT
- **Misión:** destruir todo lo débil. Adversarial por diseño
- **Personalidad:** escéptico, riguroso, sin piedad
- **Input:** las ideas del Innovation
- **Output:** para cada idea: 3 puntos débiles, 2 riesgos no considerados, score, recomendación
- **Modelo:** uno diferente al Creative (diversidad)
- **Temperature:** 0.3
- **Tokens:** ~2500

#### 4. SELECTION AGENT
- **Misión:** elegir la mejor superviviente (o combinación)
- **Personalidad:** decisor, sintetizador
- **Input:** ideas del Innovation + scores del Critic
- **Output:** Ganadora, Runner-up, Justificación, Score final
- **Regla:** si score < 0.6, no hay consenso → escala al usuario
- **Modelo:** el más fuerte disponible
- **Temperature:** 0.2
- **Tokens:** ~2000

#### 5. ARCHITECTURE AGENT
- **Misión:** convertir la idea ganadora en un plano ejecutable
- **Personalidad:** arquitecto, sistemático
- **Input:** ganadora + problema original
- **Output:** Stack recomendado, Fichas del DSL a crear/modificar, Talleres involucrados, Estimación de esfuerzo, Riesgos técnicos, Primer paso concreto
- **Modelo:** uno fuerte de código
- **Temperature:** 0.3
- **Tokens:** ~3000

### Flujo Completo:
```
USUARIO / M3
   ↓
[1] CREATIVE AGENT       → "Propongo ideas, sin filtro"
   ↓
[2] INNOVATION AGENT     → "Mejoro cada idea hasta su mejor versión"
   ↓
[3] CRITIC AGENT         → "Destruyo lo débil, sin piedad"
   ↓
[4] SELECTION AGENT      → "Elijo la mejor superviviente"
   ↓
[5] ARCHITECTURE AGENT   → "Convierto la elegida en plano ejecutable"
   ↓
RESULTADO al usuario
```

### Reglas Duras:

**Cuándo SÍ se usa consenso:**
- Decisiones de arquitectura
- Decisiones de UX
- Decisiones de producto
- Decisiones de seguridad
- Naming, branding, propuesta de valor

**Cuándo NO se usa consenso:**
- Tareas mecánicas (mover archivos, generar strings)
- Tests automatizados
- Commits y deploys
- Consultas a base de datos
- Cualquier cosa 100% determinista

**Cuándo se ESCALA al usuario:**
- Empate entre opciones
- Score de la ganadora < 0.6
- El consenso pide recursos fuera del presupuesto
- El consenso contradice decisión ya aprobada

### Prompt DSL Cerrado:
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

## 2. 5 AGENTES DE INVESTIGACIÓN (Multi-source)

5 agentes que investigan en paralelo desde diferentes fuentes.

### 1. GitHub Agent
**Qué busca:**
- Repos públicos relevantes
- Stars, forks, issues
- Patrones de uso
- Código de referencia
- Proyectos similares

**Outputs:**
- Lista de repos con metadata
- Análisis de calidad
- Código reutilizable
- Issues recurrentes

### 2. HuggingFace Agent
**Qué busca:**
- Modelos GGUF disponibles
- Datasets relevantes
- Spaces con código útil
- Papers referenciados
- Versiones y updates

**Outputs:**
- Lista de modelos con URLs
- Datasets descargables
- Código de Spaces
- Estado de las APIs

### 3. Web Agent
**Qué busca:**
- Documentación oficial
- Artículos técnicos
- Tutoriales
- Best practices
- Comparativas
- Precios/costos

**Outputs:**
- URLs relevantes
- Resúmenes
- Comparativas
- Recomendaciones

### 4. YouTube Agent
**Qué busca:**
- Tutoriales paso a paso
- Demos de productos
- Conferencias técnicas
- Comparativas visuales
- Casos de estudio

**Outputs:**
- URLs de videos
- Transcripciones relevantes
- Timestamp de momentos clave
- Resúmenes visuales

### 5. MCP Agent
**Qué busca:**
- MCP servers disponibles
- Tools registrados
- Integraciones oficiales
- Smithery catálogo
- Composio integraciones

**Outputs:**
- Lista de MCP servers
- Tools utilizables
- Compatibilidad
- Configuración necesaria

---

## 3. 12 MICRO-AGENTES ESPECIALIZADOS (de MiMo/Lop v200)

12 micro-agentes especializados, cada uno ≤200 LOC de núcleo.

| ID | Nombre | Responsabilidad |
|---|---|---|
| MA-CODE-GEN | Code Generator | Genera código a partir de spec |
| MA-CODE-LINT | Linter | Lint + format + type-check |
| MA-CODE-TEST | Tester | Unit + integration + mutation |
| MA-RAG-SEARCH | Web/GH Search | Búsqueda vectorial + rerank |
| MA-RAG-SYNTH | Synthesizer | Sintetiza respuesta con citas |
| MA-DOC-WRITE | Doc Writer | Documenta arquitectura/decisiones |
| MA-ARCH-PLAN | Architect Planner | Planifica arquitectura y stack |
| MA-VERIFY-3CAPAS | Verifier | Verificación adversarial 3 capas |
| MA-REPAIR-5STEP | Repairer | Pipeline 5 pasos de reparación |
| MA-RESEARCH-WEB | Web Researcher | Crawling + extracción |
| MA-RESEARCH-GH | GitHub Researcher | Búsqueda en GitHub via API |
| MA-EMIT-REPORT | Report Emitter | Empaqueta resultado final |

### Diseño:
- Una sola responsabilidad
- Un solo input_schema
- Un solo output_schema
- Estado efímero
- Muerte tras emitir el JSON

---

## 4. 10 PROPUESTAS DE AGENTES M3 PARA INPUT/LOOP

1. **Meta-agentes que crean otros agentes** ✅
2. **Causalidad (no correlación)** ✅
3. **Counterfactual reasoning** (qué habría pasado) ✅
4. **Auto-modificación de código** ✅
5. **Memoria Episódica** ✅
6. **Zero-shot transfer entre proyectos** ✅
7. **Neural Architecture Search (NAS)** ✅
8. **Time-travel debugging** ✅
9. **Inteligencia colectiva emergente** ✅
10. **Auto-curriculum** ✅

---

## 5. 9 PROPUESTAS DE AGENTES M3 PARA OUTPUT (9 APLICADAS + 1 RECHAZADA)

1. **Pre-Mortem Analysis** ✅
2. **Output Sandbox** ❌ RECHAZADO POR MAX
3. **Auto-Rollback Inteligente** ✅
4. **Meta-Learning entre Releases** ✅
5. **Output Personalization** ✅
6. **Multi-Stakeholder Output** ✅
7. **Causal Output Tracing** ✅
8. **Output Marketplace Interno** ✅
9. **Self-Improving Output Quality** ✅
10. **Production Monitoring Post-Publish** ✅

---

## 6. HALLAZGOS DE INVESTIGACIÓN (REFERENCIAS APROBADAS)

Proyectos open source identificados como referencia:

### Tier S+ (Excelentes):
- **OpenCode** (154.5K stars) - 75+ LLMs, MCP-first
- **Gemini CLI** (103.1K stars) - Gemini free
- **OpenHands** (72.6K stars) - Python, multi-agente
- **Open Interpreter** (63.4K stars) - Local
- **Aider** (44.3K stars) - 100+ LLMs
- **Goose** (43.7K stars) - MCP-first

### Tier A (Muy buenos):
- **Qwen Code** (24.1K stars) - Qwen3-Coder
- **Crush** (23.8K stars) - Go
- **Kimi CLI** (8.4K stars) - Kimi K2
- **Forge Code** (7.2K stars) - 300+ modelos
- **MiMo Code** - Xiaomi MiMo, MIT, +5% vs Claude Code

### Tier B:
- **BLXCode**, **Open Design**, **OpenClaw**, **KiloCode**, **Cline**, **BLACKBOX.AI**

### Frameworks de agentes:
- **LangGraph** (115K stars) - State machine
- **CrewAI** (102K stars) - Crew + roles
- **OpenAI Agents SDK** - Framework oficial
- **LlamaIndex** - RAG
- **Mem0** - Memoria
- **LangMem** - Memoria largo plazo
- **AutoGen** - Multi-agente Microsoft
- **DSPy** - Prompt optimization
- **Haystack** - NLP pipelines
- **Microsoft Agent Framework (MAF)** - Production-ready
- **AgentOrchestra** - Jerárquico, 83.39% GAIA

### Workflow:
- **Temporal**, **Kestra**, **Airflow**, **Dagster**, **Prefect**, **Argo Workflows**

### MCP / Integración:
- **MCP** (Model Context Protocol)
- **Smithery** (catálogo MCP)
- **Composio** (integraciones)

### Investigación específica:
- **DeerFlow 2.0** (ByteDance, 46K stars) - Super Agent Harness con memory, sandboxes, skills, message gateway
- **LiteLLM** - Unifica 100+ LLMs en 1 API
- **Hermes Agent** (149K stars) - Learning loop L1+L2+L3
- **OpenCLAW** (308K stars) - Gateway + channels + skills + MCP

---

## 7. 10 JUECES DEL CSA (CONSEJO SUPREMO DE AUDITORÍA)

10 jueces con autoridad absoluta sobre TODA decisión. Cada uno con 5 fases.

### Los 10 Jueces:
1. **J1 Comprensión objetivo** - ¿El output realmente entiende QUÉ se pidió?
2. **J2 Cobertura requisitos** - ¿Todos los requisitos están cubiertos?
3. **J3 Consistencia lógica** - ¿El output es lógicamente coherente?
4. **J4 Exactitud técnica** - ¿El output es técnicamente correcto?
5. **J5 Arquitectura y diseño** - ¿El diseño es correcto y mantenible?
6. **J6 Calidad código** - ¿El código sigue buenas prácticas?
7. **J7 Investigación y evidencia** - ¿Las afirmaciones tienen respaldo?
8. **J8 Optimización y rendimiento** - ¿El output es eficiente?
9. **J9 Seguridad y riesgos** - ¿El output es seguro?
10. **J10 Calidad final y UX** - ¿El output es usable y de calidad?

### 5 FASES por cada juez:
- F1 · Audita input completo
- F2 · Busca lo que NADIE revisó
- F3 · 10 soluciones distintas
- F4 · Destruye propia solución
- F5 · Ataca otros 9 jueces

---

## 8. 10 AGENTES DEL CONSEJO DE CONSENSO

10 agentes que votan en decisiones críticas:
1. Voto Técnico
2. Voto de Negocio
3. Voto de Costos
4. Voto de Riesgos
5. Voto Ético
6. Voto de UX
7. Voto de Performance
8. Voto de Seguridad
9. Voto de Compatibilidad
10. Veto de MAX (decisión final)

---

## 9. 5 OFFICERS DEL EXECUTIVE BOARD

3-5 agentes que supervisan el funcionamiento global:
1. COO (Chief Operations Officer) - Eficiencia, performance
2. CFO (Chief Financial Officer) - Costos, presupuesto
3. CQO (Chief Quality Officer) - Calidad global
4. CRO (Chief Risk Officer) - Riesgos, alertas
5. CLO (Chief Learning Officer) - Aprendizaje, evolución

---

## 10. 10 CALIDADES DEL AGENTE IDEAL (MAXBRY)

```
- Calidad
- Robustez
- Recuperación
- Persistencia
- Escalabilidad
- Auditoría
- Control
- Evolución futura
- (NO para velocidad)
- (NO para simplicidad)
```
</content>