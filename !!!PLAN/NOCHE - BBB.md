# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-095`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 unexpected-request causal-boundary localization`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ 28c3810c43eefa8bab0ffa2026c371882ead2f2f; OPEN/Ready/mergeable; base exact live integration.`
- `PREDECESSOR: NIGHT-BBB-094 dejó no final RESULTADO DEL TURNO y no matching Issue #41 handoff/material #84 movement al preflight JOBS CYCLE 100; SUPERSEDED / NOT_PASS.`
- `AUTHORITATIVE_FAILURE: F4 - 25.1 Windows Auth Journey run 33439899177 / job 99645269221 = FAILURE on exact #84 head 28c3810c...; exact-head D6/D7/Web/Desktop Portability/Windows Import remain observed green.`
- `WHY_ASSIGNED: global recalculation still places literal packaged Windows auth as the highest-value technical blocker. Current trace proves repeated boundary=unexpected-request, gatePresent=true, tokenPresent=false, but not which side owns the mismatch.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA096 owns F2/13.2. WOZ099 owns #76 legal/public-route reconciliation. Do not touch Review/Trash/#83/#76/payment/provider scope.`

### PRIMARY

**F4 / 25.1 — resolve the first exact `unexpected-request` boundary on #84 before any product corrective.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact failed run/job; STOP if lineage/head/base materially moved or duplicate ownership appears.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence lineage. Do not create a third auth PR.
3. Inspect the current redacted diagnostic trace and #84 harness only far enough to identify the first actual unexpected request: method/route/command class and expected mock/handler boundary, without secrets/token values.
4. **Do not change product auth/session logic.** If mismatch is proven harness/mock/config-only, apply only the minimum harness-side correction on #84, preserve literal product assertions unchanged and run one fresh packaged Windows auth journey.
5. If the request is caused by product request shape/route/command behavior or otherwise requires product code, STOP as `PRODUCT_SIDE_PROVEN`; report exact evidence for a later bounded JOBS corrective assignment.
6. If WDIO/Tauri service capability fails before attribution, STOP as `HARNESS_SERVICE_BLOCKED`; do not paper over it.
7. Any changed #84 head requires fresh exact-head applicable CI. **NO MERGE.**
8. Maximum claim: `F4/25.1 CAUSAL_BOUNDARY_RESOLVED`; PASS only if unchanged literal assertions actually pass in the packaged Windows journey.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** exact integration/#74/#84 SHAs; failed run/job consumed; first unexpected request identity redacted; attribution `HARNESS_ONLY`, `PRODUCT_SIDE_PROVEN`, `HARNESS_SERVICE_BLOCKED` or `UNRESOLVED`; changed files if any; unchanged assertion result; fresh exact-head run/CI if mutated.  
**STOP:** product change needed, auth/security redesign, backend/provider change, unrelated files, integration mutation, diagnostic leakage risk, or one bounded pass cannot attribute the boundary.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** other F4 work shares auth/release ownership or needs external signing/hardware/tester evidence; F2/15.1 recent-reauth materially overlaps auth/session.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-094`: `NO_RESULT / SUPERSEDED / NOT_PASS` at JOBS CYCLE 100 preflight; no final result, matching Issue #41 handoff or material #84 movement.
- `NIGHT-BBB-093`: `DIAGNOSTIC_COMPLETE / NOT_PASS`; #84 exact head `28c3810c43eefa8bab0ffa2026c371882ead2f2f`; F4 Windows Auth run `33439899177` / job `99645269221` failed.
- Reusable trace: repeated `unexpected-request`; `gatePresent=true`; `tokenPresent=false`; literal token-persistence assertion remains red.
