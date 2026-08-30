# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 049:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

SAME PR #74 permanece factual:
- OPEN/Ready/mergeable, no mergeado;
- base exacta `a9d35a3d69dd9127029fb851d189f9bd3079d03b`;
- head `14dfba52775f40f1956e3d1dcb343b07b147ba0c`;
- evidencia exact-head previamente verde preservada.

#74 queda frozen bajo el blocker previo de merge-flow; #71 solo se revalida después de integración real de #74 y nueva asignación JOBS.

### windows/review

SAME #72 sigue factual:
- PR #72 OPEN; draft=false; mergeable=true; merged=false;
- base exacta `a9d35a3d...`;
- head `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`;
- Windows Review `33327407530` SUCCESS;
- F4 Functional Matrix `33327407521` SUCCESS;
- D6 `33327407516` SUCCESS;
- D7 `33327407519` SUCCESS;
- Required CI `33327407533` SUCCESS;
- Windows Import `33327407514` SUCCESS;
- Upgrade `33327407526` SKIPPED/no aplicable.

`NIGHT-BBB-043` no dejó RESULTADO DEL TURNO/handoff observable antes de CYCLE 049 y queda superseded. `NIGHT-BBB-044` es owner único para race-check + integración SAME #72; si baseline cambia por un merge paralelo, refresh estrecho + fresh applicable CI antes de merge.

**CI-FALLBACK BBB:** F4/25.2 READ-ONLY readiness inventory solo si PRIMARY queda realmente esperando operación externa de merge/review/queue; sin rama/PR/commit/write y sin tocar #72/auth/legal/producto/matrix/docs. Recheck PRIMARY antes de cerrar.

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
- `windows/auth = NOT_COVERED` — #74 candidate green/mergeable pero merge-flow bloqueado; #71 espera integración real + nueva assignment.
- `windows/review` — #72 exact-head dedicated journey + matrix + required gates verdes; integración asignada BBB044.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

### 25.2 — `[ ] / READ-ONLY FALLBACK PREAUTHORIZED FOR BBB ONLY WHEN PRIMARY WAITS EXTERNAL MERGE/REVIEW/QUEUE`
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

La auditoría fallback no cierra 25.2 ni autoriza implementación automática.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.
