# UOOS PARTE 1 — NCT_ARQUITECTURA
(generado por Motor TEMA A · doc origen sha256:dac8daaaf0aaa4f0…)

## B1 — MANIFEST
```yaml
{
  "proyecto": "NCT_ARQUITECTURA",
  "hash_documento_origen": "dac8daaaf0aaa4f0e3a8eae6b1dd39383b3d80a25e5097270028e40a367ce7df",
  "fases": 6,
  "archivos_declarados": 0,
  "requisitos_detectados": 3
}
```

## B2 — INVENTARIO
- (sin archivos declarados)

## B3 — REQUISITOS DETECTADOS
- Garantía: mismas entradas = misma decisión siempre
- Restricción: verifica SIEMPRE antes de ejecutar
- Regla: Agentes NUNCA tocan el cerebro.

## B4 — DAG DE FASES
```
F00 PECP — Plataforma Estructura de Construcción de Proyecto  (raíz)
F01 ARQUITECTURA GENERAL  <- depende de F00
F02 ESTRUCTURA REPO 1 (BRAIN)  <- depende de F01
F03 DB XATA  <- depende de F02
F04 REPO 2 (MODULES)  <- depende de F03
F05 OBJECT STORAGE  <- depende de F04
```

## B6 — PLAN DE TRIBUNAL
Secuencia 16 pasos (P-DISCOVER→P13) · umbral 70 · nada se entrega sin pasar el tribunal

## B7 — PLAN DE DESPLIEGUE
organizador_v2 --dry-run → aprobación del Director → ejecutar plan → verificar.py → evidence.json
