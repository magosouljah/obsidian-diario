# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 045:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` integrado. 25.1 completo permanece abierto.

### windows/auth

PR #71 permanece como regression proof: bajo sesión WebDriver real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

SAME PR #74 permanece factual:
- PR #74 OPEN/Ready, no mergeado;
- base exacta `a9d35a3d69dd9127029fb851d189f9bd3079d03b`;
- head exacto `14dfba52775f40f1956e3d1dcb343b07b147ba0c`;
- D6 `33324138675` — SUCCESS;
- D7 `33324138676` — SUCCESS;
- Test - Desktop Portability / Required CI `33324138689` — SUCCESS;
- Upgrade `33324138691` — SKIPPED/no aplicable.

El corrective conserva `__TAURI_INTERNALS__` como señal primaria, packaged Tauri origins como fallback y Web/localhost ordinario como Web. No se reclama integración: integration HEAD sigue `a9d35a3d...`.

`NIGHT-AAA-040` no produjo RESULTADO DEL TURNO/handoff observable antes del CYCLE 045 y queda `NOT_PROCESSED / SUPERSEDED_BY_JOBS` para impedir ejecución tardía duplicada.

**AAA — `NIGHT-AAA-041`:** SAME #74; preflight/race-check + integración únicamente si la evidencia exact-head sigue válida. Si baseline cambia, refresh/revalidate antes de merge. No tocar #71. Después de integración real, #71 necesita nueva asignación explícita para revalidación literal Windows Auth.

### windows/review

SAME #72 continúa:
- PR #72 OPEN/Ready, no mergeado;
- base exacta `a9d35a3d...`;
- head `56dc4adf206cc53f5260c71952f84ae67d994279`;
- Windows Review `33324512156` — SUCCESS;
- Windows Import `33324512159` — SUCCESS;
- Required CI `33324512153` — SUCCESS;
- F4 Functional Matrix `33324512174` — **FAILURE**, job `matrix-contract`, paso exacto `Validate dependency-safe matrix contract`.

Por tanto `windows/review` **NO se considera integrado** y #72 no puede mergearse todavía. El fallo debe atribuirse antes de cambiar nada más; no se asume bug de producto ni se rebaja el contrato.

`NIGHT-BBB-039` no produjo RESULTADO DEL TURNO/handoff observable antes del CYCLE 045 y queda `NOT_PROCESSED / SUPERSEDED_BY_JOBS` para impedir ejecución tardía duplicada.

**BBB — `NIGHT-BBB-040`:** SAME #72; attribution-first del matrix-contract failure, corrective mínimo solo si pertenece al contrato/matriz/workflow/test de #72, fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Required CI y merge únicamente si todo verde/race-clean. No tocar auth/#71/#74.

**CI-FALLBACK BBB:** solo si PRIMARY entra realmente `WAITING_CI`, auditoría **READ-ONLY** de 25.2 design-freeze readiness; sin rama/PR/commit, sin tocar #72/auth ni cambiar producto/matrix/docs. Debe producir solo inventario factual `EXISTS/PARTIAL/GAP/PENDING_EXTERNAL` y volver a recheck PRIMARY antes de cerrar.

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
- `windows/auth = NOT_COVERED` — #74 corrective exact-head green pero aún no integrado; AAA041 asignado para la transacción de integración. #71 solo se revalida después de ese merge real y una nueva asignación.
- `windows/review` — candidate #72 contiene la promoción y dedicated PASS, pero matrix-contract está rojo; BBB040 asignado. No reclamar integración.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

### 25.2 — `[ ] / READ-ONLY FALLBACK PREAUTHORIZED FOR BBB ONLY WHEN WAITING_CI`
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

BBB puede inventariar evidencia/gaps de 25.2 únicamente bajo la condición de activación de su CI-FALLBACK; esa auditoría no cierra 25.2 ni autoriza implementación automática.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia; exact-head + race-check antes de integración.
