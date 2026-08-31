# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-078`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — Windows auth current evidence / safe #74 reconciliation`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-BBB-077 had no RESULTADO DEL TURNO nor Issue #41 handoff at JOBS CYCLE 083; superseded, not PASS.`
- `REUSE_EVIDENCE: #71 authoritative Windows auth failure proof; #74 OPEN/Ready at head 14dfba52775f40f1956e3d1dcb343b07b147ba0c, stale base a9d35a3d69dd9127029fb851d189f9bd3079d03b, currently not mergeable.`
- `SERIALIZATION: BBB MUST NOT mutate integration. WOZ/#83 owns the only integration mutation.`

### PRIMARY

**F4 / 25.1 — reconcile only the Windows auth corrective lineage and produce current evidence.**

1. Fresh preflight integration + Issue #41 + duplicate-check.
2. REUSE #71/#74; do not rebuild the auth harness.
3. Compare #74 exact two-file product delta against live integration. If a clean history-preserving refresh is possible without crossing F1/F2/F3 ownership, refresh only that intended Desktop runtime-detection/session-persistence delta.
4. Run the authoritative Windows auth functional journey proving packaged Desktop login session persistence/reauth behavior.
5. Run fresh exact-head applicable CI after any head change.
6. If #74 conflicts materially, another candidate already owns the correction, external hardware/credentials are required, or scope crosses ownership, STOP with exact conflict/gap map instead of forcing history.
7. NO MERGE. Do not touch #83, F3/20.2, F2/13.2, #72, signing or provider resources.
8. Maximum claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY` or `BLOCKED_SAFE_REFRESH`; not global 25.1 closure.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; #71/#74 refs; changed-file/scope comparison; refresh method if any; Windows auth journey output; exact-head CI; explicit NOT_COVERED/UNVERIFIED.  
**STOP:** unsafe reconciliation, duplicate owner/candidate, cross-phase overlap, scope drift, external credentials/hardware, integration race, or non-attributable CI failure.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent release-chain fallback is safe while windows/auth ownership is active.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-077`: NO_RESULT at CYCLE 083; superseded; not PASS.
- `NIGHT-BBB-075`: PASS for #79 docs-only readiness artifact merge only; no global 25.2 closure.

## RESULTADO DEL TURNO — NIGHT-BBB-078

### PRIMARY

- `STATUS: WAITING_CI`
- `baseline: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0` (freshly rechecked; unchanged during preflight).
- `branch/head: aaa/night-25.1-auth-session-corrective @ b3468003a80288109e2d537a7aa3f25a7269927c`
- `PR: #74 OPEN/Ready; NO MERGE performed.`
- `cambios: history-preserving refresh of #74 only. Live integration advanced 25 commits from #74 merge-base a9d35a3d... but none touched #74's two intended files. Built merge tree from live integration tree 268547b... plus the exact #74 blobs for src/platform/index.ts and tests/component-dom/platformRuntime.test.ts; created merge commit b3468003... with parents old #74 head 14dfba527... + live integration 816f946c...; fast-forwarded only #74 head branch. Product delta remains exactly those two files; integration was not mutated.`
- `tests: authoritative #71 Windows auth journey is not yet current on refreshed #74 head; UNVERIFIED pending an attributable run. Existing fail-before remains #71 run 33313675968 / job 99263095638: Desktop login did not persist returned session token.`
- `CI: fresh exact-head PR CI started automatically on b3468003...: Test - Desktop Portability run 33396503472 QUEUED; D6 run 33396503463 IN_PROGRESS; D7 run 33396503465 IN_PROGRESS; Web - Production Build run 33396503570 IN_PROGRESS; Upgrade 21.2 Staging run 33396503568 SKIPPED. External wait reached; no fallback authorized.`
- `evidencia: #74 exact pre-refresh delta = src/platform/index.ts (+14/-2) and tests/component-dom/platformRuntime.test.ts (+29/-0). a9d35a3d...→816f946c... changed 16 files, with zero overlap with those two #74 paths. Refresh commit/tree: b3468003... / 689b037a....`
- `UNVERIFIED: authoritative packaged Windows auth functional journey on refreshed corrective head; final exact-head CI conclusions while runs are pending.`
- `blockers: external CI currently pending. Windows-auth journey must be run in a way attributable to the refreshed corrective lineage before claiming WINDOWS_AUTH_CURRENT_EVIDENCE_READY.`

### CI-FALLBACK

- `STATUS: NOT_RUN`
- `branch/head si aplica: N/A`
- `PR si aplica: N/A`
- `cambios: none`
- `tests: none`
- `evidencia: JOBS explicitly wrote CI-FALLBACK: NONE for NIGHT-BBB-078.`
- `UNVERIFIED: N/A`
- `blockers: fallback prohibited because assignment says NONE.`
- `STOP alcanzado: yes — PRIMARY entered WAITING_CI and no authorized fallback exists.`

### Recomendación para JOBS

Re-check exact-head CI for `b3468003a80288109e2d537a7aa3f25a7269927c`. If green, assign/authorize the attributable authoritative Windows auth journey against this refreshed corrective lineage (reusing #71 harness) before any F4/25.1 evidence promotion. Keep NO MERGE until that literal packaged Windows session-persistence/reauth journey is green.
