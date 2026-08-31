# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 099:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva fail-before autoritativo histórico.
- #74 es la única product-corrective lineage actual, head `d1593d368e1015abb6a25bf98e5fa8586664ac95`, base exact `816f946c...`, OPEN/Ready/mergeable.
- #84 es el único evidence candidate exact-lineage actual, head `28c3810c43eefa8bab0ffa2026c371882ead2f2f`, OPEN/Ready/mergeable, base exact `816f946c...`.
- Exact #84 head `28c3810c...`: F4 - 25.1 Windows Auth Journey run `33439899177` / job `99645269221` = **FAILURE**. D6, D7, Web Production Build, Test - Desktop Portability y Windows Import observados SUCCESS en ese exact head.
- `NIGHT-BBB-093` añadió instrumentación redacted únicamente al harness y mantuvo las assertions literales. El run llegó al packaged Windows journey y registró repetidamente `boundary=unexpected-request`, con `gatePresent=true` y `tokenPresent=false`; error literal: `Desktop login did not persist the returned session token.`
- Esta nueva evidencia estrecha el fallo al request/mock/service boundary, pero **todavía no demuestra** si el mismatch es harness/mock/config-only, Tauri/WDIO-service, o producto request/session behavior. No se autoriza product corrective especulativo.
- `NIGHT-BBB-094` recibe ownership exclusivo para identificar el primer request inesperado y atribuirlo. Solo si se prueba harness-only puede corregir mínimamente el harness #84 y rerun con assertions literales intactas. Si producto está implicado, STOP `PRODUCT_SIDE_PROVEN` para reasignación JOBS posterior. **NO MERGE.**

### windows/review

#72 sigue OPEN/stale/frozen. No pertenece a BBB094 y su Review surface materialmente overlap con AAA095.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` conserva exact-lineage packaged evidence ejecutable y roja sobre #84 head `28c3810c...`; causal ownership del `unexpected-request` sigue pendiente de BBB094. Múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 099:** BBB `NIGHT-BBB-094` sobre #84 causal-boundary localization. Autoridad limitada a diagnostics y, solo si se prueba harness-only, corrección mínima del harness + fresh packaged Windows evidence. No product corrective, no integration mutation. CI-FALLBACK NONE.
