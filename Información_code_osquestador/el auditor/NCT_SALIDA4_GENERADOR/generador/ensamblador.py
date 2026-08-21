"""GENERADOR PARTE 2B — COMPONENTES UI + ENSAMBLADOR (cierre de S09).
ComponentesUI: por cada entidad genera formulario + lista en HTML/JS puro
(consume la API generada, paleta del Design System G1).
Ensamblador: LA función que responde la gran auditoría — toma una IDEA y
produce una APP COMPLETA VERIFICADA: embudo → design system → boilerplate →
DB → API → UI → tests generados → compilación probada. Con acta.
"""
from __future__ import annotations
import os
import py_compile
import subprocess
import sys

from generador.embudo import procesar_idea
from generador.design_system import generar_tokens
from generador.db_api_generator import (esquema_de, generar_modelos,
                                        generar_api, generar_tests_api)


def generar_componente_ui(entidad: str, campos: list, color: str) -> str:
    inputs = "\n".join(
        f'      <input id="f-{n}" placeholder="{n}" '
        f'type="{"number" if t in ("INTEGER", "REAL") else "text"}">'
        for n, t in campos)
    js_campos = ", ".join(
        f"{n}: " + (f"+v('f-{n}')" if t in ("INTEGER", "REAL")
                    else f"v('f-{n}')") for n, t in campos)
    fila = " · ".join(f"${{x.{n}}}" for n, _ in campos)
    return f"""<!-- componente generado: {entidad} -->
<section class="ent" id="sec-{entidad}">
  <h2>{entidad.capitalize()}s</h2>
  <form class="alta" onsubmit="return crear_{entidad}(event)">
{inputs}
      <button style="background:{color}">Agregar</button>
  </form>
  <ul id="lista-{entidad}"></ul>
</section>
<script>
function v(id){{return document.getElementById(id).value}}
async function cargar_{entidad}(){{
  const r = await fetch('/{entidad}s'); const xs = await r.json();
  document.getElementById('lista-{entidad}').innerHTML = xs.map(x =>
    `<li>#${{x.id}} {fila}
     <button onclick="borrar_{entidad}(${{x.id}})">✕</button></li>`).join('');
}}
async function crear_{entidad}(e){{
  e.preventDefault();
  await fetch('/{entidad}s', {{method:'POST',
    headers:{{'Content-Type':'application/json'}},
    body: JSON.stringify({{{js_campos}}})}});
  cargar_{entidad}(); return false;
}}
async function borrar_{entidad}(id){{
  await fetch(`/{entidad}s/${{id}}`, {{method:'DELETE'}});
  cargar_{entidad}();
}}
cargar_{entidad}();
</script>
"""


def generar_index(nombre: str, componentes: list[str], tokens: dict) -> str:
    c = tokens.get("colores", {})
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{nombre}</title>
<style>
body{{font-family:system-ui;background:{c.get('fondo', '#111')};
  color:{c.get('texto', '#eee')};max-width:760px;margin:0 auto;padding:24px}}
h1{{font-size:26px}} h2{{font-size:18px;margin:18px 0 8px}}
.alta{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}}
input{{padding:8px;border-radius:8px;border:1px solid #444;
  background:{c.get('superficie', '#222')};color:inherit}}
button{{padding:8px 14px;border-radius:8px;border:none;color:#fff;cursor:pointer}}
ul{{list-style:none;padding:0}} li{{padding:7px 10px;border-bottom:1px solid #333}}
</style></head><body>
<h1>{nombre}</h1>
{''.join(componentes)}
</body></html>
"""


def ensamblar_app(idea: str, destino: str) -> dict:
    """LA FUNCIÓN DE LA AUDITORÍA: idea → app completa verificada + acta."""
    acta = {"idea": idea, "pasos": [], "verificaciones": {}, "ok": False}

    # 1. Embudo (G1)
    req = procesar_idea(idea)
    acta["pasos"].append("embudo: requisitos.json generado")
    # 2. Design system (G1)
    tokens = generar_tokens(req)
    acta["pasos"].append("design_system: tokens generados")
    # 3. Esquema + código
    esquema = esquema_de(req)
    nombre = req["proyecto"]["nombre"]
    os.makedirs(destino, exist_ok=True)
    archivos = {
        "modelos.py": generar_modelos(esquema),
        "api.py": generar_api(esquema, nombre),
        "test_app_generada.py": generar_tests_api(esquema),
        "index.html": generar_index(
            nombre,
            [generar_componente_ui(e, c, tokens.get("colores", {})
                                   .get("primario", "#CC785C"))
             for e, c in esquema.items()],
            tokens),
        "requisitos.json": __import__("json").dumps(
            req, ensure_ascii=False, indent=2),
    }
    for nombre_a, contenido in archivos.items():
        with open(os.path.join(destino, nombre_a), "w",
                  encoding="utf-8") as f:
            f.write(contenido)
    acta["pasos"].append(f"generados {len(archivos)} archivos "
                         f"({len(esquema)} entidades)")

    # 4. VERIFICACIÓN REAL — compilación
    for py in ("modelos.py", "api.py", "test_app_generada.py"):
        try:
            py_compile.compile(os.path.join(destino, py), doraise=True)
            acta["verificaciones"][f"compila:{py}"] = True
        except py_compile.PyCompileError as e:
            acta["verificaciones"][f"compila:{py}"] = str(e)

    # 5. VERIFICACIÓN REAL — los tests generados CORREN
    r = subprocess.run([sys.executable, "-m", "pytest",
                        "test_app_generada.py", "-q"],
                       cwd=destino, capture_output=True, text=True,
                       timeout=120)
    acta["verificaciones"]["tests_generados"] = \
        "PASS" if r.returncode == 0 else r.stdout[-500:]

    acta["ok"] = all(v is True or v == "PASS"
                     for v in acta["verificaciones"].values())
    acta["entidades"] = sorted(esquema)
    acta["archivos"] = sorted(archivos)
    return acta
