# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 037:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados. 12.1 sigue abierto únicamente por cold/warm runtime real cuantificado. El harness real-browser ya está localizado (`npm run test:web:smoke` → WDIO + Chrome headless + Vite preview), pero el runtime que intentó AAA032 no pudo ejecutar checkout/npm/Chrome; no se fabricaron números.

13.1 sigue abierto:
- Web / #69: coordinator Save All + CAS/partial summary probado; product wiring App/Review→`saveAllWebItems` falta. PR #69 sigue OPEN @ `b2ab75ae...` sobre baseline anterior `3ad8f55a...`; cualquier integración requiere refresh/revalidation contra `02a40564...`.
- Server / #70: orphan lifecycle candidate OPEN @ `5a99ebf2...`; corrective conocido, pero safe-write tooling bloqueó aplicación segura. También stale.

## Owner actual

**AAA — `NIGHT-AAA-035` — F2/13.1 SAME #69.**

PRIMARY:
1. Preflight contra `02a40564...` + duplicate-check.
2. REUSE-FIRST SAME #69; no reemplazo/PR paralelo.
3. Refresh/reconcile candidate al baseline vivo antes de cualquier merge claim.
4. Aplicar únicamente wiring productivo mínimo App/Review→`saveAllWebItems` si existe patch/worktree seguro; conservar saved/conflict/failed + retry/idempotence semantics.
5. Full-file replacement inseguro de `App.tsx` => `STOP_WRITE_SURFACE` sin mutación destructiva.
6. No tocar #70, 13.2+, F3/F4 ni infra.
7. Evidencia: exact base/head/scope, focused product-wiring tests, fresh applicable exact-head CI y race-check antes de merge.

CI-FALLBACK: `NONE` — 12.1 necesita runtime navegador no demostrado disponible y 13.2+ ampliaría scope.

## Día 11

### 11.1 — `[x] DONE / INTEGRATED`
PR #47.

### 11.2 — `[x] DONE / INTEGRATED`
PR #54.

## Día 12

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado; runtime ejecutable faltante.

No cerrar 12.1 con benchmark sintético.

### 12.2 — `[x] DONE / INTEGRATED`
PR #50.

## Día 13

### 13.1 — `[ 🟡 ] IN PROGRESS`
- [ 🟡 ] Save All durable con resumen parcial — #69 helper probado; wiring productivo + refresh pendientes.
- [ 🟡 ] Bulk conflict-safe — #69 CAS/item semantics probado; wiring productivo pendiente.
- [ 🟡 ] Garbage journal — #70 candidate/focused evidence existe; corrective + refresh pendientes.

### 13.2
- [ ] ReviewShell Import/Edit/Bulk, CTA fija y progreso N/N.
- [ ] errores item/retry/skip/cancel/confirmación durable.
- [ ] E2E multi-file/conflicto/refresh/rollback.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Día 14

### 14.1
- [ ] MediaSource/Range + fallback seguro.
- [ ] evitar archivos gigantes completos en RAM.
- [ ] cancel/resume seguro y liberar buffers/object URLs.

### 14.2
- [ ] índice activo/shortcuts/seek/shuffle/repeat/error recoverable.
- [ ] queue/volumen responsive.
- [ ] Safari/Firefox/Chrome/iPhone, red degradada.

## Día 15

### 15.1
- [ ] SettingsShell desktop/móvil; Account/Plan/Preferences/Trash/legal.
- [ ] state machines catálogo/cache/Trash/updater.
- [ ] acciones peligrosas confirmadas + reauth.
- [ ] Vaciar Trash permanente + confirmación fuerte + recent reauth.

### 15.2
- [ ] dialog/focus/live regions/labels/contraste/zoom/reduced motion.
- [ ] baseline visual S01–S59 alcanzables.

### 15.3 — YouTube Web sin Tauri
Pendiente contrato compartido, backend OAuth/jobs server-side, Web adapter puro, upload/schedule durable y evidencia real. Web nunca depende de Tauri/helper Desktop.
