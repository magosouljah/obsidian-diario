# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

## Owner actual

**BBB — F4 / 24.2 updater recovery / rollback — `NIGHT-BBB-007`.**

21.1 + 21.2 y 24.1 están cerrados/integrados. D22/D23 conservan dependencias externas de signing/notarization. 24.2 tiene candidate real en PR #57, pero su combinación histórica era contra `672e133...`; la integración avanzó por PR #56 a `f0d65aa...`, por lo que BBB debe refrescar la misma PR y obtener nuevo CI exact-head antes de integración.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[x] DONE / INTEGRATED`

Artifact histórico PR #48 quedó incorporado por el camino combinado PR #51 y GitHub lo reporta CLOSED/MERGED con el mismo merge SHA final.

Decisiones integradas:
- nombre visible `Galer`;
- bundle ID `com.beatgaler.app`;
- fuente coherente de versión/endpoints/channel/capabilities;
- runtimes/recursos y checks anti-drift incorporados en el candidate combinado.

### 21.2 [P1 · DE/QA] — `[x] DONE / INTEGRATED`

**Artifact canónico:** PR #51 `bbb/task-21.2-upgrade-matrix`.

Exact tested head: `0fd9bee8117ca92fb9f713f0d55089f5707a2917` sobre base `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

Evidencia exact-head:
- D7 run `33243436937` — SUCCESS;
- D6 run `33243436890` — SUCCESS;
- Test - Desktop Portability / Required CI run `33243436894` — SUCCESS;
- Upgrade 21.2 Staging run `33243436914` — SUCCESS.

Integración:
- merge SHA `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`;
- parents `3560dc844...` + `0fd9bee...`;
- merge tree `7bbc0640d293749e29330fd8da65bfcf90540153` idéntico al tree del exact tested head;
- `release/desktop-manifest.json` integrado con `Galer` + `com.beatgaler.app`;
- `release/upgrade-matrix.json` integrado con baseline 0.7.4, preservación app-data/SQLite/settings/offline/cache, recovery y same-source-SHA staging.

Issue #41 handoff BBB `5461557463` = `DONE`. PR #48 quedó CLOSED/MERGED al ser incorporado por #51.

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
**Estado:** manifest ya satisfecho por Día 21; certificado/signing siguen externos y no se infieren disponibles.

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

**Artifact:** PR #55 `bbb/task-24.1-release-controls`.

Exact tested head `ba83c87dab8a56163601e913f7764c7f8682b7a6` sobre base `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.

Evidencia exact-head:
- Required CI / Test - Desktop Portability `33248059804` SUCCESS;
- F4 Release Controls `33248059891` SUCCESS;
- D6 `33248059823` SUCCESS;
- D7 `33248059990` SUCCESS.

Integración:
- PR #55 CLOSED/MERGED;
- merge SHA `672e133bc9cb8a47a29d4b34e13fc535290e5681`;
- parents `5b05ca845...` + `ba83c87...`;
- tree `90caa2979bdb4cf4d185d2b6dd8f21e830b01472`.

Requirements satisfechos:
- [x] tag/source SHA binding y checkout del mismo source SHA en release flow;
- [x] checksums/SBOM SPDX/provenance verification;
- [x] channels/rings/minimum versions/kill switch;
- [x] publication fail-closed mientras controles no autoricen release.

**No implica:** signing Windows, notarización macOS ni ejecución de release público.

### 24.2 — `ASSIGNED / IN PROGRESS` — BBB `NIGHT-BBB-007`

Candidate existente, REUSE-FIRST:
- PR #57 `F4 24.2: updater recovery and rollback acceptance`;
- branch `bbb/task-24.2-updater-recovery`;
- candidate head histórico `5c74c0948c43d53b2f8d075cd66ba70c953da3c5` sobre base `672e133bc9cb8a47a29d4b34e13fc535290e5681`;
- Test - Desktop Portability `33252718637` SUCCESS;
- D6 `33252718614` SUCCESS;
- D7 `33252718625` SUCCESS;
- Upgrade 21.2 Staging `33252718609` SKIPPED/no aplica.

El candidate implementa dependency-safe:
- [ 🟡 ] update N-1 y fallos de red/disco/firma/manifest con policy fail-closed;
- [ 🟡 ] recovery/rollback verificable;
- [ 🟡 ] planner/runbook no destructivo para retiro de artefacto malo/comunicación.

**No se marca PASS todavía:** GitHub vivo avanzó a `f0d65aa...` por PR #56 y #57 ya no está sobre el baseline actual. Los checks verdes de `5c74c094...` prueban el candidate histórico, no la nueva combinación. `NIGHT-BBB-007` debe refrescar **la misma PR**, obtener CI sobre el nuevo exact head y, si sigue Ready/mergeable, hacer race-check + merge protegido.

**Regla de ejecución:** no crear release público, no mover stable/latest, no inventar certificados. Los fallos de firma pueden probarse con fixtures/validación segura si no requieren credencial real.

**Gate:** tag→SHA→artefacto demostrable + rollback runbook + integración exact-head verificable.

## Día 25 — Matriz/freeze

### 25.1
- [ ] Web browsers/iPhone + Windows/macOS físicos;
- [ ] auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing;
- [ ] refresh/restart + cero llamadas plataforma inválida.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** trabajo técnico dependency-safe puede avanzar cross-phase, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.
