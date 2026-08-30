# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 026:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 — `NIGHT-BBB-025` (ASSIGNED).**

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. #60 integró la matriz dependency-safe de 25.1, pero 25.1 completo sigue abierto.

PR #63 `bbb/task-25.1-windows-import @ ed03b806669373758d38bfd211e8f8905c86e269` sigue OPEN/Ready, base viva `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

Fresh exact-head CYCLE 026:
- F4 Matrix `33300992450` — SUCCESS;
- D6 `33300992447` — SUCCESS;
- D7 `33300992444` — SUCCESS;
- Desktop Portability `33300992437` — SUCCESS;
- Windows Import `33300992453` — **FAILURE**;
- Upgrade 21.2 — SKIPPED/no aplicable.

Job Windows Import `99228993010`: checkout/setup/npm/prepare embedded/build completan; `tauri-plugin-wdio-webdriver` compila. Antes de assertions, el servicio efectivo entra a `TauriLaunchService.onPrepare` y falla primero con Edge WebDriver mismatch (`Edge 151.0.4129.101`, driver `unknown`, recomendación del propio servicio `autoDownloadEdgeDriver: true`), luego reporta `tauri-driver not found` y termina con `No browserName defined in capabilities nor hostname or port found`.

Por tanto:
- no existe evidencia de bug productivo de import;
- existe failure F4 launcher/session reproducible antes de assertions;
- `windows/import` continúa `NOT_COVERED`;
- no AUTOMATED_PASS ni merge.

`NIGHT-BBB-025` debe trabajar SAME #63, verificar la config/provider/session **efectivamente consumida** y hacer solo el corrective F4 mínimo que resuelva el primer failure causal. Si alcanza assertions y aparece bug de producto, registrar PRODUCT_FINDING y STOP.

CI-FALLBACK: `NONE`.

## Día 21 — Manifest e identidad únicos

### 21.1 — `[x] DONE / INTEGRATED`
#51 incorporó el artifact histórico #48. Nombre visible `Galer`, bundle ID `com.beatgaler.app`, versión/endpoints/channel/capabilities coherentes y checks anti-drift.

### 21.2 — `[x] DONE / INTEGRATED`
#51 exact tested head `0fd9bee8117ca92fb9f713f0d55089f5707a2917`; D7/D6/Required CI/Upgrade Staging SUCCESS; merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.

## Día 22 — Windows firmado

### 22.1
- [ ] servicio/certificado de firma sin private key expuesta;
- [ ] binarios + NSIS con timestamp/verificación;
- [ ] firma updater separada.

### 22.2
- [ ] clean install/upgrade/uninstall/UAC;
- [ ] SmartScreen/AV/paths/red/sleep;
- [ ] DAWs/versiones/updater válido e inválido.

**Estado:** certificado/signing siguen externos.

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
#55 merge `672e133bc9cb8a47a29d4b34e13fc535290e5681` con Required CI/release-controls/D6/D7 SUCCESS.

### 24.2 — `[x] DONE / INTEGRATED`
#57 merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d` con Required CI/D6/D7 SUCCESS.

Esto no cierra D22/D23 ni autoriza release público.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN` — BBB `NIGHT-BBB-025`

#60 integró la matriz como `7de7b57a508b3cf05cbded81501fbd3da63922a3`. Conserva `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` honestos.

SAME #63 intenta cerrar únicamente Windows/import reutilizando `test:e2e:import`:
- head `ed03b806669373758d38bfd211e8f8905c86e269`;
- base `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`;
- Windows Import `33300992453` FAILURE en launcher/session antes de assertions;
- no merge/no promoción a `AUTOMATED_PASS`.

Persisten otros gaps reales: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por prerequisitos reales.
