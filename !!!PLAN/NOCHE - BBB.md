# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-079`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — Windows auth authoritative journey on refreshed #74`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-BBB-078 = WAITING_CI; refresh itself is accepted as factual work, but WINDOWS_AUTH_CURRENT_EVIDENCE_READY was NOT earned.`
- `REUSE_EVIDENCE: #71 fail-before; #74 refreshed head b3468003a80288109e2d537a7aa3f25a7269927c.`
- `POSTCHECK_BY_JOBS: exact-head runs on b3468003... completed: Desktop Portability 33396503472 SUCCESS; D6 33396503463 SUCCESS; D7 33396503465 SUCCESS; Web Production Build 33396503570 SUCCESS; Upgrade 21.2 Staging 33396503568 SKIPPED.`
- `SERIALIZATION: BBB MUST NOT mutate integration. WOZ/#83 owns the only integration mutation.`

### PRIMARY

**F4 / 25.1 — run the literal packaged Windows auth journey against refreshed corrective lineage.**

1. Fresh preflight integration + Issue #41 + #74 exact base/head + duplicate-check.
2. Reuse #71 harness and fail-before evidence; do not rebuild the harness unless a minimal attributable compatibility fix is strictly required.
3. Prove the authoritative packaged Windows Desktop login session-persistence/reauth journey against #74 head `b3468003...` (or its exact successor only if BBB itself must make a bounded test-only compatibility change).
4. Evidence must show the literal prior failure is gone: returned session token persists through the packaged Tauri runtime path and the auth gate exits as expected.
5. If any head changes, run fresh exact-head applicable CI before claiming readiness.
6. NO MERGE. Do not touch #83, F3/20.2, AAA F2/13.2, #72, signing/notarization or provider resources.
7. Maximum claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; not global 25.1 closure.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; packaged Windows environment; #71 harness identity; literal auth assertions; run/job IDs/log excerpt; exact-head CI if head moved; explicit remaining NOT_COVERED journeys.  
**STOP:** external hardware/credential dependency, harness cannot be attributed to refreshed lineage, product scope beyond #74 corrective, integration race, duplicate owner, or non-attributable CI failure.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no safe independent F4 lane is both useful and non-overlapping while windows/auth is active; #72 Review materially depends on active AAA Review work and remains frozen.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-078`: `WAITING_CI` after safe history-preserving #74 refresh to `b3468003...`; post-turn CI is now green, but authoritative Windows auth journey remains UNVERIFIED.
- `NIGHT-BBB-075`: PASS for #79 docs-only readiness artifact merge only; no global 25.2 closure.
