"""modelos.py — generado por NCT (determinista, SQLite puro)."""
import sqlite3
import os

DB = os.environ.get("APP_DB", "app.db")

def conexion():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def crear_tablas():
    with conexion() as c:
        c.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password_hash TEXT)")

def crear_item(nombre, descripcion):
    with conexion() as c:
        cur = c.execute("INSERT INTO item (nombre, descripcion) VALUES (?, ?)", (nombre, descripcion,))
        return cur.lastrowid

def listar_item():
    with conexion() as c:
        return [dict(r) for r in c.execute("SELECT * FROM item ORDER BY id")]

def obtener_item(id_):
    with conexion() as c:
        r = c.execute("SELECT * FROM item WHERE id=?", (id_,)).fetchone()
        return dict(r) if r else None

def borrar_item(id_):
    with conexion() as c:
        return c.execute("DELETE FROM item WHERE id=?", (id_,)).rowcount > 0

def crear_usuario(email, password_hash):
    with conexion() as c:
        cur = c.execute("INSERT INTO usuario (email, password_hash) VALUES (?, ?)", (email, password_hash,))
        return cur.lastrowid

def listar_usuario():
    with conexion() as c:
        return [dict(r) for r in c.execute("SELECT * FROM usuario ORDER BY id")]

def obtener_usuario(id_):
    with conexion() as c:
        r = c.execute("SELECT * FROM usuario WHERE id=?", (id_,)).fetchone()
        return dict(r) if r else None

def borrar_usuario(id_):
    with conexion() as c:
        return c.execute("DELETE FROM usuario WHERE id=?", (id_,)).rowcount > 0
