# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-010`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — repair SAME PR #60, refresh to live baseline, exact-head CI, integrate only if green`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`
- `REUSE_PR: #60 / bbb/task-25.1-functional-matrix`
- `KNOWN_CANDIDATE_HEAD: 28d9e3819e528ae5ed23435ad39d20ef6c14641b`
- `JOBS_PRECHECK: F4 - 25.1 Functional Matrix 33260592877 SUCCESS, D6 33260592860 SUCCESS y D7 33260592764 SUCCESS sobre 28d9e381..., pero Test - Desktop Portability 33260592774 = FAILURE. Además #59 movió integration de f73c9ee... a be9e58c..., así que #60 está stale y NO es integration-ready.`

### Orden JOBS

1. Preflight factual: Plan Maestro + F4 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: continúa exclusivamente la MISMA PR #60. No abras PR/rama 25.1 duplicados.
3. Inspecciona la causa concreta del failure exact-head `Test - Desktop Portability` run `33260592774`. No asumas que el matrix gate verde compensa ese failure.
4. Refresca #60 contra `integration-v0.8.0-alpha.1 @ be9e58c9...`, preservando #59. Corrige solo el delta mínimo atribuible a F4/25.1 si existe.
5. Si el failure revela un bug de producto F2/F3 fuera de scope, clasifícalo `PRODUCT_FINDING` con evidencia y no robes ownership.
6. Tras cualquier refresh/fix exige CI aplicable al nuevo exact head: Desktop Portability/Required CI, F4 25.1 matrix y checks D6/D7 aplicables.
7. Solo si todos los gates aplicables quedan SUCCESS, revalida integration HEAD/head/base/mergeability y ejecuta race-check + merge protegido con expected-head. Verifica merge SHA.
8. Integrar #60 no convierte automáticamente todos los journeys de 25.1 en PASS: conserva `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` donde la matriz lo diga.
9. No iniciar 25.2 en este turno salvo nueva orden JOBS. No signing/notarization/release/stable/latest.
10. Actualiza solo este markdown + Issue #41 con resultado de `NIGHT-BBB-010` y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-009`  
`TURN_STATUS: PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`  
`HEAD_AFTER: bbb/task-25.1-functional-matrix @ 28d9e3819e528ae5ed23435ad39d20ef6c14641b`  
`PR: #60 OPEN / Ready.`  
`CHANGES: matrix JSON + contract runner + workflow; 40 nominal cells; no F2/F3 logic.`  
`POST-TURN JOBS EVIDENCE: matrix workflow 33260592877 SUCCESS; D6 33260592860 SUCCESS; D7 33260592764 SUCCESS; Desktop Portability 33260592774 FAILURE. Integration subsequently advanced to be9e58c... via #59.`  
`BLOCKER_PROCESSED_BY_JOBS: exact-head portability failure + stale base; gate remains intact.`

## HISTORIAL

- `NIGHT-BBB-010`: ASSIGNED — SAME #60 failure diagnosis/refresh/fix/CI.
- `NIGHT-BBB-009`: PENDING — #60 candidate; post-turn portability failure discovered by JOBS.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`; 24.2 closed.
- `NIGHT-BBB-007`: PENDING; luego CI verde.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — PR #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
