# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-015`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F3 / 17.1 — Stripe Checkout server-side software-only`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`
- `LIVE_BASE_USED: integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`
- `PR: #65 / woz/night-17.1-checkout-contract`

### Orden JOBS

1. Preflight factual completo contra GitHub vivo, Plan Maestro, F3, Registro, roles, protocolo, este ledger e Issue #41.
2. `NIGHT-WOZ-014` está DONE: PR #61 se integró como `55e0d875...`; no tocar ni reabrir 16.2. Mantener `16.2 SOFTWARE DONE / EXTERNAL TAIL` y 16.1 physical separation external.
3. REUSE-FIRST / duplicate-check: la búsqueda visible `stripe checkout idempotency webhook price` no encontró implementación reutilizable en BeatGaler. Repite búsqueda precisa antes de crear artifact para evitar duplicado oculto.
4. Implementa **solo 17.1 software dependency-safe**: modelo estable de productos/precios/trial/currency/tax e IDs internos; creación de Checkout Session server-side; idempotency keys; precios/plan nunca decididos por cliente. Conserva entitlements únicamente server-side y no concedas plan por redirect.
5. No necesitas Stripe real/credenciales para el contrato software. Usa adapter/provider boundary + tests deterministas/mocks si es el camino mínimo. No crear cuenta, producto, price, webhook endpoint productivo ni costo externo.
6. Añade pruebas suficientes para: request válida; price/plan client tampering rechazado; idempotency/retry; unsupported currency/product; provider timeout/error fail-closed; metadata/identity ligadas al usuario correcto. No avanzar 17.2 webhooks salvo que una primitive común mínima sea estrictamente necesaria y quede claramente separada.
7. Candidate en rama/PR única con scope pequeño; exact-head applicable CI. No merge si baseline se mueve sin refresh + fresh CI. Integra solo si el flujo owner autorizado y gates aplicables están verdes.
8. OUT OF SCOPE: Stripe real/provider credentials, 17.2 completo, D18–D20, F2/F4, infraestructura pagada, DNS/legal, physical staging/prod.
9. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO MÁS RECIENTE — NIGHT-WOZ-015

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-015`  
`TURN_STATUS: PENDING_CI`  
`GATE: F3/17.1 SOFTWARE CANDIDATE / NOT INTEGRATED`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`  
`HEAD_AFTER: woz/night-17.1-checkout-contract @ 584b5cf3bcdb21463e577da89825b3cd51fe2704`  
`PR: #65 OPEN / Ready / mergeable=true; base_sha b114111cafb29b4aa50cdce014059c66a75bddf2; NOT MERGED.`  
`CHANGES: added cloud-server/billing-checkout.js, cloud-server/tests/billing-checkout.test.cjs and .github/workflows/f3-17.1-checkout-contract.yml. Reused existing PLAN_CATALOG IDs; stable internal price IDs are server-owned. Commercial provider price/currency/trial/tax remain mandatory server configuration, not invented product defaults. Client-controlled plan/price/currency/trial/tax/metadata is rejected; idempotency key is bound to authenticated user + product + request id; provider failures fail closed; Checkout response explicitly grants no entitlement.`  
`TESTS: deterministic focal suite covers valid request; price/plan/currency/trial/amount tampering; retry/idempotency; identity-bound idempotency; unsupported product/currency; provider timeout/error; authenticated-user metadata/reference binding.`  
`CI: exact-head F3 - 17.1 Checkout Contract run 33276146755 SUCCESS; D6 33276146691 SUCCESS; D7 33276146719 SUCCESS; temp-auth 33276146693 SUCCESS; Upgrade 21.2 run 33276146690 SKIPPED by paths; Test - Desktop Portability / Required CI run 33276146715 still IN_PROGRESS at STOP.`  
`EVIDENCE_REUSED: existing cloud-server/plans.js PLAN_CATALOG for paid_entry/highest_paid identities; no Stripe/Checkout implementation found by precise duplicate-check; 16.2 evidence untouched.`  
`EVIDENCE_NEW: PR #65 exact head 584b5cf3...; focal CI 33276146755 SUCCESS; D6/D7/temp-auth exact-head SUCCESS.`  
`UNVERIFIED: Required CI 33276146715 final conclusion; productive Stripe account/products/prices/credentials; actual currency/trial/tax commercial decisions; real Checkout Session/provider call; webhooks/17.2; entitlement reconciliation; physical staging/prod.`  
`BLOCKERS: only exact-head Required CI 33276146715 still running for this candidate. No product decision was invented; productive billing remains external/RO/provider work.`  
`RECOMMENDATION_TO_JOBS: keep SAME PR #65. If Required CI 33276146715 closes SUCCESS and integration has not moved, issue owner race-check/merge assignment or explicitly allow integration; if baseline moves, refresh SAME #65 and require fresh applicable exact-head CI. Keep 17.2 separate.`  
`TURN_FINISHED_AT: 2026-08-29T15:29-06:00`

## RESULTADO DEL TURNO ANTERIOR — NIGHT-WOZ-014

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-014`  
`TURN_STATUS: DONE`  
`GATE: F3/16.2 SOFTWARE DONE / EXTERNAL TAIL`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`  
`PR: #61 CLOSED / MERGED -> 55e0d8759ec03b23fa8e4f1f35304922dffeb992`  
`CANDIDATE_HEAD: d254b294cf8fe78d93025271360dd73ed594898f`  
`CI: Test - Desktop Portability/Required CI 33271019389 SUCCESS; D6 33271019493 SUCCESS; D7 33271019399 SUCCESS; temp-auth 33271019373 SUCCESS; F4 matrix 33271019370 SUCCESS; Upgrade 21.2 33271019540 SKIPPED by paths.`  
`EVIDENCE: protected merge expected-head; integration reread; parents exactos 7de7b57a... + d254b294...; Issue #41 handoff 5464611743.`  
`UNVERIFIED: physical staging/prod, provider ownership/resources, DNS/TLS productivo, deploy/rollback real, Stripe 17.1.`

## HISTORIAL

- `NIGHT-WOZ-015`: PENDING_CI — PR #65 candidate 17.1 @ `584b5cf3...`; focal/D6/D7/temp-auth green; Required CI running.
- `NIGHT-WOZ-014`: DONE — SAME #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-013`: PENDING_CI — refreshed to `d254b294...`; CI later green.
- `NIGHT-WOZ-012`: PENDING_CI_REFRESH.
- `NIGHT-WOZ-011`: PENDING — #61 refreshed.
- `NIGHT-WOZ-010`: PENDING — #61 candidate software 16.2.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation external.
- `NIGHT-WOZ-008`: PENDING_CI.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrated `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
