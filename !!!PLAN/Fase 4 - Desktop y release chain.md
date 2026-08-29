# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 013:** `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 Windows import corrective transaction — `NIGHT-BBB-014`.**

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. PR #60 integró la matriz dependency-safe de 25.1, pero 25.1 completo sigue abierto.

`NIGHT-BBB-013` produjo PR #63 `bbb/task-25.1-windows-import @ 65a7bf07029babfb500d3913226ec8a5ca6e0deb`, OPEN/Ready/mergeable, reutilizando `test:e2e:import`. Required CI exact-head `33271091123` terminó SUCCESS, pero el gate funcional específico `F4 - 25.1 Windows Import Journey` run `33271091186` terminó **FAILURE** en `Run existing Windows import E2E harness`. Por evidence-before-claim, `windows/import` sigue no demostrado y #63 no se integra.

## Día 21 — Manifest e identidad únicos

### 21.1 — `[x] DONE / INTEGRATED`
PR #51 incorporó el artifact histórico #48. Nombre visible `Galer`, bundle ID `com.beatgaler.app`, versión/endpoints/channel/capabilities coherentes y checks anti-drift.

### 21.2 — `[x] DONE / INTEGRATED`
PR #51 exact tested head `0fd9bee8117ca92fb9f713f0d55089f5707a2917`; D7 `33243436937`, D6 `33243436890`, Required CI `33243436894`, Upgrade Staging `33243436914` SUCCESS; merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.

## Día 22 — Windows firmado

### 22.1
- [ ] servicio/certificado de firma sin private key expuesta;
- [ ] binarios + NSIS con timestamp/verificación;
- [ ] firma updater separada.

### 22.2
- [ ] clean install/upgrade/uninstall/UAC;
- [ ] SmartScreen/AV/paths/red/sleep;
- [ ] DAWs/versiones/updater válido e inválido.

**Estado:** certificado/signing siguen externos y no se inventan.

## Día 23 — macOS firmado/notarizado

### 23.1
- [ ] entitlements/hardened runtime/nested signing;
- [ ] notarytool Accepted + staple + offline verify;
- [ ] custodia/rotación credenciales.

### 23.2
- [ ] clean download/Gatekeeper/first run;
- [ ] Intel + Apple Silicon + macOS mínimo declarado;
- [ ] DAWs/updater/app-data.

**Estado:** Apple Developer/certificados siguen externos/deferred.

## Día 24 — Updater/procedencia/rollback

### 24.1 — `[x] DONE / INTEGRATED`
PR #55 exact tested head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

### 24.2 — `[x] DONE / INTEGRATED`
PR #57 exact tested head `4e251cae84ff55116c89c8398e78f04aecb78e3c`; Test - Desktop Portability/Required CI `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

Esto no cierra D22/D23 ni autoriza release público.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN` — BBB `NIGHT-BBB-014`

PR #60 integró la matriz como `7de7b57a508b3cf05cbded81501fbd3da63922a3`. Sigue conservando `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` honestos.

PR #63 intenta cerrar únicamente Windows/import con el harness existente. Estado factual:
- exact head `65a7bf07029babfb500d3913226ec8a5ca6e0deb`;
- Required CI `33271091123` SUCCESS;
- Windows import functional `33271091186` **FAILURE**;
- no merge/no promotion a AUTOMATED_PASS.

`NIGHT-BBB-014` debe diagnosticar la causa mínima, corregir solo workflow/glue/harness si pertenece a F4 y exigir run funcional exact-head PASS + applicable CI green. Si descubre bug de producto, registrar `PRODUCT_FINDING` para su owner sin robar implementación. No segundo residual antes de resolver/descartar #63.

Persisten, entre otros: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
