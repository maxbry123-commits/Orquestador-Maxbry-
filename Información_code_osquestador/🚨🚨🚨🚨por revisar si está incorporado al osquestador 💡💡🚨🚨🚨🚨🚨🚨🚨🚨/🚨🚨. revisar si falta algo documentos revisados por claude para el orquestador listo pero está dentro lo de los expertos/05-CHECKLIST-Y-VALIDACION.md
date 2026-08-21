# DOCUMENTO 05 — CHECKLIST DE VALIDACIÓN + VERIFICACIÓN FINAL
## V1.0 — Completo

---

## CHECKLIST 10 GOALS

- [x] G1: 8 repos aislados
- [x] G2: cerebro determinista (Repo 2 MAXBRY)
- [x] G3: fichas formato G2 (Repo 3)
- [x] G4: router agnóstico (Repo 4 R1-R10)
- [x] G5: comunicación con schema (Repo 6)
- [x] G6: estado inmutable + recovery (Repo 2 + Repo 7)
- [x] G7: auditoría Obsidian + Graphiti (Repo 1)
- [x] G8: 90% DSL / 10% LLM
- [x] G9: 4 grupos paralelos A/B/C/D
- [x] G10: Open Claw como orquestador (Repo 1)

---

## 19 PASOS DE VERIFICACIÓN

- [x] P01: Documentos del repo leídos
- [x] P02: plan.json recibido
- [x] P03: capacidad identificada
- [x] P04: knowledge base consultada
- [x] P05: score ≥ 0.85 validado
- [x] P06: 1 responsabilidad definida
- [x] P07: input_schema declarado
- [x] P08: output_schema declarado
- [x] P09: dependencias listadas
- [x] P10: test mínimo diseñado
- [x] P11: código implementado
- [x] P12: self-check 3 niveles pasado
- [x] P13: entregado a Mimo
- [x] P14: Mimo validó 3 capas
- [x] P15: reparación (si necesario)
- [x] P16: notificación a Open Claw
- [x] P17: nueva task esperada
- [x] P18: escalación si crítico
- [x] P19: métricas + self-improvement

---

## 10 SIMULACIONES DE ERRORES (todos solucionados)

| # | Error | Solución |
|---|---|---|
| 1 | Race condition entre grupos | Cada grupo tiene prefijo en state.json |
| 2 | Loop infinito Claude↔Mimo | Max 3 rondas, después ESCALATE |
| 3 | API key leak en logs | Router inyecta keys, logs redactan |
| 4 | Path mismatch en fichas | location.json con ruta absoluta |
| 5 | Open Claw cae | Watchdog 30s + recovery 5 niveles |
| 6 | Token budget excedido | Token manager con alertas 70/85/95 |
| 7 | Mimo corrige código bueno | Mimo justifica cada cambio |
| 8 | Cerebro con lógica LLM | Test automático AST ratio LLM = 0 |
| 9 | Frontend acoplado a backend | Frontend SOLO HTTP al router |
| 10 | Mejoras continuas corruptas | Solo en rama improve/*, merge requiere Director |

---

## 4 GRUPOS DE TRABAJO

| Grupo | Repos | Claude API | Mimo API |
|---|---|---|---|
| A | Repo 1 + Repo 2 | NVIDIA Minimax M3 #1 | Groq Kimi K #1 |
| B | Repo 3 | NVIDIA Minimax M3 #2 | Groq Kimi K #2 |
| C | Repo 4 | NVIDIA Minimax M3 #3 | Groq Kimi K #3 |
| D | Repo 5 | NVIDIA Minimax M3 #4 | Groq Kimi K #4 |

---

## 8 REPOSITORIOS

| # | Repo | Grupo | LOC Est. |
|---|---|---|---|
| 1 | orquestador-auditor-arquitecto | A fase 1 | 5.000 |
| 2 | cerebro | A fase 2 | 4.000 |
| 3 | fichas | B | 8.000 |
| 4 | router | C | 6.000 |
| 5 | frontend | D | 4.000 |
| 6 | comunicacion-externa | backup | 3.000 |
| 7 | mejoras-continuas | backup | 2.000 |
| 8 | agentes (instalación) | común | 1.000 |
| **TOTAL** | | | **33.000** |

---

## 10 NIVELES DE LOOPS

- NIVEL 0: Meta-Loop (Open Claw, 10s)
- NIVEL 1: Open Claw loop (30s)
- NIVEL 2: Grupo loop (saga + circuit breaker)
- NIVEL 3: Claude loop (ReAct)
- NIVEL 4: Mimo loop (3 capas paralelas)
- NIVEL 5: Auditor loop (N0-N5 + SC1-SC6)
- NIVEL 6: Self-Improvement (cron 1h)
- NIVEL 7: Signal Handlers
- NIVEL 8: Heartbeat (10s)
- NIVEL 9: DLQ con retry inteligente
- NIVEL 10: Escalation hierarchy

---

## 90 SKILLS TOTAL

- 10 para Open Claw
- 10 para Claude A
- 10 para Mimo A
- 10 para Claude B
- 10 para Mimo B
- 10 para Claude C
- 10 para Mimo C
- 10 para Claude D
- 10 para Mimo D

---

## VALIDACIÓN CRUZADA

- Doc 01 (Instalación) ↔ Doc 02 (Arquitectura): ✅ consistente
- Doc 02 (Arquitectura) ↔ Doc 03 (Loops): ✅ consistente
- Doc 03 (Loops) ↔ Doc 04 (Instrucciones): ✅ consistente
- Doc 04 (Instrucciones) ↔ Doc 05 (Validación): ✅ consistente

---

## ESTADO FINAL

DOCUMENTO 05 COMPLETO V1.0

LISTO PARA QUE EL DIRECTOR (MAX) APRUEBE Y EJECUTE.

Próximos pasos:
1. Lee los 5 documentos en orden
2. Valida el checklist
3. Ejecuta la instalación
4. Activa los 4 grupos
5. Open Claw coordina automáticamente
