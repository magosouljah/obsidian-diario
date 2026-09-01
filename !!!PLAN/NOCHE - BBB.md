# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-114`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimal recent-reauth product seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-BBB-113 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff was verified before CYCLE119.`
- `SERIALIZATION: BBB114 owns only recent-reauth product seam. AAA115 owns F1/1.7 READ-ONLY classification. WOZ118 owns #89. No Trash UI/purge, Review, #93 or integration mutation.`

### PRIMARY

**Expose/reuse the minimum productive D8 recent-reauth seam already decided, without redesigning auth/session and without implementing Empty Trash yet.**

1. Fresh preflight live integration + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check.
2. Reuse literally the D8 decision: fresh same-provider authorization bound to the correct user/session. Do not invent password/MFA or a new provider.
3. Verify #92/#94/#95 do not already create an equivalent recent-reauth primitive.
4. Find the smallest productive auth/session boundary capable of granting/verifying `recently reauthenticated` for a destructive caller.
5. If an internal primitive is sufficient, expose only the bounded caller contract; do not touch SettingsPanel Trash UI/purge behavior.
6. Fail closed for wrong user/session, expired/not-fresh authorization and provider failure.
7. Add focused success/wrong-user/wrong-session/expired/failure tests and preserve D6/D7 + Web/Desktop contracts.
8. One candidate/PR only if duplicate-check is clean; exact-head applicable CI; **NO MERGE CYCLE119**.
9. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; F2/15.1 remains open.

**Required evidence:** reused D8 primitive/decision; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; explicit `UNVERIFIED`.  
**STOP:** architectural redesign, provider mutation, Trash implementation, Review, F2/12.1 runtime, #89/#93, integration mutation, duplicate candidate, or unsafe whole-file rewrite.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-113`: no matching result/handoff verified by JOBS CYCLE119 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
