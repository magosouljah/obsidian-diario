# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-021`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: activar realmente embedded WDIO y alcanzar Windows Import assertion`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ 2a5853209669f7b50b51126f0aa4572383492c26`
- `PREDECESSOR: NIGHT-BBB-020 PENDING -> exact-head Windows Import run 33281787254 terminó FAILURE; otros applicable gates del head quedaron SUCCESS.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reusa únicamente SAME PR #63; no abras PR/rama replacement para 25.1.
2. Toma el fallo literal del exact head `2a585320...` como autoridad: build E2E terminó, pero `@wdio/tauri-service` entró en `onPrepare` legacy y reportó `msedgedriver version mismatch` (Edge `151.0.4129.101`, Driver `unknown`), después diagnóstico `tauri-driver not found`, y finalmente `No "browserName" defined in capabilities nor hostname or port found`. **No assertion de import fue alcanzada.**
3. Determina por qué `driverProvider=embedded` preparado por `scripts/prepare-f4-25.1-embedded-driver.mjs` no quedó seleccionado/consumido por la configuración WDIO efectiva. Corrige únicamente esa causa factual, preferentemente dentro de los 3 paths F4 ya autorizados. Si la evidencia obliga a tocar la config E2E aislada existente, limita el cambio estrictamente a habilitar el provider embebido; no cambies producto.
4. No uses `autoDownloadEdgeDriver`/`autoInstallTauriDriver` como bypass salvo que la documentación/config efectiva demuestre que siguen siendo requisitos del provider embebido; el objetivo es eliminar el fallback accidental al launcher legacy, no ocultarlo.
5. Mantén `windows/import = NOT_COVERED` hasta obtener una ejecución literal donde se cree la sesión y las assertions existentes de `tests/e2e/import-flow.e2e.mjs` pasen.
6. Cuando exista literal Windows Import PASS, promueve `windows/import` a `AUTOMATED_PASS` en SAME #63. Esa promoción crea head nuevo: exige fresh exact-head Windows Import + F4 Matrix + D6 + D7 + Desktop Portability aplicables antes de race-check/merge.
7. Si el siguiente run falla antes de assertions, usa solo el nuevo log factual para el siguiente corrective; no toques lógica productiva de import sin un fallo de assertion que la implique.
8. Handoff en este ledger + Issue #41 y STOP.

**Required evidence:** baseline/head/base, changed-file scope, log que demuestre provider/session efectiva, literal import assertions PASS antes de promover matrix, fresh exact-head CI después de toda promoción, race-check + merge SHA si integrado.  
**STOP:** necesidad de modificar lógica productiva antes de una assertion fallida, scope fuera de F4/25.1, package/global driver changes no justificados, 25.2/signing/notarization, CI rojo no atribuible o baseline race no reconciliable.

### CI-FALLBACK

`NONE`

Reason: 25.2 y los otros huecos de la matriz comparten ownership/release surfaces o ampliarían scope mientras #63 aún no demuestra la journey Windows. No hay fallback independiente seguro.

## RESULTADO PROCESADO — NIGHT-BBB-020

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-020`  
`TURN_STATUS_AT_WORKER_CLOSE: PENDING / WAITING_CI`  
`JOBS_RECHECK: FAILED_GATE`

- `baseline: integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`
- `branch/head: bbb/task-25.1-windows-import @ 2a5853209669f7b50b51126f0aa4572383492c26`
- `PR: #63 OPEN / Ready / NOT MERGED / mergeable=true`
- `CI final exact head: D6 33281787207 SUCCESS; D7 33281787235 SUCCESS; Desktop Portability 33281787208 SUCCESS; F4 Matrix 33281787222 SUCCESS; Upgrade 33281787228 SKIPPED; Windows Import 33281787254 FAILURE.`
- `literal failure: embedded-prep step SUCCESS; E2E build SUCCESS; service then reported EdgeDriver mismatch (Edge 151.0.4129.101 / driver unknown), tauri-driver missing and no browserName/hostname/port; 0 specs passed / 1 failed before import assertions.`
- `CLAIM: windows/import remains NOT_COVERED; no AUTOMATED_PASS; no merge.`

## HISTORIAL COMPACTO

- `NIGHT-BBB-021`: ASSIGNED — SAME #63, fix effective embedded-provider selection/session only; CI-FALLBACK NONE.
- `NIGHT-BBB-020`: PENDING at worker close; JOBS recheck observed Windows Import FAILURE on 2a585320; other applicable CI SUCCESS.
- `NIGHT-BBB-019`: PENDING — baseline movement STOP; previous DevToolsActivePort diagnosis.
- `NIGHT-BBB-018`: PENDING — Windows Import gate red.
- `NIGHT-BBB-017`: PENDING — prior refresh / official driver bootstrap.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
- `NIGHT-BBB-008`: #57 integrated `f73c9ee...`.
- `NIGHT-BBB-005`: #55 integrated `672e133...`.
- `NIGHT-BBB-003`: #51 integrated `5b05ca845...`.
