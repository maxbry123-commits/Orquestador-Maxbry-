"""api.py — proyecto_recetas (generado por NCT)."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import modelos

app = FastAPI(title="proyecto_recetas")

@app.on_event('startup')
def _inicio():
    modelos.crear_tablas()

@app.get('/salud')
def salud():
    return {'ok': True}

class RecetaIn(BaseModel):
    nombre: str
    ingredientes: str
    pasos: str

@app.post('/recetas')
def crear_receta(x: RecetaIn):
    nuevo_id = modelos.crear_receta(x.nombre, x.ingredientes, x.pasos)
    return {'id': nuevo_id}

@app.get('/recetas')
def listar_recetas():
    return modelos.listar_receta()

@app.get('/recetas/{id_}')
def obtener_receta(id_: int):
    r = modelos.obtener_receta(id_)
    if not r:
        raise HTTPException(404, 'receta_no_existe')
    return r

@app.delete('/recetas/{id_}')
def borrar_receta(id_: int):
    if not modelos.borrar_receta(id_):
        raise HTTPException(404, 'receta_no_existe')
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
