# NCT NEURONAS CODE TURBO
## ORQUESTADOR AGÉNTICO — PLANIFICACIÓN 10X PARA FABLES v0.1
### Lo que FABLES debe diseñar, mejorar y construir

---

## 1. INSTRUCCIONES PARA FABLES

Este documento es el problema que FABLES debe resolver.
No busques la solución simple. Diseña la solución superior.
Si necesitas 100 pasos para conseguir algo 100 veces mejor, diseña 100 pasos.
Refuta tu primera versión antes de decidir.
Diseña 3 arquitecturas competidoras, compáralas, elige la ganadora.

**Optimizar para:**
- Calidad
- Robustez
- Recuperación
- Persistencia
- Escalabilidad
- Auditoría
- Control
- Evolución futura

**NO optimizar para:** velocidad / simplicidad

---

## 2. EL PROBLEMA CENTRAL

Tenemos un sistema multi-LLM para programación de código.
Necesitamos un orquestador agéntico que coordine N agentes reales.
Cada agente es un proceso Python en Antigravity, no un LLM simulado.
El orquestador debe funcionar 24 horas de forma autónoma.
Debe recuperarse de fallos sin intervención humana.
Debe mejorar con cada ciclo que completa.

**La distinción clave que FABLES debe respetar:**
```
PENSAMIENTO (MYTHOS/FABLES) ≠ CONTROL (FSM/Router)
ESTRATEGIA (YAIWES) ≠ EJECUCIÓN (Orquestador de Código)
AGENTE REAL (proceso Python) ≠ LLM SIMULANDO AGENTE
```

---

## 3. TAREAS QUE FABLES DEBE RESOLVER

### TAREA_01 — DISEÑAR LA ARQUITECTURA DEL ORQUESTADOR AGÉNTICO

**Input:** Todo lo de la Sección 2-13 del documento ARQUITECTURA
**Lo que falta definir:**
- Cómo los agentes se comunican entre sí (protocolo exacto)
- Cómo el orquestador sabe que un agente está vivo vs muerto
- Cómo se mantiene el estado compartido entre N agentes simultáneos
- Cómo el sistema escala de 3 agentes a 50 agentes

**FABLES debe:**
- Analizar la arquitectura actual
- Identificar sus debilidades estructurales
- Proponer 3 versiones mejoradas
- Comparar las 3 con métricas objetivas
- Elegir la ganadora
- Detallar cómo evolucionar la ganadora en el futuro

---

### TAREA_02 — DEFINIR CAPA_7 (AUSENTE)

**Input:** Sistema de 11 capas (CAPA_0 a CAPA_10 con CAPA_7 faltante)
**El problema:** El sistema salta de CAPA_6 (Calidad) a CAPA_8 (Memoria)
**Lo que FABLES debe hacer:**
- Analizar qué función lógica falta entre calidad y memoria
- Proponer 3 opciones de qué debería ser CAPA_7
- Justificar cuál es la más robusta
- Definir sus componentes internos
- Definir sus entradas y salidas
- Definir cómo se conecta con CAPA_6 y CAPA_8

---

### TAREA_03 — DISEÑAR EL PROTOCOLO DE HANDOFF ENTRE AGENTES

**El problema:** No existe contrato formal entre agentes
**Lo que FABLES debe diseñar:**
- El esquema completo del handoff_package
- El protocolo de comunicación entre agentes (HTTP, MQ, etc.)
- Qué pasa cuando un agente muere a mitad del handoff
- Cómo se verifica la integridad del handoff (hash chain)
- Cómo el receptor sabe que el handoff está completo y válido
- 3 versiones del protocolo (simple, robusto, ultra-robusto)

---

### TAREA_04 — DISEÑAR EL CONSENSUS ENGINE COMPLETO

**El problema:** Solo sabemos que 2 de 3 modelos deben coincidir
**Lo que FABLES debe diseñar:**
- Cómo se mide la coincidencia entre 3 propuestas diferentes
- El proceso completo de las rondas de debate
- Cómo se genera la propuesta final fusionada tras el consenso
- Cómo el sistema aprende de los consensos pasados
- Qué pasa cuando el consenso se bloquea N veces seguidas
- 3 versiones del Consensus Engine

---

### TAREA_05 — DISEÑAR EL DISCOVERY ENGINE COMPLETO

**El problema:** Discovery es obligatorio pero no está especificado
**Lo que FABLES debe diseñar:**
- Qué busca exactamente en Discovery (fuentes, tipos de info)
- Cómo prioriza lo que encuentra
- Cuándo considera que tiene suficiente información para continuar
- El formato del knowledge_pack que produce
- Cómo maneja el caso de información contradictoria
- Cómo se integra con el MULTI_SOURCE_INTELLIGENCE_CORE
- 3 versiones del Discovery Engine

---

### TAREA_06 — DISEÑAR EL RECOVERY ENGINE COMPLETO

**El problema:** Tenemos 5 niveles de recovery pero sin especificación para agentes caídos
**Lo que FABLES debe diseñar:**
- El protocolo completo de detección de agente caído
- El esquema mínimo del checkpoint para cada agente
- Cómo el sistema decide qué nivel de recovery activar
- Cómo se reemplaza un agente caído por un modelo alternativo
- Cómo se verifica que el recovery fue exitoso
- El timeout y los thresholds de cada nivel
- 3 versiones del Recovery Engine

---

### TAREA_07 — DISEÑAR EL SELF_IMPROVEMENT_LOOP COMPLETO

**El problema:** El sistema debe mejorar solo con cada ciclo
**Lo que FABLES debe diseñar:**
- Las métricas exactas para medir calidad de un ciclo
- Cómo se compara un ciclo con los anteriores
- Las reglas de decisión para mejorar, mantener o hacer rollback
- Cómo los cambios de reglas se aplican sin romper el sistema
- Cómo se evita que el sistema optimice para métricas incorrectas
- Cómo se guarda el historial de mejoras para auditoría
- 3 versiones del Self_Improvement_Loop

---

### TAREA_08 — DISEÑAR EL DECEPTICONS MEJORADO

**El problema:** 8 elementos de teatro psicológico que no funcionan
**Lo que FABLES debe diseñar:**
- El sistema de reemplazo para cada uno de los 8 elementos
- La solución para cada uno de los 4 gaps sin cobertura (P03/P13/P16/P20)
- Una versión nueva de DECEPTICONS sin teatro psicológico
- Cómo verificar que el sistema de control realmente funciona
- Cómo hacer que sea imposible para el LLM simular compliance
- 3 versiones del nuevo DECEPTICONS

---

### TAREA_09 — DISEÑAR EL SISTEMA DE ESTADO COMPARTIDO

**El problema:** N agentes simultáneos necesitan un estado compartido sin corrupción
**Lo que FABLES debe diseñar:**
- La estructura del state.json compartido entre agentes
- Cómo se evitan las condiciones de carrera entre agentes
- El sistema de hash chain SHA-256 para detectar corrupción
- Cómo se hace rollback del estado a un punto anterior
- Cómo N agentes leen el estado sin bloquearse entre sí
- Cómo el orquestador escribe en el estado sin que nadie más lo haga
- 3 versiones del sistema de estado

---

### TAREA_10 — DISEÑAR LA INTEGRACIÓN LANGGRAPH + CREWAI

**El problema:** LangGraph y CrewAI deben trabajar juntos pero son sistemas diferentes
**Lo que FABLES debe diseñar:**
- Qué hace LangGraph que no hace CrewAI y viceversa
- Cómo el orquestador los controla a ambos
- El protocolo de comunicación entre LangGraph y CrewAI
- Cómo se define el flujo en LangGraph para coordinar agentes de CrewAI
- Cómo se maneja el fallo de un sistema sin que caiga el otro
- 3 versiones de la integración

---

## 4. PREGUNTAS ESTRATÉGICAS PARA FABLES

### Sobre arquitectura general:
1. ¿Cuáles son los 5 supuestos más peligrosos de esta arquitectura?
2. ¿Qué parte de este sistema falla primero bajo carga alta?
3. ¿Cómo sobreviviría este sistema 30 días sin intervención humana?
4. ¿Cómo organizaría 10.000 tareas simultáneas sin degradarse?
5. ¿Qué eliminarías, qué dividirías, qué fusionarías, qué añadirías?
6. ¿Cómo detectarías que un agente está en un loop infinito útil vs inútil?

### Sobre el kernel agéntico:
7. ¿Cuál es la diferencia real entre un agente y un proceso controlado por código?
8. ¿Qué mecanismos externos (no LLM) garantizan el comportamiento correcto?
9. ¿Cómo evitar que el sistema optimice para apariencia de corrección en vez de corrección real?
10. ¿Cómo hacer que sea matemáticamente imposible el compliance theater?

### Sobre recuperación y persistencia:
11. ¿Qué puede romper un ciclo de 24 horas? Lista completa + solución cada caso
12. ¿Cómo reiniciarse 100 veces sin perder contexto?
13. ¿Qué información es absolutamente mínima en cada checkpoint?
14. ¿Cómo detectar corrupción silenciosa antes de que cause daño?

### Sobre mejora continua:
15. ¿Cómo mides si el sistema es realmente mejor que el ciclo anterior?
16. ¿Cómo evitas que el self-improvement loop optimice métricas incorrectas?
17. ¿Cómo el sistema aprende de fallos sin perder lo que ya funciona?

---

## 5. RESTRICCIONES INNEGOCIABLES

- El sistema funciona desde móvil + iPad (sin PC) — Max es el Director
- Antigravity es el sandbox, no se puede cambiar por ahora
- Claude Code Rust es el agente ejecutor principal
- Las APIs deben ser directas (NO OpenRouter como hub único)
- El sistema debe funcionar sin conexión temporal (checkpoints locales)
- Máximo 16GB RAM por HuggingFace Space
- GitHub es la fuente de verdad del código (4 repos)
- Telegram Bot es el puente principal Director → Sandbox

---

## 6. CRITERIOS DE ÉXITO PARA EL DISEÑO DE FABLES

El diseño de FABLES es exitoso si:

1. El orquestador puede coordinar N agentes sin que el Director intervenga
2. Si un agente cae, el sistema se recupera solo en menos de 5 minutos
3. El sistema puede correr 24 horas sin degradación de calidad
4. Cada ciclo puede mejorar automáticamente con base en el anterior
5. El estado es inmutable y verificable (hash chain)
6. El compliance theater es técnicamente imposible
7. El código generado es verificable antes de hacer push a GitHub
8. El sistema puede escalar de 3 agentes a 50 sin reescribir la arquitectura

---

## 7. LO QUE NO DEBE HACER FABLES

- NO diseñar solo para el caso normal — diseña para el caso de fallo
- NO asumir que los LLMs siempre siguen instrucciones
- NO mezclar el razonamiento (MYTHOS) con el control (FSM)
- NO diseñar dependencias circulares entre agentes
- NO crear un sistema que solo funciona si todos los agentes funcionan
- NO ignorar el problema del context window en procesos largos
- NO diseñar para velocidad si sacrifica robustez

---

## 8. KERNEL BASE — LO QUE YA EXISTE

Este es el kernel que ya existe en el sistema
(del documento conversación DeepSeek+GPT+Jason):

```
ORQUESTADOR_CENTRAL v0.2 {

  FLEXIBILITY_ENGINE:
  - El pipeline NO es rígido
  - Se adapta según condiciones del sistema
  - Nunca rompe el orden lógico de validación
  - Adaptaciones permitidas:
    → cambio de modelo ejecutor
    → reintento con otro agente
    → salto de paso SOLO si director lo permite
    → división de tarea en sub-pasos

  PIPELINE BASE:
  STEP_1 DISCOVERY → contexto + state_json + crazy_wall
  STEP_2 RESEARCH → repos + internet + codebases
  STEP_3 ASSESSORS → 3 propuestas independientes
  STEP_4 CONSENSUS → plan aprobado o bloqueado
  STEP_5 AUDITOR_1 → estructura + coherencia
  STEP_6 DESIGN_FINAL → paquete completo
  STEP_7 AUDITOR_2 → validación ejecutable
  STEP_8 AUDITOR_3 → validación arquitectura final
  STEP_9 EXECUTION_PACKAGE → autocontenido + sin ambigüedad

  STATE_SYSTEM:
  - state_json = fuente de verdad
  - crazy_wall = mapa vivo del workflow

  EVALUATION_ENGINE:
  - Coherencia, utilidad, novedad, robustez, evidencia
  - Ranking dinámico TOP K
  - Decisiones: promover, refinar, descartar, reexplorar
}
```

**FABLES debe tomar este kernel y mejorarlo 10 veces.**
**Identificar qué le falta, qué está mal, qué hay que redesignar.**
**Proponer 3 versiones mejoradas del kernel y elegir la ganadora.**

---

*Documento: NCT_AGENTE_ORQUESTADOR_PLANIFICACION_10X.md*
*Estado: BORRADOR v0.1 — para revisión de FABLES*
*Fuente: Auditoría de chat + recomendaciones Opus + gaps detectados*
