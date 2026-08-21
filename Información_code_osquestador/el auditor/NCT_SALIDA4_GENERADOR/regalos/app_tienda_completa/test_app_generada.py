"""tests de la app generada — corren contra modelos.py real."""
import os, tempfile
os.environ['APP_DB'] = os.path.join(tempfile.mkdtemp(), 't.db')
import modelos

def test_tablas():
    modelos.crear_tablas()

def test_crud_item():
    modelos.crear_tablas()
    i = modelos.crear_item('nombre_demo', 'descripcion_demo')
    assert modelos.obtener_item(i) is not None
    assert any(r['id'] == i for r in modelos.listar_item())
    assert modelos.borrar_item(i) is True
    assert modelos.obtener_item(i) is None

def test_crud_usuario():
    modelos.crear_tablas()
    i = modelos.crear_usuario('email_demo', 'password_hash_demo')
    assert modelos.obtener_usuario(i) is not None
    assert any(r['id'] == i for r in modelos.listar_usuario())
    assert modelos.borrar_usuario(i) is True
    assert modelos.obtener_usuario(i) is None
