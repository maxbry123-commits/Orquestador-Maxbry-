# NCT_INTERFACE_v2.md
# Fuente de verdad — Sonnet / Opus / FABLES
# Version: 2.0 | Checkpoint: DOC4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 1 — CENTRO DE CONTROL COGNITIVO (9 CAPAS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cada capa: estado ON / OFF / SCHEDULED
SCHEDULED = activo solo bajo condiciones definidas

CAPA 1 — PENSAMIENTO
├── Modo razonamiento: rápido | profundo | auditor | creativo
├── Nivel de verificación: bajo | medio | alto
├── Autoevaluación: ON/OFF
└── Debate entre agentes: ON/OFF

CAPA 2 — SALIDA
├── Longitud: corta | media | completa
├── Formato: Markdown | JSON | PDF | código
├── Estilo: técnico | ejecutivo | docente
├── Idioma
└── Plantillas reutilizables versionadas

CAPA 3 — ORQUESTACIÓN
├── Teams activos
├── Prioridades
├── Máximo agentes simultáneos
├── Presupuesto por tarea
└── Tiempo máximo (horizon)

CAPA 4 — MÉTODOS
├── System Prompt (versionado)
├── DSL (versionado, hash chain)
├── DAG (versionado)
├── Schemas (versionado, contracts/)
├── Skills (versionado)
├── Policies (versionado)
├── Memory Rules (versionado)
└── Todos con interruptor ON/OFF independiente

CAPA 5 — MODELOS
├── Modelo preferido por task_type
├── Fallbacks (cadena definida)
├── Reglas de selección (capability.json)
└── Límites de costo y latencia

CAPA 6 — MEMORIA
├── Qué recordar (por tier)
├── Qué olvidar (TTL por tipo)
├── Compactación (Writer Subagent threshold)
├── Checkpoints (frecuencia)
└── Versiones del estado (rollback)

CAPA 7 — APRENDIZAJE
├── Registrar errores (Failure Registry)
├── Registrar éxitos (Corrections DB)
├── Métricas por agente (quality/efficiency/reliability)
└── Ranking de rendimiento

CAPA 8 — LABORATORIO
├── Probar DSL antes de activarlo (sandbox)
├── Simular ejecución (5x obligatorio)
├── Comparar 2 configuraciones (A/B)
└── Volver a versión anterior (rollback ≤10s)

CAPA 9 — GOBERNANZA (nuevo, debate aprobado)
├── Qué decisiones requieren aprobación humana
├── Qué decisiones son auto-aprobadas
├── Qué decisiones son bloqueadas siempre
└── Audit trail de cada decisión tomada
    Esta capa diferencia un sistema que "parece seguro"
    de uno que realmente está bajo control.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 2 — MODOS DE OPERACIÓN (3 modos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REGLA CLAVE: la interfaz NUNCA forma parte del Kernel.
El Kernel no sabe que existe una interfaz.
Es un cliente que consume la API del Orquestador,
igual que cualquier otro cliente.

MODO 1 — HEADLESS
├── Sin interfaz gráfica
├── Solo API / MCP / CLI
├── Ideal para VPS, servidores, automatización
└── Máximo rendimiento

MODO 2 — STUDIO
├── Interfaz web completa
├── Chat integrado con el orquestador
├── Panel de configuración (9 capas)
├── Monitoreo en tiempo real
├── Edición de DSL, Skills y Policies
└── Visualización de Teams y agentes

MODO 3 — EMBEDDED (nuevo, debate aprobado)
├── El Kernel expone API pública mínima
├── Cualquier app externa puede embeber NCT
├── Sin interfaz propia — es una librería importable
└── Caso de uso: otro sistema llama al Kernel
    como dependencia, no como servicio externo

Los 3 modos comparten el mismo Kernel sin modificarlo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 3 — ÁRBOL DE DECISIONES AUDITABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El diferenciador clave de NCT: no solo funciona,
explica POR QUÉ funciona.

ESTRUCTURA:
```
ÁRBOL DE DECISIÓN NCT:
├── Tarea: "refactorizar módulo de auth"
├── Opciones evaluadas:
│   ├── TEAM_A (code_gen + test) → score: 0.82 ← ELEGIDO
│   ├── TEAM_B (research + code) → score: 0.71
│   └── TEAM_C (audit + refactor) → score: 0.65
├── Por qué descartó TEAM_B:
│   └── budget constraint: $0.15 > límite $0.10
├── Por qué descartó TEAM_C:
│   └── capability faltante: python_3.11_typing
├── Consenso: 3/5 agentes votaron TEAM_A
└── Confidence: 0.82 (por encima de umbral 0.70)
```

Cada decisión del sistema queda registrada así.
Sirve para: depurar, auditar, mejorar, explicar al Director.
Se alimenta directamente del Decision Engine v2 (DOC1 [8.1]).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 4 — PANEL DE CONTROL (Studio)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPONENTES DEL PANEL:

1. Panel de Configuración
   Activar/desactivar métodos ON/OFF, Teams, políticas

2. Chat integrado
   Hablar con el orquestador, ver cómo planifica

3. Editor de System Prompt
   Con versiones y posibilidad de volver atrás

4. Editor DSL/DAG/Schema
   Visual, con validación antes de aplicar cambios

5. Gestor de Skills
   Instalar/actualizar/activar/desactivar como plugins

6. Monitor en tiempo real
   Qué Team activo, qué agentes trabajan, progreso

7. Configuración persistente
   Los cambios permanecen hasta modificarlos

8. Sandbox
   Probar cambios sin afectar el sistema principal

9. Mapa Vivo del Sistema
   Team + agente + tarea activos en tiempo real

10. Gestor de Perfiles
    Perfiles completos: "Programador", "Arquitecto",
    "Investigador" — cambiar con un clic

11. Centro de Experimentos
    Comparar 2 configuraciones (A/B) en la misma tarea

12. Mercado de Componentes
    Instalar Teams/Skills/DSL/Policies como plugins

13. Panel de Coste y Rendimiento
    Consumo por modelo, Team, tarea, agente

14. Centro de Versiones
    Volver a cualquier configuración anterior

15. Panel de Salud
    RAM, CPU, colas, errores, latencia, disponibilidad

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 5 — SISTEMA DE CAPACIDADES (no nombres)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Principio: no elegir agentes por nombre ("Aider").
Elegir por capacidades ("refactorizar_python", "analizar_seguridad").

Si mañana aparece un agente mejor:
→ se registran sus capacidades
→ el sistema puede usarlo sin cambiar la lógica del orquestador
→ esto hace que la arquitectura envejezca mejor

Esto ya está integrado en:
- Capability Registry [18] (DOC1)
- Agent Manifest Reader [9.3] (DOC1)
- Selección de micro-agentes en Team Agent (DOC2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BLOQUE 6 — API PÚBLICA DEL KERNEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Endpoints mínimos expuestos (para cualquier modo):

POST /v1/task          → enviar nueva tarea
GET  /v1/task/{id}     → estado de una tarea
GET  /v1/decision-tree/{id} → árbol de decisión de una tarea
POST /v1/config        → actualizar configuración (9 capas)
GET  /v1/health        → estado del sistema
GET  /v1/metrics       → panel de rendimiento
POST /v1/simulate      → simular tarea sin ejecutar
GET  /v1/checkpoint    → último checkpoint disponible
POST /v1/rollback      → volver a versión anterior

Cualquier interfaz (web, móvil, CLI, otra IA)
consume estos mismos endpoints sin privilegios especiales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — DOC4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "NCT_INTERFACE_v2",
    "version": "2.0",
    "fecha": "2026-07-04",
    "fuente_de_verdad": true
  },
  "centro_control_cognitivo": {
    "capas": 9,
    "capa_9_gobernanza": "nueva, debate aprobado",
    "estados_por_capa": ["ON","OFF","SCHEDULED"]
  },
  "modos_operacion": {
    "total": 3,
    "headless": true,
    "studio": true,
    "embedded": "nuevo, debate aprobado",
    "regla": "interfaz nunca es parte del kernel"
  },
  "arbol_decisiones": {
    "auditable": true,
    "fuente": "Decision Engine v2"
  },
  "panel_control": {
    "componentes": 15
  },
  "capacidades_no_nombres": true,
  "api_publica_endpoints": 9,
  "docs_relacionados": ["DOC1_kernel","DOC2_team_agent","DOC3_router"]
}
