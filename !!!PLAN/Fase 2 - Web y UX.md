# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Bajo ROMPECABEZAS, slices independientes pueden avanzar cuando sus dependencias reales están satisfechas, con owner explícito.

**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

**Baseline vivo CYCLE 034:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados. 12.1 sigue abierto únicamente por cold/warm runtime real cuantificado. AAA032 encontró el harness real-browser ya integrado (`npm run test:web:smoke` → WDIO + Chrome headless + Vite preview), pero su runtime no pudo ejecutar checkout/npm/Chrome; no se fabricaron números.

13.1 sigue abierto:
- Web / #69: coordinator Save All + CAS/partial summary probado, pero product wiring App/Review→`saveAllWebItems` falta. PR #69 sigue OPEN @ `b2ab75ae...` y quedó sobre baseline anterior después del merge #63.
- Server / #70: orphan lifecycle candidate OPEN @ `5a99ebf2...`; corrective exacto conocido, pero safe-write tooling bloqueó aplicación segura. También quedó sobre baseline anterior.

## Owner actual

**AAA — `NIGHT-AAA-033` — F2/13.1 SAME #69.**

PRIMARY:
1. Preflight contra baseline `02a40564...` y duplicate-check.
2. Reutilizar SAME #69; no reemplazar ni abrir PR paralelo.
3. Refresh/reconcile el candidate al baseline vivo antes de cualquier claim de integración.
4. Aplicar únicamente el wiring productivo mínimo App/Review→`saveAllWebItems` si existe una superficie de patch/worktree segura; conservar saved/conflict/failed + retry/idempotence semantics.
5. Si la única escritura disponible exige full-file replacement inseguro de `App.tsx`, STOP_WRITE_SURFACE sin mutación destructiva.
6. No tocar #70, 13.2+, F3, F4 ni infra.

CI-FALLBACK: `NONE`.

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
- [ 🟡 ] Save All durable con resumen parcial — #69 helper probado; wiring productivo pendiente.
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
