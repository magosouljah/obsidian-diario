# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, slices frontend independientes pueden avanzar antes de cerrar Fase 1 si no dependen materialmente de APIs pendientes.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.  
**Estado F2:** trabajo independiente permitido; no se declara Fase 2 globalmente cerrada/activa por un solo slice.

## Owner actual

**AAA — F2 / 11.1 Design Foundations: FULL OWNER hasta cierre explícito.**  
Baseline del artifact actual: `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.

AAA hace el ciclo completo de 11.1:
- preflight/duplicate-check;
- implementación;
- corrección de regresiones propias;
- tests DOM/a11y/unit aplicables;
- build y CI exact-head;
- handoff con evidencia.

**No existe interrupt rule hacia D7/PR #45.** D7 ya está `[x]/PASS`; AAA no vuelve automáticamente a 7.2.

Fuera de scope de AAA 11.1: APIs F1/D8, MFA/reset backend semantics, data plane, YouTube.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 [P1 · FE/DL] — `[ 🟡 ]` AAA FULL OWNER / CANDIDATE DONE, INTEGRACIÓN PENDIENTE

Artifact: PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383` — **OPEN / no mergeado**.

Handoff AAA `5456682762`: `DONE — INDEPENDENT SLICE ONLY`. Exact-head Required CI #392 `33202493998` = COMPLETED / SUCCESS; D6 cross-process #33 `33202493855` = SUCCESS. Diff declarado contra su baseline: 7 files de foundations/AccountGate/tests/docs.

Cobertura del candidate:
- tokens, tipografía, focus, button/field/feedback/icon/Dialog/loading foundations;
- dark browser autofill + reduced motion global;
- AccountGate signed-out/loading con labels/autocomplete/alerts y layout safe-area 390–430;
- contrast assertions WCAG AA;
- DOM/a11y tests afectados;
- `docs/DESIGN-FOUNDATIONS-11.1.md`.

**No marcar 11.1 `[x]` todavía:** el propio handoff limita el DONE al slice independiente; PR #47 sigue abierto/no integrado y la secuenciación sobre la integración actual `e25c604...` no está cerrada.

Checklist literal:
- [ ] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion — implementado en candidate, cierre global pendiente.
- [ ] Documentar estados; retirar duplicación inline empezando por AccountGate — implementado en candidate, cierre global pendiente.
- [ ] Corregir autofill, contraste, loading y layout 390–430 px — implementado en candidate, cierre global pendiente.
- [ ] Tests DOM/a11y afectados — verdes en candidate, cierre global pendiente.
- [ ] Build/CI aplicable verde sobre exact head — #392 SUCCESS en candidate; integración actual aún no verificada con este delta.

**NEXT_WITHIN_AREA AAA:** mantener PR #47 como artifact canónico, resolver integración/secuenciación sin duplicarlo y producir evidencia sobre el head que corresponda antes de pedir cierre global 11.1.

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