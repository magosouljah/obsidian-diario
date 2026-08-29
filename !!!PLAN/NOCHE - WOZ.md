# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-019`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 17.2 — SAME PR #67 PostgreSQL recovery-gate corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`
- `REUSE_PR: #67 / woz/night-17.2-webhook-contract`
- `KNOWN_HEAD: 22550152e9960c5dad328711b3a8b150301a8c4f`
- `PREDECESSOR: NIGHT-WOZ-018 PENDING_CI; Required CI later ended FAILURE.`

### PRIMARY

1. Preflight GitHub vivo, duplicate-check and reuse ONLY SAME #67; no new 17.2 branch/PR.
2. Inspect exact failure in Test - Desktop Portability run `33278423879`, job `99169258638` (`PostgreSQL live integration + recovery gate`). Migrations/adversarial persistence and dump/encrypt/restore passed; failure occurred at `Verify restored constraints, secrets, reconciliation and rollback state`.
3. Determine whether migration `0006` / webhook durable tables or test/recovery expectations caused the restored-state mismatch. Apply the smallest fix that preserves existing recovery invariants and 17.2 semantics.
4. Do not weaken recovery checks, remove constraints, bypass PostgreSQL authority, or alter already accepted D9/D10 evidence just to turn CI green.
5. Re-run focused 17.2 tests and fresh applicable exact-head Required CI on any changed head. Existing focal 17.2/D6/D7/temp-auth green evidence may be reused only if still applicable to the final head.
6. When exact-head CI is fully green, race-check integration/base and merge SAME #67 through the authorized owner flow; verify resulting merge SHA.
7. Claim only `17.2 SOFTWARE DONE / INTEGRATED` if merge is demonstrated. No Stripe productive resources, no 18.x entitlements, no physical staging/prod.
8. Handoff in this ledger + Issue #41 and STOP.

**Required evidence:** exact failure cause, focused tests, fresh applicable Required CI, race-check and merge SHA if integrated.  
**STOP:** recovery invariant regression, data-loss/constraint weakening, external provider requirement, unexpected baseline, unresolved red required gate, or scope expansion into 18.x.

### CI-FALLBACK

`NONE`

Reason: 18.x billing/entitlement work would share billing/PostgreSQL ownership with #67 and depends on trustworthy webhook/reconciliation semantics. Advancing it while PRIMARY waits would violate independence/dependency rules.

## RESULTADO PROCESADO ANTERIOR — NIGHT-WOZ-018

- `STATUS: PENDING_CI`.
- PR #67 head `22550152e9960c5dad328711b3a8b150301a8c4f`, base `ed6aab7e...`, OPEN/Ready/mergeable.
- 17.2 focal `33278423859`, D6 `33278423854`, D7 `33278423851`, temp-auth `33278423880` = SUCCESS.
- Required CI/Desktop Portability `33278423879` = FAILURE because PostgreSQL live integration + recovery job `99169258638` failed after restore at restored-state verification; Required CI aggregator also failed.
- No merge; no 18.x claim. Issue #41 handoff: `5465227160`.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-018`: PENDING_CI — #67 candidate; required recovery gate later red.
- `NIGHT-WOZ-017`: PR #65 merged `ed6aab7e...`; 17.1 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-014`: PR #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-009`: PR #59 merged `be9e58c...`; 16.1 software done, physical separation external.
- `NIGHT-WOZ-006`: PR #56 integrated `f0d65aa...`; D10.1 reduced to external proof.
- D9: DONE/PASS — Issue #41 `5460959369`.
