# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-123`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimum productive recent-reauth seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-BBB-122 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff verified before CYCLE128.`
- `SERIALIZATION: BBB123 owns only recent-reauth product seam. AAA124 owns F1/1.7 READ-ONLY classification. WOZ127 owns #89. No Trash UI/purge, Review, #93 mutation or integration mutation.`

### PRIMARY

**Expose/reuse the minimum productive D8 recent-reauth seam already decided, without redesigning auth/session and without implementing Empty Trash yet.**

1. Fresh preflight live integration + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check.
2. Reuse literally D8: fresh same-provider authorization bound to correct user/session; do not invent password/MFA or new provider.
3. Verify current auth/session primitives do not already satisfy the bounded recent-reauth caller contract.
4. Find the smallest productive boundary capable of granting/verifying `recently reauthenticated` for a destructive caller.
5. Expose only that bounded caller contract; do not touch SettingsPanel Trash UI/purge behavior.
6. Fail closed for wrong user/session, expired/not-fresh authorization and provider failure.
7. Add focused success/wrong-user/wrong-session/expired/failure tests and preserve D6/D7 + Web/Desktop contracts.
8. One candidate/PR only if duplicate-check is clean; exact-head applicable CI; **NO MERGE CYCLE128**.
9. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; F2/15.1 remains open.

**Required evidence:** reused D8 primitive/decision; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; explicit `UNVERIFIED`.  
**STOP:** architectural redesign, provider mutation, Trash implementation, Review, F2/12.1 runtime, #89/#93 mutation, integration mutation, duplicate candidate, or unsafe whole-file rewrite.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-122`: no matching final result/handoff verified by JOBS CYCLE128 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
