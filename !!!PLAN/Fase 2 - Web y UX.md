# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, slices frontend independientes pueden avanzar cuando sus dependencias reales están satisfechas, pero el siguiente owner/task se asigna explícitamente.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.  
**Estado F2:** 11.1 y 12.2 cerrados; D8 ya PASS; siguiente slice F2 todavía **UNASSIGNED**.

## Owner actual

**AAA cerró F2 / 12.2 y no tiene una nueva asignación activa.**

- 11.1 / PR #47: cerrado e integrado.
- 12.2 / PR #50: cerrado e integrado.
- AAA handoff Issue #41 `5460303449`: `STATUS: DONE`, `NEXT_WITHIN_AREA: none`.
- No iniciar automáticamente 11.2, 12.1 ni 15.1. JOBS/RO debe reasignar explícitamente.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 [P1 · FE/DL] — `[x] DONE / INTEGRATED`

Artifact: PR #47 `aaa/f2-11.1-design-foundations` refreshed exact head `fdc6463e6b81efedc547c97595529d28e0ba2d83`.

Después de integrar PR #49 / D8.1, AAA reutilizó #47, incorporó el baseline post-#49 y resolvió el overlap material de `AccountGate.tsx` + test DOM preservando como autoridad la seguridad de sesión de #49. El delta de 11.1 permaneció limitado a UI/a11y foundations.

Evidencia exact-head:
- Required CI #429 / run `33216364174` — SUCCESS;
- D6 #68 / `33216364104` — SUCCESS;
- D7 #39 / `33216364074` — SUCCESS;
- merge a `integration-v0.8.0-alpha.1`: `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

Checklist literal:
- [x] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion.
- [x] Documentar estados; retirar duplicación inline empezando por AccountGate.
- [x] Corregir autofill, contraste, loading y layout 390–430 px.
- [x] Tests DOM/a11y afectados.
- [x] Build/CI aplicable verde sobre exact head e integración verificable.

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa — `READY_TO_WORK / UNASSIGNED`
- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth popup/redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias:** las APIs/ciclo de cuenta de D8 ya están integradas y Gate D8 = PASS mediante Issue #41 `5460381842`. Por dependencia, 11.2 ya puede evaluarse como slice activo cuando JOBS/RO lo asigne. **No se asigna por inferencia.**

**Gate:** variantes de cuenta alcanzables, legibles y recuperables.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 [P1 · BE/FE] — Bootstrap y load — `READY_TO_WORK / UNASSIGNED`
- [ ] Índice vacío atómico en control plane.
- [ ] Separar empty/no-results/offline/auth/cloud failure.
- [ ] Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.
- [ ] Instrumentar startup por fases, comparar cold/warm y corregir regresión de carga inicial reportada.

D8 y 12.2 ya no son blockers. JOBS/RO decide explícitamente la prioridad entre 11.2, 12.1 y otros slices dependency-safe.

### 12.2 [P1/P2 · FE/DL] — Biblioteca — `[x] DONE / INTEGRATED`
- [x] Header/search/sort/tags/selection accesibles.
- [x] Card con jerarquía fija y estados sin salto.
- [x] Grid 390/768/1024/desktop; touch no depende de hover.

**Artifact canónico:** PR #50 `aaa/f2-12.2-library` exact tested head `b7a31d686a361f559783b5dc7cb8bebc5aa04e8e`, construido directamente sobre baseline post-#52 `c25ec6a824bc0ae60fbf65858d53be26d453f205`.

**Delta final:** 1 commit / 4 files; sin cambios a AccountGate/auth/session/backend/data-plane/infra.

**Evidencia exact-head:**
- Required CI #452 / run `33233250213` — SUCCESS;
- D6 #89 / `33233250229` — SUCCESS;
- D7 #62 / `33233250210` — SUCCESS;
- Productive Temp Auth Compile #173 / `33233250206` — SUCCESS;
- merge a integración `39e894c0fcefffa5d3222e3c135a086937a10a8e`;
- AAA handoff Issue #41 `5460303449` = `STATUS: DONE`.

12.2 queda cerrado; esto no declara F2 globalmente cerrada.

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
- [ ] **Follow-up RO de D8:** acción visible **“Vaciar Trash”** que haga borrado permanente, con confirmación fuerte y recent reauth antes de ejecutar.

El follow-up “Vaciar Trash” fue registrado por WOZ al cerrar D8; pertenece a F2/15.1 y **no fue implementado por PR #53**. Registrar ≠ asignar ni cerrar.

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