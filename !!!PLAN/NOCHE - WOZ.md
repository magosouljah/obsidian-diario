# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-112`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — REUSE PR #93 exact-green Windows Auth evidence candidate; final exact-head validation + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-WOZ-111 dejó NO_RESULT verificable al preflight JOBS CYCLE 113; SUPERSEDED / NOT_PASS.`
- `LIVE_PR_FACT: #93 OPEN/Ready/mergeable @ b2c4eb441280343c4b9c39d57851c6d3da33abaa, exact base 134a293985c314eb09c238115e3bcb71e79f1810; changed files only .github/workflows/f4-25.1-windows-auth.yml, scripts/run-auth-e2e.mjs, tests/e2e/auth-flow.e2e.mjs.`
- `CI_FACT_AT_ASSIGNMENT: exact-head Windows Auth run 33468863393 SUCCESS; job 99734302105 SUCCESS including isolated Windows auth assertions. D6, D7, Desktop Portability, Windows Import and secret scan also SUCCESS; Upgrade staging skipped/non-applicable.`
- `SERIALIZATION: WOZ112 exclusively owns #93 review/integration. AAA109 owns F2/13.2; BBB108 owns F2/15.1. #92 and #89 are parked/unassigned during CYCLE113.`

### PRIMARY

**F4 / 25.1 — REUSE #93 and integrate only if the evidence candidate remains exact, bounded and green at execution time.**

1. Fresh preflight integration HEAD, #93 base/head/mergeability/changed files, Issue #41 and ownership.
2. Verify #93 contains only bounded harness/evidence reconstruction; no product-auth/session mutation. Confirm literal assertions still require returned session token persistence and AccountGate exit.
3. Recheck exact-head Windows Auth run/job and all applicable required CI for `b2c4eb...`; do not inherit stale green if head/base changed.
4. Verify the successful run is on exact PR head and the auth job actually executed the isolated Windows auth assertions.
5. Immediately before integration, recheck integration HEAD, #93 head/base/mergeability, scope and owner collision.
6. If base relation remains exact, all applicable required checks are SUCCESS and race-free, WOZ112 is authorized to merge **PR #93 only** using expected-head protection.
7. Verify resulting merge SHA + parents and integration HEAD.
8. Maximum claim: `WINDOWS_PACKAGED_AUTH_LITERAL_PASS_EVIDENCE_INTEGRATED`. **Do not close global F4/25.1** unless every remaining 25.1 journey requirement is independently proven.
9. #92 remains parked; do not refresh or merge it in this turn.
10. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** pre/post integration SHA; #93 exact base/head; exact changed files; exact Windows Auth run/job and step conclusions; applicable CI; merge SHA/parents if merged; residual 25.1 UNVERIFIED list.  
**STOP:** changed baseline requiring unsafe refresh, unrelated scope drift, failed required CI, product mutation discovered, owner collision, or any integration mutation other than expected-head #93.

### CI-FALLBACK

`CI-FALLBACK: NONE` — #93 CI was already completed at JOBS assignment preflight; WOZ must not invent secondary work.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-111`: `NO_RESULT / SUPERSEDED / NOT_PASS` at JOBS CYCLE 113.
- PR #92 remains reusable exact-green on old live base but is parked/unassigned CYCLE113 because #93 is the higher-priority integration lane.
- PR #89 remains reusable/stale and has no owner/merge authority CYCLE113.
