# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 / 20.1 — observability software integration.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-069`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — SAME #75 exact-head merge transaction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`
- `PRIMARY_PR: #75 @ 40e39393247dbdd506ac01edefa84fd0b0add94c`
- `PREDECESSOR: NIGHT-WOZ-068 had no final RESULTADO DEL TURNO, Issue #41 handoff or accepted merge before JOBS CYCLE 070; SUPERSEDED and MUST NOT execute late.`
- `RECALCULATION: selected from zero because GitHub still shows #75 OPEN/non-draft/mergeable, base_sha exactly equal to live integration, unchanged four-file scope and applicable exact-head CI green. This remains the shortest factual integration step.`
- `SERIALIZATION: WOZ/#75 owns the only integration mutation authorized in CYCLE 070.`

### PRIMARY

1. Fresh race-check live integration immediately before acting. If HEAD moved from `63c9f8c9...`, STOP unless a history-preserving SAME-#75 refresh + full exact-head revalidation can safely remain within scope.
2. Verify #75 remains OPEN/non-draft/mergeable at exact head `40e39393247dbdd506ac01edefa84fd0b0add94c` and base SHA equals live integration.
3. Confirm changed paths remain exactly: `.github/workflows/f3-20.1-observability.yml`, `cloud-server/OPERATIONS-OBSERVABILITY.md`, `cloud-server/operations-observability.js`, `cloud-server/tests/operations-observability.test.cjs`.
4. Confirm applicable exact-head workflows remain complete/green before merge. JOBS CYCLE 070 verified Required CI success on exact head; no stale CI may authorize a changed head/base.
5. Execute only the authorized exact-head merge transaction using expected head SHA. Do not alter code to work around tooling/safety behavior.
6. If GitHub accepts merge, verify resulting integration SHA and parents before claiming integration.
7. Maximum claim: F3/20.1 **software observability slice integrated**. External metrics/tracing/error backend, alert delivery, retention, on-call, public status and production observability runtime remain UNVERIFIED.
8. Do not touch BBB065 capacity work, #79/#76/#72/#74/#71/#69/#70 or provider/infra resources.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** pre-merge integration SHA; exact #75 head/base; exact four-file delta; exact-head CI; merge SHA + parents if accepted; exact blocker otherwise.  
**STOP:** baseline/head changes unsafely, scope drift, mergeability changes, applicable CI red/pending, integration race, or merge flow blocked before GitHub acceptance.

### CI-FALLBACK

**F3 / 18.2 READ-ONLY provider/payment scenario gap map**, only if PRIMARY is genuinely blocked waiting on merge acceptance/review/queue or an equivalent external operation.

**Alcance:** live integration only; audit literal existing coverage for 3DS, rejection, late payment, renewal, cancel, upgrade, downgrade, refund and grace-period behavior. No writes, branch, PR, provider calls, billing mutations, secrets or #75 files.  
**Evidencia requerida:** exact baseline + scenario matrix `SOFTWARE_COVERED / PARTIAL / GAP / PENDING_EXTERNAL` with paths/tests/contracts and the smallest dependency-safe future slices.  
**STOP:** any product/provider mutation, attempt to fabricate payment evidence, overlap with BBB capacity/AAA media work, dependency on stale unmerged candidates, or attempt to close global 18.2 from audit alone. Recheck PRIMARY before closing.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-068`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 070.
- `NIGHT-WOZ-067`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 069.
- `NIGHT-WOZ-060`: `BLOCKED / MERGE_FLOW_UNAVAILABLE`; no GitHub merge accepted.
- `NIGHT-WOZ-056`: `DONE / INTEGRATED` — PR #78 merge `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; max claim `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
