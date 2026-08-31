# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas. GitHub/runtime vivo prevalece.

**Baseline vivo CYCLE 100:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness canónico localizado (`npm run test:web:smoke`), falta evidencia runtime real aplicable.

`NIGHT-WOZ-090` terminó `BLOCKED_STOP` sobre exact `816f946c...`: confirmó que el harness real usa Vite/WebdriverIO/headless Chrome, pero la superficie conectada disponible no puede lanzar checkout/Vite/WebdriverIO/Chrome. No hubo timings cold/warm, browser build ni runtime logs atribuibles. Issue #41 `5482199628`.

**Owner CYCLE 100:** ninguno para 12.1. No reciclarlo en una superficie incapaz de ejecutar navegador real.

### 13.1 — `[ 🟡 ] IN PROGRESS / FROZEN`

**Web / #69:** candidate histórico con coordinator Save All + CAS/partial summary; helper/semantics reusable, no integrabilidad actual presumida. Frozen/unowned.  
**Server / #70:** candidate histórico; baseline stale. Frozen/unowned.

No revivir #69/#70 automáticamente. Reuse helper-level solo dentro de assignment explícito.

### 13.2 — `[ 🟡 ] EXECUTABLE EVIDENCE + PROVEN PRODUCT GAP`

**Gate literal:** ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa.

Evidencia reusable:
- `NIGHT-AAA-071`: auditoría READ-ONLY; gap de exhaustive executable Web/Tauri proof + Save All no-silent-loss.
- Issue #41 `5478129410`: gap concreto en `src/App.tsx`: Review single Save y Save All pueden cerrar/avanzar antes de durable cloud completion/failure.
- `NIGHT-AAA-095`: sin resultado final/handoff/candidate material al preflight CYCLE 100; superseded; NOT_PASS.

**Owner CYCLE 100:** `NIGHT-AAA-096`.
- PRIMARY: mínimo corrective slice Review Save/Save All: esperar durable Web persistence, distinguir `saved/conflict/failed`, retry/no-silent-loss y focused executable tests + Web/Tauri/Desktop call-spies.
- Puede reutilizar semantics/helper de #69 sin revivir ni apropiarse del PR.
- Nueva branch/PR AAA bounded solo si duplicate-check sigue limpio; fresh exact-head CI; NO MERGE.
- CI-FALLBACK: NONE.

13.2 permanece OPEN aunque AAA096 produzca candidate: cierre global requiere cobertura literal suficiente de las familias Web visibles.

## Día 14

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
PR #81 conserva trabajo material limitado de playback Web, pero su base `5e117d69...` está stale respecto a integración viva. No reabrir ni mutar mientras 13.2 tiene owner activo y el camino crítico sigue por delante.

### 14.2 — `[ ]`
- [ ] índice activo/shortcuts/seek/shuffle/repeat/error recoverable.
- [ ] queue/volumen responsive.
- [ ] Safari/Firefox/Chrome/iPhone, red degradada.

## Día 15

### 15.1 — `[ 🟡 ] IN PROGRESS / BLOCKED ON REAUTH SEAM`
- [ ] SettingsShell desktop/móvil; Account/Plan/Preferences/Trash/legal.
- [ ] state machines catálogo/cache/Trash/updater.
- [ ] acciones peligrosas confirmadas + reauth.
- [ ] Vaciar Trash permanente + confirmación fuerte + recent reauth.

`NIGHT-WOZ-094` terminó `BLOCKED_STOP` con audit-first factual:
- `SettingsPanel.emptyTrash()` ya reutiliza el purge/list lifecycle existente; no hace falta segunda arquitectura.
- Beat Empty Trash no tiene strong confirmation; `emptyPresetTrash()` sí usa `confirm(...)` y demuestra la diferencia.
- visible Trash rows se limpian optimistamente antes de `platform.trash.purgeBeats()` completion; el failure path intenta reconciliar, pero la action boundary no satisface deterministic/no-false-success.
- `PlatformTrashPort` expone `purgeBeats/listBeats/restoreBeat`, pero no recent-reauth.
- current AccountGate/session surface inspeccionado no expone una bounded reusable recent-reauth seam para SettingsPanel sin cambios auth/session.
- Issue #41 `5483612373`.

**Owner CYCLE 100:** ninguno para implementación 15.1.  
**Blocker exacto:** proper auth/session owner debe exponer/reusar una seam bounded de recent reauth; después se puede reasignar la mínima wiring de strong confirmation + recent reauth + non-optimistic deterministic purge result. No cruzar BBB095 mientras éste sea owner de la investigación Windows auth actual.

Esta evidencia no cierra 15.1 completo. WOZ099 puede tocar únicamente la superficie legal de SettingsPanel bajo #76; no adquiere ownership de Trash/auth/session.

### 15.2
- [ ] dialog/focus/live regions/labels/contraste/zoom/reduced motion.
- [ ] baseline visual S01–S59 alcanzables.

### 15.3 — YouTube Web sin Tauri
Pendiente contrato compartido, backend OAuth/jobs server-side, Web adapter puro, upload/schedule durable y evidencia real. Web nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim. `READY_TO_WORK` ≠ `READY_TO_CLOSE`; no falsear browser/runtime coverage con inspección estática.
