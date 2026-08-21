# DOCUMENTO 6 — BLOQUE 15-A: ORGANIZACIÓN SAAS
# GITHUB vs STORAGE — SEPARACIÓN COMPLETA
# VERSION FINAL

## REGLA FUNDAMENTAL

GitHub = cerebro (definición, contratos, reglas, DAG, auditoría)
Storage = músculos (código ejecutable de negocio)
MAXBRY nunca guarda músculos en el cerebro.

✅ planner_offline.py → utilidad control plane (GitHub OK)
✅ validators.py → utilidad control plane (GitHub OK)
❌ artifact_code.py → va a Storage SIEMPRE

## SEPARACIÓN ESTRICTA — 4 NIVELES

NIVEL 1 — CONTENIDO: artifact_code.py → SOLO Python → B01_artifact_code/
NIVEL 2 — COMPORTAMIENTO: artifact_spec.md → SOLO ejemplos → A07_artifact_specs/
NIVEL 3 — UBICACIÓN: artifact_manifest.json → GPS → A13_artifact_manifests/
NIVEL 4 — CONTRATO: artifact_contract.json → definición → A06_artifact_contracts/

❌ Nunca mezclar código + ubicación
❌ Nunca mezclar ejecución + sistema
❌ Nunca guardar rutas dentro del código
❌ Nunca mezclar instrucciones en código

## LISTA MAESTRA

### A. CONTROL PLANE (GitHub — Repo Brain)
A01 system_manifest.json | A02 project_manifest.json | A03 Constitution
A04 Requirements | A05 Orquestador | A06 Artifact Contracts
A07 Artifact Specs | A08 Schemas | A09 Validators | A10 Ledger
A11 Documentation | A12 Tests Control Plane | A13 Artifact Manifests
A14 Planner Offline | A15 Sequence.json | A16 Fallback.json
A17 State.json | A18 Router/Dispatcher | A19 DAG Engine
A20 Loader | A21 Verifier | A22 Executor | A23 Space Client
A24 Logger | A25 Tracer | A26 Recovery Core (5 tiers)
A27 Registros (5) | A28 Instructions 1-5

### B. EXECUTION PLANE (Object Storage)
B01 Artifact Code | B02 Artifact Internal | B03 Artifact Tests
B04 Artifact Versions | B05 Artifact Packages | B06 Execution Logs
B07 Traces | B08 Runtime Outputs | B09 Checkpoints | B10 Cache

### C. RUNTIME (Brain + Spaces)
C01 Loader | C02 Verifier | C03 Executor | C04 Recovery | C05 Context Builder

### D. FUTURO (No MVP)
D01 G3 | D02 JSON Capa 2 | D03 UI Windows | D04 Sigstore/Cosign v2

## FLUJO SAAS (8 PASOS)

1. Diseñar contrato → artifact_contract.json
2. Diseñar spec → artifact_spec.md
3. Commit GitHub → Control Plane
4. IA genera código → artifact_code.py
5. Código va a Storage → B01_artifact_code/
6. Verifier valida N0-N5
7. COMMITTED
8. MAXBRY ejecuta

## CÓMO TRABAJA LA IA CONSTRUCTORA

Recibe: artifact_contract.json + artifact_spec.md
Genera: [nombre].py + [nombre].meta.md + artifact_location_plan.json
No toca: ❌ DAG ❌ Router ❌ Planner ❌ Runtime ❌ Brain ❌ Orquestador
Restricción: 90% código / 10% LLM máximo
