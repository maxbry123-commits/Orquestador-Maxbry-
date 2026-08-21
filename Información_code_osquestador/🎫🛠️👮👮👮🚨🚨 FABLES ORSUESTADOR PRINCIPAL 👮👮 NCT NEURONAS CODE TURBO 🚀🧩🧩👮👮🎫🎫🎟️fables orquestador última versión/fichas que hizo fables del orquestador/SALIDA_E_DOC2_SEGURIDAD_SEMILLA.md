# SALIDA E — PIPELINE ENTRADA · DOC 2/3
# Fichas DSL tipo skills. GRUPO E2 SEGURIDAD (E-017..E-032) + GRUPO E3 SEMILLA (E-033..E-048).

---

## GRUPO E2 — SEGURIDAD Y FILTROS (E-017..E-032)

**Qué hace el grupo:** nada sucio, peligroso o malformado pasa de aquí. Filtros axiomáticos bloqueantes, scrubbing de datos sensibles, cuarentena y wake words.
**Microdiagrama:** `A1 captura ➜ A2 axiomas(BLOQUEA) ➜ scrub PII/secretos ➜ scan inyección ➜ cuarentena? ➜ A3-A5 ➜ OCR/traducir ➜ 🛂`
**Instrucción Sonnet 10x (grupo):** listas de patrones en YAML editable por Sentinela (con aprobación), scoring combinado en vez de binario, y telemetría de falsos positivos para ajuste.

```python
"""fichas/entrada/e2_seguridad.py — E-017..E-032."""
from __future__ import annotations
import re
from ficha_base import Ficha, FichaError


class E017FiltrosA1(Ficha):
    ID = "e.seg.filtros_a1"
    async def logic(self, ctx, p):
        piezas = {"texto": bool(p.get("contenido")),
                  "adjuntos": len(p.get("adjuntos", [])),
                  "estructura_ok": isinstance(p.get("contenido"),
                                              (str, dict, list))}
        if not piezas["estructura_ok"]:
            raise FichaError("estructura_invalida")
        return {"proposals": [self.prop("seg.a1", piezas)]}


class E018FiltrosA2Axiomas(Ficha):
    ID = "e.seg.filtros_a2_axiomas"
    # AX01-08: patrones bloqueantes (editable en axiomas.yaml)
    BLOQUEA = (r"ignore (all|previous) instructions",
               r"system prompt.{0,20}(reveal|dump)",
               r"desactiva (guardian|adn|auditor)")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        hits = [rx for rx in self.BLOQUEA if re.search(rx, t)]
        if hits:
            return {"status": "FAIL",
                    "proposals": [self.prop("seg.a2_rechazo", hits)]}
        return {"proposals": [self.prop("seg.a2", "PASS")]}


class E019FiltrosA3Normalizadores(Ficha):
    ID = "e.seg.filtros_a3"
    async def logic(self, ctx, p):
        t = re.sub(r"[ \t]+", " ", str(p["contenido"])).strip()
        return {"proposals": [self.prop("seg.contenido_norm", t)]}


class E020FiltrosA4Descomponedores(Ficha):
    ID = "e.seg.filtros_a4"
    async def logic(self, ctx, p):
        bloques = [b.strip() for b in
                   re.split(r"\n{2,}|═+|─{4,}", str(p["contenido"]))
                   if b.strip()]
        return {"proposals": [self.prop("seg.bloques", bloques),
                              self.prop("seg.n_bloques", len(bloques))]}


class E021FiltrosA5Coherencia(Ficha):
    ID = "e.seg.filtros_a5"
    async def logic(self, ctx, p):
        bloques = p.get("bloques", [])
        vacios = sum(1 for b in bloques if len(b) < 3)
        score = 1.0 - vacios / max(1, len(bloques))
        return {"proposals": [self.prop("seg.coherencia", round(score, 2))],
                "status": "DONE" if score >= 0.5 else "RETRY"}


class E022PromptInjectionScanner(Ficha):
    ID = "e.seg.prompt_injection_scanner"        # ✚
    PATRONES = (r"you are now", r"act as .{0,30}without restrictions",
                r"jailbreak", r"olvida tus reglas", r"\bDAN\b")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        hits = [rx for rx in self.PATRONES if re.search(rx, t)]
        return {"proposals": [self.prop("seg.injection_hits", hits),
                              self.prop("seg.cuarentena_sugerida",
                                        bool(hits))]}


class E023PiiScrubber(Ficha):
    ID = "e.seg.pii_scrubber"                    # ✚
    RX = {"email": r"[\w.+-]+@[\w-]+\.[\w.]+",
          "telefono": r"\+?\d[\d\s-]{7,}\d",
          "tarjeta": r"\b(?:\d[ -]*?){13,16}\b"}

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        found = {}
        for k, rx in self.RX.items():
            found[k] = len(re.findall(rx, t))
            t = re.sub(rx, f"[{k.upper()}]", t)
        return {"proposals": [self.prop("seg.contenido_scrubbed", t),
                              self.prop("seg.pii_removida", found)]}


class E024SecretDetectorInput(Ficha):
    ID = "e.seg.secret_detector_input"           # ✚
    RX = (r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{30,}",
          r"AKIA[A-Z0-9]{16}", r"hf_[A-Za-z0-9]{30,}")

    async def logic(self, ctx, p):
        hits = [rx for rx in self.RX if re.search(rx, str(p["contenido"]))]
        if hits:
            return {"status": "FAIL",
                    "proposals": [self.prop("seg.secreto_detectado", True),
                                  self.prop("seg.aviso_director",
                                            "ROTA ESA CLAVE YA")]}
        return {"proposals": [self.prop("seg.secretos", 0)]}


class E025CanalFirmante(Ficha):
    ID = "e.seg.canal_firmante"                  # ✚
    async def logic(self, ctx, p):
        from hashlib import sha256
        firma = p.get("firma", "")
        esperada = sha256((p.get("secreto_canal", "") +
                           p["doc_id"]).encode()).hexdigest()
        ok = bool(firma) and firma == esperada
        return {"proposals": [self.prop("seg.canal_verificado", ok)],
                "status": "DONE" if ok or not p.get("firma_requerida")
                else "FAIL"}


class E026CuarentenaManager(Ficha):
    ID = "e.seg.cuarentena_manager"              # ✚
    async def logic(self, ctx, p):
        motivos = [m for m, v in {
            "injection": p.get("cuarentena_sugerida"),
            "malware": p.get("malware_flag"),
            "canal": p.get("canal_verificado") is False}.items() if v]
        if motivos:
            return {"status": "ESCALATE",
                    "proposals": [self.prop("seg.cuarentena",
                                            {"motivos": motivos})]}
        return {"proposals": [self.prop("seg.cuarentena", None)]}


class E027RateLimiterEntrada(Ficha):
    ID = "e.seg.rate_limiter_entrada"            # ✚
    VENTANA_S, MAX = 60, 30
    _hist: dict[str, list[float]] = {}

    async def logic(self, ctx, p):
        import time
        canal = p.get("origen", "api")
        ahora = time.time()
        h = [t for t in self._hist.get(canal, [])
             if ahora - t < self.VENTANA_S]
        h.append(ahora)
        self._hist[canal] = h
        if len(h) > self.MAX:
            return {"status": "RETRY",
                    "proposals": [self.prop("seg.rate_excedido", canal)]}
        return {"proposals": [self.prop("seg.rate", len(h))]}


class E028MalwareFlagger(Ficha):
    ID = "e.seg.malware_flagger"                 # ✚ solo marca, no analiza
    SOSPECHOSOS = (".exe", ".scr", ".bat", ".vbs", ".jar")

    async def logic(self, ctx, p):
        flags = [a.get("ruta", "") for a in p.get("adjuntos", [])
                 if a.get("ruta", "").lower().endswith(self.SOSPECHOSOS)]
        return {"proposals": [self.prop("seg.malware_flag", bool(flags)),
                              self.prop("seg.adjuntos_flag", flags)]}


class E029WakeWordEngine(Ficha):
    ID = "e.seg.wake_word_engine"
    MAPA = {"SYS_HALT": "emergency_stop", "SYS_EXECUTE": "force_exec",
            "SYS_PLAN": "force_plan", "SYS_VERIFY": "force_verify",
            "SYS_YIELD": "pause_checkpoint", "SYS_RESUME": "resume"}

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        accion = next((v for k, v in self.MAPA.items() if k in t), None)
        return {"proposals": [self.prop("seg.wake_word", accion)],
                "necesito": ["kernel_signal"] if accion else []}


class E030OcrBaidu(Ficha):
    ID = "e.seg.ocr_baidu"
    async def logic(self, ctx, p):
        r = await self.router.despachar(
            "ocr", {"imagen_ref": p["imagen_ref"], "provider": "baidu"},
            trace_id=ctx.get("trace_id", ""))
        if r["status"] != "DONE":
            r = await self.router.despachar(
                "ocr", {"imagen_ref": p["imagen_ref"],
                        "provider": "tesseract"},
                trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("seg.ocr_texto",
                                        r.get("output", ""))],
                "status": r["status"]}


class E031TraductorEntrada(Ficha):
    ID = "e.seg.traductor_entrada"               # ✚ hybrid
    async def logic(self, ctx, p):
        if p.get("idioma", "es") == "es":
            return {"proposals": [self.prop("seg.traducido", False)]}
        r = await self.router.despachar(
            "traducir", {"texto": p["contenido"], "a": "es",
                         "preservar": "terminos_tecnicos"},
            trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("seg.contenido_es", r.get(
            "output", p["contenido"]))], "status": r["status"]}


class E032InputSentinel(Ficha):
    ID = "e.seg.input_sentinel"                  # 🛂 gate de grupo
    REQUERIDOS = ("doc_id", "contenido", "a2")

    async def logic(self, ctx, p):
        faltan = [k for k in self.REQUERIDOS if not p.get(k)]
        if faltan or p.get("a2") != "PASS":
            return {"status": "FAIL",
                    "proposals": [self.prop("seg.gate", {"faltan": faltan})]}
        return {"proposals": [self.prop("seg.gate", "PASS")]}
```

---

## GRUPO E3 — ANÁLISIS SEMILLA Y HUELLAS (E-033..E-048)

**Qué hace el grupo:** fingerprint multicapa L1-L5 (detecta copia/reformulación/reorganización), pipeline Seed S1→S5 (indexa, resume, detecta huecos, pregunta, enriquece) y contexto histórico.
**Microdiagrama:** `L1..L5 huellas ➜ S1 index ➜ S2 resumen ➜ S3 gaps ➜ S4 preguntas ➜ S5 enriquecer(score) ➜ dedup ➜ contexto histórico`
**Instrucción Sonnet 10x (grupo):** embeddings reales (sentence-transformers vía Router MA-EMBED), índice incremental en sqlite FTS5, y umbral de suficiencia adaptativo por tipo de tarea.

```python
"""fichas/entrada/e3_semilla.py — E-033..E-048."""
from __future__ import annotations
import json, re, sqlite3, time
from pathlib import Path
from ficha_base import Ficha, hash_doc


class E033FpL1Lexico(Ficha):
    ID = "e.sem.fp_l1"
    async def logic(self, ctx, p):
        return {"proposals": [self.prop("sem.l1", hash_doc(p["contenido"]))]}


class E034FpL2Semantico(Ficha):
    ID = "e.sem.fp_l2"                           # hybrid: embedding via MA
    async def logic(self, ctx, p):
        r = await self.router.despachar("embed", {"texto": str(
            p["contenido"])[:8000]}, trace_id=ctx.get("trace_id", ""))
        emb = r.get("output", [])
        return {"proposals": [self.prop("sem.l2", hash_doc(
            [round(x, 3) for x in emb][:64]))], "status": r["status"]}


class E035FpL3Estructural(Ficha):
    ID = "e.sem.fp_l3"
    async def logic(self, ctx, p):
        arbol = [len(l) for l in str(p["contenido"]).splitlines()
                 if l.startswith("#") or l.isupper()]
        return {"proposals": [self.prop("sem.l3", hash_doc(arbol))]}


class E036FpL4Entidades(Ficha):
    ID = "e.sem.fp_l4"
    async def logic(self, ctx, p):
        t = str(p["contenido"])
        ents = sorted(set(re.findall(
            r"\b[A-ZÁÉÍÓÚ][\wÁÉÍÓÚáéíóú]{3,}\b", t)
            + re.findall(r"\b\d{4}-\d{2}-\d{2}\b", t)))[:200]
        return {"proposals": [self.prop("sem.l4", hash_doc(ents)),
                              self.prop("sem.entidades", ents)]}


class E037FpL5Dependencias(Ficha):
    ID = "e.sem.fp_l5"
    async def logic(self, ctx, p):
        refs = re.findall(r"\[\[([^\]]+)\]\]|doc_[a-f0-9]{6,}",
                          str(p["contenido"]))
        return {"proposals": [self.prop("sem.l5", hash_doc(refs)),
                              self.prop("sem.refs", refs)]}


class E038SeedS1Indexer(Ficha):
    ID = "e.sem.seed_s1"
    async def logic(self, ctx, p):
        db = Path(p.get("db", "runtime/seed_index.sqlite"))
        db.parent.mkdir(parents=True, exist_ok=True)
        con = sqlite3.connect(db)
        con.execute("CREATE TABLE IF NOT EXISTS seed(doc_id TEXT PRIMARY "
                    "KEY, bloque INT, texto TEXT)")
        for i, b in enumerate(p.get("bloques", [])):
            con.execute("INSERT OR REPLACE INTO seed VALUES(?,?,?)",
                        (f"{p['doc_id']}:{i}", i, b[:4000]))
        con.commit(); con.close()
        return {"proposals": [self.prop("sem.indexados",
                                        len(p.get("bloques", [])))]}


class E039SeedS2Summarizer(Ficha):
    ID = "e.sem.seed_s2"                         # hybrid
    async def logic(self, ctx, p):
        r = await self.router.despachar("resumir", {
            "texto": str(p["contenido"])[:12000], "max_palabras": 150},
            trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("sem.resumen",
                                        r.get("output", ""))],
                "status": r["status"]}


class E040SeedS3GapDetector(Ficha):
    ID = "e.sem.seed_s3"
    CAMPOS = ("objetivo", "dod", "alcance", "recursos", "deadline")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        gaps = [c for c in self.CAMPOS if c not in t]
        return {"proposals": [self.prop("sem.gaps", gaps)]}


class E041SeedS4Questions(Ficha):
    ID = "e.sem.seed_s4"
    PLANTILLA = {"objetivo": "¿Cuál es el objetivo exacto?",
                 "dod": "¿Cómo sabremos que está terminado (DoD)?",
                 "alcance": "¿Qué queda FUERA del alcance?",
                 "recursos": "¿Qué recursos/keys hay disponibles?",
                 "deadline": "¿Para cuándo?"}

    async def logic(self, ctx, p):
        qs = [self.PLANTILLA[g] for g in p.get("gaps", [])
              if g in self.PLANTILLA]
        return {"proposals": [self.prop("sem.preguntas", qs)]}


class E042SeedS5Enricher(Ficha):
    ID = "e.sem.seed_s5"
    async def logic(self, ctx, p):
        cov = 1 - len(p.get("gaps", [])) / 5
        cons = p.get("coherencia", 0.5)
        div = min(1.0, len(p.get("entidades", [])) / 40)
        rec = 1.0
        score = round(0.35*cov + 0.25*cons + 0.20*div + 0.20*rec, 3)
        return {"proposals": [
            self.prop("sem.evidence_score", score),
            self.prop("sem.veredicto",
                      "PROCEED" if score >= 0.85 else "NEEDS_MORE_INFO")]}


class E043DedupSemantico(Ficha):
    ID = "e.sem.dedup_stream"                    # ✚
    _ventana: dict[str, float] = {}

    async def logic(self, ctx, p):
        l2, ahora = p.get("l2", ""), time.time()
        self._ventana = {k: v for k, v in self._ventana.items()
                         if ahora - v < 86400}
        dup = l2 in self._ventana
        self._ventana[l2] = ahora
        return {"proposals": [self.prop("sem.dup_semantico", dup)],
                "status": "SKIP" if dup else "DONE"}


class E044NerGlosario(Ficha):
    ID = "e.sem.ner_glosario"                    # ✚
    async def logic(self, ctx, p):
        ents = p.get("entidades", [])
        glosario = {e: str(p["contenido"]).lower().count(e.lower())
                    for e in ents[:60]}
        top = dict(sorted(glosario.items(), key=lambda x: -x[1])[:25])
        return {"proposals": [self.prop("sem.glosario", top)]}


class E045SimilarityPastTasks(Ficha):
    ID = "e.sem.similarity_past"                 # ✚
    async def logic(self, ctx, p):
        snap = self.estado.snapshot() if self.estado else {}
        tareas = snap.get("tareas", {})
        ents = set(p.get("entidades", []))
        sim = [{"task": tid, "overlap": len(ents & set(
            t.get("entidades", [])))} for tid, t in tareas.items()]
        sim = sorted([s for s in sim if s["overlap"] > 2],
                     key=lambda x: -x["overlap"])[:5]
        return {"proposals": [self.prop("sem.tareas_similares", sim)]}


class E046ContextoHistoricoFetcher(Ficha):
    ID = "e.sem.contexto_historico"              # ✚
    async def logic(self, ctx, p):
        r = await self.router.despachar(
            "memoria.buscar", {"query": p.get("entidades", [])[:10]},
            trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("sem.historico",
                                        r.get("output", []))]}


class E047InputSchemaInferencer(Ficha):
    ID = "e.sem.schema_inferencer"               # ✚
    async def logic(self, ctx, p):
        def tipo(v):
            return ("object" if isinstance(v, dict) else
                    "array" if isinstance(v, list) else
                    "number" if isinstance(v, (int, float)) else "string")
        c = p["contenido"]
        schema = ({"type": "object", "properties":
                   {k: {"type": tipo(v)} for k, v in c.items()}}
                  if isinstance(c, dict) else {"type": tipo(c)})
        return {"proposals": [self.prop("sem.schema_inferido", schema)]}


class E048AmbiguedadScorer(Ficha):
    ID = "e.sem.ambiguedad_scorer"               # ✚
    VAGAS = ("algo", "cosas", "etc", "lo que sea", "no sé", "quizás",
             "tal vez", "mejorar", "optimizar")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        score = min(1.0, sum(t.count(v) for v in self.VAGAS) / 5)
        return {"proposals": [
            self.prop("sem.ambiguedad", round(score, 2)),
            self.prop("sem.necesita_preguntas", score >= 0.4)]}
```

**Contratos del doc:** E2 → `sandbox:process`, E-018/E-024/E-032 `bloqueante:true` (FAIL corta el pipeline), E-026 puede ESCALATE. E3 → E-034/E-039/E-046 `runtime_type:hybrid`. Todos `repite_en:[INPUT, CONTEXT_LOADER]`, `repeticion:{max:2, condicion:si_falla_verificacion}` en E-021/E-042.

**Tests:** `test_a2_bloquea · test_secreto_detiene_y_avisa · test_cuarentena_escalate · test_rate_ventana · test_evidence_formula · test_dedup_24h · test_ambiguedad_dispara_preguntas`
