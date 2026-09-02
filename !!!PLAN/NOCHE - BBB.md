# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-148`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimum productive recent-reauth seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-BBB-147 = NO_RESULT / SUPERSEDED / NOT_PASS; no RESULTADO DEL TURNO nor Issue #41 worker handoff verified after JOBS CYCLE152.`
- `DUPLICATE_CHECK: no current open PR discovered for the recent-reauth product seam; merged #53 remains the D8 authority/reuse lineage.`
- `SERIALIZATION: BBB148 owns only recent-reauth product seam. AAA149 owns runtime evidence. WOZ152 exclusively owns PR #98. Do not touch PR #98 six files, #89, #93, Trash UI/purge or Review.`

### PRIMARY

Expose/reuse the minimum productive D8 recent-reauth seam already decided, without redesigning auth/session and without implementing Empty Trash yet.

1. Fresh preflight live integration + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check.
2. Reuse literally D8: fresh same-provider authorization bound to the correct BeatGaler user/session; no password/MFA/new-provider invention.
3. If existing primitives already satisfy a bounded destructive-caller contract, STOP with exact reusable evidence rather than duplicating implementation.
4. If a real gap remains, expose the smallest productive boundary granting/verifying `recently reauthenticated` for a destructive caller.
5. Fail closed for wrong user, wrong session, expired/not-fresh authorization, replay where applicable, and provider failure.
6. Add focused success/wrong-user/wrong-session/expired/failure tests and preserve D6/D7 + Web/Desktop contracts.
7. One candidate/PR only if duplicate-check stays clean; exact-head applicable CI. **NO MERGE CYCLE153.**
8. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; F2/15.1 remains open.
9. Do not touch any PR #98 file (`cloud-server/productive-temp-auth-boundary.js`, `src/App.tsx`, `src/features/cloud/webTransport.worker.ts`, `src/platform/contracts.ts`, `src/platform/desktopAdapter.ts`, `src/platform/webAdapter.ts`), #89/#93, Trash implementation, Review or runtime deployment evidence.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** reused D8 primitive/decision; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; explicit `UNVERIFIED`; duplicate-check and no overlap with AAA149/WOZ152.  
**STOP:** architectural redesign, provider mutation, PR #98 overlap, Trash implementation, Review, #89/#93 mutation, integration mutation, duplicate candidate or unsafe whole-file rewrite.

### CI-FALLBACK

**F3 / 18.2 alpha-applicability evidence inventory — READ-ONLY, only while PRIMARY genuinely waits on external CI/build/review after a clean candidate exists.**

- **Scope:** inventory existing provider/payment reconciliation evidence and unresolved real-provider scenarios; classify only `SOFTWARE_PROVEN`, `UNVERIFIED_EXTERNAL`, or `NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`. No exclusion decision and no billing/provider mutation.
- **Evidence required:** exact existing PR/merge/runtime refs; unresolved 3DS/rejection/late payment/renewal failure/cancel/plan-change/refund/webhook/reconciliation list; explicit statement that F1/1.7→1.8 decides applicability.
- **STOP:** any mutation, provider state change/payment execution, new PR, gate promotion, overlap with AAA149/WOZ152, or PRIMARY leaves external wait. Return to PRIMARY immediately and recheck it before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-147`: no matching final result/handoff verified by JOBS CYCLE153 preflight → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
