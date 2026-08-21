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
- 16 API keys