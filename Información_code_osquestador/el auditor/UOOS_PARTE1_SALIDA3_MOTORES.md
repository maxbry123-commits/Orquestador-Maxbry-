# UOOS PARTE 1 — SALIDA 3: MOTORES UOOS (TEMA A+B) + FUSIÓN JUEZ + VIGILANTE
## MODO_A · 2026-07-20 · Tribunal PASS · 13 tests + regresión 40 · 3 revisiones

## B1 — MANIFEST
- uoos/motor_tema_a.py ...... TEMA A: CUALQUIER doc aprobado → UOOS Parte 1
  (manifest+inventario+requisitos+DAG+plan tribunal+plan despliegue). 0% LLM,
  determinista con hash del doc origen. Genérico: no solo NCT.
- uoos/motor_tema_b.py ...... TEMA B: carpeta de código cerrado → UOOS Parte 2
  EJECUTABLE (orden exacta al agente + plan de repos + evidencia requerida).
  Generaliza el vagón F22. Archivos sin regla → pregunta al Director, no adivina.
- orquestador/juez_fusion_y_vigilante.py
  · JuezKernel: FUSIÓN del duplicado (D2/D3) — el Juez16Pasos del Grupo 1
    ahora ES el PuertoJuez del KernelCore de Fables. Partición perfecta de
    los 16 pasos en las 3 fases (test lo demuestra). Acta con firma adjunta
    a cada fase. UNA sola fuente de verdad para juzgar.
  · Vigilante30s: vigilancia continua del diseño F5 — latidos por tarea,
    escala ATASCADA una sola vez, revive con latido.
- tribunal/juez_16_pasos.py . heredado del Grupo 1 (sin cambios)

## B6 — TRIBUNAL + 3 REVISIONES
- R1: suite → cazó 1 defecto de sintaxis → corregido → 13/13 PASS
- R2: imports limpios + regalos generados con DATOS REALES verificados
- R3: determinismo x2 + regresión Salida1 (20/20) + Salida2 (20/20)
- Integración REAL probada: KernelCore de Fables corrió 3 fases juzgadas
  por el juez fusionado → PASS

## B7 — PLAN DE DESPLIEGUE
nct-backend/motores_uoos/ ← todo. pytest 13/13 → commit "Salida 3: motores
UOOS + fusión juez + vigilante" → push → verificar.py → detente.

## 🎁 REGALOS DEL TRINEO
🚂 TREN: UOOS1_GENERADO_DE_DOC_REAL_NCT.md — el motor A corrió sobre
   DOC2_BLOQUE2_ARQUITECTURA.md real del proyecto (6 fases detectadas).
🎄 ARBOLITO: UOOS2_GENERADO_DEL_KERNEL_REAL.md — el motor B corrió sobre
   la Salida 1 real (14 archivos, tests detectados, lote firmado).
🛷 TRINEO: uoos_cli.py — los 2 motores en 1 comando para cualquier proyecto.
