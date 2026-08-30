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

### PRIMARY

Assignment ID: NIGHT-WOZ-021
STATUS: DONE / INTEGRATED — 17.2 SOFTWARE DONE / INTEGRATED
baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40
branch/head: woz/night-17.2-webhook-contract @ 27c2f30007a687a144be289a64ab986451f05c99
PR: #67 MERGED
cambios: exactamente 5 paths autorizados: .github/workflows/f3-17.2-webhook-contract.yml; cloud-server/billing-webhook.js; cloud-server/migrations/0006_billing_webhooks.sql; cloud-server/tests/billing-webhook.test.cjs; cloud-server/tests/postgres-restore.verify.cjs. Restore verifier conserva expected ledger derivado de listMigrations().
tests: focused 17.2/recovery cubierto por exact-head CI; no tests locales adicionales requeridos en este cierre.
CI: exact head 27c2f300 — F3 17.2 run 33283532676 SUCCESS; D6 33283532664 SUCCESS; D7 33283532679 SUCCESS; productive temp-auth 33283532723 SUCCESS; Test - Desktop Portability 33283532696 SUCCESS; Upgrade 21.2 33283532704 SKIPPED/no aplicable.
evidencia: pre-merge PR #67 OPEN/Ready/mergeable=true base 712b49b head 27c2f300; integration race-check permaneció 712b49b; merge ejecutado con expected_head_sha=27c2f300; merge SHA 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af; integration HEAD post-merge verificado = 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af.
UNVERIFIED: Stripe productivo, recursos externos, 18.x entitlements, physical staging/prod — fuera de scope y no reclamados.
blockers: NONE para software 17.2.
condición de STOP alcanzada: PRIMARY DONE / INTEGRATED; no autoasignar siguiente tarea.
recomendación para JOBS: aceptar 17.2 SOFTWARE DONE / INTEGRATED sobre 3ad8f55a; emitir nueva asignación explícita si corresponde continuar.

### CI-FALLBACK

Assignment ID: NIGHT-WOZ-021
STATUS: NOT RUN / NONE
baseline: 712b49b6689a31a47902dbe95e98622d001dab40
branch/head: N/A
PR: N/A
cambios: ninguno
tests: N/A
CI: N/A
evidencia: asignación vigente declara CI-FALLBACK NONE.
UNVERIFIED: N/A
blockers: N/A
condición de STOP alcanzada: fallback no autorizado/no necesario.
recomendación para JOBS: no inferir trabajo alterno.

## RESULTADO PROCESADO — NIGHT-WOZ-020

- `Assignment ID: NIGHT-WOZ-020`
- `WORKER_STATUS: PENDING / WAITING_CI`
- `baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `branch/head: woz/night-17.2-webhook-contract @ 27c2f30007a687a144be289a64ab986451f05c99`
- `PR: #67 OPEN / Ready / NOT MERGED / mergeable=true`
- `scope: exactamente cinco paths F3/recovery; no #66 overwrite.`

## HISTORIAL COMPACTO

- `NIGHT-WOZ-021`: DONE/INTEGRATED — PR #67 merged `3ad8f55a...`; 17.2 SOFTWARE DONE / INTEGRATED.
- `NIGHT-WOZ-020`: PENDING/WAITING_CI — refreshed candidate `27c2f300...`.
- `NIGHT-WOZ-019`: PENDING/WAITING_CI — minimal recovery verifier corrective.
- `NIGHT-WOZ-017`: PR #65 merged; 17.1 SOFTWARE DONE / INTEGRATED.
