# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 097:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva fail-before autoritativo histórico.
- #74 es la única product-corrective lineage actual, head `d1593d368e1015abb6a25bf98e5fa8586664ac95`, base exact `816f946c...`, OPEN/Ready/mergeable.
- #84 es el único evidence candidate exact-lineage actual, head `c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61`, OPEN/Ready/mergeable, base exact `816f946c...`.
- Exact #84 head: broad Required CI/Desktop Portability permanece verde, pero literal Windows Auth Journey `33423712589` / job `99592060690` = **FAILURE**.
- Job exacto: setup/checkout/node/rust/npm/embedded driver y release-profile Tauri build PASS; failure literal en `tests/e2e/auth-flow.e2e.mjs:64`: `Desktop login did not persist the returned session token.`
- Late `NIGHT-BBB-088` / Issue #41 `5483886991` fue recibido después de CYCLE 096 y se procesa factual en CYCLE 097: tras Sign in el expected token nunca se vuelve observable en `localStorage`. El mismo log contiene fallos repetidos `@wdio/tauri-service` DirectEval/window-state (`Failed to get window states: Error: [object Object]`) y después `Failed to clear mock store: A sessionId is required`.
- Esa evidencia **no distingue aún** producto auth/session vs mocked Tauri command path vs pérdida de capacidad de sesión/eval del servicio WDIO/Tauri. Por evidence-before-claim, otro product corrective sería especulativo.
- `NIGHT-BBB-091` no dejó resultado final/handoff ni movimiento de #74/#84 al preflight CYCLE 097; superseded / NOT_PASS.
- `NIGHT-BBB-092` recibe ownership exclusivo de una única diagnostic-only pass sobre #84: instrumentar `/auth/login` mock/response, `set_cloud_auth_token`, product session write y gate transition, sin imprimir secretos, sin cambiar assertions y sin product mutation; fresh literal Windows run + exact-head CI; **NO MERGE**.

### windows/review

#72 sigue OPEN/stale/frozen. No pertenece a BBB092 y su Review surface materialmente overlap con AAA093.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` tiene evidencia exact-lineage ejecutable y **roja sobre la corrective actual**; causal side sigue unresolved pending BBB092 diagnostic-only pass. Múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 097:** BBB `NIGHT-BBB-092` sobre #84 diagnostic boundary only. Autoridad limitada a instrumentation + literal packaged Windows evidence para resolver causal side. No product corrective, no integration mutation. CI-FALLBACK NONE.
