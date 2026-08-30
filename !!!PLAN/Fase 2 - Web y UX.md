# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 028:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.  
**Estado F2:** 11.1, 11.2 y 12.2 cerrados; 12.1 abierto solo por cold/warm runtime real; 13.1 activo con dos carriles independientes.

## Owners actuales — F2/13.1

**AAA — `NIGHT-AAA-028` — carril Web / SAME #69:** #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` OPEN/Ready/mergeable. D6 `33303237410`, D7 `33303237375` y Desktop Portability `33303237401` = SUCCESS; Upgrade no aplicable. Helper Save All secuencial por item, resumen saved/conflict/failed, retry unresolved y duplicate-id protection ya existe con focused tests. El turno 028 debe confirmar/wirear el flujo productivo real Review/Import/Bulk; no basta reclamar helper aislado. Si ya está wired, demostrarlo y no añadir cambio ceremonial. Si cambia head, fresh exact-head CI antes de merge.

**WOZ — `NIGHT-WOZ-027` — carril server:** REUSE-FIRST sobre garbage journal/reconciliation existentes; demostrar o implementar el contrato mínimo Web-callable durable para registrar/reconciliar uploads huérfanos, idempotente/fail-closed y sin borrar uploads committed/valid. No tocar el frontend de AAA.

No se cierra 13.1 hasta demostrar ambos lados sin pérdida silenciosa.

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

### 13.1 — `[ 🟡 ] IN PROGRESS — AAA 028 + WOZ 027`
- [ 🟡 ] Save All durable con resumen parcial — #69 candidate green; product wiring/integration factual aún pendiente.
- [ 🟡 ] Bulk conflict-safe o deshabilitado honestamente — helper #69 usa CAS/durable por item; product wiring debe demostrarse.
- [ 🟡 ] Garbage journal limpia uploads huérfanos — WOZ server owner.

**No overlap:** AAA no modifica server journal/reconciliation. WOZ no modifica Save All/bulk frontend. `CI-FALLBACK: NONE` para ambos.

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
