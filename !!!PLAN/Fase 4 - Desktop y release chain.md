# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 094:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva fail-before autoritativo histórico: Desktop login no persistió `beatgaler:account-session:v1` en run `33313675968` / job `99263095638`.
- #74 es la única product-corrective lineage actual, head `d1593d368e1015abb6a25bf98e5fa8586664ac95`, base `816f946c...`. La corrective vigente reconoce `window.__TAURI__` además de `__TAURI_INTERNALS__` y origins Tauri-owned.
- #84 es el único evidence candidate exact-lineage actual, head `c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61`, OPEN/Ready/mergeable, base `816f946c...`.
- Compare exacto prueba que #84 **contiene** el head actual #74 `d1593d3...` y está 3 commits por delante; por tanto la evidencia no está probando una corrective vieja.
- Exact #84 head: Desktop Portability / Required CI `33423712599` SUCCESS; D6 `33423712621` SUCCESS; D7 `33423712587` SUCCESS; Web Production Build `33423712565` SUCCESS; Windows Import Journey `33423712584` SUCCESS.
- Literal Windows Auth Journey `33423712589` / job `99592060690` = **FAILURE**. El runner empaquetado llegó a `tests/e2e/auth-flow.e2e.mjs:64` y falló: `Desktop login did not persist the returned session token.`
- `NIGHT-BBB-088` no dejó resultado final/handoff y #74/#84 no muestran movimiento posterior a los hechos ya procesados en CYCLE 093. Procesado `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-089` recibe ownership exclusivo #74/#84 para atribuir el **primer límite causal** del fallo actual antes de otro cambio, hacer como máximo la corrección mínima demostrada, refrescar #84 exacto y exigir token persistence + AccountGate exit con fresh exact-head CI. **NO MERGE.**

### windows/review

#72 sigue OPEN/stale/frozen. No pertenece a BBB089 y su Review surface materialmente overlap con AAA090.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` tiene evidencia exact-lineage ejecutable y **roja sobre la corrective actual**; múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 094:** BBB `NIGHT-BBB-089` sobre la lineage #74/#84. Autoridad limitada a diagnóstico causal + producto auth mínimo atribuible + evidencia packaged Windows exact-head. BBB no está autorizado a mutar integration. CI-FALLBACK NONE.
