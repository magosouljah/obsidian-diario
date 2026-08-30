# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-026`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: corregir launcher/session antes de assertions`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ ed03b806669373758d38bfd211e8f8905c86e269`
- `PREDECESSOR: NIGHT-BBB-025 ASSIGNED / NOT_PROCESSED at CYCLE 027 preflight — superseded to preserve monotonic execution; do not run 025 after 026.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reutiliza SAME #63; no replacement branch/PR.
2. Consume exact-head Windows Import `33300992453`, job `99228993010`, head `ed03b806...`.
3. Hecho causal verificado: prepare/build/plugin compilan, pero el servicio efectivo entra a `TauriLaunchService.onPrepare`; primer failure explícito es Edge WebDriver mismatch (`Edge 151.0.4129.101`, driver `unknown`, sugerencia del servicio: `autoDownloadEdgeDriver: true`), seguido por `tauri-driver not found` y finalmente `No browserName defined...`. Todo antes de cualquier assertion de import.
4. Diagnostica la **config efectiva**, no la intención del script. Aplica el corrective F4/harness mínimo que elimine el primer failure causal y haga que el camino de driver/session realmente usado quede provisionado/seleccionado. No apiles fixes especulativos ni toques lógica productiva de import.
5. Corre/requiere Windows Import exact-head. Solo si se alcanza sesión y las assertions existentes pasan literalmente, promover únicamente `windows/import` a `AUTOMATED_PASS`.
6. Cualquier cambio mueve head: exigir Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head antes de race-check/merge.
7. Si una assertion funcional llega a ejecutarse y falla por producto, registrar `PRODUCT_FINDING` y STOP para JOBS; no absorber el bug productivo en F4 sin reasignación.
8. Reportar RESULTADO DEL TURNO + handoff Issue #41 y STOP.

**Required evidence:** baseline/base/head; primer failure causal; config/provider/session efectiva; delta mínimo; Windows Import literal PASS o blocker factual; exact-head CI; no matrix promotion sin PASS.  
**STOP:** producto fuera de F4, 25.2/D22/D23, package/global changes no justificadas, baseline race, CI no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: 25.2 y signing/notarization amplían scope; no existe otro carril F4 independiente y seguro preautorizable sin competir por release-chain ownership.

## RESULTADO PROCESADO — NIGHT-BBB-025

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS CYCLE 027`.
- No RESULTADO DEL TURNO, nuevo head ni handoff observable al preflight.
- GitHub conserva #63 OPEN/Ready/mergeable @ `ed03b806...`; Windows Import `33300992453` sigue FAILURE.
- Se emite 026 para impedir ejecución tardía duplicada de 025.

## RESULTADO PROCESADO — NIGHT-BBB-024

- Worker cerró `PENDING / WAITING_CI` sobre #63 @ `ed03b806669373758d38bfd211e8f8905c86e269`.
- JOBS verificó fresh exact-head: F4 Matrix `33300992450` SUCCESS; D6 `33300992447` SUCCESS; D7 `33300992444` SUCCESS; Desktop Portability `33300992437` SUCCESS; Windows Import `33300992453` **FAILURE**.
- `windows/import` continúa `NOT_COVERED`; no matrix promotion; no merge.
- Issue #41 handoff previo `5467567511`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-026`: ASSIGNED — SAME #63 launcher/session corrective; CI-FALLBACK NONE.
- `NIGHT-BBB-025`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-024`: PENDING/WAITING_CI -> Windows Import FAILURE `33300992453`.
- `NIGHT-BBB-023`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-021`: PENDING -> prior Windows Import failure.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
