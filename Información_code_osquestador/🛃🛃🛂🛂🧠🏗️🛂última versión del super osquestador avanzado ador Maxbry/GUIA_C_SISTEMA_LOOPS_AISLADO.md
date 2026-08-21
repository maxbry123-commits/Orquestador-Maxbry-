# GUÍA INTERNA C — SISTEMA DE LOOPS AISLADO ESCALABLE
# "Esta es la clave del orquestador" — Director, Paso 2 pregunta 5
# Documento de trabajo de Claude — pseudo-código + Python real
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. PRINCIPIO DE DISEÑO (no negociable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El cerebro (Brain Core / MAXBRY Orquestador) NO contiene el
sistema de loops. El cerebro solo LLAMA a este módulo al
arrancar cualquier tarea, pasándole el nivel calculado.

Razón (Director, textual): "debe ser un sistema aislado que
llama el cerebro cuando arranca tanto en el orquestador como
en el agente. Pero al aislarlo podemos mejorarlo con el tiempo."

Esto significa: este módulo vive en su PROPIO repo/carpeta,
con su propio contrato de entrada/salida (usando el "enchufe
universal" — el Universal Module Contract de Opus, ver GUÍA D),
de forma que se puede reemplazar/mejorar sin tocar ni el
Kernel NCT ni el Team Agent.

UBICACIÓN: reasoning/loop_engine/ (raíz separada, NO dentro
de orchestrator/ ni de teams_agents/)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. LOS 4 NIVELES (confirmados por el Director)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIVEL_RAPIDO:    20-50 pasos    (tareas simples, DRE LOW)
NIVEL_BASICO:    100-300 pasos  (tareas medias, DRE MEDIUM)
NIVEL_AVANZADO:  300-800 pasos  (tareas complejas, DRE HIGH)
NIVEL_TURBO:     800-1000 pasos (tareas extremas, DRE EXTREME)

REGLA DE ACTIVACIÓN (Director, textual): "el cerebro debe
activar según si ve poco o mucho resultado y si el trabajo es
muy grande" → esto es DINÁMICO, no solo un cálculo inicial de
DRE. El nivel puede ESCALAR DURANTE la ejecución si el
progreso es insuficiente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. CÓMO SE DECIDE EL NIVEL (inicial + dinámico)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DECISIÓN INICIAL (usa DRE Complexity Estimator, ya en DOC1 [7.1]):
```
score_dre = (deps×2) + steps + (5 si ambiguo) + (5 si riesgo)
score 0-3   → NIVEL_RAPIDO
score 4-8   → NIVEL_BASICO
score 9-15  → NIVEL_AVANZADO
score 16+   → NIVEL_TURBO
```

ESCALADO DINÁMICO (nuevo, resuelve la regla del Director):
```
cada N pasos (checkpoint del loop actual):
    progreso = evidence_sufficiency_score()
    si progreso < umbral_esperado_para_este_punto:
        ESCALAR al siguiente nivel (RAPIDO→BASICO→AVANZADO→TURBO)
        recalcular presupuesto de pasos restantes
    si progreso >> umbral (mucho mejor de lo esperado):
        DESESCALAR (ahorra pasos, cierra antes) — opcional,
        solo si Goal-Stop Check ya confirma objetivo cumplido
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. ESTRUCTURA INTERNA DE CADA NIVEL (fases reutilizadas,
   escaladas por cantidad de pasos, NO por fases distintas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Las MISMAS 9 fases (de FUENTE 7, ya validadas) se usan en
los 4 niveles. Lo que cambia es CUÁNTOS pasos corre cada fase
y CUÁNTAS veces itera, no la fase en sí. Esto es clave para
que sea "un sistema DSL/DAG con Python + JSON" (Director,
Paso 2 pregunta 1) en vez de 4 sistemas distintos hardcodeados.

FASE_0  Inicialización y Constitución
FASE_1  Comprensión / extracción / OCR / normalización
FASE_2  Análisis / descomposición / modelado del problema
FASE_3  Planificación multiobjetivo / generación estrategias
FASE_4  Debate interno / refutaciones / hipótesis alternativas
FASE_5  Verificación / consistencia / contradicciones / pruebas
FASE_6  Optimización / simplificación / fusión / costo-beneficio
FASE_7  Autoevaluación / confianza / incertidumbre / preguntas
FASE_8  Síntesis final / documentación / memoria / cierre

DISTRIBUCIÓN DE PASOS POR NIVEL (proporcional, no fija):
```
NIVEL_RAPIDO (20-50):    ~2-6 pasos por fase, fases 4-5 pueden saltarse
NIVEL_BASICO (100-300):  ~11-33 pasos por fase, todas las fases activas
NIVEL_AVANZADO (300-800):~33-89 pasos por fase, iteración doble en 4-6
NIVEL_TURBO (800-1000):  ~89-111 pasos por fase, iteración triple,
                          Z3+GCL v1.0 activos en cada checkpoint
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. CONTRATO DE ENTRADA/SALIDA (usa el Universal Module
   Contract de Opus — el "enchufe universal")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT al Loop Engine (desde el cerebro O desde Team Agent):
```json
{
  "artifact_id": "reasoning.loop_engine.run",
  "contrato": {"rol": "transform"},
  "consume": {
    "datatype": {"family": "task", "type": "goal_lock", "version": 1},
    "schema_uri": "contracts/task.schema.json"
  },
  "expone": {
    "datatype": {"family": "task", "type": "loop_result", "version": 1},
    "schema_uri": "contracts/loop_result.schema.json"
  }
}
```

PAYLOAD DE ENTRADA (simplificado):
```json
{
  "goal_lock": {...},
  "dre_score": 12,
  "nivel_inicial": "NIVEL_AVANZADO",
  "quien_llama": "orquestador | team_agent",
  "presupuesto_max_pasos": 800,
  "checkpoint_cada_n_pasos": 25
}
```

PAYLOAD DE SALIDA:
```json
{
  "nivel_final_usado": "NIVEL_AVANZADO",
  "escalados_durante_ejecucion": 1,
  "pasos_totales_ejecutados": 412,
  "fases_completadas": ["FASE_0","FASE_1",...,"FASE_8"],
  "resultado": {...},
  "evidence_sufficiency_final": 0.91,
  "checkpoint_refs": ["sha256_1","sha256_2","..."]
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. PYTHON REAL — ESTRUCTURA DEL MÓDULO AISLADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
# reasoning/loop_engine/core.py
from enum import Enum
from dataclasses import dataclass, field

class Nivel(Enum):
    RAPIDO = ("NIVEL_RAPIDO", 20, 50)
    BASICO = ("NIVEL_BASICO", 100, 300)
    AVANZADO = ("NIVEL_AVANZADO", 300, 800)
    TURBO = ("NIVEL_TURBO", 800, 1000)

    def __init__(self, label, min_pasos, max_pasos):
        self.label = label
        self.min_pasos = min_pasos
        self.max_pasos = max_pasos

def nivel_desde_dre(score: int) -> Nivel:
    if score <= 3: return Nivel.RAPIDO
    if score <= 8: return Nivel.BASICO
    if score <= 15: return Nivel.AVANZADO
    return Nivel.TURBO

FASES = ["FASE_0","FASE_1","FASE_2","FASE_3","FASE_4",
         "FASE_5","FASE_6","FASE_7","FASE_8"]

@dataclass
class LoopState:
    nivel_actual: Nivel
    paso_actual: int = 0
    fase_actual_idx: int = 0
    escalados: int = 0
    checkpoints: list = field(default_factory=list)

def evidence_sufficiency(loop_state: LoopState, contexto: dict) -> float:
    """Reusa la fórmula ya definida en DOC1 [1.2]/[7.3]."""
    return (0.35 * contexto.get("coverage", 0) +
            0.25 * contexto.get("consistency", 0) +
            0.20 * contexto.get("diversity", 0) +
            0.20 * contexto.get("recency", 0))

def debe_escalar(loop_state: LoopState, contexto: dict, umbral: float = 0.6) -> bool:
    progreso_esperado = loop_state.paso_actual / loop_state.nivel_actual.max_pasos
    progreso_real = evidence_sufficiency(loop_state, contexto)
    return progreso_real < (progreso_esperado * umbral)

def escalar(nivel: Nivel) -> Nivel:
    orden = [Nivel.RAPIDO, Nivel.BASICO, Nivel.AVANZADO, Nivel.TURBO]
    idx = orden.index(nivel)
    return orden[min(idx + 1, len(orden) - 1)]

async def run_loop_engine(goal_lock: dict, dre_score: int,
                            checkpoint_cada_n: int = 25) -> dict:
    """Punto de entrada único. Llamado por Orquestador O Team Agent."""
    nivel = nivel_desde_dre(dre_score)
    state = LoopState(nivel_actual=nivel)

    for fase_idx, fase in enumerate(FASES):
        state.fase_actual_idx = fase_idx
        pasos_fase = state.nivel_actual.max_pasos // len(FASES)

        for paso in range(pasos_fase):
            state.paso_actual += 1
            await ejecutar_paso_de_fase(fase, state, goal_lock)

            if state.paso_actual % checkpoint_cada_n == 0:
                contexto = await recolectar_contexto(state)
                state.checkpoints.append(guardar_checkpoint(state))

                if debe_escalar(state, contexto):
                    state.nivel_actual = escalar(state.nivel_actual)
                    state.escalados += 1

                if goal_stop_check(state, contexto):
                    return finalizar_loop(state, motivo="goal_cumplido")

    return finalizar_loop(state, motivo="pasos_agotados")

def goal_stop_check(state: LoopState, contexto: dict) -> bool:
    """Ya definido en DOC1 [7.1] Goal-Stop Check P9.5 — reutilizado."""
    return evidence_sufficiency(state, contexto) >= 0.85

def finalizar_loop(state: LoopState, motivo: str) -> dict:
    return {
        "nivel_final_usado": state.nivel_actual.label,
        "escalados_durante_ejecucion": state.escalados,
        "pasos_totales_ejecutados": state.paso_actual,
        "motivo_cierre": motivo,
        "checkpoint_refs": state.checkpoints,
    }
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. CÓMO LO LLAMAN EL ORQUESTADOR Y EL TEAM AGENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESDE EL ORQUESTADOR (DOC1, tras [7.1] Mythos GoalLock):
```python
from reasoning.loop_engine.core import run_loop_engine

resultado = await run_loop_engine(
    goal_lock=oc.goal_lock,
    dre_score=oc.dre_score,
    checkpoint_cada_n=25
)
# el orquestador usa resultado["resultado"] para continuar a [8] Planner
```

DESDE EL TEAM AGENT (DOC2, tras AG1.02 análisis y consenso):
```python
from reasoning.loop_engine.core import run_loop_engine

resultado = await run_loop_engine(
    goal_lock=sub_objetivo_del_enjambre,
    dre_score=dre_local_del_enjambre,
    checkpoint_cada_n=10  # Team Agent usa checkpoints más frecuentes
)
```

MISMA LIBRERÍA, MISMO CONTRATO, DOS LLAMADORES DISTINTOS.
Esto es exactamente lo que significa "aislado" — ni el
Orquestador ni el Team Agent conocen el interior del loop,
solo llaman a run_loop_engine() con su goal_lock y dre_score.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. RELACIÓN CON "1000 LOOPS" DE FUENTE 8 (si_o_si_Maxbry)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El documento fuente 8 describía 1000 loops en 9 fases con
nombres específicos de rango (Loop 0, Loops 1-50, 51-150,
151-300, 301-500, 501-700, 701-850, 851-950, 951-1000).
Esto SE FUSIONA aquí exactamente como NIVEL_TURBO: las 9
fases de la sección 4 de esta guía SON esas mismas 9 fases,
solo que ahora son reutilizables en los 4 niveles en vez de
ser exclusivas de "1000 loops". Los rangos de la fuente 8
mapean así:
```
Loop 0            → FASE_0 (siempre 1 paso, constitución)
Loops 1-50/150     → FASE_1 (proporcional al nivel)
Loops 51-300       → FASE_2
Loops 151-500       → FASE_3
Loops 301-700       → FASE_4 (debate/refutación)
Loops 501-850       → FASE_5 (verificación)
Loops 701-950       → FASE_6 (optimización)
Loops 851-1000      → FASE_7+FASE_8 (autoevaluación+síntesis)
```
NO se construye un sistema paralelo de "1000 loops" — es
NIVEL_TURBO de este mismo módulo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA C
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_C_SISTEMA_LOOPS_AISLADO","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno","fuente_de_verdad":true,
    "importancia":"MAXIMA - Director la marco como LA CLAVE del orquestador"},
  "principio": "aislado_del_cerebro, llamado por Orquestador Y Team Agent",
  "ubicacion": "reasoning/loop_engine/ (raiz separada)",
  "niveles": {
    "RAPIDO": {"pasos":"20-50","dre":"0-3"},
    "BASICO": {"pasos":"100-300","dre":"4-8"},
    "AVANZADO": {"pasos":"300-800","dre":"9-15"},
    "TURBO": {"pasos":"800-1000","dre":"16+"}
  },
  "escalado_dinamico": "activo, basado en evidence_sufficiency vs progreso esperado",
  "fases_reutilizables": 9,
  "contrato": "usa Universal Module Contract (enchufe Opus)",
  "llamadores": ["orquestador (tras Mythos GoalLock)", "team_agent (tras consenso AG1.02)"],
  "fusion_1000_loops_fuente8": "es NIVEL_TURBO, no sistema paralelo",
  "siguiente_documento": "GUIA_D_ESTRUCTURA_REPOS_EXPANDIDA"
}
