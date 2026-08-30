# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 031:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 — `NIGHT-BBB-030` (ASSIGNED).**

SAME #63 `bbb/task-25.1-windows-import` está OPEN/Ready/mergeable sobre base `3ad8f55a...`, promotion head `1b957eff98271f78809c6eeb5fd79fed311b3286`.

Estado exact-head observado:
- **Windows Import functional journey `33305947664` — SUCCESS**;
- **Required CI `33305947677` — SUCCESS**;
- PostgreSQL live/recovery dentro de ese Required CI — SUCCESS;
- **F4 Functional Matrix `33305947676` — FAILURE**, job `matrix-contract`, step `Validate dependency-safe matrix contract`.

`NIGHT-BBB-029` no dejó RESULTADO DEL TURNO observable antes de CYCLE 031. JOBS lo supersede monotónicamente con `NIGHT-BBB-030` conservando SAME #63 y el mismo blocker reducido: atribuir/corregir únicamente el contrato de matriz. No reabrir Windows import harness sin evidencia nueva. Cualquier head nuevo exige F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head antes de race-check/merge.

## Día 21 — Manifest e identidad únicos

### 21.1 — `[x] DONE / INTEGRATED`
#51 incorporó identidad Galer + bundle ID `com.beatgaler.app`.

### 21.2 — `[x] DONE / INTEGRATED`
#51 merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858` con D7/D6/Required CI/Upgrade Staging SUCCESS.

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
#55 merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

### 24.2 — `[x] DONE / INTEGRATED`
#57 merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] WINDOWS IMPORT PROMOTED / MATRIX CONTRACT RED` — BBB `NIGHT-BBB-030`

#60 integró la matriz base como `7de7b57a508b3cf05cbded81501fbd3da63922a3`.

SAME #63 estado vivo:
- base `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`;
- head `1b957eff98271f78809c6eeb5fd79fed311b3286`;
- `windows/import` promovido a `AUTOMATED_PASS`;
- Windows Import `33305947664` SUCCESS;
- Required CI `33305947677` SUCCESS;
- F4 Matrix `33305947676` FAILURE en `Validate dependency-safe matrix contract`;
- no merge todavía.

BBB debe corregir solo el contrato de matriz si el fallo es atribuible a la promoción/evidenceCatalog; después fresh exact-head gates y race-check/merge. No se cierra 25.1 completa: persisten otros gaps y D22/D23 externos.

Persisten otros gaps reales: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por prerequisitos reales.
