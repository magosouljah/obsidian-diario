# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 062:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

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

### 25.2 — `[ 🟡 ] PR #79 STALE / CONDITIONAL FALLBACK BBB057`

PR #79 remains OPEN/non-draft/mergeable:
- branch `bbb/f4-25.2-beta-readiness @ c6ec2910522370f2506beb71ad5e0fa0317d6a61`;
- historical base `a306e3b3...`;
- live integration = `63c9f8c9...`;
- exactly one intended docs-only file `docs/beta/0.9.0-beta.1-readiness.md` (+84).

`NIGHT-BBB-056` no produjo resultado final verificable antes de CYCLE 062 y queda superseded. La nueva decisión RO de F3/20.2 hizo ejecutable un carril de mayor valor: BBB057 tiene PRIMARY en capacity runtime 80 expected / 160 validation.

#79 queda preautorizado únicamente como **CI-FALLBACK de BBB057** si el PRIMARY entra realmente en `WAITING_EXTERNAL/WAITING_RUNTIME`: history-preserving narrow refresh sobre live integration, verificar delta exacto de un solo archivo y fresh exact-head CI. **NO MERGE CYCLE 062** y no cerrar 25.2.

Even if #79 later merges, 25.2 remains open for real beta/tester/signing evidence.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido. 25.2 is not closed by the readiness document alone.
