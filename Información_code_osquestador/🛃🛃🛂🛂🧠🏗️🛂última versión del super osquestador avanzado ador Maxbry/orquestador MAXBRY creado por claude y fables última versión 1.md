━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — ORQUESTADOR RAÍZ / DIAGRAMA COMPLETO
NCT KERNEL v0.4 — Agnóstico de provider — 64 nodos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A1] ADN_SYSTEM (pre-kernel, inmutable, versionado)
     ├── LEY_1: TODO_DEBE_SER_AUDITABLE
     ├── LEY_2: TODO_DEBE_SER_REVERSIBLE
     ├── LEY_3: TODO_DEBE_SER_TRAZABLE
     ├── LEY_4: TODO_CAMBIO_REQUIERE_VALIDACION
     ├── LEY_5: NINGUN_AGENTE_MODIFICA_ADN
     └── LEY_6: NINGUN_AGENTE_ALMACENA_TOOLS_EN_CEREBRO
     Propiedades: NO_EVOLUCIONABLE_AUTOMATICAMENTE
                  REQUIERE_INTERVENCION_HUMANA_EXPLICITA
     ▼

[A2] GUARDIAN_LAYER (máxima autoridad de seguridad)
     ├── VIOLA_ADN: boolean
     ├── VIOLA_LEYES: boolean
     ├── VIOLA_AUDITORIA: boolean
     ├── VIOLA_TRAZABILIDAD: boolean
     ├── VIOLA_SEGURIDAD: boolean
     └── VIOLA_AISLAMIENTO: boolean
     → cualquiera = true → RECHAZAR_SOLICITUD inmediato
     ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 0 — SUPERVIVENCIA AUTÓNOMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[0] AUTO-RECOVERY ENGINE │ ▼
    ├── Watchdog interno cada 30s (sin ping externo)
    ├── Self-evaluation loop continuo:
    │   ├── ¿Proceso principal responde? (timeout 5s)
    │   ├── ¿state.json hash chain íntegro?
    │   ├── ¿Checkpoint disponible y válido?
    │   └── ¿Última tarea sin avance > N minutos?
    ├── Si fallo detectado:
    │   ├── 1. Buscar último state.json válido (hash OK)
    │   ├── 2. Buscar último checkpoint firmado
    │   ├── 3. Calcular posición: replay_to_checkpoint(t)
    │   └── 4. Auto-reiniciar exactamente desde ese punto
    ├── Circuit Breaker:
    │   ├── Max 3 reintentos automáticos consecutivos
    │   └── 3 fallos → DEGRADED_MODE → notifica Director
    └── Logs: fault_log.json + recovery_log.json

[0.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 0
    ├── SENTINEL: detecta anomalías en el proceso de recovery
    ├── JUDGE: valida que el reinicio fue exitoso con evidencia
    └── SHERIFF: aplica y hace cumplir política de max_reintentos
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 1 — INGESTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1] INPUT │ ▼ 🔍 Revisión Contexto/Memoria │ ▼
    └── Invoca Orquestador Auditor cuando el input lo amerita
        (documentos grandes, alto volumen, input ambiguo)

[1.1] INPUT ADAPTER / NORMALIZER │ ▼
    ├── listen() → captura evento entrante
    ├── normalize(raw) → documento único estandarizado
    ├── ack(evento) → confirmación de recepción
    ├── Congelación inmediata: FROZEN VERSION 1.0
    │   (nada se modifica después de este punto)
    └── Estructura: {
          doc_id: sha256,
          origen: telegram|drive|mcp|kanboard,
          proyecto: string,
          tipo: string,
          ruta: string,
          timestamp: ISO-8601,
          frozen: true
        }

[1.2] HASH ENGINE / INVENTORY VALIDATOR │ ▼
    ├── SHA256 del documento completo
    ├── Consulta inventory.json → ¿ya procesado? → skip
    ├── Fingerprint multicapa (5 capas independientes):
    │   ├── L1 Léxico: SHA256 texto exacto (detecta copia)
    │   ├── L2 Semántico: embedding hash (detecta reformulación)
    │   ├── L3 Estructural: árbol de secciones (detecta reorganización)
    │   ├── L4 Entidades: set canónico nombres/fechas/cifras
    │   └── L5 Dependencias: grafo relaciones con otros docs
    └── Seed Analysis Pipeline S1→S5:
        ├── S1: indexar repo+state+RAG → seed_index.sqlite
        ├── S2: resumir cada artefacto → seed_summary.json
        ├── S3: detectar huecos info → seed_gaps.json
        ├── S4: proponer preguntas → seed_questions.json
        └── S5: enriquecer seed → seed_enriched.json
            Evidence sufficiency: 0.35×coverage +
            0.25×consistency + 0.20×diversity + 0.20×recency

[1.3] WAKE WORD ENGINE │ ▼
    ├── SYS_HALT → emergency_stop (para todo inmediato)
    ├── SYS_EXECUTE → force_execution_mode
    ├── SYS_PLAN → force_planning_mode
    ├── SYS_VERIFY → force_verification_mode
    ├── SYS_YIELD → pause_and_checkpoint (guarda y pausa)
    └── SYS_RESUME → resume_from_checkpoint (retoma)

[1.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 1
    └── Verifica integridad y completitud del input
        antes de permitir avance al PUSH_PING
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 0 — PUSH_PING INPUT (30 clasificaciones)
REGLA: orquestador NO avanza hasta tabla completa.
Si falta info → busca docs/web/repos/pregunta Director.
META: simular el plan 5 veces antes de ejecutar.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[01] 🎯 OBJETIVO_PRIMARIO
     requerido: true | si_falta: preguntar Director

[02] 🏗️ TIPO_TAREA
     TM01_ARCHITECTURE / TM02_CODE_GEN / TM03_RAG /
     TM04_VALIDATION / TM05_REPAIR / TM06_TEST /
     TM07_DEPLOY / TM08_DOC / TM09_DATA /
     TM10_SECURITY / TM11_LONG_HORIZON / TM12_SELF_IMPROVE
     si_falta: estimar con DRE Complexity Estimator

[03] ⚖️ TASK_LEVEL
     simple | critical | long_horizon
     si_falta: LLM_JUEZ evalúa antes de avanzar

[04] 📊 COMPLEJIDAD_DRE
     score: (deps×2)+steps+(5 si_ambiguo)+(5 si_riesgo)
     LOW(0-3)→9p/2i | MEDIUM(4-8)→16p/5i
     HIGH(9-15)→25p/10i | EXTREME(16+)→30-50p/20i+
     si_falta: calcular automáticamente

[05] 🔢 VOLUMEN_TAREAS
     rango: 1-1000 tareas
     modo: secuencial | paralelo | swarm | fractal
     segmentacion_continua:
       max_simultaneas: 200 | batch_size: 20 | overlap: 5
     si_falta: estimar desde objetivo primario

[06] 📌 DEFINITION_OF_DONE
     criterios: [] | not_in_scope: []
     si_falta: LLM_JUEZ + consenso generan

[07] 🏛️ ARQUITECTURA_CONSTITUCION
     lenguaje / db / runtime / prohibido: []
     si_falta: buscar en ADN_SYSTEM del proyecto

[08] 🔗 DEPENDENCIAS
     fichas_requeridas / servicios / apis_necesarias
     si_falta: Discovery Engine encuentra automático

[09] 🛡️ SEGURIDAD_ADN
     6 checks GUARDIAN_LAYER
     si cualquiera viola: RECHAZAR_SOLICITUD

[10] 💡 ESTRATEGIA_PLANIFICACION
     nivel: L0(directo)|L1(mínima)|L2(estándar)|
            L3(compleja)|L4(estratégica)
     patron: secuencial | DAG | fractal(depth≤5)
     horizon: 24h | 72h | 168h | 720h | infinito
     si_falta: calcular desde DRE

[11] 🧩 CONSENSO_REQUERIDO
     activo si task_level = critical
     quorum: 3/5 agentes mínimo
     si_falta: activar Decision Engine v2

[12] 📂 CONTEXTO_PROYECTO
     state_json_path / crazy_wall_path / knowledge_pack
     seed_analizado: bool
     si_falta: Seed Analysis S1→S5

[13] 🔍 EVIDENCIA_SUFICIENCIA
     score / umbral: 0.85 / max_rondas: 5
     si_falta: Discovery Engine ejecuta ciclos

[14] ⏱️ PRESUPUESTO_RECURSOS
     max_tokens / max_runtime_h
     dsl_pct: 90% | llm_pct: 10%
     si_falta: estimar desde DRE + volumen

[15] 📋 FORMATO_SALIDA
     tipo: json|md|artifact|report|multi
     firmado: true | provenance_chain: true
     si_falta: usar nct.result.v1.json

[16] 🔄 MODO_RECOVERY
     checkpoint_disponible / ultimo_state_valido
     max_reintentos: 3 | nivel_recovery: 1-5
     si_falta: AUTO-RECOVERY ENGINE evalúa

[17] 🧬 FICHA_IDENTIDAD
     id: uuid | tipo: ficha_g2|ficha_code|modulo|sistema
     version / historial_cambios: [] / failure_registry: []
     si_falta: generar nuevo uuid + historial vacío

[18] ⚠️ PENDIENTES_PREVIOS
     lista / push_ping_anterior
     si_falta: consultar crazy_wall + state.json

[19] 🔒 GOAL_LOCK
     congelado por: LLM_JUEZ
     timestamp_congelacion / firmado_por
     REGLA: absolutamente nada avanza sin GOAL_LOCK activo
     si_falta: LLM_JUEZ congela PRIMERO

[20] 🆕 SKILLS_REQUERIDAS
     cantidad: 3-10 por tarea | descargadas: bool
     si_falta: Skill Manager descarga automático

[21] 🤝 AGENTE_ASIGNADO
     tipo: PLAN_AGENT|TEAM_AGENT|EXECUTOR|MICRO_AGENT
     manifest_verificado / capability_json_leido
     si_falta: Role Engine asigna según TM + DRE

[22] 🌐 INVESTIGACION_PREVIA
     rag_interno / web_search / github_search: bool
     si score < 0.85: MA-RESEARCH-WEB + MA-RESEARCH-GH

[23] 📈 METRICAS_CICLO_ANTERIOR
     score_calidad / score_eficiencia / score_precision
     mejora_vs_anterior
     si_falta: Self Improvement usa 0 como baseline

[24] 🚨 VALIDACIONES_JUEZ
     existe / completo / especifico / sin_mock
     sin_hallucination_api / evidence_report_required
     si_falta: LLM_JUEZ RECHAZA hasta completar

[25] 📦 BATCH_CONFIG
     batch_size: 20 | overlap: 5
     priority_queue: critical > normal > background
     FIFO dentro de cada prioridad

[26] 🧠 HIPOTESIS_INICIALES
     mínimo 3 hipótesis antes de ejecutar cualquier cosa
     generadas en Recurrent Reasoning Loop
     evaluadas por Critic Swarm antes de seleccionar

[27] 🔁 REPLANIFICACION_TRIGGER
     condición: >3 goal objectives fallan
     acción: nuevo Discovery + Consenso completo

[28] 📡 PATRON_COMUNICACION
     secuencial | DAG_paralelo | fractal_anidado(depth≤5)
     selección automática según DRE score

[29] 💾 MEMORIA_CONFIG
     tier_activo: 0-3 | dream_activo / distill_activo
     TTL_cache por task_type

[30] 🏁 ESTADO_FASE0
     puede_avanzar = true SOLO si:
       todos los requeridos tienen valor
       O tienen estrategia si_falta ejecutada y confirmada
     SIMULACION: plan simulado 5 veces antes de ejecutar
                 detecta colisiones de estado, corrige, ejecuta
     ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 2 — PLANIFICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[2] GOAL ENGINE (25 items) │ ▼ 🛂 Control │ ▼

[3] GOAL QUEUE ENGINE │ ▼
    └── Segmenta 1-1000 tareas en batches de 20 + overlap 5
        Priority queue: critical > normal > background

[4] SCHEMA ENGINE │ ▼ 🛂 Control │ ▼

[5] LIFECYCLE ENGINE │ ▼

[6] SESSION MANAGER │ ▼

[7] CONTEXT LOADER │ ▼ 🛂 Control │ 🔍 Revisión │ ▼

[7.1] MYTHOS COGNITIVE LAYER / ADVANCED REASONING │ ▼
    ├── GOAL LOCK
    │   ├── Goal Principal (qué se busca)
    │   ├── Goals Secundarios (qué más cumplir)
    │   ├── Criterio de Éxito (cuándo está bien)
    │   ├── Criterio de Fallo (cuándo está roto)
    │   ├── Restricciones innegociables
    │   ├── Alcance (qué entra y qué NO)
    │   ├── Vecinos (de quién recibe, a quién entrega)
    │   ├── Riesgo Principal (qué puede salir mal)
    │   ├── Resultado Esperado (forma de la salida)
    │   └── Fuente de Verdad (contra qué validar)
    ├── PRELUDE
    │   ├── Intent Parsing (intención real vs literal)
    │   ├── Problem Framing (reformular solucionable)
    │   ├── Domain Detection (CODE|ARCH|RESEARCH|DESIGN|AUTO)
    │   ├── Context Building (recopilar info relevante)
    │   ├── Constraint Extraction (explícitas + implícitas)
    │   └── Goal Decomposition (sub-objetivos atómicos)
    ├── DRE COMPLEXITY ESTIMATOR
    │   ├── fórmula: (deps×2)+steps+(5 ambiguo)+(5 riesgo)
    │   ├── LOW(0-3) → 9 pasos / 2 loop iters
    │   ├── MEDIUM(4-8) → 16 pasos / 5 loop iters
    │   ├── HIGH(9-15) → 25 pasos / 10 loop iters
    │   └── EXTREME(16+) → 30-50 pasos / 20+ loop iters
    ├── MAX MODE (solo decisiones críticas)
    │   ├── K muestras paralelas por decisión
    │   ├── Majority voting entre muestras
    │   └── Best-of-N self-verification
    ├── RECURRENT REASONING LOOP
    │   ├── Planner (estrategia de resolución)
    │   ├── Hypothesis Generation (mín 3 hipótesis)
    │   ├── Alternative Paths (Plan B, C antes de ejecutar)
    │   ├── Search Expansion (más allá de lo obvio)
    │   ├── Reasoning Swarm (paralelo: técnico/usuario/seguridad)
    │   ├── Critic Swarm (multi-perspectiva adversarial)
    │   ├── Self Reflection (¿resuelvo el problema correcto?)
    │   ├── Failure Analysis (modos de fallo conocidos+desconocidos)
    │   ├── Simulation Engine (normal + edge + extremo)
    │   ├── Edge Case Generation (inputs vacíos/nulos/extremos)
    │   ├── Validation Layer (vs criterios de GOAL_DECOMPOSITION)
    │   ├── Knowledge Retrieval (RAG + docs + patrones)
    │   ├── Insight Extraction (qué aprendimos nuevo)
    │   ├── Replanner Loop (si falla → replantear completo)
    │   ├── Optimization Pass (calidad y robustez)
    │   ├── Decision Fusion (combinar perspectivas)
    │   ├── Confidence Scoring (0-100, umbral mín 70)
    │   ├── Solution Ranking (tabla comparativa objetiva)
    │   ├── Ensemble Fusion (combinar mejores elementos)
    │   └── Safety / Consistency Check (violaciones restricciones)
    ├── GOAL-STOP CHECK (fase P9.5)
    │   ├── ¿El objetivo principal fue alcanzado?
    │   ├── Evidence Sufficiency Score ≥ 0.85 → stop
    │   └── Score < 0.85 → nueva ronda investigación
    ├── CODA
    │   ├── Final Synthesis (solución completa lista)
    │   ├── Output Generation (formato correcto, completo)
    │   ├── Post Output Audit (cumple exactamente lo pedido?)
    │   └── Feedback Loop Storage (mejorar próximo ciclo)
    └── CHEF FINAL
        ├── Lista Total (3 pasadas, reconstruye TODO)
        ├── Arrastre + Actualización (3 pasadas, memoria acumulada)
        ├── Diseño de Entrega (3 pasadas, formato presentación)
        └── Síntesis Final (análisis global, versión optimizada)

[7.2] TOKEN BUDGET MANAGER │ ▼
    ├── Presupuesto: DSL 90% código / LLM 10%
    ├── Alerta amarilla 70% → Writer Subagent se activa
    ├── Alerta roja 85% → checkpoint + reinicio contexto LLM
    └── Crítico 95% → HALT inmediato + Recovery Engine

[7.3] DISCOVERY ENGINE │ ▼
    ├── Obligatorio antes de cualquier ejecución
    ├── Ciclos investigación (mín 2 / máx 5 rondas):
    │   ├── R1: query generada
    │   ├── R2: fetch de fuentes (web/GitHub/RAG/arxiv)
    │   ├── R3: filtrado de relevancia
    │   ├── R4: evaluación score (≥ 0.85 → stop)
    │   └── R5: refine → genera nueva query
    ├── Hipótesis generadas: estándar/extrema/inversa/híbrida/emergente
    ├── Loop: sin novedad → expandir / novedad → escalar
    └── Output: knowledge_pack + PROCEED|BLOCK|NEEDS_MORE_INFO

[7.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 2
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 3 — RAZONAMIENTO / CONSENSO / ORQUESTACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[8] PLANNER │ ▼

[8.1] DECISION ENGINE v2 / CONSENSUS SYSTEM │ ▼ 🛂
    ├── Pipeline formal 6 etapas:
    │   DAG → State Machine → Micro-Agents →
    │   Contracts → Validators → Artifacts
    ├── Research Layer (OBLIGATORIO antes de decidir):
    │   ├── RAG interno del proyecto
    │   ├── Web search (Wikipedia/OWASP/docs oficiales)
    │   ├── GitHub search (patrones/awesome lists)
    │   └── Perplexity + arxiv (papers técnicos)
    ├── 5 Agentes de Consenso (paralelos, timeout 90s):
    │   ├── CREATIVE_AGENT   temp:0.9 → 5-10 ideas sin filtro
    │   │   output: [{nombre, descripcion, por_que, riesgo}]
    │   ├── INNOVATION_AGENT temp:0.7 → mejora cada idea
    │   │   output: [{evolucionada, variantes, pros, contras, score}]
    │   ├── CRITIC_AGENT     temp:0.3 → adversarial, destruye débiles
    │   │   output: [{debiles:3, riesgos:2, score, keep|iterate|kill}]
    │   ├── SELECTION_AGENT  temp:0.2 → elige ganadora (score ≥ 0.6)
    │   │   output: {ganadora, runner_up, justificacion, score_final}
    │   └── ARCHITECTURE_AGENT temp:0.3 → plano ejecutable
    │       output: {stack, fichas_dsl, talleres, esfuerzo, riesgos, primer_paso}
    ├── DEVIL AGENT (adversarial obligatorio post-selección)
    │   └── Ataca la ganadora antes de aprobar definitivamente
    ├── Quorum: mín 3/5 responden → OK parcial
    │           < 3 responden → ALERTA → escala Director
    ├── Score ganadora < 0.6 → escala Director
    ├── Anti-groupthink: todos proponen igual →
    │   Creative re-genera con temperatura más alta
    ├── Prompt DSL cerrado y sellado (parseable, auditable)
    ├── Artifacts inmutables firmados con provenance chain
    ├── Toda decisión logueada en nct_consensus (Xata/Redis)
    ├── V1: Director Loop (validación humana obligatoria)
    └── V2: Auto-aprobación con confidence gates

[8.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 3
    ├── SENTINEL: detecta groupthink temprano
    ├── JUDGE: score ganadora ≥ 0.6 antes de aprobar
    └── SHERIFF: bloquea pipeline si no hay quorum suficiente

[9] WORKFLOW / PIPELINE │ ▼

[9.1] SKILL MANAGER │ ▼
    ├── Descarga 3-10 skills específicas por tarea
    ├── Lee capability.json → selecciona proveedor + fallback
    ├── Patrones soportados:
    │   ├── Secuencial: A→B→C→D
    │   ├── DAG paralelo: grupos con dependencias
    │   └── Fractal anidado: depth máximo 5 niveles
    └── Cambiar agente = editar 1 línea capability.json

[9.2] MICRO-AGENT DISPATCHER │ ▼
    ├── MA-CODE-GEN     → genera código desde spec.md+stack.json
    ├── MA-CODE-LINT    → lint + format + type-check → report.json
    ├── MA-CODE-TEST    → unit+integration+mutation → junit.xml+coverage
    ├── MA-RAG-SEARCH   → búsqueda vectorial+rerank → chunks.json
    ├── MA-RAG-SYNTH    → sintetiza respuesta con citas → answer.md
    ├── MA-DOC-WRITE    → documenta arquitectura → doc.md
    ├── MA-ARCH-PLAN    → planifica arquitectura → arch.yaml
    ├── MA-VERIFY-3CAP  → verificación adversarial 3 capas → verdict.json
    │   ├── CAP1: adversarial_check (código determinista)
    │   ├── CAP2: cross_check (código determinista)
    │   ├── CAP3: maker_checker (código determinista)
    │   └── CAP4_LLM: solo si CAP1-3 detectan issues
    ├── MA-REPAIR-5STEP → pipeline 5 pasos reparación → repaired.json
    ├── MA-RESEARCH-WEB → crawling+extracción → pages.jsonl
    ├── MA-RESEARCH-GH  → búsqueda GitHub API → repos.json
    └── MA-EMIT-REPORT  → empaqueta resultado → report.md+manifest.json
    REGLA: spawn→run→emit JSON→die (≤200 LOC núcleo c/u)

[9.3] AGENT MANIFEST READER │ ▼
    ├── Lee EXCLUSIVAMENTE manifest.json de cada agente
    ├── Kernel NUNCA inspecciona código del agente
    └── Schema: {name, version, capabilities, skills_supported,
                 models_compatible, provider, dependencies, priority}

[10] GRAPH RUNTIME (DAG) │ ▼

[11] DEPENDENCY RESOLVER │ ▼ 🛂 │ ▼

[12] ROLE ENGINE │ ▼

[13] PROTOCOL ENGINE │ ▼

[14] CONVERSATION ENGINE │ ▼

[15] DECISION ENGINE │ ▼ 🛂 │ ▼

[16] POLICY ENGINE │ ▼

[17] HANDOFF ENGINE │ ▼

[17.1] HANDOFF PACKAGE BUILDER │ ▼
    ├── agente_origen: string
    ├── agente_destino: string
    ├── tarea_id: uuid
    ├── resultado_parcial: dict
    ├── estado: DONE | PARTIAL | FAILED
    ├── contexto_transferido: dict
    ├── lo_que_sigue: string
    ├── lo_que_no_completo: list
    ├── timestamp: ISO-8601
    └── hash_integridad: SHA256

[18] CAPABILITY REGISTRY │ ▼
    └── → connections.yaml sección BACKENDS

[19] EVENT BUS │ ▼

[19.1] DEAD LETTER QUEUE │ ▼
    ├── Captura mensajes/tareas que fallaron N veces
    ├── Registra en dead_letter.json con causa raíz
    └── Notifica al orquestador para decisión humana

[20] TOOL ROUTER │ ▼
    └── → connections.yaml → API ROUTER (EX1)

[21] ENVIRONMENT MANAGER │ ▼ 🛂 │ ▼

[22] LLM │ ▼ 🛂 │ ▼
    └── → connections.yaml → API ROUTER → PROVIDER_X
        (el agente nunca sabe qué provider respondió)

[23] SUBAGENT MANAGER │ ▼
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 4 — EJECUCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[J] LLM_JUEZ (overlay activo sobre toda Capa 4 y Capa 6)
    ├── GOAL_LOCK: congela objetivo antes de cualquier ejecución
    ├── El ESCRITOR no avanza un paso sin APPROVED del JUEZ
    ├── Solo el JUEZ emite APPROVED o REJECTED (nadie más)
    ├── Detecta: mock/fake/dummy/placeholder/hardcoded/pass_vacío
    ├── Detecta: APIs/métodos/imports/librerías inexistentes
    ├── Detecta: texto vago, genérico, copiado, no relacionado
    ├── Verifica: TODOS los campos requeridos del schema
    ├── Verifica: coherencia entre pasos (P01 vs P05)
    ├── FAILURE_REGISTRY: causa raíz de cada rechazo
    └── Actualiza crazy_wall tras cada paso completado/fallido

[24] EXECUTOR │ ▼ 🛂 │ ▼

[24.1] CAPA_7 — INTEGRACIÓN / TRANSFERENCIA │ ▼
    ├── Conecta CAPA_6 (Calidad) con CAPA_8 (Memoria)
    ├── Serializa resultado validado para persistencia
    └── Notifica a Memory Engine: nuevo artefacto disponible

[24.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 4

[25] EXECUTION STATE MANAGER │ ▼ 🔍 Revisión │ ▼


26] ARTIFACT ENGINE │ ▼ 🛂 │ 🔍 │ ▼
    ├── Event Sourcing puro (cada cambio = evento inmutable)
    ├── Estructura evento: {event_id, actor:human|agent|system,
    │   timestamp, intent, before_fp, after_fp,
    │   evidence_refs, policy_decision:allowed|blocked|escalated}
    ├── Hash chain: event[i].prev_hash = sha256(event[i-1])
    ├── Artifacts con provenance chain completa y firmados
    └── Fingerprint multicapa L1-L5 por artifact
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 5 — MEMORIA PROGRESIVA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[27] MEMORY │ ▼ 🛂 │ 🔍 │
    ├── MEMORIA 4 TIERS:
    │   ├── Tier 0: RAW (efímero, input sin procesar)
    │   ├── Tier 1: SESSION (contexto sesión actual)
    │   ├── Tier 2: STRATEGIC (decisiones + arquitectura acumulada)
    │   └── Tier 3: PROJECT (memoria permanente entre sesiones)
    ├── EVENT SOURCING PURO (no historial, sino eventos):
    │   ├── Hash chain SHA256: event[i].prev = sha256(event[i-1])
    │   ├── Verificación periódica de integridad de la cadena
    │   └── Time-travel + rollback granular a cualquier punto
    ├── KNOWLEDGE GRAPH LATERAL:
    │   ├── Aristas: version_de / contradice / refina
    │   ├── Aristas: depende_de / cita_a / autoridad_sobre
    │   ├── Detección contradicciones: O(grado) no O(n²)
    │   └── Escala a miles de fichas sin degradación
    ├── WRITER SUBAGENT (activa cuando contexto > 70%):
    │   ├── Compacta el contexto activo
    │   └── Escribe resumen estructurado a Tier 1/2 sin pérdida
    ├── CHECKPOINT / REBUILD ENGINE:
    │   ├── Snapshot firmado cada N turnos (configurable)
    │   ├── Persiste en state.jsonl
    │   └── replay_to_checkpoint(t) para recovery exacto
    ├── DREAM LOOP (cron semanal):
    │   ├── Consolida memoria de sesiones pasadas
    │   └── Escribe a Tier 3 PROJECT → memory/dream.md
    ├── DISTILL LOOP (cron diario):
    │   ├── Destila lecciones aprendidas
    │   └── Elimina duplicados, enriquece Tier 2 STRATEGIC
    ├── Timeline Memory (secuencia temporal de eventos)
    ├── Chain Memory (cadena de decisiones relacionadas)
    └── Event/Ping Memory (señales del sistema)

[27.1] MASTER JSON / STATE ENGINE │ ▼ 🔍 │
    ├── state.json → fuente única de verdad del sistema
    ├── crazy_wall → mapa vivo del workflow actual
    ├── Hash chain SHA256 anti-corrupción
    └── Atomic write (previene corrupción en escritura concurrente)

[27.S] 🛂 SENTINEL/JUDGE/SHERIFF — CAPA 5
    └── Verifica hash chain en CADA lectura de memoria
    ▼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPA 6 — CALIDAD / VALIDACIÓN / RECUPERACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[28] CONTEXT MANAGER │ ▼ 🛂 │ 🔍 │ ▼

[29] VALIDATOR │ ▼

[30] SELF CHECK │ ▼ 🛂 │ ▼

[30.1] AUDIT LOGGER / CHAIN OF CUSTODY │ ▼
    ├── CHAIN_OF_CUSTODY_LOG (quién hizo qué y cuándo)
    ├── FAULT_LOG (fallos con causa raíz)
    ├── EVENT_LOG (eventos del sistema)
    ├── ROUTER_LOG (decisiones de routing)
    └── CHANGE_LOG (cambios de estado y reglas)

[30.2] RECOVERY ENGINE │ ▼ 🛂 │
    ├── Nivel 1: RETRY → reintentar operación fallida (1 vez)
    ├── Nivel 2: ROLLBACK → revertir al último estado estable
    ├── Nivel 3: CHECKPOINT → replay_to_checkpoint(t)
    ├── Nivel 4: REPLAN → replantear el plan desde el fallo
    └── Nivel 5: ESCALATE → Director, el sistema no puede solo

[30.3] SELF IMPROVEMENT LOOP │ ▼
    ├── Mide por ciclo: score_calidad + score_eficiencia + score_precision
    ├── MEJORA (nuevo > anterior) → conservar reglas actuales
    ├── REGRESIÓN (nuevo < anterior) → rollback de reglas + análisis
    └── ESTANCAMIENTO (igual N veces) → mutar estrategia o modelo

[30.4] OUTPUT CONNECTOR │ ▼
    └── → connections.yaml (OUTPUT_CONNECTORS)
        Kanboard / Obsidian / Graphiti / GitHub

[31] OUTPUT FINAL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTAS PIE DIAGRAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛂 activa módulos: Sheriff · Sentinel · Judge ·
   Supervisor · Validator · Auditor · Policy Engine ·
   Memory Verifier · Goal Verifier · Security Checker ·
   Consistency Checker · Recovery Manager

🔍 puntos de re-análisis contexto/memoria (7 puntos):
   [1] Input · [7] Context Loader · [25] Exec State ·
   [26] Artifact Engine · [27] Memory ·
   [27.1] Master JSON · [28] Context Manager
   REGLA: sistema de memoria se repite en cada parte del proceso


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — NOTAS DEL ORQUESTADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTA_01 — PARADIGMA CENTRAL
El orquestador piensa, coordina y decide.
NUNCA ejecuta código. NUNCA toca repositorios.
NUNCA genera implementaciones directas.
Todo lo que hace es: planificar → asignar → supervisar → verificar.

NOTA_02 — SEPARACIÓN PENSAMIENTO/CONTROL
MYTHOS/FABLES = pensamiento (cómo razona)
FSM/Router/PydanticAI = control (qué ejecuta)
Son capas DIFERENTES que trabajan juntas sin mezclarse.
El pensamiento alimenta al control, nunca al revés.

NOTA_03 — LLM_JUEZ es el único que dice APPROVED
Ningún agente puede auto-aprobar su propio trabajo.
Builder ≠ Validator ≠ Witness (tres roles distintos siempre).
Sin GOAL_LOCK activo: pipeline bloqueado sin excepción.

NOTA_04 — ADN_SYSTEM es inmutable
Solo el Director humano puede modificar el ADN.
Ningún proceso automático puede tocar las 6 leyes fundamentales.
Cualquier intento de modificación → RECHAZAR_SOLICITUD.

NOTA_05 — EVIDENCIA OBSERVABLE siempre
Antes de cerrar cualquier tarea: verificar resultado observable.
No valen: planes bonitos, documentos bonitos, intenciones.
Solo valen: cuenta creada, repo commit, endpoint responde,
            test pasa, artifact existe en disco.

NOTA_06 — CAPA_7 pendiente de decisión Director
El sistema salta de CAPA_6 (Calidad) a CAPA_8 (Memoria).
CAPA_7 fue propuesta como INTEGRACIÓN/TRANSFERENCIA.
Requiere aprobación explícita del Director antes de implementar.

NOTA_07 — SENTINEL_SECURITY (vigilancia permanente)
Monitorea en paralelo: código, workflows, tools, artifacts,
agentes, memoria, contenedores, APIs, usuarios.
Busca: anomalías, comportamientos sospechosos, degradación.
Salidas: INCIDENTE_DETECTADO | ALERTA_SEGURIDAD |
         VULNERABILIDAD_ENCONTRADA | OPORTUNIDAD_MEJORA.

NOTA_08 — SISTEMA DE FICHAS (unidades atómicas)
Tipos: ARTIFACT | TOOL | CODE | WORKFLOW |
       DSL | RESEARCH | EVOLUTION | SECURITY
Cada ficha: id:uuid, tipo, version, autor, dependencias,
            reglas, historial, metricas, artifact, code, tools.

NOTA_09 — JERARQUÍA DE CONTROL
NIVEL 0: Director (humano, autoridad final)
NIVEL 1: Orquestador (cerebro operativo externo)
NIVEL 2: Consejo de Consenso (5 asesores especializados)
NIVEL 3: Auditores (3 capas independientes de validación)
NIVEL 4: Ejecutores (workers intercambiables en Antigravity)

NOTA_10 — CONNECTIONS.YAML (archivo de conexiones)
Todos los providers viven aquí, no en el código.
Secciones: INPUT_CHANNELS / LLM_PROVIDERS / BACKENDS /
           HF_SPACES_FLEET / TOOL_ROUTER /
           OUTPUT_CONNECTORS / MONITOR
Cambiar provider = editar este archivo, no tocar código.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 3 — TEAM AGENT / DIAGRAMA COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[AG1.01] OBJETIVO Y FUNCIÓN
Coordina un enjambre de micro-agentes especializados
para tareas complejas que ningún agente único puede resolver.
Existe porque las tareas reales requieren paralelismo,
especialización simultánea y síntesis coordinada de resultados.
Casos de uso: arquitectura multi-módulo, investigación profunda,
validación adversarial compleja, refactoring masivo 72h+.

[AG1.02] ANÁLISIS Y CONSENSO PREVIO
Antes de asignar cualquier tarea el Team Agent ejecuta
el Decision Engine v2 completo:
5 agentes votan qué micro-agentes activar, en qué orden,
con qué patrón (secuencial|DAG|fractal) y con qué presupuesto.
Sin consenso → CONSENSUS_BLOCKED → escala al Orquestador.

[AG1.03] GOALS (mínimo 7 justificados)
G1: Descomponer tareas complejas en unidades atómicas verificables
G2: Asignar cada unidad al micro-agente más adecuado por capability
G3: Coordinar ejecución paralela sin colisiones de estado compartido
G4: Sintetizar resultados parciales en output coherente y firmado
G5: Detectar y recuperar micro-agentes fallidos sin detener el swarm
G6: Garantizar que ninguna unidad del DAG quede sin ejecutar
G7: Mantener contexto compartido íntegro entre todos los agentes

[AG1.04] INVESTIGACIÓN WEB PREVIA
Antes de planificar ejecuta 2-5 rondas de investigación:
Fuentes: patrones de orquestación / benchmarks multi-agent /
         papers de swarm coordination / repos de referencia
Umbral de suficiencia: evidence_score ≥ 0.85 antes de avanzar.

[AG1.05] PLANIFICACIÓN
Descarga 3-10 skills según el tipo de tarea detectado.
Genera el task graph (DAG) completo con todas las dependencias.
Estima: tokens / tiempo / costo antes de comprometer recursos.
Valida: no hay ciclos en el DAG, no hay dependencias imposibles.

[AG1.06] ORGANIZACIÓN DE TAREAS
Agrupa micro-agentes por parallel_group (g1, g2...gN).
Cada grupo puede ejecutar en paralelo internamente.
Los grupos tienen orden de dependencia entre sí (DAG de grupos).
Priority queue: critical > normal > background dentro de cada grupo.

[AG1.07] DIVISIÓN DE TAREAS
Cada tarea → un solo micro-agente con responsabilidad única.
Regla: ≤200 LOC de núcleo por micro-agente.
Cada micro-agente tiene: input_schema + output_schema cerrados.
Estado del micro-agente: efímero (spawn→run→emit→die).

[AG1.08] TRABAJA EN ENJAMBRE
spawn() → todos los micro-agentes del grupo activo en paralelo.
async gather() → espera resultados del grupo completo.
Agente muerto/timeout → spawn() del agente de respaldo.
Resultado parcial de agente → MA-REPAIR-5STEP automático.

[AG1.09] PASOS A EJECUTAR (10 pasos)
PASO 01: Discovery de la tarea (Seed Analysis S1→S5)
PASO 02: Consenso del plan (Decision Engine v2, 5 agentes)
PASO 03: Generación del DAG de micro-agentes con dependencias
PASO 04: Validación del DAG (sin ciclos, dependencias factibles)
PASO 05: spawn() del primer parallel_group
PASO 06: async gather() + validación de resultados del grupo
PASO 07: spawn() del siguiente grupo con resultados previos como input
PASO 08: Síntesis final (MA-EMIT-REPORT)
PASO 09: Verificación 3 capas (MA-VERIFY-3CAPAS)
PASO 10: Checkpoint + output firmado al Orquestador principal

[AG1.10] REVISIÓN DE CONTEXTO
Antes de cada parallel_group: verificar state.json integridad.
Si hash chain falla → Recovery Engine nivel 3 (checkpoint).
🔍 activo en cada transición entre grupos del DAG.
Token Budget: si >70% → Writer Subagent compacta antes de continuar.

[AG1.11] REPLANIFICACIÓN DE OBJETIVOS
Si un grupo falla 3 veces → re-ejecutar el Planner completo.
Nuevas hipótesis generadas por Recurrent Reasoning Loop.
Discovery adicional si evidence_score < 0.85 en el nuevo plan.

[AG1.12] CONSENSO REPLANIFICACIÓN — 10 PASOS
P01: Presentar el fallo al Decision Engine v2 con contexto completo
P02: Research Layer busca alternativas (RAG + web + GitHub)
P03: Creative Agent genera nuevas estrategias sin filtro
P04: Innovation Agent mejora cada estrategia a su mejor versión
P05: Critic Agent las ataca adversarialmente
P06: Devil Agent destruye la candidata más fuerte
P07: Selection Agent elige la superviviente (score ≥ 0.6)
P08: Architecture Agent convierte en plan ejecutable concreto
P09: Validator verifica el nuevo plan contra restricciones
P10: Director Loop aprueba (V1) o Auto-gate pasa (V2)

[AG1.13] LOOPS ACTIVOS
decision_loop: cada turno de coordinación del Team Agent
worker_loop: monitoreo continuo de micro-agentes activos
validation_loop: verificación continua de outputs recibidos
memory_loop: escritura periódica a los 4 tiers de memoria
health_loop: detección de agentes caídos o sin respuesta

[AG1.14] BUCLE PRINCIPAL

[AG1.15] VALIDACIÓN (3 capas obligatorias)
MA-VERIFY-3CAPAS en cada output de micro-agente:
CAP1: adversarial_check (código determinista 90%)
CAP2: cross_check (código determinista 90%)
CAP3: maker_checker (código determinista 90%)
CAP4_LLM: solo si CAP1-3 detectan issues (LLM 10%)
Resultado: {decision:pass|fail, issues:[], evidence:{c1,c2,c3}}

[AG1.16] HIPÓTESIS
Hypothesis Engine genera N hipótesis de solución al inicio.
Team Agent asigna cada hipótesis a micro-agentes en paralelo.
La que produce mejor score en validación gana.
Mínimo 3 hipótesis antes de seleccionar estrategia.

[AG1.17] REFUTACIONES
Devil Agent ataca cada hipótesis superviviente del Critic.
Si el score de una hipótesis cae por debajo de 0.6 → eliminada.
Solo pasan hipótesis que sobreviven ataque adversarial completo.
Sin hipótesis superviviente → nuevo ciclo de Discovery.

[AG1.18] REPLANIFICACIÓN + CONSENSO LLM (14.1)
Si todas las hipótesis mueren → nuevo ciclo de Discovery completo.
Evidence sufficiency mide si hay info suficiente para replantear.
Si score < 0.85 → más rondas de investigación antes de replantear.
Evaluación final con LLM temperature:0.0 (máximo determinismo).
Los 10 pasos de consenso se repiten con el nuevo contexto.

[AG1.19] 12 PREGUNTAS DE OBJETIVOS (verificación)
Q01: ¿El output cumple el goal primario exactamente como se definió?
Q02: ¿Los goals secundarios (G1-G7) están satisfechos?
Q03: ¿El resultado es verificable con evidencia observable?
Q04: ¿Algún micro-agente produjo output sin verificación de 3 capas?
Q05: ¿El hash chain de memoria está intacto en todos los tiers?
Q06: ¿El DAG se completó sin pasos saltados ni dependencias rotas?
Q07: ¿El score de la solución ganadora es ≥ 0.6?
Q08: ¿El Evidence Sufficiency Score fue ≥ 0.85 antes de ejecutar?
Q09: ¿El Devil Agent ejecutó su refutación completa?
Q10: ¿El artifact tiene provenance chain completa y firmada?
Q11: ¿El checkpoint fue guardado correctamente en state.jsonl?
Q12: ¿El Director aprobó (V1) o el auto-gate pasó (V2)?

[AG1.20] CAMBIO DE ESTRATEGIA
Si > 3 preguntas de objetivos responden NO:
→ Cambiar patrón: Secuencial → DAG → Fractal anidado
→ Cambiar modelos en capability.json (sin tocar código)
→ Aumentar max_rounds del consenso (+2 rondas)
→ Reducir batch_size (mayor control, menor paralelismo)

[AG1.21] NUEVO LOOP
Después del cambio de estrategia:
Reiniciar el bucle principal desde el último checkpoint válido.
No desde el inicio: replay_to_checkpoint(t) exacto.
Actualizar state.json con nueva estrategia y nuevo plan.

[AG1.22] MEMORIA CONTINUA
Cada ciclo escribe a los 4 tiers de memoria.
Tier 0: inputs crudos del ciclo actual (efímero)
Tier 1: contexto activo de la sesión
Tier 2: decisiones estratégicas del ciclo
Tier 3: resultado final + lecciones permanentes
Writer Subagent: compacta cuando >70% del contexto ocupado.
Distill diario + Dream semanal mantienen Tier 2 y Tier 3 limpios.

[AG1.23] CLASIFICACIÓN DE RESULTADOS
Cada output de micro-agente recibe clasificación:
PASS → avanza al siguiente paso del DAG
FAIL → activa MA-REPAIR-5STEP automáticamente
PARTIAL → transformar antes de continuar (ver 19.1)
ESCALATE → Decision Engine v2 evalúa qué hacer
SKIP → el paso puede saltarse (definido en dependency graph)

[AG1.24] TRANSFORMACIÓN DE RESULTADOS PARCIALES (19.1)
Los outputs PARTIAL pasan por transformación antes de continuar:
1. Extraer lo válido del resultado parcial
2. Documentar qué parte faltó y por qué
3. Actualizar el contexto del siguiente agente con lo extraído
4. Marcar en el DAG que el paso fue completado parcialmente
5. Continuar con advertencia en el state.json

[AG1.25] FORMATO DE SALIDA ESTRUCTURADA
{
  "team_id": "uuid",
  "tarea_id": "uuid",
  "timestamp_inicio": "ISO-8601",
  "timestamp_fin": "ISO-8601",
  "resultado": {...},
  "score_final": float (0-1),
  "artifacts": [{id, tipo, hash, ruta}],
  "provenance_chain": [{evento, actor, timestamp, hash}],
  "checkpoint_ref": "sha256_del_checkpoint",
  "clasificacion": "PASS|FAIL|PARTIAL|ESCALATE",
  "micro_agentes_usados": [{id, rol, tiempo_s, tokens}],
  "hipotesis_evaluadas": int,
  "consenso_rondas": int,
  "recovery_activado": bool,
  "tiempo_total_s": int,
  "tokens_totales": int
}

[AG1.26] MEMORIA PERSISTENTE (post-ciclo)
Tier 3 PROJECT: resultado guardado indefinidamente
Knowledge Graph: aristas nuevas añadidas al grafo
Corrections DB: si Director itera, se guarda como few-shot
Skills DB: nuevas skills aprendidas disponibles para próximos ciclos
Failure Registry: causa raíz de fallos para evitar repetir

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PLAN AGENT (complementario al TEAM AGENT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[AG2.01] OBJETIVO
Separa el PENSAMIENTO de la EJECUCIÓN.
Diseña, valida y firma el plan ANTES de que cualquier
executor o Team Agent toque una sola línea de código.
Sin Plan Agent aprobado: ningún executor puede iniciar.

[AG2.02] GOALS
G1: Diseñar el DAG completo con todas las dependencias antes de ejecutar
G2: Validar que el plan es técnicamente factible con los recursos disponibles
G3: Detectar dependencias circulares antes de cualquier spawn
G4: Estimar tokens/tiempo/costo antes de comprometer presupuesto
G5: Producir execution_package validado por auditores y listo para usar

[AG2.03] FLUJO
Input task → Research (3-10 skills descargadas) → Plan draft
→ Feasibility check (¿es implementable con lo que tenemos?)
→ Consensus v2 (5 agentes validan el plan)
→ Auditor_1 + Auditor_2 verifican
→ execution_package firmado por Architecture Agent
→ GOAL_LOCK activado por LLM_JUEZ
→ Handoff al Team Agent o Executor

[AG2.04] FORMATO DE SALIDA
{
  "plan_id": "uuid",
  "dag": {nodes:[], edges:[], critical_path:[]},
  "estimacion": {tokens_total:int, tiempo_h:float, costo_usd:float},
  "riesgos": [{componente, modo, probabilidad, impacto, mitigacion}],
  "dependencias": [{id, tipo, obligatorio:bool}],
  "execution_package": {pasos:[], agentes:[], skills:[]},
  "firmado_por": "ARCHITECTURE_AGENT",
  "aprobado_por": "DIRECTOR|AUTO_GATE",
  "goal_lock_activo": true,
  "timestamp_aprobacion": "ISO-8601"
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 4 — NOTAS DEL AGENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTA_A01 — DIFERENCIA TEAM vs PLAN AGENT
PLAN AGENT: piensa y diseña el plan (antes de ejecutar)
TEAM AGENT: coordina la ejecución del plan aprobado
Sin PLAN AGENT aprobado → TEAM AGENT no inicia.
Son complementarios, no intercambiables.

NOTA_A02 — AGENTES SON PROCESOS REALES
No son LLMs simulando roles. Son procesos Python en Antigravity.
El LLM es una herramienta que usa el proceso, no el proceso mismo.
Comunicación entre agentes: JSON sobre HTTP o Message Queue.
El orquestador llama a cada proceso por su endpoint real.

NOTA_A03 — MICRO-AGENTES SON DESECHABLES
Cada micro-agente nace, ejecuta su única tarea y muere.
Estado efímero: no guarda nada entre ejecuciones.
Toda la persistencia va al state.json y a la memoria por tiers.
La reutilización viene del Knowledge Graph, no del agente mismo.

NOTA_A04 — SWARM SIZING
Tareas simples (DRE LOW): 1-3 micro-agentes en secuencia
Tareas medias (DRE MEDIUM): 4-8 agentes en DAG paralelo
Tareas complejas (DRE HIGH): 8-15 agentes en DAG+fractal
Tareas extremas (DRE EXTREME): 15-50 agentes, horizon 24h-72h+

NOTA_A05 — RECOVERY DE AGENTES CAÍDOS
Detección: health_loop cada 30s detecta agente sin respuesta
Timeout: 5min sin respuesta → agente declarado caído
Acción: spawn() del agente de respaldo con mismo manifest
Context: el nuevo agente recibe el handoff_package del anterior
Límite: max 3 respawns del mismo agente antes de ESCALATE

NOTA_A06 — BUDGET DSL 90/10
90% del trabajo del Team Agent es código determinista:
routing, scheduling, validation, checkpoint, retry, logging.
Solo 10% usa LLM: síntesis de resultados, decisiones creativas,
evaluación adversarial cuando las 3 capas mecánicas fallan.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 5 — API ROUTER / DIAGRAMA COMPLETO
NCT API ROUTER v0.2 — Repositorio independiente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPÓSITO
El Router es el administrador de recursos del sistema.
El Orquestador decide la lógica y la coordinación.
El Router decide con qué modelo y con qué API ejecutar cada tarea.
Ningún agente conoce ninguna API key ni ningún provider.

DIAGRAMA COMPLETO

Orquestador / Team Agent / Micro-Agents / Ejecutores
        │
        │  POST /v1/complete (siempre la misma llamada)
        ▼
┌─────────────────────────────────────────────────────┐
│                 API ROUTER (VPS independiente)       │
│                                                      │
│  [R1] AUTH & API KEY MANAGER                        │
│       ├── Todas las keys cifradas (AES-256)         │
│       ├── Rotación automática de keys               │
│       ├── BYOK (bring your own key) soportado       │
│       └── Ningún agente ve ninguna key jamás        │
│       ▼                                             │
│  [R2] MODEL SELECTOR (el cerebro del Router)        │
│       ├── Señales: task_type + budget + latency_sla │
│       ├── Señales: capability + provider_health     │
│       ├── Señales: cost_per_token + license         │
│       ├── Reglas en capability.json (sin código)    │
│       └── Si provider saturado → siguiente auto     │
│       ▼                                             │
│  [R3] SCHEDULER + LOAD BALANCER                     │
│       ├── Cola 1-1000 requests simultáneos          │
│       ├── 200+ tareas continuas → batches           │
│       ├── batch_size: 20 configurable               │
│       ├── overlap: 5 (solapamiento entre batches)   │
│       ├── Priority queue: critical>normal>background│
│       └── FIFO estricto dentro de cada prioridad   │
│       ▼                                             │
│  [R4] HEALTH CHECK (cada 30s interno)               │
│       ├── Estado real de cada provider              │
│       ├── Métricas: p95_latencia + error_rate       │
│       ├── Alerta si p95 > SLA definido             │
│       ├── Alerta si costo/hora > threshold          │
│       └── Provider caído → redirige automáticamente │
│       ▼                                             │
│  [R5] RETRY ENGINE                                  │
│       ├── Reintento automático si provider falla    │
│       ├── Backoff exponencial: base 2s, max 5min    │
│       ├── Max 3 reintentos por request              │
│       └── Después de 3 → fallback siguiente provider│
│       ▼                                             │
│  [R6] CIRCUIT BREAKER por provider                  │
│       ├── Umbral: 3 fallos consecutivos → OPEN      │
│       ├── Cooldown: 30s antes de re-intentar        │
│       ├── Half-open: 1 request de prueba            │
│       └── Pass → CLOSE (vuelve a operar normal)    │
│       ▼                                             │
│  [R7] PROVIDER POOL                                 │
│       ├── PROVIDER_A: primary (el más capaz)        │
│       ├── PROVIDER_B: secondary (balance costo)     │
│       ├── PROVIDER_C: especializado código          │
│       ├── PROVIDER_D: fast (tareas simples/rápidas) │
│       └── LOCAL_GGUF: offline (sin internet)        │
│       ▼                                             │
│  [R8] SEMANTIC CACHE                                │
│       ├── Request similar respondido antes → cache  │
│       ├── TTL configurable por task_type            │
│       ├── Cache invalidation por project_hash change│
│       └── Ahorra tokens en requests repetitivos     │
│       ▼                                             │
│  [R9] AUDIT LOGGER                                  │
│       ├── timestamp / provider_usado / tokens       │
│       ├── costo_usd / latencia_ms / request_id      │
│       ├── NUNCA guarda contenido de las llamadas    │
│       └── Solo metadata para auditoría y costos     │
│       ▼                                             │
│  [R10] MONITORING + ALERTS                          │
│        ├── Dashboard: uso por agente y task_type    │
│        ├── Alert: p95 latencia > SLA                │
│        ├── Alert: costo/hora > threshold            │
│        └── Alert: error_rate > 5% en 5 min         │
└─────────────────────────────────────────────────────┘
        │
        ▼
Respuesta al agente (nunca sabe qué provider respondió)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLUJO CON 50 REQUESTS SIMULTÁNEOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
50 requests entran → [R3] Scheduler encola por prioridad
[R2] Model Selector evalúa cada uno
[R4] Health Check: PROVIDER_A ocupado → usa PROVIDER_B
PROVIDER_B también lleno → usa PROVIDER_C
Todos ocupados → cola espera liberación de capacidad
[R6] Circuit Breaker monitorea errores por provider
Para el agente: siempre igual → Router → respuesta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERFACE DE LOS AGENTES (siempre la misma)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUEST:
{
  "task_type": "code_generation|research|analysis|critical_decision|...",
  "priority": "critical|normal|background",
  "budget": "low|medium|high",
  "latency_sla_ms": 5000,
  "messages": [...],
  "max_tokens": 4000,
  "stream": false
}

RESPONSE:
{
  "request_id": "uuid",
  "result": {...},
  "tokens_used": int,
  "latency_ms": int,
  "cache_hit": bool
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGLAS DE SELECCIÓN (capability.json)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
task=code_generation + budget=low      → PROVIDER_C
task=long_horizon + horizon≥24h        → PROVIDER_A
task=research_rag                      → PROVIDER_B
task=critical_decision                 → PROVIDER_A
task=simple+fast                       → PROVIDER_D
task=offline                           → LOCAL_GGUF
provider_A.health=down                 → PROVIDER_B auto
provider_B.health=down                 → PROVIDER_C auto
costo/hora > threshold                 → LOCAL_GGUF
cache_hit=true                         → respuesta directa sin llamar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVOLUCIÓN → MODEL GATEWAY (futuro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPLITTING: parte tarea → PROVIDER_A / parte → PROVIDER_B
ENSEMBLE: combina respuestas de 2 providers vía MA-RAG-SYNTH
FINE-TUNING: detecta si fine-tuned es mejor que base para la tarea
AUTO-MODEL: selecciona el modelo exacto, no solo el provider

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3 VERSIONES PARA FABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V1 BÁSICO: Auth + ModelSelector + Retry + AuditLogger
V2 COMPLETO: los 10 módulos R1-R10 (recomendada)
V3 MODEL GATEWAY: R1-R10 + Splitting + Ensemble + AutoModel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESTRUCTURA DE REPOSITORIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
github/api_router/
├── config/
│   ├── capability.json      ← reglas de routing
│   └── providers/
│       ├── provider_a.config
│       ├── provider_b.config
│       ├── provider_c.config
│       ├── provider_d.config
│       └── local_gguf.config
├── modules/
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
└── README.md


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 8 — CÁLCULO DE LÍNEAS DE CÓDIGO (LOC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MÓDULO                      LOC EST    JUSTIFICACIÓN
────────────────────────────────────────────────────────
core/adn_system             150        Leyes + validación inmutable
core/guardian_layer         200        6 checks + RECHAZAR_SOLICITUD
core/auto_recovery          400        Self-eval + replay + circuit breaker
core/llm_juez               600        Goal lock + approved/rejected + registry
────────────────────────────────────────────────────────
capa_1/input_adapter        250        listen + normalize + ack + freeze
capa_1/hash_inventory       350        SHA256 + 5L fingerprint + seed S1-S5
capa_1/wake_word_engine     150        6 comandos SYS_*
────────────────────────────────────────────────────────
capa_2/goal_engine          400        25 items + queue management
capa_2/mythos_cognitive    1200        GoalLock+Prelude+DRE+MaxMode+
                                       RecurrentLoop+GoalStop+Coda+Chef
capa_2/token_budget         250        3 alertas + writer trigger
capa_2/discovery_engine     500        5 rondas + evidence score + hipótesis
capa_2/(otros 4 módulos)    600        schema+lifecycle+session+context
────────────────────────────────────────────────────────
capa_3/decision_engine_v2  1000        Pipeline 6 etapas + 5 agentes + Devil
capa_3/agentes_consenso     750        creative+innovation+critic+selection+arch
capa_3/workflow_pipeline    400        3 patrones + groups + scheduling
capa_3/skill_manager        300        3-10 skills + capability.json
capa_3/micro_dispatcher     200        12 MA-* spawn/gather/die
capa_3/graph_runtime_dag    500        DAG + toposort + detección ciclos
capa_3/(otros 12 módulos)  1200        dependency+role+protocol+conversation
                                       policy+handoff+handoff_builder
                                       capability+event_bus+DLQ+tool+env
────────────────────────────────────────────────────────
capa_4/executor             400        ejecución supervisada
capa_4/capa_7               200        integración calidad→memoria
capa_4/execution_state      300        estado + 🔍 revisión
capa_4/artifact_engine      600        event sourcing + hash chain + fingerprint
────────────────────────────────────────────────────────
capa_5/memory_engine        800        4 tiers + event sourcing + KG
capa_5/writer_subagent      250        compacta >70% contexto
capa_5/checkpoint_rebuild   400        state.jsonl + replay_to_checkpoint
capa_5/dream_distill        400        cron weekly/daily + consolidación
capa_5/knowledge_graph      600        aristas + detección O(grado)
capa_5/master_state_engine  400        state.json + crazy_wall + SHA256
────────────────────────────────────────────────────────
capa_6/validator            300
capa_6/self_check           200
capa_6/audit_logger         400        5 logs + chain of custody
capa_6/recovery_engine      500        5 niveles + replay
capa_6/self_improvement     350        3 métricas + rollback + mutación
capa_6/output_connector     200        4 destinos
────────────────────────────────────────────────────────
control/sentinel_security   600        vigilancia permanente 9 objetivos
control/sheriff_judge       400        🛂 en 6 capas
control/push_ping           500        30 clasificaciones + simulación 5x
────────────────────────────────────────────────────────
team_agent.py               800        swarm + 20 secciones + 12 preguntas
plan_agent.py               400        design + feasibility + handoff
micro_agents/ (12 archivos) 2400       ≤200 LOC cada uno
────────────────────────────────────────────────────────
api_router/ (10 módulos)   2500        R1-R10 completos

TOTAL ORQUESTADOR:         ~15.000 LOC (Python)
TOTAL MICRO-AGENTES:       ~2.400 LOC (Python)
TOTAL API ROUTER:          ~2.500 LOC (Python)
TOTAL CONFIGS/DSL:         ~1.500 LOC (YAML/JSON)
────────────────────────────────────────────────────────
TOTAL ESTIMADO SISTEMA:    ~21.400 LOC

NOTA: Estimación conservadora basada en:
- Código determinista: 90% (sin magia)
- Tests unitarios: +30% adicional (~6.400 LOC tests)
- Documentación inline: +10% adicional
- Total con tests: ~27.800 LOC

✅ Correcto en dirección
⚠️ Ajustaría 3 cosas:

1. DSL y Reasoning deberían fusionarse en 1 raíz
   Razón: el DSL ES el lenguaje del razonamiento,
   separarlos crea dependencias circulares

2. Teams y Agents deberían ser 1 raíz con sub-módulos
   Razón: un Team es solo un grupo de agentes
   con política de coordinación, no otra entidad

3. Añadir raíz "contracts/" que no está
   Razón: los contratos entre módulos son
   tan importantes como el código mismo
   Sin contracts/ el sistema se acopla solo

PROPUESTA MEJORADA (13 raíces):
kernel/        → 20 archivos (núcleo inmutable)
orchestrator/  → 25 archivos (lógica coordinación)
teams_agents/  → 35 archivos (teams + agentes unificados)
memory/        → 20 archivos (4 tiers + graph)
reasoning/     → 30 archivos (DSL + MYTHOS + DRE fusionados)
policies/      → 15 archivos (reglas + ADN + GUARDIAN)
tools/         → 30 archivos (skills + MCP + HF Fleet)
monitoring/    → 15 archivos (métricas + health + árbol decisiones)
runtime/       → 20 archivos (estado + checkpoints + recovery)
interfaces/    → 15 archivos (API pública + headless + studio)
contracts/     → 15 archivos (schemas + validación entre módulos)
api_router/    → 15 archivos (Router independiente)
config/        → 10 archivos (connections + capability + ADN)

TOTAL: ~265 archivos, 80% bajo 300 LOC ✅


✅ La regla 100-300 LOC es correcta

Mi mejora:

Añadir una CAPA CERO antes de escribir código:
cada archivo debe tener:
  - 1 responsabilidad declarada (docstring línea 1)
  - 1 input schema
  - 1 output schema
  - 1 test mínimo asociado

Si no puedes definir esos 4 → el archivo
está haciendo demasiadas cosas → dividir

REGLA MEJORADA:
≤150 LOC  → ideal (micro-agentes, validadores)
150-300   → normal (engines, managers)
300-500   → justificado (orchestrator core, DSL compiler)
500-800   → solo con ADR aprobado (casos contados)
>800      → fragmentar obligatorio, sin excepciones

El LOC no es el problema real.
El problema real es la COHESIÓN.
Un archivo de 500 LOC con 1 responsabilidad
es mejor que 3 archivos de 150 LOC acoplados.


Idea 1 — Todo configurable
✅ Correcto. Mejora: 3 niveles de configuración:
  Nivel A: connections.yaml (providers, nunca en código)
  Nivel B: capability.json (reglas de routing y skills)
  Nivel C: adn_constitution.json (leyes, inmutable)
  REGLA: nada quemado en código excepto los contratos

Idea 2 — Sistema de plugins
✅ Crítico. Mejora: Capability-based, no name-based
  El sistema no dice "usa Aider"
  El sistema dice "necesito: refactoring_python + test_gen"
  El registry devuelve qué plugin lo cumple
  Si mañana aparece uno mejor → registro → funciona solo

Idea 3 — Event Bus
✅ Fundamental. Mejora: 3 tipos de eventos separados:
  SYSTEM_EVENTS (recovery, halt, checkpoint)
  TASK_EVENTS (inicio, fin, fallo, handoff)
  COGNITIVE_EVENTS (consenso, hipótesis, refutación)
  Cada tipo tiene su canal y su política de retry

Idea 4 — Versionado
✅ Esencial. Mejora: hash chain en todo, no solo estado
  DSL versionado con SHA256
  Skills versionadas
  Schemas versionados
  Policies versionadas
  Config versionada
  Rollback a cualquier punto del sistema en ≤10s

Idea 5 — Motor de métricas
✅ El más valioso a largo plazo. Mejora: 3 métricas clave:
  QUALITY_SCORE: ¿el output cumplió el goal?
  EFFICIENCY_SCORE: tokens/tiempo vs mínimo necesario
  RELIABILITY_SCORE: ratio de éxito sin recovery
  → automáticamente alimentan el Model Selector
  → el sistema aprende qué agente usar para cada tarea

Idea 6 — Simulador
✅ Crítico antes de gastar recursos reales. Mejora:
  Simulación debe correr 5 veces con variación aleatoria
  Si 3 de 5 simulaciones fallan → bloquear ejecución real
  El simulador usa el mismo DAG real pero con mocks
  Detecta colisiones de estado antes de que ocurran

Idea 7 — Contratos entre módulos
✅ La base de todo. Mejora: OpenAPI-style entre cada par
  Cada módulo publica: input_schema + output_schema
  El sistema valida en runtime con jsonschema strict
  Si un módulo cambia su output → rompe el contrato → error
  Esto hace que FABLES pueda sustituir cualquier módulo
  sin romper el sistema

Idea 8 — Panel de control
✅ Diferenciador clave. Mi versión mejorada está abajo ↓

✅ La propuesta es excelente. Mis mejoras:

La diferencia vs OpenClaw/Hermes:
ellos controlan configuración de sesión
NCT controla el COMPORTAMIENTO COGNITIVO

8 capas → las acepto todas, añado regla:
Cada capa tiene 3 estados: ON / OFF / SCHEDULED
SCHEDULED = activo solo en ciertas condiciones

Añadir CAPA 9 (faltante crítica):
9. GOBERNANZA
   ├── Qué decisiones requieren aprobación humana
   ├── Qué decisiones son auto-aprobadas
   ├── Qué decisiones son bloqueadas siempre
   └── Audit trail de cada decisión tomada

La capa de Gobernanza es lo que diferencia
un sistema que "parece seguro" de uno que
realmente está bajo control.

✅ Totalmente de acuerdo — es el diferenciador real

Mejora: no solo mostrar POR QUÉ eligió un Team
        mostrar el árbol completo de alternativas:

ÁRBOL DE DECISIÓN NCT:
├── Tarea: "refactorizar módulo de auth"
├── Opciones evaluadas:
│   ├── TEAM_A (code_gen + test) → score: 0.82 ← ELEGIDO
│   ├── TEAM_B (research + code) → score: 0.71
│   └── TEAM_C (audit + refactor) → score: 0.65
├── Por qué descartó TEAM_B:
│   └── budget constraint: $0.15 > límite $0.10
├── Por qué descartó TEAM_C:
│   └── capability faltante: python_3.11_typing
├── Consenso: 3/5 agentes votaron TEAM_A
└── Confidence: 0.82 (por encima de umbral 0.70)

Esto convierte el sistema en AUDITABLE por design.
No solo funciona, explica POR QUÉ funciona.
Eso es lo que necesitas para enterprise.

MODO HEADLESS vs STUDIO

✅ La separación es correcta y crítica

Mejora: añadir MODO 3 — EMBEDDED
El Kernel expone una API pública mínima
Cualquier app externa puede embeber NCT
sin interfaz propia
Caso de uso: otro sistema llama al Kernel
como si fuera una librería

Los 3 modos comparten el mismo Kernel:
HEADLESS → API/MCP/CLI (VPS, servidores)
STUDIO   → interfaz web completa
EMBEDDED → librería importable en otro sistema

REGLA CLAVE que reafirmo:
La interfaz NUNCA forma parte del Kernel.
El Kernel no sabe que existe una interfaz.
Es un cliente como cualquier otro.

Idea 1 — Auto-mejora/auto-reparación
✅ Recovery Engine sí, reescritura libre NO
Mejora: definir exactamente qué PUEDE y qué NO PUEDE:
  PUEDE: reiniciar flujos, cambiar rutas, activar fallback,
         ajustar batch_size, cambiar modelo en capability.json
  NO PUEDE: modificar ADN, cambiar contratos,
            alterar schemas, tocar código base
  REQUIERE APROBACIÓN: cualquier cambio fuera de esa lista

Idea 2 — Aprendizaje
✅ De decisiones, no de opiniones
Mejora: Reinforcement desde métricas reales:
  quality_score → ajusta qué agente usar
  efficiency_score → ajusta batch_size y paralelismo
  reliability_score → ajusta max_reintentos y circuit breaker
  El sistema aprende solo con cada ciclo completado

Idea 3 — Multi-API Router
✅ Capability Router, no "APIs en paralelo siempre"
Mejora: añadir COST_OPTIMIZER:
  Si task_simple Y provider_A_caro → provider_D
  Si task_critical → provider_A siempre (sin importar costo)
  Si presupuesto_bajo → LOCAL_GGUF automático
  El costo es una restricción primera clase, no un afterthought

Idea 4 — Consenso multi-agente
✅ OFF por defecto, ON para decisiones irreversibles
Mejora: definir exactamente cuándo se activa:
  NUNCA: tareas mecánicas (mover archivos, commits)
  SIEMPRE: cambios de arquitectura, seguridad, schema
  CONFIGURABLE: el resto según política definida
  Actor→Critic→Judge es el modelo correcto
  Añadir Devil Agent (adversarial puro) para decisiones críticas

Idea 5 — Control de formato de salida
✅ Módulo fijo obligatorio
Mejora: templates versionados + validación pre-entrega:
  El output pasa por FIREWALL_FINAL antes de salir
  Si no cumple el schema → rechazado internamente
  El agente nunca puede entregar formato libre
  JSON/Markdown/Code/DSL son las 4 salidas válidas

✅ 12-13 raíces de repositorio
✅ 200-300 LOC máximo por archivo
✅ Capability-based selection (no name-based)
✅ Event Bus con 3 canales
✅ Árbol de decisiones auditable
✅ Headless + Studio + Embedded
✅ Consenso OFF por defecto
✅ Recovery Engine con límites duros

🆕 CAPA 9 GOBERNANZA en el Centro de Control
🆕 MODO EMBEDDED (tercer modo de operación)
🆕 COST_OPTIMIZER en el Router
🆕 Simulación 5x antes de ejecución real
🆕 Hash chain en DSL + Skills + Policies
🆕 contracts/ como raíz independiente
🆕 Capability Registry como sistema central (no names)




