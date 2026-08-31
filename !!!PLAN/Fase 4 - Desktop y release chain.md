# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 066:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth
PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.
PR #74 permanece OPEN/Ready sobre snapshot anterior pero frozen. #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review
#72 sigue OPEN sobre snapshot antiguo; frozen hasta refresh seguro.

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
Integrated rows: `windows/import`, `windows/updater`, `macos/updater` = `AUTOMATED_PASS`.
Web/auth y múltiples journeys siguen `NOT_COVERED`; iPhone sigue `PENDING_EXTERNAL`.

### 25.2 — `[ 🟡 ] PR #79 STALE / CONDITIONAL FALLBACK BBB061`

GitHub CYCLE 066 confirms PR #79 remains OPEN/non-draft/mergeable:
- branch `bbb/f4-25.2-beta-readiness @ c6ec2910522370f2506beb71ad5e0fa0317d6a61`;
- historical base SHA `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`;
- live integration = `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`;
- exactly one intended docs-only file `docs/beta/0.9.0-beta.1-readiness.md` (+84).

`NIGHT-BBB-060` did not produce a final result before CYCLE 066 and is superseded. BBB061 has PRIMARY in F3/20.2 runtime capacity because the approved 80/160 target makes that lane more closure-critical.

#79 is preauthorized only as **CI-FALLBACK of BBB061** if PRIMARY truly enters `WAITING_EXTERNAL/WAITING_RUNTIME`: history-preserving narrow refresh onto live integration, verify one-file docs-only delta, fresh exact-head CI. **NO MERGE CYCLE 066** and do not close 25.2.

Even if #79 later merges, 25.2 remains open for real beta/tester/signing evidence.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido. 25.2 is not closed by the readiness document alone.
