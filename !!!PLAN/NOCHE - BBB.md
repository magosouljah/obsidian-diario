# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F3 / 20.2 — runtime capacity validation.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-057`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — execute applicable 160-concurrent capacity proof using integrated harness`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`
- `RO_DECISION: expected peak 80 simultaneous users; required validation target 160 simultaneous users (2×). This fixes the target only; it is NOT a PASS claim.`
- `PREDECESSOR: NIGHT-BBB-056 had no final RESULTADO DEL TURNO, Issue #41 handoff or #79 head change before JOBS CYCLE 062; SUPERSEDED and MUST NOT execute late.`
- `RECALCULATION: moved from #79 because the new RO capacity target removes the largest decision blocker in F3/20.2 and enables higher-value evidence work now.`
- `SERIALIZATION: BBB MUST NOT merge or move integration in CYCLE 062.`

### PRIMARY

1. Preflight live integration and inspect the already integrated PR #78 capacity harness; duplicate-check before creating anything.
2. Use the canonical target **80 expected / 160 validation**. Do not substitute arbitrary concurrency.
3. Run the existing harness only in a runtime/environment that is materially applicable to the 20.2 gate. If only synthetic/local evidence is available, run it only as diagnostic and label it non-authoritative.
4. Capture literal evidence for 160 concurrent users covering latency, error rate, queue/admission behavior, recovery behavior and any cross-tenant/data-loss safety signals the harness/runtime can actually observe.
5. Determine factual safety margin relative to the approved 80-user expected peak from measured results; do not invent one.
6. Separately verify whether durable user waitlist behavior exists. Existing fairness/bot-ordering state is not sufficient.
7. No product redesign, provider provisioning, paid infra expansion, secrets, #75 files, or unrelated F4 changes.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Maximum claim:** runtime capacity evidence at 160 only if actually demonstrated; otherwise `RUNTIME_CAPACITY_UNVERIFIED` with exact blocker. Full 20.2 cannot close unless latency/error/queue/recovery, safety margin and durable waitlist requirements are all evidenced.  
**Required evidence:** exact baseline; exact command/runtime/environment metadata safe to disclose; 80/160 parameters; measured latency/error/queue/recovery; safety observations; durable waitlist status; explicit UNVERIFIED.  
**STOP:** applicable runtime unavailable, unsafe/cost-generating operation required, test would mutate production/provider state, overlap, missing isolation guarantees, or evidence cannot be attributed to the 160 target.

### CI-FALLBACK

**F4 / 25.2 SAME #79 narrow refresh + fresh exact-head CI**, only if PRIMARY is genuinely `WAITING_EXTERNAL`/`WAITING_RUNTIME` after all safe diagnostics are exhausted.

**Alcance:** preserve exactly `docs/beta/0.9.0-beta.1-readiness.md`; history-preserving refresh of #79 onto live integration; verify one-file docs-only delta; fresh exact-head CI. **NO MERGE**.  
**Evidencia requerida:** live base; exact refreshed head; one-file delta; fresh exact-head CI; explicit real beta/tester/signing gaps.  
**STOP:** any product/signing/provider change, scope drift, conflict, baseline race, overlap, or attempt to close 25.2 from the document alone. Recheck PRIMARY before closing.

## RESULTADOS PROCESADOS

- `NIGHT-BBB-056`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 062.
- `NIGHT-BBB-049`: #79 artifact exists; historical CI stale for merge authorization.

## HISTORIAL COMPACTO

- `NIGHT-BBB-057`: ASSIGNED — F3/20.2 80 expected / 160 validation runtime proof; #79 refresh as conditional fallback only.
- `NIGHT-BBB-056`: NO_RESULT / SUPERSEDED_BY_JOBS.
