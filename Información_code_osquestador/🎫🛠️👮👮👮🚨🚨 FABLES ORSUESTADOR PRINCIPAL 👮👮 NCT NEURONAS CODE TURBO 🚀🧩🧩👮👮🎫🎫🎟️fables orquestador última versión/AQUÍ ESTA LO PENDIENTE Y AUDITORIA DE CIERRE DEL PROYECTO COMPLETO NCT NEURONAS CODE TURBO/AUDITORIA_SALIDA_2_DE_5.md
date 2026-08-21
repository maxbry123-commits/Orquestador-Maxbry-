# AUDITORÍA NCT — SALIDA 2/5 — FICHAS COMPLETAS (E/P/S/T/A)
# 3 pasadas | Trazabilidad completa | 2026-07-17
# Fuente principal: ESQUELETO_MAESTRO_PIPELINES.md

## PASADA 1 — INVENTARIO
322 fichas base (202 ✚nuevas + 120 originales) + 3 después = 325.
Estructura raíz confirmada:
```
repo 6  fichas/entrada/E-001..E-072
repo 5  fichas/procesador/P-001..P-135
repo 6  fichas/salida/S-001..S-055
repo 11 transversales/T-001..T-045
repo 2  aceleradores/A-001..A-015 (YAML puro, 0 código)
```

## PASADA 2 — NOMBRES REALES EXTRAÍDOS (ampliado desde Salida 1/5)
- E: E-001 a E-005 + E-072 (gate final) confirmados con nombre
- P: P-001 a P-030 (planificación+razonamiento) y P-076 a P-110
  (ejecución+calidad) confirmados — 65 de 135 con nombre
- S: S-001 a S-008 confirmados
- A: las 15 completas, confirmadas
- T: 0 nombres extraídos aún (pendiente Salida 3)

## PASADA 3 — HALLAZGO CRÍTICO: FICHAS MARCADAS "(ya)" = CÓDIGO REAL DE FABLE

Varias fichas P traen la marca **"(ya)"** = ya construidas por Fable
con código real, ANTES de que yo construyera nada en este chat:

| Ficha | Qué es | Mi posible duplicado en este chat |
|---|---|---|
| P-001 planner_offline | Compila requirements→sequence.json | Se relaciona con mi `gcl/goal_tree.py` — NO es lo mismo (el mío arma el árbol de metas, planner_offline compila el plan completo) — **complementarios, no duplicados** |
| P-076 ez_pipeline_16 | P-DISCOVER→P13, anti-humo | No tengo equivalente — **no es gap, ya existe** |
| P-077 loop_engine_9fases | Motor cognitivo aislado, escala 20-1000 | **POSIBLE DUPLICADO DIRECTO** de mi `loop_engine/engine.py` (ciclo de 9 fases que yo también construí) — mismo nombre conceptual, necesita comparación línea a línea |
| P-078 loops_infra_10 | Heartbeat/signals/DLQ/meta-loop | No tengo equivalente construido — **no es gap, ya existe en Fable** |
| P-079 handoff_builder | Sobre firmado orquestador→team | No tengo equivalente directo |
| P-080 team_core | Cerebro team ≤300 LOC | No construí esto — **ya existe en Fable, falta integrar** |
| P-099 llm_capsula | LLM provider-ciego vía Router | Se relaciona con mi `router/seleccion.py` — revisar solape |

**Conclusión:** de las fichas "(ya)", solo **P-077 (loop_engine_9fases)
es un duplicado directo confirmado** con mi trabajo — construí mi
propio motor de 9 fases sin saber que Fable ya tenía uno. Los demás
"(ya)" son piezas que Fable construyó y yo simplemente no toqué (no
son gaps, son integración pendiente, igual que el Kernel).

## GAPS DE FICHAS CONFIRMADOS (sin código en ningún lado)
De las 65 P nombradas: **0 tienen código real mío ni confirmado de
Fable**, salvo las marcadas "(ya)" (11 de 65). Faltan 54 de las 65
nombradas + 70 sin nombre extraer aún (P-031 a P-075).

## RESUMEN SALIDA 2/5
1 duplicado directo confirmado (P-077 vs mi loop_engine) · 6 piezas de
Fable ya construidas que solo faltan integrar · 54+70 fichas P sin
código en ningún lado · T-001 a T-045 completamente sin auditar (rep.
a Salida 3).

→ Sigue Salida 3/5: biblioteca 21 fases (contenido) + T-001..T-045
