# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 039:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` con exact-head CI verde. 25.1 completo permanece abierto.

PR #71 `bbb/night-25.1-windows-auth @ 29656aa0...` sigue como evidencia de regresión Auth sobre baseline previo. BBB034 confirmó WebDriver/session real y fallo literal: Desktop login no persistió `beatgaler:account-session:v1`. `AccountGate` productivo usa la key esperada y `storeSession()` intenta persistir antes de `syncSession`, por lo que se procesa como **PRODUCT_FINDING**, no generic harness red.

Consecuencias:
- `windows/auth` sigue `NOT_COVERED`;
- #71 no se modifica/promociona hasta corrective productivo demostrado y después requerirá refresh/revalidation frente al baseline vivo;
- AAA recibe ownership explícito del product-auth finding bajo `NIGHT-AAA-037`;
- BBB avanza `windows/review` independientemente bajo `NIGHT-BBB-036`.

## Owner actual F4

**AAA — `NIGHT-AAA-037` — product-auth blocker.** Root cause/corrective mínimo token/session persistence, sin tocar #71.

**BBB — `NIGHT-BBB-036` — F4 / 25.1 windows/review.**

PRIMARY BBB:
1. Duplicate-check de candidate/harness Windows Review.
2. Reusar embedded/desktop harness; no tocar auth/#71.
3. Crear/reusar solo slice F4 independiente para assertions literales Review.
4. No promover matrix antes de PASS literal.
5. Product bug => `PRODUCT_FINDING` + STOP.
6. Si PASS, promover solo `windows/review`, luego fresh Windows Review + F4 Matrix + D6 + D7 + Required CI/Desktop Portability antes de race-check/merge.

CI-FALLBACK: `NONE`.

## Día 21

### 21.1 — `[x] DONE / INTEGRATED`
#51.

### 21.2 — `[x] DONE / INTEGRATED`
#51 merge `5b05ca845...`.

## Día 22

### 22.1 / 22.2
Signing/certificado/SmartScreen/AV/hardware remain external/open.

## Día 23

### 23.1 / 23.2
Apple Developer/certificados/notarization/hardware remain external/deferred.

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
- `windows/auth = NOT_COVERED` — product finding; waiting corrective AAA037, después refresh/revalidation de #71.
- `windows/review = NOT_COVERED` — BBB036 active independent slice.
- other Web/Windows/macOS journeys remain NOT_COVERED unless dedicated evidence exists.
- iPhone rows remain PENDING_EXTERNAL.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia.
