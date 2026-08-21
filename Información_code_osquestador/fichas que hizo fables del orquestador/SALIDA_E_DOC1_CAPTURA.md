# SALIDA E — PIPELINE ENTRADA · DOC 1/3
# Librería de fichas DSL (tipo skills) del orquestador MAXBRY. Código de trabajo Python.
# Contenido: marco común FichaBase (enchufe v2.0) + GRUPO E1 CAPTURA (E-001..E-016).
# Regla: código compacto por ficha; el marco común hace telemetría/repetición/validación.

---

## MARCO COMÚN — `fichas/base/ficha_base.py` (~120 LOC)

**Qué hace (aplica a TODAS las fichas):** carga su contrato v2.0, valida task_id/trace_id, aplica timeout y repetición declarativa, emite telemetría y audit, y devuelve siempre `{status, proposals[], necesito[], evidencia}`.

**Instrucción Sonnet 10x (grupo):** añadir cache LRU por (ficha, hash payload), métricas Prometheus, y modo dry-run que simula sin efectos.

```python
"""FICHA_BASE — marco común. Toda ficha hereda de aquí (enchufe v2.0)."""
from __future__ import annotations
import asyncio, json, time
from hashlib import sha256
from pathlib import Path
from typing import Any


class FichaError(Exception):
    pass


class Ficha:
    ID: str = "base"
    CONTRACT: dict = {}          # subset del enchufe v2.0 relevante en runtime

    def __init__(self, audit=None, router=None, estado=None) -> None:
        self.audit, self.router, self.estado = audit, router, estado
        c = self.CONTRACT
        self.timeout = c.get("seguridad", {}).get("limites", {}) \
                        .get("timeout_ms", 30000) / 1000
        self.rep = c.get("repeticion", {"max": 1, "condicion": "nunca"})

    # ── API única ──
    async def run(self, ctx: dict, payload: dict) -> dict:
        if not ctx.get("task_id"):
            return self._fail("task_id_obligatorio")
        t0 = time.time()
        intentos = 0
        ultimo: dict = {}
        while intentos < self.rep.get("max", 1):
            intentos += 1
            try:
                ultimo = await asyncio.wait_for(
                    self.logic(ctx, dict(payload)), timeout=self.timeout)
            except asyncio.TimeoutError:
                ultimo = self._fail("timeout")
            except FichaError as exc:
                ultimo = self._fail(str(exc))
            ultimo.setdefault("status", "DONE")
            ultimo.setdefault("proposals", [])
            ultimo.setdefault("necesito", [])
            if not self._debe_repetir(ultimo):
                break
        ultimo["_ficha"] = {"id": self.ID, "ms": int((time.time()-t0)*1000),
                            "intentos": intentos}
        if self.audit:
            self.audit.evento(f"ficha.{self.ID}", {
                "task_id": ctx["task_id"], "status": ultimo["status"],
                "ms": ultimo["_ficha"]["ms"]})
        return ultimo

    def _debe_repetir(self, r: dict) -> bool:
        cond = self.rep.get("condicion", "nunca")
        if cond == "si_falla_verificacion":
            return r.get("status") == "RETRY"
        return False

    @staticmethod
    def _fail(razon: str) -> dict:
        return {"status": "FAIL", "error": razon, "proposals": []}

    @staticmethod
    def prop(path: str, value: Any, conf: float = 0.9) -> dict:
        return {"path": path, "value": value, "confidence": conf}

    # cada ficha implementa SOLO esto:
    async def logic(self, ctx: dict, payload: dict) -> dict:
        raise NotImplementedError


def hash_doc(x: Any) -> str:
    return sha256(json.dumps(x, sort_keys=True, default=str,
                             ensure_ascii=False).encode()).hexdigest()


class Registro:
    """Registry en memoria + carga de contratos JSON del disco."""
    def __init__(self) -> None:
        self.fichas: dict[str, Ficha] = {}

    def alta(self, f: Ficha) -> None:
        self.fichas[f.ID] = f

    async def correr(self, fid: str, ctx: dict, payload: dict) -> dict:
        if fid not in self.fichas:
            return {"status": "FAIL", "error": f"ficha_inexistente:{fid}"}
        return await self.fichas[fid].run(ctx, payload)
```

---

## GRUPO E1 — CAPTURA Y NORMALIZACIÓN (E-001..E-016)

**Qué hace el grupo:** convierte cualquier cosa que entre (mensaje, archivo, audio, email, captura) en UN documento canónico congelado, hasheado, limpio y trazable.
**Microdiagrama:** `escuchar ➜ sanear ➜ detectar idioma ➜ extraer adjuntos ➜ fusionar ➜ delta ➜ congelar+hash ➜ ack`
**Instrucción Sonnet 10x (grupo):** soportar streaming de archivos grandes por chunks, detección MIME real (python-magic), reintentos por canal con circuit breaker, y colas por canal con prioridad.

```python
"""fichas/entrada/e1_captura.py — E-001..E-016."""
from __future__ import annotations
import re, time, unicodedata
from pathlib import Path
from ficha_base import Ficha, FichaError, hash_doc


class E001InputListener(Ficha):
    ID = "e.entrada.input_listener"
    CANALES = ("telegram", "drive", "mcp", "api", "kanboard", "webhook")

    async def logic(self, ctx, p):
        canal = p.get("origen", "")
        if canal not in self.CANALES:
            raise FichaError(f"canal_desconocido:{canal}")
        evento = {"raw": p.get("raw"), "origen": canal,
                  "ts": time.time(), "meta": p.get("meta", {})}
        return {"proposals": [self.prop("input.evento", evento)]}


class E002NormalizerFrozen(Ficha):
    ID = "e.entrada.normalizer_frozen"

    async def logic(self, ctx, p):
        doc = {"doc_id": hash_doc(p["raw"]), "origen": p["origen"],
               "proyecto": p.get("proyecto", "default"),
               "tipo": p.get("tipo", "texto"),
               "contenido": p["raw"], "timestamp": time.time(),
               "frozen": True, "version": "1.0"}
        return {"proposals": [self.prop("input.frozen", doc)]}


class E003AckEngine(Ficha):
    ID = "e.entrada.ack_engine"

    async def logic(self, ctx, p):
        if self.router:
            await self.router.despachar(
                "notificar", {"canal": p["origen"],
                              "msg": f"RECIBIDO {p['doc_id'][:8]}"},
                trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("input.ack", True)]}


class E004HashEngine(Ficha):
    ID = "e.entrada.hash_engine"

    async def logic(self, ctx, p):
        return {"proposals": [self.prop("input.sha256",
                                        hash_doc(p["contenido"]))]}


class E005InventoryValidator(Ficha):
    ID = "e.entrada.inventory_validator"

    async def logic(self, ctx, p):
        import json
        ruta = Path(p.get("inventory", "runtime/inventory.json"))
        inv = json.loads(ruta.read_text()) if ruta.exists() else {}
        ya = p["doc_id"] in inv
        if not ya:
            inv[p["doc_id"]] = {"ts": time.time()}
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(json.dumps(inv))
        return {"proposals": [self.prop("input.duplicado", ya)],
                "status": "SKIP" if ya else "DONE"}


class E006EncodingSanitizer(Ficha):
    ID = "e.entrada.encoding_sanitizer"          # ✚ bug iPad resuelto
    INVISIBLES = dict.fromkeys(map(ord, "\u200b\u200c\u200d\u2060\ufeff"
                                        "\u00ad\u180e"))

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        t = unicodedata.normalize("NFC", t).translate(self.INVISIBLES)
        t = t.replace("\r\n", "\n").replace("\u00a0", " ")
        return {"proposals": [self.prop("input.contenido_limpio", t),
                              self.prop("input.chars_removidos",
                                        len(str(p["contenido"])) - len(t))]}


class E007IdiomaDetector(Ficha):
    ID = "e.entrada.idioma_detector"             # ✚
    PISTAS = {"es": (" el ", " que ", " para ", "ción"),
              "en": (" the ", " and ", " for ", "tion")}

    async def logic(self, ctx, p):
        t = f" {str(p['contenido']).lower()} "
        scores = {k: sum(t.count(w) for w in ws)
                  for k, ws in self.PISTAS.items()}
        idioma = max(scores, key=scores.get) if any(scores.values()) else "es"
        return {"proposals": [self.prop("input.idioma", idioma)]}


class E008AdjuntosExtractor(Ficha):
    ID = "e.entrada.adjuntos_extractor"          # ✚
    async def logic(self, ctx, p):
        hijas = []
        for adj in p.get("adjuntos", []):
            hijas.append({"parent_id": p["doc_id"],
                          "doc_id": hash_doc(adj),
                          "tipo": adj.get("tipo", "binario"),
                          "ruta": adj.get("ruta", "")})
        return {"proposals": [self.prop("input.fichas_hijas", hijas)]}


class E009MultiDocMerger(Ficha):
    ID = "e.entrada.multi_doc_merger"            # ✚
    async def logic(self, ctx, p):
        docs = p.get("docs", [])
        indice = [{"i": i, "doc_id": d["doc_id"],
                   "titulo": d.get("titulo", f"doc_{i}")}
                  for i, d in enumerate(docs)]
        corpus = "\n\n═══DOC═══\n\n".join(
            str(d.get("contenido", "")) for d in docs)
        return {"proposals": [self.prop("input.corpus", corpus),
                              self.prop("input.indice", indice)]}


class E010DeltaDetector(Ficha):
    ID = "e.entrada.delta_detector"              # ✚
    async def logic(self, ctx, p):
        import difflib
        prev, nuevo = str(p.get("previo", "")), str(p["contenido"])
        if not prev:
            return {"proposals": [self.prop("input.delta", None)]}
        difs = list(difflib.unified_diff(prev.splitlines(),
                                         nuevo.splitlines(), lineterm=""))
        return {"proposals": [self.prop("input.delta", difs[:2000]),
                              self.prop("input.delta_pct",
                                        len(difs) / max(1, len(prev
                                            .splitlines())))]}


class E011SizeGate(Ficha):
    ID = "e.entrada.size_gate"                   # ✚
    MAX_CHARS = 2_000_000

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        if len(t) <= self.MAX_CHARS:
            return {"proposals": [self.prop("input.troceado", False)]}
        trozos = [t[i:i + 500_000] for i in range(0, len(t), 500_000)]
        return {"proposals": [self.prop("input.trozos", len(trozos)),
                              self.prop("input.troceado", True)]}


class E012TimezoneNormalizer(Ficha):
    ID = "e.entrada.timezone_normalizer"         # ✚
    RE_FECHA = re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b")

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        fechas = [f"{a if len(a) == 4 else '20'+a}-{m.zfill(2)}-{d.zfill(2)}"
                  for d, m, a in self.RE_FECHA.findall(t)]
        return {"proposals": [self.prop("input.fechas_iso", fechas)]}


class E013UnitNormalizer(Ficha):
    ID = "e.entrada.unit_normalizer"             # ✚
    FACTORES = {"kb": 1024, "mb": 1024**2, "gb": 1024**3,
                "min": 60, "h": 3600, "d": 86400}

    async def logic(self, ctx, p):
        halladas = [(n, u, float(n) * self.FACTORES[u.lower()])
                    for n, u in re.findall(
                        r"(\d+(?:\.\d+)?)\s*(kb|mb|gb|min|h|d)\b",
                        str(p["contenido"]), re.I)
                    if u.lower() in self.FACTORES]
        return {"proposals": [self.prop("input.unidades_canonicas",
                                        halladas)]}


class E014VoiceToTask(Ficha):
    ID = "e.entrada.voice_to_task"               # ✚ (LLM/ASR vía Router)
    async def logic(self, ctx, p):
        r = await self.router.despachar("transcribir_audio",
                                        {"audio_ref": p["audio_ref"]},
                                        trace_id=ctx.get("trace_id", ""))
        if r["status"] != "DONE":
            raise FichaError("asr_fallo")
        return {"proposals": [self.prop("input.transcripcion",
                                        r["output"])]}


class E015ScreenshotToSpec(Ficha):
    ID = "e.entrada.screenshot_to_spec"          # ✚ (OCR + layout)
    async def logic(self, ctx, p):
        r = await self.router.despachar("ocr_layout",
                                        {"imagen_ref": p["imagen_ref"]},
                                        trace_id=ctx.get("trace_id", ""))
        if r["status"] != "DONE":
            raise FichaError("ocr_fallo")
        return {"proposals": [self.prop("input.spec_desde_imagen",
                                        r["output"])]}


class E016EmailParser(Ficha):
    ID = "e.entrada.email_parser"                # ✚
    async def logic(self, ctx, p):
        asunto = p.get("asunto", "").strip()
        cuerpo = p.get("cuerpo", "").strip()
        return {"proposals": [
            self.prop("input.goal_candidato", asunto),
            self.prop("input.contexto", cuerpo),
            self.prop("input.remitente", p.get("de", ""))]}
```

**Contratos (v2.0, patrón del grupo — 1 JSON por ficha en disco):** `categoria:pipeline · etapa:E · rol:transform · kind:code · runtime_type:compute · sandbox:process · timeout_ms:10000 · repite_en:[INPUT]`. Excepciones: E-014/E-015 `runtime_type:hybrid` (usan Router), E-005 `idempotente:true`.

**Tests del grupo:** `test_invisibles_removidos · test_duplicado_skip · test_merge_indice_correcto · test_delta_pct · test_canal_desconocido_fail · test_size_trocea`
