# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo el modelo ROMPECABEZAS, slices frontend independientes pueden avanzar antes de cerrar Fase 1 si no dependen materialmente de APIs pendientes.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable actual:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.  
**Estado F2:** trabajo independiente permitido; no se declara Fase 2 globalmente cerrada/activa por un solo slice.

## Owner actual

**AAA — F2 / 12.2 Biblioteca: FULL OWNER del artifact actual hasta integración/secuenciación o reasignación explícita.**  
La reasignación 11.1 → 12.2 está respaldada por la instrucción RO registrada en PR #50/handoff AAA. PR #47 sigue siendo dependencia canónica de #50 y no se considera cerrado globalmente por ese cambio de owner.

Artifacts canónicos existentes:
- PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383`;
- PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c`, apilado sobre #47.

AAA no crea artifacts duplicados. El ciclo pendiente es incorporar la integración canónica vigente por el método técnico autorizado, corregir regresiones propias, repetir CI exact-head y entregar handoff cuando cambie el head.

Fuera de scope de AAA en estos artifacts: APIs F1/D8, MFA/reset backend semantics, data plane, YouTube.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 [P1 · FE/DL] — `[ 🟡 ]` CANDIDATE DONE / INTEGRACIÓN PENDIENTE

Artifact: PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383` — **OPEN / no mergeado / no draft**.

Handoff AAA `5456682762`: `DONE — INDEPENDENT SLICE ONLY`. Exact-head Required CI #392 `33202493998` = COMPLETED / SUCCESS; D6 cross-process #33 `33202493855` = SUCCESS. Diff declarado contra su baseline: 7 files de foundations/AccountGate/tests/docs.

Cobertura del candidate:
- tokens, tipografía, focus, button/field/feedback/icon/Dialog/loading foundations;
- dark browser autofill + reduced motion global;
- AccountGate signed-out/loading con labels/autocomplete/alerts y layout safe-area 390–430;
- contrast assertions WCAG AA;
- DOM/a11y tests afectados;
- `docs/DESIGN-FOUNDATIONS-11.1.md`.

**Preflight JOBS 2026-08-28:** #47 ya no está sobre el baseline canónico actual: comparación desde `e25c604...` = `diverged`, `behind_by=49`. Además #47 y PR #49 modifican `src/components/AccountGate.tsx` y `tests/component-dom/accountGateWeb.test.tsx`. Por tanto el CI verde de `ddad3124...` no prueba todavía la combinación post-D8/8.1.

**No marcar 11.1 `[x]`:** el artifact debe incorporar el baseline canónico posterior a la integración autorizada de #49, resolver cualquier interacción dentro del ownership técnico correspondiente y obtener CI exact-head verde antes de integración. JOBS no prescribe rebase/merge/cherry-pick ni modifica código.

Checklist literal:
- [ ] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion — implementado en candidate, cierre global pendiente.
- [ ] Documentar estados; retirar duplicación inline empezando por AccountGate — implementado en candidate, cierre global pendiente.
- [ ] Corregir autofill, contraste, loading y layout 390–430 px — implementado en candidate, cierre global pendiente.
- [ ] Tests DOM/a11y afectados — verdes en candidate, revalidación post-baseline pendiente.
- [ ] Build/CI aplicable verde sobre exact head — #392 SUCCESS en candidate; falta exact-head del artifact actualizado sobre integración vigente.

**SECUENCIA OBLIGATORIA:** `#47` debe quedar integrado y verificable **antes** de procesar el cierre/integración de `#50`.

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa
- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth popup/redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias de cierre:** APIs de cuenta aplicables de Fase 1. En el preflight actual D8/8.2 sigue pendiente, incluyendo MFA recovery/reauth/verification/reset lifecycle; por eso **11.2 completa no es AAA NEXT dependency-safe todavía**.  
**Gate:** variantes de cuenta alcanzables, legibles y recuperables.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 [P1 · BE/FE] — Bootstrap y load
- [ ] Índice vacío atómico en control plane.
- [ ] Separar empty/no-results/offline/auth/cloud failure.
- [ ] Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.
- [ ] Instrumentar startup por fases, comparar cold/warm y corregir regresión de carga inicial reportada.

**AAA NEXT condicional:** cuando #47 y #50 estén integrados/cerrados con evidencia, si D8/8.2 sigue pendiente, JOBS reasigna AAA a **12.1** como siguiente slice F2 ya planificado que permite trabajo útil independiente. Si para entonces 8.2 ya está cerrado, JOBS reevalúa 11.2 antes de iniciar 12.1; no hay hopping automático.

### 12.2 [P1/P2 · FE/DL] — Biblioteca — `[ 🟡 ]` CANDIDATE DONE / DEPENDE DE #47
- [ ] Header/search/sort/tags/selection accesibles.
- [ ] Card con jerarquía fija y estados sin salto.
- [ ] Grid 390/768/1024/desktop; touch no depende de hover.

Artifact: PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c` — **OPEN / no mergeado / no draft**; base PR = rama #47.

Handoff AAA `5458081273`: `DONE`; exact 12.2 delta = 4 files. Required CI #416 `33213031905` = SUCCESS; D6 cross-process #56 `33213031958` = SUCCESS.

**Preflight JOBS 2026-08-28:** #50 está intencionalmente apilado sobre #47 y, comparado con integración `e25c604...`, también está `diverged`, `behind_by=49`. El CI verde demuestra el stack #47→#50 en su head actual, no la combinación con la integración canónica posterior.

**No marcar 12.2 `[x]`:** primero #47 debe quedar integrado; después #50 debe quedar basado/validado contra la integración que ya contenga #47, repetir CI exact-head si cambia el head y solo entonces integrarse por el flujo autorizado.

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