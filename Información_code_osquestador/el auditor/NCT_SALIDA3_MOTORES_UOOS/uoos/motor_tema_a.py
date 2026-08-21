"""🎁 TEMA A — MOTOR UOOS PARTE 1 (capacidad genérica del software).
Toma CUALQUIER documento de proyecto aprobado (Markdown) y lo convierte
automáticamente en un UOOS Parte 1 (diseño ejecutable): manifest + inventario
+ DAG de fases + plan de tribunal + plan de despliegue.
NO es solo para NCT: cualquier proyecto con un doc aprobado puede usarlo.
Determinista: mismo documento = mismo UOOS (hash incluido). 0% LLM.
"""
from __future__ import annotations
import json
import re
from hashlib import sha256


def _extraer_titulo(md: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else "PROYECTO_SIN_TITULO"


def _extraer_secciones(md: str) -> list[dict]:
    """Cada '## X' es una fase candidata del DAG."""
    partes = re.split(r"^##\s+", md, flags=re.MULTILINE)[1:]
    out = []
    for p in partes:
        lineas = p.splitlines()
        out.append({"nombre": lineas[0].strip(),
                    "cuerpo": "\n".join(lineas[1:]).strip()})
    return out


def _extraer_archivos(md: str) -> list[str]:
    """Rutas de archivo mencionadas (`x/y.py`, `z.html`, etc.)."""
    patron = r"`([\w\-/\.]+\.(?:py|html|js|json|yaml|yml|md|sh|css|sql))`"
    return sorted(set(re.findall(patron, md)))


def _extraer_requisitos(md: str) -> list[str]:
    """Bullets que suenan a requisito (debe/tiene que/requiere/nunca/siempre)."""
    req = []
    for linea in md.splitlines():
        limpia = linea.strip().lstrip("-*·").strip()
        if not limpia or len(limpia) < 12:
            continue
        if re.search(r"\b(debe|deber[áa]|tiene que|requiere|obligatorio|"
                     r"nunca|siempre|jam[áa]s|prohibido)\b",
                     limpia, re.IGNORECASE):
            req.append(limpia[:200])
    return req[:50]


def generar_uoos_parte1(md: str, proyecto: str | None = None,
                        repos: list[str] | None = None) -> dict:
    """El motor. Devuelve dict con el UOOS armado + render Markdown."""
    titulo = proyecto or _extraer_titulo(md)
    secciones = _extraer_secciones(md)
    archivos = _extraer_archivos(md)
    requisitos = _extraer_requisitos(md)
    hash_doc = sha256(md.encode()).hexdigest()

    fases = [{"id": f"F{i:02d}", "nombre": s["nombre"],
              "depende_de": [f"F{i-1:02d}"] if i else []}
             for i, s in enumerate(secciones)]

    uoos = {
        "uoos_version": "parte1/v1",
        "manifest": {
            "proyecto": titulo,
            "hash_documento_origen": hash_doc,
            "fases": len(fases),
            "archivos_declarados": len(archivos),
            "requisitos_detectados": len(requisitos),
        },
        "inventario": archivos,
        "requisitos": requisitos,
        "dag": fases,
        "plan_tribunal": {
            "secuencia": "16 pasos (P-DISCOVER→P13)",
            "inspectores": ["Sheriff", "Centinela", "Juez", "Supervisor",
                            "Validador", "Verificador"],
            "umbral": 70,
            "regla": "nada se entrega sin pasar el tribunal",
        },
        "plan_despliegue": {
            "motor": "despliegue determinista v2.0 (0% LLM)",
            "repos": repos or ["repo-principal"],
            "pasos": ["organizador_v2 --dry-run", "aprobación del Director",
                      "ejecutar plan", "verificar.py", "evidence.json"],
        },
    }
    return {"uoos": uoos, "markdown": _render_md(uoos)}


def _render_md(u: dict) -> str:
    m = u["manifest"]
    lineas = [
        f"# UOOS PARTE 1 — {m['proyecto']}",
        f"(generado por Motor TEMA A · doc origen sha256:{m['hash_documento_origen'][:16]}…)",
        "", "## B1 — MANIFEST",
        "```yaml",
        json.dumps(m, ensure_ascii=False, indent=2),
        "```", "", "## B2 — INVENTARIO",
        *([f"- `{a}`" for a in u["inventario"]]
          or ["- (sin archivos declarados)"]),
        "", "## B3 — REQUISITOS DETECTADOS",
        *[f"- {r}" for r in u["requisitos"][:20]],
        "", "## B4 — DAG DE FASES",
        "```",
        *[f"{f['id']} {f['nombre']}" +
          (f"  <- depende de {','.join(f['depende_de'])}"
           if f["depende_de"] else "  (raíz)") for f in u["dag"]],
        "```", "", "## B6 — PLAN DE TRIBUNAL",
        f"Secuencia {u['plan_tribunal']['secuencia']} · umbral "
        f"{u['plan_tribunal']['umbral']} · {u['plan_tribunal']['regla']}",
        "", "## B7 — PLAN DE DESPLIEGUE",
        " → ".join(u["plan_despliegue"]["pasos"]),
    ]
    return "\n".join(lineas) + "\n"
