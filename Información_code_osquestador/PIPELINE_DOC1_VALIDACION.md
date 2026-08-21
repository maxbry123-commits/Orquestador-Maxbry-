# NCT — DOCUMENTO 1 — VALIDACIÓN PREVIA A LA CONSTRUCCIÓN
# Auditoría de bandeja (3 pasadas) + verificación cruzada contra artefactos
# Fecha: 2026-07-16 | Este documento NO es el PIPELINE final — es el
# control de calidad que debe pasar ANTES de construirlo

## RESUMEN EN 5 LÍNEAS

La bandeja del proyecto define un roadmap macro de 21 fases numeradas
00-20 (idea, arquitectura, frontend, backend, testing, deploy, agentes,
etc.), NO las 6 estaciones del pipeline de ejecución (F-1 a F5) que
había estado usando como referencia. Encontré una construcción propia
de esta sesión (`atlas/fase_runner.py`) que usa el nombre "21 fases"
pero para una lista de contenido distinto. Esto se corrige antes de
seguir. El resto del sistema cruza limpio contra lo ya construido.

---

## PASADA 1 — Estructura del roadmap de 21 fases

**Fuente:** SALIDA_04_PIPELINE_RAIZ_MEJORA_100.md, SALIDA_10 (HTML),
PARCHE_GUIA_MAESTRO.md

El roadmap tiene 21 fases numeradas 00 a 20, agrupadas en 5 bloques
temáticos:

| Bloque | Fases | Motor que las ejecuta |
|---|---|---|
| 00 · Raíz | raíz maestra | Ejecutor de fases + gestor de espacio de trabajo |
| Diseño | idea · arquitectura · UX | Motor de consenso (10 roles) + plantillas de arquitectura |
| Construcción | frontend · backend · ingeniería de datos | Equipo de agentes + staff ejecutor |
| Calidad | testing · seguridad de desarrollo · autoevaluación | Entorno aislado L1-L4 + verificador + integración continua |
| Operación | despliegue · analítica · documentación · base de conocimiento | Integración final + paneles de rol + destilado de aprendizaje |
| 11 · Agentes de IA | (la fase que el sistema NCT llena) | Todo el sistema — ya cubierta ~70% |

**Mecanismo de ejecución:** un componente (`FASE_RUNNER`) lee un
archivo fuente (`biblioteca_21fases.md`, 10.613 líneas, 251 puntos de
control) y genera `fases.json`. Cada fase activada por el Director se
convierte en una tarea que entra al pipeline de ejecución estándar
(las mismas 6 estaciones F-1 a F5 que ya construí) como cualquier otra
tarea — no tiene un motor separado.

**Hallazgo 1 — archivo fuente incompleto:** el archivo
`biblioteca_21fases.md` con el texto literal de las 21 fases y sus 251
puntos de control **no está presente en la bandeja del proyecto** —
solo su descripción y categorías. Sin este archivo no se puede
reconstruir el contenido exacto de cada fase, solo su estructura.

---

## PASADA 2 — Mejoras ya aprobadas sobre el roadmap (M-01 a M-06)

**Fuente:** SALIDA_04, SALIDA_08A (segmento S24)

| Código | Mejora | Estado según bandeja |
|---|---|---|
| M-01 | Motor que parsea el archivo fuente automáticamente | Diseño aprobado |
| M-02 | Cada punto de control gana un criterio de verificación medible | Diseño aprobado |
| M-03 | Dependencias entre fases (grafo, no lista plana) | Diseño aprobado |
| M-04 | Fase 11 (Agentes de IA) pre-llenada al 70% con componentes reales | Diseño aprobado |
| M-05 | Cierre de fase requiere verificación formal + acta, nunca de palabra | Diseño aprobado |
| M-06 | Cada fase recibe entre 10 y 50 sub-metas (progreso medible fino) | Diseño aprobado |

Orden de construcción documentado para el segmento S24 (fase runner):
parser → dependencias → verificaciones → integración → verificación
final.

---

## PASADA 3 — Conteo canónico y estado de aprobación

**Fuente:** SALIDA_09, ACTA_DECISIONES_DIRECTOR.md, SALIDA_10

- Cifra oficial de unidades de trabajo: **325 fichas** (322 base + 3
  añadidas) sobre **16 repositorios**.
- El Director ya aprobó globalmente con la frase registrada:
  *"Ok necesito te apruebo todo las mejoras y las soluciones de todos
  los gaps"* — esto cierra los 15 puntos pendientes de diseño (G-01 a
  G-15) como aprobados.

**Hallazgo 2 — discrepancia numérica menor:** el acta de aprobación del
Director registra la cifra como **322/16**, mientras que el documento
de aprobación previo (SALIDA_09) y el HTML de referencia (SALIDA_10)
usan **325/16** (322 + 3 unidades añadidas después). Es probablemente
un desfase de secuencia entre documentos, no una contradicción real,
pero **queda pendiente de confirmación explícita con el Director** cuál
es la cifra final: 322 o 325.

---

## VERIFICACIÓN CRUZADA — bandeja vs. artefactos construidos en este chat

| Elemento de la bandeja | ¿Está construido en este chat? | Coincide con el diseño |
|---|---|---|
| Motor de bus (16 módulos con frontera) | Sí — `motores/motor_bus.py` + 16 manifiestos | Sí |
| Ejecutor de fases (FASE_RUNNER) | Sí — `atlas/fase_runner.py` | **No — ver Hallazgo 3** |
| Verificación formal (GCL + solver) | Sí — `gcl/z3_gate.py`, `gcl/gcl_lite.py` | Sí |
| Motor de bucles + catálogo | Sí — `loop_engine/*.py` | Sí |
| Consenso de 10 roles | Sí — `decision/consenso10.py` | Sí (quorum 6/10 idéntico) |
| Tablas de mapeo (jueces, principios, etc.) | Sí — `mapeos/tablas.yaml` | Sí |
| Configuración de modelos y llaves | Sí — `router/providers.yaml` | Sí (9 locales + 16 llaves) |
| Fichas con formato de 5 campos | Sí — `fichas/generador.py` + 20 fichas reales | Sí |
| Interfaz del sistema en producción | Sí — 7 paneles construidos | Cobertura parcial, sin conflicto |
| Gobernanza y registro de firmas | Sí — `gobernanza/ledger.py` | Sí |
| **Archivo fuente `biblioteca_21fases.md`** | **No existe en ningún lado accesible** | — |

### Hallazgo 3 — CRÍTICO: el ejecutor de fases construido no representa el roadmap real

`atlas/fase_runner.py`, construido en este chat, define una lista
interna de 21 pasos así:

```
ingesta, auditoria_docs, arbol_metas, task_index, goal_lock,
plan_offline, z3_gate, seguridad_entrada, huellas, clasificacion,
expertos, consenso, escritura, sandbox, witness, checks_salida,
reparacion, gate_final, entrega, distill, cierre_acta
```

Esto **no es el roadmap de 21 fases de la bandeja** (idea, arquitectura,
frontend, backend, testing, deploy, etc.). Es, en realidad, una
descripción de los pasos INTERNOS de una sola ejecución del pipeline
(las 6 estaciones F-1 a F5, desglosadas en más detalle). Ambas cosas
son válidas y necesarias, pero son conceptos distintos que terminaron
con el mismo nombre ("21 fases") por coincidencia numérica, causando
confusión.

**Acción requerida antes de construir el documento visual del
PIPELINE:** renombrar uno de los dos conceptos para eliminar la
ambigüedad. Propuesta:
- El roadmap macro (00-20, idea→arquitectura→...→agentes) se llama
  **"Fases del proyecto"** o **"Roadmap"**.
- La lista de 21 pasos internos que ya construí se renombra a algo
  como **"Sub-pasos de ejecución"** o se fusiona con las 6 estaciones
  existentes (F-1 a F5) para no duplicar conceptos.

Esto se resuelve en el Documento 2, antes de dibujar cualquier diagrama
de fases — necesito tu decisión sobre cuál nombre usar.

---

## PENDIENTES PARA CONFIRMAR ANTES DE CONTINUAR

1. ¿Cifra final: 322 o 325 fichas / 16 repositorios? (Hallazgo 2)
2. ¿Cómo renombrar el conflicto "21 fases" vs "21 pasos internos"?
   (Hallazgo 3 — bloqueante para el Documento 2)
3. El archivo fuente completo del roadmap (`biblioteca_21fases.md`) no
   está disponible — ¿lo tienes en algún otro lado, o el PIPELINE debe
   trabajar solo con las categorías resumidas que sí están documentadas?

---

## PRÓXIMO PASO

Con tus respuestas a los 3 puntos de arriba, arranco el Documento 2 del
PIPELINE (visual, con la paleta y formato ya aprobados) organizado por
las fases reales del roadmap — no por mis propias "salidas" de
construcción, que fue como lo estructuré antes por error.
