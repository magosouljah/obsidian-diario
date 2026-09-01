# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-140`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimum productive recent-reauth seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-BBB-139 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching worker handoff exists after JOBS CYCLE144.`
- `SERIALIZATION: BBB140 owns only the recent-reauth product seam. AAA141 owns F2/12.1 evidence. WOZ144 owns #89. No Trash UI/purge, Review, #93 mutation or integration mutation.`

### PRIMARY

**Expose/reuse the minimum productive D8 recent-reauth seam already decided, without redesigning auth/session and without implementing Empty Trash yet.**

1. Fresh preflight live integration + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check across live/open branches and PRs.
2. Reuse literally D8: fresh same-provider authorization bound to the correct user/session; do not invent password/MFA or a new provider.
3. Verify whether current primitives already satisfy a bounded recent-reauth caller contract. If yes, STOP with exact reusable evidence instead of duplicating implementation.
4. If a real gap remains, expose the smallest productive boundary capable of granting/verifying `recently reauthenticated` for a destructive caller.
5. Fail closed for wrong user/session, expired/not-fresh authorization and provider failure.
6. Add focused success/wrong-user/wrong-session/expired/failure tests and preserve D6/D7 + Web/Desktop contracts.
7. One candidate/PR only if duplicate-check is clean; exact-head applicable CI; **NO MERGE CYCLE145**.
8. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; F2/15.1 remains open.
9. Do not touch SettingsPanel Trash UI/purge behavior, Review, F2/12.1, #89 or #93.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** reused D8 primitive/decision; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; explicit `UNVERIFIED`; proof of no overlap with AAA141/WOZ144/#93.  
**STOP:** architectural redesign, provider mutation, Trash implementation, Review, F2/12.1, #89/#93 mutation, integration mutation, duplicate candidate or unsafe whole-file rewrite.

### CI-FALLBACK

**F3 / 18.2 alpha-applicability evidence inventory — READ-ONLY, only while PRIMARY is genuinely waiting on external CI/build/review after a clean candidate exists.**

- **Scope:** inventory existing provider/payment evidence and unresolved real-provider scenarios; classify each item only as `SOFTWARE_PROVEN`, `UNVERIFIED_EXTERNAL`, or `NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`. Do not make the RO exclusion decision and do not edit billing/provider code or infrastructure.
- **Evidence required:** exact existing PR/merge/runtime references; list of unverified 3DS/rejection/late payment/renewal failure/cancel/plan-change/refund/webhook/reconciliation scenarios; explicit statement that exclusion from alpha still requires JOBS/RO classification in 1.7/1.8.
- **STOP:** any mutation, provider call that changes state, payment execution, new PR, gate promotion, overlap with AAA141/WOZ144, or PRIMARY leaves external wait. Return to PRIMARY immediately.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-139`: no matching RESULTADO DEL TURNO or Issue #41 handoff verified by JOBS CYCLE145 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
