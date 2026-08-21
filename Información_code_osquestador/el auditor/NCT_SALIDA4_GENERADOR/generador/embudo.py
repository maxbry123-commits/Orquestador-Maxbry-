"""EMBUDO DE ENTRADA — F2 (cierra SIM-1 falla 1, Fases 01/02/17)
Convierte una idea vaga en lenguaje natural en requisitos estructurados
que el resto del pipeline NCT sabe procesar. 100% determinista, 0% LLM.
Mismo input = mismo output (Ley L15).
"""
import json
import re
import hashlib

# Diccionarios de detección por reglas fijas (primera que calza gana)
TIPOS_APP = [
    ("web", ["web", "página", "pagina", "sitio", "portal", "dashboard"]),
    ("api", ["api", "backend", "servicio", "endpoint", "rest"]),
    ("movil", ["app móvil", "app movil", "android", "ios", "celular"]),
    ("desktop", ["escritorio", "desktop", "windows app"]),
    ("app", ["app", "aplicación", "aplicacion", "software", "sistema"]),
]
FEATURES_CONOCIDAS = [
    ("autenticacion", ["login", "registro", "usuarios", "cuenta", "sesión", "sesion", "auth"]),
    ("crud", ["crear", "editar", "borrar", "guardar", "gestionar", "administrar", "lista"]),
    ("busqueda", ["buscar", "buscador", "búsqueda", "busqueda", "filtrar", "filtro"]),
    ("pagos", ["pago", "stripe", "paypal", "cobrar", "suscripción", "suscripcion"]),
    ("notificaciones", ["notificar", "notificación", "notificacion", "correo", "email", "alerta"]),
    ("archivos", ["subir", "archivo", "imagen", "foto", "documento", "pdf"]),
    ("reportes", ["reporte", "gráfica", "grafica", "estadística", "estadistica", "métricas", "metricas"]),
    ("tiempo_real", ["tiempo real", "chat", "websocket", "en vivo"]),
]
RESTRICCIONES = [
    ("presupuesto_bajo", ["barato", "gratis", "bajo costo", "económico", "economico"]),
    ("rapido", ["rápido", "rapido", "urgente", "ya", "pronto"]),
    ("seguro", ["seguro", "seguridad", "privado", "cifrado"]),
    ("escalable", ["escalar", "escalable", "muchos usuarios", "miles"]),
]


def _detectar(texto, tabla, multiple=True):
    texto = texto.lower()
    hallados = []
    for etiqueta, palabras in tabla:
        if any(p in texto for p in palabras):
            hallados.append(etiqueta)
            if not multiple:
                return [etiqueta]
    return hallados


def _extraer_sustantivo_dominio(texto):
    """Extrae el dominio: 'app de recetas' -> 'recetas'."""
    m = re.search(r"\b(?:de|para|sobre)\s+([a-záéíóúñ]+(?:\s+[a-záéíóúñ]+)?)", texto.lower())
    if m:
        dominio = m.group(1).strip()
        # limpiar palabras funcionales al final
        dominio = re.sub(r"\s+(con|que|donde|y|o|el|la|los|las|un|una)$", "", dominio)
        return dominio
    return "general"


def procesar_idea(idea: str) -> dict:
    """Punto de entrada del embudo. Idea vaga -> requisitos.json estructurado."""
    if not idea or not idea.strip():
        return {"error": "IDEA_VACIA", "pregunta": "¿Qué quieres construir? (1 frase)"}
    tipo = _detectar(idea, TIPOS_APP, multiple=False)
    features = _detectar(idea, FEATURES_CONOCIDAS)
    restr = _detectar(idea, RESTRICCIONES)
    dominio = _extraer_sustantivo_dominio(idea)

    # Personas (Fase 17): derivadas del dominio de forma determinista
    personas = [
        {"rol": "usuario_final", "necesidad": f"usar la solución de {dominio} fácilmente"},
        {"rol": "administrador", "necesidad": f"gestionar el contenido de {dominio}"},
    ]

    requisitos = {
        "version": "1.0.0",
        "origen": "embudo_entrada",
        "idea_original": idea.strip(),
        "hash_idea": hashlib.sha256(idea.strip().encode()).hexdigest()[:12],
        "proyecto": {
            "nombre": f"proyecto_{dominio.replace(' ', '_')}",
            "dominio": dominio,
            "tipo": tipo[0] if tipo else "web",
        },
        "personas": personas,
        "requisitos_funcionales": [
            {"id": f"RF-{i+1:03d}", "feature": f, "prioridad": "alta" if i < 2 else "media"}
            for i, f in enumerate(features or ["crud"])
        ],
        "requisitos_no_funcionales": [
            {"id": f"RNF-{i+1:03d}", "restriccion": r} for i, r in enumerate(restr)
        ],
        "huecos": [],  # campos que el modo híbrido (LLM+Tribunal) puede llenar después
        "listo_para_pipeline": True,
    }
    # Detección de huecos (para la Opción 3 híbrida del TEMA A)
    if not features:
        requisitos["huecos"].append("features_no_detectadas")
    if dominio == "general":
        requisitos["huecos"].append("dominio_ambiguo")
    if requisitos["huecos"]:
        requisitos["listo_para_pipeline"] = False
        requisitos["pregunta_al_director"] = (
            "Detecté huecos: " + ", ".join(requisitos["huecos"]) +
            ". ¿Confirmas o das más detalle? (Ley L14: 1 pregunta, nunca asumir)"
        )
    return requisitos


def guardar(requisitos: dict, ruta: str) -> str:
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(requisitos, f, ensure_ascii=False, indent=2, sort_keys=True)
    return ruta


if __name__ == "__main__":
    import sys
    idea = " ".join(sys.argv[1:]) or "quiero una app de recetas con login y buscador"
    print(json.dumps(procesar_idea(idea), ensure_ascii=False, indent=2))
