# MASTER DOCUMENTO 14: MiMoCode + LOP v200
## MAXBRY SUPER TEAM · MiMo Integration · 12 Micro · 8 Propuestas

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. MiMo CODE — ANÁLISIS

### 1.1 Qué es
- MiMo Code = agente de programación para terminal
- MIT, basado en OpenCode
- Equipo MiMo de Xiaomi
- Tareas de horizonte largo (decenas a 200+ pasos)

### 1.2 Tres Pilares Arquitectónicos

| Pilar | Problema | Mecanismos |
|---|---|---|
| **Compute** | Error acumulado | Max Mode, Goal-Stop, Dynamic Workflow |
| **Memory** | Contexto finito | Checkpoint/Rebuild, Writer, 4-tier memory |
| **Evolution** | Sin aprendizaje | Dream, Distill, project memory |

### 1.3 Stack Técnico
- Bun + TypeScript + Effect + SolidJS (TUI) + Tauri (desktop)

### 1.4 7 Loops Internos Identificados

| Loop | Frecuencia | Salida | Persistencia |
|---|---|---|---|
| decision_loop | Cada turno | Tool call o respuesta | Conversación |
| checkpoint_loop | Cada N turnos | Snapshot firmado | state.jsonl |
| writer_loop | Contexto > 70% | Resumen | memory/tier-N.md |
| max_mode_loop | Decisiones críticas | K muestras → voto | Efímero |
| dream_loop | Cada 7 días | Memoria consolidada | memory/dream.md |
| repair_loop | En error | Plan de recuperación | state.jsonl |
| evolution_loop | Al cierre | Skill/proc/prompt nuevo | skills/ |

### 1.5 Benchmark
- SWE-Bench Pro V2: +5%
- Terminal Bench 2: +5%
- Ultra long 200+ steps: beats Claude Code

---

## 2. ADAPTACIONES A NCT (REGLA: NADA LITERAL)

| Componente MiMo | Adaptación NCT v200 |
|---|---|
| Max Mode (multi-sample + voting) | `worker_pool.py` con k_samples |
| Goal-Stop | Nueva fase P9.5 goal-check |
| Dynamic Workflow | ALV_LOP_QUANTUM_FRACTAL_NESTED |
| Checkpoint/Rebuild | state/engine.py con replay_to_checkpoint(t) |
| Writer subagent | MA-RAG-SYNTH |
| 4-tier memory | EROS 3-tier → 4 tiers |
| Dream | Job cron weekly → MA-DREAM |
| Distill | Job cron daily → MA-DISTILL |
| Project memory | state/project_memory.sqlite |

---

## 3. LOP v200 — LIGURE OPERATIONAL PROCEDURE

### 3.1 Qué es
Extensión de LOP (v100) que añade:
- 12 micro-agentes especializados
- 8 nuevas propuestas (PROP-13 a PROP-20)
- Integración MiMo
- Flota HF Spaces

### 3.2 Estructura
```
lop_v200/
├── schemas/           # JSON Schemas
├── micro_agents/      # 12 micro-agentes
├── dsl/               # DSL declarativo
├── pipelines/         # Pipelines de ejecución
├── backends/          # Routers de backends
├── hf_spaces/         # Configuración flota HF
├── seed/              # Pre-análisis
├── research/          # Ciclo de investigación
└── proposals/         # PROP-13 a PROP-20
```

---

## 4. 12 MICRO-AGENTES ESPECIALIZADOS

| ID | Nombre | Input | Output | Tiempo |
|----|--------|-------|--------|--------|
| MA-CODE-GEN | Code Generator | spec.md, stack.json | code.zip + diff.patch | 5-30s |
| MA-CODE-LINT | Linter | code.zip | report.json | 2-10s |
| MA-CODE-TEST | Tester | code.zip, tests/ | junit.xml + coverage.json | 10-60s |
| MA-RAG-SEARCH | Web/GH Search | query, k | chunks.json | 3-15s |
| MA-RAG-SYNTH | Synthesizer | chunks.json | answer.md | 5-20s |
| MA-DOC-WRITE | Doc Writer | artifacts/, audience | doc.md | 5-15s |
| MA-ARCH-PLAN | Architect Planner | requirements.json | arch.yaml | 5-30s |
| MA-VERIFY-3CAPAS | Verifier | artifact, rubric | verdict.json | 10-60s |
| MA-REPAIR-5STEP | Repairer | failure.json | repaired.json | 30-120s |
| MA-RESEARCH-WEB | Web Researcher | urls[], depth | pages.jsonl | 30-300s |
| MA-RESEARCH-GH | GitHub Researcher | query, lang, stars | repos.json | 10-60s |
| MA-EMIT-REPORT | Report Emitter | state.json | report.md + manifest.json | 1-5s |

---

## 5. PATRONES DE ENCADENAMIENTO

### 5.1 Secuencial
```
A → B → C → D
```

### 5.2 DAG Paralelo
```
       ┌─ B ─┐
A ──┬──►     ─► D
     └─ C ──┘
```

### 5.3 Fractal Anidado
```
   ┌─ A ─► B ─┐
   │            ├─► D
   └─ C ─────┘
```

---

## 6. 8 NUEVAS PROPUESTAS (PROP-13 a PROP-20)

### PROP-13 — micro_agents_catalog
Catálogo de 12 micro-agentes especializados.

### PROP-14 — chain_patterns
3 patrones: secuencial, DAG, fractal.

### PROP-15 — seed_pre_analysis
Pipeline de 5 pasos antes de empezar.

### PROP-16 — research_cycle
2-5 rondas de investigación.

### PROP-17 — hf_spaces_fleet
Flota de 10-20 workers HF Spaces.

### PROP-18 — dsl_90_10_budget
90% código / 10% LLM.

### PROP-19 — mimo_integration
Integración selectiva de MiMo.

### PROP-20 — oss_backends_router
Router entre 15 backends OSS.

---

## 7. FLOTA HF SPACES (10-20 WORKERS)

### Composición:

| # | Space | Rol | GPU | Latencia |
|---|-------|-----|-----|----------|
| 1 | FLUX.1-schnell | Imágenes | T4 | 5-15s |
| 2 | Whisper-large-v3 | STT | T4 | 1-5s |
| 3 | OmniParser | Visión UI | A10G | 2-8s |
| 4 | Qwen2-VL-72B | VLM | A100 | 5-20s |
| 5 | gradio/llm-router | LLM | T4 | 2-10s |
| 6 | nct/rag-search | Búsqueda | CPU | 1-3s |
| 7 | nct/code-runner | Ejecución | CPU | 1-5s |
| 8 | nct/lint-fmt | Lint+format | CPU | 0.5-2s |
| 9 | nct/test-runner | Test+coverage | CPU | 5-30s |
| 10 | nct/security-scan | SAST+secrets | CPU | 10-60s |
| 11 | nct/dream | Consolidación | CPU | 60-300s |
| 12 | nct/distill | Destilación | CPU | 60-300s |
| 13-20 | Reservados | Failover | Mixto | Variable |

---

## 8. OPEN SOURCE BACKENDS (15)

| # | Proyecto | Stars | Lenguaje | Modelo default |
|---|----------|-------|----------|----------------|
| 1 | OpenCode | 154.5K | TypeScript | 75+ LLMs |
| 2 | Gemini CLI | 103.1K | TypeScript | Gemini free |
| 3 | OpenHands | 72.6K | Python | Varios |
| 4 | Open Interpreter | 63.4K | Python | Local |
| 5 | Aider | 44.3K | Python | 100+ LLMs |
| 6 | Goose | 43.7K | Rust | Varios |
| 7 | Qwen Code | 24.1K | TypeScript | Qwen3-Coder |
| 8 | Crush | 23.8K | Go | Varios |
| 9 | Kimi CLI | 8.4K | Python | Kimi K2 |
| 10 | Forge Code | 7.2K | Rust | 300+ modelos |
| 11 | MiMo Code | n/a | TypeScript | MiMo-V2.5 |
| 12 | Open Design | n/a | n/a | 16 CLIs |
| 13 | OpenClaw | n/a | n/a | OpenRouter |
| 14 | KiloCode | n/a | TypeScript | Kilo Gateway |
| 15 | Cline | n/a | TypeScript | 100+ |

### Router:
```python
def select_backend(task_type, budget):
    if task_type == "code_generation" and budget == "low":
        return ("opencode", "deepseek-coder")
    elif task_type == "long_horizon" and horizon_h >= 24:
        return ("mimo_code", "mimo-v2.5")
    elif task_type == "research_rag":
        return ("openhands", "qwen3-coder")
    elif task_type == "ui_design":
        return ("open_design", "sonnet-4.6")
    else:
        return ("goose", "claude-sonnet-4.6")
```

---

## 9. EJEMPLO COMPLETO: E-COMMERCE MICROSERVICE

```yaml
chain:
  id: ecommerce_microservice_v1
  pattern: dag
  level: L4_SUPERVISED_AUTONOMOUS
  budget: { max_tokens: 2_000_000, max_runtime_h: 24 }
  steps:
    - { id: MA-ARCH-PLAN,    parallel_group: g1 }
    - { id: MA-RESEARCH-WEB, parallel_group: g1 }
    - { id: MA-RESEARCH-GH,  parallel_group: g1 }
    - { id: MA-RAG-SYNTH,    parallel_group: g2 }
    - { id: MA-CODE-GEN,     parallel_group: g3 }
    - { id: MA-CODE-LINT,    parallel_group: g4 }
    - { id: MA-CODE-TEST,    parallel_group: g4 }
    - { id: MA-VERIFY-3CAPAS, parallel_group: g5 }
    - { id: MA-DOC-WRITE,    parallel_group: g5 }
    - { id: MA-EMIT-REPORT,  parallel_group: g6 }
  monitor: { pad: true, anxiety: true, drift: true }
  repair:  { pipeline: 5_steps, max_retries: 3 }
```

---

## 10. CONCLUSIÓN

LOP v200 añade:
- 12 micro-agentes especializados
- 3 patrones de encadenamiento
- 5 pasos de pre-análisis
- 2-5 rondas de research
- 10-20 workers HF Spaces
- Router de 15 backends OSS
- 8 nuevas propuestas (PROP-13 a PROP-20)
- Integración selectiva MiMo

Una extensión poderosa del LOP v100 original.
</content>