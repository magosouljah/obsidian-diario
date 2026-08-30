# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 038:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), pero falta runtime ejecutable con checkout/npm/Chrome.

No cerrar 12.1 con benchmark sintético.

### 13.1 — `[ 🟡 ] IN PROGRESS / HOLDING`

**Web / #69:** PR OPEN @ `b2ab75ae...`, base vieja `3ad8f55a...`. Coordinator Save All + CAS/partial summary probado; product wiring App/Review→`saveAllWebItems` y refresh al baseline vivo siguen pendientes. Queda HOLDING en CYCLE 038 porque AAA fue reasignado explícitamente a un product-auth finding P1 de Desktop; no existe segundo owner sobre #69.

**Server / #70:** PR OPEN @ `5a99ebf2...`; corrective conocido, safe-write tooling blocker y baseline stale. Frozen.

- [ 🟡 ] Save All durable con resumen parcial — helper probado, wiring productivo pendiente.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado, wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

### 13.2
- [ ] ReviewShell Import/Edit/Bulk, CTA fija y progreso N/N.
- [ ] errores item/retry/skip/cancel/confirmación durable.
- [ ] E2E multi-file/conflicto/refresh/rollback.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Owner CYCLE 038

AAA fue movido temporalmente a un product-auth finding descubierto por F4/Windows Auth. #69 permanece HOLDING sin owner de implementación activo; no se transfiere automáticamente a BBB/WOZ.

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
