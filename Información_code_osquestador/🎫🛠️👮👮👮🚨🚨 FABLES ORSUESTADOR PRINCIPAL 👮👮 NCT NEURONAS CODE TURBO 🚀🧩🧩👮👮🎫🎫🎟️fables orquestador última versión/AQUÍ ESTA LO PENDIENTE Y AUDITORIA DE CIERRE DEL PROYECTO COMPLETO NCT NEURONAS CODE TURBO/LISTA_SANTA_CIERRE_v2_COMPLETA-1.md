# 🎅 LISTA DE SANTA v2 — CIERRE TOTAL NCT (COMPLETA)
# 2026-07-19 | Reemplaza a la v1 (la v1 quedó incompleta — corregido)
# D1-D12: ✅ APROBADAS POR EL DIRECTOR (registrado)
# Contiene: inventario TOTAL de gaps · 3 simulaciones · ruta completa · conteo de salidas

---

## PARTE 1 — QUÉ LE FALTABA A LA v1 (auto-auditoría de Santa)

| # | Faltaba | Ahora está en |
|---|---|---|
| F1 | 🚨 Capacidad de crear APP/WEB/SOFTWARE completo (el gap MÁS GRANDE de toda la auditoría, Salida 4/5) | Salidas S07-S09 |
| F2 | Embudo de entrada: idea vaga → requisitos estructurados (Fases 01/02/17) | Salida S07 |
| F3 | Las 325 fichas (P=0 código, S=0, T=0, E con numeración rota) | Salidas S10-S11 |
| F4 | Gaps del Auditor: detector de alucinaciones + plugins + credenciales | Salida S05 |
| F5 | LLM_JUEZ 16 pasos + fusión real de duplicados (D2/D3 firmadas pero el trabajo no estaba en la ruta) | Salida S04 |
| F6 | AUD-2P: auditoría de 2 pasadas sobre las 235 mejoras (prerrequisito del ACTA) | Salida S13 |
| F7 | Frontend final unificado (7 paneles + #8 en una sola experiencia) | Salida S14 |
| F8 | Prueba punta a punta REAL: idea → app desplegada (auditoría de capacidad) | Salida S15 |
| F9 | Escalado a 1000 agentes (plan por etapas) + piloto automático 24h | S01 (plan) + S04 (wiring) |
| F10 | Tabla constitución 39→14 (requiere localizar doc fuente en bandeja) | Salida S01 |

---

## PARTE 2 — LAS 3 SIMULACIONES DEL SISTEMA 🚂

### SIM-1: "Idea vaga → web app desplegada" (el caso de uso final)
```
Director escribe: "quiero una app de recetas con login"
  → Fase 01/02: ❌ FALLA — no existe embudo idea→requisitos
  → Fase 04 UX/UI: ❌ FALLA — no existe generador de Design System
  → Fase 05: ❌ FALLA — no existe ningún boilerplate (FastAPI/React/etc.)
  → Fase 06-14 (núcleo): ✅ PASA — pipeline escribe/prueba/certifica código
  → Despliegue: ✅ PASA — F22 probado (11/11 tests)
RESULTADO: 3 fallas → se resuelven con S07 (embudo) + S08-S09 (generador)
```

### SIM-2: "Documento de OTRO proyecto → UOOS 1 → construcción → UOOS 2 → despliegue"
```
Director sube documento aprobado de un proyecto X cualquiera
  → TEMA A (doc→UOOS1): ❌ FALLA — motor no construido (solo explicado)
  → Construcción con UOOS1: ✅ PASA — el formato v2 AUTORUN funciona
  → TEMA B (cierre→UOOS2): 🔶 PARCIAL — F22 existe pero sin config.yaml
    genérico ni multi-proyecto
  → Push a GitHub: 🔶 PARCIAL — sin verificación post-push, sin dry-run,
    sin bloqueo de secrets (riesgo: subir una API key por error)
RESULTADO: 1 falla + 2 parciales → se resuelven con S06 + S02
```

### SIM-3: "Falla a mitad de ejecución" (proveedor caído + archivo corrupto)
```
Proveedor LLM se cae durante una tarea del Router
  → Retry inmediato: ❌ FALLA — R5 no existe (todo sube a recovery general)
  → Circuit breaker: ❌ FALLA — R6 no existe (sigue mandando al caído)
  → Detección proactiva: ❌ FALLA — salud 30s no existe (se entera tarde)
  → Recovery general: 🔶 RIESGO — recovery.py duplicado (mío vs Fable)
    sin reconciliar = comportamiento impredecible
RESULTADO: 3 fallas + 1 riesgo → se resuelven con S03 + S04
```

### HALLAZGOS NUEVOS de las simulaciones (integrados a la ruta):
- **H1**: renumerar las fichas E ANTES de crear fichas nuevas (si no, el índice se corrompe) → primera tarea de S10
- **H2**: la prueba punta a punta merece salida propia con evidencia → S15 creada
- **H3**: el generador web/app necesita SUS PROPIOS tests (que genere un proyecto real y compile) → dentro de S09

---

## PARTE 3 — RUTA COMPLETA: 16 SALIDAS MÍNIMAS HASTA EL DESPLIEGUE

```
🎁 S01 · TRANSCRIBIR TODO LO FIRMADO
   6 archivos Fase A + tabla J1-J10 + mapeo loops (D9-A) + tabla 39→14
   + scale_plan 300→800→1000 + firma 325 aplicada
🎁 S02 · DESPLIEGUE v2.0 UNIVERSAL (~260 LOC)
   config.yaml + dry-run + bloqueo secrets + changelog + verificar.py + tests
🎁 S03 · ROUTER COMPLETO (7 gaps)
   R1 cifrado/BYOK · R2 reglas en archivo · R3 batching · R4 salud 30s ·
   R5 retry · R6 circuit breaker · R8 caché semántico
🎁 S04 · ORQUESTADOR COMPLETO
   vigilancia 30s + LLM_JUEZ 16 pasos + FUSIÓN real de duplicados
   (loop_engine P-077 / recovery / tribunal, Fable manda + mis capas)
   + wiring piloto automático 24h
🎁 S05 · AUDITOR COMPLETO
   detector alucinaciones (verificar T-014 Fable primero, portar si falta)
   + verificar 4 plugins reales + credenciales en providers.yaml
🎁 S06 · MOTORES GENÉRICOS UOOS
   TEMA A opción 1+3 (doc→UOOS1) + TEMA B opción 3 (cierre→UOOS2)
🎁 S07 · EMBUDO DE ENTRADA 🚨 (cierra SIM-1 fallas 1)
   idea vaga → requisitos estructurados (Fases 01/02/17: personas,
   objetivos, alcance) — la boca del túnel del tren
🎁 S08 · GENERADOR WEB/APP parte 1 🚨 (gap más grande)
   Generador de Design System (colores/tipografía/tokens/dark-mode)
   + motor de boilerplates: 2 stacks primero (FastAPI+React)
🎁 S09 · GENERADOR WEB/APP parte 2
   componentes frontend + base de datos + APIs + PRUEBA REAL: el
   generador produce un proyecto que compila y corre (H3)
   (mobile/desktop = después de v1, tú decides cuándo)
🎁 S10 · FICHAS lote 1
   renumeración E (H1, primero) + 15 YAML aceleradores A +
   50 fichas P nivel avanzado/arquitecto formato UOOS Parte 1
🎁 S11 · FICHAS lote 2
   resto de P nombradas + S-001..008 + T prioritarias
   (las restantes siguen en lotes de 50, revisión de 10 en 10)
🎁 S12 · CONECTOR UNIVERSAL (panel #8)
   BOCETO visual primero → tu OK → código real con Tribunal
   (GitHub/VPS/Drive/Correo/Descarga · autónomo/semi-manual ·
   con/sin agente · resultados como Artefactos)
🎁 S13 · INTEGRACIÓN TOTAL
   Kernel Fable (710 líneas) + Auditor + Router + fichas → conexión
   MCP/API + AUD-2P sobre las 235 mejoras (gate del ACTA)
🎁 S14 · FRONTEND FINAL + DOCUMENTOS
   8 paneles unificados + README general + PIPELINE actualizado
🎁 S15 · PRUEBA PUNTA A PUNTA 🎆
   Corrida real completa: idea → requisitos → diseño → código →
   tribunal → app funcionando → evidencia. Repetir SIM-1/2/3 y
   confirmar que las 7 fallas ya no ocurren
🎁 S16 · DESPLIEGUE FINAL 🚂🎄
   Orden determinista al agente (ejecutar, no decidir) →
   evidence.json = la prueba. Sin evidencia, no está desplegado.
```

**MÍNIMO: 16 salidas.** Cada una: sandbox + Tribunal (umbral 70) + tu OK.
Se pueden acelerar en paralelo: S02+S03+S04+S05 no dependen entre sí.

---

## PARTE 4 — TABLA DE COBERTURA (todos los gaps de la auditoría → su salida)

| Gap de auditoría | Salida que lo cierra |
|---|---|
| Matriz histórica 14,15,16,17,18,23,24,25 | S01 (firmas D6-D10 + archivos) |
| Matriz 19 (3 Monitores) | ✅ Ya cerrado (monitores.py) |
| Matriz 20 (1000 agentes) | S01 plan + S13 prueba de estrés |
| Matriz 21 (1000 loops) | S01 (mapeo D9-A) |
| Matriz 22 (piloto 24h) | S04 |
| Router R1-R6, R8 | S03 |
| Orquestador O1, O2, O3 | S04 |
| Auditor A1, A2, A3 | S05 |
| Fichas E/P/S/T/A (325) | S10-S11 (+lotes continuos) |
| TEMA A + TEMA B | S06 |
| Embudo entrada (Bloque 7) | S07 |
| Generación web/app (Salida 4/5) | S08-S09 |
| Frontend final (Fase F) | S14 |
| AUD-2P 235 mejoras | S13 |
| Conector Universal | S12 |
| Linajes viejos (D1) | ✅ Archivados por tu firma |
| Índice maestro (D5) | Pospuesto a S14 por tu firma |

**Cobertura: 100% de los gaps de las 4 auditorías + trazabilidad + simulaciones tienen salida asignada. Nada queda fuera del tren.**

---

## PARTE 5 — REGLAS DE PRODUCCIÓN (vigentes en las 16 salidas)
1. Todo código se diseña con **formato UOOS Parte 1** (manifest + DSL + DAG + tribunal + plan)
2. Todo cierre usa **UOOS Parte 2** (runtime) + despliegue determinista v2.0
3. Fable manda en duplicados; lo mío se AGREGA como capa (D2/D3)
4. Nada nuevo sin verificar si ya existe (regla loop_engine)
5. Interface nueva = boceto primero, siempre
6. Tribunal 6 inspectores antes de cada entrega
7. El agente de despliegue EJECUTA, nunca decide

🎄 Ruta completa, gaps 100% cubiertos, 16 regalos hasta el despliegue.
Di "S01 GO" y Santa enciende la locomotora. 🚂🎅🎁
