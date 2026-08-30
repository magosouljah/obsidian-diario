# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 056:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

PR #74 permanece OPEN/Ready/mergeable en snapshot anterior pero frozen por blocker de merge/refresh. #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review

#72 sigue OPEN/Ready/mergeable sobre snapshot antiguo; no existe safe update-branch/history-preserving refresh en el flujo disponible. Frozen; no historical CI promotion.

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

BBB049 residual map verified on live integration:
- Web: auth/import/review/playback/edit/trash/offline/youtube/updater/billing = `NOT_COVERED`;
- Windows: import/updater `AUTOMATED_PASS`; auth/review/playback/edit/trash/offline/youtube/billing = `NOT_COVERED`;
- macOS: updater `AUTOMATED_PASS`; auth/import/review/playback/edit/trash/offline/youtube/billing = `NOT_COVERED`;
- iPhone: all ten rows = `PENDING_EXTERNAL`.

`NIGHT-BBB-050` no produjo resultado final antes de CYCLE 056 y queda superseded. `NIGHT-BBB-051` owns exactly one independent next row: **Web/auth dedicated journey**. It must prefer existing implementation + deterministic test/harness evidence, use fresh exact-head CI for changes, and stop on overlap/broad product defect. This does not promote any other row.

### 25.2 — `[ 🟡 ] GREEN CANDIDATE / SERIALIZED HOLD`

PR #79 remains OPEN/non-draft/mergeable:
- branch `bbb/f4-25.2-beta-readiness @ c6ec2910522370f2506beb71ad5e0fa0317d6a61`;
- exact base `a306e3b3...`;
- exactly one docs-only file `docs/beta/0.9.0-beta.1-readiness.md` (+84);
- compact P2/P3 beta backlog + beta test script/result form/entry-exit criteria;
- no product behavior/release/signing/provider mutation or tester PII.

#79 remains intentionally `HOLD_GREEN_PENDING_SERIAL_INTEGRATION` while WOZ owns #78 as the only integration mutation in CYCLE 056. If integration moves, #79 must be reconciled and revalidated before merge. External beta/tester/signing evidence remains open regardless.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido. 25.2 is not closed by the readiness document alone.
