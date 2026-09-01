# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-142`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 DNS-rebinding SSRF P1; diagnose live gate failure, refresh/revalidate + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-WOZ-141 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff verified before CYCLE143.`
- `LIVE_PR_FACT: #89 remains OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a with recorded base 816f946c09d998ee5a045b3e70b2fe4f3a4160d0; stale behind aa445095...; stale base does NOT authorize merge.`
- `LIVE_CI_FACT: F0/0.9 workflow run 33454881387 remains completed/FAILURE on exact head daf87da6...; this is NOT a green head.`
- `SERIALIZATION: WOZ142 exclusively owns #89 refresh/revalidation/integration. AAA139 owns F2/12.1 runtime evidence READ-ONLY. BBB138 owns recent-reauth seam. #93 remains mutation-unassigned.`

### PRIMARY

**F0 / 0.9 — REUSE #89; diagnose the live security-gate failure, preserve only the bounded SSRF P1/audit slice, refresh onto live integration and merge only under exact evidence.**

1. Fresh preflight integration HEAD, #89 base/head/mergeability/changed files, Issue #41 and owner collisions.
2. Duplicate-check any equivalent DNS-pinning/SSRF corrective integrated after #89 creation, including all changes through #96; if already resolved equivalently, STOP with evidence.
3. Inspect run `33454881387` / job `99692637830`; determine whether missing `../dist` is workflow/harness ordering inside #89 audit scope or already resolved by live integration. Do not hide, waive or bypass the failure.
4. History-preserving reconcile #89 onto current live integration `aa445095...`, preserving unrelated later integration changes.
5. Scope stays exactly audit docs + DNS-rebinding SSRF hardening/regression/security workflow needed to execute that gate; no unrelated cleanup.
6. Run exact-head F0/0.9 security gate + applicable required CI after refresh. Old-head results are non-authoritative.
7. Immediately before integration, recheck live integration HEAD, refreshed #89 exact base/head, changed files, mergeability, CI and owner collision.
8. If exact/green/race-free, WOZ142 is authorized to expected-head merge **PR #89 only** and verify merge SHA + parents.
9. Maximum claim: `F0/0.9 DNS_REBINDING_SSRF_P1_CORRECTIVE_INTEGRATED`; AI-assisted audit is not an independent pentest and F0 global remains open.
10. Do not touch Review, recent-reauth/Trash, F2/12.1 runtime deployment or production provider state. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** duplicate-check; diagnosis of run 33454881387; live integration SHA before/after; refreshed #89 base/head; changed-file inventory; exact-head security/required CI conclusions; merge SHA/parents if merged; residual P0/P1/P2/P3 and independent-review `UNVERIFIED`.  
**STOP:** unsafe refresh, scope drift, failed/cancelled required CI, baseline race, newer duplicate, auth/F2 collision, or any integration mutation other than expected-head #89.

### CI-FALLBACK

**READ-ONLY F4/25.1 / PR #93 stale-evidence inventory — only while PRIMARY is genuinely `WAITING_CI/WAITING_EXTERNAL` after a clean #89 refresh.**

- **Scope:** inspect #93 current base/head/changed files/commits, exact-head historical checks and divergence from live `aa445095...`; determine only `REUSE_REFRESHABLE`, `STALE_INVALIDATED`, or `NO_LONGER_APPLICABLE`. This is independent of #89: no #89 files/branch/PR/lock/ownership are touched. Do not mutate or adjudicate global 25.1 closure.
- **Evidence required:** live integration SHA; #93 exact base/head at start/end; changed-file inventory; existing exact-head check conclusions; divergence/material-conflict notes; explicit runtime/packaged-current-baseline `UNVERIFIED`.
- **STOP:** any mutation/rerun/review/merge/new PR/gate promotion, overlap with AAA139/BBB138, head movement during inspection, or PRIMARY no longer waiting. Return to #89 immediately when PRIMARY ceases waiting.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-141`: no matching final result/handoff verified by JOBS CYCLE143 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-140`: no matching final result/handoff verified by JOBS CYCLE142 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
