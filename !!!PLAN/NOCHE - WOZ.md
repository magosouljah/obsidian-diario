# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-018`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 17.2 — webhook integrity/idempotency/retry software contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`
- `PREDECESSOR: NIGHT-WOZ-017 DONE; PR #65 merged as ed6aab7e...; 17.1 SOFTWARE DONE / INTEGRATED.`

### Orden JOBS

1. Preflight factual contra GitHub vivo, Plan Maestro, F3, Registro, roles, protocolo, este ledger e Issue #41. GitHub manda.
2. REUSE-FIRST: busca primitives existentes de billing/webhook, raw-body capture, PostgreSQL repositories/idempotency/queue/retry. No abras duplicados si existe lineage útil.
3. Implementa un único slice software-only de **17.2 webhook integrity + durable dedupe/retry contract**: verificación de firma sobre raw body antes de parse/mutate; event ID durable/idempotente; duplicados y reordenamiento seguros; failure/retry state explícito; eventos no soportados fail-closed/no-op seguro.
4. La UI/redirect de Checkout NUNCA concede entitlement. Este slice no puede promover plan por success URL; cualquier entitlement queda server-side y reconciliable.
5. Pruebas mínimas: firma válida/inválida; body mutado; duplicate same event ID; out-of-order; handler failure + retry; timeout/error; unsupported event; atomicity/idempotency bajo concurrencia donde aplique.
6. Si necesita persistencia, reutiliza PostgreSQL durable ya autoritativo; no JSON authority. No crear RDS/Stripe resources, cuentas, secrets, endpoints públicos ni costo.
7. Candidate pequeño, branch/PR único, exact-head CI. Si integration cambia, refresh SAME lineage + fresh applicable CI antes de merge.
8. Merge solo con evidence + exact-head green + race-check. Reclama únicamente `17.2 SOFTWARE DONE / INTEGRATED`; no Stripe productivo, no entitlements 18.x, no staging físico.
9. OUT OF SCOPE: 18.1/18.2, F2/F4, provider credentials/resources, DNS/legal, physical staging/prod.
10. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO MÁS RECIENTE — NIGHT-WOZ-017

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-017`  
`TURN_STATUS: DONE`  
`GATE: F3/17.1 SOFTWARE DONE / INTEGRATED`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`  
`BRANCH/CANDIDATE_HEAD: woz/night-17.1-checkout-contract @ e65538640581f3f986748968db1f4dfb069c2579`  
`PR: #65 CLOSED / MERGED -> ed6aab7e964686cdb5fb1b84eac0198ca67f8892`  
`CHANGES: no new product code in this assignment; REUSE-FIRST consumed SAME #65 and executed final race-check + expected-head merge.`  
`TESTS: reused exact-head focal 17.1 deterministic tests already green; no rerun ceremonial.`  
`CI: F3 17.1 33276769749 SUCCESS; Desktop Portability 33276769684 SUCCESS; D6 33276769695 SUCCESS; D7 33276769698 SUCCESS; temp-auth 33276769702 SUCCESS; Upgrade 33276769715 SKIPPED/no aplicable.`  
`EVIDENCE_NEW: protected expected-head merge succeeded; merge SHA ed6aab7e964686cdb5fb1b84eac0198ca67f8892; parents b114111caf... + e655386405...; integration reread points to ed6aab7e...`  
`UNVERIFIED: Stripe account/provider credentials reales; productos/precios comerciales reales; tax/trial/currency commercial decisions; real Checkout against Stripe; webhooks/17.2; entitlement reconciliation; physical staging/prod.`  
`BLOCKERS: none para 17.1 software slice; external/productive Stripe and 17.2 remain separate.`

## HISTORIAL

- `NIGHT-WOZ-018`: ASSIGNED — F3/17.2 webhook integrity/idempotency/retry software-only.
- `NIGHT-WOZ-017`: DONE — SAME #65 merged `ed6aab7e...`; 17.1 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-016`: SUPERSEDED_BY_JOBS before worker execution.
- `NIGHT-WOZ-015`: PENDING_CI — #65 repaired at `e6553864...`; CI later green.
- `NIGHT-WOZ-014`: DONE — #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-013`: PENDING_CI — refreshed `d254b294...`; CI later green.
- `NIGHT-WOZ-012`: PENDING_CI_REFRESH.
- `NIGHT-WOZ-011`: PENDING — #61 refreshed.
- `NIGHT-WOZ-010`: PENDING — #61 candidate software 16.2.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation external.
- `NIGHT-WOZ-008`: PENDING_CI.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL.
- `NIGHT-WOZ-006`: PENDING — #56 integrated `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
