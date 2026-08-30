# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 / 20.2 — capacity harness continuation.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-052`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — one authorized replacement PR from refreshed #77 branch`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `SOURCE_ARTIFACT: CLOSED/UNMERGED #77; branch woz/night-20.2-capacity-harness @ 50aac3f0c700a88e1f058372c23ee1d96ecf247a`
- `PREDECESSOR: NIGHT-WOZ-051 produced no final RESULTADO DEL TURNO / replacement PR before JOBS CYCLE 053; SUPERSEDED and MUST NOT execute late.`
- `FACTUAL_STATE: no replacement PR was found in duplicate-check; branch was last verified ahead 2 / behind 0 with merge-base exact live integration and two intended harness/test files.`
- `HOLD_PR: #75 @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f — frozen / DO NOT TOUCH.`

### PRIMARY

1. Fresh preflight live integration + source branch + duplicate-check. If baseline/branch changed, recompute compare before any mutation.
2. REUSE-FIRST: use the existing refreshed branch only. JOBS authorizes exactly one replacement PR because #77 cannot reopen; do not create a new implementation branch or duplicate harness.
3. Require compare to remain only `cloud-server/tests/capacity-load-harness.cjs` and `cloud-server/tests/capacity-load-harness.test.cjs`, no unrelated delta.
4. Open exactly one replacement PR against current live integration and document #77 as CLOSED/unmerged predecessor.
5. Preserve explicit target input and synthetic/local-only limitation. No invented expected peak, safety margin, provider load, 2× proof, latency target or full capacity PASS.
6. Run focused deterministic tests + fresh applicable exact-head CI.
7. Merge only if exact-head green, race-clean, narrow delta unchanged and owner flow permits. Even if merged, maximum claim is `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`; global 20.2 remains open.
8. Do not touch #75/#76/#72/#74/#71/#69/#70 or provider/infra resources.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; source branch head; fresh compare; replacement PR number/head/base; focused tests; fresh exact-head CI; merge SHA only if actually merged; explicit `RUNTIME_CAPACITY_UNVERIFIED`.  
**STOP:** duplicate replacement exists, branch scope drift, baseline race that cannot be reconciled narrowly, target invention/provider operation required, overlap with another owner, unsafe write/merge flow or non-attributable CI red.

### CI-FALLBACK

`NONE`.

**Alcance:** none preauthorized.  
**Evidencia requerida:** n/a.  
**STOP:** if PRIMARY waits CI/review/merge, do not invent secondary work; recheck PRIMARY and report.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-051`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no replacement PR found before CYCLE 053.
- `NIGHT-WOZ-050`: `BLOCKED / REOPEN_UNAVAILABLE`; #77 could not reopen, branch refreshed to `50aac3f0...` and verified narrow/exact-base; no runtime-capacity PASS.
- `NIGHT-WOZ-048`: `DONE / INTEGRATED`; #73 merged as `a306e3b3...`, only reconciliation/exception-queue software slice.

## HOLDING

- F3/20.1 #75: corrective known, write-flow blocker; untouched.
- F3/18.2 residual provider/payment scenarios: external/business-policy evidence remains open.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-052`: ASSIGNED — one authorized replacement PR from existing exact-base #77 branch; CI-FALLBACK NONE.
- `NIGHT-WOZ-051`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-050`: BLOCKED / REOPEN_UNAVAILABLE.
- `NIGHT-WOZ-048`: DONE / INTEGRATED — #73.
