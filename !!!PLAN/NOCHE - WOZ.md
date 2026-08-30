# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-042`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — SAME PR #75 supply-chain pin corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `REUSE_PR: #75 / woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`
- `PREDECESSOR: NIGHT-WOZ-041 PENDING/WAITING_CI; JOBS recheck resolved Required CI to FAILURE attributable to workflow pinning.`
- `HOLD_PR: #73 / woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb — DO NOT TOUCH`

### PRIMARY

1. Preflight live integration + SAME #75 exact head/base + duplicate-check; no replacement PR and no #73 mutation.
2. Consume exact failure from Required CI run `33323457041`: Supply chain gate failed only at `Verify every external GitHub Action is immutable`.
3. Correct only `.github/workflows/f3-20.1-observability.yml`: replace floating `actions/checkout@v4` and `actions/setup-node@v4` with the exact immutable SHAs already used by canonical Required CI: `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` and `actions/setup-node@820762786026740c76f36085b0efc47a31fe5020`. Preserve workflow semantics and product code unchanged.
4. Do not broaden observability scope, wire new production call-sites, touch provider resources, #73, F2/F4, auth, matrix, infra, 20.2 or external tails.
5. Run focused observability contract if available and obtain fresh exact-head applicable CI. Required CI must become green and the dedicated F3 20.1 workflow must pass.
6. If all applicable gates are green and integration authority/flow for #75 is available, race-check and integrate SAME #75; verify merge SHA + post-merge integration HEAD. If merge flow is unavailable, report READY_FOR_INTEGRATION/BLOCKED with exact evidence and STOP.
7. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; two-action pin diff only; focused test; fresh exact-head Required CI + F3 20.1 workflow; merge SHA only if actually integrated.  
**STOP:** any non-pinning failure, semantic/product scope drift, baseline race, merge-flow unavailable, provider/RO dependency or need to touch #73.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-041

- `STATUS: PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- PR #75 OPEN/Ready/mergeable @ `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`, base `a9d35a3d...`; 4 files, +156/-0.
- Candidate software-only: structured redacted events, bounded internal counters, explicit condition→route mapping without delivery claims, fail-closed kill switches, focused tests y runbook interno.
- Required CI / Test - Desktop Portability run `33323457041` = FAILURE.
- Root cause literal: `Supply chain gate` falla en `Verify every external GitHub Action is immutable`.
- Patch del workflow confirma `actions/checkout@v4` y `actions/setup-node@v4`; canonical Required CI ya usa pins inmutables `3d3c42e...` y `820762786...`.
- PostgreSQL live/recovery y otros jobs observados no convierten el Required CI global en PASS.
- No integración; 20.1 global sigue abierto.
- PENDING_EXTERNAL/UNVERIFIED continúa: product call-site wiring, tracing/backend durable de errores/métricas, retention, provider alert resources/delivery, on-call/escalation y public status.

## RESULTADO PROCESADO — NIGHT-WOZ-040

- `STATUS: BLOCKED / MERGE_FLOW_UNAVAILABLE`.
- #73 OPEN/Ready/mergeable, base `a9d35a3d...`, exact head `fc831172c4c86d97cadb03801a6777777fd345bb`.
- Exact-head CI verde y race-check limpio; integration siguió `a9d35a3d...`.
- Merge intent bloqueado por execution layer antes de aceptación por GitHub; no merge SHA.
- #73 queda holding intacto hasta un flujo capaz de ejecutar merge.

## HOLDING

- F3/18.2 #73 exact-head green / merge-flow blocked.
- F2/#70 stale/frozen; fuera de scope.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-042`: ASSIGNED — SAME #75 immutable-action pins + fresh CI.
- `NIGHT-WOZ-041`: PENDING/WAITING_CI; final recheck = Required CI FAILURE atribuible a floating action refs.
- `NIGHT-WOZ-040`: BLOCKED/MERGE_FLOW_UNAVAILABLE — #73 green/race-clean, not merged.
- `NIGHT-WOZ-039`: PENDING/WAITING_CI -> READY_FOR_INTEGRATION by JOBS recheck.
- `NIGHT-WOZ-037`: DONE/INTEGRATED — #68 merge `a9d35a3d...`.
- `NIGHT-WOZ-033`: DONE/AUDIT_ONLY — 20.1 gap map.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
