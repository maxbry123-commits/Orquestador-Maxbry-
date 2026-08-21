# GUÍA INTERNA D — ESTRUCTURA DE REPOS EXPANDIDA
# "Separa lo más que se puedas, mientras más separado mejor
#  para Claude Code y Mimo Code" — Director, Paso 2
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRINCIPIO: BASE 8 REPOS (FUENTE 5) + EXPANSIÓN MÁXIMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El Director confirmó explícitamente: no tiene equipo de
programación, Claude/Claude Code/Mimo Code son sus "ojos".
Por eso el criterio NO es "cuántos repos son elegantes" sino
"qué tan fácil es para un agente de código abrir 1 repo y
saber EXACTAMENTE de qué se ocupa sin leer los otros 12".

Se parte de los 8 repos ya definidos (FUENTE 5) y se EXPANDEN
a 14, separando lo que en la base de 8 estaba mezclado.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAPA FINAL — 14 REPOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| # | Repo | Contenido | LOC est |
|---|------|-----------|---------|
| 1 | orquestador-nucleo | ADN+Guardian+AutoRecovery+LLM_JUEZ | 2.500 |
| 2 | orquestador-razonamiento | MYTHOS+DRE+GoalLock+PushPing | 3.000 |
| 3 | loop-engine | Sistema Loops Aislado (GUÍA C) | 1.500 |
| 4 | gcl-verificacion | GCL+Z3+SlotContract (GUÍA B) | 1.200 |
| 5 | motor-cognitivo-g2 | Motor 14 funciones + OC + sequence.json | 2.000 |
| 6 | fichas-expertos-g2 | 300 fichas (Capa A/B/C) | 8.000 |
| 7 | team-agente-cerebro | Cerebro TA + pipelines + selector | 1.500 |
| 8 | micro-agentes | 15 MA-* (DOC2+GRUPO_F) | 2.400 |
| 9 | escritor-runtime | LLM_ESCRITOR+Builder+Validator+Witness | 2.500 |
| 10 | api-router | R1-R10 + COST_OPTIMIZER (DOC3) | 2.500 |
| 11 | memoria-persistencia | 4 tiers+EventSourcing+KG+Dream/Distill | 2.000 |
| 12 | contracts-schemas | Universal Module Contract + todos schemas| 800 |
| 13 | frontend-interface | Centro Control 9 capas (DOC4) | 4.000 |
| 14 | workspaces-proyectos | Repo separado (Paso1 preg.9) | — |
| **TOTAL** | | | **~34.400** |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 1 — orquestador-nucleo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
orquestador-nucleo/
├── adn/
│   ├── adn_system.py          # 14 reglas (6 leyes+8 axiomas)
│   └── adn_constitution.json
├── guardian/
│   └── guardian_layer.py      # 6 checks RECHAZAR_SOLICITUD
├── auto_recovery/
│   ├── watchdog.py            # 30s interno, sin ping externo
│   └── replay_checkpoint.py
├── llm_juez/
│   ├── juez_core.py           # 8 estados
│   ├── juez_auditor.py        # RA+HUMO+alucinacion
│   └── failure_registry.py
└── config/
    └── connections.yaml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 2 — orquestador-razonamiento
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
orquestador-razonamiento/
├── mythos/
│   ├── goal_lock.py
│   ├── prelude.py
│   ├── dre_estimator.py
│   ├── recurrent_reasoning.py
│   ├── goal_stop_check.py
│   ├── coda.py
│   └── chef_final.py
├── push_ping/
│   └── input_engine.py        # 30 clasificaciones
├── token_budget/
│   └── budget_manager.py      # 70/85/95%
└── discovery/
    └── discovery_engine.py    # ciclos 2-5 rondas
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 3 — loop-engine (AISLADO, ver GUÍA C)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
loop-engine/
├── core.py                    # run_loop_engine() único entry point
├── niveles.py                 # RAPIDO/BASICO/AVANZADO/TURBO
├── fases/
│   ├── fase_0_init.py
│   ├── fase_1_comprension.py
│   ├── fase_2_analisis.py
│   ├── fase_3_planificacion.py
│   ├── fase_4_debate.py
│   ├── fase_5_verificacion.py
│   ├── fase_6_optimizacion.py
│   ├── fase_7_autoeval.py
│   └── fase_8_sintesis.py
├── escalado_dinamico.py
└── contracts/
    └── loop_engine.contract.json  # Universal Module Contract
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 4 — gcl-verificacion (ver GUÍA B)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
gcl-verificacion/
├── gcl/
│   ├── rules.py
│   ├── gcl_lite.py             # O(1) por fase
│   └── gcl_v1_gate.py          # gate final P13
├── z3/
│   └── z3_verifier.py
├── slot_contract/
│   ├── sc1_entrada.py
│   ├── sc2_dependencias.py
│   ├── sc3_permisos.py
│   ├── sc4_estado.py
│   ├── sc5_objetivo.py
│   └── sc6_salida.py
└── policies/
    └── gcl_rules.yaml           # 7 reglas base (GUÍA A.1)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 5 — motor-cognitivo-g2 (ver GRUPO_H sección 7)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
motor-cognitivo-g2/
├── objeto_cognitivo/
│   └── oc_schema.py            # invariantes INV-01..05
├── motor/
│   ├── scheduler.py
│   ├── dispatcher.py
│   ├── synchronizer.py
│   ├── state_machine.py
│   ├── event_bus.py
│   └── conflict_resolver.py
├── sequences/
│   └── example_sequence.json
└── enjambres/
    └── swarm_builder.py
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 6 — fichas-expertos-g2 (300 fichas, ver GRUPO_H)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
fichas-expertos-g2/
├── contrato_experto/
│   └── expert_contract_base.py  # el contrato v1.0 genérico
├── capa_a/ (a1_captura..a5_validadores, E001-E100)
├── capa_b/ (b1_analisis..b5_verificacion, E101-E200)
├── capa_c/ (c1_construccion..c5_emision, E201-E300)
└── mvp_v0.1/
    ├── E001.py  # muestra capa A
    ├── E101.py  # muestra capa B
    └── E201.py  # muestra capa C
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 7 — team-agente-cerebro (ver GUÍA A.1 gap 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
team-agente-cerebro/
├── cerebro_ta/
│   ├── core.py                # ≤100 LOC
│   ├── pipeline_selector.py    # ≤80 LOC
│   └── multitask_scheduler.py  # ≤120 LOC
├── pipelines/
│   ├── pipeline_code_gen.py
│   ├── pipeline_research.py
│   ├── pipeline_refactor.py
│   └── pipeline_generic.py
└── staff_registry.json         # mapea capability→agente externo
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 8 — micro-agentes (15 MA-*, DOC2+GRUPO_F)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
micro-agentes/
├── ma_code_gen.py       ├── ma_code_lint.py
├── ma_code_test.py      ├── ma_rag_search.py
├── ma_rag_synth.py      ├── ma_doc_write.py
├── ma_arch_plan.py      ├── ma_verify_3capas.py
├── ma_repair_5step.py   ├── ma_research_web.py
├── ma_research_gh.py    ├── ma_emit_report.py
├── ma_build.py          ├── ma_build_exec.py
└── ma_runtime_check.py
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 9 — escritor-runtime (ver GRUPO_F)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
escritor-runtime/
├── llm_escritor/
│   ├── escritor_core.py        # 7 estados
│   ├── escritor_generacion.py  # RG-01..10
│   └── escritor_protocolo.py   # PC-01..10
└── runtime/
    ├── builder.py
    ├── validator.py             # L1_static
    └── witness.py                # L2,L3,L4 + evidence_hash
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 10 — api-router (ver DOC3, sin cambios)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
api-router/
├── modules/R1_auth..R10_monitoring/
├── cost_optimizer/
└── config/capability.json + providers/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 11 — memoria-persistencia (ver DOC1 [27])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
memoria-persistencia/
├── tiers/ (tier0_raw..tier3_project)
├── event_sourcing/
├── knowledge_graph/
├── writer_subagent.py
├── dream_loop.py
├── distill_loop.py
└── master_state_engine.py      # state.json+crazy_wall
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 12 — contracts-schemas (ver GUÍA A.1 gap 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
contracts-schemas/
├── universal_module_contract.schema.json  # EL enchufe
├── task.schema.json
├── loop_result.schema.json
├── error.schema.json
└── nct.result.v1.json
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 13 — frontend-interface (ver DOC4, sin cambios)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
frontend-interface/
├── centro_control/ (9 capas)
├── modos/ (headless/studio/embedded)
├── arbol_decisiones/
└── panel_control/ (15 componentes)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO 14 — workspaces-proyectos (Paso1, pregunta 9)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
workspaces-proyectos/
├── _template/
│   ├── workflow.md
│   ├── roadmap.md
│   ├── architecture.md
│   ├── decisions.md
│   ├── research/ docs/ code/ memory/
│   ├── logs/ checkpoints/ reports/
│   └── state.json
└── proyecto_X/  (uno por proyecto real del usuario)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGLA DE CONEXIÓN ENTRE REPOS (sin imports directos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
1 nucleo ──> 2 razonamiento ──> 3 loop-engine
                                      │
                                      ▼
                              4 gcl-verificacion
                                      │
                                      ▼
                            5 motor-cognitivo-g2 ──> 6 fichas-expertos
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                                     ▼
            7 team-agente-cerebro              9 escritor-runtime
                    │                                     │
                    ▼                                     │
            8 micro-agentes ◄───────────────────────────┘
                    │
                    ▼
            10 api-router (todos lo consumen vía HTTP/contrato)
                    │
                    ▼
            11 memoria-persistencia (todos escriben aquí)
                    │
                    ▼
            13 frontend-interface (consume API, nunca importa código)

    12 contracts-schemas: consumido por TODOS, no consume a nadie
    14 workspaces-proyectos: independiente, solo I/O de archivos
```

REGLA: cada repo importa SOLO al de al lado en el flujo.
Ningún repo hace `from repo_lejano import algo` directo.
Toda comunicación entre repos no adyacentes pasa por
contracts-schemas (12) + api-router (10).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_D_ESTRUCTURA_REPOS","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno","fuente_de_verdad":true},
  "total_repos": 14,
  "loc_total_estimado": 34400,
  "base": "FUENTE_5 (8 repos) expandida",
  "repos": {
    "1":"orquestador-nucleo","2":"orquestador-razonamiento",
    "3":"loop-engine","4":"gcl-verificacion","5":"motor-cognitivo-g2",
    "6":"fichas-expertos-g2","7":"team-agente-cerebro",
    "8":"micro-agentes","9":"escritor-runtime","10":"api-router",
    "11":"memoria-persistencia","12":"contracts-schemas",
    "13":"frontend-interface","14":"workspaces-proyectos"
  },
  "regla_conexion": "solo repo adyacente, no imports directos lejanos, contracts+router median todo",
  "siguiente_documento": "GUIA_E_SENTINELA"
}
