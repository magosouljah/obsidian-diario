# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 032:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 abierto solo por cold/warm runtime real; 13.1 conserva Web #69 frozen + server #70 corrective activo.

## Owners actuales

**AAA — `NIGHT-AAA-032` — 12.1 runtime evidence.** NIGHT-AAA-031 confirmó que SAME #69 sigue necesitando product wiring en `App.tsx`, pero la superficie disponible no permitía patch seguro y el worker hizo STOP sin reemplazo peligroso. JOBS congela #69 y mueve AAA al residual 12.1: construir/usar un harness pequeño y aislado que ejecute startup Web real cold vs warm sobre la instrumentación ya integrada, con escenario reproducible y métricas cuantificadas. No timers sintéticos/unit-only.

**WOZ — `NIGHT-WOZ-031` — 13.1 server SAME #70.** #70 `woz/night-13.1-orphan-lifecycle @ 5a99ebf2...` sigue OPEN/Ready/mergeable. Focused F2 `33304798320` = SUCCESS. Required CI `33304798363` = FAILURE ya atribuida al fixture `cloud-server/tests/postgres-live.integration.cjs` que omite `isObjectStillOrphan`; PostgreSQL estuvo sano. JOBS mantiene autorización exclusiva de ese quinto test path para el corrective mínimo y fresh focused + Required CI.

## Día 11 — Foundations y AccountGate

### 11.1 — `[x] DONE / INTEGRATED`
PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54 merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.

## Día 12 — Library, cards y primera cuenta Web

### 12.1 — `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE` — AAA `NIGHT-AAA-032`
- [x] Índice vacío atómico — #64.
- [x] Empty/no-results/offline/auth/cloud failure separados — #58 + NIGHT-AAA-022.
- [x] Lazy artwork, paginación/ventana y presupuesto de memoria — #58/#66.
- [ 🟡 ] Cold/warm startup real cuantificado — instrumentación existe; benchmark real/reproducible falta.

No cerrar 12.1 ni fabricar benchmark sintético. Un harness aislado puede cerrar este residual si produce una pareja cold/warm real bajo el mismo escenario y evidencia reproducible.

### 12.2 — `[x] DONE / INTEGRATED`
PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.

## Día 13 — Import, Review y bulk edit

### 13.1 — `[ 🟡 ] IN PROGRESS`
- [ 🟡 ] Save All durable con resumen parcial — PR #69 helper green; product wiring App/Review al coordinator sigue pendiente. #69 queda **HOLDING/FROZEN** por write-surface blocker; no reemplazar ni duplicar.
- [ 🟡 ] Bulk conflict-safe o deshabilitado honestamente — #69 CAS/durable por item probado; product wiring aún debe demostrar saved/conflict/failed + partial/retry semantics.
- [ 🟡 ] Garbage journal limpia uploads huérfanos — #70 focused PASS; Required CI corrective de fixture live-PG pendiente bajo WOZ031.

**No overlap:** AAA032 no toca #69/#70; WOZ031 no toca frontend/#69. `CI-FALLBACK: NONE`.

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
