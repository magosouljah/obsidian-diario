# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-077`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — Windows auth regression proof / safe candidate refresh`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-BBB-076 produced no final RESULTADO DEL TURNO before JOBS CYCLE 082; not PASS.`
- `REUSE_EVIDENCE: #71 regression proof + #74 historical candidate; do not rebuild auth harness from scratch.`
- `SERIALIZATION: BBB MUST NOT mutate integration. WOZ/#83 is the only integration mutation authorized in CYCLE 082.`

### PRIMARY

**F4 / 25.1 — turn windows/auth from frozen history into current exact evidence.**

1. Fresh preflight integration + Issue #41 + duplicate-check.
2. REUSE #71 and #74. Determine exact current #74 base/head/delta and compare to live integration.
3. If history-preserving reconciliation is clean and does not cross F1/F2/F3 ownership, refresh #74 preserving only its intended Desktop/Windows auth delta.
4. Run the authoritative Windows auth functional journey that demonstrates current session persistence/reauth behavior required by the matrix.
5. Run fresh exact-head applicable CI after any refresh.
6. If reconciliation is unsafe, scope is stale/conflicting, or external credentials/hardware are required, STOP with an exact conflict/gap map instead of forcing history.
7. NO MERGE. Do not touch #83, F3/20.2, F2/13.2, #72, signing/provider resources.
8. Maximum claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY` or `BLOCKED_SAFE_REFRESH`; not global 25.1 closure.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; #71/#74 exact refs; changed-file/scope comparison; refresh method if used; Windows auth journey output; exact-head CI; explicit NOT_COVERED/UNVERIFIED.  
**STOP:** unsafe reconciliation, cross-phase overlap, scope drift, integration race, required external credentials/hardware, or non-attributable CI failure.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent release-chain slice is safe while windows/auth ownership is active and WOZ owns the sole integration transaction.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-076`: NO_RESULT before CYCLE 082; not PASS.
- `NIGHT-BBB-075`: PASS; #79 docs-only readiness artifact merged as `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, parents `957f9777...` + `a3c4d56e...`; no global 25.2 closure claim.
