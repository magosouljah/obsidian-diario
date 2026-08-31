# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Leer `Plan Maestro.md`. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas. GitHub/runtime vivo prevalece.

**Baseline vivo CYCLE 093:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado — harness canónico localizado (`npm run test:web:smoke`), falta evidencia runtime real aplicable.

`NIGHT-WOZ-090` terminó `BLOCKED_STOP` sobre exact `816f946c...`: confirmó que el harness real usa Vite/WebdriverIO/headless Chrome, pero la superficie conectada disponible no puede lanzar checkout/Vite/WebdriverIO/Chrome. No hubo timings cold/warm, browser build ni runtime logs atribuibles. Issue #41 `5482199628`.

**Owner CYCLE 093:** ninguno para 12.1. No reciclarlo en una superficie incapaz de ejecutar navegador real.

### 13.1 — `[ 🟡 ] IN PROGRESS / FROZEN`

**Web / #69:** candidate histórico con coordinator Save All + CAS/partial summary; helper/semantics reusable, no integrabilidad actual presumida. Frozen/unowned.  
**Server / #70:** candidate histórico; baseline stale. Frozen/unowned.

No revivir #69/#70 automáticamente. Reuse helper-level solo dentro de assignment explícito.

### 13.2 — `[ 🟡 ] EXECUTABLE EVIDENCE + PROVEN PRODUCT GAP`

**Gate literal:** ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa.

Evidencia reusable:
- `NIGHT-AAA-071`: auditoría READ-ONLY; gap de exhaustive executable Web/Tauri proof + Save All no-silent-loss.
- Issue #41 `5478129410`: gap concreto en `src/App.tsx`: Review single Save y Save All pueden cerrar/avanzar antes de durable cloud completion/failure.
- `NIGHT-AAA-088`: sin resultado final, handoff material ni nuevo PR F2/13.2 verificable al preflight CYCLE 093; superseded; NOT_PASS.

**Owner CYCLE 093:** `NIGHT-AAA-089`.
- PRIMARY: mínimo corrective slice Review Save/Save All: esperar durable Web persistence, distinguir `saved/conflict/failed`, retry/no-silent-loss y focused executable tests + Tauri/Desktop call-spies.
- Puede reutilizar semantics/helper de #69 sin revivir ni apropiarse del PR.
- Nueva branch/PR AAA bounded solo si duplicate-check sigue limpio; fresh exact-head CI; NO MERGE.
- CI-FALLBACK: NONE.

13.2 permanece OPEN aunque AAA089 produzca candidate: cierre global requiere cobertura literal suficiente de las familias Web visibles.

## Día 14

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
PR #81 conserva trabajo material limitado de playback Web, pero su historia/base está stale. No reabrir ni mutar mientras 13.2 tiene owner activo y el resto del camino crítico es más urgente.

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
