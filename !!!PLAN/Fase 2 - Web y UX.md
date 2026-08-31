# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 058:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), pero falta runtime ejecutable con checkout/npm/Chrome.

No cerrar 12.1 con benchmark sintético.

### 13.1 — `[ 🟡 ] IN PROGRESS / BLOCKED ON WRITE SURFACE`

**Web / #69:** OPEN/Ready/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base histórica `3ad8f55a...`; coordinator Save All + CAS/partial summary probado. Último resultado material: `STOP_WRITE_SURFACE`. Frozen/unowned.

**Server / #70:** OPEN/mergeable @ `5a99ebf2...`; corrective conocido, safe-write tooling blocker y baseline stale. Frozen/unowned.

- [ 🟡 ] Save All durable con resumen parcial — helper probado, wiring productivo pendiente.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado, wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

### 13.2 — `[ 🟡 ] AUDIT NOT EXECUTED / UNASSIGNED`
No existe resultado final aceptable que cierre este audit. Requiere futura asignación explícita.

**Gate:** ninguna acción Web visible llama Tauri; 0 pérdida silenciosa.

## Día 14

### 14.1 — `[ 🟡 ] ASSIGNED AAA054`
- [ ] MediaSource/Range o equivalente progresivo + fallback seguro.
- [ ] evitar archivos gigantes completos en RAM.
- [ ] cancel/resume seguro y liberar buffers/object URLs.

`NIGHT-AAA-053` no produjo resultado final verificable antes de CYCLE 058 y queda superseded. `NIGHT-AAA-054` fue recalculado desde cero como el slice F2 interno dependency-safe de mayor valor. REUSE-FIRST sobre live integration; solo implementación mínima literal; no Player redesign ni #69/#70.

### 14.2 — `[ ] / CONDITIONAL READ-ONLY FALLBACK AAA054`
- [ ] índice activo/shortcuts/seek/shuffle/repeat/error recoverable.
- [ ] queue/volumen responsive.
- [ ] Safari/Firefox/Chrome/iPhone, red degradada.

Fallback read-only solo si 14.1 queda code-complete esperando CI/review/merge; no cierra 14.2.

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
