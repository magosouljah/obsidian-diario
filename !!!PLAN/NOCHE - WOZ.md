# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-030`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — SAME PR #70: apply attributed minimal live-PG fixture corrective + fresh CI`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #70 / woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`
- `PREDECESSOR: NIGHT-WOZ-029 PENDING / ATTRIBUTED_CORRECTIVE_BLOCKED_BY_SCOPE_TOOLING — processed by JOBS CYCLE 031.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen; do NOT touch/retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; reutiliza SAME #70, no rama/PR alterno.
2. Reuse evidencia ya atribuida: focused F2 run `33304798320` SUCCESS; Required CI `33304798363` falló en `cloud-server/tests/postgres-live.integration.cjs:159`, actual `REQUIRED`, expected `ETIMEDOUT`, con PostgreSQL sano.
3. JOBS autoriza explícitamente ampliar el changed-file scope de #70 con **un solo quinto path de test**: `cloud-server/tests/postgres-live.integration.cjs`.
4. Corrective permitido: actualizar únicamente el fixture de retry ETIMEDOUT que encola `reason: orphan_upload` para suministrar una revalidación autoritativa positiva `isObjectStillOrphan: async () => true` o equivalente semánticamente exacto. El objetivo es que ese fixture vuelva a probar retry/ETIMEDOUT bajo el nuevo contrato.
5. No debilites ni cambies el comportamiento productivo fail-closed de `processGarbageBatch`; el guard debe seguir siendo obligatorio en producción.
6. No cambies migrations, infraestructura, provider resources, frontend/#69, billing/#68 ni otros tests no necesarios.
7. Tras el corrective, exige focused orphan tests/workflow + Required CI fresh exact-head. Si aparece rojo, atribuye antes de cualquier segundo cambio.
8. Si todo aplicable queda verde y integration sigue exactamente compatible, race-check + merge SAME #70; verifica merge SHA + integration HEAD. No cierres 13.1 completo porque AAA/#69 posee el lado Web.
9. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** diff del quinto test path, preservación explícita fail-closed productiva, focused tests, Required CI fresh exact-head, branch/head, race-check y merge SHA/integration HEAD si integra.  
**STOP:** necesidad de tocar producto para apaciguar el test, migration/infra/frontend/#69/#68, baseline race, CI rojo no atribuible o corrective mayor al fixture autorizado.

### CI-FALLBACK

`NONE`

Reason: #68 está frozen por execution layer y otras piezas ampliarían ownership; no existe fallback independiente seguro.

## RESULTADO PROCESADO — NIGHT-WOZ-029

### PRIMARY

- `STATUS: PENDING / ATTRIBUTED_CORRECTIVE_BLOCKED_BY_SCOPE_TOOLING`.
- `baseline:` `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- `PR #70:` OPEN/Ready/mergeable @ `5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`; original scope 4 files, no migration.
- Focused F2 `33304798320` SUCCESS.
- Required CI `33304798363` FAILURE; job `99239317593`; PostgreSQL healthy.
- Deterministic cause: new orphan fail-closed guard requires `isObjectStillOrphan`; existing PG live retry fixture omitted it and therefore returned `REQUIRED` before synthetic delete could throw `ETIMEDOUT`.
- Minimum semantic corrective: positive authoritative guard in that fixture only. No product mutation was made in 029 because the fifth test path was outside prior explicit scope.
- Issue #41 handoff `5468213443`.

### CI-FALLBACK

`NONE / NOT_RUN`.

## HOLDING — F3/18.1 / PR #68

#68 @ `2a988ec2a25d6ecfa927614fcc32cde689995103` remains frozen exact-head-green; prior merge execution blocked by connector/safety execution layer. Do not recreate/retry during 030.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-030`: ASSIGNED — corrective de fixture PG live explícitamente autorizado + fresh focused/Required CI + merge if green.
- `NIGHT-WOZ-029`: PENDING / ATTRIBUTED_CORRECTIVE_BLOCKED_BY_SCOPE_TOOLING.
- `NIGHT-WOZ-028`: no result observable; superseded.
- `NIGHT-WOZ-027`: focused F2 SUCCESS; Required CI PG failure.
- `NIGHT-WOZ-025`: BLOCKED / MERGE_TOOL_REJECTED — #68 unchanged.
- `NIGHT-WOZ-023`: #68 exact-head green candidate.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — #67 merged `3ad8f55a...`.
