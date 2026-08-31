# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-092`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 packaged Windows auth minimum diagnostic instrumentation at first post-submit boundary`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; base exact live integration.`
- `AUTHORITATIVE_FAILURE: exact #84 Windows Auth Journey run 33423712589 / job 99592060690 = FAILURE at tests/e2e/auth-flow.e2e.mjs:64; token never observable in localStorage.`
- `LATE_EVIDENCE_CONSUMED: NIGHT-BBB-088 / Issue #41 5483886991 = BLOCKED_STOP / FIRST_CAUSAL_BOUNDARY_ATTRIBUTED. It proves causal ambiguity between product auth/session, mocked Tauri command path, and WDIO/Tauri service capability; speculative corrective is forbidden.`
- `PREDECESSOR: NIGHT-BBB-091 has no final RESULTADO DEL TURNO or matching material handoff at JOBS CYCLE 097 preflight; superseded / NOT_PASS.`
- `WHY_ASSIGNED: live failure remains critical, but reuse-first now requires one diagnostic-only pass before any product or harness corrective.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA093 owns F2/13.2. WOZ096 owns F3/19.1 READ-ONLY. Trash recent-reauth implementation remains unowned to avoid auth/session overlap.`

### PRIMARY

**F4 / 25.1 — instrument the exact current #84 submit boundary only, preserve assertions, and run one fresh literal packaged Windows auth journey.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact failed run/job; STOP on duplicate ownership or material lineage movement.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence candidate. Do not fork another PR.
3. Do **not** change product auth/session behavior in this assignment. The late BBB088 handoff proves the current evidence cannot justify which side is wrong.
4. Add only the smallest diagnostic instrumentation needed to answer, in order:
   - was mocked `/auth/login` reached and what response was returned;
   - was `set_cloud_auth_token` invoked and with what success/failure boundary, without printing secret/token values;
   - did AccountGate receive the successful auth response;
   - was the product-side session write attempted/completed;
   - did the gate transition occur or did WDIO/Tauri DirectEval/session capability fail first.
5. Preserve existing literal assertions unchanged: `beatgaler:account-session:v1 = e2e-session-token` and AccountGate exit.
6. Run one fresh exact-head packaged Windows auth journey on the instrumented #84 lineage and capture exact run/job/log boundary.
7. Fresh applicable exact-head CI is required for any changed #84 head. **NO MERGE.**
8. Maximum claim: `F4/25.1 FIRST_CAUSAL_SIDE_RESOLVED` if the run distinguishes product vs harness/service boundary. Do not claim Windows auth PASS unless the unchanged literal assertions actually pass.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP. A later JOBS cycle decides any corrective owner/scope.

**Required evidence:** exact integration/#74/#84 SHAs; changed diagnostic files/functions; no secret/token values in logs; exact fresh Windows run/job; ordered submit-boundary observations; unchanged assertion result; exact-head CI; explicit product-vs-harness/service attribution or `UNRESOLVED`.  
**STOP:** product behavior change is needed, auth/security redesign, backend/provider change, unrelated product files, integration mutation, #72/AAA Review overlap, diagnostic output risks secrets, or one bounded instrumented run still cannot attribute the causal side.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** other F4 work needs external signing/hardware/tester evidence or shares release-chain/auth ownership. Trash recent-reauth overlaps this auth/session investigation and is not independent.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-091`: NO_RESULT at CYCLE 097 preflight; no matching current-assignment result; superseded; NOT_PASS.
- Late `NIGHT-BBB-088` / Issue #41 `5483886991`: `BLOCKED_STOP / FIRST_CAUSAL_BOUNDARY_ATTRIBUTED`; consumed as factual input despite arriving after CYCLE 096. It does not satisfy BBB091 and does not PASS 25.1.
- Current literal #84 Windows Auth remains RED on exact `c6c5ecb...`; run `33423712589`, job `99592060690`.
