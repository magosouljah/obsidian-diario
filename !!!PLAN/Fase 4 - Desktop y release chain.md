# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 054:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

PR #74 permanece OPEN/Ready/mergeable en snapshot anterior pero frozen por el blocker de merge/refresh. #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review

BBB047 verificó #72 OPEN/Ready/mergeable head `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`, base snapshot `a9d35a3d...` vs live `a306e3b3...`; no existe safe update-branch/history-preserving refresh en el flujo disponible. #72 sigue frozen; no historical CI promotion.

## Día 21

### 21.1 — `[x] DONE / INTEGRATED`
#51.

### 21.2 — `[x] DONE / INTEGRATED`
#51 merge `5b05ca845...`.

## Día 22

### 22.1 / 22.2
Signing/certificado/SmartScreen/AV/hardware permanecen externos/abiertos.

## Día 23

### 23.1 / 23.2
Apple Developer/certificados/notarization/hardware permanecen externos/deferred.

## Día 24

### 24.1 — `[x] DONE / INTEGRATED`
#55.

### 24.2 — `[x] DONE / INTEGRATED`
#57.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows:
- `windows/import = AUTOMATED_PASS`;
- `windows/updater = AUTOMATED_PASS`;
- `macos/updater = AUTOMATED_PASS`.

Active/holding:
- `windows/auth = NOT_COVERED` — #74/#71 frozen on refresh/integration dependency.
- `windows/review = CANDIDATE_FROZEN` — #72 stale; safe history-preserving refresh unavailable.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

**AAA/BBB/JOBS no deben promover historical CI como fresh exact-head evidence.**

### 25.2 — `[ 🟡 ] IMPLEMENTATION ASSIGNED BBB049`

BBB047 read-only inventory established:
- EXISTS: design foundations/tokens/primitives; library navigation bridge; Drawer/Player/SettingsPanel/SetupModal; focused component tests.
- PARTIAL: release controls/matrices exist but no literal complete design-freeze 25.2 artifact.
- GAP: no dedicated P2/P3 beta backlog artifact.
- GAP: no literal beta script/form/entry-exit criteria artifact.

`NIGHT-BBB-048` produced no final result before CYCLE 054 and is superseded. `NIGHT-BBB-049` PRIMARY may materialize only those missing internal readiness artifacts by reusing existing evidence. No public release/signing/notarization/product mutation. Fresh exact-head CI required for repository changes.

**BBB CI-FALLBACK:** F4/25.1 residual journey map READ-ONLY only while BBB049 PRIMARY genuinely waits CI/review/merge; no promotion without literal evidence.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido. 25.2 is not closed by inventory or documents alone unless all literal requirements are evidenced.
