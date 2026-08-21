# MASTER DOCUMENTO 19: PRE-FLIGHT + DEPENDENCIAS
## MAXBRY SUPER TEAM · Datos Pendientes · Instalación · M2.7

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. DATOS PRE-FLIGHT PENDIENTES (8 DATOS)

MAX debe proporcionar estos datos antes de la instalación autónoma:

### 1.1 GitHub
- ⏳ **Username GitHub**
- ⏳ **Personal Access Token (PAT)** con scopes:
  - `repo` (Full control)
  - `workflow` (Update workflows)
  - `admin:org` (si aplica)

### 1.2 HuggingFace
- ⏳ **Username HF**
- ⏳ **6 tokens HF** (uno por Space principal)

### 1.3 API Keys (16 total)
- 4 NVIDIA NIM keys
- 6 Cerebras keys
- 6 Groq keys
- (Formato recomendado: provider-número-uso)

### 1.4 Database
- ⏳ **Turso DB URL**
- ⏳ **Turso DB Token**

### 1.5 Otros
- ⏳ **Visibility preference** (public/private)
- ⏳ **Telegram bot token** (de @BotFather)
- ⏳ **HTM model name** (hipotético en HF)
- ⏳ **YUAN model name** (hipotético en HF)

---

## 2. APROVISIONAMIENTO AUTOMÁTICO

### Una vez con datos pre-flight:

#### PASO 1 — Crear 14 repos en GitHub

```
Repos de grupos (6):
- nct-g1-infra
- nct-g2-core
- nct-g3-ui
- nct-g4-audit
- nct-g5-orquestador ⭐
- nct-g6-asistentes

Repos de productos (8):
- nct-product-01 al nct-product-08
```

#### PASO 2 — Crear 7 HF Spaces

```
- mavis/g1-infra
- mavis/g2-core
- mavis/g3-ui
- mavis/g4-audit
- mavis/g5-orquestador ⭐
- mavis/g6-asistentes
- mavis/extras
```

Cada Space con su propio token.

#### PASO 3 — Escribir 5 Dockerfiles

```
- Dockerfile.g1
- Dockerfile.g2
- Dockerfile.g3
- Dockerfile.g4
- Dockerfile.g5
```

#### PASO 4 — Inyectar secretos

```
- API keys como GitHub Secrets
- Tokens como HF Secrets
- Credenciales encriptadas
```

#### PASO 5 — Configurar profiles

```
- Conservador
- Equilibrado (recomendado)
- Agresivo
```

#### PASO 6 — Arrancar orquestador

```
- Bootstrap autónomo
- Conexión a G1-G6
- Reporte a MAX
```

#### PASO 7 — Reporte a MAX

```
- URLs de acceso
- Comandos útiles
- Estado de cada Space
- Estado de cada repo
```

---

## 3. RESPONSABLE DE INSTALACIÓN: M2.7

### 3.1 Quién es M2.7
M2.7 es la sesión dedicada a instalación. NO diseña arquitectura (eso es M3).

### 3.2 Lo que M2.7 hace
- Lee CONSTITUCIÓN-ORQUESTADOR.md
- Lee los 18 master docs
- Lee los patches aprobados
- Ejecuta aprovisionamiento automático
- Reporta a MAX

### 3.3 Lo que M2.7 NO hace
- No modifica arquitectura
- No inventa
- No reemplaza originales
- No crea nuevas categorías sin aprobación

### 3.4 Bloqueos de M2.7
Si encuentra datos faltantes, escala a MAX.
Si encuentra inconsistencias, escala a MAX.

---

## 4. DEPENDENCIAS ENTRE GRUPOS

```
G1 INFRA ← G2 CORE ← G3 UI
   ↓           ↓         ↓
   └───► G4 AUDIT ◄─────┘
              ↓
        G5 ORQUESTADOR ⭐
              ↓
        G6 ASISTENTES
```

### Secuencia de instalación:
1. **G1 INFRA** primero (crea HF Spaces, GitHub, Docker)
2. **G6 ASISTENTES** segundo (carga modelos)
3. **G2 CORE** tercero (BIS, SID, Input/Output)
4. **G4 AUDIT** cuarto (CSA)
5. **G5 ORQUESTADOR** quinto (MAXBRY)
6. **G3 UI** último (interfaz con MAX)

---

## 5. ESTADO DE M2.7

### Actual:
- ⏳ M2.7 NO ha instalado nada
- ⏳ Espera datos pre-flight de MAX
- ⏳ Espera aprobación de arquitectura final

### Cuando arranque:
1. Verifica entorno (Python, network, secrets)
2. Crea estructura de carpetas
3. Clona template base
4. Configura profiles
5. Crea recursos externos (con pre-flight)
6. Inyecta secretos
7. Arranca servicios
8. Reporta

---

## 6. CHECKLIST DE PRE-ARQUITECTURA

Antes de que M2.7 arranque:

- [x] Constitución v3.0 completa (39 principios)
- [x] CSA 10 jueces con 5 fases
- [x] SID con 5 preguntas
- [x] BIS con 14 categorías + 13 criterios
- [x] Input Engine v4.0 (54 componentes)
- [x] Output Engine + OOS v3.1 (27 componentes)
- [x] LOOP v6.0 (15 capas + 3 ciclos)
- [x] OUTPUT v6.1 (16 capas gobernanza)
- [x] MAXBRY SUPER TEAM definido
- [x] 30 micro-agentes, 11 roles, 10 colas, 6 niveles
- [x] 12 Task Models
- [x] 5 Loop Versions
- [x] 3 Monitores
- [x] 9 modelos GGUF
- [x] 16 API keys
- [x] 19 propuestas M3 aplicadas (1 rechazada)
- [x] 170 patches documentados
- [x] 18 Master Documentos completos

### Pendiente:
- [ ] 8 datos pre-flight de MAX
- [ ] Aprobación final de MAX
- [ ] M2.7 orden de instalación

---

## 7. RECOMENDACIONES PARA MAX

### Perfil recomendado: Equilibrado
Balance costo/calidad.

### Canales prioritarios: Telegram + API REST
Telegram para chat directo, API REST para integración.

### Lista inicial de proyectos: Pendiente decisión
MAX decide qué 8 productos crear.

### Visibilidad: Decisión pendiente
MAX decide si public o private.

---

## 8. CONCLUSIÓN

El sistema está 100% diseñado. Falta solo:
1. Los 8 datos pre-flight de MAX
2. Aprobación final
3. Orden de instalación a M2.7

Cuando MAX dé el GO, M2.7 ejecuta aprovisionamiento automático y reporta.
</content>