"""PLANTILLAS del motor de boilerplates. Solo texto, cero lógica de decisión.
Cada plantilla genera un archivo completo y funcional (<=200 líneas, L02).
Versiones exactas de dependencias (L06). Sin APIs inventadas (L05).
"""


def backend_requirements():
    return "fastapi==0.111.0\nuvicorn==0.30.1\npydantic==2.7.4\n"


def backend_modelos(dom):
    return f'''"""Modelos Pydantic del dominio: {dom}."""
from pydantic import BaseModel
from typing import Optional


class {dom.capitalize()}Base(BaseModel):
    titulo: str
    descripcion: Optional[str] = None


class {dom.capitalize()}(({dom.capitalize()}Base)):
    id: int
'''


def backend_almacen(dom):
    return f'''"""Almacén en memoria del dominio: {dom} (reemplazable por DB real)."""
_datos = {{}}
_siguiente_id = [1]


def crear(item: dict) -> dict:
    item = dict(item, id=_siguiente_id[0])
    _datos[_siguiente_id[0]] = item
    _siguiente_id[0] += 1
    return item


def listar() -> list:
    return list(_datos.values())


def obtener(item_id: int):
    return _datos.get(item_id)


def borrar(item_id: int) -> bool:
    return _datos.pop(item_id, None) is not None


def buscar(q: str) -> list:
    q = q.lower()
    return [v for v in _datos.values()
            if q in v.get("titulo", "").lower()
            or q in (v.get("descripcion") or "").lower()]
'''


def backend_auth():
    return '''"""Auth mínima por token de sesión en memoria (base para JWT real)."""
import secrets

_usuarios = {}
_sesiones = {}


def registrar(usuario: str, clave: str) -> bool:
    if usuario in _usuarios:
        return False
    _usuarios[usuario] = clave
    return True


def login(usuario: str, clave: str):
    if _usuarios.get(usuario) == clave:
        token = secrets.token_hex(16)
        _sesiones[token] = usuario
        return token
    return None


def validar(token: str):
    return _sesiones.get(token)
'''


def backend_main(dom, con_auth, con_busqueda):
    cls = dom.capitalize()
    partes = [f'''"""API {dom} — generada por NCT (embudo -> design system -> boilerplate)."""
from fastapi import FastAPI, HTTPException
from modelos import {cls}Base
import almacen

app = FastAPI(title="API de {dom}")


@app.get("/salud")
def salud():
    return {{"ok": True, "servicio": "{dom}"}}


@app.post("/{dom}", status_code=201)
def crear(item: {cls}Base):
    return almacen.crear(item.model_dump())


@app.get("/{dom}")
def listar():
    return almacen.listar()


@app.get("/{dom}/{{item_id}}")
def obtener(item_id: int):
    item = almacen.obtener(item_id)
    if not item:
        raise HTTPException(404, "no encontrado")
    return item


@app.delete("/{dom}/{{item_id}}")
def borrar(item_id: int):
    if not almacen.borrar(item_id):
        raise HTTPException(404, "no encontrado")
    return {{"borrado": True}}
''']
    if con_busqueda:
        partes.append(f'''

@app.get("/buscar/{dom}")
def buscar(q: str):
    return almacen.buscar(q)
''')
    if con_auth:
        partes.append('''

from pydantic import BaseModel
import auth


class Credenciales(BaseModel):
    usuario: str
    clave: str


@app.post("/auth/registro")
def registro(c: Credenciales):
    if not auth.registrar(c.usuario, c.clave):
        raise HTTPException(409, "usuario ya existe")
    return {"registrado": True}


@app.post("/auth/login")
def hacer_login(c: Credenciales):
    token = auth.login(c.usuario, c.clave)
    if not token:
        raise HTTPException(401, "credenciales inválidas")
    return {"token": token}
''')
    return "".join(partes)


def frontend_index(nombre, dom):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{nombre}</title>
<link rel="stylesheet" href="variables.css">
<style>
body{{margin:0;font-family:var(--fuente-cuerpo);background:var(--fondo);color:var(--texto)}}
header{{background:var(--color-primario);color:#fff;padding:var(--esp-md) var(--esp-lg)}}
main{{max-width:720px;margin:0 auto;padding:var(--esp-lg)}}
.tarjeta{{background:var(--superficie);border:1px solid var(--borde);
  border-radius:var(--radio-md);padding:var(--esp-md);margin-bottom:var(--esp-sm);
  box-shadow:var(--sombra-suave,0 1px 3px rgba(0,0,0,.12))}}
input,button{{font:inherit;padding:8px 12px;border-radius:var(--radio-sm);
  border:1px solid var(--borde)}}
button{{background:var(--color-primario);color:#fff;border:none;cursor:pointer}}
</style>
<script crossorigin src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
<script crossorigin src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js"></script>
</head>
<body>
<header><h1 style="margin:0;font-family:var(--fuente-titulos)">{nombre}</h1></header>
<main><div id="raiz"></div></main>
<script type="text/babel" src="app.jsx"></script>
</body>
</html>
'''


def frontend_app(dom, con_auth, con_busqueda):
    buscador = ""
    if con_busqueda:
        buscador = '''
      <input placeholder="Buscar..." value={q}
        onChange={e => setQ(e.target.value)} style={{marginBottom: 12}} />'''
    return f'''const {{useState, useEffect}} = React;
const API = "http://localhost:8000";

function App() {{
  const [items, setItems] = useState([]);
  const [titulo, setTitulo] = useState("");
  const [q, setQ] = useState("");

  const cargar = () => fetch(API + "/{dom}").then(r => r.json()).then(setItems);
  useEffect(() => {{ cargar(); }}, []);

  const crear = () => {{
    if (!titulo.trim()) return;
    fetch(API + "/{dom}", {{
      method: "POST",
      headers: {{"Content-Type": "application/json"}},
      body: JSON.stringify({{titulo}})
    }}).then(() => {{ setTitulo(""); cargar(); }});
  }};

  const visibles = q
    ? items.filter(i => (i.titulo || "").toLowerCase().includes(q.toLowerCase()))
    : items;

  return (
    <div>{buscador}
      <div style={{{{display: "flex", gap: 8, marginBottom: 16}}}}>
        <input placeholder="Nuevo elemento de {dom}" value={{titulo}}
          onChange={{e => setTitulo(e.target.value)}} style={{{{flex: 1}}}} />
        <button onClick={{crear}}>Agregar</button>
      </div>
      {{visibles.map(i => (
        <div className="tarjeta" key={{i.id}}>
          <strong>{{i.titulo}}</strong>
          {{i.descripcion && <p>{{i.descripcion}}</p>}}
        </div>
      ))}}
      {{visibles.length === 0 && <p>Sin elementos todavía.</p>}}
    </div>
  );
}}

ReactDOM.createRoot(document.getElementById("raiz")).render(<App />);
'''


def tests_backend(dom):
    return f'''"""Tests del backend generado — prueban CRUD real sin red."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
import almacen


def test_crear_y_listar():
    almacen._datos.clear()
    item = almacen.crear({{"titulo": "prueba", "descripcion": "x"}})
    assert item["id"] >= 1
    assert len(almacen.listar()) == 1


def test_obtener_y_borrar():
    almacen._datos.clear()
    item = almacen.crear({{"titulo": "a"}})
    assert almacen.obtener(item["id"])["titulo"] == "a"
    assert almacen.borrar(item["id"]) is True
    assert almacen.obtener(item["id"]) is None


def test_buscar():
    almacen._datos.clear()
    almacen.crear({{"titulo": "pastel de chocolate"}})
    almacen.crear({{"titulo": "ensalada"}})
    assert len(almacen.buscar("pastel")) == 1
'''


def readme(nombre, dom):
    return f'''# {nombre}
Generado automáticamente por NCT (embudo → design system → boilerplate).

## Correr el backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Correr el frontend
Abrir `frontend/index.html` en el navegador (el backend debe estar en :8000).

## Tests
```
python -m pytest tests/
```
Dominio: **{dom}** · Stack: FastAPI + React
'''
