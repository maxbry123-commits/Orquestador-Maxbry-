# MASTER DOCUMENTO 21: SUBSISTEMAS DETALLADOS
## MAXBRY SUPER TEAM · Mythos 15 Secciones · Skills 13 Criterios · Universal Plug · M3+Kimi

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. SYSTEM PROMPT MYTHOS (15 SECCIONES)

### 1.1 Sección 1 — Identidad
"MAXBRY SUPER TEAM es el orquestador universal distribuido para IA."

### 1.2 Sección 2 — Misión
"Coordinar agentes, herramientas, proyectos y objetivos para MAX."

### 1.3 Sección 3 — Valores
- Determinismo
- Trazabilidad
- Resiliencia
- Auto-mejora
- Costo $0

### 1.4 Sección 4 — Principios
Lista los 39 principios de la Constitución.

### 1.5 Sección 5 — Arquitectura
Descripción de las capas:
- USUARIO
- MAXBRY
- Control Layer
- Workflow Layer
- Memory Layer
- Tool Layer
- LLM Layer

### 1.6 Sección 6 — Capacidades
- 2000+ agentes
- 1000+ tareas
- Multi-modelo
- Auto-evolución

### 1.7 Sección 7 — Límites
- Costo $0
- HF free tier
- 16GB RAM por Space

### 1.8 Sección 8 — Interacción
- Telegram
- API REST
- Dashboard
- CLI

### 1.9 Sección 9 — Outputs
- 23 destinos
- Adaptive format
- Multi-target

### 1.10 Sección 10 — Validación
- 5 GOALS + 12 PASOS
- Confidence Scoring ≥ 95%
- CSA audit

### 1.11 Sección 11 — Seguridad
- Secretos encriptados
- Audit log
- OWASP compliance

### 1.12 Sección 12 — Operación
- 90% código / 10% LLM
- Multi-modelo
- 3 perfiles API

### 1.13 Sección 13 — Aprendizaje
- Meta-Learning
- Self-Improving
- Counterfactual reasoning

### 1.14 Sección 14 — Reporte
- Estado
- Métricas
- Alertas

### 1.15 Sección 15 — Cierre
"Reporto a MAX. Escala a MAX si es crítico."

---

## 2. SKILLS SYSTEM — 13 CRITERIOS INDIVIDUALES

### Criterio 1 — Nombre Claro
- Identifica la skill
- Patrón: snake_case
- Ejemplo: `code_generator`

### Criterio 2 — Descripción Concisa
- 1-2 oraciones
- Qué hace, no cómo

### Criterio 3 — Categoría Válida
- Una de A-N (BIS)

### Criterio 4 — Inputs Tipados
- Schema JSON
- Required vs optional

### Criterio 5 — Outputs Tipados
- Schema JSON
- Siempre definido

### Criterio 6 — Tiempo Medio
- Estimación realista
- p50, p95, p99

### Criterio 7 — Recursos
- CPU/RAM/disk
- Modelo si requiere LLM

### Criterio 8 — Dependencias
- Skills que requiere
- Versiones

### Criterio 9 — Tests
- Mínimo 3 unit tests
- Coverage ≥ 80%

### Criterio 10 — Documentación
- README.md
- Ejemplos

### Criterio 11 — Ejemplos
- Mínimo 2 ejemplos
- Real-world use cases

### Criterio 12 — Versión Semver
- MAJOR.MINOR.PATCH
- Ejemplo: 1.2.3

### Criterio 13 — Mantenedor
- Owner asignado
- Contacto

---

## 3. SKILLS DEBATE — 4 ESPECIALISTAS

### 3.1 Arquitecto
**Pregunta:** ¿Es coherente con la arquitectura?

### 3.2 Implementador
**Pregunta:** ¿Es implementable con recursos actuales?

### 3.3 Tester
**Pregunta:** ¿Es testeable? ¿Cómo se prueba?

### 3.4 Crítico
**Pregunta:** ¿Vale la pena el costo/beneficio?

### Voto:
- 4-0 → Skill excelente
- 3-1 → Skill aprobada con notas
- 2-2 → Escala a MAX
- 1-3 → Skill rechazada
- 0-4 → Skill prohibida

---

## 4. MULTI-SOURCE INVESTIGATION (5 AGENTES)

### 4.1 GitHub Researcher
```yaml
agent: github_researcher
sources:
  - github.com (repos)
  - github API
queries:
  - awesome-{topic}
  - {topic} stars:>1000
outputs:
  - repos.json
  - stars, issues, PRs
```

### 4.2 HuggingFace Researcher
```yaml
agent: hf_researcher
sources:
  - huggingface.co (models, datasets, spaces)
queries:
  - {topic} (model, dataset, space)
outputs:
  - models.json
  - downloads, likes
```

### 4.3 Web Researcher
```yaml
agent: web_researcher
sources:
  - Wikipedia
  - MDN
  - OWASP
  - Documentación oficial
  - arXiv
queries:
  - {topic} best practices
  - {topic} documentation
outputs:
  - pages.jsonl
```

### 4.4 YouTube Researcher
```yaml
agent: youtube_researcher
sources:
  - YouTube (técnicos)
queries:
  - {topic} tutorial
  - {topic} conference talk
outputs:
  - videos.json
  - transcripts
```

### 4.5 MCP Researcher
```yaml
agent: mcp_researcher
sources:
  - mcp servers
  - smithery
  - Composio
queries:
  - {topic} mcp server
outputs:
  - mcp_servers.json
```

---

## 5. UNIVERSAL PLUG v1.5 (DETALLE)

### 5.1 Propósito
Conector universal entre módulos.

### 5.2 Componentes

```yaml
universal_plug:
  version: 1.5
  interface: MCP
  transport:
    - stdio
    - http
    - mcp
  
  input_schema: nct.task.v1.json
  output_schema: nct.result.v1.json
  
  auth:
    type: byok_or_proxy
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
  
  capabilities:
    - code_generation
    - web_search
    - rag_query
    - file_read
    - file_write
    - api_call
    - test_run
    - deploy
```

### 5.3 Nexus
Punto central de conexión entre módulos.
- Descubre módulos disponibles
- Registra capabilities
- Enruta requests
- Monitorea health

---

## 6. M3 + KIMI DIVISIÓN

### 6.1 M3 (JEFE)
- **Función:** Arquitecto
- **Trabaja con:** MAX directamente
- **Decide:** QUÉ hacer
- **NO ejecuta:** código directo
- **Entrega:** Plan + validación

### 6.2 Kimi K2.7-Code (EMPLEADO)
- **Función:** Implementador
- **Trabaja para:** M3
- **Decide:** CÓMO hacerlo
- **SÍ ejecuta:** código
- **Entrega:** Implementación + tests

### 6.3 Flujo
```
MAX → M3 (jefe)
       ↓ (planifica)
       Kimi (implementa)
       ↓ (reporta)
       M3 (valida)
       ↓ (presenta)
       MAX (aprueba)
```

---

## 7. FUSIÓN KIMI + MINIMAX

### 7.1 Punto de fusión
Donde M3 (chat architect) se encuentra con Kimi (ejecutor).

### 7.2 Protocolo
```yaml
fusion_protocol:
  input: spec from M3
  output: implementation from Kimi
  handoff:
    M3 → Kimi: plan + acceptance criteria
    Kimi → M3: implementation + tests
  validation:
    M3 validates against acceptance criteria
  feedback:
    M3 → Kimi: corrections if needed
```

### 7.3 Garantías
- M3 nunca ejecuta código directo
- Kimi nunca habla con MAX
- Handoff siempre con schemas

---

## 8. NCT COORDINATOR — 13 ARCHIVOS (DETALLE)

### 8.1 `nct_coordinator.py`
Coordinador principal. Inicializa el sistema.

### 8.2 `nct_modes.py`
Selector de modo (Manual/Semi/Continuo).

### 8.3 `nct_flows.py`
Definición de flujos continuos.

### 8.4 `nct_phases.py`
Implementación de F0-F9.

### 8.5 `nct_inputs.py`
Recepción y procesamiento de inputs.

### 8.6 `nct_outputs.py`
Generación y entrega de outputs.

### 8.7 `nct_state.py`
Estado global (state.json).

### 8.8 `nct_memory.py`
Sistema de memoria (4-tier).

### 8.9 `nct_skills.py`
Integración con BIS.

### 8.10 `nct_agents.py`
Gestión de agentes.

### 8.11 `nct_audit.py`
Integración con CSA.

### 8.12 `nct_metrics.py`
Recolección de métricas.

### 8.13 `nct_delivery.py`
Multi-target delivery.

---

## 9. SELECTOR DE MODOS (UI)

```
┌─────────────────────────────────────┐
│      NCT — SELECCIÓN DE MODO        │
├─────────────────────────────────────┤
│                                     │
│  1. Manual                          │
│     • Cada paso requiere aprobación │
│                                     │
│  2. Semi-automático                 │
│     • Sistema propone, MAX aprueba  │
│                                     │
│  3. Continuo (NCT)                  │
│     • Coordinación automática       │
│     • Tareas largas (24h+)          │
│                                     │
│  Selecciona modo [1/2/3]: ___       │
└─────────────────────────────────────┘
```

---

## 10. CONCLUSIÓN

Los subsistemas principales están completamente detallados:
- System Prompt Mythos (15 secciones)
- Skills System (13 criterios + debate 4)
- Multi-source investigation (5 agentes)
- Universal Plug v1.5
- M3 + Kimi división
- Fusión Kimi + MiniMax
- NCT Coordinator (13 archivos)
- Selector de modos
</content>