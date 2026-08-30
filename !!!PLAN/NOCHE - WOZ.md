# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-027`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — server half: garbage journal + orphan reconciliation Web-callable`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `PREDECESSOR: NIGHT-WOZ-026 ASSIGNED / no RESULTADO DEL TURNO observable at JOBS CYCLE 028 — superseded to preserve monotonic execution; do not run 026 after 027.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen exact-head green; do NOT touch or retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reconcile baseline before any write.
2. REUSE-FIRST sobre `cloud-server/garbage-journal-repository.js`, `garbage-reconciliation-worker.js` y contratos/tests relacionados. No reimplementar durable journal si ya satisface el requisito.
3. Auditar literalmente el residual F2/13.1: **garbage journal limpia uploads huérfanos** y el boundary Web↔server detectado por AAA. Debe existir un contrato server-side invocable por el lifecycle Web para registrar/reconciliar uploads abandonados de forma durable.
4. Si el contrato ya existe y satisface el requisito, producir evidencia focused y no abrir PR ceremonial. Si hay gap real, implementar solo el mínimo server-side necesario para registrar/reconciliar orphans, reutilizando journal/worker existentes.
5. Focused tests obligatorios: persistencia, retry, idempotencia, fail-closed y protección contra borrar un upload todavía válido/committed. No inventar timing/policies externos no definidos.
6. Mantén boundary estricto con AAA `NIGHT-AAA-028`: no tocar Save All/bulk frontend, Review/Import wiring ni archivos Web owned por AAA.
7. Si hay delta, una sola rama/PR F2 server mínima. No tocar billing/Stripe/F3 18.2+, #68, Desktop, signing, provider resources ni infraestructura.
8. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** baseline/base/head; artifacts reutilizados; contrato Web-callable real o gap exacto; persistencia/retry/idempotencia; protección committed/valid; focused tests; exact-head CI si hay candidate; UNVERIFIED explícito.  
**STOP:** necesidad de tocar carril frontend AAA, decisión RO/policy no definida, baseline material no reconciliable, scope creep, CI rojo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: #68 sigue bloqueado por execution layer; 18.2 comparte billing; 13.2/D14/D15 ampliarían scope.

## RESULTADO PROCESADO — NIGHT-WOZ-026

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS CYCLE 028`.
- No RESULTADO DEL TURNO ni artifact/handoff nuevo fue observable en el ledger/Issue #41 al preflight.
- La pieza server 13.1 sigue sin owner concurrente y se reemite como 027.

## HOLDING — F3/18.1 / PR #68

- #68 `woz/night-18.1-entitlements-reservation @ 2a988ec2a25d6ecfa927614fcc32cde689995103` sigue OPEN/Ready/mergeable=true sobre base `3ad8f55a...`.
- Exact-head applicable CI permanece green según evidencia ya aceptada.
- El intento de merge de `NIGHT-WOZ-025` fue bloqueado por execution/safety layer antes de que GitHub aceptara la mutación; integration sigue `3ad8f55a...`; no existe merge SHA.
- No recrear candidate ni repetir merge ceremonialmente durante 027.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-027`: ASSIGNED — F2/13.1 server garbage-journal/orphan cleanup; fallback NONE.
- `NIGHT-WOZ-026`: NOT_PROCESSED / SUPERSEDED.
- `NIGHT-WOZ-025`: BLOCKED / MERGE_TOOL_REJECTED — #68 unchanged.
- `NIGHT-WOZ-023`: #68 exact-head green candidate.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — #67 merged `3ad8f55a...`.
