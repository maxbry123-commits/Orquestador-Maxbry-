"""🎁 TEMA B — MOTOR UOOS PARTE 2 (cierre → ejecutable, capacidad genérica).
Toma una carpeta de código YA CONSTRUIDO (los "vagones cerrados" de cualquier
proyecto, no solo NCT) y genera automáticamente:
  1. UOOS Parte 2: la orden ejecutable exacta para el agente (o script)
  2. El plan de despliegue determinista (generaliza el vagón F22)
  3. El checklist de evidencia que probará que se desplegó de verdad
El agente EJECUTA la orden — nunca decide. 0% LLM en la generación.
"""
from __future__ import annotations
import json
import os
from hashlib import sha256


def _inventariar(carpeta: str, ignorar=("__pycache__", ".git",
                                        ".pytest_cache", "node_modules")) -> list[dict]:
    inv = []
    for raiz, dirs, archivos in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in ignorar]
        for a in sorted(archivos):
            if a.endswith((".pyc",)):
                continue
            ruta = os.path.join(raiz, a)
            rel = os.path.relpath(ruta, carpeta)
            with open(ruta, "rb") as f:
                contenido = f.read()
            inv.append({"ruta": rel, "bytes": len(contenido),
                        "sha256": sha256(contenido).hexdigest()})
    return inv


def _detectar_tests(inv: list[dict]) -> list[str]:
    return [a["ruta"] for a in inv
            if "test" in os.path.basename(a["ruta"]).lower()
            and a["ruta"].endswith(".py")]


def _clasificar_repos(inv: list[dict], reglas: dict | None = None) -> dict:
    reglas = reglas or {
        "backend": (".py", ".sql", ".yaml", ".yml", ".toml"),
        "frontend": (".html", ".css", ".js", ".jsx"),
        "docs": (".md", ".pdf", ".txt"),
    }
    plan: dict[str, list] = {r: [] for r in reglas}
    otros = []
    for a in inv:
        destino = next((r for r, exts in reglas.items()
                        if a["ruta"].endswith(exts)), None)
        (plan[destino] if destino else otros).append(a["ruta"])
    plan["_sin_regla"] = otros
    return plan


def generar_uoos_parte2(carpeta: str, proyecto: str,
                        destino: str = "github",
                        reglas_repos: dict | None = None) -> dict:
    """El motor. Escanea la carpeta cerrada y arma la Parte 2 completa."""
    inv = _inventariar(carpeta)
    tests = _detectar_tests(inv)
    plan_repos = _clasificar_repos(inv, reglas_repos)
    hash_lote = sha256(json.dumps(
        [(a["ruta"], a["sha256"]) for a in inv],
        sort_keys=True).encode()).hexdigest()

    orden = _orden_al_agente(proyecto, tests, plan_repos, destino, hash_lote)
    evidencia = {
        "requerida": [
            "salida completa de pytest (todos PASS)",
            "hash del commit local == hash remoto (verificar.py)",
            f"conteo de archivos subidos == {len(inv)}",
            "evidence.json escrito y con ok:true",
        ],
        "regla": "SIN evidence.json NO está desplegado (patrón Witness)",
    }
    uoos2 = {
        "uoos_version": "parte2/v1",
        "proyecto": proyecto,
        "hash_lote": hash_lote,
        "archivos": len(inv),
        "tests_detectados": tests,
        "plan_repos": plan_repos,
        "destino": destino,
        "orden_al_agente": orden,
        "evidencia": evidencia,
    }
    return {"uoos2": uoos2, "markdown": _render_md(uoos2), "inventario": inv}


def _orden_al_agente(proyecto, tests, plan_repos, destino, hash_lote) -> str:
    lineas = [
        f"ORDEN DE DESPLIEGUE — {proyecto} (lote sha256:{hash_lote[:16]}…)",
        "Eres el EJECUTOR. NO analices, NO mejores, NO decidas. Pasos:",
    ]
    n = 1
    if tests:
        lineas.append(f"{n}. python -m pytest {' '.join(sorted(set(os.path.dirname(t) or '.' for t in tests)))} -q")
        lineas.append(f"   → si algo falla: DETENTE y pega la salida. No arregles nada.")
        n += 1
    for repo, archivos in plan_repos.items():
        if repo == "_sin_regla" or not archivos:
            continue
        lineas.append(f"{n}. Copia estos {len(archivos)} archivos a {proyecto}-{repo}/ "
                      f"(lista exacta en plan_repos.{repo})")
        n += 1
    if plan_repos.get("_sin_regla"):
        lineas.append(f"{n}. ARCHIVOS SIN REGLA detectados "
                      f"({len(plan_repos['_sin_regla'])}): pregunta al "
                      f"Director antes de tocarlos. NO adivines destino.")
        n += 1
    lineas += [
        f"{n}. git add -A && git commit -m '{proyecto}: lote {hash_lote[:12]}'",
        f"{n+1}. git push ({destino}) y pega la salida completa.",
        f"{n+2}. python verificar.py → confirma evidence.json ok:true.",
        f"{n+3}. DETENTE. Fin de la orden.",
    ]
    return "\n".join(lineas)


def _render_md(u: dict) -> str:
    return "\n".join([
        f"# UOOS PARTE 2 — {u['proyecto']} (EJECUTABLE)",
        f"(generado por Motor TEMA B · lote sha256:{u['hash_lote'][:16]}… · "
        f"{u['archivos']} archivos)",
        "", "## ORDEN AL AGENTE (copiar y pegar tal cual)",
        "```", u["orden_al_agente"], "```",
        "", "## PLAN DE REPOS",
        "```json", json.dumps({k: len(v) for k, v in u["plan_repos"].items()},
                              ensure_ascii=False, indent=2), "```",
        "", "## EVIDENCIA REQUERIDA",
        *[f"- {e}" for e in u["evidencia"]["requerida"]],
        "", f"**{u['evidencia']['regla']}**", "",
    ])
