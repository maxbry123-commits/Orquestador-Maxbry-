# PLANTILLA DE ESPECIFICACIÓN TÉCNICA DE MÓDULO
## Instrucciones operativas para que cualquier IA estructre el diseño de un agente, orquestador, conector o subsistema.

---

## 0. METADATOS DEL DOCUMENTO

| Campo | Valor |
|---|---|
| Nombre del módulo | — |
| Versión de la especificación | 1.0.0 |
| Fecha | — |
| Autor del documento | — |
| Estado | Borrador / Revisión / Aprobado |
| Dependencias aguas arriba | — |
| Consumido por | — |
| Sustituye a | — |

> Esta plantilla es la única forma válida de documentar un módulo dentro del proyecto. Cualquier desviación se considera una propuesta de cambio arquitectónico y debe pasar por revisión.

---

## 1. NOMBRE DEL MÓDULO

Identificador único del componente. Debe coincidir con el nombre del directorio que lo contiene y con el `name` en su `manifest.json`. Sin espacios. En minúsculas y `snake_case`.

---

## 2. OBJETIVO

Una sola frase. Imperativa. Sin ambigüedad. Ejemplo: "Garantizar la idempotencia del procesamiento de documentos en la fase de ingesta".

---

## 3. FILOSOFÍA DEL MÓDULO

Por qué existe este módulo y por qué se diseñó así. No qué hace, **por qué**. Tres a cinco frases máximo. Debe responder:

- Qué problema del sistema evita.
- Qué principio de diseño encarna.
- Qué invariante protege.

---

## 4. ALCANCE

### Qué hace
Lista exhaustiva y verificable.

### Qué NO hace
Lista exhaustiva y verificable. Tan importante como la anterior: previene el scope creep.

---

## 5. PROBLEMA QUE RESUELVE

Descripción concreta del fallo, fricción o riesgo que motivó la creación del módulo. Sin generalidades.

---

## 6. DECISIONES DE ARQUITECTURA

Lista numerada. Cada decisión:

- **Decisión:** enunciado.
- **Motivo:** razón técnica explícita.
- **Consecuencia:** qué implica, qué restricción introduce.
- **Trade-off aceptado:** qué se sacrificó.

---

## 7. ALTERNATIVAS EVALUADAS Y DESCARTADAS

Para cada decisión crítica de la sección 6, nombrar al menos una alternativa descartada y el motivo.

| Decisión | Alternativa | Motivo del descarte |
|---|---|---|
| — | — | — |

---

## 8. COMPONENTES INTERNOS

Subdivisión lógica del módulo. Para cada uno:

- Nombre.
- Responsabilidad (una frase).
- Interfaz pública (entradas/salidas, no firmas de funciones).
- Estado propio (persistente o volátil).

---

## 9. RESPONSABILIDADES

Lista cerrada de verbos en infinitivo. Cada responsabilidad debe ser:

- Accionable por una sola función del componente.
- Verificable.
- Perteneciente a este módulo, no a sus vecinos.

---

## 10. INTERFACES PÚBLICAS

Cada interfaz debe especificar:

- Nombre.
- Propósito (una frase).
- Precondiciones que el llamante debe cumplir.
- Postcondiciones garantizadas.
- Efectos colaterales observables (escrituras, I/O, notificaciones).
- Modalidad: síncrona / asíncrona / fire-and-forget.

Nombrar también las interfaces **implícitas** (manifest.json, health endpoint, eventos publicados).

---

## 11. CONTRATOS

### Contrato funcional
Lista de invariantes que el módulo garantiza siempre. Si alguna fallara, el módulo es incorrecto aunque su salida parezca válida.

### Contrato de datos
Esquema de cada entidad que el módulo emite o consume. Versiones semánticas. Compatibilidad hacia atrás comprometida (sí/no, hasta cuándo).

### Contrato de errores
Catálogo cerrado de tipos de error, sus códigos, su significado y la respuesta esperada del consumidor.

---

## 12. ENTRADAS

| Origen | Tipo de dato | Frecuencia esperada | Volumen máximo | Validaciones |
|---|---|---|---|---|

Para cada entrada:

- Formato aceptado (no el formato único interno, sino los aceptados a la entrada).
- Caracteres / estructuras prohibidas.
- Comportamiento ante entrada inválida (rechazo, cuarentena, normalización).

---

## 13. SALIDAS

| Destino | Tipo de dato | Frecuencia | Garantía de entrega | Idempotencia |
|---|---|---|---|---|

Para cada salida:

- Esquema exacto.
- Cuándo se emite.
- Qué garantiza el módulo sobre el destinatario.
- Política de reintento si el destinatario falla.

---

## 14. ESTADOS INTERNOS

Diagrama textual (no gráfico) de los estados posibles y las transiciones legales. Incluir el estado inicial, el estado final estable y los estados transitorios.

**Regla:** Todo estado no documentado se considera bug.

---

## 15. FLUJO COMPLETO DE EJECUCIÓN

Secuencia numerada, paso a paso, del camino feliz. Debe responder "¿qué pasa literalmente cuando llega un documento / evento / comando X?".

Para cada paso:

- Acción concreta.
- Módulo responsable.
- Si modifica estado, indicar a qué estado lleva.

---

## 16. CASOS ESPECIALES

Comportamientos que **se desvían del camino feliz pero son parte del contrato**. Ejemplos: primer arranque, arranque en frío, reinicio tras crash, fase 0 vacía, etc.

---

## 17. CASOS LÍMITE

Lista cerrada. Cada caso:

- Entrada.
- Comportamiento esperado.
- Justificación.

**Regla:** si un caso límite no está en la lista, el comportamiento del módulo es indefinido.

---

## 18. REGLAS DE NEGOCIO

Lista enumerada. Imperativas. Sin excepciones implícitas. Ejemplos válidos:

- "Un documento cuyo `hash` ya existe en el inventario no se reprocesa."
- "Una fusión siempre genera un documento nuevo; los originales se archivan."

---

## 19. POLÍTICAS

Normas que el módulo aplica y que provienen de una capa superior (políticas globales del orquestador). Cada política debe referenciar al documento que la origina.

---

## 20. SEGURIDAD

- Autenticación / autorización esperada.
- Manejo de secretos (cómo entran, cómo se almacenan, cómo se rotan).
- Datos sensibles: qué se redacta en logs, qué se cifra en reposo, qué sale del sistema.
- Ataques específicos que el módulo mitiga.
- Principios de mínimos privilegios asumidos.

---

## 21. MANEJO DE ERRORES

| Tipo de error | Detección | Acción | Notificación | Recuperación |
|---|---|---|---|---|

Para cada error:

- Cómo se detecta.
- Si es transitorio o permanente.
- Política de reintentos.
- Cuándo escala a `dead_letter` o equivalente.
- Qué información se loguea (nunca payloads completos de secretos).

---

## 22. RECUPERACIÓN ANTE FALLOS

- Estado se restaura desde… (journal, snapshot, registry).
- Qué se considera estado consistente.
- Qué operaciones son idempotentes.
- Qué pasa si el módulo arranca con estado corrupto.
- Qué pasa si el módulo arranca sin red / sin disco / sin reloj.

---

## 23. CONFIGURACIÓN

Cada clave de configuración:

- Nombre, tipo, valor por defecto.
- Si es obligatoria u opcional.
- Si admite recarga en caliente.
- Si es sensible (secret).

Formato recomendado: tabla.

---

## 24. DEPENDENCIAS

| Dependencia | Tipo | Versión mínima | Obligatoria | Justificación |
|---|---|---|---|---|

Incluir:

- Dependencias de otros módulos del proyecto.
- Dependencias externas (librerías, servicios, protocolos).
- Versiones fijadas con motivo.

---

## 25. INTEGRACIÓN CON OTROS MÓTODULOS

Lista de módulos que dependen de este y de los que este depende. Para cada relación:

- Dirección (proveedor / consumidor).
- Protocolo o interfaz compartida.
- Acoplamiento (puntual / continuo / bidireccional).

---

## 26. RESTRICCIONES

Lo que este módulo **no puede hacer** aunque se lo pidan. Formato imperativo, no explicativo.

---

## 27. RENDIMIENTO ESPERADO

- Latencia p50 / p95 / p99 esperada.
- Throughput esperado en operación normal y en pico.
- Uso de memoria en estado estable.
- Uso de CPU en estado estable.

Si el rendimiento es crítico, indicar también el comportamiento bajo carga máxima.

---

## 28. ESCALABILIDAD

- Horizontal: ¿admite múltiples instancias? ¿cómo se coordinan?
- Vertical: ¿qué recursos son limitantes?
- Punto de ruptura esperado.

---

## 29. OBSERVABILIDAD

- Health check: ruta, formato de respuesta, frecuencia.
- Métricas expuestas (nombre, tipo, etiquetas).
- Logs estructurados: campos, niveles, destinos.
- Traces distribuidos: spans emitidos, atributos clave.
- Señales externas aceptadas (webhooks, eventos push).

---

## 30. REGISTRO DE EVENTOS (LOGGING)

- Formato del log (estructurado sí/no, esquema concreto).
- Niveles y cuándo se usa cada uno.
- Qué información nunca se loguea (secretos, PII, payloads completos).
- Rotación y retención.
- Correlación: cómo se enlazan eventos del mismo flujo (request_id, doc_id, workflow_id).

---

## 31. MÉTRICAS

Lista de métricas concretas con nombre, tipo (counter, gauge, histogram) y propósito. Sin métricas decorativas: cada métrica debe responder una pregunta operacional.

---

## 32. ROBUSTEZ

- Técnicas aplicadas (atomic writes, circuit breakers, retries con backoff, deduplicación, idempotencia).
- Límites concretos (reintentos máximos, cooldown, tamaño máximo de cola).
- Qué tipo de fallo se considera aceptable vs inaceptable.

---

## 33. CRITERIOS DE ACEPTACIÓN

Lista de criterios verificables. Cada uno:

- Condición medible.
- Cómo se mide.
- Resultado esperado.

Sin criterios de aceptación no hay módulo terminado.

---

## 34. PRUEBAS RECOMENDADAS

- Tipos de prueba aplicables (unit, integración, contrato, property-based, caos).
- Escenarios mínimos a cubrir.
- Datos de prueba representativos y adversarial (incluir entradas malformadas, vacías, masivas, concurrentes).
- Cómo se ejecutan en CI.

---

## 35. LIMITACIONES CONOCIDIDAS

Lista honesta de lo que el módulo **no puede** hacer hoy, aunque esté en su dominio. No son bugs. No son deuda. Son límites conocidos y aceptados.

---

## 36. POSIBLES EXTENSIONES FUTURAS

Lista priorizada (impacto / coste). No se implementan ahora. Sirven para evitar bloqueos arquitectónicos futuros.

---

## 37. RESUMEN EJECUTIVO

Máximo 10 líneas. Para un responsable de proyecto que no va a leer el resto. Tres bloques:

- Qué es y por qué existe.
- Qué problema resuelve hoy.
- Qué pasa si se elimina.

---

## 38. INSTRUCCIONES PARA FABELS

Esta especificación define la arquitectura y los requisitos funcionales del módulo. Constituye el contrato de implementación.

Fables no puede modificar, reinterpretar ni debilitar:

- El objetivo del módulo.
- La filosofía.
- La arquitectura definida.
- Los contratos e interfaces.
- Las reglas de negocio.
- El comportamiento esperado.
- El flujo lógico.
- Las políticas.
- El alcance.

Fables debe asumir que esta especificación representa el mínimo exigible. Su responsabilidad consiste en construir la mejor implementación posible, optimizando —cuando proceda— rendimiento, concurrencia, modularidad, mantenibilidad, legibilidad, robustez, resiliencia, tolerancia a fallos, seguridad, calidad de código, organización del proyecto, patrones de diseño, consumo de memoria, consumo de CPU, tiempos de respuesta, observabilidad, registro de eventos, cobertura de pruebas y capacidad de evolución futura.

Fables debe analizar de forma continua si la implementación puede mejorarse sin alterar el diseño. Si detecta una mejora que requiera modificar la arquitectura, NO debe implementarla directamente. En su lugar debe generar una **Propuesta de Cambio Arquitectónico** indicando: problema detectado, causa, solución propuesta, ventajas, riesgos, impacto sobre otros módulos, compatibilidad hacia atrás, coste de implementación y recomendación final. Solo tras la aprobación de la propuesta, esa mejora podrá incorporarse.

El objetivo es que cada implementación represente la máxima calidad técnica posible sin alterar la visión, el concepto ni los objetivos definidos para el módulo.
