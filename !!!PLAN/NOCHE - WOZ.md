# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-019`
- `ASSIGNMENT_STATUS: PENDING`
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

## RESULTADO DEL TURNO — NIGHT-WOZ-019

- `LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-019`
- `TURN_STATUS: PENDING`
- `BASE_BEFORE: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`
- `HEAD_AFTER: woz/night-17.2-webhook-contract @ 8a5341114e00f373bd88553f3f95be53a153b6b8`
- `PR: #67`
- `TURN_FINISHED_AT: 2026-08-29T17:03-06:00`

### PRIMARY — RESULTADO

- `STATUS: WAITING_CI`.
- Preflight factual: Assignment vigente `NIGHT-WOZ-019`, SAME #67 OPEN/Ready/mergeable, base exacta `ed6aab7e...`; duplicate-check PASS; ningún nuevo branch/PR creado.
- Failure original confirmado: run `33278423879`, job `99169258638`; migrations/adversarial persistence PASS, dump/encrypt/restore PASS, failure únicamente en `Verify restored constraints, secrets, reconciliation and rollback state`.
- Causa exacta: `cloud-server/tests/postgres-restore.verify.cjs` tenía expectativa hardcodeada del ledger `['0001','0002','0003','0004','0005']`, mientras el candidate #67 agrega migration `0006_billing_webhooks.sql`. El live integration ya validaba contra `listMigrations()`. El restore conservó la migración nueva; la expectativa de recovery estaba stale.
- Cambio mínimo: commit `8a5341114e00f373bd88553f3f95be53a153b6b8`, únicamente `cloud-server/tests/postgres-restore.verify.cjs`; importa `listMigrations()` y exige que el ledger restaurado coincida exactamente con todas las versiones del source actual, manteniendo checksum validation y todos los checks existentes de secrets, reconciliation, rotation/rollback y constraints.
- `TESTS`: ejecución local no disponible mediante el conector; el cambio disparó fresh exact-head CI automáticamente. No se afirma PASS local no observado.
- `CI`: fresh exact-head head `8a534111...`: F3 17.2 run `33280134623` IN_PROGRESS; D6 `33280134598` IN_PROGRESS; D7 `33280134660` QUEUED; temp-auth `33280134648` IN_PROGRESS; Required CI/Desktop Portability `33280134630` QUEUED. Recheck único realizado al cierre; todavía no existe conclusión final.
- `EVIDENCE`: PR #67 head vivo `8a534111...`; base `ed6aab7e...`; causalidad demostrada por contraste entre restore verifier hardcodeado y migration source/listMigrations; commit corrective limitado al verifier.
- `UNVERIFIED`: resultado final fresh CI, recovery job verde en nuevo head, race-check final, merge SHA, Stripe productivo, endpoint público/provider deliveries, 18.x, staging/prod físico.
- `BLOCKERS`: espera externa verificable de GitHub Actions/Required CI. No unresolved implementation blocker conocido en este punto.
- `STOP alcanzado`: PRIMARY entró en `WAITING_CI`; no se integra sin exact-head Required CI verde.
- `RECOMMENDATION_TO_JOBS`: mantener SAME #67 / mismo Assignment lineage. En próximo ciclo, si todos los checks fresh exact-head terminan SUCCESS y integration sigue compatible, autorizar/procesar race-check + protected merge por owner; si algún gate falla, emitir solo corrective log-driven dentro de 17.2. No abrir 18.x automáticamente.

### CI-FALLBACK — RESULTADO

- `STATUS: NOT_EXECUTED`.
- `CI-FALLBACK: NONE` escrito explícitamente por JOBS.
- No se inventó ni autoasignó trabajo alterno.
- `STOP alcanzado`: fallback inexistente/no autorizado.

## RESULTADO PROCESADO ANTERIOR — NIGHT-WOZ-018

- `STATUS: PENDING_CI`.
- PR #67 head `22550152e9960c5dad328711b3a8b150301a8c4f`, base `ed6aab7e...`, OPEN/Ready/mergeable.
- 17.2 focal `33278423859`, D6 `33278423854`, D7 `33278423851`, temp-auth `33278423880` = SUCCESS.
- Required CI/Desktop Portability `33278423879` = FAILURE because PostgreSQL live integration + recovery job `99169258638` failed after restore at restored-state verification; Required CI aggregator also failed.
- No merge; no 18.x claim. Issue #41 handoff: `5465227160`.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-019`: PENDING / WAITING_CI — stale recovery ledger expectation corrected in SAME #67 @ `8a534111...`; fresh exact-head CI running/queued; no merge.
- `NIGHT-WOZ-018`: PENDING_CI — #67 candidate; required recovery gate later red.
- `NIGHT-WOZ-017`: PR #65 merged `ed6aab7e...`; 17.1 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-014`: PR #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-009`: PR #59 merged `be9e58c...`; 16.1 software done, physical separation external.
- `NIGHT-WOZ-006`: PR #56 integrated `f0d65aa...`; D10.1 reduced to external proof.
- D9: DONE/PASS — Issue #41 `5460959369`.
