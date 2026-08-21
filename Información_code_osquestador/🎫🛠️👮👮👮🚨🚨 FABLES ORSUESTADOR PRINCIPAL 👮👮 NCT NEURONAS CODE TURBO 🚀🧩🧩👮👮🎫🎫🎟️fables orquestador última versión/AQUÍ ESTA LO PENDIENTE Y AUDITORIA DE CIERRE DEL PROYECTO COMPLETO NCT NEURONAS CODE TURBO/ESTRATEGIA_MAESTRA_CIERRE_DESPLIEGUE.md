# ESTRATEGIA MAESTRA — RUTA DE CIERRE Y DESPLIEGUE NCT
# 2026-07-17 | Basado en auditoría de 5 salidas + hallazgos críticos

## ÍNDICE
1. Principio rector
2. Fase A — Solo transcribir (rápido, ya diseñado)
3. Fase B — Requiere tu aprobación (decisiones, no código)
4. Fase C — Solo código (sin decisiones pendientes)
5. Fase D — Integración (código ya existe, hay que conectarlo)
6. Fase E — Generación web/app (proyecto aparte, al final del código)
7. Fase F — Frontend/UI final (última, integra todo)
8. Despliegue
9. Tabla de seguimiento

---

## 1. PRINCIPIO RECTOR
**No se construye nada nuevo sin antes verificar si ya existe** (regla
que evita repetir el error de `loop_engine.py` duplicado). Orden fijo:
1º transcribir lo decidido → 2º decidir lo pendiente → 3º programar lo
que no tiene decisión pendiente → 4º integrar lo que ya existe → 5º lo
grande y nuevo (generador web/app) → 6º frontend → 7º desplegar.

---

## 2. FASE A — SOLO TRANSCRIBIR (ya diseñado y aprobado, sin decisiones)
No requiere tu aprobación — ya está aprobado en el ACTA/SALIDA_09. Solo
falta escribir el archivo.

| # | Archivo a crear | Contenido (ya definido) |
|---|---|---|
| A1 | `jueces_mapping.yaml` | J1-J10 con sus 5 fases + sistema de veto (ya tengo el detalle completo) |
| A2 | `adn/constitucion_39_mapping.md` | Tabla 39 artículos → destino v3 (ya tengo la tabla completa, 39/39) |
| A3 | `ma/ma_30_registry.yaml` | 30 MA con columna implementado_por (15 código + 15 fichas) |
| A4 | `exec/scale_plan.yaml` | Roadmap 300→800→1000 agentes por etapas |
| A5 | `org/estructura_historica_mapping.yaml` | R1-R11/Q1-Q10/TM01-12/5 Officers → absorbidos |
| A6 | `SALIDA_09` firma | Ratificar 325 fichas/16 repos como cifra oficial (ya explicado 265 vs 322) |

**Salida de esta fase:** 6 archivos, cero código nuevo, cero diseño
nuevo — solo pasar a limpio lo que ya está resuelto en la bandeja.

---

## 3. FASE B — REQUIERE TU APROBACIÓN (decisiones, no código)
Aquí SÍ te presento opciones y espero SÍ/NO antes de tocar nada.

| # | Decisión | Opciones |
|---|---|---|
| B1 | Vigencia de NCT/APEX y DOC_25 Bloque0 | ¿Historia superada / tienen requisitos vigentes que faltan? |
| B2 | Duplicado `loop_engine.py` vs `P-077` de Fable | ¿Cuál queda como versión única, o se fusionan? |
| B3 | Duplicado `recovery.py`/`tribunal.py` míos vs los de Fable (SALIDA_02) | Mismo tipo de decisión que B2 |
| B4 | TEMA A (doc→UOOS1): confirmar si se construye ya o después de Fase D | Orden de prioridad |
| B5 | Índice maestro de auditoría formal (documento único consolidado) | ¿Se construye ahora o se usa esta estrategia como sustituto? |

**Salida de esta fase:** tus respuestas B1-B5 desbloquean las fases C y D.

---

## 4. FASE C — SOLO CÓDIGO (sin decisiones pendientes, se ejecuta directo)

| # | Tarea | Detalle |
|---|---|---|
| C1 | Fichas nivel avanzado/arquitecto | Usando UOOS Parte 1 como guía, formato 5 campos, lotes de 50, tu revisión de 10 en 10 — empezar por las 65 P ya nombradas (Salida 2/5) |
| C2 | Gaps del Router (R1-R6, R8) | Cifrado+rotación+BYOK, reglas en archivo, batching, salud automática, retry, circuit breaker, caché — todo sin decisiones pendientes, solo construcción |
| C3 | Vigilancia continua del Orquestador (30s) | Sin decisión pendiente, se agrega a `recovery.py` (o su reemplazo, según B3) |
| C4 | TEMA B (motor cierre→UOOS2+despliegue, Opción 3 híbrida) | Ya aprobado, solo construir |

---

## 5. FASE D — INTEGRACIÓN (el código YA EXISTE, hay que traerlo y conectarlo)
Nada de esto se programa de nuevo — se copia, se verifica, se conecta.

| # | Qué integrar | De dónde |
|---|---|---|
| D1 | Kernel/ADN/Guardian | `SALIDA_01_KERNEL_NUCLEO.md` (código real, ~710 líneas) |
| D2 | Auditor de documentos Fase 0 (backend completo) | Tanda 3 — contracts.py+resilience.py+plugins+servidor MCP+manual 10 pasos |
| D3 | Detector de alucinaciones | `T-014 hallucination_check` (S13) — verificar archivo real antes de asumir que falta |
| D4 | Piezas del Router ya construidas por Fable (R1-R10 diseño) | `si_o_si.md` — comparar contra mi Router y fusionar huecos |
| D5 | Conexión MCP + API de todo lo anterior | Última acción de esta fase — es lo que "engancha" los repos aislados (Router/Orquestador/Auditor/Fichas) al sistema principal |

---

## 6. FASE E — GENERACIÓN WEB/APP (proyecto propio, el más grande, va aparte)
El gap más grande de toda la auditoría (Salida 4/5). No se mezcla con
las fases anteriores — merece su propio ciclo panel-de-expertos +
opciones + simulación cuando llegue su turno.

| # | Qué construir | Alcance |
|---|---|---|
| E1 | Generador de Design System | Colores/tipografía/tokens/dark-mode a partir de una especificación |
| E2 | Generador de boilerplates | Empezar por 2-3 stacks (ej. FastAPI+React, no los 10 de una vez) |
| E3 | Mobile/Desktop | Solo si el Director lo prioriza — es el más costoso de todos |

---

## 7. FASE F — FRONTEND/UI FINAL (la última, integra TODO lo anterior)
Se hace al final a propósito: solo tiene sentido diseñar la interface
definitiva cuando ya se sabe qué partes existen de verdad (A-E
resueltas). Incluye: unir mis 7 paneles ya construidos + lo que salga
de D5 (conexiones MCP/API) en una sola experiencia coherente.

---

## 8. DESPLIEGUE (al cerrar todo lo anterior)
Usa el vagón F22 ya construido y probado + su versión generalizada de
TEMA B (Fase C4): organizar → desplegar → detectar versión → subir.
Orden al agente: ejecutar, no decidir (regla ya establecida).

---

## 9. TABLA DE SEGUIMIENTO (marcar según avance)

| Fase | Ítems | Requiere aprobación | Estado |
|---|---|---|---|
| A — Transcribir | 6 | No | Pendiente iniciar |
| B — Decisiones | 5 | **Sí, tuya** | Pendiente tus respuestas |
| C — Código directo | 4 | No | Bloqueado por B4 (parcial) |
| D — Integración | 5 | Parcial (B1-B3) | Bloqueado por B1-B3 |
| E — Web/app | 3 | Sí, ciclo propio | Al final, sin iniciar |
| F — Frontend final | 1 | Sí, diseño final | Última, sin iniciar |
| Despliegue | 1 | No (ya probado) | Al cerrar todo |

**Camino más corto a resultados visibles:** A (hoy mismo, sin
bloqueos) → tus respuestas B1-B5 → C y D en paralelo → E → F →
despliegue.
