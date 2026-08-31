# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-074`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — durable user waitlist minimal internal slice`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`
- `PREDECESSOR: NIGHT-WOZ-073 produced no RESULTADO DEL TURNO or new Issue #41 handoff before this JOBS cycle and is superseded after critical-path recalculation, not PASS.`
- `DUPLICATE_CHECK: #78 capacity harness is already integrated; Issue #41 continues to record durable user waitlist as GAP; no separate waitlist implementation was found by current repo search.`
- `SERIALIZATION: WOZ MUST NOT merge or mutate integration this cycle. BBB/#79 alone owns the possible integration mutation.`

### PRIMARY

**F3 / 20.2 — implement only the missing durable user-waitlist control-plane slice.**

1. Fresh preflight live integration + Issue #41 + #78 artifacts + duplicate-check. REUSE-FIRST: preserve existing admission control/per-bot ceiling and harness; do not rebuild them.
2. Identify the smallest durable control-plane representation needed for users who cannot receive transport capacity immediately. It must survive process restart and be tenant/user scoped without leaking credentials or media payloads.
3. Implement only queue persistence + minimal enqueue/dequeue/claim/recovery semantics needed to make the waitlist durable and safe. No UI redesign, no provider capacity increase, no billing, no runtime load claim.
4. Keep behavior fail-closed on corrupt/ambiguous state and compatible with the existing 80 expected / 160 validation capacity contract.
5. Add focused tests proving persistence/restart recovery, ordering/duplicate handling as applicable, tenant isolation and no secret/media persistence in the waitlist record.
6. Run focused tests and fresh applicable exact-head CI on the candidate. **NO MERGE.** Hand off exact base/head/paths/tests/CI.
7. Maximum claim: durable-waitlist software slice ready. **Do not claim F3/20.2 PASS**: real 160-concurrent runtime, latency/error/queue/recovery measurement and safety margin remain separate evidence.
8. Do not touch #79/#81/#76, F2/13.2, payment provider scenarios, signing/notarization or infrastructure/provider resources.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact live base; duplicate-check; changed paths; persistence schema/format or reuse rationale; focused persistence/restart/isolation tests; fresh exact-head CI; explicit remaining 160-runtime gaps.  
**STOP:** an existing equivalent durable waitlist is found; required change overlaps active #79 or frozen owned work; persistence authority is ambiguous; scope expands into provider/runtime/infra; baseline race; product CI red; safe minimal slice cannot be isolated.

### CI-FALLBACK

**F3 / 18.2 READ-ONLY billing-scenario evidence gap map**, only if PRIMARY becomes code-complete and genuinely `WAITING_CI`/review.

**Alcance:** live integration and existing tests/docs only; map literal evidence for 3DS, rejection, late payment, renewal, cancel, upgrade, downgrade, refund and grace periods. No provider calls, no writes, no payment mutations.  
**Evidencia requerida:** exact baseline; scenario → existing code/test/provider-proof mapping; `PASS_SOFTWARE / GAP_PROVIDER / GAP_TEST / UNVERIFIED`; smallest independent next evidence action.  
**STOP:** any write/provider call; overlap with waitlist paths; attempt to close 18.2 without provider evidence; PRIMARY leaves waiting state. Recheck PRIMARY before closing.

## RESULTADO DEL TURNO — NIGHT-WOZ-074

### PRIMARY

- `Assignment ID:` NIGHT-WOZ-074
- `STATUS:` WAITING_CI
- `baseline:` integration-v0.8.0-alpha.1 @ `957f97771b7a15554cf6e002fe9eb215c71a65cc` (fresh preflight matched assignment baseline).
- `branch/head:` `woz/night-074-durable-waitlist` @ `52b58f56d66430db1ecdce9f572680c61d5d9fe3`.
- `PR:` #83 draft/open; NO MERGE.
- `cambios:` added `cloud-server/durable-user-waitlist.js`, `cloud-server/tests/durable-user-waitlist.test.cjs`, `.github/workflows/f3-20.2-durable-waitlist.yml`. Store is atomic JSON with mode 0600, schema v1 containing only `id`, `tenant_id`, `user_id`, `enqueued_at`, `claimed_at`; idempotent tenant/user enqueue, FIFO tenant claim, stale-claim recovery, tenant-scoped dequeue, strict corrupt/unknown-field fail-closed parsing. Existing #78 capacity harness and transport logic were not rebuilt.
- `tests:` focused exact-head test executed by workflow and PASS; covers persistence across re-instantiation/restart, FIFO order, duplicate suppression, tenant isolation, cross-tenant dequeue denial, stale-claim recovery, no token/secret/media/payload/storageChatId persistence, corrupt JSON and forbidden-field fail-closed.
- `CI:` dedicated `F3 20.2 Durable Waitlist` run `33374728945` on exact head = SUCCESS. PR-wide checks/Required CI were still external/in-progress at the one allowed final recheck; PRIMARY therefore remains WAITING_CI.
- `evidencia:` PR #83 exact base/head; workflow run `33374728945`; Issue #41 handoff `5476019571`. Duplicate-check found historical #26 in-memory bounded waitlist but no equivalent durable user waitlist on live tree; #79 is F4/25.2 docs-only and does not overlap changed paths.
- `UNVERIFIED:` real 160-concurrent runtime; latency/error/queue/recovery measurements; safety margin; production/admission runtime wiring of this isolated store; completion of full PR Required CI.
- `blockers:` external PR CI only for this turn; serialization explicitly forbids WOZ integration mutation this cycle.
- `condición de STOP alcanzada:` PRIMARY code-complete entered verifiable WAITING_CI; after independent fallback, one factual recheck still showed PR-wide checks in progress. No merge attempted.
- `recomendación para JOBS:` keep #83 unmerged until exact-head required CI is green; then explicitly assign the integration/runtime-wiring decision. Do not mark F3/20.2 PASS until real 160-concurrent runtime/latency/error/queue/recovery/safety-margin evidence exists.

### CI-FALLBACK

- `Assignment ID:` NIGHT-WOZ-074 / CI-FALLBACK
- `STATUS:` DONE_READ_ONLY
- `baseline:` integration-v0.8.0-alpha.1 @ `957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- `branch/head:` none; read-only against live baseline.
- `PR:` none.
- `cambios:` none.
- `tests:` no tests executed; inspected existing billing checkout/reconciliation tests only.
- `CI:` N/A read-only.
- `evidencia:` existing software proves server-owned checkout metadata/idempotency/fail-closed provider errors plus reconciliation match/divergence/replay/ambiguous/provider-failure behavior. Scenario map: `3DS = GAP_PROVIDER/GAP_TEST`; `rejection = GAP_PROVIDER` (software provider-error fail-closed exists, no provider scenario proof); `late payment = GAP_PROVIDER/GAP_TEST`; `renewal = GAP_PROVIDER/GAP_TEST`; `cancel = GAP_PROVIDER/GAP_TEST`; `upgrade = GAP_PROVIDER/GAP_TEST`; `downgrade = GAP_PROVIDER/GAP_TEST`; `refund = GAP_PROVIDER/GAP_TEST`; `grace periods = GAP_PROVIDER/GAP_TEST`.
- `UNVERIFIED:` all nine real provider scenario outcomes; no provider calls were made.
- `blockers:` provider/sandbox evidence absent by design; fallback authority was READ-ONLY.
- `condición de STOP alcanzada:` completed literal evidence-gap map without writes/provider calls and did not claim 18.2 closure; returned to PRIMARY and rechecked once.
- `recomendación para JOBS:` smallest independent next evidence action for 18.2 is an isolated provider sandbox scenario matrix/evidence run when explicitly assigned; software tests alone must not be promoted to provider PASS.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-074`: WAITING_CI / PR #83 exact head `52b58f56d66430db1ecdce9f572680c61d5d9fe3`; dedicated CI PASS, full PR CI pending; fallback 18.2 gap map DONE_READ_ONLY.
- `NIGHT-WOZ-073`: NO_RESULT before this cycle; superseded by JOBS074 after fresh critical-path recalculation, not PASS.
- `NIGHT-WOZ-072`: NO_RESULT; superseded historically.
- `NIGHT-WOZ-070`: DONE / INTEGRATED; PR #75 merged as `5e117d69dba852d544cc1fee805eff55ffa820eb`; F3/20.1 software observability integrated; external tails remain UNVERIFIED.
- Older results remain historical in Issue #41 and git history.
