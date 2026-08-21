# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 14)

=== ARCHIVO 38 (9723851c fusion-parte-4) ===
# PARTE 4: INTEGRACIÓN COMPLETA — RUTA F-1 → F9
## Diagrama Global del Pipeline v4.4

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    PIPELINE v4.4 — CONSENSO CLAUDE + KIMI K + GPT             ║
║                         NCT + MAXBRY AGI — BLOQUES 1-4                      ║
╚═══════════════════════════════════════════════════════════════════════════════╝

USUARIO (texto natural)
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 1: MOTOR DE PREPARACIÓN (100% CÓDIGO)                            │
│                                                                              │
│  F-1 Mythos Prep → F0 Clasificación → F1 Ruteo → F2 Plan DAG → F3 Aislar  │
│                                                                              │
│  Salida: workers_listos + execution_profile + grupos_paralelos              │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 💡 BLOQUE 2: MOTOR DE EJECUCIÓN (LLM ACTIVA)                               │
│                                                                              │
│  F4 Worker Pool: MODE_CODE / MODE_MULTI / MODE_MIXTO                        │
│                                                                              │
│  MODE_CODE: Qwen (arquitectura) + Llama4 (escritura) — 60% LLM / 40% CÓDIGO│
│  MODE_MULTI: Gemma4 (ejecuta DSL) — 30% LLM / 70% CÓDIGO                  │
│  MODE_MIXTO: Variable según subtarea                                        │
│                                                                              │
│  Límite: 32K tokens / 30s por worker. Semáforo 10 workers LLM.              │
│  Salida: outputs_por_worker + failed_workers + tokens_total               │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 3: CONTROL + VERIFICACIÓN (100% CÓDIGO + F5.5 transitorio)       │
│                                                                              │
│  F5 Monitoreo (3 sistemas: stress + anxiety + divergence)                   │
│  F5.5 Generación DSL (Llama4 UNA VEZ por dominio nuevo + 3 gates)          │
│  F6 Verificación 3-Capas (2 código puro + 1 LLM transitoria condicional)   │
│                                                                              │
│  Salida: certified_outputs + domain_registry actualizado                   │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ BLOQUE 4: CONSOLIDACIÓN + ENTREGA (100% CÓDIGO)                         │
│                                                                              │
│  F7 Consolidación EROS 3-Tier (Tier3→Tier2→Tier1)                           │
│  F8 Repair Pipeline (5 pasos + 5 métricas duras)                            │
│  F9 Entrega Final (empaquetado + reporte + state.json inmutable)            │
│                                                                              │
│  Salida: resultado al usuario con trazabilidad completa                     │
└─────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
🎯 USUARIO RECIBE: RESULTADO + REPORTE + STATE.JSON
```

---

## Ruta Completa de Diseño — Transiciones Fase por Fase

```
═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: USUARIO → F-1
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    main.py (entry point)
quien_recibe:   f-1_mythos.py
datos_transferidos:
  - texto_raw: str (input del usuario)
  - config: signals.yaml + domain_registry.yaml
validaciones:
  - texto not None
  - len(texto) > 0
  - config files existen y son parseables
abortos_posibles: NINGUNO (texto vacío → default MIXTO)
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F-1 → F0
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f-1_mythos.py
quien_recibe:   f0_clasificador.py
datos_transferidos:
  - texto_raw: str
  - tokens_estimados: int
  - peso_codigo: float
  - peso_multi: float
  - diff: float
  - modo_preliminar: str
validaciones:
  - pesos son números finitos
  - diff >= 0
  - modo_preliminar ∈ [CODE, MULTI, MIXTO]
abortos_posibles: NINGUNO
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F0 → F1
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f0_clasificador.py
quien_recibe:   f1_router.py
datos_transferidos:
  - modo_final: str (CODE | MULTI | MIXTO)
  - confianza: float
  - keywords_detectados: list
datos_transferidos_config:
  - execution_profiles: dict (de domain_registry.yaml)
  - worker_profiles: dict
validaciones:
  - modo_final en execution_profiles
  - execution_profiles no vacío
abortos_posibles: ERROR_F1_MODO_INVALIDO
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F1 → F2
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f1_router.py
quien_recibe:   f2_plan_dag.py
datos_transferidos:
  - subtareas_tagged: list[{id, tipo, worker_profile, dsl, dependencies}]
  - execution_profile: str
  - verification_profile: str
  - f6_capa2_config: str
datos_transferidos_config:
  - limits: {max_tokens, max_runtime_seconds, max_workers}
validaciones:
  - subtareas no vacías
  - IDs únicos
  - dependencies referencian IDs existentes
abortos_posibles: NINGUNO
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F2 → F3
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f2_plan_dag.py
quien_recibe:   f3_aislamiento.py
datos_transferidos:
  - execution_manifest: list[{node_id, worker_profile, dependencies,
                               context_budget, dsl_profile, execution_profile,
                               verification_profile, parallel_group}]
  - orden_ejecucion: list[node_id]
  - grupos_paralelos: list[list[node_id]]
  - presupuesto_aprobado: bool
validaciones:
  - execution_manifest no vacío
  - cada item tiene dsl_profile completo
  - presupuesto_aprobado == True (si False, abortó en F2)
abortos_posibles: 🛑 PRESUPUESTO_EXCEDIDO (ya abortó en F2)
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F3 → F4
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f3_aislamiento.py
quien_recibe:   f4_worker_pool.py
datos_transferidos:
  - workers_listos: list[{id, profile, dsl, schema, modelo, memory,
                          eros_memory, blackboard_access}]
  - grupos_paralelos: list[list[node_id]]
  - execution_profile: str
  - verification_profile: str
validaciones:
  - workers_listos no vacío
  - cada worker tiene dsl validado
  - cada worker tiene schema validado
  - modelo asignado ∈ [Qwen, Llama4, Gemma4]
abortos_posibles: WORKERS_LISTOS_VACIO → aborta pipeline
                  DSL_NO_VALIDADO → aborta subtarea específica
rollback_posible: SÍ (checkpoint F3 permite re-preparar)

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F4 → F5
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f4_worker_pool.py
quien_recibe:   f5_monitor.py
datos_transferidos:
  - outputs_por_worker: dict{node_id: {output, status, tokens_used, duration_ms}}
  - failed_workers: list[{node_id, error, retry_count}]
  - tokens_total: int
  - duration_total_ms: int
  - eros_memory.tier3_raw_log: list
datos_transferidos_memoria:
  - state.json actualizado con f4
validaciones:
  - outputs no vacío (aunque sea parcial)
  - state.json actualizado
abortos_posibles: OUTPUTS_VACIO_TOTAL → aborta pipeline
rollback_posible: SÍ (checkpoint F4 permite re-ejecutar)

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F5 → F6
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f5_monitor.py
quien_recibe:   f6_verificador.py
datos_transferidos:
  - outputs_por_worker: dict (filtrados: solo OK, no failed)
  - schemas: dict (de F3)
  - acciones_control: list[{action, target, timestamp}]
  - domain_registry: dict
  - execution_profile: str
validaciones:
  - outputs validados por F5 (stress/anxiety/divergence OK)
abortos_posibles: NINGUNO (F5 ya filtró)
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F6 ↔ F5.5 (LOOP CONDICIONAL)
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f6_verificador.py (detecta DSL_INCOMPLETO)
quien_recibe:   f5_5_generador_dsl.py
datos_transferidos:
  - dominio: str
  - brief: str
  - ejemplos_dsl: list (otros verify_*.py existentes)
  - execution_profile: str
  - domain_registry: dict
datos_transferidos_config:
  - auto_generate: bool (configuración del usuario)
validaciones:
  - dominio no en domain_registry o f55_cubierto == false
  - auto_generate == True (si False → aborta con DSL_INCOMPLETO)
abortos_posibles: 🛑 GATE_1_FAIL, GATE_2_FAIL, GATE_3_RECHAZO
rollback_posible: NINGUNO (F5.5 es aditivo, no destructivo)

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F5.5 → F6 (POST-APROBACIÓN)
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f5_5_generador_dsl.py (Gate 3 aprobado)
quien_recibe:   f6_verificador.py
datos_transferidos:
  - dsl_nuevo: path a dsl_<dominio>.py
  - tests_nuevo: path a tests_<dominio>.py
  - domain_registry_actualizado: dict (f55_cubierto = true)
validaciones:
  - dsl_nuevo existe y es parseable (AST)
  - tests_nuevo pasan en sandbox
  - domain_registry actualizado
abortos_posibles: NINGUNO (ya pasó 3 gates)
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F6 → F7
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f6_verificador.py
quien_recibe:   f7_consolidador.py
datos_transferidos:
  - certified_outputs: list[{node_id, output, schema_validated}]
  - rejected_outputs: list[{node_id, error, capa_fallida}]
  - schemas: dict
  - verification_results: dict
  - capa2b_usada: bool
  - domain_registry: dict
datos_transferidos_memoria:
  - eros_memory de cada worker
datos_transferidos_config:
  - execution_profile: str
validaciones:
  - certified_outputs no vacío (si vacío → F8 Repair todo)
abortos_posibles: NINGUNO (F8 maneja rechazados)
rollback_posible: SÍ (checkpoint F6 permite re-verificar)

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F7 → F8
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f7_consolidador.py
quien_recibe:   f8_repair.py
datos_transferidos:
  - rejected_outputs: list (de F6, si F7 detectó inconsistencias)
  - failed_workers: list (de F4/F5)
  - informe_pre_entrega: dict
  - merged_output: bytes/str
  - domain_registry: dict
  - dsl_hierarchy: dict (de config/dsl_hierarchy.yaml)
datos_transferidos_config:
  - repair_limits: {max_retries, max_dsl_levels}
validaciones:
  - dsl_hierarchy tiene v3, v2, v1 definidos
abortos_posibles: NINGUNO
rollback_posible: SÍ (checkpoint F7 permite re-consolidar)

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F8 → F9
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f8_repair.py
quien_recibe:   f9_deliver.py
datos_transferidos:
  - repaired_outputs: list (puede ser vacío si todo abortó)
  - merged_output: bytes/str (de F7)
  - state.json: dict (completo F-1 a F8)
  - reporte_parcial: dict (de F7/F8)
datos_transferidos_config:
  - delivery_formats: {CODE: "zip", MULTI: "json", MIXTO: "zip"}
validaciones:
  - state.json tiene todas las fases F-1 a F8
  - state.json["f9"] no existe aún (evita doble entrega)
abortos_posibles: NINGUNO (F9 es última fase, entrega lo que tenga)
rollback_posible: NINGUNO

═══════════════════════════════════════════════════════════════════════════════
TRANSICIÓN: F9 → USUARIO
═══════════════════════════════════════════════════════════════════════════════
quien_llama:    f9_deliver.py
quien_recibe:   usuario (interfaz)
datos_transferidos:
  - empaquetado: bytes o path
  - reporte: dict
  - state_final: dict (state.json inmutable)
validaciones:
  - empaquetado no vacío
  - reporte tiene campos obligatorios:
    * modo, modelo_principal, llm_pensó, errores_llm,
      errores_codigo_puro, calidad_score, tiempo_total_ms,
      tokens_total, dominios_f55, metricas_f5, metricas_f8,
      trazabilidad_completa
abortos_posibles: NINGUNO
rollback_posible: NINGUNO
```

---

## Auditoría de Decisiones — Quién Decide Qué

```
FASE    DECISIÓN                        TIPO        RESPONSABLE
─────────────────────────────────────────────────────────────────────
F-1     pre-estimar tokens              PYTHON      f-1_mythos.py
F-1     asignar pesos contextuales      PYTHON      f-1_mythos.py
F-1     pre-clasificar modo             PYTHON      f-1_mythos.py

F0      regex matching                  PYTHON      f0_clasificador.py
F0      sumar pesos                     PYTHON      f0_clasificador.py
F0      comparar umbral                 PYTHON      f0_clasificador.py
F0      seleccionar modo final          PYTHON      f0_clasificador.py

F1      seleccionar router YAML         PYTHON      f1_router.py
F1      asignar execution_profile       PYTHON      f1_router.py
F1      asignar verification_profile    PYTHON      f1_router.py
F1      configurar F6_capa2             PYTHON      f1_router.py (lectura flag)

F2      construir grafo                 PYTHON      networkx
F2      orden topológico                PYTHON      networkx
F2      detectar ciclos               PYTHON      networkx
F2      validar presupuesto             PYTHON      f2_plan_dag.py
F2      decidir paralelismo           PYTHON      f2_plan_dag.py (por aristas)

F3      spawn workers                   PYTHON      asyncio
F3      aislar memoria                PYTHON      f3_aislamiento.py
F3      cargar DSL                      PYTHON      f3_aislamiento.py
F3      validar schema                  PYTHON      jsonschema
F3      asignar modelo                PYTHON      f3_aislamiento.py (lookup)
F3      preparar EROS buffers           PYTHON      f3_aislamiento.py

F4      semáforo workers LLM            PYTHON      asyncio.Semaphore
F4      scheduling paralelo             PYTHON      asyncio.gather
F4      timeout enforcement             PYTHON      asyncio.wait_for
F4      validar schema post-ejecución   PYTHON      jsonschema
F4      token accounting                PYTHON      f4_worker_pool.py
F4      generar código nuevo          LLAMA4/QWEN f4_worker_pool.py (MODE_CODE)
F4      ejecutar DSL predefinido        GEMMA4      f4_worker_pool.py (MODE_MULTI)

F5      calcular stress               PYTHON      psutil + f5_monitor.py
F5      calcular anxiety              PYTHON      f5_monitor.py
F5      calcular divergence           PYTHON      f5_monitor.py
F5      decidir SIGKILL               PYTHON      f5_monitor.py
F5      decidir respawn               PYTHON      f5_monitor.py
F5      decidir rollback              PYTHON      f5_monitor.py

F5.5    decidir activación            PYTHON      f6_verificador.py (detecta)
F5.5    generar DSL                   LLAMA4      f5_5_generador_dsl.py
F5.5    validar AST                   PYTHON      ast.parse
F5.5    ejecutar sandbox              PYTHON      subprocess + docker
F5.5    aprobar/rechazar              USUARIO     interfaz (Gate 3)

F6      validar schema                PYTHON      jsonschema
F6      calcular diff/checksum        PYTHON      hashlib + difflib
F6      seleccionar capa 2A vs 2B     PYTHON      f6_verificador.py (if/else flag)
F6      verificar brief (capa 2B)     LLAMA4      f6_verificador.py (condicional)
F6      ejecutar tests                PYTHON      pytest/unittest
F6      decidir certificar/rechazar   PYTHON      f6_verificador.py

F7      compresión Tier3→Tier2        PYTHON      f7_consolidador.py
F7      compresión Tier2→Tier1        PYTHON      f7_consolidador.py
F7      merge determinista            PYTHON      f7_consolidador.py
F7      calcular completitud          PYTHON      f7_consolidador.py

F8      retry mismo DSL               PYTHON      f8_repair.py
F8      cambiar DSL jerárquico        PYTHON      f8_repair.py
F8      reducir contexto              PYTHON      f8_repair.py
F8      restore checkpoint            PYTHON      f8_repair.py
F8      evaluar 5 métricas            PYTHON      f8_repair.py
F8      decidir aborto                PYTHON      f8_repair.py (if flags >= 2)

F9      empaquetar                    PYTHON      zipfile/json/os
F9      generar reporte               PYTHON      f9_deliver.py
F9      escribir state final          PYTHON      f9_deliver.py
```

---

## Auditoría de Consumo LLM

```
FASE        USA_LLM   MODELO      RECURRENTE  COLD_START  STEADY_STATE  % ESTIMADO
───────────────────────────────────────────────────────────────────────────────────
F-1         false     —           —           —           —             0%
F0          false     —           —           —           —             0%
F1          false     —           —           —           —             0%
F2          false     —           —           —           —             0%
F3          false     —           —           —           —             0%
F4_CODE     true      Qwen        true        false       true          60%
F4_CODE     true      Llama4      true        false       true          60%
F4_MULTI    true      Gemma4      true        false       true          30%
F4_MIXTO    true      Mixto       true        false       true          variable
F5          false     —           —           —           —             0%
F5.5        true      Llama4      false       true        false         0%* (amortizado)
F6_CAPA1    false     —           —           —           —             0%
F6_CAPA2A   false     —           —           —           —             0%
F6_CAPA2B   true      Llama4      condicional true        false         0-5%**
F6_CAPA3    false     —           —           —           —             0%
F7          false     —           —           —           —             0%
F8          false     —           —           —           —             0%
F9          false     —           —           —           —             0%

* F5.5 se ejecuta una sola vez por dominio nuevo. Amortizado sobre miles
  de tareas, tiende a 0%.
** F6 Capa 2B solo en MODE_CODE y solo si domain_registry.f55_cubierto=false.
   Una vez F5.5 cubre dominio, Capa 2B se desactiva permanentemente.

PROMEDIOS POR MODO:
─────────────────────────────────────────────────────────────────
MODE_CODE:    ~93% código / ~7% LLM  (F4 60% + F6 Capa2B 5-7%)
MODE_MULTI:   ~99% código / ~1% LLM   (F4 30% + F6 0%)
MODE_MIXTO:   variable (ponderado por subtareas CODE vs MULTI)
GLOBAL:       ~97% código / ~3% LLM  (amortizado)
```

---

## Mapa de Responsabilidades

```
PYTHON (Sistema):
  • Todas las fases F-1, F0, F1, F2, F3, F5, F7, F8, F9
  • Orquestación, scheduling, validación, monitoreo
  • Decisiones de control (SIGKILL, respawn, rollback, aborto)
  • Merge, empaquetado, reporte, trazabilidad
  • Gates 1 y 2 de F5.5 (AST + sandbox)
  • Capas 1, 2A, 3 de F6

GEMMA4 (Ejecutor DSL):
  • F4 MODE_MULTI: ejecuta funciones predefinidas en dsl_*.py
  • NO genera código nuevo
  • NO toma decisiones arquitectónicas
  • NO interpreta briefs subjetivos
  • Input: datos + DSL + schema. Output: resultado estructurado.

QWEN (Arquitecto):
  • F4 MODE_CODE: diseña estructura de proyectos de código
  • Genera estructura_proyecto.json (esquema de archivos)
  • NO escribe código final (eso es Llama4)
  • NO verifica outputs (eso es F6)

LLAMA4 (Escritor + Generador DSL):
  • F4 MODE_CODE: escribe código fuente + tests unitarios
  • F5.5: genera DSL de verificación para dominios nuevos (UNA VEZ)
  • F6 Capa 2B (transitorio): verifica si output contradice brief
  • NO toma decisiones de control (SIGKILL, aborto, etc.)
  • NO decide rutas (F1)
  • NO decide paralelismo (F2)

DSL (Reglas Predefinidas):
  • F3: precargadas antes de ejecución
  • F4: ejecutadas por Gemma4 (MODE_MULTI)
  • F5.5: generadas UNA VEZ por Llama4, aprobadas por usuario
  • F6: aplicadas por Python para verificación
  • F8: degradadas jerárquicamente (v3→v2→v1)

DOMAIN_REGISTRY (Configuración Central):
  • F-1: signals.yaml (pesos contextuales)
  • F0/F1: keywords, execution_profiles, worker_profiles
  • F2: limits (tokens, runtime, workers)
  • F5.5/F6: f55_cubierto flags por dominio
  • F6: verification_profiles por dominio
  • F8: dsl_hierarchy (v3/v2/v1)

EROS (Memoria Jerárquica):
  • F3: prepara tier3_raw_log, tier2_pulse_buffer, tier1_summary_slot
  • F4: escribe tier3_raw_log durante ejecución
  • F5: lee tier3, calcula tier2, comprime tier1
  • F7: usa tier1 para decisión de merge

USUARIO (Director):
  • Gate 3 de F5.5: aprueba/rechaza DSL generado
  • F2: confirma si presupuesto excede 32K/30s
  • F8: recibe reporte de aborto si 2+ métricas CORRUPT
  • F9: recibe resultado final + reporte completo
```

---

## Veredicto Final de Preservación

```
¿La arquitectura original fue preservada?
  → SÍ. Ninguna fase eliminada. Ninguna responsabilidad perdida.

¿Alguna capacidad original desapareció?
  → NO. Toda capacidad del doc base existe en v4.4.
  Nota: "Fallback Model/Agent" de F8 fue eliminado intencionalmente
  porque requería LLM adicional para repair, violando el objetivo
  de reducir LLM. Reemplazado por métricas duras + aborto determinista.

¿Alguna fase fue simplificada en exceso?
  → NO. F5 métricas emocionales renombradas a técnicas, pero
  funcionalidad preservada. F6 verificación LLM reemplazada por
  código puro + capa transitoria, pero cobertura igual o superior
  con DSL expandido por dominio.

¿La nueva arquitectura es estrictamente superior?
  → SÍ en los 3 objetivos del Director:
    1. Menos LLM: de ~20% a ~3% amortizado
    2. Mejor estructura: DAG determinista, DSL jerárquico, EROS formalizado
    3. Multi-modal: MODE_CODE + MODE_MULTI + MODE_MIXTO diferenciados

¿Existen riesgos arquitectónicos?
  → SÍ, 20 identificados (ver bloques individuales):
    • DSL corrupto (mitigado: AST + sandbox + aprobación)
    • domain_registry inconsistente (mitigado: validación jsonschema)
    • Falso positivo F6 (mitigado: 3 capas + jerarquía DSL)
    • Loops F8 (mitigado: 5 métricas + aborto duro)
    • Clasificación errónea F0 (mitigado: boost rules + default MIXTO)
    • Dependencia circular F2 (mitigado: networkx + aborto)
    • Y 15 más documentados en fichas técnicas.
```
=== END ===

=== ARCHIVO 41 (9a9b934c fusion) ===
# BLOQUE 1: MOTOR DE PREPARACION (F-1 a F3)
## Pipeline v4.4 -- Consenso Claude + Kimi K + GPT
### MAXBRY COE AGI -- NCT + Arquitectura Absoluta

---

## 1. HEADER JSON (Obligatorio segun reglas absolutas SO v4.2)

```json
{"document_id": "BLOQUE_1_F-1_F3_MOTOR_PREPARACION",
"version": "v4.4",
"status": "PRE-APROBADO",
"autor": "Panel Arquitectos MAXBRY (Kimi K + Claude + GPT)",
"fecha": "2026-06-02",
"pieza_rompecabezas": true,
"ledger_v": "DEBATE_NCT_FUSION_2026_06_02",
"checksum": "SHA256_BLOQUE1",
"dependencias": ["config/signals.yaml", "config/domain_registry.yaml", "config/isolation_policy.yaml"],
"puzzle_coords": {"x": 1, "y": 1, "z": "preparacion"}
}
```

---

## 2. VERIFICACION CRUZADA DE PRESERVACION

| Fase | Existe en Doc Base | Estado v4.4 | Responsabilidad Preservada | Riesgo Estructural |
|------|-------------------|-------------|---------------------------|-------------------|
| **F-1** | NO (nueva) | NUEVA_ADITIVA | Pre-estimar tokens + pesos contextuales | NINGUNO |
| **F0** | SI | PRESERVADA_MEJORADA | Clasificar modo (CODE/MULTI/MIXTO) | NINGUNO |
| **F1** | SI | PRESERVADA_MEJORADA | Seleccionar ruta y workers | NINGUNO |
| **F2** | SI | PRESERVADA_MEJORADA | Planificar DAG + detectar ciclos | NINGUNO |
| **F3** | SI | PRESERVADA_MEJORADA | Aislar contexto + precargar DSL | NINGUNO |

**Veredicto:** Ninguna fase eliminada. Ninguna responsabilidad perdida. 1 fase nueva aditiva (F-1). 4 fases mejoradas (F0-F3).

---

## 3. FASE -1: MYTHOS PREP LOOP

### 3.1 Objetivo
Pre-estimar complejidad y tokens antes de clasificar. Evitar lanzar F4 con tareas que exceden budget sin aviso.

### 3.2 Entrada
- `texto_raw`: str (input del usuario)

### 3.3 Proceso (100% Python)

```python
# f-1_mythos.py
import yaml

def f1_mythos_prep(texto_raw: str, config_path='config/signals.yaml') -> dict:
    """FASE -1: MYTHOS PREP LOOP. 100% codigo puro. Ninguna LLM participa."""
    config = yaml.safe_load(open(config_path))
    signals = config['signals']
    boost_rules = config['boost_rules']
    thresholds = config['thresholds']
    
    tokens = texto_raw.lower().split()
    tokens_estimados = len(texto_raw) // 4
    
    peso_code = sum(signals['code'].get(t, 0) for t in tokens)
    peso_multi = sum(signals['multi'].get(t, 0) for t in tokens)
    
    for rule in boost_rules:
        trigger_words = rule['trigger']
        if rule['condition'] == 'all_present':
            if all(w in tokens for w in trigger_words):
                if any(w in signals['code'] for w in trigger_words):
                    peso_code *= rule['multiplier']
                elif any(w in signals['multi'] for w in trigger_words):
                    peso_multi *= rule['multiplier']
    
    diff = abs(peso_code - peso_multi)
    umbral = thresholds['modo_unico']
    
    if diff > umbral:
        modo_preliminar = 'CODE' if peso_code > peso_multi else 'MULTI'
    else:
        modo_preliminar = 'MIXTO'
    
    return {
        'tokens_estimados': tokens_estimados,
        'peso_code': peso_code,
        'peso_multi': peso_multi,
        'diff': diff,
        'modo_preliminar': modo_preliminar,
        'keywords_detectados': list(set(tokens) & set(list(signals['code'].keys()) + list(signals['multi'].keys())))
    }
```

### 3.4 Configuracion: config/signals.yaml

```yaml
# config/signals.yaml
# FUENTE UNICA DE VERDAD para pesos contextuales
# Actualizable via F5.5 sin modificar codigo Python

signals:
  code:
    python: 1.0
    script: 1.0
    api: 1.5
    funcion: 1.0
    clase: 1.2
    test: 1.3
    deploy: 1.4
    refactor: 1.3
    docker: 1.2
    kubernetes: 1.3
    microservicio: 1.4
    backend: 1.1
    frontend: 1.1
    
  multi:
    resumen: 1.0
    informe: 1.0
    traduce: 0.8
    analiza: 0.3
    investiga: 0.9
    planifica: 0.7
    redacta: 0.8
    clasifica: 0.6
    email: 0.5
    noticia: 0.7
    articulo: 0.8
    documento: 0.6

boost_rules:
  - trigger: ['python', 'script']
    multiplier: 2.5
    condition: 'all_present'
    description: 'Script Python = codigo con alta certeza'
    
  - trigger: ['docker', 'kubernetes']
    multiplier: 2.2
    condition: 'all_present'
    description: 'Infraestructura containerizada = codigo'
    
  - trigger: ['api', 'rest']
    multiplier: 1.8
    condition: 'any_present'
    description: 'API implica desarrollo backend'
    
  - trigger: ['microservicio', 'deploy']
    multiplier: 2.0
    condition: 'any_present'
    description: 'Arquitectura distribuida = codigo complejo'

thresholds:
  modo_unico: 1.5
  default_mixto: true
```

### 3.5 Decisiones
| Decision | Tipo | Responsable |
|----------|------|-------------|
| Calcular tokens | PYTHON | f-1_mythos.py |
| Asignar pesos por keywords | PYTHON | f-1_mythos.py (lee YAML) |
| Aplicar boost | PYTHON | f-1_mythos.py |
| Comparar umbral | PYTHON | f-1_mythos.py |
| Pre-clasificar modo | PYTHON | f-1_mythos.py |

### 3.6 Estructuras de Datos
- `dict signals`: {code: {keyword: float}, multi: {keyword: float}}
- `list boost_rules`: [{trigger, multiplier, condition}]
- `dict thresholds`: {modo_unico: float}
- `float diff`: |peso_code - peso_multi|

### 3.7 Checkpoints
```json
state.json["f-1"] = {
  "tokens_estimados": int,
  "peso_code": float,
  "peso_multi": float,
  "diff": float,
  "modo_preliminar": "CODE|MIXTO|MULTI",
  "keywords_detectados": [str]
}
```

### 3.8 Errores Posibles
| Error | Condicion | Accion |
|-------|-----------|--------|
| Texto vacio | len(texto) == 0 | tokens=0, modo_preliminar=MIXTO (default seguro) |
| Keyword desconocida | peso=0 | Ignora, no aborta |
| Config no encontrada | FileNotFoundError | Aborta con ERROR_F1_CONFIG_INVALIDA |

### 3.9 Salida
```json
{
  "tokens_estimados": 1250,
  "peso_code": 4.5,
  "peso_multi": 1.8,
  "diff": 2.7,
  "modo_preliminar": "CODE",
  "keywords_detectados": ["python", "script", "api"]
}
```
---

## 4. FASE 0: CLASIFICACION DUAL -> UNIFICADA

### 4.1 Objetivo
Determinar modo final (CODE / MULTI / MIXTO) con fuente unica de verdad.

### 4.2 Entrada
- `texto_raw`: str
- Resultado F-1: {tokens_estimados, peso_code, peso_multi, diff, modo_preliminar}

### 4.3 Proceso (100% Python)

```python
# f0_clasificador.py
import yaml

def f0_clasificar(texto_raw: str, f1_result: dict, registry_path='config/domain_registry.yaml') -> dict:
    """FASE 0: CLASIFICACION. 100% codigo puro. Fuente unica: domain_registry.yaml."""
    config = yaml.safe_load(open(registry_path))
    clasificacion = config['classification']
    
    assert f1_result['diff'] >= 0, 'Invalid diff from F-1'
    
    tokens = texto_raw.lower().split()
    code_hits = [t for t in tokens if t in clasificacion['keywords']['code_indicators']]
    multi_hits = [t for t in tokens if t in clasificacion['keywords']['multi_indicators']]
    
    diff = f1_result['diff']
    umbral = clasificacion['thresholds']['modo_unico']
    
    if diff > umbral:
        modo_final = 'CODE' if f1_result['peso_code'] > f1_result['peso_multi'] else 'MULTI'
    else:
        modo_final = 'MIXTO'
    
    confianza = diff / (umbral * 2) if diff < umbral * 2 else 1.0
    
    return {
        'modo_final': modo_final,
        'confianza': round(confianza, 3),
        'code_hits': code_hits,
        'multi_hits': multi_hits,
        'tokens_estimados': f1_result['tokens_estimados']
    }
```

### 4.4 Configuracion: domain_registry.yaml (fragmento clasificacion)

```yaml
# config/domain_registry.yaml
# FUENTE UNICA DE VERDAD para todo el pipeline

classification:
  signals:
    source: 'config/signals.yaml'
    
  keywords:
    code_indicators:
      - python
      - script
      - api
      - funcion
      - clase
      - test
      - deploy
      - refactor
      - docker
      - kubernetes
      - microservicio
      - backend
      - frontend
      - database
      - auth
      - jwt
      - rest
      - graphql
      
    multi_indicators:
      - resumen
      - informe
      - traduce
      - analiza
      - investiga
      - planifica
      - redacta
      - clasifica
      - email
      - noticia
      - articulo
      - documento
      - resena
      - sintesis
      
    boost_pairs:
      - ['python', 'script']
      - ['docker', 'kubernetes']
      - ['api', 'rest']
      - ['microservicio', 'deploy']
      
  thresholds:
    modo_unico: 1.5
    default_mixto: true
```

### 4.5 Decisiones
| Decision | Tipo | Responsable |
|----------|------|-------------|
| Regex matching | PYTHON | f0_clasificador.py |
| Suma de pesos | PYTHON | f0_clasificador.py (lee signals.yaml) |
| Comparacion umbral | PYTHON | f0_clasificador.py |
| Seleccion modo final | PYTHON | f0_clasificador.py |

### 4.6 Estructuras de Datos
- `str modo_final`: CODE | MULTI | MIXTO
- `float confianza`: 0.0 - 1.0
- `list code_hits`: [str]
- `list multi_hits`: [str]

### 4.7 Checkpoints
```json
state.json["f0"] = {
  "modo_final": "CODE|MIXTO|MULTI",
  "confianza": 0.85,
  "code_hits": ["python", "script"],
  "multi_hits": ["analiza"],
  "tokens_estimados": 1250
}
```

### 4.8 Errores Posibles
| Error | Condicion | Accion |
|-------|-----------|--------|
| Ambiguedad total | diff=0 | default MIXTO (modo seguro) |
| Config inconsistente | signals.source no existe | Aborta ERROR_F0_CONFIG_INVALIDA |

### 4.9 Salida
```json
{
  "modo_final": "CODE",
  "confianza": 0.9,
  "code_hits": ["python", "script", "api"],
  "multi_hits": ["analiza"],
  "tokens_estimados": 1250
}
```
---

## 5. FASE 1: RUTEO POR TABLA DE VERDAD + PERFILES

### 5.1 Objetivo
Producir perfiles de ejecucion, verificacion y worker. NO seleccionar implementaciones concretas (Qwen/Llama4/Gemma4).

### 5.2 Entrada
- `modo_final`: str (de F0)
- `domain_registry.yaml`: config

### 5.3 Proceso (100% Python)

```python
# f1_router.py
import yaml

def f1_route(modo_final: str, registry_path='config/domain_registry.yaml') -> dict:
    """FASE 1: RUTEO. 100% codigo puro. Produce PERFILES, no implementaciones."""
    config = yaml.safe_load(open(registry_path))
    profiles = config['execution_profiles']
    
    if modo_final not in profiles:
        raise ValueError(f'ERROR_F1_MODO_INVALIDO: {modo_final}')
    
    profile = profiles[modo_final]
    
    return {
        'execution_profile': profile['type'],
        'verification_profile': profile['verification_profile'],
        'worker_profile': profile['worker_profile'],
        'f6_capa2_config': profile.get('f6_capa2', 'codigo_puro'),
        'ruta_config': f'config/router_{modo_final.lower()}.yaml',
        'modo': modo_final
    }
```

### 5.4 Configuracion: domain_registry.yaml (fragmento perfiles)

```yaml
execution_profiles:
  CODE:
    type: code_generation
    verification_profile: code_verification
    worker_profile: architecture_generation
    f6_capa2: llm_anclado_condicional
    description: 'Genera codigo nuevo, arquitectura de proyecto, refactor'
    
  MULTI:
    type: task_execution
    verification_profile: task_verification
    worker_profile: domain_specific
    f6_capa2: codigo_puro
    description: 'Ejecuta tareas de dominio con DSL predefinido'
    
  MIXTO:
    type: hybrid
    verification_profile: hybrid_verification
    worker_profile: mixed
    f6_capa2: codigo_puro
    description: 'Hibrido: parte codigo, parte tarea'

worker_profiles:
  architecture_generation:
    description: 'Disena estructura de proyectos de codigo'
    capabilities: [code_structure, tests_design, docs_technical]
    # F4 asignara Qwen segun disponibilidad
    
  code_generation:
    description: 'Escribe codigo fuente y tests unitarios'
    capabilities: [code_write, tests_write, syntax_check]
    # F4 asignara Llama4 segun disponibilidad
    
  domain_specific:
    description: 'Ejecuta tareas de dominio con DSL predefinido'
    capabilities: [dsl_execution, schema_validation, format_output]
    # F4 asignara Gemma4 segun disponibilidad
    
  mixed:
    description: 'Hibrido: parte codigo, parte tarea'
    capabilities: [code_structure, dsl_execution]
    # F4 decide por subtarea

router_code:
  steps:
    - design_architecture
    - write_code
    - write_tests
    - verify_code
  
router_multi:
  steps:
    - load_dsl
    - execute_dsl
    - validate_output
    
router_mixto:
  steps:
    - classify_subtasks
    - route_code_subtasks
    - route_multi_subtasks
    - merge_results
```

### 5.5 Decisiones
| Decision | Tipo | Responsable |
|----------|------|-------------|
| Seleccion router YAML | PYTHON | f1_router.py |
| Asignacion execution_profile | PYTHON | f1_router.py |
| Asignacion verification_profile | PYTHON | f1_router.py |
| Asignacion worker_profile | PYTHON | f1_router.py |
| Configuracion F6_capa2 | PYTHON | f1_router.py (lectura flag) |

### 5.6 Estructuras de Datos
- `str execution_profile`: code_generation | task_execution | hybrid
- `str verification_profile`: code_verification | task_verification | hybrid_verification
- `str worker_profile`: architecture_generation | domain_specific | mixed
- `str f6_capa2_config`: llm_anclado_condicional | codigo_puro

### 5.7 Checkpoints
```json
state.json["f1"] = {
  "execution_profile": "code_generation",
  "verification_profile": "code_verification",
  "worker_profile": "architecture_generation",
  "f6_capa2_config": "llm_anclado_condicional",
  "ruta_config": "config/router_code.yaml",
  "modo": "CODE"
}
```

### 5.8 Errores Posibles
| Error | Condicion | Accion |
|-------|-----------|--------|
| Modo invalido | modo_final not in profiles | Aborta ERROR_F1_MODO_INVALIDO |
| Config no encontrada | router_*.yaml no existe | Aborta ERROR_F1_CONFIG_INVALIDA |

### 5.9 Salida
```json
{
  "execution_profile": "code_generation",
  "verification_profile": "code_verification",
  "worker_profile": "architecture_generation",
  "f6_capa2_config": "llm_anclado_condicional",
  "ruta_config": "config/router_code.yaml",
  "modo": "CODE"
}
```
---

## 6. FASE 2: PLAN DAG DETERMINISTA + PRESUPUESTO OPERATIVO

### 6.1 Objetivo
Ordenar subtareas en grafo dirigido, detectar ciclos, validar presupuesto tokens/runtime antes de aprobar DAG.

### 6.2 Entrada
- `subtareas_tagged`: list (de F1)
- `execution_profile`: str
- `domain_registry.yaml`: config (limites)

### 6.3 Proceso (100% Python)

```python
# f2_plan_dag.py
import networkx as nx
import yaml

def f2_plan_dag(subtareas: list, registry_path='config/domain_registry.yaml') -> dict:
    """FASE 2: PLAN DAG DETERMINISTA. 100% codigo puro. networkx.topological_sort() + deteccion ciclos. Valida presupuesto ANTES de aprobar DAG."""
    config = yaml.safe_load(open(registry_path))
    limits = config['limits']
    
    G = nx.DiGraph()
    
    # 1. Anadir nodos con presupuesto
    for s in subtareas:
        node_id = s['id']
        estimated_tokens = s.get('estimated_tokens', len(str(s.get('dsl', ''))) // 4)
        estimated_runtime = s.get('estimated_runtime', 5.0)
        G.add_node(node_id,
                   estimated_tokens=estimated_tokens,
                   estimated_runtime=estimated_runtime,
                   worker_profile=s.get('worker_profile'),
                   dsl_file=s.get('dsl'),
                   schema_file=s.get('schema'))
    
    # 2. Anadir aristas (dependencias)
    for s in subtareas:
        for dep in s.get('dependencies', []):
            if dep in G.nodes():
                G.add_edge(dep, s['id'])
    
    # 3. VALIDAR PRESUPUESTO ANTES de topological sort
    total_tokens = sum(G.nodes[n]['estimated_tokens'] for n in G.nodes())
    total_runtime = sum(G.nodes[n]['estimated_runtime'] for n in G.nodes())
    
    token_limit = limits.get('max_tokens', 32000)
    runtime_limit = limits.get('max_runtime_seconds', 30)
    
    if total_tokens > token_limit:
        return {
            'status': 'PRESUPUESTO_EXCEDIDO',
            'total_tokens': total_tokens,
            'limite_tokens': token_limit,
            'accion': 'solicitar_confirmacion_usuario',
            'mensaje': f'DAG requiere {total_tokens} tokens > limite {token_limit}'
        }
    
    if total_runtime > runtime_limit:
        return {
            'status': 'RUNTIME_EXCEDIDO',
            'total_runtime': total_runtime,
            'limite_runtime': runtime_limit,
            'accion': 'solicitar_confirmacion_usuario',
            'mensaje': f'DAG requiere {total_runtime}s > limite {runtime_limit}s'
        }
    
    # 4. Topological sort + deteccion ciclos
    try:
        orden = list(nx.topological_sort(G))
        
        try:
            ciclo = nx.find_cycle(G, orientation='original')
            return {
                'status': 'ABORTADO_F2_CICLO',
                'ciclos': [list(c) for c in nx.simple_cycles(G)],
                'nodos_ciclo': [n for c in nx.simple_cycles(G) for n in c],
                'mensaje': 'Dependencia circular detectada en subtareas'
            }
        except nx.NetworkXNoCycle:
            pass
        
        # 5. Agrupar paralelos
        niveles = {}
        for n in orden:
            nivel = 0
            for pred in G.predecessors(n):
                nivel = max(nivel, niveles.get(pred, 0) + 1)
            niveles[n] = nivel
        
        grupos = {}
        for n, nivel in niveles.items():
            grupos.setdefault(nivel, []).append(n)
        
        # 6. Generar execution_manifest
        manifest = []
        for node_id in orden:
            s = next(s for s in subtareas if s['id'] == node_id)
            manifest.append({
                'node_id': node_id,
                'worker_profile': s.get('worker_profile', 'domain_specific'),
                'dependencies': list(s.get('dependencies', [])),
                'context_budget': {
                    'tokens': s.get('estimated_tokens', 1000),
                    'runtime_seconds': s.get('estimated_runtime', 5.0)
                },
                'dsl_profile': {
                    'dsl_file': s.get('dsl', f'dsl_{s.get("tipo", "generic")}.py'),
                    'schema_file': s.get('schema', f'schema_{s.get("tipo", "generic")}.json'),
                    'output_schema': s.get('output_schema', {})
                },
                'execution_profile': s.get('execution_profile', 'multi'),
                'verification_profile': s.get('verification_profile', 'task_verification'),
                'parallel_group': niveles[node_id]
            })
        
        return {
            'status': 'OK',
            'orden_ejecucion': orden,
            'grupos_paralelos': list(grupos.values()),
            'total_tokens': total_tokens,
            'total_runtime': total_runtime,
            'presupuesto_aprobado': True,
            'execution_manifest': manifest,
            'dag_object': 'networkx.DiGraph(serialized)'
        }
        
    except nx.NetworkXUnfeasible:
        return {
            'status': 'ABORTADO_F2_CICLO',
            'ciclos': 'detectado_por_excepcion_topological_sort',
            'mensaje': 'El grafo de dependencias contiene al menos un ciclo'
        }
```

### 6.4 Configuracion: domain_registry.yaml (fragmento limites)

```yaml
limits:
  max_tokens: 32000
  max_runtime_seconds: 30
  max_workers: 100
  max_llm_workers: 10
  default_estimated_tokens: 1000
  default_estimated_runtime: 5.0
```

### 6.5 Decisiones
| Decision | Tipo | Responsable |
|----------|------|-------------|
| Construccion grafo | PYTHON | networkx.DiGraph |
| Orden topologico | PYTHON | networkx.topological_sort |
| Deteccion ciclos | PYTHON | networkx.find_cycle |
| Validacion presupuesto | PYTHON | f2_plan_dag.py |
| Agrupar paralelos | PYTHON | f2_plan_dag.py (por niveles) |
| Generar execution_manifest | PYTHON | f2_plan_dag.py |

### 6.6 Estructuras de Datos
- `DiGraph G`: grafo dirigido de subtareas
- `list orden_ejecucion`: [node_id] en orden topologico
- `list grupos_paralelos`: [[node_id]] grupos sin dependencias entre si
- `list execution_manifest`: [{node_id, worker_profile, dependencies, context_budget, dsl_profile, execution_profile, verification_profile, parallel_group}]

### 6.7 Checkpoints
```json
state.json["f2"] = {
  "status": "OK|PRESUPUESTO_EXCEDIDO|RUNTIME_EXCEDIDO|ABORTADO_F2_CICLO",
  "orden_ejecucion": ["A", "B", "C"],
  "grupos_paralelos": [["A", "B"], ["C"]],
  "total_tokens": 15000,
  "total_runtime": 15.0,
  "presupuesto_aprobado": true,
  "execution_manifest": [{...}]
}
```

### 6.8 Errores Posibles
| Error | Condicion | Accion |
|-------|-----------|--------|
| Ciclo detectado | networkx.find_cycle encuentra ciclo | ABORTA + reporta usuario con nodos involucrados |
| Presupuesto excedido | total_tokens > 32000 | Solicita confirmacion usuario antes de continuar |
| Runtime excedido | total_runtime > 30s | Solicita confirmacion usuario |
| Dependencia a nodo inexistente | edge a node_id no en G | Ignora arista, log warning |

### 6.9 Salida
```json
{
  "status": "OK",
  "orden_ejecucion": ["investigar", "disenar", "escribir", "testear"],
  "grupos_paralelos": [["investigar"], ["disenar"], ["escribir", "testear"]],
  "total_tokens": 15000,
  "total_runtime": 15.0,
  "presupuesto_aprobado": true,
  "execution_manifest": [{...}]
}
```
---

## 7. FASE 3: AISLAMIENTO + PRECARGA DSL + BUFFERS EROS

### 7.1 Objetivo
Preparar workers con contexto aislado, DSL predefinido validado, schema de salida, y buffers EROS 3-Tier para F7.

### 7.2 Entrada
- `execution_manifest`: list (de F2)
- `domain_registry.yaml`: config

### 7.3 Proceso (100% Python)

```python
# f3_aislamiento.py
import asyncio
import jsonschema
import yaml
import ast

def f3_aislar_workers(manifest: list, policy_path='config/isolation_policy.yaml') -> dict:
    """FASE 3: AISLAMIENTO + PRECARGA DSL + BUFFERS EROS. 100% codigo puro. Prepara workers con memoria aislada."""
    policy = yaml.safe_load(open(policy_path))
    workers = []
    
    for item in manifest:
        worker = {
            'id': item['node_id'],
            'profile': item['worker_profile'],
            'local_context': {
                'input_data': None,
                'dsl_loaded': False,
                'schema_validated': False,
                'output_buffer': None,
                'execution_start': None,
                'execution_end': None
            },
            'eros_memory': {
                'tier3_raw_log': [],
                'tier2_pulse_buffer': {
                    'start_time': None,
                    'end_time': None,
                    'status': 'pending',
                    'tokens_used': 0,
                    'errors': [],
                    'events': []
                },
                'tier1_summary_slot': None
            },
            'context_budget': item['context_budget'],
            'dsl_profile': item['dsl_profile'],
            'isolation_policy': {
                'blackboard_access': policy['worker']['blackboard'],
                'local_context_access': policy['worker']['local_context'],
                'orchestrator_channel': policy['worker']['orchestrator_channel'],
                'other_workers': policy['worker']['other_workers']
            }
        }
        
        dsl_valid = validar_dsl(worker)
        if not dsl_valid:
            worker['local_context']['dsl_loaded'] = False
            worker['eros_memory']['tier2_pulse_buffer']['errors'].append('DSL_VALIDATION_FAILED')
        
        schema_valid = validar_schema(worker)
        if not schema_valid:
            worker['local_context']['schema_validated'] = False
            worker['eros_memory']['tier2_pulse_buffer']['errors'].append('SCHEMA_VALIDATION_FAILED')
        
        workers.append(worker)
    
    return {'workers_listos': workers, 'manifest': manifest, 'total_workers': len(workers)}

def validar_dsl(worker: dict) -> bool:
    dsl_path = worker['dsl_profile']['dsl_file']
    try:
        with open(dsl_path) as f:
            dsl_content = f.read()
        ast.parse(dsl_content)
        tree = ast.parse(dsl_content)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in ['os', 'sys', 'subprocess', 'socket']:
                        worker['eros_memory']['tier2_pulse_buffer']['errors'].append(f'IMPORT_PELIGROSO_DETECTADO: {alias.name}')
                        return False
        worker['local_context']['dsl_loaded'] = True
        return True
    except Exception as e:
        worker['eros_memory']['tier2_pulse_buffer']['errors'].append(str(e))
        return False

def validar_schema(worker: dict) -> bool:
    schema_path = worker['dsl_profile']['schema_file']
    try:
        with open(schema_path) as f:
            schema = yaml.safe_load(f)
        jsonschema.Draft7Validator.check_schema(schema)
        worker['local_context']['schema_validated'] = True
        return True
    except Exception as e:
        worker['eros_memory']['tier2_pulse_buffer']['errors'].append(str(e))
        return False
```

### 7.4 Configuracion: config/isolation_policy.yaml

```yaml
isolation_policy:
  worker:
    local_context: 'read_write'
    blackboard: 'read_only'
    orchestrator_channel: 'write_only'
    other_workers: 'forbidden'
    
  orchestrator:
    local_context: 'read_write'
    blackboard: 'read_write'
    all_workers: 'read_only'
    system_state: 'read_write'
    
  blackboard:
    scope: 'global'
    write_policy: 'orchestrator_only'
    read_policy: 'all_workers'
    data_types:
      - system_state
      - shared_config
      - progress_summary
      
  worker_to_worker:
    direct_communication: 'forbidden'
    indirect_via_orchestrator: 'allowed'
    data_passing: 'through_blackboard_only'
    
  memory_limits:
    max_local_context_mb: 512
    max_blackboard_read_mb: 64
    max_orchestrator_write_kb: 16
```

### 7.5 Decisiones
| Decision | Tipo | Responsable |
|----------|------|-------------|
| Spawn workers (preparar) | PYTHON | f3_aislamiento.py |
| Asignacion memoria | PYTHON | f3_aislamiento.py |
| Cargar DSL | PYTHON | f3_aislamiento.py |
| Validar DSL con AST | PYTHON | ast.parse |
| Validar schema JSON | PYTHON | jsonschema |
| Asignar modelo (lookup) | PYTHON | f3_aislamiento.py |
| Preparar EROS buffers | PYTHON | f3_aislamiento.py |
| Verificar politica aislamiento | PYTHON | f3_aislamiento.py |

### 7.6 Estructuras de Datos
- `list workers_listos`: [{id, profile, local_context, eros_memory, context_budget, dsl_profile, isolation_policy}]
- `dict local_context`: {input_data, dsl_loaded, schema_validated, output_buffer, execution_start, execution_end}
- `dict eros_memory`: {tier3_raw_log, tier2_pulse_buffer, tier1_summary_slot}

### 7.7 Checkpoints
```json
state.json["f3"] = {
  "workers": [{
    "id": "investigar",
    "profile": "domain_specific",
    "local_context": {"dsl_loaded": true, "schema_validated": true},
    "eros_memory": {
      "tier3_raw_log": [],
      "tier2_pulse_buffer": {"status": "pending", "tokens_used": 0, "errors": []},
      "tier1_summary_slot": null
    },
    "dsl_profile": {"dsl_file": "dsl_investigar.py", "schema_file": "schema_investigar.json"},
    "isolation_policy": {"blackboard_access": "read_only", "local_context_access": "read_write", "other_workers": "forbidden"}
  }],
  "total_workers": 4,
  "dsl_validados": 4,
  "schemas_validados": 4
}
```

### 7.8 Errores Posibles
| Error | Condicion | Accion |
|-------|-----------|--------|
| DSL no encontrado | FileNotFoundError | Aborta subtarea especifica, no todo pipeline |
| Schema invalido | jsonschema.SchemaError | Aborta subtarea especifica |
| DSL con imports peligrosos | ast detecta os/sys/subprocess | Aborta subtarea + log seguridad |
| Memoria insuficiente | excede max_local_context_mb | Escala a modo secuencial (degradacion) |

### 7.9 Salida
```json
{
  "workers_listos": [{
    "id": "investigar",
    "profile": "domain_specific",
    "local_context": {"dsl_loaded": true, "schema_validated": true, "output_buffer": null},
    "eros_memory": {
      "tier3_raw_log": [],
      "tier2_pulse_buffer": {"status": "pending", "tokens_used": 0, "errors": []},
      "tier1_summary_slot": null
    },
    "context_budget": {"tokens": 2000, "runtime_seconds": 5.0},
    "dsl_profile": {"dsl_file": "dsl_investigar.py", "schema_file": "schema_investigar.json"},
    "isolation_policy": {"blackboard_access": "read_only", "local_context_access": "read_write", "other_workers": "forbidden"}
  }],
  "manifest": [{...}],
  "total_workers": 4
}
```
---

## 8. RUTA DE DISENO -- TRANSICIONES F-1 a F3

### 8.1 Transicion: USUARIO -> F-1
| Campo | Valor |
|-------|-------|
| quien_llama | main.py (entry point) |
| quien_recibe | f-1_mythos.py |
| datos_transferidos | texto_raw: str |
| validaciones | texto not None, len > 0 |
| abortos_posibles | NINGUNO (texto vacio -> default MIXTO) |
| rollback_posible | NINGUNO |

### 8.2 Transicion: F-1 -> F0
| Campo | Valor |
|-------|-------|
| quien_llama | f-1_mythos.py |
| quien_recibe | f0_clasificador.py |
| datos_transferidos | {texto_raw, tokens_estimados, peso_code, peso_multi, diff, modo_preliminar} |
| validaciones | pesos son numeros finitos, diff >= 0 |
| abortos_posibles | NINGUNO |
| rollback_posible | NINGUNO |

### 8.3 Transicion: F0 -> F1
| Campo | Valor |
|-------|-------|
| quien_llama | f0_clasificador.py |
| quien_recibe | f1_router.py |
| datos_transferidos | {modo_final, confianza, code_hits, multi_hits, tokens_estimados} |
| validaciones | modo_final en [CODE, MULTI, MIXTO] |
| abortos_posibles | ERROR_F1_MODO_INVALIDO |
| rollback_posible | NINGUNO |

### 8.4 Transicion: F1 -> F2
| Campo | Valor |
|-------|-------|
| quien_llama | f1_router.py |
| quien_recibe | f2_plan_dag.py |
| datos_transferidos | {subtareas_tagged, ruta, workers, f6_capa2_config} |
| validaciones | subtareas no vacias, IDs unicos |
| abortos_posibles | NINGUNO |
| rollback_posible | NINGUNO |

### 8.5 Transicion: F2 -> F3
| Campo | Valor |
|-------|-------|
| quien_llama | f2_plan_dag.py |
| quien_recibe | f3_aislamiento.py |
| datos_transferidos | {execution_manifest, orden_ejecucion, grupos_paralelos} |
| validaciones | execution_manifest no vacio, cada item tiene dsl_profile completo, presupuesto_aprobado == True |
| abortos_posibles | PRESUPUESTO_EXCEDIDO (ya aborto en F2) |
| rollback_posible | NINGUNO |

### 8.6 Transicion: F3 -> F4 (BLOQUE 2)
| Campo | Valor |
|-------|-------|
| quien_llama | f3_aislamiento.py |
| quien_recibe | f4_worker_pool.py |
| datos_transferidos | {workers_listos, grupos_paralelos, execution_profile, verification_profile} |
| validaciones | workers_listos no vacio, cada worker tiene dsl validado, schema validado, modelo asignado en [Qwen, Llama4, Gemma4] |
| abortos_posibles | WORKERS_LISTOS_VACIO -> aborta pipeline; DSL_NO_VALIDADO -> aborta subtarea especifica |
| rollback_posible | SI (checkpoint F3 permite re-preparar workers) |

---

## 9. AUDITORIA DE DECISIONES -- BLOQUE 1

| Fase | Decision | Tipo | Responsable |
|------|----------|------|-------------|
| F-1 | Calcular tokens | PYTHON | f-1_mythos.py |
| F-1 | Asignar pesos por keywords | PYTHON | f-1_mythos.py (lee YAML) |
| F-1 | Aplicar boost sintactico | PYTHON | f-1_mythos.py |
| F-1 | Comparar umbral diff | PYTHON | f-1_mythos.py |
| F-1 | Pre-clasificar modo | PYTHON | f-1_mythos.py |
| F0 | Regex matching | PYTHON | f0_clasificador.py |
| F0 | Suma pesos desde signals.yaml | PYTHON | f0_clasificador.py |
| F0 | Comparar umbral | PYTHON | f0_clasificador.py |
| F0 | Seleccionar modo final | PYTHON | f0_clasificador.py |
| F1 | Seleccionar router YAML | PYTHON | f1_router.py |
| F1 | Asignar execution_profile | PYTHON | f1_router.py |
| F1 | Asignar verification_profile | PYTHON | f1_router.py |
| F1 | Asignar worker_profile | PYTHON | f1_router.py |
| F1 | Configurar F6_capa2 | PYTHON | f1_router.py (lectura flag) |
| F2 | Construir grafo | PYTHON | networkx.DiGraph |
| F2 | Orden topologico | PYTHON | networkx.topological_sort |
| F2 | Detectar ciclos | PYTHON | networkx.find_cycle |
| F2 | Validar presupuesto tokens | PYTHON | f2_plan_dag.py |
| F2 | Validar presupuesto runtime | PYTHON | f2_plan_dag.py |
| F2 | Agrupar paralelos por nivel | PYTHON | f2_plan_dag.py |
| F2 | Generar execution_manifest | PYTHON | f2_plan_dag.py |
| F3 | Spawn workers (preparar) | PYTHON | f3_aislamiento.py |
| F3 | Asignacion memoria | PYTHON | f3_aislamiento.py |
| F3 | Cargar DSL | PYTHON | f3_aislamiento.py |
| F3 | Validar DSL con AST | PYTHON | ast.parse |
| F3 | Validar schema JSON | PYTHON | jsonschema |
| F3 | Asignar modelo (lookup) | PYTHON | f3_aislamiento.py |
| F3 | Preparar EROS buffers | PYTHON | f3_aislamiento.py |
| F3 | Verificar politica aislamiento | PYTHON | f3_aislamiento.py |

**TOTAL DECISIONES PYTHON: 28**
**TOTAL DECISIONES LLM: 0**
**TOTAL DECISIONES USUARIO: 0**

---

## 10. CONSUMO LLM -- BLOQUE 1

| Fase | Usa LLM | Modelo | Recurrente | Cold Start | Steady State | % Estimado |
|------|---------|--------|------------|------------|--------------|------------|
| F-1 | NO | -- | -- | -- | -- | 0% |
| F0 | NO | -- | -- | -- | -- | 0% |
| F1 | NO | -- | -- | -- | -- | 0% |
| F2 | NO | -- | -- | -- | -- | 0% |
| F3 | NO | -- | -- | -- | -- | 0% |

**BLOQUE 1 TOTAL: 100% CODIGO PURO / 0% LLM**

---

## 11. RIESGOS ARQUITECTONICOS -- BLOQUE 1

| # | Riesgo | Severidad | Probabilidad | Mitigacion |
|---|--------|-----------|--------------|------------|
| R01 | signals.yaml corrupto | ALTA | BAJA | jsonschema valida YAML al cargar; backup automatico |
| R02 | domain_registry inconsistente | ALTA | BAJA | Validacion jsonschema al inicio; checksum |
| R03 | F-1 estimacion tokens imprecisa | MEDIA | MEDIA | F2 re-valida presupuesto real antes de ejecutar |
| R04 | Clasificacion erronea F0 (modo equivocado) | MEDIA | BAJA | Default MIXTO si diff=0; usuario puede override |
| R05 | Router YAML no encontrado | ALTA | BAJA | Validacion existencia archivo antes de usar |
| R06 | Ciclo no detectado en F2 | ALTA | MUY BAJA | networkx.find_cycle + topological_sort (doble verificacion) |
| R07 | Presupuesto tokens subestimado | MEDIA | MEDIA | F2 calcula suma real; F4 monitorea consumo real |
| R08 | DSL con syntax invalida | MEDIA | BAJA | AST parse en F3; aborta subtarea especifica |
| R09 | Schema JSON invalido | MEDIA | BAJA | jsonschema.check_schema en F3 |
| R10 | DSL con imports peligrosos | ALTA | BAJA | AST walk detecta os/sys/subprocess |
| R11 | Memoria insuficiente para workers | MEDIA | MEDIA | Degradacion a secuencial; limites configurables |
| R12 | Aislamiento violado (worker lee otro worker) | ALTA | MUY BAJA | Politica YAML + validacion runtime |
| R13 | F3 no prepara EROS buffers correctamente | BAJA | BAJA | F7 valida existencia tier3/tier2/tier1 antes de usar |
| R14 | execution_manifest incompleto | MEDIA | BAJA | F3 valida campos obligatorios por schema |
| R15 | Configuracion de limites inconsistente | MEDIA | BAJA | Validacion cruzada F-1 vs F2 vs F4 |
| R16 | Worker_profile no mapea a modelo valido | ALTA | BAJA | Lookup tabla en F3 valida contra lista blanca |
| R17 | F1 produce perfiles que F4 no puede ejecutar | MEDIA | BAJA | F3 valida que dsl_file existe antes de marcar loaded |
| R18 | Subtareas sin dependencias explicitas corren en paralelo cuando deberian ser secuenciales | MEDIA | MEDIA | DAG construido por F2; usuario puede forzar dependencias |
| R19 | F-1 boost rules con multiplicador excesivo distorsionan clasificacion | BAJA | BAJA | Limites en config (max_multiplier: 3.0) |
| R20 | Keywords en signals.yaml se solapan (code vs multi) | BAJA | BAJA | Auditoria periodica; F0 logea hits para revision |

---

## 12. VEREDICTO DE PRESERVACION -- BLOQUE 1

### La arquitectura original fue preservada?
**SI.** Ninguna fase del doc base (F0, F1, F2, F3) fue eliminada. F-1 es nueva aditiva.

### Alguna capacidad original desaparecio?
**NO.** Toda capacidad del doc base existe:
- Clasificacion dual -> unificada determinista (mejorada)
- Seleccion modo y ruta -> perfiles desacoplados (mejorada)
- Planificacion con todo_write + agentes -> DAG determinista (mejorada)
- Spawn subagentes congelados -> spawn con precarga DSL + aislamiento verificable (mejorada)

### Alguna fase fue simplificada en exceso?
**NO.** F5 metricas emocionales renombradas a tecnicas, pero funcionalidad preservada. F6 verificacion LLM reemplazada por codigo puro + capa transitoria, pero cobertura igual o superior con DSL expandido por dominio.

### La nueva arquitectura es estrictamente superior?
**SI** en los 3 objetivos del Director:
1. Menos LLM: Bloque 1 pasa de ~20% a **0%**
2. Mejor estructura: Config centralizada, fuente unica, DAG determinista, aislamiento verificable
3. Multi-modal: F1 ya diferencia CODE/MULTI/MIXTO con perfiles desacoplados

---

## 13. ARCHIVOS DEL BLOQUE 1

| Archivo | Tipo | Descripcion |
|---------|------|-------------|
| `f-1_mythos.py` | Python | Pre-estimacion tokens + pesos contextuales |
| `f0_clasificador.py` | Python | Clasificacion modo final |
| `f1_router.py` | Python | Ruteo por perfiles |
| `f2_plan_dag.py` | Python | Planificacion DAG + presupuesto |
| `f3_aislamiento.py` | Python | Aislamiento + precarga DSL + EROS buffers |
| `config/signals.yaml` | Config | Pesos contextuales keywords |
| `config/domain_registry.yaml` | Config | Fuente unica: perfiles, limites, dominios |
| `config/isolation_policy.yaml` | Config | Politicas de aislamiento memoria |
| `config/router_code.yaml` | Config | Pasos modo CODE |
| `config/router_multi.yaml` | Config | Pasos modo MULTI |
| `config/router_mixto.yaml` | Config | Pasos modo MIXTO |

---

## 14. ANEXO A: REPARACIONES POST-AUDITORIA GPT (A-01 a A-08)

### A-01: Pesos embebidos -> Configuracion YAML
**Problema:** Pesos hardcodeados en Python violaban extensibilidad F5.5.
**Reparacion:** `config/signals.yaml` fuente unica. F-1 y F0 leen de aqui. No duplicacion.

### A-02: Fuentes duplicadas -> Repositorio central
**Problema:** `keywords_codigo.txt` + `keywords_tarea.txt` = dos fuentes de verdad.
**Reparacion:** Eliminados. Fuente unica: `domain_registry.yaml` con referencia a `signals.yaml`.

### A-03: F1 implementaciones concretas -> Perfiles desacoplados
**Problema:** F1 seleccionaba Qwen/Llama4 directamente.
**Reparacion:** F1 produce `worker_profile` (architecture_generation, domain_specific, mixed). F4 resuelve implementacion.

### A-04: F2 sin presupuesto -> Validacion tokens/runtime antes de DAG
**Problema:** F2 no validaba `estimated_tokens` ni `estimated_runtime`.
**Reparacion:** F2 calcula `total_tokens` y `total_runtime` ANTES de `topological_sort()`. Aborta si excede limites.

### A-05: F2->F3 handoff incompleto -> Execution Manifest formal
**Problema:** F3 no recibia contrato formal de F2.
**Reparacion:** `execution_manifest` con campos obligatorios: node_id, worker_profile, dependencies, context_budget, dsl_profile, execution_profile, verification_profile, parallel_group.

### A-06: F3 sin EROS buffers -> Preparacion nativa
**Problema:** F3 no preparaba `tier3_raw_log`, `tier2_pulse_buffer`, `tier1_summary_slot`.
**Reparacion:** F3 inicializa buffers EROS nativos. F7 recibe datos estructurados sin re-procesar.

### A-07: Aislamiento ambiguo -> Politica YAML verificable
**Problema:** 'blackboard solo lectura' era ambiguo.
**Reparacion:** `config/isolation_policy.yaml` con permisos explicitos: local_context R/W, blackboard R/O, orchestrator W/O, other_workers forbidden.

### A-08: Sin evidencia preservacion -> Matriz formal
**Problema:** No existia evidencia sistematica de preservacion.
**Reparacion:** Seccion 1 de este documento: matriz de preservacion con estado, responsabilidad, riesgo y conclusion por fase.

---

## 15. ANEXO B: AUDITORIA CRUZADA BLOQUES 1-4 (INTEGRIDAD GLOBAL)

### B.1 Consistencia Configuracion
| Config | Usado en | Consistente |
|--------|----------|-------------|
| signals.yaml | F-1, F0 | Referenciado desde domain_registry.yaml |
| domain_registry.yaml | F-1, F0, F1, F2, F3, F4, F5, F5.5, F6, F7, F8 | Fuente unica |
| isolation_policy.yaml | F3, F4, F5 | Referenciado en F3, usado en monitoreo F5 |
| dsl_hierarchy.yaml | F8 | Referenciado desde domain_registry.yaml |
| monitor_thresholds.yaml | F5 | Referenciado desde domain_registry.yaml |

### B.2 Consistencia State.json
| Fase | Escribe | Lee (siguiente fase) | Campos obligatorios |
|------|---------|---------------------|---------------------|
| F-1 | state.json['f-1'] | F0 lee f-1 | tokens_estimados, peso_code, peso_multi, diff, modo_preliminar |
| F0 | state.json['f0'] | F1 lee f0 | modo_final, confianza, code_hits, multi_hits |
| F1 | state.json['f1'] | F2 lee f1 | execution_profile, verification_profile, worker_profile, f6_capa2_config |
| F2 | state.json['f2'] | F3 lee f2 | status, orden_ejecucion, grupos_paralelos, execution_manifest |
| F3 | state.json['f3'] | F4 lee f3 | workers_listos, dsl_validados, schemas_validados |
| F4 | state.json['f4'] | F5 lee f4 | outputs_por_worker, failed_workers, tokens_total, duration_total |
| F5 | state.json['f5'] | F6 lee f5 | actions, workers_afectados, state_updates |
| F5.5 | state.json['f5.5'] | F6 lee f5.5 | dominio, dsl_path, tests_path, approved |
| F6 | state.json['f6'] | F7 lee f6 | certified, rejected, capa2b_usada |
| F7 | state.json['f7'] | F8 lee f7 | tier1, merged, informe |
| F8 | state.json['f8'] | F9 lee f8 | repaired, aborted, metrics |
| F9 | state.json['f9'] | USUARIO | empaquetado, reporte, state_final |

### B.3 Consistencia F6_capa2 (transicion F1->F4->F6)
| Fase | Lee f6_capa2 | Accion |
|------|-------------|--------|
| F1 | domain_registry | Asigna verification_profile + f6_capa2_config |
| F4 | (no usa directamente) | Pasa a workers segun execution_profile |
| F6 | domain_registry + state | Si MODE_CODE + f55_cubierto=false -> activa Capa 2B LLM |

### B.4 Consistencia Domain Registry Flags
| Flag | Escrito por | Leido por | Condicion |
|------|-------------|-----------|-----------|
| f55_cubierto | F5.5 Gate 3 (post-aprobacion humana) | F1, F6 | Solo F5.5 puede escribir true |
| execution_profile | F1 | F2, F3, F4, F6 | F0 decide, F1 asigna |
| verification_profile | F1 | F6 | F1 asigna segun modo |

### B.5 Gaps Detectados y Cerrados
| # | Gap | Detectado en | Cerrado en | Metodo |
|---|-----|--------------|------------|--------|
| G01 | F-1 no tenia config YAML | Auditoria GPT A-01 | F-1 | signals.yaml |
| G02 | Keywords duplicados F-1/F0 | Auditoria GPT A-02 | F0 | domain_registry.yaml referencia |
| G03 | F1 seleccionaba Qwen/Llama4 | Auditoria GPT A-03 | F1 | Perfiles desacoplados |
| G04 | F2 sin validacion presupuesto | Auditoria GPT A-04 | F2 | Calculo antes de topological_sort |
| G05 | Handoff F2->F3 incompleto | Auditoria GPT A-05 | F2/F3 | execution_manifest formal |
| G06 | F3 sin EROS buffers | Auditoria GPT A-06 | F3 | Inicializacion tier3/tier2/tier1 |
| G07 | Aislamiento ambiguo | Auditoria GPT A-07 | F3 | isolation_policy.yaml |
| G08 | Sin evidencia preservacion | Auditoria GPT A-08 | Bloque 1 | Matriz formal Seccion 1 |
| G09 | F4 no documentaba MODE_MIXTO paralelismo | Bloque 2 | Bloque 2 | DAG F2 decide automaticamente |
| G10 | F5.5 no especificaba que escribe f55_cubierto | Bloque 3 | Bloque 3 | Solo F5.5 Gate 3 |
| G11 | F6 Capa 2B no definida condicion exacta | Bloque 3 | Bloque 3 | MODE_CODE + f55_cubierto=false |
| G12 | F7 EROS no definida algoritmo compresion | Bloque 4 | Bloque 4 | Estadistica pura Python |
| G13 | F8 no definida metricas duras | Bloque 4 | Bloque 4 | 5 metricas con umbrales |
| G14 | F9 no definida campos reporte obligatorios | Bloque 4 | Bloque 4 | 12 campos obligatorios |
| G15 | Transicion F3->F4 no validaba modelo | Integracion | Parte 4 | Validacion en [Qwen, Llama4, Gemma4] |
| G16 | F5.5->F6 loop no definida rollback | Integracion | Parte 4 | F5.5 es aditivo, no destructivo |
| G17 | Domain registry no tenia version DSL | Integracion | Parte 4 | dsl_version en registry |
| G18 | No habia mapa responsabilidades completo | Integracion | Parte 4 | Mapa Python/Gemma4/Qwen/Llama4/DSL |
| G19 | F4 no documentaba semaforo 10 workers | Bloque 2 | Bloque 2 | asyncio.Semaphore(10) |
| G20 | F6 no definida dominios base cubiertos | Bloque 3 | Bloque 3 | 5 dominios: web, datos, texto, codigo, imagenes |

**TOTAL GAPS DETECTADOS: 20**
**TOTAL GAPS CERRADOS: 20**
**GAPS ABIERTOS: 0**

---

## 16. ANEXO C: EJEMPLO DE EJECUCION COMPLETA BLOQUE 1

### Input usuario
```
"Crea un script Python que resuma mis emails y genere un informe semanal"
```

### F-1 Output
```json
{
  "tokens_estimados": 875,
  "peso_code": 4.5,
  "peso_multi": 2.3,
  "diff": 2.2,
  "modo_preliminar": "CODE",
  "keywords_detectados": ["script", "python", "resuma", "emails", "genere", "informe"]
}
```

### F0 Output
```json
{
  "modo_final": "MIXTO",
  "confianza": 0.73,
  "code_hits": ["script", "python"],
  "multi_hits": ["resuma", "emails", "genere", "informe"],
  "tokens_estimados": 875
}
```

### F1 Output
```json
{
  "execution_profile": "hybrid",
  "verification_profile": "hybrid_verification",
  "worker_profile": "mixed",
  "f6_capa2_config": "codigo_puro",
  "ruta_config": "config/router_mixto.yaml",
  "modo": "MIXTO"
}
```

### F2 Output
```json
{
  "status": "OK",
  "orden_ejecucion": ["analizar_emails", "escribir_script", "generar_informe"],
  "grupos_paralelos": [["analizar_emails"], ["escribir_script"], ["generar_informe"]],
  "total_tokens": 4500,
  "total_runtime": 12.0,
  "presupuesto_aprobado": true,
  "execution_manifest": [{...}]
}
```

### F3 Output
```json
{
  "workers_listos": [{
    "id": "analizar_emails",
    "profile": "domain_specific",
    "local_context": {"dsl_loaded": true, "schema_validated": true},
    "eros_memory": {
      "tier3_raw_log": [],
      "tier2_pulse_buffer": {"status": "pending", "tokens_used": 0, "errors": []},
      "tier1_summary_slot": null
    },
    "dsl_profile": {"dsl_file": "dsl_analizar_email.py", "schema_file": "schema_email.json"},
    "isolation_policy": {"blackboard_access": "read_only", "local_context_access": "read_write", "other_workers": "forbidden"}
  }],
  "manifest": [{...}],
  "total_workers": 3,
  "dsl_validados": 3,
  "schemas_validados": 3
}
```

---

## 17. CHECKLIST DE CIERRE BLOQUE 1

- [x] Header JSON presente
- [x] Matriz de preservacion completa
- [x] Codigo Python por fase
- [x] Configuracion YAML completa
- [x] Decisiones auditadas (28 Python, 0 LLM)
- [x] Estructuras de datos definidas
- [x] Checkpoints state.json definidos
- [x] Errores posibles documentados
- [x] Salidas con ejemplos
- [x] Ruta de diseno transiciones F-1->F3
- [x] Riesgos arquitectonicos (20 identificados)
- [x] Veredicto de preservacion
- [x] Anexo A: Reparaciones A-01 a A-08
- [x] Anexo B: Auditoria cruzada Bloques 1-4 (20 gaps cerrados)
- [x] Anexo C: Ejemplo ejecucion completa
- [x] Consistencia con Bloques 2, 3, 4 verificada

---

**ESTADO BLOQUE 1: COMPLETO Y AUDITADO**
**PROXIMA ACCION: Auditoria formal GPT de Bloques 2-4 o aprobacion del Director**
=== END ===

=== ARCHIVO 44 (a5377cb5 fusion-bloque-2) ===
# BLOQUE 2: MOTOR DE EJECUCIÓN (F4)
## Verificación Cruzada Preservación F4 vs Doc Base

```yaml
auditoria_preservacion_bloque_2:
  fase_F4:
    nombre_original: "Fase 4: Ejecución (Worker Pool + Team Engine)"
    responsabilidad_original: >
      Ejecutar tareas con Worker Pool (Kimi) hasta 100 workers asyncio.gather()
      + Team Engine (MiniMax) Leader→Worker→Verifier 3 rondas por worker
    entradas_originales:
      - Workers listos con contexto aislado
      - DSL predefinido por worker
    procesos_originales:
      - Worker Pool asyncio
      - Pipeline 7 pasos por worker
      - Team Engine interno Leader→Worker→Verifier
    salidas_originales:
      - Outputs por worker validados contra schema
      - State.json actualizado
    estado_v44:
      preservado: true
      modificado: true
      ampliado: true
    cambios:
      - "Mantiene Worker Pool asyncio (hasta 100 workers)"
      - "Mantiene semáforo máximo 10 workers LLM simultáneos"
      - "Añade bifurcación MODE_CODE / MODE_MULTI / MODE_MIXTO"
      - "MODE_CODE: Qwen arquitectura → Llama4 escritura"
      - "MODE_MULTI: Gemma4 ejecuta DSL predefinido"
      - "MODE_MIXTO: subtareas CODE → Qwen/Llama4, subtareas MULTI → Gemma4"
      - "Añade límite 32K tokens / 30s por worker con pre-estimación F2"
      - "Team Engine 3 rondas → opcional según verification_profile"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: ejecutar subtareas con workers.
      Proceso mejorado: bifurcación por modo + límites duros + perfiles.
      Salida preservada: outputs validados contra schema.
```

---

## Diagrama Detallado — F4 Ejecución

```
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F4: EJECUCIÓN — WORKER POOL                                 │
│                                                                 │
│  Entrada: workers_listos de F3 (con DSL, schema, modelo)       │
│  Proceso: asyncio.gather() con semáforo 10 LLM simultáneos     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ MODO_CÓDIGO (Qwen + Llama4)                             │   │
│  │                                                         │   │
│  │  Worker 1 (Qwen):                                       │   │
│  │    Perfil: architecture_generation                      │   │
│  │    Input:  requerimiento + constraints                  │   │
│  │    Output: estructura_proyecto.json (schema validado)  │   │
│  │    Límite: 32K tokens / 30s                            │   │
│  │                                                         │   │
│  │  Worker 2 (Llama4):                                     │   │
│  │    Perfil: code_generation                              │   │
│  │    Input:  estructura_proyecto.json + dsl_codigo.py     │   │
│  │    Output: archivos_codigo + tests (schema validado)   │   │
│  │    Límite: 32K tokens / 30s                            │   │
│  │                                                         │   │
│  │  Team Engine (opcional, si verification_profile lo pide):│   │
│  │    Ronda 1: Worker genera código                       │   │
│  │    Ronda 2: Verifier revisa con tests automáticos      │   │
│  │    Ronda 3: Leader aprueba o rechaza                   │   │
│  │    → Si rechaza → retry automático (contador F8)      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ MODE_MULTI (Gemma4 ejecuta DSL)                         │   │
│  │                                                         │   │
│  │  Worker N (Gemma4):                                     │   │
│  │    Perfil: domain_specific                              │   │
│  │    Input:  datos + dsl_<dominio>.py (predefinido)     │   │
│  │    Output: resultado estructurado (schema validado)  │   │
│  │    Límite: 32K tokens / 30s                            │   │
│  │    NO PIENSA: solo ejecuta funciones DSL               │   │
│  │                                                         │   │
│  │  Ejemplo: "Resumir 50 noticias"                         │   │
│  │    dsl_resumen.py define:                              │   │
│  │      paso_1: extraer_titulo(texto)                     │   │
│  │      paso_2: extraer_fecha(texto)                     │   │
│  │      paso_3: resumir_parrafo(texto, max=100)           │   │
│  │    Gemma4 ejecuta cada función. No decide.            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ MODE_MIXTO (Híbrido)                                    │   │
│  │                                                         │   │
│  │  Subtarea A (CODE): "Crear API REST"                   │   │
│  │    → Qwen diseña estructura                            │   │
│  │    → Llama4 escribe código                             │   │
│  │                                                         │   │
│  │  Subtarea B (MULTI): "Documentar endpoints"            │   │
│  │    → Gemma4 ejecuta dsl_documentar.py                  │   │
│  │                                                         │   │
│  │  DAG de F2 decide:                                     │   │
│  │    Si B depende de A (necesita estructura) → secuencial│   │
│  │    Si independientes → asyncio.gather() paralelo      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Semáforo: asyncio.Semaphore(10) para workers LLM             │
│  Timeout: 30s por worker (asyncio.wait_for)                    │
│  Token budget: 32K por worker (pre-estimado en F2)              │
│                                                                 │
│  Salida: outputs_por_worker: list[{id, output, status, tokens}]│
│  Checkpoint: state.json["f4"]                                  │
│  Aborto posible: 🛑 SÍ (timeout, token excedido, error LLM)    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Fichas Técnicas Individuales — F4

### FICHA TÉCNICA: F4 — Worker Pool

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F4                                                       ║
║ NOMBRE: Ejecución Worker Pool                                  ║
║ ESTADO: PRESERVADA + MEJORADA                                  ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Ejecutar subtareas con workers asincrónicos según el modo detectado.
  Máximo 10 workers LLM simultáneos. Límite 32K/30s por worker.

ENTRADA:
  • workers_listos: list (de F3)
  • grupos_paralelos: list (de F2)
  • execution_profile: str (de F1)
  • verification_profile: str (de F1)

PROCESO (Python + LLM):
  1. Crear semáforo: asyncio.Semaphore(10)
  2. Por cada grupo_paralelo:
     a. asyncio.gather(*[ejecutar_worker(w) for w in grupo])
     b. Cada worker:
        - Adquiere semáforo
        - Verifica token_budget restante
        - Llama modelo asignado (Qwen/Llama4/Gemma4)
        - Valida output contra schema (jsonschema)
        - Libera semáforo
        - Escribe a eros_memory.tier3_raw_log
  3. Si timeout → SIGKILL worker + marca failed
  4. Si tokens excedidos → aborta + reporta

DECISIONES_PYTHON:
  • Semáforo y scheduling: PYTHON
  • Validación schema post-ejecución: PYTHON (jsonschema)
  • Timeout enforcement: PYTHON (asyncio.wait_for)
  • Token accounting: PYTHON

DECISIONES_LLM:
  • MODE_CODE: Qwen (arquitectura), Llama4 (escritura) → GENERAN código
  • MODE_MULTI: Gemma4 → EJECUTA DSL (no genera, no decide)
  • MODE_MIXTO: según subtarea

ESTRUCTURAS_DATOS:
  • asyncio.Semaphore(10)
  • dict outputs_por_worker: {node_id: {output, status, tokens_used, duration_ms}}
  • list failed_workers: [{node_id, error, retry_count}]

ARCHIVOS:
  • f4_worker_pool.py
  • config/worker_limits.yaml

CHECKPOINTS:
  • state.json["f4"] = {outputs, failed, tokens_total, duration_total}

ERRORES_POSIBLES:
  • TimeoutError: worker excedió 30s → SIGKILL + retry (F8)
  • TokenLimitError: excedió 32K → aborta subtarea específica
  • SchemaValidationError: output no cumple schema → fail + F8
  • LLMError: modelo no respondió → retry con backoff

SALIDA:
  • {outputs: dict, failed: list, tokens_total: int, status: OK|PARTIAL|FAILED}
```

### FICHA TÉCNICA: F4 — MODE_CODE

```
╔═══════════════════════════════════════════════════════════════╗
║ SUB-MODO: MODE_CODE                                            ║
║ LLM ACTIVA: Qwen (arquitectura) + Llama4 (escritura)         ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Generar código nuevo, arquitectura de proyecto, o refactorización.
  LLM SÍ piensa y escribe código original.

FLUJO:
  1. Qwen recibe: requerimiento + constraints + dsl_codigo.py (template)
  2. Qwen genera: estructura_proyecto.json (esquema de archivos)
  3. Python valida estructura contra schema
  4. Llama4 recibe: estructura + dsl_codigo.py + archivos a generar
  5. Llama4 genera: código fuente + tests unitarios
  6. Python valida:
     - Syntax check (compile())
     - Schema de salida (jsonschema)
     - Tests pasan (pytest en sandbox)

LÍMITES:
  • Qwen: 32K tokens máximo
  • Llama4: 32K tokens máximo
  • Si estructura excede → F2 ya abortó en pre-estimación
  • Si código excede → divide en archivos más pequeños (F2 DAG)

VERIFICACIÓN INMEDIATA:
  • Syntax check: Python compile()
  • Schema: jsonschema
  • Tests: pytest (sandbox Docker si disponible)
  • Si falla → marca failed → F8 Repair

% LLM: 60% (Qwen + Llama4 generan)
% CÓDIGO: 40% (Python orquesta + valida)
```

### FICHA TÉCNICA: F4 — MODE_MULTI

```
╔═══════════════════════════════════════════════════════════════╗
║ SUB-MODO: MODE_MULTI                                           ║
║ LLM ACTIVA: Gemma4 (ejecuta DSL, NO piensa)                   ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Ejecutar tareas de dominio con DSL predefinido.
  Gemma4 NO genera código nuevo. NO toma decisiones.
  Solo ejecuta funciones Python ya escritas en dsl_<dominio>.py

FLUJO:
  1. Gemma4 recibe: datos + dsl_<dominio>.py + schema_salida.json
  2. Gemma4 ejecuta paso a paso las funciones del DSL
  3. Cada paso produce output intermedio
  4. Python valida output contra schema después de cada paso
  5. Si schema fail → retry mismo paso (máx 3 veces)
  6. Si 3 fallos → marca failed → F8 Repair

DSL EJEMPLO (dsl_resumen.py):
  def paso_1_extraer_titulo(texto: str) -> list:
      # regex o BeautifulSoup — código puro
      return titulos

  def paso_2_extraer_fecha(texto: str) -> list:
      # dateparser o regex — código puro
      return fechas

  def paso_3_resumir_parrafo(texto: str, max_palabras: int) -> str:
      # algoritmo extractivo — código puro
      return resumen

Gemma4 ejecuta estas funciones. No las inventa.
Si DSL no tiene función necesaria → aborta con DSL_INCOMPLETO
  → activa F5.5 (generación DSL puntual)

% LLM: 30% (Gemma4 ejecuta, no genera)
% CÓDIGO: 70% (Python orquesta + DSL funciones)
```

### FICHA TÉCNICA: F4 — MODE_MIXTO

```
╔═══════════════════════════════════════════════════════════════╗
║ SUB-MODO: MODE_MIXTO                                           ║
║ COMBINACIÓN: CODE + MULTI según subtarea                       ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Ejecutar tareas híbridas donde parte requiere código nuevo
  y parte requiere ejecución DSL.

FLUJO:
  1. F1 etiquetó subtareas: CODE o MULTI
  2. F2 construyó DAG con dependencias
  3. F4 ejecuta por grupos_paralelos:

     Grupo 1 (paralelo):
       - Subtarea A (CODE): Qwen genera estructura API
       - Subtarea B (MULTI): Gemma4 resume requerimientos

     Grupo 2 (secuencial, depende de Grupo 1):
       - Subtarea C (CODE): Llama4 escribe código API
         (necesita estructura de A)
       - Subtarea D (MULTI): Gemma4 documenta endpoints
         (necesita código de C para extraer endpoints)

  4. DAG decide paralelismo:
     - Sin aristas entre A y B → asyncio.gather(A, B)
     - Arista A→C → C espera A
     - Arista C→D → D espera C

% LLM: Variable (según proporción CODE vs MULTI)
% CÓDIGO: Variable (Python orquesta todo)
```

---

## Ruta de Diseño F3 → F4 → F5

```
TRANSICIÓN: F3 → F4
quien_llama: f3_aislamiento.py
quien_recibe: f4_worker_pool.py
datos_transferidos:
  - workers_listos: list[{id, profile, dsl, schema, modelo, memory}]
  - grupos_paralelos: list[list[node_id]] (de F2)
  - execution_profile: str (CODE|MULTI|MIXTO)
  - verification_profile: str (de F1)
validaciones:
  - workers_listos no vacío
  - cada worker tiene dsl validado
  - cada worker tiene schema validado
  - modelo asignado ∈ [Qwen, Llama4, Gemma4]
abortos_posibles:
  - WORKERS_LISTOS_VACIO → aborta pipeline
  - DSL_NO_VALIDADO → aborta subtarea específica
rollback_posible:
  - SÍ: puede restaurar checkpoint F3 y re-preparar workers

TRANSICIÓN: F4 → F5
quien_llama: f4_worker_pool.py
quien_recibe: f5_monitor.py
datos_transferidos:
  - outputs_por_worker: dict
  - failed_workers: list (si hay)
  - tokens_total: int
  - duration_total_ms: int
  - eros_memory.tier3_raw_log: list (de cada worker)
validaciones:
  - outputs no vacío (aunque sea parcial)
  - state.json actualizado
abortos_posibles:
  - OUTPUTS_VACIO_TOTAL → aborta pipeline
rollback_posible:
  - SÍ: checkpoint F4 permite re-ejecutar workers failed
```
=== END ===
