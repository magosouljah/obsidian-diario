# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-043`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — SAME PR #75 supply-chain pin corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `REUSE_PR: #75 / woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`
- `PREDECESSOR: NIGHT-WOZ-042 had no worker result and no GitHub mutation; superseded by JOBS CYCLE 044 so it cannot execute late.`
- `HOLD_PR: #73 / woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb — DO NOT TOUCH`

### PRIMARY

1. Preflight live integration + SAME #75 exact head/base + duplicate-check; no replacement PR and no #73 mutation.
2. Reuse the attributed failure already established: Required CI `33323457041` failed only because the new F3 20.1 workflow used floating `actions/checkout@v4` and `actions/setup-node@v4` and the supply-chain gate requires immutable refs.
3. Correct only `.github/workflows/f3-20.1-observability.yml`: use canonical immutable pins already used by Required CI: `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` and `actions/setup-node@820762786026740c76f36085b0efc47a31fe5020`.
4. Preserve workflow/product/observability semantics. Do not broaden 20.1, wire production call-sites, touch provider resources, #73, F2/F4, auth, matrix, infrastructure, 20.2 or external tails.
5. Run focused observability contract if applicable and obtain fresh exact-head Required CI + dedicated F3 20.1 workflow. Both must be green.
6. If all applicable gates are green, race-check integration. If baseline moved, refresh/reconcile and revalidate before merge; if race-clean and merge flow is available, integrate SAME #75 and verify merge SHA/post-merge integration HEAD.
7. If merge flow remains unavailable, report READY_FOR_INTEGRATION/BLOCKED with exact evidence and STOP; do not hop to #73.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; two-pin diff only; focused test; fresh exact-head Required CI + F3 20.1 workflow; merge SHA only if actually integrated.  
**STOP:** any non-pinning failure, semantic/product scope drift, baseline race requiring broad conflict work, merge-flow unavailable, provider/RO dependency or need to touch #73.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO / SUPERSEDED — NIGHT-WOZ-042

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- Live #75 recheck in CYCLE 044: OPEN/Ready/mergeable, base `a9d35a3d...`, head still `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`.
- No new commit, no new CI, no handoff and no integration attributable to 042.
- Same minimal corrective remains globally useful, so it is reissued under unique current ID `NIGHT-WOZ-043`; 042 must not execute later.

## RESULTADO PROCESADO — NIGHT-WOZ-041

- `STATUS: PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- PR #75 candidate adds software-only structured redacted events, bounded counters, explicit condition→route mapping without delivery claims, fail-closed kill switches, focused tests and internal runbook.
- Required CI `33323457041` FAILURE only at immutable external GitHub Action validation.
- Product call-site wiring, tracing/durable backend, retention, provider alert resources/delivery, on-call/escalation and public status remain open/external.

## HOLDING

- F3/18.2 #73 exact-head green / merge-flow blocked; untouched.
- F2/#70 stale/frozen; outside scope.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-043`: ASSIGNED — SAME #75 immutable-action pin corrective + fresh exact-head CI.
- `NIGHT-WOZ-042`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-041`: WAITING_CI -> Required CI FAILURE attributable to floating action refs.
- `NIGHT-WOZ-040`: BLOCKED/MERGE_FLOW_UNAVAILABLE — #73 green/race-clean, not merged.
- `NIGHT-WOZ-037`: DONE/INTEGRATED — #68 merge `a9d35a3d...`.
- `NIGHT-WOZ-033`: DONE/AUDIT_ONLY — 20.1 gap map.
