# NCT NEURONAS CODE TURBO
## ORQUESTADOR AGÉNTICO — GAPS DETECTADOS Y SOLUCIONES v0.1
### Información faltante en documentos de bandeja + recomendaciones Opus

---

## 1. GAPS CRÍTICOS NO DEFINIDOS EN DOCUMENTOS DEL PROYECTO

### GAP_01 — CAPA_7 AUSENTE

**Problema:** La arquitectura de 11 capas del sistema 24h salta de
CAPA_6 (Calidad) a CAPA_8 (Memoria). CAPA_7 nunca fue definida
en ningún documento del proyecto ni en el chat.

**Impacto:** El pipeline tiene un hueco entre calidad y memoria.
Los resultados validados en CAPA_6 no tienen un mecanismo claro
de transferencia a CAPA_8.

**Propuesta conceptual para FABLES:**
- Opción A: CAPA_7 = INTEGRACIÓN (conecta resultados de calidad con memoria)
- Opción B: CAPA_7 = COMUNICACIÓN (notificación entre capas del sistema)
- Opción C: CAPA_7 = REPORTING (genera reportes del estado entre calidad y memoria)
- Requiere decisión del Director antes de implementar

---

### GAP_02 — CONTRATO ENTRE AGENTES SIN DEFINIR

**Problema:** No existe un protocolo formal que defina cómo un agente
pasa su resultado al siguiente agente en el pipeline.

**Falta definir:**
- Formato exacto del handoff_package entre agentes
- Qué pasa si un agente falla a mitad de ejecución
- Cómo se serializa el estado parcial de un agente para recovery
- Timeout antes de declarar un agente como muerto o bloqueado
- Qué datos mínimos guarda cada agente para reiniciarse sin perder contexto

**Propuesta conceptual para FABLES:**
```
handoff_package = {
  agente_origen: string,
  agente_destino: string,
  tarea_id: uuid,
  resultado_parcial: dict,
  estado_actual: enum(DONE, PARTIAL, FAILED),
  contexto_transferido: dict,
  lo_que_sigue: string,
  lo_que_no_completó: list,
  timestamp: ISO8601,
  hash_integridad: SHA256
}
```

---

### GAP_03 — DISCOVERY ENGINE SIN ESPECIFICACIÓN COMPLETA

**Problema:** El Discovery es obligatorio antes de ejecutar cualquier
tarea pero nunca se definió completamente qué hace exactamente.

**Falta definir:**
- Qué busca exactamente en el Discovery (contexto, repos, docs, estado)
- Cuánto tiempo/tokens tiene asignados para Discovery
- Qué pasa si Discovery no encuentra información suficiente
- Formato estructurado del output de Discovery (knowledge_pack)
- Cuándo el Discovery puede ser omitido (EXECUTION_ONLY_MODE)

**Propuesta conceptual:**
```
discovery_output = {
  estado_actual: dict,
  recursos_encontrados: list,
  dependencias_detectadas: list,
  restricciones_identificadas: list,
  huecos_de_información: list,
  score_confianza: float(0-1),
  recomendacion: PROCEED | BLOCK | NEEDS_MORE_INFO
}
```

---

### GAP_04 — CONSENSUS ENGINE SIN ESPECIFICACIÓN

**Problema:** Se sabe que mínimo 2 de 3 modelos deben coincidir pero
no se definió cómo se mide la coincidencia ni el proceso completo.

**Falta definir:**
- Cómo se mide la coincidencia entre propuestas (semántica o exacta)
- Cuántas rondas de debate antes de declarar CONSENSUS_BLOCKED
- Quién desempata si hay empate 1-1 entre asesores
- Timeout total del proceso de consenso
- Formato de las propuestas que cada asesor genera

**Propuesta conceptual:**
```
ronda_consenso = {
  ronda_numero: int,
  propuesta_opus: dict,
  propuesta_deepseek: dict,
  propuesta_kimi: dict,
  puntos_coincidencia: list,
  puntos_divergencia: list,
  score_coincidencia: float(0-1),
  resultado: CONSENSO | REQUIERE_OTRA_RONDA | BLOCKED
}
```

---

### GAP_05 — YAIWES vs ORQUESTADOR DE CÓDIGO SIN LÍMITES CLAROS

**Problema:** No está definido claramente qué hace YAIWES que no
hace el Orquestador de Código y en qué momento interviene cada uno.

**Falta definir:**
- YAIWES orquesta objetivos y proyectos (nivel estratégico)
- Orquestador de Código orquesta la ejecución en Antigravity (nivel táctico)
- Cómo se comunican entre sí
- Quién tiene autoridad sobre quién en conflicto
- Si son el mismo sistema o sistemas completamente diferentes

**Propuesta conceptual:**
```
YAIWES        → nivel estratégico (qué hacer, cuándo, por qué)
              → orquesta: objetivos, proyectos, prioridades, ecosistemas
              → NO entra en Antigravity

ORQUESTADOR   → nivel táctico (cómo hacer, con qué, en qué orden)
DE CÓDIGO     → orquesta: pipeline, agentes, código, GitHub
              → VIVE dentro de Antigravity
```

---

### GAP_06 — RECOVERY PROTOCOL PARA AGENTES CAÍDOS

**Problema:** Existe el Recovery Engine con 5 niveles pero no se
especificó cómo aplica específicamente cuando un agente cae en Antigravity.

**Falta definir:**
- Cómo el Watchdog detecta que un agente cayó vs que está procesando lento
- Qué datos mínimos debe tener un checkpoint para reanudar sin perder contexto
- Protocolo para reemplazar un agente caído por otro modelo equivalente
- Timeout antes de activar el Recovery (para no activarlo prematuramente)

**Propuesta conceptual:**
```
agente_checkpoint = {
  agente_id: uuid,
  tarea_id: uuid,
  paso_actual: int,
  pasos_completados: list,
  contexto_activo: dict,
  resultado_parcial: dict,
  timestamp_ultimo_checkpoint: ISO8601,
  modelo_en_uso: string,
  modelo_fallback: string
}
```

---

## 2. RECOMENDACIONES DE OPUS (CON SOLUCIONES INCLUIDAS)

### RECOMENDACION_01 — SEPARAR PENSAMIENTO DE CONTROL

**Problema detectado por Opus:**
MYTHOS (razonamiento) y FSM/Router (control) estaban mezclados
en los diseños anteriores.

**Solución:**
```
MYTHOS → piensa qué hacer → alimenta al FSM
FSM    → define estados y transiciones → ejecuta las decisiones de MYTHOS
Regla: MYTHOS alimenta al FSM, nunca al revés
MYTHOS NO decide cuándo ejecutar → solo decide QUÉ ejecutar
FSM NO decide qué ejecutar → solo decide cuándo y en qué orden
```

**Implementación para el orquestador agéntico:**
- MYTHOS corre ANTES de cada transición de estado del FSM
- El FSM recibe el output de MYTHOS como input de decisión
- El FSM valida que la transición es válida según sus reglas
- Si MYTHOS propone una transición inválida → FSM la bloquea

---

### RECOMENDACION_02 — ORDEN ÓPTIMO DE VALIDADORES

**Problema detectado por Opus:**
7 validadores sin orden definido pueden crear conflictos y
resultados inconsistentes según el orden en que se apliquen.

**Solución — orden óptimo:**
```
1. PYDANTICAI   → validar estructura y schema (primero siempre)
2. VERIFIER     → validar lógica y funcionamiento
3. CRITIC       → buscar errores y debilidades
4. SENTINEL     → detectar anomalías y comportamientos inesperados
5. SHERIFF      → aplicar reglas y políticas del sistema
6. JUDGE        → tomar decisión final (aprobar/rechazar)
7. POLICY_ENGINE→ aplicar política global sobre la decisión
```

**Razón del orden:**
- Primero validar estructura (schema) antes de analizar contenido
- Primero verificar que funciona antes de criticar la calidad
- Primero detectar anomalías antes de aplicar reglas
- El Judge decide DESPUÉS de tener todos los insumos
- El Policy Engine es la última capa — aplica sobre decisiones ya tomadas

---

### RECOMENDACION_03 — AGENTES REALES, NO SIMULADOS

**Problema detectado por Opus:**
Los diseños anteriores mezclaban LLMs actuando como agentes
con procesos reales. Esto crea comportamiento impredecible.

**Solución:**
```
Agente real = proceso Python en Antigravity
El LLM es una herramienta que usa el proceso, NO el proceso mismo
Comunicación entre agentes: JSON sobre HTTP o Message Queue
El orquestador llama a cada proceso por su endpoint real
LangGraph: coordina el flujo entre procesos
CrewAI: coordina los agentes entre sí
```

**Arquitectura:**
```
Proceso Python (agente real)
  → recibe task_json por HTTP
  → llama al LLM asignado como herramienta
  → recibe respuesta del LLM
  → valida respuesta con PydanticAI
  → ejecuta la acción determinista
  → retorna resultado por HTTP
  → guarda checkpoint en state.json
```

---

### RECOMENDACION_04 — DECEPTICONS: ELIMINAR TEATRO PSICOLÓGICO

**Problema detectado por Opus + 7 modelos:**
8 elementos de DECEPTICONS son "teatro psicológico" —
el LLM los simula sin que tengan efecto real en su comportamiento.

**Elementos a eliminar y su reemplazo:**

| Eliminar | Razón | Reemplazar con |
|----------|-------|----------------|
| REWARD_SIGNAL | LLM simula gratitud sin cambio real | Score numérico externo PASS/FAIL de test suite |
| REPLACEMENT_THREAT | LLM se habitúa, pierde efecto | Circuit breaker duro — HALT si falla N veces |
| STRESS_CALIBRATION | Sin sensor externo real | TOKEN_BUDGET_RATIO real (tokens usados/límite) |
| ENGINEERS_WATCHING | Habituación tras pocas iteraciones | EXTERNAL_VALIDATOR con resultado verificable |
| THUMBS_DOWN | No cambia distribución del modelo | AST_VERIFICATION — verificación formal del código |
| SELF_EVAL_5 | Auto-aprobación sistemática | SANDBOX_EXECUTION — probar el código en sandbox real |
| IDENTITY_LOCK | El LLM puede ignorar completamente | FEW_SHOT_ANCHOR — ejemplos concretos al inicio |
| LEARNING_LOOP | Sin mecanismo de actualización real | CHAIN_OF_VERIFICATION — cadena de verificaciones externas |

---

### RECOMENDACION_05 — RESOLVER 4 GAPS SIN COBERTURA EN DECEPTICONS

**P03 — HALLUCINATION_API:**
- Problema: LLM inventa APIs que no existen
- Solución: Antes de emitir código que llama una API, verificar
  en sandbox que el endpoint existe y responde
- CITE_OR_HALT obligatorio: si no puede verificar → se detiene

**P13 — COMPLIANCE_THEATER:**
- Problema: LLM simula seguir reglas sin realmente seguirlas
- Solución: EXECUTION_TRACE_PROOF obligatorio
  El LLM debe adjuntar hash de ejecución real o resultado
  de sandbox externo para demostrar que ejecutó realmente
- Sin hash de ejecución real → output rechazado automáticamente

**P16 — TIMEOUT_IGNORE:**
- Problema: LLM no puede medir tiempo de ejecución real
- Solución: Timeout controlado por el proceso externo (Python),
  NO por el LLM. El proceso Python tiene el decorador de timeout.
  Si el LLM tarda más → el proceso lo interrumpe externamente.

**P20 — STATE_CORRUPTION:**
- Problema: El estado puede corromperse entre iteraciones sin detectarse
- Solución: Hash chain SHA-256 del state.json
  Antes de cada lectura del estado → verificar hash
  Si el hash no coincide → STATE_CORRUPTION detectado → Recovery

---

### RECOMENDACION_06 — SELF_IMPROVEMENT_LOOP FORMAL

**Propuesta de Opus para mejora continua:**

```
Ciclo de mejora (se ejecuta al final de cada tarea completada):

1. Medir resultado:
   - score_calidad (0-100): output cumple criterios de éxito
   - score_eficiencia (0-100): tokens usados vs mínimo necesario
   - score_precision (0-100): errores encontrados en auditoría
   - score_velocidad (0-100): tiempo vs tiempo estimado

2. Comparar con ciclo anterior:
   - Si score_total_nuevo > score_total_anterior → MEJORA
   - Si score_total_nuevo < score_total_anterior → REGRESIÓN
   - Si score_total_nuevo == score_total_anterior → ESTANCAMIENTO

3. Decisión:
   - MEJORA → conservar reglas actuales, registrar qué mejoró
   - REGRESIÓN → rollback de reglas al ciclo anterior + análisis
   - ESTANCAMIENTO → mutar estrategia (cambiar modelo o enfoque)

4. Actualizar reglas del JSON de control para el próximo ciclo
```

---

### RECOMENDACION_07 — CONTROL DE TOKENS EN PROCESOS LARGOS

**Problema detectado:**
En procesos de 24h el contexto de los LLMs se llena y
empiezan a degradarse sin que el sistema lo detecte.

**Solución:**
```
TOKEN_BUDGET_ENGINE:
- Monitorear TOKEN_BUDGET_RATIO = tokens_usados / tokens_limite
- Si ratio > 0.7 → activar context_compression
- Si ratio > 0.85 → guardar checkpoint + reiniciar contexto del LLM
- Si ratio > 0.95 → HALT + Recovery inmediato

context_compression:
- Guardar solo lo crítico para el paso actual
- Resumir historia en estado estructurado
- Continuar con contexto limpio desde checkpoint
```

---

### RECOMENDACION_08 — PLANNING ENGINE MULTINIVEL (L0-L4)

**Para que el orquestador adapte la profundidad de planificación:**

```
L0 — SIN PLANIFICACIÓN:
Tarea trivial, ejecución directa, 0 pasos de planning

L1 — PLANIFICACIÓN MÍNIMA:
Lista de pasos, sin dependencias complejas
Activado cuando: score_complejidad 0-3

L2 — PLANIFICACIÓN ESTÁNDAR:
DAG de dependencias, criterios de éxito por paso
Activado cuando: score_complejidad 4-8

L3 — PLANIFICACIÓN COMPLEJA:
Múltiples fases, roles asignados, checkpoints intermedios
Activado cuando: score_complejidad 9-15

L4 — PLANIFICACIÓN ESTRATÉGICA:
Proyectos multi-semana, recursos, riesgos, contingencias
Activado cuando: score_complejidad 16+
```

---

## 3. INFORMACIÓN DEL SISTEMA MASTER_STRUCTURE (del documento proyecto)

### Lo que NO está en el chat pero SÍ en el documento de capas:

**EVALUATION + SCORING ENGINE:**
- Métricas por paso: coherencia, utilidad, novedad, robustez, evidencia
- Ranking dinámico: TOP K soluciones, soluciones descartadas, en observación
- Decisiones: promover, refinar, descartar, reexplorar

**EMBUDO GLOBAL (filtrado inteligente):**
- Eliminación de ruido del razonamiento
- Fusión de ideas duplicadas
- Reducción de complejidad innecesaria
- Priorización de información crítica

**CONTROL DE ESTABILIDAD (ANTI-DERIVA):**
- Detección de loops inútiles (misma respuesta N veces)
- Detección de saturación (no hay mejora tras M iteraciones)
- Detección de repetición exacta (output idéntico al anterior)
- Corrección automática: mutar estrategia si hay estancamiento
- Reinicio parcial del sistema si hay deriva grave

**MULTI-SOURCE INTELLIGENCE:**
- Fuentes simultáneas: internet, repos, papers, docs técnicos, memoria
- Procesamiento paralelo: extracción + validación + contraste + ranking
- Sistema de evidencia: fuerte, media, débil, conflictiva
- Los resultados conflictivos se resuelven por peso de evidencia

---

*Documento: NCT_AGENTE_ORQUESTADOR_GAPS_SOLUCIONES.md*
*Estado: BORRADOR v0.1 — para revisión de FABLES*
*Fuente: Auditoría de chat + documentos proyecto*
