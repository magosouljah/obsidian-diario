# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 023:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto únicamente por cold/warm real cuantificado; D13–D15 no cerrados.

## Owner actual

**AAA — F2 / 13.1 — `NIGHT-AAA-023` (ASSIGNED).**

El residual 12.1 no se transfirió ni cerró falsamente: queda abierto por evidencia runtime cold/warm. JOBS mueve AAA explícitamente a 13.1 porque es trabajo dependency-safe e independiente y repetir 12.1 sin superficie ejecutable sería tiempo muerto.

PR #58 quedó integrada como `58a6bf61441f08bf68aa63673c0d5f2994b220d9` y cerró lazy artwork + taxonomía mínima de startup + timing/tests. Atomic empty-index quedó **DONE / INTEGRATED** por PR #64 como `b114111cafb29b4aa50cdce014059c66a75bddf2`.

PR #66 `aaa/night-12.1-pagination-windowing` quedó **CLOSED / MERGED** como `712b49b6689a31a47902dbe95e98622d001dab40`. Contiene first-load bounded, `WebLibraryWindowConsumer`, refresh tras shrink, métricas de materialización, continuidad sintética 10,321 beats y wiring React productivo por cursor `bgPage`.

`NIGHT-AAA-022` hizo REUSE-FIRST y verificó evidencia literal existente:
- `src/features/library/webLibrary.ts` distingue `ready / empty / no-results / offline / auth-failure / cloud-failure`;
- `tests/component-dom/webLibrary.test.ts` afirma literalmente esos estados;
- no se abrió PR ceremonial.

Por tanto taxonomy/state queda **demostrado**. El único residual de 12.1 es comparar startup Web cold vs warm real bajo el mismo escenario, con cache/session cold vs preservados y métricas cuantificadas/reproducibles. La prueba de timing existente demuestra instrumentación, no esa comparación.

## Día 11 — Foundations y AccountGate

### 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`

- [x] **Índice vacío atómico en control plane.** PR #64 integrado.
- [x] **Separar empty/no-results/offline/auth/cloud failure.** Evidencia integrada #58 + verificación literal `NIGHT-AAA-022`.
- [x] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** #58/#66 integrados.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Instrumentación existe; falta comparación cold/warm real cuantificada/reproducible.

No cerrar 12.1 hasta esa evidencia. No fabricar benchmark sintético para sustituir startup real.

### 12.2 — `[x] DONE / INTEGRATED`
PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.

## Día 13 — Import, Review y bulk edit

### 13.1 — `[ 🟡 ] ASSIGNED — AAA NIGHT-AAA-023`
- [ ] Save All durable con resumen parcial.
- [ ] Bulk conflict-safe o deshabilitado honestamente.
- [ ] Garbage journal limpia uploads huérfanos.

**Scope de 023:** solo 13.1, REUSE-FIRST, una sola rama/PR si existe gap real. No 13.2, D14/D15, YouTube, billing, Desktop ni infra.

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
