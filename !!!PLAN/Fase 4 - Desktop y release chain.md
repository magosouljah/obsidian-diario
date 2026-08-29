# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable al preflight JOBS CYCLE 007:** `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

## Owner actual

**BBB — F4 / 24.2 → 25.1 dependency-safe — `NIGHT-BBB-008`.**

21.1 + 21.2 y 24.1 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. PR #57 fue refrescado al baseline vivo y ya tiene exact-head Required CI/D6/D7 verdes; BBB debe race-check + integrar, y después reducir 25.1 por REUSE-FIRST sin invadir producto F2/F3.

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

No implica signing Windows, notarización macOS ni release público.

### 24.2 — `[ 🟡 ] READY FOR OWNER MERGE` — BBB `NIGHT-BBB-008`

**Candidate único REUSE-FIRST:** PR #57 `bbb/task-24.2-updater-recovery`.

Estado vivo verificado por JOBS:
- exact refreshed head `4e251cae84ff55116c89c8398e78f04aecb78e3c`;
- exact base `f0d65aa66988e3e1a026e237b65c65a56b098aa9`;
- OPEN / Ready / mergeable=true;
- Required CI exact-head SUCCESS;
- D6 `33255401544` SUCCESS;
- D7 `33255401512` SUCCESS.

Candidate cubre dependency-safe:
- [ 🟡 ] update N-1 y fallos de red/disco/firma/manifest con policy fail-closed;
- [ 🟡 ] recovery/rollback verificable;
- [ 🟡 ] planner/runbook no destructivo para retiro de artifact malo/comunicación.

**No se marca `[x]` hasta merge SHA verificable.** BBB debe revalidar base/head/checks; si integration cambió materialmente, refrescar la misma PR y obtener nuevo exact-head CI. JOBS no mergea código BeatGaler.

**Regla:** no crear release público, no mover stable/latest, no inventar certificados.  
**Gate:** tag→SHA→artefacto demostrable + rollback runbook + integración exact-head verificable.

## Día 25 — Matriz/freeze

### 25.1 — `NEXT AFTER #57 / BBB NIGHT-BBB-008`
- [ ] Web browsers/iPhone + Windows/macOS físicos;
- [ ] auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing;
- [ ] refresh/restart + cero llamadas plataforma inválida.

`NIGHT-BBB-008` autoriza únicamente **REUSE-FIRST dependency-safe matrix audit** después de integrar #57:
- inventariar workflows/fixtures/evidencia existente;
- separar cobertura automatizada de pruebas físicas/credenciales externas;
- cerrar solo gaps F4-matrix internos pequeños sin modificar lógica de producto F2/F3;
- findings de producto vuelven a JOBS para owner correcto;
- un único candidate si existe delta real.

No falsear browser/iPhone/Windows/macOS físicos si no se ejecutan realmente.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
