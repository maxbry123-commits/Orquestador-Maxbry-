# NCT — NEURONAS CODE TURBO — PIPELINE TÉCNICO v3.0
# DOCUMENTO 1/7 — ÍNDICE COMPLETO DEL PROYECTO + FORMATO DE LECTURA
# Fecha: 2026-07-15 | Software de orquestación determinista multi-agente
# Consume: SALIDA_04_PIPELINE_RAIZ (Fable) + auditoría completa de este chat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. QUÉ ES NCT (una sola definición, sin metáforas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NCT (Neuronas Code Turbo) es un sistema de orquestación multi-agente
determinista: coordina múltiples agentes de IA y componentes de software
para construir, verificar y desplegar código, separando estrictamente
las tareas creativas/probabilísticas (razonamiento con LLM) de las
tareas mecánicas/deterministas (ejecución, despliegue, verificación).

Principio de diseño central: **todo lo que se puede resolver con reglas
fijas se resuelve con código, nunca con un modelo de lenguaje.** Un LLM
decide QUÉ hacer; el código determinista decide CÓMO ejecutarlo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ÍNDICE COMPLETO — TODOS LOS DOCUMENTOS DEL PROYECTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 1.1 Documentos de diseño original (bandeja del proyecto, autoría: Fable)
| Documento | Contenido |
|---|---|
| ACTA_DECISIONES_DIRECTOR.md | Firma oficial del Director: 15/15 gaps cerrados, decisiones de staff, formato de fichas 5-campos, aprobación global |
| DISENO_ORQUESTACION_FUSIONADO.md | Arquitectura de 6 capas (Director→Fable→Claude Code→Router→Staff→Infra) |
| PROMPT_PIPELINE_INSTRUCCIONES_ARBOLITO.md | Instrucciones originales para generar el primer PIPELINE |
| SALIDA_01_PLAN_MAESTRO_Y_PASADA_1.md | Plan de 10 entregas + extracción de 30 requisitos del Director |
| SALIDA_02_AUDITORIA_PASADAS_2_3.md | Cruce del corpus histórico contra el Kernel v3 (matriz de 25 elementos) |
| SALIDA_03_PASADA_4_Y_15_GAPS_BANDERAS.md | Los 15 gaps (G-01 a G-15) con solución técnica cada uno |
| SALIDA_04_PIPELINE_RAIZ_MEJORA_100.md | El PIPELINE original: 16 repos, diagramas horizontal/transversal, FASE_RUNNER |
| SALIDA_05_REFUTACIONES_Y_CONSENSOS.md | 4 refutaciones internas + 4 consensos de 10 especialistas |
| SALIDA_06_SIMULACIONES_Y_25_PASOS.md | 5 simulaciones de validación + los 25 pasos de razonamiento oficial |
| SALIDA_07_DSL_DAG_CODIGO_Y_FICHAS_AVANZADAS.md | Primer código Python real: motor_bus, goal_tree, monitores, fase_runner |
| SALIDA_08A_CLAUDE_CODE_SAAS_INTERFACES.md | Instrucciones S20-S31 (órdenes de construcción) + diseño SaaS |
| SALIDA_08B_200_MEJORAS.md | Catálogo de 239 mejoras propuestas (M-007 a M-239) |
| SALIDA_09_LISTA_REGALOS_SANTA.md | Cuestionario de aprobación: 15 gaps con estado ✅/🔶 esperando firma del Director |
| SALIDA_10_TREN_ARBOL_NAVIDAD.html | Visualización interactiva del sistema (versión temática original) |
| PARCHE_GUIA_MAESTRO.md | Índice de las 11 entregas de Fable + guía de edición del sistema |
| ORDEN_T1_AUDITORIA_REPOS.md | Orden de auditoría de repos reales de GitHub (pendiente de ejecutar) |

### 1.2 Documentos de análisis inicial (esta sesión)
| Documento | Contenido |
|---|---|
| DOC1_BOMBILLOS_FALTANTES.md | Auditoría: qué código ya existía vs qué faltaba de los 16 repos originales |
| DOC2_PROMPT_PIPELINE_TREN_NAVIDAD.md | Primer PIPELINE de esta sesión (versión temática, ANTECESOR de este documento) |

### 1.3 Código construido — SALIDA A (infraestructura base)
| Documento/Archivo | Contenido |
|---|---|
| config.py | 17 feature flags + 11 límites operativos del sistema |
| state.json | Registro de 18 nodos de tarea (T-001 a T-018), estado inicial |
| a2_dsl_dag.yaml | Los 18 nodos DSL completos con contrato input/output + DAG-001 (grafo de dependencias) |
| router/core.py | Núcleo del Router: única puerta de entrada/salida del sistema, ledger hash-chain |
| router/auth.py | Emisión de tokens, roles (user/engineer/admin), revocación, rate limiting |
| router/cola.py | Cola de prioridades (critical/normal/background) |
| router/balanceo.py | Balanceador round-robin con detección de destinos caídos |
| router/providers.yaml | Configuración de 9 modelos locales + 16 slots de API keys (solo nombres de variable) |
| router/seleccion.py | Selección de modelo por perfil de usuario (n0-n5) con fallback |
| gateway/mcp.py | Gateway de herramientas MCP con control de permisos por rol |
| motores/motor_bus.py | Bus de comunicación entre los 16 módulos del sistema, valida fronteras declaradas |
| motores/manifests/*.yaml (16 archivos) | Declaración de frontera (con qué módulos puede comunicarse cada uno) |
| loops/loop_runner.py | Ejecutor de bucles con presupuesto (tokens/tiempo/iteraciones) y detección de estancamiento |
| tribunal/tribunal.py | Sistema de verificación de calidad: 2 vetos + 4 jueces con score ponderado |
| recovery/recovery.py | Write-Ahead Log + escalera de 6 niveles de recuperación ante fallos |
| anclas/ancla_agent.py | Sistema de inyección forzada de contexto (documentos/instrucciones) en cada paso de ejecución |
| anclas/mesa_anclaje.html | Interfaz de 2 paneles para gestionar el sistema de anclaje |

### 1.4 Código construido — SALIDA B (motor de razonamiento y ejecución)
| Documento/Archivo | Contenido |
|---|---|
| gcl/goal_tree.py | Constructor de árbol de metas (10-50 sub-metas) con hash de integridad (GoalLock) |
| gcl/gcl_lite.py | Verificador de invariantes O(1) por cada paso de ejecución |
| gcl/z3_gate.py | Verificación matemática formal con Z3 solver: demuestra que un plan es factible antes de ejecutarlo |
| gcl/tren_ascii.py | Utilidad de visualización de estado de ejecución en consola |
| loop_engine/engine.py | Motor de ciclo de 9 fases obligatorias por iteración de trabajo |
| loop_engine/detectores.py | 6 detectores de anomalías: estancamiento, oscilación, regresión, deriva, presupuesto, timeout |
| loop_engine/catalogo.py | Generador de 1.080 configuraciones de bucle + selector por criterio |
| escritor/escritor_core.py | Generador de artefactos de código con metadatos de autoría y hash de nacimiento |
| runtime/builder.py | Entorno aislado de ejecución (sandbox): proceso separado, sin variables de entorno heredadas, con timeout forzado |
| witness/witness.py | Sistema de certificación: ejecuta pruebas de forma independiente al autor del código |
| witness/inspector.py | Analizador estático: detecta secretos, código peligroso, violaciones de estilo sin ejecutar nada |

### 1.5 Código construido — Sistema nervioso (memoria, auditoría, gobierno)
| Documento/Archivo | Contenido |
|---|---|
| memoria/memoria.py | Sistema de memoria de 4 niveles (sesión, trabajo indexado, conocimiento, WAL persistente) |
| auditoria/audit_bus.py | Bus de eventos con cadena de hashes + medición de duración por operación |
| monitores/monitores.py | 3 monitores de salud del sistema (ánimo, presión, desviación) — solo reportan, nunca corrigen |
| sentinela/sentinela.py | Sistema de propuestas de cambio que requiere firma criptográfica del Director para aplicarse |
| decision/consenso10.py | Motor de votación: mesa de 5 (normal) o mesa de 10 (crítico) con quorum |
| atlas/fase_runner.py | Ejecutor de las 21 fases del roadmap del proyecto, con checkpoints verificables |
| gobernanza/ledger.py | Registro de firmas encadenado + generador de reporte de estado del sistema |
| fichas/generador.py | Fábrica de unidades de trabajo con formato de 5 campos obligatorios + test de humo automático |
| mapeos/tablas.yaml | 5 tablas de correspondencia (jueces, artículos de constitución, micro-agentes, organización, niveles) |
| main.py | Punto de entrada que acopla todos los módulos del sistema |
| .github/workflows/ci.yml | Integración continua: verifica estilo + corre la prueba end-to-end en cada cambio |

### 1.6 Frontend — interfaces construidas
| Documento/Archivo | Contenido |
|---|---|
| frontend/panel_tren_vivo.html | Panel de monitoreo en tiempo real de los 18 nodos de tarea |
| frontend/ventanas_del_tren.html | Interfaz de ejecución por etapas visuales con punto de interrupción e intervención manual |
| frontend/constructor_nocode.html | Constructor visual de flujos de trabajo sin escribir código |
| frontend/panel_router_3.html | Panel de configuración del Router: entrada/receptor/salida en 3 columnas |
| frontend/panel_orquestador.html | Panel de composición de funciones con ejecución en sandbox real |
| frontend/panel_auditor_ios.html | Panel de gestión documental con sistema de anclaje integrado |

### 1.7 Módulos avanzados de desarrollo (10 herramientas)
| Documento/Archivo | Contenido |
|---|---|
| regalos_dev/indice_repo.py | Indexador de símbolos de código basado en AST (funciones/clases del repositorio) |
| regalos_dev/parche_quirurgico.py | Aplicador de cambios de código con verificación de hash y rollback |
| regalos_dev/tdd_forzado.py | Forzador de desarrollo dirigido por pruebas: prohíbe implementar sin prueba fallida previa |
| regalos_dev/refactor_ast.py | Renombrador de símbolos multi-archivo con verificación de compilación |
| regalos_dev/transaccion_multi.py | Editor transaccional multi-archivo: todo-o-nada con rollback automático |
| regalos_dev/corredor.py | Ejecutor instantáneo de código en sandbox con detección de dependencias faltantes |
| regalos_dev/revisor_diff.py | Revisor automático de cambios: detecta secretos y eliminación indebida de pruebas |
| regalos_dev/guardia_regresion.py | Sistema de detección de regresión de comportamiento mediante huella de salida |
| regalos_dev/memoria_codigo.py | Registro de decisiones de diseño atado al hash del archivo (detecta decisiones obsoletas) |
| regalos_dev/comandante.py | Orquestador de la cadena completa de desarrollo en una sola invocación |

### 1.8 Módulos de composición visual (ventanas encadenadas)
| Documento/Archivo | Contenido |
|---|---|
| ventanas/estacion.py | Unidad de ejecución visual: entrada, proceso, salida con registro de estado |
| ventanas/cadena.py | Encadenador de unidades con soporte de punto de interrupción e intervención |
| ventanas/protocolo.py | Protocolo de comunicación panel-backend (formato de eventos serializables) |
| ventanas/arquitecto.py | Validador de arquitectura de proyecto: detecta violación de capas y ciclos |
| ventanas/exportador_dsl.py | Convertidor de flujo visual a nodos DSL ejecutables |
| ventanas/plantillas/*.yaml (4 archivos) | Plantillas de arquitectura: hexagonal, pipeline, eventos, microservicios |

### 1.9 Panel de conexión + puente de integración
| Documento/Archivo | Contenido |
|---|---|
| puente.py | 5 funciones de integración expuestas para API/MCP: ejecución, configuración, anclaje, envío, cadena |
| conexiones.yaml | Mapa de integración: qué endpoint corresponde a cada panel, cómo envolver en FastAPI o MCP |
| mcp_tools.json | Definición de las 5 herramientas MCP con esquema de entrada |

### 1.10 Infraestructura de despliegue y operación
| Documento/Archivo | Contenido |
|---|---|
| api_router.py | Envoltorio HTTP (FastAPI) real del Router: endpoints /route /status /token |
| estres.py | Prueba de carga: 1.000 solicitudes, medición de throughput e integridad del ledger |
| nct_cli.py | Interfaz de línea de comandos: status, demo, reporte, prueba de estrés |
| respaldo.py | Sistema de empaquetado con manifiesto de hashes + verificación de integridad |
| sistema/nct-router.service | Configuración systemd para ejecución persistente del Router |
| sistema/Caddyfile | Configuración de proxy TLS automático |
| telegram/bot_santa.py | Bot de notificación por Telegram (comandos de estado y reporte) |
| saas/demo_gate.py | Control de acceso por plan (gratuito limitado / profesional / equipo) con aislamiento de datos |
| openclaw/config.yaml | Configuración del canal de emergencia: acceso restringido solo a operaciones de recuperación |
| desplegar.sh | Script de despliegue de un comando: instala dependencias y verifica con la prueba end-to-end |

### 1.11 Vagón de despliegue a repositorio (F22)
| Documento/Archivo | Contenido |
|---|---|
| despliegue/organizador.py | Clasificador determinista: asigna cada archivo a su repositorio de destino por reglas fijas |
| despliegue/desplegador.py | Creador de repositorios Git reales con commits automáticos, idempotente |
| despliegue/detector_version.py | Detector de cambios con versionado semántico automático |
| despliegue/subir_a_github.sh | Script de un comando: organiza y sube todo a GitHub |
| DESPLIEGUE_COMO_LO_HAGO_HOY.md | Guía operativa para el usuario sin conocimientos de programación |

### 1.12 Fichas de trabajo generadas (unidades de prueba)
| Documento | Contenido |
|---|---|
| fichas/LOTE_1A_E001_E010.md | 10 unidades de trabajo del Pipeline de Entrada, formato 5 campos, prueba de humo verificada |
| fichas/LOTE_1B_E011_E020.md | 10 unidades adicionales (validación, normalización, clasificación, seguridad) |

### 1.13 Documentos de continuidad (checkpoint del proyecto)
| Documento | Contenido |
|---|---|
| checkpoint.json | Estado completo del proyecto en formato estructurado |
| PARCHE_DE_RECUPERACION.md / v2 | Guía de continuidad ante cambio de sesión o modelo |
| INDICE_COMPLETO_DOCUMENTOS.md | Índice de las salidas de esta sesión (versión anterior a este documento) |
| LISTA_DE_PENDIENTES.md | Registro de tareas pendientes con prioridad |
| UOOS_PARTE1/2_F22_PARA_APROBAR.md | Documento de aprobación del sistema de despliegue |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. FORMATO DE LECTURA — CÓMO SE EXPLICA CADA COMPONENTE (documentos 2-7)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cada componente técnico se documenta con esta estructura completa —
ninguna sección es opcional ni se resume:

```
COMPONENTE: [nombre exacto]

FUENTES (archivo por archivo, sin omitir ninguno):
  - archivo.py — clases/funciones que contiene, responsabilidad exacta
  - archivo.yaml — qué configura
  (si el componente se construyó con 5 documentos, se listan los 5)

EXPLICACIÓN TÉCNICA (para ingeniero de software o para un agente IA):
  - Firma de funciones, estructura de datos, algoritmo, complejidad,
    dependencias, contrato de entrada/salida — sin ambigüedad, sin
    resumir. Un ingeniero o una IA debe poder reconstruir el
    comportamiento exacto solo leyendo esta sección.

EXPLICACIÓN EN LENGUAJE LLANO (para cualquier persona, sin jerga):
  - Qué problema resuelve, qué hace paso a paso, por qué existe,
    qué pasaría si no existiera. Sin tecnicismos innecesarios, pero
    sin omitir información — se explica el MISMO comportamiento que
    la sección técnica, solo que con palabras distintas.

DIAGRAMA DE FLUJO (horizontal, siempre):
  entrada → paso 1 → paso 2 → paso 3 → salida
  (con anotación de qué verifica o transforma en cada flecha)

EVIDENCIA DE VERIFICACIÓN:
  - Qué pruebas se ejecutaron, qué resultado dieron, qué casos límite
    se comprobaron (fallos inducidos, ataques simulados, etc.)
```

Regla de no-ambigüedad: si una explicación técnica y su versión en
lenguaje llano describen comportamientos distintos, hay un error en el
documento y debe corregirse — ambas deben describir EXACTAMENTE el
mismo sistema, solo con distinto nivel de vocabulario.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. SÍMBOLOS DE ESTADO USADOS EN TODO EL PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
[CONSTRUIDO]     = código real, probado, con evidencia de verificación
[DISEÑADO]       = especificado por Fable, código aún no construido
[EXTENSIÓN]      = módulo adicional no solicitado en el diseño original
[GATE-MATEMÁTICO]= punto de verificación formal con Z3 (sin demostración, no continúa)
[TRIBUNAL]       = punto de verificación de calidad (6 inspectores)
[ANCLAJE]        = punto de inyección forzada de contexto
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. ESTRUCTURA DE LOS 7 DOCUMENTOS DE ESTA SERIE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Doc | Contenido |
|---|---|
| 1 | (este) Índice completo del proyecto + formato de lectura |
| 2 | Infraestructura base: configuración, Router, Bus de módulos, Tribunal, Recuperación, Anclaje |
| 3 | Motor de razonamiento: árbol de metas, verificación Z3, motor de bucles, Escritor/Sandbox/Certificación |
| 4 | Sistema nervioso: memoria, auditoría, sentinela, ejecutor de fases, punto de entrada principal, fichas, frontend |
| 5 | Módulos avanzados: herramientas de desarrollo, composición visual, panel de conexión |
| 6 | Infraestructura de operación: API HTTP, pruebas de carga, CLI, despliegue a repositorio |
| 7 | Recursos operativos, las 15 leyes del sistema, glosario técnico-simple |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. TABLA DE AUDITORÍA — NOMBRES DE ARCHIVO REPETIDOS ENTRE DOCUMENTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Nombre | Ubicación única confirmada | Nota |
|---|---|---|
| config.py | SALIDA A, sección 1.3 | archivo único en todo el proyecto |
| mcp_tools.json | sección 1.9 y 1.10 | mismo contenido, entregado en 2 salidas distintas — verificado idéntico |
| main.py | sección 1.5 | archivo único — punto de entrada del sistema completo |
| builder.py | sección 1.4 (runtime/) | no confundir con desplegador.py de sección 1.11 |
| ledger.py | sección 1.5 (gobernanza/) | no confundir con audit_bus.py de la misma sección |

Este apartado se actualiza cada vez que se detecte un conflicto real de
nombres (mismo nombre de archivo, contenido distinto, en documentos
diferentes) — actualmente no hay conflictos activos, solo casos de
nombre compartido con contenido verificado como idéntico o distinguible
por ruta completa.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMEN DE ESTE DOCUMENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Índice completo de ~90 documentos del proyecto (diseño original +
código construido + interfaces + infraestructura + checkpoint), más el
formato exacto que usarán los 6 documentos siguientes: cada componente
con sus fuentes exactas, explicación técnica completa, explicación en
lenguaje llano completa (mismo contenido, distinto vocabulario),
diagrama de flujo y evidencia de verificación.

→ Esperando aprobación para continuar con Documento 2/7 | FIX <detalle>
