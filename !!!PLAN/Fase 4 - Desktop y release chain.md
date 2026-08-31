# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 091:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva fail-before autoritativo: Desktop login no persistió `beatgaler:account-session:v1` en run `33313675968` / job `99263095638`.
- #74 permanece producto corrective lineage en head `b3468003a80288109e2d537a7aa3f25a7269927c`, base `816f946c...`.
- #84 permanece el único evidence candidate exact-lineage en `d13a1969aef1ca53ee7fbed0bcba241ceb766d42`, OPEN/Ready/mergeable, base `816f946c...`.
- #84 Required CI `33407580663` = SUCCESS, pero literal Windows auth functional journey `33407580887` / job `99538870371` = FAILURE.
- El log exacto llegó al test real `tests/e2e/auth-flow.e2e.mjs:64` y falló literalmente: `Desktop login did not persist the returned session token.` Build, checkout, deps y embedded WebDriver sí alcanzaron ejecución; por tanto el último handoff verificable `NIGHT-BBB-085` es `BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED`, no harness-only.
- `NIGHT-BBB-086` recibe ownership exclusivo y explícito de la slice de producto #74/#84 para hacer la corrección mínima que explique la persistencia del token, refrescar #84 sobre esa lineage y exigir fresh exact-head packaged Windows evidence. **NO MERGE.**

### windows/review

#72 sigue OPEN/stale/frozen. No pertenece a BBB086 y su Review surface materialmente overlap con AAA087.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` tiene evidencia exact-lineage ejecutable pero roja; múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 091:** BBB `NIGHT-BBB-086` sobre la lineage #74/#84. Autoridad limitada a producto auth mínimo + evidencia packaged Windows exact-head. BBB no está autorizado a mutar integration.
