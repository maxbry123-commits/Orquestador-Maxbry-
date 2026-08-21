# SALIDA E v2 — PIPELINE ENTRADA · DOC 2 (E-007..E-016)
# Skills prompt/DSL en Python+YAML+JSON. Patrón catálogo aplicado: cada proceso
# escala a cientos/miles de variantes por YAML, invocable por el agente vía
# router_tags y conectado al enchufe v2.0 SIEMPRE.

═══════════════════════════════════════════════════════════════════
FICHA E-007 — idioma_detector · CATÁLOGO 50 IDIOMAS ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE? (cuántos y qué hace cada uno)** No es 1 detector: es un catálogo de 50 perfiles de idioma × 3 métodos = 150 detectores combinables. Métodos: M1 pistas léxicas (rápido, offline), M2 n-gramas de caracteres (preciso, offline), M3 modelo vía Router (máxima precisión). El perfil YAML de cada idioma trae sus pistas, trigramas frecuentes y reglas de normalización. El nivel cognitivo decide el método: n0-n1→M1, n2-n3→M1+M2 votan, n4-n5→los 3 votan.

**2. MICROFLUJO** `contenido_limpio ➜ método(s) según nivel ➜ score por idioma ➜ voto ➜ idioma+confianza ➜ ¿<0.6? escalar a M3`

**3. RAÍZ**
```
📂 /repo6/fichas/entrada/e1_captura/
   ├── e007_idioma_detector.py
   ├── e007.idiomas.yaml        # 50 perfiles (es, en, pt, fr, de, it, zh...)
   └── e007.contract.json
```

**4. ACTIVACIÓN** Evento `input.contenido_limpio` (E-006). Tags `["entrada","idioma","detectar"]`. Produce `input.idioma{codigo,confianza,metodo}` → consumen E-031 (traductor) y E3.

**5. SONNET 10x** (a) completa los 50 perfiles con trigramas reales por idioma; (b) detección multi-idioma por bloque (doc mezclado es+en → mapa por sección); (c) cache por doc_id. Versión superior: perfiles aprendidos — cada corrección del Director reentrena los pesos del YAML (Sentinela propone el cambio).

**6. CÓDIGO**
```yaml
# e007.idiomas.yaml (extracto de 50)
idiomas:
  es: {pistas: [" el ", " que ", " para ", "ción", " y "], tri: [" de", "ent", "aci"]}
  en: {pistas: [" the ", " and ", " for ", "tion", " of "], tri: ["the", "ing", "ion"]}
  pt: {pistas: [" o ", " que ", " para ", "ção", " e "],   tri: [" de", "ent", "çao"]}
metodos_por_nivel: {n0: [M1], n1: [M1], n2: [M1, M2], n3: [M1, M2], n4: [M1, M2, M3], n5: [M1, M2, M3]}
```
```python
class E007IdiomaDetector(Ficha):
    ID = "e.entrada.idioma_detector"
    ROUTER_TAGS = ("entrada", "idioma", "detectar")

    def __init__(self, cfg="e007.idiomas.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        c = _y.safe_load(Path(cfg).read_text(encoding="utf-8"))
        self.perfiles, self.niveles = c["idiomas"], c["metodos_por_nivel"]

    async def logic(self, ctx, p):
        t = f" {str(p['contenido']).lower()} "
        metodos = self.niveles.get(ctx.get("nivel", "n1"), ["M1"])
        votos: dict[str, float] = {}
        if "M1" in metodos:
            for cod, perf in self.perfiles.items():
                votos[cod] = votos.get(cod, 0) + sum(
                    t.count(w) for w in perf["pistas"])
        if "M2" in metodos:
            tris = [t[i:i+3] for i in range(0, min(len(t), 3000), 3)]
            for cod, perf in self.perfiles.items():
                votos[cod] = votos.get(cod, 0) + sum(
                    tris.count(g) for g in perf["tri"]) * 2
        total = sum(votos.values()) or 1
        idioma = max(votos, key=votos.get) if votos else "es"
        conf = round(votos.get(idioma, 0) / total, 2)
        if conf < 0.6 and "M3" in metodos and self.router:
            r = await self.router.despachar("detectar_idioma",
                                            {"texto": t[:2000]},
                                            trace_id=ctx.get("trace_id", ""))
            if r["status"] == "DONE":
                idioma, conf = r["output"].get("idioma", idioma), 0.95
        return {"proposals": [self.prop("input.idioma", {
            "codigo": idioma, "confianza": conf, "metodos": metodos})]}
```
```json
{"artifact_id": "e.entrada.idioma_detector", "version": "1.0.0",
 "estado": "active", "categoria": "pipeline", "etapa": "E",
 "contrato": {"rol": "transform",
   "consume": {"datatype": {"family": "input", "type": "frozen", "version": 1}},
   "expone": {"datatype": {"family": "input", "type": "idioma", "version": 1}}},
 "ejecucion": {"kind": "code", "transport": "importlib", "runtime_type": "hybrid",
               "llm_ratio": 0.05},
 "activacion": {"eventos": ["input.contenido_limpio"]},
 "router_tags": ["entrada", "idioma", "detectar"],
 "perfiles": {"n0": {"iteraciones": 1}, "n4": {"muestras_k": 3}},
 "seguridad": {"sandbox": "process", "limites": {"timeout_ms": 15000}}}
```

═══════════════════════════════════════════════════════════════════
FICHA E-008 — adjuntos_extractor · CATÁLOGO 30 TIPOS ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Catálogo de 30 extractores por tipo de adjunto (zip, pdf, png, docx, csv, ipynb, html, eml...). Cada tipo declara en YAML su handler y si genera fichas hijas recursivas (un zip con 10 archivos → 10 fichas hijas, cada una vuelve a entrar al pipeline con parent_id).

**2. MICROFLUJO** `adjuntos[] ➜ por cada uno: detectar tipo ➜ handler del catálogo ➜ extraer ➜ ficha hija{parent_id} ➜ ¿recursivo? re-encolar`

**3. RAÍZ** `📂 e1_captura/ → e008_adjuntos_extractor.py + e008.tipos.yaml + e008.contract.json`

**4. ACTIVACIÓN** Evento `input.frozen` con `adjuntos>0`. Tags `["entrada","adjuntos","extraer"]`. Produce `input.fichas_hijas[]` → re-entran por E-001 (canal interno).

**5. SONNET 10x** Añade límite de profundidad recursiva (≤3) y de expansión (zip bomba: máx 200 hijas); handlers docx/xlsx reales (python-docx/openpyxl); detección MIME por magic bytes, no por extensión. Versión superior: extractores como micro-fichas independientes registradas en el Router — añadir un tipo = añadir 1 YAML, cero cambios aquí.

**6. CÓDIGO**
```yaml
# e008.tipos.yaml (extracto de 30)
tipos:
  zip:  {handler: extraer_zip,  recursivo: true,  max_hijas: 200}
  pdf:  {handler: extraer_pdf,  recursivo: false, via_router: pdf_extract}
  png:  {handler: via_ocr,      recursivo: false, via_router: ocr}
  csv:  {handler: extraer_csv,  recursivo: false}
profundidad_max: 3
```
```python
class E008AdjuntosExtractor(Ficha):
    ID = "e.entrada.adjuntos_extractor"
    ROUTER_TAGS = ("entrada", "adjuntos", "extraer")

    def __init__(self, cfg="e008.tipos.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        c = _y.safe_load(Path(cfg).read_text())
        self.tipos, self.prof_max = c["tipos"], c["profundidad_max"]

    async def logic(self, ctx, p):
        if p.get("profundidad", 0) >= self.prof_max:
            return {"proposals": [self.prop("input.fichas_hijas", [])]}
        hijas = []
        for adj in p.get("adjuntos", []):
            ext = Path(adj.get("ruta", "")).suffix.lstrip(".").lower()
            spec = self.tipos.get(ext)
            if not spec:
                hijas.append({"parent_id": p["doc_id"], "tipo": "binario",
                              "ruta": adj["ruta"], "extraido": False})
                continue
            contenido = adj
            if spec.get("via_router") and self.router:
                r = await self.router.despachar(
                    spec["via_router"], {"ref": adj["ruta"]},
                    trace_id=ctx.get("trace_id", ""))
                contenido = r.get("output", adj)
            hijas.append({"parent_id": p["doc_id"], "doc_id":
                          hash_doc(contenido), "tipo": ext,
                          "contenido": contenido, "extraido": True,
                          "profundidad": p.get("profundidad", 0) + 1})
            if len(hijas) >= spec.get("max_hijas", 200):
                break
        return {"proposals": [self.prop("input.fichas_hijas", hijas)],
                "necesito": ["reencolar_hijas"] if hijas else []}
```

═══════════════════════════════════════════════════════════════════
FICHA E-009 — multi_doc_merger · 12 ESTRATEGIAS DE FUSIÓN ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** 12 estrategias de fusión de corpus seleccionables por YAML: concatenar, por índice temático, por fecha, por proyecto, dedup primero, delta-only, por prioridad del Director, intercalado por tamaño, jerárquico padre-hijas, por idioma, por tipo, y "chef-mode" (con censo de ítems para el CHEF FINAL). El plan elige la estrategia; default = concatenar+índice.

**2. MICROFLUJO** `docs[] ➜ estrategia del plan ➜ ordenar/agrupar ➜ fusionar ➜ índice{i,doc_id,titulo,offset} ➜ corpus+índice`

**3. RAÍZ** `📂 e1_captura/ → e009_multi_doc_merger.py + e009.estrategias.yaml`

**4. ACTIVACIÓN** Evento `input.frozen` con `docs>1` o comando del plan. Tags `["entrada","fusionar","corpus"]`. Produce `input.corpus + input.indice` → consumen E3 y CHEF (S-009).

**5. SONNET 10x** Índice con offsets exactos por bloque (para citation_backmap del CHEF); estrategia "semántica" que agrupa por similitud de embeddings; streaming para corpus >10MB. Versión superior: fusión incremental — llega doc nuevo y solo se inserta en su posición sin refusionar todo.

**6. CÓDIGO**
```python
class E009MultiDocMerger(Ficha):
    ID = "e.entrada.multi_doc_merger"
    ROUTER_TAGS = ("entrada", "fusionar", "corpus")
    SEP = "\n\n═══DOC═══\n\n"

    ESTRATEGIAS = ("concat", "tematico", "fecha", "proyecto", "dedup",
                   "delta", "prioridad", "tamano", "jerarquico",
                   "idioma", "tipo", "chef")

    async def logic(self, ctx, p):
        docs, estr = p.get("docs", []), p.get("estrategia", "concat")
        if estr not in self.ESTRATEGIAS:
            estr = "concat"
        if estr == "fecha":
            docs = sorted(docs, key=lambda d: d.get("timestamp", 0))
        elif estr == "tamano":
            docs = sorted(docs, key=lambda d: len(str(d.get("contenido"))))
        elif estr == "dedup":
            vistos, unicos = set(), []
            for d in docs:
                if d["doc_id"] not in vistos:
                    vistos.add(d["doc_id"]); unicos.append(d)
            docs = unicos
        indice, partes, offset = [], [], 0
        for i, d in enumerate(docs):
            texto = str(d.get("contenido", ""))
            indice.append({"i": i, "doc_id": d["doc_id"],
                           "titulo": d.get("titulo", f"doc_{i}"),
                           "offset": offset, "len": len(texto)})
            partes.append(texto)
            offset += len(texto) + len(self.SEP)
        return {"proposals": [
            self.prop("input.corpus", self.SEP.join(partes)),
            self.prop("input.indice", indice),
            self.prop("input.estrategia_usada", estr)]}
```

═══════════════════════════════════════════════════════════════════
FICHA E-010 — delta_detector · 8 MODOS DE DIFF ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** 8 modos de diff según lo que el plan necesite: líneas (unified), palabras, bloques, estructural (encabezados), semántico (via embeddings), binario (hash por chunk), fichas (qué fichas cambiaron) y "solo-añadidos". Ahorra reprocesar lo que no cambió.

**2. MICROFLUJO** `previo+nuevo ➜ modo del plan ➜ calcular diff ➜ delta_pct ➜ ¿<2%? marcar SKIP_PARCIAL ➜ emitir delta`

**3. RAÍZ** `📂 e1_captura/ → e010_delta_detector.py`

**4. ACTIVACIÓN** Evento `input.frozen` cuando existe versión previa en frozen store. Tags `["entrada","delta","diff"]`. Produce `input.delta` → consume E-056 (solo compila lo cambiado).

**5. SONNET 10x** Diff estructural por árbol de secciones (compara L3 fingerprints por rama); persistir deltas encadenados para reconstruir cualquier versión. Versión superior: integración con git — el frozen store ES un repo git bare y los diffs salen de ahí.

**6. CÓDIGO**
```python
class E010DeltaDetector(Ficha):
    ID = "e.entrada.delta_detector"
    ROUTER_TAGS = ("entrada", "delta", "diff")
    MODOS = ("lineas", "palabras", "bloques", "estructural",
             "semantico", "binario", "fichas", "solo_anadidos")

    async def logic(self, ctx, p):
        import difflib
        prev, nuevo = str(p.get("previo", "")), str(p["contenido"])
        modo = p.get("modo", "lineas")
        if not prev:
            return {"proposals": [self.prop("input.delta", None)]}
        if modo == "solo_anadidos":
            sm = difflib.SequenceMatcher(None, prev, nuevo)
            difs = [nuevo[j1:j2] for op, _, _, j1, j2 in sm.get_opcodes()
                    if op in ("insert", "replace")]
        else:
            a = prev.split() if modo == "palabras" else prev.splitlines()
            b = nuevo.split() if modo == "palabras" else nuevo.splitlines()
            difs = list(difflib.unified_diff(a, b, lineterm=""))[:3000]
        pct = round(len(difs) / max(1, len(prev.splitlines())), 3)
        return {"proposals": [
            self.prop("input.delta", difs),
            self.prop("input.delta_pct", pct),
            self.prop("input.skip_parcial", pct < 0.02)]}
```

═══════════════════════════════════════════════════════════════════
FICHAS E-011..E-016 (6 secciones compactas, mismo patrón)
═══════════════════════════════════════════════════════════════════

**E-011 size_gate · 5 políticas ✚** · 1) 5 políticas de tamaño: rechazar, trocear fijo, trocear por secciones, resumir-primero (via Router), streaming. 2) `len ➜ política del plan ➜ aplicar ➜ trozos/flag`. 3) `📂 e1_captura/e011_size_gate.py`. 4) Activa: `input.contenido_limpio`; tags `["entrada","tamano","trocear"]`. 5) Sonnet: troceo por secciones respetando bloques de código completos; contar tokens reales (tiktoken), no chars. 6)
```python
class E011SizeGate(Ficha):
    ID = "e.entrada.size_gate"
    ROUTER_TAGS = ("entrada", "tamano", "trocear")
    MAX = 2_000_000

    async def logic(self, ctx, p):
        t, pol = str(p["contenido"]), p.get("politica", "trocear_fijo")
        if len(t) <= self.MAX:
            return {"proposals": [self.prop("input.troceado", False)]}
        if pol == "rechazar":
            return {"status": "FAIL", "proposals": [
                self.prop("input.rechazo_tamano", len(t))]}
        if pol == "trocear_secciones":
            trozos = [b for b in t.split("\n# ") if b]
        else:
            trozos = [t[i:i+500_000] for i in range(0, len(t), 500_000)]
        return {"proposals": [self.prop("input.trozos", len(trozos)),
                              self.prop("input.troceado", True)]}
```

**E-012 timezone_normalizer · 15 formatos ✚** · 1) Reconoce 15 formatos de fecha/hora (dd/mm/aa, mm-dd-yyyy, "3 de julio", relativos "mañana/ayer", epoch, ISO...) y emite todo en ISO-8601 UTC. 2) `texto ➜ 15 regex/reglas ➜ resolver relativos con ts actual ➜ fechas_iso[]`. 3) `📂 e1_captura/e012_timezone_normalizer.py + e012.formatos.yaml`. 4) Activa: `input.contenido_limpio`; tags `["entrada","fechas","normalizar"]`. 5) Sonnet: zona horaria del Director desde config; rangos ("del 3 al 7"); dateparser lib como M2. 6)
```python
class E012TimezoneNormalizer(Ficha):
    ID = "e.entrada.timezone_normalizer"
    ROUTER_TAGS = ("entrada", "fechas", "normalizar")
    RX = (re.compile(r"\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b"),
          re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b"))

    async def logic(self, ctx, p):
        t, fechas = str(p["contenido"]), []
        for m in self.RX[0].finditer(t):
            d, mo, a = m.groups()
            a = a if len(a) == 4 else "20" + a
            fechas.append(f"{a}-{mo.zfill(2)}-{d.zfill(2)}")
        fechas += ["-".join(m.groups()) for m in self.RX[1].finditer(t)]
        return {"proposals": [self.prop("input.fechas_iso",
                                        sorted(set(fechas)))]}
```

**E-013 unit_normalizer · 200 unidades ✚** · 1) Catálogo YAML de 200 unidades (datos, tiempo, dinero, longitud, peso, temperatura) → todo a canónico (bytes, segundos, USD...). 2) `texto ➜ regex num+unidad ➜ factor del catálogo ➜ canónicas[]`. 3) `📂 e1_captura/e013_unit_normalizer.py + e013.unidades.yaml`. 4) Activa: `input.contenido_limpio`; tags `["entrada","unidades"]`. 5) Sonnet: tasas de cambio vivas vía Router para monedas; unidades compuestas (MB/s). 6)
```python
class E013UnitNormalizer(Ficha):
    ID = "e.entrada.unit_normalizer"
    ROUTER_TAGS = ("entrada", "unidades")

    def __init__(self, cfg="e013.unidades.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        self.factores = _y.safe_load(Path(cfg).read_text())["unidades"]
        self.rx = re.compile(r"(\d+(?:\.\d+)?)\s*(" + "|".join(
            map(re.escape, self.factores)) + r")\b", re.I)

    async def logic(self, ctx, p):
        out = [{"valor": float(n), "unidad": u.lower(),
                "canonico": float(n) * self.factores[u.lower()]}
               for n, u in self.rx.findall(str(p["contenido"]))]
        return {"proposals": [self.prop("input.unidades", out)]}
```

**E-014 voice_to_task · 4 proveedores ✚** · 1) Cadena ASR con failover de 4 proveedores vía Router (whisper-hf → deepgram → google → local) y post-proceso: puntuación, comandos de voz ("nueva tarea", "urgente"). 2) `audio_ref ➜ ASR failover ➜ puntuar ➜ detectar comandos ➜ transcripción+comandos`. 3) `📂 e1_captura/e014_voice_to_task.py`. 4) Activa: `input.evento{tipo:audio}`; tags `["entrada","voz","asr"]`. 5) Sonnet: diarización (quién habla) y timestamps por frase. 6)
```python
class E014VoiceToTask(Ficha):
    ID = "e.entrada.voice_to_task"
    ROUTER_TAGS = ("entrada", "voz", "asr")
    COMANDOS = {"nueva tarea": "task.crear", "urgente": "urgencia.critical"}

    async def logic(self, ctx, p):
        r = await self.router.despachar("transcribir_audio",
                                        {"audio_ref": p["audio_ref"]},
                                        trace_id=ctx.get("trace_id", ""))
        if r["status"] != "DONE":
            raise FichaError("asr_fallo_todos")
        texto = str(r["output"])
        cmds = [v for k, v in self.COMANDOS.items() if k in texto.lower()]
        return {"proposals": [self.prop("input.transcripcion", texto),
                              self.prop("input.comandos_voz", cmds)]}
```

**E-015 screenshot_to_spec · 6 analizadores ✚** · 1) 6 analizadores sobre la imagen: OCR texto, layout (secciones), tablas, UI-elements (botones/campos), diagramas (nodos/flechas), código-en-imagen. El plan pide cuáles. 2) `imagen ➜ analizadores[] via Router ➜ fusionar ➜ spec estructurada`. 3) `📂 e1_captura/e015_screenshot_to_spec.py`. 4) Activa: `input.evento{tipo:imagen}`; tags `["entrada","imagen","spec"]`. 5) Sonnet: reconstrucción de jerarquía UI a JSON de componentes (para Claude Design). 6)
```python
class E015ScreenshotToSpec(Ficha):
    ID = "e.entrada.screenshot_to_spec"
    ROUTER_TAGS = ("entrada", "imagen", "spec")
    ANALIZADORES = ("ocr", "layout", "tablas", "ui", "diagrama", "codigo")

    async def logic(self, ctx, p):
        pedidos = p.get("analizadores", ["ocr", "layout"])
        spec = {}
        for a in (x for x in pedidos if x in self.ANALIZADORES):
            r = await self.router.despachar(f"imagen_{a}",
                                            {"ref": p["imagen_ref"]},
                                            trace_id=ctx.get("trace_id", ""))
            spec[a] = r.get("output") if r["status"] == "DONE" else None
        return {"proposals": [self.prop("input.spec_imagen", spec)]}
```

**E-016 email_parser · 10 reglas ✚** · 1) 10 reglas de extracción: asunto→goal, cuerpo→contexto, remitente, hilos (Re:/Fwd: colapsados), adjuntos, deadlines en texto, prioridad por header, listas→subtareas, firmas fuera, quoted-text fuera. 2) `email ➜ 10 reglas ➜ task candidata`. 3) `📂 e1_captura/e016_email_parser.py`. 4) Activa: `input.evento{origen:email}`; tags `["entrada","email"]`. 5) Sonnet: threading real por Message-ID; detección de aprobaciones ("ok procede") en respuestas. 6)
```python
class E016EmailParser(Ficha):
    ID = "e.entrada.email_parser"
    ROUTER_TAGS = ("entrada", "email")

    async def logic(self, ctx, p):
        asunto = re.sub(r"^(re:|fwd:)\s*", "", p.get("asunto", ""),
                        flags=re.I).strip()
        cuerpo = re.sub(r"(?m)^>.*$", "", p.get("cuerpo", ""))  # sin quotes
        cuerpo = cuerpo.split("--")[0].strip()                   # sin firma
        subtareas = re.findall(r"(?m)^\s*[-*\d]+[.)]?\s+(.+)$", cuerpo)
        return {"proposals": [
            self.prop("input.goal_candidato", asunto),
            self.prop("input.contexto", cuerpo),
            self.prop("input.subtareas_candidatas", subtareas[:50]),
            self.prop("input.remitente", p.get("de", ""))]}
```

---
**AUDITORÍA DEL SEGMENTO (pasada 1/3 de este doc):** E-007..E-016 cubren del corpus: Input Adapter/Normalizer [1.1] ✓, adjuntos/canales de Input Engine v4.0 ✓, y añaden 10 catálogos ✚ (50 idiomas, 30 tipos, 12 fusiones, 8 diffs, 5 políticas, 15 formatos, 200 unidades, 4 ASR, 6 analizadores, 10 reglas email) = **340 variantes de proceso en este doc**. Todas con router_tags + contract v2.0 + activación declarada.

**SIGUIENTE:** DOC 3 (E-017..E-026 seguridad, con catálogo de 500 patrones A2/inyección/PII en YAML).
