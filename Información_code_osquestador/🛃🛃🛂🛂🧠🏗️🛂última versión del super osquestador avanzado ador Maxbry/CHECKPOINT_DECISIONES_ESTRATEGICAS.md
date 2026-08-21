# CHECKPOINT — DECISIONES ESTRATÉGICAS v1
# Fuente de verdad — respuestas del Director al PASO 1
# Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JERARQUÍA DE 4 NIVELES (confirmada, definitiva)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIVEL A — MAXBRY AGI
  Software de razonamiento avanzado (hecho con Opus)
  Nivel más alto, controla a MAXBRY Orquestador (futuro)

NIVEL B — MAXBRY ORQUESTADOR (= nuestro Kernel NCT, en construcción)
  Controlado en el futuro por MAXBRY AGI
  Controla a TEAM Agente

NIVEL C — TEAM AGENTE (sub-orquestador)
  Staff de agentes de código: Open Claw, Open Code, Open Hand,
  Claude Code, Mimo Code — trabajan en paralelo
  TEAM Agente NO necesita saber de código, solo ejecuta/coordina
  Crea micro-agentes DSL/DAG (90% code/10% LLM) SOLO si:
    a) la tarea lo requiere Y
    b) no hay ya un agente de staff con esa capability

NIVEL D — SENTINELA (nuevo módulo, no existía)
  Mini-agente de funciones básicas: vigila desempeño/resultados,
  analiza, evalúa, planifica mejora, diseña
  Tiene copia DEDICADA de Claude Code + Mimo Code (separada del staff)
  NUNCA modifica el cerebro base (ni Orquestador ni Team Agent)
  SOLO mejora: método de trabajo, desempeño, pipelines
  Puede mejorar tanto al Orquestador como al Team Agent
    (siempre a nivel de método/desempeño, nunca el cerebro)
  Presenta cambios al Director antes de aplicar — requiere aprobación

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SISTEMA DE PASOS ESCALABLE (reemplaza escala fija DRE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIVEL_RAPIDO:    20-50 pasos
NIVEL_BASICO:    100-300 pasos
NIVEL_AVANZADO:  300-800 pasos
NIVEL_TURBO:     800-1000 pasos

Implementación: PIPELINE DSL+DAG con preguntas integradas,
código Python + doble lenguaje + JSON (recomendación Opus)
→ reduce programación real vs. escribir cada paso a mano

INTEGRACIÓN CON EXISTENTE:
MYTHOS = sistema de razonamiento (el "qué" pensar)
Sistema de loops = método de trabajo continuo para cadenas
                   extensas (el "cómo" sostenerlo en el tiempo)
NO se reemplazan entre sí — MYTHOS corre DENTRO de cada loop
del nivel que corresponda según DRE Complexity Estimator.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEAM AGENTE — REDISEÑO CONFIRMADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- NO es un "super agente" monolítico de 200-500 LOC
- Cerebro pequeño determinista (inspirado en el Orquestador)
  con diferentes PIPELINES para ejecutar métodos de trabajo
- Debe poder trabajar múltiples tareas simultáneas en modo
  loops/bucles (paralelismo real, no solo secuencial)
- Micro-agentes MA-* (los 15 ya definidos en DOC2+GRUPO_F)
  COMPLEMENTAN a los agentes de staff externos, no los reemplazan
- Regla de creación de micro-agente nuevo:
  IF capability_requerida NOT IN staff_agents_disponibles
  THEN Team Agent construye micro-agente DSL/DAG
  ELSE usa el agente de staff ya disponible

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NUEVO REPO SEPARADO — WORKSPACES DE PROYECTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Repo adicional (NO dentro de las 13 raíces del Kernel):
Contiene los documentos de los proyectos que el orquestador
ejecuta (tareas del usuario) — workspace por proyecto con
su propia carpeta, memoria, docs, siguiendo el patrón de
Workspace Orchestration (Workspace Manager + Git Manager +
Document Agent + Knowledge Agent, ya visto en modo recepción)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CEREBRO MÍNIMO (microkernel puro) — CONFIRMADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Decisión: dejar el cerebro (Brain Core) al mínimo posible.
Razón del Director: permite modificar más el orquestador
teniendo una hoja de rutas separada.

PENDIENTE DE ENTREGA (pedido explícito, punto 10):
1. Documento MD segmentado: TODA la raíz del Kernel Orquestador
2. Documento MD segmentado: TODA la raíz del Team Agente
3. 1 HTML visual del Orquestador (mapa navegable)
4. 1 HTML visual del Team Agente (mapa navegable)
Esto se construye DESPUÉS de leer el documento de Opus
("enchufe universal") en la bandeja del proyecto — Paso 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGLA DE APORTE (autorización del Director)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Claude puede añadir cualquier mejora que considere valiosa.
Si detecta algo que NO aporta, genera conflicto o es
redundante → lo señala explícitamente al Director en vez
de omitirlo silenciosamente. El Director decide eliminar/aprobar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOCUMENTO PENDIENTE DE LOCALIZAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Enchufe universal" = documento hecho por Opus en la bandeja
del proyecto (JSON/DSL MAXBRY/YAIWES/NCT). Se lee en Paso 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"DECISIONES_ESTRATEGICAS_v1","fecha":"2026-07-05","fuente_de_verdad":true},
  "jerarquia_4_niveles": {
    "A_maxbry_agi": "razonamiento avanzado, hecho con Opus, futuro controlador",
    "B_maxbry_orquestador": "Kernel NCT en construccion, controla Team Agente",
    "C_team_agente": "sub-orquestador, staff agentes codigo externos",
    "D_sentinela": "nuevo, auto-repara metodo/desempeno, nunca el cerebro"
  },
  "escala_pasos": {"rapido":"20-50","basico":"100-300","avanzado":"300-800","turbo":"800-1000"},
  "implementacion_escala": "PIPELINE DSL+DAG + Python + JSON, no hardcode",
  "mythos_vs_loops": "MYTHOS=razonamiento, Loops=sostenimiento continuo, se integran",
  "team_agente_rediseno": {
    "cerebro_pequeno_determinista": true,
    "multiples_pipelines_metodos_trabajo": true,
    "multitarea_paralela_loops": true,
    "micro_agentes_solo_si_falta_capability_en_staff": true
  },
  "sentinela_nuevo_modulo": {
    "vigila_analiza_evalua_planifica_disena": true,
    "usa_claude_code_mimo_code_dedicado": true,
    "nunca_modifica_cerebro": true,
    "mejora_orquestador_y_team_agente_metodo_desempeno": true,
    "requiere_aprobacion_director_antes_aplicar": true
  },
  "repo_workspaces_separado": true,
  "cerebro_minimo_microkernel": true,
  "pendiente_entregar": ["MD_segmentado_orquestador","MD_segmentado_team_agente",
                          "HTML_orquestador","HTML_team_agente"],
  "documento_opus_pendiente_leer": "enchufe_universal_bandeja_proyecto",
  "siguiente_paso": "PASO_2 leer documentos bandeja proyecto"
}
