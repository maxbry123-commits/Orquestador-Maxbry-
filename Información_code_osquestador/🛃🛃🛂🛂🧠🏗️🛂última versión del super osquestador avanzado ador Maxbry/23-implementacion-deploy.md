# MASTER DOCUMENTO 23: IMPLEMENTACIÓN Y DEPLOY
## MAXBRY SUPER TEAM · Estructura · Código · Tests · Deployment

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. ESTRUCTURA DE ARCHIVOS

### 1.1 Regla general
- Máximo 200 líneas por archivo
- Una responsabilidad por archivo
- Naming snake_case para Python
- Type hints obligatorios

### 1.2 Estructura MAXBRY

```
/workspace/maxbry/g5-orquestador/
├── README.md
├── pyproject.toml
├── Dockerfile
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── constitution.py        # 39 principios
│   │   ├── csa.py                # 10 jueces
│   │   ├── sid.py                # 5 preguntas
│   │   └── bis.py                # 14 categorías
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── micro_30.py           # 30 micro-agentes
│   │   ├── consensus_5.py        # 5 consenso
│   │   ├── investigation_5.py    # 5 investigación
│   │   ├── officers_5.py         # 5 officers
│   │   └── council_10.py         # 10 consejo
│   │
│   ├── engines/
│   │   ├── __init__.py
│   │   ├── input_engine.py       # 54 componentes
│   │   ├── output_engine.py      # 13 componentes
│   │   ├── oos.py                # 14 componentes OOS
│   │   ├── ovfs.py               # Output Virtual FS
│   │   └── loop_engine.py        # 15 capas + 3 ciclos
│   │
│   ├── state/
│   │   ├── __init__.py
│   │   ├── state.py              # state.json
│   │   ├── events.py             # event log
│   │   ├── memory.py             # 4-tier memory
│   │   └── checkpoints.py        # snapshots firmados
│   │
│   ├── orchestration/
│   │   ├── __init__.py
│   │   ├── skyner.py             # líder
│   │   ├── task_models.py        # 12 TM
│   │   ├── loop_versions.py      # 5 ALV
│   │   └── monitors.py           # 3 monitores
│   │
│   └── delivery/
│       ├── __init__.py
│       ├── multi_target.py       # 23 destinos
│       ├── adaptive.py           # adaptive format
│       └── feedback.py           # feedback loop
│
├── tests/
│   ├── unit/                     # 100+ tests
│   ├── integration/              # 30+ tests
│   └── e2e/                      # 10+ tests
│
├── scripts/
│   ├── bootstrap.sh
│   ├── health_check.py
│   └── report.py
│
└── config/
    ├── profile_conservador.yaml
    ├── profile_equilibrado.yaml
    └── profile_agresivo.yaml
```

---

## 2. EJEMPLO DE CÓDIGO

### 2.1 constitution.py (extracto)

```python
from enum import Enum
from typing import List

class ConstitutionPrinciple:
    def __init__(self, number: int, version: str, title: str, description: str):
        self.number = number
        self.version = version
        self.title = title
        self.description = description

class Constitution:
    PRINCIPLES: List[ConstitutionPrinciple] = [
        ConstitutionPrinciple(1, "v1.0", "FILOSOFÍA",
            "El Orquestador opera como Director de Empresa, no como IA."),
        ConstitutionPrinciple(2, "v1.0", "OBJETIVOS DE ESCALA",
            "Soporta 2000+ agentes y 1000+ tareas simultáneas."),
        # ... 37 más
    ]
    
    @classmethod
    def get(cls, number: int) -> ConstitutionPrinciple:
        return next(p for p in cls.PRINCIPLES if p.number == number)
    
    @classmethod
    def all(cls) -> List[ConstitutionPrinciple]:
        return cls.PRINCIPLES
    
    @classmethod
    def by_version(cls, version: str) -> List[ConstitutionPrinciple]:
        return [p for p in cls.PRINCIPLES if p.version == version]
```

### 2.2 sid.py (extracto)

```python
SID_QUESTIONS = [
    "What is this?",
    "Who is it for?",
    "What problem does it solve?",
    "How is it used?",
    "What is it NOT?"
]

async def run_sid(task: str) -> dict:
    answers = []
    for question in SID_QUESTIONS:
        ans = await generate_answer(task, question)
        score = await score_answer(ans)
        answers.append({"q": question, "a": ans, "score": score})
    
    total = sum(a["score"] for a in answers) / 5
    return {
        "answers": answers,
        "total_score": total,
        "decision": "pass" if total >= 95 else "fail"
    }
```

### 2.3 csa.py (extracto)

```python
class CSAJudge:
    def __init__(self, id: str, name: str, question: str, evaluator: callable):
        self.id = id
        self.name = name
        self.question = question
        self.evaluator = evaluator
    
    async def run(self, artifact: dict, rubric: dict) -> dict:
        # 5 phases
        phase_1 = self.audit_input(artifact, rubric)   # F1
        phase_2 = self.find_unreviewed(artifact)         # F2
        phase_3 = self.generate_alternatives(artifact)   # F3
        phase_4 = self.destroy_self(artifact)            # F4
        phase_5 = self.attack_others(artifact)           # F5
        
        issues = sum([phase_1, phase_2, phase_3, phase_4, phase_5], [])
        score = max(0, 100 - len(issues) * 5)
        
        return {
            "judge": self.id,
            "score": score,
            "issues": issues,
            "phases": {
                "F1": phase_1, "F2": phase_2,
                "F3": phase_3, "F4": phase_4, "F5": phase_5
            }
        }

# 10 jueces
CSA_JUDGES = [
    CSAJudge("J1", "COMPRENSIÓN", "¿Entendimos QUÉ quiere MAX?", eval_j1),
    CSAJudge("J2", "COBERTURA", "¿Cubrimos TODO?", eval_j2),
    # ... 8 más
]
```

---

## 3. TESTS

### 3.1 Unit Tests (ejemplo)

```python
# test_constitution.py

def test_principles_count():
    assert len(Constitution.PRINCIPLES) == 39

def test_v1_has_13_principles():
    v1 = Constitution.by_version("v1.0")
    assert len(v1) == 13

def test_v2_has_13_principles():
    v2 = Constitution.by_version("v2.0")
    assert len(v2) == 13

def test_v3_has_13_principles():
    v3 = Constitution.by_version("v3.0")
    assert len(v3) == 13

def test_get_principle_by_number():
    p = Constitution.get(1)
    assert p.title == "FILOSOFÍA"

def test_sid_questions_fixed():
    assert len(SID_QUESTIONS) == 5
    assert SID_QUESTIONS[0] == "What is this?"

def test_csa_has_10_judges():
    assert len(CSA_JUDGES) == 10
```

### 3.2 Integration Tests

```python
# test_sid_csa_flow.py

async def test_sid_to_csa():
    # SID
    sid_result = await run_sid("Crear API REST")
    assert sid_result["decision"] == "pass"
    
    # CSA
    artifact = {"code": "...", "tests": "..."}
    rubric = {"spec": "...", "criteria": [...]}
    
    results = await asyncio.gather(*[
        j.run(artifact, rubric) for j in CSA_JUDGES
    ])
    
    avg = sum(r["score"] for r in results) / 10
    assert avg >= 80
```

---

## 4. DOCKERFILE

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    git curl wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY src/ /app/src/
COPY config/ /app/config/
COPY scripts/ /app/scripts/

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python scripts/health_check.py || exit 1

# Run
CMD ["python", "-m", "src.core.constitution"]
```

---

## 5. DEPLOYMENT EN HF SPACES

### 5.1 Estructura HF Space

```
mavis/g5-orquestador/
├── README.md (con SDK metadata)
├── requirements.txt
├── Dockerfile (opcional)
├── app.py (entry point para Gradio/Streamlit)
└── src/
    └── ...
```

### 5.2 SDK Metadata (README.md header)

```yaml
---
title: G5 Orquestador MAXBRY
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: true
license: mit
---
```

### 5.3 Secrets (HF Space Settings)

```
NVIDIA_NIM_KEY_01=...
NVIDIA_NIM_KEY_02=...
...
CEREBRAS_KEY_01=...
...
GROQ_KEY_01=...
...
HF_TOKEN=...
GITHUB_TOKEN=...
TURSO_URL=...
TURSO_TOKEN=...
TELEGRAM_BOT_TOKEN=...
```

---

## 6. BOOTSTRAP SCRIPT

```bash
#!/bin/bash
# bootstrap.sh

set -e

echo "🚀 MAXBRY SUPER TEAM Bootstrap"

# 1. Verificar entorno
python --version || (echo "Python 3.11+ requerido" && exit 1)

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Verificar secrets
python scripts/verify_secrets.py

# 4. Health check
python scripts/health_check.py

# 5. Inicializar state
python scripts/init_state.py

# 6. Cargar skills BIS
python scripts/load_bis.py

# 7. Iniciar orquestador
echo "✅ Bootstrap completo"
echo "📊 Report:"
python scripts/report.py
```

---

## 7. MONITORING

### 7.1 Métricas clave

```python
METRICS = {
    "tasks_total": Counter(),
    "tasks_success": Counter(),
    "tasks_failed": Counter(),
    "agents_active": Gauge(),
    "consensus_score": Histogram(),
    "csa_scores": Histogram(),
    "llm_tokens_used": Counter(),
    "loop_iterations": Histogram(),
    "drift_score": Gauge(),
    "anxiety_level": Gauge(),
}
```

### 7.2 Health Check Endpoint

```python
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "agents_active": METRICS["agents_active"].value,
        "tasks_total": METRICS["tasks_total"].value,
        "uptime": get_uptime(),
        "version": "1.0.0"
    }
```

---

## 8. CONCLUSIÓN

La implementación está completamente especificada:
- Estructura de archivos (<200 LOC c/u)
- Código de ejemplo (Constitution, SID, CSA)
- Tests (unit, integration, e2e)
- Dockerfile
- Deployment HF Spaces
- Bootstrap script
- Monitoring

Listo para implementación cuando MAX apruebe.
</content>