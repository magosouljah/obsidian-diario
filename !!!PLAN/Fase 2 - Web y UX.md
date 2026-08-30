# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 027:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 abierto solo por cold/warm runtime real; 13.1 activo con dos carriles independientes y ownership explícito; D13–D15 no cerrados.

## Owners actuales — F2/13.1

**AAA — `NIGHT-AAA-027` — carril Web:** Save All multi-item + progreso/resumen parcial + bulk conflict-safe, reutilizando durable commits/CAS existentes. AAA no toca server garbage journal.

**WOZ — `NIGHT-WOZ-026` — carril server:** REUSE-FIRST sobre garbage journal/reconciliation existentes; demostrar o implementar el contrato mínimo Web-callable durable para registrar/reconciliar uploads huérfanos, con cleanup idempotente/fail-closed y focused tests. WOZ no toca Save All/bulk frontend de AAA.

NIGHT-AAA-025 confirmó single-save durable, CAS por item y componentes server-side de garbage journal ya existentes. El gap quedó dividido por boundary real Web↔server; ninguno de los dos carriles puede fingir cierre completo de 13.1 por sí solo.

PR #58 quedó integrada como `58a6bf61441f08bf68aa63673c0d5f2994b220d9`; PR #64 atomic empty-index como `b114111cafb29b4aa50cdce014059c66a75bddf2`; PR #66 pagination/windowing como `712b49b6689a31a47902dbe95e98622d001dab40`.

NIGHT-AAA-022 demostró taxonomy/state `ready / empty / no-results / offline / auth-failure / cloud-failure`. El único residual 12.1 es startup Web cold vs warm real, mismo escenario, cache/session cold vs preservados, con métricas cuantificadas/reproducibles.

## Día 11 — Foundations y AccountGate

### 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`
- [x] Índice vacío atómico — #64.
- [x] Empty/no-results/offline/auth/cloud failure separados — #58 + NIGHT-AAA-022.
- [x] Lazy artwork, paginación/ventana y presupuesto de memoria — #58/#66.
- [ 🟡 ] Cold/warm startup real cuantificado — instrumentación existe; benchmark real falta.

No cerrar 12.1 ni fabricar benchmark sintético.

### 12.2 — `[x] DONE / INTEGRATED`
PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.

## Día 13 — Import, Review y bulk edit

### 13.1 — `[ 🟡 ] IN PROGRESS — AAA 027 + WOZ 026`
- [ 🟡 ] Save All durable con resumen parcial — AAA Web owner.
- [ 🟡 ] Bulk conflict-safe o deshabilitado honestamente — AAA Web owner; CAS por item; cero pérdida silenciosa.
- [ 🟡 ] Garbage journal limpia uploads huérfanos — WOZ server owner; reutilizar journal/worker existente y cerrar únicamente el contrato durable Web-callable si el gap es real.

**No overlap:** AAA no modifica `cloud-server/garbage-journal-repository.js`, `garbage-reconciliation-worker.js` ni el server contract de WOZ. WOZ no modifica Save All/bulk frontend ni los primitives Web owned por AAA. Ambos `CI-FALLBACK: NONE`.

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
