# DOCUMENTO 13: PARCHES EXTRAS Y HALLAZGOS DE RESEARCH
## Extraído del historial del chat

---

## 1. PARCHES-EXTRAS — CSA FASES DETALLADAS

### CSA-FASE-J1 · JUEZ 1: COMPRENSIÓN DEL OBJETIVO

Las 5 fases del juez:
- F1 · Audita input completo
- F2 · Busca lo que NADIE revisó
- F3 · 10 soluciones distintas
- F4 · Destruye propia solución
- F5 · Ataca otros 9 jueces

### CSA-FASE-J2 · JUEZ 2: COBERTURA DE REQUISITOS
- F1 · Audita input completo (lista TODOS los requisitos)
- F2 · Busca requisitos no escritos
- F3 · 10 mapeos requisito→output
- F4 · Busca requisitos olvidados
- F5 · "¿Cubriste este requisito?"

### CSA-FASE-J3 · JUEZ 3: CONSISTENCIA LÓGICA
- F1 · Lee todo el output
- F2 · Contradicciones internas, saltos lógicos
- F3 · 10 análisis lógicos distintos
- F4 · Busca fallas en su propio análisis
- F5 · "¿Esto contradice lo que otro dijo?"

### CSA-FASE-J4 · JUEZ 4: EXACTITUD TÉCNICA
- F1 · Revisa código, comandos, configs
- F2 · Errores técnicos sutiles, edge cases
- F3 · 10 verificaciones técnicas distintas
- F4 · Verifica referencias, sintaxis, versiones
- F5 · "¿El código realmente compila?"

### CSA-FASE-J5 · JUEZ 5: ARQUITECTURA Y DISEÑO
- F1 · Entiende la arquitectura propuesta
- F2 · Patrones incorrectos, acoplamiento, deuda técnica
- F3 · 10 arquitecturas alternativas
- F4 · Busca problemas de escalabilidad
- F5 · "¿Esta arquitectura escala?"

### CSA-FASE-J6 · JUEZ 6: CALIDAD DE CÓDIGO
- F1 · Lee todo el código
- F2 · Code smells, anti-patterns, magic numbers
- F3 · 10 alternativas de implementación
- F4 · Busca complejidad innecesaria
- F5 · "¿Hay mejor manera de escribir esto?"

### CSA-FASE-J7 · JUEZ 7: INVESTIGACIÓN Y EVIDENCIA
- F1 · Lista TODAS las afirmaciones del output
- F2 · Afirmaciones sin fuente, datos inventados
- F3 · 10 fuentes de evidencia distintas
- F4 · Cuestiona la credibilidad de las fuentes
- F5 · "¿De dónde sacaste este dato?"

### CSA-FASE-J8 · JUEZ 8: OPTIMIZACIÓN Y RENDIMIENTO
- F1 · Mide latencia, memoria, throughput
- F2 · Cuellos de botella, memory leaks
- F3 · 10 optimizaciones posibles
- F4 · Busca optimizaciones que empeoran legibilidad
- F5 · "¿Esto es realmente necesario?"

### CSA-FASE-J9 · JUEZ 9: SEGURIDAD Y RIESGOS
- F1 · Busca vulnerabilidades OWASP top 10
- F2 · Vulnerabilidades nuevas, supply chain attacks
- F3 · 10 análisis de seguridad distintos
- F4 · Busca formas de bypassear la seguridad
- F5 · "¿Esto es seguro de verdad?"

### CSA-FASE-J10 · JUEZ 10: CALIDAD FINAL Y UX
- F1 · Experimenta como usuario final
- F2 · Fricciones, confusión, ambigüedad
- F3 · 10 mejoras de UX posibles
- F4 · Busca errores de documentación
- F5 · "¿El usuario final lo entenderá?"

---

## 2. 13 CRITERIOS DE SKILLS (INDIVIDUALES)

### 1. Relevancia
- Score 0-10
- Comparar contra skills alternativas
- Considerar contexto del proyecto

### 2. Efectividad Comprobada
- Track record
- Casos de éxito
- Métricas históricas
- Feedback de usuarios

### 3. Costo de Aplicación
- Tokens consumidos
- Tiempo de ejecución
- Recursos necesarios
- Costo monetario

### 4. Compatibilidad
- Universal Plug v1.5
- Otros módulos
- Skills relacionadas
- Modelos disponibles

### 5. Mantenibilidad
- Complejidad
- Documentación
- Dependencias
- Facilidad de actualizar

### 6. Documentación
- README
- Ejemplos
- API docs
- Casos de uso
- Troubleshooting

### 7. Reusabilidad
- Generalidad
- Parametrización
- Abstracción
- Aplicabilidad múltiple

### 8. Seguridad
- Vulnerabilidades
- Permisos necesarios
- Sandboxing
- Validación de inputs

### 9. Performance
- Latencia
- Throughput
- Recursos consumidos
- Benchmarks

### 10. Escalabilidad
- Comportamiento con 10x datos
- Comportamiento con 100x datos
- Horizontal scaling
- Resource limits

### 11. Compliance
- GDPR
- Licencias de código
- Privacidad
- Regulaciones del dominio

### 12. Test Coverage
- Unit tests
- Integration tests
- Edge cases
- Coverage %

### 13. Comunidad / Soporte
- Stars en GitHub
- Issues resueltos
- Mantenedores activos
- Foros / Discord
- Actualizaciones recientes

---

## 3. 5 AGENTES DE INVESTIGACIÓN (DETALLADOS)

### 1. GitHub Agent
**Qué busca:**
- Repos públicos relevantes
- Stars, forks, issues
- Patrones de uso
- Código de referencia
- Proyectos similares

**Outputs:**
- Lista de repos con metadata
- Análisis de calidad
- Código reutilizable
- Issues recurrentes

### 2. HuggingFace Agent
**Qué busca:**
- Modelos GGUF disponibles
- Datasets relevantes
- Spaces con código útil
- Papers referenciados
- Versiones y updates

**Outputs:**
- Lista de modelos con URLs
- Datasets descargables
- Código de Spaces
- Estado de las APIs

### 3. Web Agent
**Qué busca:**
- Documentación oficial
- Artículos técnicos
- Tutoriales
- Best practices
- Comparativas
- Precios/costos

**Outputs:**
- URLs relevantes
- Resúmenes
- Comparativas
- Recomendaciones

### 4. YouTube Agent
**Qué busca:**
- Tutoriales paso a paso
- Demos de productos
- Conferencias técnicas
- Comparativas visuales
- Casos de estudio

**Outputs:**
- URLs de videos
- Transcripciones relevantes
- Timestamp de momentos clave
- Resúmenes visuales

### 5. MCP Agent
**Qué busca:**
- MCP servers disponibles
- Tools registrados
- Integraciones oficiales
- Smithery catálogo
- Composio integraciones

**Outputs:**
- Lista de MCP servers
- Tools utilizables
- Compatibilidad
- Configuración necesaria

---

## 4. 8 HALLAZGOS DE RESEARCH

### RESEARCH-1 · DEERFLOW 2.0 (BYTEDANCE)
```
- Autor: ByteDance
- GitHub: 46k stars
- Tipo: Super Agent Harness
- Aporta: Orquesta sub-agentes, Memory, Sandboxes, Skills, Message Gateway
- REUTILIZABLE como base
```

### RESEARCH-2 · LITELLM
```
- Tipo: LLM Gateway
- Unifica 100+ LLMs en 1 API
- Reemplaza 16 adapters
- Aporta: Una sola interfaz, routing automático, fallback, load balancing
```

### RESEARCH-3 · MICROSOFT AGENT FRAMEWORK (MAF)
```
- Autor: Microsoft
- Tipo: Production-ready multi-agent
- Aporta: Workflows production-ready, patrones probados, documentación
```

### RESEARCH-4 · AGENTORCHESTRA
```
- Tipo: Patrón jerárquico multi-agent
- Score: 83.39% en GAIA benchmark
- Aporta: Patrón de orquestación jerárquica, alta performance, validado empíricamente
```

### RESEARCH-5 · OPENCLAW
```
- GitHub: 308k stars
- Tipo: Gateway + channels + skills + MCP
- Aporta: Gateway unificado, múltiples canales, Skills integradas, MCP support
```

### RESEARCH-6 · HERMES AGENT
```
- GitHub: 149k stars
- Tipo: Learning loop agent
- Aporta: Learning loop L1+L2+L3, mejora continua, adaptación al usuario, memory persistente
```

### RESEARCH-7 · LANGGRAPH
```
- GitHub: 115k stars
- Tipo: State machine para agents
- Aporta: Grafos de estado, ciclos, persistencia, human-in-the-loop, patrones complejos
```

### RESEARCH-8 · CREWAI
```
- GitHub: 102k stars
- Tipo: Multi-agent framework
- Aporta: Concepto de Crew, roles definidos, tasks asignables, process management
```

---

## 5. 23 DESTINOS DE MULTI-TARGET DELIVERY

### Archivos / Documentos (5)
1. Markdown (.md)
2. PDF
3. HTML
4. DOCX
5. Texto plano

### Código (5)
6. ZIP
7. GitHub repo
8. GitLab repo
9. Bitbucket
10. Paquete (tarball)

### Datos (3)
11. JSON
12. YAML
13. XML

### Comunicación (3)
14. Email
15. Slack/Discord
16. Telegram

### Almacenamiento (3)
17. Drive Mavis
18. S3-compatible
19. HF Dataset

### APIs (2)
20. REST API
21. Webhook

### Otros (2)
22. MCP server
23. Streaming output

---

## 6. CAPAS DEL SISTEMA (RESUMEN)

### APLICADAS (vía patches individuales):
- **9 patches OUTPUT v6.1** (capas A-P gobernanza)
- **9 patches INPUT v4.0** (capas A-I)
- **15 patches LOOP v6.0** (capas A-O)

### PROPUESTAS M3 APLICADAS:
- **9 patches OUTPUT** (Pre-Mortem, Auto-Rollback, Meta-Learning, Personalization, Multi-Stakeholder, Causal Tracing, Marketplace, Self-Improving, Production Monitoring)
- **10 patches INPUT/LOOP** (Meta-agentes, Causalidad, Counterfactual, Auto-modificación, Memoria Episódica, Zero-shot transfer, NAS, Time-travel, Inteligencia colectiva, Auto-curriculum)

### PENDIENTE:
- ~~Output Sandbox~~ ❌ RECHAZADO POR MAX

---

## 7. PATCHES TOTALES (170)

### Parches Output v6.1 (9):
1. Pre-Mortem Analysis ✅
2. Output Sandbox ❌ RECHAZADO
3. Auto-Rollback Inteligente ✅
4. Meta-Learning entre Releases ✅
5. Output Personalization ✅
6. Multi-Stakeholder Output ✅
7. Causal Output Tracing ✅
8. Output Marketplace Interno ✅
9. Self-Improving Output Quality ✅
10. Production Monitoring Post-Publish ✅

### Parches Output v6.1 Gobernanza (16):
A-P. Las 16 capas del Output Governor

### Parches Input v4.0 (9):
A-I. Las 9 capas del Input Engine

### Parches Loop v6.0 (15):
A-O. Las 15 capas del Loop

### Parches Propuestas Input/Loop (10):
1-10. Las 10 propuestas M3 para INPUT/LOOP

### Parches Orquestador (51):
- Constitución v1.0 (13 principios)
- Constitución v2.0 (13 principios)
- Constitución v3.0 (componentes)
- Estructura interna (7 componentes)
- Pipeline (2)
- Fases (1)
- Razonamiento (2)
- Configuraciones (1)
- Subsistemas (5)
- Componentes críticos (7)

### Parches Infra (23):
- 6 grupos (G1-G6)
- 9 modelos GGUF
- 3 APIs
- Categorías BIS
- Skills recomendadas
- Capacidades
- Costo $0
- Pre-flight pendientes

### Parches Extras (37):
- CSA Fases (10 jueces × 5 fases)
- Skills Criterios (13 individuales)
- Investigación Agentes (5 individuales)
- Hallazgos Research (8)
- Delivery Destinos (1)

---

## 8. INFORMACIÓN GUARDADA EN MEMORIA PERSISTENTE

### Topics:
1. **nct-fase0-memory** (estado del proyecto)
2. **nct-patches-completos** (índice de los 170 patches)

### Información respaldada:
- Decisiones cerradas
- Patches aplicados
- Versiones (v1.0 → v6.2)
- Decisiones pendientes
- Estado del proyecto
- Sobrevive a cierres de sesión

---

## 9. PROMPT DSL DE MAXBRY (Resumen)

```
DSL es un lenguaje declarativo-generativo en Python
donde cada acción de NCT se describe como un módulo con:
- inputs
- outputs
- contract
- dependencies
- consensus_required
- runtime

El motor G2 lee esos módulos y los ejecuta.
NO es un system prompt — es código Python real.
```

### Cada módulo NCT:
```
nct.<taller>.<verbo>
├── id
├── version
├── owner_workshop
├── description
├── inputs
├── outputs
├── contract
├── dependencies
├── consensus
├── runtime
├── memory_keys
├── llm_budget
└── validators
```

### Reglas:
- `id` debe ser jerárquico: `nct.<taller>.<verbo>`
- `contract` se valida antes y después
- `dependencies` se resuelven con DAG
- `consensus.required = true` → pasa por 5 agentes
- `memory_keys` son punteros a Xata
- `llm_budget` limita tokens por módulo
- Al menos 2 validators (schema + negocio)

---

## 10. TALLERES DE NCT (Referencias)

Los talleres son las áreas de trabajo:

- **FRONTEND** - generación de UI/UX
- **DISEÑO** - tokens visuales, theming
- **ARQUITECTURA** - diseño de sistemas
- **BACKEND** - lógica de servidor
- **CREATIVIDAD** - consensos, ideas
- **TESTING** - generación de tests
- **DEVOPS** - integración continua
- **RAG** - búsqueda vectorial
- **RESEARCH** - investigación web
- **VALIDACIÓN** - quality assurance

---

## 11. ESTADO FINAL DE LA AUDITORÍA

### Documentos consolidados creados: 13+
### Total bytes extraídos del chat: ~130KB
### Total parches individuales: 170
### Total código Python: 726 líneas
### Constitución: 1276 líneas
### Memoria persistente: 2 topics
</content>