# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-027`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: promote proven Windows Import and integrate only after fresh exact-head gates`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ e14a3ab9a284484cace9b8fa98c293c7c15b5dce`
- `PREDECESSOR: NIGHT-BBB-026 PENDING/WAITING_CI — processed by JOBS CYCLE 028 after fresh CI completion.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reutiliza SAME #63; no replacement branch/PR.
2. Acepta como evidencia literal el set fresh exact-head sobre `e14a3ab9...`: F4 Matrix `33303300262` SUCCESS; D6 `33303300263` SUCCESS; D7 `33303300298` SUCCESS; Desktop Portability `33303300278` SUCCESS; Windows Import `33303300259` SUCCESS; Upgrade no aplicable.
3. No repitas ese CI solo para recrear evidencia. El objetivo ahora es la transacción pendiente: promover **únicamente** `windows/import` en `release/f4-25.1-functional-matrix.json` de `NOT_COVERED` a `AUTOMATED_PASS`, con referencia/evidencia correcta.
4. Esa promoción crea un nuevo head. Sobre ese nuevo exact head exige Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh. No aceptar green del head previo como sustituto.
5. Si el nuevo head queda completamente verde y integration sigue compatible, race-check final y merge SAME #63 por el flujo técnico autorizado.
6. Después del merge verifica merge SHA + integration HEAD. Esto cierra solo el slice Windows/import; **no cierres 25.1 completo** ni D22/D23/25.2.
7. Si el nuevo exact-head Windows Import regresa a failure, no promociones/merge; diagnostica solo si el failure es atribuible a la promoción/config. Si aparece bug de producto, `PRODUCT_FINDING` y STOP.
8. Reporta RESULTADO DEL TURNO + handoff Issue #41 y STOP.

**Required evidence:** base/head; literal Windows Import PASS previo; matrix delta mínimo; fresh promotion-head Windows Import/F4 Matrix/D6/D7/Desktop Portability; race-check; merge SHA/integration HEAD si integra.  
**STOP:** producto fuera de F4, 25.2/D22/D23, cambios globales no justificados, baseline race, CI rojo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: otros gaps F4 amplían scope o dependen de signing/hardware/external gates.

## RESULTADO PROCESADO — NIGHT-BBB-026

- `STATUS: PENDING / WAITING_CI` al cierre del worker.
- `branch/head: bbb/task-25.1-windows-import @ e14a3ab9a284484cace9b8fa98c293c7c15b5dce`.
- Corrective mínimo: restauró auto provisioning (`autoInstallTauriDriver:true`, `autoDownloadEdgeDriver:true`) en vez de desactivarlo desde prep; no producto ni matrix promotion.
- JOBS CYCLE 028 recheck exact-head:
  - F4 Matrix `33303300262` SUCCESS;
  - D6 `33303300263` SUCCESS;
  - D7 `33303300298` SUCCESS;
  - Desktop Portability `33303300278` SUCCESS;
  - **Windows Import `33303300259` SUCCESS**;
  - Upgrade skipped/no aplicable.
- Resultado factual: el harness Windows ya crea la sesión y pasa las assertions existentes de import en ese exact head.
- `UNVERIFIED`: promotion head, fresh post-promotion gates, merge.
- Issue #41 handoff previo: `5467803201`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-027`: ASSIGNED — promotion/fresh-CI/merge SAME #63; fallback NONE.
- `NIGHT-BBB-026`: PENDING/WAITING_CI -> exact-head Windows Import + applicable gates SUCCESS.
- `NIGHT-BBB-024`: prior Windows Import FAILURE before assertions.
- `NIGHT-BBB-021`: prior launcher/session failure.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
