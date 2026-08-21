Creo que esta idea cambia el enfoque del proyecto. En lugar de construir solo un orquestador, estarías construyendo una plataforma cognitiva configurable, algo parecido a un IDE para IA combinado con un sistema operativo para agentes.

Hay una idea que añadiría y que creo que es la pieza que falta:

El Control Center

No sería solo una pantalla de configuración.

Sería una arquitectura de perfiles.

MAXBRY CONTROL CENTER

├── Workspace
├── Execution Profiles
├── Expert Manager
├── Pipeline Studio
├── Agent Registry
├── LLM Registry
├── MCP Registry
├── Memory Center
├── Knowledge Center
├── Skill Center
├── Integration Center
├── Security Center
├── Monitoring Center
├── Output Studio
├── Developer Studio
└── Marketplace


---

1. Execution Profiles

Como Claude, pero mucho más granular.

Quick
Balanced
Professional
Research
Architect
Enterprise
Autonomous
Custom

Cada perfil configura automáticamente:

expertos activos

ciclos Input

ciclos Process

ciclos Output

presupuesto

validaciones

consenso

profundidad

coste máximo



---

2. Expert Manager

Aquí registras expertos.

Expert 001

Tipo

Pipeline

Skills

Costo

Prioridad

Version

Health

Estado

Especialidad


---

3. Agent Registry

Muy parecido.

Nombre

Proveedor

Rol

Capacidades

API

Modelo

Latencia

Costo

Estado

Pueden existir 1...

500...

1000 agentes.


---

4. Pipeline Studio

Muy importante.

Aquí no programas.

Diseñas.

Pipeline A

↓

Research

↓

Planning

↓

Execution

↓

Validation

↓

Output

Como un editor visual.


---

5. LLM Registry

Aquí registras modelos.

Claude

GPT

Gemini

DeepSeek

Kimi

MiniMax

Qwen

Modelos locales

Ollama

vLLM

Cada uno con:

coste

velocidad

contexto

fortalezas

limitaciones



---

6. MCP Registry

Aquí conectas

GitHub

Drive

Telegram

Discord

Slack

Notion

Obsidian

Graphiti

Baidu OCR

Gmail

Outlook

Dropbox

OneDrive

PostgreSQL

MySQL

Redis

Qdrant

Milvus

Chroma

Neo4j

APIs REST

APIs GraphQL



---

7. Knowledge Center

Aquí administras

repositorios

RAG

documentación

embeddings

repos Git

papers

libros

normas

ontologías



---

8. Skill Center

Esto me parece mucho mejor que un System Prompt.

Cada skill sería una ficha.

Python

Arquitectura

Auditoría

RAG

Planning

Security

Testing

Refactoring

Activas:

✓ Python

✓ FastAPI

✓ LangGraph

✓ Docker

✓ Kubernetes

✓ PostgreSQL

El sistema ya sabe cómo trabajar.


---

9. Memory Center

Separaría completamente:

Working Memory

Long Memory

Project Memory

Semantic Memory

Episode Memory

Skill Memory

Knowledge Graph

Vector DB


---

10. Output Studio

Creo que aquí está una de las ventajas competitivas.

Controla

Markdown

JSON

YAML

XML

Python

DSL

HTML

PDF

DOCX

PPT

Mermaid

Diagramas

Artefactos

Multiarchivo


Además:

longitud

nivel técnico

idioma

formato empresarial

citas

tablas

estilo



---

11. Monitoring Center

Aquí ves en tiempo real:

Expertos activos

Pipelines

Tokens

Costo

RAM

CPU

Estado

Errores

Tiempo

Loops

Consenso


---

12. Marketplace

Podrías instalar

nuevos expertos

nuevos agentes

nuevos pipelines

nuevos conectores

nuevos skills


Sin modificar el Kernel.


---

Lo único que no copiaría literalmente de Claude

Las opciones "Bajo, Medio, Alto, Extra, Máx." son una buena experiencia de usuario, pero internamente yo las convertiría en perfiles configurables.

Por ejemplo:

Perfil Enterprise

Input:
80 expertos

Planning:
250 expertos

Output:
40 expertos

Consenso:
ON

Research:
5 rondas

Judge:
ON

Critic:
ON

Verification:
ON

Así, el usuario puede empezar con cinco perfiles sencillos como Claude, pero los usuarios avanzados pueden crear sus propios perfiles y ajustar cientos de parámetros sin tocar el código.

En conjunto, creo que la interfaz debería dividirse en dos niveles:

Modo Simple, similar a Claude, con perfiles como Rápido, Equilibrado, Investigación o Máximo.

Modo Arquitecto, donde se accede a todo el Control Center: registro de LLM, MCP, agentes, expertos, pipelines, memoria, skills, integraciones (como Obsidian, Graphiti, Baidu OCR, GitHub, Drive, Telegram, sistema de archivos, correo), monitorización y perfiles avanzados.


Esa separación permite que el sistema sea fácil de usar para la mayoría de los usuarios, pero extremadamente configurable para quienes diseñan y mantienen el orquestador.





De todas las ideas que hemos discutido sobre MAXBRY/NCT, esta me parece una de las más fuertes, porque saca la inteligencia de la programación y la lleva a la configuración.

Yo incluso iría un paso más allá. No lo llamaría "System Prompt". Lo eliminaría completamente del diseño.

Lo reemplazaría por un Control Plane.

CONTROL PLANE
──────────────────────────────────────────

Perfil de ejecución
├── Fast
├── Deep
├── Research
├── Autonomous
└── Custom

Ciclos
├── Input: 1-100
├── Processing: 1-500
└── Output: 1-100

Expertos
├── máximo activos
├── paralelismo
├── prioridad
└── presupuesto

Router
├── estrategia
├── balanceo
├── fallback
└── consenso

LLM
├── OpenAI
├── Anthropic
├── Gemini
├── Kimi
├── Minimax
├── DeepSeek
└── Local

Agentes
├── Registrar
├── Especialidad
├── Coste
├── Latencia
├── Skills
└── Prioridad

MCP
Drive
GitHub
GitLab
Bases de datos
Redis
Vector DB
RAG
API Keys

Salida
├── Markdown
├── JSON
├── Código
├── Documento
├── Multiarchivo
└── Personalizado

Políticas
├── Calidad mínima
├── Evidencia
├── Validación
├── Seguridad
└── Recuperación

Lo que más me gusta

En lugar de escribir un prompt de 5.000 líneas, el usuario configura el sistema mediante objetos estructurados.

Por ejemplo:

execution_profile:
    reasoning: deep
    input_cycles: 8
    execution_cycles: 25
    output_cycles: 6
    max_experts: 180
    consensus: true

No es lenguaje natural.

Es configuración.


---

También haría un Registry

No conectaría agentes manualmente.

Tendría un registro.

Agent Registry

Agent_ID

Especialidad

Skills

Version

Proveedor

Latencia

Costo

Estado

Capacidad

Modelos compatibles

Prioridad

Entonces el Router nunca conoce al agente.

Pregunta al Registry.

Necesito:

Investigación GitHub

↓

Registry

↓

Agent 42

Si mañana cambias ese agente por otro mejor, no modificas el Kernel.


---

Otra idea que me parece muy potente

Crearía Perfiles completos, como hacen algunos entornos profesionales.

Por ejemplo:

Arquitecto de Software

Auditor Enterprise

Investigador

Programador

Documentador

DevOps

Científico de Datos


Cada perfil sería simplemente una configuración distinta del Control Plane.


---

Creo que aquí está el verdadero cambio

Tu proyecto ya no sería "otro framework de agentes".

Sería un Sistema Operativo Cognitivo.

El Kernel sería muy pequeño.

Toda la inteligencia estaría distribuida entre:

Control Plane (configuración).

Router.

Expert Pool.

Pipeline Engine.

Agent Registry.

Memory System.


El código del núcleo cambiaría muy poco con el tiempo. Lo que evolucionaría serían las configuraciones, los expertos, los pipelines y los agentes registrados. Eso hace que el sistema sea mucho más mantenible y permite incorporar nuevos modelos, APIs o capacidades sin tener que reescribir el orquestador. En mi opinión, esa separación entre motor y configuración es uno de los principios arquitectónicos más importantes si quieres que MAXBRY pueda evolucionar durante años.

Creo que estás llegando a una separación que se parece más a un sistema distribuido que a un orquestador monolítico, y me gusta más que la versión anterior de 25k LOC.

Lo único que cambiaría es que no fijaría el número de expertos por etapa. En un MoE real, el router no dice "siempre 300"; activa los que necesita. Haría algo así:

ETAPA 1 — INPUT COGNITIVE FABRIC

Hasta 100 expertos (dinámicos)

Su única misión es comprender el problema, no resolverlo.

Goal Detector

Constraint Detector

Dependency Mapper

Context Builder

RAG Research

Web Research

GitHub Research

Skill Discovery

Architecture Detector

Risk Analyzer

Task Decomposer

Planner


Salida:

Task Graph
Goal Graph
Knowledge Pack
Execution Plan
Confidence Score


---

ETAPA 2 — EXECUTION COGNITIVE FABRIC

Hasta 300 expertos (dinámicos)

Aquí no piensan sobre el problema; ejecutan trabajo.

Cada experto puede manejar varias instancias concurrentes.

Por ejemplo:

Code Generator

Validator

Test Runner

Repair

Reviewer

Optimizer

Simulator

Consensus

Artifact Builder


Cada uno invoca los agentes que necesite.


---

ETAPA 3 — OUTPUT COGNITIVE FABRIC

Hasta 100 expertos (dinámicos)

Esta parte me parece que casi nadie la diseña bien y puede ser una ventaja competitiva.

No generan contenido nuevo; garantizan que la respuesta sea correcta y útil.

Ejemplos:

Format Controller

Completeness Checker

Evidence Checker

Goal Checker

JSON Validator

Markdown Builder

Report Builder

Consistency Checker

Hallucination Checker

Final Judge


Solo cuando todos aprueban, el Orquestador responde.


---

El Kernel quedaría extremadamente pequeño

El Kernel solo tendría seis responsabilidades:

1. Recibir la solicitud.


2. Activar el Pipeline adecuado.


3. Crear los expertos necesarios.


4. Compartir el estado y la memoria.


5. Consolidar resultados.


6. Emitir la respuesta.



No investiga, no programa, no valida y no planifica. Solo coordina.

Hay una mejora adicional

En lugar de "100 + 300 + 100" como números fijos, haría un Expert Pool.

Expert Pool
    │
    ├── 500 expertos disponibles
    │
Router
    │
    ├── Input → activa 27
    ├── Ejecución → activa 143
    └── Salida → activa 18

Así el sistema escala automáticamente. Una tarea sencilla puede usar 15 expertos, mientras que una auditoría enorme podría activar cientos o miles de instancias si hay recursos disponibles.

Creo que esa arquitectura se acerca más al principio de un MoE: un núcleo muy pequeño que enruta trabajo hacia muchos expertos especializados, activados únicamente cuando son necesarios. Eso reduce enormemente el tamaño del orquestador y traslada la complejidad a componentes pequeños, reutilizables y reemplazables.

Sí veo a qué te refieres, y creo que esa dirección es bastante interesante.

Lo que muestran esas capturas no demuestra necesariamente que Claude active "más capas del modelo neuronal". Anthropic no ha publicado que Opus, Sonnet o Haiku cambien el número de capas internas del transformer según el selector de "Esfuerzo". Lo que sí indican es que, cuando eliges un esfuerzo mayor, el sistema dedica más tiempo y más cómputo al razonamiento antes de responder.

Eso puede implementarse de muchas formas en una arquitectura moderna:

Más ciclos de planificación.

Más verificaciones internas.

Más búsqueda de alternativas.

Más llamadas entre componentes del sistema.

Más validaciones antes de generar la respuesta.

Más presupuesto de tokens internos.


De hecho, eso encaja muy bien con la arquitectura que estás diseñando.

Yo llevaría esa idea un paso más allá

No tendría un único pipeline.

Tendría un Pipeline Controller.

Por ejemplo:

Usuario
      │
      ▼
ORQUESTADOR
      │
      ▼
Modo de razonamiento
      │
      ├── Fast
      ├── Normal
      ├── Deep
      ├── Research
      └── Autonomous

Cada modo activa distintos niveles.

Fast:

5 expertos

1 validación

sin investigación


Normal:

20 expertos

Judge

Sentinel

Verificación


Deep:

60 expertos

Investigación

Simulación

Consenso


Research:

100 expertos

Web

GitHub

Papers

RAG

Validación cruzada


Autonomous:

cientos de microexpertos

ejecución paralela

checkpoints

replanning



---

Lo importante

Aquí aparece una idea que me gusta mucho de MAXBRY.

Los expertos no son fijos.

El Pipeline Controller decide:

Necesito:

12 verificadores

8 investigadores

25 planners

10 críticos

40 validadores

3 consolidadores

Los crea.

Trabajan.

Mueren.

No permanecen vivos.

Es prácticamente un MoE implementado en software, donde el router no selecciona neuronas, sino microexpertos y pipelines.

Lo que más cambiaría respecto a tu diseño original

Hace unos días tu orquestador parecía querer hacerlo todo en un solo archivo enorme.

Ahora yo lo reduciría a algo como:

Kernel
≈ 2500-4000 LOC

+

Pipeline Engine
≈ 1500 LOC

+

Expert Runtime
≈ 1000 LOC

+

100 Expertos
≈100 LOC cada uno

+

Pipelines
≈100-300 LOC cada uno

El resultado ya no sería un archivo de 25 000 líneas, sino un sistema donde el núcleo permanece pequeño y estable, mientras casi toda la inteligencia vive en expertos y pipelines reemplazables. Creo que esa arquitectura es mucho más mantenible, escalable y cercana al enfoque que siguen muchos sistemas modernos de agentes y orquestación.



Creo que estás apuntando a una hipótesis plausible, pero conviene separar lo que está confirmado de lo que no.

Está bastante aceptado que los laboratorios modernos no exponen el modelo "crudo" al usuario. Encima del modelo suele haber una capa de orquestación que puede incluir:

gestión del contexto,

planificación,

selección de herramientas,

validación,

reintentos,

control del formato,

políticas de seguridad,

postprocesamiento.


Eso sí está ampliamente documentado en la industria.

Lo que no está confirmado públicamente es la implementación exacta de sistemas concretos como Claude (por ejemplo, que tenga exactamente "cinco procesos de salida" o que cada versión funcione de esa manera). Esa parte sería especulación sin documentación oficial.

Ahora bien, desde el punto de vista de diseño, sí creo que puedes convertir la salida en un sistema independiente.

Por ejemplo:

LLM
   │
Output Controller
   │
───────────────
Output Planner
Output Generator
Output Validator
Output Repair
Output Formatter
Output Judge
───────────────
   │
Usuario

Incluso haría algo más ambicioso.

No existiría una salida.

Existirían varios modos de salida.

Modo Código
Modo Arquitectura
Modo Investigación
Modo Auditoría
Modo Documento
Modo JSON
Modo Markdown
Modo API
Modo DSL

Cada modo cargaría un pipeline distinto.

Por ejemplo:

Modo Código

Generar
↓
Compilar
↓
Lint
↓
Tests
↓
Repair
↓
Output

Mientras que un informe usaría otro pipeline:

Research
↓
Evidence
↓
Outline
↓
Writing
↓
Consistency
↓
Formatting

Yo incluso añadiría un Output Profile.

Algo así:

output_profile:
   style: enterprise
   format: markdown
   max_tokens: 12000
   citations: true
   evidence: required
   validation: strict

Entonces el orquestador no le diría al LLM simplemente "responde", sino:

> "Ejecuta el pipeline de salida Enterprise con validación estricta y formato Markdown."



Ahí es donde creo que está una de las mayores oportunidades de mejora.


---

La idea que más me gusta de todo lo que hemos hablado

Hasta ahora has dividido muy bien:

Kernel

Expertos

Agentes

Pipeline

Memoria


Pero creo que falta tratar la salida como un subsistema completo, no como el último paso.

Si el razonamiento tiene 20 etapas, la salida también podría tener 8-10 etapas. De hecho, en muchos sistemas actuales, una respuesta deficiente no se debe a que el modelo "no supiera" la solución, sino a que la capa de generación y validación de la salida no fue lo suficientemente estricta.

Si MAXBRY adopta ese enfoque desde el principio, el resultado sería un sistema donde el Output Engine tiene casi tanta importancia como el Reasoning Engine. En una arquitectura de este tipo, la calidad percibida por el usuario depende tanto del motor cognitivo como de cómo se transforma y verifica el resultado antes de entregarlo.


Creo que ese es uno de los problemas más difíciles de los sistemas con LLM. Muchas veces el razonamiento interno puede ser aceptable, pero la salida falla porque la traducción del estado interno a texto o a artefactos no está suficientemente controlada.

Yo no dejaría que el LLM "escriba directamente" la respuesta final. Separaría la salida en varias etapas, igual que separaste el razonamiento.

Estado final
      │
Output Planner
      │
Output Builder
      │
Output Validator
      │
Output Repair
      │
Output Judge
      │
Output Formatter
      │
Respuesta al usuario

Cada etapa tendría una única responsabilidad:

Output Planner: decide qué debe contener la respuesta (código, informe, JSON, explicación, etc.).

Output Builder: genera un primer borrador.

Output Validator: verifica que no falte ningún requisito.

Output Repair: corrige omisiones, formato o inconsistencias detectadas.

Output Judge: compara el resultado contra el objetivo original y las reglas de calidad.

Output Formatter: adapta la respuesta al formato solicitado.


En vez de preguntarle al modelo "¿la respuesta está bien?", usaría una lista de comprobaciones objetivas, por ejemplo:

¿Todos los objetivos fueron cubiertos?

¿Se generaron todos los archivos requeridos?

¿Hay referencias a funciones inexistentes?

¿Quedan marcadores como TODO, FIXME o placeholders?

¿El formato coincide con el contrato esperado?

¿Se respetó la estructura solicitada?


Solo si todas esas comprobaciones pasan, la respuesta se libera.

Además, añadiría un Output Contract. Antes de generar la salida, el sistema define exactamente qué debe producir:

output:
  artifacts:
    - report.md
    - state.json
    - tests.xml
  requirements:
    - sin placeholders
    - formato válido
    - evidencia incluida

El LLM no decide libremente qué entregar; debe satisfacer ese contrato.

Finalmente, introduciría un Output Diff: antes de enviar la respuesta, el sistema compara el objetivo inicial con la salida final y marca cualquier elemento que falte. Si detecta diferencias importantes, vuelve automáticamente a la etapa de reparación.

En esencia, trataría la salida como una línea de producción con control de calidad, no como un único paso de generación. Esa separación suele producir resultados mucho más consistentes que confiar en una sola generación del modelo, incluso cuando el razonamiento interno ha sido bueno.

Esta es probablemente la decisión arquitectónica más importante del sistema. Yo no usaría una memoria única porque se convierte rápidamente en un cuello de botella y aumenta el riesgo de inconsistencias.

Usaría un modelo de memoria por niveles, parecido a cómo funcionan los sistemas operativos y las bases de datos distribuidas.

MEMORIA GLOBAL
         (solo lectura para expertos)
                 │
     ┌───────────┼───────────┐
     │           │           │
Proyecto      Knowledge     Skills
State         Base          Registry
     │
──────────── Snapshot ────────────
     │
 E01    E02    E03 ... E100
 Mem    Mem    Mem
 Local  Local  Local
     │     │      │
 Resultados parciales
     └─────┴──────┘
          │
    Fusion Engine
          │
 Commit
          │
 Memoria Global

Yo separaría la memoria en cinco tipos:

1. Memoria Global (solo lectura durante el trabajo)

Estado del proyecto.

Configuración.

Objetivos.

DSL.

Inventario.


Ningún experto la modifica directamente.


2. Memoria Local del Experto

Hipótesis.

Variables temporales.

Resultados intermedios.


Se destruye al terminar el trabajo.


3. Memoria Compartida de la Tarea

Visible solo para los expertos que participan en esa tarea.

Sirve para intercambiar resultados parciales.



4. Memoria de Largo Plazo

Artefactos aprobados.

Historial.

Versiones.

Métricas.

Conocimiento consolidado.



5. Event Log

Cada acción genera un evento.

No se sobrescribe información; se registra qué ocurrió y cuándo.




Una regla importante

Los expertos no escriben en la memoria global.

Solo pueden devolver algo como:

{
  "proposal": {
    "update_state": "...",
    "confidence": 0.94
  }
}

Después un Memory Manager o un Commit Manager decide si esa información pasa a formar parte del estado oficial, tras las validaciones necesarias.

Eso evita que dos expertos modifiquen el mismo dato simultáneamente y facilita la trazabilidad.

Mi mejora sobre tu idea

Yo añadiría un concepto de Snapshot.

Cuando empieza una tarea:

se crea una copia consistente del estado (snapshot),

todos los expertos trabajan sobre esa misma versión,

al finalizar, el sistema fusiona los resultados,

si todo pasa las validaciones, se hace un único commit al estado global.


Es muy parecido a cómo funcionan sistemas de control de versiones o bases de datos con transacciones.

Así puedes tener 100, 500 o 1.000 expertos trabajando en paralelo sin que se pisen entre sí. Cada uno opera sobre una visión consistente del proyecto y solo el resultado consolidado modifica la memoria principal. Esa estrategia suele escalar mucho mejor que permitir escrituras concurrentes sobre un único estado compartido.


Creo que la idea puede llevarse más lejos, pero haría una separación muy clara para evitar que el sistema se vuelva caótico.

No haría que un experto "haga una tarea". Haría que un experto aplique una operación cognitiva.

Es decir, un experto siempre recibe:

> Estado → Procesa → Devuelve un resultado estructurado.



Nunca modifica directamente el sistema. Nunca toma decisiones globales. Solo produce evidencia.

Por ejemplo, los expertos podrían agruparse así:

Grupo 1. Comprensión

Goal Extractor

Intent Analyzer

Constraint Detector

Context Builder

Dependency Mapper


Grupo 2. Investigación

Repo Researcher

Skill Finder

Documentation Finder

RAG Searcher

Evidence Collector


Grupo 3. Razonamiento

Planner

Alternative Generator

Risk Analyzer

Trade-off Analyzer

Complexity Estimator


Grupo 4. Verificación

Schema Validator

Consistency Checker

Evidence Validator

Contradiction Detector

Quality Auditor


Grupo 5. Ejecución

Code Generator

Test Generator

Refactoring Planner

Artifact Builder


Grupo 6. Consolidación

Result Merger

Conflict Resolver

Priority Ranker

Final Synthesizer


Ahí es donde introduciría otra regla importante.

El experto NO llama agentes directamente.

En su lugar hace algo como:

Necesito:
- buscar repos
- generar código
- validar pruebas

Y devuelve esa solicitud al orquestador.

Después el Orchestrator Router decide:

qué agente usar,

qué modelo usar,

qué herramienta usar,

si ejecutar en paralelo,

si usar caché,

si reutilizar resultados anteriores.


Eso mantiene el desacoplamiento.


---

También introduciría un concepto parecido a un sistema operativo:

User
    │
Main Orchestrator
    │
Task Scheduler
    │
──────────────────────────────
Pool de 100 Expertos
──────────────────────────────
Research
Planning
Validation
Testing
Documentation
Security
...
──────────────────────────────
Agent Router
──────────────────────────────
OpenHands
Aider
OpenClaw
Claude Code
Minimax
Kimi
GitHub
RAG
Skills

Los expertos nunca saben quién ejecutará la tarea.

Solo producen trabajo.

El Router decide el ejecutor.


---

Lo que sí veo muy potente de tu idea es que el usuario sigue conversando con el orquestador mientras, por detrás, decenas o cientos de expertos trabajan en paralelo. Ese patrón ya aparece en algunos sistemas modernos de agentes, aunque cada uno lo implementa de forma diferente.

Mi mejora sería añadir un componente intermedio: un Task Scheduler. En lugar de que el orquestador coordine cientos de expertos directamente, el Scheduler administra la cola, las prioridades, los tiempos de espera, los reintentos y el balanceo de carga. El orquestador se concentra en la conversación y en las decisiones de alto nivel; el Scheduler distribuye el trabajo; los expertos procesan información; y el Router selecciona las herramientas o agentes adecuados para ejecutar cada solicitud.

Esa separación hace que el sistema pueda crecer desde unas pocas tareas concurrentes hasta cientos o miles de instancias sin convertir el orquestador principal en un bloque de código enorme y difícil de mantener.
Sí, esa evolución tiene bastante sentido y, de hecho, es más flexible que hacer un único pipeline gigante.

En lugar de pensar en 100 expertos, yo pensaría en 100 workers cognitivos que comparten el mismo motor pero pueden cargar pipelines distintos.

Por ejemplo:

KERNEL
                    │
        Router + Scheduler + State
                    │
      ┌─────────────┼─────────────┐
      │             │             │
 Grupo A        Grupo B       Grupo C
 Planning      Coding        Auditoría
 20 workers    40 workers    40 workers
      │             │             │
 Pipeline A    Pipeline B    Pipeline C

Cada worker ejecuta exactamente el mismo código base:

worker.run(
    pipeline="audit_v2",
    state=current_state
)

El pipeline define qué hace ese worker.

Por ejemplo:

Pipeline de planificación

Input
↓
Goal
↓
Constraints
↓
Task Decomposition
↓
Plan

Pipeline de programación

Input
↓
Architecture
↓
Generate Code
↓
Lint
↓
Tests
↓
Output

Pipeline de auditoría

Input
↓
Evidence
↓
Cross Check
↓
Risk Analysis
↓
Verdict

El router podría decidir dinámicamente:

5 workers para tareas simples.

20 para tareas medianas.

80 para una tarea crítica.

O dividirlos entre varios pipelines en paralelo.


Lo que me gusta de esta idea es que la inteligencia deja de estar "quemada" en el orquestador. El kernel solo administra recursos, estado y comunicación. El comportamiento vive en los pipelines, que son fáciles de modificar, versionar y sustituir.

La única precaución sería evitar crear 100 workers "porque sí". Conviene que el router los active según la complejidad y las necesidades de la tarea. Así obtienes escalabilidad sin desperdiciar recursos. Ese patrón se parece más a un sistema operativo que administra procesos que a un orquestador monolítico.



Yo lo programaría como un microkernel, no como 100 clases diferentes. La clave es que el cerebro existe una sola vez y los 100 expertos son instancias de ese cerebro.

La arquitectura sería aproximadamente así:

ORQUESTADOR (Kernel)
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     Router      Scheduler     Fusion Engine
        │
        ▼
   Expert Pool (100)
        │
 ┌──────┼──────┐
 │      │      │
E01    E02    E03 ... E100
 │      │      │
 └──────┼──────┘
        │
 Cognitive Engine (1 solo)
        │
   Pipeline Cognitivo

Los 100 expertos no tendrían código propio. Cada uno sería algo como:

expert_id: E17
pipeline: planning
priority: 8
skills:
  - reasoning
  - planning
temperature: 0.4

Todos llamarían al mismo motor:

result = cognitive_engine.run(
    expert_config,
    input_state
)

El Cognitive Engine sería el único lugar donde vive el razonamiento.

Después dividiría el razonamiento en micro-pipelines:

Input
 ↓
Goal
 ↓
Context
 ↓
Hypothesis
 ↓
Analysis
 ↓
Validation
 ↓
Decision
 ↓
Output

Cada experto podría ejecutar el pipeline completo o solo una parte, según lo que indique el router.

Luego añadiría un Fusion Engine, cuya única función sería:

eliminar duplicados,

detectar contradicciones,

puntuar confianza,

construir una respuesta única.


Lo que más cambiaría respecto a tu diseño actual es esto:

Kernel: 2.000–4.000 LOC.

Cognitive Engine: 1.500–3.000 LOC.

Router/Fusion: 1.000 LOC.

Expertos: prácticamente 0 LOC; son archivos de configuración (yaml/json) que instancian el mismo motor.

Pipelines: archivos DSL independientes y editables.


Así, en lugar de mantener 100 implementaciones, mantienes un solo cerebro, un solo kernel y 100 configuraciones. Si mejoras el motor cognitivo, los 100 expertos mejoran automáticamente. Esa es una arquitectura mucho más cercana al principio de reutilización que hace escalables a los sistemas MoE, aunque implementada en software en lugar de mediante redes neuronales.

Sí, esa idea es técnicamente coherente, pero haría una distinción importante.

En un MoE real, los 100 expertos no son iguales. Aunque tienen la misma arquitectura (el mismo tipo de red neuronal), sus pesos son distintos porque cada uno aprendió patrones diferentes durante el entrenamiento. El router elige cuáles activar según la entrada.

En un orquestador basado en código, podrías trasladar ese principio así:

Todos los expertos comparten la misma plantilla de código (misma interfaz y ciclo de ejecución).

Lo que cambia es su configuración, pipeline, prompt, reglas o skills.

El router decide qué expertos activar para una tarea concreta.

Pueden ejecutarse en paralelo y luego un módulo de fusión combina sus resultados.


Es decir, no tendrías 100 cerebros escritos desde cero. Tendrías:

1 motor cognitivo común (el código).

100 instancias de ese motor con configuraciones distintas.

1 router que selecciona cuáles participan.

1 fusionador que integra las respuestas.


Eso reduce muchísimo el código y facilita el mantenimiento. Si mejoras el motor cognitivo, automáticamente mejoran los 100 expertos.

Incluso podrías ir un paso más allá: los expertos no tendrían que estar definidos por dominio ("programación", "matemáticas"), sino por operaciones cognitivas: analizar, comparar, generar hipótesis, detectar contradicciones, validar evidencia, estimar riesgos, priorizar, sintetizar, etc. El conocimiento especializado se obtendría aparte, mediante herramientas, RAG o especialistas, mientras los expertos aplican esas operaciones cognitivas sobre la información disponible.

En ese sentido, tu propuesta se parece más a un MoE cognitivo implementado en software que a copiar literalmente la arquitectura neuronal de un MoE. Es una inspiración arquitectónica, no una reproducción del mecanismo matemático.

Sí, y la investigación es interesante porque confirma parte de tu intuición y corrige otra parte.

En modelos MoE modernos como Kimi K2/K2.5 o MiniMax-M1, un "experto" no es un agente ni un módulo programado para una profesión. Es una red neuronal feed-forward (FFN) dentro de cada capa Transformer. Un router (gating network) decide para cada token qué expertos activar; los demás no participan. 

Lo más importante es cómo se especializan:

No existe un experto llamado "programador" o "matemático".

La especialización emerge durante el entrenamiento.

Investigaciones recientes muestran que muchos expertos terminan especializándose en operaciones muy concretas, como cerrar expresiones, procesar cierto tipo de estructura lingüística o realizar transformaciones semánticas específicas, más que en dominios amplios. 


Al mismo tiempo, otros estudios encuentran evidencia de que sí pueden aparecer expertos con cierta inclinación hacia dominios (por ejemplo, ciencia o programación), pero esa especialización también emerge del entrenamiento y no está codificada manualmente. 

Esto tiene una consecuencia para tu arquitectura:

Tu idea de construir expertos como Goal Detector, Constraint Detector, Dependency Mapper o Risk Analyzer no copia literalmente un MoE, pero sí copia uno de sus principios fundamentales: cada componente tiene una única responsabilidad y el router decide cuándo utilizarlo.

La diferencia es que:

MoE neuronal: los expertos son redes neuronales entrenadas automáticamente.

MAXBRY: los expertos serían microcomponentes programados, verificables y reemplazables, coordinados por un router y un pipeline.


Esa segunda aproximación se parece más a una arquitectura cognitiva modular inspirada en MoE que a un MoE clásico. Técnicamente es una analogía válida, pero no es el mismo mecanismo interno que usan Kimi o MiniMax.



















