# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 101:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ 🟡 ] cold/warm startup Web real cuantificado.

Harness canónico: `npm run test:web:smoke` → Vite/WebdriverIO/headless Chrome. `NIGHT-WOZ-090` probó que la superficie conectada usada entonces no podía lanzar checkout/Vite/WebdriverIO/Chrome; no fabricar timings con inspección estática. Sin owner CYCLE 101.

### 13.1 — `[ 🟡 ] FROZEN`

#69 Web y #70 Server son candidates históricos stale/frozen. Helper/semantics de #69 pueden reutilizarse solo bajo scope explícito; no revivir PRs automáticamente.

### 13.2 — `[ 🟡 ] EXECUTABLE EVIDENCE + PROVEN PRODUCT GAP`

**Gate literal:** ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa.

Evidencia reusable:
- `NIGHT-AAA-071`: audit READ-ONLY; falta exhaustive executable Web/Tauri proof + Save All no-silent-loss.
- Issue #41 `5478129410`: `src/App.tsx` Review single Save / Save All pueden cerrar o avanzar antes de durable cloud completion/failure.
- `NIGHT-AAA-096`: sin resultado final/handoff/candidate material al preflight CYCLE 101; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 101:** `NIGHT-AAA-097`.
- PRIMARY: mínimo Review Save/Save All durable action-boundary corrective; esperar persistencia Web durable, distinguir `saved/conflict/failed`, retry/no-silent-loss y focused tests + Web/no-Tauri call-spies.
- Reuse helper/semantics de #69 sin revivirlo.
- Un bounded candidate solo si duplicate-check sigue limpio; fresh exact-head CI; **NO MERGE**.
- CI-FALLBACK: NONE.

13.2 sigue OPEN aun si AAA097 produce candidate; cierre global requiere cobertura literal suficiente de acciones Web visibles.

## Día 14

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
#81 conserva material playback Web pero está stale. No mutar mientras camino crítico superior siga abierto.

### 14.2 — `[ ]`
- [ ] índice activo/shortcuts/seek/shuffle/repeat/error recoverable;
- [ ] queue/volumen responsive;
- [ ] Safari/Firefox/Chrome/iPhone, red degradada.

## Día 15

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`

`NIGHT-WOZ-094` probó:
- `SettingsPanel.emptyTrash()` ya reutiliza purge/list lifecycle; no hace falta segunda arquitectura;
- falta strong confirmation;
- UI se limpia optimistamente antes de `platform.trash.purgeBeats()` completion;
- `PlatformTrashPort` no expone recent reauth;
- AccountGate/session inspeccionado no expone bounded reusable recent-reauth seam para SettingsPanel.

**Owner CYCLE 101:** ninguno. No cruzar BBB096 mientras éste es owner exclusivo de la causalidad Windows auth. Después, asignar seam auth/session bounded bajo owner correcto y recién entonces wiring Trash mínimo.

### 15.2
- [ ] dialog/focus/live regions/labels/contraste/zoom/reduced motion;
- [ ] baseline visual S01–S59 alcanzables.

### 15.3 — YouTube Web sin Tauri
Pendiente contrato compartido, backend OAuth/jobs server-side, Web adapter puro, upload/schedule durable y evidencia real. Web nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; `READY_TO_WORK` ≠ `READY_TO_CLOSE`; no falsear browser/runtime coverage.
