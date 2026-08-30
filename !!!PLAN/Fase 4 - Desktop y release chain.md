# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 038:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` con exact-head CI verde. 25.1 completo permanece abierto.

PR #71 `bbb/night-25.1-windows-auth @ 29656aa0...` sigue OPEN/Ready/mergeable sobre base `02a40564...`. BBB034 hizo attribution-first y confirmó que el workflow llegó a WebDriver/session real y ejecutó `tests/e2e/auth-flow.e2e.mjs`; el failure literal fue: Desktop login did not persist the returned session token. `AccountGate` productivo usa la misma key esperada y `storeSession()` intenta persistir antes de `syncSession`, por lo que esto se procesa como **PRODUCT_FINDING**, no como generic CI/harness red.

Consecuencias:
- `windows/auth` sigue `NOT_COVERED`;
- #71 no se modifica ni promociona hasta corrective productivo demostrado;
- AAA recibe ownership explícito del product-auth finding bajo `NIGHT-AAA-036`;
- BBB deja #71 intacta y avanza una fila independiente: `windows/review` bajo `NIGHT-BBB-035`.

## Owner actual F4

**BBB — `NIGHT-BBB-035` — F4 / 25.1 windows/review.**

PRIMARY:
1. Duplicate-check de candidate/harness existente para Windows Review.
2. Reusar embedded/desktop harness ya integrado; no tocar product auth ni archivos/branch/PR #71.
3. Crear/reusar solo slice F4 independiente para assertions literales de Review journey.
4. No promover matrix antes de PASS literal.
5. Si assertion revela bug de producto: `PRODUCT_FINDING` + STOP.
6. Si PASS, promover únicamente `windows/review`, luego fresh Windows Review + F4 Matrix + D6 + D7 + Required CI/Desktop Portability antes de race-check/merge.

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
- `windows/auth = NOT_COVERED` — #71 product finding; waiting explicit product corrective by AAA.
- `windows/review = NOT_COVERED` — BBB035 active independent slice.
- other Web/Windows/macOS journeys remain NOT_COVERED unless dedicated evidence exists.
- iPhone rows remain PENDING_EXTERNAL.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia.
