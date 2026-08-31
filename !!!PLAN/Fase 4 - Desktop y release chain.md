# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 080:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

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
#51.

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

### 25.2 — `[ 🟡 ] EXACT CANDIDATE / BBB075`

GitHub CYCLE 080 confirma PR #79 OPEN/non-draft/mergeable:
- branch `bbb/f4-25.2-beta-readiness @ a3c4d56e8317d7711832154ecc72afe581d2b309`;
- exact base SHA `957f97771b7a15554cf6e002fe9eb215c71a65cc` = live integration al preflight;
- changed_files = 1; scope docs-only `docs/beta/0.9.0-beta.1-readiness.md`;
- exact-head workflow runs observados: Test - Desktop Portability SUCCESS; D6 SUCCESS; D7 SUCCESS; Upgrade 21.2 Staging SKIPPED.

`NIGHT-BBB-074` no dejó resultado verificable antes de CYCLE 080 y queda superseded, no PASS.

**Owner CYCLE 080:** `NIGHT-BBB-075`.
PRIMARY: fresh race-check de integration/base/head/file-delta/CI y, solo si todo sigue exacto, expected-head merge de SAME #79 + verify merge SHA/parents. BBB/#79 es la única integración mutation autorizada del ciclo. CI-FALLBACK: NONE.

Incluso si #79 se integra, 25.2 permanece abierto por beta/tester/signing evidence real. El readiness document no cierra el gate por sí solo.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido; tester execution y release-chain evidence aplicable siguen pendientes.
