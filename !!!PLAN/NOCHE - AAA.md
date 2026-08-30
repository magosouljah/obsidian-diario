# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** F2 — Web / UX.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-027`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.1 — Save All + bulk conflict-safe, carril Web dependency-safe`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `PREDECESSOR: NIGHT-AAA-026 ASSIGNED / NOT_PROCESSED at CYCLE 027 preflight — superseded to preserve monotonic execution; do not run 026 after 027.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reconciliar baseline si integration cambió antes de cualquier escritura.
2. REUSE-FIRST sobre `webReviewSave`, `commitWebBeatEdit()` y `commitWebImportedBeat()`; no reimplementar single-beat durable commit ni INDEX CAS.
3. Implementar únicamente el carril Web: **Save All** multi-item usando commits durables existentes, con progreso y resumen parcial explícito de éxitos/fallos.
4. Hacer bulk conflict-safe reutilizando CAS por item; si una variante bulk global no puede ser segura con los primitives actuales, deshabilitarla honestamente y mantener camino item-by-item durable. Cero pérdida silenciosa.
5. Añadir focused tests de success total, partial failure, conflict y retry/idempotencia donde aplique.
6. **No cerrar 13.1:** WOZ tiene `NIGHT-WOZ-026` exclusivamente sobre el server half de garbage journal/orphan cleanup. No tocar sus archivos/ownership ni crear journal frontend-only.
7. Si hay gap de código, una sola rama/PR F2 mínima. Fuera de scope: `cloud-server/garbage-journal-repository.js`, `garbage-reconciliation-worker.js`, endpoints/server journal de WOZ, billing, Desktop, infra, 13.2, D14 y D15.
8. Reportar RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** baseline/base/head; tests total/partial/conflict; durable/CAS por item; cero silent loss; exact-head CI aplicable; UNVERIFIED explícito.  
**STOP:** necesidad de modificar server-side journal/cleanup, baseline material no reconciliable, overlap con WOZ, scope creep, CI rojo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: el server half pertenece a WOZ bajo assignment separado; 13.2/D14/D15 ampliarían scope.

## RESULTADO PROCESADO — NIGHT-AAA-026

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS CYCLE 027`.
- No RESULTADO DEL TURNO, branch/PR ni handoff nuevo observable al preflight.
- Se emite 027 para impedir ejecución tardía duplicada de 026.

## RESULTADO PROCESADO — NIGHT-AAA-025

- `STATUS: PENDING / STOP_OWNERSHIP_BOUNDARY`.
- Baseline `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; no branch/PR/cambio ceremonial.
- REUSE-FIRST confirmó single-save durable, INDEX CAS por item y componentes server-side de garbage journal existentes.
- Gaps: no Save All productivo con partial summary/bulk lossless; orphan cleanup requiere contrato Web-callable server-side o owner del server half.
- Issue #41 handoff `5467548340`.

## HISTORIAL COMPACTO

- `NIGHT-AAA-027`: ASSIGNED — Save All + bulk conflict-safe Web-only; CI-FALLBACK NONE.
- `NIGHT-AAA-026`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-025`: PENDING — STOP_OWNERSHIP_BOUNDARY; handoff `5467548340`.
- `NIGHT-AAA-024`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-022`: PENDING — taxonomy/state demostrado; cold/warm real sigue abierto.
- `NIGHT-AAA-020`: DONE — #66 merged `712b49b6689...`.
