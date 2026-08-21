```json
{
  "documento": "UI_PANEL_ORQUESTADOR — instrucciones de construcción para Sonnet",
  "prototipo_referencia": "UI-PANEL-ORQUESTADOR.html (diseño congelado: grises/negro)",
  "se_engancha_en": "V11 gateway (backend ya existe) + FICHA-MEJORA-UI de V12 paso 942b",
  "regla_madre": "la UI NUNCA ejecuta lógica — solo lee estado y emite comandos/eventos al gateway. Cada botón = una función MCP ya registrada (frontend abierto)."
}
```

# INSTRUCCIONES UI — PANEL DEL ORQUESTADOR (para Sonnet)

## 1. DISEÑO CONGELADO (no inventar otro)
- Paleta EXACTA del prototipo: fondo `#0e0e10`, paneles `#17171a`/`#1e1e22`, bordes `#2c2c31`, texto `#d6d6da`, dim `#8a8a92`, blanco `#f0f0f4`; acentos apagados: ok `#9aa89a`, warn `#b0a58a`, err `#a88a8a`. Sin colores vivos.
- Tipos: IBM Plex Mono (cuerpo) + Georgia/serif (títulos). Layout 3 columnas: nav 210px · main fluido · side 300px.

## 2. STACK Y ARCHIVOS (límites LOC del PIPELINE aplican)
```
frontend/  (repo nct-backend, servido por gateway_api)
  index.html            (shell, ≤150)
  app.js                (router de vistas + fetch, ≤300)
  views/panel.js        (≤250)   views/router_conn.js (≤250)
  views/config.js       (≤250)   views/tren.js        (≤200)
  views/gobernanza.js   (≤250)   views/logs.js        (≤200)
  ui.css                (paleta congelada, ≤200)
```
Vanilla JS + fetch. PROHIBIDO: frameworks pesados, build steps, localStorage para estado del orquestador (el estado vive en Postgres, la UI solo lo lee).

## 3. CONTRATO CON EL BACKEND (todo ya existe en V11)
- `GET  /api/estado`            → FSM, nodo, vagón, llm_pct, paso/1000 (lee state.json+workflows)
- `GET  /api/monitores`         → guardian/watchdog/PAD/drift/ansiedad (eventos F5)
- `GET  /api/eventos?n=50`      → stream tipado (event_bus)
- `GET/PUT /api/config_runtime` → SOLO claves de config_runtime.* (Sentinela-scope). PUT exige firma → escribe en ledger → evento. NUNCA expone ADN/Guardian/contracts.
- `GET  /api/router`            → estado conexión, tools MCP registrados
- `POST /api/router/probar` · `POST /api/router/reregistrar`
- `POST /api/comando`           → {cmd: GO|OK|FIX|PAUSA|ESTADO|SALTAR|UNLOCK|ABORT, arg} (V2 comandos.py)
- `GET  /api/gobernanza/pendientes` · `POST /api/gobernanza/firmar` (doble confirmación si DESTRUCTIVA)
- MCP: cada endpoint anterior TAMBIÉN es tool MCP (gateway_mcp) — la UI es un cliente más, sin privilegios.

## 4. LAS 6 VISTAS (orden de construcción)
1. **Panel**: topbar de estado + lockbar INPUT_BLOCK (hash + "ver literal" → modal con raw_text) + tren de vagones + pendientes de gobernanza.
2. **Router/Conexiones**: modo salida (MCP/API/ambos), endpoint, key (solo escribe env ref, jamás muestra el valor), webhook, heartbeat, probar/re-registrar.
3. **Configuración**: SOLO claves config_runtime (modo trabajo, nivel default, workers máx, llm_pct, toggles batching/timeout adaptativo/simulación5x/staff). Guardar → modal "firmar en ledger".
4. **Tren**: los 14 vagones con estado (✓/●/·), paso actual, despliegues D# con link a evidence.json.
5. **Gobernanza**: fichas-mejora con consenso, UNLOCKs solicitados, destructivas bloqueadas (doble confirmación UI).
6. **Logs**: eventos tipados con filtro por tipo (SYSTEM/TASK/COGNITIVE).

## 5. REGLAS DURAS
- R1: botón sin endpoint real = PROHIBIDO (nada decorativo).
- R2: la UI no interpreta — muestra el dato crudo + su hash cuando exista.
- R3: acciones de escritura SIEMPRE pasan por firma/ledger; DESTRUCTIVA = doble confirmación + mostrar snapshot_id.
- R4: pinned lockbar visible en TODAS las vistas (GAP-P3-034).
- R5: tests: 1 test de contrato por endpoint consumido (mock del gateway) + 1 e2e con gateway real.

## 6. ENTREGA (formato UOOS §7)
Cada archivo: ruta + código completo ≤90c/línea + comando de verificación + evidencia. Orden: ui.css → index → app.js → vistas 1-6 → tests. Cierra con despliegue parcial (frontend/ entra a nct-backend vía deploy_config existente).

## 7. MEJORAS FUTURAS (backlog, NO ejecutar ahora — E08)
Dark/light toggle en grises · gráfica llm_pct histórica · vista de atlas embebida (HTML del exporter) · websocket para eventos en vivo (hoy: polling 5s) · modo studio/embedded (NCT_INTERFACE_v2 3 modos).
