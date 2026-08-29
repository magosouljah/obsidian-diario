# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices frontend independientes pueden avanzar cuando sus dependencias reales están satisfechas, pero el owner/task se asigna explícitamente.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable al preflight JOBS CYCLE 007:** `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto. PR #58 ya existe y tiene Required CI exact-head verde, pero aún no está integrado.

## Owner actual

**AAA — F2 / 12.1 — FULL OWNER — `NIGHT-AAA-008`.**

- PR #58 `aaa/night-12.1-bootstrap-load` está OPEN/Ready/mergeable=true.
- Exact head: `d7cc93f9c4318be7f993bd033483c4e7f1834a55`; base `f0d65aa...`.
- Required CI `33254699647` = SUCCESS sobre exact head.
- #58 cubre el **slice A**: lazy artwork + taxonomy mínima + startup timing/tests. No cierra atomic empty-index, pagination/window/memory ni cold/warm residual.
- `NIGHT-AAA-008`: race-check + merge protegido si la combinación sigue válida; después comenzar únicamente atomic empty-index como siguiente sub-slice. No abrir duplicate de #58.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 [P1 · FE/DL] — `[x] DONE / INTEGRATED`

PR #47 exact head `fdc6463e6b81efedc547c97595529d28e0ba2d83`; Required CI `33216364174` SUCCESS; merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

- [x] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion.
- [x] Documentar estados; retirar duplicación inline empezando por AccountGate.
- [x] Corregir autofill, contraste, loading y layout 390–430 px.
- [x] Tests DOM/a11y afectados.
- [x] Build/CI aplicable verde sobre exact head e integración verificable.

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa — `[x] DONE / INTEGRATED`

PR #54 exact tested head `e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; Required CI `33239731204` SUCCESS; merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

- [x] Login/register/MFA/verify/reset/recovery/error/offline.
- [x] OAuth popup/redirect, blocked/cancel/retry.
- [x] Tests/acceptance Web/DOM y a11y afectada; D6/D7 sin regresión.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 [P1 · BE/FE] — Bootstrap y load — `IN PROGRESS` — AAA `NIGHT-AAA-008`

- [ ] **Índice vacío atómico en control plane.** Siguiente sub-slice explícito después de integrar #58; aún no PASS.
- [ 🟡 ] **Separar empty/no-results/offline/auth/cloud failure.** Implementado en #58 candidate; Required CI verde; aún no integrado.
- [ 🟡 ] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** Lazy artwork está en #58 candidate; pagination/window/memory siguen abiertos.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Timing está en #58 candidate; cold/warm cuantificado y residual tuning siguen abiertos.

**Regla:** integrar #58 no convierte 12.1 completo en `[x]`. Evidence-before-claim por subrequisito.

### 12.2 [P1/P2 · FE/DL] — Biblioteca — `[x] DONE / INTEGRATED`

PR #50 exact tested head `b7a31d686a361f559783b5dc7cb8bebc5aa04e8e`; Required CI `33233250213`, D6 `33233250229`, D7 `33233250210`, compile `33233250206` SUCCESS; merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.

- [x] Header/search/sort/tags/selection accesibles.
- [x] Card con jerarquía fija y estados sin salto.
- [x] Grid 390/768/1024/desktop; touch no depende de hover.

## Día 13 — Import, Review y bulk edit

### 13.1 [P1 · FE/BE]
- [ ] Save All durable con resumen parcial.
- [ ] Bulk conflict-safe o deshabilitado honestamente.
- [ ] Garbage journal limpia uploads huérfanos.

### 13.2 [P1 · FE/DL/QA]
- [ ] ReviewShell Import/Edit/Bulk, CTA fija y progreso N/N.
- [ ] Errores item/retry/skip/cancel/confirmación durable.
- [ ] E2E multi-file/conflicto/refresh/rollback.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Día 14 — Playback, queue y descargas

### 14.1 [P1/P2 · FE/BE]
- [ ] MediaSource/Range + fallback seguro.
- [ ] Evitar archivos gigantes completos en RAM.
- [ ] Cancel/resume seguro y liberar buffers/object URLs.

### 14.2 [P2 · FE/DL/QA]
- [ ] Índice activo/shortcuts/seek/shuffle/repeat/error recoverable.
- [ ] Queue/volumen responsive.
- [ ] Safari/Firefox/Chrome/iPhone, archivos pequeños/grandes, red degradada.

**Gate:** no crash por fallback soportado y pista activa inequívoca.

## Día 15 — Settings, Trash, accesibilidad y YouTube Web

### 15.1 [P1 · FE/DL] — `QUEUED / UNASSIGNED`
- [ ] SettingsShell desktop/móvil; Account/Plan/Preferences/Trash/legal.
- [ ] State machines reales para catálogo/cache/Trash/updater.
- [ ] Acciones peligrosas separadas, confirmadas y con reauth.
- [ ] **Follow-up RO de D8:** acción visible “Vaciar Trash” con borrado permanente, confirmación fuerte y recent reauth.

### 15.2 [P2 · QA/DL]
- [ ] Dialog/focus restoration/live regions/labels/contraste/zoom/reduced motion.
- [ ] Reemplazar controles/glifos vacíos y alerts/confirms nativos.
- [ ] Baseline visual S01–S59 alcanzables.

### 15.3 [P1 · FE/BE/QA] — YouTube Web sin Tauri

**Regla de producto:** YouTube existe en Desktop y Web. El `false` actual de `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` es temporal.

#### A. Contrato compartido
- [ ] Interface channel status/connect/disconnect/upload/schedule/cancel/retry/progress.
- [ ] UI compartida sin dependencia directa a `src/lib/tauri.ts`.
- [ ] `src/platform/capabilities.ts` como fuente visible.
- [ ] No activar capability Web hasta gate real.

#### B. Desktop adapter
- [ ] Encapsular Tauri/Rust actual detrás del contrato sin reescritura innecesaria.
- [ ] Mantener Desktop Direct/Offline/YouTube verdes.

#### C. Backend YouTube Web
- [ ] OAuth server-side con state validado y callbacks/orígenes controlados.
- [ ] Tokens/provider secrets cifrados en persistencia durable Fase 1.
- [ ] Endpoints tenant-scoped para status/connect/jobs/schedule/progress/cancel/retry.
- [ ] Jobs idempotentes y reconciliables.
- [ ] Punto de enforcement quotas/entitlements para 18.1.

#### D. Web adapter puro
- [ ] Solo HTTP/Web APIs seguras; prohibido Tauri/localhost helper/Desktop dependency.
- [ ] OAuth popup/redirect/blocked/cancel/retry/expiry/reconnect.
- [ ] Errores humanos sin terminología interna.

#### E. Job/upload Web
- [ ] No cargar archivos grandes completos en RAM si hay streaming/chunked seguro.
- [ ] Progreso durable tras refresh.
- [ ] Cancel/retry bounded y estado final inequívoco.
- [ ] Schedule timezone explícito + validación server-side.

#### F. UI compartida
- [ ] Selección → Visual/crop → Metadata/Presets → Visibilidad/Schedule → canal → progreso/recovery.
- [ ] Diferencia Desktop/Web en adapters/capabilities, no dos wizards.
- [ ] Estados accesibles/responsive.

#### G. Evidencia
- [ ] Unit contrato/capabilities/validaciones.
- [ ] DOM: intento YouTube Web→Tauri = FAIL.
- [ ] Integration UI→Web adapter→backend y Desktop sin regresión.
- [ ] Backend: tenant isolation/OAuth state/token secrecy/idempotencia/schedule/cancel/retry.
- [ ] E2E controlado connect→upload→progress→result + cancel/retry/disconnect.
- [ ] CI cross-platform Desktop Direct/Offline/YouTube verde.

**Dependencias reales de 15.3:** auth/session + persistencia durable aptas para OAuth/provider data.  
**Gate:** upload YouTube Web controlado end-to-end sin Tauri/helper, estado durable y secretos control-side; Desktop conserva funcionalidades. Solo entonces capability Web = true.

### Gates posteriores de 15.3
- 16.1: callbacks/entornos separados.
- 18.1: quotas/entitlements server-side.
- 25.1: matriz cross-platform/browser.
- Gates de publicación permanecen obligatorios.
