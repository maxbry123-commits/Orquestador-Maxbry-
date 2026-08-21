# MASTER DOCUMENTO 12: PIPELINE + FASES
## MAXBRY SUPER TEAM · 10 Fases + Fase 0.5 + FABLES + CHEF FINAL

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. LAS 10 FASES DEL PIPELINE

### FASE 0 — Pre-Boot
- Verifica entorno
- Carga configuración
- Inicializa HF Spaces
- Verifica tokens y secrets

### FASE 0.5 — Confirmation Gate ⭐
- Muestra plan a MAX
- Pide confirmación
- Bloquea hasta aprobación
- **REGLA INTOCABLE** (no proceder sin aprobación)

### FASE 1 — Input Reception
- Recibe input de MAX
- Detecta canal
- Auth + rate limit
- Log input

### FASE 2 — Input Processing
- Aplica Input Engine v4.0
- 54 componentes
- Genera input canónico

### FASE 3 — Planning
- Genera plan
- Descomposición de tareas
- Asignación de recursos
- Consensus del consejo

### FASE 4 — Execution
- Ejecuta tareas
- Monitoreo continuo
- 3 monitores activos
- Repair pipeline si falla

### FASE 5 — Validation
- CSA audita (10 jueces × 5 fases)
- SID verifica definición
- BIS valida skills

### FASE 6 — Refinement
- Si score < 95%, refina
- Iteración hasta score OK
- Máximo N iteraciones

### FASE 7 — Output Generation
- Aplica Output Engine
- OOS prepara entrega
- OVFS estructura
- 16 capas gobernanza

### FASE 8 — Delivery
- Multi-target (23 destinos)
- Adaptive format
- Confirmation tracking

### FASE 9 — Monitoring
- Post-delivery
- Feedback loop
- Production monitoring
- Auto-rollback si degrada

---

## 2. 4 ESCENARIOS DE EJECUCIÓN

### Escenario 1 — Tarea Simple (9 pasos)
- Input → Parse → Plan → Execute → Validate → Refine → Output → Deliver → Monitor

### Escenario 2 — Tarea Media (16 pasos)
- Input → Receive → Normalize → Parse → Validate → Intent → Context → Plan → Consensus → Execute → Monitor → Validate → Refine → Output → Deliver → Monitor

### Escenario 3 — Tarea Compleja (25 pasos)
- Pre-análisis (5)
- Research (5)
- Plan (5)
- Execute (5)
- Validate (5)

### Escenario 4 — Tarea Crítica (30-50 pasos)
- Pre-análisis (10)
- Research (10)
- Plan (10)
- Execute (10)
- Validate (10)
- + pasos adicionales según necesidad

---

## 3. COMPLEXITY ESTIMATOR

```python
def estimate_complexity(task):
    factors = {
        "length": len(task.input),
        "novelty": task.novelty_score,
        "dependencies": len(task.dependencies),
        "ambiguity": task.ambiguity_score,
        "risk": task.risk_score
    }
    return weighted_sum(factors)
```

### Categorías:
- 0-20: Simple (TM01-TM02)
- 21-40: Media (TM03-TM05)
- 41-60: Compleja (TM06-TM08)
- 61-80: Avanzada (TM09-TM10)
- 81-100: Crítica (TM11-TM12)

---

## 4. FABLES — 5 FASES

(Ver Master 11 para detalle)

1. Inicialización
2. Generación Adversarial
3. Crítica Multi-Agente
4. Refinamiento Iterativo
5. Síntesis Final

---

## 5. CHEF FINAL — 4 PASOS

(Ver Master 11 para detalle)

1. Revisión Final
2. Validación Cruzada
3. Refinamiento Cosmético
4. Emisión

---

## 6. LISTA_GLOBAL (4 REGLAS)

### Regla 1 — Una tarea por vez principal
No paralelizar tareas de la misma sesión MAX.

### Regla 2 — Tareas independientes en paralelo
Sí paralelizar si son independientes.

### Regla 3 — Tareas dependientes secuenciales
Si A depende de B, A espera a B.

### Regla 4 — Tareas críticas aisladas
Tareas críticas (TM11) en su propio contexto.

---

## 7. CHECKPOINTS

Cada fase genera checkpoint:
- F0: Pre-boot state
- F0.5: Confirmation state
- F1: Raw input
- F2: Canonical input
- F3: Plan approved
- F4: Execution log
- F5: CSA verdict
- F6: Refined output
- F7: Output sealed
- F8: Delivery state
- F9: Post-delivery state

---

## 8. DIAGRAMA

```
        F0 - Pre-Boot
           ↓
        F0.5 - Confirmation Gate ⭐
           ↓
        F1 - Input Reception
           ↓
        F2 - Input Processing (54 componentes)
           ↓
        F3 - Planning
           ↓
        F4 - Execution
           ↓
        F5 - Validation (CSA + SID + BIS)
           ↓
        F6 - Refinement (si score < 95%)
           ↓
        F7 - Output Generation (13+14+OVFS)
           ↓
        F8 - Delivery (23 destinos)
           ↓
        F9 - Monitoring + Feedback
```

---

## 9. ESTADOS POR FASE

Cada fase tiene estados:
- PENDING
- RUNNING
- CHECKPOINTED
- VALIDATED
- FAILED
- RECOVERING
- COMPLETED

---

## 10. CONCLUSIÓN

El pipeline tiene:
- 10 fases progresivas
- Fase 0.5 confirmation gate
- 4 escenarios de ejecución
- Complexity estimator
- FABLES 5 fases
- CHEF FINAL 4 pasos
- Lista global 4 reglas
- Checkpoints por fase
- Estados por fase
</content>