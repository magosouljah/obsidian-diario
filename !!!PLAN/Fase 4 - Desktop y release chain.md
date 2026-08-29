# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 017:** `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 Windows import runner bootstrap corrective — `NIGHT-BBB-017`.**

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. #60 integró la matriz dependency-safe de 25.1, pero 25.1 completo sigue abierto.

PR #63 `bbb/task-25.1-windows-import @ 8768856ff8ea15c7fa164e4b433abccf02852fb1` sigue OPEN/Ready/mergeable sobre base viva `b114111caf...`. Exact-head F4 Matrix `33276125761`, D6 `33276125754`, D7 `33276125735` y Desktop Portability `33276125736` = SUCCESS. Windows Import `33276125806` = **FAILURE** después de prepare PASS: Edge `151.0.4129.101` con msedgedriver mismatch/unknown, `tauri-driver not found` y WDIO sin browser/session. `windows/import` permanece `NOT_COVERED`. `NIGHT-BBB-017` corrige solo ese tooling/harness mínimo; no product fix F2/F3.

## Día 21 — Manifest e identidad únicos

### 21.1 — `[x] DONE / INTEGRATED`
#51 incorporó el artifact histórico #48. Nombre visible `Galer`, bundle ID `com.beatgaler.app`, versión/endpoints/channel/capabilities coherentes y checks anti-drift.

### 21.2 — `[x] DONE / INTEGRATED`
#51 exact tested head `0fd9bee8117ca92fb9f713f0d55089f5707a2917`; D7 `33243436937`, D6 `33243436890`, Required CI `33243436894`, Upgrade Staging `33243436914` SUCCESS; merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.

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

## Día 24 — Updater/procedancia/rollback

### 24.1 — `[x] DONE / INTEGRATED`
#55 exact tested head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

### 24.2 — `[x] DONE / INTEGRATED`
#57 exact tested head `4e251cae84ff55116c89c8398e78f04aecb78e3c`; Required CI/Desktop Portability `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

Esto no cierra D22/D23 ni autoriza release público.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN` — BBB `NIGHT-BBB-017`

#60 integró la matriz como `7de7b57a508b3cf05cbded81501fbd3da63922a3`. Conserva `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` honestos.

SAME #63 intenta cerrar únicamente Windows/import reutilizando `test:e2e:import`. Estado factual:
- head `8768856ff8ea15c7fa164e4b433abccf02852fb1`;
- base `b114111cafb29b4aa50cdce014059c66a75bddf2`;
- F4 Matrix `33276125761` SUCCESS;
- D6 `33276125754` SUCCESS;
- D7 `33276125735` SUCCESS;
- Desktop Portability `33276125736` SUCCESS;
- Windows Import `33276125806` **FAILURE** por driver/session bootstrap;
- no merge/no promotion a `AUTOMATED_PASS`.

`NIGHT-BBB-017` debe reparar solo EdgeDriver/Tauri Driver/WDIO session bootstrap, reutilizar la configuración existente y exigir Windows Import functional PASS + applicable fresh exact-head CI. Si aparece bug producto, registrar `PRODUCT_FINDING` y no robar implementación.

Persisten, entre otros: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
