# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, 21.1 puede avanzar en paralelo si no requiere prerequisitos todavía inexistentes.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

## Owner actual

**BBB — F4 / 21.1 Release Manifest: FULL OWNER hasta cierre.**

BBB hace el ciclo completo de 21.1:
- preflight/duplicate-check;
- audit de fuentes actuales;
- implementación de normalización dentro de 21.1 cuando sea técnicamente segura;
- corrección de sus propias regresiones;
- tests/checks de consistencia;
- build/CI aplicable;
- handoff con evidencia.

**No vuelve automáticamente a D7/PR #46.** D7 ya está `[x]/PASS` y WOZ avanzó a D8.

`RO DECISION REQUIRED`: BBB no inventa bundle ID final. Si esa decisión falta, aísla ese único subitem y continúa todo lo demás de 21.1.

Fuera de scope: 21.2, firma Windows, notarización macOS, certificados/credenciales, release/beta.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[ 🟡 ]` BBB FULL OWNER / FINDING ACTIVO

Audit BBB Issue #41 `5456640788`, base revisada `23bded948c4377b28fc48a72378816968d4cd413`: **READ ONLY / FINDING**. No cierre ni `[x]`.

#### REUSE verificado
- VERSION `0.8.0-alpha.1` y package/package-lock/Cargo/Tauri/Settings ya alineados mediante `scripts/version.mjs`.
- Node `22.23.2`, Rust `1.98.0` y runtime source pins existen.
- Runtime provenance registra SHA/gitSha/bytes y workflows emiten SHA256SUMS.
- macOS ya tiene FFmpeg/Node/Bot API universales con verificaciones y provenance.
- Windows ya stagea/verifica Node + Bot API y digests instalados.
- Tauri capability declaration no diverge Windows/macOS.
- Release workflow ya exige Windows/macOS desde el mismo `head_sha`, VERSION/tag coherentes y genera un `latest.json` común.

#### GAP verificado
1. **G1 — bundle ID final:** `vtm.beatgaler.playground` sigue presente; decisión final = `RO DECISION REQUIRED`.
2. **G2 — updater endpoint:** duplicado entre `tauri.conf.json`, compile-time `BEATGALER_UPDATER_ENDPOINT` y workflows; falta fuente canónica/drift guard.
3. **G3 — channel/feed:** beta/stable existe en semántica de versión, pero no como invariant del updater/feed; falta fuente canónica de channel/ring.
4. **G4 — Windows FFmpeg:** runtime requerido por producción no está incluido/verificado en packaging Windows equivalente a macOS.
5. **G5 — manifest tooling SHA:** `release-desktop-updater.yml` verifica que builds Windows/macOS compartan SHA, pero el generator `scripts/updater-manifest.mjs` no queda demostrado desde ese mismo SHA.

#### DEPENDENCIES
- G1 requiere decisión RO/DE; BBB no la inventa.
- G2/G3 que requieran escoger semántica pública de endpoint/channel se escalan a DE/WOZ/RO; BBB puede continuar normalización segura que no tome esa decisión.
- Signing/notarization/certs/publication/D24 siguen fuera de scope.
- `wdio:default` no es divergencia 21.1, pero política final de permisos debe decidirse antes de release público.

#### NEXT_WITHIN_AREA BBB
- continuar 21.1 sin duplicar artifact;
- resolver G2/G3 solo hasta donde exista decisión verificable;
- stage/package Windows FFmpeg + provenance/digest/executability guard;
- fijar/assert release manifest tooling al mismo SHA de artifacts;
- añadir drift/consistency tests y CI exact-head;
- aislar G1 como `RO DECISION REQUIRED` si sigue sin decisión;
- entregar evidencia; no marcar 21.1 `[x]` desde el audit.

Checklist literal:
- [ ] Inventariar VERSION/npm/Cargo/Tauri/Settings y escoger una fuente coherente de versión sin cambiar semántica de producto — REUSE verificado; cierre global pendiente.
- [ ] Unificar versión/endpoints/channel/capabilities donde existan divergencias reales — gaps G2/G3 abiertos.
- [ ] Incluir/verificar runtimes Windows presentes en Cloud y recursos universales macOS con digests — G4 abierto.
- [ ] Añadir checks/tests que fallen si las fuentes vuelven a divergir — pendiente de delta.
- [ ] Ejecutar build/CI aplicable sobre exact head — pendiente de delta.
- [ ] Bundle ID final: `RO DECISION REQUIRED`.

**Gate 21.1:** no hay versión/endpoints divergentes ni runtime omitido; lo que dependa literalmente del bundle ID final no se marca `[x]` hasta decisión RO.

### 21.2 [P1 · DE/QA]
- [ ] Upgrade desde 0.7.4 preservando settings/SQLite/offline/cache.
- [ ] Instalación limpia + datos corruptos/incompletos con recovery.
- [ ] Artefactos staging desde mismo SHA.

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

**Regla:** 21.1 sí puede adelantarse y ser propiedad completa de BBB; firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.