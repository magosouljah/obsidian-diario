# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-076`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — Windows auth regression proof / safe candidate refresh`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-BBB-075 = PASS; PR #79 merged as 816f946c09d998ee5a045b3e70b2fe4f3a4160d0, parents 957f9777... + a3c4d56e...; maximum claim only F4/25.2 internal beta-readiness artifact integrated.`
- `SERIALIZATION: BBB MUST NOT mutate integration this cycle. WOZ/#83 is the only authorized integration mutation.`

### PRIMARY

**F4 / 25.1 — reuse #71/#74 and turn windows/auth from frozen history into current exact evidence.**

1. Fresh preflight integration + Issue #41 + duplicate-check.
2. REUSE-FIRST #71 regression proof and #74 candidate; do not rebuild the auth harness from scratch.
3. Determine exact current #74 base/head/delta and whether history-preserving reconciliation onto `816f946c...` is safe without crossing F1/F2/F3 ownership.
4. If safe, refresh #74 history-preservingly, preserve only its intended Windows/Desktop auth product delta, and run fresh exact-head applicable CI plus the authoritative Windows auth functional journey.
5. If refresh is unsafe or #74 scope conflicts with current integration, STOP with exact conflict/gap map; do not force cherry-pick/rewrite.
6. Do not merge integration. Do not touch #83, F3/20.2, F2/13.2, signing/provider resources.
7. Maximum claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY` or `BLOCKED_SAFE_REFRESH`; not global 25.1 closure.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live baseline; #71/#74 exact refs; changed-file/scope comparison; refresh method if used; Windows auth journey result; exact-head CI; remaining NOT_COVERED/UNVERIFIED.  
**STOP:** unsafe history reconciliation, cross-phase product overlap, scope drift, integration race, required external credentials/hardware, or failing non-attributable CI.

### CI-FALLBACK

`CI-FALLBACK: NONE` — avoid mixing release-chain/auth ownership while WOZ owns the sole integration transaction.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

### NIGHT-BBB-075

- STATUS: `PASS`.
- #79 exact docs-only candidate merged as `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- Parents verified: `957f97771b7a15554cf6e002fe9eb215c71a65cc` + `a3c4d56e8317d7711832154ecc72afe581d2b309`.
- Issue #41 handoff `5477503306`.
- UNVERIFIED remains tester execution, signing/notarization, release GO and global 25.2 closure.
