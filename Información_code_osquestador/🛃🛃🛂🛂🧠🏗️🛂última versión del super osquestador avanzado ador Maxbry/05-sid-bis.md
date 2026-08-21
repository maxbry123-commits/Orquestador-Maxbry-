# MASTER DOCUMENTO 05: SID + BIS COMPLETO
## MAXBRY SUPER TEAM · SID 5 Preguntas + BIS 14 Categorías

**Versión:** 1.0
**Fecha:** 2026-06-28
**Tipo:** Master Document
**Max chars:** 60,000
**Estado:** ✅ COMPLETO

---

## 1. SID — SISTEMA INTELIGENTE DE DEFINICIÓN

### 1.1 Propósito

Antes de producir cualquier cosa, el sistema **define QUÉ es** el proyecto/tarea. Esto evita el 90% de los errores que ocurren por malentendidos.

### 1.2 Las 5 Preguntas Fijas (NUNCA cambian)

#### Pregunta 1: ¿QUÉ ES ESTO?
**Output esperado:** Definición clara y concisa en 1-2 oraciones.

**Ejemplo:**
```
Tarea: "Crear API REST"
SID-Q1: "API REST para gestión de tareas multi-tenant 
        con autenticación JWT y rate limiting."
```

#### Pregunta 2: ¿PARA QUIÉN ES?
**Output esperado:** Audiencia objetivo específica.

**Ejemplo:**
```
SID-Q2: "Equipos de desarrollo de 5-50 personas que 
        necesitan SaaS de productividad sin inversión 
        inicial en infraestructura."
```

#### Pregunta 3: ¿QUÉ PROBLEMA RESUELVE?
**Output esperado:** Pain point específico y cuantificable.

**Ejemplo:**
```
SID-Q3: "Equipos pequeños gastan $500+/mes en SaaS 
        comerciales y necesitan alternativa económica 
        con control total de datos."
```

#### Pregunta 4: ¿CÓMO SE USA?
**Output esperado:** Ejemplo de uso real paso a paso.

**Ejemplo:**
```
SID-Q4: "1. POST /auth/login → JWT
        2. POST /tasks con JWT → crear tarea
        3. GET /tasks → listar
        4. Webhook on task.completed"
```

#### Pregunta 5: ¿QUÉ NO ES?
**Output esperado:** Exclusiones explícitas.

**Ejemplo:**
```
SID-Q5: "NO es:
        - NO es un SaaS público
        - NO es para empresas > 1000 empleados
        - NO incluye UI web (solo API)
        - NO reemplaza Jira/Monday (más simple)"
```

### 1.3 Definition Score

Cada respuesta se puntúa:
- **0-20:** Vacío o incorrecto
- **21-50:** Parcial
- **51-80:** Aceptable
- **81-94:** Bueno
- **95-100:** Excelente

**Score agregado ≥ 95%** requerido para continuar producción.

### 1.4 Ejecución

```python
async def run_sid(task: str) -> dict:
    questions = [
        "What is this?",
        "Who is it for?",
        "What problem does it solve?",
        "How is it used?",
        "What is it NOT?"
    ]

    answers = []
    for q in questions:
        # 90% mecánico (templates), 10% LLM si es complejo
        ans = await generate_answer(task, q)
        score = await score_answer(ans)
        answers.append({"q": q, "a": ans, "score": score})

    total_score = sum(a["score"] for a in answers) / 5

    return {
        "answers": answers,
        "total_score": total_score,
        "decision": "pass" if total_score >= 95 else "fail"
    }
```

---

## 2. BIS — BIBLIOTECA INTELIGENTE DE SKILLS

### 2.1 Propósito

BIS es el **único repositorio** de skills del sistema. Cualquier skill nueva debe pasar por BIS.

### 2.2 Las 14 Categorías

#### A · ARQUITECTURA
Diseño de sistemas, patrones, decisiones arquitectónicas, C4, arc42.

#### B · GESTIÓN
Gestión de proyectos, planificación, recursos, scrum, kanban.

#### C · FRONTEND
HTML, CSS, JS, frameworks UI/UX (React, Vue, Svelte, etc.).

#### D · BACKEND
APIs, servidores, lógica de negocio, microservicios.

#### E · MÓVIL
iOS, Android, React Native, Flutter, Swift, Kotlin.

#### F · ESCRITORIO
Aplicaciones desktop, Electron, Tauri, GTK, Qt.

#### G · BASES DE DATOS
SQL (PostgreSQL, MySQL), NoSQL (MongoDB), vectoriales (Qdrant, Pinecone).

#### H · APIs
REST, GraphQL, gRPC, webhooks, OpenAPI.

#### I · DEVOPS
CI/CD (GitHub Actions, GitLab CI), Docker, K8s, Terraform.

#### J · IA
LLMs, ML, agentes, RAG, fine-tuning, embeddings.

#### K · TESTING
Unit (Jest, pytest), integration, E2E (Playwright, Cypress), performance.

#### L · SEGURIDAD
Auth (OAuth, JWT), encryption, vulnerabilities, OWASP, secrets.

#### M · AUTOMATIZACIÓN
Scripts, workflows, RPA, schedulers, cron jobs.

#### N · LENGUAJES
Python, JS, Go, Rust, Java, C++, Ruby, PHP, Swift, Kotlin.

### 2.3 Los 13 Criterios de Skills

Una skill debe cumplir 13 criterios para ser aprobada:

1. **Nombre claro** - Identifica la skill
2. **Descripción** - 1-2 oraciones
3. **Categoría** - Una de las 14
4. **Inputs** - Schema definido
5. **Outputs** - Schema definido
6. **Tiempo medio** - Estimación
7. **Recursos** - CPU/RAM/disk
8. **Dependencias** - Skills que requiere
9. **Tests** - Al menos 3 unit tests
10. **Documentación** - README
11. **Ejemplos** - 2+ ejemplos
12. **Versión** - Semver
13. **Mantenimiento** - Owner asignado

### 2.4 Las 3 Versiones de Skills

#### v1 — Skills Básicas
- Una sola responsabilidad
- Sin estado
- Síncronas
- ≤ 200 LOC

#### v2 — Skills Avanzadas
- Multi-responsabilidad relacionada
- Estado en memoria
- Asíncronas permitidas
- ≤ 500 LOC

#### v3 — Skills Complejas
- Orquestación de otras skills
- Estado persistente
- Asíncronas con callbacks
- ≤ 2000 LOC

### 2.5 Debate de Skills (4 Especialistas)

Antes de aprobar una skill nueva, 4 especialistas debaten:

| Especialista | Pregunta |
|--------------|----------|
| **Arquitecto** | ¿Es coherente con la arquitectura? |
| **Implementador** | ¿Es implementable? |
| **Tester** | ¿Es testeable? |
| **Critic** | ¿Vale la pena? |

Si 3+ están de acuerdo → aprobada. Si no → rechazada.

---

## 3. INTEGRACIÓN SID + BIS

### 3.1 Flujo

```
Tarea nueva
    ↓
SID (5 preguntas)
    ↓
Score ≥ 95%? → No → Bloquea
    ↓ Sí
BIS busca skills relevantes
    ↓
Skills encontradas (≥ 3)
    ↓
Aplica skill primaria
    ↓
Skill genera output
    ↓
CSA audita
    ↓
Output final
```

### 3.2 Skills derivadas de SID

Las respuestas a las 5 preguntas de SID alimentan BIS:

```
SID-Q1 → Categorías A-N relacionadas
SID-Q2 → Audiencia objetivo → skills UX
SID-Q3 → Problema → skills de solución
SID-Q4 → Ejemplo → tests derivados
SID-Q5 → Exclusiones → skills excluidas
```

---

## 4. EJEMPLO COMPLETO

### Tarea: "Crear chatbot de Telegram con LLM"

### SID:
```
Q1: Bot de Telegram que responde preguntas usando LLM
    con RAG sobre documentos del usuario.

Q2: Desarrolladores y profesionales que quieren consultar
    sus documentos desde el móvil sin abrir laptop.

Q3: Consultar docs en PC requiere abrir laptop, buscar,
    abrir, leer. Bot Telegram responde en segundos.

Q4: 1. User sube PDF a bot
    2. Bot indexa en vector DB
    3. User pregunta
    4. Bot busca chunks relevantes
    5. Bot sintetiza respuesta con LLM

Q5: NO es:
    - NO es app móvil nativa
    - NO procesa imágenes
    - NO tiene memoria entre conversaciones
```

**Score:** 96/100 → APROBADO

### BIS Lookup:
- Categoría H (APIs) → skills de Telegram Bot
- Categoría J (IA) → skills de RAG
- Categoría G (BASES DE DATOS) → skills de vector DB
- Categoría C (FRONTEND) → skills de UX conversacional

**Skills seleccionadas:** 5

### Producción:
Aplica skills en orden DAG → output final → CSA audita.

---

## 5. AUDITORÍA BIS

### Periodicidad
- Auto-curación: cada 7 días
- Auditoría completa: cada 30 días
- Auditoría por evento: cuando se añade skill

### Métricas
- Skills totales
- Skills usadas (últimos 30 días)
- Skills huérfanas
- Skills duplicadas
- Skills con bugs

---

## 6. CONCLUSIÓN

SID garantiza que sabemos QUÉ queremos. BIS garantiza que tenemos CÓMO hacerlo. Juntos, eliminan el 90% de errores por malentendidos y falta de recursos.
</content>