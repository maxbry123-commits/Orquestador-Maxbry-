# INSTRUCCIONES SONNET — PARTE 1/2 (S7-S13)
# Formato por salida: OBJETIVO · ARCHIVOS+LOC · CONTRATOS · ORDEN · TESTS · PROHIBIDO
# Regla global: máx 400 LOC/archivo · Python 3.11 · enchufe v1.5 en todo módulo ·
# task_id+trace_id en todo dato · sin LLM fuera de cápsulas · flags solo en config.

---

## S7 — ENCHUFE UNIVERSAL v1.5 (repo 12: contracts-schemas)
**OBJETIVO:** implementar el validador y registry del Universal Module Contract v1.5 (schema JSON ya cerrado). Nada se conecta al sistema sin pasar por aquí.
**ARCHIVOS:**
- `contracts/universal_module_contract.v1.5.json` (copiar schema aprobado tal cual)
- `enchufe/validator.py` ~250 — jsonschema strict + 22 invariantes cross-field (rol source⇒consume null; estado active⇒hash real sha256:64; transform⇒input_map/output_map; deadline≥timeout; sandbox none⇒permisos vacíos...)
- `enchufe/registry.py` ~200 — alta/baja/consulta de contratos; solo estado `active` es conectable; índice por datatype para autoensamblaje
- `enchufe/compat.py` ~120 — `son_compatibles(a,b)`: produce.datatype==consume.datatype + versioning min/max/mode
**ORDEN:** schema → validator → tests 53 casos (suite ya definida, 100% pass) → registry → compat.
**TESTS:** los 53 casos existentes + `test_active_sin_hash_falla` + `test_autoensamblaje_por_datatype`.
**PROHIBIDO:** relajar el schema; aceptar contratos draft en runtime; inferir campos faltantes.

---

## S8 — INPUT FABRIC P1 (repo 6: fichas/input)
**OBJETIVO:** fase de entrada completa: Anchor → PUSH_PING(30 clasificaciones) → filtros A1-A5 → OCR → normalización → descomposición → GOAL_LOCK → Task Graph.
**ARCHIVOS:**
- `input/anchor.py` ~300 — clasifica intención, lanza en paralelo (asyncio.gather): preguntas al Director + investigación previa; emite `knowledge_pack`
- `input/push_ping.py` ~350 — las 30 clasificaciones (tabla del KERNEL v2 [§PUSH_PING] literal, enum + reglas); salida: `{clase, prioridad, nivel_sugerido}`
- `input/filtros_a.py` ~380 — A1 captura multimodal, A2 axiomáticos AX01-08 (BLOQUEANTE: cualquier hit → REJECTED), A3 normalizadores, A4 descomponedores, A5 coherencia. 20 checks por grupo = funciones puras
- `input/ocr_adapter.py` ~150 — Baidu OCR vía ficha `kind:api`; fallback tesseract local; SOLO se invoca en P1 (Sheriff SH05 lo vigila)
- `input/goal_lock.py` ~120 — construye GoalLock (Salida 2) desde objetivo+DoD+not_in_scope; congela con hash; sin DoD → pregunta al Director, JAMÁS inventa
- `input/task_graph.py` ~200 — descompone en subtareas con depends_on; salida = requirements.json para PLANNER_OFFLINE
**CONTRATO SALIDA P1:** `{goal_lock_hash, task_graph, knowledge_pack, clase_pushping}` — required los 4.
**TESTS:** `test_a2_bloquea_axioma`, `test_goal_sin_dod_pregunta`, `test_pushping_30_clases`, `test_ocr_fuera_p1_imposible`.
**PROHIBIDO:** filtrar/descartar información del Director (regla SCANNER); avanzar sin GOAL_LOCK; OCR fuera de P1.

---

## S9 — ESCRITOR + RUNTIME (repos 8-9)
**OBJETIVO:** implementar LLM_ESCRITOR (doc canónico A.2) y RUNTIME real (Builder/Validator/Witness) que produce Evidence Report L1-L4 con hash — lo que el Juez (Salida 2) ya consume.
**ARCHIVOS:**
- `escritor/escritor_core.py` ~350 — recibe `Instruction`, genera output según `output_schema`, self_check honesto, adjunta `instruction_id`; few-shot desde FailureRegistry; NUNCA declara éxito en texto
- `runtime/builder.py` ~200 — prepara sandbox (venv/Docker), instala deps declaradas en ficha
- `runtime/validator_niveles.py` ~380 — L1 static (ruff+mypy+AST), L2 build (import+compile), L3 runtime (pytest de la ficha), L4 feature (test de aceptación del DoD); cada nivel: `{status, logs, duracion}`
- `runtime/witness.py` ~180 — reproduce ejecución 1 vez, calcula `evidence_hash = sha256(report sin el campo hash)` (fórmula exacta del Juez), firma
**ORDEN:** builder → validator L1..L4 → witness → escritor.
**TESTS:** IT-style: `test_l3_fallo_status_fail`, `test_evidence_hash_reproducible`, `test_escritor_humo_autodetectado`.
**PROHIBIDO:** mocks en L3/L4; evidencia sin hash; Escritor auto-aprobándose.

---

## S10 — OUTPUT FABRIC P3 (repo 6: fichas/output)
**OBJETIVO:** subsistema de salida: OutputContract → Planner → Builder → 10 checks binarios E-OUT → Repair(1 retry) → Output Diff vs goal → Formatter.
**ARCHIVOS:**
- `output/output_contract.py` ~150 — declara ANTES de generar: formato, secciones required, límites, audiencia
- `output/planner_builder.py` ~250 — arma la salida por secciones desde el consolidado de Fusion
- `output/checks_eout.py` ~350 — E-OUT-001..010 binarios (completitud DoD, sin humo, sin scope creep, formato, citas/evidencia, límites LOC, secciones, coherencia goal, sin placeholders, hash presente). PASS=10/10
- `output/repair.py` ~150 — 1 solo retry dirigido por los checks fallidos; si vuelve a fallar → ESCALATE al Juez
- `output/diff_goal.py` ~120 — diff semántico salida vs GoalLock.DoD; % cobertura por ítem
- `output/formatter.py` ~150 — MD/JSON/HTML según contrato; sellado final hash-chain
**TESTS:** `test_10_checks_binarios`, `test_repair_solo_1_retry`, `test_diff_cubre_dod`.
**PROHIBIDO:** emitir con <10/10; más de 1 repair; formatear antes de validar.

---

## S11 — VERIFIER N0-N5 + SC1-SC6 + GCL (repo 4: validacion)
**OBJETIVO:** la aduana G2 completa.
**ARCHIVOS:**
- `verifier/n0_n5.py` ~380 — N0 GPG (gpg-agent), N1 sha256+revocation_list, N2 jsonschema+allowed_imports whitelist, N3 versión, N4 compat kernel, N5 AST ratio LLM>10% o diff>0.05 → REJECTED (+cache por hash, invalidar en DEPRECATED; corre en CI/CD y runtime)
- `verifier/slot_contract.py` ~150 — SC1 id único en APPROVED, SC2 hash verificable, SC3 schemas no vacíos, SC4 runtime_type, SC5 llm_ratio≤0.10, SC6 idempotente explícito
- `gcl/gcl_lite.py` ~120 — O(1) por fase: presupuesto>0 + contratos + task_id + hash(last_ledger)
- `gcl/gcl_v1.py` ~250 — gate final F4 único: Z3 sat/unsat con 5 restricciones (goal_lock, scope, recursos, DAG completo, evidencia); `z3-solver==4.12.4`
- `verifier/revocation.py` ~100 — revocation_list.json firmado, Set[str]
**TESTS:** IT04 commit sin GPG→REJECTED, IT05 ficha 15% LLM→REJECTED, `test_z3_unsat_bloquea_f4`.
**PROHIBIDO:** GCL decidiendo (solo verifica); saltar N0-N5 "por rapidez"; passphrase en env.

---

## S12 — MEMORIA 4 TIERS + FAISS (repo 11, extiende Salida 3)
**OBJETIVO:** memoria completa sobre el State Engine ya hecho.
**ARCHIVOS:**
- `memoria/tiers.py` ~250 — Tier0 constitution / 1 blueprints / 2 artifacts / 3 states / 4 metadata con schemas G2 ítem 44; TTL {0:None,1:30d,2:7d,3:24h,4:1h}; GC cada `G2_GC_INTERVAL`
- `memoria/faiss_brain.py` ~300 — `faiss_brain[task_id]=IndexFlatL2`; modo `G2_FAISS_MODE: faiss|dict`; lazy init + unload 30min; Spaces reciben embeddings, JAMÁS acceden a FAISS
- `memoria/shared_knowledge.py` ~200 — BINARIO: solo COMMITTED entra, escritura atómica completa-o-nada; dependency_graph con hash_snapshot; huérfana→busca→si no→TaskRejectedError
- `memoria/kg_sqlite.py` ~250 — grafo de conocimiento (nodos/relaciones) SQLite; alimenta Graphiti
**TESTS:** IT06 sin COMMIT no entra, `test_ttl_gc`, `test_faiss_fallback_dict`, `test_huerfana_rejected`.
**PROHIBIDO:** memoria del usuario fuera de su dispositivo; parciales en shared_knowledge.

---

## S13 — AUDIT BUS (repo 1: auditor/)
**OBJETIVO:** bus transversal con puntos marcados por fase (matriz DSL SH05).
**ARCHIVOS:**
- `auditor/audit_bus.py` ~250 — API única `evento(tipo,datos)` (ya consumida por KernelCore); cola async; hash-chain JSONL (patrón FailureRegistry); OpenTelemetry span por ficha → traces.jsonl
- `auditor/obsidian_writer.py` ~200 — 1 nota MD por evento relevante en vault `/audit_vault/{task_id}/`, backlinks [[goal]] [[ficha]]
- `auditor/graphiti_writer.py` ~200 — relaciones al KG (kg_sqlite): tarea→ficha→evidencia→resultado
- `auditor/hallucination_check.py` ~250 — SelfCheckGPT: 3 muestras vía Router, divergencia>umbral → flag `HALLUCINATION` al Juez (P2/P3 únicamente)
- `auditor/g2cli.py` ~200 — Typer: `status/logs/pause/trace <trace_id>/recover --dry-run`
**TESTS:** `test_cadena_audit_integra`, `test_trace_reconstruye_arbol`, `test_hallucination_flag`.
**PROHIBIDO:** auditoría opcional; escribir al bus sin task_id; borrar notas del vault.
