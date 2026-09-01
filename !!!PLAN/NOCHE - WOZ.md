# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-119`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 DNS-rebinding SSRF P1; refresh/revalidate + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-WOZ-118 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching RESULTADO DEL TURNO or Issue #41 handoff verified before CYCLE120.`
- `LIVE_PR_FACT: #89 OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a, recorded base 816f946c09d998ee5a045b3e70b2fe4f3a4160d0, mergeable=true; base remains materially stale versus live integration 43fdf70e... and does NOT authorize merge.`
- `SERIALIZATION: WOZ119 exclusively owns #89 refresh/revalidation/integration. AAA116 owns F1/1.7 READ-ONLY classification. BBB115 owns recent-reauth seam. #93 remains mutation-unassigned.`

### PRIMARY

**F0 / 0.9 — REUSE #89; preserve only the bounded SSRF P1/audit slice, refresh onto live integration and merge only under exact evidence.**

1. Fresh preflight integration HEAD, #89 base/head/mergeability/changed files, Issue #41 and owner collisions.
2. Duplicate-check any DNS-pinning/SSRF corrective integrated after #89 creation. If already resolved equivalently, STOP with evidence instead of refreshing.
3. History-preserving reconcile #89 onto current live integration, preserving unrelated #92/#94/#95 and all later integration changes.
4. Scope stays exactly audit docs + DNS-rebinding SSRF hardening/regression/workflow; no unrelated cleanup.
5. Run exact-head F0/0.9 security gate + all applicable required CI after refresh. Old-head green is non-authoritative.
6. Immediately before integration, recheck live integration HEAD, refreshed #89 exact base/head, changed files, mergeability, CI and owner collision.
7. If exact/green/race-free, WOZ119 is authorized to expected-head merge **PR #89 only** and verify merge SHA + parents.
8. Maximum claim: `F0/0.9 DNS_REBINDING_SSRF_P1_CORRECTIVE_INTEGRATED`; AI-assisted audit is not an independent pentest and F0 global remains open.
9. Do not touch Review, recent-reauth/Trash or production deploy/runtime.
10. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** duplicate-check; live integration SHA before/after; refreshed #89 base/head; changed-file inventory; exact-head security/required CI conclusions; merge SHA/parents if merged; residual P0/P1/P2/P3 and independent-review `UNVERIFIED`.  
**STOP:** unsafe refresh, scope drift, failed/cancelled required CI, baseline race, newer duplicate, auth/F2 collision or any integration mutation other than expected-head #89.

### CI-FALLBACK

**READ-ONLY F4/25.1 / PR #93 evidence applicability inventory — only while PRIMARY is genuinely WAITING_CI/WAITING_EXTERNAL after a clean #89 refresh.**

- Scope: inspect #93 current base/head/changed files, old Windows Auth evidence and delta from live integration; identify exactly what would need refresh/revalidation if 1.7 keeps Windows Auth `MUST_CLOSE` for alpha.
- Evidence required: current #93 base/head/mergeability; old exact-green run IDs/SHA; current live baseline delta; explicit `UNVERIFIED`; no claims of canonical coverage.
- STOP: any mutation of #93/branch/workflow/product, any new PR, any CI rerun, any 25.1 promotion, any overlap with BBB115/AAA116, or the moment PRIMARY stops waiting externally. Return to PRIMARY and recheck #89 before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-118`: no matching final result/handoff verified by JOBS CYCLE120 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-117`: `NO_RESULT / SUPERSEDED / NOT_PASS` in CYCLE119.
