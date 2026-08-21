# UOOS PARTE 2 — nct-kernel (EJECUTABLE)
(generado por Motor TEMA B · lote sha256:f504f7e5d5033468… · 14 archivos)

## ORDEN AL AGENTE (copiar y pegar tal cual)
```
ORDEN DE DESPLIEGUE — nct-kernel (lote sha256:f504f7e5d5033468…)
Eres el EJECUTOR. NO analices, NO mejores, NO decidas. Pasos:
1. python -m pytest tests -q
   → si algo falla: DETENTE y pega la salida. No arregles nada.
2. Copia estos 13 archivos a nct-kernel-backend/ (lista exacta en plan_repos.backend)
3. Copia estos 1 archivos a nct-kernel-docs/ (lista exacta en plan_repos.docs)
4. git add -A && git commit -m 'nct-kernel: lote f504f7e5d503'
5. git push (github) y pega la salida completa.
6. python verificar.py → confirma evidence.json ok:true.
7. DETENTE. Fin de la orden.
```

## PLAN DE REPOS
```json
{
  "backend": 13,
  "frontend": 0,
  "docs": 1,
  "_sin_regla": 0
}
```

## EVIDENCIA REQUERIDA
- salida completa de pytest (todos PASS)
- hash del commit local == hash remoto (verificar.py)
- conteo de archivos subidos == 14
- evidence.json escrito y con ok:true

**SIN evidence.json NO está desplegado (patrón Witness)**
