# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 046:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

SAME PR #74 permanece factual:
- OPEN/Ready/mergeable, no mergeado;
- base exacta `a9d35a3d69dd9127029fb851d189f9bd3079d03b`;
- head `14dfba52775f40f1956e3d1dcb343b07b147ba0c`;
- D6 `33324138675` SUCCESS; D7 `33324138676` SUCCESS; Required CI `33324138689` SUCCESS; Upgrade `33324138691` SKIPPED/no aplicable.

`NIGHT-AAA-041` hizo race-check y el merge expected-head fue bloqueado antes de mutación por la superficie de seguridad del connector. #74 queda `STOP_MERGE_FLOW_BLOCKED`/frozen; no repetir el mismo intento sin cambio factual. #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review

SAME #72 ahora está factual y completamente verde:
- PR #72 OPEN/Ready/mergeable, no mergeado;
- base exacta `a9d35a3d...`;
- head `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`;
- Windows Review `33327407530` SUCCESS;
- F4 Functional Matrix `33327407521` SUCCESS;
- D6 `33327407516` SUCCESS;
- D7 `33327407519` SUCCESS;
- Test - Desktop Portability / Required CI `33327407533` SUCCESS;
- Windows Import `33327407514` SUCCESS;
- Upgrade `33327407526` SKIPPED/no aplicable.

El fallo previo del matrix-contract fue atribuido a una referencia de evidencia interpretada como path; BBB corrigió únicamente el prefijo de esa referencia sin relajar el contrato ni cambiar producto. `NIGHT-BBB-041` es race-check + integración SAME #72; si baseline cambia, fresh reconciliation/CI antes de merge.

**CI-FALLBACK BBB:** F4/25.2 READ-ONLY readiness inventory solo si PRIMARY queda realmente esperando una operación externa de merge/review/queue; sin rama/PR/commit/write y sin tocar #72/auth/producto/matrix/docs. Recheck PRIMARY antes de cerrar.

CI-FALLBACK AAA: `NONE`.

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
- `windows/auth = NOT_COVERED` — #74 exact-head green pero merge-flow blocked; #71 espera integración real + nueva assignment.
- `windows/review` — #72 exact-head dedicated journey + matrix + required gates verdes; integración pendiente bajo BBB041.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

### 25.2 — `[ ] / READ-ONLY FALLBACK PREAUTHORIZED FOR BBB ONLY WHEN PRIMARY WAITS EXTERNAL MERGE/REVIEW/QUEUE`
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

La auditoría fallback no cierra 25.2 ni autoriza implementación automática.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia; exact-head + race-check antes de integración.
