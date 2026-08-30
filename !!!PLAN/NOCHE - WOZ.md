# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F2 — Web/server durable cleanup.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-031`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — SAME PR #70: execute attributed live-PG fixture corrective + fresh CI`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #70 / woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`
- `PREDECESSOR: NIGHT-WOZ-030 had no RESULTADO DEL TURNO observable at JOBS CYCLE 032; superseded monotonically with SAME corrective scope.`
- `HOLDING_ITEM: F3 / 18.1 / PR #68 remains frozen; do NOT touch/retry it in this assignment.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; reutiliza SAME #70, no rama/PR alterno.
2. Reuse evidencia ya atribuida: focused F2 run `33304798320` SUCCESS; Required CI `33304798363` falló en `cloud-server/tests/postgres-live.integration.cjs:159`, actual `REQUIRED`, expected `ETIMEDOUT`, con PostgreSQL sano.
3. JOBS mantiene la autorización explícita de un solo quinto changed-file path: `cloud-server/tests/postgres-live.integration.cjs`.
4. Corrective permitido: actualizar únicamente el fixture ETIMEDOUT que encola `reason: orphan_upload` para suministrar revalidación autoritativa positiva `isObjectStillOrphan: async () => true` o equivalente semánticamente exacto.
5. Preserva sin cambios el comportamiento productivo fail-closed de `processGarbageBatch`; el guard sigue siendo obligatorio en producción.
6. No migrations, infra, provider resources, frontend/#69, billing/#68 ni tests no necesarios.
7. Tras el corrective, exige focused orphan workflow/tests + Required CI fresh exact-head. Si cualquier rojo aparece, atribuye antes de un segundo cambio.
8. Si todo aplicable queda verde y integration sigue compatible, race-check + merge SAME #70; verifica merge SHA + integration HEAD. No cierres 13.1 completo porque #69 Web sigue frozen/separado.
9. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** exact diff del quinto test path, preservación fail-closed productiva, focused tests, Required CI fresh exact-head, branch/head, race-check y merge SHA/integration HEAD si integra.  
**STOP:** necesidad de tocar producto para apaciguar test, migration/infra/frontend/#69/#68, baseline race, CI rojo no atribuible o corrective mayor al fixture autorizado.

### CI-FALLBACK

`NONE`

Reason: #68 está frozen y un merge suyo movería el baseline de #70; no es fallback materialmente independiente. Otras piezas ampliarían ownership.

## RESULTADO PROCESADO — NIGHT-WOZ-029

- `STATUS: PENDING / ATTRIBUTED_CORRECTIVE_BLOCKED_BY_SCOPE_TOOLING`.
- PR #70 OPEN/Ready/mergeable @ `5a99ebf2...`.
- Focused F2 `33304798320` SUCCESS.
- Required CI `33304798363` FAILURE por fixture live-PG sin `isObjectStillOrphan`; PostgreSQL sano.
- Issue #41 `5468213443`.

## HOLDING — F3/18.1 / PR #68

#68 @ `2a988ec2a25d6ecfa927614fcc32cde689995103` permanece OPEN/Ready/mergeable, exact-head green histórico y frozen por merge-execution blocker. No recrear/reintentar durante 031.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-031`: ASSIGNED — SAME #70 corrective de fixture + fresh CI + merge if green.
- `NIGHT-WOZ-030`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-029`: PENDING / attributed corrective.
- `NIGHT-WOZ-027`: focused F2 SUCCESS; Required CI PG fixture failure.
- `NIGHT-WOZ-025`: #68 exact-head green but merge execution blocked.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
