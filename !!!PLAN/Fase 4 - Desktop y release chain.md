# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, preparación/auditoría independiente de esta fase puede empezar antes de Fase 1/2/3 si no requiere prerequisitos todavía inexistentes.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

## Estado paralelo

**BBB — F4 / 21.1 readiness audit:** `READY_IF_BLOCKED`  
BBB tiene primero un re-review D7 disponible sobre PR #46 @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`. Al entregar ese handoff, si no existe otro delta crítico D7 listo, pasa automáticamente a este audit READ ONLY.

Scope del audit standby:
- inventariar VERSION/npm/Cargo/Tauri/Settings;
- endpoints/channels/capabilities por plataforma;
- runtimes/resources Windows/macOS y digests ya existentes;
- identificar divergencias exactas que impedirían un manifest único desde un mismo SHA.

Fuera de scope: elegir bundle ID final, cambiar archivos, firmar, notarizar, generar release o ejecutar 22/23/24. El audit no marca 21.1 `[x]`.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO]
- [ ] Fijar bundle ID final antes de migrar app-data/updater.
- [ ] Unificar VERSION/npm/Cargo/Tauri/Settings, endpoint y channel.
- [ ] Incluir runtimes Windows presentes en Cloud y recursos universales macOS con digests.

### 21.2 [P1 · DE/QA]
- [ ] Upgrade desde 0.7.4 preservando settings/SQLite/offline/cache.
- [ ] Instalación limpia + datos corruptos/incompletos con recovery.
- [ ] Artefactos staging desde mismo SHA.

**Gate:** no versión/endpoints divergentes ni runtime omitido.

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

## Día 24 — Updater/procedencia/rollback

### 24.1
- [ ] tag protegido = SHA consumido;
- [ ] checksums/SBOM/provenance;
- [ ] channels/rings/minimum version/kill switch.

### 24.2
- [ ] update N-1 y fallos de red/disco/firma/manifest;
- [ ] recovery/rollback;
- [ ] retiro artefacto malo/comunicación.

**Gate:** tag→SHA→artefacto demostrable + rollback runbook.

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

**Regla:** prep/audit puede adelantarse; firma/notarización/release/beta solo con prerequisitos reales.