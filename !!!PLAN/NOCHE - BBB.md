# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-087`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — minimum product auth corrective on exact #74/#84 lineage`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ b3468003a80288109e2d537a7aa3f25a7269927c.`
- `EVIDENCE_CANDIDATE: PR #84 @ d13a1969aef1ca53ee7fbed0bcba241ceb766d42; OPEN/Ready/mergeable; literal Windows auth evidence harness on #74 lineage.`
- `PREDECESSOR: NIGHT-BBB-086 had no final RESULTADO DEL TURNO nor matching material Issue #41 handoff at CYCLE 092 preflight; superseded, NOT_PASS.`
- `AUTHORITATIVE_FAILURE: run 33407580887 / job 99538870371 reached real packaged Windows/Tauri auth and failed at tests/e2e/auth-flow.e2e.mjs:64: Desktop login did not persist the returned session token.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA088 owns F2/13.2; WOZ091 exclusively owns #83 Ready/exact-head/integration transaction.`

### PRIMARY

**F4 / 25.1 — correct only the minimum product logic proven insufficient by the exact Windows auth journey, then regenerate exact-lineage evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact checks; duplicate-check before mutation.
2. Reuse #74 as sole product-corrective lineage and #84 as sole Windows-auth evidence candidate; do not fork duplicates.
3. Diagnose only the literal product boundary behind missing `beatgaler:account-session:v1` persistence in packaged Tauri.
4. Apply the minimum product correction on #74 lineage; preserve auth/security contract, backend API and unrelated surfaces.
5. Refresh #84 onto corrected exact #74 product head without losing harness semantics; record exact ancestry/head mapping.
6. Re-run literal packaged Windows/Tauri auth journey. Require both token persistence and AccountGate exit.
7. Any moved #74/#84 head requires fresh applicable exact-head CI; record run/job IDs and literal assertions.
8. **NO MERGE.** Do not touch integration, #83, AAA F2/13.2, #72, signing/notarization or provider resources.
9. Maximum claim if green: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; global 25.1 remains OPEN for uncovered journeys.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration/#74/#84 pre/post heads; changed-file/function map; root cause tied to token persistence; packaged Windows runner; token persistence + AccountGate-exit assertions; exact-head CI and run/job IDs; explicit NOT_COVERED rows.  
**STOP:** auth/security redesign, backend/provider changes, unrelated product files, duplicate owner, integration mutation, #72/review overlap, or failure remains unattributable after bounded diagnostic.

### CI-FALLBACK

`CI-FALLBACK: NONE` — safe secondary F4 work would overlap release-chain ownership or widen scope while auth evidence is pending.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-086`: NO_RESULT at CYCLE 092 preflight; superseded; NOT_PASS.
- `NIGHT-BBB-085`: BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED. #84 head `d13a1969...`; Required CI `33407580663` SUCCESS; literal Windows auth `33407580887` / job `99538870371` FAILURE on missing persisted session token; no merge. Issue #41 `5481842956`.
- `NIGHT-BBB-081`: established exact #84 evidence candidate; NOT_PASS.
