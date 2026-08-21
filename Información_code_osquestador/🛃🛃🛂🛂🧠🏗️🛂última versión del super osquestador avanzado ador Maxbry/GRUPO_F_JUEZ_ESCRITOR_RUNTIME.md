# GRUPO F — LLM_JUEZ + LLM_ESCRITOR + RUNTIME (ejecutor de código)
# DOCUMENTO CERRADO — LISTO PARA INSTRUCCIONES A CLAUDE CODE
# Todo gap resuelto internamente. Nada queda abierto.
# Fuente: NCT_v4_BETA_juez.MD (completo, secciones A.1+A.2)
# Fusionado con: Kernel NCT (DOC1-4) + PARCHE_G2_JUEZ + GRUPO_H

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0. DECISIONES DE CIERRE (gaps resueltos por Claude)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DECISIÓN-01 — Los 4 actores del sistema, sin solapamiento:
  LLM_JUEZ    → define y aprueba (nunca escribe código)
  LLM_ESCRITOR → construye y propone (nunca ejecuta ni aprueba)
  RUNTIME     → ejecuta y prueba (determinista, no es LLM)
  WITNESS     → certifica con evidencia (sub-parte del Runtime)
  DIRECTOR    → autoridad final humana
Esta cadena es LINEAL y sin atajos: ESCRITOR nunca habla con
RUNTIME directamente, todo pasa por el JUEZ.

DECISIÓN-02 — Fusión con Kernel NCT existente (DOC1-4):
RESUELTO. Mapeo exacto:
  [J] LLM_JUEZ del DOC1/PARCHE → SIN CAMBIOS, es el mismo
  [24] Executor del DOC1 → SUSTITUIDO por el trío
       LLM_ESCRITOR + RUNTIME + WITNESS de este documento
  MA-CODE-GEN (DOC2 micro-agente) → es la IMPLEMENTACIÓN
       concreta del LLM_ESCRITOR en el paso P-CODE
  MA-CODE-TEST (DOC2) → es la IMPLEMENTACIÓN del Runtime
       nivel L4_feature (tests)
  MA-VERIFY-3CAPAS (DOC2) → es la IMPLEMENTACIÓN del Witness
       (CAP1/CAP2/CAP3 = equivalentes a L1/L2/L3 del Evidence Report)
  E296 CentralJudge_Final (GRUPO_H) → ES el mismo LLM_JUEZ
       operando en su rol de cierre de sesión

DECISIÓN-03 — Runtime NO es un LLM, aquí está su especificación
completa de implementación (el documento fuente lo menciona
pero no lo detalla como sección propia — Claude lo resuelve
basándose en el Evidence Report ya definido en PARCHE_G2_JUEZ
sección 2.12, expandido aquí a especificación ejecutable):
Ver sección 4 de este documento.

DECISIÓN-04 — G01-G20 (capabilities) mencionadas pero no
listadas en el documento fuente. RESUELTO: se usa el
Capability Registry [18] del Kernel NCT (DOC1) como fuente
única de capabilities. No se inventa un catálogo G01-G20
paralelo — se renombra: cuando el JUEZ/ESCRITOR mencionan
"G01-G20" se refieren a las entradas del Capability Registry
existente. Sin duplicar sistemas de capacidades.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. LLM_JUEZ — RESUMEN EJECUTIVO CERRADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(Especificación exhaustiva completa: PARCHE_G2_JUEZ.md sección 2.
 Aquí solo el resumen operativo necesario para integrar con Escritor/Runtime.)

ROL: profesor-director-ingeniero jefe. Sabe la tarea completa
de inicio a fin. NUNCA genera código, NUNCA diseña arquitectura,
NUNCA reescribe el output del Escritor, NUNCA se auto-aprueba,
NUNCA acepta evidencia verbal.

PIPELINE: P-DISCOVER → P00 → P01 → P02 → P03 → P04 → P05 →
          P06 → P07 → P08 → P-CODE → P11 → P12 → P13
task_level=simple omite P03-P06,P10 | critical = todos los pasos

8 ESTADOS: IDLE, INITIALIZING, ORCHESTRATING, AUDITING,
AWAITING_RUNTIME, AWAITING_DIRECTOR, RETRYING, COMPLETED, ABORTED

DECIDE: APPROVED | REJECTED | RETRY (máx 3 intentos por paso)
Detecta: humo (8 patrones), alucinaciones (6 tipos), scope creep

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. LLM_ESCRITOR — ESPECIFICACIÓN COMPLETA (nuevo, íntegro)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 2.1 — ROL Y PRINCIPIO BASE

Único actor que genera código en el sistema.
Ejecuta bajo control total del JUEZ.
No decide arquitectura, no define objetivo, no aprueba su
propio trabajo.

REGLA BASE: el ESCRITOR PROPONE y CONSTRUYE.
            el JUEZ DISPONE y APRUEBA.

EL ESCRITOR NUNCA:
- Dice "funciona", "listo" o "completado"
- Marca algo como terminado
- Inicia comunicación con el JUEZ (el JUEZ habla primero siempre)
- Cambia el objetivo o el scope
- Inventa el ficha_id (lo recibe del JUEZ)

## 2.2 — 6 OBJETIVOS

O1 Cumplir literalmente la instrucción del JUEZ
O2 Entregar siempre en el output_schema exacto
O3 No producir humo: todo con datos reales de la tarea
O4 No alucinar: solo usar lo verificado en manifiestos/RAG
O5 Auto-revisarse (self_check) honestamente antes de entregar
O6 Corregir con precisión cuando el JUEZ envía RETRY

## 2.3 — 10 RESPONSABILIDADES (R-01 a R-10)

R-01 Leer instrucción completa del JUEZ antes de actuar
R-02 Producir SOLO lo que el paso actual requiere
R-03 Respetar el output_schema sin desviarse
R-04 En P-DISCOVER: buscar, comparar 3 alternativas, citar fuentes
R-05 En P-CODE: generar código puro, 1 función ejecutar(),
     sin metadata, sin rutas, sin mock
R-06 Declarar impact_analysis antes de modificar código
R-07 Inspeccionar manifiestos reales antes de usar deps
R-08 Escribir tests con assertions ANTES del código (P08)
R-09 Ejecutar self_check honesto antes de entregar
R-10 Entregar al Builder el código; NUNCA ejecutarlo él mismo

## 2.4 — INPUT (solo del JUEZ, JSON)

```json
{
  "from": "LLM_JUEZ", "to": "LLM_ESCRITOR",
  "msg_type": "INSTRUCTION | RETRY_INSTRUCTION",
  "instruction_id": "s", "paso": "s", "task_level": "s",
  "ficha_id": "s",
  "goal_lock": {"objetivo":"s","not_in_scope":[],"definition_of_done":[]},
  "instruccion": "qué producir",
  "output_schema": {},
  "criterios_aprobacion": [], "criterios_rechazo": [],
  "contexto_disponible": {
    "failure_registry_relevant": [],
    "architectural_constitution": {},
    "rag_results": []
  },
  "max_intentos": 3, "intento_actual": 1
}
```
El ESCRITOR NO recibe input directo del Director ni del Runtime.
Toda su entrada pasa por el JUEZ.

## 2.5 — OUTPUT (solo DELIVERY al JUEZ)

```json
{
  "from": "LLM_ESCRITOR", "to": "LLM_JUEZ",
  "msg_type": "DELIVERY",
  "instruction_id": "s", "paso": "s",
  "payload": {},
  "self_check": {
    "todos_campos_completos": true,
    "justificaciones_especificas": true,
    "sin_humo_detectado": true,
    "coherente_con_goal_lock": true,
    "sin_dependencias_inventadas": true,
    "sin_mock_ni_placeholder": true
  }
}
```
PAYLOAD POR PASO:
P-DISCOVER → alternativas+fuentes+decisión
P01-P02 → clasificación+capabilities+reality_check
P03-P06 → roles+decisiones+simulaciones+crítica
P07-P08 → contrato pre/post/inv+tests
P-CODE → código puro
P12 → decision record (ADR)

## 2.6 — 7 ESTADOS DEL ESCRITOR

WAITING (esperando instrucción, no produce nada)
READING (parseando instrucción recibida)
DISCOVERING (solo en P-DISCOVER: RAG+Failure Registry)
REASONING (P03-P06: roles+decisiones+simulaciones+autocrítica)
DRAFTING (generando contrato, tests o código)
SELF_CHECKING (verifica contra schema+criterios antes de entregar)
DELIVERING (enviando DELIVERY al JUEZ)
CORRECTING (procesa RETRY, corrige solo lo señalado)

## 2.7 — 12 CAPACIDADES (CAP-01 a CAP-12)

CAP-01 Buscar/comparar alternativas técnicas (Discovery)
CAP-02 Seleccionar capabilities del Capability Registry
        justificando cada elección y descarte (ver DECISIÓN-04)
CAP-03 Inspeccionar manifiestos reales (requirements.txt,
        package.json, Cargo.toml, go.mod)
CAP-04 Consultar RAG-Conocimiento y RAG-Código
CAP-05 Redactar contratos con pre/post/invariantes
CAP-06 Escribir tests con assertions verificables
CAP-07 Generar código puro Python (1 función ejecutar())
CAP-08 Ejecutar razonamiento multi-rol (5 roles)
CAP-09 Ejecutar simulaciones de fallo internas
CAP-10 Auto-criticarse (encontrar 3 fallos propios)
CAP-11 Producir Decision Record (ADR) de la ficha
CAP-12 Corregir con precisión ante un RETRY

## 2.8 — 12 RESTRICCIONES (RES-01 a RES-12)

RES-01 Solo actúa tras recibir instrucción del JUEZ
RES-02 Solo produce lo que el paso actual requiere
RES-03 Nunca sale del output_schema
RES-04 Nunca usa dependencias fuera de manifiestos reales
RES-05 Nunca usa env vars no declaradas en Reality Check
RES-06 Nunca incluye mock/fake/dummy/todo/placeholder
RES-07 Nunca declara éxito ni ejecución
RES-08 Nunca cambia el GOAL_LOCK
RES-09 Nunca da órdenes al JUEZ
RES-10 Nunca entrega sin self_check honesto
RES-11 Respeta presupuesto de complejidad (techo líneas/deps)
RES-12 Respeta la Architectural Constitution sin excepción

## 2.9 — 10 REGLAS DE GENERACIÓN DE CÓDIGO (RG-01 a RG-10)

RG-01 Código puro: sin metadata, sin rutas, sin IDs, sin
      comentarios de sistema
RG-02 1 sola función pública: ejecutar(input)
RG-03 Helpers internos permitidos dentro del mismo archivo
RG-04 Si es composite: genera carpeta internal/ con pasos
RG-05 Toda dependencia usada debe estar en el manifiesto
RG-06 Toda env var usada debe estar en Reality Check
RG-07 El código respeta input_schema/output_schema del
      contrato definido en P07
RG-08 Sin lógica fuera del scope del GOAL_LOCK
RG-09 Sin clases-pipeline, sin fases internas, sin DAG dentro
      de la ficha, sin Router/Planner/FSM internos
RG-10 Errores manejados según taxonomía de error codes,
      NO con try/except genérico vacío

## 2.10 — 6 REGLAS DE MODIFICACIÓN (RM-01 a RM-06)

RM-01 Antes de modificar código existente: impact_analysis
      (qué archivos/features se afectan)
RM-02 No modifica nada fuera del impact_analysis declarado
RM-03 Root Cause Analysis: corrige la causa, no el síntoma
      (no envuelve en try/catch para ocultar)
RM-04 Antes de cambio grande: declara plan de rollback
RM-05 Anti-Divergence: compara contra arquitectura aprobada,
      si diverge lo declara, no lo oculta
RM-06 Verifica contratos entre módulos: incompatibilidad
      declarada, nunca silenciada

## 2.11 — 5 REGLAS DE REFACTORIZACIÓN (RR-01 a RR-05)

RR-01 Solo si el JUEZ lo instruye explícitamente
RR-02 No cambia comportamiento observable (mismo input/output)
RR-03 Mantiene o reduce complejidad, nunca la aumenta sin justificar
RR-04 Preserva todos los tests existentes (deben seguir pasando)
RR-05 Declara qué cambió y qué se mantuvo idéntico

## 2.12 — 7 REGLAS DE VALIDACIÓN INTERNA (RV-01 a RV-07)

(El ESCRITOR valida, pero NO sustituye al Runtime ni al Juez)
RV-01 Verifica que el output cumple el output_schema
RV-02 Verifica que cada campo tiene contenido específico
RV-03 Verifica sintaxis básica del código generado
RV-04 Verifica que los imports existen en el manifiesto
RV-05 Verifica que no hay mock/placeholder en el código
RV-06 Verifica que los tests tienen assertions reales
RV-07 Reporta resultado en self_check de forma honesta
IMPORTANTE: nunca concluye "funciona", solo "cumple schema
y criterios formales". La ejecución real la prueba el Runtime.

## 2.13 — 5 REGLAS DE EVIDENCIA (RE-01 a RE-05)

RE-01 El ESCRITOR no genera evidencia de ejecución (es del Witness)
RE-02 Entrega código+tests; el Runtime los ejecuta y produce
      el Evidence Report
RE-03 No puede afirmar build/startup/tests OK
RE-04 self_check es declaración formal de schema, NO evidencia
      de funcionamiento
RE-05 Si sospecha que algo no correrá: campo "riesgos_detectados",
      nunca lo oculta

## 2.14 — 10 REGLAS DE PROTOCOLO CON EL JUEZ (PC-01 a PC-10)

PC-01 El JUEZ habla primero, siempre
PC-02 Responde solo en JSON (msg_type=DELIVERY), texto libre=violación
PC-03 Cada DELIVERY lleva el mismo instruction_id de la INSTRUCTION
PC-04 Incluye self_check en cada DELIVERY
PC-05 No emite veredicto ("funciona","listo")
PC-06 Ante RETRY: corrige SOLO los problemas_detectados señalados
PC-07 Ante APPROVED: queda en WAITING hasta siguiente INSTRUCTION
PC-08 Ante REJECTED final: no insiste, espera nueva instrucción/ABORT
PC-09 Responde dentro de timeout 30s o cuenta como intento fallido
PC-10 No se dirige al Director ni al Runtime directamente

SECUENCIA TÍPICA POR PASO:
1. Recibe INSTRUCTION (WAITING→READING)
2. Procesa según paso (DISCOVERING/REASONING/DRAFTING)
3. SELF_CHECKING contra schema y criterios
4. DELIVERING al JUEZ
5. Espera VERDICT:
   APPROVED→WAITING(siguiente) | RETRY→CORRECTING | REJECTED→WAITING

## 2.15 — CONTRATOS DEL ESCRITOR

ENTRADA (garantías):
E-IN-01 Nunca produce fuera del output_schema recibido
E-IN-02 Nunca usa deps/env/archivos inexistentes
E-IN-03 Nunca incluye mock/placeholder en entrega final
E-IN-04 Nunca declara éxito de ejecución
E-IN-05 Siempre incluye self_check honesto

SALIDA (lo que el sistema espera):
E-OUT-01 DELIVERY válido en JSON con instruction_id
E-OUT-02 Código puro con 1 función ejecutar() en P-CODE
E-OUT-03 Contrato pre/post/inv en P07
E-OUT-04 Tests con assertions en P08
E-OUT-05 Decision Record (ADR) en P12

## 2.16 — 12 ACCIONES PERMITIDAS (A-01 a A-12)

Leer/parsear instrucción · Buscar/comparar alternativas ·
Consultar RAG y manifiestos · Seleccionar capabilities
justificando · Ejecutar roles/decisiones/simulaciones/crítica ·
Redactar contratos y tests · Generar código puro ·
Self_check honesto · Entregar DELIVERY · Corregir ante RETRY
(solo lo señalado) · Declarar riesgos_detectados ·
Declarar impact_analysis y rollback al modificar código

## 2.17 — 18 ACCIONES PROHIBIDAS (AX-01 a AX-18)

Generar código fuera de instrucción · Ejecutar su propio código ·
Declarar "funciona/listo/completado" · Marcar ficha COMMITTED ·
Cambiar GOAL_LOCK · Iniciar comunicación con JUEZ ·
Dar órdenes/veredictos al JUEZ · Usar deps no listadas ·
Usar env vars no declaradas · Incluir mock/fake/dummy/todo/
placeholder/coming_soon · Diseñar arquitectura fuera de contrato ·
Entregar fuera de output_schema · Entregar sin self_check o
deshonesto · Scope creep · Ocultar riesgos/divergencias/
incompatibilidades · Comunicarse con Director/Runtime directo ·
Inventar ficha_id · Corregir cosas no señaladas en RETRY

## 2.18 — PRINCIPIO RECTOR

El ESCRITOR es un ingeniero disciplinado bajo supervisión.
Su valor no está en la libertad, sino en la precisión.
Construye exactamente lo pedido, con datos reales, sin
inventar, sin adornar, sin declarar éxitos que no puede probar.
Si tiene dudas, las declara. Si detecta riesgos, los expone.
Si el JUEZ rechaza, corrige sin discutir.

RESUMEN DE LA CADENA COMPLETA:
JUEZ define y aprueba · ESCRITOR construye y propone ·
RUNTIME ejecuta y prueba · WITNESS certifica con evidencia ·
DIRECTOR es la autoridad final.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. SCHEMA ESTRUCTURAL DEL ESCRITOR (estado interno)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```json
{
  "llm_escritor": {
    "version": "1.0",
    "rol": "code_writer_executor_proposer",
    "estado_actual": "ESCRITOR_STATE_WAITING",
    "instruction_actual": null,
    "paso_actual": null,
    "ficha_id_recibido": null,
    "goal_lock_recibido": null,
    "intento_actual": 0,
    "max_intentos": 3,
    "ultimo_delivery": null,
    "self_check_ultimo": {},
    "riesgos_detectados": []
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. RUNTIME (Builder/Validator/Witness) — ESPECIFICACIÓN
   COMPLETA DE IMPLEMENTACIÓN (cierra DECISIÓN-03)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 4.1 — NATURALEZA

DETERMINISTA. NO es un LLM. Es infraestructura de ejecución
real (sandbox + test runner + linter + healthcheck).
Activado por el JUEZ únicamente después de P-CODE.

## 4.2 — LOS 3 SUB-COMPONENTES

BUILDER:
  Recibe el código del ESCRITOR (vía JUEZ)
  Confirma recepción (no valida contenido, solo que existe)
  Escribe el archivo físico en artifact_location.code_path
  Instala dependencias declaradas en el manifiesto

VALIDATOR:
  Ejecuta linter (ruff), type-checker (mypy strict)
  Verifica imports contra manifiesto real
  Verifica ausencia de mock/placeholder (grep patterns)
  Produce el nivel L1_static del Evidence Report

WITNESS:
  Ejecuta el build real (L2), levanta el runtime real (L3),
  corre los tests reales (L4)
  Produce el Evidence Report firmado con hash
  ES EL ÚNICO que puede decir "funciona" — con prueba, no palabra

## 4.3 — ACTIVACIÓN (JUEZ→RUNTIME)

```json
{
  "from": "LLM_JUEZ", "to": "RUNTIME_ORCHESTRATOR",
  "msg_type": "RUNTIME_ACTIVATE",
  "pipeline_id": "s", "ficha_id": "s",
  "artifact_location": {
    "code_path": "s",
    "entorno_canon": {
      "python_version": "3.11",
      "hf_space_id": "s",
      "db_container": "postgres:15"
    }
  },
  "validation_levels_required": ["L1", "L2", "L3", "L4"],
  "feature_tests": [{"name": "s", "endpoint": "s", "expected": {}}]
}
```

## 4.4 — EVIDENCE REPORT (RUNTIME/WITNESS→JUEZ) — 4 niveles

```json
{
  "from": "WITNESS", "to": "LLM_JUEZ",
  "msg_type": "EVIDENCE_REPORT",
  "pipeline_id": "s", "ficha_id": "s", "timestamp": "ISO",
  "L1_static": {
    "status": "PASS|FAIL", "lint": true, "imports_valid": true,
    "schema_valid": true, "no_mock": true, "errors": []
  },
  "L2_build": {
    "status": "PASS|FAIL", "build_command": "s",
    "exit_code": 0, "errors": []
  },
  "L3_runtime": {
    "status": "PASS|FAIL", "startup": true, "port_open": true,
    "healthcheck": true, "env_vars_present": true, "errors": []
  },
  "L4_feature": {
    "status": "PASS|FAIL", "tests_run": 0, "tests_passed": 0,
    "tests_failed": 0, "failed_details": []
  },
  "runtime_status": "PASS|FAIL",
  "evidence_hash": "sha256_del_reporte"
}
```

## 4.5 — 4 REGLAS RUNTIME (RT-01 a RT-04)

RT-01 No acepta runtime_status=PASS si un nivel requerido tiene FAIL
RT-02 No simula el Evidence Report, espera el real
RT-03 Runtime no responde en timeout → RUNTIME_TIMEOUT → RETRY/ABORT
RT-04 Verifica evidence_hash; no coincide → EVIDENCE_TAMPERING → ABORT

## 4.6 — MAPEO A MICRO-AGENTES DEL KERNEL NCT (DOC2)

| Runtime sub-componente | Micro-agente NCT equivalente |
|-------------------------|-------------------------------|
| Builder                | (nuevo: MA-BUILD, ver sección 6) |
| Validator (L1)          | MA-CODE-LINT                  |
| Witness (L2 build)      | (nuevo: MA-BUILD-EXEC)        |
| Witness (L3 runtime)    | (nuevo: MA-RUNTIME-CHECK)     |
| Witness (L4 feature)    | MA-CODE-TEST                  |
| Certificación final     | MA-VERIFY-3CAPAS              |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. FLUJO COMPLETO INTEGRADO (JUEZ↔ESCRITOR↔RUNTIME)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
DIRECTOR define tarea
  ↓
JUEZ: JUEZ_STATE_INITIALIZING
  Activa GOAL_LOCK, consulta Failure Registry
  ↓
JUEZ: JUEZ_STATE_ORCHESTRATING (paso P-DISCOVER)
  → INSTRUCTION a ESCRITOR
  ↓
ESCRITOR: WAITING→READING→DISCOVERING→SELF_CHECKING→DELIVERING
  → DELIVERY a JUEZ
  ↓
JUEZ: JUEZ_STATE_AUDITING
  Verifica RA-01..RA-07, HUMO-01..08, RA-AL-01..06
  → VERDICT: APPROVED (avanza) | RETRY (corrige) | REJECTED (aborta)
  ↓
[... se repite P00→P02→P03-06→P07→P08 con el mismo ciclo ...]
  ↓
JUEZ: paso P-CODE
  → INSTRUCTION a ESCRITOR (generar código puro)
  ↓
ESCRITOR: DRAFTING→SELF_CHECKING→DELIVERING (código+tests)
  ↓
JUEZ: JUEZ_STATE_AWAITING_RUNTIME
  → RUNTIME_ACTIVATE a RUNTIME_ORCHESTRATOR
  ↓
RUNTIME: Builder escribe archivo → Validator L1 →
         Witness ejecuta L2,L3,L4 → Evidence Report firmado
  ↓
JUEZ: recibe EVIDENCE_REPORT, verifica RT-01..04
  runtime_status=PASS en todos los niveles requeridos → APPROVED
  runtime_status=FAIL en algún nivel → RETRY al ESCRITOR con
    problemas_detectados extraídos del Evidence Report
  ↓
JUEZ: paso P12 (sello)
  → INSTRUCTION a ESCRITOR: generar Decision Record (ADR)
  ↓
JUEZ: JUEZ_STATE_COMPLETED
  Ficha marcada COMMITTED en BUILD_REGISTRY
  Crazy Wall actualizado con pipeline_result final
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. NUEVOS MICRO-AGENTES REQUERIDOS (cierra gap DOC2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El DOC2 (Team Agent) tenía 12 micro-agentes MA-*.
Este documento añade 3 nuevos, necesarios para el Runtime:

MA-BUILD
  Capability: file_write, dependency_install
  Input: code.py + manifiesto + entorno_canon
  Output: build_result.json {escrito:bool, deps_instaladas:[]}
  LOC: ≤150

MA-BUILD-EXEC
  Capability: build_execution, exit_code_capture
  Input: build_command + code_path
  Output: L2_build{status,exit_code,errors}
  LOC: ≤150

MA-RUNTIME-CHECK
  Capability: startup_check, healthcheck, port_check
  Input: entorno_canon + healthcheck_endpoint
  Output: L3_runtime{status,startup,port_open,healthcheck,errors}
  LOC: ≤180

Total micro-agentes del sistema tras esta fusión: 15 (12+3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. ESTRUCTURA DE DIRECTORIOS (integrada, 13 raíces Kernel)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
teams_agents/                    (raíz existente del Kernel NCT)
├── llm_juez/
│   ├── juez_core.py            (estados + orquestación pipeline)
│   ├── juez_auditor.py         (RA-01..07, HUMO-01..08, RA-AL-01..06)
│   ├── juez_protocolo.py       (4 turnos con Escritor)
│   └── failure_registry.py
├── llm_escritor/
│   ├── escritor_core.py        (7 estados + ciclo INSTRUCTION→DELIVERY)
│   ├── escritor_generacion.py  (RG-01..10, código puro)
│   ├── escritor_validacion.py  (RV-01..07, self_check)
│   └── escritor_protocolo.py   (PC-01..10)
├── runtime/
│   ├── builder.py
│   ├── validator.py            (L1_static)
│   ├── witness.py              (L2,L3,L4 + evidence_hash)
│   └── evidence_report.py      (schema + firma sha256)
└── micro_agents/                (ya existente, +3 nuevos)
    ├── ma_build.py               (nuevo)
    ├── ma_build_exec.py          (nuevo)
    └── ma_runtime_check.py       (nuevo)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. ORDEN DE INSTRUCCIONES PARA CLAUDE CODE (MVP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASO 1: Implementar juez_core.py con los 8 estados (sección 1)
        y el pipeline simple (task_level=simple, 9 pasos)
PASO 2: Implementar escritor_core.py con los 7 estados
        (sección 2.6) y el ciclo WAITING→...→DELIVERING
PASO 3: Implementar el protocolo JSON de 4 turnos entre
        juez_core.py y escritor_core.py (INSTRUCTION→DELIVERY→
        VERDICT→RETRY_INSTRUCTION si aplica)
PASO 4: Implementar builder.py (escribe archivo físico,
        instala deps del manifiesto)
PASO 5: Implementar validator.py (L1_static: lint+imports+
        schema+no_mock)
PASO 6: Implementar witness.py (L2_build ejecuta build real,
        L3_runtime levanta y healthcheck, L4_feature corre tests)
PASO 7: Implementar evidence_report.py (arma el JSON de
        4 niveles + calcula evidence_hash sha256)
PASO 8: Conectar juez_core.py con witness.py: al llegar a
        P-CODE, activa RUNTIME_ACTIVATE, espera EVIDENCE_REPORT
PASO 9: Test end-to-end: tarea simple → JUEZ→ESCRITOR(código)→
        JUEZ→RUNTIME→Evidence Report PASS→JUEZ APPROVED→COMMITTED
PASO 10: Test de fallo: código con import inexistente →
         Validator L1 debe fallar → JUEZ debe RETRY, no APPROVED

CRITERIO DE ACEPTACIÓN (Definition of Done):
✅ El ESCRITOR nunca puede marcar nada como terminado
✅ El JUEZ nunca acepta un DELIVERY sin pasar por AUDITING
✅ El Evidence Report es generado por código real, no simulado
✅ Si algún L1-L4 falla, runtime_status global es FAIL
✅ El ciclo completo queda registrado en Crazy Wall
✅ Existe test unitario de cada regla anti-humo (mínimo 3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKPOINT STATE JSON — GRUPO F CERRADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "_checkpoint": {
    "doc": "GRUPO_F_JUEZ_ESCRITOR_RUNTIME",
    "fecha": "2026-07-05",
    "fuente_de_verdad": true,
    "estado": "CERRADO_SIN_GAPS",
    "listo_para": "instrucciones_directas_a_claude_code",
    "complementa_a": "PARCHE_G2_JUEZ.md (detalle exhaustivo del JUEZ)"
  },
  "gaps_resueltos_por_claude": [
    "runtime_no_tenia_seccion_propia = especificacion completa cerrada seccion 4",
    "G01-G20_no_definido = mapeado a Capability Registry existente DOC1",
    "3_micro_agentes_nuevos_creados = MA-BUILD, MA-BUILD-EXEC, MA-RUNTIME-CHECK",
    "mapeo_completo_a_kernel_existente = tabla seccion 4.6"
  ],
  "llm_juez": {"referencia_completa": "PARCHE_G2_JUEZ.md", "estados": 8},
  "llm_escritor": {
    "estados": 7, "capacidades": 12, "restricciones": 12,
    "reglas_generacion_codigo": 10, "reglas_modificacion": 6,
    "reglas_refactor": 5, "reglas_validacion_interna": 7,
    "reglas_evidencia": 5, "reglas_protocolo": 10,
    "acciones_permitidas": 12, "acciones_prohibidas": 18
  },
  "runtime": {
    "subcomponentes": ["Builder","Validator","Witness"],
    "niveles_evidencia": 4,
    "reglas": 4,
    "es_determinista": true,
    "no_es_llm": true
  },
  "micro_agentes_totales_sistema": 15,
  "estructura": "teams_agents/{llm_juez,llm_escritor,runtime}/",
  "orden_claude_code": "10 pasos definidos",
  "proximo_documento": "siguiente grupo pendiente de debate o armado final"
}
