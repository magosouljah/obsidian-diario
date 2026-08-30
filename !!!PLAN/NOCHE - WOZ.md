# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — operación/capacidad.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-050`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — REUSE CLOSED PR #77 as explicitly authorized PRIMARY`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `REUSE_PR: #77 / woz/night-20.2-capacity-harness @ 204a03fc48d161b6943f7b11bea2bfc16bf54b05 — CLOSED/UNMERGED; prior premature execution remains rejected as evidence.`
- `PREDECESSOR: NIGHT-WOZ-049 produced no RESULTADO DEL TURNO / Issue #41 handoff and #77 state/head did not move before JOBS CYCLE 051; SUPERSEDED and MUST NOT execute late.`
- `HOLD_PR: #75 @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f — frozen / DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + #77 branch/head + duplicate-check. Confirm #77 remains CLOSED/unmerged and branch delta remains only the intended capacity harness/test slice.
2. REUSE-FIRST: do not create a second harness PR. JOBS explicitly authorizes SAME #77 as the PRIMARY artifact.
3. Inspect existing #77 delta before mutation. Preserve the guard requiring an explicit target and forbidding invented expected peak / 2× PASS claims.
4. Reconcile SAME #77 branch narrowly onto live integration `a306e3b3...`; reopen SAME #77 only if GitHub allows it and refreshed delta remains exactly this slice. If reopen is unavailable, structured blocker + STOP; do not create #78 automatically.
5. Scope remains harness/software-only: deterministic local synthetic measurement of attempted concurrency/ops, latency p50/p95/p99 where meaningful, queue/wait, errors/rejections and recovery. No provider/production load, secrets, costs or infrastructure.
6. Run focused deterministic tests + fresh applicable exact-head CI on the refreshed head.
7. Maximum positive result: `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`. Do not mark 20.2 PASS and do not invent approved expected peak, safety margin or 2× proof.
8. Merge only if narrow candidate is exact-head green, race-clean, and owner flow authorizes integration. Even if merged, global 20.2 remains open for approved target + real runtime proof.
9. Do not touch #75, #76, #72/#74/#71, #69/#70 or provider resources.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; #77 closed/unmerged pre-state; changed files; refreshed head/base; focused tests; fresh exact-head CI; merge SHA only if actually merged; explicit `RUNTIME_CAPACITY_UNVERIFIED`.  
**STOP:** branch overlap/scope drift, reopen unavailable, target invention required, provider/infra/load operation required, fresh non-attributable red, another owner changes #77, or broad transport redesign.

### CI-FALLBACK

`NONE`.

**Alcance:** none preauthorized.  
**Evidencia requerida:** n/a.  
**STOP:** if PRIMARY waits CI/review/merge, do not invent secondary work; only recheck PRIMARY and report status.

## RESULTADO PROCESADO — NIGHT-WOZ-049

- `STATUS: NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO or Issue #41 handoff was observable before CYCLE 051.
- GitHub confirms #77 remains CLOSED/unmerged at `204a03fc...`; no refresh/reopen/CI/merge claim was promoted.

## RESULTADO PROCESADO — NIGHT-WOZ-048

- `STATUS: DONE / INTEGRATED`.
- #73 exact head `fc831172c4c86d97cadb03801a6777777fd345bb`; merge/post-merge integration `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- Accepted result: reconciliation/exception-queue software slice integrated; full 18.2 remains open.
- Issue #41 handoff: `5470883416`.

## HOLDING

- F3/20.1 #75: corrective known, previous write flow blocked; untouched.
- F3/18.2 residual provider/payment scenarios: external/business-policy evidence remains open.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-050`: ASSIGNED — reuse/refresh/reopen SAME #77 as F3/20.2 harness PRIMARY; CI-FALLBACK NONE.
- `NIGHT-WOZ-049`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-048`: DONE/INTEGRATED — #73 merged as `a306e3b3...`.
- `NIGHT-WOZ-045`: DONE/AUDIT_ONLY — 20.2 gap map.
