"""FUSIÓN JUEZ (D2/D3: Fable manda, mi tabla se conserva como mapeo oficial)
+ VIGILANCIA CONTINUA 30s (gap del Orquestador, diseño F5 de Fables).

JuezKernel: adaptador que expone la interfaz PuertoJuez que KernelCore de
Fables espera (goal_lock_activo + veredicto async), respaldado por la tabla
de 16 pasos del Grupo 1. UNA sola fuente de verdad para juzgar — se acabó
el duplicado.

Vigilante30s: watchdog del diseño F5 — cada tarea reporta latido; si un
latido envejece más del límite, el vigilante escala (recovery/rotación).
"""
from __future__ import annotations
import asyncio
import time

from tribunal.juez_16_pasos import SECUENCIA_16, Juez16Pasos

# ── FUSIÓN: el juez de 16 pasos como PuertoJuez del Kernel ─────────────

# Qué pasos de la tabla 16 aplican en cada fase del kernel de Fables
PASOS_POR_FASE = {
    "P1_INPUT":   ("P-DISCOVER", "P-01", "P-02", "P-03"),
    "P2_PROCESS": ("P-04", "P-05", "P-06", "P-07", "P-08", "P-09",
                   "P-10", "P-11"),
    "P3_OUTPUT":  ("P-12", "P-12B", "P-13A", "P-13"),
}


class JuezKernel:
    """Cumple el Protocol PuertoJuez de kernel_core.py (Fables).
    goal_lock_activo() → del GoalLock real de F0.
    veredicto(fase, resultado) → corre el Juez16Pasos del Grupo 1 con la
    evidencia de la fase: los pasos de OTRAS fases se auto-acreditan
    (ya fueron o serán juzgados en su propia fase). Una sola fuente de
    verdad para juzgar — se acabó el duplicado."""

    def __init__(self, goal_lock=None, checks: dict | None = None):
        self._lock = goal_lock
        self._juez = Juez16Pasos(checks)

    def set_goal_lock(self, lock) -> None:
        self._lock = lock

    def goal_lock_activo(self) -> bool:
        return self._lock is not None

    async def veredicto(self, fase, resultado):
        """El kernel pasa Fase y ResultadoFase; devolvemos su Clasificacion."""
        from kernel.kernel_core import Clasificacion   # import tardío
        fase_id = getattr(fase, "value", str(fase))
        pasos_de_fase = set(PASOS_POR_FASE.get(fase_id, ()))
        payload = resultado.payload if isinstance(resultado.payload, dict) else {}
        evidencias = dict(payload.get("evidencias", {}))
        # los pasos que NO son de esta fase se acreditan automáticamente
        for paso_id, *_ in SECUENCIA_16:
            if paso_id not in pasos_de_fase:
                evidencias.setdefault(paso_id, True)
        acta = self._juez.ejecutar({"evidencias": evidencias})
        payload["acta_juez"] = {"puntaje": acta["puntaje"],
                                "veredicto": acta["veredicto"],
                                "firma": acta["firma"]}
        if acta["veredicto"] == "APROBADO":
            return Clasificacion.PASS
        if acta["puntaje"] >= 50:                  # dudoso → que decida humano
            return Clasificacion.ESCALATE
        return Clasificacion.FAIL


# ── VIGILANCIA CONTINUA 30s (diseño F5) ────────────────────────────────


class Vigilante30s:
    """Cada tarea registrada debe dar latido. Si el último latido supera
    `limite_s`, el vigilante la marca ATASCADA y llama al escalador
    (recovery: reintentar, rotar estrategia o avisar al Director)."""

    def __init__(self, limite_s: float = 90.0, intervalo_s: float = 30.0,
                 escalador=None, reloj=time.monotonic):
        self.limite_s = limite_s
        self.intervalo_s = intervalo_s
        self.escalador = escalador or (lambda t, e: None)
        self._reloj = reloj
        self._tareas: dict[str, dict] = {}
        self._corriendo = False

    def registrar(self, task_id: str, descripcion: str = "") -> None:
        self._tareas[task_id] = {"desc": descripcion,
                                 "ultimo_latido": self._reloj(),
                                 "estado": "VIVA", "escaladas": 0}

    def latido(self, task_id: str) -> None:
        if task_id in self._tareas:
            t = self._tareas[task_id]
            t["ultimo_latido"] = self._reloj()
            if t["estado"] == "ATASCADA":
                t["estado"] = "VIVA"               # se recuperó sola

    def terminar(self, task_id: str) -> None:
        self._tareas.pop(task_id, None)

    def revisar_una_vez(self) -> list[dict]:
        """Una pasada del watchdog. Devuelve las escaladas de esta ronda."""
        ahora = self._reloj()
        escaladas = []
        for tid, t in self._tareas.items():
            edad = ahora - t["ultimo_latido"]
            if edad >= self.limite_s and t["estado"] == "VIVA":
                t["estado"] = "ATASCADA"
                t["escaladas"] += 1
                evento = {"task_id": tid, "desc": t["desc"],
                          "sin_latido_s": round(edad, 1),
                          "escalada_n": t["escaladas"]}
                self.escalador(tid, evento)
                escaladas.append(evento)
        return escaladas

    async def correr(self) -> None:
        self._corriendo = True
        while self._corriendo:
            self.revisar_una_vez()
            await asyncio.sleep(self.intervalo_s)

    def detener(self) -> None:
        self._corriendo = False

    def estado(self) -> dict:
        return {tid: t["estado"] for tid, t in self._tareas.items()}
