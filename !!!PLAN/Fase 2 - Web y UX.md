# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas. GitHub/runtime vivo prevalece sobre snapshots históricos.

**Baseline vivo CYCLE 080:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), falta evidencia runtime real aplicable.

No cerrar 12.1 con benchmark sintético.

### 13.1 — `[ 🟡 ] IN PROGRESS / FROZEN`

**Web / #69:** OPEN/Ready historical candidate; coordinator Save All + CAS/partial summary probado, pero product wiring seguro no queda demostrado por ese candidate. Frozen/unowned.  
**Server / #70:** OPEN historical candidate; corrective conocido, baseline stale. Frozen/unowned.

- [ 🟡 ] Save All durable con resumen parcial — helper/evidence existe; wiring productivo literal sigue por demostrar.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado; wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

No revivir #69/#70 automáticamente. Cualquier write slice nuevo requiere owner JOBS explícito.

### 13.2 — `[ 🟡 ] EXECUTABLE EVIDENCE GAP`

**Gate literal:** ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa.

Evidencia reusable confirmada:
- `NIGHT-AAA-071` completó auditoría READ-ONLY sobre baseline `957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- No justificó cierre: detectó brecha plausible en Save All para resumen de fallo parcial/conflicto/retry y faltó prueba ejecutable exhaustiva de que acciones Web visibles no invocan Tauri/Desktop.
- `NIGHT-AAA-075` no dejó resultado verificable antes de CYCLE 080 y queda superseded, no PASS.

**Owner CYCLE 080:** `NIGHT-AAA-076`.
- PRIMARY: REUSE AAA071; construir mínimo browser/component journey con call-spies `invoke`/`listen` para familias Web visibles ejercitables y assertions Save All partial-failure/conflict/retry/no-silent-loss.
- Puede aplicar únicamente la corrección F2 mínima si el test demuestra un gap literal.
- Sin #69/#70/#81, sin redesign y sin merge de integración.
- CI-FALLBACK: NONE.

13.2 permanece OPEN hasta evidencia completa. Un test parcial no autoriza `[x]` global si quedan familias Web visibles UNVERIFIED.

## Día 14

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
- [ ] MediaSource/Range o equivalente progresivo + fallback seguro.
- [ ] evitar archivos gigantes completos en RAM.
- [ ] cancel/resume seguro y liberar buffers/object URLs.

PR #81 conserva trabajo material limitado de playback Web, pero su historia/base está stale y la superficie segura de reconciliation no ha sido demostrada. No reabrir ni mutar mientras AAA076 trabaja 13.2.

### 14.2 — `[ ]`
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

**Principio:** evidence-before-claim. `READY_TO_WORK` ≠ `READY_TO_CLOSE`; no falsear browser/runtime coverage con inspección estática.
