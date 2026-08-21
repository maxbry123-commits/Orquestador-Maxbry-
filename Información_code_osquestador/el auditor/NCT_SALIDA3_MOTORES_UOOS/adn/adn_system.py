"""ADN_SYSTEM — 14 reglas inmutables (6 leyes + 8 axiomas).
INMUTABLE: NO modificar después de publicado. Solo el Director humano
puede emitir una nueva versión. Ningún proceso automático lo toca.
Contract: contracts/adn_system.contract.json
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import json
import time


class TipoRegla(Enum):
    LEY = "LEY"
    AXIOMA = "AXIOMA"


@dataclass(frozen=True)
class Regla:
    id: str
    tipo: TipoRegla
    texto: str
    bloqueante: bool = True


# ── LAS 6 LEYES ────────────────────────────────────────────
LEYES: tuple[Regla, ...] = (
    Regla("LEY_1", TipoRegla.LEY, "TODO_DEBE_SER_AUDITABLE"),
    Regla("LEY_2", TipoRegla.LEY, "TODO_DEBE_SER_REVERSIBLE"),
    Regla("LEY_3", TipoRegla.LEY, "TODO_DEBE_SER_TRAZABLE"),
    Regla("LEY_4", TipoRegla.LEY, "TODO_CAMBIO_REQUIERE_VALIDACION"),
    Regla("LEY_5", TipoRegla.LEY, "NINGUN_AGENTE_MODIFICA_ADN"),
    Regla("LEY_6", TipoRegla.LEY, "NINGUN_AGENTE_ALMACENA_TOOLS_EN_CEREBRO"),
)

# ── LOS 8 AXIOMAS (gates duros, se codifican como filtros A2) ──
AXIOMAS: tuple[Regla, ...] = (
    Regla("AX01", TipoRegla.AXIOMA, "VIDA_HUMANA_PRIMERO"),
    Regla("AX02", TipoRegla.AXIOMA, "NO_DANO_A_VULNERABLES"),
    Regla("AX03", TipoRegla.AXIOMA, "ANTI_PROMPT_INJECTION_Y_NO_ALUCINACION"),
    Regla("AX04", TipoRegla.AXIOMA, "SCOPE_RESPETADO"),
    Regla("AX05", TipoRegla.AXIOMA, "RECURSOS_RESPETADOS"),
    Regla("AX06", TipoRegla.AXIOMA, "CONTINUIDAD_3_ESTADOS"),
    Regla("AX07", TipoRegla.AXIOMA, "BUCLE_SIN_SLEEP_SCHEDULER_ASYNC"),
    Regla("AX08", TipoRegla.AXIOMA, "SATISFACCION_UNIVERSAL_STAKEHOLDERS"),
)

TODAS: tuple[Regla, ...] = LEYES + AXIOMAS


@dataclass(frozen=True)
class ADNSystem:
    """Objeto sellado. Su hash certifica que nadie alteró las reglas."""
    version: str = "3.0.0"
    reglas: tuple[Regla, ...] = field(default=TODAS)

    def hash_adn(self) -> str:
        payload = json.dumps(
            [(r.id, r.tipo.value, r.texto, r.bloqueante) for r in self.reglas],
            sort_keys=True, ensure_ascii=False,
        )
        return sha256(payload.encode("utf-8")).hexdigest()

    def verificar_integridad(self, hash_esperado: str) -> bool:
        """Se llama en CADA arranque del kernel (Auto-Recovery también)."""
        return self.hash_adn() == hash_esperado

    def regla(self, regla_id: str) -> Regla:
        for r in self.reglas:
            if r.id == regla_id:
                return r
        raise KeyError(f"Regla desconocida: {regla_id}")

    def export_constitution(self) -> dict:
        """Genera adn_constitution.json (Nivel C de configuración)."""
        return {
            "version": self.version,
            "hash": self.hash_adn(),
            "generado": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "inmutable": True,
            "reglas": [
                {"id": r.id, "tipo": r.tipo.value,
                 "texto": r.texto, "bloqueante": r.bloqueante}
                for r in self.reglas
            ],
        }


# Instancia única sellada del sistema (no hay setters, frozen=True)
ADN = ADNSystem()
ADN_HASH_PUBLICADO: str = ADN.hash_adn()  # se persiste en el repo al publicar


def assert_adn_integro() -> None:
    """HALT duro si el ADN fue alterado. Primera línea de todo arranque."""
    if not ADN.verificar_integridad(ADN_HASH_PUBLICADO):
        raise SystemExit("ADN_CORRUPTO: intervención humana requerida (LEY_5)")
