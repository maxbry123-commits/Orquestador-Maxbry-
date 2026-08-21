# DOCUMENTO 14: DETALLES ADICIONALES DEL CHAT
## Extraído del historial del chat

---

## 1. DLG DSL DE NCT (Resumen Adicional)

El DSL es un lenguaje declarativo-generativo en Python donde cada acción de NCT se describe como un módulo con:
- inputs
- outputs
- contract
- dependencies
- consensus_required
- runtime

El motor G2 lee esos módulos y los ejecuta.

### G2 ARTIFACT ENGINE - Componentes del motor DSL:
```
G2 ARTIFACT ENGINE
 ├── DSL          ← sintaxis para escribir módulos
 ├── DAG          ← grafo de dependencias entre módulos
 ├── Contracts    ← esquemas JSON que validan entradas/salidas
 ├── Validators   ← funciones que prueban el contrato
 ├── State Machine← estados del módulo (idle → running → done / fail)
 ├── Memory       ← lectura/escritura en Xata durante ejecución
 └── LLM          ← agente LLM para la parte 10% (con consenso)
```

### Cada pieza cumple un rol fijo:
- DSL dice QUÉ hacer
- DAG dice EN QUÉ ORDEN
- Contracts dice QUÉ FORMA debe tener la entrada/salida
- Validators dice SI ESTÁ BIEN
- State Machine dice EN QUÉ PUNTO está
- Memory dice QUÉ RECUERDA
- LLM dice QUÉ DECIDE cuando hay ambigüedad

### Estructura de un Módulo DSL:

```
MÓDULO NCT
├── id              "nct.creativity.run_consensus"
├── version         "1.0.0"
├── owner_workshop  "NCT-CREATIVIDAD"
├── description     "Corre el consenso de 5 agentes sobre una idea"
├── inputs          { idea: string, max_agents: int = 5 }
├── outputs         { winner: object, runner_up: object, reasoning_log: array }
├── contract        { schema de inputs, schema de outputs }
├── dependencies    [ "nct.creativity.creative_agent", "nct.creativity.critic", ... ]
├── consensus       { required: true, agents: [...], tiebreaker: "selection" }
├── runtime         { sandbox: "wasm-py|docker|process", timeout_s: 120 }
├── memory_keys     [ "nct:project:<id>:creativity:last_run" ]
├── llm_budget      { max_calls: 5, max_tokens_per_call: 4000 }
└── validators      [ "nct.validators.outputs_not_empty", "nct.validators.winner_has_score" ]
```

### Reglas:
- `id` debe ser jerárquico: `nct.<taller>.<verbo>`
- `contract` se valida antes y después de ejecutar; si falla → módulo a `fail`
- `dependencies` se resuelven con el DAG
- `consensus.required = true` significa que el LLM no decide solo
- `memory_keys` son los punteros a Xata
- `llm_budget` limita uso de tokens por módulo

### Mapa Paso → Módulo(s) DSL:

| Paso | Módulo(s) DSL | Taller | Consensus |
|---|---|---|---|
| 0 | nct.capture.append_turn | (transversal) | no |
| 0 | nct.capture.write_context_md | (transversal) | no |
| 1 | nct.frontend.scaffold_app | FRONTEND | sí |
| 1 | nct.design.apply_theme_tokens | DISEÑO | no |
| 2 | nct.history.scan_repo | ARQUITECTURA | no |
| 2 | nct.history.build_timeline | BACKEND | no |
| 2 | nct.history.bridge_to_xata | BACKEND | no |
| 3 | nct.creativity.run_consensus | CREATIVIDAD | sí (5 agentes) |
| 3 | nct.architecture.propose_blueprint | ARQUITECTURA | sí |
| 4 | nct.config.register_api_key | BACKEND | no |
| 4 | nct.config.set_router_policy | BACKEND | no |
| 4 | nct.config.select_default_model | FRONTEND | no |
| 5 | nct.artifact.register_ficha | ARQUITECTURA | no |
| 5 | nct.artifact.execute_in_sandbox | BACKEND | no |
| 5 | nct.artifact.read_from_xata | BACKEND | no |
| 5 | nct.artifact.write_to_xata | BACKEND | no |
| 6 | nct.consensus.configure_per_agent_keys | ARQUITECTURA | no |
| 6 | nct.chat.switch_active_model | FRONTEND | no |
| 7 | nct.github.connect_repo | DEVOPS | no |
| 7 | nct.github.push_branch | DEVOPS | no |
| 7 | nct.xata.bootstrap_schema | BACKEND | no |

### Cómo se define un módulo nuevo:
1. Nombre — elige un id con la jerarquía nct.<taller>.<verbo>
2. Inputs / Outputs — escribe las firmas
3. Contract — define el schema JSON
4. Dependencies — qué otros módulos necesita
5. Consensus — pregúntate si toca diseño/seguridad/UX
6. Runtime — sandbox preferido
7. Memory keys — qué lee/escribe
8. LLM budget — tope conservador
9. Validators — al menos 2
10. Tests — el taller TESTING genera casos

### DAG (grafo de dependencias):
- Si A depende de B, B corre ANTES
- Si B y C no dependen entre sí, corren EN PARALELO
- El orquestador puede inyectar dependencias dinámicas
- Si el DAG tiene ciclos → error de diseño

### State Machine del módulo:
```
        ┌──────┐  inputs OK + deps OK
idle ──►│ ready│──────────────────────► running
        └──────┘                              │
            ▲                                 │
            │ retry                           ▼
            │                            ┌────────┐
        ┌───────┐  contract OK          │  done  │
  fail ◄│failed │◄───────────────────── └────────┘
        └───────┘
            ▲
            │ cualquier error
            │
         running ──► timeout ──► failed
```

### Memoria Xata - Schema mínimo:
- Tabla nct_modules: una fila por módulo registrado
- Tabla nct_runs: una fila por ejecución
- Tabla nct_memory: key-value con scope
- Tabla nct_consensus: una fila por decisión de los 5 agentes

---

## 2. VALIDATORS (TESTS BARATOS)

Dos tipos:

### De contrato (vienen del schema):
- Si el input no es JSON válido o falta un campo → fail

### De negocio (funciones específicas):
- nct.validators.outputs_not_empty
- nct.validators.winner_has_score
- nct.validators.no_secrets_in_outputs (CRÍTICO)
- nct.validators.filenames_are_ascii

---

## 3. UNIVERSAL MODULE CONTRACT v1.5 (JSON Schema)

### Concepto:
Contrato universal de módulos que permite conectar fichas de código, prompts DSL, APIs, MCP, bases de datos, herramientas y LLMs externos mediante una interfaz común.

### Función:
Cada ficha declara:
- Qué consume
- Qué produce
- Cómo se ejecuta
- Bajo qué reglas puede conectarse

### Conexión:
- código
- LLM
- DSL prompt
- API
- MCP
- DB
- tools

### Compatibilidad:
Las fichas se unen automáticamente si sus entradas y salidas son compatibles.

### Seguridad:
Define permisos, límites, sandbox y recuperación.

### Resultado:
Construye pipelines DAG donde cada módulo es una neurona reutilizable.

### Ecosistemas compatibles:
- MAXBRY
- YAIWES
- NCT Neuronas Code Turbo

### Schema principal (campos requeridos):
```json
{
  "artifact_id": "string",
  "artifact_version": "semver",
  "contract_version": "string",
  "contract_hash": "sha256:...",
  "hash_algorithm": "sha256",
  "estado": "draft|testing|active|deprecated|blocked",
  "ciclo_vida": {...},
  "registry_metadata": {...},
  "contrato": {
    "rol": "transform|source|sink",
    "consume": {...},
    "expone": {...},
    "errores": {...},
    "restricciones": {...}
  },
  "naturaleza": {
    "determinista": true,
    "idempotente": true,
    "puro": false,
    "efectos": {...}
  },
  "seguridad": {...},
  "ejecucion": {
    "kind": "code|llm|db|api|tool",
    "transport": "stdio|importlib|http|sdk|prompt|mcp",
    "config": {...},
    "fallback": {...}
  },
  "resultado": {
    "success_schema_uri": "...",
    "error_schema_uri": "...",
    "trace_id_format": "uuid|ulid|snowflake"
  },
  "dependencias": {...},
  "versioning": {
    "min": "semver",
    "max": "semver",
    "mode": "semver_strict|semver_loose|exact"
  },
  "gobernanza_ref": {...}
}
```

---

## 4. CONSENSO DE 5 AGENTES (Detalles de flujo)

```
[1] M3 detecta que una decisión necesita consenso.
    │
    ▼
[2] Genera el prompt DSL cerrado (en .mavi/prompts/consensus.txt).
    El prompt contiene:
    - Problema (del usuario)
    - Contexto del proyecto (del CONTEXT.md)
    - Restricciones (presupuesto, tiempo, stack)
    │
    ▼
[3] M3 spawnea 5 sub-sesiones en paralelo (módulo nct.consensus.run_consensus).
    Cada una recibe:
    - El prompt DSL
    - Su rol (Creative / Innovation / etc.)
    - Su key + modelo
    - Timeout: 60s
    │
    ▼
[4] M3 espera respuestas (timeout global: 90s).
    │
    ├── Si los 5 responden: sigue a [5].
    ├── Si 3-4 responden: sigue con los que hay + marca "quorum parcial".
    └── Si <3 responden: ALERTA + escala al usuario.
    │
    ▼
[5] M3 loguea todo en nct_consensus (Xata):
    {
      "topic": "...",
      "agents_responded": ["creative", "innovation", "critic", "selection", "architecture"],
      "winner": {...},
      "runner_up": {...},
      "reasoning_log": [...],
      "decided_at": "...",
      "decided_by": "consensus"
    }
    │
    ▼
[6] M3 presenta al usuario:
    - Ganadora
    - Runner-up (por si el usuario prefiere)
    - Razonamiento corto del Critic
    - Plano de ejecución del Architecture
    │
    ▼
[7] Usuario aprueba / itera / cancela.
```

### Visualización (lo que el usuario ve):

```
┌──────────────────────────────────────────────────────────────┐
│ CONSENSO EN CURSO                                            │
│ Tema: "Stack para app de journaling"                          │
│                                                              │
│ [Creative]    ✅ Idea 1-5 generadas                          │
│ [Innovation]  ✅ Ideas mejoradas con score                   │
│ [Critic]      ✅ 2 ideas killed, 3 survived                  │
│ [Selection]   ⏳ Eligiendo...                                 │
│ [Architecture] ⏸ Esperando                                   │
│                                                              │
│ Tiempo: 0:23 / 1:30                                          │
└──────────────────────────────────────────────────────────────┘
```

### Después:
```
┌──────────────────────────────────────────────────────────────┐
│ CONSENSO COMPLETADO                                          │
│ Ganadora: "Next.js + Xata + Anthropic con workers"           │
│ Score: 0.82                                                  │
│ Razón: "Más rápido de iterar y mejor DX que alternativas"    │
│                                                              │
│ Plano de ejecución:                                          │
│ 1. Crear repo con plantilla                                  │
│ 2. Configurar Xata                                           │
│ 3. Implementar auth (NextAuth)                               │
│ 4. ...                                                       │
│                                                              │
│ [✅ Aprobar]  [🔄 Iterar]  [❌ Cancelar]                       │
└──────────────────────────────────────────────────────────────┘
```

### Manejo de fallos del consenso:
- Un agente da respuesta vacía → Reintentar 1 vez. Si falla, marcar partial_quorum
- Dos agentes dan contradictorias → Critic media. Si persiste → escala
- Todos proponen lo mismo (sin diversidad) → Creative re-genera con más temperatura
- Score muy bajo → Escala con 2 mejores opciones
- Usuario rechaza → Guardar corrección + ajustar prompt DSL

### Por qué es un SISTEMA y no un prompt:
- Estructura (5 agentes definidos)
- Contratos (formato JSON)
- Estado (qué respondió cada uno, en qué orden)
- Memoria (resultados en Xata)
- Auditoría (todo se loguea)
- Recuperación (si un agente falla, sigue)
- Evolución (correcciones del usuario lo mejoran)

---

## 5. RECUPERACIÓN DEL CHAT (5 HORAS)

### Lo que pasó:
1. M3 recibió muchas salidas con aprobaciones
2. M3 debía crear un parche por cada aprobación
3. M3 se perdió, hizo patches redundantes
4. M3 encontró attachments que no procesó
5. M3 intentó consolidar sin éxito

### Lo que aprendí:
- Cada aprobación = 1 parche
- Max 100K caracteres por documento
- Releer instrucciones cada vez que termino un documento
- Bucle continuo sin detenerse
- Verificación cruzada al final

### Estado actual (junio 2026):
- 170 patches con documentación individual
- 19 archivos Python reales (726 líneas)
- Constitución 1276 líneas
- 13+ documentos consolidados (140+ KB)
- Memoria persistente en 2 topics
</content>