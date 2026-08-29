# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices frontend independientes pueden avanzar cuando sus dependencias reales están satisfechas, pero el owner/task se asigna explícitamente.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable CYCLE 009:** `integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto.

## Owner actual

**AAA — F2 / 12.1 — FULL OWNER — `NIGHT-AAA-010`.**

PR #58 `aaa/night-12.1-bootstrap-load` sigue OPEN y conserva head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`. Su combinación probada quedó atrás: integration avanzó primero a `f73c9ee...` y ahora a `be9e58c...` por #59. No existe resultado verificable de `NIGHT-AAA-009`; JOBS lo supersedió antes de ejecución verificable para evitar una orden stale. AAA debe refrescar la MISMA PR contra el baseline vivo, obtener CI aplicable exact-head/merge-candidate y solo entonces race-check + merge protegido. No duplicate.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### Tarea 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] IN PROGRESS` — AAA `NIGHT-AAA-010`

- [ ] **Índice vacío atómico en control plane.** No iniciar hasta integrar #58.
- [ 🟡 ] **Separar empty/no-results/offline/auth/cloud failure.** Candidate #58; aún no integrado y requiere refresh/CI vigente.
- [ 🟡 ] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** Lazy artwork está en #58; pagination/window/memory siguen abiertos.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Timing está en #58; cold/warm cuantificado/residual siguen abiertos.

**Orden 010:** refresh de la MISMA PR #58 sobre `be9e58c...`; CI aplicable a la nueva combinación; merge protegido solo si PASS. Después, atomic empty-index como único sub-slice nuevo. Pagination/window/memory y cold/warm residual quedan fuera de 010.

### 12.2 — `[x] DONE / INTEGRATED`
PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.

## Día 13 — Import, Review y bulk edit

### 13.1
- [ ] Save All durable con resumen parcial.
- [ ] Bulk conflict-safe o deshabilitado honestamente.
- [ ] Garbage journal limpia uploads huérfanos.

### 13.2
- [ ] ReviewShell Import/Edit/Bulk, CTA fija y progreso N/N.
- [ ] Errores item/retry/skip/cancel/confirmación durable.
- [ ] E2E multi-file/conflicto/refresh/rollback.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Día 14 — Playback, queue y descargas

### 14.1
- [ ] MediaSource/Range + fallback seguro.
- [ ] Evitar archivos gigantes completos en RAM.
- [ ] Cancel/resume seguro y liberar buffers/object URLs.

### 14.2
- [ ] Índice activo/shortcuts/seek/shuffle/repeat/error recoverable.
- [ ] Queue/volumen responsive.
- [ ] Safari/Firefox/Chrome/iPhone, archivos pequeños/grandes, red degradada.

## Día 15 — Settings, Trash, accesibilidad y YouTube Web

### 15.1
- [ ] SettingsShell desktop/móvil; Account/Plan/Preferences/Trash/legal.
- [ ] State machines reales para catálogo/cache/Trash/updater.
- [ ] Acciones peligrosas separadas, confirmadas y con reauth.
- [ ] “Vaciar Trash” con borrado permanente, confirmación fuerte y recent reauth.

### 15.2
- [ ] Dialog/focus restoration/live regions/labels/contraste/zoom/reduced motion.
- [ ] Baseline visual S01–S59 alcanzables.

### 15.3 — YouTube Web sin Tauri

**Regla de producto:** YouTube existe en Desktop y Web; Web nunca depende de Tauri/helper Desktop.

Pendiente: contrato compartido, Desktop adapter, backend OAuth/jobs server-side, Web adapter puro, upload/schedule durable, UI compartida y evidencia unit/integration/E2E. Capability Web no se activa hasta gate real.

**Dependencias reales:** auth/session + persistencia durable aptas para OAuth/provider data; 16.1 callbacks/entornos separados; 18.1 quotas/entitlements; 25.1 matriz cross-platform/browser.
