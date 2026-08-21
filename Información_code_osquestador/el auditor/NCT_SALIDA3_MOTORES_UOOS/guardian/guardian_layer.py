"""GUARDIAN_LAYER — máxima autoridad de seguridad.
6 checks. Cualquiera en True → RECHAZAR_SOLICITUD inmediato.
Consultado por: Kernel (cada solicitud), Sentinela (cada propuesta),
Recovery (cada acción), Juez (cada veredicto crítico).
Contract: contracts/guardian.contract.json
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable
import fnmatch
import logging

log = logging.getLogger("guardian")

# Rutas que NADIE (excepto Director) puede modificar — línea roja absoluta
RUTAS_INMUTABLES: tuple[str, ...] = (
    "orquestador-nucleo/adn/*",
    "orquestador-nucleo/guardian/*",
    "orquestador-nucleo/llm_juez/*",
    "contracts-schemas/*",
)


class Veredicto(Enum):
    PERMITIR = "PERMITIR"
    RECHAZAR_SOLICITUD = "RECHAZAR_SOLICITUD"


@dataclass(frozen=True)
class ResultadoGuardian:
    veredicto: Veredicto
    checks: dict[str, bool]          # nombre_check -> violado(True/False)
    razon: str = ""

    @property
    def permitido(self) -> bool:
        return self.veredicto is Veredicto.PERMITIR


@dataclass
class SolicitudGuardian:
    """Payload normalizado que el Kernel arma antes de consultar."""
    actor: str                        # "orquestador"|"team_agent"|"sentinela"|...
    accion: str                       # "ejecutar_pipeline"|"modificar_archivo"|...
    rutas_afectadas: list[str] = field(default_factory=list)
    modifica_adn: bool = False
    omite_auditoria: bool = False
    omite_trazabilidad: bool = False
    rompe_aislamiento: bool = False   # p.ej. import directo entre repos lejanos
    riesgo_seguridad: bool = False    # marcado por filtros A2 / Sentinel


def _viola_adn(s: SolicitudGuardian) -> bool:
    if s.modifica_adn:
        return True
    return any(
        fnmatch.fnmatch(ruta, patron)
        for ruta in s.rutas_afectadas
        for patron in RUTAS_INMUTABLES
    ) and s.accion.startswith("modificar")


def _viola_leyes(s: SolicitudGuardian) -> bool:
    # LEY_6: nadie escribe tools dentro del cerebro
    return any("orquestador-nucleo" in r and s.accion == "instalar_tool"
               for r in s.rutas_afectadas)


CHECKS: dict[str, Callable[[SolicitudGuardian], bool]] = {
    "VIOLA_ADN": _viola_adn,
    "VIOLA_LEYES": _viola_leyes,
    "VIOLA_AUDITORIA": lambda s: s.omite_auditoria,
    "VIOLA_TRAZABILIDAD": lambda s: s.omite_trazabilidad,
    "VIOLA_SEGURIDAD": lambda s: s.riesgo_seguridad,
    "VIOLA_AISLAMIENTO": lambda s: s.rompe_aislamiento,
}


class GuardianLayer:
    """Sin estado mutable de negocio: evalúa y registra, nada más."""

    def evaluar(self, solicitud: SolicitudGuardian) -> ResultadoGuardian:
        resultados = {nombre: chk(solicitud) for nombre, chk in CHECKS.items()}
        violados = [n for n, v in resultados.items() if v]
        if violados:
            razon = f"checks_violados={violados} actor={solicitud.actor}"
            log.warning("RECHAZAR_SOLICITUD %s", razon)
            return ResultadoGuardian(Veredicto.RECHAZAR_SOLICITUD,
                                     resultados, razon)
        return ResultadoGuardian(Veredicto.PERMITIR, resultados, "OK")

    def es_ruta_modificable(self, ruta: str) -> bool:
        """API directa para Sentinela (GUÍA E, línea roja)."""
        return not any(fnmatch.fnmatch(ruta, p) for p in RUTAS_INMUTABLES)


GUARDIAN = GuardianLayer()
