# Fase 4 — Artefactos desktop confiables y release chain

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 21–25 de septiembre  
**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

## Día 21 — 21 de septiembre — Manifest e identidad únicos

**Resultado:** Web, backend y desktop comparten versión, endpoints y matriz de capabilities.

### Tarea 21.1 [P1 · DE/RO] — Release manifest

- [ ] Fijar bundle ID final antes de migrar app-data/updater.
- [ ] Unificar VERSION/npm/Cargo/Tauri/Settings, endpoint y channel.
- [ ] Incluir runtimes Windows presentes en Cloud y recursos universales macOS con digests.

### Tarea 21.2 [P1 · DE/QA] — Migración y compatibilidad

- [ ] Probar upgrade desde 0.7.4 y preservar settings/SQLite/offline/cache.
- [ ] Probar instalación limpia y datos corruptos/incompletos con recovery seguro.
- [ ] Generar artefactos de staging desde el mismo SHA.

**Dependencias:** release branch y app identity del Día 19.  
**Evidencia:** manifest diff, version check y upgrade test.  
**Gate de salida:** no hay versión/endpoints divergentes ni runtime omitido.

## Día 22 — 22 de septiembre — Windows firmado

**Resultado:** instalador y binarios Windows tienen publisher verificable.

### Tarea 22.1 [P0 · DE/OP] — Authenticode

- [ ] Integrar certificado/servicio de firma sin exponer private key.
- [ ] Firmar binarios e instalador NSIS con timestamp; verificar cadena tras descarga.
- [ ] Conservar firma Tauri de updater como capa separada.

### Tarea 22.2 [P1 · QA/DE] — Matriz limpia

- [ ] Instalación/upgrade/uninstall como usuario estándar y UAC esperado.
- [ ] SmartScreen/antivirus, paths no ASCII/largos, offline/poor network y sleep/wake.
- [ ] DAWs y versiones Windows declaradas por product owner; updater válido e inválido.

**Dependencias:** certificado disponible y manifest Día 21.  
**Evidencia:** `signtool verify`, timestamp, screenshots/logs clean-machine.  
**Gate de salida:** Windows no muestra publisher desconocido y core flows pasan tras instalar.

## Día 23 — 23 de septiembre — macOS firmado y notarizado

**Resultado:** DMG/app aceptados por Gatekeeper en Intel y Apple Silicon soportados.

### Tarea 23.1 [P0 · DE/OP] — Developer ID

- [ ] Revisar entitlements/hardened runtime y firmar nested binaries en orden correcto.
- [ ] Enviar con `notarytool`, esperar Accepted, staple ticket a app/DMG y verificar offline.
- [ ] Custodiar/rotar certificado y credenciales mediante secretos de entorno protegido.

### Tarea 23.2 [P1 · QA/DE] — Matriz física

- [ ] Instalar desde descarga en cuenta limpia, verificar Gatekeeper/Finder y first run.
- [ ] Intel + Apple Silicon, macOS mínimo 12 y versiones declaradas; sleep/wake/firewall/disk pressure.
- [ ] DAWs declarados, updater válido/inválido y preservación de app-data.

**Dependencias:** membership/certificado y binarios universales.  
**Evidencia:** codesign/notary/stapler/spctl y logs físicos.  
**Gate de salida:** artefacto notarizado/stapled y core flows pasan en ambas arquitecturas prometidas.

## Día 24 — 24 de septiembre — Updater, procedencia y rollback

**Resultado:** una mala versión puede detenerse o revertirse sin sobrescribir evidencia.

### Tarea 24.1 [P0/P1 · DE/OP] — Cadena inmutable

- [ ] Tag protegido debe resolver exactamente al SHA de los runs consumidos.
- [ ] Checksums, SBOM y provenance por artefacto; eliminar selección arbitraria y `--clobber` final.
- [ ] Canales internal/beta/stable, porcentaje/rings, minimum version y kill switch.

### Tarea 24.2 [P1 · QA/DE] — Lifecycle updater

- [ ] Update desde N-1, cancelación, red cortada, disco lleno, firma inválida y manifest alterado.
- [ ] Reinicio/recovery y rollback a la versión compatible anterior.
- [ ] Ensayar retiro de `latest.json`/artefacto malo y comunicación de incidente.

**Dependencias:** artefactos firmados.  
**Evidencia:** release ledger, attestation y rollback rehearsal.  
**Gate de salida:** tag→SHA→artefacto es demostrable y rollback cumple runbook.

## Día 25 — 25 de septiembre — Matriz cross-platform y freeze estructural

**Resultado:** candidato beta conserva funciones y el rediseño deja de cambiar estructura.

### Tarea 25.1 [P1 · QA/FE/DE] — Suite completa

- [ ] Web Chrome/Safari/Firefox/iPhone; Windows y macOS físicos; cuenta limpia y upgrade.
- [ ] Auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing por capability.
- [ ] Comparar datos al refresh/restart y confirmar cero llamadas de plataforma inválida.

### Tarea 25.2 [P1/P2 · DL/RO] — Design freeze

- [ ] Aprobar tokens, navegación, library, drawer, player, settings y wizard.
- [ ] Registrar P2/P3 restantes; solo a11y/copy/error/regresión entra antes de RC.
- [ ] Preparar guion beta, formulario y criterios P0/P1/P2.

**Dependencias:** Fases 2–4.  
**Evidencia:** matriz firmada, snapshots y backlog triage.  
**Gate de salida:** beta candidate `0.9.0-beta.1`, 0 P0 conocido y ningún P1 core conocido.
