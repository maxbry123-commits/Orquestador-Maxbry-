# SALIDA E v2 — PIPELINE ENTRADA · DOC 1
# Prompt PIPELINE DSL: fichas tipo skills (Python + YAML + JSON combinados).
# Formato por ficha: 6 secciones obligatorias. Este doc: FICHA MAESTRA DE EJEMPLO
# (LOOPS 1-1000) + fichas E-001..E-006. Los siguientes docs repiten el patrón.

═══════════════════════════════════════════════════════════════════
FICHA EJEMPLO MAESTRO — T-LOOP-1000 · catalogo_loops_1000 ✚
(este es el patrón que siguen TODAS las fichas del sistema)
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE? (cuántos son y qué función hace cada uno)**
Es una CADENA, no una función: un catálogo de 1000 bucles distintos generados desde 10 FAMILIAS × 20 TAREAS × 5 INTENSIDADES (10×20×5 = 1000 loops únicos, cada uno con id, condición de salida y presupuesto propio). Las 10 familias:
- F1 VERIFICACIÓN (loops 0001-0100): re-chequean un resultado hasta que pasa o agota presupuesto
- F2 REFINAMIENTO (0101-0200): mejoran una salida iterativamente comparando contra rúbrica
- F3 INVESTIGACIÓN (0201-0300): ciclos query→fetch→filtrar→score (Discovery R1-R5)
- F4 CONSENSO (0301-0400): rondas de votación entre expertos hasta quórum
- F5 REPARACIÓN (0401-0500): diagnóstico→parche→test→repite si falla
- F6 EXPLORACIÓN (0501-0600): generan alternativas divergentes (anti-eco)
- F7 CONSOLIDACIÓN (0601-0700): fusionan lotes con verificación por conteo (CHEF)
- F8 VIGILANCIA (0701-0800): heartbeat/watchdog/sondeo periódico (infra)
- F9 APRENDIZAJE (0801-0900): destilan lecciones a memoria (dream/distill)
- F10 ESCALADO (0901-1000): reintentos con backoff+jitter y escalera a Director
Cada loop se parametriza por INTENSIDAD n1-n5 (iteraciones ×1/×3/×10/×30/×100) y el PLANNER_OFFLINE los inserta en el plan; el runtime solo los ejecuta.

**2. MICROFLUJO**
`pedir loop(familia,tarea,nivel) ➜ resolver id ➜ cargar spec YAML ➜ validar presupuesto ➜ iterar[cuerpo ➜ evaluar ➜ ¿salir?] ➜ emitir resultado+evidencia`

**3. RAÍZ EXTENDIDA**
```
📂 /repo3/loops/catalogo/
   ├── loop_catalog.yaml          # las 10 familias × 20 tareas (200 specs base)
   ├── loop_factory.py            # genera los 1000 combinando con n1-n5
   ├── loop_runner.py             # ejecuta cualquier loop por id
   ├── t_loop_1000.contract.json  # enchufe v2.0
   └── ejemplos.json              # 12 loops de muestra resueltos
```

**4. ACTIVACIÓN Y DEPENDENCIAS**
- **Quién la activa:** el PLANNER_OFFLINE (inserta loop_ids en sequence.json) y el Loop Engine en runtime. El Router la ubica por tags `["loop","iterar","catalogo"]`.
- **Cuándo:** cada vez que un paso del plan declara `"loop": "F5-T07-n3"`.
- **Depende de:** ficha_base, state.snapshot, cost_governor (P-110).
- **Produce:** `loop.resultado` + `loop.evidencia` → consumen Juez y Fusion.

**5. INSTRUCCIONES SONNET 10x (mejorar y diseñar versión superior)**
Mejora directa: (a) añade familia F11 "SIMULACIÓN" con entornos sintéticos; (b) aprende `iteraciones_optimas` por tarea desde métricas históricas y ajusta el YAML; (c) permite loops COMPUESTOS (un loop cuyo cuerpo es otro loop, profundidad ≤3). Versión superior (v2): convierte el catálogo en grafo — loops que se encadenan por condición (`si F1 falla 2 veces ➜ saltar a F5`), compilado también offline; añade poda automática: loops con tasa de éxito <20% en 30 días pasan a deprecated con aviso a Sentinela.

**6. CÓDIGO (Python + YAML + JSON combinados, enchufe v2.0)**

`loop_catalog.yaml` (extracto — 3 de las 200 specs base):
```yaml
familias:
  F1:
    nombre: verificacion
    tareas:
      T01: {cuerpo: recheck_schema,   salida: "checks_ok==true",  base_iters: 3}
      T02: {cuerpo: recheck_hash,     salida: "hash_estable",     base_iters: 2}
  F5:
    nombre: reparacion
    tareas:
      T07: {cuerpo: diagnosticar_parchear_testear, salida: "tests_pass", base_iters: 5}
intensidades: {n1: 1, n2: 3, n3: 10, n4: 30, n5: 100}
```

`t_loop_1000.contract.json` (extracto enchufe v2.0):
```json
{"artifact_id": "t.loop.catalogo_1000", "version": "1.0.0",
 "estado": "active", "categoria": "transversal", "etapa": "T",
 "contrato": {"rol": "service"},
 "ejecucion": {"kind": "code", "transport": "importlib",
               "runtime_type": "compute", "idempotente": true},
 "activacion": {"eventos": ["plan.paso_con_loop"],
                "condicion": "sequence.pasos[*].loop != null"},
 "router_tags": ["loop", "iterar", "catalogo"],
 "perfiles": {"n1": {"iteraciones": 1}, "n5": {"iteraciones": 100}},
 "seguridad": {"sandbox": "process", "limites": {"timeout_ms": 600000}}}
```

`loop_factory.py` + `loop_runner.py`:
```python
"""Catálogo 1000 loops: 10 familias × 20 tareas × 5 intensidades."""
from __future__ import annotations
import asyncio, time
import yaml
from pathlib import Path
from ficha_base import Ficha, FichaError


class LoopFactory:
    def __init__(self, ruta="loops/catalogo/loop_catalog.yaml"):
        self.cat = yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))

    def spec(self, loop_id: str) -> dict:
        """'F5-T07-n3' → spec completa con iteraciones resueltas."""
        fam, tarea, nivel = loop_id.split("-")
        base = self.cat["familias"][fam]["tareas"][tarea]
        mult = self.cat["intensidades"][nivel]
        return {**base, "loop_id": loop_id,
                "iteraciones": base["base_iters"] * mult,
                "familia": self.cat["familias"][fam]["nombre"]}

    def listar(self) -> list[str]:
        return [f"{f}-{t}-{n}" for f, fv in self.cat["familias"].items()
                for t in fv["tareas"] for n in self.cat["intensidades"]]


class TLoop1000(Ficha):
    ID = "t.loop.catalogo_1000"
    ROUTER_TAGS = ("loop", "iterar", "catalogo")

    def __init__(self, cuerpos: dict, **kw):
        super().__init__(**kw)
        self.factory = LoopFactory()
        self.cuerpos = cuerpos            # nombre_cuerpo -> async fn(ctx,st)

    async def logic(self, ctx, p):
        spec = self.factory.spec(p["loop_id"])
        cuerpo = self.cuerpos.get(spec["cuerpo"])
        if cuerpo is None:
            raise FichaError(f"cuerpo_desconocido:{spec['cuerpo']}")
        estado, historia = dict(p.get("estado_inicial", {})), []
        for i in range(spec["iteraciones"]):
            estado = await cuerpo(ctx, estado)
            historia.append({"i": i, "ok": estado.get("ok", False)})
            if self._condicion(spec["salida"], estado):
                break
            await asyncio.sleep(0)        # AX07: sin sleep bloqueante
        return {"proposals": [
            self.prop("loop.resultado", estado),
            self.prop("loop.evidencia", {"loop_id": spec["loop_id"],
                                         "iters": len(historia),
                                         "historia": historia[-10:]})]}

    @staticmethod
    def _condicion(expr: str, st: dict) -> bool:
        if "==" in expr:
            k, v = expr.split("==")
            return str(st.get(k.strip())) == v.strip().strip('"')
        return bool(st.get(expr.strip()))
```

═══════════════════════════════════════════════════════════════════
FICHA E-001 — input_listener
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Único punto de entrada del sistema. Escucha 6 canales (telegram, drive, mcp, api, kanboard, webhook), valida que el canal exista y empaqueta el evento crudo con timestamp. 1 función, pero es la puerta: si esto falla, nada entra.

**2. MICROFLUJO** `evento llega ➜ ¿canal válido? ➜ empaquetar {raw,origen,ts,meta} ➜ emitir input.evento`

**3. RAÍZ**
```
📂 /repo6/fichas/entrada/e1_captura/
   ├── e001_input_listener.py
   ├── e001.contract.json
   └── e001.meta.md
```

**4. ACTIVACIÓN** El Router la activa con el evento externo `canal.mensaje_nuevo` (tags `["entrada","listener","canal"]`). Es la ficha 0: nada la precede. Produce `input.evento` → consume E-002.

**5. SONNET 10x** Añade: (a) modo long-polling y modo webhook por canal desde YAML; (b) buffer de ráfagas (acumula 2s y entrega lote); (c) canal "archivo local" para pruebas sin red. Versión superior: listener declarativo — canales definidos 100% en `canales.yaml` (url, auth_env, formato), cero código nuevo por canal.

**6. CÓDIGO**
```yaml
# e001.canales.yaml
canales:
  telegram: {tipo: webhook, auth_env: TELEGRAM_TOKEN}
  drive:    {tipo: polling, intervalo_s: 60, auth_env: GDRIVE_TOKEN}
  api:      {tipo: http,    puerto: 7860}
```
```python
class E001InputListener(Ficha):
    ID = "e.entrada.input_listener"
    ROUTER_TAGS = ("entrada", "listener", "canal")

    def __init__(self, ruta_canales="e001.canales.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        self.canales = _y.safe_load(
            Path(ruta_canales).read_text())["canales"]

    async def logic(self, ctx, p):
        canal = p.get("origen", "")
        if canal not in self.canales:
            raise FichaError(f"canal_desconocido:{canal}")
        evento = {"raw": p.get("raw"), "origen": canal,
                  "ts": time.time(), "meta": p.get("meta", {}),
                  "config_canal": self.canales[canal]}
        return {"proposals": [self.prop("input.evento", evento)]}
```
```json
{"artifact_id": "e.entrada.input_listener", "version": "1.0.0",
 "estado": "active", "categoria": "pipeline", "etapa": "E",
 "contrato": {"rol": "source",
   "expone": {"datatype": {"family": "input", "type": "evento", "version": 1}}},
 "ejecucion": {"kind": "code", "transport": "importlib", "runtime_type": "compute"},
 "activacion": {"eventos": ["canal.mensaje_nuevo"]},
 "router_tags": ["entrada", "listener", "canal"],
 "seguridad": {"sandbox": "process", "limites": {"timeout_ms": 10000}}}
```

═══════════════════════════════════════════════════════════════════
FICHA E-002 — normalizer_frozen
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Convierte cualquier evento en el documento canónico ÚNICO del sistema y lo CONGELA (frozen v1.0): a partir de aquí nadie modifica el original, solo se derivan copias. Calcula doc_id = sha256 del contenido.

**2. MICROFLUJO** `input.evento ➜ extraer contenido ➜ doc_id=sha256 ➜ armar doc canónico ➜ frozen=true ➜ emitir input.frozen`

**3. RAÍZ** `📂 /repo6/fichas/entrada/e1_captura/ → e002_normalizer_frozen.py + e002.contract.json`

**4. ACTIVACIÓN** La activa el evento `input.evento` de E-001 (Router tags `["entrada","normalizar","congelar"]`). Produce `input.frozen` → consumen E-004, E-005, E-006 y el Audit Bus (primer 🔍 de memoria).

**5. SONNET 10x** Soporta contenido binario (guarda ref + hash, no el blob), esquema de doc canónico versionado (v1.0→v1.1 con migrador), y verificación de congelamiento: cualquier intento de mutar el frozen dispara evento `seg.frozen_violado`. Versión superior: frozen store append-only con content-addressing (como git objects).

**6. CÓDIGO**
```python
class E002NormalizerFrozen(Ficha):
    ID = "e.entrada.normalizer_frozen"
    ROUTER_TAGS = ("entrada", "normalizar", "congelar")

    async def logic(self, ctx, p):
        doc = {"doc_id": hash_doc(p["raw"]), "origen": p["origen"],
               "proyecto": p.get("proyecto", "default"),
               "tipo": p.get("tipo", "texto"), "contenido": p["raw"],
               "timestamp": time.time(), "frozen": True, "version": "1.0"}
        ruta = Path(f"runtime/frozen/{doc['doc_id']}.json")
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if not ruta.exists():                      # append-only
            ruta.write_text(json.dumps(doc, ensure_ascii=False,
                                       default=str))
        return {"proposals": [self.prop("input.frozen", doc)]}
```
```json
{"artifact_id": "e.entrada.normalizer_frozen", "estado": "active",
 "categoria": "pipeline", "etapa": "E", "version": "1.0.0",
 "contrato": {"rol": "transform",
   "consume": {"datatype": {"family": "input", "type": "evento", "version": 1}},
   "expone":  {"datatype": {"family": "input", "type": "frozen", "version": 1}}},
 "ejecucion": {"kind": "code", "transport": "importlib",
               "runtime_type": "compute", "idempotente": true},
 "activacion": {"eventos": ["input.evento"]},
 "router_tags": ["entrada", "normalizar", "congelar"],
 "repite_en": ["INPUT"],
 "seguridad": {"sandbox": "process", "limites": {"timeout_ms": 10000}}}
```

═══════════════════════════════════════════════════════════════════
FICHA E-006 — encoding_sanitizer ✚
═══════════════════════════════════════════════════════════════════

**1. ¿QUÉ HACE?** Elimina caracteres invisibles unicode (zero-width, BOM, soft-hyphen — el bug del iPad que corrompía tu código copiado), normaliza NFC, unifica CRLF→LF y espacios raros. Reporta cuántos caracteres removió por canal para detectar la fuente sucia.

**2. MICROFLUJO** `input.frozen ➜ NFC ➜ strip invisibles ➜ CRLF→LF ➜ nbsp→espacio ➜ contar removidos ➜ emitir contenido_limpio`

**3. RAÍZ** `📂 /repo6/fichas/entrada/e1_captura/ → e006_encoding_sanitizer.py + e006.contract.json + e006.invisibles.yaml`

**4. ACTIVACIÓN** Evento `input.frozen` (paralelo con E-004/E-007). Tags `["entrada","sanear","unicode"]`. Produce `input.contenido_limpio` → consumen TODOS los filtros E2 y las huellas E3.

**5. SONNET 10x** (a) tabla de invisibles y homóglifos en YAML editable (Sentinela propone nuevos con evidencia); (b) métrica `chars_removidos_por_canal` a la serie temporal T-026; (c) modo estricto que RECHAZA si >5% del doc es invisible (probable ofuscación). Versión superior: detector de homóglifos con mapa confusables de Unicode (ej: а cirílica vs a latina) aplicado solo a bloques de código.

**6. CÓDIGO**
```yaml
# e006.invisibles.yaml
invisibles: ["\u200b", "\u200c", "\u200d", "\u2060", "\ufeff", "\u00ad", "\u180e"]
reemplazos: {"\u00a0": " ", "\r\n": "\n"}
umbral_rechazo_pct: 5
```
```python
class E006EncodingSanitizer(Ficha):
    ID = "e.entrada.encoding_sanitizer"
    ROUTER_TAGS = ("entrada", "sanear", "unicode")

    def __init__(self, cfg="e006.invisibles.yaml", **kw):
        super().__init__(**kw)
        import yaml as _y
        c = _y.safe_load(Path(cfg).read_text())
        self.tabla = dict.fromkeys(map(ord, "".join(c["invisibles"])))
        self.reemplazos = c["reemplazos"]
        self.umbral = c["umbral_rechazo_pct"] / 100

    async def logic(self, ctx, p):
        import unicodedata
        orig = str(p["contenido"])
        t = unicodedata.normalize("NFC", orig).translate(self.tabla)
        for k, v in self.reemplazos.items():
            t = t.replace(k, v)
        removidos = len(orig) - len(t)
        if removidos / max(1, len(orig)) > self.umbral:
            return {"status": "ESCALATE", "proposals": [
                self.prop("seg.posible_ofuscacion", removidos)]}
        return {"proposals": [
            self.prop("input.contenido_limpio", t),
            self.prop("input.chars_removidos",
                      {"n": removidos, "canal": p.get("origen", "?")})]}
```

═══════════════════════════════════════════════════════════════════
FICHAS E-003, E-004, E-005 (mismo patrón 6 secciones, compactas)
═══════════════════════════════════════════════════════════════════

**E-003 ack_engine** · 1) Confirma recepción al canal origen con doc_id corto — el Director siempre sabe que llegó. 2) `input.frozen ➜ armar msg ➜ router.notificar(canal) ➜ ack=true`. 3) `📂 e1_captura/e003_ack_engine.py`. 4) Activa: `input.frozen`; tags `["entrada","ack","notificar"]`; produce `input.ack`→Audit. 5) Sonnet: ack con botones inline (recibido/cancelar/prioridad) en Telegram; reintento si el canal no responde. 6)
```python
class E003AckEngine(Ficha):
    ID = "e.entrada.ack_engine"
    ROUTER_TAGS = ("entrada", "ack", "notificar")
    async def logic(self, ctx, p):
        r = await self.router.despachar("notificar", {
            "canal": p["origen"],
            "msg": f"✅ RECIBIDO {p['doc_id'][:8]}"},
            trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("input.ack",
                                        r["status"] == "DONE")]}
```

**E-004 hash_engine** · 1) SHA256 del contenido completo — la identidad inmutable del documento en todo el sistema. 2) `contenido ➜ sha256 ➜ input.sha256`. 3) `📂 e1_captura/e004_hash_engine.py`. 4) Activa: `input.frozen`; tags `["entrada","hash"]`; consume E-005 y hash-chain. 5) Sonnet: añadir blake3 (más rápido en móvil) con flag; hash por bloque para docs gigantes. 6)
```python
class E004HashEngine(Ficha):
    ID = "e.entrada.hash_engine"
    ROUTER_TAGS = ("entrada", "hash")
    async def logic(self, ctx, p):
        return {"proposals": [self.prop("input.sha256",
                                        hash_doc(p["contenido"]))]}
```

**E-005 inventory_validator** · 1) ¿Este doc ya se procesó? Consulta inventory.json; si ya está → SKIP (ahorra todo el pipeline). Si no, lo registra. Idempotente. 2) `sha256 ➜ ¿en inventario? ➜ sí:SKIP / no:registrar ➜ seguir`. 3) `📂 e1_captura/e005_inventory_validator.py + runtime/inventory.json`. 4) Activa: `input.sha256`; tags `["entrada","inventario","dedup"]`; gate previo a E2. 5) Sonnet: inventario en sqlite con índice por proyecto+fecha; TTL configurable; comando `reprocesar doc_id` que salta el skip. 6)
```python
class E005InventoryValidator(Ficha):
    ID = "e.entrada.inventory_validator"
    ROUTER_TAGS = ("entrada", "inventario", "dedup")
    async def logic(self, ctx, p):
        ruta = Path("runtime/inventory.json")
        inv = json.loads(ruta.read_text()) if ruta.exists() else {}
        if p["sha256"] in inv and not p.get("forzar"):
            return {"status": "SKIP",
                    "proposals": [self.prop("input.duplicado", True)]}
        inv[p["sha256"]] = {"ts": time.time(),
                            "proyecto": p.get("proyecto", "default")}
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(json.dumps(inv))
        return {"proposals": [self.prop("input.duplicado", False)]}
```

---
**PLAN DE LOS SIGUIENTES DOCS (mismo formato, ≤800 líneas c/u):**
DOC 2: E-007..E-016 · DOC 3: E-017..E-026 · DOC 4: E-027..E-038 · DOC 5: E-039..E-050 · DOC 6: E-051..E-062 · DOC 7: E-063..E-072 + wiring DAG completo. Luego SALIDA P (docs 8-16) y SALIDA S+T+A (docs 17-22).
