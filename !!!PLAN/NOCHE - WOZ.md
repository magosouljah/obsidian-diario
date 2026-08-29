# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-018`
- `ASSIGNMENT_STATUS: PENDING`
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

## RESULTADO DEL TURNO MÁS RECIENTE — NIGHT-WOZ-018

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-018`  
`TURN_STATUS: PENDING_CI`  
`GATE: F3/17.2 SOFTWARE CANDIDATE / NOT INTEGRATED`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`  
`HEAD_AFTER: woz/night-17.2-webhook-contract @ 22550152e9960c5dad328711b3a8b150301a8c4f`  
`BRANCH/CANDIDATE_HEAD: woz/night-17.2-webhook-contract @ 22550152e9960c5dad328711b3a8b150301a8c4f`  
`PR: #67 OPEN / Ready; base_sha ed6aab7e964686cdb5fb1b84eac0198ca67f8892; NOT MERGED.`  
`CHANGES: software-only 17.2 candidate: raw-body verifier boundary; PostgreSQL billing_webhook_events durable event ledger + subject ordering watermark; duplicate/event-ID immutable-field guard; FAILED retry transition; out-of-order safe ignore; unsupported-event safe no-op; entitlementGranted=false; migration 0006 transaction-bounded; focal immutable-pinned workflow.`  
`TESTS: deterministic 17.2 suite covers valid/invalid signature, mutated/non-raw body, duplicate event ID, strict out-of-order, equal-timestamp distinct events, failure+retry, timeout/error fail-closed, unsupported event and concurrent duplicate handling.`  
`CI: exact head 22550152... — F3 17.2 run 33278423859 SUCCESS; D6 33278423854 SUCCESS; D7 33278423851 SUCCESS; temp-auth 33278423880 SUCCESS; Upgrade 33278423852 SKIPPED/no aplicable; Test - Desktop Portability / Required CI 33278423879 IN_PROGRESS at STOP.`  
`EVIDENCE_REUSED: authoritative PostgreSQL/migration infrastructure and idempotent ON CONFLICT/state-transition pattern from existing control-plane/direct-operation repositories; no productive drill or unrelated CI rerun requested.`  
`EVIDENCE_NEW: PR #67; final delta is 8 commits ahead / 0 behind from ed6aab7e and exactly four 17.2 paths; focal exact-head 17.2 gate SUCCESS; integration reread remained ed6aab7e before STOP.`  
`UNVERIFIED: final Required CI conclusion; merge/race transaction; real Stripe webhook secret/signature provider integration; public webhook endpoint; productive event delivery; async external queue/worker; entitlement 18.x reconciliation; physical staging/prod.`  
`BLOCKERS: only exact-head Test - Desktop Portability / Required CI 33278423879 still running for integration eligibility.`  
`RECOMMENDATION_TO_JOBS: keep SAME PR #67. If Required CI closes SUCCESS and integration remains ed6aab7e-compatible, issue owner race-check/protected merge assignment without rerun ceremonial. If integration moves, refresh SAME lineage + fresh applicable exact-head CI. Do not start 18.x from this result.`

## HISTORIAL

- `NIGHT-WOZ-018`: PENDING_CI — PR #67 @ `22550152...`; focal/D6/D7/temp-auth green; Required CI still running; no merge.
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
