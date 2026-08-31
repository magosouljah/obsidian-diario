# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-072`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.1 — SAME #76 legal candidate reconciliation + canonical in-app wiring`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`
- `PRIMARY_PR: #76 @ 36d218609cf2488997755312fa2dafd0a019d070; stale vs live baseline.`
- `PREDECESSOR: NIGHT-WOZ-071 had no final RESULTADO DEL TURNO before this JOBS cycle and is superseded because owner PR #82 moved integration.`
- `BASELINE_EVENT: PR #82 merged after WOZ071 assignment. It adds Web production-deploy tooling/config and moved integration to 957f9777...; do not assume deployment/runtime proof beyond GitHub artifacts.`
- `SERIALIZATION: WOZ MUST NOT merge #76 this cycle. BBB alone owns the single possible integration mutation (#79).`

### PRIMARY

1. Fresh preflight live integration + duplicate-check #76; reuse SAME PR/branch only.
2. Reconcile #76 history-preservingly onto live `957f9777...` if conflict-free; keep scope F3/19.1 only.
3. Reuse owner-approved Privacy/Terms documents and public routes already in #76; do not rewrite approved policy.
4. Close only the literal internal software gap: replace temporary/placeholder Settings Privacy/Terms surfaces with canonical source linkage/content while preserving one source of truth where practical.
5. Account for PR #82's deploy/config artifacts only insofar as they affect route tests or baseline conflicts; do not mutate owner deploy/infra lane.
6. Add/adjust focused tests for public routes + in-app legal consistency and direct SPA route contract where testable without provider/runtime claims.
7. Obtain fresh applicable exact-head CI on the final refreshed head. NO MERGE this cycle; hand off a ready exact-head candidate for the next serialized integration cycle.
8. Maximum claim: refreshed software/legal candidate ready with evidence. Production DNS/TLS/actual hosting, counsel review, provider/business evidence remain UNVERIFIED unless directly demonstrated.
9. Do not touch #79/#81, 20.2 capacity, signing/notarization or provider resources.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; changed paths; canonical source consistency; focused tests; fresh exact-head CI; explicit external tails.  
**STOP:** legal-policy ambiguity; conflict/scope drift; baseline race; history-preserving reconciliation unavailable; CI red/pending for product cause; provider/deployment mutation required; overlap.

### CI-FALLBACK

`CI-FALLBACK: NONE` — previous 18.2 read-only scenario auditing is already substantially mapped and repeating it would risk duplicate work. Remain on PRIMARY wait and recheck exact status before closing.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-071`: no final result observed before JOBS reassignment; superseded due live baseline move by owner PR #82.
- `NIGHT-WOZ-070`: `DONE / INTEGRATED`; PR #75 merged as `5e117d69dba852d544cc1fee805eff55ffa820eb`; F3/20.1 software observability integrated, external observability tails remain UNVERIFIED.
- Older results remain historical in Issue #41 and git history.
