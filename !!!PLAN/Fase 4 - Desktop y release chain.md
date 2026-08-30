# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 032:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**BBB — F4 / 25.1 SAME PR #63 — `NIGHT-BBB-031` (ASSIGNED).**

SAME #63 `bbb/task-25.1-windows-import` está OPEN/Ready/mergeable sobre base `3ad8f55a...`, exact head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df`.

JOBS CYCLE 032 resolvió la espera de NIGHT-BBB-030 con GitHub vivo. Fresh exact-head checks observados sobre `7a6b7443...`:
- `matrix-contract` — SUCCESS;
- Windows import functional journey — SUCCESS;
- Required CI — SUCCESS;
- PostgreSQL live integration + recovery gate — SUCCESS;
- portable Windows + macOS smoke + supply-chain/web-shared gates observados SUCCESS;
- upgrade staging — SKIPPED/no aplicable.

Por tanto el blocker de `matrix-contract` está corregido. `NIGHT-BBB-031` no debe modificar más el candidate: únicamente changed-file scope + race-check final + merge SAME #63 con expected-head guard si integration sigue compatible. Después verificar merge SHA + integration HEAD. No cerrar 25.1 completo: solo queda demostrada/integrable la fila `windows/import` y persisten otros gaps.

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

### 25.1 — `[ 🟡 ] WINDOWS IMPORT SLICE EXACT-HEAD GREEN / MERGE PENDING` — BBB `NIGHT-BBB-031`

#60 integró la matriz base como `7de7b57a508b3cf05cbded81501fbd3da63922a3`.

SAME #63 estado vivo:
- base `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`;
- head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df`;
- `windows/import` permanece `AUTOMATED_PASS`;
- fresh `matrix-contract` SUCCESS;
- fresh Windows Import SUCCESS;
- fresh Required CI SUCCESS;
- no merge todavía.

BBB debe hacer solo final race-check/merge; no rerun ceremonial mientras head y baseline no cambien. Si integration cambia antes del merge, evidence-before-claim exige revalidar la combinación material.

Persisten otros gaps reales: journeys core no demostrados cross-platform, iPhone runner/hardware externo, YouTube/billing donde la matriz marque gap y signing/notarization externos.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por prerequisitos reales.
