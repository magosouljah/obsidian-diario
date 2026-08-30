# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-046`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — parameterized capacity/load harness software slice`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `PREDECESSOR: NIGHT-WOZ-045 DONE/AUDIT_ONLY; produced a literal gap map and left 20.2 open.`
- `HOLD_PR: #75 @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f — WRITE_TOOL_SAFETY / DO NOT RETRY`
- `HOLD_PR_2: #73 @ fc831172c4c86d97cadb03801a6777777fd345bb — MERGE_FLOW_UNAVAILABLE / DO NOT TOUCH`

### PRIMARY

1. Preflight live integration + duplicate-check. Confirm #73/#75 remain untouched holding candidates.
2. Build the **minimum reusable software harness** needed for future F3/20.2 proof, without selecting or inventing an approved expected peak.
3. The harness must be parameterized by an explicit target supplied at execution time and must refuse to claim/pass the 2× requirement when the approved target is absent.
4. Measure/report at least: attempted concurrency/operations, latency distribution or p50/p95/p99 where meaningful, error count/rate, queue depth/wait or explicit lack of durable queue, and recovery timing for the exercised synthetic/control path.
5. Reuse existing admission-control/per-bot ceiling behavior; do not redesign product/provider transport. No production/provider load, costs, secrets, bot creation or infrastructure changes in this assignment.
6. Keep scope isolated from #75 observability files and #73 billing reconciliation. Prefer new harness/test/workflow files and only touch existing direct-transport code if absolutely required by a literal testability gap; STOP instead of broad product changes.
7. Run focused deterministic tests + fresh exact-head CI for the new harness candidate. This can prove harness correctness only, **not** capacity PASS.
8. Do not mark 20.2 `[x]`; runtime 2× approved-peak execution remains external/future evidence.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live baseline; branch/head/PR if created; changed-file list proving independence from #73/#75; focused harness tests; fresh exact-head CI; explicit distinction `HARNESS_READY` vs `RUNTIME_CAPACITY_UNVERIFIED`.  
**STOP:** expected peak would need invention, provider/infra/load operation required, overlap with #73/#75, broad direct-transport redesign, costly load, secrets/costs or non-attributable CI failure.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-045

- `STATUS: DONE / AUDIT_ONLY / 20.2 REMAINS OPEN`.
- baseline `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; no branch/PR/code/infra mutation.
- Gap map accepted:
  - capacity envelope `PARTIAL`;
  - approved expected peak `GAP / prerequisite missing`;
  - load/stress harness `GAP`;
  - literal 2× proof `PENDING_EXTERNAL`;
  - latency `GAP`;
  - errors/queue/recovery `PARTIAL`;
  - admission control + per-bot ceiling `EXISTS (software)`;
  - safety margin `GAP`;
  - durable user waitlist `GAP`.
- Existing ceiling/fairness software is not capacity proof. No load test was executed and no number was invented.
- Recommendation consumed by JOBS: split work into approved target, software harness, then controlled runtime proof. 046 owns only the software-harness slice.

## HOLDING

- F3/20.1 #75: exact pin corrective known, but previous write flow blocked; no retry under 046.
- F3/18.2 #73: exact-head green/mergeable but prior merge flow unavailable; untouched under 046.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-046`: ASSIGNED — F3/20.2 parameterized capacity/load harness; no PASS claim.
- `NIGHT-WOZ-045`: DONE/AUDIT_ONLY — 20.2 gap map.
- `NIGHT-WOZ-044`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-043`: BLOCKED/WRITE_TOOL_SAFETY — #75 unchanged.
- `NIGHT-WOZ-040`: BLOCKED/MERGE_FLOW_UNAVAILABLE — #73 green/race-clean, not merged.
- `NIGHT-WOZ-037`: DONE/INTEGRATED — #68 merge `a9d35a3d...`.
