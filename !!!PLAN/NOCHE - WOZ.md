# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-026`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — server half: garbage journal + orphan reconciliation Web-callable`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `PREDECESSOR: NIGHT-WOZ-025 BLOCKED / MERGE_TOOL_REJECTED — processed by JOBS CYCLE 027.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen exact-head green; do NOT touch or retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reconcile baseline before any write.
2. REUSE-FIRST sobre los componentes server-side ya encontrados por AAA: `cloud-server/garbage-journal-repository.js`, `garbage-reconciliation-worker.js` y contratos/tests relacionados. No reimplementar durable journal si ya satisface el requisito.
3. Auditar literalmente el residual F2/13.1: **“garbage journal limpia uploads huérfanos”** y el boundary detectado por `NIGHT-AAA-025`: falta demostrar/crear un contrato server-side que Web pueda invocar de forma segura para registrar/reconciliar uploads abandonados.
4. Si el contrato ya existe y satisface el requisito, producir evidencia focused y no abrir PR ceremonial. Si existe gap real, implementar solo el mínimo server-side necesario para que el lifecycle Web pueda registrar/reconciliar orphans de forma durable, idempotente y fail-closed, reutilizando el journal/worker existentes.
5. Añadir focused tests de persistencia/retry/idempotencia y de que cleanup no borra un upload que todavía sea válido/committed. No inventar timings/policies externos no definidos; si una decisión de producto es necesaria, STOP / RO DECISION REQUIRED.
6. Mantener el boundary estricto con AAA: **no tocar** Save All frontend, bulk UI/orchestration, `webReviewSave`, `commitWebBeatEdit()`, `commitWebImportedBeat()` ni archivos frontend que AAA posea bajo `NIGHT-AAA-027`.
7. Si hay delta, una sola rama/PR F2 server mínima. No tocar billing/Stripe/F3 18.2+, #68, Desktop, signing, provider resources ni infraestructura.
8. Reportar RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** baseline/base/head; qué se reutilizó; contrato Web-callable real o gap exacto; persistencia/retry/idempotencia; protección contra borrar committed/valid; focused tests; exact-head CI aplicable; UNVERIFIED explícito.  
**STOP:** necesidad de tocar carril frontend AAA, decisión RO/policy no definida, baseline material no reconciliable, scope creep, CI rojo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: #68 está bloqueado por execution layer; 18.2 comparte billing; 13.2/D14/D15 ampliarían scope. No inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-025

### PRIMARY

- `STATUS: BLOCKED / MERGE_TOOL_REJECTED`.
- Baseline `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- PR #68 `woz/night-18.1-entitlements-reservation @ 2a988ec2a25d6ecfa927614fcc32cde689995103` sigue OPEN/Ready/mergeable=true.
- Exact-head CI revalidado: F3 18.1 `33299898356` SUCCESS; D6 `33299898222` SUCCESS; D7 `33299898232` SUCCESS; Productive Temp Auth Compile `33299898207` SUCCESS; Desktop Portability `33299898130` SUCCESS.
- Race-check inmediatamente antes del intento confirmó integration/base/head exactos.
- Merge con expected-head guard fue bloqueado por la safety/execution layer antes de que GitHub aceptara la mutación; recheck posterior dejó integration en `3ad8f55a...`.
- No existe merge SHA; 18.1 NO integrado; Stripe/provider productivo y 18.2 siguen UNVERIFIED/no iniciados.
- Handoff Issue #41 también fue bloqueado por la misma execution layer.
- JOBS CYCLE 027 preserva/freezea #68 y mueve el turno ejecutable de WOZ al server half independiente de F2/13.1.

### CI-FALLBACK

- `STATUS: NONE / NOT_RUN`.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-026`: ASSIGNED — F2/13.1 server garbage-journal/orphan cleanup; CI-FALLBACK NONE.
- `NIGHT-WOZ-025`: BLOCKED / MERGE_TOOL_REJECTED — #68 unchanged; integration `3ad8f55a...`.
- `NIGHT-WOZ-024`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-023`: PENDING/WAITING_CI -> exact-head GREEN.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — #67 merged `3ad8f55a...`.
- `NIGHT-WOZ-017`: #65 merged; 17.1 SOFTWARE DONE / INTEGRATED.
