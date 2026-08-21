# PARCHE DETALLADO — TODOS LOS PENDIENTES Y GAPS, CON TRAZABILIDAD
# NCT | 2026-07-17 | Uso: reconstruir el estado exacto en otro chat sin perder detalle
# Cada ítem trae: qué es, de dónde salió (cita), y qué se necesita EXACTO para cerrarlo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — LOS 11 GAPS DE LA MATRIZ HISTÓRICA (25 elementos vs Kernel v3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Trazabilidad de origen:** `SALIDA_02_AUDITORIA_PASADAS_2_3.md`, sección
"PASADA 3 — MATRIZ DE VERIFICACIÓN CRUZADA (histórico → Kernel v3)".
Cita textual de la tabla completa de Fable (25 filas, columnas:
Elemento | Estado en Kernel v3 | Evidencia):

```
14 | Goals 10-50 distribuidos en procesos | 🚩 | Solo existe 1 GoalLock
   global; multi-goal por fase no diseñado
15 | Consenso 10 roles + consolidación | 🚩 | Decision Engine v2 = 5
   agentes+Devil (quorum 3/5). Histórico CSA=10 jueces, si_o_si=10
   roles. Reconciliar
16 | CSA 10 Jueces J1-J10 | 🚩 | Jueces 3 niveles G2 existen, pero
   mapeo J1-J10→niveles no escrito
17 | Constitución 39 principios | 🚩 | ADN=14 reglas (6 leyes+8
   axiomas). Tabla 39→14 (qué absorbió qué) no existe
18 | 30 MA (MA-01..30) vs 15 MA-* | 🚩 | FABLES definió 15; histórico
   intocable dice 30
19 | 3 Monitores PAD/Anxiety/Drift | 🚩 | No aparecen en Kernel v3
20 | 1000 agentes coordinados | 🚩 | Pools 80/15/5 + 300 expertos ≠
   1000; escala declarativa no diseñada
21 | 1000+ bucles/loops diferentes | 🔶 | 4 niveles × 9 fases ×
   policies = combinatoria alta; catálogo explícito no generado
22 | Piloto automático / continuous runtime | 🔶 | Sistema 24h en
   docs históricos + heartbeat S15; wiring proactivo no cableado
23 | 11 roles R1-R11 / 10 queues / 12 TM / 5 officers | 🚩 | Sin
   equivalente explícito en v3
24 | Regla "solo agregar capas, nunca reemplazar" | 🔶 | v3 evolucionó
   (reemplazó estructuras); necesita ACTA DE EVOLUCIÓN aprobada por
   Director para legalizar los cambios
25 | 322 fichas vs ~265 archivos | 🚩 | Pregunta abierta P5 del
   checkpoint — reconciliación numérica pendiente
```

**Regla histórica citada literal** (de la misma fuente, grupo G-A):
*"SOLO AGREGO capas, NUNCA reemplazo" · "MANTENER nombres originales" ·
"Mantener cantidades exactas" · "NUNCA crear/cambiar sin APROBADO
explícito de MAX"*

### Estado tras cruce con el código de este chat (auditoría propia, 2026-07-17)

| # | Elemento | Cerrado en este chat? | QUÉ FALTA EXACTO PARA CERRAR |
|---|---|---|---|
| 14 | Goals 10-50 por fase | No | Decisión del Director: ¿1 GoalLock global (como está) o rediseñar `gcl/goal_tree.py` para aceptar N árboles, uno por cada una de las 21 fases? Si se aprueba rediseño: modificar `ConstructorArbol` para aceptar `fase_id` y permitir múltiples árboles activos simultáneos en `state.json` |
| 15 | Consenso 10 roles | Parcial | Tengo mesa-10 en `decision/consenso10.py` (quorum 6/10). Falta: mapear esos 10 roles a los J1-J10 históricos por nombre exacto — tabla de equivalencia explícita, aprobada por el Director |
| 16 | CSA J1-J10 mapeo | No | Escribir la tabla `jueces_j1_j10.yaml`: qué juez histórico (J1..J10) corresponde a qué inspector actual del Tribunal (Sheriff/Centinela/Juez/Supervisor/Validador/Verificador) — puede requerir crear 4 roles nuevos si no hay equivalencia 1:1 |
| 17 | 39 principios → 14 reglas ADN | No | Leer el documento fuente de los 39 principios (dentro de `MAXBRY_SUPER_TEAM` según cita) y escribir tabla `constitucion_39_a_14.yaml` mostrando qué principios se fusionaron en cada una de las 14 reglas del ADN — requiere localizar el documento de los 39 principios completos en la bandeja (aún no leído en detalle en este chat) |
| 18 | 30 MA vs 15 MA | No | Decisión del Director: ¿ampliar mis 15 MA-* actuales a 30 (nombrando los 15 que faltan) o declarar formalmente que 15 absorbe a los 30 (requiere Acta de Evolución firmada, por la regla "nunca reducir cantidades" citada arriba)? |
| 19 | 3 Monitores | **Sí, cerrado** | `monitores/monitores.py` ya implementa PAD/Anxiety/Drift. Sin acción pendiente |
| 20 | 1000 agentes coordinados | No | Diseñar el mecanismo de escalado: cómo los pools actuales (80/15/5 + 300 expertos) crecen hasta 1000 sin romper el Router (relacionado con gap Router R7 Provider Pool). Requiere: plan de escalado por etapas + prueba de estrés a 1000 agentes reales (no solo 1000 requests HTTP, que ya probé) |
| 21 | 1000+ loops | Parcial — CONFLICTO DE TAXONOMÍA | Construí 1080 loops en `loop_engine/catalogo.py` con taxonomía propia (4 niveles × 9 fases × 30 dominios). El documento histórico pide una taxonomía DISTINTA: 10 familias (verificación/refinamiento/investigación/consenso/reparación/exploración/consolidación/vigilancia/aprendizaje/escalado) × 20 tareas × 5 intensidades = 1000. **Decisión del Director requerida:** ¿mantener mi taxonomía, migrar a la histórica, o mapear una contra otra? |
| 22 | Piloto automático continuo | Parcial | Tengo `initiative.py` (S07, base) y `notify_and_continue`. Falta: cablear el modo continuo real 24h (que el sistema hable sin que el usuario le pregunte primero) — no construido en este chat |
| 23 | 11 roles/10 colas/12 TM/5 oficiales | No | Sin diseño ni código. Requiere: localizar el documento fuente completo de R1-R11/Q1-Q10/TM01-TM12/5 Officers (mencionado pero no leído en detalle) y decidir si se integran o se declaran obsoletos por Acta de Evolución |
| 24 | Acta de Evolución | Pendiente de firma | El documento (`SALIDA_09_LISTA_REGALOS_SANTA.md`, gap G-15) ya está redactado — falta que el Director lo firme explícitamente. Esto es una APROBACIÓN, no una construcción |
| 25 | 322 vs 265 fichas | Parcial | Cifra oficial actual: 325 (322+3). Falta: confirmar de dónde salió el número "265" citado en el documento histórico — puede ser un conteo de archivos físicos vs fichas lógicas (1 archivo puede contener varias fichas). Requiere auditoría literal de esa fuente específica |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — GAPS DEL ROUTER (7), CON QUÉ CERRARLOS EXACTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Trazabilidad:** `si_o_si.md`, "BLOQUE 5 — API ROUTER / DIAGRAMA
COMPLETO — NCT API ROUTER v0.2", módulos R1-R10 + Cost Optimizer.
Documento propio generado en este chat: `GAP_01_ROUTER.md`.

| # | Gap | Qué existe hoy | QUÉ FALTA EXACTO |
|---|---|---|---|
| R1 | Cifrado+rotación+BYOK | `router/auth.py` maneja tokens propios sin cifrar | Agregar cifrado AES-256 a las keys en reposo (librería `cryptography`), función de rotación programada (cron o loop interno), y endpoint para que el cliente registre su propia key (BYOK) |
| R2 | Reglas en archivo declarativo | `router/seleccion.py` tiene la lógica en código Python | Crear `capability.json` con el esquema de reglas (task_type, budget, latency_sla, capability, provider_health, cost_per_token, license) y reescribir `seleccion.py` para leer ese archivo en vez de tener la lógica fija |
| R3 | Batching (batch_size 20, overlap 5) | `router/cola.py` prioriza pero no agrupa | Agregar función `agrupar_lotes(cola, tamano=20, solape=5)` que tome N tareas y las despache juntas cuando hay 200+ pendientes |
| R4 | Salud automática 30s | `router/balanceo.py` marca sano/no-sano manual | Agregar un loop en segundo plano (`asyncio` o hilo) que haga ping cada 30s a cada destino, mida p95 de latencia y tasa de error, y dispare alerta si el costo por hora supera un umbral configurable |
| R5 | Retry a nivel Router | Solo existe recovery a nivel sistema general (`recovery/recovery.py`) | Agregar reintentos específicos DENTRO del Router antes de que la tarea suba al sistema de recovery general — 2-3 intentos inmediatos por fallo de red |
| R6 | Circuit Breaker | No existe | Nueva clase `CircuitBreaker` en `router/`: cuenta fallos consecutivos por proveedor, y tras N fallos lo saca de rotación por T segundos automáticamente |
| R8 | Caché semántico | No existe | Nuevo módulo que compare la solicitud entrante contra las últimas N respondidas (por similitud, no exacta) y reuse la respuesta si coincide lo suficiente — requiere decidir el motor de similitud (embeddings locales vs hash) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 3 — GAPS DEL ORQUESTADOR PRINCIPAL (3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Trazabilidad:** `SALIDA_01_KERNEL_NUCLEO.md` (código real, ~710
líneas) + `PARCHE_RECUPERACION_03_ESTADO_ACTUAL.md`.
Documento propio: `GAP_02_ORQUESTADOR_PRINCIPAL.md`.

| # | Gap | QUÉ FALTA EXACTO |
|---|---|---|
| O1 | Vigilancia continua 30s | Construir loop de auto-chequeo dentro de `recovery/recovery.py` que corra solo cada 30s, sin esperar que algo falle primero (hoy es reactivo, no proactivo) |
| O2 | LLM_JUEZ 16 pasos | Alinear `tribunal/tribunal.py` (6 inspectores) contra la secuencia de 16 pasos citada (P-DISCOVER→P13) — puede requerir dividir cada inspector actual en sub-pasos, o mapear 1:1 y documentar la equivalencia |
| O3 | Reconciliar duplicados | Comparar línea por línea mi `recovery.py`/`tribunal.py` contra el código real de Fable en `SALIDA_02` (LLM_JUEZ+Recovery 6 niveles) — decidir cuál queda como versión única, o fusionar tomando lo mejor de cada uno |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 4 — GAPS DEL AUDITOR DE DOCUMENTOS (1 confirmado + 2 sin verificar)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Trazabilidad:** `CHECKPOINT_AUDITORIA_MAESTRO.md` (Tanda 3) +
`si_o_si para el orquestador Maxbry.md` (código Python de ejemplo con
OCR Baidu + Graphiti + Obsidian + detector de alucinaciones).
Documento propio: `GAP_03_AUDITOR_DOCUMENTOS.md`.

| # | Gap | QUÉ FALTA EXACTO |
|---|---|---|
| A1 | Detector de alucinaciones | Construir módulo nuevo (no existe en ningún lado): recibe una afirmación + sus fuentes citadas, compara contra el texto real de la fuente, devuelve confianza 0-1 o rechazo si no encuentra respaldo. Hay código Python de referencia real en `si_o_si para el orquestador Maxbry.md` — falta portarlo/adaptarlo |
| A2 | Verificar plugins reales | Abrir y leer el contenido interno real de los archivos "plugins" (inputs/outputs/agents/workflows) mencionados en `SALIDA_2_v2_B_plugins` — confirmar si Obsidian/Graphiti/OCR/Kanboard tienen código real o son plantillas vacías. Acción: búsqueda específica en bandeja del contenido interno de esos 4 plugins |
| A3 | Credenciales en providers.yaml | Una vez confirmado A2, agregar los 4 servicios a la configuración de proveedores (solo nombres de variables de entorno, nunca valores) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 5 — FICHAS (325 totales)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Trazabilidad:** `ESQUELETO_MAESTRO_PIPELINES.md` (nombres reales
E-001 a E-005+, P-111 a P-135, S-001 a S-008, A-001 a A-015 completas).

| Categoría | Total | Con código real | QUÉ FALTA EXACTO |
|---|---|---|---|
| E (Entrada) | 72 | ~20 (mías, E-001 a E-020) + 10 (Fable, E-017 a E-026) | **Conflicto de numeración confirmado**: mi E-003 (hash+lock) no es la E-003 real (`ack_engine`); mi contenido corresponde a la E-004 real (`hash_engine`). Hay que renumerar mis 20 fichas contra los nombres reales del esqueleto maestro, ficha por ficha, antes de continuar. Faltan ~42-52 sin tocar |
| P (Proceso) | 135 | 0 | Nombres reales conocidos solo para P-111 a P-135 (25). Faltan P-001 a P-110 — sus nombres deben extraerse de la bandeja (no completado aún) |
| S (Salida) | 55 | 0 | Nombres reales conocidos: S-001 a S-008 (8). Faltan S-009 a S-055 (47) — nombres sin extraer |
| T (Transversales) | 45 | 0 | Ningún nombre extraído todavía — pendiente búsqueda específica |
| A (Aceleradores) | 15 | 0 (son YAML de perfil, 0 líneas de código por diseño) | Los 15 nombres SÍ están completos (nivel_0_rapido … perfil_movil) — falta escribir los 15 archivos YAML reales |

**Regla del Director para esta ronda:** las fichas que se construyan
ahora deben ser SOLO nivel avanzado y nivel arquitecto (no niveles
básicos), usando el formato UOOS Parte 1 como guía de construcción.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 6 — LOS 2 TEMAS GRANDES (motores genéricos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### TEMA A — motor genérico documento→UOOS Parte 1
**Aprobado por el Director:** construir AMBAS alternativas (Opción 1 +
Opción 3), no solo una.

- **Opción 1 (reglas, determinista):** detector de estructura por
  patrones fijos (encabezados "Objetivo:", listas, tablas) → llena
  B1-B4 de UOOS. QUÉ FALTA: escribir el módulo completo, no existe
  ningún código de esto todavía.
- **Opción 3 (híbrido):** Opción 1 primero, luego un LLM llena SOLO
  los huecos que quedaron vacíos, y el Tribunal verifica cada relleno
  contra el texto original antes de aceptarlo. QUÉ FALTA: lo mismo que
  Opción 1, más el paso de verificación con Tribunal — ninguno de los
  dos está construido aún, solo explicado en este chat.

### TEMA B — motor genérico cierre→UOOS Parte 2+despliegue
**Aprobado por el Director:** Opción 3 (híbrida).
- Mecanismo: buscar `config.yaml` del proyecto → si existe, usarlo; si
  no, usar auto-detección (la que ya tiene `despliegue/organizador.py`).
- QUÉ FALTA: agregar el paso de "buscar config.yaml primero" al
  organizador actual — es una modificación pequeña sobre código ya
  existente y probado, no una construcción desde cero.

### Índice maestro de auditoría
QUÉ FALTA: no construido. Requiere recorrer TODA la bandeja + todo el
chat, fila por fila (formato ya definido en la Especificación del
PIPELINE, Bloque 3).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 7 — AUDITORÍA DE CAPACIDAD (¿produce app/web/software 100%?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Ya realizada en este chat.** Resultado literal: el núcleo SÍ produce
software real de punta a punta SI el objetivo ya viene estructurado
(demostrado con `main.py --demo`). Débil/vacío en: Fase 01 (idea),
Fase 02 (requisitos), Fase 04 (UX/UI parcial), Fase 15 (producto),
Fase 17 (UX research). QUÉ FALTA EXACTO: construir el "embudo de
entrada" — un componente que tome una idea vaga en lenguaje natural y
la convierta en los requisitos estructurados que el resto del sistema
sí sabe procesar. No diseñado, no construido.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 8 — AUDITORÍA PENDIENTE (4 de 5 salidas sin hacer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Salida 2/5: fichas P/S/T completas (nombres) + documentos Router/
  Auditor tipo `si_o_si` restantes sin leer en detalle
- Salida 3/5: contenido real de la biblioteca de 21 fases (más allá
  de los nombres ya extraídos — falta el detalle de checkpoints 251)
- Salida 4/5: frontend y generación de web/app — pendiente de revisar
  específicamente qué existe vs qué falta en ese tema
- Salida 5/5: cruce final consolidado de todo lo anterior

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 9 — INPUT/OUTPUT BLOCKS LITERALES DE ESTA RONDA (para trazabilidad)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**INPUT del Director (resumen de la instrucción que originó este parche):**
Pidió auditoría en 5 salidas de la bandeja + verificación cruzada con
el chat; dijo que nada se descarta, lo que no está debe integrarse;
ordenó iniciar creación de fichas nivel avanzado+arquitecto usando
UOOS Parte 1; aprobó TEMA A con Opción 1 Y 3 juntas; aprobó TEMA B con
Opción 3; pidió panel de expertos+3 debates+2 refutaciones+simulaciones
para las deficiencias (bloque pendiente, no ejecutado aún); pidió
revisar de nuevo qué falta de frontend y generación web/app; pidió
dividir todo en salidas separadas con aprobación una por una.

**OUTPUT de esta sesión (qué se entregó hasta ahora):**
Explicación de mecanismo de TEMA A (ambas opciones) y TEMA B (opción
3) · Salida 1/5 de la auditoría (matriz de 25 elementos, 11 gaps) ·
este parche detallado con trazabilidad completa.

**PENDIENTE INMEDIATO SIGUIENTE (para continuar en cualquier chat):**
Salida 2/5 de la auditoría (fichas P/S/T + Router/Auditor) — no
iniciada todavía.
