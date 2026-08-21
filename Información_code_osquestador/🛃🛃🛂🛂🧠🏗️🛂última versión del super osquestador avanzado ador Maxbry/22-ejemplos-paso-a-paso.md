# MASTER DOCUMENTO 22: EJEMPLOS COMPLETOS PASO A PASO
## MAXBRY SUPER TEAM · E-Commerce · SaaS API · Contratos YAML

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. EJEMPLO 1: CREAR MICROSERVICIO E-COMMERCE

### 1.1 Spec de MAX
"Necesito un microservicio para gestionar productos y stock de una tienda online. Con REST API, JWT auth y deploy en HF Spaces."

### 1.2 SID (5 Preguntas)

**Q1 — Qué es:**
"Microservicio REST para gestión de productos y stock con autenticación JWT."

**Q2 — Para quién:**
"Desarrolladores de e-commerce que necesitan backend simple para tienda online pequeña/mediana."

**Q3 — Qué problema resuelve:**
"Crear un backend desde cero toma 2-4 semanas. Este microservicio lo entrega en 24 horas con todas las features básicas."

**Q4 — Cómo se usa:**
"1. POST /auth/register → crear usuario
2. POST /auth/login → JWT
3. POST /products (con JWT) → crear producto
4. GET /products → listar
5. PUT /products/{id}/stock → actualizar stock
6. GET /products/{id} → ver detalle"

**Q5 — Qué NO es:**
"NO es un marketplace completo
NO incluye pasarela de pago
NO incluye UI web
NO procesa imágenes
NO escala a millones de productos"

**Score:** 96/100 → APROBADO

### 1.3 BIS Lookup

Categorías relevantes:
- H (APIs)
- D (Backend)
- G (Bases de datos)
- L (Seguridad)
- K (Testing)

Skills seleccionadas: 6

### 1.4 Plan Generado

```yaml
plan:
  id: plan-ecommerce-001
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  steps:
    - id: research
      parallel_group: g1
      agents: [MA-RESEARCH-WEB, MA-RESEARCH-GH]
    - id: architecture
      parallel_group: g1
      agent: MA-ARCH-PLAN
    - id: synth
      parallel_group: g2
      agent: MA-RAG-SYNTH
      input_from: g1
    - id: code
      parallel_group: g3
      agent: MA-CODE-GEN
      input_from: g2
    - id: lint
      parallel_group: g4
      agent: MA-CODE-LINT
      input_from: g3
    - id: test
      parallel_group: g4
      agent: MA-CODE-TEST
      input_from: g3
    - id: verify
      parallel_group: g5
      agent: MA-VERIFY-3CAPAS
      input_from: g4
    - id: doc
      parallel_group: g5
      agent: MA-DOC-WRITE
      input_from: g3
    - id: deliver
      parallel_group: g6
      agent: MA-EMIT-REPORT
      input_from: g5
```

### 1.5 Ejecución

**Duración:** 18h 23min
**Tokens:** 1.2M
**Resultado:** PASS (CSA score 96/100)

### 1.6 Outputs

- Código: 8 archivos Python
- Tests: 24 unit tests + 8 integration
- Docs: README.md + ARCHITECTURE.md
- Deploy: HF Space "mavis/ecommerce-microservice"

---

## 2. EJEMPLO 2: SAAS API MULTI-TENANT

### 2.1 Spec de MAX
"Diseña, implementa, testea y documenta una API REST multi-tenant para una SaaS de gestión de tareas con autenticación JWT, rate limiting y auditoría, lista para producción en 24h."

### 2.2 SID

**Q1:** "API REST multi-tenant para SaaS de gestión de tareas"
**Q2:** "Equipos de 5-50 personas"
**Q3:** "SaaS comerciales cuestan $500+/mes; alternativa económica con control"
**Q4:** "1. POST /tenants → crear tenant
        2. POST /auth → JWT
        3. POST /tasks → crear tarea
        4. GET /tasks → listar
        5. Rate limit 1000 req/h
        6. Audit log de todo"
**Q5:** "NO es para >1000 usuarios
        NO incluye UI web
        NO reemplaza Jira"

**Score:** 97/100 → APROBADO

### 2.3 Pipeline Completo

```yaml
chain:
  id: saas_tasks_api_v1
  pattern: dag
  level: L5_CONTINUOUS_AUTONOMOUS_72H_PLUS
  budget: { max_tokens: 5_000_000, max_runtime_h: 24 }
  
  research:
    sources:
      web:
        - "owasp jwt"
        - "fastapi multi-tenant"
        - "rate limit algorithms"
      github:
        - "fastapi-template stars:>1000"
        - "awesome-saas"
    rounds: { min: 2, max: 4 }
  
  steps:
    - { id: MA-ARCH-PLAN,     parallel_group: g1 }
    - { id: MA-RESEARCH-WEB,  parallel_group: g1 }
    - { id: MA-RESEARCH-GH,   parallel_group: g1 }
    - { id: MA-RAG-SYNTH,     parallel_group: g2 }
    - { id: MA-CODE-GEN,      parallel_group: g3 }
    - { id: MA-CODE-LINT,     parallel_group: g4 }
    - { id: MA-CODE-TEST,     parallel_group: g4 }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5 }
    - { id: MA-DOC-WRITE,     parallel_group: g5 }
    - { id: MA-EMIT-REPORT,   parallel_group: g6 }
  
  monitor: { pad: true, anxiety: true, drift: true }
  repair:  { pipeline: 5_steps, max_retries: 3 }
  hf_fleet: { min_workers: 10, max_workers: 20 }
```

### 2.4 Diagrama

```
                ┌─ MA-ARCH-PLAN ────┐
                │                    │
g1 ─────────────►├─ MA-RESEARCH-WEB ─┤
                │                    ├─► MA-RAG-SYNTH
                └─ MA-RESEARCH-GH ──┘                │
                                                   ▼
                                            MA-CODE-GEN
                                                   │
                ┌─ MA-CODE-LINT ───┐                │
                │                    ├─► MA-VERIFY-3CAPAS
g4 ─────────────►├─ MA-CODE-TEST ───┤                │
                │                    │                ▼
                └────────────────────┘         MA-DOC-WRITE
                                                   │
                                                   ▼
                                            MA-EMIT-REPORT
```

### 2.5 Resultado

- **Duración:** 22h 47min
- **Tests:** 47 unit + 12 integration + 8 E2E
- **Coverage:** 87%
- **CSA Score:** 97/100
- **Output:** Listo para producción

---

## 3. CONTRATOS YAML (EJEMPLOS)

### 3.1 Contrato de Skill

```yaml
skill_contract:
  skill_id: code_generator
  version: 1.2.0
  category: J-IA
  interface:
    inputs:
      - name: spec
        type: string
        required: true
      - name: stack
        type: object
        required: true
      - name: constraints
        type: array
        required: false
    outputs:
      - name: code
        type: file
        format: zip
      - name: diff
        type: file
        format: patch
  capabilities:
    - code_generation
    - multi_language
  limits:
    max_tokens: 50000
    max_runtime_s: 120
    max_files: 50
  dependencies:
    - arch_planner
    - rag_search
  tests:
    unit: 5
    integration: 2
    coverage: 85%
  owner: g5-orquestador
  license: MIT
```

### 3.2 Contrato de Agente

```yaml
agent_contract:
  agent_id: MA-VERIFY-3CAPAS
  type: deterministic_with_llm_fallback
  budget:
    code_pct: 90
    llm_pct: 10
    max_tokens: 50_000
  inputs: { artifact: object, rubric: object }
  outputs: { decision: enum, issues: array }
  code_steps:
    - parse_artifact
    - schema_validate
    - cap1_adversarial
    - cap2_cruzada
    - cap3_maker_checker
  llm_steps:
    - when: "any(cap.issues)"
      call: llm_adversarial_review
      max_tokens: 4_000
      temperature: 0.0
```

### 3.3 Contrato de Pipeline

```yaml
pipeline_contract:
  pipeline_id: ecommerce_v1
  version: 1.0.0
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget:
    max_tokens: 2_000_000
    max_runtime_h: 24
  steps: [ ... ]
  consensus: required
  audit: full_csa
  delivery:
    targets: [github, hf_space, telegram]
    format: adaptive
```

---

## 4. ÁRBOL DE ENTREGA NCT COORDINATOR

```
NCT
├── Coordinator (nct_coordinator.py)
│   ├── Modes (nct_modes.py)
│   │   ├── Manual
│   │   ├── Semi-automático
│   │   └── Continuo
│   │
│   ├── Flows (nct_flows.py)
│   │   ├── Flow F0-F9
│   │   └── Custom flows
│   │
│   └── Phases (nct_phases.py)
│       ├── Phase 0 (Pre-Boot)
│       ├── Phase 0.5 (Confirmation)
│       └── Phase 1-9
│
├── Core
│   ├── Inputs (nct_inputs.py) → Input Engine v4.0
│   ├── Outputs (nct_outputs.py) → Output Engine + OOS
│   ├── State (nct_state.py) → state.json
│   └── Memory (nct_memory.py) → 4-tier memory
│
├── Skills (nct_skills.py) → BIS
│   ├── 14 categorías
│   ├── 13 criterios
│   └── Debate 4 especialistas
│
├── Agents (nct_agents.py)
│   ├── 30 micro-agentes
│   ├── 11 internal roles
│   └── 10-agent council
│
├── Audit (nct_audit.py) → CSA
│   ├── 10 Jueces
│   └── 5 Fases
│
├── Metrics (nct_metrics.py)
│   ├── PAD
│   ├── Anxiety
│   └── Drift
│
└── Delivery (nct_delivery.py)
    ├── 23 destinos
    └── Adaptive format
```

---

## 5. MAPA FUSIÓN FINAL

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  MAX ────► MAXBRY SUPER TEAM                            │
│                │                                         │
│                ├──► SID (5 preguntas)                    │
│                ├──► BIS (skills lookup)                  │
│                ├──► Plan generation                      │
│                ├──► Consensus (10 agentes)               │
│                ├──► Execution (30 micro-agentes)         │
│                ├──► CSA audit (10 jueces)                │
│                ├──► Output Engine                        │
│                ├──► Multi-target delivery               │
│                └──► Feedback loop                        │
│                                                          │
│  G6 ASISTENTES ────► 9 GGUF + 16 API keys              │
│  G1-G4 INFRA/CORE/UI/AUDIT ────► Workers                │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 6. CONCLUSIÓN

Los ejemplos paso a paso muestran cómo MAXBRY SUPER TEAM ejecuta tareas reales:
- E-commerce microservice (8 archivos Python)
- SaaS API multi-tenant (production-ready)
- Contratos YAML estructurados
- Árbol de entrega NCT Coordinator
- Mapa de fusión final

Cada ejemplo demuestra el flujo completo desde SID hasta delivery.
</content>