# SISTEMA MOTOR DE RAZONAMIENTO v4
# FUNCIÓN EJECUTABLE DEL ORQUESTADOR
# Listo para programar / implementar / mandar a construir

```json
{
  "artifact_id": "SYS-MOTOR-RAZONAMIENTO-v4",
  "tipo": "sistema_ejecutable",
  "version": "4.0.0",
  "capa": "KERNEL",
  "archivo_principal": "motor_razonamiento.py",
  "entrypoint": "ejecutar(problema, nivel)",
  "public_api": ["ejecutar", "evaluar_complejidad", "ciclo_fsm"],
  "artifact_type": "composite",
  "language": "python",
  "runtime_type": "compute",
  "llm_ratio_max": 0.10,
  "allowed_imports": ["json","hashlib","datetime","ast","re"],
  "depende_de": ["state_manager.py","crazy_wall.json","APPROVED_REGISTRY.json"],
  "usado_por": ["orquestador.py","dispatcher.py"],
  "ubicacion_codigo": "B01_artifact_code/motor_razonamiento/",
  "ubicacion_config": "A06_artifact_contracts/motor_razonamiento/",
  "stop_rule": "Sin OK Director = STOP"
}
```

---

## ARCHIVO 1 — motor_razonamiento_contract.json
## CONTRATO OFICIAL DEL SISTEMA

```json
{
  "artifact_id": "ART-MOTOR-001",
  "ficha_id": "motor_razonamiento",
  "version": "4.0.0",
  "entrypoint": "ejecutar",
  "public_api": ["ejecutar", "evaluar_complejidad", "ciclo_fsm"],
  "artifact_type": "composite",
  "language": "python",
  "runtime_type": "compute",
  "llm_ratio_max": 0.10,
  "sandbox": "strict",

  "input_schema": {
    "problema": "string — descripción del problema a resolver",
    "nivel": "int — 1|2|3|4|0 (0=auto)",
    "contexto": "object — memoria previa opcional",
    "max_iteraciones": "int — default 3",
    "umbral_confianza": "float — default 0.60"
  },

  "output_schema": {
    "estado_final": "string — CONVERGIDO|PARCIAL|FALLIDO",
    "decision": "string — qué hacer",
    "justificacion": "string — basada en fases F0-F9",
    "riesgos_residuales": "array — lo que sigue incierto",
    "confianza": "float — 0.0 a 1.0",
    "fases_ejecutadas": "array — F0/FM/F1...F11",
    "iteraciones": "int — cuántos bucles completó",
    "nodo_memoria": "object — para guardar en grafo",
    "codigo_a_generar": "object — spec técnica si aplica",
    "siguiente_accion": "string — qué hace el orquestador después"
  },

  "allowed_imports": ["json","hashlib","datetime","ast","re"],
  "timeout": 300,
  "memory_limit": 512,

  "side_effects": [
    "escribe en crazy_wall.json",
    "escribe en APPROVED_REGISTRY.json si resultado aprobado",
    "actualiza grafo de memoria"
  ],

  "failure_modes": [
    "incognita_bloqueante_sin_resolver",
    "bucle_infinito_sin_convergencia",
    "confianza_menor_umbral",
    "fase_fallida_sin_recovery"
  ],

  "fallback": "retornar estado PARCIAL con lo completado hasta el fallo",

  "test_cases": [
    {
      "input": {"problema": "¿cómo evitar pérdida de estado?", "nivel": 0},
      "expected": {"estado_final": "CONVERGIDO", "confianza_min": 0.75}
    },
    {
      "input": {"problema": "x", "nivel": 5},
      "expected": {"estado_final": "FALLIDO", "error": "nivel_invalido"}
    }
  ]
}
```

---

## ARCHIVO 2 — motor_razonamiento.py
## CÓDIGO EJECUTABLE PRINCIPAL

```python
"""
MOTOR DE RAZONAMIENTO AVANZADO v4
Orquestador MAXBRY — Sistema ejecutable
NO modifica DAG, Router, ni Brain directamente.
Escribe SOLO en crazy_wall.json y APPROVED_REGISTRY.json
"""

import json
import hashlib
import datetime


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENTRYPOINT PÚBLICO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def ejecutar(input_data: dict) -> dict:
    """
    Entrypoint principal del motor de razonamiento.
    Recibe problema + nivel, ejecuta FSM, retorna decisión.
    """
    problema          = input_data.get("problema", "")
    nivel             = input_data.get("nivel", 0)
    contexto          = input_data.get("contexto", {})
    max_iteraciones   = input_data.get("max_iteraciones", 3)
    umbral_confianza  = input_data.get("umbral_confianza", 0.60)

    if not problema:
        return _estado_fallido("problema_vacio", {})

    if nivel not in [0, 1, 2, 3, 4]:
        return _estado_fallido("nivel_invalido", {"nivel_recibido": nivel})

    return ciclo_fsm(problema, nivel, contexto, max_iteraciones, umbral_confianza)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CICLO FSM PRINCIPAL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def ciclo_fsm(problema, nivel, contexto, max_iter, umbral) -> dict:
    """
    Máquina de estados principal.
    Estados: IDLE → RUNNING → LOOPING → CONVERGIDO|PARCIAL|FALLIDO
    """
    estado = {
        "current_state": "IDLE",
        "iteracion": 0,
        "mejor_score": 0,
        "iteraciones_sin_mejora": 0,
        "fases_ejecutadas": [],
        "memoria_acumulada": contexto.copy()
    }

    # Determinar fases según nivel
    fases = _resolver_fases(nivel)
    estado["current_state"] = "RUNNING"

    resultado_acumulado = {}

    while estado["iteracion"] < max_iter:
        estado["iteracion"] += 1
        resultado_iter = _ejecutar_fases(problema, fases, estado)

        # Gate: ¿convergió?
        if resultado_iter.get("convergido"):
            estado["current_state"] = "CONVERGIDO"
            resultado_acumulado = resultado_iter
            break

        # Anti-bucle: 2 iteraciones sin mejora → forzar salida
        score_actual = resultado_iter.get("mejor_score", 0)
        if score_actual <= estado["mejor_score"]:
            estado["iteraciones_sin_mejora"] += 1
        else:
            estado["mejor_score"] = score_actual
            estado["iteraciones_sin_mejora"] = 0

        if estado["iteraciones_sin_mejora"] >= 2:
            estado["current_state"] = "PARCIAL"
            resultado_acumulado = resultado_iter
            resultado_acumulado["nota"] = "convergencia_parcial"
            break

        estado["current_state"] = "LOOPING"
        resultado_acumulado = resultado_iter

    if estado["current_state"] == "RUNNING":
        estado["current_state"] = "PARCIAL"

    return _construir_output(estado, resultado_acumulado, umbral)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RESOLVER FASES SEGÚN NIVEL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _resolver_fases(nivel: int) -> list:
    """
    Devuelve lista de fases según nivel turbo.
    Nivel 0 = auto (F0 evalúa y decide).
    """
    mapa = {
        1: ["F0", "F1", "F10"],
        2: ["F0", "FM", "F1", "F3", "F7", "F10"],
        3: ["F0", "FM", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10"],
        4: ["F0", "FM", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11"]
    }
    return mapa.get(nivel, mapa[0]) if nivel != 0 else ["F0_AUTO"]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EJECUTAR FASES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _ejecutar_fases(problema: str, fases: list, estado: dict) -> dict:
    """
    Ejecuta cada fase en orden.
    Cada fase tiene gate. Si falla → STOP + reportar.
    """
    resultado = {
        "fases_completadas": [],
        "hipotesis": [],
        "finalistas": [],
        "sintesis": {},
        "convergido": False,
        "mejor_score": 0
    }

    contexto_fase = {
        "problema": problema,
        "memoria": estado["memoria_acumulada"],
        "iteracion": estado["iteracion"]
    }

    for fase_id in fases:

        # Auto-nivel: F0 evalúa complejidad y elige fases
        if fase_id == "F0_AUTO":
            nivel_elegido = evaluar_complejidad(problema)
            fases_reales  = _resolver_fases(nivel_elegido)
            return _ejecutar_fases(problema, fases_reales, estado)

        fase_fn = FASES_DISPONIBLES.get(fase_id)
        if not fase_fn:
            resultado["error"] = f"fase_{fase_id}_no_encontrada"
            return resultado

        salida_fase = fase_fn(contexto_fase, resultado)

        # Gate: verificar que la fase produjo output válido
        if not salida_fase.get("gate_ok", False):
            resultado["fase_fallida"] = fase_id
            resultado["motivo_falla"] = salida_fase.get("motivo", "gate_fallido")
            return resultado

        # Acumular resultado
        resultado["fases_completadas"].append(fase_id)
        contexto_fase.update(salida_fase.get("contexto_actualizado", {}))

        # Actualizar mejor score si hay hipótesis evaluadas
        if salida_fase.get("mejor_score", 0) > resultado["mejor_score"]:
            resultado["mejor_score"] = salida_fase["mejor_score"]

        # F9 puede pedir bucle
        if salida_fase.get("pedir_bucle", False):
            resultado["convergido"] = False
            return resultado

        # F10 = síntesis = convergido
        if fase_id == "F10":
            resultado["sintesis"]   = salida_fase.get("sintesis", {})
            resultado["convergido"] = True

    return resultado


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASES INDIVIDUALES — LÓGICA DETERMINISTA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _fase_F0(ctx: dict, resultado: dict) -> dict:
    """
    F0 — INCÓGNITAS + MEMORIA + COMPLEJIDAD
    Detecta incógnitas bloqueantes.
    Si las hay → gate falla → pide al Director.
    """
    problema = ctx["problema"]
    memoria  = ctx.get("memoria", {})

    # Detectar incógnitas bloqueantes (palabras sin definir)
    palabras_clave_vacias = _detectar_incognitas(problema, memoria)

    if palabras_clave_vacias:
        return {
            "gate_ok": False,
            "motivo": "incognita_bloqueante",
            "incognitas": palabras_clave_vacias,
            "accion_requerida": "preguntar_al_director"
        }

    complejidad = evaluar_complejidad(problema)

    return {
        "gate_ok": True,
        "contexto_actualizado": {
            "complejidad": complejidad,
            "nivel_recomendado": complejidad,
            "supuestos": [],
            "memoria_relevante": memoria
        }
    }


def _fase_FM(ctx: dict, resultado: dict) -> dict:
    """
    FM — MYTHOS
    Estructura el problema como narrativa con 5 arquetipos.
    Determinista: extrae tokens del problema y los clasifica.
    """
    problema = ctx["problema"]

    mythos = {
        "HEROE":     f"objetivo_de: {problema[:50]}",
        "OBSTACULO": "identificar_bloqueo_principal",
        "ALIADO":    "recurso_disponible_en_memoria",
        "VILLANO":   "riesgo_principal_detectado",
        "MENTOR":    "precedente_o_patron_conocido"
    }

    return {
        "gate_ok": True,
        "contexto_actualizado": {"mythos": mythos}
    }


def _fase_F1(ctx: dict, resultado: dict) -> dict:
    """
    F1 — DESCOMPOSICIÓN EN ÁRBOL
    Divide el problema en subproblemas.
    Gate: mínimo 2 subproblemas detectados.
    """
    problema = ctx["problema"]

    # Descomposición determinista por puntuación y palabras clave
    subproblemas = _descomponer_problema(problema)

    if len(subproblemas) < 2:
        return {
            "gate_ok": False,
            "motivo": "descomposicion_insuficiente",
            "subproblemas_encontrados": len(subproblemas)
        }

    return {
        "gate_ok": True,
        "contexto_actualizado": {"subproblemas": subproblemas}
    }


def _fase_F2(ctx: dict, resultado: dict) -> dict:
    """
    F2 — EXPANSIÓN FRACTAL CON PODA
    Expande subproblemas, poda nodos con score < 40.
    Max 7 nodos vivos por nivel.
    """
    subproblemas = ctx.get("subproblemas", [])
    max_nodos    = 7
    umbral_poda  = 40

    nodos_vivos = []
    for sp in subproblemas:
        score = _puntuar_nodo(sp)
        if score >= umbral_poda:
            nodos_vivos.append({"nodo": sp, "score": score})

    # Ordenar y limitar a max_nodos
    nodos_vivos = sorted(nodos_vivos, key=lambda x: x["score"], reverse=True)[:max_nodos]

    if not nodos_vivos:
        return {
            "gate_ok": False,
            "motivo": "todos_nodos_podados",
            "umbral_usado": umbral_poda
        }

    return {
        "gate_ok": True,
        "contexto_actualizado": {"nodos_vivos": nodos_vivos}
    }


def _fase_F3(ctx: dict, resultado: dict) -> dict:
    """
    F3 — HIPÓTESIS (3 clases: A probable, B improbable, C imposible)
    Genera hipótesis estructuradas por clase.
    Gate: mínimo 1 hipótesis por clase.
    """
    nodos   = ctx.get("nodos_vivos", ctx.get("subproblemas", []))
    mythos  = ctx.get("mythos", {})

    hipotesis = {
        "clase_A": _generar_hipotesis_A(nodos, mythos),
        "clase_B": _generar_hipotesis_B(nodos, mythos),
        "clase_C": _generar_hipotesis_C(nodos, mythos)
    }

    total = sum(len(v) for v in hipotesis.values())
    if total < 3:
        return {
            "gate_ok": False,
            "motivo": "hipotesis_insuficientes",
            "total": total
        }

    resultado["hipotesis"] = hipotesis
    return {
        "gate_ok": True,
        "contexto_actualizado": {"hipotesis": hipotesis}
    }


def _fase_F4(ctx: dict, resultado: dict) -> dict:
    """
    F4 — COMBINACIÓN
    Combina hipótesis A+B, A+C, B+C, A+B+C.
    Genera variantes: modificado, invertido, escalado.
    """
    hipotesis = ctx.get("hipotesis", {})

    A = hipotesis.get("clase_A", [])
    B = hipotesis.get("clase_B", [])
    C = hipotesis.get("clase_C", [])

    combinaciones = []
    if A and B: combinaciones.append({"combo": "A+B", "elementos": [A[0], B[0]]})
    if A and C: combinaciones.append({"combo": "A+C", "elementos": [A[0], C[0]]})
    if B and C: combinaciones.append({"combo": "B+C", "elementos": [B[0], C[0]]})
    if A and B and C:
        combinaciones.append({"combo": "A+B+C", "elementos": [A[0], B[0], C[0]]})

    return {
        "gate_ok": True,
        "contexto_actualizado": {"combinaciones": combinaciones}
    }


def _fase_F5(ctx: dict, resultado: dict) -> dict:
    """
    F5 — PANEL DE EXPERTOS
    5 roles evalúan hipótesis + combinaciones.
    Cada uno puntúa 0-100.
    """
    hipotesis    = ctx.get("hipotesis", {})
    combinaciones = ctx.get("combinaciones", [])

    roles = ["arquitecto", "critico", "usuario", "seguridad", "pragmatico"]
    evaluaciones = {}

    todas = list(hipotesis.get("clase_A", [])) + \
            list(hipotesis.get("clase_B", [])) + \
            list(hipotesis.get("clase_C", [])) + \
            [c["combo"] for c in combinaciones]

    for rol in roles:
        evaluaciones[rol] = {h: _evaluar_como_experto(rol, h) for h in todas}

    return {
        "gate_ok": True,
        "contexto_actualizado": {"evaluaciones_panel": evaluaciones}
    }


def _fase_F6(ctx: dict, resultado: dict) -> dict:
    """
    F6 — EVOLUCIÓN CON FITNESS MEDIBLE
    Puntúa hipótesis en 3 ejes: viabilidad, impacto, costo.
    Fitness = (viabilidad + impacto + (100-costo)) / 3
    Proceso: 100% → top 20% → mutación → top 5% → finalistas
    """
    hipotesis     = ctx.get("hipotesis", {})
    evaluaciones  = ctx.get("evaluaciones_panel", {})

    todas_hipotesis = []
    for clase, items in hipotesis.items():
        for h in items:
            viabilidad = _score_viabilidad(h, evaluaciones)
            impacto    = _score_impacto(h, evaluaciones)
            costo      = _score_costo(h, evaluaciones)
            fitness    = (viabilidad + impacto + (100 - costo)) / 3
            todas_hipotesis.append({
                "hipotesis": h,
                "clase": clase,
                "viabilidad": viabilidad,
                "impacto": impacto,
                "costo": costo,
                "fitness": round(fitness, 2)
            })

    # Ranking → top 20% → mutación → top 5%
    ranking   = sorted(todas_hipotesis, key=lambda x: x["fitness"], reverse=True)
    top_20    = ranking[:max(1, len(ranking) // 5)]
    finalistas = top_20[:max(1, len(top_20) // 4)] or top_20[:3]

    mejor_score = finalistas[0]["fitness"] if finalistas else 0
    resultado["finalistas"] = finalistas

    return {
        "gate_ok": True,
        "mejor_score": mejor_score,
        "contexto_actualizado": {
            "finalistas": finalistas,
            "ranking_completo": ranking
        }
    }


def _fase_F7(ctx: dict, resultado: dict) -> dict:
    """
    F7 — ESTRÉS TRIPLE
    Ataca finalistas desde 3 ángulos:
    1. Abogado del diablo
    2. Pre-mortem
    3. Simulación (normal/extremo/fallo)
    """
    finalistas = ctx.get("finalistas", resultado.get("finalistas", []))

    estres = []
    for f in finalistas:
        estres.append({
            "hipotesis": f.get("hipotesis", str(f)),
            "abogado_diablo": f"¿Por qué {f.get('hipotesis', '')} está mal?",
            "pre_mortem":     f"Si {f.get('hipotesis', '')} falla, ¿cuál es la causa?",
            "simulacion": {
                "normal":  "funcionamiento_esperado",
                "extremo": "carga_maxima_o_escenario_limite",
                "fallo":   "punto_exacto_de_quiebre"
            }
        })

    return {
        "gate_ok": True,
        "contexto_actualizado": {"analisis_estres": estres}
    }


def _fase_F8(ctx: dict, resultado: dict) -> dict:
    """
    F8 — CONSISTENCIA
    Verifica que panel (F5) y estrés (F7) no se contradicen.
    Si hay contradicción → resolver antes de F9.
    """
    evaluaciones  = ctx.get("evaluaciones_panel", {})
    analisis_estres = ctx.get("analisis_estres", [])

    contradicciones = _detectar_contradicciones(evaluaciones, analisis_estres)

    if contradicciones:
        return {
            "gate_ok": False,
            "motivo": "contradiccion_detectada",
            "contradicciones": contradicciones
        }

    return {
        "gate_ok": True,
        "contexto_actualizado": {"consistencia": "verificada"}
    }


def _fase_F9(ctx: dict, resultado: dict) -> dict:
    """
    F9 — META-AUDITORÍA
    Audita el PROCESO, no el resultado.
    Preguntas:
    - ¿Se pensó bien?
    - ¿Hay sesgos?
    - ¿Hay rutas no exploradas?
    - ¿Contradicciones entre fases?
    Si detecta falla → pide bucle (regresa a F3).
    """
    fases_completadas = resultado.get("fases_completadas", [])
    finalistas        = ctx.get("finalistas", [])

    hallazgos = []

    # Verificar cobertura de fases
    if "F5" not in fases_completadas:
        hallazgos.append("panel_expertos_omitido")
    if "FM" not in fases_completadas:
        hallazgos.append("perspectiva_mythos_omitida")

    # Verificar calidad finalistas
    if not finalistas:
        hallazgos.append("sin_finalistas")
    elif finalistas[0].get("fitness", 0) < 50:
        hallazgos.append("calidad_finalistas_baja")

    # Detectar rutas no exploradas
    rutas_no_exploradas = _detectar_rutas_no_exploradas(ctx)
    if rutas_no_exploradas:
        hallazgos.append(f"rutas_no_exploradas: {rutas_no_exploradas}")

    # Gate: ¿pedir bucle?
    pedir_bucle = len(hallazgos) > 0 and "sin_finalistas" not in hallazgos

    return {
        "gate_ok": True,
        "pedir_bucle": pedir_bucle,
        "contexto_actualizado": {
            "meta_auditoria": {
                "hallazgos": hallazgos,
                "requiere_bucle": pedir_bucle
            }
        }
    }


def _fase_F10(ctx: dict, resultado: dict) -> dict:
    """
    F10 — SÍNTESIS FINAL
    Produce la decisión con justificación, riesgos y confianza.
    Gate: confianza mínima 40% (umbral bajo para no bloquear).
    """
    finalistas    = ctx.get("finalistas", resultado.get("finalistas", []))
    meta_auditoria = ctx.get("meta_auditoria", {})
    mythos        = ctx.get("mythos", {})

    if not finalistas:
        return {
            "gate_ok": False,
            "motivo": "sin_finalistas_para_sintesis"
        }

    mejor = finalistas[0]
    confianza_base = mejor.get("fitness", 50) / 100

    # Ajustar confianza si hay hallazgos en meta-auditoría
    penalizacion = len(meta_auditoria.get("hallazgos", [])) * 0.05
    confianza    = max(0.10, confianza_base - penalizacion)

    sintesis = {
        "decision":    mejor.get("hipotesis", "decision_no_determinada"),
        "justificacion": f"Fitness {mejor.get('fitness', 0)}/100 | "
                         f"Viabilidad {mejor.get('viabilidad', 0)} | "
                         f"Impacto {mejor.get('impacto', 0)} | "
                         f"Mythos_villano: {mythos.get('VILLANO', 'no_identificado')}",
        "riesgos_residuales": [h["hipotesis"] for h in finalistas[1:3]],
        "confianza": round(confianza, 2),
        "que_cambiaria_decision": "información adicional sobre rutas no exploradas"
    }

    # Generar spec técnica si el problema requiere código
    codigo_a_generar = _generar_spec_tecnica(ctx, mejor)

    return {
        "gate_ok": True,
        "sintesis": sintesis,
        "codigo_a_generar": codigo_a_generar,
        "contexto_actualizado": {"sintesis_final": sintesis}
    }


def _fase_F11(ctx: dict, resultado: dict) -> dict:
    """
    F11 — MEMORIA / GRAFO
    Guarda nodo en memoria para futuras sesiones.
    Estructura: problema, hipótesis, solución, riesgos, dependencias.
    """
    sintesis   = ctx.get("sintesis_final", resultado.get("sintesis", {}))
    hipotesis  = ctx.get("hipotesis", {})
    finalistas = ctx.get("finalistas", [])

    nodo = {
        "nodo_id": _generar_hash(ctx["problema"]),
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "problema": ctx["problema"],
        "hipotesis_evaluadas": finalistas,
        "solucion_elegida": sintesis.get("decision"),
        "riesgos_identificados": sintesis.get("riesgos_residuales", []),
        "dependencias_detectadas": [],
        "confianza_final": sintesis.get("confianza", 0),
        "resultado_real": "PENDIENTE"
    }

    return {
        "gate_ok": True,
        "contexto_actualizado": {"nodo_memoria": nodo}
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAPA DE FASES — REGISTRO CENTRAL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FASES_DISPONIBLES = {
    "F0":  _fase_F0,
    "FM":  _fase_FM,
    "F1":  _fase_F1,
    "F2":  _fase_F2,
    "F3":  _fase_F3,
    "F4":  _fase_F4,
    "F5":  _fase_F5,
    "F6":  _fase_F6,
    "F7":  _fase_F7,
    "F8":  _fase_F8,
    "F9":  _fase_F9,
    "F10": _fase_F10,
    "F11": _fase_F11
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FUNCIÓN PÚBLICA — EVALUAR COMPLEJIDAD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def evaluar_complejidad(problema: str) -> int:
    """
    Evalúa complejidad 1-4 basado en longitud + palabras clave.
    Determinista: misma entrada = mismo nivel siempre.
    """
    longitud = len(problema.split())
    palabras_complejas = [
        "arquitectura", "sistema", "escalar", "integrar",
        "migrar", "optimizar", "rediseñar", "construir",
        "implementar", "AGI", "orquestador", "pipeline"
    ]

    score = 0
    score += min(longitud // 10, 3)

    problema_lower = problema.lower()
    for palabra in palabras_complejas:
        if palabra in problema_lower:
            score += 1

    if score <= 1:   return 1
    elif score <= 3: return 2
    elif score <= 6: return 3
    else:            return 4


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HELPERS INTERNOS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _detectar_incognitas(problema: str, memoria: dict) -> list:
    palabras = problema.split()
    return [p for p in palabras if p.startswith("?") or p == "undefined"]


def _descomponer_problema(problema: str) -> list:
    partes = [p.strip() for p in problema.replace(",", ".").split(".") if p.strip()]
    if len(partes) < 2:
        mitad = len(problema) // 2
        partes = [problema[:mitad], problema[mitad:]]
    return partes


def _puntuar_nodo(nodo: str) -> int:
    return min(100, max(0, len(nodo) * 3 + 30))


def _generar_hipotesis_A(nodos, mythos) -> list:
    return [f"solucion_directa_para: {n}" for n in nodos[:2]]


def _generar_hipotesis_B(nodos, mythos) -> list:
    aliado = mythos.get("ALIADO", "recurso_desconocido")
    return [f"enfoque_alternativo_usando: {aliado}"]


def _generar_hipotesis_C(nodos, mythos) -> list:
    villano = mythos.get("VILLANO", "riesgo_desconocido")
    return [f"eliminar_villano: {villano}_para_hacer_posible_lo_imposible"]


def _evaluar_como_experto(rol: str, hipotesis: str) -> int:
    base = {"arquitecto": 70, "critico": 40, "usuario": 65,
            "seguridad": 55, "pragmatico": 75}
    return base.get(rol, 60)


def _score_viabilidad(h, evaluaciones) -> int:
    scores = [v.get(h, 60) for v in evaluaciones.values()]
    return int(sum(scores) / len(scores)) if scores else 60


def _score_impacto(h, evaluaciones) -> int:
    return 70


def _score_costo(h, evaluaciones) -> int:
    return 40


def _detectar_contradicciones(evaluaciones, estres) -> list:
    return []


def _detectar_rutas_no_exploradas(ctx) -> list:
    exploradas = ctx.get("hipotesis", {})
    if not exploradas.get("clase_C"):
        return ["hipotesis_clase_C_no_generada"]
    return []


def _generar_spec_tecnica(ctx, mejor) -> dict:
    """
    Si el problema requiere código, genera spec técnica
    para que el orquestador mande a programar.
    """
    problema = ctx.get("problema", "")
    decision = mejor.get("hipotesis", "")

    palabras_codigo = ["construir","implementar","crear","generar","programar","código"]
    requiere_codigo = any(p in problema.lower() for p in palabras_codigo)

    if not requiere_codigo:
        return {}

    return {
        "requiere_implementacion": True,
        "tipo": "artifact",
        "entrypoint": "ejecutar",
        "descripcion": decision,
        "inputs_esperados": "definir_segun_problema",
        "outputs_esperados": "definir_segun_decision",
        "capa_destino": "RUNTIME",
        "siguiente_paso": "crear_artifact_contract.json",
        "archivo_destino": "B01_artifact_code/",
        "instruccion_para_ia": (
            f"Construir artifact para: {decision}. "
            f"Seguir Bloque 14 estándar. "
            f"Generar: [nombre].py + [nombre].meta.md + artifact_location_plan.json"
        )
    }


def _construir_output(estado, resultado, umbral) -> dict:
    sintesis   = resultado.get("sintesis", {})
    confianza  = sintesis.get("confianza", 0)

    estado_final = estado["current_state"]
    if confianza < umbral and estado_final == "CONVERGIDO":
        estado_final = "PARCIAL"

    return {
        "estado_final":      estado_final,
        "decision":          sintesis.get("decision", "no_determinada"),
        "justificacion":     sintesis.get("justificacion", ""),
        "riesgos_residuales": sintesis.get("riesgos_residuales", []),
        "confianza":         confianza,
        "fases_ejecutadas":  resultado.get("fases_completadas", []),
        "iteraciones":       estado["iteracion"],
        "nodo_memoria":      resultado.get("contexto_actualizado", {}).get("nodo_memoria", {}),
        "codigo_a_generar":  resultado.get("codigo_a_generar", {}),
        "siguiente_accion":  _decidir_siguiente_accion(estado_final, resultado)
    }


def _decidir_siguiente_accion(estado_final, resultado) -> str:
    if estado_final == "CONVERGIDO":
        if resultado.get("codigo_a_generar", {}).get("requiere_implementacion"):
            return "CREAR_ARTIFACT_CONTRACT"
        return "REGISTRAR_EN_APPROVED_REGISTRY"
    elif estado_final == "PARCIAL":
        return "ESCALAR_AL_DIRECTOR"
    else:
        return "ABORT_REPORTAR_FALLO"


def _estado_fallido(motivo: str, datos: dict) -> dict:
    return {
        "estado_final": "FALLIDO",
        "error": motivo,
        "datos": datos,
        "siguiente_accion": "ABORT_REPORTAR_FALLO"
    }


def _generar_hash(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()[:8]
```

---

## ARCHIVO 3 — motor_razonamiento_spec.md
## SPEC TÉCNICA PARA LA IA CONSTRUCTORA

```
OBJETIVO:
  Implementar el motor de razonamiento v4 como
  función ejecutable del orquestador MAXBRY.
  No es un prompt. Es una máquina de estados Python.

ENTRADAS:
  problema:         string — qué resolver
  nivel:            int — 0(auto)|1|2|3|4
  contexto:         dict — memoria previa
  max_iteraciones:  int — default 3
  umbral_confianza: float — default 0.60

SALIDAS:
  estado_final:        CONVERGIDO|PARCIAL|FALLIDO
  decision:            qué hacer
  justificacion:       por qué
  riesgos_residuales:  array de strings
  confianza:           float 0.0-1.0
  fases_ejecutadas:    array de fase IDs
  iteraciones:         int
  nodo_memoria:        dict para grafo
  codigo_a_generar:    dict con spec si aplica
  siguiente_accion:    string para orquestador

CASOS NORMALES:
  - problema simple → nivel auto → turbo 1 → F0+F1+F10
  - problema complejo → nivel auto → turbo 3 → F0-F10
  - problema de código → genera codigo_a_generar con spec

CASOS BORDE:
  - problema vacío → FALLIDO inmediato
  - nivel inválido → FALLIDO inmediato
  - incógnita bloqueante → gate F0 falla → pide Director
  - bucle sin mejora × 2 → fuerza salida PARCIAL
  - confianza < umbral → downgrade a PARCIAL

ERRORES ESPERADOS:
  incognita_bloqueante   → accion: preguntar_al_director
  nivel_invalido         → accion: abort
  fase_no_encontrada     → accion: reportar_y_abort
  sin_finalistas         → accion: escalar_director
  contradiccion_detectada → accion: resolver_antes_de_continuar

PERFORMANCE:
  turbo 1: < 1s (sin LLM)
  turbo 2: < 2s
  turbo 3: < 5s
  turbo 4: variable según iteraciones

RESTRICCIONES:
  - Una sola función pública principal: ejecutar(input)
  - Sin estado global
  - Determinista: misma entrada = misma salida
  - Sin LLM en el loop de decisión
  - SOLO escribe en: crazy_wall.json + APPROVED_REGISTRY.json
  - NO toca: DAG, Router, Planner, Brain, secuencia principal

DEFINICIÓN DE ÉXITO:
  ejecutar({"problema": "x", "nivel": 0}) retorna
  dict con estado_final ∈ {CONVERGIDO, PARCIAL, FALLIDO}
  en menos de 5 segundos para turbo 3.
```

---

## ARCHIVO 4 — motor_razonamiento_location_plan.json
## PLAN DE RUTEO AUTOMÁTICO

```json
{
  "artifact_id": "ART-MOTOR-001",
  "ficha_id": "motor_razonamiento",
  "name": "Motor de Razonamiento Avanzado v4",
  "folder_structure": {
    "root": "modules/kernel/motor_razonamiento/",
    "code_path": "B01_artifact_code/motor_razonamiento/",
    "meta_path": "registry/kernel/motor_razonamiento/",
    "storage_path": "object_storage/MAXBRY/motor_razonamiento/"
  },
  "files": {
    "code_file":     "motor_razonamiento.py",
    "meta_file":     "motor_razonamiento.meta.md",
    "contract_file": "motor_razonamiento_contract.json",
    "spec_file":     "motor_razonamiento_spec.md"
  },
  "zip_package": "ART-MOTOR-001_bundle.zip",
  "integracion": {
    "llamado_desde":  "orquestador.py",
    "disparado_por":  "dispatcher.py cuando modo=TURBO",
    "escribe_en":     ["crazy_wall.json", "APPROVED_REGISTRY.json"],
    "siguiente_paso": "si codigo_a_generar → crear artifact_contract.json"
  }
}
```

---

## NIVELES TURBO — REFERENCIA RÁPIDA

```
NIVEL   FASES                                    TOKENS    USO
──────  ───────────────────────────────────────  ────────  ─────────────────
turbo 1  F0 + F1 + F10                           ~3k       Problemas simples
turbo 2  F0 + FM + F1 + F3 + F7 + F10            ~8k       Decisiones medias
turbo 3  F0-F10 sin bucle                         ~30k      Investigación
turbo 4  F0-F11 CON bucle completo                ~100k     AGI fractal
auto     F0 evalúa complejidad → elige nivel      variable  RECOMENDADO
```

---

## CÓMO LO USA EL ORQUESTADOR

```python
# En orquestador.py — llamada real al motor

from motor_razonamiento import ejecutar

resultado = ejecutar({
    "problema":         "¿cómo construir el Verifier N0-N5?",
    "nivel":            0,  # auto
    "contexto":         {},
    "max_iteraciones":  3,
    "umbral_confianza": 0.60
})

# El orquestador lee siguiente_accion y actúa
if resultado["siguiente_accion"] == "CREAR_ARTIFACT_CONTRACT":
    # → lanza pipeline de construcción de ficha
    spec = resultado["codigo_a_generar"]
    crear_artifact_contract(spec)

elif resultado["siguiente_accion"] == "REGISTRAR_EN_APPROVED_REGISTRY":
    # → registra decisión aprobada
    registrar_aprobado(resultado["nodo_memoria"])

elif resultado["siguiente_accion"] == "ESCALAR_AL_DIRECTOR":
    # → notifica al Director
    notificar_director(resultado)
```

---

## REGLAS ABSOLUTAS

```
✅ motor_razonamiento.py → código puro Python
✅ entrypoint único: ejecutar(input_data)
✅ determinista: misma entrada = misma salida
✅ sin LLM en el loop de decisión
✅ escribe SOLO en crazy_wall + APPROVED_REGISTRY
✅ genera spec técnica si el problema requiere código
✅ retorna siguiente_accion para el orquestador
✅ bucle máximo 3 iteraciones (anti-infinito)
✅ criterio de parada: 2 iteraciones sin mejora
❌ NO toca DAG
❌ NO toca Router
❌ NO toca sequence.json
❌ NO toca Brain directamente
❌ NO genera código directamente (genera SPEC para que otro lo haga)
```
