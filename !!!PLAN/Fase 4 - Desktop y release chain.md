# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 042:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` con exact-head CI verde. 25.1 completo permanece abierto.

### windows/auth

PR #71 sigue como evidencia de regresión Auth: bajo WebDriver/session real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`.

AAA038 creó PR #74 `aaa/night-25.1-auth-session-corrective @ 92058b42e6e455f641e8a494f5c85ae1f2214834` sin tocar #71. D6 `33321752555` y D7 `33321752537` terminaron SUCCESS, pero `Test - Desktop Portability / Required CI` `33321752522` terminó FAILURE. El fallo es literal y atribuible al candidate: `src/platform/index.ts(10,22): Property '__TAURI_INTERNALS__' does not exist on type '(Window & typeof globalThis) | RuntimeWindow'`; Web build y portability/native gates caen por ese compile error. No hay PASS, no integración y #71 no vuelve todavía a BBB.

**AAA — `NIGHT-AAA-039`:** SAME #74; corregir solo ese error de tipado/compile preservando el corrective runtime y el contrato auth; focused regression + fresh exact-head gates. No tocar #71 ni matrix.

### windows/review

PR #72 `bbb/night-25.1-windows-review @ 3219996e181ef3f53508b1ea1d272d84b73bc1a4` está OPEN/Ready/mergeable sobre baseline vivo. BBB037 atribuyó el fallo previo a expectativa incorrecta del harness (`F#m` vs normalización productiva `f#m`) y corrigió solo el test.

Fresh exact-head sobre `3219996e...`:
- Windows Review `33321799798` — **SUCCESS**;
- Windows Import `33321799800` — SUCCESS;
- Desktop Portability `33321799802` — SUCCESS;
- D6 `33321799792` — SUCCESS;
- D7 `33321799819` — SUCCESS;
- Upgrade 21.2 — SKIPPED/no aplicable.

Este PASS literal autoriza el siguiente paso, pero `windows/review` todavía no está promovido en la matriz y #72 no está integrado.

**BBB — `NIGHT-BBB-038`:** SAME #72; promover únicamente `windows/review = AUTOMATED_PASS`, luego fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Desktop Portability sobre el nuevo head; race-check + merge solo si todos verdes. No tocar auth/#71/#74.

CI-FALLBACK AAA: `NONE`.  
CI-FALLBACK BBB: `NONE`.

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
- `windows/auth = NOT_COVERED` — #74 corrective compile failure; AAA039 assigned. Después de #74 integrado, #71 requiere nueva asignación BBB y PASS literal antes de matrix promotion.
- `windows/review = NOT_COVERED` en matriz actual — literal dedicated PASS ya existe en #72 head `3219996e...`; BBB038 asignado para promotion + fresh post-promotion gates + merge.
- otras Web/Windows/macOS journeys permanecen NOT_COVERED salvo evidencia dedicada.
- iPhone rows permanecen PENDING_EXTERNAL.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia.
