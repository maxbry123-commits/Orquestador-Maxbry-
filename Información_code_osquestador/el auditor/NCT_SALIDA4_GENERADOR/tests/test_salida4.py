"""TESTS SALIDA 4 — Generador parte 2 + LA GRAN AUDITORÍA como test:
¿NCT produce una app 100% funcional de principio a fin? → SÍ, y aquí se prueba.
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from generador.db_api_generator import (esquema_de, generar_modelos,
                                        generar_api, generar_tests_api)
from generador.ensamblador import ensamblar_app, generar_componente_ui
from generador.embudo import procesar_idea


def test_esquema_por_dominio_y_auth():
    req = procesar_idea("app de recetas con login")
    e = esquema_de(req)
    assert "receta" in e and "usuario" in e      # dominio + autenticación


def test_esquema_generico_para_dominio_desconocido():
    req = procesar_idea("app de astrologia cuantica")
    assert "item" in esquema_de(req)             # fallback, nunca crash


def test_modelos_generados_compilan_y_funcionan(tmp_path):
    e = {"tarea": [("titulo", "TEXT"), ("hecha", "INTEGER")]}
    ruta = tmp_path / "modelos.py"
    ruta.write_text(generar_modelos(e))
    import subprocess
    r = subprocess.run([sys.executable, "-c",
                        "import os; os.environ['APP_DB']='" +
                        str(tmp_path / "t.db") + "';"
                        "import modelos; modelos.crear_tablas();"
                        "i=modelos.crear_tarea('x',0);"
                        "assert modelos.obtener_tarea(i)['titulo']=='x'"],
                       cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_api_generada_tiene_crud_completo():
    e = {"producto": [("nombre", "TEXT"), ("precio", "REAL")]}
    api = generar_api(e, "tienda")
    for pieza in ("@app.post('/productos')", "@app.get('/productos')",
                  "@app.get('/productos/{id_}')",
                  "@app.delete('/productos/{id_}')", "HTTPException(404"):
        assert pieza in api


def test_componente_ui_consume_la_api():
    c = generar_componente_ui("tarea", [("titulo", "TEXT")], "#CC785C")
    assert "fetch('/tareas'" in c and "method:'POST'" in c \
        and "method:'DELETE'" in c


# ══ LA GRAN AUDITORÍA (pendiente histórico) COMO TESTS ══════════════════

def test_AUDITORIA_idea_a_app_funcional(tmp_path):
    """El sistema PRODUCE un entregable real: compila + sus tests pasan."""
    acta = ensamblar_app("app de tareas con login y buscador",
                         str(tmp_path / "app"))
    assert acta["ok"] is True, acta
    assert acta["verificaciones"]["tests_generados"] == "PASS"
    assert all(v is True for k, v in acta["verificaciones"].items()
               if k.startswith("compila:"))
    assert (tmp_path / "app" / "index.html").exists()


def test_AUDITORIA_tres_dominios_distintos(tmp_path):
    """No es un truco de un solo caso: 3 dominios diferentes, 3 apps OK."""
    for i, idea in enumerate(["app de recetas con buscador",
                              "tienda con login",
                              "blog simple"]):
        acta = ensamblar_app(idea, str(tmp_path / f"a{i}"))
        assert acta["ok"] is True, (idea, acta)


def test_AUDITORIA_determinista(tmp_path):
    """Misma idea = mismos archivos generados byte a byte (L15)."""
    ensamblar_app("app de tareas", str(tmp_path / "x"))
    ensamblar_app("app de tareas", str(tmp_path / "y"))
    for a in ("modelos.py", "api.py", "index.html"):
        assert (tmp_path / "x" / a).read_text() == \
               (tmp_path / "y" / a).read_text()


def test_acta_registra_todo(tmp_path):
    acta = ensamblar_app("blog simple", str(tmp_path / "b"))
    assert len(acta["pasos"]) >= 3
    assert acta["entidades"] and acta["archivos"]
    assert "idea" in acta                        # trazabilidad completa
