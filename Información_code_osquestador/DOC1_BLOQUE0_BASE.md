# DOCUMENTO 1 — BLOQUE 0: BASE DEL PROYECTO
# CONSTITUCIÓN + PRE-DIAGRAMA + GOVERNANCE + ROADMAP
# VERSION FINAL

```json
{
  "protocol_id": "MAXBRY_BUILD_SYSTEM_V1",
  "block_id": "B0_FOUNDATION",
  "purpose": "Definir identidad, límites, objetivos y reglas del sistema",
  "mandatory": true,
  "creates_code": false,
  "authority_order": [
    "CONSTITUTION","ARCHITECTURE","BLUEPRINT",
    "TASKS","CONTRACTS","SPECS","ARTIFACTS"
  ],
  "construction_sequence": [
    "Arquitectura","Bloques","Componentes","Tareas","Contratos","Código"
  ],
  "ai_role": "Arquitecto y Constructor",
  "human_role": "Director",
  "forbidden_actions": [
    "Modificar constitución sin aprobación",
    "Crear código sin contrato",
    "Alterar dependencias definidas",
    "Inventar componentes fuera de arquitectura",
    "Construir sin leer system_manifest.json + project_index.json"
  ]
}
```

## INSTRUCCIONES PARA LA IA

Antes de construir cualquier componente debes:
1. Leer system_manifest.json
2. Leer project_index.json
3. Leer la constitución
4. Leer la arquitectura
5. Leer el blueprint
6. Identificar dependencias
7. Construir únicamente lo autorizado

Regla absoluta: ARQUITECTURA → COMPONENTES → TAREAS → CONTRATOS → CÓDIGO

⚠️ ANTI-SOBRE-INGENIERÍA:
Si propones más de 3 componentes para resolver algo simple → PARAR
MVP primero. Escalar después. NUNCA al revés.

---

## 0. ARCHIVOS RAÍZ

### system_manifest.json
```json
{
  "project_id": "MAXBRY_G2",
  "name": "MAXBRY",
  "version": "1.0",
  "architecture_version": "G2",
  "artifact_standard": "v3",
  "control_plane": "github",
  "execution_plane": "storage",
  "entrypoint": "sequence.json",
  "status_file": "PROJECT_STATUS.md",
  "task_file": "TASKS.md",
  "registry_file": "BUILD_REGISTRY.md",
  "layers": ["kernel","runtime","verification","state"],
  "components_count": 25,
  "artifact_count": 0,
  "created_at": "[FECHA]"
}
```

### project_index.json
```json
{
  "documents": {
    "roadmap": "ROADMAP.md",
    "architecture": "ARCHITECTURE.md",
    "blueprint": "BLUEPRINT.md",
    "tasks": "TASKS.md",
    "decisions": "DECISIONS.md"
  },
  "registries": {
    "build": "BUILD_REGISTRY.md",
    "approval": "APPROVAL_LEDGER.json",
    "dependency": "DEPENDENCY_REGISTRY.json"
  },
  "artifacts": {
    "contracts": "A06_artifact_contracts/",
    "specs": "A07_artifact_specs/",
    "manifests": "A13_artifact_manifests/",
    "code": "storage/B01_artifact_code/"
  },
  "standards": {
    "artifact": "ARTIFACT_STANDARD.md",
    "versioning": "VERSIONING_POLICY.md",
    "errors": "ERROR_CODES.md",
    "loader": "LOADER_CONTRACT.md"
  }
}
```

---

## 1. PERFIL.md
Constitución T0 del proyecto — identidad, propósito, definición formal del sistema

## 2. NORTH STAR METRIC
Métrica única de éxito global
- North Star: [descripción]
- Medición: [métrica]

## 3. OBJETIVOS 1/3/5 AÑOS
Evolución temporal verificable

## 4. ALCANCE (IN / OUT)
- IN_SCOPE: [lista]
- OUT_SCOPE: [lista]

## 5. PRINCIPIOS DE DISEÑO
- Modularidad
- Desacoplamiento
- Determinismo
- Trazabilidad
- Auditoría
- 90% código / 10% LLM aislado
- Brain sin código de negocio
- Código externo cargado bajo demanda

## 6. ANTI-PATRONES PROHIBIDOS
- Acoplamiento fuerte entre módulos
- Dependencias ocultas
- Estado global no auditado
- Código sin contrato
- LLM como orquestador
- Sobre-ingeniería
- Código de negocio en GitHub brain
- Fases/clases internas dentro de fichas

## 7. CAPABILITY GRAPH (ALTO NIVEL)
```json
{
  "capability_graph": {
    "version": "1.0",
    "capabilities": [
      {"id":"CAP-01","name":"PLANIFICAR","component":"PLANNER_OFFLINE","layer":"KERNEL","enables":["CAP-02","CAP-03"],"status":"MVP"},
      {"id":"CAP-02","name":"EJECUTAR","component":"RUNTIME","layer":"RUNTIME","depends_on":["CAP-04","CAP-05"],"status":"MVP"},
      {"id":"CAP-03","name":"VERIFICAR","component":"VERIFIER","layer":"VERIFICATION","enables":["CAP-02"],"status":"MVP"},
      {"id":"CAP-04","name":"RECUPERAR","component":"RECOVERY_CORE","layer":"STATE","status":"MVP"},
      {"id":"CAP-05","name":"MEMORIZAR","component":"STATE_MANAGER","layer":"STATE","status":"MVP"},
      {"id":"CAP-06","name":"AUDITAR","component":"AUDIT_SYSTEM","layer":"VERIFICATION","status":"MVP"},
      {"id":"CAP-07","name":"OBSERVAR","component":"OBSERVABILITY","layer":"VERIFICATION","status":"MVP"}
    ],
    "dependency_order": ["CAP-05","CAP-04","CAP-03","CAP-07","CAP-06","CAP-02","CAP-01"]
  }
}
```

## 8. MAPA DE DEPENDENCIAS
- Brain → depende de Verification, State, Memory
- Memory → depende de State
- Verification → depende de State
- State → independiente (base de todo)

## 9. RIESGOS ARQUITECTÓNICOS
- Acoplamiento entre módulos
- Complejidad del runtime
- Inconsistencia de estado
- Eventos mal definidos
- Sobre-ingeniería
- LLM tomando decisiones de flujo

---

## PRE-DIAGRAMA ESTRUCTURAL (15 DOMINIOS)

01_core, 02_runtime, 03_state, 04_event_bus, 05_swarm,
06_memory, 07_validation, 08_repair, 09_security,
10_protocols, 11_observability, 12_infrastructure,
13_ui, 14_self_audit, 15_future_systems (EXPERIMENTAL — no MVP)

---

## CONSTITUCIÓN DEL SISTEMA

Jerarquía normativa:
OBJETIVOS → CONSTITUCIÓN → DECISIONES → CONTRATOS → SCHEMAS → ARTIFACTS → CÓDIGO

### REGLA UNIVERSAL G3
"Ningún modelo construye sin pre-diagrama previo"

PROHIBIDO iniciar construcción sin:
- ✅ Pre-diagrama de 15 dominios aprobado
- ✅ Bloque 0 completo y aprobado
- ✅ system_manifest.json presente
- ✅ project_index.json presente
- ✅ template_completeness_check = COMPLETO

Aplica a: Claude, GPT, Kimi, Gemini — cualquier modelo.

---

## MOTOR DECISIONES — FSM KERNEL

Estados FSM:
IDLE → PARSE → ROUTE → EXECUTE → VERIFY → COMMIT → IDLE

Tabla de transiciones:
- IDLE + input_recibido → PARSE
- PARSE + input_valido → ROUTE
- ROUTE + modo_identificado → EXECUTE
- EXECUTE + ejecucion_ok → VERIFY
- VERIFY + verificacion_ok → COMMIT
- COMMIT + commit_ok → IDLE

Archivo: kernel.py | Capa: KERNEL | Tarea: T001
NUNCA usar LLM para decidir transiciones.

---

## CLASIFICADOR INTENCIONES — ROUTER

Archivo: router/dispatcher.py | Capa: KERNEL | Tarea: T003

Keywords por modo:
- CONSTRUIR: ["construye","genera","crea","implementa"] peso:10
- INVESTIGAR: ["investiga","busca","analiza","explora"] peso:10
- AUDITAR: ["audita","revisa","verifica","valida"] peso:10
- APROBAR: ["aprueba","confirma","acepta","ok"] peso:10
- RECUPERAR: ["recupera","restaura","rollback","repair"] peso:10

---

## 12 MAPAS DEL SISTEMA

MVP (construir ahora):
- MAPA 01: VISIÓN GLOBAL
- MAPA 02: CAPABILITY MAP
- MAPA 03: COMPONENT MAP
- MAPA 04: DEPENDENCY MAP
- MAPA 05: DATA FLOW MAP
- MAPA 06: GOVERNANCE MAP
- MAPA 07: STATE MAP

POST-MVP:
- MAPA 08: COST FLOW MAP
- MAPA 09: SECURITY MAP
- MAPA 10: RECOVERY MAP
- MAPA 11: TESTING MAP
- MAPA 12: ROADMAP TEMPORAL

---

## MAPA MENTAL (9 CAPAS)
VISIÓN → OBJETIVOS → CAPABILITIES → RAMAS_APEX → MÓDULOS → CONTRATOS → EVENTOS → ESTADOS → CÓDIGO

---

## ROADMAP

### FASE 0 — FUNDACIÓN [P0 CRÍTICA]
Entregables: ARCHITECTURE.md, CONTRACTS v1, system_manifest.json
Criterio: documentos base aprobados por Director

### FASE 1 — CORE + RUNTIME MÍNIMO [P0]
Entregables: core engine, execution loop, task handler
Criterio: DAG ejecuta 1 ficha real

### FASE 2 — EVENT SYSTEM + STATE [P1]
Entregables: event bus, state manager, snapshots
Criterio: State persiste y recupera tras fallo

### FASE 3 — VALIDACIÓN + OBSERVABILIDAD [P1]
Entregables: validation layer N0-N5, logging, métricas
Criterio: todo artifact pasa N0-N5

### FASE 4 — ROBUSTEZ + SEGURIDAD [P1]
Entregables: security layer, sandboxing, error handling
Criterio: GCL v1.0 gate final F4 activo

### FASE 5 — ESCALADO [P2]
📌 POSPONER — solo si el sistema lo necesita.

MILESTONES: M1:Core | M2:Runtime | M3:Event+State | M4:Observable | M5:Escalable
