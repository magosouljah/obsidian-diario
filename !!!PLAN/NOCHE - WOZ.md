# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — billing/entitlements software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-035`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 18.1 — reactivate SAME PR #68 on live baseline`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `REUSE_PR: #68 / woz/night-18.1-entitlements-reservation @ 2a988ec2a25d6ecfa927614fcc32cde689995103`
- `PREDECESSOR: NIGHT-WOZ-034 NOT_PROCESSED / SUPERSEDED_BY_JOBS — no RESULTADO DEL TURNO/handoff final new observed; 20.1 returns to holding.`
- `HOLDING_ITEM: F3/20.1 gap map remains valid; no active owner this cycle.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reuse SAME #68; no replacement branch/PR.
2. Recalculate from live baseline `02a40564...`. #68 was built/tested on `3ad8f55a...`; old green CI is historical only.
3. Refresh/reconcile #68 onto live integration preserving only its authorized 18.1 delta: server-side subscription-state authority, quota enforcement before reservation, PostgreSQL advisory-lock transaction for race-safe reservation and Billing Portal contract that never grants entitlement from redirect/session.
4. REUSE-FIRST: preserve existing #68 implementation and tests; do not rewrite billing architecture or start 18.2.
5. After refresh, run focused 18.1 tests plus fresh applicable exact-head D6/D7/Required CI/Desktop Portability and any dedicated 18.1 workflow. Evidence must correspond to the refreshed exact head.
6. Race-check integration again before merge. Merge SAME #68 only if head/base/scope are exact and all applicable gates are green through the authorized owner flow.
7. If the prior merge-execution/tooling blocker recurs after the candidate is fully green, record `PENDING_PROCESS_BLOCKER` with exact error and STOP; do not create a duplicate PR or force/bypass.
8. No Stripe productive credentials/resources, 18.2, grace-period decisions, F2/F4, #70, 20.1 implementation, provider infra, costs or secrets.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Evidence required:** live baseline, refreshed exact head, changed-file scope, focused tests, fresh applicable exact-head CI, race-check, merge SHA + post-merge integration HEAD if integration succeeds.  
**STOP:** destructive/unsafe refresh, unrelated delta, stale CI, merge/process blocker, provider/external expansion, scope creep or non-attributable CI failure.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback. 20.1 would be separate ownership/scope and 18.2 depends materially on 18.1.

## RESULTADO PROCESADO — NIGHT-WOZ-034

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No final result/handoff was observable before CYCLE 036.
- Recalculated path moved WOZ back to earlier F3 gate 18.1/#68.

## RESULTADO PROCESADO — NIGHT-WOZ-033

- `STATUS: DONE / AUDIT_ONLY — 20.1 remains OPEN`.
- Baseline `02a40564...`; no branch/PR/code.
- Gap map: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing matrix GAP except backup partial contract; on-call/status external; runbook partial; kill switches GAP.
- Handoff Issue #41 `5468767913`.

## HOLDING

- F3/20.1 gap map above — valid, unassigned this cycle.
- F2/13.1/#70 @ `5a99ebf2...` — stale/frozen; safe-write tooling blocker; not WOZ scope this cycle.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-035`: ASSIGNED — SAME #68 refresh/revalidate/integrate if green.
- `NIGHT-WOZ-034`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-033`: DONE / AUDIT_ONLY — 20.1 gap map.
- `NIGHT-WOZ-031`: BLOCKED / SAFE_WRITE_TOOLING_LIMIT; #70 restored exactly.
- `NIGHT-WOZ-025`: #68 exact-head green historically but merge execution blocked.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
