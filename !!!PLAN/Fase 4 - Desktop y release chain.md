# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, 21.1 puede avanzar en paralelo si no requiere prerequisitos todavía inexistentes.

**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

## Owner actual

**BBB — F4 / 21.2 Upgrade Matrix: FULL OWNER / PRECHECK por instrucción RO explícita 2026-08-28.**

El cambio 21.1 → 21.2 no convierte 21.1 en cerrado: PR #48 sigue OPEN/DRAFT y no integrado. BBB puede hacer precheck dependency-safe de 21.2 y preparar casos sobre el contrato existente, pero ningún resultado de 21.2 sustituye la integración verificable de 21.1.

**No vuelve automáticamente a D7/PR #46.** D7 ya está `[x]/PASS` y WOZ está en D8.

Fuera de scope de 21.2: signing Windows, notarización macOS, certificados/credenciales, release/beta pública, Día 24.

---

## Día 21 — Manifest e identidad únicos

### 21.1 [P1 · DE/RO] — `[ 🟡 ]` COMPLETE_TECHNICAL / INTEGRACIÓN PENDIENTE

Artifact canónico: PR #48 `bbb/f4-21.1-release-manifest` @ `a3ba448e9ded04f73ee77a3556809dcf72e707f5` — **OPEN / DRAFT / no mergeado**.

Handoff BBB Issue #41 `5457967950`: `READY_FOR_INTEGRATION / COMPLETE_TECHNICAL`.

#### Evidencia del candidate #48
- RO resolvió identidad visible/final para este slice: nombre `Galer`; bundle ID `com.beatgaler.app`.
- VERSION y fuentes package/Cargo/Tauri/Settings normalizadas mediante fuente canónica y drift guards.
- updater endpoint/channel/feed normalizados con fuente de manifest consistente.
- Windows FFmpeg incluido/pinneado con digest, installer/runtime provenance y guards equivalentes.
- Windows/macOS release artifacts, provenance y manifest tooling quedan amarrados al mismo source SHA dentro del candidate.
- D6 y D7 aplicables verdes; Required CI #412 `33212138329` = SUCCESS; Web/shared, PostgreSQL recovery, Windows, macOS arm64/x86_64 y supply-chain verdes según handoff exact-head.

El audit anterior `5456640788` queda como evidencia histórica de gaps de entrada, **no** como estado vivo: G1–G5 fueron tratados en el candidate #48 y la decisión RO de bundle ID ya existe.

#### Preflight JOBS 2026-08-28

- PR #48 continúa `OPEN / DRAFT / no mergeado` aunque su handoff técnico sea verde.
- Comparación de #48 contra integración canónica `e25c604...`: `diverged`, `behind_by=49`; su merge-base sigue en `23bded948...`.
- #48 y PR #49 tocan `package.json`; por tanto el CI verde del head `a3ba448...` no prueba la combinación posterior a D8/8.1.

#### STOP/PENDING 21.1

**No marcar 21.1 `[x]` todavía.** Antes del cierre debe existir evidencia verificable de un artifact #48 actualizado contra la integración vigente después de #49, estado de PR apto para integración por el flujo autorizado, CI exact-head aplicable verde e integración canónica demostrable. JOBS no decide el método técnico para refrescar el branch ni mergea código BeatGaler.

Checklist literal:
- [ ] Inventariar VERSION/npm/Cargo/Tauri/Settings y escoger una fuente coherente de versión sin cambiar semántica de producto — cubierto en candidate; cierre post-integración pendiente.
- [ ] Unificar versión/endpoints/channel/capabilities donde existan divergencias reales — cubierto en candidate; revalidación post-baseline pendiente.
- [ ] Incluir/verificar runtimes Windows presentes en Cloud y recursos universales macOS con digests — cubierto en candidate; revalidación post-baseline pendiente.
- [ ] Añadir checks/tests que fallen si las fuentes vuelven a divergir — cubierto en candidate; revalidación post-baseline pendiente.
- [ ] Ejecutar build/CI aplicable sobre exact head — #412 SUCCESS en candidate; falta exact-head tras incorporar integración vigente si cambia el head.
- [ ] Bundle ID final — decisión RO existente: `com.beatgaler.app`; cierre global pendiente de integración.

**Gate 21.1:** no hay versión/endpoints divergentes ni runtime omitido; no se considera satisfecho globalmente hasta integración verificable del candidate actualizado.

### 21.2 [P1 · DE/QA] — `[ 🟡 ]` BBB FULL OWNER / PRECHECK ACTIVO
- [ ] Upgrade desde 0.7.4 preservando settings/SQLite/offline/cache.
- [ ] Instalación limpia + datos corruptos/incompletos con recovery.
- [ ] Artefactos staging desde mismo SHA.

**Asignación vigente:** Issue #41 `5458104890`/último handoff RO-BBB: 21.2 asignado a BBB con estrategia dependency-safe mientras #48/21.1 no esté integrado. El trabajo útil permitido ahora es preflight, duplicate-check, matriz/casos y reutilización verificable; la validación final que dependa del release manifest canónico debe esperar a la integración de 21.1.

**BBB NEXT:** continuar 21.2 Upgrade Matrix dentro de ese límite; en paralelo, cooperar con el flujo autorizado para que #48 incorpore el baseline posterior a #49, revalide exact-head y pueda integrarse. No declarar 21.1 ni 21.2 `[x]` por anticipado.

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

**Regla:** 21.1 puede adelantarse y ya tiene candidate técnico completo; 21.2 puede hacer trabajo dependency-safe bajo BBB; firma/notarización/release/beta siguen bloqueadas por sus prerequisitos reales.