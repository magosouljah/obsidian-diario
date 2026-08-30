# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 025:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 — `NIGHT-BBB-024` (ASSIGNED).**

`NIGHT-BBB-023` no produjo RESULTADO DEL TURNO ni head/handoff nuevo antes de CYCLE 025 y quedó `NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no debe ejecutarse después de 024.

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. #60 integró la matriz dependency-safe de 25.1, pero 25.1 completo sigue abierto.

PR #63 `bbb/task-25.1-windows-import @ 033c2b55a0c46471b7e7ddb3af57b626699ac6e6` sigue OPEN/Ready y su base viva es `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

Evidencia exact-head vigente:
- F4 Matrix `33284981451` — SUCCESS;
- D6 `33284981429` — SUCCESS;
- D7 `33284981377` — SUCCESS;
- Windows Import `33284981477` — **FAILURE**;
- Desktop Portability de ese head no sustituye el failure funcional;
- Upgrade 21.2 — SKIPPED/no aplicable.

Job Windows Import `99186491944`: setup, exact checkout, Node, Rust, npm y `Prepare isolated embedded Tauri WebDriver` terminaron SUCCESS; `Run existing Windows import E2E harness` terminó FAILURE. Por tanto:
- no existe PASS literal de import;
- `windows/import` continúa `NOT_COVERED`;
- no se promueve matrix;
- #63 no se integra todavía.

`NIGHT-BBB-024` debe consumir el primer failure causal del run actual y aplicar únicamente el corrective F4/harness mínimo sobre SAME #63. Si llega a ejecutarse una assertion funcional y demuestra un bug de producto, registrar `PRODUCT_FINDING` y STOP para JOBS.

CI-FALLBACK: `NONE`.

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

## Día 24 — Updater/procedencia/rollback

### 24.1 — `[x] DONE / INTEGRATED`
#55 exact tested head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

### 24.2 — `[x] DONE / INTEGRATED`
#57 exact tested head `4e251cae84ff55116c89c8398e78f04aecb78e3c`; Required CI/Desktop Portability `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

Esto no cierra D22/D23 ni autoriza release público.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN` — BBB `NIGHT-BBB-024`

#60 integró la matriz como `7de7b57a508b3cf05cbded81501fbd3da63922a3`. Conserva `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` honestos.

SAME #63 intenta cerrar únicamente Windows/import reutilizando `test:e2e:import`. Estado vivo:
- head `033c2b55a0c46471b7e7ddb3af57b626699ac6e6`;
- base `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`;
- Windows Import `33284981477` FAILURE en E2E harness;
- no merge/no promoción a `AUTOMATED_PASS`.

Persisten otros gaps reales: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
