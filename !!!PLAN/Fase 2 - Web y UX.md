# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, slices frontend independientes pueden avanzar antes de cerrar Fase 1 si no dependen materialmente de sus APIs pendientes.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

## Estado paralelo actual

**AAA — F2 / 11.1 Design foundations slice:** `[ 🟡 ] READY_TO_WORK`  
Baseline de producto: `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.

Scope inmediato independiente:
- tokens, tipografía, focus, buttons, fields, feedback, Dialog y reduced motion;
- autofill, contraste, loading y layout 390–430 en AccountGate;
- retirar duplicación visual inline únicamente donde el foundation nuevo la sustituya limpiamente;
- tests DOM/a11y de primitives afectados.

Fuera de scope: APIs Día 8, MFA/reset backend, data plane, YouTube. Este slice no marca 11.1 `[x]` hasta evidencia completa y review/integración aplicables. AAA conserva PR #45 de 7.2 intacto para retorno cuando WOZ publique contrato 7.1.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 [P1 · FE/DL] — Design foundations
- [ ] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion.
- [ ] Documentar estados; retirar duplicación inline empezando por AccountGate.
- [ ] Corregir autofill, contraste, loading y layout 390–430 px.

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa
- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth popup/redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias de cierre:** APIs de cuenta aplicables de Fase 1.  
**Gate:** variantes de cuenta alcanzables, legibles y recuperables.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 [P1 · BE/FE] — Bootstrap y load
- [ ] Índice vacío atómico en control plane.
- [ ] Separar empty/no-results/offline/auth/cloud failure.
- [ ] Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.
- [ ] Instrumentar startup por fases, comparar cold/warm y corregir regresión de carga inicial reportada.

### 12.2 [P1/P2 · FE/DL] — Biblioteca
- [ ] Header/search/sort/tags/selection accesibles.
- [ ] Card con jerarquía fija y estados sin salto.
- [ ] Grid 390/768/1024/desktop; touch no depende de hover.

**Dependencias de cierre:** data plane + foundations.  
**Gate:** registro → empty gallery → Add Beat sin Desktop previo.

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

### 15.1 [P1 · FE/DL]
- [ ] SettingsShell desktop/móvil; Account/Plan/Preferences/Trash/legal.
- [ ] State machines reales para catálogo/cache/Trash/updater.
- [ ] Acciones peligrosas separadas, confirmadas y con reauth.

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

**Regla:** el nuevo paralelismo permite construir foundations y otros slices sin dependencia; no permite fingir que auth/provider/producción ya existen.