# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, 21.1 puede avanzar en paralelo si no requiere prerequisitos todavía inexistentes.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

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

**No vuelve automáticamente a D7/PR #46.** WOZ absorbió el cierre D7.

`RO DECISION REQUIRED`: BBB no inventa bundle ID final. Si esa decisión falta, aísla ese único subitem y continúa todo lo demás de 21.1.

Fuera de scope: 21.2, firma Windows, notarización macOS, certificados/credenciales, release/beta.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[ 🟡 ]` BBB FULL OWNER
- [ ] Inventariar VERSION/npm/Cargo/Tauri/Settings y escoger una fuente coherente de versión sin cambiar semántica de producto.
- [ ] Unificar versión/endpoints/channel/capabilities donde existan divergencias reales.
- [ ] Incluir/verificar runtimes Windows presentes en Cloud y recursos universales macOS con digests.
- [ ] Añadir checks/tests que fallen si las fuentes vuelven a divergir.
- [ ] Ejecutar build/CI aplicable sobre exact head.
- [ ] Bundle ID final: `RO DECISION REQUIRED` si todavía no existe decisión verificable.

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