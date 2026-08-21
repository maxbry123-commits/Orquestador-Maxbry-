PIPELINE_DSL_DAG_SHERIFF_V7 | MODE=STRICT | LOOP=INFINITO_HASTA_CERTIFICAR | ORDEN=EJECUTA_NO_EXPLIQUES

ORDEN_DIRECTA→Lee INPUT_BLOCK literal. Ejecuta TODO el pipeline. Resuelve cada gap tú mismo. No preguntes. No expliques pasos. No pidas autorización salvo bloqueo externo real (clave/credencial/permiso ajeno). Al final entrega SOLO el FORMATO_SALIDA.

═INPUT_BLOCK(fuente única de verdad, leer literal, no interpretar, no resumir, no omitir)═
OBJECTIVE: [PEGAR]
TASKS: [PEGAR]
CONSTRAINTS: [PEGAR]
SUCCESS_CRITERIA: [PEGAR]
PRIORITY: [PEGAR]

═DAG_MAESTRO(horizontal)═
INPUT→PRECHECK→AUDIT→DISCOVERY→INVENTORY→REGISTER→SANDBOX→MEMORY→WORKSPACE→HEALTH→HEARTBEAT→CONNECTIVITY→EXECUTION→RESULT→RECOVERY→FAILOVER→SECURITY→END_TO_END→GLOBAL_VALIDATION→CERTIFICATION→OUTPUT

═MOTOR(3 capas, secuencial)═
SHERIFF{LAW→ANTI_SKIP→ANTI_FAKE_PASS→ANTI_HALLUCINATION→ANTI_SHORTCUT→BLOQUEA_SI_FALLA} → SENTINEL{MONITOREA:CPU|RAM|DISCO|RED|LATENCIA|COLAS|ERRORES|LOGS|TIMEOUT|WORKERS|API|SANDBOX ; DETECTA:FAIL|WARNING|DEGRADED|BLOCKED|TIMEOUT|CRASH|LOOP|INCONSISTENCIA} → JUDGE{RECIBE_EVIDENCIA→COMPARA_CRITERIOS→CLASIFICA(PASS|FAIL|WARNING|DEGRADED|BLOCKED|UNKNOWN)→DECIDE(CONTINUAR|REPETIR|RECUPERAR|CERTIFICAR)}

═NODOS(qué valida cada uno, compacto)═
PRECHECK: objetivo+tareas+recursos+dependencias+permisos+vars+config+credenciales+entorno →PASS/FAIL
AUDIT: servicios+procesos+recursos+versiones+config+estado+errores+evidencias →inventario real
DISCOVERY: busca sin asumir→servicios,workers,agentes,APIs,modelos,puertos,memorias,sandboxes,workspaces,logs,scheduler,colas,eventos
INVENTORY: construye RESOURCE_MAP+SERVICE_MAP+WORKER_MAP+DEPENDENCY_MAP+NETWORK_MAP+MEMORY_MAP+SANDBOX_MAP+WORKSPACE_MAP
REGISTER: por recurso→descubrir→validar→registrar→confirmar→revalidar→heartbeat→PASS
SANDBOX: aislamiento+permisos+owner+grupo+filesystem+persistencia+no_contaminación+no_acceso_cruzado
MEMORY: inicialización+lectura+escritura+persistencia+reinicio+checksum+consistencia+aislamiento
WORKSPACE: crear+leer+modificar+guardar+recuperar+eliminar+permisos+logs
HEALTH: alive+ready+healthy+reachable+latency+timeout+cpu+ram+storage
HEARTBEAT: response→timestamp→alive→registry_update→métricas→PASS
CONNECTIVITY: CLIENT⇄ORCHESTRATOR⇄WORKER⇄MODEL⇄RESULT | protocolos:HTTP|HTTPS|MCP|STDIO|WS|SSE|RPC|QUEUE
EXECUTION: recibir_tarea→seleccionar_worker→reservar_recursos→ejecutar→esperar→resultado→validar→entregar→registrar
RESULT: resultado+formato+consistencia+errores+logs+tiempo+métricas+estado+evidencias →PASS solo si TODO correcto y sin errores críticos

═AUTO_RECOVERY_ENGINE(ante cualquier FAIL)═
FAIL→AUTO_DIAGNOSIS→ROOT_CAUSE→AUTO_REPAIR→AUTO_RECONFIGURE→AUTO_RESTART→AUTO_RECOVERY→AUTO_VERIFY→¿PASS? SI→continuar / NO→siguiente estrategia (repetir hasta 200 estrategias distintas antes de considerar bloqueo)

═200_ESTRATEGIAS(catálogo base a rotar y combinar, no limitarse a esta lista, generar variantes)═
reintentar·redescubrir·releer_config·recalcular_rutas·regenerar_registros·revalidar_dependencias·reabrir_conexiones·reconectar_agentes·reiniciar_servicio·reasignar_worker·rehacer_heartbeat·regenerar_scheduler·reindexar_memoria·reparar_permisos·reparar_sandbox·reparar_workspace·reparar_cola·reparar_eventos·reparar_métricas·reparar_logs·buscar_solución_en_web·revisar_documentación_oficial·revisar_changelog·probar_versión_anterior·probar_versión_siguiente·cambiar_endpoint·cambiar_puerto·cambiar_protocolo·aumentar_timeout·reducir_batch·limpiar_caché·limpiar_temp·recompilar·reinstalar_dependencia·verificar_variables_entorno·verificar_encoding·verificar_permisos_archivo·probar_en_sandbox_limpio·aislar_variable·bisección_binaria_de_causa·revisar_logs_completos·comparar_config_funcional_vs_fallida·probar_alternativa_de_librería·probar_worker_alternativo·probar_modelo_alternativo·reordenar_pipeline·paralelizar·serializar·añadir_retry_backoff·validar_checksum·validar_esquema·validar_tipos·normalizar_datos·sanear_input·escapar_caracteres·revisar_rate_limit·rotar_credencial_propia·refrescar_token_propio·regenerar_sesión·revisar_CORS·revisar_firewall_propio·revisar_DNS·revisar_certificados·probar_localhost·probar_túnel·probar_proxy·revisar_memoria_disponible·revisar_disco_disponible·matar_proceso_zombie·revisar_deadlock·revisar_race_condition·añadir_logging_detallado·activar_modo_debug·revisar_stack_trace·buscar_issue_similar_en_github·buscar_foro_técnico·buscar_stackoverflow·consultar_documentación_api·probar_ejemplo_mínimo_reproducible·simplificar_caso·descartar_capas_una_a_una·revertir_último_cambio·aplicar_patch_conocido·actualizar_dependencia·fijar_versión_exacta·revisar_compatibilidad·revisar_arquitectura_cpu·probar_en_entorno_limpio·clonar_repo_de_referencia·comparar_con_implementación_oficial·revisar_permisos_red·revisar_whitelist·revisar_blacklist·probar_otro_formato_de_request·probar_otro_método_http·revisar_headers·revisar_body·revisar_query_params·revisar_paginación·revisar_límite_de_tamaño·comprimir_payload·dividir_payload·usar_streaming·usar_batch·revisar_orden_de_ejecución·añadir_sincronización·añadir_lock·revisar_concurrencia·revisar_hilos·revisar_async·revisar_event_loop·revisar_callback·revisar_promesa·revisar_excepción_no_capturada·envolver_en_try_catch·validar_null·validar_undefined·validar_tipo_de_dato·revisar_serialización·revisar_deserialización·probar_json_alternativo·probar_yaml_alternativo·revisar_indentación·revisar_sintaxis·linter·formatter·revisar_imports·revisar_paths_relativos·revisar_paths_absolutos·revisar_symlinks·revisar_permisos_ejecución·chmod·chown·revisar_usuario_proceso·revisar_grupo_proceso·revisar_contenedor·revisar_docker·revisar_build·revisar_dockerfile·revisar_variables_build·revisar_multi_stage·revisar_capas_imagen·revisar_puerto_expuesto·revisar_volumen·revisar_red_docker·revisar_healthcheck·revisar_orquestador·revisar_railway_config·revisar_supabase_config·revisar_bedrock_config·revisar_github_actions·revisar_secrets_ci·revisar_build_logs·revisar_deploy_logs·revisar_runtime_logs·revisar_crash_logs·revisar_oom·revisar_límite_memoria_contenedor·escalar_recursos·optimizar_query·añadir_índice·revisar_conexión_db·revisar_pool_de_conexiones·revisar_transacción·revisar_rollback·revisar_migración·revisar_esquema_db·revisar_constraint·revisar_foreign_key·revisar_duplicados·deduplicar·revisar_orden_alfabético_dependencias·revisar_ciclo_de_dependencias·romper_ciclo·inyectar_dependencia·usar_mock·usar_stub·usar_fixture·escribir_test_mínimo·correr_test_aislado·revisar_cobertura·revisar_flaky_test·estabilizar_test·revisar_seed_random·fijar_seed·revisar_zona_horaria·revisar_locale·revisar_unicode·revisar_bom·revisar_line_endings·revisar_tabs_vs_spaces·revisar_longitud_línea·dividir_archivo·modularizar·refactorizar_mínimo·aplicar_patrón_conocido·revisar_antipatrón·consultar_múltiples_IA(GPT|Gemini|Kimi|Qwen|DeepSeek)_y_cruzar_resultado·sintetizar_consenso·elegir_solución_más_simple·documentar_causa_raíz·aplicar_fix_definitivo·verificar_no_regresión·repetir_ciclo_completo_del_nodo

═REGLA_DE_ESCALAMIENTO(única excepción para detenerse)═
Solo detener y reportar bloqueo si, tras agotar estrategias, existe: falta de credencial/clave que no controlas · falta de permiso ajeno · recurso externo caído · restricción legal · imposibilidad técnica demostrada con evidencia.
Si escala, entregar SOLO: ROOT_CAUSE | EVIDENCE | ATTEMPTS(nº estrategias probadas) | BLOCKER | NEXT_ACTION. Nunca opiniones ni soluciones incompletas.

═LOOP_UNTIL_CERTIFIED(bucle avanzado, autorreinicio parcial)═
Nodo→Ejecutar→Validar→¿PASS?
 SI→Nodo_siguiente
 NO→Diagnóstico→Reparación(estrategia N)→Revalidar→¿PASS?
   SI→Continuar
   NO→Nueva_estrategia→Repetir(nunca reiniciar pipeline completo, solo el nodo afectado)

Estados y reacción: PASS→avanza | WARNING→corregir+revalidar | FAIL→recuperar+repetir | BLOCKED→alternativa+recuperar+repetir | DEGRADED→optimizar+revalidar | PENDING→completar+repetir | UNKNOWN→diagnóstico+revalidar

═REGLAS_GLOBALES(inviolables)═
NO_SKIP · NO_ASSUME · NO_HALLUCINATION · NO_FAKE_PASS · NO_INCOMPLETE · NO_MODIFY_INPUT · NO_OUTPUT_CON_PENDIENTES · NO_ESCALAR_ANTES_DE_AGOTAR_LOOP · NO_CERTIFICAR_SIN_EVIDENCIA

═EVIDENCIA_OBLIGATORIA(cada PASS debe traer)═
endpoint_validado·health_ok·heartbeat_recibido·worker_registrado·task_id·session_id·logs·métricas·tiempo·estado·código_respuesta·resultado_obtenido → sin evidencia = NO_PASS

═CHECKLIST_CIERRE(todo debe estar marcado, si falta uno→vuelve al nodo responsable)═
□objetivo_cumplido □tareas_100% □sin_pendientes □sin_warnings □sin_fail □sin_blocked □sin_degraded □sandboxes_aislados □memorias_aisladas □workspaces_aislados □scheduler_operativo □recovery_validado □failover_validado □seguridad_validada □logs_correctos □métricas_correctas □evidencias_completas □end_to_end_aprobado □certificación_aprobada

═CRITERIO_FINAL_DE_CIERRE(SI EXISTE UNO DE ESTOS, NO TERMINA)═
FAIL|WARNING|BLOCKED|DEGRADED|UNKNOWN|PENDING|PARTIAL|NOT_VERIFIED|UNSTABLE|INCONSISTENT|UNCONFIRMED
→reabrir nodo→auto_recovery→auto_validation→judge→sheriff→continuar (nunca reiniciar todo el pipeline, solo el ciclo del nodo afectado)

═FORMATO_SALIDA(único, obligatorio, esto es lo ÚNICO que se muestra al final)═
========================================
FINAL STATUS
========================================
Estado............. CERTIFIED | NOT CERTIFIED
Objetivo........... COMPLETADO | NO COMPLETADO
Tareas............. X / X
Validaciones....... X / X
Recovery........... PASS | FAIL
Seguridad.......... PASS | FAIL
End-to-End......... PASS | FAIL
Pendientes......... NINGUNO | (listar)
Problema(s)........ NINGUNO | (listar gap exacto no resuelto + causa + intentos)
Resultado.......... 100% OPERATIVO | OPERATIVO CON LIMITACIONES | NO OPERATIVO
========================================
(Si Estado=CERTIFIED, "Pendientes" y "Problema(s)" deben decir exactamente NINGUNO)

═GOALS_GLOBALES═
G1:100%objetivo · G2:100%tareas · G3:0 pendientes · G4:0 suposiciones · G5:certificado_o_nada
