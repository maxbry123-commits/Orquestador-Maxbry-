# GUÍA INTERNA E — SENTINELA (módulo nuevo)
# Nivel D de la jerarquía (ver GUÍA A)
# Versión: 1.0 | Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. DEFINICIÓN (respuestas 4-6 del Paso 1, textuales)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"mini agente con funciones muy básicas: vigila el desempeño
y los resultados, analiza, evalúa, planifica mejora y diseña.
Usa Claude Code y Mimo Code para la tarea. Nunca modifica el
cerebro base, solo el desempeño, el método de trabajo. También
puede mejorar al Team Agente pero no el cerebro, solo mejora
el método de trabajo, el desempeño."

REGLA ABSOLUTA: Sentinela tiene su PROPIA copia instalada de
Claude Code + Mimo Code, separada del staff que usa el Team
Agente. No comparte instancias — así nunca compite por
recursos ni se mezcla su trabajo con tareas del usuario.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. QUÉ PUEDE Y QUÉ NO PUEDE TOCAR (línea roja exacta)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PUEDE MODIFICAR (método/desempeño):
✅ policies/gcl_rules.yaml (ajustar umbrales de reglas)
✅ reasoning/loop_engine/niveles.py (ajustar rangos de pasos)
✅ team-agente-cerebro/pipelines/*.py (mejorar un pipeline)
✅ api-router/config/capability.json (ajustar reglas de routing)
✅ Cualquier archivo de configuración (.yaml/.json) de
   comportamiento, NUNCA de identidad/leyes

NO PUEDE MODIFICAR (cerebro/identidad, línea roja absoluta):
❌ orquestador-nucleo/adn/ (las 14 reglas, inmutables)
❌ orquestador-nucleo/guardian/ (los 6 checks)
❌ orquestador-nucleo/llm_juez/ (el pipeline P-DISCOVER..P13)
❌ contracts-schemas/ (el Universal Module Contract)
❌ Cualquier archivo marcado INMUTABLE en su header
   (ver regla de header obligatorio de GRUPO_H sección 3)

VERIFICACIÓN AUTOMÁTICA: antes de cualquier cambio, Sentinela
consulta GUARDIAN_LAYER (el mismo de DOC1 [A2]) con la
pregunta "¿este archivo pertenece a orquestador-nucleo o
contracts-schemas?" → si SÍ, RECHAZA automáticamente sin
llegar siquiera a proponer el cambio al Director.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. FLUJO COMPLETO DEL SENTINELA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
[1] VIGILAR (continuo, cron cada 1h — reusa NIVEL 6 de
    FUENTE 7 "self-improvement loop")
    │
    ▼
[2] ANALIZAR
    Lee métricas: QUALITY_SCORE, EFFICIENCY_SCORE,
    RELIABILITY_SCORE (ya definidas en DOC1 [30.3])
    de Orquestador Y de Team Agente por separado
    │
    ▼
[3] EVALUAR
    ¿Hay degradación sostenida en 3+ ciclos?
    ¿Hay un patrón de fallo repetido en Failure Registry?
    Si NO → vuelve a [1] (nada que hacer)
    Si SÍ → continúa a [4]
    │
    ▼
[4] PLANIFICAR MEJORA
    Genera hipótesis de causa raíz (Root Cause Analysis,
    mismo patrón RM-03 del LLM_ESCRITOR en GRUPO_F)
    │
    ▼
[5] DISEÑAR
    Propone el cambio concreto (diff de archivo, NO el
    cerebro — verificado contra la línea roja de sección 2)
    │
    ▼
[6] INVESTIGAR (RAG + web, mismo patrón MA-RESEARCH-WEB)
    Busca: cómo otros orquestadores resolvieron patrones
    similares, si hay librerías/técnicas mejores disponibles
    │
    ▼
[7] CONSTRUIR EN SANDBOX
    Usa SU copia dedicada de Claude Code + Mimo Code
    (nunca la del staff del Team Agent)
    Construye el cambio en una rama improve/* aislada
    │
    ▼
[8] PROBAR
    Corre el mismo test suite del módulo afectado
    Compara resultado nuevo vs baseline (3 métricas)
    │
    ▼
[9] PRESENTAR AL DIRECTOR
    NUNCA aplica solo. Presenta: qué detectó, qué propone,
    resultado del sandbox, diff exacto
    │
    ▼
[10] ESPERAR APROBACIÓN
    APPROVED → merge a main
    REJECTED → descarta, registra por qué en su propia memoria
               (para no repetir la misma propuesta rechazada)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. PYTHON REAL — ESTRUCTURA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```python
# sentinela/core.py
from enum import Enum

class LineaRoja(Enum):
    """Archivos que Sentinela NUNCA puede tocar."""
    PROHIBIDO = [
        "orquestador-nucleo/adn/",
        "orquestador-nucleo/guardian/",
        "orquestador-nucleo/llm_juez/",
        "contracts-schemas/",
    ]

def es_modificable(ruta_archivo: str) -> bool:
    """Consulta GUARDIAN_LAYER antes de proponer cualquier cambio."""
    for prohibido in LineaRoja.PROHIBIDO.value:
        if ruta_archivo.startswith(prohibido):
            return False
    # también rechaza si el header dice INMUTABLE
    if archivo_tiene_header_inmutable(ruta_archivo):
        return False
    return True

async def ciclo_sentinela():
    """Se ejecuta cada 1h (cron), reusa self_improvement de DOC1."""
    metricas_orq = leer_metricas("orquestador")
    metricas_ta = leer_metricas("team_agente")

    for objetivo, metricas in [("orquestador", metricas_orq),
                                ("team_agente", metricas_ta)]:
        if detectar_degradacion(metricas, ventana_ciclos=3):
            hipotesis = analizar_causa_raiz(metricas)
            propuesta = disenar_mejora(hipotesis, objetivo)

            if not es_modificable(propuesta.ruta_archivo):
                registrar_rechazo_automatico(propuesta, razon="linea_roja")
                continue

            evidencia_previa = investigar_rag_web(hipotesis)
            resultado_sandbox = await construir_y_probar_en_sandbox(
                propuesta, evidencia_previa,
                agente_dedicado="sentinela_claude_code"  # copia separada
            )

            if resultado_sandbox.mejora_confirmada:
                presentar_al_director(propuesta, resultado_sandbox)
                # espera aprobación — NUNCA aplica solo
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. UBICACIÓN Y AISLAMIENTO DE RECURSOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NUEVO REPO (15º, añadido a GUÍA D):
```
sentinela/
├── core.py
├── vigilancia/
│   ├── metricas_reader.py
│   └── degradacion_detector.py
├── analisis/
│   └── root_cause_analysis.py
├── diseno/
│   └── propuesta_builder.py
├── sandbox/
│   ├── sandbox_runner.py
│   └── agentes_dedicados/       # Claude Code + Mimo Code
│       ├── claude_code_sentinela/  # instalación SEPARADA
│       └── mimo_code_sentinela/    # instalación SEPARADA
├── memoria_propia/
│   └── rechazos_previos.jsonl   # no repetir propuestas rechazadas
└── linea_roja.py                # consulta GUARDIAN_LAYER
```

RAZÓN DEL AISLAMIENTO DE AGENTES: si Sentinela usara la misma
instancia de Claude Code que el Team Agent, una tarea de
auto-mejora podría competir por tokens/tiempo con una tarea
real del usuario. Instancias separadas = 0 interferencia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — GUÍA E
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {"doc":"GUIA_E_SENTINELA","version":"1.0",
    "fecha":"2026-07-05","tipo":"documento_interno","fuente_de_verdad":true},
  "nivel_jerarquia": "D (ver GUIA_A)",
  "puede_modificar": ["gcl_rules.yaml","loop_engine/niveles.py",
    "team_agente/pipelines/*","router/capability.json"],
  "no_puede_modificar": ["orquestador-nucleo/adn","guardian",
    "llm_juez","contracts-schemas","archivos_header_INMUTABLE"],
  "agentes_dedicados": "copia separada Claude Code + Mimo Code, nunca comparte con staff Team Agent",
  "requiere_aprobacion_director": true,
  "repo_nuevo": "sentinela/ (15o repo, añadir a GUIA_D)",
  "flujo_pasos": 10,
  "siguiente_documento": "GUIA_F_MD_HTML_SEGMENTADO"
}
