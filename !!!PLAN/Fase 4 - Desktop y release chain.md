# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, preparación/auditoría independiente de esta fase puede empezar antes de Fase 1/2/3 si no requiere prerequisitos todavía inexistentes.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

## Estado paralelo actual

**BBB — READ ONLY / F4 21.1 readiness audit:** `[ 🟡 ]`  
Baseline de producto para auditoría: `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.

Scope inmediato:
- inventariar VERSION/npm/Cargo/Tauri/Settings;
- endpoints/channels/capabilities por plataforma;
- runtimes/resources Windows/macOS y digests ya existentes;
- identificar divergencias exactas que impedirían un manifest único desde un mismo SHA.

Fuera de scope: elegir bundle ID final, cambiar archivos, firmar, notarizar, generar release o ejecutar 22/23/24. Este audit **no marca 21.1 `[x]`**; prepara el slice reutilizable.

---

## Día 21 — Manifest e identidad únicos

**Resultado:** Web, backend y desktop comparten versión, endpoints y matriz de capabilities.

### Tarea 21.1 [P1 · DE/RO] — Release manifest

- [ ] Fijar bundle ID final antes de migrar app-data/updater.
- [ ] Unificar VERSION/npm/Cargo/Tauri/Settings, endpoint y channel.
- [ ] Incluir runtimes Windows presentes en Cloud y recursos universales macOS con digests.

### Tarea 21.2 [P1 · DE/QA] — Migración y compatibilidad

- [ ] Probar upgrade desde 0.7.4 y preservar settings/SQLite/offline/cache.
- [ ] Probar instalación limpia y datos corruptos/incompletos con recovery seguro.
- [ ] Generar artefactos de staging desde el mismo SHA.

**Dependencias de cierre:** release branch y app identity final.  
**Evidencia:** manifest diff, version check y upgrade test.  
**Gate de salida:** no hay versión/endpoints divergentes ni runtime omitido.

## Día 22 — Windows firmado

### Tarea 22.1 [P0 · DE/OP] — Authenticode
- [ ] Integrar certificado/servicio de firma sin exponer private key.
- [ ] Firmar binarios e instalador NSIS con timestamp; verificar cadena tras descarga.
- [ ] Conservar firma Tauri de updater como capa separada.

### Tarea 22.2 [P1 · QA/DE] — Matriz limpia
- [ ] Instalación/upgrade/uninstall como usuario estándar y UAC esperado.
- [ ] SmartScreen/antivirus, paths no ASCII/largos, offline/poor network y sleep/wake.
- [ ] DAWs/versiones Windows declaradas; updater válido e inválido.

**Dependencias reales:** certificado disponible + manifest apto.  
**Gate:** Windows no muestra publisher desconocido y core flows pasan tras instalar.

## Día 23 — macOS firmado y notarizado

### Tarea 23.1 [P0 · DE/OP] — Developer ID
- [ ] Entitlements/hardened runtime y firma nested binaries correcta.
- [ ] `notarytool` Accepted + staple + verificación offline.
- [ ] Custodia/rotación de credenciales en entorno protegido.

### Tarea 23.2 [P1 · QA/DE] — Matriz física
- [ ] Descarga/cuenta limpia/Gatekeeper/Finder/first run.
- [ ] Intel + Apple Silicon, macOS mínimo 12 y versiones declaradas.
- [ ] DAWs, updater y preservación app-data.

**Dependencias reales:** membership/certificado + binarios universales.  
**Gate:** artefacto notarizado/stapled y core flows pasan en ambas arquitecturas prometidas.

## Día 24 — Updater, procedencia y rollback

### Tarea 24.1 [P0/P1 · DE/OP]
- [ ] Tag protegido resuelve exactamente al SHA consumido.
- [ ] Checksums, SBOM y provenance; sin selección arbitraria/`--clobber` final.
- [ ] Canales internal/beta/stable, rings, minimum version y kill switch.

### Tarea 24.2 [P1 · QA/DE]
- [ ] Update N-1, cancelación, red cortada, disco lleno, firma/manifest inválido.
- [ ] Reinicio/recovery y rollback a versión compatible.
- [ ] Ensayar retiro de artefacto malo y comunicación.

**Dependencias:** artefactos firmados.  
**Gate:** tag→SHA→artefacto demostrable y rollback cumple runbook.

## Día 25 — Matriz cross-platform y freeze estructural

### Tarea 25.1 [P1 · QA/FE/DE]
- [ ] Web Chrome/Safari/Firefox/iPhone; Windows/macOS físicos; limpia + upgrade.
- [ ] Auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing por capability.
- [ ] Refresh/restart y cero llamadas de plataforma inválida.

### Tarea 25.2 [P1/P2 · DL/RO]
- [ ] Aprobar tokens, navegación, library, drawer, player, settings y wizard.
- [ ] Registrar P2/P3; solo a11y/copy/error/regresión entra antes de RC.
- [ ] Preparar guion beta, formulario y criterios P0/P1/P2.

**Dependencias de cierre:** Fases 2–4 suficientemente integradas.  
**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 conocido y ningún P1 core conocido.

**Regla:** preparación/auditoría puede adelantarse; firma/notarización/release/beta solo ocurren con prerequisitos reales.