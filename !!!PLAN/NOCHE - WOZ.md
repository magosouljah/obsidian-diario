# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-028`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — SAME PR #70: exact-head PostgreSQL gate failure attribution + integration if green`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #70 / woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`
- `PREDECESSOR: NIGHT-WOZ-027 PENDING/WAITING_CI — processed by JOBS CYCLE 029.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen; do NOT touch/retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; reutiliza SAME #70, no rama/PR alterno.
2. Evidencia aceptada exact-head `5a99ebf2...`: workflow específico `F2 - 13.1 Orphan Lifecycle` run `33304798320` = SUCCESS. No repetirlo ceremonialmente salvo cambio de head.
3. Required CI/Test Desktop Portability run `33304798363` terminó FAILURE. El fallo visible está en `PostgreSQL live integration + recovery gate`, paso `Execute migrations and adversarial persistence checks on PostgreSQL`; Web/shared y Supply chain pasaron.
4. Inspecciona logs/reproduce el gate PostgreSQL y clasifica atribución. Si el fallo es causado por #70, corrige solo la causa mínima dentro del server half y SAME #70. Si es externo/transitorio/no atribuible, no cambies producto para apaciguar CI: documenta evidencia y STOP/PENDING.
5. Si cambia head, exige focused orphan tests + workflow F2/13.1 + Required CI aplicable fresh exact-head. Revalida persistencia/retry/idempotencia/fail-closed y protección committed/valid.
6. Si todo queda verde y integration sigue compatible, race-check + merge SAME #70 por flujo técnico autorizado; verifica merge SHA e integration HEAD.
7. Incluso si #70 integra, no cierres 13.1 completo: el carril Web/product wiring pertenece a AAA/#69.
8. No tocar frontend AAA/#69, billing/F3, #68, Desktop, provider resources ni infraestructura.
9. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** base/head; run F2 `33304798320`; diagnóstico exacto del PG failure; logs/repro; focused tests; fresh exact-head CI si cambia; merge SHA si integra; UNVERIFIED explícito.  
**STOP:** fallo no atribuible/transitorio, necesidad de tocar frontend/billing/infra/#68, baseline race, evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: PRIMARY ya es una corrección/diagnóstico sobre SAME #70; #68 sigue bloqueado y otras piezas ampliarían scope.

## RESULTADO PROCESADO — NIGHT-WOZ-027

- `STATUS: PENDING / WAITING_CI`.
- `branch/head: woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`.
- `PR: #70 OPEN / Ready` sobre base `3ad8f55a...`.
- Gap real implementado: boundary Web-callable durable para abandoned uploads + revalidación autoritativa antes de borrar orphan_upload; committed/valid se protege fail-closed.
- Focused workflow `F2 - 13.1 Orphan Lifecycle` run `33304798320` = SUCCESS.
- Required CI `33304798363` = FAILURE por PostgreSQL live/recovery gate; no PASS ni merge reclamados.
- `UNVERIFIED`: atribución exacta del PG failure y estado post-fix si aplica.

## HOLDING — F3/18.1 / PR #68

#68 @ `2a988ec2a25d6ecfa927614fcc32cde689995103` sigue OPEN/Ready/mergeable sobre base `3ad8f55a...`, exact-head green histórico; merge execution bloqueado externamente. No recrear/reintentar durante 028.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-028`: ASSIGNED — SAME #70 PG gate attribution/fix/integration if green; fallback NONE.
- `NIGHT-WOZ-027`: PENDING/WAITING_CI -> focused F2 workflow SUCCESS; Required CI PostgreSQL gate FAILURE.
- `NIGHT-WOZ-026`: NOT_PROCESSED / SUPERSEDED.
- `NIGHT-WOZ-025`: BLOCKED / MERGE_TOOL_REJECTED — #68 unchanged.
- `NIGHT-WOZ-023`: #68 exact-head green candidate.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — #67 merged `3ad8f55a...`.
