# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices frontend independientes pueden avanzar cuando sus dependencias reales están satisfechas, pero el owner/task se asigna explícitamente.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Integración estable CYCLE 008:** `integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto.

## Owner actual

**AAA — F2 / 12.1 — FULL OWNER — `NIGHT-AAA-009`.**

PR #58 `aaa/night-12.1-bootstrap-load` sigue OPEN/Ready/mergeable=true, head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`, pero su base observada es `f0d65aa...` y la integración avanzó a `f73c9ee...` por #57. El intento anterior de merge fue bloqueado correctamente porque el merge-candidate no tenía Required CI. AAA debe refrescar la MISMA PR contra el baseline vivo, obtener CI aplicable exact-head/merge-candidate y solo entonces race-check + merge protegido. No duplicate.

---

## Día 11 — Foundations y AccountGate

### Tarea 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### Tarea 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] IN PROGRESS` — AAA `NIGHT-AAA-009`

- [ ] **Índice vacío atómico en control plane.** No iniciar hasta integrar #58.
- [ 🟡 ] **Separar empty/no-results/offline/auth/cloud failure.** Candidate #58; aún no integrado.
- [ 🟡 ] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** Lazy artwork está en #58; pagination/window/memory siguen abiertos.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Timing está en #58; cold/warm cuantificado/residual siguen abiertos.

**Orden 009:** refresh de la MISMA PR #58 sobre `f73c9ee...`; CI exacto; merge protegido si PASS. Después, atomic empty-index como único sub-slice nuevo. Pagination/window/memory y cold/warm residual quedan fuera de 009.

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
