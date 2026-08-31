# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-086`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — minimum product auth corrective on exact #74/#84 lineage`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ b3468003a80288109e2d537a7aa3f25a7269927c; ownership of this bounded F4 slice is explicitly transferred to BBB for CYCLE 091.`
- `EVIDENCE_CANDIDATE: PR #84 @ d13a1969aef1ca53ee7fbed0bcba241ceb766d42; OPEN/Ready/mergeable; literal Windows auth evidence harness on #74 lineage.`
- `PREDECESSOR: NIGHT-BBB-085 = BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED; no harness/workflow-only corrective justified.`
- `AUTHORITATIVE_FAILURE: run 33407580887 / job 99538870371 reached real packaged Windows/Tauri auth and failed at tests/e2e/auth-flow.e2e.mjs:64: Desktop login did not persist the returned session token.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA087 and WOZ090 do not own #74/#84.`

### PRIMARY

**F4 / 25.1 — correct only the minimum product logic proven insufficient by the exact Windows auth journey, then regenerate exact-lineage evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact checks; duplicate-check before mutation.
2. Reuse #74 as the sole product-corrective lineage and #84 as the sole Windows-auth evidence candidate. Do not create duplicate product/evidence PRs unless the existing branches are technically unwritable; if so STOP/report rather than fork silently.
3. Diagnose only the literal product boundary behind missing `beatgaler:account-session:v1` persistence in the packaged Tauri runtime. Use the existing fail-before/fail-current evidence; do not reopen generic harness triage.
4. Apply the minimum product correction needed on #74 lineage. Preserve auth/security contract, backend API, unrelated runtime/platform logic and non-auth surfaces.
5. Refresh #84 onto the corrected exact #74 product head without losing the existing harness semantics. Record exact ancestry/head mapping.
6. Re-run the literal packaged Windows/Tauri auth journey. Require both: returned session token persists in `beatgaler:account-session:v1`, and AccountGate exits successfully.
7. Any moved #74/#84 head requires fresh applicable exact-head CI. Record run/job IDs and literal assertions.
8. **NO MERGE.** Do not touch integration, #83, AAA F2/13.2, WOZ F2/12.1, #72, signing/notarization or provider resources.
9. Maximum claim if green: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; global 25.1 remains OPEN for uncovered journeys.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration/#74/#84 pre/post heads; changed-file/function map; root cause tied to token persistence; packaged Windows runner; token persistence + AccountGate-exit assertions; exact-head CI and run/job IDs; explicit NOT_COVERED rows.  
**STOP:** correction requires auth/security contract redesign, backend/provider changes, unrelated product files, duplicate active owner, integration mutation, #72/review overlap, or failure remains unattributable after minimum bounded diagnostic.

### CI-FALLBACK

`CI-FALLBACK: NONE` — safe secondary F4 work would either overlap the same release-chain ownership or widen scope while exact auth evidence is pending.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-085`: BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED. #84 head `d13a1969...`; Required CI `33407580663` SUCCESS; literal Windows auth `33407580887` / job `99538870371` FAILURE on missing persisted session token; no harness/workflow correction justified; no merge. Issue #41 `5481842956`.
- `NIGHT-BBB-084`: NO_RESULT at CYCLE 090; superseded; NOT_PASS.
- `NIGHT-BBB-081`: established exact #84 evidence candidate; NOT_PASS.
