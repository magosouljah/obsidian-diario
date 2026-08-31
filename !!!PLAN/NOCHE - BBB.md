# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-094`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 unexpected-request causal-boundary localization`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ 28c3810c43eefa8bab0ffa2026c371882ead2f2f; OPEN/Ready/mergeable; base exact live integration.`
- `PREDECESSOR: NIGHT-BBB-093 WAITING_CI is now factually complete as diagnostic evidence because exact-head Actions materialized and failed. F4/25.1 remains NOT_PASS.`
- `AUTHORITATIVE_FAILURE: F4 - 25.1 Windows Auth Journey run 33439899177 / job 99645269221 = FAILURE on exact #84 head 28c3810c...; trace shows repeated boundary=unexpected-request, gatePresent=true, tokenPresent=false. Broad D6/D7/Web/Desktop Portability/Windows Import exact-head runs are green.`
- `WHY_ASSIGNED: current evidence narrows the failure to the request/mock/service boundary but still does not justify a product corrective. The next critical step is to identify what request is unexpected and which side owns the mismatch without changing product behavior.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA095 owns F2/13.2. WOZ098 owns F3/18.2 READ-ONLY. Do not touch Review/Trash/#83/payment/provider scope.`

### PRIMARY

**F4 / 25.1 — resolve the exact `unexpected-request` boundary on #84 before any product corrective.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact failed run/job; STOP if lineage/head/base materially moved or duplicate ownership appears.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence lineage. Do not create a third auth PR.
3. Inspect the current diagnostic trace and #84 harness only far enough to identify the first actual unexpected request: method/route/command class and expected mock/handler boundary, with secrets/token values redacted.
4. **Do not change product auth/session logic.** If the mismatch is proven harness/mock/config-only, apply only the minimum harness-side correction on #84, preserve literal product assertions unchanged and rerun one fresh packaged Windows auth journey.
5. If the unexpected request is caused by product request shape/route/command behavior or otherwise requires product code change, STOP as `PRODUCT_SIDE_PROVEN`; report exact evidence so JOBS can authorize a later bounded corrective.
6. If service/session capability fails before causal attribution, STOP as `HARNESS_SERVICE_BLOCKED`; do not paper over it.
7. Any changed #84 head requires fresh exact-head applicable CI. **NO MERGE.**
8. Maximum claim: `F4/25.1 CAUSAL_BOUNDARY_RESOLVED`; claim PASS only if unchanged literal assertions actually pass on the packaged Windows journey.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** exact integration/#74/#84 SHAs; exact failed run/job consumed; first unexpected request identity without sensitive values; attribution `HARNESS_ONLY`, `PRODUCT_SIDE_PROVEN`, `HARNESS_SERVICE_BLOCKED` or `UNRESOLVED`; changed files if any; unchanged assertion result; fresh exact-head run/CI if mutated.  
**STOP:** product change needed, auth/security redesign, backend/provider change, unrelated files, integration mutation, diagnostic leakage risk, or one bounded pass cannot attribute the boundary.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** other F4 work shares release/auth ownership or requires external signing/hardware/tester evidence; Trash recent-reauth overlaps auth/session materially.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-093`: `DIAGNOSTIC_COMPLETE / NOT_PASS` processed by JOBS CYCLE 099. #84 moved to `28c3810c43eefa8bab0ffa2026c371882ead2f2f`; exact F4 Windows Auth run `33439899177` / job `99645269221` failed.
- Exact trace: repeated `unexpected-request`; `gatePresent=true`; `tokenPresent=false`; literal error remains `Desktop login did not persist the returned session token.`
- This evidence narrows but does not yet prove product-vs-harness/service ownership; no PASS or product corrective authorized.
