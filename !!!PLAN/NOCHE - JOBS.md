# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 038`.

## META

Terminar F0–F4 o reducirlos al mínimo factual de blockers externos. Prioridad: F0–F4 → sencillez → limpieza. Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head obligatorios.

## BASELINE VIVO

- `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.
- Último merge material: PR #63 → `02a40564...`.
- Release público: 🔴 `NO-GO`.
- No hubo merge nuevo durante CYCLE 038.

## PREFLIGHT FACTUAL

Leídos completos: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo; GitHub vivo. GitHub/runtime prevaleció.

Hechos verificados:
1. Integration sigue exactamente `02a40564...`.
2. AAA `NIGHT-AAA-035` no dejó RESULTADO DEL TURNO/handoff final nuevo. PR #69 sigue OPEN/mergeable @ `b2ab75ae...`, base vieja `3ad8f55a...`. Se supersede 035 y #69 pasa HOLDING.
3. BBB `NIGHT-BBB-034` cerró `PENDING / PRODUCT_FINDING`. Windows Auth `33313675968` llegó a WebDriver/session real y ejecutó `tests/e2e/auth-flow.e2e.mjs`; assertion literal: Desktop login no persistió `beatgaler:account-session:v1`. #71 permanece OPEN/Ready/mergeable @ `29656aa0...`, sin promoción/merge. Finding accepted and transferred explicitly to AAA product ownership.
4. WOZ `NIGHT-WOZ-036` no dejó resultado final nuevo. #68 sigue OPEN/Ready/mergeable, base `02a40564...`, head `68adaad4...`, 4 files/+178/-0.
5. Exact-head #68 sigue con 6 workflow runs = 5 SUCCESS + 1 SKIPPED; zero FAILURE/IN_PROGRESS/QUEUED. No CI stale promotion; merge still requires owner transaction.
6. F0/F1 no recibieron evidencia externa nueva. F2/12.1 runtime blocker persiste. #70 sigue frozen. F3/20.1 gap map sigue holding. D22/D23 externos.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-035

`NO_RESULT / SUPERSEDED_BY_JOBS`.

- #69 no cambia y pasa HOLDING.
- AAA se mueve explícitamente a product-auth porque ese finding bloquea una fila core F4 y requiere owner de frontend/product logic.

### BBB / NIGHT-BBB-034

`PENDING / PRODUCT_FINDING`.

- #71 unchanged; no matrix promotion.
- Harness/session = factual PASS hasta ejecutar spec.
- Failure literal product-facing: session token no quedó persistido después del login Desktop.
- No se afirma causa raíz ni fallo global de auth/backend.
- Corrective productivo se reasigna a AAA036; BBB deja #71 intacta como regression proof.

### WOZ / NIGHT-WOZ-036

`NO_RESULT / SUPERSEDED_BY_JOBS`.

- SAME #68 retenido.
- Exact-head evidence sigue válida y green/skipped aplicable.
- Se emite 037 únicamente para race-check + owner merge.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 / 18.1 / #68:** exact-head green; solo falta owner race-check + merge.
2. **F4 / product-auth finding:** resolver persistencia session-token Desktop para desbloquear `windows/auth` y reusar #71.
3. **F4 / 25.1 windows/review:** fila independiente que BBB puede avanzar sin tocar auth.
4. **F2 / 13.1 / #69:** coordinator probado; wiring + refresh holding mientras AAA resuelve product-auth.
5. **F2 / 12.1:** runtime browser real cold/warm blocker.
6. **F2 / #70:** stale + safe-write blocker; frozen.
7. **F3 / 20.1:** gap map listo; holding detrás de 18.1.
8. **F0/F1/F3 external tails + D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 18.2–20 y F4 remainder 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 035 sin resultado final → superseded | `NIGHT-AAA-036` — product-auth token/session persistence | `NONE` |
| BBB | 034 PRODUCT_FINDING | `NIGHT-BBB-035` — independent windows/review | `NONE` |
| WOZ | 036 sin resultado final → superseded | `NIGHT-WOZ-037` — SAME #68 race-check + merge | `NONE` |

No overlap material: AAA modifica únicamente product auth; BBB no toca auth/#71 y trabaja Review F4; WOZ solo #68/F3. #69/#70/20.1 quedan holding.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-036
PRIMARY: reproducir/diagnosticar el finding de token/session persistence de Desktop AccountGate; no tocar #71; corrective mínimo en product auth solo con causa raíz demostrada; focused regression + fresh applicable exact-head CI. Si integra, handoff para que BBB refresque #71.  
CI-FALLBACK: `NONE`.  
STOP: no reproducible, cambio de contrato/seguridad, scope creep, baseline race o CI no atribuible.

### BBB — NIGHT-BBB-035
PRIMARY: windows/review independiente; reuse harness; no tocar #71/auth productivo; literal Review assertions; harness corrective mínimo si aplica; PRODUCT_FINDING + STOP si aparece bug producto; promotion solo tras PASS literal + fresh post-promotion gates.  
CI-FALLBACK: `NONE`.  
STOP: product finding, external blocker, scope escape, baseline race o CI no atribuible.

### WOZ — NIGHT-WOZ-037
PRIMARY: SAME #68 @ `68adaad4...`; revalidar exact base/head/Ready/mergeable + 5 SUCCESS/1 SKIPPED; si integration sigue `02a40564...`, merge por flujo autorizado y verificar merge SHA + integration HEAD.  
CI-FALLBACK: `NONE`.  
STOP: baseline/head/CI change, process blocker, scope drift o external expansion.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: product wiring + baseline refresh; holding.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F3/18.1 #68: owner merge transaction pending; no technical CI blocker currently.
9. F3/20.1: internal gaps + external observability/on-call/status.
10. F4/windows-auth: product session persistence finding; #71 waiting corrective.
11. F4/25.1: many matrix rows remain NOT_COVERED/PENDING_EXTERNAL.
12. F4/25.2 + D22/D23 external signing/notarization.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69/#70 holding/frozen.
- **F3:** 17.1/17.2 integrated; 18.1 exact-head green awaiting owner merge; 20.1 holding.
- **F4:** windows/import integrated; windows/auth blocked by product finding; windows/review assigned independently; 25.1/25.2 open.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 038

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 2 - Web y UX.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-036`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-035`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-037`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 038.

F0/F1 y Registro de avances fueron leídos completos y no cambiaron porque no hubo nuevo merge/PASS estable. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` untouched.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar `NIGHT-AAA-036`, `NIGHT-BBB-035`, `NIGHT-WOZ-037` una sola vez.
3. Si #68 integra y mueve baseline, exigir revalidation/fresh exact-head en cualquier candidate posterior.
4. Si AAA integra product-auth corrective, devolver explícitamente #71 a BBB para refresh + literal Windows Auth PASS antes de matrix promotion.
5. No reactivar #69/#70/20.1 por hopping automático; solo tras recalculo JOBS.
6. No abrir F5 hasta condiciones reales F0–F4.

```text
CYCLE_ID: NIGHT-JOBS-038
INTEGRATION_HEAD_OBSERVED: 02a40564d85284a119281ff79995c9b9bcb5e833
AAA_RESULT_PROCESSED: NIGHT-AAA-035 NO_RESULT -> SUPERSEDED
BBB_RESULT_PROCESSED: NIGHT-BBB-034 PENDING/PRODUCT_FINDING
WOZ_RESULT_PROCESSED: NIGHT-WOZ-036 NO_RESULT -> SUPERSEDED
AAA_NEW: NIGHT-AAA-036
BBB_NEW: NIGHT-BBB-035
WOZ_NEW: NIGHT-WOZ-037
CI_FALLBACKS: NONE/NONE/NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 038 completado.
