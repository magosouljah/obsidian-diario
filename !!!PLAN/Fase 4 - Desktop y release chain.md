# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 083:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 permanece `[ 🟡 ]`.
- PR #79 / F4 25.2 readiness docs fue integrado como `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; parents `957f97771b7a15554cf6e002fe9eb215c71a65cc` + `a3c4d56e8317d7711832154ecc72afe581d2b309`.
- Ese merge NO demuestra tester execution, signing/notarization ni global 25.2 closure.

### windows/auth

- #71 conserva regression proof: Desktop login no persistió `beatgaler:account-session:v1` bajo la sesión probada.
- #74 sigue OPEN/Ready, head `14dfba52775f40f1956e3d1dcb343b07b147ba0c`, stale base `a9d35a3d69dd9127029fb851d189f9bd3079d03b`, actualmente not mergeable; no se presume integrable.
- `NIGHT-BBB-077` no dejó resultado final antes de CYCLE 083; superseded/not PASS.
- `NIGHT-BBB-078` posee esta pieza: REUSE #71/#74, reconcile solo el corrective de auth si history-preserving/ownership-safe, fresh exact-head CI + authoritative Windows auth journey, NO MERGE.

### windows/review

#72 sigue OPEN/stale/frozen hasta refresh seguro; no pertenece a BBB078 salvo reasignación futura explícita.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware permanecen externos/abiertos.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` = automated evidence. `windows/auth` y múltiples journeys permanecen sin evidencia actual completa; iPhone sigue external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
PR #79 docs-only readiness artifact ya está integrado. Gate real sigue pendiente de beta/tester execution, 0 P0 y ningún P1 core conocido, además de release-chain evidence aplicable.

**Owner CYCLE 083:** BBB `NIGHT-BBB-078` sobre F4/25.1 windows/auth. BBB no está autorizado a mutar integration este ciclo.
