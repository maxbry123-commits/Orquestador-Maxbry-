# DOCUMENTO 5: CONFIGURACIONES DEL ORQUESTADOR
## Extraído del historial del chat

---

## 1. 3 PERFILES DE APIs INTERCAMBIABLES

3 perfiles de uso de APIs que MAX puede elegir según contexto.

### 🛡️ CONSERVADOR
```
- NVIDIA NIM: 4 keys (alta calidad)
- Cerebras: 1-2 keys (verificación)
- Groq: 1-2 keys (emergencias)
- Prioriza calidad sobre velocidad
- Costo: alto
```

### ⚖️ EQUILIBRADO (DEFAULT)
```
- NVIDIA NIM: 1 key
- Cerebras: 6 keys (mayor uso)
- Groq: 4-6 keys (complemento)
- Balance calidad/velocidad
- Costo: medio
```

### ⚡ AGRESIVO
```
- NVIDIA NIM: 1 key (solo crítico)
- Cerebras: todas las keys
- Groq: todas las keys
- Velocidad máxima
- Costo: optimizado por uso
```

### Cambio de perfil:
- Automático por contexto
- Manual cuando MAX quiera
- Default: Equilibrado

---

## 2. DATOS PRE-FLIGHT PENDIENTES DE MAX

Lo que MAX debe dar para que el sistema arranque:

```
1. ⏳ GitHub username + PAT
2. ⏳ HF username + 6 tokens
3. ⏳ 16 API keys con labels
4. ⏳ Turso DB credentials
5. ⏳ Visibility preference (public/private)
6. ⏳ Telegram bot token
7. ⏳ HTM model name (no encontrado en HF)
8. ⏳ YUAN model name (no encontrado en HF)
```

---

## 3. INICIO AUTÓNOMO — LO QUE EL SISTEMA HACE SOLO

Una vez que MAX da datos pre-flight, el sistema:

1. Crea 14 repos en GitHub (6 factories + 8 products)
2. Crea 7 HF Spaces con own tokens
3. Escribe 5 Dockerfiles
4. Inyecta secretos
5. Configura profiles
6. Arranca orquestador
7. Reporta a MAX

---

## 4. ARQUITECTURA DE COSTOS

### Objetivo $0:
```
HuggingFace Free Tier:
- 7 Spaces con 16GB RAM c/u
- CPU básico gratis
- Storage limitado

API Free Tiers:
- 4 NVIDIA NIM keys (free tier)
- 6 Cerebras keys (free tier)
- 6 Groq keys (free tier)

GGUF Local:
- 9 modelos cuantizados
- 0.6GB - 3GB cada uno
- Sin costo de inferencia
```

### Límites a respetar:
```
- HF Spaces pueden dormirse por inactividad
- Rate limits de APIs
- Memoria limitada por Space
- Cold starts posibles
```

---

## 5. CAPACIDADES DEL SISTEMA

```
- 2000+ agentes simultáneos (CAPACIDAD, no reales)
- 1000+ tareas simultáneas
- 7 HF Spaces con 16GB c/u = 112GB RAM
- ~13.5GB usados por modelos
- 87% margen libre
```

### Escalabilidad:
- Horizontal: agregar HF Spaces
- Vertical: upgrade a Spaces larger
- Sin redesign del código

---

## 6. REGLAS ABSOLUTAS DE MAX

```
"NUNCA crear ni cambiar nada sin mi APROBADO explícito"
"SOLO AGREGO capas, NUNCA reemplazo"
"MANTENER todos los nombres originales"
"5 GOALS + 12 PASOS obligatorios en CADA salida"
"Cada salida empieza con: 'APLICANDO SYSTEM PROMPT — 5 GOALS + 12 PASOS'"
"Cada salida termina con: AUDIT FINAL (PASO 12)"
"3 separate inventories: Tools ≠ Agents ≠ AI Models"
"Orquestador INDEPENDIENTE — no mezclar con GGUF/AI keys/proyectos"
"NO inventar datos — preguntar si falta info, no inventar"
"NO alucinar"
"MVP first, anti-overengineering"
"NO PC environment — solo smartphones + iPad Pro"
"Input is sacred — Input Block nunca modifica/resume/parafrese/reinterpreta"
"DSL/DAG nunca prompt libre — solo estructurado"
"G5 gestiona agentes (no al revés)"
"Orquestador debe confirmar proyecto antes de ejecutar (Fase 0.5)"
"APIs intercambiables (profiles: conservador/equilibrado/agresivo)"
"Structure <200 lines per file — M2.7 puede editar sin romper"
"Cada HF Space per group = isolated, own token"
"Cada project = separate root in GitHub"
"No inventar nuevas categorías que modifiquen las existentes"
"Cada salida validar antes de patchear (checklist de validación)"
"Mostrar PENDIENTE si algo no está aprobado — STATE JSON actualizado siempre"
```

---

## 7. FORMATO DE SALIDA ESTÁNDAR

### 5 GOALS (siempre):
- **G1** · goal_primary
- **G2** · goal_secondary
- **G3** · goal_success
- **G4** · goal_failure
- **G5** · goal_restriction

### 12 PASOS (siempre):
- **PASO 01** · literal_read
- **PASO 02** · think
- **PASO 03** · plan
- **PASO 04** · decompose
- **PASO 05** · hypotheses
- **PASO 06** · swarm
- **PASO 07** · critic
- **PASO 08** · simulate
- **PASO 09** · validate
- **PASO 10** · consensus
- **PASO 11** · report
- **PASO 12** · audit

### Inicio de cada salida:
"APLICANDO SYSTEM PROMPT — 5 GOALS + 12 PASOS"

### Final de cada salida:
"AUDIT FINAL (PASO 12)"

---

## 8. MI SYSTEM PROMPT OPERATIVO (M3)

Reglas grabadas en `/workspace/nct-proyecto/MI-SYSTEM-PROMPT-OPERATIVO.md`:

5 GOALS + 12 PASOS + 7 pasos adicionales + 8 reglas absolutas + cosas intocables

### 7 pasos adicionales:
1. Buscar memoria
2. Validar propuesta
3. Validar salida
4. Validar trazabilidad
5. STATE JSON actualizado

### 8 reglas absolutas:
1. Nunca inventar
2. Nunca mezclar orquestador con GGUF/proyectos
3. Si falta info, PREGUNTAR (no inventar)
4. M3 debe proponer SUS ideas, no solo registrar las de MAX
5. M3 debe CREAR archivos reales, no solo parchear docs
6. M3 no alucinar
7. M3 no hacer preguntas en vez de proponer
8. M3 no saltarse preguntas

---

## 9. VALIDACIÓN OBLIGATORIA POR SALIDA

5 pasos de validación antes de cada salida:
1. Buscar memoria
2. Validar propuesta
3. Validar salida
4. Validar trazabilidad
5. STATE JSON actualizado

Archivo: `/workspace/nct-proyecto/VALIDACION-POR-SALIDA.md` (2667 bytes)

---

## 10. COSAS INTOCABLES

NO se modifican, solo se respeta su existencia:

- **10 Jueces CSA** (J1-J10)
- **Auditor SID** (5 preguntas fijas)
- **Constitución** (39 principios)
- **14 categorías BIS**
- **Nombres y cantidades originales** ya aprobados

### REGLA: Solo AGREGAR capas, nunca reemplazar.

---

## 11. ESTADO DEL PROYECTO

- ✅ 100 patches con documentación individual
- ✅ 19 archivos Python reales (726 líneas)
- ✅ Constitución 1276 líneas
- ✅ Memoria persistente: 2 topics
- ⏳ Bloqueado esperando pre-flight data de MAX
- ⏳ M2.7 no ha instalado nada (espera GO de MAX)
</content>
</invoke>