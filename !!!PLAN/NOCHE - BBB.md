# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / functional matrix.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-040`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #72 post-promotion matrix-contract attribution/corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `REUSE_PR: #72 / bbb/night-25.1-windows-review @ 56dc4adf206cc53f5260c71952f84ae67d994279`
- `PREDECESSOR: NIGHT-BBB-039 had no RESULTADO DEL TURNO/handoff by JOBS CYCLE 045; superseded explicitly to prevent late duplicate execution.`

### PRIMARY

1. Preflight live integration + SAME #72 exact head/base + duplicate-check; no replacement PR and no auth/#71/#74 work.
2. Reuse exact-head evidence on `56dc4adf206cc53f5260c71952f84ae67d994279`: Windows Review `33324512156` SUCCESS; Windows Import `33324512159` SUCCESS; Required CI `33324512153` SUCCESS. F4 Functional Matrix `33324512174` is FAILURE specifically at `Validate dependency-safe matrix contract`.
3. Attribution-first: determine the literal dependency-safe matrix rule violated by promoting only `windows/review = AUTOMATED_PASS`. Do not assume product failure and do not lower the matrix contract.
4. If the failure is a bounded inconsistency in matrix/workflow/test evidence within #72 scope, apply only the minimum corrective on SAME #72. If it requires product logic, auth overlap, unrelated rows, signing/notarization or a gate change, report `PRODUCT_FINDING/BLOCKED` and STOP.
5. On any new head obtain fresh exact-head Windows Review + F4 Functional Matrix + D6 + D7 + Desktop Portability/Required CI. All applicable gates must be green.
6. If all gates are green, race-check integration. If baseline changed, refresh/reconcile and revalidate; otherwise merge SAME #72 through authorized BBB flow and verify merge SHA/post-merge integration HEAD.
7. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** literal contract failure/root cause; minimal diff if any; exact new head; fresh Windows Review/F4 Matrix/D6/D7/Required CI; merge SHA only if actually integrated.  
**STOP:** product finding, auth/#71/#74 overlap, unrelated matrix-row change, baseline race requiring broad conflict work, non-attributable CI red, merge-flow unavailable or gate relaxation.

### CI-FALLBACK

**AREA: F4 / 25.2 — READ-ONLY design-freeze readiness inventory.**

**Condición de activación:** solo si PRIMARY llega realmente a `WAITING_CI` después de un corrective válido y GitHub todavía no tiene resultado final de esos checks.  
**Alcance:** read-only contra integration vivo; inventariar evidencia existente y gaps literales para tokens/nav/library/drawer/player/settings/wizard, backlog P2/P3, guion beta/formulario/criterios. No crear rama, PR, commit ni cambiar matrix/product/docs. No revisar auth/#71/#74 ni archivos de #72.  
**Evidencia requerida:** lista factual de artefactos/rutas ya existentes + gaps no cubiertos, con SHA baseline observado; distinguir `EXISTS`, `PARTIAL`, `GAP`, `PENDING_EXTERNAL`.  
**STOP:** cualquier necesidad de escritura, solapamiento con PRIMARY/AAA/WOZ, dependencia de resultado de #72, intento de cerrar 25.2 sin evidencia o scope más allá de inventario. Tras el audit, volver a comprobar PRIMARY antes de cerrar turno.

## RESULTADO PROCESADO / SUPERSEDED — NIGHT-BBB-039

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO ni handoff nuevo observable en Issue #41 al preflight CYCLE 045.
- GitHub vivo conserva #72 OPEN/Ready, no mergeado, exact head `56dc4adf206cc53f5260c71952f84ae67d994279`, base `a9d35a3d...`.
- El fallo matrix-contract sigue factual; para impedir ejecución tardía/duplicada, el mismo PRIMARY se reemite como `NIGHT-BBB-040`.

## RESULTADO PROCESADO — NIGHT-BBB-038

- `STATUS: PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- SAME #72 promoted only `windows/review` to `AUTOMATED_PASS`; Issue #41 handoff `5470100644`.
- Current exact head: `56dc4adf206cc53f5260c71952f84ae67d994279`; base `a9d35a3d...`; OPEN/Ready/mergeable.
- Windows Review `33324512156` SUCCESS.
- Windows Import `33324512159` SUCCESS.
- Required CI `33324512153` SUCCESS.
- F4 Functional Matrix `33324512174` FAILURE; job `matrix-contract`, failing step exactly `Validate dependency-safe matrix contract`.
- No merge; `windows/review` is not claimed integrated while this gate remains red.

## HISTORIAL COMPACTO

- `NIGHT-BBB-040`: ASSIGNED — SAME #72 matrix-contract attribution/corrective; 25.2 audit-only fallback if PRIMARY waits CI.
- `NIGHT-BBB-039`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-038`: WAITING_CI -> matrix-contract FAILURE after promotion.
- `NIGHT-BBB-037`: literal Windows Review PASS on pre-promotion head.
- `NIGHT-BBB-034`: PENDING / PRODUCT_FINDING windows/auth.
- `NIGHT-BBB-031`: DONE/INTEGRATED — #63 merge `02a40564...`.
