# 🌳 ÁRBOL HORIZONTAL TRANSVERSAL — MAXBRY

> Un árbol de navidad acostado. La raíz es la constitución. Las ramas son los componentes del G2 v2.5. Los frutos son los documentos. Las raíces secundarias son los pendientes.

---

## DIAGRAMA (texto expandible)

```
═══════════════════════════════════════════════════════════════════════════════════════════════════════════
RAÍZ (CONSTITUCIÓN)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

PERFIL_maxbry_v1                      G2_v2.5_FINAL_AUDITADO (246 ítems)
   │                                          │
   │ LEY INMUTABLE                            │ HASH: G2_PECP_v2.5_FINAL_AUDITADO
   │                                          │
═══════════════════════════════════════════════════════════════════════════════════════════════════════════
TRONCO 1 — REGLAS DE HIERRO (Nivel 1, inamovibles)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

PATCH-001 agentes B                    PATCH-001 locales                    PROTOCOLO_FICHAS
   │                                       │                                    │
   │ runtime_type=agent                    │ Agents locales en dispositivo      │ 3 archivos .py + .meta.md +
   │ max_steps + allowed_actions           │ del usuario                         │ artifact_location_plan.json
   │ + environment                         │                                     │
   │ + requires_approval                   │                                     │
   └───────────────────────────────────────┴────────────────────────────────────┘
                                                                                    │
                                                                                    │ ENCHUFE/CONEXIÓN
                                                                                    │ (lenguaje cerebro ↔ ficha)
                                                                                    ▼

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
TRONCO 2 — MOTOR / CEREBRO G2 v2.5 (las 5 piezas + capas)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

                        ┌─────────────────────────────────────┐
                        │   G2 CEREBRO (5 piezas)              │
                        │                                     │
                        │   1. Router dispatcher               │
                        │   2. Índice Maestro                 │
                        │   3. Motor DAG                      │
                        │   4. Recovery Core (5 tiers)         │
                        │   5. Loader+Verifier+Executor       │
                        │                                     │
                        │   + 4 capas internas:               │
                        │   - KERNEL                          │
                        │   - RUNTIME                         │
                        │   - VERIFICATION                    │
                        │   - STATE                           │
                        └─────────────┬───────────────────────┘
                                      │
        ┌─────────────────┬───────────┴──────────┬─────────────────┐
        │                 │                      │                 │
        ▼                 ▼                      ▼                 ▼
   secuencia DAG    state.json (Crazy   FAISS en BRAIN    Execution Layer
   (sequence.json  Wall) escritura       (task_memory)     (local + HF + remote)
   + fallback.json  atómica                               │
        │                                                  ▼
        │                                              Verifier N0→N5
        │                                              + Slot Contract
        │                                              SC1-SC6
        │
        ▼
   Execution Layer 3 runners
   - LOCAL (importlib+asyncio)
   - HF (httpx+Bearer)
   - REMOTE (futuro)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
TRONCO 3 — UNIDAD DE TRABAJO (las fichas)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

                              ┌──────────────────────┐
                              │      FICHA           │
                              │  1 función ejecutar()│
                              │  1 .meta.md          │
                              │  1 .location_plan    │
                              └─────────┬────────────┘
                                        │
            ┌───────────────────────────┼───────────────────────────┐
            │                           │                           │
            ▼                           ▼                           ▼
   compute (80%)                  hybrid (15%)                  llm (5%)
   runtime_type=compute            runtime_type=hybrid           runtime_type=llm
   Sin LLM                        código 90% + LLM 10%          LLM como herramienta
            │                           │                           │
            └───────────────────────────┴───────────────────────────┘
                                        │
                            runtime_type=agent (PATCH-001)
                            Categoría B (lista cerrada, ADR necesario)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
TRONCO 4 — ESTADO Y MEMORIA
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

                  ┌──────────────────────────────────────────┐
                  │     ESTADO PERSISTIDO                    │
                  │                                          │
                  │  CrazyWall[task_id][ficha_id]            │
                  │    ↓ atomic write (mkstemp+fsync+replace)│
                  │    WAL (append-only)                     │
                  │    ↓ checkpoint cada 1000 OR 60s        │
                  │    checkpoints.json                      │
                  │                                          │
                  │  + shared_knowledge (COMMITTED only)    │
                  │  + task_memory (privada)                │
                  │  + FAISS en BRAIN (búsqueda semántica) │
                  │  + KG SQLite (knowledge graph)          │
                  └──────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
RAÍCES SECUNDARIAS — MÉTODO DE TRABAJO (Nivel 3)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES_KIMI_K_v4.1          CONSOLIDADO_150_INSTRUCCIONES         KIMI_PARTE_1..8
   │                                       │                                    │
   │ Método del constructor                │ Compilado de 150 instrucciones     │ Parches específicos
   │ (24 secciones)                        │                                    │ (formatos, registros,
   │                                       │                                    │  motor, modos, verificación,
   └───────────────────────────────────────┴────────────────────────────────────┘    ZIP, checklist)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
FRUTOS — DOCUMENTOS DE EXTRACCIÓN (Nivel 4)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

              DOC_EXTRACCION_1              DOC_EXTRACCION_2              DOC_EXTRACCION_3
                       │                          │                            │
                       └──────────────────────────┴────────────────────────────┘
                                              │
                                              ▼
                                 Cosas extraídas con anti-alucinación.
                                 Cada DOC cita fuente o [NO_ENCONTRADO].

   IMPLEMENTAR_SISTEMA         GUIAS (Claude Code, AI recuerda, AI más inteligente)
                                       │
                                       ▼
                            Cómo construir el sistema.
                            (no qué construir — eso es G2 + tu diseño)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
RAMAS PENDIENTES (Nivel 6 — vacías hasta resolver)
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

D01 Orquestación >50 Spaces
D02 Cuántos Spaces por rol
D03 Conexión API entre Spaces
D04 Costo infraestructura
D05 Failover regiones HF
  │
  └─ Estas 5 ramas están VACÍAS hasta que se cierren los 10 roles.

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
ESTADO FINAL
═══════════════════════════════════════════════════════════════════════════════════════════════════════════

  ✅ CERRADO EN G2 v2.5:
     - 5 piezas del cerebro
     - DAG / FSM
     - 1 ficha = 1 función
     - Verifier N0-N5
     - Slot Contract SC1-SC6
     - FAISS en BRAIN
     - shared_knowledge binario
     - 13 reglas absolutas
     - Runtime types (compute/hybrid/llm/agent)
     - 3 archivos por ficha
     - 28 lenguajes de cumplimiento (referencia)

  ⏳ ABIERTO (decisión del Director):
     - C1-C8: 8 contradicciones entre documentos
     - D01-D05: 5 pendientes estructurales
     - Migración v3.1/v7.1 → G2 v2.5 (¿se hace, sí o no?)

  ❌ RECHAZADO DEFINITIVO (15 ítems de v3.1):
     LoRA, Thinking traces, gRPC/ZeroMQ, Comandos imperativos,
     Autonomía objetivos, Multi-agente votación, Optimización no-crítica,
     Sleep, Traducción NL↔Tensor, Autonomía Nivel 2, Optimización velocidad,
     Autooptimización, Optimizador multiagente, Optimizar método,
     Optimización extrema.

═══════════════════════════════════════════════════════════════════════════════════════════════════════════
```

---

## LECTURA DEL ÁRBOL

| Si quieres saber... | Mirar... |
|---|---|
| ¿Cuál es la ley suprema? | Raíz → PERFIL + G2 v2.5 |
| ¿Qué puede tocar qué? | Tronco 1 (PATCH + PROTOCOLO) |
| ¿Cómo opera el cerebro? | Tronco 2 (las 5 piezas) |
| ¿Qué es una ficha exactamente? | Tronco 3 (la unidad) |
| ¿Cómo se persiste el estado? | Tronco 4 (estado y memoria) |
| ¿Cómo trabaja el constructor? | Raíces secundarias (KIMI método) |
| ¿Qué falta resolver? | Ramas pendientes + estado final |
