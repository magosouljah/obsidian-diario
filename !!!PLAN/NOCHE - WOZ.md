# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-149`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 DNS-rebinding SSRF P1; diagnose live gate failure, refresh/revalidate + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-WOZ-148 = NO_RESULT / SUPERSEDED / NOT_PASS; no RESULTADO DEL TURNO nor Issue #41 handoff verified before JOBS CYCLE150.`
- `LIVE_PR_FACT: #89 remains OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a, recorded base 816f946c09d998ee5a045b3e70b2fe4f3a4160d0; stale behind live aa445095...; mechanical mergeability never authorizes merge.`
- `LIVE_CI_FACT: F0/0.9 run 33454881387 remains completed/FAILURE on exact head daf87da6...; known failure is Rust unit contracts because tauri::generate_context! requires missing frontendDist ../dist. Earlier audit/DNS/TS/cloud steps passed. Gate is not waived.`
- `SERIALIZATION: WOZ149 exclusively owns #89 refresh/revalidation/integration. AAA146 owns F2/12.1 runtime evidence READ-ONLY. BBB145 owns recent-reauth seam. #93 remains mutation-unassigned.`

### PRIMARY

REUSE #89; diagnose the live security-gate failure, preserve only the bounded SSRF P1/audit slice, refresh onto live integration and merge only under exact evidence.

1. Fresh preflight integration HEAD, #89 base/head/mergeability/changed files, Issue #41 and owner collisions.
2. Duplicate-check equivalent DNS-pinning/SSRF corrective integrated after #89 creation through #96; if already resolved equivalently, STOP with evidence.
3. Confirm run `33454881387`: Rust unit contracts fail before substantive Rust tests because `frontendDist ../dist` is absent. Apply the smallest history-preserving workflow/harness ordering correction within #89 audit scope, or prove live integration already supplies it. Do not hide/waive/bypass the gate.
4. History-preserving reconcile #89 onto live integration `aa4450956579de381e82acf06c660b658c703cd1`, preserving unrelated later changes.
5. Scope remains audit docs + DNS-rebinding SSRF hardening/regression + security workflow strictly needed to execute the gate; no unrelated cleanup.
6. Run exact-head F0/0.9 security gate + applicable Required CI after refresh. Old-head results are non-authoritative.
7. Immediately before integration recheck live integration HEAD, refreshed #89 exact base/head, changed files, mergeability, CI and ownership.
8. If exact/green/race-free, WOZ149 is authorized to expected-head merge **PR #89 only**, then verify merge SHA + parents.
9. Maximum claim: `F0/0.9 DNS_REBINDING_SSRF_P1_CORRECTIVE_INTEGRATED`; AI-assisted audit is not independent pentest; F0 global stays open.
10. Do not touch Review, recent-reauth/Trash, F2/12.1 runtime deployment or production provider state. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** duplicate-check; exact diagnosis; integration SHA before/after; refreshed #89 base/head; changed files; exact-head security/Required CI; merge SHA/parents if merged; residual P0/P1/P2/P3 and independent-review `UNVERIFIED`.  
**STOP:** unsafe refresh, scope drift, failed/cancelled required CI, baseline race, newer duplicate, auth/F2 collision, or any integration mutation other than expected-head #89.

### CI-FALLBACK

**READ-ONLY F4/25.1 / PR #93 stale-evidence inventory — only while PRIMARY genuinely waits externally after a clean #89 refresh.**

- **Scope:** inspect #93 exact base/head/changed files/commits, historical checks and divergence from live; classify only `REUSE_REFRESHABLE`, `STALE_INVALIDATED`, or `NO_LONGER_APPLICABLE`. No #89 touch and no #93 mutation.
- **Evidence required:** live integration SHA; #93 exact start/end head; changed-file inventory; existing check conclusions; divergence/material-conflict notes; packaged-current-baseline/runtime `UNVERIFIED`.
- **STOP:** any mutation/rerun/review/merge/new PR/gate promotion, overlap with AAA146/BBB145, head movement, or PRIMARY stops waiting. Return immediately to #89.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-148`: no matching final result/handoff verified by JOBS CYCLE150 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
