# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 012:** `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`.

## Owner actual

**BBB — F4 / 25.1 functional coverage residual — `NIGHT-BBB-013`.**

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. PR #60, que añade la matriz dependency-safe de 25.1, quedó integrada como `7de7b57a508b3cf05cbded81501fbd3da63922a3`; la tarea 25.1 completa sigue abierta porque el artifact conserva gaps `NOT_COVERED`, `PENDING_EXTERNAL` y `PRODUCT_FINDING` que el merge no convierte en PASS.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[x] DONE / INTEGRATED`

Artifact histórico PR #48 quedó incorporado por PR #51.

Decisiones integradas:
- nombre visible `Galer`;
- bundle ID `com.beatgaler.app`;
- fuente coherente de versión/endpoints/channel/capabilities;
- runtimes/recursos y checks anti-drift incorporados.

### 21.2 [P1 · DE/QA] — `[x] DONE / INTEGRATED`

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

**Dependencia:** certificado + manifest. **Gate:** publisher verificable + core flows.  
**Estado:** manifest satisfecho; certificado/signing siguen externos y no se inventan.

## Día 23 — macOS firmado/notarizado

### 23.1
- [ ] entitlements/hardened runtime/nested signing;
- [ ] notarytool Accepted + staple + offline verify;
- [ ] custodia/rotación credenciales.

### 23.2
- [ ] clean download/Gatekeeper/first run;
- [ ] Intel + Apple Silicon + macOS mínimo declarado;
- [ ] DAWs/updater/app-data.

**Dependencia:** membership/cert + universales. **Gate:** notarizado/stapled + core flows.  
**Estado:** Apple Developer/certificados siguen externos/deferred según F0/1.2.

## Día 24 — Updater/procedencia/rollback

### 24.1 — `[x] DONE / INTEGRATED`

PR #55 exact tested head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.

Satisfecho:
- [x] tag/source SHA binding y checkout mismo source SHA;
- [x] checksums/SBOM SPDX/provenance verification;
- [x] channels/rings/minimum versions/kill switch;
- [x] publicación fail-closed mientras controles no autoricen release.

### 24.2 — `[x] DONE / INTEGRATED`

PR #57 exact tested head `4e251cae84ff55116c89c8398e78f04aecb78e3c`; Test - Desktop Portability/Required CI `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

Satisfecho técnicamente:
- [x] update N-1 y fallos de red/disco/firma/manifest con policy fail-closed;
- [x] recovery/rollback verificable;
- [x] planner/runbook no destructivo para retiro de artifact malo/comunicación.

Esto no cierra D22/D23 ni autoriza release público, signing, notarization o movimiento stable/latest.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN` — BBB `NIGHT-BBB-013`

PR #60 `bbb/task-25.1-functional-matrix`:
- exact tested head `945638c8bb650b0ce0bbe569e48a791a93d80e39`;
- F4 - 25.1 Functional Matrix `33265800007` SUCCESS;
- D6 `33265800004` SUCCESS;
- D7 `33265800022` SUCCESS;
- Test - Desktop Portability `33265800008` SUCCESS;
- Upgrade 21.2 Staging `33265800019` SKIPPED/no aplicable;
- protected expected-head merge `7de7b57a508b3cf05cbded81501fbd3da63922a3`, parents exactos `58a6bf614...` + `945638c8...`.

La matriz integrada conserva la verdad del coverage:
- harnesses Web/component/desktop existentes cubren piezas de auth/import/Review/playback/edit/Trash/offline/downloads/updater;
- no todos los journeys core están demostrados end-to-end en Web + Windows + macOS;
- iPhone runner/hardware sigue `PENDING_EXTERNAL`/sin evidencia;
- YouTube/billing dedicados siguen abiertos donde la matriz los marca;
- integrar #60 **no** convierte esos gaps en PASS.

`NIGHT-BBB-013` debe escoger un solo slice dependency-safe de mayor retorno entre los journeys `NOT_COVERED`, reutilizar harnesses existentes y producir evidencia funcional real. No segunda matriz, no reabrir #60, no fixes F2/F3 robados. Bugs descubiertos → `PRODUCT_FINDING` con owner correspondiente. Exact-head obligatorio para candidate/merge.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
