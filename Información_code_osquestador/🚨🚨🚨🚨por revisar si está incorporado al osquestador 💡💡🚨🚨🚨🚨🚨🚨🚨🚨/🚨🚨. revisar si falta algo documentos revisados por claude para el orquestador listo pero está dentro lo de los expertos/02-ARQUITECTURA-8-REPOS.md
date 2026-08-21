# DOCUMENTO 02 — ARQUITECTURA FINAL DE 8 REPOS
## V1.0 — Completo

---

## MAPA DE REPOSITORIOS

| # | Repo | Grupo | LOC Est. |
|---|---|---|---|
| 1 | orquestador-auditor-arquitecto | A fase 1 | 5.000 |
| 2 | cerebro | A fase 2 | 4.000 |
| 3 | fichas | B | 8.000 |
| 4 | router | C | 6.000 |
| 5 | frontend | D | 4.000 |
| 6 | comunicacion-externa | backup | 3.000 |
| 7 | mejoras-continuas | backup | 2.000 |
| 8 | agentes | común | 1.000 |
| **TOTAL** | | | **33.000** |

---

## REPO 1 — ORQUESTADOR-AUDITOR-ARQUITECTO (Grupo A fase 1)

```
orquestador-auditor-arquitecto/
├── auditor/
│   ├── core.py                    # auditor central
│   ├── obsidian/
│   │   ├── writer.py
│   │   └── reader.py
│   ├── graphiti/
│   │   ├── writer.py              # FalkorDB
│   │   └── reader.py
│   ├── slash/                     # SENTINEL/JUDGE/SHERIFF
│   │   ├── sentinel.py
│   │   ├── judge.py
│   │   └── sheriff.py
│   └── carpetas_independientes/
│       ├── grupo_a/
│       ├── grupo_b/
│       ├── grupo_c/
│       └── grupo_d/
├── arquitecto/
│   ├── planner_offline.py         # PLANNER_OFFLINE del G2
│   ├── dag_builder.py
│   └── consensus.py               # 5+1 agentes
├── loops/
│   ├── meta_loop.py               # NIVEL 0
│   ├── open_claw_loop.py          # NIVEL 1
│   ├── signal_handlers.py         # NIVEL 7
│   └── heartbeat.py               # NIVEL 8
└── config/
    ├── connections.yaml
    ├── capability.json
    └── adn_constitution.json
```

**Función:** Primer repo a construir. Coordina y audita los otros 4.

---

## REPO 2 — CEREBRO (Grupo A fase 2)

```
cerebro/
├── maxbry/                        # 🧠 CEREBRO determinista
│   ├── core.py                    # <300 LOC
│   ├── loader.py                  # carga sequence.json
│   ├── executor.py                # ejecuta DAG
│   └── state_reader.py
├── kernel/                        # KERNEL inmutable
│   ├── adn.py                     # 6 LEYES
│   ├── guardian.py
│   ├── auto_recovery.py           # watchdog 30s
│   ├── llm_juez.py                # GOAL_LOCK
│   └── recovery_5niveles.py
├── fsm/
│   ├── states.py
│   ├── transitions.py
│   └── audit.py
├── loops/
│   ├── grupo_loop.py              # NIVEL 2
│   └── escalation.py              # NIVEL 10
├── config/
│   ├── connections.yaml
│   ├── capability.json
│   ├── adn_constitution.json
│   └── fallback.json
├── contracts/
│   ├── task.schema.json
│   ├── sequence.schema.json
│   └── state.schema.json
└── tools/
    ├── dsl_dag_validator.py
    ├── dag_validator.py
    ├── gcl_lite.py
    └── gcl_v1.py
```

---

## REPO 3 — FICHAS (Grupo B) — 3 ETAPAS AQUÍ

```
fichas/
├── imput/                         # ETAPA 1: captura
│   ├── 01_capture/
│   │   ├── capture.py             # 1 función ejecutar()
│   │   ├── capture.meta.md
│   │   ├── capture.location.json
│   │   └── test_capture.py
│   ├── 02_normalize/
│   └── 03_hash/
├── procesamiento/                 # ETAPA 2: razonamiento
│   ├── 01_parse/
│   ├── 02_dre/
│   ├── 03_consensus/              # 5+1 agentes
│   ├── 04_decision/
│   └── 05_validate/
├── output/                        # ETAPA 3: entrega
│   ├── 01_format/
│   └── 02_emit/
├── contracts/                     # Slot Contract SC1-SC6
│   ├── sc1_ficha_id.json
│   ├── sc2_hash.json
│   ├── sc3_schemas.json
│   ├── sc4_runtime_type.json
│   ├── sc5_llm_ratio.json
│   └── sc6_idempotente.json
├── verifier/                      # N0-N5
│   ├── n0_gpg.py
│   ├── n1_hash.py
│   ├── n2_schema.py
│   ├── n3_version.py
│   ├── n4_compat.py
│   └── n5_ast.py
└── loops/
    ├── claude_loop.py             # NIVEL 3
    └── mimo_loop.py               # NIVEL 4
```

**Las 3 ETAPAS DE ESPECIALISTAS viven aquí:**
- ETAPA 1 (input): `fichas/imput/`
- ETAPA 2 (razonamiento): `fichas/procesamiento/`
- ETAPA 3 (output): `fichas/output/`

---

## REPO 4 — ROUTER (Grupo C)

```
router/
├── modules/                       # R1-R10
│   ├── R1_auth_key_manager/
│   ├── R2_model_selector/
│   ├── R3_scheduler_lb/
│   ├── R4_health_check/
│   ├── R5_retry_engine/
│   ├── R6_circuit_breaker/
│   ├── R7_provider_pool/
│   ├── R8_semantic_cache/
│   ├── R9_audit_logger/
│   └── R10_monitoring/
├── config/
│   ├── capability.json
│   └── providers/
│       ├── provider_a.config
│       ├── provider_b.config
│       ├── provider_c.config
│       ├── provider_d.config
│       └── local_gguf.config
├── loops/
│   └── circuit_breaker.py
└── tests/
```

---

## REPO 5 — FRONTEND (Grupo D)

```
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/                  # SOLO HTTP al router
│   └── hooks/
├── public/
├── tests/
└── README.md
```

**REGLA:** Frontend SOLO consume API HTTP del router. NUNCA imports directos.

---

## REPO 6 — COMUNICACIÓN EXTERNA

```
comunicacion-externa/
├── mcp/                           # Model Context Protocol
│   ├── servers/
│   │   ├── obsidian_mcp.py
│   │   ├── graphiti_mcp.py
│   │   ├── github_mcp.py
│   │   └── filesystem_mcp.py
│   └── clients/
├── api_externa/
│   ├── telegram/
│   ├── drive/
│   ├── kanboard/
│   └── webhooks/
├── adapters/
│   ├── input_adapter.py
│   ├── output_connector.py
│   └── format_adapter.py
├── loops/
│   ├── dlq_retry.py               # NIVEL 9
│   └── saga_compensation.py
└── tests/
```

---

## REPO 7 — MEJORAS CONTINUAS

```
mejoras-continuas/
├── self_improvement/              # NIVEL 6
│   ├── metrics.py                 # 3 métricas
│   ├── decision.py                # MEJORA/REGRESION/ESTANCAMIENTO
│   └── rollback.py
├── dream_loop/                    # semanal
├── distill_loop/                  # diario
├── failure_registry/
└── tests/
```

---

## REPO 8 — AGENTES (instalación)

```
agentes/
├── claude_code/
│   ├── install.sh
│   ├── config_a.yaml              # NVIDIA_API_KEY_A
│   ├── config_b.yaml
│   ├── config_c.yaml
│   └── config_d.yaml
├── mimo_code/
│   ├── install.sh
│   ├── config_a.yaml              # GROQ_API_KEY_A
│   ├── config_b.yaml
│   ├── config_c.yaml
│   └── config_d.yaml
├── open_claw/
│   ├── install.sh                 # comando hermes
│   ├── config.yaml
│   └── orchestrator.py
└── api_keys/
    └── .gitignore
```

---

## CONEXIONES ENTRE REPOS

```
Open Claw (Repo 1, 2)
    │
    ├─→ GRUPO A → Repo 1 (orquestador-auditor) + Repo 2 (cerebro)
    │
    ├─→ GRUPO B → Repo 3 (fichas)
    │
    ├─→ GRUPO C → Repo 4 (router)
    │
    └─→ GRUPO D → Repo 5 (frontend)

Repo 6, 7 → los que terminen primero
Repo 8 → instalación común
```

**Regla:** cada repo importa solo al de al lado. NO imports directos entre grupos.

---

## DÓNDE VAN LAS 3 ETAPAS

| Etapa | Repo | Carpeta | Función |
|---|---|---|---|
| ETAPA 1 - input | Repo 3 (fichas) | `imput/` | captura, normaliza, hashea |
| ETAPA 2 - procesamiento | Repo 3 (fichas) | `procesamiento/` | razona, decide, valida |
| ETAPA 3 - output | Repo 3 (fichas) | `output/` | formatea y entrega |

---

## CRITERIOS DE ACEPTACIÓN

- [x] 8 repositorios definidos
- [x] Cada repo tiene estructura clara
- [x] 3 etapas en Repo 3 (fichas)
- [x] Conexiones entre repos
- [x] Sin imports directos entre grupos
- [x] LOC estimado: 33.000

DOCUMENTO 02 COMPLETO V1.0
