# DOCUMENTO 5 — BLOQUE 5: FORMATO DE SALIDA + ROMPECABEZAS
# VERSION FINAL

## 1. FORMATO OBLIGATORIO POR DOCUMENTO (7 SECCIONES)

SECCIÓN 1: ENCABEZADO JSON
SECCIÓN 2: TÍTULO LEGIBLE
SECCIÓN 3: RESUMEN EJECUTIVO (3-5 líneas)
SECCIÓN 4: ÍNDICE NUMERADO
SECCIÓN 5: CONTENIDO
SECCIÓN 6: MÓDULO ROMPECABEZAS
SECCIÓN 7: MINI ESTRUCTURA (origen / conecta_con / para_qué)

## 2. SISTEMA ROMPECABEZAS 🧩

```json
{
  "pieza_id": "ART-0001",
  "sistema": "CEREBRO | DATABASE",
  "vive_en": "REPO brain | REPO modules | Xata | Storage",
  "alimentado_por": ["pieza_id anterior"],
  "alimenta_a": ["pieza_id siguiente"],
  "rompe_si_falta": ["lista de impactados"],
  "contrato": "artifact_contract.json"
}
```

SISTEMA CEREBRO: orquestador, DAG, verifier, memoria, sequence.json, constitución
SISTEMA DATABASE: fichas, contratos, índices, código Python, logs

## 3. FLUJO DE CONEXIÓN

CEREBRO → DEPENDENCY_REGISTRY → Loader pide ficha → DB XATA
→ Storage entrega artifact_code.py → Verifier N0-N5
→ Executor en Space → Crazy Wall actualiza → GCL v1.0 gate F4

## 4. DOBLE LÉXICO OBLIGATORIO

🗣️ BÁSICO: explicación para no técnicos
⚙️ TÉCNICO: explicación con términos exactos
▶️ EJEMPLO: caso concreto de uso

## 5. ANTI-ALUCINACIÓN

- Si tiene fuente → citar fuente
- Si no tiene fuente → marcar [NO_ENCONTRADO]
- NUNCA inventar datos, rutas, nombres o versiones

## 6. NOTA HTML — FONDO NEGRO

Especificaciones:
- Fondo: #0a0e27
- Títulos: #00d4ff (cyan)
- Aprobados: #00ff00 (verde)
- Pendientes: #ff9800 (naranja)
- Rechazados: #ff4444 (rojo)
- Texto base: #e0e0e0

## 7. INSTRUCCIONES AI CON ÍNDICE DSL

Formato:
PASO 1: [acción] → [resultado esperado]
PASO 2: [acción] → [resultado esperado]
STOP_RULE: [condición de parada]

## 8. BLOQUES COPIABLES

═══ BLOQUE 1 DE N — [nombre] ═══
[contenido]
═══ FIN BLOQUE 1 ═══

## 9. [PENDIENTE_DIRECTOR]

Si algo no está definido → marcar [PENDIENTE_DIRECTOR]
STOP — no inventar — esperar aprobación.

## REGLAS:
- Kimi K → genera MD directo
- Claude / GPT → pedir permiso al Director antes de generar MD
- Si no puede generar MD → BLOQUE PYTHON + BLOQUE TXT copiables
