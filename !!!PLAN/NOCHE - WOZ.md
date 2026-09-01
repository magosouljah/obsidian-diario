# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-110`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — REUSE PR #92 signed-out startup-loader corrective; exact-head validation + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-WOZ-109 no dejó RESULTADO DEL TURNO/matching handoff verificable al CYCLE 111 preflight; SUPERSEDED / NOT_PASS. #89 remains OPEN/stale and unowned this cycle.`
- `NEW_FACT: PR #92 OPEN/Ready/mergeable @ 9947380ce8095b718a400d1e7781d21e67b29be9 is directly based on live 134a293... and addresses observed deployed signed-out runtime: AccountGate rendered while static Loading Galer loader remained above it.`
- `SERIALIZATION: WOZ110 exclusively owns #92 review/integration. AAA107 owns F2/13.2 and NO MERGE. BBB106 owns #84 and NO MERGE. #89 is parked/unassigned during CYCLE111.`

### PRIMARY

**F2 / 12.1 — REUSE #92 and integrate only if the candidate is exact, bounded and green.**

1. Fresh preflight integration HEAD, #92 base/head/mergeability/changed files, Issue #41 and ownership.
2. Duplicate-check/reuse #92; verify the delta is limited to dismissing `#beatgaler-startup-loader` only when signed-out `.bg-account-gate` is actually rendered, and does not alter authenticated bootstrap/data-plane semantics.
3. Verify the runtime finding is represented accurately: DOM contains AccountGate while `Loading Galer...` remains visible; do not claim authenticated startup fixed from signed-out evidence alone.
4. Verify exact-head applicable CI for `9947380...`, including Web/shared and Required CI/portability gates actually required by repo policy. Skipped non-applicable jobs are not PASS claims.
5. Immediately before integration, recheck integration HEAD, #92 head/base/mergeability, scope and owner collision.
6. If base=head relation remains exact, all applicable required checks SUCCESS and race-free, WOZ110 is authorized to merge **PR #92 only** using expected-head protection.
7. Verify resulting merge SHA + parents.
8. Maximum claim: `F2/12.1 SIGNED_OUT_LOADER_CORRECTIVE_INTEGRATED`; **12.1 remains NOT_PASS** until the deployed resulting baseline is tested for applicable signed-out/authenticated startup and cold/warm behavior.
9. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** pre/post integration SHA; #92 exact base/head; changed files; semantic proof; exact check names/conclusions; merge SHA/parents if merged; runtime items still UNVERIFIED.  
**STOP:** changed baseline requiring unsafe refresh, unrelated scope drift, failed required CI, ambiguous candidate semantics, owner collision, or any integration mutation other than expected-head #92.

### CI-FALLBACK

**Trigger:** only while #92 is genuinely `WAITING_CI` / waiting equivalent external check.

`CI-FALLBACK: READ-ONLY F1/1.7 blocker-classification prep.`

- **Scope:** classify current alpha blockers from live Plan/GitHub as `HARD_BLOCKER`, `CLOSE_OR_RO_EXCLUDE`, or `EXTERNAL/RO_DECISION`; no implementation, branch, PR, provider or plan mutation.
- **Evidence required:** blocker → current evidence → missing evidence/decision, with #92 status clearly separated.
- **STOP:** no gate closure, no owner reassignment, no code/infra, no #89 mutation. Return to PRIMARY when #92 CI resolves.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-109`: `NO_RESULT / SUPERSEDED / NOT_PASS` at JOBS CYCLE 111.
- #89 remains reusable but stale; CYCLE111 prioritizes the exact-base, already-existing #92 runtime corrective and grants no #89 integration authority.
