"""MOTOR DE BOILERPLATES — F1 parte 2 (gap más grande, Fase 05)
Toma requisitos.json (del embudo) + tokens (del design_system) y genera
un proyecto REAL FastAPI + React que compila y corre:
  backend/ (FastAPI con CRUD del dominio + auth si se pidió)
  frontend/ (React sin build: index.html + app.jsx vía CDN, con tokens)
Determinista: mismos requisitos = mismo proyecto (L15).
Stack 1 de 2 aprobados (FastAPI+React). Cada plantilla <=200 líneas (L02).
"""
import os
import json
from . import plantillas


def _tiene(requisitos, feature):
    return any(r["feature"] == feature
               for r in requisitos.get("requisitos_funcionales", []))


def generar_proyecto(requisitos: dict, tokens: dict, destino: str) -> dict:
    """Genera el árbol completo del proyecto. Devuelve el manifiesto."""
    dominio = requisitos["proyecto"]["dominio"].replace(" ", "_")
    nombre = requisitos["proyecto"]["nombre"]
    con_auth = _tiene(requisitos, "autenticacion")
    con_busqueda = _tiene(requisitos, "busqueda")

    archivos = {
        "backend/main.py": plantillas.backend_main(dominio, con_auth, con_busqueda),
        "backend/modelos.py": plantillas.backend_modelos(dominio),
        "backend/almacen.py": plantillas.backend_almacen(dominio),
        "backend/requirements.txt": plantillas.backend_requirements(),
        "frontend/index.html": plantillas.frontend_index(nombre, dominio),
        "frontend/app.jsx": plantillas.frontend_app(dominio, con_auth, con_busqueda),
        "frontend/variables.css": None,  # se escribe con los tokens reales
        "README.md": plantillas.readme(nombre, dominio),
        "tests/test_backend.py": plantillas.tests_backend(dominio),
    }
    if con_auth:
        archivos["backend/auth.py"] = plantillas.backend_auth()

    os.makedirs(destino, exist_ok=True)
    escritos = []
    for ruta, contenido in archivos.items():
        completa = os.path.join(destino, ruta)
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        if ruta.endswith("variables.css"):
            from .design_system import exportar_css
            contenido = exportar_css(tokens)
        with open(completa, "w", encoding="utf-8") as f:
            f.write(contenido)
        escritos.append(ruta)

    manifiesto = {
        "proyecto": nombre,
        "stack": "fastapi+react",
        "dominio": dominio,
        "features": [r["feature"] for r in requisitos.get("requisitos_funcionales", [])],
        "archivos": sorted(escritos),
        "como_correr": {
            "backend": "cd backend && pip install -r requirements.txt && uvicorn main:app",
            "frontend": "abrir frontend/index.html (usa el backend en :8000)",
            "tests": "cd tests && python -m pytest test_backend.py",
        },
    }
    with open(os.path.join(destino, "manifiesto.json"), "w", encoding="utf-8") as f:
        json.dump(manifiesto, f, ensure_ascii=False, indent=2, sort_keys=True)
    return manifiesto
