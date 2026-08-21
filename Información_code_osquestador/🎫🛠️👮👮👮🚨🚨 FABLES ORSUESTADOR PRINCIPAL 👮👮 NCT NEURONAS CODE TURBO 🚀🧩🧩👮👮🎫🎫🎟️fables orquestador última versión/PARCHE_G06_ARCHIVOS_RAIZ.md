# PARCHE G06 — ARCHIVOS RAÍZ FALTANTES DEL BRAIN
# UBICACIÓN: Bloque 15-A (Organización SaaS)
# Carpeta: raíz github.com/[PROYECTO]-brain/
# VERSION FINAL

---

## CONTEXTO

Los siguientes 4 archivos estaban referenciados en la
estructura del brain pero sin contenido definido:

- project_manifest.json ← identidad global
- sequence.json         ← fuente única de flujo
- fallback.json         ← jerarquía de recuperación
- state.json            ← Crazy Wall (estado global)

---

## ARCHIVO 1 — project_manifest.json
Propósito: identidad global del proyecto
Diferencia con system_manifest.json:
  system_manifest = técnico (capas, componentes, rutas)
  project_manifest = identidad (quién, qué, cuándo)

```json
{
  "project_id": "MAXBRY_G2",
  "project_name": "MAXBRY",
  "project_version": "1.0",
  "architecture_version": "G2",
  "template_version": "1.0",
  "constitution_version": "1.0",
  "current_phase": "FASE_0_FUNDACION",
  "current_status": "SPEC_COMPLETE",
  "north_star": "Sistema capaz de ejecutar, coordinar y validar procesos complejos de forma modular y controlada",
  "owner": "Director",
  "created_at": "[FECHA]",
  "updated_at": "[FECHA]"
}
```

REGLAS:
- No contiene código
- No contiene contratos
- No contiene tareas
- Solo identidad global
- Actualizar updated_at en cada cambio

---

## ARCHIVO 2 — sequence.json
Propósito: pipeline completo del sistema — FUENTE ÚNICA DE FLUJO
Regla: DAG Engine lee este archivo para construir el grafo
Regla: nada externo define el orden de ejecución
schema_version: "1.0" obligatorio en cada archivo

```json
{
  "sequence_id": "SEQ-001",
  "version": "1.0",
  "schema_version": "1.0",
  "created_at": "[FECHA]",
  "description": "Pipeline principal del sistema",
  "steps": [
    {
      "step_id": "S001",
      "nombre": "inicializar_kernel",
      "tipo": "secuencial",
      "fichas": ["ART-0001"],
      "depends_on": [],
      "critico": true,
      "condition": null,
      "timeout_seg": 30,
      "on_failure": "fallback",
      "tags": ["kernel", "init"]
    },
    {
      "step_id": "S002",
      "nombre": "cargar_artifacts",
      "tipo": "paralelo",
      "fichas": ["ART-0002", "ART-0003"],
      "depends_on": ["S001"],
      "critico": true,
      "condition": null,
      "timeout_seg": 60,
      "on_failure": "fallback",
      "tags": ["runtime", "load"]
    },
    {
      "step_id": "S003",
      "nombre": "ejecutar_pipeline",
      "tipo": "secuencial",
      "fichas": ["ART-0004"],
      "depends_on": ["S002"],
      "critico": false,
      "condition": "state.artifacts_loaded == true",
      "timeout_seg": 120,
      "on_failure": "abort",
      "tags": ["runtime", "execute"]
    }
  ]
}
```

CAMPOS OBLIGATORIOS POR PASO:
- step_id       → identificador único
- nombre        → descripción corta
- tipo          → "secuencial" | "paralelo"
- fichas[]      → lista de artifact_ids
- depends_on[]  → aristas del DAG
- critico       → true = no puede saltarse
- condition     → null | string evaluable con safe_eval
- timeout_seg   → tiempo máximo
- on_failure    → "fallback" | "abort" | "compensate"
- tags[]        → clasificación

REGLA condition (safe_eval con AST):
- Nodos permitidos: ast.Compare, ast.Name, ast.Constant, ast.BoolOp
- ast.Call o ast.Import → SecurityError (anti-inyección)
- null = siempre ejecuta

---

## ARCHIVO 3 — fallback.json
Propósito: jerarquía de recuperación ante fallos
Regla: orquestador consulta este archivo cuando un paso falla
Jerarquía: retry → alternate → abort → compensate

```json
{
  "fallback_id": "FALLBACK-001",
  "version": "1.0",
  "schema_version": "1.0",
  "created_at": "[FECHA]",
  "global_policy": {
    "max_total_retries": 10,
    "escalate_to_director_after": 3,
    "log_all_failures": true
  },
  "levels": [
    {
      "level": 1,
      "nombre": "retry",
      "descripcion": "Reintentar la misma ficha",
      "max_intentos": 3,
      "backoff_ms": "1000 * 2^attempt + random(0, 1000)",
      "jitter": true,
      "condicion": "error_type != SCHEMA_ERROR"
    },
    {
      "level": 2,
      "nombre": "alternate",
      "descripcion": "Usar ficha sustituta definida en contrato",
      "campo_contrato": "sustituible_por",
      "condicion": "sustituible_por != null AND retry_agotado"
    },
    {
      "level": 3,
      "nombre": "abort",
      "descripcion": "Marcar paso como FAIL y congelar",
      "accion": "set_state(step, FAIL) + freeze_pipeline",
      "condicion": "alternate_fallido OR alternate_no_disponible"
    },
    {
      "level": 4,
      "nombre": "compensate",
      "descripcion": "Deshacer efectos de pasos anteriores",
      "accion": "ejecutar compensate_fn() de cada paso completado",
      "condicion": "abort_critico == true"
    }
  ],
  "error_policies": {
    "ERR_HASH":          "retry",
    "ERR_SCHEMA":        "abort",
    "ERR_TIMEOUT":       "retry",
    "ERR_MEMORY":        "abort",
    "ERR_IMPORT":        "abort",
    "ERR_RUNTIME":       "retry",
    "ERR_COMPAT":        "abort",
    "ERR_NOT_FOUND":     "alternate",
    "ERR_NOT_COMMITTED": "abort",
    "ERR_VERSION":       "alternate"
  }
}
```

REGLA JITTER:
  backoff_ms = 1000 * 2^attempt + random(0, 1000)
  Evita thundering herd en retries paralelos.

---

## ARCHIVO 4 — state.json (CRAZY WALL)
Propósito: estado global del sistema — única fuente de verdad
Regla: orquestador escribe SOLO aquí — nunca en código
Regla: escritura atómica — nunca escritura parcial
Regla: append-only con hash chain para auditabilidad

```json
{
  "state_id": "STATE-001",
  "version": "1.0",
  "schema_version": "1.0",
  "created_at": "[FECHA]",
  "updated_at": "[FECHA]",

  "pipeline": {
    "sequence_id": "SEQ-001",
    "estado_global": "RUNNING",
    "fase_actual": "FASE_0_FUNDACION",
    "paso_actual": "S001",
    "paso_anterior": null,
    "paso_siguiente": "S002",
    "iniciado_at": "[TIMESTAMP]",
    "completado_at": null
  },

  "steps": {
    "S001": {
      "estado": "COMPLETED",
      "iniciado_at": "[TIMESTAMP]",
      "completado_at": "[TIMESTAMP]",
      "intentos": 1,
      "error": null
    },
    "S002": {
      "estado": "RUNNING",
      "iniciado_at": "[TIMESTAMP]",
      "completado_at": null,
      "intentos": 1,
      "error": null
    },
    "S003": {
      "estado": "PENDING",
      "iniciado_at": null,
      "completado_at": null,
      "intentos": 0,
      "error": null
    }
  },

  "artifacts": {
    "ART-0001": {
      "estado": "ACTIVE",
      "cargado_at": "[TIMESTAMP]",
      "hash_verificado": true,
      "space": "hf_space_01"
    }
  },

  "errores_activos": [],

  "hash_anterior": "sha256_del_state_anterior",
  "hash_actual": "sha256(state_actual + hash_anterior)"
}
```

ESTADOS VÁLIDOS PIPELINE:
  IDLE | RUNNING | PAUSED | FAILED | COMPLETED

ESTADOS VÁLIDOS PASO:
  PENDING | RUNNING | COMPLETED | FAILED | SKIPPED | COMPENSATED

REGLAS CRAZY WALL:
  ✅ Escritura atómica — todo o nada
  ✅ Hash chain — cada estado referencia el anterior
  ✅ Timestamp en cada cambio
  ✅ Solo el orquestador escribe
  ❌ Nunca escritura parcial
  ❌ Nunca escritura desde agentes
  ❌ Nunca escritura desde LLM

---

## RESUMEN UBICACIONES

```
📂 github.com/[PROYECTO]-brain/
├── system_manifest.json    ← ya definido en DOC6
├── project_index.json      ← ya definido en DOC6
├── project_manifest.json   ← NUEVO (este parche)
└── 📂 flujo/
    ├── sequence.json       ← NUEVO (este parche)
    ├── fallback.json       ← NUEVO (este parche)
    └── state.json          ← NUEVO (este parche)
```

## ORDEN DE LECTURA DEL ORQUESTADOR

1. system_manifest.json    → identidad técnica
2. project_index.json      → índice maestro
3. flujo/sequence.json     → qué ejecutar y en qué orden
4. flujo/state.json        → estado actual del pipeline
5. flujo/fallback.json     → qué hacer si algo falla
6. memoria/recovery_core/  → si hay fallo crítico

REGLA: el orquestador lee estos 5 archivos al inicio.
       No necesita explorar el repo.
       No necesita preguntar al Director.
       Ya sabe todo.
