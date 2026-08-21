# SALIDA E — PIPELINE ENTRADA · DOC 3/3
# GRUPO E4 CLASIFICACIÓN, GOAL Y COMPILACIÓN (E-049..E-072) + NOTA: QUÉ FALTA PARA ARRANCAR.

---

## GRUPO E4 — CLASIFICACIÓN, GOAL Y COMPILACIÓN (E-049..E-072)

**Qué hace el grupo:** convierte el documento limpio y analizado en: clasificación PUSH_PING completa → GoalLock congelado → task graph → requirements.json listo para el PLANNER_OFFLINE. Nada avanza incompleto.
**Microdiagrama:** `PUSH_PING 30 ➜ SID/BIS ➜ DRE ➜ GOAL_LOCK ➜ task graph ➜ presupuesto/keys/cuotas ➜ simular×5 ➜ requirements ➜ 🛂`
**Instrucción Sonnet 10x (grupo):** tabla PUSH_PING completa de 30 campos desde YAML, DRE con features aprendidas del histórico, simulador con detección real de colisiones de recursos, y formulario Telegram inline para DoD.

```python
"""fichas/entrada/e4_goal.py — E-049..E-072."""
from __future__ import annotations
import json, time, uuid
from pathlib import Path
from ficha_base import Ficha, FichaError, hash_doc


class E049PushPing30(Ficha):
    ID = "e.goal.push_ping_30"
    # Los 30 campos con estrategia si_falta (tabla completa en push_ping.yaml)
    CAMPOS = {**{f"c{i:02d}": "auto" for i in range(1, 31)},
              "c01": "preguntar_director",   # OBJETIVO_PRIMARIO
              "c03": "juez_evalua",          # TASK_LEVEL
              "c06": "juez_consenso",        # DoD
              "c19": "juez_congela"}         # GOAL_LOCK

    async def logic(self, ctx, p):
        tabla = p.get("push_ping", {})
        faltan = [c for c in self.CAMPOS if c not in tabla]
        resueltos = {c: {"si_falta": self.CAMPOS[c]} for c in faltan
                     if self.CAMPOS[c] == "auto"}
        pendientes = [c for c in faltan if self.CAMPOS[c] != "auto"]
        return {"proposals": [self.prop("goal.push_ping_faltan", pendientes),
                              self.prop("goal.push_ping_auto", resueltos)],
                "status": "RETRY" if pendientes else "DONE",
                "necesito": ["director_pregunta"] if pendientes else []}


class E050Sid5Preguntas(Ficha):
    ID = "e.goal.sid_5"
    Q = ("que", "por_que", "como", "cuando", "con_que")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        sid = {q: q.replace("_", " ") in t or q == "que" for q in self.Q}
        return {"proposals": [self.prop("goal.sid", sid),
                              self.prop("goal.sid_score",
                                        sum(sid.values()) / 5)]}


class E051Bis14Categorias(Ficha):
    ID = "e.goal.bis_14"
    CATS = ("codigo", "arquitectura", "investigacion", "documento",
            "reparacion", "test", "deploy", "datos", "seguridad",
            "diseño", "planificacion", "auditoria", "memoria", "otros")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        scores = {c: t.count(c[:6]) for c in self.CATS}
        cat = max(scores, key=scores.get) if any(scores.values()) else "otros"
        return {"proposals": [self.prop("goal.bis", cat)]}


class E052DreEstimator(Ficha):
    ID = "e.goal.dre_estimator"
    async def logic(self, ctx, p):
        deps = len(p.get("refs", []))
        steps = max(1, p.get("n_bloques", 1) // 3)
        score = (deps * 2 + steps
                 + (5 if p.get("ambiguedad", 0) >= 0.4 else 0)
                 + (5 if p.get("bis") in ("seguridad", "deploy") else 0))
        nivel = ("LOW" if score <= 3 else "MEDIUM" if score <= 8
                 else "HIGH" if score <= 15 else "EXTREME")
        return {"proposals": [self.prop("goal.dre", {"score": score,
                                                     "nivel": nivel})]}


class E053GoalLockBuilder(Ficha):
    ID = "e.goal.goal_lock_builder"
    async def logic(self, ctx, p):
        if not p.get("objetivo") or not p.get("dod"):
            return {"status": "RETRY",
                    "necesito": ["dod_generator"],
                    "proposals": [self.prop("goal.lock", None)]}
        lock = {"objetivo": p["objetivo"], "dod": list(p["dod"]),
                "not_in_scope": list(p.get("not_in_scope", [])),
                "fuente_verdad": p.get("fuente_verdad", ""),
                "ts": time.time()}
        lock["hash"] = hash_doc(lock)
        return {"proposals": [self.prop("goal.lock", lock)]}


class E054DodGenerator(Ficha):
    ID = "e.goal.dod_generator"                  # hybrid: propone, Juez valida
    async def logic(self, ctx, p):
        r = await self.router.despachar("dod_desde_objetivo", {
            "objetivo": p.get("objetivo", ""),
            "contexto": str(p.get("contenido", ""))[:6000]},
            trace_id=ctx.get("trace_id", ""))
        if r["status"] != "DONE":
            return {"status": "ESCALATE",
                    "proposals": [self.prop("goal.dod_pregunta",
                                            "Director: define DoD")]}
        return {"proposals": [self.prop("goal.dod_propuesto", r["output"]),
                              self.prop("goal.dod_requiere_aprobacion",
                                        True)]}


class E055TaskGraphBuilder(Ficha):
    ID = "e.goal.task_graph_builder"
    async def logic(self, ctx, p):
        bloques = p.get("bloques", [])
        nodos = [{"id": f"T{i:03d}", "texto": b[:200], "depends_on":
                  [f"T{i-1:03d}"] if i and "luego" in b.lower() else []}
                 for i, b in enumerate(bloques)]
        return {"proposals": [self.prop("goal.task_graph", nodos)]}


class E056RequirementsCompiler(Ficha):
    ID = "e.goal.requirements_compiler"
    async def logic(self, ctx, p):
        if not p.get("lock"):
            raise FichaError("sin_goal_lock")
        req = {"task_id": ctx["task_id"], "goal_lock": p["lock"],
               "dre": p.get("dre", {}), "bis": p.get("bis", "otros"),
               "nivel_cognitivo": p.get("nivel", "n1"),
               "pasos": [{"ficha_id": n["id"],
                          "depends_on": n["depends_on"]}
                         for n in p.get("task_graph", [])],
               "batch": p.get("batch", {}),
               "presupuesto": p.get("presupuesto", {})}
        ruta = Path(f"runtime/plans/{ctx['task_id']}/requirements.json")
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(json.dumps(req, ensure_ascii=False, indent=1))
        return {"proposals": [self.prop("goal.requirements_ref", str(ruta)),
                              self.prop("goal.requirements_hash",
                                        hash_doc(req))]}


class E057DirectorQuestionQueue(Ficha):
    ID = "e.goal.director_queue"
    async def logic(self, ctx, p):
        qs = p.get("preguntas", [])
        if qs and self.router:
            await self.router.despachar("notificar", {
                "canal": "telegram",
                "msg": "PREGUNTAS:\n" + "\n".join(
                    f"{i+1}. {q}" for i, q in enumerate(qs))},
                trace_id=ctx.get("trace_id", ""))
        return {"proposals": [self.prop("goal.preguntas_enviadas",
                                        len(qs))]}


class E058BatchSegmentador(Ficha):
    ID = "e.goal.batch_segmentador"
    async def logic(self, ctx, p):
        n = len(p.get("task_graph", [])) or 1
        modo = ("secuencial" if n <= 3 else "paralelo" if n <= 50
                else "swarm" if n <= 400 else "fractal")
        return {"proposals": [self.prop("goal.batch", {
            "total": n, "batch_size": 20, "overlap": 5, "modo": modo,
            "prioridad": p.get("urgencia", "normal")})]}


class E059FichaIdentidadGen(Ficha):
    ID = "e.goal.ficha_identidad"
    async def logic(self, ctx, p):
        return {"proposals": [self.prop("goal.identidad", {
            "id": str(uuid.uuid4()), "tipo": p.get("tipo", "ficha_g2"),
            "version": "1.0.0", "historial": [],
            "failure_registry": []})]}


class E060SimuladorPlanX5(Ficha):
    ID = "e.goal.simulador_x5"
    async def logic(self, ctx, p):
        grafo = {n["id"]: set(n["depends_on"])
                 for n in p.get("task_graph", [])}
        colisiones = []
        for corrida in range(5):
            vistos: set[str] = set()
            for nid, deps in grafo.items():
                if not deps <= vistos and deps - set(grafo):
                    colisiones.append({"corrida": corrida, "nodo": nid,
                                       "dep_inexistente":
                                       list(deps - set(grafo))})
                vistos.add(nid)
        return {"proposals": [self.prop("goal.simulaciones",
                                        {"corridas": 5,
                                         "colisiones": colisiones})],
                "status": "FAIL" if colisiones else "DONE"}


class E061PreflightPresupuesto(Ficha):
    ID = "e.goal.preflight_presupuesto"          # ✚
    COSTO_NIVEL = {"n0": 1, "n1": 2, "n2": 5, "n3": 12, "n4": 30, "n5": 80}

    async def logic(self, ctx, p):
        n = len(p.get("task_graph", [])) or 1
        unidades = n * self.COSTO_NIVEL.get(p.get("nivel", "n1"), 2)
        limite = p.get("limite_unidades", 500)
        return {"proposals": [self.prop("goal.presupuesto", {
            "estimado": unidades, "limite": limite})],
            "status": "ESCALATE" if unidades > limite else "DONE"}


class E062CredentialsChecker(Ficha):
    ID = "e.goal.credentials_checker"            # ✚
    async def logic(self, ctx, p):
        import os
        requeridas = p.get("keys_requeridas",
                           ["OPENROUTER_KEY", "GITHUB_TOKEN"])
        faltan = [k for k in requeridas if k not in os.environ]
        return {"proposals": [self.prop("goal.keys_faltantes", faltan)],
                "status": "ESCALATE" if faltan else "DONE"}


class E063ApiQuotaChecker(Ficha):
    ID = "e.goal.api_quota_checker"              # ✚
    async def logic(self, ctx, p):
        r = await self.router.despachar("quota_status", {},
                                        trace_id=ctx.get("trace_id", ""))
        quotas = r.get("output", {})
        agotadas = [k for k, v in quotas.items()
                    if isinstance(v, (int, float)) and v <= 0]
        return {"proposals": [self.prop("goal.quotas", quotas)],
                "status": "RETRY" if agotadas else "DONE"}


class E064DeadlineNegotiator(Ficha):
    ID = "e.goal.deadline_negotiator"            # ✚
    HORAS = {"LOW": 2, "MEDIUM": 12, "HIGH": 48, "EXTREME": 168}

    async def logic(self, ctx, p):
        nivel = p.get("dre", {}).get("nivel", "MEDIUM")
        cola = p.get("tareas_en_cola", 0)
        horas = self.HORAS[nivel] + cola * 2
        return {"proposals": [self.prop("goal.deadline_propuesto_h",
                                        horas)]}


class E065TaskSplitterRepo(Ficha):
    ID = "e.goal.task_splitter_repo"             # ✚
    async def logic(self, ctx, p):
        import re as _re
        repos = sorted(set(_re.findall(
            r"repo[s]?\s+([a-z0-9\-_]+)", str(p["contenido"]).lower())))
        return {"proposals": [self.prop("goal.repos_afectados",
                                        repos or ["default"])]}


class E066TenantNamespacer(Ficha):
    ID = "e.goal.tenant_namespacer"              # ✚
    PROYECTOS = ("jarvis", "spacein", "nct", "maxbry", "yaiwes")

    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        tenant = next((x for x in self.PROYECTOS if x in t), "maxbry")
        return {"proposals": [self.prop("goal.tenant", tenant)]}


class E067UrgenciaClassifier(Ficha):
    ID = "e.goal.urgencia_classifier"            # ✚
    async def logic(self, ctx, p):
        t = str(p["contenido"]).lower()
        urg = ("critical" if any(w in t for w in
                                 ("urgente", "ya", "producción caída",
                                  "critical")) else
               "background" if any(w in t for w in
                                   ("cuando puedas", "algún día"))
               else "normal")
        return {"proposals": [self.prop("goal.urgencia", urg)]}


class E068EnvironmentSnapshotter(Ficha):
    ID = "e.goal.environment_snapshotter"        # ✚
    async def logic(self, ctx, p):
        import platform, sys
        return {"proposals": [self.prop("goal.entorno", {
            "python": sys.version.split()[0],
            "so": platform.system(), "ts": time.time()})]}


class E069FormGeneratorDod(Ficha):
    ID = "e.goal.form_generator_dod"             # ✚
    async def logic(self, ctx, p):
        form = {"titulo": "Definir DoD",
                "campos": [{"id": "criterio_1", "tipo": "texto"},
                           {"id": "criterio_2", "tipo": "texto"},
                           {"id": "not_in_scope", "tipo": "texto"},
                           {"id": "fuente_verdad", "tipo": "texto"}]}
        return {"proposals": [self.prop("goal.form_dod", form)],
                "necesito": ["telegram_form"]}


class E070InputReplayCache(Ficha):
    ID = "e.goal.input_replay_cache"             # ✚
    async def logic(self, ctx, p):
        ruta = Path(f"runtime/replay/{p['doc_id']}.json")
        if ruta.exists():
            return {"proposals": [self.prop(
                "goal.replay", json.loads(ruta.read_text()))],
                "status": "SKIP"}
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(json.dumps({"resultado_e": p.get("resultado", {})},
                                   default=str))
        return {"proposals": [self.prop("goal.replay", None)]}


class E071DependencyPrechecker(Ficha):
    ID = "e.goal.dependency_prechecker"          # ✚
    async def logic(self, ctx, p):
        r = await self.router.despachar("registry.status", {
            "fichas": p.get("fichas_requeridas", [])},
            trace_id=ctx.get("trace_id", ""))
        estados = r.get("output", {})
        no_ok = [f for f, s in estados.items() if s != "COMMITTED"]
        return {"proposals": [self.prop("goal.deps_no_committed", no_ok)],
                "status": "FAIL" if no_ok else "DONE"}


class E072GoalVerifier(Ficha):
    ID = "e.goal.goal_verifier"                  # 🛂 gate final del pipeline E
    async def logic(self, ctx, p):
        checks = {"goal_lock": bool(p.get("lock", {}).get("hash")),
                  "requirements": bool(p.get("requirements_ref")),
                  "push_ping_completo": not p.get("push_ping_faltan"),
                  "sin_colisiones": not p.get("simulaciones",
                                              {}).get("colisiones"),
                  "presupuesto_ok": p.get("presupuesto",
                                          {}).get("estimado", 0)
                  <= p.get("presupuesto", {}).get("limite", 1)}
        malos = [k for k, v in checks.items() if not v]
        return {"proposals": [self.prop("goal.gate_e", checks)],
                "status": "FAIL" if malos else "DONE"}
```

**Contratos del grupo:** E-054/E-063/E-071 `runtime_type:hybrid`; E-049/E-053/E-072 `bloqueante:true`; E-060 `repeticion:{max:2, condicion:si_falla_verificacion}`; todos `repite_en:[CONTEXT_LOADER, MASTER_JSON]`.

**Wiring del PIPELINE E (orden de ejecución, DSL DAG):**
```
E-001→E-002→(E-006‖E-007‖E-004)→E-005→E-008→E-009→E-010→E-011
→E-017→E-018🛑→(E-022‖E-023‖E-024🛑‖E-028)→E-026→E-027→E-019→E-020→E-021
→(E-029‖E-030‖E-031)→E-032🛂
→(E-033..E-037 en paralelo)→E-038→E-039→E-040→E-041→E-042→E-043→(E-044‖E-045‖E-046‖E-047‖E-048)
→E-049→(E-050‖E-051)→E-052→E-053↺E-054/E-069→E-055→(E-058‖E-059‖E-064..E-068)
→(E-061‖E-062‖E-063‖E-071)→E-060→E-056→E-057→E-070→E-072🛂 → PLANNER_OFFLINE
```

---

# 📌 NOTA — QUÉ TE FALTA A NIVEL DE PROGRAMACIÓN PARA ARRANCAR EL ORQUESTADOR

Del más urgente al menos:
1. **main.py de ensamblaje real**: instanciar State+Juez+Pool+Router+Red y conectar los puertos (el esqueleto de 30 líneas está en Salida 5+6; falta escribirlo con imports reales y correrlo).
2. **Salidas P y S**: los pipelines PROCESADOR y SALIDA con su código (siguientes 2 salidas). Sin P no hay ejecución; sin S no hay entrega.
3. **Los YAML de expertos** (E001-E300): existe el motor, faltan los archivos de configuración (0 LOC c/u, pero hay que escribirlos — puede generarlos Sonnet con plantilla).
4. **Claves en entorno**: OPENROUTER_KEY, GITHUB_TOKEN, HF_TOKEN, TELEGRAM_WEBHOOK_URL, BAIDU_OCR (opcional), GPG key para firmas. Solo Railway Variables/env.
5. **Primer sequence.json real**: correr PLANNER_OFFLINE con un requirements.json de una tarea pequeña tuya (MVP paso 1 del plan G2).
6. **Deploy**: subir a Railway/HF Space (puerto 7860), GitHub Actions keep-alive 5 min, y el workflow CI con los tests IT01-06 + AX.
7. **vps_agent** (mini FastAPI con whitelist) SOLO si vas a usar el conector VPS.
8. **Poblar el atlas** (S18): correr `generar_atlas()` con los nodos reales para tener los ~50 HTML.
9. **contracts en disco**: generar los .contract.json v2.0 de cada ficha (plantilla dada; Sonnet los produce en lote).
10. **Pruebas de humo**: 1 tarea end-to-end E→P→S con evidencia L1-L4 antes de darlo por vivo.

**Tests del doc:** `test_push_ping_incompleto_retry · test_goal_sin_dod_escala · test_simulador_detecta_dep_inexistente · test_gate_e_bloquea · test_keys_faltantes_escalate`
