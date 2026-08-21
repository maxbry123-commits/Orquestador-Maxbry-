# AUDITORÍA NCT — SALIDA 1/5 — NÚCLEO/KERNEL/ROUTER/TRIBUNAL
# 3 pasadas por documento | Trazabilidad completa | 2026-07-17

## PASADA 1 — INVENTARIO (documentos auditados esta salida)
SALIDA_01 a SALIDA_10 (Fable) · PARCHE_GUIA_MAESTRO · ACTA_DECISIONES_
DIRECTOR · PARCHE_RECUPERACION_03 · SALIDA_01_KERNEL_NUCLEO (código) ·
NCT_APEX_PROTOCOLO_v3.0 (8 partes) · DOC_25_NCT_BLOQUE0 · PARTE_B_MAPA_
MENTAL_JSON

## PASADA 2 — HALLAZGO CRÍTICO: 3 LINAJES DE DISEÑO DISTINTOS EN LA BANDEJA

| Linaje | Fecha | Autor | Stack/protocolo | Estado |
|---|---|---|---|---|
| **NCT v3 "Kernel Transductor"** | 2026-07-12 | Fable | Router R1-R10, Enchufe v2.0, 322 fichas, determinismo estricto | **Vigente — es el que construí en este chat** |
| **NCT/APEX Protocolo v3.0** | sin fecha exacta, anterior | posiblemente "Kimi" (citado literal) | SEG_xxx segmentos, Approval Ledger, Capability Registry, PASS_KPI_SIGMA, chat-os header | **Sin confirmar si sigue vigente o fue reemplazado** |
| **DOC_25 Bloque 0 / Panel Expertos** | 2026-05-24 | Claude Opus 4.7 | Supabase+Neon+Qdrant+Redis, GitHub 2 repos, MAXBRY AI LLM CODE (Qwen 10B), Claude Code Chino (Qwen/GLM) | **Anterior a Fable — probablemente superado, sin confirmar** |

**Por qué importa:** el DOC_25 usa un stack TECNOLÓGICO distinto al que
construí (Qdrant/Supabase/Redis vs mi memoria local FAISS-style; "NO
Railway" explícito). Si ese documento sigue vigente, hay una
contradicción de infraestructura sin resolver. Si está superado, hay
que decirlo explícito para no auditar contra un fantasma.

**ACCIÓN REQUERIDA DEL DIRECTOR:** confirmar si DOC_25/NCT_APEX son
historia (superados por el ACTA del 12-jul) o si tienen requisitos que
todavía aplican y no se llevaron al diseño v3.

## PASADA 3 — CRUCE: LOS 30 REQUISITOS ORIGINALES (R01-R30) vs ENTREGADO

Fuente: `SALIDA_01_PLAN_MAESTRO_Y_PASADA_1.md`, tabla completa de 30
requisitos literales del Director, cada uno con su "cubierto en".

| Estado | Cantidad | Detalle |
|---|---|---|
| Cubiertos según Fable (S1-S10) | 30/30 | Fable declaró los 30 resueltos en sus propias 10 salidas |
| Verificados por mí con código real en este chat | 14/30 | R04(mejora raíz)·R05(diagramas H/T)·R11(motores)·R12(código ejecutable)·R13(DSL)·R19(estructura)·R20(Claude Code)·R25(loops)·R26(gaps con 🚩) parcial·R30(dividir en salidas) — el resto son de proceso/gobernanza, no de código |
| Sin verificar directamente | 16/30 | R02(parche guía)·R06(20 fases ChatGPT)·R07-R10(refutaciones/consensos/simulaciones/25pasos — documentales, no código)·R14-R18·R21-R24·R27-R29 |

## GAPS NUEVOS ENCONTRADOS EN ESTA SALIDA (no listados antes)

| # | Gap | Fuente | Qué falta |
|---|---|---|---|
| N1 | **R23 "20/21 fases de ChatGPT" — origen del término confirmado** | SALIDA_01 R06 | El roadmap de 21 fases se llama así porque el Director lo trajo originalmente de una conversación con ChatGPT — no es invención de Fable. No cambia nada técnico, pero aclara la trazabilidad de origen que pediste |
| N2 | Reconciliación de linajes (los 3 de la tabla de arriba) | Este hallazgo | Sin resolver — requiere decisión del Director, no código |
| N3 | Mesa de consenso: histórico dice 10 jueces J1-J10; SALIDA_05 la define como "5 originales + 5 nuevos + Devil, quorum 6/10" | SALIDA_05 checkpoint | Esto es DISTINTO a mi `consenso10.py` (que hice sin roles nombrados, solo mesa-5/mesa-10 genérica) — falta nombrar los 10 roles específicos en mi código |
| N4 | AUD-2P (auditoría de 2 pasadas) sobre las 235 mejoras, condición puesta por el ACTA antes de integrarlas | ACTA sección 0 | No ejecutada — es un prerrequisito que el ACTA exige antes de tocar las 235 mejoras del backlog (S8B) |

## RESUMEN SALIDA 1/5
3 linajes de diseño detectados (1 vigente confirmado, 2 sin confirmar
vigencia) · 30 requisitos originales cruzados (14 verificados con
código real, 16 solo documentales) · 4 gaps nuevos · Acción pendiente
del Director: confirmar vigencia de DOC_25/NCT_APEX.

→ Sigue Salida 2/5: fichas P/S/T completas + Router/Auditor si_o_si
