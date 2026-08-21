# MASTER DOCUMENTO 10: MODELOS Y APIs
## MAXBRY SUPER TEAM · 9 GGUF + 16 API Keys + 3 Perfiles

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. 9 MODELOS GGUF

### Modelos confirmados en HuggingFace:

| # | Modelo | Params | GGUF Size | Uso |
|---|--------|--------|-----------|-----|
| 1 | **HRM-Text-1B** (Sapient) | 1B | 0.6GB | Razonamiento jerárquico |
| 2 | **Qwen2.5-Coder-1.5B** | 1.5B | 1GB | Generación de código |
| 3 | **Granite-4.1-3B** (IBM) | 3B | 2GB | Asistente general |
| 4 | **Granite-3.2-2B** (IBM) | 2B | 1.5GB | Asistente compacto |
| 5 | **LFM2.5-1.2B-Thinking** | 1.2B | 0.8GB | Razonamiento |
| 6 | **Gemma-4-E4B** (Google) | 4B | 2.5GB | Asistente eficiente |
| 7 | **Gemma-4-E2B** (Google) | 2B | 1.5GB | Asistente compacto |
| 8 | **GPT-OSS-20B** (OpenAI) | 21B total / 3.6B active MoE | 13GB | Modelo fuerte |
| 9 | **Nemotron-3-Nano-4B** (NVIDIA) | 4B | 2.5GB | Asistente NVIDIA |

**Total local:** ~25.6GB

---

## 2. 16 API KEYS

### 2.1 NVIDIA NIM (4 keys)

| Key | Label sugerido | Uso |
|-----|----------------|-----|
| NIM-01 | SKYNER (líder G5) | Tareas principales |
| NIM-02 | Razonamiento | Razonamiento complejo |
| NIM-03 | Código | Generación de código |
| NIM-04 | Backup | Respaldo |

### 2.2 Cerebras (6 keys)

| Key | Label sugerido | Uso |
|-----|----------------|-----|
| CER-01 | COO | Operaciones |
| CER-02 | CTO | Técnico |
| CER-03 | Razonamiento | Análisis |
| CER-04 | Código | Code-gen |
| CER-05 | Backup-1 | Respaldo |
| CER-06 | Backup-2 | Respaldo |

### 2.3 Groq (6 keys)

| Key | Label sugerido | Uso |
|-----|----------------|-----|
| GROQ-01 | CFO | Costos |
| GROQ-02 | CMO | Comunicación |
| GROQ-03 | Historian | Memoria |
| GROQ-04 | Razonamiento | Análisis rápido |
| GROQ-05 | Backup-1 | Respaldo |
| GROQ-06 | Backup-2 | Respaldo |

---

## 3. 3 PERFILES DE USO

### 3.1 Conservador

```yaml
profile:
  name: conservador
  primary: groq
  secondary: nim
  fallback: cerebras
  rules:
    - never use GPT-OSS-20B (too heavy)
    - max 3 retries
    - timeout: 60s
  budget:
    max_tokens_per_task: 100_000
  use_cases:
    - Tareas simples
    - Bajo costo
    - Bajo riesgo
```

### 3.2 Equilibrado (RECOMENDADO)

```yaml
profile:
  name: equilibrado
  primary: nim
  secondary: cerebras
  fallback: groq
  rules:
    - GPT-OSS-20B only for hard tasks
    - max 5 retries
    - timeout: 120s
  budget:
    max_tokens_per_task: 500_000
  use_cases:
    - Mayoría de tareas
    - Balance costo/calidad
```

### 3.3 Agresivo

```yaml
profile:
  name: agresivo
  primary: cerebras
  secondary: nim
  fallback: groq
  rules:
    - always try GPT-OSS-20B first
    - max 10 retries
    - timeout: 300s
  budget:
    max_tokens_per_task: 2_000_000
  use_cases:
    - Tareas críticas
    - Máxima calidad
    - Costo no importa
```

---

## 4. ROUTER INTELIGENTE

```python
def select_model(task, profile):
    candidates = MODELS_BY_CAPABILITY[task.type]
    if profile == "conservador":
        return cheapest(candidates)
    elif profile == "equilibrado":
        return best_quality_per_dollar(candidates)
    else:  # agresivo
        return best_quality(candidates)
```

### Reglas de routing:
- Tarea simple → GGUF local
- Tarea media → Groq
- Tarea compleja → Cerebras o NIM
- Tarea crítica → GPT-OSS-20B vía NIM

---

## 5. DATASETS (60)

Descargados con PARCHE-v15:
- 30 datasets de código
- 15 datasets de texto
- 10 datasets especializados
- 5 datasets de testing

Total: 60 datasets con URLs verificadas.

---

## 6. ADAPTERS (60)

Descargados con PARCHE-v15:
- 30 LoRA adapters
- 15 QLoRA adapters
- 10 prefix tuning
- 5 prompt tuning

Total: 60 adapters con URLs verificadas.

---

## 7. CAPACIDADES

### Hardware disponible:
- 7 HF Spaces × 16GB = 112GB RAM
- ~13.5GB usados por modelos G6
- 87% margen libre

### Throughput estimado:
- 1000+ tareas/día con perfil equilibrado
- 2000+ tareas/día con perfil conservador
- 100+ tareas/día con perfil agresivo

---

## 8. CONCLUSIÓN

G6 (Asistentes) tiene:
- 9 modelos GGUF locales
- 16 API keys (4 NIM + 6 Cerebras + 6 Groq)
- 3 perfiles de uso
- Router inteligente
- 60 datasets
- 60 adapters
- Capacidad para 1000+ tareas/día
- Costo $0/mes con free tiers
</content>