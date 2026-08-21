# MAPA SEGMENTADO — ORQUESTADOR (MAXBRY Orquestador / Kernel NCT)
# Toda la raíz, cerrado, para visualizar y decidir cambios futuros
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUÉ ES EL ORQUESTADOR (1 frase)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El cerebro determinista que decide QUÉ hacer, CUÁNDO,
CON QUIÉN y CON QUÉ NIVEL DE PROFUNDIDAD. Nunca ejecuta
código él mismo — delega todo a Team Agente y Fichas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 1 — IDENTIDAD (repo 1: orquestador-nucleo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ADN_SYSTEM      14 reglas inmutables (6 leyes + 8 axiomas)
GUARDIAN_LAYER  6 checks, rechaza si viola ADN/leyes/auditoría/
                trazabilidad/seguridad/aislamiento
AUTO_RECOVERY   watchdog 30s interno, replay_to_checkpoint,
                circuit breaker 3 reintentos
LLM_JUEZ        8 estados, pipeline P-DISCOVER..P13, único
                que dice APPROVED/REJECTED, nunca escribe código

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 2 — ENTRADA (dentro de repo 1+2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT ADAPTER     normaliza, congela (FROZEN v1.0), hashea
HASH ENGINE       fingerprint 5 capas (L1 léxico..L5 dependencias)
WAKE WORD ENGINE  6 comandos SYS_HALT/EXECUTE/PLAN/VERIFY/YIELD/RESUME
PUSH_PING         30 clasificaciones obligatorias antes de avanzar
                  (objetivo, tipo tarea, DRE, volumen, DoD, etc.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 3 — RAZONAMIENTO (repo 2: orquestador-razonamiento)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MYTHOS          GoalLock+Prelude+DRE+MaxMode+RecurrentLoop+
                GoalStop+Coda+ChefFinal
DRE ESTIMATOR   score→ RAPIDO(0-3)/BASICO(4-8)/AVANZADO(9-15)/
                TURBO(16+)
TOKEN BUDGET    90% DSL código / 10% LLM, alertas 70/85/95%
DISCOVERY       ciclos 2-5 rondas, evidence_score≥0.85

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 4 — LOOP ENGINE (repo 3, AISLADO — la clave)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 solo entry point: run_loop_engine(goal_lock, dre_score)
4 niveles escalables: RAPIDO(20-50)/BASICO(100-300)/
AVANZADO(300-800)/TURBO(800-1000) pasos
9 fases reutilizables en los 4 niveles (Init→Comprensión→
Análisis→Planificación→Debate→Verificación→Optimización→
Autoeval→Síntesis)
Escalado DINÁMICO durante ejecución si progreso insuficiente
Llamado por: Orquestador Y Team Agente (mismo módulo, 2 llamadores)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 5 — VERIFICACIÓN FORMAL (repo 4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GCL-lite    O(1) por paso, presupuesto+contratos+task_id+hash
GCL v1.0    gate final único en P13, usa motor Z3 (SAT/UNSAT)
SLOT CONTRACT SC1-SC6: entrada válida→dependencias→permisos→
              estado consistente→objetivo alcanzable (Z3)→salida
Z3 SOLVER   verifica presupuesto+deadline+dependencias a la vez

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 6 — MOTOR COGNITIVO G2 (repo 5+6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJETO COGNITIVO (OC)  reemplaza LISTA_GLOBAL, versionado,
                       5 invariantes
MOTOR 14 FUNCIONES     Scheduler/Dispatcher/Synchronizer/
                       StateMachine/EventBus/ConflictResolver
300 EXPERTOS           Capa A(100 entrada)+B(100 razonamiento)+
                       C(100 salida), 15 células de 20
CONTRATO EXPERTO v1.0  schema-in/schema-out, anti-echo-chamber
                       (overlap<30%)
SISTEMA JUECES 3 NIV.  Local(por enjambre)→Capa(B1/B2/C)→
                       Central(E296=mismo LLM_JUEZ del repo 1)
MAPEO A LOOP ENGINE    RAPIDO/BASICO=solo MYTHOS directo,
                       AVANZADO=1-3 expertos/fase,
                       TURBO=enjambre completo/célula

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 7 — CONSENSO (dentro de repo 2, DOC1 [8.1])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5 AGENTES  Creative(0.9)→Innovation(0.7)→Critic(0.3)→
           Selection(0.2)→Architecture(0.3)
DEVIL AGENT  ataca la ganadora antes de aprobar
QUORUM     mín 3/5, <3→ALERTA Director
V1/V2      Director Loop (humano) / Auto-gate (confidence)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 8 — MEMORIA (repo 11)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 TIERS       Tier0 RAW(efímero)→Tier1 SESSION→Tier2 STRATEGIC→
              Tier3 PROJECT(permanente)
EVENT SOURCING  hash chain SHA256, time-travel/rollback
KNOWLEDGE GRAPH aristas: version_de/contradice/refina/depende_de
WRITER SUBAGENT compacta si contexto>70%
DREAM/DISTILL   semanal/diario
FAISS+TTL       {0:None,1:30d,2:7d,3:24h,4:1h} (de G2_PECP)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 9 — CALIDAD Y RECUPERACIÓN (repo 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOVERY 5 NIVELES  Retry→Rollback→Checkpoint→Replan→Escalate
SELF IMPROVEMENT    3 métricas (calidad/eficiencia/confiabilidad)
                    → alimenta Sentinela (repo 15) para decidir mejoras
AUDIT LOGGER        5 logs (custody/fault/event/router/change)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 10 — CONEXIÓN CON EXTERIOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
API ROUTER (repo 10)     10 módulos R1-R10 + COST_OPTIMIZER,
                         agentes ciegos al provider
CONTRACTS (repo 12)      Universal Module Contract (enchufe
                         Opus) — TODO módulo lo emite para existir
TEAM AGENTE (repo 7-9)   recibe órdenes, nunca ve el cerebro
SENTINELA (repo 15)      vigila desempeño, propone mejoras de
                         MÉTODO (nunca toca este mapa completo)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLUJO COMPLETO EN 1 VISTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input → [Seg.1 Identidad valida] → [Seg.2 Entrada+PushPing]
→ [Seg.3 MYTHOS razona] → [Seg.4 Loop Engine ejecuta N pasos]
  → (si nivel lo justifica) [Seg.6 invoca expertos G2]
→ [Seg.7 Consenso si es crítico] → [Seg.5 GCL/Z3/SlotContract
  verifica en cada paso] → handoff a Team Agente (repo 7)
→ [Seg.8 Memoria persiste todo] → [Seg.9 Recovery si falla]
→ Output final + [Seg.10 Router entrega vía API]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{
  "_checkpoint": {"doc":"MAPA_MD_ORQUESTADOR","version":"1.0",
    "fecha":"2026-07-05","fuente_de_verdad":true},
  "segmentos": 10,
  "repos_cubiertos": [1,2,3,4,5,6,7,8,9,10,11,12],
  "para_html": "MAPA_HTML_ORQUESTADOR.html (siguiente archivo)"
}
