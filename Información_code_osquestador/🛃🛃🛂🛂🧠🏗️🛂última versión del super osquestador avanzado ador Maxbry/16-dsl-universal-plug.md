# MASTER DOCUMENTO 16: DSL + UNIVERSAL PLUG v1.5
## MAXBRY SUPER TEAM · DSL DAG · Universal Module Contract · Validación Cruzada

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. DSL — DOMAIN SPECIFIC LANGUAGE

### 1.1 Qué es
DSL es el lenguaje estructurado que usa NCT para definir tareas, workflows, pipelines y configuraciones. **Nunca es prompt libre.**

### 1.2 Reglas
- Estructura cerrada (no free-form)
- Validado contra schema
- Parseable deterministamente
- Versionado (semver)
- Schema-first

### 1.3 Tipos de DSL soportados

| Tipo | Uso | Schema |
|------|-----|--------|
| DSL Task | Definir tarea | task.v1.json |
| DSL Pipeline | Definir pipeline | pipeline.v1.json |
| DSL Agent | Definir agente | agent.v1.json |
| DSL Skill | Definir skill | skill.v1.json |
| DSL Project | Definir proyecto | project.v1.json |
| DSL Workflow | Definir workflow | workflow.v1.json |
| DSL DAG | Definir DAG | dag.v1.json |

---

## 2. DSL TASK (Ejemplo)

```yaml
task:
  id: task-2026-06-28-001
  type: simple
  level: L2_SUPERVISED
  input:
    source: telegram
    raw: "crear API REST para tareas"
  goals:
    primary: "API funcional"
    secondary: "Con tests"
    success: "Tests pasan + API responde"
    failure: "Tests fallan o API no responde"
    restriction: "No usar frameworks pesados"
  steps:
    - id: s1
      action: parse_input
    - id: s2
      action: validate_schema
    - id: s3
      action: generate_plan
    - id: s4
      action: execute
    - id: s5
      action: validate
    - id: s6
      action: deliver
  budget:
    max_tokens: 100_000
    max_runtime_s: 600
```

---

## 3. DSL PIPELINE (Ejemplo)

```yaml
pipeline:
  id: pipeline-001
  name: "Crear API REST"
  pattern: dag
  steps:
    - id: parse
      agent: MA-01
      input_from: user
      output_to: ctx.parsed
    - id: plan
      agent: MA-06
      input_from: ctx.parsed
      output_to: ctx.plan
      depends_on: parse
    - id: execute
      agent: MA-15
      input_from: ctx.plan
      output_to: ctx.executed
      depends_on: plan
    - id: verify
      agent: MA-16
      input_from: ctx.executed
      output_to: ctx.verified
      depends_on: execute
  consensus: required
  audit: full_csa
```

---

## 4. DSL DAG

### 4.1 Estructura

```yaml
dag:
  id: dag-001
  nodes:
    - id: A
      type: task
      agent: MA-01
    - id: B
      type: task
      agent: MA-06
    - id: C
      type: task
      agent: MA-15
  edges:
    - { from: A, to: B }
    - { from: B, to: C }
  groups:
    - { id: g1, nodes: [A, B], parallel: true }
```

### 4.2 Validación
- No ciclos
- Topological sort válido
- Cada nodo tiene agente
- Cada edge tiene origen y destino válidos

---

## 5. UNIVERSAL PLUG v1.5

### 5.1 Qué es
MAXBRY Module Contract JSON Schema. Define cómo los módulos se conectan entre sí.

### 5.2 Schema (resumido)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MAXBRY Module Contract",
  "version": "1.5",
  "type": "object",
  "required": ["module_id", "version", "interface"],
  "properties": {
    "module_id": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9_]*$"
    },
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$"
    },
    "interface": {
      "type": "object",
      "required": ["inputs", "outputs"],
      "properties": {
        "inputs": { "type": "array" },
        "outputs": { "type": "array" }
      }
    },
    "dependencies": {
      "type": "array",
      "items": { "type": "string" }
    },
    "capabilities": {
      "type": "array"
    },
    "limits": {
      "type": "object"
    },
    "metadata": {
      "type": "object"
    }
  }
}
```

### 5.3 Ejemplo de Módulo

```json
{
  "module_id": "ma_code_gen",
  "version": "1.0.0",
  "interface": {
    "inputs": [
      {
        "name": "spec",
        "type": "string",
        "required": true
      },
      {
        "name": "stack",
        "type": "object",
        "required": true
      }
    ],
    "outputs": [
      {
        "name": "code",
        "type": "file"
      },
      {
        "name": "diff",
        "type": "file"
      }
    ]
  },
  "dependencies": ["ma_arch_plan"],
  "capabilities": ["code_generation", "diff_creation"],
  "limits": {
    "max_tokens": 50000,
    "max_runtime_s": 120
  },
  "metadata": {
    "owner": "g5-orquestador",
    "category": "J-IA",
    "license": "MIT"
  }
}
```

---

## 6. UNIVERSAL MODULE CONTRACT v1.5 (JSON Schema Completo)

### Campos obligatorios:
- `module_id`
- `version`
- `interface.inputs`
- `interface.outputs`

### Campos opcionales:
- `dependencies`
- `capabilities`
- `limits`
- `metadata`
- `tags`
- `author`

### Validación:
- Schema válido contra Draft-07
- module_id único
- version semver
- interface tipado
- dependencies resolubles

---

## 7. SISTEMA DE VALIDACIÓN CRUZADA (DSL DAG)

### 7.1 Concepto
DSL DAG de validación cruzada garantiza que:
- Cada documento referencia al menos 2 docs más
- Las referencias son válidas
- No hay contradicciones entre docs
- Las dependencias son resolubles

### 7.2 Estructura

```yaml
cross_validation:
  node: MASTER-XX
  references_to:
    - MASTER-YY
    - MASTER-ZZ
  referenced_by:
    - MASTER-WW
  consistency_check:
    no_contradictions: true
    terms_aligned: true
    versions_match: true
    schema_compatible: true
```

### 7.3 Ejecución

```python
def cross_validate(doc_a, doc_b):
    # Check no contradictions
    if contradiction(doc_a, doc_b):
        return {"valid": False, "reason": "contradiction"}
    
    # Check term alignment
    if not terms_aligned(doc_a, doc_b):
        return {"valid": False, "reason": "term_misalignment"}
    
    # Check version compatibility
    if not versions_match(doc_a, doc_b):
        return {"valid": False, "reason": "version_mismatch"}
    
    return {"valid": True}
```

---

## 8. VALIDACIÓN EN CADA MASTER DOC

Cada Master Doc tiene:

```yaml
node:
  id: MASTER-XX
  status: complete
  size: <60000 chars
  cross_refs:
    - MASTER-YY
  sentinel_pass: true
  judge_score: 92
  completeness: 100
```

---

## 9. CONCLUSIÓN

El DSL + Universal Plug v1.5 + Universal Module Contract + DSL DAG de validación cruzada forman el sistema de contratos que garantiza interoperabilidad entre módulos. Ningún módulo se conecta sin pasar por estos schemas.
</content>