# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 084:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva fail-before autoritativo: Desktop login no persistió `beatgaler:account-session:v1` bajo la sesión probada.
- `NIGHT-BBB-078` realizó un refresh history-preserving seguro de #74 sin mutar integración. #74 ahora está OPEN/Ready/mergeable en head `b3468003a80288109e2d537a7aa3f25a7269927c`, base exacta `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, con el mismo delta intencional de dos archivos.
- Exact-head post-refresh: Desktop Portability `33396503472` SUCCESS; D6 `33396503463` SUCCESS; D7 `33396503465` SUCCESS; Web Production Build `33396503570` SUCCESS; Upgrade 21.2 Staging `33396503568` SKIPPED.
- Eso NO satisface todavía windows/auth: falta el journey literal packaged Windows atribuible a la lineage refrescada.
- `NIGHT-BBB-079` posee esa prueba actual. NO MERGE.

### windows/review

#72 sigue OPEN/stale/frozen. No pertenece a BBB079; además su Review surface tiene dependencia material con el trabajo activo AAA080, por lo que no es fallback seguro.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` y múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 084:** BBB `NIGHT-BBB-079` sobre F4/25.1 windows/auth. BBB no está autorizado a mutar integration este ciclo.
