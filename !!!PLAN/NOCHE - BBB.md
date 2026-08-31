# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-097`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — sanitize and identify first unexpected auth request on #84`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; exact live base.`
- `EVIDENCE_CANDIDATE: PR #84 @ 28c3810c43eefa8bab0ffa2026c371882ead2f2f; OPEN/Ready/mergeable; exact live base.`
- `PREDECESSOR: NIGHT-BBB-096 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff al preflight JOBS CYCLE 102; SUPERSEDED / NOT_PASS.`
- `AUTHORITATIVE_FAILURE: Windows Auth Journey 33439899177 / job 99645269221 = FAILURE; repeated unexpected-request, gatePresent=true, tokenPresent=false.`
- `WHY_ASSIGNED: la siguiente operación segura sigue siendo causal y diagnostic-only; no existe evidencia que autorice product correction.`
- `SERIALIZATION: BBB owns #84 diagnostics only. AAA098 owns F2/13.2. WOZ101 owns D10.2 READ-ONLY. Do not touch Review/Trash/#83/#76/#85/provider/payment/integration.`

### PRIMARY

**F4 / 25.1 — diagnostic-only first unexpected-request localization; no speculative product fix.**

1. Fresh preflight integration/#74/#84/Issue #41; STOP on material lineage/head/base race or duplicate owner.
2. Reuse #84 only; no third auth PR and no product changes.
3. Make the smallest diagnostic-only harness change needed to record the **first** unexpected request as sanitized `{method, pathname/requestClass}`. Exclude query, body, headers, token, password and secret values.
4. Preserve literal assertions unchanged: exact returned session token persists and AccountGate exits.
5. Run one fresh packaged Windows Auth journey on exact new #84 head plus applicable exact-head CI.
6. If trace proves the harness is rejecting a legitimate required request, BBB may apply only the corresponding minimum harness allowlist/mock correction and rerun once with assertions unchanged.
7. If trace proves product request/route/command behavior is the required correction, STOP `PRODUCT_SIDE_PROVEN`; do not mutate product #74.
8. If WDIO/Tauri service prevents attribution, STOP `HARNESS_SERVICE_BLOCKED`; no workaround that weakens assertions.
9. **NO MERGE.** Maximum claim: `F4/25.1 CAUSAL_BOUNDARY_RESOLVED`; PASS only if literal packaged assertions actually pass.
10. Escribir RESULTADO DEL TURNO aquí + Issue #41 handoff y STOP.

**Required evidence:** exact base/#74/#84 heads; sanitized first unexpected request; attribution; changed files; unchanged assertion result; fresh run/job + exact-head CI; explicit UNVERIFIED.  
**STOP:** product mutation needed, auth/security redesign, unrelated files, diagnostic leakage risk, integration mutation, or bounded diagnostic cannot attribute cause.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-096`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 102; no final result ni matching handoff.
- `NIGHT-BBB-095`: `BLOCKED_STOP / HARNESS_SERVICE_BLOCKED`; exact #84 `28c3810c...`, run `33439899177` / job `99645269221` red. Issue #41 `5485389606`.
- `NIGHT-BBB-093`: diagnostic trace introduced; literal auth remained NOT_PASS.
