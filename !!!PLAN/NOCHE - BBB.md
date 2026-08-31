# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-093`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 packaged Windows auth first-causal-side diagnostic`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; base exact live integration.`
- `AUTHORITATIVE_FAILURE: exact #84 F4 - 25.1 Windows Auth Journey run 33423712589 = FAILURE; broad Desktop Portability and related current-head gates remain green.`
- `PREDECESSOR: NIGHT-BBB-092 produced no final result, matching Issue #41 handoff, head movement or fresh literal run before JOBS CYCLE 098 preflight; SUPERSEDED / NOT_PASS.`
- `WHY_ASSIGNED: fresh global recalculation still places exact packaged Windows auth as blocker #1. Evidence-before-claim permits only the minimum diagnostic pass until product-vs-mock/service causality is resolved.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA094 owns F2/13.2 Review. WOZ097 owns F3/18.2 evidence mapping READ-ONLY. Trash recent-reauth implementation remains unowned because it overlaps the auth/session boundary.`

### PRIMARY

**F4 / 25.1 — instrument only the first post-submit causal boundary on exact #84 lineage; preserve product behavior and literal assertions.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact failed run; STOP if lineage/head/base materially moved or another owner/candidate now owns this exact slice.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence lineage. Do not create a third auth PR.
3. Do **not** change product auth/session behavior in this assignment.
4. Add only the smallest redacted diagnostic instrumentation needed to establish, in order:
   - whether mocked `/auth/login` is reached and a successful response is returned;
   - whether `set_cloud_auth_token` is invoked and whether that boundary succeeds/fails, without logging token/secret values;
   - whether AccountGate receives the successful auth response;
   - whether the product session write is attempted/completed;
   - whether gate transition occurs, or WDIO/Tauri DirectEval/session capability fails first.
5. Keep existing literal assertions unchanged: expected session token persistence and AccountGate exit.
6. Run one fresh exact-head packaged Windows auth journey and capture exact run/job plus the ordered causal observations.
7. Fresh applicable exact-head CI is required for any changed #84 head. **NO PRODUCT CORRECTIVE. NO MERGE.**
8. Maximum claim: `F4/25.1 FIRST_CAUSAL_SIDE_RESOLVED`. Claim PASS only if unchanged literal assertions actually pass.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP. A later JOBS cycle decides any corrective scope/owner.

**Required evidence:** exact integration/#74/#84 SHAs; changed diagnostic files/functions; proof no secret/token values are emitted; exact fresh Windows run/job; ordered submit-boundary observations; unchanged assertion result; exact-head CI; explicit product-vs-harness/service attribution or `UNRESOLVED`.  
**STOP:** product behavior change required, auth/security redesign, backend/provider change, unrelated product files, integration mutation, #72/AAA Review overlap, diagnostic output risks sensitive values, or one bounded instrumented run still cannot attribute the causal side.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** other F4 work either needs signing/hardware/tester evidence or shares release/auth ownership. Trash recent-reauth materially overlaps this auth/session investigation.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-092`: `NO_RESULT / SUPERSEDED / NOT_PASS` at JOBS CYCLE 098 preflight; no matching handoff/head movement/fresh run.
- Late `NIGHT-BBB-088` / Issue #41 `5483886991`: reusable factual boundary only; product vs mocked Tauri/WDIO service remains unresolved.
- Exact #84 Windows Auth remains RED on `c6c5ecb...`; run `33423712589` = FAILURE.
