# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 021:** `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto solo por residual cold/warm + taxonomy/state; D13–D15 no cerrados.

## Owner actual

**AAA — F2 / 12.1 residual cold/warm + taxonomy/state — `NIGHT-AAA-021` (ASSIGNED).**

PR #58 quedó integrada como `58a6bf61441f08bf68aa63673c0d5f2994b220d9` y cerró slice A: lazy artwork + taxonomía mínima de startup + timing/tests. Atomic empty-index quedó **DONE / INTEGRATED** por PR #64 como `b114111cafb29b4aa50cdce014059c66a75bddf2`.

PR #66 `aaa/night-12.1-pagination-windowing` quedó **CLOSED / MERGED** como `712b49b6689a31a47902dbe95e98622d001dab40`. El candidate probado e integrado contiene:
- first-load/materialización bounded;
- `WebLibraryWindowConsumer` current/next/previous/refresh + acceso por offset;
- refresh seguro tras shrink;
- métricas de materialización;
- continuidad sintética de 10,321 beats sin duplicados/omisiones y sin artwork eager;
- wiring React productivo por cursor `bgPage`, con Previous/Next reales y sin reconstruir un `Beat[]` global.

Evidencia exact-head de #66:
- Required CI / Desktop Portability `33278321854` — SUCCESS;
- D6 `33278321859` — SUCCESS;
- D7 `33278321867` — SUCCESS;
- merge verificado `712b49b6689a31a47902dbe95e98622d001dab40`.

Residuales literales de 12.1:
- **cold/warm cuantificado** del startup Web;
- cualquier separación de taxonomy/state `empty / no-results / offline / auth / cloud failure` que todavía no esté demostrada por evidencia existente.

`NIGHT-AAA-021` debe hacer REUSE-FIRST, cerrar solo esos residuales y no abrir D13–D15 automáticamente.

CI-FALLBACK para `NIGHT-AAA-021`: `NONE`.

## Día 11 — Foundations y AccountGate

### 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] IN PROGRESS / RESIDUAL` — AAA `NIGHT-AAA-021`

- [x] **Índice vacío atómico en control plane.** PR #64 integrado.
- [ 🟡 ] **Separar empty/no-results/offline/auth/cloud failure.** Slice A integrada en #58; cerrar residual solo donde falta evidencia literal.
- [x] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** Lazy artwork integrado; bounded pagination/window/memory + navegación productiva integrado por #66.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Timing integrado en #58; falta cuantificación cold/warm verificable.

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

**Regla:** YouTube existe en Desktop y Web; Web nunca depende de Tauri/helper Desktop.

Pendiente: contrato compartido, Desktop adapter, backend OAuth/jobs server-side, Web adapter puro, upload/schedule durable, UI compartida y evidencia unit/integration/E2E. Capability Web no se activa hasta gate real.

**Dependencias reales:** auth/session + persistencia durable aptas para OAuth/provider data; 16.1 callbacks/entornos separados; 18.1 quotas/entitlements; 25.1 matriz cross-platform/browser.
