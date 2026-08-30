# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-021`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 17.2 — SAME PR #67 final exact-head gate + race/merge transaction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `REUSE_PR: #67 / woz/night-17.2-webhook-contract @ 27c2f30007a687a144be289a64ab986451f05c99`
- `PREDECESSOR: NIGHT-WOZ-020 PENDING / WAITING_CI — refreshed candidate; JOBS recheck now sees focused 17.2/D6/D7/temp-auth SUCCESS while Desktop Portability 33283532696 remains IN_PROGRESS.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reusa ONLY SAME #67; no nueva rama/PR 17.2.
2. Recheck exact head `27c2f30007a687a144be289a64ab986451f05c99`. Evidencia ya observada por JOBS para este head: F3 17.2 `33283532676` SUCCESS; D6 `33283532664` SUCCESS; D7 `33283532679` SUCCESS; productive temp-auth `33283532723` SUCCESS; Upgrade 21.2 `33283532704` SKIPPED/no aplicable. `Test - Desktop Portability` `33283532696` sigue IN_PROGRESS al emitir esta asignación.
3. Si Desktop Portability completa SUCCESS y integration sigue en `712b49b...`, haz race-check final, verifica que #67 siga limitada a los 5 paths F3/recovery esperados y mergea SAME #67 por el flujo técnico autorizado. Verifica merge SHA + nuevo integration HEAD.
4. Si Desktop Portability falla, NO merges: diagnostica solo la causa literal. Corrige únicamente si pertenece al scope 17.2/recovery ya autorizado; cualquier head nuevo requiere fresh applicable exact-head CI.
5. Si integration se mueve antes del merge, refresh/reconcile SAME #67 contra el baseline vivo, preserva únicamente el delta 17.2/recovery y vuelve a exigir fresh exact-head CI completo para la nueva combinación.
6. Preserva invariantes: restore verifier deriva ledger esperado de `listMigrations()`; checksum/secrets/reconciliation/rotation/rollback/constraints no se debilitan.
7. Solo tras merge demostrado puedes reclamar `17.2 SOFTWARE DONE / INTEGRATED`. No Stripe productivo, no 18.x entitlements, no physical staging/prod.
8. Handoff en este ledger + Issue #41 y STOP.

**Required evidence:** exact final base/head, focused 17.2/recovery PASS, all applicable exact-head CI, changed-file scope, race-check, merge SHA e integration HEAD si integrado.  
**STOP:** CI rojo, recovery invariant regression, baseline race no reconciliable, delta ajeno, data-loss/constraint weakening, provider externo requerido o expansión a 18.x.

### CI-FALLBACK

`NONE`

Reason: 18.x comparte billing/PostgreSQL ownership y depende de semánticas 17.2 confiables; iniciar 18.x mientras #67 espera el último gate violaría independencia material. No inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-020

- `Assignment ID: NIGHT-WOZ-020`
- `WORKER_STATUS: PENDING / WAITING_CI`
- `baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `branch/head: woz/night-17.2-webhook-contract @ 27c2f30007a687a144be289a64ab986451f05c99`
- `PR: #67 OPEN / Ready / NOT MERGED / mergeable=true`
- `scope: exactamente cinco paths F3/recovery; no #66 overwrite.`
- `JOBS_RECHECK: F3 17.2 33283532676 SUCCESS; D6 33283532664 SUCCESS; D7 33283532679 SUCCESS; temp-auth 33283532723 SUCCESS; Desktop Portability 33283532696 IN_PROGRESS; Upgrade SKIPPED.`
- `UNVERIFIED: final Desktop Portability conclusion; race-check; merge SHA; integration HEAD post-merge.`

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

- `NIGHT-WOZ-021`: ASSIGNED — SAME #67 final exact-head gate + race/merge; CI-FALLBACK NONE.
- `NIGHT-WOZ-020`: PENDING/WAITING_CI — 27c2f300; focused gates green; Desktop Portability still running at JOBS recheck.
- `NIGHT-WOZ-019`: PENDING/WAITING_CI — minimal recovery verifier corrective `8a534111...`; CI later all green on old base.
- `NIGHT-WOZ-018`: PENDING_CI — original #67 recovery gate red.
- `NIGHT-WOZ-017`: PR #65 merged `ed6aab7e...`; 17.1 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-014`: PR #61 merged `55e0d875...`; 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- `NIGHT-WOZ-009`: PR #59 merged `be9e58c...`; 16.1 software done, physical separation external.
- `NIGHT-WOZ-006`: PR #56 integrated `f0d65aa...`; D10.1 reduced to external proof.
- D9: DONE/PASS — Issue #41 `5460959369`.
