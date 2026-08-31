# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-080`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — make Windows auth harness attributable to refreshed #74 lineage`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-BBB-079 = BLOCKED_STOP; historical #71 Windows auth harness cannot prove refreshed #74 because it executes old/diverged head.`
- `REUSE_EVIDENCE: #71 fail-before run 33313675968 / job 99263095638; #74 refreshed head b3468003a80288109e2d537a7aa3f25a7269927c; exact-head generic CI green.`
- `SERIALIZATION: BBB MUST NOT mutate integration. WOZ/#83 owns the only integration mutation.`

### PRIMARY

**F4 / 25.1 — bounded test-only/history-preserving exact-lineage Windows auth proof.**

1. Fresh preflight integration + Issue #41 + #71/#74 exact heads + duplicate-check.
2. Do not accept generic #74 CI as auth evidence and do not rerun the old #71 job as proof for #74.
3. Create or refresh only the minimum BBB-owned test/workflow lineage **from exact #74 head `b3468003...`** needed to run the existing #71 packaged Windows auth journey without altering #74 product logic.
4. Prefer reuse/cherry-pick of harness/workflow-only commits or an existing workflow-dispatch mechanism. No product auth rewrite unless a new factual harness-only incompatibility makes execution impossible; in that case STOP and report.
5. Run the literal packaged Windows/Tauri auth assertions attributable to that exact lineage: returned session token persists and auth gate exits; include reauth/session persistence as already encoded by the harness where applicable.
6. If the test-only head moves, require fresh exact-head applicable CI before claiming readiness.
7. **NO MERGE.** Do not touch #83, F3/20.2, AAA F2/13.2, #72, signing/notarization or provider resources.
8. Maximum claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; not global 25.1 closure.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact #74 product head; exact BBB test-only head; changed files proving harness/workflow-only scope; packaged Windows environment; #71 harness identity; literal auth assertions; run/job IDs/log excerpt; exact-head CI; explicit remaining NOT_COVERED journeys.  
**STOP:** test-only portability cannot be achieved without product changes outside #74, external hardware/credential dependency, duplicate owner, integration mutation would be required, scope overlaps AAA Review/#72, or CI failure cannot be attributed.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent F4 lane is both useful and non-overlapping while windows/auth is active; #72 Review materially depends on active AAA Review work and remains frozen.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

### NIGHT-BBB-079

- `STATUS: BLOCKED_STOP`
- `baseline: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `#74: b3468003a80288109e2d537a7aa3f25a7269927c`
- `#71 harness: 29656aa0a040043934380c97e0145608c69e8daf`
- `fail-before: run 33313675968 / job 99263095638 — Desktop login did not persist returned session token`
- `finding: #71 and #74 histories diverge; rerunning historical #71 cannot prove refreshed #74.`
- `UNVERIFIED: token persistence + gate exit on refreshed #74 packaged Windows lineage.`
- `RECOMMENDATION_TO_JOBS: authorize bounded successor making #71 harness executable on exact #74 lineage.`
- `CI-FALLBACK: NONE / NOT_EXECUTED`.

- `NIGHT-BBB-078`: safe history-preserving #74 refresh to `b3468003...`; exact-head Desktop Portability/D6/D7/Web Build later green, but auth journey unverified.
- `NIGHT-BBB-075`: PASS for #79 docs-only readiness artifact merge only; no global 25.2 closure.
