# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 049:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), pero falta runtime ejecutable con checkout/npm/Chrome.

No cerrar 12.1 con benchmark sintético.

### 13.1 — `[ 🟡 ] IN PROGRESS / BLOCKED ON WRITE SURFACE`

**Web / #69:** PR OPEN/Ready/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base histórica `3ad8f55a...`; coordinator Save All + CAS/partial summary probado. `NIGHT-AAA-043` revalidó que integration y #69 divergen desde ese merge-base y que integration cambia fuera de los dos archivos de #69. No pudo hacer refresh/product wiring de forma segura con la superficie de escritura disponible y terminó `PENDING / STOP_WRITE_SURFACE`. #69 queda frozen/unowned hasta superficie patch-capable.

**Server / #70:** PR OPEN/mergeable @ `5a99ebf2...`; corrective conocido, safe-write tooling blocker y baseline stale. Frozen/unowned.

- [ 🟡 ] Save All durable con resumen parcial — helper probado, wiring productivo pendiente.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado, wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

### 13.2 — `[ 🟡 ] AUDIT QUEUED AS CONDITIONAL FALLBACK`

`NIGHT-AAA-044` no produjo RESULTADO DEL TURNO antes de CYCLE 049 y queda superseded. Para no perder el trabajo útil, el mismo audit **read-only** queda preautorizado únicamente como `CI-FALLBACK` de `NIGHT-AAA-045`, y solo si el PRIMARY #76 entra realmente en WAITING_CI/review/merge.

Fallback permitido:
- ReviewShell Import/Edit/Bulk;
- CTA fija y progreso N/N;
- errores item/retry/skip/cancel/confirmación durable;
- E2E multi-file/conflicto/refresh/rollback;
- dependencia exacta con #69/#70.

Resultado permitido: matriz `EXISTS/PARTIAL/GAP/PENDING_DEPENDENCY` + slices mínimos/path/symbol/test. No branch/PR/commit/write y no PASS claim. El worker debe recheckear #76 antes de cerrar turno.

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
