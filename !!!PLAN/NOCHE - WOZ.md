# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-029`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — SAME PR #70: PostgreSQL Required CI attribution/corrective + integrate only if green`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #70 / woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`
- `PREDECESSOR: NIGHT-WOZ-028 had no RESULTADO DEL TURNO observable at JOBS CYCLE 030; superseded to preserve monotonic execution.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen; do NOT touch/retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; reutiliza SAME #70, no rama/PR alterno.
2. Reuse focused F2/13.1 evidence: `F2 - 13.1 Orphan Lifecycle` run `33304798320` = SUCCESS on exact head `5a99ebf2...`.
3. Required CI `33304798363` remains FAILURE on the same head. The visible failing job is `PostgreSQL live integration + recovery gate`, step `Execute migrations and adversarial persistence checks on PostgreSQL`.
4. Attribution-first: inspect/reproduce that exact gate and determine whether #70's 4-file server delta caused the failure. #70 changes only `.github/workflows/f2-13.1-orphan-lifecycle.yml`, `cloud-server/garbage-reconciliation-worker.js`, `cloud-server/orphan-upload-lifecycle.js`, and `cloud-server/tests/orphan-upload-lifecycle.test.cjs`; no migration file changed.
5. A recent Required CI on unrelated F4 PR #63 against the same integration baseline had its PostgreSQL live/recovery job SUCCESS, so do not assume provider-wide failure. Use logs/repro to classify candidate-specific vs transient/non-attributable.
6. If attributable, correct only the minimum server-half cause in SAME #70 and require focused orphan tests/workflow + Required CI fresh exact-head. Preserve persistence/idempotency/retry/fail-closed and protection of committed/valid uploads.
7. If non-attributable/transient, do not mutate product to appease CI; document concrete evidence and STOP/PENDING. Do not ceremonial-rerun unless the failure classification justifies it.
8. If everything applicable becomes green and integration remains compatible, race-check + merge SAME #70; verify merge SHA + integration HEAD. Do not close 13.1 complete because AAA/#69 owns Web wiring.
9. No frontend AAA/#69, billing/F3, #68, Desktop, provider resources or infrastructure.
10. Report RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** exact failure attribution, logs/repro, 4-file scope confirmation, focused tests, fresh exact-head CI if head changes/justified rerun, race-check, merge SHA if integrated, explicit UNVERIFIED.  
**STOP:** failure non-attributable/transient without justified corrective, need to touch frontend/billing/infra/#68, baseline race, insufficient evidence.

### CI-FALLBACK

`NONE`

Reason: #68 is externally merge-blocked/frozen and other pieces would expand ownership; no independent fallback is safe.

## RESULTADO PROCESADO — NIGHT-WOZ-027 / STATE CARRIED THROUGH 028

- `PR #70`: OPEN/Ready/mergeable, base `3ad8f55a...`, head `5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`.
- Focused F2/13.1 workflow `33304798320` = SUCCESS.
- Required CI `33304798363` = FAILURE; PostgreSQL live/recovery gate failed before any PASS claim.
- `NIGHT-WOZ-028`: no new result/handoff observable at CYCLE 030; no GitHub head movement on #70.
- Changed-file scope remains exactly four server/F2 files; no migration file.

## HOLDING — F3/18.1 / PR #68

#68 @ `2a988ec2a25d6ecfa927614fcc32cde689995103` remains a frozen exact-head-green candidate with prior merge execution blocked by the connector/safety execution layer. Do not recreate/retry during 029.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-029`: ASSIGNED — SAME #70 PG failure attribution/corrective + integration only if green; fallback NONE.
- `NIGHT-WOZ-028`: no result observable at CYCLE 030; superseded.
- `NIGHT-WOZ-027`: PENDING/WAITING_CI -> focused F2 workflow SUCCESS; Required CI PostgreSQL gate FAILURE.
- `NIGHT-WOZ-025`: BLOCKED / MERGE_TOOL_REJECTED — #68 unchanged.
- `NIGHT-WOZ-023`: #68 exact-head green candidate.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — #67 merged `3ad8f55a...`.
