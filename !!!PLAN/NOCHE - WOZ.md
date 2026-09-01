# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-109`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 security candidate, refresh + exact-head validation + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT_REBASED: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-WOZ-108 no final result/handoff verified; SUPERSEDED / NOT_PASS.`
- `NEW_FACT: PR #91 landed during JOBS CYCLE 110 as 134a293... after exact-head CI. #89 remains OPEN/Ready @ daf87da6... on stale base 816f946c... and must now reconcile #88/#90/#91.`
- `SERIALIZATION: WOZ109 exclusively owns #89 review/refresh/integration. AAA106 owns F2/13.2 and NO MERGE. BBB105 owns #84 and NO MERGE. WOZ109 is the only integration mutation owner after the #91 concurrent merge.`

### PRIMARY

**F0 / 0.9 — make #89 current and integrate only if exact/race-free.**

1. Fresh preflight integration HEAD (`134a293...` or newer), #89 base/head/mergeability/changed files, Issue #41 and ownership.
2. REUSE #89; verify exact DNS-pinning/rebinding semantics and regression coverage.
3. Reconcile audit/docs with #88 technical signing seam, #90 OAuth readiness software and #91 Web bootstrap corrective already integrated. Preserve: AI-assisted audit ≠ independent pentest; productive signing and actual OAuth rotation remain external.
4. History-preserving refresh/rebase/union #89 onto the live integration head only if clean and scope-bounded. Conflict/unrelated scope drift => STOP.
5. Run/recheck exact-head F0/0.9 security workflow + Required CI and all applicable checks.
6. Immediately before merge recheck integration head, #89 head/base/mergeability and owner collision. If exact-base/head, all applicable CI SUCCESS and race-free, WOZ109 is authorized to merge **PR #89 only** with expected-head protection.
7. Verify merge SHA + parents. Maximum claim = `F0/0.9 AI_ASSISTED_SECURITY_SLICE PASS/INTEGRATED + DNS_REBINDING_P1_FIXED`; no independent-pentest/F0-global/release claim.
8. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** live pre/post integration; old/new #89 base/head; changed files; refresh method; semantic proof; exact-head workflow names/conclusions; merge SHA/parents if merged; residual security/signing/OAuth external state.  
**STOP:** conflict/scope drift, unrelated auth/Web/provider/deploy changes, external credentials/signing, failed required CI, base/head race, or any integration mutation other than expected-head #89.

### CI-FALLBACK

**Trigger:** only if refreshed #89 reaches genuine `WAITING_CI`.

`CI-FALLBACK: READ-ONLY F1/1.7 blocker-classification prep.`

- **Scope:** using current Plan/GitHub only, map remaining alpha blockers after #91 integration into `HARD_BLOCKER`, `CLOSE_OR_RO_EXCLUDE`, `EXTERNAL/RO_DECISION`; no code, branch, PR, provider or plan mutation.
- **Evidence required:** exact blocker → current evidence → missing evidence/decision; no fabricated PASS.
- **STOP:** no implementation, no owner reassignment, no F1 closure claim. Return to #89 as soon as CI resolves.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-108`: `NO_RESULT / SUPERSEDED / NOT_PASS` at JOBS CYCLE 110.
- #90 readiness software and #91 Web bootstrap corrective are now integrated; #89 remains reusable/stale until WOZ109 refreshes it.
