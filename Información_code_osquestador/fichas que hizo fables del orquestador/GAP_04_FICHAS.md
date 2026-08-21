# NCT — GAPS DE LAS FICHAS (repo aislado, se conecta después)
# Fuente: ACTA_DECISIONES_DIRECTOR.md + PARCHE_RECUPERACION_03

## ESTADO GENERAL (según tu propia regla: si ya está como ficha, no es gap)

Cifra oficial: 325 fichas totales (322 base + 3 nuevas), organizadas en
3 pipelines por letra (E=Entrada 72 · P=Proceso 135 · S=Salida 55) +
T=Transversales 45 + A=Aceleradores 15.

Con código REAL (no solo diseño/tabla), lo que existe hoy:

| Rango | Autor | Cantidad | Tema |
|---|---|---|---|
| E-017 a E-026 | Fable (código real, confirmado) | 10 | Seguridad |
| E-001 a E-020 | Yo, en este chat (2 lotes probados) | 20 | Input listener, sanitizar, INPUT LOCK, clasificar, perfil, semillas, PUSH_PING, goal, requisitos, SID, email, unicode, idioma, truncado, quitar-secretos, chunks, prioridad, tokens, dedupe, empacar |

**Nota de posible solape:** tus E-017-026 (Fable) y mis E-001-020 (yo)
tienen rangos de número distintos pero pueden tocar temas parecidos
(ambos son "Pipeline E", entrada). No es un error, pero cuando se junte
todo hay que revisar que no haya 2 fichas distintas resolviendo lo mismo
con el mismo número o con números que deberían ser el mismo.

## LO QUE FALTA (según tu regla: SOLO es gap si no está ni en ficha ni en código)

Como el diseño ya tiene las 325 fichas MAPEADAS (con tabla, nombre y
categoría, aunque sin código), **técnicamente no hay "gap" de fichas**
— están documentadas. Lo que falta es EJECUCIÓN, que tu propia ACTA ya
ordenó como plan (reinicio total, formato 5 campos, lotes de 50):

| # | Qué falta | Cantidad |
|---|---|---|
| F-1 | Fichas del Pipeline E sin código real | ~42 (72 totales − 30 ya hechas) |
| F-2 | Fichas del Pipeline P sin código real | 135 (0 hechas aún) |
| F-3 | Fichas del Pipeline S sin código real | 55 (0 hechas aún) |
| F-4 | Fichas Transversales sin código real | 45 (0 hechas aún) |
| F-5 | Fichas Aceleradoras sin código real | 15 (0 hechas aún) |

## MICRO-DIAGRAMA (el proceso que ya tienes definido para esto)

```
ficha diseñada (tabla) → generador de 5 campos (ya construido por mí:
`fichas/generador.py`) → lote de 50 → smoke test en jaula → revisión
tuya de 10 en 10 → firma al ledger → siguiente lote
```

## RESUMEN: no hay gaps de DISEÑO en fichas (325/325 mapeadas). El
"faltante" real es 295 fichas sin código todavía — pero eso ya está
planeado como proceso (no es un hueco sorpresa, es el plan de ejecución
que tu ACTA ya aprobó). El generador y el molde de lotes ya existen.
