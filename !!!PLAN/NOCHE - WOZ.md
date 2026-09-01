# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-138`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 DNS-rebinding SSRF P1; diagnose live gate failure, refresh/revalidate + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-WOZ-137 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff verified before CYCLE139.`
- `LIVE_PR_FACT: #89 remains OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a with recorded base 816f946c09d998ee5a045b3e70b2fe4f3a4160d0; stale base does NOT authorize merge.`
- `LIVE_CI_FACT: F0/0.9 workflow run 33454881387 reconsulted CYCLE139 = completed/FAILURE on exact head daf87da6...; this is NOT a green head.`
- `SERIALIZATION: WOZ138 exclusively owns #89 refresh/revalidation/integration. AAA135 owns F1/1.7 READ-ONLY classification. BBB134 owns recent-reauth seam. PR #96 is ACTIVE_EXTERNAL_CANDIDATE with no night mutation owner; #93 remains mutation-unassigned.`

### PRIMARY

**F0 / 0.9 — REUSE #89; diagnose the live security-gate failure, preserve only the bounded SSRF P1/audit slice, refresh onto live integration and merge only under exact evidence.**

1. Fresh preflight integration HEAD, #89 base/head/mergeability/changed files, Issue #41 and owner collisions.
2. Duplicate-check any equivalent DNS-pinning/SSRF corrective integrated after #89 creation; if already resolved equivalently, STOP with evidence.
3. Inspect run `33454881387` / job `99692637830`; determine whether missing `../dist` is a workflow/harness ordering defect inside #89 audit scope or a consequence already resolved by live integration. Do not hide, waive or bypass the failure.
4. History-preserving reconcile #89 onto current live integration, preserving unrelated later integration changes.
5. Scope stays exactly audit docs + DNS-rebinding SSRF hardening/regression/security workflow needed to execute that gate; no unrelated cleanup.
6. Run exact-head F0/0.9 security gate + applicable required CI after refresh. Old-head results are non-authoritative.
7. Immediately before integration, recheck live integration HEAD, refreshed #89 exact base/head, changed files, mergeability, CI and owner collision.
8. If exact/green/race-free, WOZ138 is authorized to expected-head merge **PR #89 only** and verify merge SHA + parents.
9. Maximum claim: `F0/0.9 DNS_REBINDING_SSRF_P1_CORRECTIVE_INTEGRATED`; AI-assisted audit is not an independent pentest and F0 global remains open.
10. Do not touch Review, recent-reauth/Trash, PR #96 or production deploy/runtime. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** duplicate-check; diagnosis of run 33454881387; live integration SHA before/after; refreshed #89 base/head; changed-file inventory; exact-head security/required CI conclusions; merge SHA/parents if merged; residual P0/P1/P2/P3 and independent-review `UNVERIFIED`.  
**STOP:** unsafe refresh, scope drift, failed/cancelled required CI, baseline race, newer duplicate, auth/F2 collision, PR #96 mutation, or any integration mutation other than expected-head #89.

### CI-FALLBACK

**READ-ONLY F2/12.1 / PR #96 stability + evidence inventory — only while PRIMARY is genuinely `WAITING_CI/WAITING_EXTERNAL` after a clean #89 refresh.**

- **Scope:** inspect #96 current base/head/changed files/commits, branch activity, exact-head check-runs/statuses and whether a matching worker/handoff has appeared; determine only `HANDOFF_READY`, `CI_PENDING`, `ACTIVE_EXTERNAL`, or `UNSTABLE_ACTIVE_EXTERNAL`. Do not adjudicate 12.1 closure.
- **Evidence required:** live integration SHA; #96 exact base/head at start/end of inspection; changed-file inventory; exact check-runs/statuses tied to that head; timestamps/activity sufficient to detect head movement; explicit public-runtime `UNVERIFIED`.
- **STOP:** any mutation of #96/branch/workflow/product, any CI rerun, review/merge action, new PR, 12.1 promotion, overlap with BBB134/AAA135, or head movement during inspection. If head changes, record `UNSTABLE_ACTIVE_EXTERNAL`, stop fallback. The moment PRIMARY ceases waiting externally, return to #89 and recheck before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-137`: no matching final result/handoff verified by JOBS CYCLE139 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-136`: no matching final result/handoff verified by JOBS CYCLE138 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
