# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 13)

=== ARCHIVO 11 (31e85428 fusion-bloque-4) ===
# BLOQUE 4: CONSOLIDACIÓN + REPAIR + ENTREGA (F7 + F8 + F9)
## Verificación Cruzada Preservación vs Doc Base

```yaml
auditoria_preservacion_bloque_4:
  fase_F7:
    nombre_original: "Fase 7: Consolidación Jerárquica (EROS 3-Tier + Coordinator)"
    responsabilidad_original: >
      EROS 3-Tier: Tier 3 (Executors) → logs crudos,
      Tier 2 (Controllers) → Strategic Pulses,
      Tier 1 (Orchestrator) → <5% contexto.
      Coordinator (MiniMax) recibe outputs, integra, maneja escalados.
    entradas_originales:
      - Outputs certificados de F6
      - Logs crudos de workers
    procesos_originales:
      - Compresión jerárquica EROS
      - Integración por Coordinator
      - Informe pre-entrega: completitud, drift, etc.
    salidas_originales:
      - Informe pre-entrega consolidado
    estado_v44:
      preservado: true
      modificado: true
      ampliado: true
    cambios:
      - "EROS 3-Tier implementado en código puro (estadística)"
      - "Tier 3 → tier2: resumen estadístico (count, mean, success_rate)"
      - "Tier 2 → tier1: solo métricas críticas <5% contexto"
      - "Coordinator → merge determinista por tipo de tarea"
      - "Añade completitud check: X de Y subtareas listas"
      - "Añade drift detection: divergence_kl residual"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: consolidar resultados de workers.
      Proceso mejorado: compresión jerárquica definida algorítmicamente.
      Salida preservada: informe pre-entrega.

  fase_F8:
    nombre_original: "Fase 8: Repair Pipeline (5 pasos)"
    responsabilidad_original: >
      Paso 1: Retry simple (3 intentos)
      Paso 2: Context Compression (L1/L2)
      Paso 3: Fallback Model / Agent
      Paso 4: Restore Checkpoint
      Paso 5: Escalate (Coordinator decide)
    entradas_originales:
      - Outputs rechazados de F6
      - Workers failed de F4/F5
    procesos_originales:
      - 5 pasos de repair con decisiones del Coordinator
    salidas_originales:
      - Output reparado o aborto final
    estado_v44:
      preservado: true
      modificado: true
      ampliado: true
    cambios:
      - "Paso 1: Retry mismo DSL (3 intentos) — preservado"
      - "Paso 2: Cambia a DSL más simple (jerarquía v3→v2→v1)"
      - "Paso 3: Reduce contexto 50% + re-ejecuta DSL"
      - "Paso 4: Restore checkpoint (snapshot previo) — preservado"
      - "Paso 5: Aborto duro con 5 métricas context_integrity_score"
      - "Elimina 'Fallback Model/Agent' (requería LLM adicional)"
      - "Añade métricas duras para decisión aborto"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: reparar outputs fallidos.
      Proceso mejorado: DSL jerárquico + métricas duras + aborto determinista.
      Salida preservada: output reparado o aborto con reporte.

  fase_F9:
    nombre_original: "Fase 9: Consolidación Final y Entrega"
    responsabilidad_original: >
      Merge resultados + Consistencia global.
      Empaquetado (KIMI_REF + archivos + URLs).
      State.json final: trazabilidad completa.
    entradas_originales:
      - Informe pre-entrega de F7
      - Outputs certificados de F6
    procesos_originales:
      - Merge final
      - Empaquetado
      - State.json final
    salidas_originales:
      - Resultado al usuario
    estado_v44:
      preservado: true
      modificado: false
      ampliado: false
    cambios:
      - "100% código puro preservado"
      - "Reporte JSON automático con métricas completas"
      - "MODE_CODE entrega: código + documentación + tests"
      - "MODE_MULTI entrega: formato por tipo de tarea"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: entregar resultado al usuario.
      Proceso preservado: merge + empaquetado + state final.
      Sin modificaciones. Fase más estable del pipeline.
```

---

## Diagrama Detallado — F7 + F8 + F9

```
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F7: CONSOLIDACIÓN JERÁRQUICA (EROS 3-Tier)                │
│                                                                 │
│  Entrada: certified_outputs de F6 + eros_memory de cada worker│
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ TIER 3: LOGS CRUDOS (de F3/F4/F5)                       │   │
│  │   • eros_memory.tier3_raw_log de cada worker           │   │
│  │   • Formato: [{timestamp, event, data}]                 │   │
│  │   • Tamaño: ~100% del contexto original                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ TIER 2: STRATEGIC PULSES (compresión estadística)       │   │
│  │   • total_workers: len(logs)                            │   │
│  │   • success_rate: OK / total                            │   │
│  │   • avg_duration_ms: mean(durations)                      │   │
│  │   • errors: [error for error in logs if error]          │   │
│  │   • tokens_total: sum(tokens)                           │   │
│  │   • Tamaño: ~20% del contexto original                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ TIER 1: ORQUESTADOR (<5% contexto)                      │   │
│  │   • ok: success_rate >= 0.9                             │   │
│  │   • critical_errors: errors[:3] (solo primeros 3)        │   │
│  │   • duration_ms: avg_duration_ms                        │   │
│  │   • completitud: len(certified) / len(total_workers)    │   │
│  │   • drift_residual: max(divergence_kl residuals)        │   │
│  │   • Tamaño: <5% del contexto original                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  MERGE DETERMINISTA:                                            │
│    • MODE_CODE: concatena archivos de código + tests + docs    │
│    • MODE_MULTI: concatena resultados estructurados JSON         │
│    • MODE_MIXTO: merge por subtarea según tipo                 │
│                                                                 │
│  Salida: {merged_output, tier1_summary, informe_pre_entrega}   │
│  Checkpoint: state.json["f7"]                                    │
│  Aborto posible: 🛑 SÍ (completitud < 50%)                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F8: REPAIR PIPELINE — 100% CÓDIGO                          │
│                                                                 │
│  Entrada: rejected_outputs de F6 + failed_workers de F4/F5     │
│                                                                 │
│  Paso 1: ⚙️ RETRY MISMO DSL (3 intentos)                      │
│    • Re-ejecuta worker con DSL original                        │
│    • Contador: retry_count += 1                                │
│    • Si éxito → reemplaza output rechazado                    │
│    • Si falla 3 veces → Paso 2                                 │
│                              │                                  │
│                              ▼                                  │
│  Paso 2: ⚙️ CAMBIA A DSL MÁS SIMPLE (jerarquía v3→v2→v1)    │
│    • v3_completo: todos campos, validación estricta           │
│    • v2_medio: campos críticos, validación media               │
│    • v1_minimo: solo campo crítico, no vacío                  │
│    • Intenta v2 → si falla → intenta v1                       │
│    • Si v1 falla → Paso 3                                      │
│                              │                                  │
│                              ▼                                  │
│  Paso 3: ⚙️ REDUCE CONTEXTO 50% + RE-EJECUTA                 │
│    • Comprime input_data (trunca, resume, filtra)            │
│    • Re-ejecuta DSL con contexto reducido                     │
│    • Si éxito → output parcial (degradado)                     │
│    • Si falla → Paso 4                                         │
│                              │                                  │
│                              ▼                                  │
│  Paso 4: ⚙️ RESTORE CHECKPOINT (snapshot previo)              │
│    • Recupera state.json de checkpoint anterior                │
│    • Re-ejecuta desde F3 con datos originales                │
│    • Si éxito → output restaurado                              │
│    • Si falla → Paso 5                                         │
│                              │                                  │
│                              ▼                                  │
│  Paso 5: ⚙️ EVALÚA ABORTO CON 5 MÉTRICAS DURAS                │
│    • schema_compliance_rate     < 0.5  → CORRUPT             │
│    • output_divergence_index    > 0.3  → CORRUPT             │
│    • dsl_execution_failure_rate > 0.4  → CORRUPT             │
│    • repair_pattern_stability   true   → CORRUPT             │
│    • token_budget_deviation     > 3.0  → CORRUPT             │
│                                                                 │
│    • 2+ flags CORRUPT → 🛑 ABORTA + reporta usuario          │
│    • 1 flag  → DEGRADED → retry con parámetros alternativos   │
│    • 0 flags → CONTINUA (improbable, pero posible)            │
│                                                                 │
│  Salida: {repaired_outputs: list, aborted: list,              │
│           metrics: dict, status: OK|PARTIAL|ABORTED}           │
│  Checkpoint: state.json["f8"]                                    │
│  Aborto posible: 🛑 SÍ (2+ métricas CORRUPT)                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F9: ENTREGA FINAL — 100% CÓDIGO                            │
│                                                                 │
│  Entrada: merged_output de F7 + repaired de F8                │
│                                                                 │
│  Proceso:                                                       │
│    1. Empaquetado según modo:                                  │
│       • MODE_CODE: zip con código + tests + docs + README      │
│       • MODE_MULTI: JSON estructurado + resumen markdown       │
│       • MODE_MIXTO: zip combinado (código + resultados)          │
│    2. Genera reporte automático (Python, no LLM):              │
│       • Modelo usado: Gemma4 / Llama4 / Qwen / Mixto           │
│       • ¿Usó LLM que piensa? SÍ (solo F4) / NO                 │
│       • Errores LLM detectados: N                              │
│       • Errores código puro: N                                 │
│       • Calidad score: X/100                                    │
│       • Tiempo estimado vs real                                 │
│       • Tokens totales consumidos                               │
│       • Dominios cubiertos por F5.5: list                       │
│       • Métricas F5: stress, anxiety, divergence                │
│       • Métricas F8: repairs, retries, aborts                   │
│    3. Escribe state.json final con trazabilidad completa        │
│       • state.json["f9"] = {timestamp, modo, calidad, métricas}│
│                                                                 │
│  Salida: {empaquetado: path/bytes,                              │
│           reporte: dict,                                        │
│           state_final: dict}                                    │
│                                                                 │
│  Checkpoint: state.json["f9"] (FINAL)                            │
│  Aborto posible: NINGUNO (última fase)                         │
│                                                                 │
│  🎯 USUARIO RECIBE:                                             │
│    • Resultado empaquetado (zip/json/md)                       │
│    • Reporte de ejecución completo                              │
│    • state.json con trazabilidad                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Fichas Técnicas Individuales — F7 + F8 + F9

### FICHA TÉCNICA: F7 — Consolidación EROS

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F7                                                       ║
║ NOMBRE: Consolidación Jerárquica EROS 3-Tier                   ║
║ ESTADO: PRESERVADA + MEJORADA (algoritmo especificado)        ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Comprimir logs de ejecución en 3 niveles y consolidar outputs
  certificados en un resultado final.

ENTRADA:
  • certified_outputs: list (de F6)
  • eros_memory de cada worker (tier3_raw_log)
  • state.json completo

PROCESO (100% Python puro):
  1. TIER 3 → TIER 2 (por worker):
     logs = worker["eros_memory"]["tier3_raw_log"]
     pulse = {
       "total_events": len(logs),
       "ok_events": sum(1 for l in logs if l["status"] == "OK"),
       "error_events": [l for l in logs if l["status"] != "OK"],
       "duration_ms": logs[-1]["timestamp"] - logs[0]["timestamp"]
     }
     worker["eros_memory"]["tier2_pulse_buffer"] = pulse

  2. TIER 2 → TIER 1 (global):
     all_pulses = [w["tier2"] for w in workers]
     summary = {
       "ok": sum(p["ok_events"] for p in all_pulses) / sum(p["total_events"]) >= 0.9,
       "critical_errors": [e for p in all_pulses for e in p["error_events"]][:3],
       "avg_duration_ms": sum(p["duration_ms"] for p in all_pulses) / len(all_pulses),
       "completitud": len(certified_outputs) / len(workers)
     }

  3. MERGE DETERMINISTA:
     if execution_profile == "CODE":
        merged = concat_code_files(certified_outputs)
     elif execution_profile == "MULTI":
        merged = merge_json_outputs(certified_outputs)
     else:  # MIXTO
        merged = merge_by_subtask_type(certified_outputs)

DECISIONES_PYTHON:
  • Compresión estadística: PYTHON
  • Merge: PYTHON (concatenación estructurada)

DECISIONES_LLM:
  • NINGUNA

ESTRUCTURAS_DATOS:
  • dict tier2_by_worker: {id: pulse}
  • dict tier1_global: summary
  • bytes/str merged_output

ARCHIVOS:
  • f7_consolidador.py

CHECKPOINTS:
  • state.json["f7"] = {tier1, merged, informe}

SALIDA:
  • {merged_output, tier1_summary, informe_pre_entrega}
```

### FICHA TÉCNICA: F8 — Repair Pipeline

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F8                                                       ║
║ NOMBRE: Repair Pipeline 5 Pasos + Métricas Duras             ║
║ ESTADO: PRESERVADA + MEJORADA (DSL jerárquico + métricas)     ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Reparar outputs rechazados por F6 o workers failed por F4/F5.
  4 pasos de retry + 1 paso de evaluación con métricas duras.

ENTRADA:
  • rejected_outputs: list (de F6)
  • failed_workers: list (de F4/F5)
  • domain_registry: dict (para DSL jerárquico)

PROCESO (100% Python puro):
  Por cada output rechazado:
    1. RETRY x3: re-ejecuta mismo DSL, mismo contexto
       • Si éxito → reemplaza output
       • Si falla x3 → Paso 2

    2. DSL JERÁRQUICO:
       • Intenta v2_medio (menos campos obligatorios)
       • Si falla → intenta v1_minimo (solo campo crítico)
       • Si falla → Paso 3

    3. REDUCE CONTEXTO 50%:
       • Trunca input_data a la mitad
       • Re-ejecuta DSL más simple
       • Si éxito → output parcial (calidad degradada)
       • Si falla → Paso 4

    4. RESTORE CHECKPOINT:
       • Recupera state.json de checkpoint F3
       • Re-ejecuta pipeline desde F3
       • Si éxito → output restaurado
       • Si falla → Paso 5

    5. EVALÚA ABORTO (5 métricas):
       • schema_compliance_rate = valid_fields / total_fields
       • output_divergence_index = levenshtein(plan, actual) / len(plan)
       • dsl_execution_failure_rate = failed_executions / total_attempts
       • repair_pattern_stability = mismo_error_en_2_reparaciones
       • token_budget_deviation = abs(tokens_usados - budget) / budget

       • flags = sum(1 for m in metrics if m["status"] == "CORRUPT")
       • if flags >= 2: ABORTA
       • if flags == 1: DEGRADED (retry alternativo)
       • if flags == 0: CONTINUA (raro)

DECISIONES_PYTHON:
  • Todo el pipeline de repair: PYTHON
  • Evaluación métricas: PYTHON
  • Decisión aborto: PYTHON (if flags >= 2)

DECISIONES_LLM:
  • NINGUNA (eliminado "Fallback Model/Agent" del doc base)

ESTRUCTURAS_DATOS:
  • dict repair_status: {node_id: {paso, intentos, output, flags}}
  • list aborted: [node_id]
  • list repaired: [node_id]

ARCHIVOS:
  • f8_repair.py
  • config/dsl_hierarchy.yaml

CHECKPOINTS:
  • state.json["f8"] = {repaired, aborted, metrics}

SALIDA:
  • {repaired_outputs: list, aborted: list, status: OK|PARTIAL|ABORTED}
```

### FICHA TÉCNICA: F9 — Entrega Final

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F9                                                       ║
║ NOMBRE: Entrega Final y Reporte Automático                   ║
║ ESTADO: PRESERVADO (sin cambios)                              ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Empaquetar resultado final y generar reporte completo.
  Entregar al usuario con trazabilidad total.

ENTRADA:
  • merged_output de F7
  • repaired_outputs de F8
  • state.json completo (F-1 a F9)

PROCESO (100% Python puro):
  1. Empaquetado:
     • MODE_CODE: zip(código + tests + docs + README.md)
     • MODE_MULTI: JSON estructurado + resumen.md
     • MODE_MIXTO: zip combinado

  2. Reporte automático (Python genera, no LLM):
     reporte = {
       "modo": execution_profile,
       "modelo_principal": "Qwen" if CODE else "Gemma4" if MULTI else "Mixto",
       "llm_pensó": True if F4_usado else False,
       "errores_llm": len([e for e in state if e.get("llm_error")]),
       "errores_codigo_puro": len([e for e in state if e.get("code_error")]),
       "calidad_score": calcular_calidad(state),
       "tiempo_total_ms": state["f9"]["timestamp"] - state["f-1"]["timestamp"],
       "tokens_total": sum(s.get("tokens", 0) for s in state.values()),
       "dominios_f55": [d for d in domain_registry if d.get("f55_cubierto")],
       "metricas_f5": {
         "max_stress": max(s.get("stress", 0) for s in state.values()),
         "max_anxiety": max(s.get("anxiety", 0) for s in state.values()),
         "max_divergence": max(s.get("divergence", 0) for s in state.values())
       },
       "metricas_f8": {
         "repairs": len(state.get("f8", {}).get("repaired", [])),
         "aborts": len(state.get("f8", {}).get("aborted", []))
       },
       "trazabilidad_completa": True
     }

  3. state.json final:
     • Añade f9 con timestamp, reporte, paths de entrega

DECISIONES_PYTHON:
  • Empaquetado: PYTHON (zipfile, json, os)
  • Reporte: PYTHON (formateo estructurado)
  • Trazabilidad: PYTHON (recorrido state.json)

DECISIONES_LLM:
  • NINGUNA

ESTRUCTURAS_DATOS:
  • bytes empaquetado
  • dict reporte
  • dict state_final

ARCHIVOS:
  • f9_deliver.py

CHECKPOINTS:
  • state.json["f9"] (FINAL, inmutable)

SALIDA:
  • {empaquetado: bytes/path, reporte: dict, state_final: dict}
```

---

## Ruta de Diseño F6 → F7 → F8 → F9

```
TRANSICIÓN: F6 → F7
quien_llama: f6_verificador.py
quien_recibe: f7_consolidador.py
datos_transferidos:
  - certified_outputs: list
  - eros_memory de workers
  - schemas: dict
validaciones:
  - certified_outputs no vacío (si vacío → F8 Repair todo)
abortos_posibles: NINGUNO (F8 maneja rechazados)
rollback_posible: SÍ (checkpoint F6 permite re-verificar)

TRANSICIÓN: F7 → F8
quien_llama: f7_consolidador.py
quien_recibe: f8_repair.py
datos_transferidos:
  - rejected_outputs: list (si F7 detectó inconsistencias)
  - failed_workers: list
  - informe_pre_entrega: dict
validaciones:
  - rejected no vacío (si vacío → salta F8, va directo F9)
abortos_posibles: NINGUNO
rollback_posible: SÍ (checkpoint F7 permite re-consolidar)

TRANSICIÓN: F8 → F9
quien_llama: f8_repair.py
quien_recibe: f9_deliver.py
datos_transferidos:
  - repaired_outputs: list (puede ser vacío si todo abortó)
  - merged_output de F7
  - state.json completo
validaciones:
  - state.json tiene todas las fases F-1 a F8
abortos_posibles: NINGUNO (F9 es última fase, entrega lo que tenga)
rollback_posible: NINGUNO

TRANSICIÓN: F9 → USUARIO
quien_llama: f9_deliver.py
quien_recibe: usuario (interfaz)
datos_transferidos:
  - empaquetado: bytes/path
  - reporte: dict
  - state_final: dict
validaciones:
  - empaquetado no vacío
  - reporte tiene campos obligatorios
abortos_posibles: NINGUNO
rollback_posible: NINGUNO
```
=== END ===

=== ARCHIVO 14 (357d97be fusion-bloque-1) ===
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
---

## ANEXO D: ELEMENTOS COMPLEMENTARIOS POST-REVISIÓN

### D.1 DIAGRAMA ASCII -- BLOQUE 1 COMPLETO (F-1 → F3)

```
USUARIO (texto natural)
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ F-1: MYTHOS PREP LOOP                                       │
│ ⚙️ 100% CÓDIGO                                              │
│ • Tokeniza: len(texto) // 4                                 │
│ • Peso keywords: signals.yaml                               │
│ • Boost sintáctico: [python,script] ×2.5                  │
│ • Umbral: |code - multi| > 1.5 → modo único                │
│                                                             │
│ Output: {tokens, peso_code, peso_multi, diff, modo_pre}     │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ F0: CLASIFICACIÓN DUAL → UNIFICADA                          │
│ ⚙️ 100% CÓDIGO                                              │
│ • Regex code: keywords ∈ domain_registry.code_indicators    │
│ • Regex multi: keywords ∈ domain_registry.multi_indicators│
│ • Decisión dura: diff > 1.5 → CODE|MULTI else MIXTO        │
│                                                             │
│ Output: {modo_final, confianza, code_hits, multi_hits}      │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ F1: RUTEO POR TABLA DE VERDAD + PERFILES                    │
│ ⚙️ 100% CÓDIGO                                              │
│ • Carga router_{modo}.yaml                                  │
│ • Produce execution_profile (NO implementación)            │
│ • Produce verification_profile                              │
│ • Produce worker_profile (architecture|domain|mixed)       │
│ • Configura F6_capa2 desde domain_registry flag             │
│                                                             │
│ Output: {execution, verification, worker, f6_capa2, ruta}   │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ F2: PLAN DAG DETERMINISTA + PRESUPUESTO                     │
│ ⚙️ 100% CÓDIGO                                              │
│ • Construye G=(V,E) con networkx.DiGraph()                  │
│ • Valida presupuesto: total_tokens < 32K                    │
│ • Valida runtime: total_runtime < 30s                      │
│ • topological_sort() → orden_ejecucion                     │
│ • find_cycle() → ABORTA si ciclo detectado                 │
│ • Agrupa paralelos por nivel                                │
│ • Genera execution_manifest                                 │
│                                                             │
│ Output: {orden, grupos_paralelos, manifest, presupuesto}    │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ F3: AISLAMIENTO + PRECARGA DSL + BUFFERS EROS               │
│ ⚙️ 100% CÓDIGO                                              │
│ • Spawn workers (asyncio.create_task preparado)            │
│ • Aisla memoria local por worker                            │
│ • Carga dsl_<tipo>.py → valida AST (ast.parse)            │
│ • Valida schema JSON (jsonschema)                          │
│ • Asigna modelo: lookup [Qwen|Llama4|Gemma4]               │
│ • Inicializa EROS 3-Tier buffers: tier3/tier2/tier1        │
│ • Verifica isolation_policy.yaml                            │
│                                                             │
│ Output: {workers_listos, manifest, dsl_validados}           │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
  [TRANSICIÓN A BLOQUE 2: F4 EJECUCIÓN]
```

---

### D.2 VERIFICACIÓN CRUZADA FASE POR FASE -- FORMATO EXACTO

#### F-1: Mythos Prep Loop

```yaml
fase: F-1
nombre_original: NO_EXISTE_EN_DOC_BASE
responsabilidad_original: N/A
entradas_originales: [texto_raw]
procesos_originales: N/A
salidas_originales: N/A
estado_v44:
  preservado: N/A
  modificado: N/A
  ampliado: true
cambios:
  - Fase nueva aditiva pre-F0
  - Pre-estimación tokens heurística
  - Pesos contextuales configurables vía YAML
riesgo_estructural: NINGUNO
preguntas_verificacion:
  elimino_funcion: NO
  reemplazo_funcion: NO
  mejora_aditiva: SI
  perdida_capacidad: NO
  regresion_funcional: NO
veredicto: NUEVA_ADITIVA
```

#### F0: Clasificación

```yaml
fase: F0
nombre_original: Fase 0: Clasificación Dual (Kimi + MiniMax)
responsabilidad_original: Clasificar intención usuario + tipo tarea
entradas_originales: [texto_raw]
procesos_originales: Clasificación dual paralela → decisión unificada
salidas_originales: [clasificación_unificada]
estado_v44:
  preservado: true
  modificado: true
  ampliado: true
cambios:
  - Reemplaza LLM dual por regex + pesos Python
  - Añade umbral numérico |code - multi| < 1.5
  - Añade activadores MODE_CODE vs MODE_MULTI
  - Fuente única: domain_registry.yaml
riesgo_estructural: NINGUNO
preguntas_verificacion:
  elimino_funcion: NO
  reemplazo_funcion: SI (proceso interno, no responsabilidad)
  mejora_aditiva: SI
  perdida_capacidad: NO
  regresion_funcional: NO
veredicto: PRESERVADA_MEJORADA
```

#### F1: Ruteo

```yaml
fase: F1
nombre_original: Fase 1: Selección de Modo y Ruta
responsabilidad_original: Seleccionar modo agente + ruta ejecución
entradas_originales: [clasificación_unificada]
procesos_originales: Decisión unificada de modo y ruta
salidas_originales: [modo_seleccionado, ruta_ejecución]
estado_v44:
  preservado: true
  modificado: true
  ampliado: true
cambios:
  - Reemplaza decisión LLM por tabla verdad YAML
  - Desacopla implementación concreta (Qwen/Llama4/Gemma4)
  - Añade perfiles: execution, verification, worker
  - Añade F6_capa2 config desde domain_registry
riesgo_estructural: NINGUNO
preguntas_verificacion:
  elimino_funcion: NO
  reemplazo_funcion: SI (proceso interno)
  mejora_aditiva: SI
  perdida_capacidad: NO
  regresion_funcional: NO
veredicto: PRESERVADA_MEJORADA
```

#### F2: Plan DAG

```yaml
fase: F2
nombre_original: Fase 2: Skills y Descomposición
responsabilidad_original: Planificación con todo_write + agentes
entradas_originales: [modo_seleccionado, requerimientos]
procesos_originales: Descomposición en subtareas + orden
salidas_originales: [plan_unificado, subtareas, agentes, orden]
estado_v44:
  preservado: true
  modificado: true
  ampliado: true
cambios:
  - Reemplaza planificación LLM por networkx.topological_sort
  - Añade detección ciclos con aborto determinista
  - Añade validación presupuesto tokens/runtime antes de DAG
  - Añade execution_manifest formal
  - Añade paralelismo automático por niveles
riesgo_estructural: NINGUNO
preguntas_verificacion:
  elimino_funcion: NO
  reemplazo_funcion: SI (proceso interno)
  mejora_aditiva: SI
  perdida_capacidad: NO
  regresion_funcional: NO
veredicto: PRESERVADA_MEJORADA
```

#### F3: Aislamiento

```yaml
fase: F3
nombre_original: Fase 3: Aislamiento y Preparación
responsabilidad_original: Spawn subagentes congelados + Structured Summaries
entradas_originales: [plan_subtareas]
procesos_originales: Aislamiento de contexto por worker
salidas_originales: [workers_listos, contexto_aislado, tools]
estado_v44:
  preservado: true
  modificado: true
  ampliado: true
cambios:
  - Mantiene spawn workers con asyncio
  - Añade precarga DSL schema antes de lanzar
  - Añade validación AST + jsonschema
  - Añade asignación modelo por lookup tabla
  - Añade EROS 3-Tier buffers (tier3/tier2/tier1)
  - Añade isolation_policy.yaml verificable
  - Blackboard SOLO LECTURA entre workers
riesgo_estructural: NINGUNO
preguntas_verificacion:
  elimino_funcion: NO
  reemplazo_funcion: SI (proceso interno)
  mejora_aditiva: SI
  perdida_capacidad: NO
  regresion_funcional: NO
veredicto: PRESERVADA_MEJORADA
```

---

### D.3 MAPA DE RESPONSABILIDADES -- BLOQUE 1 (F-1 a F3)

```yaml
mapa_responsabilidades_bloque_1:

  Python / Sistema:
    responsabilidades:
      - F-1: Calcular tokens, asignar pesos, aplicar boost, comparar umbral
      - F0: Regex matching, sumar pesos, decidir modo final
      - F1: Seleccionar router YAML, asignar perfiles, configurar F6_capa2
      - F2: Construir grafo DAG, topological_sort, detectar ciclos
      - F2: Validar presupuesto tokens/runtime antes de aprobar DAG
      - F2: Agrupar paralelos, generar execution_manifest
      - F3: Spawn workers, aislar memoria, cargar DSL
      - F3: Validar DSL con AST (ast.parse), validar schema JSON
      - F3: Asignar modelo por lookup tabla [Qwen|Llama4|Gemma4]
      - F3: Preparar buffers EROS 3-Tier (tier3/tier2/tier1)
      - F3: Verificar isolation_policy.yaml
      - F3: Gestionar blackboard SOLO LECTURA
      - Transiciones: Validar datos entre fases, manejar abortos
    archivos:
      - f-1_mythos.py
      - f0_clasificador.py
      - f1_router.py
      - f2_plan_dag.py
      - f3_aislamiento.py

  Gemma4:
    responsabilidades_bloque_1:
      - NINGUNA en F-1, F0, F1, F2, F3
      - Gemma4 NO decide, NO clasifica, NO rutea, NO planifica
      - Gemma4 solo aparece en F4 (Bloque 2) como ejecutor DSL
    nota: Bloque 1 es 100% código puro, sin LLM

  Qwen:
    responsabilidades_bloque_1:
      - NINGUNA en F-1, F0, F1, F2, F3
      - Qwen aparece solo en F4 (Bloque 2) como arquitecto código
    nota: Bloque 1 es 100% código puro, sin LLM

  Llama4:
    responsabilidades_bloque_1:
      - NINGUNA en F-1, F0, F1, F2, F3
      - Llama4 aparece solo en F4 (Bloque 2) como escritor código
      - Llama4 aparece en F5.5 (Bloque 3) como generador DSL puntual
    nota: Bloque 1 es 100% código puro, sin LLM

  DSL (Reglas Predefinidas):
    responsabilidades_bloque_1:
      - F3: dsl_<tipo>.py precargados antes de ejecución
      - F3: Schema JSON validado contra output esperado
      - F3: DSL NO se genera al vuelo en Bloque 1
      - F3: DSL se carga desde disco, se valida AST
    archivos:
      - dsl_resumen.py, dsl_codigo.py, dsl_investigar.py, etc.
      - schema_resumen.json, schema_codigo.json, etc.

  Domain Registry (Configuración Central):
    responsabilidades_bloque_1:
      - F-1: signals.yaml (pesos contextuales)
      - F0/F1: keywords, execution_profiles, worker_profiles
      - F2: limits (tokens, runtime, workers)
      - F3: isolation_policy.yaml
      - F1: f6_capa2 config (flag domain_registry)
    nota: Fuente única de verdad para todo el pipeline
    archivos:
      - config/domain_registry.yaml
      - config/signals.yaml
      - config/isolation_policy.yaml

  EROS (Memoria Jerárquica):
    responsabilidades_bloque_1:
      - F3: Inicializar tier3_raw_log (logs crudos)
      - F3: Inicializar tier2_pulse_buffer (métricas comprimidas)
      - F3: Inicializar tier1_summary_slot (<5% contexto)
      - F3: Preparar estructura para F7 (Bloque 4)
    nota: EROS se llena en F4/F5, se comprime en F7

  Usuario (Director):
    responsabilidades_bloque_1:
      - F2: Confirmar si presupuesto excede 32K/30s (si aplica)
      - F3: Aprobar DSL en F5.5 (Gate 3) -- fuera de Bloque 1
      - F8: Recibir reporte aborto si 2+ métricas CORRUPT
    nota: Bloque 1 requiere mínima intervención usuario
```

---

### D.4 EJEMPLO DE DSL PRECARGADO EN F3

```python
# dsl_resumen.py -- Ejemplo de DSL precargado en F3
# Este archivo se valida con ast.parse() antes de ejecutarse
# Gemma4 (en F4) ejecuta estas funciones, NO las inventa

def extraer_titulo(texto: str) -> list:
    """Extrae títulos usando regex o BeautifulSoup."""
    import re
    return re.findall(r'<h1>(.*?)</h1>', texto)

def extraer_fecha(texto: str) -> list:
    """Extrae fechas en formato ISO."""
    import re
    from datetime import datetime
    fechas = re.findall(r'\d{4}-\d{2}-\d{2}', texto)
    return [datetime.strptime(f, '%Y-%m-%d') for f in fechas]

def resumir_parrafo(texto: str, max_palabras: int = 100) -> str:
    """Resume párrafo usando algoritmo extractivo."""
    palabras = texto.split()
    if len(palabras) <= max_palabras:
        return texto
    return ' '.join(palabras[:max_palabras]) + '...'

# Schema de salida esperado (schema_resumen.json)
# {
#   'titulo': str,
#   'resumen': str,
#   'fecha': str,
#   'longitud_original': int,
#   'longitud_resumen': int
# }
```

---

### D.5 CHECKLIST DE INTEGRIDAD BLOQUE 1

| # | Verificación | Estado | Evidencia |
|---|-------------|--------|-----------|
| 1 | Header JSON presente | ✅ | Sección 1 |
| 2 | Mapa de Preservación Estructural | ✅ | Sección 2 + Anexo D.2 |
| 3 | Verificación Cruzada Fase por Fase (5 preguntas) | ✅ | Anexo D.2 YAML |
| 4 | Diagrama en 4 Bloques (global F-1→F9) | ✅ | parte_4_integracion_completa.md |
| 5 | Diagrama Bloque 1 (F-1→F3) | ✅ | Anexo D.1 ASCII |
| 6 | Diseño Interno de Cada Fase (40-60 líneas) | ✅ | Secciones 3-7 |
| 7 | Ruta de Diseño Completa (transiciones) | ✅ | Sección 8 |
| 8 | Auditoría de Decisiones (FASE/DECISIÓN/TIPO) | ✅ | Sección 9 |
| 9 | Auditoría de Consumo LLM | ✅ | Sección 10 |
| 10 | Riesgos Arquitectónicos (mínimo 20) | ✅ | Sección 11 |
| 11 | Veredicto Final (4 preguntas) | ✅ | Sección 12 |
| 12 | Mapa de Responsabilidades | ✅ | Anexo D.3 |
| 13 | Reparaciones Post-Auditoría | ✅ | Anexo A |
| 14 | Auditoría Cruzada Bloques 1-4 | ✅ | Anexo B |
| 15 | Ejemplo de Ejecución Completa | ✅ | Anexo C |
| 16 | Ejemplo de DSL Precargado | ✅ | Anexo D.4 |
| 17 | Consistencia con Bloques 2-4 verificada | ✅ | Anexo B |

**TOTAL VERIFICACIONES: 17/17 ✅**

---

**ESTADO BLOQUE 1: COMPLETO + AUDITADO + REVISADO**
**FECHA REVISIÓN: 2026-06-02**
**PRÓXIMA ACCIÓN: Auditoría formal GPT de Bloques 2-4**
=== END ===

=== ARCHIVO 31 (779ccf3b fusion-bloque-3) ===
# BLOQUE 3: MOTOR DE CONTROL + VERIFICACIÓN (F5 + F5.5 + F6)
## Verificación Cruzada Preservación vs Doc Base

```yaml
auditoria_preservacion_bloque_3:
  fase_F5:
    nombre_original: "Fase 5: Monitoreo Simultáneo (PAD + Ansiedad + Anti-Drift)"
    responsabilidad_original: >
      Monitorear ejecución con 3 sistemas simultáneos:
      PAD (arousal/pleasure), Ansiedad (duda en círculos nivel 1/2/3),
      Anti-Drift (KL divergence plan vs actual)
    entradas_originales:
      - State.json actualizado durante ejecución
      - Métricas de workers
    procesos_originales:
      - PAD: arousal > 0.8 AND pleasure < 0.2 → SIGKILL + respawn
      - Ansiedad: nivel 1/2/3 → confirmar o respawn
      - Anti-Drift: KL(plan||actual) > 0.02 → halt + rollback
    salidas_originales:
      - State.json actualizado
      - Decisiones de control (SIGKILL, respawn, rollback)
    estado_v44:
      preservado: true
      modificado: true
      ampliado: true
    cambios:
      - "Renombra métricas emocionales a técnicas duras"
      - "PAD → system_stress: (cpu+memory+queue)/3 > 0.8 → SIGKILL"
      - "Pleasure → success_rate: passed/total < 0.2 → SIGKILL"
      - "Ansiedad → anxiety_level: errores_consecutivos >= 3 → confirmar/respawn"
      - "Anti-Drift → divergence_kl: KL(plan_output||actual_output) > 0.02 → rollback"
      - "Mantiene 3 sistemas simultáneos, ahora 100% código puro"
      - "Añade jsonschema validation + timeout checks + pytest"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: monitorear ejecución y tomar acciones de control.
      Proceso mejorado: métricas subjetivas → fórmulas matemáticas duras.
      Salida preservada: decisiones de control (SIGKILL, respawn, rollback).

  fase_F5_5:
    nombre_original: "NO EXISTÍA en doc base"
    estado_v44: "NUEVA_ADITIVA"
    responsabilidad: >
      Generar DSL de verificación para dominios nuevos no cubiertos.
      Llama4 genera reglas UNA SOLA VEZ con 3 gates de seguridad.
    riesgo_estructural: NINGUNO
    conclusion: "Nueva fase aditiva. No elimina ni modifica fases existentes."

  fase_F6:
    nombre_original: "Fase 6: Verificación 3-Capas (Adversarial + Cruzada + Maker-Checker)"
    responsabilidad_original: >
      Verificar outputs con 3 capas:
      Capa 1 Adversarial (MiniMax): Verifier busca errores 3 rondas
      Capa 2 Cruzada (Kimi): Executor B valida output de A
      Capa 3 Maker-Checker: Módulo A produce, Módulo B verifica
    entradas_originales:
      - Outputs de workers
      - Brief original del usuario
    procesos_originales:
      - Capa 1: LLM adversarial busca errores
      - Capa 2: LLM cruzada valida
      - Capa 3: Maker-Checker con LLM
    salidas_originales:
      - Output certificado si 3 capas OK
    estado_v44:
      preservado: true
      modificado: true
      ampliado: true
    cambios:
      - "Capa 1: jsonschema Python puro (reemplaza LLM adversarial)"
      - "Capa 2: diff + checksum hashlib Python puro (reemplaza LLM cruzada)"
      - "Capa 3: pytest/unittest Python puro (reemplaza Maker-Checker LLM)"
      - "Añade: Capa 2 LLM anclado SOLO en MODE_CODE y SOLO si domain_registry f55_cubierto=false"
      - "Añade: DSL de verificación expandible por dominio"
      - "5 dominios base cubiertos: web, datos, texto, código, imágenes"
    riesgo_estructural: NINGUNO
    conclusion: >
      Responsabilidad preservada: verificar outputs antes de entrega.
      Proceso mejorado: 3 capas LLM → 2 capas código puro + 1 capa LLM transitoria.
      Salida preservada: output certificado o rechazado.
```

---

## Diagrama Detallado — F5 + F5.5 + F6

```
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F5: MONITOREO SIMULTÁNEO — 100% CÓDIGO                     │
│                                                                 │
│  Entrada: outputs_por_worker + state.json durante ejecución     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SISTEMA 1: SYSTEM_STRESS (ex-PAD)                       │   │
│  │                                                         │   │
│  │  Métricas:                                              │   │
│  │    • cpu_percent > 80%                                  │   │
│  │    • memory_percent > 80%                               │   │
│  │    • queue_depth > 20                                   │   │
│  │                                                         │   │
│  │  Fórmula: stress = (cpu + memory + queue/25) / 3        │   │
│  │  Umbral: stress > 0.8 → SIGKILL + respawn              │   │
│  │                                                         │   │
│  │  Acción: asyncio.create_task(respawn_worker(id))        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SISTEMA 2: ANXIETY_LEVEL (ex-Ansiedad)                   │   │
│  │                                                         │   │
│  │  Métricas:                                              │   │
│  │    • errores_consecutivos por worker                    │   │
│  │    • retries_sin_exito                                  │   │
│  │    • schema_validation_fails                            │   │
│  │                                                         │   │
│  │  Niveles:                                               │   │
│  │    • Nivel 1: 1 error → log warning                   │   │
│  │    • Nivel 2: 2 errores → retry automático              │   │
│  │    • Nivel 3: >=3 errores → confirmar o respawn        │   │
│  │                                                         │   │
│  │  Acción: si nivel 3 → marca worker para F8 Repair       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SISTEMA 3: DIVERGENCE_KL (ex-Anti-Drift)               │   │
│  │                                                         │   │
│  │  Métricas:                                              │   │
│  │    • KL(plan_output || actual_output)                   │   │
│  │      = Σ plan_i * log(plan_i / actual_i)                │   │
│  │                                                         │   │
│  │  Simplificación código puro:                            │   │
│  │    • diff_ratio = levenshtein(plan, actual) / len(plan) │   │
│  │    • Si diff_ratio > 0.02 → ROLLBACK                    │   │
│  │                                                         │   │
│  │  Acción: restore checkpoint F3 + re-ejecutar worker     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Salida: {acciones: [SIGKILL, ROLLBACK, RETRY],               │
│           workers_afectados: list,                            │
│           state_updates: dict}                                 │
│  Checkpoint: state.json["f5"]                                  │
│  Aborto posible: 🛑 SÍ (stress crítico en múltiples workers)  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ 💡 F5.5: GENERACIÓN DSL — DOMINIO NUEVO (transitorio)          │
│                                                                 │
│  Activación: F6 detecta "DSL_INCOMPLETO" para dominio X        │
│  Condición: domain_registry[dominio][f55_cubierto] == false   │
│  Permiso: usuario aprueba generación (configurable)            │
│                                                                 │
│  Proceso (Llama4 UNA SOLA VEZ):                                │
│    1. Llama4 genera: dsl_<dominio>_v1.yaml                    │
│    2. Llama4 genera: template_<dominio>.py                    │
│    3. Llama4 genera: tests_<dominio>.py                        │
│                                                                 │
│  3 GATES obligatorios:                                         │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ GATE 1: AST ESTÁTICO                                     │ │
│    │   • Python ast.parse() verifica syntax válida          │ │
│    │   • Detecta: os.system, eval, exec, __import__         │ │
│    │   • Detecta: imports no declarados                     │ │
│    │   Resultado: PASS / FAIL                                 │ │
│    └─────────────────────────────────────────────────────────┘ │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ GATE 2: DOCKER SANDBOX                                   │ │
│    │   • Ejecuta tests en contenedor aislado                  │ │
│    │   • Timeout: 60s                                         │ │
│    │   • Sin acceso a red, filesystem host, variables entorno │ │
│    │   Resultado: PASS / FAIL                                 │ │
│    └─────────────────────────────────────────────────────────┘ │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ GATE 3: APROBACIÓN HUMANA                                │ │
│    │   • Usuario revisa DSL generado                          │ │
│    │   • Usuario aprueba / rechaza                            │ │
│    │   • Si aprueba → domain_registry[dominio][f55_cubierto] = true
│    │   • Si rechaza → aborta + reporta                        │ │
│    └─────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Post-aprobar:                                                 │
│    • F6 Capa 2 cambia a "código puro" para este dominio      │
│    • Futuras tareas de este dominio: 0% LLM en verificación   │
│    • DSL se añade a config/dsl/ permanentemente               │
│                                                                 │
│  % LLM: Puntual (una sola vez por dominio)                    │
│  % CÓDIGO: 100% en gates 1 y 2                                 │
│  Checkpoint: state.json["f5.5"]                                │
│  Aborto posible: 🛑 SÍ (Gate 1/2/3 falla)                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ⚙️ F6: VERIFICACIÓN 3-CAPAS                                    │
│                                                                 │
│  Entrada: outputs_por_worker de F4 + acciones de F5          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CAPA 1: SCHEMA VALIDATION (Python puro)                 │   │
│  │   • jsonschema.validate(output, schema_json)             │   │
│  │   • ¿Todos campos obligatorios presentes?               │   │
│  │   • ¿Tipos correctos? (str, int, list, dict)           │   │
│  │   • ¿Formatos válidos? (email, URL, fecha ISO)          │   │
│  │   Resultado: PASS / FAIL con lista de errores           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CAPA 2A: DIFF + CHECKSUM (Python puro) — DEFAULT       │   │
│  │   • hashlib.sha256(output.encode()).hexdigest()         │   │
│  │   • Compara contra expected_pattern si existe           │   │
│  │   • levenshtein(output, expected) / len(expected)       │   │
│  │   Resultado: PASS / DIVERGENCE_DETECTED                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CAPA 2B: LLM ANCLADO (condicional) — SOLO SI:           │   │
│  │   • execution_profile == MODE_CODE                      │   │
│  │   • domain_registry[dominio][f55_cubierto] == false     │   │
│  │                                                         │   │
│  │   LLM recibe: brief original + output generado           │   │
│  │   Pregunta: "¿Este output contradice el brief?"        │   │
│  │   Respuesta: SÍ/NO + razón                               │   │
│  │   Si SÍ → marca CONTRADICCION_BRIEF → F8 Repair        │   │
│  │   Si NO → pasa                                          │   │
│  │                                                         │   │
│  │   NOTA: Capa 2B es TRANSITORIA.                         │   │
│  │   Una vez F5.5 cubre dominio → Capa 2B se desactiva.   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CAPA 3: TESTS AUTOMÁTICOS (Python puro)                 │   │
│  │   • pytest tests_<dominio>.py (generados en F5.5)      │   │
│  │   • unittest para validaciones específicas              │   │
│  │   • Si código: compile() + syntax check                │   │
│  │   • Si web: BeautifulSoup checks (SEO, responsive)     │   │
│  │   • Si datos: pandas schema validation                  │   │
│  │   • Si texto: longitud + formato + encoding             │   │
│  │   • Si imágenes: dimensiones + formato + checksum        │   │
│  │   Resultado: PASS / FAIL con logs detallados            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Lógica de decisión:                                            │
│    • Capa 1 FAIL → F8 Repair (schema inválido)               │
│    • Capa 2A FAIL → F8 Repair (divergencia detectada)          │
│    • Capa 2B CONTRADICCION → F8 Repair (brief violado)         │
│    • Capa 3 FAIL → F8 Repair (tests no pasan)                │
│    • TODAS PASS → output certificado → F7                      │
│                                                                 │
│  DSL de verificación por dominio (ejemplos):                    │
│    verify_web.py:    SEO, responsive, accesibilidad, performance│
│    verify_datos.py:  schema, tipos, nulos, rangos              │
│    verify_texto.py:  longitud, formato, encoding, idioma        │
│    verify_codigo.py: syntax, tests, imports, seguridad         │
│    verify_imagen.py: dimensiones, formato, checksum, metadata   │
│                                                                 │
│  Salida: {certified_outputs: list, rejected: list,             │
│           capa2b_usada: bool, f55_cubierto: bool}              │
│  Checkpoint: state.json["f6"]                                    │
│  Aborto posible: 🛑 SÍ (todos outputs rechazados)              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Fichas Técnicas Individuales — F5 + F5.5 + F6

### FICHA TÉCNICA: F5 — Monitoreo

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F5                                                       ║
║ NOMBRE: Monitoreo Simultáneo 3-Sistemas                        ║
║ ESTADO: PRESERVADA + MEJORADA (métricas renombradas)          ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Monitorear ejecución de workers en tiempo real.
  Detectar stress, errores consecutivos, divergencia plan vs actual.
  Tomar acciones: SIGKILL, respawn, rollback.

ENTRADA:
  • outputs_por_worker: dict (de F4, actualizado en tiempo real)
  • state.json: dict global
  • métricas sistema: cpu, memory, queue_depth

PROCESO (100% Python puro):
  1. Cada 500ms (asyncio loop):
     a. system_stress = (cpu + memory + queue_depth/25) / 3
     b. anxiety_level = errores_consecutivos_por_worker
     c. divergence_kl = levenshtein(plan_output, actual_output) / len(plan)
  2. Evaluar umbrales:
     • stress > 0.8 → SIGKILL worker + respawn
     • anxiety >= 3 → marca para F8 Repair
     • divergence > 0.02 → rollback a checkpoint F3
  3. Escribir métricas a state.json["f5"]

DECISIONES_PYTHON:
  • Cálculo métricas: PYTHON (psutil, asyncio)
  • Comparación umbrales: PYTHON
  • Acciones control: PYTHON (asyncio.create_task, os.kill)

DECISIONES_LLM:
  • NINGUNA

ESTRUCTURAS_DATOS:
  • dict stress_by_worker: {worker_id: float}
  • dict anxiety_by_worker: {worker_id: int}
  • dict divergence_by_worker: {worker_id: float}
  • list actions_queue: [{action, target, timestamp}]

ARCHIVOS:
  • f5_monitor.py
  • config/monitor_thresholds.yaml

CHECKPOINTS:
  • state.json["f5"] = {stress, anxiety, divergence, actions}

ERRORES_POSIBLES:
  • Stress crítico global: SIGKILL múltiples workers
  • Divergencia masiva: rollback completo a F3
  • Loop de anxiety: si mismo worker falla 3 veces → F8 Repair

SALIDA:
  • {actions: list, workers_afectados: list, state_updates: dict}
```

### FICHA TÉCNICA: F5.5 — Generación DSL

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F5.5                                                     ║
║ NOMBRE: Generación DSL para Dominio Nuevo                    ║
║ ESTADO: NUEVA ADITIVA                                          ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Cuando F6 detecta dominio sin reglas de verificación,
  generar DSL, template y tests UNA SOLA VEZ con aprobación.

ACTIVACIÓN:
  • F6 Capa 3 detecta: "dominio 'podcast' no tiene verify_podcast.py"
  • Consulta domain_registry: f55_cubierto == false
  • Si usuario configuró auto-generate: true → activa F5.5
  • Si auto-generate: false → aborta con DSL_INCOMPLETO

PROCESO:
  1. Llama4 recibe: brief del dominio + ejemplos de otros verify_*.py
  2. Llama4 genera:
     • dsl_podcast_v1.yaml (reglas de verificación)
     • template_podcast.py (estructura de tarea)
     • tests_podcast.py (tests unitarios)
  3. Gate 1: AST estático
     • ast.parse() verifica syntax
     • Detecta imports peligrosos (os, sys, subprocess)
     • Detecta eval/exec/__import__
  4. Gate 2: Docker sandbox
     • Ejecuta tests_podcast.py en contenedor
     • Timeout 60s, sin red, sin filesystem host
     • Verifica que tests pasan con datos de ejemplo
  5. Gate 3: Aprobación humana
     • Muestra DSL generado al usuario
     • Usuario aprueba / rechaza / modifica
     • Si aprueba: copia a config/dsl/ + domain_registry.f55_cubierto=true
     • Si rechaza: descarta + reporta DSL_INCOMPLETO

DECISIONES_PYTHON:
  • Activación: PYTHON (consulta domain_registry)
  • Gate 1: PYTHON (ast.parse)
  • Gate 2: PYTHON (subprocess + docker)
  • Gate 3: PYTHON (interfaz usuario)

DECISIONES_LLM:
  • Generación DSL: Llama4 (UNA SOLA VEZ)

ESTRUCTURAS_DATOS:
  • dict domain_registry: {dominio: {f55_cubierto: bool, dsl_version: str}}
  • list pending_generations: [{dominio, status}]

ARCHIVOS:
  • f5_5_generador_dsl.py
  • config/dsl/ (directorio DSL permanentes)
  • config/domain_registry.yaml

CHECKPOINTS:
  • state.json["f5.5"] = {dominio, status, gates_passed}

ERRORES_POSIBLES:
  • Gate 1 FAIL: syntax inválida → retry generación (máx 3)
  • Gate 2 FAIL: tests fallan → retry con más ejemplos
  • Gate 3 RECHAZO: usuario no aprueba → permanece f55_cubierto=false

SALIDA:
  • {dominio: str, dsl_path: str, tests_path: str, approved: bool}
```

### FICHA TÉCNICA: F6 — Verificación 3-Capas

```
╔═══════════════════════════════════════════════════════════════╗
║ FASE: F6                                                       ║
║ NOMBRE: Verificación 3-Capas                                   ║
║ ESTADO: PRESERVADA + MEJORADA                                  ║
╚═══════════════════════════════════════════════════════════════╝

OBJETIVO:
  Verificar outputs de workers antes de consolidación.
  2 capas código puro + 1 capa LLM transitoria (solo cold-start).

ENTRADA:
  • outputs_por_worker: dict (de F4)
  • schemas: dict (de F3)
  • domain_registry: dict (para saber si f55_cubierto)
  • execution_profile: str (MODE_CODE vs MODE_MULTI)

PROCESO:
  Por cada output:
    1. CAPA 1: jsonschema.validate(output, schema)
       • ¿Campos obligatorios? ¿Tipos? ¿Formatos?
       • FAIL → marca SCHEMA_INVALIDO
    2. CAPA 2A (default): diff + checksum
       • hashlib.sha256(output)
       • Si expected_pattern existe: levenshtein ratio
       • FAIL → marca DIVERGENCIA
    3. CAPA 2B (condicional):
       • SI execution_profile == MODE_CODE
         AND domain_registry[dominio].f55_cubierto == false
         → Llama4 anclado revisa: "¿contradice brief?"
       • SINO → salta Capa 2B
    4. CAPA 3: tests automáticos
       • Ejecuta verify_<dominio>.py
       • Ejecuta tests_<dominio>.py (de F5.5 si existe)
       • FAIL → marca TESTS_FALLIDOS
    5. Si todas capas PASS → CERTIFICADO
       Si alguna FAIL → F8 Repair

DECISIONES_PYTHON:
  • Selección capa 2A vs 2B: PYTHON (if/else domain_registry)
  • Validación schema: PYTHON (jsonschema)
  • Diff/checksum: PYTHON (hashlib, difflib)
  • Tests: PYTHON (pytest, unittest)

DECISIONES_LLM:
  • Capa 2B: Llama4 anclado (SOLO si cold-start dominio + MODE_CODE)

ESTRUCTURAS_DATOS:
  • dict verification_results: {worker_id: {capa1, capa2, capa3, final}}
  • list certified: [worker_id]
  • list rejected: [worker_id]
  • bool capa2b_usada: true/false

ARCHIVOS:
  • f6_verificador.py
  • verify_*.py (uno por dominio)

CHECKPOINTS:
  • state.json["f6"] = {certified, rejected, capa2b_usada}

SALIDA:
  • {certified_outputs: list, rejected: list, capa2b_usada: bool}
```

---

## Ruta de Diseño F4 → F5 → F5.5 → F6

```
TRANSICIÓN: F4 → F5
quien_llama: f4_worker_pool.py
quien_recibe: f5_monitor.py
datos_transferidos:
  - outputs_por_worker: dict
  - failed_workers: list
  - tokens_total: int
  - duration_total_ms: int
  - eros_memory.tier3_raw_log: list
validaciones:
  - outputs no vacío (aunque sea parcial)
  - state.json actualizado
abortos_posibles: OUTPUTS_VACIO_TOTAL → aborta pipeline
rollback_posible: SÍ (checkpoint F4 permite re-ejecutar)

TRANSICIÓN: F5 → F6
quien_llama: f5_monitor.py
quien_recibe: f6_verificador.py
datos_transferidos:
  - outputs_por_worker: dict (filtrados: solo OK, no failed)
  - schemas: dict (de F3)
  - acciones de control aplicadas (SIGKILL, respawn, rollback)
validaciones:
  - outputs validados por F5 (stress/anxiety/divergence OK)
abortos_posibles: NINGUNO (F5 ya filtró)
rollback_posible: NINGUNO

TRANSICIÓN: F5.5 ↔ F6 (loop condicional)
quien_llama: f6_verificador.py (detecta DSL_INCOMPLETO)
quien_recibe: f5_5_generador_dsl.py
datos_transferidos:
  - dominio: str
  - brief: str
  - ejemplos_dsl: list (otros verify_*.py existentes)
validaciones:
  - dominio no en domain_registry o f55_cubierto=false
  - usuario autorizó auto-generate
abortos_posibles: 🛑 SÍ (usuario rechaza Gate 3)
rollback_posible: NINGUNO (F5.5 es aditivo, no destructivo)

TRANSICIÓN: F6 → F7
quien_llama: f6_verificador.py
quien_recibe: f7_consolidador.py
datos_transferidos:
  - certified_outputs: list
  - schemas: dict
  - verification_results: dict
validaciones:
  - certified_outputs no vacío (si vacío → F8 Repair todo)
abortos_posibles: NINGUNO (F8 maneja rechazados)
rollback_posible: SÍ (checkpoint F6 permite re-verificar)
```
=== END ===
