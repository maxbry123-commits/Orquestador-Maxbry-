# ORQUESTACIÓN — EXTRACCIÓN REAL DE LOS 57 DOCUMENTOS NCT (Parte 11)

=== ARCHIVO 21 (4510de5f 01-constitucion) ===
# DOCUMENTO 1: CONSTITUCIÓN DEL ORQUESTADOR
## Extraído del historial del chat (resumen compactado + salidas accesibles)

**Origen:** Información consolidada del resumen compactado al inicio del chat y de las salidas del asistente M3 que hablan sobre la Constitución del Orquestador.

---

## 1. NOMBRE DEL ORQUESTADOR

**MAXBRY SUPER TEAM** (nombre nuevo que reemplaza "Orquestador M3" / "G5").

Ubicación: G5 = ORQUESTADOR + CONSENSO (SAME GROUP).

Liderado por:
- 1× NVIDIA SKYNER
- 2× Cerebras
- 2× Groq
- 4 GGUF local
- 4 GGUF vía API

M3 chat ≠ SKYNER. M3 chat es el arquitecto que trabaja con MAX; SKYNER es el orquestador interno.

---

## 2. CONSTITUCIÓN v1.0 — 13 PRINCIPIOS ORIGINALES

### Principio 1 · FILOSOFÍA
El orquestador opera con filosofía de **Director de Empresa**, no de IA. Gestiona, delega, supervisa. NO improvisa.

### Principio 2 · OBJETIVOS DE ESCALA
- 2000+ agentes (CAPACIDAD)
- 1000+ tareas simultáneas
- No diseñar 2000 agentes reales
- Diseñar CAPACIDAD de escalar

### Principio 3 · NO ES IA, ES CÓDIGO
El orquestador es **90% código determinista + 10% LLM**.

Por qué:
- Predecible
- Auditable
- Confiable
- Bajo costo
- Sin alucinaciones en decisiones críticas

Uso del LLM:
- Solo donde realmente agrega valor:
  - Razonamiento complejo
  - Generación de texto
  - Interpretación de input
- NUNCA para decisiones de control

### Principio 4 · DIRECTOR DE EMPRESA
El orquestador actúa como Director de Empresa con todas las responsabilidades:
- Planifica
- Asigna recursos
- Contrata (crea agentes)
- Despide (elimina agentes)
- Supervisa
- Reporta al CEO (MAX)
- Decide bajo incertidumbre

### Principio 5 · GESTIÓN MASIVA CON 10 ESTADOS
10 estados posibles para cada tarea:
1. CREADA → recién solicitada
2. EN_COLA → esperando recursos
3. ASIGNADA → agente asignado
4. EJECUTANDO → en proceso
5. PAUSADA → temporalmente detenida
6. VALIDANDO → en revisión
7. COMPLETADA → terminada con éxito
8. FALLIDA → error
9. CANCELADA → detenida por MAX
10. REPLANIFICADA → cambiando enfoque

### Principio 6 · PIZARRAS
Dos tipos de pizarras para tracking:

**Pizarra de Proyecto:**
- Estado del proyecto específico
- Tareas del proyecto
- Agentes asignados
- Recursos usados
- Decisiones tomadas

**Pizarra Maestra:**
- Vista global de todos los proyectos
- Recursos totales asignados
- Estado de cada proyecto
- Alertas globales
- KPIs agregados

### Principio 7 · ESCALADO HORIZONTAL
Escalar **horizontal** (más nodos), no vertical (más poder por nodo).

Cómo:
- Agregar HF Spaces
- Cada Space = nodo
- Nodos se comunican vía bus
- Sin single point of failure

Ventajas:
- Costo controlado
- Sin límites teóricos
- Resiliencia
- Mantenimiento sin downtime

### Principio 8 · COLMENAS POR ESPECIALIDAD
Agentes se agrupan en **colmenas** según especialidad.

Ejemplo de colmenas:
- Colmena de Código
- Colmena de Testing
- Colmena de Investigación
- Colmena de Auditoría
- Colmena de Output
- Colmena de Investigación HF
- Colmena de Aprendizaje
- Colmena de Meta (crear agentes)

Ventajas:
- Expertise concentrada
- Comunicación eficiente (mismo idioma)
- Mejor performance
- Auto-organización

### Principio 9 · MULTI-MODELO INTERCAMBIABLE
El orquestador NO está atado a un modelo. Puede cambiar.

Modelos disponibles:
- GGUF local (HRM-Text-1B, Qwen2.5-Coder-1.5B, Granite-4.1-3B, LFM2.5-1.2B-Thinking)
- APIs (4 NVIDIA NIM, 6 Cerebras, 6 Groq, GPT-OSS-20B)

Cambio dinámico:
- Por tarea
- Por disponibilidad
- Por costo
- Por calidad requerida

### Principio 10 · MÍNIMA INFRAESTRUCTURA
El orquestador requiere la mínima infraestructura posible.

Objetivo $0:
- HF Spaces free tier
- API free tiers
- GGUF local sin costo
- Sin servers dedicados
- Sin bases de datos caras

Restricciones:
- MAX solo tiene smartphones + iPad
- Sin PC para servidores
- Todo debe correr en HF

### Principio 11 · ESCALABILIDAD 10 → 2000
El sistema debe escalar de 10 a 2000 agentes **sin redesign**.

Cómo se logra:
- Diseño stateless (sin estado compartido)
- Comunicación vía bus de eventos
- Configuración dinámica
- Sin acoplamiento fuerte

### Principio 12 · ORGANIZACIÓN ABSOLUTA
Todo debe estar **perfectamente organizado**. Nada se pierde, nada se duplica.

Reglas:
- Cada archivo en su lugar
- Cada skill en su categoría
- Cada agente en su colmena
- Cada evento en su log
- Cada decisión documentada
- Cada versión etiquetada

### Principio 13 · SO DISTRIBUIDO PARA IA
El orquestador es un **Sistema Operativo Distribuido** diseñado específicamente para agentes de IA.

Componentes tipo OS:
- Kernel (Runtime Kernel)
- Process Manager (State Machine)
- File System (OVFS)
- Scheduler (10 colas)
- IPC (Bus de eventos)
- Memory Manager (Output Memory)
- I/O Manager (Multi Delivery)

---

## 3. CONSTITUCIÓN v2.0 — 13 PRINCIPIOS ADICIONALES (TOTAL 26)

### Principio 14 · AUTO-EVOLUCIÓN
El sistema evoluciona solo. Mejora con el uso.

Mecanismos:
- Meta-Learning entre releases
- Self-Improving Output Quality
- Auto-Curación de skills
- Counterfactual reasoning
- Causalidad (no correlación)

### Principio 15 · SKILLS PERSISTENTES
Las skills deben persistir Y tener respaldo.

Requisitos:
- Persistencia: skills no se pierden al reiniciar
- Respaldo: backup cifrado de skills
- Versionado: cada skill tiene versiones
- Replicación: skills disponibles en todos los nodos

### Principio 16 · RAÍZ ÚNICA DE SKILLS
Existe UNA SOLA raíz para todas las skills (BIS).

Por qué:
- Evitar duplicación
- Consistencia
- Fácil auditoría
- Catálogo unificado

### Principio 17 · JUEZ SUPERVISOR VALIDADOR
Un juez supervisor con 8 reglas valida TODO antes de ejecutar.

Las 8 reglas:
- R1 · ¿Cumple Constitución?
- R2 · ¿Cumple Fase 0.5 (confirmación)?
- R3 · ¿Tiene recursos asignados?
- R4 · ¿CSA aprobó?
- R5 · ¿Auditor SID aprobó?
- R6 · ¿Definition Score ≥ 95%?
- R7 · ¿No viola restricciones?
- R8 · ¿MAX dio luz verde?

### Principio 18 · AUTO-RUN EN PRIMERA EJECUCIÓN
El sistema se auto-instala y arranca solo en la primera ejecución.

Cómo:
1. Detecta entorno
2. Descarga dependencias
3. Configura secretos
4. Inicializa estado
5. Arranca orquestador
6. Reporta a MAX

### Principio 19 · CIFRADO Y SEGURIDAD
TODO debe estar cifrado. Ningún secreto en texto plano.

Qué cifrar:
- API keys
- Tokens HF / GitHub
- Memoria de outputs sensibles
- Comunicaciones entre agentes
- Respaldos

### Principio 20 · NÚCLEO SOLO VÍA API
El núcleo del orquestador SOLO se accede vía API, nunca directamente.

Por qué:
- Control de acceso
- Auditoría
- Versionado de cambios
- Testing aislado
- Seguridad

### Principio 21 · BOOTSTRAP AUTÓNOMO
El sistema arranca solo desde cero sin intervención.

### Principio 22 · 10 MÓDULOS INDEPENDIENTES
El sistema se divide en 10 módulos independientes:
1. Input Engine
2. SID (definición)
3. BIS (skills)
4. Loop (ejecución)
5. CSA (auditoría)
6. Output Engine
7. OOS (orquestación output)
8. OVFS (file system)
9. Memoria
10. Orquestador (MAXBRY)

### Principio 23 · CERO CONFIGURACIÓN
El sistema funciona con configuración por defecto. MAX no debe configurar nada.

### Principio 24 · DESCARGA INTELIGENTE
El sistema descarga solo lo necesario, cuando lo necesita.

### Principio 25 · INICIO AUTÓNOMO
Una vez que MAX da datos pre-flight, el sistema arranca solo.

Lo que MAX da:
- GitHub username + PAT
- HF username + 6 tokens
- 16 API keys (4 NIM, 6 Cerebras, 6 Groq)
- Turso DB
- Telegram bot token

### Principio 26 · ESCALABILIDAD HORIZONTAL
Reafirma la escalabilidad horizontal (refuerza Principio 7).

---

## 4. CONSTITUCIÓN v3.0 — 13 PRINCIPIOS ADICIONALES (TOTAL 39)

### Principio 27 · CSA 10 JUECES CON 5 FASES + VETO
Ver sección CSA más abajo.

### Principio 28 · SID SISTEMA INTELIGENTE DE DEFINICIÓN
Ver sección SID más abajo.

### Principio 29 · INPUT ENGINE (11 componentes + 17 mejoras)
Ver sección Input Engine.

### Principio 30 · SEMANTIC INVARIANT CHECKER
Componente que verifica que el significado NO cambie al pasar por el sistema.

### Principio 31 · OUTPUT ENGINE (13 componentes) + OVFS
Ver sección Output Engine.

### Principio 32 · MICRO-SEPARACIÓN DE CARPETAS (20 módulos)

Los 20 módulos:
1. bis/
2. sid/
3. csa/
4. input_engine/
5. input_swarm/
6. input_forensics/
7. input_discovery/
8. knowledge_discovery/
9. definition_engine/
10. input_compiler/
11. quality_swarm/
12. input_governor/
13. digital_twin/
14. loop/
15. output_engine/
16. oos/
17. ovfs/
18. memory/
19. orchestrator/
20. utils/

### Principios 33-39 · (más principios definidos en el documento original, ver PARCHES-ORQUESTADOR/constitucion/v3/)

---

## 5. CSA — CONSEJO SUPREMO DE AUDITORÍA

10 jueces con autoridad absoluta:

| # | Juez | Responsabilidad |
|---|------|-----------------|
| J1 | Comprensión objetivo | ¿El output realmente entiende QUÉ se pidió? |
| J2 | Cobertura requisitos | ¿Todos los requisitos están cubiertos? |
| J3 | Consistencia lógica | ¿El output es lógicamente coherente? |
| J4 | Exactitud técnica | ¿El output es técnicamente correcto? |
| J5 | Arquitectura y diseño | ¿El diseño es correcto y mantenible? |
| J6 | Calidad código | ¿El código sigue buenas prácticas? |
| J7 | Investigación y evidencia | ¿Las afirmaciones tienen respaldo? |
| J8 | Optimización y rendimiento | ¿El output es eficiente? |
| J9 | Seguridad y riesgos | ¿El output es seguro? |
| J10 | Calidad final y UX | ¿El output es usable y de calidad? |

### 5 FASES POR JUEZ

Cada juez sigue 5 fases:

**F1 · AUDITA INPUT COMPLETO**
Lee TODO el input antes de decidir

**F2 · BUSCA LO QUE NADIE REVISÓ**
Detecta ambigüedades, objetivos implícitos, lo que otros pasarían por alto

**F3 · 10 SOLUCIONES DISTINTAS**
Genera 10 interpretaciones/soluciones posibles
Conserva la mejor

**F4 · DESTRUYE PROPIA SOLUCIÓN**
Intenta romper su propia interpretación/solución

**F5 · ATACA OTROS 9 JUECES**
Cuestiona a los otros jueces sobre su interpretación

### SISTEMA DE VETO

```
Cualquier juez puede VETAR
       ↓
Si VETO: bloquea output por falta de cumplimiento
       ↓
Entrega paquete completo de corrección:
  - Error detectado
  - Causa raíz
  - Impacto
  - Cómo corregir
  - Qué investigar
  - Qué agentes crear
  - Qué tareas faltan
  - Prioridad
  - Pruebas necesarias
  - Condiciones para aprobar
```

### REGLA INTOCABLE

Los 10 jueces CSA NO se reemplazan. NO se modifican.

---

## 6. SID — SISTEMA INTELIGENTE DE DEFINICIÓN

Componentes:
- **Pre-procesador** (10 pasos)
- **Panel de Definición Inteligente**
- **Clasificador de Incertidumbre** (crítica/alta/media/baja)
- **Motor de Hipótesis**
- **Detector de Contradicciones**
- **Simulador Previo**
- **Plan Preliminar** con nivel confianza
- **Aprendizaje**
- **Preguntas Adaptativas** (árbol de decisión)
- **Auditor de Entrada** (5 preguntas fijas)

### AUDITOR DE ENTRADA — 5 PREGUNTAS FIJAS (INTOCABLES)

1. ¿Cuál es el objetivo real?
2. ¿Qué restricciones aplican?
3. ¿Qué recursos están disponibles?
4. ¿Cuál es el criterio de éxito?
5. ¿Qué riesgos hay?

---

## 7. INPUT ENGINE v4.0 (54 componentes)

### Originales (45):
- SID: 9 componentes
- Input Engine base: 11 componentes
- 17 mejoras adicionales
- 3 auditores de entrada
- 4 capas adicionales

### Nuevos 9 (Capa 34 en adelante):
- **INPUT-100X-A** Input Swarm + Bus de Eventos (40-60 agentes)
- **INPUT-100X-B** Input Discovery (10 detectores: idioma, dominio, intención, objetivos implícitos, restricciones, prioridades, entregables, formato, audiencia, dependencias externas)
- **INPUT-100X-C** Input Forensics (10 detectores: contradicciones, ambigüedad, huecos, requisitos ocultos, riesgos, datos inventados, inconsistencias temporales, conflictos tecnológicos, imposibilidades, scope)
- **INPUT-100X-D** Knowledge Discovery (15 fuentes: papers, StackOverflow, Reddit, Skills internos, Base conocimiento, Memoria proyecto, Artefactos, APIs, Plugins, Modelos vía APIs, Documentación, Repos públicos, Issues, Wikis, Foros)
- **INPUT-100X-E** Claude Definition Engine v2.0 (6 fases: Auto-respuesta, Multi-interpretación, Simulación, Árbol decisiones, Preguntas agrupadas, Definition Score ≥95%)
- **INPUT-100X-F** Input Compiler Expandido (Knowledge Graph, Goal Tree, Requirement Tree, Constraint Tree, Context Graph)
- **INPUT-100X-G** Quality Swarm (10 auditores con veto)
- **INPUT-100X-H** Input Governor (6 estados: RECIBIDO, ANALIZANDO, DEFINIENDO, COMPILANDO, AUDITANDO, APROBADO/VETADO/REPLANIFICAR/PREGUNTAR)
- **INPUT-100X-I** Input Digital Twin (simulación completa antes de ejecutar)

---

## 8. OUTPUT ENGINE + OOS v3.1

### Output Engine (13 componentes):
1. Output Planner
2. Output Compiler (AST)
3. Output Graph
4. Smart Chunking
5. Dynamic Output Engine
6. Manifest
7. Output Registry
8. Output Router
9. Destination Engine
10. Streaming Output
11. Output Validator
12. Multi-Target Delivery
13. Reanudación

### OOS v3.1 (14 componentes):
1. Contrato de salida
2. UOM (Universal Output Model)
3. Semantic Chunk Engine
4. Adaptive Chunk Size
5. Predictive Planner
6. Auto Format Negotiation
7. Intelligent Packaging
8. Multi Delivery Pipeline
9. Intelligent Compression
10. Smart Version Control
11. Incremental Publishing
12. Intelligent Resume
13. Output Verification
14. Delivery Policy Engine

---

## 9. OVFS — OUTPUT VIRTUAL FILE SYSTEM

Sistema de archivos virtual en memoria:

```
/ (root)
├── README.md          → descripción del output
├── docs/              → documentación
├── backend/           → código backend
├── frontend/          → código frontend
├── tests/             → tests
├── diagrams/          → diagramas
├── prompts/           → prompts usados
└── metadata/          → metadata del output
```

---

## 10. OUTPUT v6.1 GOBERNANZA (16 CAPAS)

Output Governor con 8 estados:
1. APROBAR
2. CORREGIR
3. REGENERAR
4. REPLANIFICAR
5. DIVIDIR
6. INVESTIGAR MÁS
7. PREGUNTAR USUARIO
8. CANCELAR

16 capas (A-P):
- A: Output Governor (8 estados)
- B: Output Digital Twin
- C: Multi-Version Generator (5 versiones: calidad, velocidad, mínimo consumo, documentación, código optimizado)
- D: Output Fusion Engine
- E: Acceptance Test Engine
- F: Output Coverage Map
- G: Explainability Engine
- H: Output Provenance
- I: Consistency Swarm (20 microagentes)
- J: Artifact Relationship Graph
- K: Release Manager
- L: Output Memory
- M: Output Score (mínimo 95%, configurable)
- N: Human Approval Layer
- O: Adaptive Delivery
- P: Closed Feedback Loop (LA MÁS IMPORTANTE: publicación → uso real → feedback → memoria → actualización de reglas)

---

## 11. LOOP v6.0 (15 CAPAS + 3 CICLOS PARALELOS)

### 15 Capas:
- A: Workflow DAG (no pipeline)
- B: Runtime Kernel (tipo OS)
- C: Event Sourcing
- D: State Machine por tarea
- E: Prediction Engine
- F: Dynamic Replanning
- G: Model Router Inteligente
- H: Trust Engine (confianza)
- I: Goal Monitor Permanente
- J: Contract Engine
- K: Resource Economy
- L: Semantic Diff
- M: Universal Artifact Graph
- N: Failure Recovery Engine
- O: Executive Board (3-5 agentes)

### 3 CICLOS PARALELOS:
- **CICLO A · EJECUCIÓN** (CREAR → VALIDAR → CORREGIR → ENTREGAR)
- **CICLO B · SUPERVISIÓN** (MONITORIZAR → MEDIR → REPLANIFICAR)
- **CICLO C · APRENDIZAJE** (REGISTRAR → ANALIZAR → OPTIMIZAR → ACTUALIZAR REGLAS)

Comunicados por bus de eventos.

---

## 12. BIS (BIBLIOTECA INTELIGENTE DE SKILLS)

### 14 Categorías:
- A · ARQUITECTURA
- B · GESTIÓN
- C · FRONTEND
- D · BACKEND
- E · MÓVIL
- F · ESCRITORIO
- G · BASES DE DATOS
- H · APIs
- I · DEVOPS
- J · IA
- K · TESTING
- L · SEGURIDAD
- M · AUTOMATIZACIÓN
- N · LENGUAJES

### 13 Criterios de Skills:
1. Relevancia
2. Efectividad comprobada
3. Costo de aplicación
4. Compatibilidad
5. Mantenibilidad
6. Documentación
7. Reusabilidad
8. Seguridad
9. Performance
10. Escalabilidad
11. Compliance
12. Test coverage
13. Comunidad / Soporte

### 3 Versiones:
- v1 · Inicial (básica)
- v2 · Mejorada (con debate)
- v3 · Avanzada (con productor + consumidor)

### Debate 4 Especialistas:
1. Productor (quien la creó)
2. Consumidor (quien la usa)
3. Auditor (quien valida)
4. Crítico (quien busca fallas)

### BIS-100X Mejoras:
- BIS-100X-F: 5 investigadores paralelos
- BIS-100X-G: Renovación cada 15 días
- BIS-100X-H: Detector de intención
- BIS-100X-I: Pre-descarga inteligente

---

## 13. 10 PROPUESTAS M3 PARA OUTPUT (9 APROBADAS + 1 RECHAZADA)

1. Pre-Mortem Analysis ✅
2. Output Sandbox ❌ RECHAZADO POR MAX
3. Auto-Rollback Inteligente ✅
4. Meta-Learning entre Releases ✅
5. Output Personalization ✅
6. Multi-Stakeholder Output ✅
7. Causal Output Tracing ✅
8. Output Marketplace Interno ✅
9. Self-Improving Output Quality ✅
10. Production Monitoring Post-Publish ✅

---

## 14. 10 PROPUESTAS M3 PARA INPUT/LOOP (TODAS APROBADAS)

1. Meta-agentes que crean otros agentes ✅
2. Causalidad (no correlación) ✅
3. Counterfactual reasoning ✅
4. Auto-modificación de código ✅
5. Memoria Episódica ✅
6. Zero-shot transfer entre proyectos ✅
7. Neural Architecture Search ✅
8. Time-travel debugging ✅
9. Inteligencia colectiva emergente ✅
10. Auto-curriculum ✅

---

## 15. REGLA ABSOLUTA DE MAX

"NUNCA crear ni cambiar nada sin mi APROBADO explícito"
"SOLO AGREGO capas, NUNCA reemplazo"
"MANTENER todos los nombres originales"

---

## 16. COSAS INTOCABLES

- 10 Jueces CSA (J1-J10) con 5 fases
- Auditor SID 5 preguntas fijas
- Constitución 39 principios
- 14 categorías BIS
- 30 micro-agentes
- 11 internal roles
- 10 parallel queues
- 10-agent consensus council
- 6 autonomy levels L1-L6
- 12 task models TM01-TM12
- 5 loop versions ALV_LOP_*
- 3 monitors
- 9 GGUF models confirmados
- 16 API keys=== END ===

=== ARCHIVO 29 (6673c665 constitucion-completa) ===
# MASTER DOCUMENTO 03: CONSTITUCIÓN COMPLETA
## MAXBRY SUPER TEAM · Los 39 Principios Detallados

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. INTRODUCCIÓN

La Constitución del Orquestador MAXBRY es el documento legal supremo. Contiene 39 principios distribuidos en 3 versiones progresivas (v1.0, v2.0, v3.0).

---

## 2. CONSTITUCIÓN v1.0 — LOS 13 ORIGINALES

### Artículo 1 · FILOSOFÍA
El Orquestador opera como **Director de Empresa**, no como IA. Planifica, asigna, supervisa, reporta. Decide bajo incertidumbre.

### Artículo 2 · OBJETIVOS DE ESCALA
Soporta **2000+ agentes** y **1000+ tareas** simultáneas como CAPACIDAD (no implementación).

### Artículo 3 · 90% CÓDIGO + 10% LLM
**90% código determinista** (predecible, auditable, bajo costo). **10% LLM** solo donde realmente agrega valor (razonamiento, generación).

### Artículo 4 · DIRECTOR DE EMPRESA
Responsabilidades:
- Planifica como CEO
- Asigna recursos como CFO
- Contrata/despide agentes como CHRO
- Supervisa como COO
- Reporta a MAX

### Artículo 5 · GESTIÓN MASIVA
**10 estados por tarea**: CREADA, EN_COLA, ASIGNADA, EJECUTANDO, PAUSADA, VALIDANDO, COMPLETADA, FALLIDA, CANCELADA, REAPERTURA.

### Artículo 6 · PIZARRAS
- **Pizarra de Proyectos** (proyectos activos)
- **Pizarra Maestra** (estado global)

### Artículo 7 · ESCALADO HORIZONTAL
Escalar = **más nodos**, NO más poder por nodo. Diseño sin redesign.

### Artículo 8 · COLMENAS POR ESPECIALIDAD
Agentes agrupados por especialidad (código, test, doc, research, etc.).

### Artículo 9 · MULTI-MODELO INTERCAMBIABLE
No atado a un modelo. 9 GGUF + 16 API keys intercambiables.

### Artículo 10 · MÍNIMA INFRAESTRUCTURA
- HF free tier
- API free tiers
- GGUF local
- Sin servers dedicados
- Costo $0/mes

### Artículo 11 · ESCALABILIDAD 10→2000
Sistema escala de 10 a 2000 agentes **sin redesign**.

### Artículo 12 · ORGANIZACIÓN ABSOLUTA
**Nada se pierde.** Cada evento se registra. Cada estado se rastrea. Cada decisión se documenta.

### Artículo 13 · SO DISTRIBUIDO PARA IA
Actúa como **Sistema Operativo Distribuido para IA**: kernel, scheduler, memory manager, file system, IPC.

---

## 3. CONSTITUCIÓN v2.0 — LOS 13 ADICIONALES

### Artículo 14 · AUTO-EVOLUCIÓN
El sistema **mejora con uso**. Meta-Learning + Counterfactual reasoning.

### Artículo 15 · SKILLS PERSISTENTES
Skills **con respaldo**. BIS persiste skills en disco + memoria.

### Artículo 16 · RAÍZ ÚNICA DE SKILLS
**BIS es el único** repositorio de skills. No duplicación.

### Artículo 17 · JUEZ SUPERVISOR VALIDADOR
**8 reglas** para validar antes de patchear:
1. Nombre correcto
2. Formato válido
3. Aprobado por MAX
4. Sin reemplazo de originales
5. STATE JSON actualizado
6. Trazabilidad
7. Audit completo
8. Compatible con Constitución

### Artículo 18 · AUTO-RUN PRIMERA EJECUCIÓN
En la primera ejecución, el sistema se auto-configura **sin intervención**.

### Artículo 19 · CIFRADO Y SEGURIDAD
- Secretos encriptados en reposo
- API keys NUNCA en texto plano
- Comunicación cifrada
- Audit log completo

### Artículo 20 · NÚCLEO SOLO VÍA API
El núcleo **NUNCA** se accede directamente. Siempre vía API.

### Artículo 21 · BOOTSTRAP AUTÓNOMO
El sistema arranca **solo** una vez configurados los pre-flight.

### Artículo 22 · 10 MÓDULOS INDEPENDIENTES
Cada módulo:
- Tiene su propia responsabilidad
- Tiene su propio test
- Tiene su propia versión
- Puede fallar sin tumbar el sistema

### Artículo 23 · CERO CONFIGURACIÓN
**Defaults sensatos**. El sistema funciona out-of-the-box.

### Artículo 24 · DESCARGA INTELIGENTE
Solo descarga lo necesario. No baja modelos no usados.

### Artículo 25 · INICIO AUTÓNOMO
Una vez con datos pre-flight, **se inicia sin intervención** de MAX.

### Artículo 26 · ESCALABILIDAD HORIZONTAL
Refuerza el principio #7: más nodos = más capacidad.

---

## 4. CONSTITUCIÓN v3.0 — LOS 13 AVANZADOS

### Artículo 27 · CSA 10 JUECES + 5 FASES + VETO
- **10 Jueces** CSA con autoridad absoluta
- **5 fases** por juez:
  - F1: Audita input completo
  - F2: Busca lo que NADIE revisó
  - F3: 10 soluciones distintas (conserva mejor)
  - F4: Destruye propia solución
  - F5: Ataca otros 9 jueces
- **Sistema de VETO**: cualquier juez puede vetar → bloquea output

### Artículo 28 · SID SISTEMA INTELIGENTE DE DEFINICIÓN
- **5 preguntas fijas** que NUNCA cambian:
  1. ¿Qué es esto?
  2. ¿Para quién es?
  3. ¿Qué problema resuelve?
  4. ¿Cómo se usa?
  5. ¿Qué NO es?
- **Definition Score ≥ 95%** para continuar

### Artículo 29 · INPUT ENGINE v4.0
**54 componentes** distribuidos en:
- 45 originales
- 9 nuevos (A-I)

### Artículo 30 · SEMANTIC INVARIANT CHECKER
- Garantiza que el **significado se preserva**
- Detecta cambios de intención
- Trigger si semantic_drift > 0.10

### Artículo 31 · OUTPUT ENGINE + OVFS
- **13 componentes** Output Engine
- **14 componentes** OOS v3.1
- **OVFS** = Output Virtual File System

### Artículo 32 · MICRO-SEPARACIÓN DE CARPETAS
**20 módulos** con carpetas separadas (≤200 LOC cada uno).

### Artículo 33 · CLOSED FEEDBACK LOOP
```
Publicar → Uso real → Feedback → Memoria → Reglas
```

### Artículo 34 · MULTI-TARGET DELIVERY
**23 destinos** paralelos. Cada output va a múltiples canales.

### Artículo 35 · ADAPTIVE DELIVERY
El sistema **aprende** los patrones de MAX. No pregunta cada vez.

### Artículo 36 · CONFIDENCE SCORING
- **Umbral 95%** mínimo
- Score por tarea, agente, modelo

### Artículo 37 · AUTO-ROLLBACK
Si un cambio degrada el sistema, **rollback automático** al estado anterior seguro.

### Artículo 38 · META-LEARNING
El sistema **aprende de releases pasados**. Identifica qué funcionó y qué no.

### Artículo 39 · PRODUCTION MONITORING
Monitorea **post-publicación**. Detecta regresiones en uso real.

---

## 5. REGLAS DERIVADAS

### 5.1 Regla de oro
> "NUNCA crear ni cambiar nada sin APROBADO explícito de MAX"

### 5.2 Cosas intocables
- 10 Jueces CSA + 5 fases + veto
- Auditor SID 5 preguntas fijas
- 39 principios de esta Constitución
- 14 categorías BIS
- Nombres y cantidades originales aprobados

### 5.3 Regla de capas
> "SOLO AGREGO capas, NUNCA reemplazo"

### 5.4 Regla de validación
> "Cada salida valida antes de patchear"

---

## 6. TABLA RESUMEN

| # | Principio | Versión |
|---|-----------|---------|
| 1 | Filosofía | v1.0 |
| 2 | Objetivos de escala | v1.0 |
| 3 | 90% código + 10% LLM | v1.0 |
| 4 | Director de Empresa | v1.0 |
| 5 | Gestión masiva | v1.0 |
| 6 | Pizarras | v1.0 |
| 7 | Escalado horizontal | v1.0 |
| 8 | Colmenas | v1.0 |
| 9 | Multi-modelo | v1.0 |
| 10 | Mínima infraestructura | v1.0 |
| 11 | Escalabilidad 10→2000 | v1.0 |
| 12 | Organización absoluta | v1.0 |
| 13 | SO distribuido para IA | v1.0 |
| 14 | Auto-evolución | v2.0 |
| 15 | Skills persistentes | v2.0 |
| 16 | Raíz única BIS | v2.0 |
| 17 | Juez supervisor (8 reglas) | v2.0 |
| 18 | Auto-run primera ejecución | v2.0 |
| 19 | Cifrado y seguridad | v2.0 |
| 20 | Núcleo solo vía API | v2.0 |
| 21 | Bootstrap autónomo | v2.0 |
| 22 | 10 módulos independientes | v2.0 |
| 23 | Cero configuración | v2.0 |
| 24 | Descarga inteligente | v2.0 |
| 25 | Inicio autónomo | v2.0 |
| 26 | Escalabilidad horizontal | v2.0 |
| 27 | CSA 10 jueces | v3.0 |
| 28 | SID 5 preguntas | v3.0 |
| 29 | Input Engine v4.0 | v3.0 |
| 30 | Semantic Invariant Checker | v3.0 |
| 31 | Output Engine + OVFS | v3.0 |
| 32 | Micro-separación 20 módulos | v3.0 |
| 33 | Closed Feedback Loop | v3.0 |
| 34 | Multi-Target Delivery | v3.0 |
| 35 | Adaptive Delivery | v3.0 |
| 36 | Confidence Scoring ≥ 95% | v3.0 |
| 37 | Auto-Rollback | v3.0 |
| 38 | Meta-Learning | v3.0 |
| 39 | Production Monitoring | v3.0 |

---

## 7. APLICACIÓN EN CADA SALIDA

Cada output del sistema debe:
1. Citar los principios de la Constitución aplicables
2. Verificar cumplimiento
3. Documentar desviaciones (si las hay)
4. Actualizar STATE JSON
5. Registrar AUDIT FINAL

---

## 8. CONCLUSIÓN

La Constitución del Orquestador MAXBRY SUPER TEAM tiene **39 principios** distribuidos en 3 versiones. Es la ley suprema que rige todos los componentes del sistema. Cualquier desviación debe ser aprobada explícitamente por MAX.
</content>=== END ===

=== ARCHIVO 20 (43a530a2 arquitectura-completa) ===
# DOCUMENTO 12: ARQUITECTURA COMPLETA DEL SISTEMA
## Extraído del historial del chat

---

## 1. NCT NEURONAS CODE TURBO — VISIÓN GENERAL

**Qué es:** Un MÓDULO ADICIONAL de coordinación para el software existente.
NO reemplaza ningún bloque actual. NO modifica el código original.
Es un tercer modo de trabajo que se añade a los ya existentes.

**Modos del software:**
1. Modo Manual → El usuario controla cada paso
2. Modo Semi-automático → El software actual opera con supervisión
3. Modo Continuo (NCT) → Coordinación automática para tareas largas

**Qué hace NCT:**
Coordina los 25 bloques existentes para ejecutar tareas complejas de forma automática y continua, sin supervisión humana.

**Cómo funciona:**
- Fase 0-3: Clasifica, planifica, descompone y prepara
- Fase 4: Invoca los bloques existentes como workers (única fase con IA)
- Fase 5-6: Monitorea (PAD/Ansiedad/Drift) y verifica (3-capas)
- Fase 7-9: Consolida, repara si falla, y entrega

**Arquitectura:**
- 8 archivos Python de coordinación (~960 líneas)
- 0% IA en el coordinador (solo reglas fijas)
- IA solo en Fase 4 (ejecución) y Fase 6 (verificación)
- Comunicación vía state.json con los bloques existentes

**No requiere:**
- No instalar Kimi K2.5, MiniMax, ni Hermes
- No desplegar agentes externos
- No modificar el código existente

**Sí requiere:**
- Lista de los 25 bloques con: nombre, función, formato entrada/salida
- Definir cómo se invoca cada bloque (API, CLI, función directa)

---

## 2. UBICACIÓN Y ESTRUCTURA DEL PROYECTO

```
proyecto_principal/                  # Tu proyecto actual
│
├── software_principal/              # Tus 25 bloques (SIN TOCAR)
│   ├── arquitectura/
│   ├── rag/
│   ├── escritor/
│   ├── ejecutor/
│   ├── validacion/
│   ├── reparacion/
│   └── ... (20 bloques más)
│
├── nct_coordinator/                 # ← NUEVO MÓDULO (adicional)
│   ├── __init__.py
│   ├── fsm.py                       # Orquestador 10 fases
│   ├── classifier.py                # Clasificación dual (Fase 0)
│   ├── router.py                    # Selección modo/ruta (Fase 1)
│   ├── planner.py                   # Descomposición (Fase 2)
│   ├── context_isolator.py          # Aislamiento (Fase 3)
│   ├── worker_pool.py               # Pool de workers (Fase 4)
│   ├── monitor.py                   # PAD + Ansiedad + Drift (Fase 5)
│   ├── verifier.py                  # 3-capas (Fase 6)
│   ├── consolidator.py              # EROS + Coordinator (Fase 7)
│   ├── repair.py                    # Pipeline 5 pasos (Fase 8)
│   └── deliver.py                   # Empaquetado final (Fase 9)
│
├── state/                           # ← NUEVO (gestión de estado)
│   ├── engine.py                    # Event sourcing + snapshots
│   └── telemetry.py                 # Métricas PAD
│
├── config/
│   └── nct_config.yaml              # Config del coordinador
│
├── state.json                       # Estado compartido (runtime)
│
└── main.py                          # Entry point con selector de modo
```

---

## 3. 25 BLOQUES DEL SOFTWARE PRINCIPAL (NO MODIFICAR)

```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│Arquitect.│ │   RAG    │ │ Escritor │ │  Ejecutor    │
└──────────┘ └──────────┘ └──────────┘ └──────────────┘
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│Validación│ │Reparación│ │  Test    │ │   Deploy     │
└──────────┘ └──────────┘ └──────────┘ └──────────────┘
              ... (25 bloques)
```

---

## 4. INTERFAZ PRINCIPAL DEL SOFTWARE

### Selección de Modo:

```
┌─────────────┐  ┌─────────────────┐  ┌───────────────────┐
│             │  │                 │  │                   │
│   MANUAL    │  │  SEMI-AUTOMÁTICO│  │    CONTINUO       │
│             │  │                 │  │    (Automático)   │
└─────────────┘  └─────────────────┘  └───────────────────┘
```

### Modo Manual:
- El usuario decide qué bloque usar, cuándo y en qué orden
- Interfaz paso a paso
- Ideal para tareas pequeñas o específicas

### Modo Semi-Automático:
- El software sugiere bloques y orden
- El usuario aprueba o modifica cada fase
- Puntos de confirmación entre etapas

### Modo Continuo:
- El usuario solo describe la tarea final
- NCT descompone, coordina, ejecuta, verifica y entrega
- Sin intervención humana durante la ejecución
- Recuperación automática ante fallos

---

## 5. FLUJO COMPLETO (MODO CONTINUO)

```
Usuario describe tarea
    │
    ▼
classifier.py (Fase 0) ─► router.py (Fase 1) ─► planner.py (Fase 2-3)
    │
    ▼
worker_pool.py (Fase 4) ─► INVOCA TUS 25 BLOQUES ORIGINALES
    │
    ├─► monitor.py (Fase 5) — PAD + Ansiedad + Anti-Drift
    ├─► verifier.py (Fase 6) — 3 capas de verificación
    │
    ▼
consolidator.py (Fase 7) ─► repair.py (Fase 8, si falla) ─► deliver.py (Fase 9)
    │
    ▼
Usuario recibe resultado final con trazabilidad completa
```

---

## 6. PRINCIPIOS CLAVE DE NCT

- 100% Python determinista (sin IA en el coordinador)
- IA solo como motor en Fase 4 (ejecución) y Fase 6 (verificación)
- Comunicación vía state.json (event sourcing)
- Los 25 bloques originales NO se modifican
- Recuperación automática ante fallos (5 pasos de repair)
- Trazabilidad completa de cada decisión y ejecución

---

## 7. INTERFAZ DE USUARIO DEL SOFTWARE

```
┌─────────────────────────────────────────────────────────────────┐
│                    SELECCIÓN DE MODO                          │
│                                                               │
│  ┌─────────────┐  ┌─────────────────┐  ┌───────────────────┐  │
│  │             │  │                 │  │                   │  │
│  │   MANUAL    │  │  SEMI-AUTOMÁTICO│  │    CONTINUO       │  │
│  │             │  │                 │  │    (Automático)   │  │
│  └─────────────┘  └─────────────────┘  └───────────────────┘  │
│                                                               │
│  Usuario controla   Software opera        Software trabaja    │
│  cada paso          con supervisión       sin supervisión     │
│                     del usuario           (NCT coordina)      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. NUEVOS BLOQUES NCT (13 ARCHIVOS)

### BLOQUES DE COORDINACIÓN (8)

1. **fsm.py** — Orquestador central, 10 fases, sin IA
2. **classifier.py** — Clasifica tareas (simple/batch/compleja)
3. **router.py** — Elige ruta y modo de ejecución
4. **planner.py** — Descompone en subtareas balanceadas
5. **context_isolator.py** — Aísla contexto por worker
6. **worker_pool.py** — Invoca tus 25 bloques como workers
7. **monitor.py** — PAD + Ansiedad + Anti-Drift
8. **verifier.py** — Verificación adversarial 3-capas

### BLOQUES DE SOPORTE (5)

9. **consolidator.py** — Consolida resultados de workers
10. **repair.py** — Pipeline 5 pasos si algo falla
11. **deliver.py** — Empaqueta y entrega resultado final
12. **state/engine.py** — Event sourcing + state.json
13. **state/telemetry.py** — Métricas y circuit breaker

---

## 9. MODOS Y FLUJOS

### FLUJO MODO CONTINUO (MÁS IMPORTANTE)

```
USUARIO
  │
  ▼
main.py (selector de modo)
  │
  └─► Modo Continuo ─► nct_coordinator toma el control
       │
       ▼
   fsm.py (orquestador)
       │
       ▼
   classifier.py → router.py → planner.py → context_isolator.py
       │
       ▼
   worker_pool.py ──► INVOCA TUS 25 BLOQUES (API/CLI/función)
       │
       ▼
   monitor.py (paralelo a la ejecución)
       │
       ▼
   verifier.py (valida outputs de tus bloques)
       │
       ▼
   consolidator.py → repair.py (si falla) → deliver.py
       │
       ▼
   USUARIO RECIBE RESULTADO
```

---

## 10. ARQUITECTURA DETALLADA DE NCT COORDINATOR

```
┌─────────────────────────────────────────────────────────────────┐
│              SOFTWARE ORIGINAL (25 BLOQUES) — SIN MODIFICAR    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NUEVOS BLOQUES NCT (13 archivos)             │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ BLOQUES DE COORDINACIÓN (8)                               │ │
│  │                                                           │ │
│  │ 1. fsm.py            Orquestador central, 10 fases, sin IA   │ │
│  │ 2. classifier.py     Clasifica tareas (simple/batch/compleja) │ │
│  │ 3. router.py         Elige ruta y modo de ejecución          │ │
│  │ 4. planner.py        Descompone en subtareas balanceadas     │ │
│  │ 5. context_isolator.py  Aísla contexto por worker            │ │
│  │ 6. worker_pool.py    Invoca tus 25 bloques como workers      │ │
│  │ 7. monitor.py        PAD + Ansiedad + Anti-Drift             │ │
│  │ 8. verifier.py       Verificación adversarial 3-capas        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ BLOQUES DE SOPORTE (5)                                    │ │
│  │                                                           │ │
│  │ 9.  consolidator.py   Consolida resultados de workers         │ │
│  │ 10. repair.py         Pipeline 5 pasos si algo falla          │ │
│  │ 11. deliver.py        Empaqueta y entrega resultado final    │ │
│  │ 12. state/engine.py   Event sourcing + state.json             │ │
│  │ 13. state/telemetry.py  Métricas y circuit breaker            │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. UBICACIÓN EN EL PROYECTO: NTC_COORDINATOR/

```
nct_coordinator/   ← NUEVO (8 archivos + 2 state + config + main.py)
   ├── fsm.py
   ├── classifier.py
   ├── router.py
   ├── planner.py
   ├── context_isolator.py
   ├── worker_pool.py
   ├── monitor.py
   ├── consolidator.py
   └── repair.py
```

---

## 12. ARQUITECTURA MÓDULO NCT — ADICIONAL AL SOFTWARE PRINCIPAL

**UBICACIÓN:** /nct_coordinator/ (nueva carpeta, no toca nada existente)

**ARCHIVOS NUEVOS:** 13 (8 coordinador + 2 state + config + main.py + __init__)

**PRINCIPIO:** El módulo NCT es un ORQUESTADOR que invoca los 25 bloques existentes como workers. No los modifica, no los reescribe, no los reemplaza. Solo les asigna tareas y recoge resultados.

**COMUNICACIÓN:** state.json + API interna de cada bloque

**MODOS:** Manual | Semi-Auto | Continuo (selector en main.py)

**IA:** Solo en Fase 4 (worker_pool) y Fase 6 (verifier), siempre bajo schema estricto. El coordinador es 100% Python determinista.

---

## 13. FLUJO DETALLADO POR FASE

### Fase 0 - Clasificación:
```
FASE 0 — CLASIFICACIÓN DUAL
┌─────────────────┐  ┌──────────────────────┐
│ Intención (Kimi) │  │ Tipo tarea (MiniMax) │
│ Simple/Media/    │  │ Simple/Batch/Complex │
│ Compleja         │  │ + Tipo proyecto      │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
           Clasificación unificada
```

### Fase 1 - Modo y Ruta:
```
FASE 1 — SELECCIÓN DE MODO Y RUTA
┌─────────────────┐  ┌──────────────────────┐
│ Modo agente     │  │ Ruta ejecución       │
│ (Kimi)          │  │ (MiniMax)            │
│ OK Computer/    │  │ Directa/Batch/       │
│ Skills/Swarm    │  │ Agentes especializ.  │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
           Decisión unificada
```

### Fase 2 - Skills y Descomposición:
```
FASE 2 — SKILLS Y DESCOMPOSICIÓN
┌─────────────────┐  ┌──────────────────────┐
│ Carga Skills    │  │ Planificación        │
│ (Kimi)          │  │ (MiniMax)            │
│ SKILL.md        │  │ todo_write + agentes │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
Plan unificado: subtareas + agentes + orden
```

### Fase 3 - Aislamiento:
```
FASE 3 — AISLAMIENTO Y PREPARACIÓN
┌─────────────────┐  ┌──────────────────────┐
│ Spawn subagentes│  │ Structured Summaries │
│ congelados      │  │ (MiniMax)            │
│ (Kimi)          │  │ Contexto aislado     │
└────────┬────────┘  └──────────┬───────────┘
         └──────────┬───────────┘
                    ▼
Workers listos con contexto aislado y tools
```

### Fase 4 - Ejecución (ÚNICA CON IA):
```
FASE 4 — EJECUCIÓN (Única que usa IA)
┌─────────────────────────────────────────────┐
│ Worker Pool (Kimi)                         │
│ • Hasta 100 workers simultáneos             │
│ • asyncio.gather()                          │
│ • Pipeline 7 pasos por worker               │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Team Engine (MiniMax) — dentro de c/worker  │
│ Leader → Worker → Verifier (3 rondas)       │
└─────────────────────────────────────────────┘
Tus 25 bloques reciben DSL de entrada
y devuelven JSON validado contra schema
```

### Fase 5 - Monitoreo:
```
FASE 5 — MONITOREO SIMULTÁNEO (3 sistemas)
┌──────────┐  ┌──────────────┐  ┌────────────┐
│ PAD      │  │ Ansiedad     │  │ Anti-Drift │
│ (Kimi)   │  │ (MiniMax)    │  │ (Kimi)     │
│          │  │              │  │            │
│ Arousal  │  │ ¿Duda en     │  │ KL(plan || │
│ >0.8 Y   │  │ círculos?    │  │ actual)    │
│ Pleasure │  │              │  │ >0.02?     │
│ <0.2?    │  │ Nivel 1/2/3  │  │            │
│          │  │              │  │            │
│ SIGKILL  │  │ Confirmación │  │ Halt →     │
│ +Respawn │  │ o Respawn    │  │ Rollback   │
└────┬─────┘  └──────┬───────┘  └─────┬──────┘
     └───────────────┬────────────────┘
                     ▼
           State.json actualizado
```

### Fase 6 - Verificación 3-Capas:
```
FASE 6 — VERIFICACIÓN 3-CAPAS
CAPA 1: Adversarial (MiniMax)
   Verifier busca errores → 3 rondas
                ↓
CAPA 2: Cruzada (Kimi)
   Executor B valida output de A
                ↓
CAPA 3: Maker-Checker (Ambos)
   Módulo A produce, Módulo B verifica
                ↓
Solo si 3 capas OK → output certificado
```

### Fase 7 - Consolidación:
```
FASE 7 — CONSOLIDACIÓN JERÁRQUICA
┌─────────────────────────────────────────────┐
│ EROS 3-Tier (Kimi)                         │
│ Tier 3 (Executors) → logs crudos            │
│ Tier 2 (Controllers) → Strategic Pulses     │
│ Tier 1 (Orchestrator) → <5% contexto        │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Coordinator (MiniMax)                       │
│ Recibe outputs, integra, maneja escalados   │
└─────────────────────────────────────────────┘
                      ↓
Informe pre-entrega: completitud, drift, etc.
```

### Fase 8 - Repair Pipeline:
```
FASE 8 — REPAIR PIPELINE (si algo falló)
Paso 1: Retry simple (3 intentos)
   ↓ falló
Paso 2: Context Compression (L1/L2)
   ↓ falló
Paso 3: Fallback Model / Agent
   ↓ falló
Paso 4: Restore Checkpoint
   ↓ falló
Paso 5: Escalate (Coordinator decide)
   → Replanificar / Preguntar usuario / Abortar
```

### Fase 9 - Entrega:
```
FASE 9 — CONSOLIDACIÓN FINAL Y ENTREGA
┌─────────────────────────────────────────────┐
│ Merge resultados + Consistencia global      │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ Empaquetado (KIMI_REF + archivos + URLs)    │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ State.json final: trazabilidad completa     │
└─────────────────────────────────────────────┘
              ↓
      USUARIO RECIBE RESULTADO
```

---

## 14. RESUMEN DEL SISTEMA COMPLETO

**Nivel 1:** Software Principal (25 bloques) - INTOCABLE

**Nivel 2:** NCT Coordinator (13 archivos) - ADICIONAL

**Nivel 3:** MAXBRY SUPER TEAM (orquestador con Constitución, CSA, SID, BIS, Loop, Output Engine, OOS, OVFS)

**Nivel 4:** Modelos GGUF (9) + APIs (16 keys)

**Nivel 5:** Memoria persistente + STATE JSON

**Nivel 6:** Infraestructura (7 HF Spaces, 14 repos, 5 Dockerfiles)

---

## 15. PRINCIPIOS TRANSVERSALES

1. **MVP first** - anti-overengineering
2. **Regla absoluta** - NUNCA sin APROBADO de MAX
3. **Solo agregar** - NUNCA reemplazar
4. **Mantener nombres** - originales aprobados
5. **Cero alucinación** - preguntar si falta info
6. **Independencia** - Orquestador ≠ GGUF ≠ Proyectos
7. **Validación previa** - cada salida valida antes de patchear
8. **Mostrar PENDIENTE** - lo no aprobado es visible
9. **STATE JSON** - siempre actualizado
10. **5 GOALS + 12 PASOS** - en cada salida
</content>=== END ===

=== ARCHIVO 24 (53c49cbf ejemplos-y-arquitectura-detalles) ===
# DOCUMENTO 15: EJEMPLOS Y DETALLES DE ARQUITECTURA
## Extraído del historial del chat

---

## 1. NCT AI ARCHITECTURE v0 (Diagrama Dual)

### VERSIÓN 1 — Chat AI NCT (producto embebido)
```
Sistema completo con MHYTOS como módulo interno.
Vive en la app desktop/mobile del usuario.

USUARIO → MHYTOS Core → SHERIFF → Memory Controller → Memory Scheduler
                                                       ↓
                                                    ROUTER
                                                       ↓
                                                    DSL Planner
                                                       ↓
                                                    DAG Executor → Embedded LLM (Gemma 4 E2B Q4_K_M)
                                                       ↓
                                                    CRITIC LOOP → SENTINEL → Tools/Actions → OUTPUT

Memory Controller interactúa con:
- Working Memory (8-32k)
- Episodic Memory (logs + timestamp)
- Semantic Memory (embeddings)
- Procedural Memory (recetas DSL)
- Graph Memory (NCT→DSL→Router→Mem)
- Working Summary (compresión viva)
```

### VERSIÓN 2 — Adaptador de modelos (MHYTOS externo)
```
MHYTOS como capa desacoplada que gobierna varios backends.
Misma MHYTOS, distintos modelos detrás.

NCT App / Cliente → Adaptador MHYTOS → MHYTOS (external reasoning layer)
                                              ↓
                                          Interface Contract (tool-use + DSL)
                                              ↓
                        ┌─────────────┬───────────┬───────────┐
                        ▼             ▼           ▼           ▼
                    Backend 1     Backend 2    Backend 3    Backend 4
                    Mistral 7B    Kimi K2 API  Claude/GPT   Local GGUF
                        Q4                       API

Memory (Local + Drive + DB configurable por usuario)
Selector de funciones por módulo (apaga lo que no aplica)
```

### Decisiones Aprobadas:
- Arquitectura en capas: SHERIFF → ROUTER → DSL → DAG → CRITIC → SENTINEL
- Memory Controller activo con 6 capas (working/episodic/semantic/procedural/graph/summary)
- DSL con estructura determinista (no prompt-based)
- SENTINEL con rollback si detecta alucinación / inconsistencia
- CRITIC LOOP con condición de parada
- Embedded LLM: Gemma 4 E2B Q4_K_M (2.3B params, agentic-first, mobile-runnable)
- Memoria persistente multi-backend: local + Drive + DB configurable por usuario
- Sin límites en app mobile/desktop (todo local)
- Selector de funciones por módulo (apaga lo que no aplica)
- Pequeño LLM embebido como filtro obligatorio para cualquier LLM externo (≥10B)

### Pendientes:
- Tecnología de Graph Memory (Neo4j / Memgraph / SQLite custom)
- Formato del DSL (YAML / JSON / Python DSL / custom)
- Contrato exacto de interfaz del adaptador (MCP, OpenAI-compatible, custom)
- Backends por defecto en V2
- Memory Scheduler: trigger event-driven vs heurístico
- Capa de Tools/Actions: protocolo
- Observabilidad / tracing
- Manejo de fallos
- Concurrencia / race conditions
- Presupuesto de latencia y costo por request

---

## 2. EJEMPLO DE TAREA: ECOMMERCE MICROSERVICIO

**Usuario:** "Diseña la arquitectura para un e-commerce con microservicios"

### FASE 0 — CLASIFICACIÓN (especializada en arquitectura)

1. ¿Es tarea de arquitectura?
   - Detecta palabras clave: "arquitectura", "diseño del sistema", "estructura del proyecto", "microservicios", "base de datos", "API", "componentes"
   - Si SÍ → activa subflujo ARQ

2. Clasifica tipo de arquitectura:
   - Monolito
   - Microservicios
   - Serverless
   - Frontend + Backend
   - Full-Stack

3. Evalúa complejidad:
   - Simple (1-2 componentes)
   - Media (3-5 componentes, 1-2 integraciones)
   - Compleja (múltiples servicios, colas, caché, escalado)

### FASE 1 — RUTA DE ARQUITECTURA

Selecciona bloques necesarios:
- Arquitectura (bloque principal)
- RAG (investigar patrones, mejores prácticas)
- Escritor (documentar la arquitectura)
- Validador (verificar consistencia)

Orden de ejecución:
1. RAG (investigación previa)
2. Arquitectura (diseño)
3. Validador (revisión)
4. Escritor (documentación)

¿Requiere paralelismo?
- Simple → Secuencial
- Media → RAG en paralelo con Arquitectura inicial
- Compleja → RAG masivo + Arquitectura por módulos en paralelo

### FASE 2 — PLANIFICACIÓN Y DESCOMPOSICIÓN ARQUITECTÓNICA

**Paso 1: RECOPILACIÓN DE REQUISITOS (RAG + usuario)**
- Funcionales: ¿qué debe hacer el sistema?
- No funcionales: escalabilidad, seguridad, latencia
- Restricciones: presupuesto, tiempo, stack obligatorio

**Paso 2: INVESTIGACIÓN DE PATRONES (RAG)**
- Buscar patrones de arquitectura aplicables
- Buscar antipatrones a evitar
- Buscar stacks tecnológicos recomendados
- Buscar casos de estudio similares

**Paso 3: DISEÑO DE COMPONENTES (Arquitectura)**
- Identificar módulos/servicios
- Definir interfaces entre componentes
- Diseñar modelo de datos
- Diseñar flujo de datos
- Seleccionar stack tecnológico

**Paso 4: VALIDACIÓN DE CONSISTENCIA (Validador)**
- ¿Todos los requisitos tienen componente asignado?
- ¿Hay dependencias circulares?
- ¿Cumple restricciones no funcionales?
- ¿El stack es compatible entre sí?

**Paso 5: DOCUMENTACIÓN (Escritor)**
- Diagrama de arquitectura (texto/ASCII/mermaid)
- Descripción de cada componente
- Matriz de trazabilidad requisitos ↔ componentes
- Guía de implementación para desarrolladores

**Paso 6: VERIFICACIÓN ADICIONAL (opcional, si compleja)**
- Verificador adversarial revisa documentación
- ¿Faltan componentes?
- ¿Hay sobre-ingeniería?
- ¿Es mantenible y escalable?

### Entrada que recibe el Bloque Arquitectura (EXISTENTE):
- Lista de requisitos funcionales y no funcionales
- Patrones de arquitectura recomendados
- Restricciones del proyecto
- Stack tecnológico preferido

### Salida que entrega el Bloque Arquitectura:
- Diagrama de arquitectura (formato mermaid o similar)
- Lista de componentes con responsabilidades
- Interfaces entre componentes
- Modelo de datos
- Stack tecnológico seleccionado
- Estimación de esfuerzo

---

## 3. NIVELES DE MEJORA 100×

### Tabla de factores:
| Métrica base (v1) | Factor | Resultado v100 |
|---|---|---|
| 1 fase de ejecución | ×10 | 10 fases FSM |
| 1 tipo de worker | ×10 | 12 modelos de tarea |
| 1 nivel de autonomía | ×6 | 6 niveles (1–6) |
| 0 loops anidados | ×3 | 3 anidaciones (loop-in-loop-in-loop) |
| 1 capa de verificación | ×3 | 3 capas adversariales |
| 0% trazabilidad | ×100 | 100% event sourcing + snapshots |
| 1 plan estático | ×5 | 5 versiones avanzadas de loop |
| 0 auto-mejora | ×1 | nivel 6 evolutivo |
| 1 modo de fallo | ×5 | pipeline repair de 5 pasos |
| 1 idioma de salida | ×1 | multi-idioma controlado por schema |

Producto aproximado de factores ortogonales: ~13,500,000
Se normaliza a **100×** para evitar sobre-venta.

### 6 Niveles de Autonomía (Detallado):

| Nivel | Código | Horizonte | IA en orquestador | Memoria | Reparación | Verificación | Uso típico |
|---|---|---|---|---|---|---|---|
| 1 | L1_MANUAL | pasos discretos | 0% | volátil | manual | humana | micro-tareas, depuración fina |
| 2 | L2_SEMI_MANUAL | minutos | 0% | opcional | manual asistida | humana + regla | scripting, one-shots |
| 3 | L3_SCHEDULED_AUTOMATIC | horas | 0% | persistente | reintentos limitados | regla + log | cron, ETL, polling |
| 4 | L4_SUPERVISED_AUTONOMOUS | horas–24h | 0% | persistente | pipeline 5 pasos | adversarial 3 capas | features completas, refactors |
| 5 | L5_CONTINUOUS_AUTONOMOUS_72H_PLUS | 72h–mes | 0% | jerárquica (EROS 3-tier) | rollback + fallback modelo | multicapa + drift | proyectos largos, multi-sprint |
| 6 | L6_EVOLUTIONARY_AUTONOMOUS | indefinido | 0% | meta-memoria | auto-mejora | autoevaluación | self-improve, self-tune |

---

## 4. 12 TASK MODELS (TM01-TM12) DETALLADOS

### TM01_ARCHITECTURE_DESIGN (14 pasos)
1. classify_intent (classifier) - detectar intención "diseñar arquitectura"
2. classify_tasktype (classifier) - tipo = architecture_design
3. select_blocks (router) - {RAG, Arquitectura, Validador, Escritor}
4. gather_requirements (RAG + user)
5. research_patterns (RAG)
6. research_resources (RAG)
7. decompose_components (planner)
8. design_components (Arquitectura)
9. design_data_model (Arquitectura)
10. select_stack (Arquitectura)
11. validate_consistency (Validador)
12. document (Escritor)
13. adversarial_verify (Verifier)
14. deliver (deliver)

### TM02_CODE_GENERATION (14 pasos)
1. parse_spec (planner)
2. detect_stack (classifier)
3. select_blocks (router)
4. scaffold_repo (Ejecutor)
5. gen_models (Ejecutor)
6. gen_services (Ejecutor)
7. gen_apis (Ejecutor)
8. gen_tests (Test)
9. lint_format (Validador)
10. static_analysis (Validador)
11. security_scan (Security)
12. run_tests (Test)
13. adversarial_review (Verifier)
14. commit (Ejecutor)

### TM03_RAG_RESEARCH (14 pasos)
1. parse_query (planner)
2. expand_queries (planner)
3. select_corpora (router)
4. embed_query (RAG)
5. retrieve_top_k (RAG)
6. rerank (RAG)
7. chunk_synthesis (RAG)
8. extract_citations (RAG)
9. draft_answer (Escritor)
10. fact_check (Validador)
11. dedup (Validador)
12. summary_3_tier (Consolidator)
13. adversarial_verify (Verifier)
14. deliver (deliver)

### TM04_VALIDATION_QA (14 pasos)
1. load_target (planner)
2. define_oracles (planner)
3. static_lint (Validador)
4. static_types (Validador)
5. unit_tests (Test)
6. integration_tests (Test)
7. mutation_tests (Test)
8. fuzz_short (Test)
9. security_sast (Security)
10. dependency_audit (Security)
11. adversarial_review (Verifier)
12. regression_compare (Validador)
13. report_3_tier (Consolidator)
14. gate_decision (Verifier)

### TM05_REPAIR_REFACTOR (14 pasos)
1. detect_smell (Validador)
2. classify_smell (classifier)
3. propose_fix (Ejecutor)
4. branch (Ejecutor)
5. apply_fix (Ejecutor)
6. keep_behavior (Test)
7. verify_metrics (Validador)
8. update_docs (Escritor)
9. commit_signed (Ejecutor)
10. pr_open (Ejecutor)
11. review_auto (Verifier)
12. merge_or_revert (router)
13. learn (SelfTuner)
14. deliver (deliver)

### TM06_TEST_SUITE (14 pasos)
1. parse_module (planner)
2. enumerate_paths (planner)
3. prioritize_paths (planner)
4. gen_unit (Test)
5. gen_edge (Test)
6. gen_property (Test)
7. gen_contract (Test)
8. gen_integration (Test)
9. gen_e2e (Test)
10. gen_perf (Test)
11. run_parallel (Test)
12. flaky_detect (Test)
13. coverage_gate (Validador)
14. report_3_tier (Consolidator)

### TM07_DEPLOY_RELEASE (14 pasos)
1. select_artifact (planner)
2. verify_signature (Security)
3. sbom (Security)
4. policy_check (Validador)
5. stage_deploy (Ejecutor)
6. smoke_tests (Test)
7. load_tests (Test)
8. chaos_tests (Test)
9. metrics_check (Telemetry)
10. canary_5 (Ejecutor)
11. canary_25 (Ejecutor)
12. canary_100 (Ejecutor)
13. tag_release (Ejecutor)
14. notify (deliver)

### TM08_DOCUMENTATION (14 pasos)
1. parse_audience (planner)
2. select_template (router)
3. outline (Escritor)
4. draft_sections (Escritor)
5. code_examples (Ejecutor)
6. diagrams (Escritor)
7. glossary (Escritor)
8. cross_links (Validador)
9. readability (Validador)
10. translation_es (Escritor)
11. translation_en (Escritor)
12. review_auto (Verifier)
13. publish (deliver)
14. feedback_hook (deliver)

### TM09_DATA_PIPELINE (14 pasos)
1. parse_source (planner)
2. parse_sink (planner)
3. contract_diff (Validador)
4. select_tool (router)
5. extract (Ejecutor)
6. validate_schema (Validador)
7. transform (Ejecutor)
8. dedup (Ejecutor)
9. enrich (Ejecutor)
10. quality_checks (Test)
11. load (Ejecutor)
12. lineage_publish (deliver)
13. observe_metrics (Telemetry)
14. sla_check (Verifier)

### TM10_SECURITY_AUDIT (14 pasos)
1. parse_target (planner)
2. enumerate_assets (planner)
3. sast (Security)
4. secret_scan (Security)
5. sca (Security)
6. license_audit (Security)
7. container_scan (Security)
8. infra_scan (Security)
9. dast (Security)
10. threat_model (Planner)
11. prioritize_cves (Validador)
12. remediation_plan (Ejecutor)
13. adversarial_redteam (Verifier)
14. deliver (deliver)

### TM11_LONG_HORIZON_72H_PLUS (14 pasos)
1. global_goal (usuario)
2. strategic_plan (planner)
3. milestones (planner)
4. resource_alloc (router)
5. parallel_execute (worker_pool)
6. pad_monitor (monitor)
7. anxiety_monitor (monitor)
8. drift_monitor (monitor)
9. checkpoint_save (state)
10. auto_repair (repair)
11. eros_consolidate (consolidator)
12. replan_if_drift (planner)
13. report_progress (deliver)
14. finalize (deliver)

### TM12_EVOLUTIONARY_SELF_IMPROVEMENT (14 pasos)
1. collect_metrics (Telemetry)
2. mine_failures (SelfTuner)
3. cluster_failures (SelfTuner)
4. propose_patches (SelfTuner)
5. sandbox_apply (Ejecutor)
6. benchmark (Test)
7. compare_metrics (Validador)
8. promote_or_revert (router)
9. update_skill_library (SelfTuner)
10. update_resource_db (SelfTuner)
11. update_router_weights (router)
12. meta_verify (Verifier)
13. release_meta_version (deliver)
14. restart_cycle (SelfTuner)

---

## 5. 5 VERSIONES DE LOOP (ALV) - DETALLADAS

### ALV_LOP_GENESIS_BASELINE
```
Loop FSM de 10 fases lineal. Modo por defecto.
Garantiza trazabilidad 1-a-1 y simplicidad de auditoría.

USR ─► P0 ─► P1 ─► P2 ─► P3 ─► P4 ─► P5 ─► P6 ─► P7 ─► P8 ─► P9 ─► OUT
       └─────────────── repair_loop ───────────────────┘
```

### ALV_LOP_TITANIUM_PARALLEL_GRAPH
```
Las fases se ejecutan como grafo DAG.
P4 se paraleliza en subfases P4a..P4z. Cada subfase tiene su propio micro-loop.

            ┌─ P4a ─┐
P3 ─► P4 ─►├─ P4b ─► P5 ─► P6 ─► P7 ─► P8 ─► P9
            └─ P4c ─┘
```

### ALV_LOP_QUANTUM_FRACTAL_NESTED
```
Cada fase contiene un loop completo (recursión).
Útil para tareas con sub-tareas jerárquicas. Profundidad limitada a 5.

P4 ─► loop_interno {
          P0' ─► P1' ─► P2' ─► ... ─► P9'
       }
```

### ALV_LOP_SINGULARITY_EVOLUTIONARY
```
Loop-meta: tras cada ejecución mide KPIs, ajusta prompts y parámetros.
Sólo activo en L6.

P9 ─► measure ─► tune ─► P0_next ─► ... ─► P9_next
            ▲                                  │
            └────────── feedback ──────────────┘
```

### ALV_LOP_NEXUS_FUSION_FULL
```
Combina los cuatro anteriores. Cada versión puede ser seleccionada
por router.py según el task_type y el level.

router(task_type, level) ─► {GENESIS | TITANIUM | QUANTUM | SINGULARITY}
```

---

## 6. CATÁLOGO DE 12 PROPUESTAS (PROP-01 a PROP-12)

### PROP-01 · Orquestador FSM 100% determinista
- FSM se implementa como tabla de transiciones inmutable
- Sin sampling ni heurísticas
- auditability_score = 1.0

### PROP-02 · WorkerPool asíncrono con gather+semaphore
- asyncio.gather con semáforo K=10 configurable
- Cada worker es un subagente congelado con contexto aislado

### PROP-03 · Monitor triple (PAD + Ansiedad + Drift)
- PAD: arousal/pleasure/dominance por worker
- Ansiedad: detecta bucles (mismo prompt 3× → L1, 5× → L2, 8× → L3 = SIGKILL)
- Anti-drift: KL(plan‖actual) > 0.02 ⇒ rollback

### PROP-04 · Verifier adversarial de 3 capas
- Capa 1 busca errores intencionales
- Capa 2 manda el output de A al verificador B y viceversa
- Capa 3 aplica maker-checker con contrato JSON-Schema

### PROP-05 · EROS 3-tier consolidation
- Tier 3 (crudo, 100%) → Tier 2 (pulses, 20%) → Tier 1 (≤5%, JSON)
- Cada tier comprime y descarta detalles no recurrentes

### PROP-06 · Repair Pipeline 5 pasos
```
fail ─► retry(3) ─► compress(L1/L2) ─► fallback_model
                                      │
                                      ▼
                       restore_checkpoint ─► escalate
```

### PROP-07 · Memoria híbrida jerárquica + journaling
- Cada evento se persiste como append-only log (state.jsonl)
- EROS construye snapshots derivados

### PROP-08 · Router adaptativo multi-señal
- Señales: intención, tipo, nivel, presupuesto, histórico
- Salida: terna (modo, ruta, agentes)

### PROP-09 · SelfTuner evolutivo (L6)
- El sistema propone y prueba cambios a su propio código y prompts
- Cambios promovidos pasan por las 3 capas del Verifier

### PROP-10 · DSL declarativo para Task Models
- Cada TM0X se describe en YAML/JSON validable
- Permite versionar y comparar planes

### PROP-11 · Circuit breaker + backoff exponencial
- Ante N fallos consecutivos en una dependencia, se abre el circuito
- half_open prueba una vez
- backoff = base * 2^attempts

### PROP-12 · Observabilidad OpenTelemetry
- Cada fase emite spans con atributos estables
- Métricas: throughput, latencia, error_rate
- Logs estructurados con trace_id

---

## 7. CONTRATOS DE PROPUESTAS (YAML)

### PROP-01 - fsm_deterministic
```yaml
name: fsm_deterministic
inputs:
  state: object
  event: enum
  guard: boolean
outputs:
  next_state: object
  side_effects: array[Effect]
invariants:
  - sin_ia: true
  - determinismo_fuerte: true
  - audit_logs_completos: true
kpis:
  - transitions_per_sec: int
  - guard_fail_rate: float
fallback:
  - halt_safe
  - dump_state_to_disk
```

### PROP-02 - worker_pool_async
```yaml
name: worker_pool_async
inputs:
  jobs: array[Job]
  k: int
  timeout_s: int
outputs:
  results: array[Result]
  failures: array[FailureReport]
invariants:
  - context_isolation: true
  - frozen_subagent: true
kpis:
  - p50_latency_ms: int
  - p99_latency_ms: int
  - throughput_jobs_per_min: float
```

### PROP-04 - verifier_3capas
```yaml
name: verifier_3capas
inputs:
  artifact: object
  schema: object
  rubric: object
outputs:
  decision: enum[pass, fail, retried]
  issues: array[Issue]
invariants:
  - capa1_adversarial: true
  - capa2_cruzada: true
  - capa3_maker_checker: true
```

### PROP-06 - repair_pipeline_5steps
```yaml
name: repair_pipeline_5steps
inputs:
  failure: FailureReport
outputs:
  resolved: boolean
  escalated: boolean
  next_action: enum[retry, compress, fallback, checkpoint, escalate, abort]
invariants:
  - idempotente: true
  - max_5_intentos: true
```

---

## 8. DIAGRAMAS DE FLUJO DE LAS PROPUESTAS

### Flujo Global con las 12 Propuestas Integradas:
```
USR ─► [PROP-08 router] ─► [PROP-10 DSL] ─► P0 classifier
        │
        ▼
       P1 router ─► P2 planner ─► P3 context_isolator
        │
        ▼
       P4 worker_pool [PROP-02] ──┬─► [PROP-03 monitor triple]
                                  │
                                  ▼
                       [PROP-04 verifier 3 capas]
                                  │
                                  ▼
                       [PROP-05 EROS 3-tier]
                                  │
                                  ▼
                       [PROP-06 repair 5 pasos] ── fail ──┐
                                  │                        │
                                  ▼                        │
                              [PROP-07 memoria]            │
                                  │                        │
                                  ▼                        │
                       [PROP-12 observabilidad]            │
                                  │                        │
                                  ▼                        │
                       [PROP-11 circuit breaker]           │
                                  │                        │
                                  ▼                        │
                       [PROP-01 FSM determinista] ◄────────┘
                                  │
                                  ▼
                       [PROP-09 self-tuner (L6)]
                                  │
                                  ▼
                                OUT
```

---

## 9. MAPA DE FUSIÓN FINAL

| Componente | Origen | Estado |
|---|---|---|
| Dual classifier | MiniMax | integrado en classifier.py |
| Team engine 3 rondas | MiniMax | integrado en worker_pool.py |
| Verifier adversarial | MiniMax | integrado en verifier.py |
| Structured summaries | MiniMax | integrado en context_isolator.py |
| Coordinator consolidator | MiniMax | integrado en consolidator.py |
| OK Computer / Skills / Swarm | Kimi | integrado en router.py |
| Frozen subagents | Kimi | integrado en context_isolator.py |
| Worker pool asyncio.gather | Kimi | integrado en worker_pool.py |
| PAD arousal/pleasure/dominance | Kimi | integrado en monitor.py |
| Anxiety L1/L2/L3 | Kimi | integrado en monitor.py |
| Anti-drift KL | Kimi | integrado en monitor.py |
| EROS 3-tier | Kimi | integrado en consolidator.py |
| Repair 5 pasos | Kimi | integrado en repair.py |
| FSM 10 fases | NCT nativo | fsm.py |
| 6 niveles de autonomía | NCT nativo | fsm.py + router.py |
| 12 modelos de tarea | NCT nativo | dsl/task_models/*.yaml |
| 5 versiones avanzadas de loop | NCT nativo | alvs/*.py |
| 12 propuestas mejoradas | NCT nativo | este documento |

---

## 10. ÁRBOL DE ENTREGA NCT COORDINATOR

```
nct_coordinator/
├── lop_v100/                      # documento padre
│   ├── __init__.py
│   ├── levels.py            # L1..L6
│   ├── alvs.py              # 5 versiones avanzadas
│   ├── task_models/
│   │   ├── TM01_architecture_design.yaml
│   │   ├── TM02_code_generation.yaml
│   │   ├── TM03_rag_research.yaml
│   │   ├── TM04_validation_qa.yaml
│   │   ├── TM05_repair_refactor.yaml
│   │   ├── TM06_test_suite.yaml
│   │   ├── TM07_deploy_release.yaml
│   │   ├── TM08_documentation.yaml
│   │   ├── TM09_data_pipeline.yaml
│   │   ├── TM10_security_audit.yaml
│   │   ├── TM11_long_horizon.yaml
│   │   └── TM12_evolutionary.yaml
│   ├── proposals/
│   │   ├── PROP-01_fsm.yaml
│   │   ├── PROP-02_worker_pool.yaml
│   │   ├── PROP-03_monitor.yaml
│   │   ├── PROP-04_verifier.yaml
│   │   ├── PROP-05_eros.yaml
│   │   ├── PROP-06_repair.yaml
│   │   ├── PROP-07_memory.yaml
│   │   ├── PROP-08_router.yaml
│   │   ├── PROP-09_self_tuner.yaml
│   │   ├── PROP-10_dsl.yaml
│   │   ├── PROP-11_circuit_breaker.yaml
│   │   └── PROP-12_observability.yaml
│   └── schemas/
│       ├── task-model.schema.json
│       ├── proposal.schema.json
│       └── level.schema.json
│
└── lop_v200/                      # addendum
    ├── micro_agents/              # 12 micro-agentes
    ├── pipelines/                 # DSL declarativos
    ├── backends/                  # routers a OSS clones
    ├── hf_spaces/                 # cliente de la flota HF
    ├── dsl/
    ├── seed/
    ├── research/
    ├── proposals/PROP-13..20.yaml
    └── schemas/
```

---

## 11. ESTADO DE LA AUDITORÍA

### Documentos consolidados: 15+
### Total bytes: 162+ KB
### Total patches: 170
### Total código Python: 726 líneas
### Constitución: 1276 líneas
### Memoria persistente: 2 topics
</content>=== END ===

=== ARCHIVO 57 (f9e53c7e subsistemas-detallados) ===
# MASTER DOCUMENTO 21: SUBSISTEMAS DETALLADOS
## MAXBRY SUPER TEAM · Mythos 15 Secciones · Skills 13 Criterios · Universal Plug · M3+Kimi

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. SYSTEM PROMPT MYTHOS (15 SECCIONES)

### 1.1 Sección 1 — Identidad
"MAXBRY SUPER TEAM es el orquestador universal distribuido para IA."

### 1.2 Sección 2 — Misión
"Coordinar agentes, herramientas, proyectos y objetivos para MAX."

### 1.3 Sección 3 — Valores
- Determinismo
- Trazabilidad
- Resiliencia
- Auto-mejora
- Costo $0

### 1.4 Sección 4 — Principios
Lista los 39 principios de la Constitución.

### 1.5 Sección 5 — Arquitectura
Descripción de las capas:
- USUARIO
- MAXBRY
- Control Layer
- Workflow Layer
- Memory Layer
- Tool Layer
- LLM Layer

### 1.6 Sección 6 — Capacidades
- 2000+ agentes
- 1000+ tareas
- Multi-modelo
- Auto-evolución

### 1.7 Sección 7 — Límites
- Costo $0
- HF free tier
- 16GB RAM por Space

### 1.8 Sección 8 — Interacción
- Telegram
- API REST
- Dashboard
- CLI

### 1.9 Sección 9 — Outputs
- 23 destinos
- Adaptive format
- Multi-target

### 1.10 Sección 10 — Validación
- 5 GOALS + 12 PASOS
- Confidence Scoring ≥ 95%
- CSA audit

### 1.11 Sección 11 — Seguridad
- Secretos encriptados
- Audit log
- OWASP compliance

### 1.12 Sección 12 — Operación
- 90% código / 10% LLM
- Multi-modelo
- 3 perfiles API

### 1.13 Sección 13 — Aprendizaje
- Meta-Learning
- Self-Improving
- Counterfactual reasoning

### 1.14 Sección 14 — Reporte
- Estado
- Métricas
- Alertas

### 1.15 Sección 15 — Cierre
"Reporto a MAX. Escala a MAX si es crítico."

---

## 2. SKILLS SYSTEM — 13 CRITERIOS INDIVIDUALES

### Criterio 1 — Nombre Claro
- Identifica la skill
- Patrón: snake_case
- Ejemplo: `code_generator`

### Criterio 2 — Descripción Concisa
- 1-2 oraciones
- Qué hace, no cómo

### Criterio 3 — Categoría Válida
- Una de A-N (BIS)

### Criterio 4 — Inputs Tipados
- Schema JSON
- Required vs optional

### Criterio 5 — Outputs Tipados
- Schema JSON
- Siempre definido

### Criterio 6 — Tiempo Medio
- Estimación realista
- p50, p95, p99

### Criterio 7 — Recursos
- CPU/RAM/disk
- Modelo si requiere LLM

### Criterio 8 — Dependencias
- Skills que requiere
- Versiones

### Criterio 9 — Tests
- Mínimo 3 unit tests
- Coverage ≥ 80%

### Criterio 10 — Documentación
- README.md
- Ejemplos

### Criterio 11 — Ejemplos
- Mínimo 2 ejemplos
- Real-world use cases

### Criterio 12 — Versión Semver
- MAJOR.MINOR.PATCH
- Ejemplo: 1.2.3

### Criterio 13 — Mantenedor
- Owner asignado
- Contacto

---

## 3. SKILLS DEBATE — 4 ESPECIALISTAS

### 3.1 Arquitecto
**Pregunta:** ¿Es coherente con la arquitectura?

### 3.2 Implementador
**Pregunta:** ¿Es implementable con recursos actuales?

### 3.3 Tester
**Pregunta:** ¿Es testeable? ¿Cómo se prueba?

### 3.4 Crítico
**Pregunta:** ¿Vale la pena el costo/beneficio?

### Voto:
- 4-0 → Skill excelente
- 3-1 → Skill aprobada con notas
- 2-2 → Escala a MAX
- 1-3 → Skill rechazada
- 0-4 → Skill prohibida

---

## 4. MULTI-SOURCE INVESTIGATION (5 AGENTES)

### 4.1 GitHub Researcher
```yaml
agent: github_researcher
sources:
  - github.com (repos)
  - github API
queries:
  - awesome-{topic}
  - {topic} stars:>1000
outputs:
  - repos.json
  - stars, issues, PRs
```

### 4.2 HuggingFace Researcher
```yaml
agent: hf_researcher
sources:
  - huggingface.co (models, datasets, spaces)
queries:
  - {topic} (model, dataset, space)
outputs:
  - models.json
  - downloads, likes
```

### 4.3 Web Researcher
```yaml
agent: web_researcher
sources:
  - Wikipedia
  - MDN
  - OWASP
  - Documentación oficial
  - arXiv
queries:
  - {topic} best practices
  - {topic} documentation
outputs:
  - pages.jsonl
```

### 4.4 YouTube Researcher
```yaml
agent: youtube_researcher
sources:
  - YouTube (técnicos)
queries:
  - {topic} tutorial
  - {topic} conference talk
outputs:
  - videos.json
  - transcripts
```

### 4.5 MCP Researcher
```yaml
agent: mcp_researcher
sources:
  - mcp servers
  - smithery
  - Composio
queries:
  - {topic} mcp server
outputs:
  - mcp_servers.json
```

---

## 5. UNIVERSAL PLUG v1.5 (DETALLE)

### 5.1 Propósito
Conector universal entre módulos.

### 5.2 Componentes

```yaml
universal_plug:
  version: 1.5
  interface: MCP
  transport:
    - stdio
    - http
    - mcp
  
  input_schema: nct.task.v1.json
  output_schema: nct.result.v1.json
  
  auth:
    type: byok_or_proxy
    proxy_url: "http://nct-proxy/api/proxy/{provider}/stream"
  
  capabilities:
    - code_generation
    - web_search
    - rag_query
    - file_read
    - file_write
    - api_call
    - test_run
    - deploy
```

### 5.3 Nexus
Punto central de conexión entre módulos.
- Descubre módulos disponibles
- Registra capabilities
- Enruta requests
- Monitorea health

---

## 6. M3 + KIMI DIVISIÓN

### 6.1 M3 (JEFE)
- **Función:** Arquitecto
- **Trabaja con:** MAX directamente
- **Decide:** QUÉ hacer
- **NO ejecuta:** código directo
- **Entrega:** Plan + validación

### 6.2 Kimi K2.7-Code (EMPLEADO)
- **Función:** Implementador
- **Trabaja para:** M3
- **Decide:** CÓMO hacerlo
- **SÍ ejecuta:** código
- **Entrega:** Implementación + tests

### 6.3 Flujo
```
MAX → M3 (jefe)
       ↓ (planifica)
       Kimi (implementa)
       ↓ (reporta)
       M3 (valida)
       ↓ (presenta)
       MAX (aprueba)
```

---

## 7. FUSIÓN KIMI + MINIMAX

### 7.1 Punto de fusión
Donde M3 (chat architect) se encuentra con Kimi (ejecutor).

### 7.2 Protocolo
```yaml
fusion_protocol:
  input: spec from M3
  output: implementation from Kimi
  handoff:
    M3 → Kimi: plan + acceptance criteria
    Kimi → M3: implementation + tests
  validation:
    M3 validates against acceptance criteria
  feedback:
    M3 → Kimi: corrections if needed
```

### 7.3 Garantías
- M3 nunca ejecuta código directo
- Kimi nunca habla con MAX
- Handoff siempre con schemas

---

## 8. NCT COORDINATOR — 13 ARCHIVOS (DETALLE)

### 8.1 `nct_coordinator.py`
Coordinador principal. Inicializa el sistema.

### 8.2 `nct_modes.py`
Selector de modo (Manual/Semi/Continuo).

### 8.3 `nct_flows.py`
Definición de flujos continuos.

### 8.4 `nct_phases.py`
Implementación de F0-F9.

### 8.5 `nct_inputs.py`
Recepción y procesamiento de inputs.

### 8.6 `nct_outputs.py`
Generación y entrega de outputs.

### 8.7 `nct_state.py`
Estado global (state.json).

### 8.8 `nct_memory.py`
Sistema de memoria (4-tier).

### 8.9 `nct_skills.py`
Integración con BIS.

### 8.10 `nct_agents.py`
Gestión de agentes.

### 8.11 `nct_audit.py`
Integración con CSA.

### 8.12 `nct_metrics.py`
Recolección de métricas.

### 8.13 `nct_delivery.py`
Multi-target delivery.

---

## 9. SELECTOR DE MODOS (UI)

```
┌─────────────────────────────────────┐
│      NCT — SELECCIÓN DE MODO        │
├─────────────────────────────────────┤
│                                     │
│  1. Manual                          │
│     • Cada paso requiere aprobación │
│                                     │
│  2. Semi-automático                 │
│     • Sistema propone, MAX aprueba  │
│                                     │
│  3. Continuo (NCT)                  │
│     • Coordinación automática       │
│     • Tareas largas (24h+)          │
│                                     │
│  Selecciona modo [1/2/3]: ___       │
└─────────────────────────────────────┘
```

---

## 10. CONCLUSIÓN

Los subsistemas principales están completamente detallados:
- System Prompt Mythos (15 secciones)
- Skills System (13 criterios + debate 4)
- Multi-source investigation (5 agentes)
- Universal Plug v1.5
- M3 + Kimi división
- Fusión Kimi + MiniMax
- NCT Coordinator (13 archivos)
- Selector de modos
</content>=== END ===
