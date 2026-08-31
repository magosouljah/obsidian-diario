# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-071`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.1 — SAME #76 legal baseline reconciliation, canonical in-app wiring and exact-head candidate`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5e117d69dba852d544cc1fee805eff55ffa820eb`
- `PRIMARY_PR: #76 @ 36d218609cf2488997755312fa2dafd0a019d070, currently stale/non-mergeable; reuse only, no duplicate PR.`
- `PREDECESSOR: NIGHT-WOZ-070 = DONE / INTEGRATED; PR #75 merged as 5e117d69... and F3/20.1 software slice is integrated.`
- `RECALCULATION: F3/20.2 is runtime-external; 19.1 has an existing owner-approved legal candidate with a literal internal gap (SettingsPanel temporary/placeholder legal copy), making it the next dependency-safe F3 software slice.`
- `SERIALIZATION: WOZ MUST NOT merge #76 in the same turn unless the final refreshed candidate has fresh exact-head CI and a final race-check. BBB alone owns possible #79 merge.`

### PRIMARY

1. Fresh preflight live integration + duplicate-check #76; reuse SAME PR/branch only.
2. Reconcile #76 history-preservingly onto live `5e117d69...` if conflict-free and keep scope F3/19.1 only.
3. Verify canonical Privacy/Terms documents and public `/privacy` + `/terms` routing already in #76; do not rewrite approved legal policy.
4. Close only the literal internal software gap documented by #76: replace temporary/placeholder in-app Settings Privacy/Terms surfaces with canonical document content/source linkage, preserving one source of truth where practical.
5. Add/adjust focused tests for public routes + in-app legal surface consistency and direct SPA route contract where testable without provider deployment.
6. Obtain fresh applicable exact-head CI on final head. If CI is fully green and integration still exact, perform final race-check and merge #76 using expected-head protection; otherwise stop PENDING with exact blocker.
7. Maximum claim: F3/19.1 software/legal surfaces integrated. Production hosting SPA fallback, public deployment, counsel/provider/business external evidence remain UNVERIFIED unless actually demonstrated.
8. Do not touch #79/#81, 20.2 capacity, Stripe price PR #80/default branch, signing/notarization or provider resources.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; changed paths; canonical source consistency; focused tests; fresh exact-head CI; merge SHA + parents if merged; explicit external tails.  
**STOP:** legal-policy ambiguity, conflict/scope drift, baseline race, CI red/pending, provider/deployment mutation required, or overlap.

### CI-FALLBACK

**F3 / 18.2 READ-ONLY payment-scenario gap map**, only during genuine `WAITING_CI`/review/merge queue.

**Alcance:** live integration only; 3DS, rejection, late payment, renewal, cancel, upgrade, downgrade, refund and grace-period coverage. No writes/provider calls/credentials and no #76 files.  
**Evidencia requerida:** exact baseline + `SOFTWARE_COVERED/PARTIAL/GAP/PENDING_EXTERNAL` with literal contracts/tests and minimum future slices.  
**STOP:** any write/provider mutation, overlap, policy invention, or attempt to close 18.2 from audit alone. Recheck PRIMARY before closing.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-070`: `DONE / INTEGRATED`; PR #75 merged as `5e117d69dba852d544cc1fee805eff55ffa820eb`. F3/20.1 software observability integrated; external observability tails remain UNVERIFIED.
- Older results remain historical in Issue #41 and git history.
