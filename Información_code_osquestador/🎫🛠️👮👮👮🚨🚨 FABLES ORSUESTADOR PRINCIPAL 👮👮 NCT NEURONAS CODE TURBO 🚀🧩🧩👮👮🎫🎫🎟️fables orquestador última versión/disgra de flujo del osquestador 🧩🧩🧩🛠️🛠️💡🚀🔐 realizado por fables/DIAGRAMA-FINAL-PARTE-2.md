```json
{
  "checkpoint_id": "DIAGRAMA-FINAL-PARTE-2-de-3",
  "fases_cubiertas": "F4 (ejecución — única con IA plena), F5 (monitoreo), F6 (verificación 3 capas + aduana G2)",
  "pasadas": "3 (inventario doc por doc + comparación vs Parte 1 + validación cruzada interna)",
  "integra_adicionalmente": "elementos rescatables de MAXBRY SUPER TEAM (CSA 10 jueces como panel de F6-C, BIS 13 criterios, 5 agentes investigación, consenso 5 agentes) que la Parte 1 no había incorporado",
  "estilo": "documento 30 (deepseck)"
}
```

# VERSIÓN FINAL — PARTE 2/3 (F4 → F6)

```
                 [VIENE DE PARTE 1: F3 entrega Handoff firmado]
                            │
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F4: EJECUCIÓN — ÚNICA FASE CON IA PLENA                       │
│                                                               │
│ ┌───────────────────────────────────────────────────────────┐ │
│ │ F4.1 RAZONAMIENTO (motor F0-F11 + Mythos integrado)       │ │
│ │  nivel 1→3 fases | nivel 4→12 fases | nivel 0→auto        │ │
│ │  F0 incógnitas bloqueantes → FM MYTHOS (40 pasos,         │ │
│ │  5 arquetipos narrativos, estructura el problema) →       │ │
│ │  F1 árbol → F2 expansión fractal (máx 7 nodos, poda≥40)   │ │
│ │  → F3 hipótesis A/B/C → F4 combinación → F5 panel 5       │ │
│ │  expertos 0-100 → F6 evolución genética (fitness=         │ │
│ │  (viab+imp+(100-costo))/3, top20%→mutación→top5%) →       │ │
│ │  F7 estrés triple: abogado del diablo + pre-mortem +      │ │
│ │  simulación normal/extremo/fallo                          │ │
│ │  CADENA DE CONTROL (12 capas, orden fijo): MYTHOS→FSM→    │ │
│ │  ROUTER→SHERIFF→SENTINEL→VERIFIER→CRITIC→JUDGE→POLICY→    │ │
│ │  PYDANTICAI→RETRY_ENGINE→LLM                              │ │
│ │  + EURS Standard/Turbo + DRE 9 pasos + micro-ciclo 7      │ │
│ │  (razonamiento de la serie MAXBRY, sobrevive como método) │ │
│ └─────────────────────────┬─────────────────────────────────┘ │
│ ┌─────────────────────────▼─────────────────────────────────┐ │
│ │ F4.2 ENJAMBRE COGNITIVO (código real H1)                  │ │
│ │  LOOP ENGINE: 9 fases, escala 20→1000 loops, escalado     │ │
│ │  dinámico si progreso_real < esperado×0.6                 │ │
│ │  EXPERT POOL: 300 expertos YAML (0 LOC c/u), 15 células,  │ │
│ │  activa 20-500 según nivel; mapeo fase→célula (GUIA_A1:   │ │
│ │  FASE_4 debate→célula B4 E161-E180 + Devil Agent)         │ │
│ │  Si falta capability → TDAG _spawn ad-hoc (draft, solo    │ │
│ │  permanente con firma del Director en ledger)             │ │
│ │  ANTI-ECHO: score similitud ≤0.30 entre expertos          │ │
│ │  MEMORIA TRANSACCIONAL: nadie escribe directo →           │ │
│ │  proposals append-only → FusionEngine (accuracy·0.35 +    │ │
│ │  evidencia·0.30 + contexto·0.20 + recencia·0.15) →        │ │
│ │  1 COMMIT único a ObjetoCognitivo.evolucionar()           │ │
│ │  (9 bloques, versión++, fingerprint sha256 encadenado)    │ │
│ └─────────────────────────┬─────────────────────────────────┘ │
│ ┌─────────────────────────▼─────────────────────────────────┐ │
│ │ F4.3 WORKER POOL PARALELO (fusión Kimi+MiniMax, doc 30)   │ │
│ │  hasta 100 workers asyncio.gather (Kimi)                  │ │
│ │  dentro de c/worker: Team Engine leader→worker→verifier   │ │
│ │  3 rondas (MiniMax) | granularidad adaptativa: router     │ │
│ │  decide 1-grande vs 100-chicos según tarea                │ │
│ │  TEAM mode ≠ parallel branches: equipos completos pueden  │ │
│ │  COMPETIR sobre el mismo input, coordinador elige mejor   │ │
│ │  BATCHING: llamadas LLM agrupadas 8-16 (no 1-by-1, 4-10x) │ │
│ │  MULTI-POOL por concern (UI/research/deploy/audit),       │ │
│ │  cada pool con su cola, auto-scaler y budget              │ │
│ │  90/10: presupuesto llm_pct≤0.10 vigilado (PROP-18)       │ │
│ └─────────────────────────┬─────────────────────────────────┘ │
│ ┌─────────────────────────▼─────────────────────────────────┐ │
│ │ F4.4 ESCRITOR + STAFF + ORQUESTADORES PARALELOS           │ │
│ │  LLM_ESCRITOR (O1-O6/R01-R10): tests con assertions       │ │
│ │  ANTES del código; NUNCA dice "funciona"; solo recibe     │ │
│ │  del Juez (INSTRUCTION/RETRY_INSTRUCTION, máx 3)          │ │
│ │  STAFF EXTERNO (pipelines intercambiables, MAPA_TEAM):    │ │
│ │  pipeline_code_gen→Claude Code/OpenCode | research→       │ │
│ │  5 agentes investigación (GitHub/HF/Web/YouTube/MCP,      │ │
│ │  2-5 rondas, stop evidencia≥85%) | refactor→Aider/        │ │
│ │  OpenClaw | generic→micro-agente propio                   │ │
│ │  MICRO-AGENTES propios SOLO si staff no cubre capability  │ │
│ │  (15 definidos MA-CODE-GEN..MA-RUNTIME-CHECK, spawn→run→  │ │
│ │  emit JSON→die, ≤200 LOC, 90/10)                          │ │
│ │  ORQUESTADOR PARALELO: Execution Pipeline DSL (OpenClaw,  │ │
│ │  15 nodos N00-N13, código probado) corre COMPLETO en      │ │
│ │  paralelo — recibe orden DSL, devuelve resultado firmado, │ │
│ │  el Witness lo certifica igual que cualquier artifact     │ │
│ │  + flota HF Spaces: 10-20 workers remotos MCP (PROP-17,   │ │
│ │  ComputePool 80 / HybridPool 15 / LLMPool 5)              │ │
│ └───────────────────────────────────────────────────────────┘ │
│ DISCIPLINA E01-E12 (UOOS): tras GO prohibido replanificar,    │
│ prohibido proponer arquitecturas alternativas, comunicación   │
│ con Director limitada a 7 eventos                             │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F5: MONITOREO SIMULTÁNEO (0% IA — corre EN PARALELO a F4)     │
│                                                               │
│ ┌────────────┐ ┌──────────────┐ ┌───────────────────────┐    │
│ │ GUARDIAN   │ │ WATCHDOG 30s │ │ TRIPLE MONITOR (doc30)│    │
│ │ 6 booleanos│ │ ¿responde?   │ │ PAD: arousal>0.8 ∧    │    │
│ │ →RECHAZO   │ │ ¿hash chain  │ │  pleasure<0.2 →       │    │
│ │ inmediato  │ │  íntegro?    │ │  SIGKILL+respawn      │    │
│ │            │ │ ¿checkpoint  │ │ ANSIEDAD (MiniMax):   │    │
│ │            │ │  válido?     │ │  ¿duda en círculos?   │    │
│ │            │ │ ¿estancado?  │ │  L1 log→L2 pause→     │    │
│ │            │ │ 3 fallos →   │ │  L3 SIGKILL           │    │
│ │            │ │ DEGRADED_MODE│ │ ANTI-DRIFT (Kimi):    │    │
│ │            │ │ + notifica   │ │  KL(plan‖actual)>0.02 │    │
│ │            │ │  Director    │ │  → halt + rollback    │    │
│ └────────────┘ └──────────────┘ └───────────────────────┘    │
│ ┌───────────────────────────────────────────────────────────┐ │
│ │ 6 DETECTORES UOOS siempre activos: estancamiento /        │ │
│ │ repetición / deriva_objetivo / tiempo_excesivo /          │ │
│ │ tokens_excesivos / degradación → el loop activo ROTA      │ │
│ │ estrategia de su pool (delta_score medido, nunca repite   │ │
│ │ la misma táctica) → escalada fija de 5 niveles            │ │
│ │ LOOPS-INFRA (separado del Loop cognitivo): heartbeat 30s, │ │
│ │ señales SYS_HALT/PAUSE/RESUME, DLQ con jitter, meta-loop  │ │
│ │ vigila loops sin avance                                   │ │
│ │ SENTINEL_SECURITY: vigila código/workflows/tools/agentes/ │ │
│ │ memoria/contenedores/APIs → INCIDENTE|ALERTA|VULN|MEJORA  │ │
│ └───────────────────────────────────────────────────────────┘ │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
┌───────────────────────────────────────────────────────────────┐
│ F6: VERIFICACIÓN — "LA ADUANA G2" (3 capas secuenciales)      │
│                                                               │
│ CAPA A (0% IA) — INTEGRIDAD TÉCNICA                           │
│  VERIFIER N0-N5: N0 firma GPG → N1 sha256 → N2 schema →      │
│  N3 semver → N4 whitelist imports (AST) → N5 llm_ratio        │
│  ≤0.10 (AST) — falla UNO → STOP                               │
│  + Enchufe Universal v2.0: 22 invariantes cross-field,        │
│  autoensamblaje por datatype, solo contratos "active"         │
│  + 10 checks E-OUT-001..010 del Output Fabric (PASS 10/10)    │
│                                                               │
│ CAPA B (0% IA) — VERIFICACIÓN FORMAL                          │
│  GCL lite por fase + GCL v1.0 gate final con Z3 (SAT/UNSAT)   │
│  + SlotContract SC1-SC6                                       │
│                                                               │
│ CAPA C (IA SOLO AQUÍ) — JUICIO                                │
│  SISTEMA JUECES 3 NIVELES: Local(≥0.70)→Capa(≥0.60)→          │
│  Central(E296, final) | default=RETRY, NUNCA aprueba          │
│  sin evidencia | jueces votan EN PARALELO SIN VERSE           │
│  (anti-anclaje) | Sheriff+Centinela con VETO inmediato        │
│  Panel opcional para tareas critical: los 10 criterios CSA    │
│  (J1 objetivo..J10 UX) sobreviven como RÚBRICA del Juez       │
│  Central — no como 10 agentes separados                       │
│  + CONSENSO 5 AGENTES para decisiones de diseño:              │
│  Creative/Innovation/Critic/Selection/Architecture —          │
│  3+ de acuerdo→procede | empate→escala a Director             │
│                                                               │
│ WITNESS (0% IA) — LA PRUEBA REAL                              │
│  Builder escribe archivo físico → Validator L1 (lint/mypy/    │
│  anti-mock) → Witness ejecuta: L2 build real → L3 runtime     │
│  levanta → L4 tests reales → firma evidence_hash              │
│  RT-01: no PASS si nivel requerido falló | RT-02: nunca       │
│  simula el reporte | RT-04: hash no coincide →                │
│  EVIDENCE_TAMPERING → abort                                   │
│  GOAL CHECK (RT-31, UOOS): Tribunal PASA ≠ nodo done —        │
│  si el goal real no se cumplió, NO se marca terminado         │
└───────────────────────────┬───────────────────────────────────┘
                            ▼
                 [PARTE 3/3: F7 memoria → F8 recovery → F9 entrega]
```

## RESUMEN AMPLIO — PARTE 2

**F4 es la única fase donde la IA piensa, y aún así está encadenada.** El razonamiento entra por Mythos (que estructura el problema como narrativa antes de tocar lógica), baja al motor F0-F11 (hipótesis→evolución genética→estrés triple), y todo lo que produce pasa por la cadena de control de 12 capas — el pensamiento nunca ejecuta nada directamente, solo alimenta al control. El enjambre de 300 expertos funciona como un MoE de software: cientos escriben propuestas en paralelo pero NINGUNO tiene permiso de escritura sobre el objeto compartido; solo el FusionEngine consolida, con pesos fijos y un único commit versionado con huella criptográfica. Encima corre el paralelismo físico de la fusión Kimi+MiniMax: hasta 100 workers, cada uno con su propio mini-equipo leader/worker/verifier de 3 rondas, con batching de llamadas LLM y pools separados por tipo de trabajo para que una carga no bloquee otra. El staff externo (Claude Code, OpenCode, Aider, los 5 investigadores) se usa ANTES que construir nada propio; los micro-agentes propios son el último recurso; y el Execution Pipeline DSL de OpenClaw corre como un orquestador paralelo completo cuya salida se certifica igual que cualquier otra. La disciplina E01-E12 evita el mal que esta misma conversación sufrió: una vez dado el GO, el agente no replantea ni divaga.

**F5 vigila sin pensar.** Tres relojes independientes (Guardian booleano, watchdog de 30s, y el triple monitor PAD/Ansiedad/Drift de la fusión) más los 6 detectores de UOOS. La decisión clave: cuando algo se atasca, el sistema NO reintenta lo mismo — rota la estrategia del pool y mide el delta. Y los loops de infraestructura (heartbeat, colas muertas) están deliberadamente separados de los loops cognitivos: uno vigila la máquina, el otro vigila el pensamiento.

**F6 es la aduana en 3 capas + la prueba física.** Primero código puro (N0-N5, Z3, contratos) — la mayoría de los fallos muere aquí sin gastar un token de IA. Solo lo que sobrevive llega al Juez, que por diseño desconfía: su veredicto por defecto es RETRY, los jueces no se ven entre sí, y dos roles (Sheriff/Centinela) pueden vetar sin importar el score. Lo que la serie MAXBRY aportaba (CSA 10 jueces, consenso de 5) sobrevive aquí como rúbrica y como panel de decisiones de diseño — no como burocracia de 10 agentes más. Y al final, el Witness: nada está "hecho" hasta que se construyó de verdad, corrió de verdad y pasó tests de verdad, con hash de evidencia. El GOAL CHECK remata: pasar la aduana no es lo mismo que cumplir el objetivo.

**Gaps integrados en esta parte** (adicionales a Parte 1): GAP-P2-054/055 (motor F0-F11+niveles), GAP-CIERRE-006 (Mythos+cadena 12 capas), GAP-P3-031 histórico (cadena orden), GAP-P2-045/046/047 (ObjetoCognitivo/memoria transaccional/TDAG), GAP-P3-008 (mapeo fases→células), GAP-P3-040 (Loop Engine+1000 loops), doc30 completo (worker pool/team engine/PAD/ansiedad/drift/3 capas), GAP-CIERRE-008 (batching/multi-pool), GAP-P2-033 (TEAM vs branches), GAP-P3-019/020/021 (Escritor/Runtime/protocolo), GAP-CIERRE-003 (OpenClaw paralelo), PROP-17/18 (flota HF+presupuesto 90/10), GAP-P2-036 (E01-E12), GAP-P2-041 (11 loops/delta/detectores), GAP-P3-028 (Loops-Infra separado), NOTA_07 (Sentinel Security), GAP-P3-026 (Enchufe v2.0 22 invariantes), S10 (E-OUT 10 checks), GUIA_B (GCL/Z3/SC1-6), GAP-P3-051 histórico (jueces 3 niveles), GAP-P2-042 (Tribunal veto+voto ciego), CSA/consenso-5 rescatados de serie MAXBRY (como rúbrica/panel), GAP-P2-050+P3-020 (Witness L1-L4), GAP-P2-038 (Goal Check RT-31).

¿OK para Parte 3/3 (F7 memoria → F8 recovery → F9 entrega + despliegue determinista)?
