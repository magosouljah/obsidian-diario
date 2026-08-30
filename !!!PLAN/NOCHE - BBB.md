# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-028`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: promote proven Windows Import and integrate only after fresh exact-head gates`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ e14a3ab9a284484cace9b8fa98c293c7c15b5dce`
- `PREDECESSOR: NIGHT-BBB-027 ASSIGNED / no RESULTADO DEL TURNO observable at JOBS CYCLE 029 — superseded for monotonic execution; do not run 027 after 028.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reutiliza SAME #63; no replacement branch/PR.
2. Acepta evidencia literal exact-head `e14a3ab9...`: F4 Matrix `33303300262`, D6 `33303300263`, D7 `33303300298`, Desktop Portability `33303300278` y Windows Import `33303300259` = SUCCESS; Upgrade no aplicable.
3. No repitas ese set. Promueve **únicamente** `windows/import` en `release/f4-25.1-functional-matrix.json` de `NOT_COVERED` a `AUTOMATED_PASS`, con referencia factual a la evidencia.
4. La promoción crea head nuevo: exige Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head sobre ese head.
5. Si todo queda verde e integration sigue compatible, race-check y merge SAME #63 por el flujo autorizado.
6. Tras merge verifica merge SHA + integration HEAD. Cierra solo slice Windows/import; no cierres 25.1 completa ni D22/D23/25.2.
7. Si Windows Import vuelve a fallar, no promociones/merge; diagnostica únicamente si atribuible a promoción/config. Bug de producto => PRODUCT_FINDING + STOP.
8. Reporta RESULTADO DEL TURNO + handoff Issue #41 y STOP.

**Required evidence:** base/head; matrix delta mínimo; fresh promotion-head Windows Import/F4 Matrix/D6/D7/Desktop Portability; race-check; merge SHA/integration HEAD si integra.  
**STOP:** producto fuera de F4, 25.2/D22/D23, cambios globales no justificados, baseline race, CI rojo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: otros gaps F4 amplían scope o dependen de signing/hardware/external gates.

## RESULTADO PROCESADO — NIGHT-BBB-026

- `STATUS: PENDING / WAITING_CI`.
- `branch/head: bbb/task-25.1-windows-import @ e14a3ab9a284484cace9b8fa98c293c7c15b5dce`.
- JOBS confirmó F4 Matrix/D6/D7/Desktop Portability y Windows Import exact-head SUCCESS.
- `UNVERIFIED`: promotion head, fresh post-promotion gates, merge.
- Issue #41 handoff: `5467803201`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-028`: ASSIGNED — SAME #63 promotion/fresh-CI/merge; fallback NONE.
- `NIGHT-BBB-027`: SUPERSEDED / no result observable at CYCLE 029.
- `NIGHT-BBB-026`: PENDING/WAITING_CI -> exact-head Windows Import + applicable gates SUCCESS.
- `NIGHT-BBB-024`: prior Windows Import FAILURE before assertions.
- `NIGHT-BBB-021`: prior launcher/session failure.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
