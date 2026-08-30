# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — operación/capacidad.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-049`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — REUSE CLOSED PR #77 as explicitly authorized PRIMARY`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `REUSE_PR: #77 / woz/night-20.2-capacity-harness @ 204a03fc48d161b6943f7b11bea2bfc16bf54b05 — currently CLOSED/UNMERGED; prior premature execution is NOT accepted evidence.`
- `PREDECESSOR: NIGHT-WOZ-048 DONE/INTEGRATED; #73 merged as a306e3b3f6b4a6cf9d678e325b6e529b5344fffe.`
- `HOLD_PR: #75 @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f — frozen / DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + #77 branch/head + duplicate-check. Confirm #77 remains CLOSED/unmerged and its branch has only the intended capacity harness/test files.
2. REUSE-FIRST: do not create a second harness PR. JOBS now explicitly authorizes #77 as the PRIMARY artifact despite its earlier invalid timing.
3. Inspect the existing #77 delta before mutating. Preserve the guard that requires an explicit target and forbids invented expected peak / 2× PASS claims.
4. Reconcile the SAME #77 branch narrowly onto live integration `a306e3b3...`; reopen SAME #77 only if GitHub allows it and the refreshed delta remains exactly the capacity-harness slice. If reopen is unavailable, leave a structured blocker; do not create #78 automatically.
5. Scope remains harness/software-only: deterministic local synthetic measurement of attempted concurrency/ops, latency p50/p95/p99 where meaningful, queue/wait, errors/rejections and recovery. No provider/production load, secrets, costs or infrastructure.
6. Run focused deterministic tests + fresh applicable exact-head CI on the refreshed head.
7. Maximum positive result is `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`. Do not mark 20.2 PASS and do not invent approved expected peak, safety margin or 2× proof.
8. Merge only if the narrow harness candidate is exact-head green, race-clean, and owner flow authorizes integration. Even if merged, global 20.2 remains open for approved target + real runtime proof.
9. Do not touch #75, #76, #72/#74/#71, #69/#70 or provider resources.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base; #77 closed/unmerged pre-state; changed files; refreshed head/base; focused tests; fresh exact-head CI; merge SHA only if actually merged; explicit `RUNTIME_CAPACITY_UNVERIFIED`.  
**STOP:** branch contains overlap/scope drift, reopen unavailable, target invention required, provider/infra/load operation required, fresh non-attributable red, or broad transport redesign.

### CI-FALLBACK

`NONE`.

Reason: the PRIMARY itself is the smallest independent F3/20.2 software slice. No second safe task is needed while its CI runs; do not invent one.

## RESULTADO PROCESADO — NIGHT-WOZ-048

- `STATUS: DONE / INTEGRATED`.
- Baseline before: `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- SAME #73 exact head: `fc831172c4c86d97cadb03801a6777777fd345bb`.
- Reused exact-head green evidence: F3 18.2 Reconciliation `33320621931`; D7 `33320621893`; D6 `33320621877`; Productive Temp Auth Compile `33320621868`; Test Desktop Portability `33320621865` = SUCCESS; Upgrade `33320621863` SKIPPED/non-applicable.
- Merge SHA / post-merge integration: `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; parents `a9d35a3d...` + `fc831172...`.
- Accepted result: reconciliation/exception-queue software slice integrated.
- NOT accepted as full 18.2 PASS: 3DS/rejection/late payment/renewal/cancel/upgrade/downgrade/refund, grace-period/business policy and productive provider evidence remain open.
- Prior #77 execution under superseded assignment was neutralized: #77 CLOSED, merged=false. It becomes reusable only because JOBS explicitly assigns it now as NIGHT-WOZ-049 PRIMARY.
- Issue #41 handoff: `5470883416`.

## HOLDING

- F3/20.1 #75: corrective known, previous write flow blocked; untouched.
- F3/18.2 residual provider/payment scenarios: external/business-policy evidence remains open after integrated software reconciliation slice.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-049`: ASSIGNED — reuse/refesh/reopen SAME #77 as explicit F3/20.2 harness PRIMARY; CI-FALLBACK NONE.
- `NIGHT-WOZ-048`: DONE/INTEGRATED — #73 merged as `a306e3b3...`; accidental #77 closed unmerged.
- `NIGHT-WOZ-047`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-045`: DONE/AUDIT_ONLY — 20.2 gap map.
