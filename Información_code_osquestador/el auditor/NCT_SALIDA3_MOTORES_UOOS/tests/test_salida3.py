"""TESTS SALIDA 3 — Motor TEMA A + Motor TEMA B + Fusión Juez + Vigilante."""
import sys, os, asyncio
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from uoos.motor_tema_a import generar_uoos_parte1
from uoos.motor_tema_b import generar_uoos_parte2
from orquestador.juez_fusion_y_vigilante import (JuezKernel, Vigilante30s,
                                                 PASOS_POR_FASE)
from tribunal.juez_16_pasos import SECUENCIA_16

DOC_DEMO = """# Proyecto Tienda Verde

## Fase de diseño
La app debe permitir registro de usuarios. El backend `api/main.py` requiere
autenticación JWT. Nunca se guardan contraseñas en claro.

## Fase de construcción
Se construye `web/index.html` y `api/modelos.py`. Todo cambio requiere tests.

## Fase de entrega
Siempre se despliega con evidencia. El archivo `deploy/subir.sh` sube a GitHub.
"""


# ── TEMA A ──────────────────────────────────────────────────────────────
def test_tema_a_genera_uoos1_completo():
    r = generar_uoos_parte1(DOC_DEMO)
    u = r["uoos"]
    assert u["manifest"]["proyecto"] == "Proyecto Tienda Verde"
    assert u["manifest"]["fases"] == 3
    assert "api/main.py" in u["inventario"] and "deploy/subir.sh" in u["inventario"]
    assert any("Nunca" in req or "requiere" in req for req in u["requisitos"])
    assert u["dag"][1]["depende_de"] == ["F00"]     # cadena secuencial
    assert "## B4 — DAG DE FASES" in r["markdown"]


def test_tema_a_determinista():
    a = generar_uoos_parte1(DOC_DEMO)
    b = generar_uoos_parte1(DOC_DEMO)
    assert a["uoos"] == b["uoos"] and a["markdown"] == b["markdown"]


def test_tema_a_sirve_para_cualquier_proyecto():
    otro = "# Blog de Cocina\n\n## Único paso\nCrear `posts.md`. Debe ser simple."
    u = generar_uoos_parte1(otro)["uoos"]
    assert u["manifest"]["proyecto"] == "Blog de Cocina"
    assert u["inventario"] == ["posts.md"]


# ── TEMA B ──────────────────────────────────────────────────────────────
def _proyecto_cerrado(tmp_path):
    (tmp_path / "app.py").write_text("print('hola')")
    (tmp_path / "test_app.py").write_text("def test_x(): assert True")
    (tmp_path / "index.html").write_text("<html></html>")
    (tmp_path / "README.md").write_text("# doc")
    (tmp_path / "datos.bin").write_bytes(b"\x00\x01")
    return str(tmp_path)


def test_tema_b_genera_uoos2(tmp_path):
    r = generar_uoos_parte2(_proyecto_cerrado(tmp_path), "tienda")
    u = r["uoos2"]
    assert u["archivos"] == 5
    assert u["tests_detectados"] == ["test_app.py"]
    assert "app.py" in u["plan_repos"]["backend"]
    assert "index.html" in u["plan_repos"]["frontend"]
    assert u["plan_repos"]["_sin_regla"] == ["datos.bin"]
    assert "NO analices" in u["orden_al_agente"]
    assert "pregunta al" in u["orden_al_agente"]    # sin_regla → Director
    assert "evidence.json" in u["orden_al_agente"]


def test_tema_b_hash_de_lote_cambia_si_cambia_codigo(tmp_path):
    c = _proyecto_cerrado(tmp_path)
    h1 = generar_uoos_parte2(c, "p")["uoos2"]["hash_lote"]
    (tmp_path / "app.py").write_text("print('cambiado')")
    h2 = generar_uoos_parte2(c, "p")["uoos2"]["hash_lote"]
    assert h1 != h2                                 # trazabilidad real


def test_tema_b_generaliza_mas_alla_de_nct(tmp_path):
    (tmp_path / "juego.js").write_text("let x=1")
    r = generar_uoos_parte2(str(tmp_path), "mi-juego", destino="vps")
    assert r["uoos2"]["destino"] == "vps"
    assert "juego.js" in r["uoos2"]["plan_repos"]["frontend"]


# ── FUSIÓN JUEZ ─────────────────────────────────────────────────────────
def test_fusion_cubre_los_16_pasos_sin_repetir():
    todos = [p for pasos in PASOS_POR_FASE.values() for p in pasos]
    assert sorted(todos) == sorted(p[0] for p in SECUENCIA_16)
    assert len(todos) == len(set(todos)) == 16      # partición perfecta


def test_juez_kernel_pass_y_fail():
    from kernel.kernel_core import Clasificacion, Fase, ResultadoFase
    juez = JuezKernel(goal_lock=object())
    ev_ok = {p: True for p in PASOS_POR_FASE["P1_INPUT"]}
    r_ok = ResultadoFase(Fase.P1_INPUT, Clasificacion.PASS,
                         {"evidencias": ev_ok})
    assert asyncio.run(juez.veredicto(Fase.P1_INPUT, r_ok)) is Clasificacion.PASS
    assert "acta_juez" in r_ok.payload              # el acta queda adjunta
    r_mal = ResultadoFase(Fase.P1_INPUT, Clasificacion.PASS,
                          {"evidencias": {}})       # sin evidencia de P1
    v = asyncio.run(juez.veredicto(Fase.P1_INPUT, r_mal))
    assert v is not Clasificacion.PASS


def test_juez_kernel_dentro_del_kernel_fables():
    """Integración real: KernelCore corre con el juez FUSIONADO."""
    from kernel.kernel_core import (KernelCore, Enchufes, Solicitud,
                                    Clasificacion, ResultadoFase, Fase)

    class _Pipe:
        def seleccionar(self, ctx): return "p"
        async def ejecutar(self, fase, ctx):
            ev = {p: True for p in PASOS_POR_FASE[fase.value]}
            return ResultadoFase(fase, Clasificacion.PASS,
                                 {"evidencias": ev})

    class _Exp:
        async def activar(self, f, necesidades, snapshot): pass
        async def liberar(self, f): pass

    class _Est:
        def snapshot(self): return {}
        def commit(self, proposals, actor): return "c1"
        def checkpoint(self, e): return "cp"
        def verificar_hash_chain(self): return True

    class _Fus:
        def consolidar(self, p): return {"ok": True}

    class _Aud:
        def evento(self, t, d): pass

    juez = JuezKernel(goal_lock=object())
    k = KernelCore(Enchufes(pipeline=_Pipe(), expertos=_Exp(), estado=_Est(),
                            fusion=_Fus(), audit=_Aud(), juez=juez))
    resp = asyncio.run(k.procesar(Solicitud(raw={}, origen="api")))
    assert resp.clasificacion is Clasificacion.PASS  # 3 fases juzgadas por
    # el MISMO juez de 16 pasos — duplicado eliminado


# ── VIGILANTE 30s ───────────────────────────────────────────────────────
def test_vigilante_escala_tarea_atascada():
    t = [0.0]
    escaladas = []
    v = Vigilante30s(limite_s=90, escalador=lambda tid, e: escaladas.append(e),
                     reloj=lambda: t[0])
    v.registrar("T1", "generar módulo")
    t[0] = 50.0
    assert v.revisar_una_vez() == []                # aún viva
    t[0] = 95.0
    r = v.revisar_una_vez()
    assert len(r) == 1 and r[0]["task_id"] == "T1"
    assert v.estado()["T1"] == "ATASCADA" and escaladas


def test_vigilante_latido_revive():
    t = [0.0]
    v = Vigilante30s(limite_s=90, reloj=lambda: t[0])
    v.registrar("T1")
    t[0] = 95.0
    v.revisar_una_vez()
    v.latido("T1")                                  # el worker respondió
    assert v.estado()["T1"] == "VIVA"
    t[0] = 100.0
    assert v.revisar_una_vez() == []                # no re-escala


def test_vigilante_no_escala_dos_veces_seguidas():
    t = [0.0]
    n = []
    v = Vigilante30s(limite_s=10, escalador=lambda tid, e: n.append(1),
                     reloj=lambda: t[0])
    v.registrar("T1")
    t[0] = 11
    v.revisar_una_vez()
    t[0] = 12
    v.revisar_una_vez()                             # sigue ATASCADA, no repite
    assert len(n) == 1


# ── E2E: TEMA A + TEMA B en cadena (el ciclo de vida completo) ─────────
def test_E2E_ciclo_documento_a_despliegue(tmp_path):
    """Doc aprobado → UOOS1 (diseño) → [se construye] → UOOS2 (ejecutable)."""
    u1 = generar_uoos_parte1(DOC_DEMO, repos=["tienda-backend",
                                              "tienda-frontend"])
    assert u1["uoos"]["plan_despliegue"]["repos"] == ["tienda-backend",
                                                      "tienda-frontend"]
    # "construcción" simulada de lo que el UOOS1 declaró
    for a in u1["uoos"]["inventario"]:
        p = tmp_path / a
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"# construido: {a}")
    u2 = generar_uoos_parte2(str(tmp_path), "tienda")
    assert u2["uoos2"]["archivos"] == len(u1["uoos"]["inventario"])
    assert "ORDEN DE DESPLIEGUE" in u2["uoos2"]["orden_al_agente"]
