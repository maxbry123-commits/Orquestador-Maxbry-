# DOCUMENTO 01 — INSTALACIÓN DE AGENTES + SKILLS
## Para Open Claw, 4 Claude Code, 4 Mimo Code
## V1.0 — Completo

---

## 1. INSTALACIÓN DE OPEN CLAW (Orquestador)

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes --version
hermes setup
hermes model --provider openrouter --model "anthropic/claude-sonnet-4"
hermes tools --enable all
hermes gateway start --port 8642
```

### 10 Skills para Open Claw

1. find-skills: `npx skills add vercel-labs/skills --skill find-skills`
2. skill-creator: `/plugin install example-skills@anthropic-agent-skills`
3. superpowers: `/plugin install obra/superpowers`
4. vercel-react-best-practices: `npx skills add vercel-labs/agent-skills`
5. frontend-design: `/plugin install example-skills@anthropic-agent-skills`
6. software-architecture: `npx skills add composiohq/awesome-claude-skills`
7. systematic-debugging: `/plugin install obra/superpowers`
8. tdd-workflow: `/plugin install obra/superpowers`
9. code-review: `/plugin install example-skills@anthropic-agent-skills`
10. webapp-testing: `/plugin install example-skills@anthropic-agent-skills`

---

## 2. INSTALACIÓN DE 4 CLAUDE CODE

```
npm install -g @anthropic-ai/claude-code
claude --version
```

### 4 API keys (NVIDIA Minimax M3)

| Claude | Variable | Grupo |
|---|---|---|
| A | NVIDIA_API_KEY_A | cerebro + auditor |
| B | NVIDIA_API_KEY_B | fichas |
| C | NVIDIA_API_KEY_C | router |
| D | NVIDIA_API_KEY_D | frontend |

```bash
export ANTHROPIC_BASE_URL=https://integrate.api.nvidia.com/v1
export ANTHROPIC_AUTH_TOKEN=$NVIDIA_API_KEY_A
claude --model "minimax/minimax-m3"
```

### Skills por Claude Code

**Claude A:** superpowers, software-architecture, mcp-builder, recursive-research, deep-research, prompt-engineering, article-extractor, brainstorming, notebooklm-integration, systematic-debugging

**Claude B:** artifacts-builder, mcp-builder, docx, pdf, xlsx, csv-data-summarizer, recursive-research, code-review, systematic-debugging, superpowers

**Claude C:** aws-skills, connect, playwright-browser-automation, ffuf-web-fuzzing, software-architecture, superpowers, code-review, systematic-debugging, mcp-builder, prompt-engineering

**Claude D:** vercel-react-best-practices, frontend-design, artifacts-builder, d3-visualization, anydesign, canvas-design, webapp-testing, superpowers, tdd-workflow, code-review

---

## 3. INSTALACIÓN DE 4 MIMO CODE

```
pip install mimo-code
mimo --version
```

### 4 API keys (Groq Kimi K)

| Mimo | Variable | Grupo |
|---|---|---|
| A | GROQ_API_KEY_A | cerebro + auditor |
| B | GROQ_API_KEY_B | fichas |
| C | GROQ_API_KEY_C | router |
| D | GROQ_API_KEY_D | frontend |

```bash
export MIMO_BASE_URL=https://api.groq.com/openai/v1
export MIMO_AUTH_TOKEN=$GROQ_API_KEY_A
export MIMO_MODEL=moonshotai/kimi-k2-instruct
mimo start
```

### Skills por Mimo Code

**Mimo A:** code-review, systematic-debugging, tdd-workflow, testing-best-practices, software-architecture, mcp-builder, ralph-loop, superpowers, prompt-engineering, recursive-research

**Mimo B:** code-review, tdd-workflow, testing-best-practices, docx, xlsx, csv-data-summarizer, systematic-debugging, superpowers, ralph-loop, software-architecture

**Mimo C:** code-review, tdd-workflow, testing-best-practices, aws-skills, ffuf, software-architecture, systematic-debugging, ralph-loop, superpowers, prompt-engineering

**Mimo D:** code-review, vercel-react-best-practices, frontend-design, webapp-testing, tdd-workflow, testing-best-practices, systematic-debugging, ralph-loop, superpowers, artifacts-builder

---

## 4. ORDEN DE INSTALACIÓN

1. Instalar Open Claw (30 min)
2. Validar Open Claw + skills (15 min)
3. Instalar Claude A (10 min)
4. Instalar Mimo A (10 min)
5. Grupo A activo
6. Instalar Claude B, C, D en paralelo (30 min)
7. Instalar Mimo B, C, D en paralelo (30 min)
8. Validar 4 grupos activos (15 min)
9. Open Claw inicia coordinación (5 min)

TOTAL: ~2.5 horas

---

## 5. VALIDACIÓN DE API KEYS

```bash
claude --test-connection
mimo --test-connection
hermes --test-connection
```

Si falla: registrar, esperar 5 min, reintentar 1 vez, escalar si persiste.

---

## 6. EJEMPLO `.meta.md`

```markdown
# Ficha: capture

## Identidad
- ficha_id: CLAUDE-CAPTURE-20260706-030000-A8F3C2
- version: 1.0.0
- modelo: Claude Code A
- fecha_creacion: 2026-07-06
- hash: a8f3c2

## Stage
imput

## Propósito
Captura evento entrante y normaliza a formato estándar.

## Input Schema
ruta: contratos/imput_input.schema.json

## Output Schema
ruta: contratos/imput_output.schema.json

## Runtime
- runtime_type: compute
- llm_ratio_estimado: 0.0
- timeout_seg: 30
- memory_mb: 128
- sandbox: strict
- idempotente: true

## Contrato
- efectos: []
- dependencias: []

## Tests
ruta: tests/test_capture.py

## Versionado
- estado: DRAFT
- reemplaza: null
- historial_cambios: []

## Auditor
- n0_gpg: pendiente
- n1_hash: pendiente
- n2_schema: pendiente
- n3_version: pendiente
- n4_compat: pendiente
- n5_ast: pendiente
- sc1_ficha_id: pendiente
- sc2_hash: pendiente
- sc3_schemas: pendiente
- sc4_runtime_type: pendiente
- sc5_llm_ratio: pendiente
- sc6_idempotente: pendiente
```

---

## 7. EJEMPLO `location.json`

```json
{
  "artifact_id": "CLAUDE-CAPTURE-20260706-030000-A8F3C2",
  "ficha_id": "capture",
  "name": "Capture Input",
  "folder_structure": {
    "root": "fichas/imput/01_capture/",
    "code_path": "fichas/imput/01_capture/capture.py",
    "meta_path": "fichas/imput/01_capture/capture.meta.md",
    "test_path": "fichas/imput/01_capture/test_capture.py"
  },
  "files": {
    "code_file": "capture.py",
    "meta_file": "capture.meta.md",
    "test_file": "test_capture.py"
  },
  "repo": "fichas",
  "group": "B",
  "claude_instance": "B",
  "mimo_instance": "B",
  "created_by": "claude_code_b",
  "validated_by": "mimo_code_b"
}
```

---

## 8. COMANDO OPEN CLAW PARA DISTRIBUIR SKILLS

```bash
hermes skills distribute --group A --skills "superpowers,software-architecture,mcp-builder,recursive-research,deep-research,prompt-engineering,article-extractor,brainstorming,notebooklm-integration,systematic-debugging"
hermes skills distribute --group B --skills "artifacts-builder,mcp-builder,docx,pdf,xlsx,csv-data-summarizer,recursive-research,code-review,systematic-debugging,superpowers"
hermes skills distribute --group C --skills "aws-skills,connect,playwright-browser-automation,ffuf-web-fuzzing,software-architecture,superpowers,code-review,systematic-debugging,mcp-builder,prompt-engineering"
hermes skills distribute --group D --skills "vercel-react-best-practices,frontend-design,artifacts-builder,d3-visualization,anydesign,canvas-design,webapp-testing,superpowers,tdd-workflow,code-review"
```

---

## 9. RECOVERY SI FALLA API KEY

```python
import os
import time
import requests

def test_key(agente, key):
    try:
        if agente.startswith("claude"):
            r = requests.get("https://integrate.api.nvidia.com/v1/models",
                headers={"Authorization": f"Bearer {key}"}, timeout=10)
            return r.status_code == 200
        elif agente.startswith("mimo"):
            r = requests.get("https://api.groq.com/openai/v1/models",
                headers={"Authorization": f"Bearer {key}"}, timeout=10)
            return r.status_code == 200
    except Exception as e:
        log_failure(agente, e)
        return False

def recovery_key(agente, key):
    for attempt in range(3):
        if test_key(agente, key):
            return True
        time.sleep(2 ** attempt)
    backup = os.environ.get(f"{agente.upper()}_BACKUP")
    if backup and test_key(agente, backup):
        os.environ[agente] = backup
        return True
    escalate_director(f"API key de {agente} falló")
    return False
```

---

## 10. RESUMEN DE COSTOS

| Componente | Skills | API | Costo Est. |
|---|---|---|---|
| Open Claw | 10 | OpenRouter | $5/día |
| Claude A | 10 | NVIDIA #1 | $20/día |
| Claude B | 10 | NVIDIA #2 | $20/día |
| Claude C | 10 | NVIDIA #3 | $20/día |
| Claude D | 10 | NVIDIA #4 | $20/día |
| Mimo A | 10 | Groq #1 | $3/día |
| Mimo B | 10 | Groq #2 | $3/día |
| Mimo C | 10 | Groq #3 | $3/día |
| Mimo D | 10 | Groq #4 | $3/día |
| **TOTAL** | **90** | | **$97/día** |

---

## 11. CRITERIOS DE ACEPTACIÓN

- [x] Open Claw tiene comando de instalación
- [x] 4 Claude Code con 4 API keys separadas
- [x] 4 Mimo Code con 4 API keys separadas
- [x] 10 skills por cada agente (90 totales)
- [x] Ejemplo de .meta.md
- [x] Ejemplo de location.json
- [x] Orden de instalación
- [x] Validación de API keys
- [x] Recovery si falla
- [x] Comando Open Claw para distribuir skills
- [x] Tabla resumen de costos
- [x] Criterios de aceptación

DOCUMENTO 01 COMPLETO V1.0
