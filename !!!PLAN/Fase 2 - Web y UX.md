# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas. GitHub/runtime vivo prevalece sobre snapshots históricos.

**Baseline vivo CYCLE 082:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness localizado (`npm run test:web:smoke`), falta evidencia runtime real aplicable.

No cerrar 12.1 con benchmark sintético.

### 13.1 — `[ 🟡 ] IN PROGRESS / FROZEN`

**Web / #69:** historical candidate con coordinator Save All + CAS/partial summary, pero no se presume product wiring correcto ni integrabilidad actual. Frozen/unowned.  
**Server / #70:** historical candidate; baseline stale. Frozen/unowned.

- [ 🟡 ] Save All durable con resumen parcial — helper/evidence reusable existe; wiring productivo literal sigue abierto.
- [ 🟡 ] Bulk conflict-safe — CAS/item semantics probado; wiring productivo pendiente.
- [ 🟡 ] Garbage journal — candidate/focused evidence existe; corrective + refresh pendientes.

No revivir #69/#70 automáticamente. Reuse de helpers/semantics solo dentro de un assignment explícito y sin tomar ownership del PR histórico.

### 13.2 — `[ 🟡 ] EXECUTABLE EVIDENCE + PROVEN PRODUCT GAP`

**Gate literal:** ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa.

Evidencia reusable:
- `NIGHT-AAA-071`: auditoría READ-ONLY; dejó gap de exhaustive executable Web/Tauri proof + Save All no-silent-loss.
- Issue #41 `5478129410`, handoff tardío `NIGHT-AAA-074`, revalidó sobre baseline vivo `816f946c...` un gap concreto en `src/App.tsx`: Review single Save y Save All llaman `cloudifyImportedBeats(...)` fire-and-forget y el flujo puede cerrar/avanzar antes de durable cloud completion/failure.
- Ese handoff no corresponde a AAA077 y no lo convierte en PASS; sí es evidencia reusable factual del gap actual.
- `NIGHT-AAA-077`: no resultado final antes de CYCLE 082; not PASS.

**Owner CYCLE 082:** `NIGHT-AAA-078`.
- PRIMARY: mínimo corrective slice del Review Save/Save All action boundary: esperar durable Web persistence, distinguir `saved/conflict/failed`, exponer retry/no-silent-loss y añadir focused executable tests + Tauri/Desktop call-spy para los paths tocados.
- Puede reutilizar semantics/helper de #69 sin revivir ni apropiarse del PR.
- Nueva branch/PR AAA bounded; fresh exact-head CI; NO MERGE.
- CI-FALLBACK: NONE.

13.2 permanece OPEN aunque AAA078 produzca candidate: cierre global requiere cobertura literal suficiente de las familias Web visibles, no solo el corrective slice.

## Día 14

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
- [ ] MediaSource/Range o equivalente progresivo + fallback seguro.
- [ ] evitar archivos gigantes completos en RAM.
- [ ] cancel/resume seguro y liberar buffers/object URLs.

PR #81 conserva trabajo material limitado de playback Web, pero su historia/base está stale y la superficie segura de reconciliation no ha sido demostrada. No reabrir ni mutar mientras AAA078 trabaja 13.2.

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
