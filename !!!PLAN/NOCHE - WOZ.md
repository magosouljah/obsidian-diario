# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — operación/capacidad.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-051`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — explicit replacement PR authorization from refreshed #77 branch`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `SOURCE_ARTIFACT: CLOSED/UNMERGED #77; refreshed branch woz/night-20.2-capacity-harness @ 50aac3f0c700a88e1f058372c23ee1d96ecf247a`
- `PREDECESSOR: NIGHT-WOZ-050 BLOCKED / REOPEN_UNAVAILABLE after GitHub 422; processed by JOBS CYCLE 052.`
- `FACTUAL_STATE: compare live integration→50aac3f0 is AHEAD by 2, BEHIND by 0; exact merge-base is a306e3b3... and delta is exactly two added harness/test files (+139/-0).`
- `HOLD_PR: #75 @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f — frozen / DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + refreshed branch `50aac3f0...` + duplicate-check. STOP if baseline or branch changed materially after assignment.
2. JOBS explicitly authorizes creating **one replacement PR only** from existing refreshed branch `woz/night-20.2-capacity-harness` because SAME #77 cannot be reopened. Do not create another branch or another duplicate artifact.
3. Before opening replacement PR, verify compare remains exactly two intended files: `cloud-server/tests/capacity-load-harness.cjs` and `cloud-server/tests/capacity-load-harness.test.cjs`, with no unrelated delta.
4. Preserve explicit target requirement and synthetic/local-only limitation. No invented expected peak, safety margin, provider load, 2× proof or capacity PASS.
5. Open replacement PR against live `integration-v0.8.0-alpha.1`; document that #77 is CLOSED/unmerged and this PR is the authorized continuation, not a second implementation.
6. Run focused deterministic tests + fresh applicable exact-head CI on the replacement PR head.
7. Maximum positive result before external/runtime evidence: `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
8. Merge only if exact-head green, race-clean, narrow delta unchanged and owner flow permits. Even if merged, global 20.2 remains open for approved target + real 2× runtime proof + safety margin/waitlist evidence.
9. Do not touch #75, #76, #72/#74/#71, #69/#70 or provider resources.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; source branch head; compare proving 2 files/ahead2/behind0; replacement PR number/head/base; focused tests; fresh exact-head CI; merge SHA only if actually merged; explicit `RUNTIME_CAPACITY_UNVERIFIED`.  
**STOP:** branch scope drift, duplicate replacement PR already exists, target invention required, provider/infra/load operation required, fresh non-attributable red, another owner changes branch, or broad transport redesign.

### CI-FALLBACK

`NONE`.

**Alcance:** none preauthorized.  
**Evidencia requerida:** n/a.  
**STOP:** if PRIMARY waits CI/review/merge, do not invent secondary work; only recheck PRIMARY and report status.

## RESULTADO PROCESADO — NIGHT-WOZ-050

- `STATUS: BLOCKED / REOPEN_UNAVAILABLE`.
- #77 remained CLOSED/unmerged; GitHub returned 422 on reopen because branch was force-pushed/recreated.
- SAME branch was reconciled cleanly onto live base and now points to `50aac3f0c700a88e1f058372c23ee1d96ecf247a`.
- Fresh compare from live integration: `ahead_by=2`, `behind_by=0`, merge-base exactly `a306e3b3...`, two intended files only (+139/-0).
- Focused tests/CI were not run after STOP; runtime capacity remains unverified.
- JOBS CYCLE 052 accepts only the refreshed branch artifact and explicitly authorizes one replacement PR; no 20.2 PASS claim.

## RESULTADO PROCESADO — NIGHT-WOZ-048

- `STATUS: DONE / INTEGRATED`.
- #73 exact head `fc831172c4c86d97cadb03801a6777777fd345bb`; merge/post-merge integration `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- Accepted result: reconciliation/exception-queue software slice integrated; full 18.2 remains open.
- Issue #41 handoff: `5470883416`.

## HOLDING

- F3/20.1 #75: corrective known, previous write flow blocked; untouched.
- F3/18.2 residual provider/payment scenarios: external/business-policy evidence remains open.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-051`: ASSIGNED — explicit one-time replacement PR authorization from refreshed #77 branch `50aac3f0...`; runtime capacity unverified; CI-FALLBACK NONE.
- `NIGHT-WOZ-050`: BLOCKED/REOPEN_UNAVAILABLE — branch refreshed cleanly; #77 cannot reopen.
- `NIGHT-WOZ-049`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-048`: DONE/INTEGRATED — #73 merged as `a306e3b3...`.
