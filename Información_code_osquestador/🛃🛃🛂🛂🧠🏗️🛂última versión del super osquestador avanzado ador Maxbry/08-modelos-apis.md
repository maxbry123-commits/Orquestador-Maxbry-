# DOCUMENTO 8: MODELOS GGUF Y APIs
## Extraído del historial del chat

---

## 1. 9 MODELOS GGUF CONFIRMADOS

| # | Modelo | Autor | Parámetros | Notas |
|---|--------|-------|------------|-------|
| 1 | **HRM-Text-1B** | Sapient Inc. | 1B | Tamaño GGUF: 0.6GB. Paper: arxiv 2504.12345 |
| 2 | **Qwen2.5-Coder-1.5B** | Alibaba | 1.5B | Code specialist |
| 3 | **Granite-4.1-3B** | IBM | 3B | General |
| 4 | **Granite-3.2-2B** | IBM | 2B | Bajo consumo |
| 5 | **LFM2.5-1.2B-Thinking** | Liquid | 1.2B | Modo Thinking (razonamiento explícito) |
| 6 | **Gemma-4-E4B** | Google | MoE 4B | Backup de alto rendimiento |
| 7 | **Gemma-4-E2B** | Google | MoE 2B | Bajo consumo MoE |
| 8 | **GPT-OSS-20B** | OpenAI | 21B total / 3.6B active | MXFP4 |
| 9 | **Nemotron-3-Nano-4B** | NVIDIA | 4B | Integración NVIDIA NIM |

### HF References:
- HRM-Text-1B: `sapientinc/HRM-Text-1B`
- GPT-OSS-20B: `openai/gpt-oss-20b`

---

## 2. USO RECOMENDADO POR MODELO

### HRM-Text-1B
- Razonamiento profundo
- Análisis complejo
- Tareas que requieren pensar

### Qwen2.5-Coder-1.5B
- Generación de código
- Code review
- Refactoring
- Debugging

### Granite-4.1-3B
- Tareas generales
- Balance rendimiento/costo
- Producción

### Granite-3.2-2B
- Bajo consumo
- Tareas simples
- Inferencia rápida

### LFM2.5-1.2B-Thinking
- Razonamiento explícito
- Mostrar pasos de pensamiento
- Decisiones que requieren transparencia

### Gemma-4-E4B
- Tareas multimodales
- Razonamiento general
- Backup de alto rendimiento

### Gemma-4-E2B
- Bajo consumo
- Tareas MoE ligeras
- Inferencia eficiente

### GPT-OSS-20B MXFP4
- Tareas críticas
- Máxima calidad
- Cuando se necesita el mejor modelo disponible

### Nemotron-3-Nano-4B
- Integración NVIDIA NIM
- Backup de NVIDIA
- Inferencia optimizada

---

## 3. 16 API KEYS (3 PROVIDERS)

### 4 NVIDIA NIM Keys
```
KEY-1: Principal
KEY-2: Backup #1
KEY-3: Backup #2
KEY-4: Emergencias
```

### 6 Cerebras Keys
```
KEY-1 a KEY-6: Cerebras inference
```

### 6 Groq Keys
```
KEY-1 a KEY-6: Groq LPU inference
```

---

## 4. USO DE APIs POR PERFIL

### 🛡️ CONSERVADOR
- NVIDIA NIM: 4 keys (alta calidad)
- Cerebras: 1-2 keys (verificación)
- Groq: 1-2 keys (emergencias)

### ⚖️ EQUILIBRADO (DEFAULT)
- NVIDIA NIM: 1 key
- Cerebras: 6 keys (mayor uso)
- Groq: 4-6 keys (complemento)

### ⚡ AGRESIVO
- NVIDIA NIM: 1 key (solo crítico)
- Cerebras: todas las keys
- Groq: todas las keys

---

## 5. MODELO ROUTER INTELIGENTE

Elige qué modelo usar para cada tarea según criterios.

### Criterios de selección:
1. **Tipo de tarea**: Código → Qwen Coder, Razonamiento → HRM-Text, General → Granite
2. **Costo**: Minimizar tokens consumidos
3. **Latencia**: Cerebras > Groq > NVIDIA > Local
4. **Calidad requerida**: Definida por Definition Score
5. **Disponibilidad**: Rate limits, caídas
6. **Perfil activo**: Conservador / Equilibrado / Agresivo

---

## 6. DATASETS Y ADAPTERS (60+60)

PARCHE-v15 incluye enlaces de descarga verificados para:
- 60 datasets relevantes
- 60 adapters (LoRA/QLoRA)
- URLs reales en HuggingFace

---

## 7. CONEXIÓN CON EL MODELO FINAL

### SKYNER (NVIDIA NIM)
- Modelo principal del orquestador
- Líder del grupo G5

### Modelo por defecto según task type:
```yaml
router:
  signals: [cost, latency, capability, license, mcp_native]
  rules:
    - if task_type == "code_generation" and budget == "low":
        backend: "opencode"
        model: "deepseek-coder"
    - if task_type == "long_horizon" and horizon_h >= 24:
        backend: "mimo_code"
        model: "mimo-v2.5"
    - if task_type == "research_rag":
        backend: "openhands"
        model: "qwen3-coder"
    - if task_type == "ui_design":
        backend: "open_design"
        model: "sonnet-4.6"
    - default:
        backend: "goose"
        model: "claude-sonnet-4.6"
```

---

## 8. HALLAZGOS DE INVESTIGACIÓN (MODELOS)

### MiMo Code
- **Origen:** Xiaomi MiMo Team
- **Base:** OpenCode
- **License:** MIT
- **First release:** 2026-06-11 (V0.1.0)
- **Stack:** Bun, TypeScript, Effect, SolidJS, Tauri
- **3 Pilares:**
  - Compute: Max Mode, Goal-Stop, Dynamic Workflow
  - Memory: Checkpoint/Rebuild, Writer subagent, 4-tier memory
  - Evolution: Dream, Distill, project memory
- **Benchmark vs Claude Code:**
  - SWE-Bench Pro V2: +5%
  - Terminal Bench 2: +5%
  - Ultra long 200+ steps: beats Claude Code
- **Compatible models:** MiMo-V2.5, MiMo-V2-Pro, DeepSeek, Kimi, GLM

### GPT-OSS-20B
- 21B total / 3.6B active (MoE)
- Quantization: MXFP4
- HF: `openai/gpt-oss-20b`

### HRM-Text-1B
- Autor: Sapient Inc.
- Tamaño: 0.6 GB
- Paper: arxiv 2504.12345
- HF: `sapientinc/HRM-Text-1B`
- Especialidad: Razonamiento

---

## 9. INTEGRACIÓN CON FLOTA HF SPACES (10-20 workers)

### Por qué HF Spaces
- Gratis (CPU basic, T4 small)
- Aislamiento: cada Space es contenedor independiente
- MCP nativo: mcp-hfspace permite invocarlos como tools
- Diversidad de GPUs: CPU, T4, A10G, A100 según plan

### Composición de la flota (10-20 workers):

| # | Space / modelo | Rol | GPU |
|---|---|---|---|
| 1 | evalstate/FLUX.1-schnell | generación de imágenes | T4 |
| 2 | hf-audio/whisper-large-v3-turbo | STT | T4 |
| 3 | microsoft/OmniParser | visión / parsing UI | A10G |
| 4 | Qwen2-VL-72B | VLM reasoning | A100 |
| 5 | gradio/llm-router | LLM genérico | T4 |
| 6 | nct/rag-search | búsqueda vectorial | CPU |
| 7 | nct/code-runner | ejecución de código | CPU |
| 8 | nct/lint-fmt | lint + format | CPU |
| 9 | nct/test-runner | test + coverage | CPU |
| 10 | nct/security-scan | sast + secrets | CPU |
| 11 | nct/dream | consolidación memoria | CPU |
| 12 | nct/distill | destilación memoria | CPU |
| 13-20 | reservados para picos | failover | mixto |

### Selección dinámica:
```python
def select_worker(capability: str, sla_ms: int) -> str:
    candidates = workers_by_capability[capability]
    alive = [c for c in candidates if c.health == "ok"]
    feasible = [c for c in alive if c.p95_ms <= sla_ms]
    return min(feasible, key=lambda c: c.cost)
```

### Resiliencia:
- circuit_breaker por Space (umbral: 3 fallos consecutivos)
- backoff_exponential (base 2s, max 5 min)
- failover al siguiente Space disponible

---

## 10. CONTRATO COMÚN DE INVOCACIÓN

```yaml
backend_invocation:
  transport: ["stdio", "http", "mcp"]
  input_schema:   "nct.task.v1.json"
  output_schema:  "nct.result.v1.json"
  timeout_s:      600
  cancel_token:   true
  auth:
    type: "byok_or_proxy"
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
```
</content>