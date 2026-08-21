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
        c.execute("CREATE TABLE IF NOT EXISTS receta (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, ingredientes TEXT, pasos TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password_hash TEXT)")

def crear_receta(nombre, ingredientes, pasos):
    with conexion() as c:
        cur = c.execute("INSERT INTO receta (nombre, ingredientes, pasos) VALUES (?, ?, ?)", (nombre, ingredientes, pasos,))
        return cur.lastrowid

def listar_receta():
    with conexion() as c:
        return [dict(r) for r in c.execute("SELECT * FROM receta ORDER BY id")]

def obtener_receta(id_):
    with conexion() as c:
        r = c.execute("SELECT * FROM receta WHERE id=?", (id_,)).fetchone()
        return dict(r) if r else None

def borrar_receta(id_):
    with conexion() as c:
        return c.execute("DELETE FROM receta WHERE id=?", (id_,)).rowcount > 0

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
