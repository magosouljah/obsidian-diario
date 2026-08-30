# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-020`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F3 / 17.2 — SAME PR #67 refresh/race transaction after baseline moved`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `REUSE_PR: #67 / woz/night-17.2-webhook-contract`
- `KNOWN_HEAD: 8a5341114e00f373bd88553f3f95be53a153b6b8`
- `PREDECESSOR: NIGHT-WOZ-019 PENDING/WAITING_CI — minimal recovery verifier corrective committed; all fresh exact-head CI later completed SUCCESS, but that head/base combination predates merge #66.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reuse ONLY SAME #67; no new 17.2 branch/PR.
2. Treat fresh CI on `8a534111...` as valid evidence for that exact old combination only: F3 17.2 `33280134623` SUCCESS; D6 `33280134598` SUCCESS; D7 `33280134660` SUCCESS; temp-auth `33280134648` SUCCESS; Required CI/Desktop Portability `33280134630` SUCCESS.
3. Because integration moved to `712b49b...` by merge #66 after the corrective was authored, refresh/reconcile SAME #67 onto live baseline before integration. Preserve only the intended 17.2 delta and the one-lineage recovery verifier corrective.
4. Re-check that the stale-ledger root cause remains resolved: restore verifier must derive the expected migration ledger from `listMigrations()` while preserving checksum, secrets, reconciliation, rotation/rollback and constraint checks.
5. Any refreshed/cherry-picked/rebased head is a new exact head: require fresh applicable CI for the final combination. Do not merge using only the old-green head evidence.
6. If final exact-head Required CI and focused 17.2/recovery gates are all green, race-check and merge SAME #67 through authorized owner flow; verify merge SHA + integration HEAD.
7. Claim only `17.2 SOFTWARE DONE / INTEGRATED` if merge is demonstrated. No Stripe productive resources, no 18.x entitlements, no physical staging/prod.
8. Handoff in this ledger + Issue #41 and STOP.

**Required evidence:** refreshed base/head, changed-file scope, focused 17.2/recovery PASS, fresh applicable exact-head CI, race-check and merge SHA if integrated.  
**STOP:** recovery invariant regression, conflict with #66, unrelated delta appears, data-loss/constraint weakening, external provider requirement, CI red, or scope expansion into 18.x.

### CI-FALLBACK

`NONE`

Reason: 18.x shares billing/PostgreSQL ownership and depends on trustworthy 17.2 semantics; no independent fallback is safe.

## RESULTADO DEL TURNO — NIGHT-WOZ-020

### PRIMARY

- `Assignment ID: NIGHT-WOZ-020`
- `STATUS: PENDING / WAITING_CI`
- `baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `branch/head: woz/night-17.2-webhook-contract @ 27c2f30007a687a144be289a64ab986451f05c99`
- `PR: #67 OPEN / Ready / NOT MERGED`
- `cambios: SAME #67 fue refrescado sobre baseline vivo y conserva exactamente cinco paths: .github/workflows/f3-17.2-webhook-contract.yml; cloud-server/billing-webhook.js; cloud-server/migrations/0006_billing_webhooks.sql; cloud-server/tests/billing-webhook.test.cjs; cloud-server/tests/postgres-restore.verify.cjs. No delta de #66 fue sobrescrito.`
- `tests: no se fabricó resultado local nuevo; el corrective de restore conserva listMigrations() y el resto de invariantes previamente verdes. Fresh exact-head CI requerido para 27c2f300... todavía no observable.`
- `CI: WAITING_CI — al cierre de este turno fetch_commit_workflow_runs(27c2f300...) devolvió 0 runs; evidencia verde 8a534111... queda explícitamente old-combination-only.`
- `evidencia: #66 delta vs old baseline toca únicamente Web Library/frontend; #67 changed-file scope son cinco paths F3/recovery disjuntos. GitHub confirmó #67 reabierto con base 712b49b..., head 27c2f300..., 1 commit y 5 changed files.`
- `UNVERIFIED: fresh applicable exact-head CI sobre 27c2f300...; focused 17.2/recovery PASS en esta combinación; race-check final; merge SHA; integration HEAD post-merge.`
- `blockers: espera externa verificable de GitHub Actions para el nuevo exact head.`
- `condición de STOP alcanzada: WAITING_CI; CI-FALLBACK es NONE, por lo que no se inventa trabajo alterno.`
- `recomendación para JOBS: mantener NIGHT-WOZ-020 PENDING hasta observar CI del exact head 27c2f300...; si todo lo aplicable queda verde, reasignar/continuar la transacción de race-check + merge SAME #67; si CI red, conservar scope 17.2/recovery y corregir únicamente la causa factual.`

### CI-FALLBACK

- `Assignment ID: NIGHT-WOZ-020`
- `STATUS: NOT_RUN`
- `baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `branch/head: N/A`
- `PR: N/A`
- `cambios: NONE`
- `tests: NONE`
- `CI: NONE`
- `evidencia: asignación vigente declara CI-FALLBACK = NONE.`
- `UNVERIFIED: NONE`
- `blockers: NONE`
- `condición de STOP alcanzada: fallback inexistente por orden explícita.`
- `recomendación para JOBS: no asignar 18.x como fallback mientras 17.2 siga pendiente.`

## RESULTADO PROCESADO — NIGHT-WOZ-019

- `TURN_STATUS: PENDING / WAITING_CI`
- `BASE_BEFORE: integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`
- `HEAD_AFTER: woz/night-17.2-webhook-contract @ 8a5341114e00f373bd88553f3f95be53a153b6b8`
- `PR: #67 OPEN / Ready / NOT MERGED`
- `ROOT CAUSE: postgres-restore.verify.cjs hardcodeaba ledger 0001..0005 mientras #67 añade 0006_billing_webhooks.sql; restore conservó 0006 y el verifier estaba stale.`
- `CHANGE: corrective mínimo solo en cloud-server/tests/postgres-restore.verify.cjs para exigir ledger restaurado exacto == listMigrations() actual, preservando checks existentes.`
- `CI FINAL OBSERVADO POR JOBS: F3 17.2 33280134623 SUCCESS; D6 33280134598 SUCCESS; D7 33280134660 SUCCESS; temp-auth 33280134648 SUCCESS; Required CI/Desktop Portability 33280134630 SUCCESS.`
- `UNVERIFIED: combinación refreshed contra 712b49b..., final race-check, merge SHA.`

## HISTORIAL COMPACTO

- `NIGHT-WOZ-020`: PENDING/WAITING_CI — SAME #67 refreshed onto 712b49b... as 27c2f300...; fresh exact-head CI pending; CI-FALLBACK NONE.
- `NIGHT-WOZ-019`: PENDING/WAITING_CI — minimal recovery verifier corrective `8a534111...`; CI later all green on old base.
- `NIGHT-WOZ-018`: PENDING_CI — original #67 recovery gate red.
- `NIGHT-WOZ-017`: PR #65 merged `ed6aab7e...`; 17.1 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-014`: PR #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-009`: PR #59 merged `be9e58c...`; 16.1 software done, physical separation external.
- `NIGHT-WOZ-006`: PR #56 integrated `f0d65aa...`; D10.1 reduced to external proof.
- D9: DONE/PASS — Issue #41 `5460959369`.
