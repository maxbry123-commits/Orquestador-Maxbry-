# NCT_KERNEL_ORQUESTADOR_v2.md
# Fuente de verdad — Sonnet / Opus / FABLES
# Version: 2.0 | Checkpoint: DOC1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — ORQUESTADOR RAÍZ / DIAGRAMA COMPLETO
NCT KERNEL v0.4 — Agnóstico de provider — 64 nodos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
    │       output: {stack, fichas_dsl, esfuerzo, riesgos, primer_paso}
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
    Selección por CAPABILITIES no por nombre de agente:
    "necesito: refactoring_python + test_gen"
    El registry devuelve qué agente lo cumple.
    Si aparece uno mejor mañana → registro → funciona solo.

[19] EVENT BUS │ ▼
    ├── SYSTEM_EVENTS (recovery, halt, checkpoint)
    ├── TASK_EVENTS (inicio, fin, fallo, handoff)
    └── COGNITIVE_EVENTS (consenso, hipótesis, refutación)
    Cada canal tiene su política de retry independiente.

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

[26] ARTIFACT ENGINE │ ▼ 🛂 │ 🔍 │ ▼
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
    ├── Hash chain en DSL + Skills + Policies versionados
    │   Rollback a cualquier punto del sistema en ≤10s
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
    ├── Valida contratos entre módulos (OpenAPI-style)
    ├── input_schema + output_schema por cada módulo
    ├── jsonschema strict en runtime
    └── Cambio de output → rompe contrato → error inmediato

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
    PUEDE: reiniciar flujos, cambiar rutas, activar fallback,
           ajustar batch_size, cambiar modelo en capability.json
    NO PUEDE: modificar ADN, cambiar contratos, alterar schemas
    REQUIERE APROBACIÓN: cualquier cambio fuera de esa lista

[30.3] SELF IMPROVEMENT LOOP │ ▼
    ├── Mide por ciclo:
    │   ├── QUALITY_SCORE: ¿el output cumplió el goal?
    │   ├── EFFICIENCY_SCORE: tokens/tiempo vs mínimo necesario
    │   └── RELIABILITY_SCORE: ratio de éxito sin recovery
    ├── → alimentan automáticamente el Model Selector del Router
    ├── → el sistema aprende qué agente usar para cada tarea
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — NOTAS DEL ORQUESTADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

NOTA_11 — 3 NIVELES DE CONFIGURACIÓN (nuevo, debate aprobado)
Nivel A: connections.yaml (providers, NUNCA en código)
Nivel B: capability.json (reglas de routing y skills)
Nivel C: adn_constitution.json (leyes, inmutable)
REGLA: nada quemado en código excepto los contratos de interfaz.

NOTA_12 — CONTRATOS ENTRE MÓDULOS (nuevo, debate aprobado)
Cada módulo publica: input_schema + output_schema.
El sistema valida en runtime con jsonschema strict.
Si un módulo cambia su output → rompe el contrato → error.
Esto permite que FABLES sustituya cualquier módulo sin romper el sistema.
Raíz dedicada: contracts/ con 15 archivos de schemas.

NOTA_13 — REGLA LOC POR ARCHIVO (nuevo, debate aprobado)
Cada archivo debe tener antes de escribir código:
  1. 1 responsabilidad declarada (docstring línea 1)
  2. 1 input schema
  3. 1 output schema
  4. 1 test mínimo asociado
≤150 LOC → ideal (micro-agentes, validadores)
150-300  → normal (engines, managers)
300-500  → justificado (orchestrator core, DSL compiler)
500-800  → solo con ADR aprobado
>800     → fragmentar obligatorio, sin excepciones
La COHESIÓN importa más que el LOC.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 3 — ESTRUCTURA REPOSITORIO (13 raíces)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

github/
├── kernel/          → 20 archivos (núcleo inmutable: ADN, Guardian, Recovery)
├── orchestrator/    → 25 archivos (lógica coordinación: MYTHOS, Decision, Planner)
├── teams_agents/    → 35 archivos (teams + agentes unificados + 12 MA-*)
├── memory/          → 20 archivos (4 tiers + KG + Dream + Distill)
├── reasoning/       → 30 archivos (DSL + MYTHOS + DRE fusionados)
├── policies/        → 15 archivos (reglas + ADN + GUARDIAN + Gobernanza)
├── tools/           → 30 archivos (skills + MCP + HF Fleet)
├── monitoring/      → 15 archivos (métricas + health + árbol decisiones)
├── runtime/         → 20 archivos (estado + checkpoints + recovery)
├── interfaces/      → 15 archivos (API pública + headless + studio + embedded)
├── contracts/       → 15 archivos (schemas + validación entre módulos)
├── api_router/      → 15 archivos (Router independiente R1-R10)
└── config/          → 10 archivos (connections.yaml + capability.json + ADN)

TOTAL: ~265 archivos, 80% bajo 300 LOC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 4 — CÁLCULO LOC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MÓDULO                      LOC EST
core/adn_system             150
core/guardian_layer         200
core/auto_recovery          400
core/llm_juez               600
capa_1/input_adapter        250
capa_1/hash_inventory       350
capa_1/wake_word_engine     150
capa_2/goal_engine          400
capa_2/mythos_cognitive    1200
capa_2/token_budget         250
capa_2/discovery_engine     500
capa_2/(otros 4 módulos)    600
capa_3/decision_engine_v2  1000
capa_3/agentes_consenso     750
capa_3/workflow_pipeline    400
capa_3/skill_manager        300
capa_3/micro_dispatcher     200
capa_3/graph_runtime_dag    500
capa_3/(otros 12 módulos)  1200
capa_4/executor             400
capa_4/capa_7               200
capa_4/execution_state      300
capa_4/artifact_engine      600
capa_5/memory_engine        800
capa_5/writer_subagent      250
capa_5/checkpoint_rebuild   400
capa_5/dream_distill        400
capa_5/knowledge_graph      600
capa_5/master_state_engine  400
capa_6/validator            300
capa_6/self_check           200
capa_6/audit_logger         400
capa_6/recovery_engine      500
capa_6/self_improvement     350
capa_6/output_connector     200
control/sentinel_security   600
control/sheriff_judge       400
control/push_ping           500
contracts/ (15 schemas)     750

TOTAL ORQUESTADOR:   ~15.750 LOC (Python)
TOTAL CONFIGS/DSL:   ~1.500 LOC (YAML/JSON)
TOTAL SISTEMA:       ~21.400 LOC
Total con tests:     ~27.800 LOC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — DOC1
Fuente de verdad para Sonnet / Opus / FABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "NCT_KERNEL_ORQUESTADOR_v2",
    "version": "2.0",
    "fecha": "2026-07-04",
    "fuente_de_verdad": true,
    "instruccion": "Leer este JSON antes de cualquier acción de construcción."
  },
  "kernel": {
    "nodos_totales": 64,
    "capas": ["CAPA_0","CAPA_1","CAPA_2","CAPA_3","CAPA_4","CAPA_5","CAPA_6"],
    "push_ping_clasificaciones": 30,
    "micro_agentes_MA": 12,
    "sentinel_points": 7
  },
  "decisiones_aprobadas": {
    "NO_ping_externo": true,
    "NO_nombres_AI_en_codigo": true,
    "NO_OpenRouter_hub_unico": true,
    "SI_event_sourcing_puro": true,
    "SI_fingerprint_5_capas": true,
    "SI_consenso_5_agentes_plus_devil": true,
    "SI_budget_dsl_90_10": true,
    "SI_memoria_4_tiers": true,
    "SI_capability_based_no_name_based": true,
    "SI_event_bus_3_canales": true,
    "SI_contratos_entre_modulos": true,
    "SI_13_raices_repositorio": true,
    "SI_simulacion_5x_preejecutar": true,
    "SI_hash_chain_dsl_skills_policies": true
  },
  "nuevas_integraciones_debate": {
    "CAPA_9_GOBERNANZA": "pendiente DOC4 Interface",
    "MODO_EMBEDDED": "pendiente DOC4 Interface",
    "COST_OPTIMIZER": "pendiente DOC3 Router",
    "contracts_raiz": "integrado en 13 raices",
    "capability_registry_central": "integrado en [18]"
  },
  "pendientes": {
    "PATCH_002": "Director sube a bandeja",
    "CAPA_7_decision": "Director aprueba función exacta",
    "OBJ3_ANTIGRAVITY": "bloqueado hasta que Director abra sandbox",
    "JSON_YAIWES": "pendiente OBJ1",
    "JSON_DECEPTICONS": "pendiente OBJ1"
  },
  "proximos_docs": {
    "DOC2": "NCT_TEAM_AGENT_v2.md",
    "DOC3": "NCT_API_ROUTER_v2.md",
    "DOC4": "NCT_INTERFACE_v2.md"
  }
}
