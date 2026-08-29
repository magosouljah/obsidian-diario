# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable CYCLE 008:** `integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

## Owner actual

**BBB — F4 / 25.1 dependency-safe — `NIGHT-BBB-009`.**

21.1 + 21.2, 24.1 y 24.2 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. BBB completó el audit REUSE-FIRST de 25.1: existe cobertura reutilizable amplia, pero no una matriz funcional completa demostrada cross-browser/cross-OS/iPhone/YouTube/billing.

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

PR #57 `bbb/task-24.2-updater-recovery` fue integrado después de race-check exacto.

Evidencia:
- exact tested head `4e251cae84ff55116c89c8398e78f04aecb78e3c`;
- exact base probado `f0d65aa66988e3e1a026e237b65c65a56b098aa9`;
- Test - Desktop Portability/Required CI `33255401498` SUCCESS;
- D6 `33255401544` SUCCESS;
- D7 `33255401512` SUCCESS;
- merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`, parents exactos `f0d65aa...` + `4e251cae...`.

Satisfecho técnicamente:
- [x] update N-1 y fallos de red/disco/firma/manifest con policy fail-closed;
- [x] recovery/rollback verificable;
- [x] planner/runbook no destructivo para retiro de artifact malo/comunicación.

Esto no cierra D22/D23 ni autoriza release público, signing, notarization o movimiento stable/latest.

## Día 25 — Matriz/freeze

### 25.1 — `[ 🟡 ] IN PROGRESS` — BBB `NIGHT-BBB-009`

Audit REUSE-FIRST ya confirmado:
- Web/component/desktop harnesses reutilizables cubren auth/import/Review/playback/edit/Trash/offline/downloads y updater recovery/static portability;
- Web E2E explícito actualmente demuestra boot compilado sin Tauri, no todos los journeys;
- Windows/macOS tienen gates nativos/build/portability y harnesses, pero no evidencia explícita de todos los journeys funcionales en ambos OS;
- no se encontró runner funcional iPhone;
- YouTube tiene helper de release pero no journey E2E dedicado verificado;
- billing tiene plan code pero no journey funcional/E2E dedicado verificado.

`NIGHT-BBB-009` autoriza únicamente:
- componer un **único matrix/runner dependency-safe** sobre harnesses existentes;
- mapear cada requisito a `AUTOMATED_PASS`, `PENDING_EXTERNAL`, `PRODUCT_FINDING` o `NOT_COVERED` con evidencia concreta;
- añadir solo gaps pequeños F4-matrix-only que no cambien lógica F2/F3;
- un único candidate si existe delta real, con tests/CI exact-head.

No falsear iPhone/hardware/credenciales externas ni reparar producto fuera de F4.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
