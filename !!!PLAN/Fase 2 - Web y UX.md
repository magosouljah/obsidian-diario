# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 047:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), pero falta runtime ejecutable con checkout/npm/Chrome.

No cerrar 12.1 con benchmark sintético. `NIGHT-AAA-043` tiene un CI-FALLBACK **read-only** para inventariar requisitos/paths/comandos de runtime únicamente si #69 queda esperando CI; ese fallback no cierra 12.1.

### 13.1 — `[ 🟡 ] IN PROGRESS`

**Web / #69:** PR OPEN/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base histórica `3ad8f55a...`; coordinator Save All + CAS/partial summary probado; product wiring App/Review/Import/Bulk + refresh al baseline vivo pendientes. `NIGHT-AAA-042` no dejó resultado observable y queda superseded; `NIGHT-AAA-043` es owner único y debe reutilizar SAME #69.

**Server / #70:** PR OPEN/mergeable @ `5a99ebf2...`; corrective conocido, safe-write tooling blocker y baseline stale. Frozen; no owner activo en CYCLE 047.

- [ 🟡 ] Save All durable con resumen parcial — helper probado, wiring productivo pendiente.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado, wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

### 13.2
- [ ] ReviewShell Import/Edit/Bulk, CTA fija y progreso N/N.
- [ ] errores item/retry/skip/cancel/confirmación durable.
- [ ] E2E multi-file/conflicto/refresh/rollback.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Owner CYCLE 047

**AAA — `NIGHT-AAA-043` — SAME #69.** Refresh mínimo al baseline vivo, preservar coordinator/CAS ya probado y conectar `saveAllWebItems` al flujo Web real sin tocar #70 ni reimplementar single-item commit/server garbage journal. Focused tests + fresh exact-head CI.

**CI-FALLBACK AAA:** F2/12.1 READ-ONLY runtime-prerequisite inventory solo si PRIMARY entra en WAITING_CI; sin rama/PR/commit/write, sin benchmark sintético; luego recheck PRIMARY.

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
