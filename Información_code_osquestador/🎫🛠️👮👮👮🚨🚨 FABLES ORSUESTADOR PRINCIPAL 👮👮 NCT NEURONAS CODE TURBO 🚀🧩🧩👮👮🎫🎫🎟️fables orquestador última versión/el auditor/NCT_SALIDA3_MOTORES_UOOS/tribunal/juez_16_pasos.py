"""LLM_JUEZ 16 PASOS — F5 (gap O2 del Orquestador)
Alinea el Tribunal de 6 inspectores (Sheriff/Centinela/Juez/Supervisor/
Validador/Verificador, umbral 70) con la secuencia histórica de 16 pasos
(P-DISCOVER -> P13). Equivalencia 1:1 documentada + ejecutor secuencial.
Determinista: cada paso es una función de chequeo, no un LLM.
"""
import json
import hashlib

# ── LA TABLA DE EQUIVALENCIA (el mapeo que faltaba, gap O2) ──────────────
# paso, nombre histórico, inspector responsable, qué verifica
SECUENCIA_16 = [
    ("P-DISCOVER", "descubrimiento",      "Sheriff",     "existe input y es legible"),
    ("P-01",       "inventario",          "Sheriff",     "todos los archivos declarados existen"),
    ("P-02",       "integridad",          "Sheriff",     "hashes coinciden, nada corrupto"),
    ("P-03",       "alcance",             "Centinela",   "no hay scope-creep (Ley L13)"),
    ("P-04",       "dependencias",        "Centinela",   "versiones exactas declaradas (Ley L06)"),
    ("P-05",       "apis_reales",         "Centinela",   "cero APIs/librerías inventadas (Ley L05)"),
    ("P-06",       "estructura",          "Juez",        "1 archivo = 1 responsabilidad, <=200 líneas (L02)"),
    ("P-07",       "sintaxis",            "Juez",        "el código compila/parsea sin errores"),
    ("P-08",       "logica",              "Juez",        "tests unitarios del bloque en verde"),
    ("P-09",       "estado_via_eventos",  "Supervisor",  "estado solo cambia por eventos (L10)"),
    ("P-10",       "dag_respetado",       "Supervisor",  "el orden del DAG no se saltó (L08)"),
    ("P-11",       "sandbox",             "Supervisor",  "ejecución solo en sandbox declarado (L09)"),
    ("P-12",       "evidencia",           "Validador",   "toda tarea dejó evidencia (L11)"),
    ("P-12B",      "sin_alucinaciones",   "Validador",   "afirmaciones respaldadas por fuentes"),
    ("P-13A",      "reproducible",        "Verificador", "mismo input = mismo output (L15)"),
    ("P-13",       "sello_final",         "Verificador", "puntaje >= 70 y firma del lote"),
]

UMBRAL = 70


class Juez16Pasos:
    """Ejecuta los 16 pasos en orden. Cada paso recibe el contexto del lote
    y devuelve (ok, puntos, detalle). checks es un dict opcional que permite
    inyectar funciones reales por paso; sin función = chequeo declarativo
    (pasa si el contexto trae la evidencia con ese nombre)."""

    def __init__(self, checks: dict | None = None):
        self.checks = checks or {}

    def _defecto(self, paso_id, contexto):
        ev = contexto.get("evidencias", {})
        return (paso_id in ev and bool(ev[paso_id]),
                f"evidencia['{paso_id}'] {'presente' if paso_id in ev else 'AUSENTE'}")

    def ejecutar(self, contexto: dict) -> dict:
        resultados, puntos = [], 0
        por_paso = round(100 / len(SECUENCIA_16), 4)  # 6.25
        for paso_id, nombre, inspector, descripcion in SECUENCIA_16:
            fn = self.checks.get(paso_id)
            try:
                ok, detalle = fn(contexto) if fn else self._defecto(paso_id, contexto)
            except Exception as e:  # un check que explota = paso fallido, nunca crash
                ok, detalle = False, f"error_en_check: {e}"
            if ok:
                puntos += por_paso
            resultados.append({"paso": paso_id, "nombre": nombre,
                               "inspector": inspector, "ok": ok, "detalle": detalle})
            if not ok and inspector == "Sheriff":
                # Fallo del Sheriff = frenar en seco (sin input íntegro nada sigue)
                break
        puntaje = round(puntos, 2)
        veredicto = "APROBADO" if puntaje >= UMBRAL and all(r["ok"] for r in resultados) \
            else ("APROBADO_CON_PUNTAJE" if puntaje >= UMBRAL else "RECHAZADO")
        acta = {
            "puntaje": puntaje, "umbral": UMBRAL, "veredicto": veredicto,
            "pasos_ejecutados": len(resultados), "pasos_totales": len(SECUENCIA_16),
            "detalle": resultados,
        }
        acta["firma"] = hashlib.sha256(
            json.dumps(acta, sort_keys=True, ensure_ascii=False).encode()
        ).hexdigest()[:16]
        return acta


def tabla_equivalencia() -> list:
    """Exporta la tabla 16 pasos <-> 6 inspectores (para jueces_mapping.yaml)."""
    return [{"paso": p, "nombre": n, "inspector": i, "verifica": d}
            for p, n, i, d in SECUENCIA_16]


if __name__ == "__main__":
    ctx = {"evidencias": {p: True for p, _, _, _ in SECUENCIA_16}}
    print(json.dumps(Juez16Pasos().ejecutar(ctx), ensure_ascii=False, indent=2)[:800])
