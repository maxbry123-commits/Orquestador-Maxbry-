# PARCHE DE CIERRE — GRUPO H + GRUPO F
# Gaps detectados en auditoría, resueltos por Claude
# Fecha: 2026-07-05

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARCHE 1 — PIPELINE JUEZ: P09, P10, P13 (GRUPO F)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GAP REAL: el documento fuente NUNCA nombra P09, P10, P13
explícitamente. Solo aparecen como números en RO-07 (activación
por task_level) y en RES-11 ("presupuesto declarado en P09/P10").

RESUELTO (Claude decide, coherente con el resto del pipeline):

P09 — COMPLEXITY_BUDGET_DECLARE
  El ESCRITOR declara el presupuesto de complejidad:
  techo de líneas, techo de dependencias, techo de capabilities
  a usar en el código que va a construir.
  Ocurre DESPUÉS de P08 (tests) y ANTES de P-CODE.
  Se omite en simple (confirma RO-07).

P10 — COMPLEXITY_BUDGET_APPROVE
  El JUEZ audita el presupuesto declarado en P09 contra la
  Architectural Constitution. Si el presupuesto es excesivo
  para la tarea → RETRY con presupuesto ajustado.
  Se omite en simple (confirma RO-07, se agrupa con P03-P06).

P13 — SESSION_CLOSE
  Paso final tras P12 (sello/ADR). El JUEZ:
  - Verifica que BUILD_REGISTRY tiene la ficha COMMITTED
  - Genera pipeline_result final completo
  - Cierra Crazy Wall con snapshot final
  - Transición a JUEZ_STATE_COMPLETED
  Nunca se omite (ni en simple ni en critical) — es el cierre
  formal obligatorio de cualquier pipeline.

PIPELINE COMPLETO DEFINITIVO (14 pasos nombrados, sin huecos):
P-DISCOVER → P00(objetivo) → P01(clasificación) → P02(reality_check)
→ P03(roles) → P04(decisiones) → P05(simulaciones) → P06(crítica)
→ P07(contrato) → P08(tests) → P09(budget_declare)
→ P10(budget_approve) → P-CODE → P11(verificación/runtime)
→ P12(sello/ADR) → P13(session_close)

simple omite: P03,P04,P05,P06,P09,P10 (6 pasos)
critical: los 14 completos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARCHE 2 — MEJORAS 100X + PROPUESTAS NUEVAS (GRUPO H)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GAP: GRUPO H solo referenció que existen "20 mejoras 100x" y
"10 propuestas nuevas" sin detallarlas. Se cierran aquí.

10 PROPUESTAS NUEVAS (las más accionables para MVP):

P-NUEVA-01 Memoria Episódica del Razonamiento
  Guarda no solo el resultado sino el CAMINO completo de
  razonamiento de cada sesión, indexado y consultable.

P-NUEVA-02 Probador de Estrés Cognitivo
  Batería de problemas límite ejecutada antes de cada release
  para medir degradación del sistema bajo carga/ambigüedad.

P-NUEVA-03 Cómplices Cognitivos (expert duplication intencional)
  Duplicar deliberadamente un experto crítico con distinta
  configuración para detectar sesgo por comparación de outputs.

P-NUEVA-04 Tiempo de Reflexión Obligatorio
  Antes de C1 (construcción), pausa mínima donde B5 revisa
  una vez más el plan sin presión de avanzar.

P-NUEVA-05 Sistema de Castigos/Recompensas por Experto
  Ajuste de prioridad de selección de un experto según su
  historial de error_rate (no re-entrenamiento, solo prioridad).

P-NUEVA-06 Modo Socrático
  Ante ambigüedad irresoluble en Capa A, el sistema genera
  preguntas clarificadoras en vez de asumir.

P-NUEVA-07 Cómplices Externos (protocolo consulta humana)
  Punto de pausa formal donde el Juez Central puede escalar
  al Director antes de comprometer recursos grandes.

P-NUEVA-08 Pruebas Adversariales Automáticas
  Suite de inputs maliciosos/ambiguos ejecutada en CI antes
  de cada release del sistema.

P-NUEVA-09 Versionado del Razonamiento
  El sequence.json y los patrones de enjambre se versionan
  igual que el código — permite comparar cómo razonó v1 vs v2.

P-NUEVA-10 Meta-cognición (el sistema sabe cuánto sabe)
  confidence_final del OC se calibra contra el historial real
  de aciertos, no es solo un promedio de confidence individuales.

DECISIÓN DE INTEGRACIÓN AL MVP (Claude decide):
v0.1-v0.2: NINGUNA de estas 10 (kernel mínimo primero)
v1.0: P-NUEVA-01, 04, 06, 09 (bajo costo, alto valor)
v2.0: P-NUEVA-02, 03, 05, 08 (requieren banco de pruebas maduro)
v3.0: P-NUEVA-07, 10 (requieren historial de producción real)

MEJORAS 100X — LAS 5 MÁS CRÍTICAS PARA MVP (de las 20):
1. Objeto Cognitivo con invariantes (YA integrado, sección 2 GRUPO H)
2. Contrato fijo del experto (YA integrado, sección 3 GRUPO H)
3. Anti-echo-chamber por diseño (YA integrado, sección 3 GRUPO H)
4. Sequence.json inmutable (YA integrado, sección 7 GRUPO H)
5. Consenso ponderado por fórmula, no mayoría simple
   (YA integrado, sección 8 GRUPO H)
Las 15 restantes son optimizaciones de v1.5 en adelante,
no bloquean el MVP — se listan en el documento fuente original
que ya está en la bandeja del proyecto, no se duplican aquí.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARCHE 3 — VALIDACIÓN CRUZADA FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ GRUPO H: 300 expertos, 4 grupos, contrato experto, motor
   cognitivo, jueces 3 niveles, roadmap — CONFIRMADO completo
✅ GRUPO F: JUEZ+ESCRITOR+RUNTIME, pipeline 14 pasos ahora
   con TODOS nombrados — CONFIRMADO completo tras este parche
✅ Sin contradicciones entre GRUPO H y GRUPO F (Juez Central
   E296 = mismo JUEZ del GRUPO F, confirmado consistente)
✅ Sin contradicciones con Kernel NCT DOC1-4 (mapeos verificados)

NO HAY MÁS GAPS PENDIENTES en GRUPO H y GRUPO F.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT JSON — PARCHE CIERRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "PARCHE_CIERRE_H_F",
    "fecha": "2026-07-05",
    "fuente_de_verdad": true
  },
  "pipeline_juez_definitivo": {
    "total_pasos": 14,
    "nombrados_100pct": true,
    "nuevos_resueltos": ["P09_budget_declare","P10_budget_approve","P13_session_close"],
    "simple_omite": ["P03","P04","P05","P06","P09","P10"]
  },
  "propuestas_nuevas": {
    "total": 10,
    "v1.0": ["P-NUEVA-01","P-NUEVA-04","P-NUEVA-06","P-NUEVA-09"],
    "v2.0": ["P-NUEVA-02","P-NUEVA-03","P-NUEVA-05","P-NUEVA-08"],
    "v3.0": ["P-NUEVA-07","P-NUEVA-10"]
  },
  "gaps_pendientes": "NINGUNO",
  "grupo_h_estado": "CERRADO_VALIDADO",
  "grupo_f_estado": "CERRADO_VALIDADO"
}
