"""api.py — proyecto_general (generado por NCT)."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import modelos

app = FastAPI(title="proyecto_general")

@app.on_event('startup')
def _inicio():
    modelos.crear_tablas()

@app.get('/salud')
def salud():
    return {'ok': True}

class ItemIn(BaseModel):
    nombre: str
    descripcion: str

@app.post('/items')
def crear_item(x: ItemIn):
    nuevo_id = modelos.crear_item(x.nombre, x.descripcion)
    return {'id': nuevo_id}

@app.get('/items')
def listar_items():
    return modelos.listar_item()

@app.get('/items/{id_}')
def obtener_item(id_: int):
    r = modelos.obtener_item(id_)
    if not r:
        raise HTTPException(404, 'item_no_existe')
    return r

@app.delete('/items/{id_}')
def borrar_item(id_: int):
    if not modelos.borrar_item(id_):
        raise HTTPException(404, 'item_no_existe')
    return {'borrado': True}

class UsuarioIn(BaseModel):
    email: str
    password_hash: str

@app.post('/usuarios')
def crear_usuario(x: UsuarioIn):
    nuevo_id = modelos.crear_usuario(x.email, x.password_hash)
    return {'id': nuevo_id}

@app.get('/usuarios')
def listar_usuarios():
    return modelos.listar_usuario()

@app.get('/usuarios/{id_}')
def obtener_usuario(id_: int):
    r = modelos.obtener_usuario(id_)
    if not r:
        raise HTTPException(404, 'usuario_no_existe')
    return r

@app.delete('/usuarios/{id_}')
def borrar_usuario(id_: int):
    if not modelos.borrar_usuario(id_):
        raise HTTPException(404, 'usuario_no_existe')
    return {'borrado': True}
