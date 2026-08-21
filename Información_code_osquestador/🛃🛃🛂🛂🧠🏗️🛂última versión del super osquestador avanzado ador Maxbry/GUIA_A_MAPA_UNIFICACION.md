# GUÍA INTERNA A — MAPA MAESTRO DE UNIFICACIÓN
# Documento de trabajo de Claude — fuente de verdad para construir
# NO resumir. Auditar antes de cada armado final.
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROPÓSITO DE ESTE DOCUMENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Existen 6+ documentos fuente que describen arquitecturas
parcialmente superpuestas del mismo sistema, escritos en
momentos distintos con distinto nivel de madurez. Este
documento es el ÁRBITRO: dice qué aporta cada uno, qué se
fusiona, qué se descarta, y por qué. Sin esto, el riesgo es
reconstruir el mismo concepto 3 veces con 3 nombres distintos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INVENTARIO DE FUENTES (con veredicto)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUENTE 1 — Kernel NCT DOC1-4 (construido por Sonnet, este chat)
  Contiene: 64 nodos, PUSH_PING 30, MYTHOS, Decision Engine v2,
  Memory 4 tiers, Team Agent v1, API Router R1-R10, Interface 9 capas
  VEREDICTO: ES LA BASE. Todo lo demás se fusiona SOBRE esto,
  no lo reemplaza salvo donde se indique explícitamente abajo.

FUENTE 2 — GRUPO_H (MAXBRY AGI G2, 300 expertos)
  Contiene: OC, Motor Cognitivo 14 funciones, contrato experto
  v1.0, 3 niveles jueces, sequence.json
  VEREDICTO: VÁLIDO. Es el catálogo de "fichas de razonamiento"
  que corren usando el motor determinista de FUENTE 4.

FUENTE 3 — GRUPO_F (JUEZ+ESCRITOR+RUNTIME)
  VEREDICTO: VÁLIDO. Sin cambios. Es transversal a todo.

FUENTE 4 — "cerebro G2 alma definitiva" (G2_PECP v2.5, 246 ítems)
  Contiene: cerebro de 5 piezas (Router/Índice/DAG/Memoria/
  Loader-Verifier-Executor), PLANNER_OFFLINE, Slot Contract
  SC1-SC6, Verifier N0-N5, GCL-lite+GCL v1.0 (motor Z3),
  Causal Engine, fallback.json 4 niveles, 2 repos (brain+modules)
  VEREDICTO: SE FUSIONA COMPLETO. Es el MOTOR DE EJECUCIÓN
  DETERMINISTA que le faltaba al Kernel NCT. Ver mapeo exacto
  en sección siguiente. Confirmado por el Director como
  "aportar GCL/Z3/SlotContract completo, si ya aprobado o no
  aporta nada se ignora" → SÍ aporta, SE INTEGRA.

FUENTE 5 — "02-ARQUITECTURA-8-REPOS.md"
  Contiene: 8 repos concretos con estructura de carpetas
  VEREDICTO: BASE VÁLIDA para estructura de repos, pero el
  Director pidió "separar lo más posible" → se EXPANDE, no
  se usa tal cual (ver GUÍA D).

FUENTE 6 — Doc con "14 repos + G1-G6 + 7 HF Spaces + MAXBRY
  SUPER TEAM (30 micro-agentes/11 roles/6 niveles autonomía)"
  VEREDICTO: IGNORADO EN SU MAYORÍA. El Director confirmó:
  "si ya está aprobado o no aporta nada nuevo lo ignoras".
  El Team Agent ya fue rediseñado en el Paso 1 (staff de
  agentes externos + micro-agentes condicionales) — ese
  rediseño YA CUBRE lo que "MAXBRY SUPER TEAM" intentaba
  resolver, con mejor separación cerebro/ejecución.
  ÚNICO valor rescatado: la referencia de "dónde viven los
  agentes" (HF Spaces como infraestructura de ejecución) —
  el Director lo confirmó como "solo referencia de conexión".

FUENTE 7 — "03-LOOPS-10-NIVELES" + "07-LOOP-CLAUDE-10X-MHYTOS"
  + "orquestacion-from-docs-part12" (6 niveles autonomía L1-L6)
  VEREDICTO: SE FUSIONA COMPLETO como el "Sistema de Loops
  Aislado" que el Director marcó como LA CLAVE del orquestador.
  Ver GUÍA C.

FUENTE 8 — "si_o_si_orquestador_parte_2" + "si_o_si_para_
  Maxbry" (microkernel Brain Core 11 módulos, Workspace
  Orchestration, Perfiles/DNA, 1000 loops en 9 fases,
  Hyper Planner/World Model/Causal Engine, Ultra/Omega Plan)
  VEREDICTO: PARCIAL.
  - Microkernel Brain Core 11 módulos → SE ADOPTA como
    filosofía de diseño del cerebro (confirmado Paso 1 preg.10)
  - Workspace Orchestration → SE ADOPTA como repo separado
    (confirmado Paso 1 preg.9)
  - 1000 loops / Hyper Planner / World Model → SE FUSIONA
    dentro del Sistema de Loops Aislado (GUÍA C) como el
    nivel TURBO (800-1000), no como sistema paralelo nuevo
  - Perfiles/DNA (Goal/Skill/Workflow/Decision/Learning/
    Project DNA) → SE FUSIONA con FICHA_IDENTIDAD + GOAL_LOCK
    ya existentes en PUSH_PING [17] y [19] de DOC1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JERARQUÍA FINAL (4 niveles, ya confirmada, ratificada aquí)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIVEL A — MAXBRY AGI (razonamiento avanzado, hecho con Opus,
          futuro controlador — fuera del alcance de construcción
          actual, solo se deja el gancho de conexión)
NIVEL B — MAXBRY ORQUESTADOR = FUENTE 1 (Kernel NCT) fusionado
          con FUENTE 4 (motor G2_PECP) — ESTE es "el cerebro"
NIVEL C — TEAM AGENTE = DOC2 rediseñado (staff agentes externos
          + micro-agentes condicionales + pipelines propios)
NIVEL D — SENTINELA (nuevo, ver GUÍA E — no construido aún)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAPEO EXACTO FUENTE 4 → KERNEL NCT (FUENTE 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DOC1 nodo existente          | FUENTE 4 aporta              | Acción
------------------------------|-------------------------------|------------------
[24] Executor                 | Loader+Verifier+Executor      | FUSIONAR: [24]
                               | separados, DAG topological    | se divide en 3
                               | sort a nivel ficha            | sub-módulos
[26] Artifact Engine           | Object Storage + Xata index   | AÑADIR: backend
                               |                                | concreto de storage
[29] Validator                 | Verifier N0-N5 + Slot         | REEMPLAZAR: [29]
                               | Contract SC1-SC6               | se implementa así
[30.2] Recovery Engine         | fallback.json 4 niveles       | FUSIONAR: mismos
                               | (retry/alternate/abort/        | 5 niveles ya
                               | compensate)                    | existentes, se
                               |                                | añade "compensate"
NUEVO (no existía en DOC1)     | PLANNER_OFFLINE                | AÑADIR nodo nuevo:
                               | (Requirements→DAG compiler,    | vive ANTES de [2]
                               | Python puro, repo brain)        | Goal Engine, en F-1
NUEVO                          | GCL-lite (por fase, O(1))       | AÑADIR: se activa
                               | + GCL v1.0 (gate final, Z3)    | en [30] Self Check
                               |                                 | y en P12/P13 del
                               |                                 | pipeline JUEZ
NUEVO                          | Causal Engine (causa/habilita/  | AÑADIR: nueva
                               | efecto_si_falla/sustituible_por)| sub-función en
                               |                                 | Recovery Engine
NUEVO                          | Speculative Execution           | AÑADIR: optimización
                               | (pre-carga fichas COMMITTED)    | opcional v1.5+
[27] Memory                    | FAISS en BRAIN + TTL por tier   | FUSIONAR: Tier0-3
                               | {0:None,1:30d,2:7d,3:24h,4:1h}  | ya mapea, se añade
                               |                                 | TTL concreto
NUEVO                          | 5 Registros (APPROVED,          | AÑADIR: se integra
                               | INTEGRATION, KPI, LEDGER,       | con [30.1] Audit
                               | PUZZLE_MAP)                     | Logger existente

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGLAS ABSOLUTAS DE FUENTE 4 — YA COMPATIBLES CON DOC1
(confirmación de no-conflicto, no requieren cambio)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ "MAXBRY decide, LLM ejecutan" = ya es nuestra regla de oro
✅ "90% código/10% LLM" = ya está en Token Budget Manager [7.2]
✅ "Agentes NUNCA tocan el cerebro" = ya es LEY_5 del ADN_SYSTEM
✅ "1 ficha = 1 función aislada" = ya es RG-01/RG-02 del ESCRITOR
✅ "sequence.json única fuente de flujo" = ya integrado en GRUPO_H
✅ "DAG=ejecución / FSM=gobernanza" = ya es la separación
   Graph Runtime[10] (DAG) vs Lifecycle Engine[5]+Decision[15] (FSM)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LO QUE SE DESCARTA EXPLÍCITAMENTE (con razón)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ HFSM / BehaviorTree / GOAP-MAXBRY (FUENTE 4 ya las marca
   como "reliquias eliminadas" — reemplazadas por DAG+Causal+
   PLANNER_OFFLINE. NO se reintroducen.)
❌ CCL 20 capas / 14 motores F-1 / 7 motores (ídem, eliminadas
   en FUENTE 4, razón: redundantes con MYTHOS)
❌ 5 técnicas ML / NeuronCore / Pattern Scanner (ídem)
❌ "MAXBRY SUPER TEAM" completo tal cual descrito en FUENTE 6
   (30 micro-agentes/11 roles/10 colas/12 task models) — ya
   cubierto por el Team Agent rediseñado (Paso 1, respuestas 7-8)
❌ 14 repos + G1-G6 + 7 HF Spaces COMO ESTRUCTURA CENTRAL
   (FUENTE 6) — sobrevive solo como "referencia de dónde
   viven los agentes externos", no como arquitectura de repos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PENDIENTE DE CONSTRUIR (siguientes guías)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GUÍA B — GCL + Z3 + Slot Contract integrado (pseudo+Python)
GUÍA C — Sistema de Loops Aislado escalable 10-1000 (LA CLAVE)
GUÍA D — Estructura final de repos (expandida al máximo)
GUÍA E — Sentinela (módulo nuevo, auto-mejora de método/desempeño)
GUÍA F — MD segmentado + HTML visual (Orquestador + Team Agent)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA A
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_A_MAPA_UNIFICACION","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno_no_para_director",
    "fuente_de_verdad":true},
  "fuentes_auditadas": 8,
  "veredictos": {
    "fuente1_kernel_nct": "ES_LA_BASE",
    "fuente2_grupo_h": "VALIDO_catalogo_fichas",
    "fuente3_grupo_f": "VALIDO_transversal",
    "fuente4_g2_pecp_alma": "SE_FUSIONA_COMPLETO_motor_ejecucion",
    "fuente5_8repos": "BASE_para_expandir",
    "fuente6_14repos_g1g6": "IGNORADO_mayoria_solo_referencia_infra",
    "fuente7_10niveles_loops": "SE_FUSIONA_como_sistema_loops_aislado",
    "fuente8_sisisi_brain_workspace": "PARCIAL_microkernel+workspace+dna_si"
  },
  "mapeo_fuente4_a_doc1": {
    "executor_dividido_en_3": "loader+verifier+executor",
    "artifact_engine_add": "object_storage+xata",
    "validator_reemplazado_por": "verifier_N0N5+slot_contract_SC1SC6",
    "recovery_fusiona": "fallback_json_4_niveles+compensate",
    "nuevo_planner_offline": "vive_antes_de_goal_engine_en_F-1",
    "nuevo_gcl": "gcl_lite_por_fase+gcl_v1_gate_final_Z3",
    "nuevo_causal_engine": "sub_funcion_de_recovery_engine",
    "nuevo_speculative_exec": "optimizacion_opcional_v1.5",
    "memory_fusiona": "faiss_brain+ttl_por_tier",
    "nuevo_5_registros": "integra_con_audit_logger"
  },
  "descartado": ["HFSM","BehaviorTree","GOAP-MAXBRY","CCL_20capas",
    "14_motores_F-1","5_tecnicas_ML","NeuronCore","Pattern_Scanner",
    "MAXBRY_SUPER_TEAM_completo","14repos_G1-G6_como_estructura_central"],
  "siguiente_documento": "GUIA_B_GCL_Z3_SLOTCONTRACT"
}
