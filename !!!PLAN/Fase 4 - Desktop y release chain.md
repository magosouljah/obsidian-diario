# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 034:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado actual

PR #63 `bbb/task-25.1-windows-import` fue **MERGED** con exact tested head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df`; merge SHA `02a40564d85284a119281ff79995c9b9bcb5e833`.

Evidencia exact-head reutilizada antes de merge:
- Windows Import `33308327283` SUCCESS;
- F4 Functional Matrix `33308327295` SUCCESS;
- D6 `33308327262` SUCCESS;
- D7 `33308327271` SUCCESS;
- Desktop Portability `33308327289` SUCCESS;
- Upgrade 21.2 SKIPPED/no aplicable.

Esto integra **solo** la fila `windows/import = AUTOMATED_PASS`; 25.1 completo permanece abierto.

## Owner actual

**BBB — `NIGHT-BBB-032` — F4 / 25.1 `windows/auth`.**

PRIMARY: REUSE-FIRST sobre `desktop_e2e` + shared auth coverage. Demostrar literalmente el journey Windows/auth mediante harness/workflow mínimo F4. No tocar producto salvo que un assertion real revele un bug; en ese caso registrar `PRODUCT_FINDING` y STOP. Promover únicamente la fila `windows/auth` después de PASS literal + fresh exact-head applicable CI + race-check limpio.

CI-FALLBACK: `NONE`.

## Día 21 — Manifest e identidad únicos

### 21.1 — `[x] DONE / INTEGRATED`
#51 incorporó identidad Galer + bundle ID `com.beatgaler.app`.

### 21.2 — `[x] DONE / INTEGRATED`
#51 merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.

## Día 22 — Windows firmado

### 22.1
- [ ] servicio/certificado de firma sin private key expuesta;
- [ ] binarios + NSIS con timestamp/verificación;
- [ ] firma updater separada.

### 22.2
- [ ] clean install/upgrade/uninstall/UAC;
- [ ] SmartScreen/AV/paths/red/sleep;
- [ ] DAWs/versiones/updater válido e inválido.

**Estado:** signing/certificado externos.

## Día 23 — macOS firmado/notarizado

### 23.1
- [ ] entitlements/hardened runtime/nested signing;
- [ ] notarytool Accepted + staple + offline verify;
- [ ] custodia/rotación credenciales.

### 23.2
- [ ] clean download/Gatekeeper/first run;
- [ ] Intel + Apple Silicon + macOS mínimo declarado;
- [ ] DAWs/updater/app-data.

**Estado:** Apple Developer/certificados externos/deferred.

## Día 24 — Updater/procedencia/rollback

### 24.1 — `[x] DONE / INTEGRATED`
#55 merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

### 24.2 — `[x] DONE / INTEGRATED`
#57 merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] IN PROGRESS`

#60 integró la matriz base. #63 integró `windows/import = AUTOMATED_PASS`.

Gaps honestos restantes incluyen:
- Web browser auth/import/review/playback/edit/trash/offline;
- Windows auth/review/playback/edit/trash/offline;
- macOS auth/import/review/playback/edit/trash/offline;
- YouTube/billing donde no existe evidencia dedicada;
- iPhone = `PENDING_EXTERNAL` por runner/hardware/credenciales.

`NIGHT-BBB-032` toma únicamente `windows/auth` por ser un slice harness-backed y no externo.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** firma/notarización/release/beta siguen bloqueadas por prerequisitos reales. No convertir gaps externos en PASS.
