# DOCUMENTO 04 — INSTRUCCIONES PARA OPEN CLAW Y LOS 4 GRUPOS
## V1.0 — Completo

---

## INSTRUCCIONES PARA OPEN CLAW

### Misión
Open Claw es el director de los 4 grupos. NO escribe código. NO modifica archivos. SOLO coordina.

### Pasos de instalación
1. Instalar Hermes Agent
2. Configurar modelo
3. Habilitar tools
4. Iniciar gateway
5. Descargar 10 skills obligatorios (ver Doc 01)

### Bucle principal
```
CADA 10 SEGUNDOS:
1. Heartbeat interno
2. Poll estado de grupos A, B, C, D
3. Detectar bloqueos o caídas
4. Re-priorizar tasks
5. Asignar siguiente task al grupo IDLE
6. Escalar si hay error crítico
```

### Reglas duras
- NUNCA escribir código en repos de los grupos
- SIEMPRE usar HTTP/JSON para hablar con grupos
- SIEMPRE registrar señales externas
- SIEMPRE emitir métricas cada 30s
- SIEMPRE escalar al Director si supera nivel 4

### Skills que debe tener siempre listos
- find-skills
- skill-creator
- superpowers
- systematic-debugging
- tdd-workflow
- code-review
- software-architecture
- recursive-research
- deep-research
- webapp-testing

---

## INSTRUCCIONES PARA GRUPO A (Claude A + Mimo A)

### Repos
- Fase 1: orquestador-auditor-arquitecto (Repo 1)
- Fase 2: cerebro (Repo 2)

### APIs
- Claude A: NVIDIA Minimax M3
- Mimo A: Groq Kimi K

### Claude A — Debe hacer
1. Esperar task de Open Claw
2. Investigar (P01-P05)
3. Diseñar (P06-P10)
4. Implementar 4 archivos (.py + .meta.md + .location.json + test)
5. Auto-check 3 niveles
6. Entregar a Mimo A

### Mimo A — Debe hacer
1. Recibir archivos de Claude A
2. Validar 3 capas (lint, schema, tests)
3. Si pasa → APPROVED → notificar a Open Claw
4. Si falla → REJECTED con razón específica
5. Si 3 rondas falla → ESCALATE a Open Claw

### Skills Claude A
superpowers, software-architecture, mcp-builder, recursive-research, deep-research, prompt-engineering, article-extractor, brainstorming, notebooklm-integration, systematic-debugging

### Skills Mimo A
code-review, systematic-debugging, tdd-workflow, testing-best-practices, software-architecture, mcp-builder, ralph-loop, superpowers, prompt-engineering, recursive-research

---

## INSTRUCCIONES PARA GRUPO B (Claude B + Mimo B)

### Repo
- fichas (Repo 3)

### APIs
- Claude B: NVIDIA Minimax M3
- Mimo B: Groq Kimi K

### Claude B — Debe hacer
1. Recibir task de Open Claw
2. Crear ficha nueva (en imput/, procesamiento/ o output/)
3. Escribir 4 archivos: nombre.py + nombre.meta.md + nombre.location.json + test_nombre.py
4. Validar formato G2: 1 función ejecutar(input), <300 LOC, sin clases
5. Auto-check
6. Entregar a Mimo B

### Mimo B — Debe hacer
1. Validar 3 capas
2. Verificar Slot Contract SC1-SC6
3. Verificar que pasa Verifier N0-N5
4. APPROVED o REJECTED

### Skills Claude B
artifacts-builder, mcp-builder, docx, pdf, xlsx, csv-data-summarizer, recursive-research, code-review, systematic-debugging, superpowers

### Skills Mimo B
code-review, tdd-workflow, testing-best-practices, docx, xlsx, csv-data-summarizer, systematic-debugging, superpowers, ralph-loop, software-architecture

---

## INSTRUCCIONES PARA GRUPO C (Claude C + Mimo C)

### Repo
- router (Repo 4)

### APIs
- Claude C: NVIDIA Minimax M3
- Mimo C: Groq Kimi K

### Claude C — Debe hacer
1. Implementar los 10 módulos R1-R10 del router
2. Cada módulo en su carpeta
3. Cumplir 90% Python / 10% LLM
4. NO exponer API keys
5. Auto-check
6. Entregar a Mimo C

### Mimo C — Debe hacer
1. Validar que el router es agnóstico de provider
2. Verificar circuit breaker
3. Verificar que el balanceo funciona
4. Validar con tests de carga
5. APPROVED o REJECTED

### Skills Claude C
aws-skills, connect, playwright-browser-automation, ffuf-web-fuzzing, software-architecture, superpowers, code-review, systematic-debugging, mcp-builder, prompt-engineering

### Skills Mimo C
code-review, tdd-workflow, testing-best-practices, aws-skills, ffuf, software-architecture, systematic-debugging, ralph-loop, superpowers, prompt-engineering

---

## INSTRUCCIONES PARA GRUPO D (Claude D + Mimo D)

### Repo
- frontend (Repo 5)

### APIs
- Claude D: NVIDIA Minimax M3
- Mimo D: Groq Kimi K

### Claude D — Debe hacer
1. Construir UI que consume API del router
2. Solo HTTP, nunca imports directos
3. Responsive + accesible
4. Tests E2E con Playwright
5. Auto-check
6. Entregar a Mimo D

### Mimo D — Debe hacer
1. Validar responsive
2. Validar accesibilidad
3. Validar que consume API correctamente
4. E2E tests pasan
5. APPROVED o REJECTED

### Skills Claude D
vercel-react-best-practices, frontend-design, artifacts-builder, d3-visualization, anydesign, canvas-design, webapp-testing, superpowers, tdd-workflow, code-review

### Skills Mimo D
code-review, vercel-react-best-practices, frontend-design, webapp-testing, tdd-workflow, testing-best-practices, systematic-debugging, ralph-loop, superpowers, artifacts-builder

---

## BUCLE COMÚN (todos los grupos)

```
1. Open Claw envía task
2. Claude investiga (P01-P05) → score ≥ 0.85
3. Claude diseña (P06-P10)
4. Claude implementa (4 archivos)
5. Claude auto-check 3 niveles
6. Claude entrega a Mimo
7. Mimo valida 3 capas
   - Pasa → APPROVED → notificar Open Claw
   - Falla → REJECTED + razón → Claude repara (max 3 rondas)
8. Si 3 rondas falla → ESCALATE a Open Claw
9. Open Claw notifica al Director si es crítico
```

---

## 10 GOALS + 19 PASOS (COMUNES A TODOS LOS GRUPOS)

### 10 Goals
G1: Separación total de repos
G2: Cerebro determinista (no LLM)
G3: Fichas como Lego (formato G2)
G4: Router agnóstico de provider
G5: Comunicación tipada con schema
G6: Estado inmutable + recovery
G7: Auditoría central (Obsidian + Graphiti)
G8: 90% DSL / 10% LLM
G9: 4 grupos paralelos
G10: Open Claw como orquestador

### 19 Pasos
P01: Leer documentos del repo
P02: Leer plan.json recibido
P03: Identificar capacidad necesaria
P04: Consultar knowledge base
P05: Score ≥ 0.85 o escalar
P06: Definir 1 responsabilidad
P07: Declarar input_schema
P08: Declarar output_schema
P09: Listar dependencias
P10: Diseñar test mínimo
P11: Implementar código
P12: Self-check 3 niveles
P13: Entregar a Mimo
P14: Mimo valida 3 capas
P15: Si falla, reparar (max 3 rondas)
P16: Si aprueba, notificar Open Claw
P17: Esperar nueva task
P18: Si error crítico, escalar
P19: Métricas + self-improvement

---

## CRITERIOS DE ACEPTACIÓN

- [x] Instrucciones para Open Claw
- [x] Instrucciones para Grupo A
- [x] Instrucciones para Grupo B
- [x] Instrucciones para Grupo C
- [x] Instrucciones para Grupo D
- [x] Bucle común definido
- [x] 10 Goals + 19 Pasos
- [x] Skills por cada agente

DOCUMENTO 04 COMPLETO V1.0
