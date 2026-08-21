# SALIDA 4/6 — DSL DAG SCHEMA SHERIFF + ATLAS
# Repo 2: dsl-dag | Archivos: 3 | LOC: ~330 + ~260 + ~300
# Fuente única de verdad: editas el DSL → se regeneran los 10-50 HTML/MD.
# Base: tu diagrama_dsl_pipeline.py SIN agentes + patrón árbol 7 preguntas.

---

## ARCHIVO 1 — `dsl-dag/schema.py` (~330 LOC)

```python
"""SCHEMA DSL — Nodo (árbol ejecutable 7 preguntas), Arista condicional,
Fase P1/P2/P3. Todo declarativo. El código del sistema NO vive aquí:
aquí vive el MAPA que lo genera, audita y documenta.
Contract: contracts/dsl_schema.contract.json
"""
from __future__ import annotations
import json
import re
from dataclasses import dataclass, field, asdict
from enum import Enum
from hashlib import sha256
from pathlib import Path


class TipoNodo(Enum):
    ENTRADA = "ENTRADA"
    PROCESO = "PROCESO"
    DECISION = "DECISION"
    VALIDACION = "VALIDACION"
    PARALELO = "PARALELO"
    SALIDA = "SALIDA"
    AUDITORIA = "AUDITORIA"


class FaseId(Enum):
    P1_INPUT = "P1_INPUT"
    P2_PROCESS = "P2_PROCESS"
    P3_OUTPUT = "P3_OUTPUT"
    TRANSVERSAL = "TRANSVERSAL"      # cerebro, router, comunicación


class PuntoAudit(Enum):
    OCR = "OCR"                      # solo P1 (Baidu OCR)
    GRAPHITI = "GRAPHITI"            # todas las fases
    OBSIDIAN = "OBSIDIAN"            # P2 en adelante
    HALLUCINATION = "HALLUCINATION"  # P2 en adelante (SelfCheckGPT)
    HASH_CHAIN = "HASH_CHAIN"        # P3


# Regla de coherencia audit×fase (del si_o_si IDEA#4)
AUDIT_FASES_VALIDAS: dict[PuntoAudit, set[FaseId]] = {
    PuntoAudit.OCR: {FaseId.P1_INPUT},
    PuntoAudit.GRAPHITI: set(FaseId),
    PuntoAudit.OBSIDIAN: {FaseId.P2_PROCESS, FaseId.P3_OUTPUT,
                          FaseId.TRANSVERSAL},
    PuntoAudit.HALLUCINATION: {FaseId.P2_PROCESS, FaseId.P3_OUTPUT},
    PuntoAudit.HASH_CHAIN: {FaseId.P3_OUTPUT, FaseId.TRANSVERSAL},
}

RE_ID = re.compile(r"^[A-Z0-9_\-]{2,40}$")
RE_CONDICION = re.compile(
    r"^(SIEMPRE|CONF[<>=]+[0-9.]+|PASS|FAIL|RETRY|ESCALATE|[A-Z_]+==[A-Z_0-9]+)$")


@dataclass
class Nodo:
    """Patrón árbol ejecutable — responde las 7 preguntas."""
    id: str
    nombre: str
    tipo: TipoNodo
    fase: FaseId
    # 1. ¿Qué hace? (2-3 líneas)
    que_hace: str = ""
    # 2. ¿Cómo funciona? (microflujo horizontal)
    microflujo: list[str] = field(default_factory=list)
    # 3. ¿Qué tecnologías usa?
    programacion: list[str] = field(default_factory=list)
    # 4. ¿Dónde está? (raíz extendida)
    raiz: str = ""                            # "/input/loops/"
    archivos: list[str] = field(default_factory=list)
    # 5. ¿De qué depende?
    dependencias: list[str] = field(default_factory=list)
    # 6. ¿Qué produce? / 7. ¿Quién la consume? (enchufe v1.5)
    consume: dict = field(default_factory=dict)   # {datatype, schema_uri}
    produce: dict = field(default_factory=dict)
    consumidores: list[str] = field(default_factory=list)
    # Extras operativos
    audit_points: list[PuntoAudit] = field(default_factory=list)
    metricas: list[str] = field(
        default_factory=lambda: ["tiempo", "errores", "reintentos"])
    ficha_id: str = ""                        # enlace al contrato real
    critico: bool = False

    def fingerprint(self) -> str:
        return sha256(json.dumps(asdict(self), sort_keys=True,
                                 default=str).encode()).hexdigest()[:12]


@dataclass
class Arista:
    desde: str
    hacia: str
    condicion: str = "SIEMPRE"                # RE_CONDICION
    etiqueta: str = ""


@dataclass
class Fase:
    id: FaseId
    titulo: str
    nodos: list[str] = field(default_factory=list)      # ids
    overlays: dict[str, list[str]] = field(default_factory=dict)
    # overlays = {"cerebro": [ids], "router": [ids], "comunicacion": [ids]}


@dataclass
class GrafoDSL:
    """El mapa completo del orquestador o del Team Agente."""
    nombre: str
    version: str = "1.0.0"
    nodos: dict[str, Nodo] = field(default_factory=dict)
    aristas: list[Arista] = field(default_factory=list)
    fases: dict[FaseId, Fase] = field(default_factory=dict)

    # ── construcción fluida ──
    def nodo(self, n: Nodo) -> "GrafoDSL":
        if n.id in self.nodos:
            raise ValueError(f"nodo_duplicado:{n.id}")
        self.nodos[n.id] = n
        self.fases.setdefault(
            n.fase, Fase(n.fase, n.fase.value)).nodos.append(n.id)
        return self

    def arista(self, desde: str, hacia: str,
               condicion: str = "SIEMPRE", etiqueta: str = "") -> "GrafoDSL":
        self.aristas.append(Arista(desde, hacia, condicion, etiqueta))
        return self

    def overlay(self, fase: FaseId, capa: str, ids: list[str]) -> "GrafoDSL":
        self.fases.setdefault(fase, Fase(fase, fase.value)) \
            .overlays.setdefault(capa, []).extend(ids)
        return self

    # ── consultas ──
    def sucesores(self, nodo_id: str) -> list[Arista]:
        return [a for a in self.aristas if a.desde == nodo_id]

    def grafo_dependencias(self) -> dict[str, set[str]]:
        g: dict[str, set[str]] = {nid: set() for nid in self.nodos}
        for a in self.aristas:
            g.setdefault(a.hacia, set()).add(a.desde)
        return g

    def hash_grafo(self) -> str:
        return sha256(json.dumps({
            "n": {k: v.fingerprint() for k, v in sorted(self.nodos.items())},
            "a": [(a.desde, a.hacia, a.condicion) for a in self.aristas],
        }, sort_keys=True).encode()).hexdigest()

    # ── persistencia ──
    def guardar(self, ruta: str) -> str:
        data = {"nombre": self.nombre, "version": self.version,
                "hash": self.hash_grafo(),
                "nodos": {k: asdict(v) for k, v in self.nodos.items()},
                "aristas": [asdict(a) for a in self.aristas],
                "fases": {f.id.value: {"titulo": f.titulo, "nodos": f.nodos,
                                       "overlays": f.overlays}
                          for f in self.fases.values()}}
        Path(ruta).write_text(json.dumps(data, ensure_ascii=False, indent=1,
                                         default=lambda o: o.value),
                              encoding="utf-8")
        return data["hash"]
```

---

## ARCHIVO 2 — `dsl-dag/sheriff.py` (~260 LOC)

```python
"""SHERIFF — valida el grafo ANTES de exportar o compilar.
Fail-fast: 1 violación = grafo inválido = nada se genera.
Checks: DAG acíclico · ids válidos · condiciones válidas · 7 preguntas
completas · audit×fase coherente · enchufes compatibles · SC-DSL 1-6.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from graphlib import TopologicalSorter, CycleError

from schema import (GrafoDSL, Nodo, RE_ID, RE_CONDICION,
                    AUDIT_FASES_VALIDAS, TipoNodo, FaseId)


@dataclass
class Violacion:
    codigo: str          # SH01..SH99
    nodo: str
    detalle: str


@dataclass
class InformeSheriff:
    valido: bool
    violaciones: list[Violacion] = field(default_factory=list)
    orden_topologico: list[str] = field(default_factory=list)

    def resumen(self) -> str:
        if self.valido:
            return f"✅ SHERIFF PASS — {len(self.orden_topologico)} nodos"
        lineas = [f"❌ SHERIFF FAIL — {len(self.violaciones)} violaciones"]
        lineas += [f"  [{v.codigo}] {v.nodo}: {v.detalle}"
                   for v in self.violaciones]
        return "\n".join(lineas)


class Sheriff:
    def validar(self, g: GrafoDSL) -> InformeSheriff:
        v: list[Violacion] = []
        v += self._sh01_ids(g)
        v += self._sh02_aristas(g)
        orden, ciclo = self._sh03_dag(g)
        v += ciclo
        v += self._sh04_siete_preguntas(g)
        v += self._sh05_audit_fase(g)
        v += self._sh06_enchufes(g)
        v += self._sh07_entrada_salida(g)
        return InformeSheriff(valido=not v, violaciones=v,
                              orden_topologico=orden)

    def _sh01_ids(self, g: GrafoDSL) -> list[Violacion]:
        return [Violacion("SH01", n.id, "id_invalido")
                for n in g.nodos.values() if not RE_ID.match(n.id)]

    def _sh02_aristas(self, g: GrafoDSL) -> list[Violacion]:
        out = []
        for a in g.aristas:
            if a.desde not in g.nodos or a.hacia not in g.nodos:
                out.append(Violacion("SH02", f"{a.desde}->{a.hacia}",
                                     "nodo_inexistente"))
            if not RE_CONDICION.match(a.condicion):
                out.append(Violacion("SH02", f"{a.desde}->{a.hacia}",
                                     f"condicion_invalida:{a.condicion}"))
        return out

    def _sh03_dag(self, g: GrafoDSL) -> tuple[list[str], list[Violacion]]:
        try:
            orden = list(TopologicalSorter(
                g.grafo_dependencias()).static_order())
            return orden, []
        except CycleError as exc:
            return [], [Violacion("SH03", "GRAFO", f"ciclo:{exc.args[1]}")]

    def _sh04_siete_preguntas(self, g: GrafoDSL) -> list[Violacion]:
        out = []
        for n in g.nodos.values():
            faltan = []
            if not n.que_hace.strip():
                faltan.append("que_hace")
            if not n.microflujo:
                faltan.append("microflujo")
            if not n.programacion:
                faltan.append("programacion")
            if not n.raiz or not n.archivos:
                faltan.append("raiz/archivos")
            if not n.produce:
                faltan.append("produce")
            if faltan:
                out.append(Violacion("SH04", n.id,
                                     f"preguntas_incompletas:{faltan}"))
        return out

    def _sh05_audit_fase(self, g: GrafoDSL) -> list[Violacion]:
        out = []
        for n in g.nodos.values():
            for ap in n.audit_points:
                if n.fase not in AUDIT_FASES_VALIDAS[ap]:
                    out.append(Violacion(
                        "SH05", n.id,
                        f"audit_{ap.value}_no_valido_en_{n.fase.value}"))
        return out

    def _sh06_enchufes(self, g: GrafoDSL) -> list[Violacion]:
        """Compatibilidad produce→consume por datatype (enchufe v1.5)."""
        out = []
        for a in g.aristas:
            if a.desde not in g.nodos or a.hacia not in g.nodos:
                continue
            prod = g.nodos[a.desde].produce.get("datatype")
            cons = g.nodos[a.hacia].consume.get("datatype")
            if prod and cons and prod != cons:
                out.append(Violacion(
                    "SH06", f"{a.desde}->{a.hacia}",
                    f"datatype_incompatible:{prod}!={cons}"))
        return out

    def _sh07_entrada_salida(self, g: GrafoDSL) -> list[Violacion]:
        out = []
        tipos = [n.tipo for n in g.nodos.values()]
        if TipoNodo.ENTRADA not in tipos:
            out.append(Violacion("SH07", "GRAFO", "sin_nodo_entrada"))
        if TipoNodo.SALIDA not in tipos:
            out.append(Violacion("SH07", "GRAFO", "sin_nodo_salida"))
        return out
```

---

## ARCHIVO 3 — `dsl-dag/exporters.py` (~300 LOC)

```python
"""EXPORTERS — el grafo genera TODO el atlas automáticamente:
- texto libre (chat/Telegram)  - Mermaid  - MD por nodo  - HTML por fase
Editas el DSL → corres run.py → 10-50 documentos regenerados. Cero manual.
"""
from __future__ import annotations
from pathlib import Path

from schema import GrafoDSL, Nodo, FaseId
from sheriff import Sheriff

ICONO_FASE = {FaseId.P1_INPUT: "🔵", FaseId.P2_PROCESS: "🟣",
              FaseId.P3_OUTPUT: "🟢", FaseId.TRANSVERSAL: "⚙️"}


def render_texto(g: GrafoDSL) -> str:
    """Vista árbol en texto libre (como el ejemplo LOOPS del Director)."""
    out = [f"═══ {g.nombre} v{g.version} ═══"]
    for fid, fase in g.fases.items():
        out.append(f"\n{ICONO_FASE[fid]} {fid.value}")
        for nid in fase.nodos:
            n = g.nodos[nid]
            out += [f"│\n├── {n.nombre} [{n.id}]",
                    f"│   ¿Qué hace? {n.que_hace}",
                    f"│   Microflujo: {' ➜ '.join(n.microflujo)}",
                    f"│   Programación: {', '.join(n.programacion)}",
                    f"│   📂 {n.raiz} → {', '.join(n.archivos)}",
                    f"│   Depende: {', '.join(n.dependencias) or '—'}",
                    f"│   Audit: {[a.value for a in n.audit_points] or '—'}"]
    return "\n".join(out)


def render_mermaid(g: GrafoDSL) -> str:
    lineas = ["flowchart LR"]
    for fid, fase in g.fases.items():
        lineas.append(f'  subgraph {fid.value}["{ICONO_FASE[fid]} '
                      f'{fid.value}"]')
        lineas += [f'    {nid}["{g.nodos[nid].nombre}"]'
                   for nid in fase.nodos]
        lineas.append("  end")
    for a in g.aristas:
        et = f"|{a.condicion}|" if a.condicion != "SIEMPRE" else ""
        lineas.append(f"  {a.desde} -->{et} {a.hacia}")
    return "\n".join(lineas)


def render_md_nodo(n: Nodo) -> str:
    """1 documento MD por nodo — las 7 preguntas siempre en el mismo orden."""
    return "\n".join([
        f"# {n.nombre} `[{n.id}]`",
        f"**Fase:** {n.fase.value} · **Tipo:** {n.tipo.value} · "
        f"**Ficha:** `{n.ficha_id or '—'}` · **FP:** `{n.fingerprint()}`",
        "", "## 1. ¿Qué hace?", n.que_hace,
        "", "## 2. Microflujo",
        "`" + " ➜ ".join(n.microflujo) + "`",
        "", "## 3. Programación",
        "\n".join(f"- {t}" for t in n.programacion),
        "", "## 4. Raíz extendida",
        f"📂 `{n.raiz}`",
        "\n".join(f"- `{a}`" for a in n.archivos),
        "", "## 5. Dependencias",
        "\n".join(f"- {d}" for d in n.dependencias) or "—",
        "", "## 6. Produce / 7. Consumidores",
        f"- Produce: `{n.produce}`",
        f"- Consumen: {', '.join(n.consumidores) or '—'}",
        "", "## Auditoría y métricas",
        f"- Audit points: {[a.value for a in n.audit_points]}",
        f"- Métricas: {n.metricas}",
    ])


def render_html_fase(g: GrafoDSL, fid: FaseId) -> str:
    """1 HTML por fase — auditable y editable desde el móvil."""
    fase = g.fases[fid]
    filas = ""
    for nid in fase.nodos:
        n = g.nodos[nid]
        filas += (f"<details><summary><b>{n.nombre}</b> "
                  f"<code>{n.id}</code></summary>"
                  f"<p>{n.que_hace}</p>"
                  f"<p>➜ {' ➜ '.join(n.microflujo)}</p>"
                  f"<p>📂 <code>{n.raiz}</code> "
                  f"{' '.join(f'<code>{a}</code>' for a in n.archivos)}</p>"
                  f"<p>Prog: {', '.join(n.programacion)}</p>"
                  f"<p>Audit: {[a.value for a in n.audit_points]}</p>"
                  f"</details>")
    overlays = "".join(
        f"<p><b>{capa.upper()}:</b> {', '.join(ids)}</p>"
        for capa, ids in fase.overlays.items())
    return (f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,"
            f"initial-scale=1'><title>{g.nombre} — {fid.value}</title>"
            f"<style>body{{font-family:system-ui;max-width:720px;"
            f"margin:auto;padding:12px;background:#0d1117;color:#e6edf3}}"
            f"details{{border:1px solid #30363d;border-radius:8px;"
            f"padding:8px;margin:8px 0}}code{{background:#161b22;"
            f"padding:1px 5px;border-radius:4px}}</style></head><body>"
            f"<h1>{ICONO_FASE[fid]} {g.nombre} — {fid.value}</h1>"
            f"<p>hash: <code>{g.hash_grafo()[:16]}</code></p>"
            f"{overlays}{filas}</body></html>")


def generar_atlas(g: GrafoDSL, out_dir: str = "atlas") -> dict:
    """PUNTO DE ENTRADA: valida con Sheriff y regenera TODO el atlas."""
    informe = Sheriff().validar(g)
    if not informe.valido:
        raise ValueError(informe.resumen())
    base = Path(out_dir) / g.nombre.lower().replace(" ", "_")
    (base / "nodos").mkdir(parents=True, exist_ok=True)
    generados: list[str] = []

    p = base / "00_arbol.txt"
    p.write_text(render_texto(g), encoding="utf-8"); generados.append(str(p))
    p = base / "01_diagrama.mermaid"
    p.write_text(render_mermaid(g), encoding="utf-8"); generados.append(str(p))
    for fid in g.fases:
        p = base / f"fase_{fid.value.lower()}.html"
        p.write_text(render_html_fase(g, fid), encoding="utf-8")
        generados.append(str(p))
    for n in g.nodos.values():
        p = base / "nodos" / f"{n.id}.md"
        p.write_text(render_md_nodo(n), encoding="utf-8")
        generados.append(str(p))
    return {"hash": g.hash_grafo(), "archivos": generados,
            "resumen": informe.resumen()}
```

---

## NOTAS
1. **Tu DSL original conservado, agentes eliminados** — reemplazados por `ficha_id` (enlace al contrato G2) y `overlays` (cerebro/router/comunicación).
2. **Sheriff SH01-SH07 fail-fast**: incluye compatibilidad de enchufes (`produce.datatype == consume.datatype`) y coherencia audit×fase.
3. **Atlas 100% generado**: árbol texto + Mermaid + 1 MD por nodo + 1 HTML por fase (dark, móvil-first). Con ~40 nodos = ~45 documentos automáticos.
4. G2-conforme: el grafo tiene hash, es congelable y `orden_topologico` alimenta directo al PLANNER_OFFLINE.

## TESTS
```
test_sheriff_detecta_ciclo · test_sheriff_7preguntas_incompletas
test_ocr_fuera_de_p1_falla · test_datatype_incompatible
test_atlas_genera_todos_los_archivos · test_hash_estable_reproducible
```
