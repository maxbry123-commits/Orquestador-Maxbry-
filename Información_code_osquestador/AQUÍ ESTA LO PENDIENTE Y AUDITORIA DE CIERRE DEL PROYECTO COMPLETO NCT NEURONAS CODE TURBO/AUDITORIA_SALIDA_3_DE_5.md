# AUDITORÍA NCT — SALIDA 3/5 — TRANSVERSALES (T) + CORRECCIÓN DE GAPS
# 3 pasadas | 2026-07-17 | Fuente: ESQUELETO_MAESTRO + SALIDA_03_15_GAPS

## PASADA 1 — T-001 a T-045 COMPLETAS (nombres reales)
```
T-001..010 state_engine·wal_dual·crazy_wall·fusion·memoria_4tiers·
  faiss_brain·shared_knowledge·kg_sqlite·event_sourcing·checkpoint_
  rebuild — YA CODIFICADAS (Salidas 3/3.1/S12 de Fable)
T-011 dream_loop · T-012 distill_loop · T-013 writer_subagent
T-014..022 audit_bus·obsidian_writer·graphiti_writer·hallucination_
  check·recovery_engine·watchdog·heartbeat·dlq_infra·failure_registry
  — YA CODIFICADAS (S2/S13/S15 de Fable)
T-023 red_universal · T-024 enchufe_registry_v2 · T-025 sentinela_metodo
T-026..045 (✚nuevas): metrics_timeseries·anomaly_detector·budget_alarms·
  key_rotation·backup_restore·cold_archiver·migration_runner·schema_
  registry·feature_flags·kill_switch·quota_tenant·uptime_prober·
  incident_manager·oncall_notifier·resource_monitor·otel_exporter·
  log_compactor·secrets_manager·chaos_schedule·config_versioner
```
**HALLAZGO:** `T-014 hallucination_check` — **YA EXISTE marcado como
código de Fable (S13)**. Esto CONTRADICE mi hallazgo anterior (Bloque 4
del parche detallado) donde dije "detector de alucinaciones no existe
en ningún lado". **Corrección: si existe diseño/código de Fable, falta
verificar el archivo real, no construirlo desde cero.**

## PASADA 2 — CORRECCIÓN GRANDE: gaps de la matriz de 25, ya resueltos por Sonnet/Fable

Fuente: `SALIDA_03_PASADA_4_Y_15_GAPS_BANDERAS.md` — cada 🚩G-xx trae
"Estado: ✅ Resuelto por Sonnet" con solución de diseño concreta:

| Gap | Antes decía | Solución real ya escrita |
|---|---|---|
| G-05 (30 MA vs 15) | 🚩 abierto | `ma/ma_30_registry.yaml`: 15 apuntan a MA-* reales, 15 a fichas del esqueleto — cantidad 30 preservada. **Falta solo escribir el YAML**, diseño cerrado |
| G-06 (3 Monitores) | 🚩 abierto | Código especificado completo (3 archivos ≤150 LOC) — **coincide con lo que yo construí** (`monitores/monitores.py`). Confirmado cerrado de verdad |
| G-07 (1000 agentes) | 🚩 abierto | Roadmap declarativo: 300(v1.0)→800(v2.0)→1000(v3.0) vía `exec/scale_plan.yaml`, autoscaler ya soporta pools elásticos. **No se construye ahora — se declara el camino**, decide el Director cuándo subir el techo |
| G-08 (R1-R11/Q1-Q10/TM/Officers) | 🚩 abierto | Tabla de absorción completa: R1-R11→roles del pipeline+7 managers · Q1-Q10→PoolRouter+DLQ nombradas · TM01-12→12 combinaciones nivel×perfil · 5 Officers→5 VISTAS del panel (no agentes). **Falta escribir `org/estructura_historica_mapping.yaml`**, diseño cerrado |

## PASADA 3 — RECUENTO ACTUALIZADO DE GAPS REALES (post-corrección)

De los 8 que tenía como "abiertos" en el Bloque 1 del parche anterior:
- **G-05, G-06, G-07, G-08 → RECLASIFICADOS**: diseño cerrado, solo
  falta ESCRIBIR el archivo de configuración (no diseñar de nuevo)
- Siguen genuinamente sin solución diseñada: **G-14(metas por fase),
  G-15/16(CSA J1-J10), G-17(39 principios), G-25(322 vs 265)** —
  pendiente confirmar si SALIDA_03 los resuelve también (no visto aún
  el texto completo de esos 4)

## RESUMEN SALIDA 3/5
T-001 a T-045 completas (45/45 nombradas) · detector de alucinaciones
posiblemente YA EXISTE (contradice hallazgo previo, requiere
verificación del archivo real) · 4 gaps reclasificados de "sin
resolver" a "solución escrita, falta el archivo YAML" · 4 gaps
pendientes de confirmar si tienen solución en el resto de SALIDA_03.

→ Sigue Salida 4/5: frontend + generación web/app
