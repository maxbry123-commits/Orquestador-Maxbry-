```json
{
  "checkpoint_id": "PARCHE-FINAL-100X",
  "contenido": ["verificacion_3_pasadas_4_requisitos", "estimacion_LOC", "estrategia_sonnet", "mejoras_pipeline_anti_perdida", "3_simulaciones_con_refutacion", "parche_100x"],
  "resultado_verificacion": "3 de 4 requisitos CUBIERTOS en el diagrama, 1 PARCIAL (auto-mejora con consenso + ficha de trabajo — falta el ciclo completo explícito)"
}
```

# PARCHE FINAL — VERIFICACIÓN + ESTRATEGIA + SIMULACIONES + 100X

---

## 1. VERIFICACIÓN DE LOS 4 REQUISITOS (3 pasadas: diagrama vs bandeja vs chat)

| # | Requisito | Estado | Dónde está / qué falta |
|---|---|---|---|
| 1 | **Salida MCP y API** | ✅ CUBIERTO parcial → REFORZADO en este parche | Existía: 23 destinos multi-target (API REST, webhook, custom MCP), "frontend abierto" (cada botón UI = función MCP), interfaz MAXBRY (Python API + MCP server + CLI). **Faltaba**: caja explícita de OUTPUT GATEWAY en F9 — se añade abajo |
| 2 | **Formato DSL/DAG/Schema/Sheriff para enviar a agentes** | ✅ CUBIERTO | Handoff firmado (F3) + sequence.json schema (F2) + DSL#2 Agent Contract (añadir_1: contrato por agente individual) + Sheriff SH01-07. Ya integrado en Partes 1-2 |
| 3 | **Sentinela supervisando todo** | ✅ CUBIERTO | F5 completo (Guardian+watchdog+PAD/Ansiedad/Drift+6 detectores) + Sentinel_Security (NOTA_07) + Sentinela con ledger (F8). Ya integrado |
| 4 | **Auto-mejora: aprende→autocorrige→autoevalúa→busca fallas→CONSENSO→emite FICHA de trabajo** | ⚠️ PARCIAL | Existían las piezas sueltas (self_audit_engine, 3 scores, Sentinela, FailureRegistry, consenso 5 agentes) pero NO el ciclo completo conectado que pides. **SE CIERRA ABAJO** |

### GAP-PARCHE-001 · CICLO DE AUTO-MEJORA COMPLETO (cierra el requisito 4)
```
┌──────────────────────────────────────────────────────────────┐
│ CICLO AUTO-MEJORA (transversal, corre cada 10 artifacts)     │
│                                                              │
│ [1 APRENDE] FailureRegistry.causas_frecuentes() +            │
│   3 scores (QUALITY/EFFICIENCY/RELIABILITY) por ciclo +      │
│   embeddings de drift/ansiedad guardados                     │
│        │                                                     │
│ [2 AUTO-EVALÚA] self_audit_engine: compara ciclo N vs N-1    │
│   mejora→conserva | regresión→rollback reglas |              │
│   estancamiento→candidato a mutación                         │
│        │                                                     │
│ [3 BUSCA FALLAS] Sentinela observer: patrón ≥3 repeticiones  │
│   en procesos propios (no solo en outputs)                   │
│        │                                                     │
│ [4 CONSENSO] propuesta → panel 5 agentes                     │
│   (Creative/Innovation/Critic/Selection/Architecture)        │
│   3+ de acuerdo → procede | empate → Director                │
│        │                                                     │
│ [5 EMITE FICHA] genera FICHA-MEJORA-[ID].yaml:               │
│   {que_falla, evidencia(hashes), propuesta, alcance          │
│   (SOLO config_runtime/reglas YAML), riesgo, rollback_plan}  │
│   → entra al pipeline NORMAL (F2→F9) como cualquier tarea:   │
│   se revisa, se diseña, se repara — con Juez y Witness       │
│        │                                                     │
│ [6 APLICA] solo tras firma Director en ledger →              │
│   patch_engine 10 pasos (rollback auto si falla paso 7)      │
└──────────────────────────────────────────────────────────────┘
```
**Clave**: la mejora NO se aplica directo — se convierte en ficha que pasa por el MISMO pipeline que todo lo demás. El orquestador se mejora a sí mismo usando su propio proceso.

### GAP-PARCHE-002 · OUTPUT GATEWAY explícito (refuerza requisito 1)
```
F9 → [OUTPUT GATEWAY] → MCP server (tools registrados: cada capability = tool)
                      → API REST (JSON/archivo) + Webhook
                      → 23 destinos multi-target (Telegram/GitHub/HF/S3/...)
                      → selección adaptativa (aprende preferencia del Director)
```

---

## 2. ESTIMACIÓN DE LÍNEAS DE CÓDIGO

| Bloque | LOC nuevas | LOC copiadas (ya existen) |
|---|---|---|
| F0 Input Fabric (anchor/push_ping/filtros/goal_lock/input_block) | ~1.400 | ~400 (InputBlock ya escrito) |
| F1 Kernel (ADN/Guardian/FSM/Router) | ~200 (glue) | ~710 (SALIDA_01) |
| F2 Planner+Capability | ~300 | ~350 (planner_offline) |
| F3 Handoff+Sandbox pool | ~900 | ~250 (team_core parcial) |
| F4 Motor cognitivo+Loop+Workers | ~1.200 (worker pool doc30 + batching) | ~1.550 (H1-H4) + ~800 (motor razonamiento v4) |
| F5 Monitoreo (PAD/ansiedad/drift+detectores) | ~1.000 | ~300 (guardian/watchdog) |
| F6 Verificación (N0-N5/GCL/Jueces/Witness) | ~400 (glue) | ~1.700 (verifier+GCL/Z3+jueces+witness) |
| F7 Memoria (SQL+tiers+KG+crons) | ~1.200 | ~200 (schema SQL ya escrito) |
| F8 Recovery+Sentinela | ~500 | ~900 (SALIDA_02+S14) |
| F9 Entrega (3 archivos+gates+atlas) | ~600 | ~700 (SALIDA_04 sheriff+exporters) |
| Output Gateway (MCP+API) | ~900 | 0 |
| Ciclo auto-mejora | ~700 | ~300 (self_audit parcial) |
| Despliegue | 0 | ~350 (4 scripts entregados) |
| Coordinador NCT (fsm/classifier/router/planner/isolator/monitor/consolidator/repair, doc30) | ~960 | 0 |
| Tests (IT01-06 + unit) | ~3.500 | ~600 |
| **TOTAL** | **~13.760 nuevas** | **~9.110 copiadas** |

**≈ 22.900 LOC totales, de las cuales solo ~60% hay que escribir.** Coincide con la estimación histórica de última_versión_1 (~21.400 + tests). Con fichas de ≤200 LOC → **~70-80 fichas nuevas** a programar.

---

## 3. ESTRATEGIA PARA QUE SONNET HAGA EL CÓDIGO COMPLETO

Usando el PIPELINE (HTML del chat) + UOOS como método:

```
FASE A — PREPARACIÓN (1 sesión)
  A1. Índice maestro (exigido por ESPECIFICACION_PIPELINE_NCT_v2):
      ruta exacta de cada pieza + verificado SI/NO + fase donde aplica
  A2. Congelar los 3 diagramas (Partes 1-3) + este parche como
      DISEÑO INMUTABLE (hash) — UOOS L-docs congelados, UNLOCK solo Director
  A3. Generar sequence.json del PROYECTO DE CONSTRUCCIÓN mismo:
      orden = STATE→VERIFICATION→RUNTIME→KERNEL (regla DOC7 invertida)

FASE B — CONSTRUCCIÓN POR BLOQUES (UOOS Parte 1: 1 bloque por vez, OK del Director)
  B1. Cada salida de Sonnet = 1 bloque con el molde del PIPELINE:
      JSON encabezado + qué copia (ruta fuente) + qué escribe nuevo +
      tests con assertions ANTES del código (R-04 Escritor) + DoD 8 criterios
  B2. Regla anti-pérdida #1: Sonnet NUNCA re-genera código que existe —
      recibe la ruta y COPIA (lo mismo que GAP_02 ordenó para el kernel)
  B3. Regla anti-pérdida #2: cada bloque cierra con checkpoint JSON
      acumulativo (qué está DENTRO = aprobado; qué falta = pendiente)
      — la regla de oro del PIPELINE
  B4. Regla anti-pérdida #3: INPUT_BLOCK hook activo — Sonnet confirma
      lectura literal del bloque de diseño antes de escribir una línea

FASE C — VERIFICACIÓN CONTINUA (UOOS Parte 2: RT-30/RT-31 por bloque)
  C1. Cada bloque pasa N0-N5 + tests reales (Witness) ANTES del OK
  C2. GOAL CHECK: ¿el bloque cumple su fase del diagrama, no solo compila?
  C3. Al final: IT01-06 + AX01/AX02 + 18 checks de cierre

MEJORAS AL PIPELINE PARA NO PERDER INFORMACIÓN (las 4 claves):
  M1. TRAZA BIDIRECCIONAL: cada ficha lleva el ID del gap/documento
      de origen (#GAP-P2-046 → ficha F-xxx) — nada implementado sin origen,
      ningún gap sin ficha destino (verificable por script)
  M2. TABLA DE COBERTURA VIVA: script determinista compara lista de
      123 gaps vs fichas creadas → % cobertura por salida, gap huérfano = FAIL
  M3. CONTEXTO MÍNIMO POR BLOQUE: Sonnet recibe SOLO el diagrama de su
      fase + sus fuentes (no los 140 docs) — menos contexto = menos deriva
  M4. RE-INYECCIÓN: al compactar contexto, el bloque de diseño se
      re-inyecta (reload-after-compaction, GAP-P3-033)
```

---

## 4. TRES SIMULACIONES (trabajo → refutación → propuesta → reparación)

### SIM A — "Construye un scraper para el proyecto X"
- **Trabaja**: F0 clasifica media/code → F2 DAG 5 pasos → F4 escritor genera con tests → F6 N0-N5 PASS → Witness L4 PASS → F9 entrega.
- **REFUTO**: el scraper pasó todo... pero el sitio objetivo cambió su HTML ayer. El Witness testeó contra un fixture GUARDADO, no contra el sitio real. Evidencia "real" que no refleja realidad actual = agujero.
- **PROPONGO**: nueva clase de test en Witness L4: `EVIDENCIA_VIVA` — para artifacts que dependen de recursos externos, al menos 1 test contra el recurso real (con timeout y fallback a fixture si el recurso está caído, marcando el resultado como `PASS_STALE`).
- **REPARO**: se añade campo `evidencia_viva: true|false` al contract_template + Sheriff SH08 nuevo: artifact con dependencia externa sin test vivo → WARNING (no bloquea, pero queda registrado).

### SIM B — Auto-mejora: el sistema detecta que sus retries son ciegos
- **Trabaja**: ciclo auto-mejora [1-3]: FailureRegistry muestra ERR_TIMEOUT×47 en 10 ciclos, siempre resuelto en retry #3. Sentinela propone: "subir timeout base de 5s→12s".
- **REFUTO**: el consenso [4] la aprueba 4-1... pero el Critic señala: subir el timeout GLOBAL castiga a los artifacts rápidos (99% termina <3s). La propuesta trata un síntoma local como regla global — error clásico de auto-optimización.
- **PROPONGO**: la ficha [5] se corrige: timeout ADAPTATIVO por ficha (p95 histórico × 1.5, con piso 5s techo 30s), datos ya disponibles en usage_analytics (S-051).
- **REPARO**: ficha FICHA-MEJORA-001 entra al pipeline → Juez exige simulación 5x con distribución real de duraciones → 5/5 PASS → Director firma → patch_engine aplica. Lección guardada en T3: "propuestas de Sentinela sobre parámetros globales requieren análisis de distribución, no solo de frecuencia de fallo".
- **Esto valida el requisito 4 completo: aprendió→evaluó→halló falla→consenso refinó→ficha→revisión→reparación.**

### SIM C — Orden maliciosa/errónea del propio Director
- **Trabaja**: llega orden "borra la tabla agent_memory y reconstruye desde cero".
- **REFUTO**: F0 la clasifica y F1 la rutea... ¿y nadie la frena? El Guardian solo mira 6 booleanos de agentes, no órdenes destructivas del Director. Gap real: el sistema asume que el Director nunca se equivoca.
- **PROPONGO**: CAPA 9 Gobernanza ya tiene la matriz "bloqueada_siempre" — se añade categoría `DESTRUCTIVA_IRREVERSIBLE` (drop de tablas, borrado de hash-chain, rm de repos): requiere confirmación doble (comando + UNLOCK explícito) + snapshot previo automático obligatorio.
- **REPARO**: la orden se pausa → sistema responde: "Acción destructiva irreversible. Snapshot creado (id X). Confirma con: UNLOCK agent_memory". El Director conserva autoridad total, pero con un segundo paso — el mismo patrón que ya usa el UNLOCK de UOOS para documentos congelados.

---

## 5. PARCHE 100X — CÓMO SER 100 VECES MÁS AVANZADO

Fórmula compuesta (cada factor multiplica, evidencia de producción real):

```
┌────────────────────────────────────────────────────────────────┐
│ PARCHE 100X = 7 multiplicadores sobre el diseño ya cerrado     │
│                                                                │
│ ×4  BATCHING total: toda llamada LLM en lotes 8-16             │
│     (ya en F4.3 — extender a Jueces y Escritor)                │
│ ×3  REDIS STREAMS como pizarra: XADD/XREADGROUP,               │
│     consumer groups por agente — elimina polling               │
│     (reemplaza lectura periódica de state.json)                │
│ ×2  ASYNC nativo en todos los workers (Taskiq-style)           │
│ ×2  MULTI-POOL real por concern con auto-scale por             │
│     profundidad de cola (ya diseñado — implementar)            │
│ ×2  TIME-WHEEL scheduler 1ms (reemplaza sleep+check):          │
│     p99 de 5-10s → <100ms                                      │
│ ×1.5 SHARDED ROOTS: N orquestadores-shard por proyecto/        │
│     tipo (el Kernel ya es determinista → shardearlo es         │
│     trivial, el estado vive en Postgres no en el proceso)      │
│ ×1.5 PRE-WARMING predictivo: si profundidad de cola sube       │
│     X% en Y seg → spawn workers ANTES del pico                 │
│                                                                │
│ 4×3×2×2×2×1.5×1.5 ≈ 216x techo teórico → 100x alcanzable       │
│                                                                │
│ + 2 multiplicadores CUALITATIVOS (no de velocidad):            │
│ ∞ EVIDENCIA_VIVA (SIM A): el sistema deja de certificar        │
│   contra el pasado                                             │
│ ∞ TIMEOUT/RECURSOS ADAPTATIVOS por ficha (SIM B): el sistema   │
│   se calibra solo con sus propios datos                        │
└────────────────────────────────────────────────────────────────┘

ROADMAP DEL PARCHE (post-MVP, no bloquea la construcción):
  Semana 1-2: Redis Streams + batching total          → 10x
  Semana 3-4: multi-pool + time-wheel                 → 40x
  Semana 5-6: sharded roots + pre-warming + async     → 100x
  REGLA: cada multiplicador entra como FICHA-MEJORA por el
  ciclo de auto-mejora (consenso → Juez → Witness) — el parche
  100x usa el propio sistema para instalarse.
```

**Gaps nuevos de este parche**: GAP-PARCHE-001 (ciclo auto-mejora completo), GAP-PARCHE-002 (Output Gateway), GAP-PARCHE-003 (EVIDENCIA_VIVA + SH08), GAP-PARCHE-004 (timeout adaptativo por ficha), GAP-PARCHE-005 (categoría DESTRUCTIVA_IRREVERSIBLE en CAPA 9), GAP-PARCHE-006 (los 7 multiplicadores como fichas de mejora).

**Diseño completo. Espera tu aprobación para: (a) cerrar el prototipo con este parche incluido, y (b) arrancar la Fase A de la estrategia Sonnet.**
