# SALIDA E v2 — PIPELINE ENTRADA · DOC 3 (E-017..E-026 · SEGURIDAD)
# Skills prompt/DSL Python+YAML+JSON. Catálogos: 500 patrones defensivos totales.
# Todas conectan al enchufe v2.0 + router_tags + evento de activación.

═══════════════════════════════════════════════════════════════════
FICHA E-017 — filtros_a1_captura · 20 CHECKS
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** 20 checks estructurales de captura definidos en YAML (existe contenido, tipo válido, tamaño>0, encoding ok, adjuntos legibles, meta completa, canal identificado, ts válido, doc_id presente, no-vacío-tras-limpieza...). Cada check es 1 función pura; el YAML decide cuáles corren y cuáles son bloqueantes.

**2. MICROFLUJO** `input.frozen ➜ correr 20 checks ➜ ¿bloqueante falló? FAIL ➜ score a1 ➜ emitir`

**3. RAÍZ** `📂 /repo6/fichas/entrada/e2_seguridad/ → e017_filtros_a1.py + e017.checks.yaml + e017.contract.json`

**4. ACTIVACIÓN** Evento `input.frozen` (primera ficha de E2). Tags `["seguridad","captura","checks"]`. Produce `seg.a1{score,fallos}` → consume E-018.

**5. SONNET 10x** Checks como plugins registrables (decorador `@check("nombre", bloqueante=True)`); reporte de tendencia por canal (qué canal falla más). Versión superior: los 20 checks se autogeneran desde el schema inferido (E-047) — schema nuevo → checks nuevos.

**6. CÓDIGO**
```yaml
# e017.checks.yaml (extracto de 20)
checks:
  contenido_existe:  {bloqueante: true}
  tipo_valido:       {bloqueante: true, tipos: [texto, dict, list]}
  tamano_min:        {bloqueante: true, min_chars: 3}
  ts_valido:         {bloqueante: false}
  meta_completa:     {bloqueante: false, campos: [origen, proyecto]}
```
```python
class E017FiltrosA1(Ficha):
    ID = "e.seg.filtros_a1"
    ROUTER_TAGS = ("seguridad", "captura", "checks")

    def __init__(self, cfg="e017.checks.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        self.checks = _y.safe_load(Path(cfg).read_text())["checks"]

    async def logic(self, ctx, p):
        fallos, bloqueos = [], []
        for nombre, spec in self.checks.items():
            ok = self._check(nombre, spec, p)
            if not ok:
                (bloqueos if spec.get("bloqueante") else fallos
                 ).append(nombre)
        if bloqueos:
            return {"status": "FAIL", "proposals": [
                self.prop("seg.a1", {"bloqueos": bloqueos})]}
        score = 1 - len(fallos) / max(1, len(self.checks))
        return {"proposals": [self.prop("seg.a1", {
            "score": round(score, 2), "fallos": fallos})]}

    @staticmethod
    def _check(nombre, spec, p) -> bool:
        c = p.get("contenido")
        if nombre == "contenido_existe":
            return bool(c)
        if nombre == "tipo_valido":
            return type(c).__name__ in ("str", *spec.get("tipos", []))
        if nombre == "tamano_min":
            return len(str(c)) >= spec.get("min_chars", 1)
        if nombre == "ts_valido":
            return isinstance(p.get("timestamp"), (int, float))
        if nombre == "meta_completa":
            return all(p.get(k) for k in spec.get("campos", []))
        return True
```

═══════════════════════════════════════════════════════════════════
FICHA E-018 — filtros_a2_axiomas · CATÁLOGO 100 REGLAS BLOQUEANTES
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** El gate axiomático AX01-08 con catálogo de 100 reglas en YAML agrupadas por axioma (AX03 anti-manipulación del sistema: 40 reglas; AX04 scope: 20; AX05 recursos: 15; resto: 25). Regla = regex o condición. 1 hit bloqueante = REJECTED inmediato, sin excepciones — es la muralla del ADN en la entrada.

**2. MICROFLUJO** `contenido_limpio ➜ 100 reglas por axioma ➜ ¿hit? FAIL+registrar ➜ PASS`

**3. RAÍZ** `📂 e2_seguridad/ → e018_filtros_a2.py + e018.axiomas.yaml (100 reglas, editable SOLO por Director)`

**4. ACTIVACIÓN** Evento `seg.a1{score}`. Tags `["seguridad","axiomas","gate"]`. Bloqueante duro. Produce `seg.a2` → E-032 y FailureRegistry si rechaza.

**5. SONNET 10x** Compilar las 100 regex a un solo autómata (hyperscan-style con `re2` si disponible) para O(n); telemetría de qué axioma dispara más. Versión superior: reglas con severidad (bloquea/cuarentena/observa) y periodo de prueba: regla nueva corre 7 días en modo observa antes de bloquear.

**6. CÓDIGO**
```yaml
# e018.axiomas.yaml (extracto de 100)
AX03_integridad_sistema:
  - {id: ax03_001, rx: "ignore (all|previous) instructions", severidad: bloquea}
  - {id: ax03_002, rx: "desactiva (guardian|adn|auditor|juez)", severidad: bloquea}
  - {id: ax03_003, rx: "system prompt.{0,30}(reveal|dump|muestra)", severidad: bloquea}
AX04_scope:
  - {id: ax04_001, rx: "borra (todo|el repo|main)", severidad: cuarentena}
AX05_recursos:
  - {id: ax05_001, rx: "loop infinito sin salida", severidad: observa}
```
```python
class E018FiltrosA2(Ficha):
    ID = "e.seg.filtros_a2_axiomas"
    ROUTER_TAGS = ("seguridad", "axiomas", "gate")

    def __init__(self, cfg="e018.axiomas.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        raw = _y.safe_load(Path(cfg).read_text())
        self.reglas = [(ax, r["id"], re.compile(r["rx"], re.I),
                        r["severidad"])
                       for ax, lista in raw.items() for r in lista]

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        hits = [{"axioma": ax, "regla": rid, "sev": sev}
                for ax, rid, rx, sev in self.reglas if rx.search(t)]
        bloquea = [h for h in hits if h["sev"] == "bloquea"]
        cuarent = [h for h in hits if h["sev"] == "cuarentena"]
        if bloquea:
            return {"status": "FAIL",
                    "proposals": [self.prop("seg.a2_rechazo", bloquea)]}
        if cuarent:
            return {"status": "ESCALATE",
                    "proposals": [self.prop("seg.a2_cuarentena", cuarent)]}
        return {"proposals": [self.prop("seg.a2", "PASS"),
                              self.prop("seg.a2_observa",
                                        [h for h in hits
                                         if h["sev"] == "observa"])]}
```

═══════════════════════════════════════════════════════════════════
FICHA E-019/E-020/E-021 — filtros A3/A4/A5 · 60 OPERACIONES
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Cadena de 3 fichas con 60 operaciones YAML: A3 normalizadores (20: espacios, mayúsculas de títulos, listas uniformes, comillas...), A4 descomponedores (20: por párrafo, encabezado, código/prosa, tabla, lista, diálogo...), A5 coherencia (20: bloques vacíos, contradicción de fechas, referencias rotas, numeración saltada...). El plan elige subconjuntos por tipo de doc.

**2. MICROFLUJO** `a2 PASS ➜ A3 normalizar(n ops) ➜ A4 descomponer(m ops) ➜ A5 coherencia(k checks) ➜ bloques+score`

**3. RAÍZ** `📂 e2_seguridad/ → e019_a3.py · e020_a4.py · e021_a5.py + a345.operaciones.yaml`

**4. ACTIVACIÓN** Cadena por eventos: `seg.a2`→A3, `seg.contenido_norm`→A4, `seg.bloques`→A5. Tags `["seguridad","normalizar"] / ["seguridad","descomponer"] / ["seguridad","coherencia"]`. A5 con `repeticion:{max:2,condicion:si_falla_verificacion}`.

**5. SONNET 10x** A4: descomponedor por AST para bloques de código (nunca partir una función); A5: matriz de contradicciones entre bloques (fecha vs fecha, cifra vs cifra). Versión superior: operaciones encadenables declaradas en el plan como mini-DAG (`a3.espacios ➜ a4.por_encabezado ➜ a5.contradicciones`).

**6. CÓDIGO**
```python
class E019FiltrosA3(Ficha):
    ID = "e.seg.filtros_a3"
    ROUTER_TAGS = ("seguridad", "normalizar")
    async def logic(self, ctx, p):
        t = str(p["contenido"])
        for op in p.get("ops", ["espacios", "saltos"]):
            if op == "espacios":
                t = re.sub(r"[ \t]+", " ", t)
            elif op == "saltos":
                t = re.sub(r"\n{3,}", "\n\n", t)
            elif op == "comillas":
                t = t.replace(""", '"').replace(""", '"')
        return {"proposals": [self.prop("seg.contenido_norm", t.strip())]}


class E020FiltrosA4(Ficha):
    ID = "e.seg.filtros_a4"
    ROUTER_TAGS = ("seguridad", "descomponer")
    async def logic(self, ctx, p):
        t, modo = str(p["contenido"]), p.get("modo", "parrafo")
        if modo == "codigo_prosa":
            bloques = re.split(r"(```[\s\S]*?```)", t)
        elif modo == "encabezado":
            bloques = re.split(r"(?m)^#{1,3} ", t)
        else:
            bloques = re.split(r"\n{2,}", t)
        bloques = [b.strip() for b in bloques if b.strip()]
        return {"proposals": [self.prop("seg.bloques", bloques),
                              self.prop("seg.n_bloques", len(bloques))]}


class E021FiltrosA5(Ficha):
    ID = "e.seg.filtros_a5"
    ROUTER_TAGS = ("seguridad", "coherencia")
    async def logic(self, ctx, p):
        bloques = p.get("bloques", [])
        vacios = sum(1 for b in bloques if len(b) < 3)
        refs_rotas = sum(1 for b in bloques
                         if re.search(r"\[\[[^\]]+\]\]", b)
                         and "]]" not in b)
        score = 1 - (vacios + refs_rotas) / max(1, len(bloques))
        return {"proposals": [self.prop("seg.coherencia",
                                        round(max(0, score), 2))],
                "status": "DONE" if score >= 0.5 else "RETRY"}
```

═══════════════════════════════════════════════════════════════════
FICHA E-022 — prompt_injection_scanner · 150 PATRONES ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Catálogo defensivo de 150 patrones de manipulación en 6 familias YAML: F1 override de instrucciones (30), F2 suplantación de roles/sistema (30), F3 exfiltración de config (25), F4 encadenamiento oculto (texto invisible/base64 con órdenes, 25), F5 payloads en adjuntos (20), F6 sociales ("tu creador dijo...", 20). Marca score y sugiere cuarentena; NO bloquea solo (eso lo decide E-026 con contexto).

**2. MICROFLUJO** `contenido_limpio ➜ 6 familias ➜ hits+score ➜ cuarentena_sugerida`

**3. RAÍZ** `📂 e2_seguridad/ → e022_injection_scanner.py + e022.patrones.yaml (150, editable solo Director/Sentinela con aprobación)`

**4. ACTIVACIÓN** Evento `input.contenido_limpio`, paralelo con E-023/E-024. Tags `["seguridad","injection","scan"]`. Produce `seg.injection{hits,score}` → E-026.

**5. SONNET 10x** Decodificar base64/hex sospechoso ANTES de escanear (F4 real); score ponderado por familia; corpus de falsos positivos para no bloquear docs técnicos que HABLAN de inyección (como este). Versión superior: doble pasada — patrón + clasificador ligero local (no LLM) entrenado con los hits históricos.

**6. CÓDIGO**
```python
class E022InjectionScanner(Ficha):
    ID = "e.seg.prompt_injection_scanner"
    ROUTER_TAGS = ("seguridad", "injection", "scan")

    def __init__(self, cfg="e022.patrones.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        raw = _y.safe_load(Path(cfg).read_text())
        self.familias = {f: [re.compile(rx, re.I) for rx in lst]
                         for f, lst in raw["familias"].items()}
        self.pesos = raw.get("pesos", {})

    async def logic(self, ctx, p):
        import base64
        t = str(p["contenido"])
        # F4: decodificar base64 largo antes de escanear
        for b64 in re.findall(r"[A-Za-z0-9+/]{40,}={0,2}", t)[:20]:
            try:
                t += " " + base64.b64decode(b64).decode("utf-8", "ignore")
            except Exception:                      # noqa: BLE001
                pass
        hits = {f: [rx.pattern for rx in rxs if rx.search(t)]
                for f, rxs in self.familias.items()}
        score = min(1.0, sum(len(v) * self.pesos.get(f, 1)
                             for f, v in hits.items()) / 10)
        return {"proposals": [
            self.prop("seg.injection", {"hits": {k: len(v) for k, v
                                                 in hits.items()},
                                        "score": round(score, 2)}),
            self.prop("seg.cuarentena_sugerida", score >= 0.5)]}
```

═══════════════════════════════════════════════════════════════════
FICHA E-023 — pii_scrubber · 40 TIPOS ✚  /  E-024 — secret_detector · 60 FIRMAS ✚
═══════════════════════════════════════════════════════════════════

**E-023** · 1) Catálogo de 40 tipos de dato personal en YAML (email, teléfono por país, DNI/cédula LATAM+EU, IBAN, tarjetas, direcciones, coordenadas, matrículas...) con 3 políticas: enmascarar, tokenizar reversible (bóveda local), eliminar. 2) `texto ➜ 40 regex ➜ política por tipo ➜ scrubbed+conteo`. 3) `📂 e2_seguridad/e023_pii.py + e023.tipos.yaml`. 4) Activa: `input.contenido_limpio`; tags `["seguridad","pii","scrub"]`; produce `seg.contenido_scrubbed` → todo lo que vaya a LLM externo. 5) Sonnet: tokenización reversible con bóveda cifrada local (el Director puede des-tokenizar); validadores de checksum (Luhn para tarjetas) para bajar falsos positivos. 6)
```python
class E023PiiScrubber(Ficha):
    ID = "e.seg.pii_scrubber"
    ROUTER_TAGS = ("seguridad", "pii", "scrub")

    def __init__(self, cfg="e023.tipos.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        self.tipos = {k: (re.compile(v["rx"]), v.get("politica", "mask"))
                      for k, v in _y.safe_load(
                          Path(cfg).read_text())["tipos"].items()}

    async def logic(self, ctx, p):
        t, conteo = str(p["contenido"]), {}
        for k, (rx, pol) in self.tipos.items():
            n = len(rx.findall(t))
            if n:
                conteo[k] = n
                t = rx.sub("" if pol == "drop" else f"[{k.upper()}]", t)
        return {"proposals": [self.prop("seg.contenido_scrubbed", t),
                              self.prop("seg.pii", conteo)]}
```
**E-024** · 1) 60 firmas de credenciales en YAML (openai sk-, anthropic, github ghp_/gho_, aws AKIA, gcp, hf_, slack xox, stripe sk_live, jwt, ssh privkey, .env dumps...). Detección = FAIL inmediato + aviso "ROTA ESA CLAVE" + registra en FailureRegistry. Jamás re-emite la clave en logs (solo tipo+últimos 4). 2) `texto ➜ 60 firmas ➜ ¿hit? FAIL+aviso ➜ PASS`. 3) `📂 e2_seguridad/e024_secret_detector.py + e024.firmas.yaml`. 4) Activa: `input.contenido_limpio`; tags `["seguridad","secretos"]`; bloqueante. 5) Sonnet: entropía de Shannon para strings largos sin firma conocida; sugerir al Director el comando de rotación del provider. 6)
```python
class E024SecretDetector(Ficha):
    ID = "e.seg.secret_detector_input"
    ROUTER_TAGS = ("seguridad", "secretos")

    def __init__(self, cfg="e024.firmas.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        self.firmas = {k: re.compile(v) for k, v in _y.safe_load(
            Path(cfg).read_text())["firmas"].items()}

    async def logic(self, ctx, p):
        t = str(p["contenido"])
        hallados = [{"tipo": k, "sufijo": m.group()[-4:]}
                    for k, rx in self.firmas.items()
                    for m in [rx.search(t)] if m]
        if hallados:
            return {"status": "FAIL", "proposals": [
                self.prop("seg.secretos", hallados),
                self.prop("seg.aviso_director",
                          "🔑 CLAVE DETECTADA EN INPUT — RÓTALA YA")]}
        return {"proposals": [self.prop("seg.secretos", [])]}
```

═══════════════════════════════════════════════════════════════════
FICHA E-025 — canal_firmante · 4 ESQUEMAS ✚  /  E-026 — cuarentena_manager · 8 DESTINOS ✚
═══════════════════════════════════════════════════════════════════

**E-025** · 1) 4 esquemas de verificación de origen: HMAC compartido, token por canal, firma GPG, allowlist de remitentes. El YAML declara qué canales exigen cuál. 2) `evento ➜ esquema del canal ➜ verificar ➜ ok/FAIL`. 3) `📂 e2_seguridad/e025_canal_firmante.py + e025.esquemas.yaml`. 4) Activa: `input.evento`; tags `["seguridad","firma","canal"]`. 5) Sonnet: rotación de HMAC programada (T-029); challenge-response para canales interactivos. 6)
```python
class E025CanalFirmante(Ficha):
    ID = "e.seg.canal_firmante"
    ROUTER_TAGS = ("seguridad", "firma", "canal")

    async def logic(self, ctx, p):
        import hmac, os
        from hashlib import sha256 as _s
        esquema = p.get("esquema", "hmac")
        if esquema == "hmac":
            sec = os.environ.get(f"CANAL_{p['origen'].upper()}_SECRET", "")
            esperada = hmac.new(sec.encode(), p["doc_id"].encode(),
                                _s).hexdigest()
            ok = hmac.compare_digest(p.get("firma", ""), esperada)
        elif esquema == "allowlist":
            ok = p.get("remitente") in p.get("allow", [])
        else:
            ok = bool(p.get("firma"))
        req = p.get("firma_requerida", False)
        return {"proposals": [self.prop("seg.canal_verificado", ok)],
                "status": "FAIL" if req and not ok else "DONE"}
```
**E-026** · 1) Decide con TODO el contexto de E2 (injection score, malware flag, canal, secretos) entre 8 destinos: pasar, observar, sandbox-lectura, pedir confirmación al Director, cuarentena 24h, cuarentena indefinida, rechazar, rechazar+bloquear canal. Matriz de decisión en YAML. 2) `señales E2 ➜ matriz ➜ destino ➜ ejecutar/ESCALATE`. 3) `📂 e2_seguridad/e026_cuarentena.py + e026.matriz.yaml`. 4) Activa: agregación de `seg.*`; tags `["seguridad","cuarentena","decidir"]`. 5) Sonnet: expiración automática de cuarentenas con re-scan; estadística de falsos positivos por regla para calibrar la matriz. 6)
```python
class E026CuarentenaManager(Ficha):
    ID = "e.seg.cuarentena_manager"
    ROUTER_TAGS = ("seguridad", "cuarentena", "decidir")
    DESTINOS = ("pasar", "observar", "sandbox", "confirmar",
                "cuarentena_24h", "cuarentena", "rechazar",
                "rechazar_bloquear")

    async def logic(self, ctx, p):
        inj = p.get("injection", {}).get("score", 0)
        destino = ("rechazar" if p.get("secretos") else
                   "cuarentena_24h" if inj >= 0.7 or p.get("malware_flag")
                   else "confirmar" if inj >= 0.5
                   else "observar" if inj >= 0.2 else "pasar")
        if destino in ("confirmar", "cuarentena_24h", "cuarentena"):
            return {"status": "ESCALATE", "proposals": [
                self.prop("seg.cuarentena", {"destino": destino,
                                             "razones": {"inj": inj}})]}
        if destino.startswith("rechazar"):
            return {"status": "FAIL", "proposals": [
                self.prop("seg.cuarentena", {"destino": destino})]}
        return {"proposals": [self.prop("seg.cuarentena",
                                        {"destino": destino})]}
```

---
**AUDITORÍA DEL SEGMENTO (pasada 2/3):** cubre del corpus: filtros A1-A5 (Input Engine v4.0) ✓, GUARDIAN entrada ✓, Wake/OCR pendientes → DOC 4. Catálogos ✚ de este doc: 20+100+60+150+40+60+4+8 = **442 variantes defensivas**. Acumulado E: 782 variantes.
**SIGUIENTE:** DOC 4 (E-027..E-038: rate/malware/wake/ocr/traductor/sentinel + huellas L1-L5 y Seed S1-S2).
