# Fase 4 — Artefactos desktop confiables y release chain

> Leer `Plan Maestro.md`. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 040:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado actual

PR #63 fue MERGED y dejó `windows/import = AUTOMATED_PASS` con exact-head CI verde. 25.1 completo permanece abierto.

PR #71 sigue como evidencia de regresión Auth: bajo WebDriver/session real el Desktop login no persistió `beatgaler:account-session:v1`. `windows/auth` sigue `NOT_COVERED`. AAA tiene ownership productivo exclusivo bajo `NIGHT-AAA-038`; AAA no toca #71.

PR #72 `bbb/night-25.1-windows-review @ e32ee7016adda60d3ac1b3be792b6ab9fa0e2708` está OPEN/Ready sobre baseline vivo. Exact-head recheck CYCLE 040:
- Desktop Portability `33319185559` SUCCESS;
- D6 `33319185558` SUCCESS;
- D7 `33319185556` SUCCESS;
- Windows Import `33319185575` SUCCESS;
- Upgrade 21.2 SKIPPED/no aplicable;
- dedicated Windows Review `33319185581` **FAILURE**.

Job `99278020815`: setup/checkout/Node/Rust/npm/embedded preparation SUCCESS; failure queda localizado en `Run Windows Review E2E harness`. Aún no está atribuido a harness vs conducta productiva, por lo que `windows/review` permanece `NOT_COVERED` y no hay matrix promotion.

## Owners actuales F4

**AAA — `NIGHT-AAA-038` — product-auth blocker.** Root cause/corrective mínimo token/session persistence; no tocar #71.

**BBB — `NIGHT-BBB-037` — SAME #72 windows/review.** Attribution-first del run `33319185581`; harness defect → corrective mínimo SAME #72; product behavior defect tras sesión/assertion → `PRODUCT_FINDING` + STOP. No tocar auth/#71.

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
- `windows/auth = NOT_COVERED` — product finding; waiting AAA038 corrective, después #71 refresh/revalidation bajo asignación JOBS explícita.
- `windows/review = NOT_COVERED` — #72 dedicated workflow failure awaiting BBB037 attribution/corrective.
- other Web/Windows/macOS journeys remain NOT_COVERED unless dedicated evidence exists.
- iPhone rows remain PENDING_EXTERNAL.

### 25.2
- [ ] design freeze tokens/nav/library/drawer/player/settings/wizard;
- [ ] backlog P2/P3;
- [ ] guion beta/formulario/criterios.

**Gate:** beta candidate `0.9.0-beta.1`, 0 P0 y ningún P1 core conocido.

**Regla:** no convertir findings/product gaps/external prerequisites en PASS por conveniencia.
