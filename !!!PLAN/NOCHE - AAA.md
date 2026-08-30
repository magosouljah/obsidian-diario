# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** Desktop product-auth corrective.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-039`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 blocker / Desktop product-auth — SAME PR #74 compile corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `REUSE_PR: #74 / aaa/night-25.1-auth-session-corrective @ 92058b42e6e455f641e8a494f5c85ae1f2214834`
- `PREDECESSOR: NIGHT-AAA-038 PENDING/WAITING_CI; JOBS CYCLE 042 recheck resolved Required CI to FAILURE.`

### PRIMARY

1. Preflight live integration + SAME #74 head/base + duplicate-check; no replacement PR.
2. Consume exact failure from `Test - Desktop Portability / Required CI` run `33321752522`: Web/shared build fails at `src/platform/index.ts(10,22)` because `__TAURI_INTERNALS__` is not available on the current `Window | RuntimeWindow` type union.
3. Correct only that typing/compile issue while preserving the intended runtime semantics from AAA038: `__TAURI_INTERNALS__` primary signal; packaged Tauri origins fallback; ordinary localhost/Web must remain Web.
4. Do not broaden auth/security contract, refactor platform selection, touch #71, matrix, #72, F2/F3 or infra.
5. Run focused platform/runtime regression and obtain fresh applicable exact-head CI. D6/D7/Required CI must be green; compile failure must disappear.
6. If all applicable gates are green and integration authority for #74 belongs to AAA under the current flow, race-check and integrate; otherwise report READY_FOR_INTEGRATION with exact evidence and STOP. Do not touch #71 afterward without a new JOBS assignment.
7. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; compile fix diff; focused regression; fresh exact-head D6/D7/Required CI; merge SHA only if actually integrated.  
**STOP:** semantic drift, auth contract change, baseline race, CI red not attributable, merge flow unavailable or need to touch #71.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-AAA-038

- `STATUS: PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- PR #74 OPEN/Ready/mergeable @ `92058b42e6e455f641e8a494f5c85ae1f2214834`, base `a9d35a3d...`.
- D6 `33321752555` SUCCESS; D7 `33321752537` SUCCESS; Upgrade 21.2 SKIPPED.
- `Test - Desktop Portability / Required CI` `33321752522` FAILURE.
- Literal root failure: `src/platform/index.ts(10,22): error TS2339: Property '__TAURI_INTERNALS__' does not exist on type '(Window & typeof globalThis) | RuntimeWindow'.`
- No pass, no merge, no #71 revalidation.

## HOLDING

- F2/12.1 cold/warm real: runtime navegador ejecutable faltante.
- F2/13.1 Web #69: coordinator probado; wiring/refresh pendientes y candidate stale.
- F2/13.1 server #70: frozen por safe-write + stale baseline.

## HISTORIAL COMPACTO

- `NIGHT-AAA-039`: ASSIGNED — SAME #74 typing/compile corrective + fresh CI.
- `NIGHT-AAA-038`: PENDING/WAITING_CI; final recheck = Required CI FAILURE por TS compile.
- `NIGHT-AAA-037`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-032`: PENDING / STOP_RUNTIME_UNAVAILABLE.
- `NIGHT-AAA-031`: PENDING / STOP_WRITE_SURFACE.
- `NIGHT-AAA-027`: #69 created.
