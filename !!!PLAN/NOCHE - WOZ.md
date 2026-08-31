# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-080`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — #83 history-preserving reconcile + fresh exact-head CI + readiness/integration transaction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRIMARY_PR: #83 @ 52b58f56d66430db1ecdce9f572680c61d5d9fe3; OPEN/DRAFT; stale base 957f97771b7a15554cf6e002fe9eb215c71a65cc; 3-file durable-waitlist scope.`
- `PREDECESSOR: NIGHT-WOZ-079 produced no final RESULTADO DEL TURNO before CYCLE 081; superseded by material integration move, not PASS.`
- `SERIALIZATION: WOZ/#83 is the ONLY integration mutation authorized in CYCLE 081. AAA/BBB may create/update bounded candidates but may not merge integration.`

### PRIMARY

1. Fresh preflight integration + Issue #41 + duplicate-check.
2. Reuse #83; do not recreate durable waitlist.
3. Reconfirm exact changed files and intended scope. Compare stale base `957f9777...` to live `816f946c...` and perform only a history-preserving reconciliation if clean/safe.
4. Preserve the bounded durable user waitlist semantics; no payment/provider/infra/F2/F4 expansion.
5. Run focused waitlist tests and fresh applicable exact-head CI after reconciliation.
6. Attempt Draft→Ready only through an authorized verifiable GitHub path. Do not bypass if tooling still cannot mutate safely.
7. If #83 becomes Ready, exact base/head/scope/CI remain green and integration has not raced, merge through expected-head protection and verify resulting integration SHA + both parents.
8. Maximum claim: `F3/20.2 DURABLE_WAITLIST_INTEGRATED` if merged; runtime 160 capacity evidence remains independently required before closing 20.2.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live baseline; old/new #83 base/head; changed-file list; reconciliation method; focused tests; exact-head CI; Ready state; merge SHA/parents if accepted; explicit runtime-capacity UNVERIFIED.  
**STOP:** unsafe history reconciliation, scope drift, Draft→Ready tooling failure, CI not concluded/green, integration race, expected-head mismatch, or merge rejection.

### CI-FALLBACK

**F3 / 20.2 runtime capacity evidence — READ-ONLY / REUSE #78.** Execute only after PRIMARY has actually entered `WAITING_CI` or another verifiable external wait caused by #83 reconciliation/readiness.

- **Scope:** use already-integrated #78 harness only; no code/infra/provider mutation. Target 80 expected / 160 validation.
- **Required evidence:** environment identity; 160 concurrency proof; latency/error/queue/recovery; no-data-loss/no-cross-tenant; measured safety margin versus 80; explicit applicability limits.
- **STOP:** only local/synthetic environment that cannot satisfy the plan; credentials/provider/infra mutation required; overlap; or PRIMARY wait resolves. Recheck PRIMARY before closing.
- Fallback cannot substitute #83 integration and cannot close 20.2 alone.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-079`: NO_RESULT before CYCLE 081; superseded due integration move, not PASS.
- `NIGHT-WOZ-078`: BLOCKED_STOP; #83 exact/scoped/CI-green on old baseline but Draft→Ready tooling failed before mutation.
