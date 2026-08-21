# NCT — GAPS DEL ORQUESTADOR PRINCIPAL (repo aislado)
# Fuente: SALIDA_01_KERNEL_NUCLEO.md (código real de Fable, confirmado)

## CORRECCIÓN IMPORTANTE SOBRE LO QUE YA DIJE ANTES
En la ronda anterior asumí que el Kernel (ADN + Guardian + Kernel Core)
podía ser un hueco. **Es falso** — encontré el código real, completo,
de Fable en la bandeja (`SALIDA_01_KERNEL_NUCLEO.md`, ~710 líneas entre
los 3 archivos). Esto NO es un gap: existe, está escrito, solo falta
integrarlo a mi estructura de repos (copiar el archivo, no programarlo
de nuevo).

## LO QUE SÍ EXISTE COMO CÓDIGO REAL (de Fable, no mío)

| Componente | Archivo | Qué hace |
|---|---|---|
| ADN System | `adn/adn_system.py` (~150 líneas) | 14 reglas inmutables (6 leyes + 8 axiomas), selladas con hash — nadie las cambia sin el Director |
| Guardian Layer | `guardian/guardian_layer.py` (~180 líneas) | 6 verificaciones de seguridad; cualquiera en falso = rechazo inmediato de la solicitud |
| Kernel Core | `kernel/kernel_core.py` (~380 líneas) | El cerebro mínimo: recibe, activa el pipeline, crea expertos, comparte estado, consolida, emite — nada más |

## GAPS REALES ENCONTRADOS

| # | Función requerida | ¿Existe? |
|---|---|---|
| O-1 | Auto-Recovery Engine con vigilancia interna cada 30s (sin depender de un ping externo) | **No construido por mí** — mi `recovery.py` reacciona a fallos reportados, pero no vigila solo de forma continua |
| O-2 | LLM_JUEZ de 16 pasos (P-DISCOVER→P13) como pipeline específico de juicio | Parcialmente — mi `tribunal.py` juzga con 6 inspectores, pero no sigue exactamente esta secuencia de 16 pasos con esos nombres |
| O-3 | Reconciliar mi Kernel/Tribunal/Recovery con los de Fable | **Pendiente de decisión tuya** — construí versiones propias de piezas que Fable ya había resuelto (ver nota abajo) |

## NOTA IMPORTANTE: posible duplicado, no solo del Router

Al buscar esto encontré que Fable también documentó (no solo diseñó,
sino con código real según `PARCHE_RECUPERACION_03`) piezas que YO
también construí por mi cuenta en este chat, sin saber que ya existían:

- **Recovery de 6 niveles + WAL** — Fable lo construyó (SALIDA_02/03).
  Yo también construí mi propio `recovery.py` con 6 niveles + WAL.
  Hay que comparar los dos y quedarnos con uno (o fusionar).
- **DSL DAG Sheriff** (genera diagramas automáticamente) — Fable lo
  construyó (SALIDA_04). Yo no construí un generador automático de
  diagramas — esto SÍ sería un gap real de mi lado.

## MICRO-DIAGRAMA DE CÓMO ENCAJAN LAS PIEZAS

```
ADN (reglas fijas) → Guardian (verifica cada solicitud) → Kernel Core
  (recibe→activa pipeline→crea expertos→consolida→emite)
     │
     └── se apoya en: Auto-Recovery (vigilancia continua) +
         LLM_JUEZ 16 pasos (veredictos) — ambos con código de Fable
         que aún no está copiado a mi estructura de salida
```

## RESUMEN: 3 gaps reales (Auto-Recovery continuo, alinear
LLM_JUEZ de 16 pasos, y decidir qué hacer con las piezas duplicadas)
+ 1 acción pendiente que no es un gap sino integración: copiar el
código real de Fable (Kernel/ADN/Guardian) a la estructura final.
