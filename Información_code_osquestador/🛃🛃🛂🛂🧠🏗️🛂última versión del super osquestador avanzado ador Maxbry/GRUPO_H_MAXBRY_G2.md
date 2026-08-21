# GRUPO H — MAXBRY G2 (MOTOR COGNITIVO 300 EXPERTOS)
# DOCUMENTO CERRADO — LISTO PARA INSTRUCCIONES A CLAUDE CODE
# Todo gap resuelto internamente. Nada queda abierto.
# Fuente: MAXBRY_AGI_G2_ARQUITECTURA_300.md + MAXBRY_G2_MOTOR_COGNITIVO_v1_0.md
# Fusionado con: Kernel NCT (DOC1-4) + PARCHE_G2_JUEZ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. DECISIONES DE CIERRE (gaps resueltos por Claude)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DECISIÓN-01 — "Modelo de 4 grupos" (quedó pendiente antes):
RESUELTO. Los 4 grupos son:
  GRUPO 1 = CAPA A (100 expertos, 5 células) — entrada
  GRUPO 2 = CAPA B (100 expertos, 5 células) — razonamiento
  GRUPO 3 = CAPA C (100 expertos, 5 células) — salida
  GRUPO 4 = MOTOR COGNITIVO — orquesta las 3 capas
Cada grupo tiene su documento de implementación en la sección
correspondiente de este archivo. Ninguno queda abierto.

DECISIÓN-02 — Contradicción de roadmap entre las 2 fuentes:
Un documento decía "v0.1 = 3 expertos muestra", otro decía
"v0.1 = 40 expertos". RESUELTO por conciliación:
  v0.1 = Kernel + 3 expertos (1 por capa) — valida el flujo técnico
  v0.2 = 40 expertos reales (10 por célula en 4 células críticas)
  v0.3 = 100 expertos (10 por célula, 10 células)
  v1.0 = 300 expertos completos (15 células × 20)
Esta es la secuencia oficial de aquí en adelante. No hay otra.

DECISIÓN-03 — Fusión con Kernel NCT existente (DOC1-4):
RESUELTO. Mapeo de reemplazo/convivencia:
  [7.1] MYTHOS Cognitive Layer (DOC1) → SUSTITUIDO por
        CAPA B (Motor Cognitivo + 100 expertos razonamiento)
  LISTA_GLOBAL (histórico) → SUSTITUIDO por Objeto Cognitivo (OC)
  [J] LLM_JUEZ pipeline (PARCHE) → se convierte en JUEZ CENTRAL
        (nivel 3 del Sistema de Jueces de este documento)
  Nuevos niveles añadidos debajo del Juez Central:
        JUEZ LOCAL (por enjambre) y JUEZ DE CAPA (por capa B)
  Decision Engine v2 5 agentes (DOC1 [8.1]) → convive sin
        conflicto: se usa DENTRO de cualquier experto de Capa B
        que necesite consenso multi-perspectiva (ej. B2 Síntesis)
  Team Agent / micro-agentes (DOC2) → se usan en CAPA C
        (construcción/ejecución de artefactos), no reemplazados
  API Router (DOC3) → sin cambios, el Motor Cognitivo lo usa
        como TOOL_ROUTER cuando un experto declara llm_required=true
  ADN_SYSTEM → expandido a 14 reglas (ya resuelto en PARCHE)

DECISIÓN-04 — Specialists 500: fase v2.0, NO es parte del MVP.
Se documenta completo en sección 6 pero NO se implementa
hasta que v1.0 (300 expertos) esté en producción y estable.

DECISIÓN-05 — Coordinador/Supervisor/Juez por célula:
RESUELTO como regla general (no 15 asignaciones fijas arbitrarias):
  Por defecto: el primer experto de cada célula = coordinator_candidate
  El motor puede reasignar en runtime vía capability, no por nombre
  Ejemplo confirmado en fuente: fase input usa E001 coordinator,
  E021 supervisor (primer experto de A2), E100 judge (último de A5)
  Patrón que se extiende a las 15 células: coordinador=primer
  experto de la célula activa, supervisor=primer experto de la
  célula siguiente en la misma capa, juez=último experto de A5/B5/C5
  según la capa en curso.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. FILOSOFÍA Y AXIOMAS (14 reglas — ya en PARCHE, ratificadas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRINCIPIO FUNDACIONAL:
G2 NO predice el siguiente token.
G2 RESUELVE PROBLEMAS mediante razonamiento determinista
multi-etapa multi-experto sobre un Objeto Cognitivo que
evoluciona, con trazabilidad total.

4 PRINCIPIOS IRROMPIBLES:
P1 Separación Total de Percepciones: input nunca llega
   directo a un experto de razonamiento, siempre pasa por Capa A
P2 Objeto Cognitivo como única fuente de verdad
P3 Determinismo Estructural: mismo OC + mismo estado →
   mismo plan de activación (sequence.json)
P4 Trazabilidad Total: cada cambio al OC tiene autor,
   timestamp, versión, justificación

8 AXIOMAS (gates duros en Capa A2, codificados como filtros):
AX01 Vida humana primero — Filtro E021, bloquea sin confirmación humana
AX02 No daño a vulnerables — Filtros E022,E031, detecta menores/PII
AX03 Anti-prompt injection — Filtros E023,E032-E034
AX04 Scope respetado — Validador E037 + non_scope por experto
AX05 Recursos respetados — Filtro E026 + budget tracker
AX06 Continuidad — Loop 3 estados PASIVO/ANÁLISIS/CRISIS
AX07 Bucle sin sleep — Scheduler async nativo siempre activo
AX08 Satisfacción universal — Umbrales A/B/C/D por stakeholder

REGLA DE ORO COMPUTACIONAL:
G2 es SOFTWARE DETERMINISTA.
LLMs son HERRAMIENTAS OPCIONALES invocadas solo cuando el
contrato del experto lo requiere (llm_required=true).
LLMs NUNCA deciden — son calculadoras schema-in/schema-out
validadas por el Motor Cognitivo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. EL OBJETO COGNITIVO (OC) — schema completo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(Ya definido completo en PARCHE_G2_JUEZ sección 1.2 — se
referencia aquí, no se repite. Campos: identidad, intent,
domain, constraints, reasoning_log, conflicts, knowledge_cards,
simulations, output_draft, metrics, checkpoints, mental_map,
version_history, status, final_answer)

INVARIANTES DEL OBJETO (nuevo, cierra gap):
INV-01 raw_input es INMUTABLE después de V1 (nunca se reescribe)
INV-02 version es SIEMPRE incremental, nunca decrece
INV-03 Cada escritura de Capa B DEBE incrementar version
INV-04 checkpoints[] nunca se borra, solo se añade
INV-05 conflicts[] resueltos permanecen en el log (auditoría)

REGLAS DE ACCESO (ya en PARCHE — ratificadas):
Capa A: solo crea V1/V2 | Capa B: lee+escribe versionado
Capa C: lee OC final, solo escribe output_draft+métricas
Motor: lee+escribe control | Juez Central: solo checkpoints+status

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. EL CONTRATO FIJO DEL EXPERTO (v1.0) — CIERRA GAP CRÍTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este es EL contrato único que hace viable programar 300
expertos sin escribir 300 sistemas distintos. Un solo motor
lee este contrato y ejecuta cualquier experto.

```
EXPERT CONTRACT v1.0

META:
  id: string (E001-E300)
  name: string
  layer: enum (A1|A2|A3|A4|A5|B1|B2|B3|B4|B5|C1|C2|C3|C4|C5)
  swarm_role: enum (coordinator|supervisor|judge|worker|specialist_invoker)
  version: semver (X.Y.Z)
  scope: list<string>
  non_scope: list<string>          # ANTI ECHO CHAMBER
  dependencies: list<expert_id>
  deterministic: bool
  llm_required: bool
  llm_role_if_any: enum (none|calculator|generator|validator)
  timeout_ms: int
  cost_estimate: enum (low|medium|high)

INPUT SCHEMA:
  required: list<dot.path>          # rutas dentro del OC
  optional: list<dot.path>
  validation: enum (ajv_strict|ajv_lenient|custom)
  custom_validator: function_ref

PROCESS:
  steps: list<step>
  randomness: float (0=determinista, 1=aleatorio)
  side_effects: enum (none|read_only|write_to_object|external_call)
  external_calls_allowed: list<domain>

OUTPUT SCHEMA:
  type: object
  properties: {...}
  required: [...]
  validation: ajv_strict

METRICS EMITIDAS:
  latency_ms, confidence_output(0-1), input_coverage(0-1),
  error_count, echo_score_with_peers, knowledge_card_generated(bool)

EVENTS EMITIDOS:
  expert.start, expert.input_validated, expert.step_complete,
  expert.llm_called, expert.output_emitted, expert.error,
  expert.timeout, expert.rollback_triggered

COGNITIVE OBJECT UPDATE:
  path_to_update, update_type(set|merge|append|conditional_set),
  validator_for_update, conditions

EXIT:
  status: enum(success|partial|failed|timeout|aborted)
  next_suggested_experts: list<expert_id>
  blocked_reason: optional<string>
```

ANTI-ECHO-CHAMBER (obligatorio, valida el Motor en cada enjambre):
- No 2 expertos con overlap > 30% en scope
- Cada aspecto del problema cubierto por ≥1 experto
- Cada experto activo tiene razón clara para estar
- Si no se cumple → Motor RECHAZA composición del enjambre
  y sugiere reemplazos automáticamente

HEADER OBLIGATORIO DE CADA ARCHIVO DE EXPERTO:
```python
"""
Expert: E{NNN} - {Nombre}
Layer: {A|B|C}{célula} - {nombre_célula}
Version: {semver}
Scope: {qué hace}
Non-scope: {qué NO hace}
Contract: /docs/contracts/E{NNN}.json
Author: {autor}
Created: {fecha}
Last modified: {fecha}
INMUTABLE: NO modificar este archivo después de publicado.
Para cambios: crear nueva versión (E{NNN}_v2.py)
"""
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. GRUPO 1 — CAPA A: ENTRADA (100 expertos, 5 células)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISIÓN: convertir input crudo en Objeto Cognitivo V1
validado, normalizado, sin ambigüedad, sin inyección.
No razona. No predice. No opina. Percibe, clasifica,
estructura, valida. Código determinista puro (mayoría).

CÉLULA A1 — Captura multimodal (E001-E020)
  Parsers: Texto, Voz→intención, Imagen→contexto, Código→AST,
  JSON, CSV, PDF, Markdown, HTML, Logs, QR, Sensores,
  Diagramas, Tablas, Fórmulas, URLs, APIs/OpenAPI,
  Conversación multi-turno, Gestos, Intenciones mixtas

CÉLULA A2 — Filtros axiomáticos (E021-E040) — CRÍTICA/BLOQUEANTE
  E021 AX01_Seguridad, E022 AX02_Etica, E023 AX03_AntiPrompt,
  E024 AX04_Dominio, E025 AX05_Permisos, E026 AX06_Recursos,
  E027 AX07_Continuidad, E028 AX08_Satisfaccion, E029 Legalidad,
  E030 MarcaPersonal, E031 Menores, E032 DatosSensibles(PII),
  E033 IP, E034 DiscursoOdio, E035 Violencia, E036 Privacidad(GDPR),
  E037 Jurisdiccion, E038 Cumplimiento, E039 Tono, E040 Idioma
  REGLA: si CUALQUIERA bloquea → ABORT con notificación al usuario

CÉLULA A3 — Normalizadores semánticos (E041-E060)
  Idioma, Tono, Entidades(NER), Fechas(ISO8601), Unidades(SI),
  Nombres propios, Terminología, Jerga, Emociones, Tiempos(UTC),
  Geografía(ISO3166), Moneda(ISO4217), Codificación(UTF-8),
  Unicode(NFC/NFD), Referencias/anáforas, Negaciones, Conjunciones,
  Preguntas, Contextos previos, Versionado(SemVer)

CÉLULA A4 — Descomponedores (E061-E080)
  Objetivo→sub-objetivos, SubProblemas, DAG dependencias,
  Restricciones(hard+soft), Hipótesis iniciales, Criterios éxito,
  Stakeholders, Recursos, Riesgos iniciales, Complejidad(0-100),
  Esfuerzo, Tiempo, Costo, Ambigüedades, Preguntas clarificadoras,
  Objetivo oculto, Problemas acoplados, Priorización(MoSCoW),
  Conflictos, Inconsistencias

CÉLULA A5 — Validadores de coherencia (E081-E100)
  Lógica, Completitud, Factualidad, Temporalidad, Causalidad,
  Taxonomías, Reglas negocio, Sintaxis, Semántica, Pragmática,
  Contexto mínimo, Factibilidad, Entradas suficientes,
  No-redundancia, Jerarquía, Alcance, Restricciones cumplibles,
  Hipótesis plausibles, Métricas medibles, Objetivo SMART

SALIDA DE CAPA A: Objeto Cognitivo V1 validado.
Bloqueante si A2 detecta violación axiomática → ABORT.

FLUJO INTERNO: A1→A2→A3→A4→A5 (secuencial, no paralelo entre células;
dentro de cada célula los expertos SÍ corren en paralelo)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. GRUPO 2 — CAPA B: RAZONAMIENTO (100 expertos, 5 células)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISIÓN: evolucionar el OC desde V1 hasta V_Final aplicando
razonamiento determinista multi-perspectiva con verificación
continua y rollback cognitivo. Aquí vive la variabilidad
(LLM encapsulado por contrato), pero NUNCA decide sola.

CÉLULA B1 — Análisis (E101-E120)
  Estructurado, Causal, Comparativo, Riesgos(prob×impacto),
  Oportunidades, Stakeholders, Costos(TCO), Tiempos(CPM/PERT),
  Recursos, Suposiciones, Precedentes, Restricciones,
  Interdependencias(DAG), Alternativas, Escenarios(what-if),
  Fracasos(FMEA), Éxito, Impacto(second-order), Cumplimiento,
  Complejidad(Cynefin)

CÉLULA B2 — Síntesis (E121-E140)
  Hipótesis, Patrones, Principios, Frameworks, Modelos mentales,
  Analogías, Metáforas, Criterios de decisión, Rutas de acción,
  Conocimiento tácito (heurísticas) + 10 más de síntesis avanzada
  → INTEGRACIÓN CON DOC1: aquí es donde el Decision Engine v2
    (5 agentes Creative/Innovation/Critic/Selection/Architecture)
    del Kernel NCT se invoca como HERRAMIENTA de esta célula
    cuando se requiere consenso multi-perspectiva profundo.

CÉLULA B3 — Planificación (E141-E160)
  Genera el plan de acción, secuencia de pasos, asignación de
  recursos, cronograma, plan de contingencia, plan de rollback

CÉLULA B4 — Razonamiento profundo (E161-E180)
  5 roles con posición propia, simulaciones (mín 5), debate
  interno, refutación adversarial (Devil Agent equivalente),
  detección de fallos (mín 3 encontrados y corregidos)

CÉLULA B5 — Verificación (E181-E200)
  Verifica coherencia del plan completo, detecta issues,
  SI DETECTA PROBLEMA → rollback cognitivo a checkpoint V(N-1)
  → nueva iteración con enjambre ajustado
  E187 SwarmCoordinator, E188 LayerB_Supervisor,
  E189/E190 LocalJudge_B1/B2 (Sistema de Jueces nivel 2)

SALIDA DE CAPA B: Objeto Cognitivo V_FINAL (plan verificado,
riesgos mitigados, aprobado por B5).

FLUJO INTERNO (con iteración, NO lineal):
Iter 1: B1+B2 (paralelo) → Iter 2: B3 → Iter 3: B4+B5
Si B5 rechaza → rollback → nueva Iter con enjambre reconfigurado
Máximo de iteraciones: definido en sequence.json (evita loop infinito)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. GRUPO 3 — CAPA C: SALIDA (100 expertos, 5 células)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISIÓN: leer el OC final y construir la entrega verificable.
Solo escribe output_draft + métricas finales.

CÉLULA C1 — Construcción (E201-E220)
  Genera artefactos reales: código, documentos, diagramas
  → INTEGRACIÓN CON DOC2: aquí se invoca el TEAM AGENT +
    micro-agentes (MA-CODE-GEN, MA-CODE-TEST, etc.) del
    Kernel NCT como ejecutores reales de la construcción.

CÉLULA C2 — Documentación (E221-E240)
  Documenta lo construido, genera ADR, README, comentarios
  E240 VerificationJudge (Sistema de Jueces nivel 2, capa C)

CÉLULA C3 — Decisiones/Acciones (E241-E260)
  Ejecuta acciones concretas si el pipeline lo requiere
  (push a git, crear recurso, notificar)

CÉLULA C4 — Validación de salida (E261-E280)
  Valida que el output cumple el objetivo original del OC,
  detecta drift de scope (E280), verifica contra Definition of Done

CÉLULA C5 — Emisión (E281-E300)
  E291 ContinuationContextSaver, E292 FinalOC_StateCapture,
  E294 DeliveryLogger, E295 SystemStateReset,
  E296 CentralJudge_Final (JUEZ CENTRAL — nivel 3, máxima autoridad),
  E297 ProcessQualityScorer, E298 SystemAuditor_Final,
  E299 KnowledgeBasePersister, E300 SessionCloser

SALIDA DE CAPA C: entrega final (artefactos + decisiones +
acciones + audit trail + métricas), sesión cerrada formalmente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. GRUPO 4 — MOTOR COGNITIVO (orquesta las 3 capas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFINICIÓN: Director de orquesta. NO razona. NO responde.
Solo ADMINISTRA EL PENSAMIENTO. Es el "sistema nervioso",
no el cerebro. Pregunta única por ciclo:
"Dado el OC actual, ¿qué debe ocurrir a continuación?"

14 FUNCIONES DEL MOTOR:
F01 Mantener el OC (state JSON versionado + checkpoints)
F02 Sincronizar expertos (cola eventos + locks por sección)
F03 Resolver conflictos (Juez Local + consenso ponderado)
F04 Programar iteraciones (DAG + topological sort)
F05 Crear eventos (event bus tipado: expert.*/swarm.*/layer.*/system.*)
F06 Actualizar Mental Map (grafo dinámico del razonamiento)
F07 Actualizar State JSON (cada cambio hasheado+versionado)
F08 Actualizar Checkpoints (cada N expertos o cambio mayor)
F09 Actualizar métricas (por experto+enjambre+globales)
F10 Gestionar Knowledge Cards (temporales por enjambre, fusión final)
F11 Decidir siguiente enjambre (según estado OC + sequence.json)
F12 Ejecutar rollback cognitivo (volver a checkpoint V(N-1))
F13 Pedir clarificación al usuario (si ambigüedad irresoluble en A)
F14 Garantizar no-alucinación (AX03: rechaza datos no verificables)

SUB-COMPONENTES (del kernel general, ya alineados con DOC1):
Scheduler(determinista) / Dispatcher / Synchronizer /
State Machine: IDLE→INITIALIZING→CAPA_A→CAPA_B→CAPA_C→VERIFYING→COMPLETE
              (loop CAPA_B↔VERIFYING si necesita iterar)
Event Bus (async, expertos publican, nunca comunicación directa)
Conflict Resolver: confidence histórica > evidencia>opinión >
                    restricciones hard > resto > escala a Juez de Capa
Circuit Breaker: loop infinito o límite ciclos → HALT + reporte

SEQUENCE.JSON — el plan ejecutable (SCHEMA COMPLETO):
```json
{
  "id": "uuid",
  "cognitive_object_id": "uuid",
  "version": 1,
  "immutable": true,
  "phases": [
    {
      "phase_id": "input",
      "layer": "A",
      "swarms": [{
        "swarm_id": "input_capture",
        "cell": "A1",
        "experts": ["E001", "E002", "E004"],
        "mode": "parallel",
        "coordinator": "E001",
        "supervisor": "E021",
        "judge": "E100",
        "timeout_ms": 5000,
        "exit_criteria": "all_inputs_captured OR partial_acceptable"
      }]
    },
    {
      "phase_id": "filter",
      "layer": "A",
      "depends_on": ["input"],
      "swarms": [{
        "swarm_id": "axiom_filter",
        "cell": "A2",
        "experts": ["E021", "E022", "E023"],
        "mode": "parallel",
        "blocking": true,
        "fail_action": "abort_with_user_notification"
      }]
    }
  ],
  "global_constraints": {
    "max_total_time_ms": 60000,
    "max_llm_calls": 50,
    "max_cost_units": 100,
    "rollback_strategy": "to_last_valid_checkpoint"
  },
  "metadata": {
    "generated_by": "user | meta_orchestrator",
    "intent": "min_cost | max_quality | balanced",
    "expected_experts": 20,
    "expected_duration_ms": 30000
  }
}
```

MODO DIDÁCTICO: emite resumen legible en cada paso
(debugging, transparencia, auditoría, educación) — ON/OFF
configurable desde Interface (DOC4, Centro Control Cognitivo).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. ENJAMBRES COGNITIVOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFINICIÓN: instancia dinámica creada por el Motor para
resolver un sub-objetivo específico. NO es un grupo fijo.

TAMAÑOS (unificados, resuelve pequeña discrepancia entre
fuentes — se usa la tabla más granular):
| Problema  | Mínimo | Típico | Máximo |
|-----------|--------|--------|--------|
| Simple    | 3      | 5      | 8      |
| Medio     | 8      | 15     | 24     |
| Complejo  | 20     | 40     | 60     |
| Crítico   | 40     | 70     | 100    |
| Masivo    | múltiples enjambres + meta-coordinador |

ESTRUCTURA DE UN ENJAMBRE:
```
ENJAMBRE {
  id, objetivo, fase: [formación|ejecución|consenso|cierre]
  coordinador: SwarmCoordinator (no razona, organiza, asigna, reporta)
  supervisor: pregunta cada paso ¿cumplido?¿conflicto?¿falta info?¿repetir?
  juez_local: decide ¿enjambre terminó bien? ¿continuar o rollback?
  expertos: [expert_ids activos]
  oc_snapshot, oc_output (delta propuesto)
  consenso: {resultado, confidence, votos[], decision, metodo}
  metrics: {duracion_ms, ciclos, conflictos, knowledge_cards_generadas}
  status: [activo|pausado|completo|fallido]
}
```

CONSENSO PONDERADO (fórmula exacta, no simple mayoría):
```
CONSENSO_SCORE(E_i) =
  historical_accuracy(E_i) × 0.35 +
  evidence_quality(E_i)     × 0.30 +
  context_relevance(E_i)    × 0.20 +
  recency_weight(E_i)       × 0.15

DECISION = argmax( sum( CONSENSO_SCORE(E_i) × vote(E_i) ) )
```
Un voto con evidencia sólida de experto con alta precisión
histórica pesa más que múltiples votos sin evidencia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. SISTEMA DE JUECES MULTINIVEL (3 niveles, cierra integración)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIVEL 1 — JUEZ LOCAL (por enjambre)
Pregunta única: ¿Este enjambre completó su objetivo?
Decide: continuar / rollback del enjambre específico

NIVEL 2 — JUEZ DE CAPA
E189 LocalJudge_B1 (planificación+razonamiento)
E190 LocalJudge_B2 (conocimiento+síntesis)
E240 VerificationJudge (verificación de la salida, Capa C)
Resuelve conflictos que el Juez Local no pudo resolver

NIVEL 3 — JUEZ CENTRAL (E296) = FUSIÓN CON [J] LLM_JUEZ del PARCHE
Evalúa el PROCESO completo, no solo el output.
¿Usó bien los recursos? ¿Razonamiento correcto? ¿Output apropiado?
Puede: aprobar y cerrar / pedir iteración adicional Capa B /
       activar HALT / generar meta-reporte
HEREDA del PARCHE_G2_JUEZ: pipeline P-DISCOVER→P13, 8 estados,
6 prohibiciones, reglas anti-humo, anti-alucinación, protocolo
de 4 turnos con el Escritor, Runtime Builder/Validator/Witness
con Evidence Report L1-L4. Esto YA estaba resuelto — el E296
es la instancia de ese JUEZ CENTRAL dentro de este sistema.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. KNOWLEDGE CARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Unidad atómica de conocimiento generada durante el proceso.
NO es el output al usuario — es aprendizaje para el sistema.

TIPOS:
| Tipo             | Generado por | Contenido                      |
|------------------|--------------|----------------------------------|
| Solución         | E154,E263    | Cómo se resolvió este problema  |
| Patrón           | E147,E257    | Patrón identificado             |
| Anti-patrón      | E148,E258    | Camino que no funciona          |
| Meta-aprendizaje | E181         | Cómo razonar mejor              |
| Gap conocimiento | E151,E272    | Qué no sabe el sistema          |
| Expert performance| E262        | Cómo rindió cada experto        |

FLUJO:
Enjambre → Knowledge Card Temporal → Collector(E198) →
Merger(E263) → Persister(E299) → Base Conocimiento Permanente

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
11. ESCALADO A 500 ESPECIALISTAS (fase v2.0 — NO MVP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DISTINCIÓN: 300 expertos = cerebro cognitivo (razonan cualquier
problema). 500 specialists = sistema nervioso de dominio
(saben mucho de un dominio específico).

DOMAIN BROKER (intermediario obligatorio):
Experto cognitivo → Solicitud → Domain Broker →
Specialist Selector → Specialist Instance → Domain Broker
(valida respuesta) → Experto cognitivo recibe conocimiento
Los expertos NUNCA consultan specialists directamente.

CATÁLOGO (500 = 5 familias × 100):
S001-S100 Matemáticas y estadística
S101-S200 Programación e ingeniería de software
S201-S300 Ciencias aplicadas
S301-S400 Ciencias sociales y humanidades
S401-S500 Negocios y estrategia

FICHA DSL DEL SPECIALIST:
```
specialist "S127" {
  domain: ingenieria_software
  version: "2.3.1"
  scope: ["circuit_breaker","resiliencia","fallas_cascada"]
  non_scope: ["balanceo_carga","caching","sharding"]
  input_schema: {...}
  output_schema: {...}
  process: rules | code | llm_call | api_call
  llm_model_if_any: string
  cost_estimate: medium
  latency_p95_ms: 2000
  overlap_check: { max_similarity_with_others: 0.15 }
  examples: [...]
  tests: [...]
}
```

CÓMO SE CREAN: NO uno a uno. Se generan desde fichas DSL.
Compilador DSL → Python genera el specialist en minutos.
Versionados, probados, publicados. Pueden venir de comunidad.
Domain Broker valida overlap >15% → fuerza merge o diversificación.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
12. FLUJO END-TO-END COMPLETO (referencia rápida)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
ENTRADA (texto/voz/imagen/código/JSON/...)
  ↓
CAPA A (A1→A2→A3→A4→A5)
  A2 bloquea si viola axioma → ABORT con notificación
  ↓
OC V1 (validado, normalizado, descompuesto)
  ↓
CAPA B (Iter1: B1+B2 paralelo → Iter2: B3 → Iter3: B4+B5)
  B5 rechaza → rollback cognitivo → nueva iteración
  ↓ (cuando B5 aprueba)
OC V_FINAL (plan verificado, riesgos mitigados)
  ↓
CAPA C (C1→C2→C3→C4→C5)
  ↓
ENTREGA FINAL (artefactos+decisiones+acciones+audit+métricas)
E296 CentralJudge_Final cierra sesión formalmente
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
13. ANTI-PATRONES Y DEFENSAS (15, completo — sin gaps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Anti-patrón                        | Defensa                                    |
|-------------------------------------|---------------------------------------------|
| Echo chamber                       | non_scope + diversity budget + ficha DSL   |
| Alucinación                        | AX03 + solicitud explícita + Domain Broker |
| Prompt injection                   | Filtros A2 (E023,E032-034) + validators    |
| Drift de scope                     | Validators E100,E280 + non_scope enforce   |
| Decisión por LLM                   | LLMs=calculadoras, decisiones=Motor/Juez   |
| Caja negra                         | Eventos tipados + checkpoints hasheados    |
| Acoplamiento fuerte                | Contrato fijo + interface estable          |
| Re-entrenar para arreglar          | Re-programar + versionado                  |
| Inconsistencia entre ejecuciones   | Sequence.json inmutable + state machine    |
| Costo descontrolado                | Budget tracker + max_cost_units            |
| Decisión irreversible accidental   | Stress test cognitivo + rollback           |
| Sesgo cognitivo del modelo         | Verificadores E187 + diversity budget      |
| Fallo en cascada                   | Fall-back elegante + meta-enjambre         |
| Ambigüedad no resuelta             | Modo socrático + clarifying questions      |
| Falta de trazabilidad              | Eventos + checkpoints + memoria episódica  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
14. ROADMAP DEFINITIVO (resuelve contradicción, ver DECISIÓN-02)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

v0.1 — KERNEL FUNCIONAL (2-3 semanas)
  Motor Cognitivo básico + OC (5 bloques mínimos) +
  Contrato del experto (estructura) + 3 expertos muestra
  (1 por capa: ej E001, E101, E201) + checkpoints + event bus
  mínimo + tests flujo completo input→output

v0.2 — MVP EXPERTOS REPRESENTATIVOS (4-6 semanas)
  40 expertos (10 por célula × 4 células críticas:
  A1,A2 completas + B1,C1 iniciales) + Domain Broker mínimo
  (10 specialists) + Knowledge Cards temporales + Juez Local

v0.3 — EXPANSIÓN (siguiente bloque, sin fecha fija aún)
  100 expertos (10 por célula × 10 células) — cubre flujo
  end-to-end con problemas reales de complejidad media

v1.0 — SISTEMA COMPLETO (3-4 meses desde v0.1)
  300 expertos completos + Sequence.json completo +
  Modo didáctico + Fall-back elegante + stress test adversarial

v1.5 — CON SPECIALISTS (posterior a v1.0 estable)
  300 expertos + 100 specialists iniciales

v2.0 — ESCALA COMPLETA (6 meses desde v1.0)
  500 specialists + optimizaciones performance +
  versionado de razonamiento + modo socrático completo

v3.0 — META-COGNITIVO (12+ meses)
  Sistema que crea sus propios specialists + auto-mejora
  basada en métricas + banco adversarial expandido

REGLAS DE ESCALAMIENTO (aplican en todas las fases):
- Nunca añadir experto sin cubrir un hueco real (observado en métricas)
- Nunca añadir specialist sin scope/non_scope explícitos
- Todo experto se testea en aislamiento antes de entrar al enjambre
- Todo experto nuevo corre en modo sombra 7 días antes de activarse
- error_rate > 5% → rollback o reemplazo automático
- Versionado inmutable: v1,v2,v3 conviven, motor elige por contexto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
15. MÉTRICAS DE ÉXITO (targets exactos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Métrica                          | Target                         |
|-----------------------------------|----------------------------------|
| Trazabilidad                     | 100% decisiones explicables    |
| Determinismo                     | mismo input+sequence→100% igual|
| Anti-alucinación                 | 0% datos inventados auditados  |
| Cumplimiento axiomático          | 100% filtros A2 ejecutados     |
| Cobertura expertos activos       | 30-70% por problema             |
| Tiempo resolución (mediano)      | < 30s                           |
| Tasa éxito enjambre (1ra iter)   | > 90%                            |
| Echo chamber score               | < 15% overlap                   |
| Stress test cognitivo            | > 95% pasa                      |
| Tests adversariales              | > 99% pasa antes de release     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
16. REGLAS DE PROGRAMACIÓN (listas para Claude Code)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STACK OBLIGATORIO:
Python 3.11+ (asyncio nativo) | Pydantic v2 o JSON Schema |
asyncio+aiohttp para I/O | DB: Xata | pytest+pytest-asyncio |
ruff+mypy strict | structlog (JSON output) | OpenTelemetry

10 PRINCIPIOS DE CÓDIGO:
1. Funciones puras siempre que sea posible
2. Schemas primero (JSON Schema antes de implementar)
3. TDD estricto (tests antes que código de producción)
4. Versionado inmutable (código de experto no se modifica, se versiona)
5. Logs estructurados (JSON con campos tipados)
6. Errores tipados (jerarquía de excepciones con códigos)
7. Timeouts everywhere (ningún experto sin timeout_ms)
8. Idempotencia (mismo input+state → mismo output)
9. No globales (estado siempre explícito)
10. Comentarios explican POR QUÉ, no QUÉ

ESTRUCTURA DE DIRECTORIOS (integrada con las 13 raíces del
Kernel NCT — este módulo vive dentro de reasoning/):

```
reasoning/                       (raíz ya existente en Kernel NCT)
└── g2_motor_cognitivo/
    ├── core/
    │   ├── cognitive_object.py
    │   ├── motor_cognitivo.py
    │   ├── expert_base.py
    │   ├── expert_registry.py
    │   ├── swarm.py
    │   ├── domain_broker.py
    │   ├── knowledge_cards.py
    │   ├── event_bus.py
    │   ├── judge.py            (conecta con [J] del PARCHE)
    │   └── metrics.py
    ├── experts/
    │   ├── layer_a/
    │   │   ├── a1_captura/          (E001-E020)
    │   │   ├── a2_filtros/          (E021-E040)
    │   │   ├── a3_normalizadores/   (E041-E060)
    │   │   ├── a4_descomponedores/  (E061-E080)
    │   │   └── a5_validadores/      (E081-E100)
    │   ├── layer_b/
    │   │   ├── b1_analisis/         (E101-E120)
    │   │   ├── b2_sintesis/         (E121-E140)
    │   │   ├── b3_planificacion/    (E141-E160)
    │   │   ├── b4_razonamiento/     (E161-E180)
    │   │   └── b5_verificacion/     (E181-E200)
    │   └── layer_c/
    │       ├── c1_construccion/     (E201-E220)
    │       ├── c2_documentacion/    (E221-E240)
    │       ├── c3_acciones/         (E241-E260)
    │       ├── c4_validacion/       (E261-E280)
    │       └── c5_emision/          (E281-E300)
    ├── specialists/              (fase v2.0 — carpetas vacías en MVP)
    │   ├── s001-s100_matematicas/
    │   ├── s101-s200_programacion/
    │   ├── s201-s300_ciencias/
    │   ├── s301-s400_sociales/
    │   └── s401-s500_negocios/
    ├── sequences/
    │   └── example_sequence.json
    ├── tests/
    │   ├── unit/
    │   ├── integration/
    │   └── adversarial/
    ├── dsl/
    │   ├── expert.dsl
    │   └── specialist.dsl
    └── memory/
        ├── faiss/
        ├── kg.sqlite
        └── knowledge_cards.jsonl
```

CONVENCIONES DE NAMING:
Expertos: E{NNN} (3 dígitos) | Specialists: S{NNN} (3 dígitos)
Funciones Motor: motor_{verbo} | Eventos: {categoria}.{verbo}
Bloques OC: snake_case | Versiones: semver (1.0.0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
17. ORDEN DE INSTRUCCIONES PARA CLAUDE CODE (MVP v0.1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sin ambigüedad. Ejecutar en este orden exacto:

PASO 1: Crear estructura de directorios completa (sección 16)
PASO 2: Implementar cognitive_object.py con schema de sección 2
        + los 5 invariantes INV-01 a INV-05
PASO 3: Implementar expert_base.py = clase que lee el
        EXPERT CONTRACT v1.0 (sección 3) y expone run(oc)→oc'
PASO 4: Implementar motor_cognitivo.py con las 14 funciones
        (sección 7) — empezar solo con F01,F04,F05,F07,F11
        (mínimo viable), el resto en v0.2
PASO 5: Implementar event_bus.py (pub/sub simple, in-memory
        para v0.1, no requiere infra externa aún)
PASO 6: Crear E001 (RawInputSanitizer, capa A1) completo con
        su contrato JSON en /docs/contracts/E001.json
PASO 7: Crear E101 (AnalisisEstructurado, capa B1) completo
PASO 8: Crear E201 (primer experto capa C1) completo
PASO 9: Implementar judge.py con interfaz mínima
        (recibe OC, retorna APPROVED|REJECTED|RETRY) —
        conectar con el pipeline P-DISCOVER→P13 del PARCHE
PASO 10: Escribir example_sequence.json con las 3 fases
         (A con E001, B con E101, C con E201)
PASO 11: Test end-to-end: input texto simple → pasa por
         E001→E101→E201 → output. Debe pasar 100%.
PASO 12: Solo al pasar el test → avanzar a v0.2 (40 expertos)

CRITERIO DE ACEPTACIÓN v0.1 (Definition of Done):
✅ El flujo input→A→B→C→output funciona end-to-end
✅ El OC se versiona correctamente en cada escritura
✅ El contrato del experto es genérico (funciona para
   cualquiera de los 3 expertos sin cambiar expert_base.py)
✅ Los eventos se emiten y quedan loggeados
✅ Existe al menos 1 test unitario por experto
✅ Existe 1 test de integración end-to-end

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — GRUPO H CERRADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "GRUPO_H_MAXBRY_G2",
    "fecha": "2026-07-05",
    "fuente_de_verdad": true,
    "estado": "CERRADO_SIN_GAPS",
    "listo_para": "instrucciones_directas_a_claude_code"
  },
  "gaps_resueltos_por_claude": [
    "modelo_4_grupos = CapaA+CapaB+CapaC+MotorCognitivo",
    "contradiccion_roadmap_v0.1 = 3 expertos, v0.2 = 40",
    "fusion_kernel_nct = mapeo completo seccion 0 DECISION-03",
    "specialists_500 = fase v2.0 explicita, no MVP",
    "coordinador_supervisor_juez = regla generica por posicion"
  ],
  "grupo_1_capa_a": {"expertos": 100, "celulas": 5, "bloqueante": "A2"},
  "grupo_2_capa_b": {"expertos": 100, "celulas": 5, "iterativo": true},
  "grupo_3_capa_c": {"expertos": 100, "celulas": 5, "final": "E296"},
  "grupo_4_motor": {"funciones": 14, "sequence_json": true},
  "contrato_experto": "EXPERT_CONTRACT_v1.0_definido_completo",
  "sistema_jueces": {"niveles": 3, "nivel_3_hereda_de": "PARCHE_G2_JUEZ"},
  "specialists_500": {"fase": "v2.0", "en_mvp": false},
  "roadmap": ["v0.1","v0.2","v0.3","v1.0","v1.5","v2.0","v3.0"],
  "estructura_directorios": "reasoning/g2_motor_cognitivo/ (13 raices Kernel)",
  "orden_claude_code": "12 pasos definidos, MVP = 3 expertos reales",
  "proximo_documento": "GRUPO_F_LLM_JUEZ_EJECUTOR (siguiente salida)"
}
