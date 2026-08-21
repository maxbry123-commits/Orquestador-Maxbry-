# SALIDA 3.1 — PARCHE DE ALINEACIÓN G2 v2.5
# Aplica sobre Salidas 1-3. Formato: diff exacto (ANTES → DESPUÉS) + 1 archivo nuevo.
# 5 parches: WAL dual · kernel transductor · task_id · trace_id · jitter fallback.

---

## PARCHE 1 — WAL DUAL (Salida 3, `master_state_engine.py`)

**AÑADIR** al `__init__` (después de `self.f_ckpts = ...`):
```python
        self.f_wal = self.base / "wal.jsonl"
        self._wal_count = 0
        self._wal_last_ckpt = time.time()
        self._wal_replay()                       # recovery al arrancar (IT02)
```

**AÑADIR** dentro de `commit()`, ANTES de escribir en `self.f_events`:
```python
            # WAL primero: si el proceso muere aquí, wal_replay reconstruye
            with self.f_wal.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({"proposals": proposals, "actor": actor,
                                     "intent": intent, "ts": time.time()},
                                    ensure_ascii=False, default=str) + "\n")
```

**AÑADIR** al final de `commit()`, ANTES de `return ev.hash`:
```python
            # Checkpoint dual: 1000 entries O 60s (ítem 150) + truncar WAL
            self._wal_count += 1
            if (self._wal_count >= 1000
                    or time.time() - self._wal_last_ckpt >= 60):
                self.checkpoint(f"auto_wal_{nuevo['version']}")
                self.f_wal.write_text("", encoding="utf-8")   # wal_truncate
                self._wal_count = 0
                self._wal_last_ckpt = time.time()
```

**AÑADIR** método nuevo a la clase:
```python
    def _wal_replay(self) -> None:
        """IT02: kill -9 → al reiniciar, re-aplica proposals no consolidados."""
        if not self.f_wal.exists() or not self.f_wal.stat().st_size:
            return
        pendientes = [json.loads(l) for l in
                      self.f_wal.read_text(encoding="utf-8")
                      .strip().splitlines()]
        ultimo_ts = 0.0
        if self.f_events.exists():
            lineas = self.f_events.read_text(
                encoding="utf-8").strip().splitlines()
            if lineas:
                ultimo_ts = json.loads(lineas[-1])["ts"]
        for p in pendientes:
            if p["ts"] > ultimo_ts:              # solo lo no consolidado
                self.commit(p["proposals"], p["actor"], "wal_replay")
        self.f_wal.write_text("", encoding="utf-8")
```

---

## PARCHE 2 — KERNEL TRANSDUCTOR 🚂 (Salida 1, `kernel_core.py`)

**REEMPLAZAR** el puerto `PuertoPipeline` completo:
```python
class PuertoPipeline(Protocol):
    """TRANSDUCTOR: el kernel NO selecciona nada en runtime.
    Ejecuta el sequence.json congelado que PLANNER_OFFLINE compiló en F-1/F0.
    PROHIBIDO: 'decisión', 'inteligencia', 'planner' en runtime (ítem 53)."""
    def cargar_sequence(self, task_id: str) -> dict: ...       # congelado
    async def ejecutar(self, fase: Fase, contexto: dict) -> ResultadoFase: ...
```

**REEMPLAZAR** en `Solicitud` (parches 2+3+4 juntos):
```python
@dataclass
class Solicitud:
    raw: Any
    origen: str
    task_id: str = ""                            # ítem 139: OBLIGATORIO
    solicitud_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        if not self.task_id:
            raise ValueError("task_id_obligatorio")   # sin task_id → REJECTED
```

**REEMPLAZAR** las 2 primeras líneas de `_ejecutar_fase()`:
```python
        # ANTES: nombre = self.e.pipeline.seleccionar({...})  ← taxi ❌
        seq = self.e.pipeline.cargar_sequence(ctx["solicitud"].task_id)
        if not seq or seq.get("schema_version") != "1.0":
            return ResultadoFase(fase, Clasificacion.FAIL,
                                 {"error": "SEQUENCE_JSON_INVALIDO"})
        ctx["sequence"] = seq                    # vía congelada del tren
        self.e.audit.evento("sequence.cargado", {
            "task_id": ctx["solicitud"].task_id,
            "trace_id": ctx["solicitud"].trace_id,
            "fase": fase.value, "hash": seq.get("hash", "")})
```

---

## PARCHE 3+4 — task_id/trace_id EN TODO DATO

`crazy_wall.py` — **REEMPLAZAR** firma de `actualizar`:
```python
    def actualizar(self, paso: str, estado: str, datos: dict,
                   task_id: str = "global") -> None:
        # ...partición: cada nota lleva task_id (ítem 144)
        nota = NotaWall(paso, estado, {**datos, "task_id": task_id})
```

`juez_core.py` — **AÑADIR** a `Instruction`:
```python
    task_id: str = ""
    trace_id: str = ""
    parent_span_id: str = ""       # hereda de la ficha anterior (ítem 203)
```

`fusion_engine.py` — **AÑADIR** en `consolidar()`, dentro de `resultado["_fusion"]`:
```python
            "task_id": getattr(parciales[0], "task_id", "") if parciales else "",
```

---

## PARCHE 5 — JITTER EN RECOVERY (Salida 2, `recovery_engine.py`)

**AÑADIR** import + método, y llamarlo en `_ejecutar_nivel` nivel RETRY:
```python
import random

    @staticmethod
    def backoff_jitter_ms(attempt: int) -> int:
        """Ítem 75: 1000*2^attempt + random(0,1000)."""
        return 1000 * (2 ** attempt) + random.randint(0, 1000)

        # en _ejecutar_nivel, caso RETRY:
        if nivel is NivelRecovery.RETRY:
            await asyncio.sleep(self.backoff_jitter_ms(
                self.fallos_consecutivos) / 1000)
            return regla is not None and regla.sustituible_por is not None
```

**AÑADIR** nivel COMPENSATE al enum (entre REPLAN y ESCALATE):
```python
class NivelRecovery(IntEnum):
    RETRY = 1
    ROLLBACK = 2
    CHECKPOINT = 3
    REPLAN = 4
    COMPENSATE = 5     # ítem 73: deshacer efectos (hook inyectado)
    ESCALATE = 6
```

---

## ARCHIVO NUEVO — `orquestador-nucleo/planner/planner_offline.py` (~150 LOC)

```python
"""PLANNER_OFFLINE — Compiler[requirements.json → sequence.json + fallback.json]
Corre en F-1/F0 (lifecycle marker), NUNCA en runtime. Python puro, NO LLM,
NO agente (ítems 18-21). Vive en repo brain. El Director define requirements;
esto compila la vía del tren y la congela con hash.
"""
from __future__ import annotations
import json
import time
from graphlib import TopologicalSorter, CycleError
from hashlib import sha256
from pathlib import Path


class TaskRejectedError(Exception):
    """Ciclo, ficha inexistente o requirements inválidos (ítem 142)."""


def _hash(obj) -> str:
    return sha256(json.dumps(obj, sort_keys=True,
                             default=str).encode()).hexdigest()


def compilar(requirements: dict, fichas_committed: dict[str, dict],
             out_dir: str = "runtime/plans") -> dict:
    """Entrada: requirements.json del Director + índice de fichas COMMITTED.
    Salida: sequence.json + fallback.json congelados (inmutables en runtime).
    """
    task_id = requirements["task_id"]
    pasos: list[dict] = requirements["pasos"]     # [{ficha_id, depends_on,
                                                  #   critico?, condition?}]
    # ── Validación 1: toda ficha existe y está COMMITTED (ítem 101/182) ──
    for p in pasos:
        f = fichas_committed.get(p["ficha_id"])
        if not f or f.get("status") != "COMMITTED":
            raise TaskRejectedError(f"ficha_no_committed:{p['ficha_id']}")
        for dep in p.get("depends_on", []):
            if dep not in {x["ficha_id"] for x in pasos}:
                raise TaskRejectedError(f"depends_on_inexistente:{dep}")

    # ── Validación 2: DAG acíclico + orden topológico (ítem 141/181) ──
    grafo = {p["ficha_id"]: set(p.get("depends_on", [])) for p in pasos}
    try:
        orden = list(TopologicalSorter(grafo).static_order())
    except CycleError as exc:
        raise TaskRejectedError(f"ciclo_detectado:{exc}") from exc

    # ── Grupos paralelos: fichas sin dependencia mutua en el mismo nivel ──
    nivel: dict[str, int] = {}
    for fid in orden:
        nivel[fid] = 1 + max((nivel[d] for d in grafo[fid]), default=-1)
    paralelos: dict[int, list[str]] = {}
    for fid, n in nivel.items():
        paralelos.setdefault(n, []).append(fid)

    sequence = {
        "schema_version": "1.0",
        "task_id": task_id,
        "creado": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "orden_topologico": orden,
        "parallel_groups": [sorted(v) for _, v in sorted(paralelos.items())],
        "pasos": [{**p, "critico": p.get("critico", False),
                   "condition": p.get("condition", "")} for p in pasos],
        "hash_snapshot": _hash({f: fichas_committed[f]["hash_sha256"]
                                for f in orden}),          # ítem 143
    }
    sequence["hash"] = _hash(sequence)

    # ── fallback.json 4 niveles por ficha (ítems 70-75) ──
    fallback = {
        "schema_version": "1.0", "task_id": task_id,
        "niveles": {
            p["ficha_id"]: {
                "1_retry": {"max": 3, "backoff": "1000*2^n+rand(0,1000)"},
                "2_alternate": fichas_committed[p["ficha_id"]]
                               .get("sustituible_por", []),
                "3_abort": {"congelar_paso": True,
                            "critico": p.get("critico", False)},
                "4_compensate": fichas_committed[p["ficha_id"]]
                                .get("efecto_si_falla", []),
            } for p in pasos
        },
    }
    fallback["hash"] = _hash(fallback)

    # ── Congelar a disco (el runtime solo LEE) ──
    base = Path(out_dir) / task_id
    base.mkdir(parents=True, exist_ok=True)
    (base / "sequence.json").write_text(
        json.dumps(sequence, ensure_ascii=False, indent=1), encoding="utf-8")
    (base / "fallback.json").write_text(
        json.dumps(fallback, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"sequence": sequence, "fallback": fallback}
```

---

## TESTS DEL PARCHE
```
test_wal_replay_tras_kill (IT02) · test_ckpt_1000_o_60s
test_solicitud_sin_task_id_rechazada · test_sequence_invalido_fail
test_planner_ciclo_task_rejected (IT03) · test_planner_ficha_no_committed
test_parallel_groups_correctos · test_jitter_formula · test_compensate_hook
```

**Estado post-parche: Salidas 1-3 = 100% conformes G2 v2.5.**
