# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

## Owner actual

**BBB — F4 / 21.2 Upgrade Matrix: FULL OWNER por instrucción RO explícita 2026-08-28.**

BBB consolidó el camino técnico de 21.1 + 21.2 en PR #51. Esto no convierte ninguno en cerrado hasta que el artifact combinado tenga evidencia exact-head válida contra el baseline vigente y quede integrado.

Fuera de scope: signing Windows, notarización macOS, certificados/credenciales, release/beta pública, Día 24.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[ 🟡 ] COMPLETE_TECHNICAL / CIERRE POR CAMINO COMBINADO #51`

Artifact histórico: PR #48 `bbb/f4-21.1-release-manifest` @ `a3ba448e9ded04f73ee77a3556809dcf72e707f5` — técnico completo, pero no integrado.

Handoff BBB Issue #41 `5457967950`: `READY_FOR_INTEGRATION / COMPLETE_TECHNICAL`.

Decisión RO ya resuelta para este slice:
- nombre visible: `Galer`;
- bundle ID: `com.beatgaler.app`.

El trabajo 21.1 fue incorporado por BBB al PR #51 como parte del camino combinado 21.1+21.2. Por tanto #48 queda **superseded para integración solo cuando #51 aterrice**; mientras #51 no esté integrado, 21.1 permanece `[ 🟡 ]`.

Checklist literal:
- [ ] Inventariar VERSION/npm/Cargo/Tauri/Settings y escoger fuente coherente — implementado en candidate; cierre de integración pendiente.
- [ ] Unificar versión/endpoints/channel/capabilities donde existan divergencias reales — implementado; integración pendiente.
- [ ] Incluir/verificar runtimes Windows y recursos universales macOS con digests — implementado; integración pendiente.
- [ ] Checks/tests anti-drift — implementados; exact-head final pendiente.
- [ ] Build/CI aplicable sobre exact head final — pendiente en combinación canónica definitiva.
- [ ] Bundle ID final `com.beatgaler.app` — decisión RO resuelta; integración pendiente.

**Gate 21.1:** no hay versión/endpoints divergentes ni runtime omitido; no se considera satisfecho globalmente hasta integración verificable del camino combinado.

### 21.2 [P1 · DE/QA] — `[ 🟡 ] BBB FULL OWNER / PR #51 ACTIVO`
- [ ] Upgrade desde 0.7.4 preservando settings/SQLite/offline/cache — implementado en candidate #51; cierre pendiente.
- [ ] Instalación limpia + datos corruptos/incompletos con recovery — implementado en candidate #51; cierre pendiente.
- [ ] Artefactos staging desde mismo SHA — workflow/candidate presente; evidencia exact-head final pendiente.

**Artifact canónico de integración:** PR #51 `bbb/task-21.2-upgrade-matrix` — OPEN / DRAFT. Head observado por JOBS: `f70f17ea41cd26bd833bf7ee91949a3e4d752d4e`.

El PR declara y evidencia en código el camino combinado:
- manifest 21.1 + identidad final;
- bridge no destructivo desde app-data 0.7.4;
- preservación SQLite/settings/offline/cache y rollback source intacto;
- recovery conservador de SQLite corrupto;
- upgrade NSIS 0.7.4 → Galer;
- staging Windows + macOS atado al source SHA.

**Preflight JOBS actual:**
- integración canónica ya avanzó a `489d81b...`;
- #51 fue preparado originalmente sobre `14002b29...`;
- el propio contrato del PR exige fresh union + CI si integración se mueve;
- Required CI del head `f70f17e...` estaba `QUEUED` al snapshot de JOBS; D6 del mismo head ya aparecía SUCCESS.

**No marcar 21.1 ni 21.2 `[x]`:** BBB continúa el mismo PR, completa CI/staging exact-head, incorpora el baseline vigente cuando toque integración y repite evidencia si el head cambia.

**BBB NEXT:** continuar #51 dentro de su owner. No signing/notarization/release/D24.

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

**Regla:** 21.1/21.2 pueden construirse en paralelo con F1/F2, pero firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.