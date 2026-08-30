# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 052:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

SAME PR #74 permanece OPEN/Ready/mergeable en su snapshot anterior, pero sigue frozen bajo el blocker previo de merge-flow. #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review

SAME #72 al preflight CYCLE 052:
- OPEN; draft=false; merged=false; mergeable=true;
- head `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`, sin cambio desde CYCLE 050;
- base SHA registrada en PR: `a9d35a3d69dd9127029fb851d189f9bd3079d03b`;
- live integration sigue `a306e3b3...` por merge #73;
- old green evidence es histórica y no autoriza merge sobre live baseline.

`NIGHT-BBB-046` no dejó RESULTADO DEL TURNO/handoff observable antes de CYCLE 052 y queda superseded. `NIGHT-BBB-047` es owner único para narrow refresh SAME #72 sobre `a306e3b3...`, fresh applicable exact-head CI y merge solo si vuelve a quedar race-clean/green.

**CI-FALLBACK BBB:** F4/25.2 READ-ONLY readiness inventory solo si PRIMARY queda realmente esperando CI/merge/review/queue; sin writes; recheck PRIMARY antes de cerrar.

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
- `windows/auth = NOT_COVERED` — #74 holding; #71 waits integration + nueva assignment.
- `windows/review` — #72 candidate sigue stale tras #73; refresh/fresh CI asignado BBB047.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

### 25.2 — `[ ] / READ-ONLY FALLBACK PREAUTHORIZED FOR BBB ONLY WHEN PRIMARY WAITS EXTERNAL OPERATION`
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

La auditoría fallback no cierra 25.2 ni autoriza implementación automática.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.
