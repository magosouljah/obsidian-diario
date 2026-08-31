# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F3 / 20.2 — runtime capacity validation.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-065`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — applicable 160-concurrent capacity proof using integrated harness`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`
- `RO_DECISION: expected peak 80 simultaneous users; required validation target 160 simultaneous users (2×). Target selection is NOT PASS.`
- `PREDECESSOR: NIGHT-BBB-064 had no final RESULTADO DEL TURNO, Issue #41 handoff, runtime evidence or attributable artifact before JOBS CYCLE 070; SUPERSEDED and MUST NOT execute late.`
- `RECALCULATION: selected from zero because 80/160 remains fixed and applicable runtime capacity evidence is still a direct F0-F4 closure blocker.`
- `SERIALIZATION: BBB MUST NOT merge or move integration in CYCLE 070.`

### PRIMARY

1. Preflight live integration and reuse the already integrated PR #78 capacity harness; duplicate-check first.
2. Use exactly **80 expected / 160 validation**. Do not substitute arbitrary concurrency.
3. Run the existing harness only in a runtime/environment materially applicable to 20.2. Synthetic/local evidence may be diagnostic only and is non-authoritative for PASS.
4. Capture literal evidence at 160 for latency, error rate, queue/admission behavior, recovery behavior and cross-tenant/data-loss safety signals actually observable.
5. Determine factual safety margin against the approved 80-user expected peak from measured results.
6. Separately verify durable user waitlist behavior; fairness/bot-ordering state alone is insufficient.
7. No product redesign, provider provisioning, paid infra expansion, secrets, #75 files or unrelated F4 changes.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Maximum claim:** runtime capacity evidence at 160 only if actually demonstrated; otherwise `RUNTIME_CAPACITY_UNVERIFIED` with exact blocker. Full 20.2 cannot close unless latency/error/queue/recovery, safety margin and durable waitlist are evidenced.  
**Required evidence:** exact baseline; exact command/runtime/environment metadata safe to disclose; 80/160 parameters; measured latency/error/queue/recovery; safety observations; durable waitlist status; explicit UNVERIFIED.  
**STOP:** applicable runtime unavailable, unsafe/cost-generating operation required, test would mutate production/provider state, overlap, missing isolation guarantees, or evidence cannot be attributed to 160.

### CI-FALLBACK

**F4 / 25.2 SAME #79 narrow refresh + fresh exact-head CI**, only if PRIMARY is genuinely `WAITING_EXTERNAL`/`WAITING_RUNTIME` after all safe diagnostics are exhausted.

**Alcance:** preserve exactly `docs/beta/0.9.0-beta.1-readiness.md`; history-preserving refresh of #79 onto live integration; verify one-file docs-only delta; fresh exact-head CI. **NO MERGE**.  
**Evidencia requerida:** live base; exact refreshed head; one-file delta; fresh exact-head CI; explicit real beta/tester/signing gaps.  
**STOP:** any product/signing/provider change, scope drift, conflict, baseline race, overlap, or attempt to close 25.2 from the document alone. Recheck PRIMARY before closing.

## RESULTADOS PROCESADOS

- `NIGHT-BBB-064`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 070.
- `NIGHT-BBB-063`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 069.
- `NIGHT-BBB-049`: #79 docs-only artifact exists; historical CI does not authorize integration on current baseline.
