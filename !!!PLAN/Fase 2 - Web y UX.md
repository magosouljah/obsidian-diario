# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 014:** `integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 sigue abierto; D13–D15 no cerrados.

## Owner actual

**AAA — F2 / 12.1 SAME PR #64 merge + residual pagination/window/memory — `NIGHT-AAA-015`.**

PR #58 quedó integrada como `58a6bf61441f08bf68aa63673c0d5f2994b220d9` y cerró slice A: lazy artwork + taxonomía mínima de startup + timing/tests.

Atomic empty-index candidate: PR #64 `aaa/night-12.1-atomic-empty-index @ 3e7fd0a0d7db6f7f423de47c86e643c36d6bcd24`, OPEN/Ready/mergeable, base exacta `55e0d875...`. Reutiliza advisory locks PostgreSQL y `commitIndexCopyOnWrite` para `/transport/index/ensure` server-side idempotente/fail-closed + Web fallback cuando falta el pinned INDEX. AAA corrigió el cycle Web atribuible y el harness de tests focales dentro de la misma lineage.

GitHub factual CYCLE 014: `Test - Desktop Portability / Required CI` run `33272883660` terminó **SUCCESS** exact-head sobre `3e7fd0a0...`; Web+shared, Portable Windows y native macOS observados SUCCESS. #64 no se marca integrada hasta owner race-check/merge.

## Día 11 — Foundations y AccountGate

### 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] IN PROGRESS / ATOMIC CANDIDATE GREEN` — AAA `NIGHT-AAA-015`

- [ 🟡 ] **Índice vacío atómico en control plane.** Candidate #64 exact-head green y mergeable; owner debe hacer race-check + protected merge. Si cambia baseline/head, refresh SAME lineage + fresh applicable CI. Tras merge cerrar solo este sub-slice.
- [ 🟡 ] **Separar empty/no-results/offline/auth/cloud failure.** Slice A integrada en #58; residual abierto donde no esté probado.
- [ 🟡 ] **Thumbnails/lazy artwork, paginación/ventana y presupuesto de memoria.** Lazy artwork integrado en #58; pagination/window/memory es el siguiente residual asignado a AAA después de #64.
- [ 🟡 ] **Instrumentar startup por fases, comparar cold/warm y corregir regresión inicial.** Timing integrado en #58; cold/warm cuantificado/residual sigue abierto.

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
