# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — billing/entitlements software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-039`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F3 / 18.2 — reconciliation + exception-queue software contract`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`

### PRIMARY

Assignment ID: NIGHT-WOZ-039
STATUS: PENDING / WAITING_CI
baseline: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b
branch/head: woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb
PR: #73 OPEN / Ready; created from exact live baseline
cambios: exactly 4 paths — cloud-server/billing-reconciliation.js; cloud-server/migrations/0008_billing_reconciliation.sql; cloud-server/tests/billing-reconciliation.test.cjs; .github/workflows/f3-18.2-reconciliation.yml. REUSE-FIRST conserva billing_subscription_state de #68 y webhook/event ledger de #67. Candidate detecta divergence provider↔BeatGaler, persiste exception queue durable/idempotente con attempt_count, serializa por advisory xact lock y falla cerrado ante snapshot desconocido/incompleto o provider failure; nunca concede entitlement desde reconciliation/session.
tests: focused suite committed: matching authoritative state; divergence durable; replay/idempotency + retry attempt; ambiguous provider state fail-closed; provider lookup failure fail-closed. No ejecución local reclamada.
CI: consulta inmediata exact-head fc831172 devolvió 0 workflow runs observables; fresh applicable CI todavía pendiente. No se reutilizó CI histórico y no se intentó merge.
evidencia: preflight confirmó assignment 039 no procesado, baseline vivo a9d35a3d y #68/18.1 integrado. Duplicate-check: no branch 18.2 ni PR reconciliation/exception existente. PR #73 base_sha=a9d35a3d, head=fc831172, changed_files=4, additions=186, deletions=0. Handoff Issue #41 comment 5469672078.
UNVERIFIED: Stripe/provider productivo; 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund; grace periods aprobados; integración/merge del candidate. Esos tails no se reclaman ni se inventan.
blockers: fresh exact-head CI aún no observable.
condición de STOP alcanzada: WAITING_CI; CI-FALLBACK NONE; no esperar interactuando.
recomendación para JOBS: conservar SAME #73/head y recheck fresh applicable exact-head CI; si todo verde y baseline/race-check permanecen válidos, reemitir transacción de integración al owner. Mantener 18.2 global abierto por provider/business tails.

### CI-FALLBACK

Assignment ID: NIGHT-WOZ-039
STATUS: NOT RUN / NONE
baseline: a9d35a3d69dd9127029fb851d189f9bd3079d03b
branch/head: N/A
PR: N/A
cambios: ninguno
tests: N/A
CI: N/A
evidencia: JOBS declaró CI-FALLBACK NONE.
UNVERIFIED: N/A
blockers: N/A
condición de STOP alcanzada: fallback no autorizado.
recomendación para JOBS: no inferir trabajo alterno.

## RESULTADO PROCESADO — NIGHT-WOZ-038

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO/handoff observable al preflight CYCLE 040.

## ÚLTIMO RESULTADO MATERIAL

- `NIGHT-WOZ-037: DONE / INTEGRATED`.
- PR #68 exact head `68adaad4a5b1b2b50ba192c1b58325cbba0472e3` merged como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- F3/18.1 `[x] SOFTWARE DONE / INTEGRATED`.

## HOLDING

- F3/20.1 gap map WOZ033 válido, unassigned.
- F2/#70 stale/frozen; fuera de scope.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-039`: PENDING/WAITING_CI — #73 @ `fc831172...`.
- `NIGHT-WOZ-038`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-037`: DONE/INTEGRATED — #68 merge `a9d35a3d...`.
- `NIGHT-WOZ-033`: DONE/AUDIT_ONLY — 20.1 gap map.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
