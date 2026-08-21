"""GENERADOR PARTE 2A — DB + API (S09: componentes + DB + API real).
Desde requisitos.json (embudo G1) genera:
  · modelos.py — SQLAlchemy-free: SQLite puro con esquema por entidad
  · api_<entidad>.py — endpoints CRUD FastAPI reales por entidad
Determinista: mismos requisitos = misma app. 0% LLM.
"""
from __future__ import annotations
import os

# Entidades y campos por dominio (extensible; fallback genérico)
ESQUEMAS_DOMINIO = {
    "tareas": {"tarea": [("titulo", "TEXT"), ("hecha", "INTEGER"),
                         ("categoria", "TEXT")]},
    "recetas": {"receta": [("nombre", "TEXT"), ("ingredientes", "TEXT"),
                           ("pasos", "TEXT")]},
    "tienda": {"producto": [("nombre", "TEXT"), ("precio", "REAL"),
                            ("stock", "INTEGER")]},
    "blog": {"post": [("titulo", "TEXT"), ("cuerpo", "TEXT"),
                      ("autor", "TEXT")]},
}
ESQUEMA_GENERICO = {"item": [("nombre", "TEXT"), ("descripcion", "TEXT")]}


def esquema_de(requisitos: dict) -> dict:
    dominio = requisitos.get("proyecto", {}).get("dominio", "")
    base = dict(ESQUEMAS_DOMINIO.get(dominio, ESQUEMA_GENERICO))
    features = {rf["feature"] for rf in
                requisitos.get("requisitos_funcionales", [])}
    if "autenticacion" in features:
        base["usuario"] = [("email", "TEXT"), ("password_hash", "TEXT")]
    return base


def generar_modelos(esquema: dict) -> str:
    """modelos.py: SQLite puro, creación de tablas + CRUD por entidad."""
    lineas = [
        '"""modelos.py — generado por NCT (determinista, SQLite puro)."""',
        "import sqlite3", "import os", "",
        'DB = os.environ.get("APP_DB", "app.db")', "",
        "def conexion():",
        "    c = sqlite3.connect(DB)",
        "    c.row_factory = sqlite3.Row",
        "    return c", "",
        "def crear_tablas():",
        "    with conexion() as c:",
    ]
    for ent, campos in esquema.items():
        cols = ", ".join([f"{n} {t}" for n, t in campos])
        lineas.append(f'        c.execute("CREATE TABLE IF NOT EXISTS {ent} '
                      f'(id INTEGER PRIMARY KEY AUTOINCREMENT, {cols})")')
    lineas.append("")
    for ent, campos in esquema.items():
        nombres = [n for n, _ in campos]
        marcas = ", ".join(["?"] * len(nombres))
        lineas += [
            f"def crear_{ent}({', '.join(nombres)}):",
            f"    with conexion() as c:",
            f"        cur = c.execute(\"INSERT INTO {ent} "
            f"({', '.join(nombres)}) VALUES ({marcas})\", "
            f"({', '.join(nombres)},))",
            f"        return cur.lastrowid", "",
            f"def listar_{ent}():",
            f"    with conexion() as c:",
            f"        return [dict(r) for r in "
            f"c.execute(\"SELECT * FROM {ent} ORDER BY id\")]", "",
            f"def obtener_{ent}(id_):",
            f"    with conexion() as c:",
            f"        r = c.execute(\"SELECT * FROM {ent} WHERE id=?\", "
            f"(id_,)).fetchone()",
            f"        return dict(r) if r else None", "",
            f"def borrar_{ent}(id_):",
            f"    with conexion() as c:",
            f"        return c.execute(\"DELETE FROM {ent} WHERE id=?\", "
            f"(id_,)).rowcount > 0", "",
        ]
    return "\n".join(lineas)


def generar_api(esquema: dict, nombre_proyecto: str) -> str:
    """api.py: FastAPI con CRUD real por entidad, montado sobre modelos.py."""
    lineas = [
        f'"""api.py — {nombre_proyecto} (generado por NCT)."""',
        "from fastapi import FastAPI, HTTPException",
        "from pydantic import BaseModel",
        "import modelos", "",
        f'app = FastAPI(title="{nombre_proyecto}")', "",
        "@app.on_event('startup')",
        "def _inicio():",
        "    modelos.crear_tablas()", "",
        "@app.get('/salud')",
        "def salud():",
        "    return {'ok': True}", "",
    ]
    tipos = {"TEXT": "str", "INTEGER": "int", "REAL": "float"}
    for ent, campos in esquema.items():
        clase = ent.capitalize()
        lineas += [f"class {clase}In(BaseModel):"]
        lineas += [f"    {n}: {tipos.get(t, 'str')}" for n, t in campos]
        lineas += [
            "",
            f"@app.post('/{ent}s')",
            f"def crear_{ent}(x: {clase}In):",
            f"    nuevo_id = modelos.crear_{ent}("
            f"{', '.join('x.' + n for n, _ in campos)})",
            f"    return {{'id': nuevo_id}}", "",
            f"@app.get('/{ent}s')",
            f"def listar_{ent}s():",
            f"    return modelos.listar_{ent}()", "",
            f"@app.get('/{ent}s/{{id_}}')",
            f"def obtener_{ent}(id_: int):",
            f"    r = modelos.obtener_{ent}(id_)",
            f"    if not r:",
            f"        raise HTTPException(404, '{ent}_no_existe')",
            f"    return r", "",
            f"@app.delete('/{ent}s/{{id_}}')",
            f"def borrar_{ent}(id_: int):",
            f"    if not modelos.borrar_{ent}(id_):",
            f"        raise HTTPException(404, '{ent}_no_existe')",
            f"    return {{'borrado': True}}", "",
        ]
    return "\n".join(lineas)


def generar_tests_api(esquema: dict) -> str:
    """Tests REALES de la app generada (SQLite en tmp, sin red)."""
    lineas = [
        '"""tests de la app generada — corren contra modelos.py real."""',
        "import os, tempfile",
        "os.environ['APP_DB'] = os.path.join(tempfile.mkdtemp(), 't.db')",
        "import modelos", "",
        "def test_tablas():",
        "    modelos.crear_tablas()", "",
    ]
    for ent, campos in esquema.items():
        valores = []
        for n, t in campos:
            valores.append("1" if t == "INTEGER" else
                           "1.5" if t == "REAL" else f"'{n}_demo'")
        lineas += [
            f"def test_crud_{ent}():",
            f"    modelos.crear_tablas()",
            f"    i = modelos.crear_{ent}({', '.join(valores)})",
            f"    assert modelos.obtener_{ent}(i) is not None",
            f"    assert any(r['id'] == i for r in modelos.listar_{ent}())",
            f"    assert modelos.borrar_{ent}(i) is True",
            f"    assert modelos.obtener_{ent}(i) is None", "",
        ]
    return "\n".join(lineas)
