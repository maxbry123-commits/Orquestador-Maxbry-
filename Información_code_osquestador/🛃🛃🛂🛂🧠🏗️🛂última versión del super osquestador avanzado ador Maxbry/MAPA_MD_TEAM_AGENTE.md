# MAPA SEGMENTADO — TEAM AGENTE (sub-orquestador)
# Toda la raíz, cerrado, para visualizar y decidir cambios futuros
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUÉ ES EL TEAM AGENTE (1 frase)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sub-orquestador que recibe órdenes del MAXBRY Orquestador,
NUNCA ve el cerebro, y coordina un STAFF de agentes de código
externos (Open Claw, Open Code, Open Hand, Claude Code, Mimo
Code) trabajando en paralelo. Solo crea micro-agentes propios
si el staff no cubre la capability requerida.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 1 — CEREBRO PEQUEÑO (repo 7: team-agente-cerebro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
core.py               ≤100 LOC, recibe orden de MAXBRY Orquestador
pipeline_selector.py  ≤80 LOC, elige pipeline por capability match
multitask_scheduler   ≤120 LOC, asyncio.gather() multitarea real
staff_registry.json   mapea capability→agente externo disponible
TOTAL: ≤300 LOC — inspirado en el Orquestador pero minúsculo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 2 — PIPELINES INTERCAMBIABLES (repo 7)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pipeline_code_gen.py   usa staff: Claude Code / Open Code
pipeline_research.py   usa staff: agentes de investigación
pipeline_refactor.py   usa staff: Aider / Open Claw
pipeline_generic.py    fallback: construye micro-agente MA-*
Cada pipeline = 1 método de trabajo intercambiable sin tocar
el cerebro (Segmento 1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 3 — STAFF DE AGENTES EXTERNOS (referencia, viven
fuera del repo, Team Agente solo los conecta)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Open Claw   Open Code   Open Hand
Claude Code (instancia del STAFF, distinta a la del Sentinela)
Mimo Code   (ídem)
Aider       Codex
Todos ejecutan en PARALELO cuando la tarea lo permite.
Team Agente NO necesita saber programar — solo enruta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 4 — MICRO-AGENTES PROPIOS (repo 8, condicional)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Regla de creación:
  SI capability YA está en staff_registry → usar staff
  SI NO está → construir micro-agente DSL/DAG (90%code/10%LLM)
15 micro-agentes ya definidos (MA-CODE-GEN...MA-RUNTIME-CHECK)
Tipo SmolAgent pero MÁS determinista, NUNCA solo-prompt
Regla: spawn→run→emit JSON→die, ≤200 LOC c/u

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 5 — ESCRITOR + RUNTIME (repo 9)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LLM_ESCRITOR  único que genera código, 7 estados, nunca
              declara "funciona/listo", propone bajo control
BUILDER       escribe archivo físico, instala deps
VALIDATOR     L1_static (lint+imports+schema+no_mock)
WITNESS       L2_build+L3_runtime+L4_feature, evidence_hash
              único que puede decir "funciona" — con prueba

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 6 — LOOP ENGINE (mismo módulo del Orquestador,
repo 3, reutilizado — NO duplicado)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Team Agente llama run_loop_engine() tras su propio consenso
(AG1.02), con checkpoint_cada_n=10 (más frecuente que el
Orquestador, porque trabaja sub-objetivos más pequeños)
Multitarea real: cada sub-tarea del enjambre puede llamar su
propia instancia del Loop Engine en paralelo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 7 — ENJAMBRE / TEAM AGENT ORIGINAL (DOC2, 26 secc.)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7 goals, DAG con parallel_groups, simulación 5x antes de
ejecutar, validación 3 capas (MA-VERIFY-3CAPAS), 12 preguntas
de objetivos, hipótesis+refutación (Devil Agent), memoria
continua 4 tiers, formato salida estructurada firmado

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 8 — PLAN AGENT (complementario, DOC2 AG2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Separa PENSAMIENTO de EJECUCIÓN. Diseña y firma el plan
ANTES de que Team Agente ejecute nada. Sin Plan Agent
aprobado → Team Agente no inicia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 9 — CONEXIÓN CON EL CEREBRO (línea de autoridad)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAXBRY Orquestador → (handoff_package firmado SHA256) →
Team Agente → ejecuta → (resultado firmado) → MAXBRY Orquestador
Team Agente JAMÁS lee orquestador-nucleo/ ni contracts-schemas/
directamente — solo recibe el payload ya validado por GCL/SC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGMENTO 10 — SENTINELA MEJORA ESTE AGENTE (no lo construye)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sentinela (repo 15, ver GUÍA E) puede modificar:
  ✅ pipelines/*.py (Segmento 2)
  ✅ staff_registry.json (Segmento 3, ajustar prioridades)
NO puede modificar: core.py del cerebro pequeño (Segmento 1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLUJO COMPLETO EN 1 VISTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Orden MAXBRY → [Seg.1 cerebro decide pipeline] →
[Seg.7 DAG+simulación 5x] → [Seg.2 pipeline elegido] →
¿capability en staff? SÍ→[Seg.3 staff ejecuta paralelo]
                      NO→[Seg.4 crea micro-agente]
→ [Seg.5 Escritor+Runtime valida código real] →
[Seg.6 Loop Engine si necesita razonamiento profundo] →
[Seg.8 Plan Agent ya aprobó antes de empezar] →
resultado firmado → [Seg.9 vuelve a MAXBRY Orquestador]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{
  "_checkpoint": {"doc":"MAPA_MD_TEAM_AGENTE","version":"1.0",
    "fecha":"2026-07-05","fuente_de_verdad":true},
  "segmentos": 10,
  "repos_cubiertos": [3,7,8,9],
  "para_html": "MAPA_HTML_TEAM_AGENTE.html (siguiente archivo)"
}
