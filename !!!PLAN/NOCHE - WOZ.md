# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-073`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.1 — SAME #76 legal candidate reconciliation + canonical in-app wiring`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`
- `PRIMARY_PR: #76 @ 36d218609cf2488997755312fa2dafd0a019d070`
- `PREDECESSOR: NIGHT-WOZ-072 had no final RESULTADO DEL TURNO or new Issue #41 handoff visible before CYCLE 074; superseded by JOBS.`
- `SERIALIZATION: WOZ MUST NOT merge #76 this cycle. BBB alone owns the possible integration mutation (#79).`

### PRIMARY

1. Fresh preflight live integration + duplicate-check #76; reuse SAME PR/branch only.
2. History-preserving reconcile #76 onto live `957f97771b7a15554cf6e002fe9eb215c71a65cc` if conflict-free; keep scope F3/19.1 only.
3. Reuse owner-approved Privacy/Terms documents and public routes already in #76; do not rewrite approved policy.
4. Close only the literal internal software gap: replace temporary/placeholder Settings Privacy/Terms surfaces with canonical source linkage/content while preserving one source of truth where practical.
5. Account for #82 deploy/config artifacts only for route tests/baseline conflicts; do not mutate deployment/infra lane.
6. Add/adjust focused tests for public routes + in-app legal consistency and direct SPA route contract where testable without provider/runtime claims.
7. Obtain fresh applicable exact-head CI on final refreshed head. **NO MERGE.** Hand off exact-head candidate.
8. Maximum claim: refreshed software/legal candidate ready. DNS/TLS/actual hosting, counsel review, provider/business evidence remain UNVERIFIED unless directly demonstrated.
9. Do not touch #79/#81, 20.2 capacity, signing/notarization or provider resources.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; changed paths; canonical source consistency; focused tests; fresh applicable exact-head CI; explicit external tails.  
**STOP:** legal ambiguity; conflict/scope drift; baseline race; history-preserving reconcile unavailable; product CI red/pending; provider/deployment mutation required; overlap.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent secondary write/audit currently beats the risk of duplicate work. Remain on PRIMARY wait and recheck exact status before closing.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-072`: NO_RESULT before CYCLE 074; superseded by JOBS after fresh duplicate-check; #76 unchanged/open/stale.
- `NIGHT-WOZ-071`: no final result before prior baseline move; superseded.
- `NIGHT-WOZ-070`: `DONE / INTEGRATED`; PR #75 merged as `5e117d69dba852d544cc1fee805eff55ffa820eb`; F3/20.1 software observability integrated, external tails remain UNVERIFIED.
- Older results remain historical in Issue #41 and git history.
