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

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-073`: NO_RESULT before this cycle; superseded by JOBS074 after fresh critical-path recalculation, not PASS.
- `NIGHT-WOZ-072`: NO_RESULT; superseded historically.
- `NIGHT-WOZ-070`: DONE / INTEGRATED; PR #75 merged as `5e117d69dba852d544cc1fee805eff55ffa820eb`; F3/20.1 software observability integrated; external tails remain UNVERIFIED.
- Older results remain historical in Issue #41 and git history.
