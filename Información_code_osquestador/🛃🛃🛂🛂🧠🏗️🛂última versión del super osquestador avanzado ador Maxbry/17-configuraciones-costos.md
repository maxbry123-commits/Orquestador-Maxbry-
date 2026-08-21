# MASTER DOCUMENTO 17: CONFIGURACIONES + COSTOS
## MAXBRY SUPER TEAM · 3 Perfiles · Pre-flight Pendientes · Costo $0

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. OBJETIVO DE COSTO

### $0/mes
- HF Spaces free tier
- API free tiers
- GGUF local sin costo
- Sin servers dedicados
- Sin bases de datos caras

---

## 2. 3 PERFILES DE USO DE API

### 2.1 Conservador

```yaml
profile: conservador
description: Bajo costo, baja capacidad
primary: groq
secondary: nim
fallback: cerebras
rules:
  - no_gpt_oss_20b: true
  - max_retries: 3
  - timeout_s: 60
budget:
  max_tokens_per_task: 100_000
expected_throughput: 2000+ tasks/day
use_cases:
  - Tareas simples
  - Bajo riesgo
  - Bajo costo
```

### 2.2 Equilibrado (RECOMENDADO)

```yaml
profile: equilibrado
description: Balance costo/calidad
primary: nim
secondary: cerebras
fallback: groq
rules:
  - gpt_oss_20b_for_hard_tasks: true
  - max_retries: 5
  - timeout_s: 120
budget:
  max_tokens_per_task: 500_000
expected_throughput: 1000+ tasks/day
use_cases:
  - Mayoría de tareas
  - Balance costo/calidad
```

### 2.3 Agresivo

```yaml
profile: agresivo
description: Máxima calidad
primary: cerebras
secondary: nim
fallback: groq
rules:
  - always_try_gpt_oss_20b_first: true
  - max_retries: 10
  - timeout_s: 300
budget:
  max_tokens_per_task: 2_000_000
expected_throughput: 100+ tasks/day
use_cases:
  - Tareas críticas
  - Máxima calidad
  - Costo no importa
```

---

## 3. PRE-FLIGHT PENDIENTES (DATOS QUE MAX DEBE DAR)

### 3.1 GitHub
- ⏳ **Username GitHub** - Para crear repos
- ⏳ **Personal Access Token (PAT)** - Para automatizar

### 3.2 HuggingFace
- ⏳ **Username HF** - Para crear Spaces
- ⏳ **6 tokens HF** - 1 por cada Space principal

### 3.3 API Keys (16 total)
- 4 NVIDIA NIM keys
- 6 Cerebras keys
- 6 Groq keys
- (Las keys reales NO están en este doc)

### 3.4 Database
- ⏳ **Turso DB credentials** - Para state persistente

### 3.5 Otros
- ⏳ **Visibility preference** (public/private) para repos y Spaces
- ⏳ **Telegram bot token** - Para canal principal
- ⏳ **HTM model name** - Hipotético modelo HTM
- ⏳ **YUAN model name** - Hipotético modelo YUAN

---

## 4. ARRANQUE AUTÓNOMO

### Una vez con datos pre-flight, el sistema:

1. Crea 14 repos en GitHub
   - 6 repos para grupos (G1-G6)
   - 8 repos para productos

2. Crea 7 HF Spaces
   - 1 por cada grupo G1-G6
   - 1 adicional para extras

3. Escribe 5 Dockerfiles
   - Cada grupo con su Dockerfile

4. Inyecta secretos
   - API keys
   - Tokens
   - Credenciales

5. Configura profiles
   - Conservador
   - Equilibrado
   - Agresivo

6. Arranca el orquestador
   - Inicialización automática
   - Reporte a MAX

---

## 5. CAPACIDADES OBJETIVO

### Cantidad
- **2000+ agentes** simultáneos (CAPACIDAD, no implementación)
- **1000+ tareas** simultáneas

### Hardware
- 7 HF Spaces × 16GB RAM = 112GB total
- ~13.5GB usados por modelos G6
- **87% margen libre**

### Throughput
- 2000+ tasks/día (conservador)
- 1000+ tasks/día (equilibrado)
- 100+ tasks/día (agresivo)

---

## 6. INFRAESTRUCTURA

### 7 HF Spaces
| Space | Propósito | RAM |
|-------|-----------|-----|
| g1-infra | Infraestructura | 16GB |
| g2-core | BIS, SID, Input/Output | 16GB |
| g3-ui | Telegram, API, Dashboard | 16GB |
| g4-audit | CSA | 16GB |
| g5-orquestador | MAXBRY | 16GB |
| g6-asistentes | 9 modelos GGUF | 16GB |
| extras | Reservas | 16GB |

### 14 Repos GitHub
- nct-g1-infra
- nct-g2-core
- nct-g3-ui
- nct-g4-audit
- nct-g5-orquestador ⭐
- nct-g6-asistentes
- (8 repos para productos)

### 5 Dockerfiles
- Dockerfile.g1
- Dockerfile.g2
- Dockerfile.g3
- Dockerfile.g4
- Dockerfile.g5

---

## 7. LIMITACIONES

### HF Spaces
- Pueden dormirse por inactividad
- Rate limits
- Cold starts
- 16GB RAM máximo por Space

### APIs Free Tier
- Rate limits
- Cuotas mensuales
- Latencia variable

### GGUF Local
- Carga en RAM
- Inferencia más lenta que API
- Modelos más pequeños

---

## 8. REGLAS DE COSTO

### 8.1 Nunca exceder presupuesto
Cada task tiene `max_tokens` y `max_runtime_s`.

### 8.2 Perfil por defecto
Recomendado: **Equilibrado** (balance costo/calidad).

### 8.3 Cambio dinámico
El sistema puede cambiar de perfil si:
- MAX lo solicita
- El presupuesto se agota
- La tarea es crítica

### 8.4 Monitoreo de costo
Cada task reporta:
- Tokens usados
- Tiempo de inferencia
- Costo estimado (en tiempo, no dinero)

---

## 9. CAPACIDADES POR HARDWARE

### Con 7 HF Spaces (16GB c/u):
- 2000+ agentes en estado latente
- 1000+ tareas activas simultáneamente
- 87% margen libre de RAM
- Inferencia local para modelos GGUF
- Cold start < 30s

---

## 10. CONCLUSIÓN

El sistema está diseñado para costo $0/mes con:
- 3 perfiles API intercambiables
- 16 API keys + 9 GGUF modelos
- 7 HF Spaces
- 14 repos GitHub
- 5 Dockerfiles
- 87% margen libre de RAM
- 1000-2000+ tareas/día

Falta solo que MAX dé los 8 datos pre-flight pendientes para arranque autónomo.
</content>