# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, slices frontend independientes pueden avanzar antes de cerrar Fase 1 si no dependen materialmente de APIs pendientes.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.  
**Estado F2:** trabajo independiente permitido; no se declara Fase 2 globalmente cerrada por un solo slice.

## Owner actual

**AAA — F2 / 12.2 Biblioteca: FULL OWNER del artifact actual hasta integración/secuenciación o reasignación explícita.**

11.1 ya fue integrado y cerrado. AAA conserva ownership de 12.2 / PR #50; no crea artifact duplicado. Fuera de scope: APIs F1/D8, MFA/reset backend semantics, data plane, YouTube.

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

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa
- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth popup/redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias de cierre:** APIs de cuenta aplicables de Fase 1. D8/8.2 sigue `[ 🟡 ] / PENDING` y conserva decisiones de provider/retención/provider-only reauth, por lo que **11.2 completa todavía no es AAA NEXT dependency-safe**.

**Gate:** variantes de cuenta alcanzables, legibles y recuperables.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 [P1 · BE/FE] — Bootstrap y load
- [ ] Índice vacío atómico en control plane.
- [ ] Separar empty/no-results/offline/auth/cloud failure.
- [ ] Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.
- [ ] Instrumentar startup por fases, comparar cold/warm y corregir regresión de carga inicial reportada.

**AAA NEXT condicional:** después de integrar/cerrar 12.2, si D8 sigue pendiente, JOBS reasigna AAA explícitamente a **12.1** como siguiente slice F2 independiente. Si D8 ya cerró para entonces, JOBS reevalúa 11.2 antes de iniciar 12.1.

### 12.2 [P1/P2 · FE/DL] — Biblioteca — `[ 🟡 ] CANDIDATE DONE / INTEGRACIÓN PENDIENTE`
- [ ] Header/search/sort/tags/selection accesibles — implementado en candidate; cierre global pendiente.
- [ ] Card con jerarquía fija y estados sin salto — implementado en candidate; cierre global pendiente.
- [ ] Grid 390/768/1024/desktop; touch no depende de hover — implementado en candidate; cierre global pendiente.

Artifact canónico: PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c` — **OPEN / no mergeado / non-draft**.

El candidate original fue intencionalmente apilado sobre la rama #47 y tiene Required CI #416 `33213031905` SUCCESS + D6 `33213031958` SUCCESS. Sin embargo #47 fue después refreshed e integrado como `489d81b...`; el head #50 actual no constituye todavía evidencia exacta de la combinación canónica viva.

**No marcar 12.2 `[x]`:**
1. conservar/reutilizar PR #50;
2. seguir la secuencia JOBS para evitar refresh doble mientras WOZ mueve D8.2;
3. incorporar el baseline canónico que ya contenga los cambios previos autorizados;
4. repetir CI exact-head si cambia el head;
5. integrar por flujo autorizado y solo entonces cerrar 12.2.

**Dependencias de cierre:** data plane + foundations. Foundations 11.1 ya está cerrado; falta integración verificable del slice 12.2.  
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