# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-138`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimum productive recent-reauth seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-BBB-137 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff verified before CYCLE143.`
- `SERIALIZATION: BBB138 owns only recent-reauth product seam. AAA139 owns F2/12.1 runtime evidence READ-ONLY. WOZ142 owns #89. No Trash UI/purge, Review, #93 mutation or integration mutation.`

### PRIMARY

**Expose/reuse the minimum productive D8 recent-reauth seam already decided, without redesigning auth/session and without implementing Empty Trash yet.**

1. Fresh preflight live integration + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check, including branches/PRs created after CYCLE142.
2. Reuse literally D8: fresh same-provider authorization bound to the correct user/session; do not invent password/MFA or a new provider.
3. Verify whether current auth/session primitives already satisfy a bounded recent-reauth caller contract. If yes, STOP with exact reusable evidence instead of duplicating implementation.
4. If a real gap remains, expose the smallest productive boundary capable of granting/verifying `recently reauthenticated` for a destructive caller.
5. Fail closed for wrong user/session, expired/not-fresh authorization and provider failure.
6. Add focused success/wrong-user/wrong-session/expired/failure tests and preserve D6/D7 + Web/Desktop contracts.
7. One candidate/PR only if duplicate-check is clean; exact-head applicable CI; **NO MERGE CYCLE143**.
8. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; F2/15.1 remains open.
9. Do not touch SettingsPanel Trash UI/purge behavior, Review, F2/12.1, #89 or #93.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff only, then STOP.

**Required evidence:** reused D8 primitive/decision; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; explicit `UNVERIFIED`; proof of no overlap with AAA139/WOZ142/#93.  
**STOP:** architectural redesign, provider mutation, Trash implementation, Review, F2/12.1, #89/#93 mutation, integration mutation, duplicate candidate, or unsafe whole-file rewrite.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-137`: no matching final result/handoff verified by JOBS CYCLE143 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
