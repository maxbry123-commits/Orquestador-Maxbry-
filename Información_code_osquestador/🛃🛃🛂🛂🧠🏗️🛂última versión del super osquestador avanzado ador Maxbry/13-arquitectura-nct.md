# MASTER DOCUMENTO 13: ARQUITECTURA NCT
## MAXBRY SUPER TEAM · NCT Coordinator · 25 Bloques · Versión 1+2

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. NCT — NEURONAS CODE TURBO

### 1.1 Visión general
NCT es el **proyecto global** que contiene MAXBRY SUPER TEAM. No es el orquestador en sí, sino el ecosistema donde opera.

### 1.2 Ubicación del proyecto
```
/workspace/nct-proyecto/
├── CONSOLIDADO-FINAL/ (18 docs consolidados)
├── MASTER-FINAL/ (13+ docs master)
├── CONSTITUCION-ORQUESTADOR.md
├── PARCHE-v14 a PARCHE-v17
├── PATCHES-*
└── PARCHES-*

/workspace/maxbry/
├── g1-infra/
├── g2-core/
├── g3-ui/
├── g4-audit/
├── g5-orquestador/ ⭐
└── g6-asistentes/
```

---

## 2. LOS 25 BLOQUES DEL SOFTWARE PRINCIPAL

### Bloques originales (NO modificados por MAXBRY):

1. **Inicializador** - Boot del sistema
2. **Config Loader** - Carga configuración
3. **State Manager** - Estado global
4. **Event Bus** - Bus de eventos
5. **Logger** - Sistema de logs
6. **Error Handler** - Manejo de errores
7. **Network Manager** - Red
8. **Storage Manager** - Almacenamiento
9. **Auth Manager** - Autenticación
10. **Permission Manager** - Permisos
11. **Cache Manager** - Caché
12. **Queue Manager** - Colas
13. **Worker Pool** - Pool de workers
14. **Task Scheduler** - Scheduler
15. **Result Aggregator** - Agregador
16. **Retry Manager** - Reintentos
17. **Circuit Breaker** - Circuit breaker
18. **Metrics Collector** - Métricas
19. **Health Checker** - Health
20. **Notification Manager** - Notificaciones
21. **Plugin Manager** - Plugins
22. **API Gateway** - Gateway API
23. **Database Connector** - DB
24. **External Service Client** - Servicios externos
25. **Telemetry** - Telemetría

---

## 3. NCT COORDINATOR

### 3.1 Qué es
NCT Coordinator es la interfaz principal de NCT. Tiene 13 archivos.

### 3.2 Los 13 archivos

1. `nct_coordinator.py` - Coordinador principal
2. `nct_modes.py` - Selector de modos
3. `nct_flows.py` - Definición de flujos
4. `nct_phases.py` - Fases (F0-F9)
5. `nct_inputs.py` - Inputs
6. `nct_outputs.py` - Outputs
7. `nct_state.py` - Estado
8. `nct_memory.py` - Memoria
9. `nct_skills.py` - Skills
10. `nct_agents.py` - Agentes
11. `nct_audit.py` - Auditoría
12. `nct_metrics.py` - Métricas
13. `nct_delivery.py` - Entrega

### 3.3 Interfaz de Selección de Modo

```
┌─────────────────────────────────┐
│   NCT - Selección de Modo       │
├─────────────────────────────────┤
│                                 │
│  1. Manual                      │
│  2. Semi-automático             │
│  3. Continuo (NCT)              │
│                                 │
└─────────────────────────────────┘
```

---

## 4. DOS VERSIONES DE ARQUITECTURA

### 4.1 Versión 1 — Chat AI NCT (Original)
- Asistente de chat tradicional
- Procesa mensajes
- Genera respuestas
- Memoria simple

### 4.2 Versión 2 — Adaptador MYTHOS
- Wrapper sobre V1
- Añade razonamiento profundo
- Añade Mythos system prompt
- Añade control de alto nivel

### 4.3 Diagrama V1 vs V2

```
         V1                              V2
   ┌──────────┐                   ┌──────────┐
   │   Chat   │                   │ MYTHOS   │
   │  AI NCT  │                   │ (control)│
   └────┬─────┘                   └────┬─────┘
        │                              │
        │                       ┌──────▼──────┐
        │                       │ Adaptador   │
        │                       │  MYTHOS     │
        │                       └──────┬──────┘
        │                              │
        └──────────────┬───────────────┘
                       │
                ┌──────▼──────┐
                │   LLMs      │
                └─────────────┘
```

---

## 5. FLUJO CONTINUO

```
MAX → Telegram
   ↓
MAXBRY recibe
   ↓
SID (5 preguntas)
   ↓
BIS lookup
   ↓
Plan generado
   ↓
Consensus consejo
   ↓
Ejecutar (30 micro-agentes)
   ↓
Validar (CSA)
   ↓
Refinar si score < 95%
   ↓
Output Engine
   ↓
Multi-target Delivery
   ↓
Monitoreo
   ↓
Feedback → Memoria → Mejora
```

---

## 6. PRINCIPIOS DE LA ARQUITECTURA

### 6.1 Modularidad
- Cada bloque tiene responsabilidad única
- Comunicación vía bus de eventos
- Acoplamiento débil

### 6.2 Determinismo
- 90% código determinista
- 10% LLM donde aporta
- Reproducibilidad alta

### 6.3 Trazabilidad
- Cada acción se registra
- State siempre actualizado
- Logs estructurados

### 6.4 Resiliencia
- Circuit breakers
- Retry con backoff
- Failover automático
- Repair pipeline

---

## 7. FASES DETALLADAS

### F0 - Pre-Boot
Verifica:
- Python version
- HF Spaces
- Tokens
- Secrets
- Network

### F1 - Input
Recibe:
- Telegram message
- API call
- CLI command
- Web dashboard

### F2 - Process
Aplica Input Engine v4.0.

### F3 - Plan
Genera plan con consensus.

### F4 - Execute
30 micro-agentes + 12 especializados.

### F5 - Validate
CSA 10 jueces.

### F6 - Refine
Hasta score ≥ 95%.

### F7 - Output
Output Engine + OOS + OVFS.

### F8 - Deliver
Multi-target.

### F9 - Monitor
Post-delivery.

---

## 8. INTEGRACIÓN CON MAXBRY

MAXBRY NO modifica los 25 bloques. Los INVOCA como workers.

```
MAXBRY
  ↓ (invoca)
NCT Coordinator
  ↓ (coordina)
25 Bloques
  ↓ (producen)
Output
```

---

## 9. INTERFAZ

### Para MAX:
- Telegram (principal)
- API REST
- Dashboard web
- CLI

### Para MAXBRY:
- Python API
- MCP server
- CLI directo

---

## 10. CONCLUSIÓN

NCT es el ecosistema. MAXBRY es el orquestador. Los 25 bloques son los músculos. Los 13 archivos NCT Coordinator son el sistema nervioso. Las 10 fases son el flujo sanguíneo. Todo junto forma el Sistema Operativo Distribuido para IA.
</content>