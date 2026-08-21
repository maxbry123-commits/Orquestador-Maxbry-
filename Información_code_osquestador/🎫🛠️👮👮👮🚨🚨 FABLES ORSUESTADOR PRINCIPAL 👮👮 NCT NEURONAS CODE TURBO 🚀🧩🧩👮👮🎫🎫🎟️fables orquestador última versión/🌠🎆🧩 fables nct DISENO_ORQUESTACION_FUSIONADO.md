# 🚂 DISEÑO DE ORQUESTACIÓN NCT — VERSIÓN FUSIONADA FINAL
# Fusiona: estrategia 7 puntos del Director (ACTA) + Plan Mavis 24 fases +
# 18-20 repos nuevos + jerarquía Fable/Claude Code | Fecha: 2026-07-12 | v1.0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. LA CADENA DE MANDO (quién orquesta a quién — 6 capas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
CAPA 0 · DIRECTOR (móvil/iPad) ── aprueba cada fase, revisa lotes de 10
   │
CAPA 1 · FABLE 5 (este chat) ── DISEÑA + hace lo CRÍTICO + emite las
   │      órdenes DSL/DAG/Schema listas para copiar/pegar
   │      (Sonnet queda como preparador de terreno cuando se use)
   ▼
CAPA 2 · CLAUDE CODE (app Anthropic) ── ÚNICO EJECUTOR REAL
   │      · Instancia CC-1 → kernel/backend/router (lo crítico)
   │      · Instancia CC-2 → frontend
   │      · Instancia CC-3 → fichas/skills
   │      (CC-1 coordina a CC-2 y CC-3, como decidiste en 3.1)
   ▼
CAPA 3 · ROUTER/GATEWAY (Cloudflare Workers) ── EL CORAZÓN, prioridad 100%
   │      Auth · Balanceo · Cola · Logs · Selección de modelo
   │      ÚNICA puerta a: HF Spaces, VPS, Docker, providers
   ▼
CAPA 4 · STAFF DE AGENTES (GitHub, solo conocen el Router)
   │      Grupo A/B/C/D = ClaudeCode+MimoCode+Codex c/u → 1 grupo : 1 repo
   │      Grupo F = resto de agentes + OPEN CLAW (interface de emergencia:
   │      si algo falla, tú entras por Open Claw→Router y reparas sin código)
   ▼
CAPA 5 · INFRAESTRUCTURA
          VPS Hetzner (cerebro: /data + /opt/nct-*) · GitHub (repos) ·
          HF Workers (sandbox de fichas) · MCP Gateway (tools, en VPS)
          MiniMax/Groq/Cerebras/NVIDIA = SOLO API keys en LiteLLM (no opinan)
          GPT = asesor externo opcional (fuera de la cadena de mando)
```
**Regla de oro (del plan Mavis, se conserva):** nunca saltar capas.
DISEÑO (Fable) → EJECUCIÓN (Claude Code) → VALIDACIÓN (HF/Witness) →
CIERRE (tú apruebas). Cada eslabón deja evidencia.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. MAPA DE REPOS ACTUALIZADO (~20, tus 7 principales + tarea1-5 + técnicos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Grupo | Repos | Quién construye |
|---|---|---|
| NÚCLEO | orquestador-principal · orquestador-auditor · memoria | CC-1 (crítico, órdenes de Fable) |
| RED | nct-router · nct-mcp-gateway | CC-1 — PRIMERO DE TODO |
| CARA | frontend(chat) · web · command-center | CC-2 |
| TALLER | fichas-skills · agentes(staff) · loops-engine | CC-3 |
| OPERACIÓN | tarea-1..tarea-5 (tus 5 nuevos: trabajo aislado por encargo) | grupos A-D |
| RESPALDO | openclaw-install · claude-code-config · mimo-code-config · watchdog | CC-1 |
Principio intacto: **1 grupo = 1 repo, nadie trabaja en 2** → nada se rompe.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ORDEN DE CONSTRUCCIÓN (tu prioridad + fases Mavis renumeradas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
ETAPA 1 · LA VÍA        Router + MCP Gateway + LiteLLM (Fases 4/5/8/10 Mavis)
  🎯 tu regla: "el Router debe funcionar al 100%" — nada más arranca sin él
ETAPA 2 · LOS OJOS      Orquestador Auditor desplegado en VPS (ya hay código
  Fase 0) + interface iOS-archivos + anclaje GitHub↔VPS (API/MCP)
ETAPA 3 · EL MOTOR      Sistema Loops (selector 1-1000, multi-proyecto)
  anclado a auditor+memoria
ETAPA 4 · LA CARA       Chat frontend con agente embebido (capa sobre el
  selector LLM) — separado/remoto del kernel
ETAPA 5 · LOS ELFOS     Staff A-D+F instalado en repo agentes, cada uno
  servidor independiente conectado SOLO al Router · Open Claw emergencia
ETAPA 6 · LA FÁBRICA    Cascada de fichas nueva (lotes de 50, tu revisión
  de 10 en 10) — la fábrica que hace los juguetes 🎁
ETAPA 7 · LA TIENDA     Web (3 proyectos, NCT separado) + demo FREE 3
  pruebas + cola sobredemanda + apps móvil/tablet/PC
```
Cada etapa cierra con: tests + evidencia Witness + tu OK. Sin OK no hay
etapa siguiente (Capa 0 manda).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. LAS 3 VÍAS DE COMUNICACIÓN (tu P7, cableado exacto)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
VÍA 1 (normal):     Chat frontend ──► Router ──► agentes/ejecución
VÍA 2 (dirección):  Fable/Claude Code ──► Router ──► auditor + agentes ──► GitHub
VÍA 3 (emergencia): TÚ ──► Open Claw UI ──► Router ──► reparar agentes
```
El Router registra TODO (logs/auditoría) — las 3 vías dejan huella.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. QUÉ CAMBIA DEL PLAN MAVIS (delta, lo demás se conserva)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Plan Mavis decía | Ahora (ACTA) |
|---|---|
| Mavis = capa 1 diseño | FABLE 5 = capa 1 · MiniMax sale de la línea de mando |
| 14 repos | ~20 repos (tus 7 principales + tarea1-5 + técnicos) |
| GPT-5 audita a MiniMax | GPT = asesor opcional externo |
| "Mavis reporta" | Claude Code reporta con evidencia L1-L4 al Witness |
Se CONSERVAN: modelo 5 capas (renumerado a 6 con el staff), paths VPS,
protocolo MD5, regla dura VPS (solo OpenClaw+ClaudeCode+MimoCode),
Telegram vía Router, workers.json en GitHub con espejo, watchdog, fases
de testing/verificación C1-C4/documentación/entrega.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. CHECKPOINT JSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```json
{ "documento": "DISEÑO_ORQUESTACION_FUSIONADO", "version": "1.0",
  "fecha": "2026-07-12", "estado": "PROPUESTO — espera OK del Director",
  "fusiona": ["ACTA_DECISIONES", "PLAN-EJECUCION-NCT_v2 (Mavis 24 fases)",
              "repos 18-20 del Director", "jerarquia Fable5+ClaudeCode"],
  "primera_accion_al_OK": "ETAPA 1: emitir orden DSL del Router para Claude Code",
  "api_keys": "van a /opt/nct-secrets/.env (permisos 600) via Claude Code — el Director las pasa cuando la ETAPA 1 arranque" }
```
