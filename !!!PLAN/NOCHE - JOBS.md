# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 023`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 023

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- El movimiento proviene del merge verificado de PR #67; parent base `712b49b6689a31a47902dbe95e98622d001dab40` + exact tested head `27c2f30007a687a144be289a64ab986451f05c99`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos: Plan Maestro, F0–F4, roles/coordinación, protocolo nocturno, ledgers JOBS/AAA/BBB/WOZ, Registro de avances, Issue #41 y GitHub vivo.

Hechos materiales verificados:
1. integration HEAD = `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
2. WOZ `NIGHT-WOZ-021` = DONE/INTEGRATED; #67 merged y 17.2 software puede cerrarse.
3. AAA `NIGHT-AAA-022` = PENDING por falta de benchmark cold/warm real; taxonomy/state sí quedó demostrado por evidencia integrada literal.
4. BBB `NIGHT-BBB-021` cerró WAITING_CI sobre #63 head `033c2b55a0c46471b7e7ddb3af57b626699ac6e6`. JOBS recheck: Windows Import run `33284981477` = COMPLETED/FAILURE; job `99186491944` muestra setup/checkout/Node/Rust/npm/embedded-prepare SUCCESS y `Run existing Windows import E2E harness` FAILURE.
5. PR #63 sigue OPEN/Ready, base `3ad8f55a...`, head `033c2b55...`; no replacement PR ni merge.
6. `windows/import` no tiene PASS literal y sigue `NOT_COVERED`.
7. F0/F1 tails externos siguen sin evidencia nueva que autorice cierre.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-022`
- Taxonomy/state `ready / empty / no-results / offline / auth-failure / cloud-failure` aceptado como demostrado por código/tests existentes.
- 12.1 NO se cierra: queda únicamente cold/warm real cuantificado/reproducible.
- No se ordena repetir el mismo intento sin una superficie/harness capaz de ejecutar dos startups comparables.
- Para evitar tiempo muerto, ownership AAA cambia explícitamente a F2/13.1 dependency-safe bajo `NIGHT-AAA-023`.

### BBB / `NIGHT-BBB-021`
- WAITING_CI resuelto por JOBS: `33284981477` terminó FAILURE sobre exact head `033c2b55...`.
- La preparación embedded pasó; el harness E2E falló. No se infiere la causa textual sin consumir el output del run actual.
- No PASS, no matrix promotion, no merge.
- Se emite corrective `NIGHT-BBB-022` sobre SAME #63 para consumir el primer failure causal del job `99186491944` y corregir solo F4/harness.

### WOZ / `NIGHT-WOZ-021`
- #67 exact-head CI final verde: F3 17.2 `33283532676`, D6 `33283532664`, D7 `33283532679`, temp-auth `33283532723`, Desktop Portability `33283532696` SUCCESS.
- PR #67 merged; integration post-merge `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- F3/17.2 = `[x] SOFTWARE DONE / INTEGRATED` sin reclamar Stripe productivo/infra externa.
- WOZ pasa explícitamente a F3/18.1 software-only bajo `NIGHT-WOZ-022`.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / SAME #63:** resolver el Windows Import harness hasta assertion/PASS literal; es el blocker técnico más concreto actualmente rojo.
2. **F3 / 18.1:** 17.2 ya integrado; avanzar limits/entitlements/reserva/subscription-state software reduce F3 sin depender de provider productivo.
3. **F2 / D13.1:** avanzar trabajo independiente mientras 12.1 espera una superficie real de medición cold/warm.
4. **F2 / 12.1 cold/warm:** sigue gate abierto, pero no justifica dejar AAA inactivo ni fabricar evidencia.
5. **F0/F1 + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20, resto de F4 25.1/25.2 y tails externos. F5 permanece cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 022 PENDING; taxonomy demostrado, cold/warm abierto | `NIGHT-AAA-023` — F2/13.1 | `NONE` |
| BBB | 021 WAITING_CI → run 33284981477 FAILURE | `NIGHT-BBB-022` — SAME #63 corrective desde failure actual | `NONE` |
| WOZ | 021 DONE/INTEGRATED; #67 merged | `NIGHT-WOZ-022` — F3/18.1 software-only | `NONE` |

No overlap material: AAA=Web import durability; BBB=F4 Windows E2E harness; WOZ=billing/entitlements server-side.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-023`
PRIMARY: F2/13.1 únicamente — Save All durable con resumen parcial, bulk conflict-safe o deshabilitado honestamente, garbage journal/cleanup de uploads huérfanos. REUSE-FIRST; una sola rama/PR si hay gap.  
EVIDENCE: focused success/partial-failure/conflict/cleanup tests + no silent loss + applicable exact-head CI.  
STOP: 13.2/D14/D15, billing, Desktop, infra, scope creep o CI no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-022`
PRIMARY: SAME #63; consumir run `33284981477`/job `99186491944`, identificar primer failure causal actual y hacer corrective F4/harness mínimo. Windows Import literal PASS antes de promover matrix. Head nuevo → fresh applicable exact-head gates + race-check.  
EVIDENCE: failure causal, exact delta, session/assertion/PASS o blocker nuevo factual, CI exact-head.  
STOP: bug productivo fuera de F4, 25.2/D22/D23, package/global change no justificado, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-022`
PRIMARY: F3/18.1 software-only — limits/entitlements server-side antes de reserva; transacción/reserva anti-race; Billing Portal/cancelación/subscription-state contract server-side. REUSE-FIRST #65/#67.  
EVIDENCE: concurrency/limits/state focused tests + applicable exact-head CI; migration evidence si aplica.  
STOP: Stripe/provider real, 18.2+, grace-period/business decision, infra/costo o CI no atribuible.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: único residual cold/warm runtime real cuantificado.
6. F2: D13–D15 abiertos; D13.1 ahora asignado.
7. F3: 18–20 abiertos; 18.1 ahora asignado. 16.1/16.2 conservan tails externos.
8. F4/25.1: Windows Import `33284981477` FAILURE; #63 no mergeado; otros matrix gaps siguen honestos. D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 reducido a cold/warm runtime; D13.1 en ejecución, 13.2–15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 y 17.2 software integrados; 18.1 ahora activo; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 Windows Import todavía rojo; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 023

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → baseline `3ad8f55a...`, 17.2 integrado, 12.1 residual real, #63 failure actual y owners 023/022/022;
- `!!!PLAN/Fase 2 - Web y UX.md` → taxonomy/state demostrado; cold/warm único residual; D13.1 asignado;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md` → 17.2 `[x] SOFTWARE DONE / INTEGRATED`; 18.1 asignado;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 023;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-023`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-022`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-022`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 023.

JOBS no modificó código BeatGaler ni infraestructura. No se rebajó ningún gate. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de cualquier claim.
2. Procesar BBB 022 primero si #63 produce nuevo candidate/CI; exigir Windows Import literal PASS.
3. Procesar WOZ 022 y no permitir que software 18.1 se confunda con Stripe/provider productivo.
4. Procesar AAA 023 con cero pérdida silenciosa como gate literal de D13.
5. Mantener 12.1 cold/warm como residual explícito hasta que exista evidencia runtime real.
6. Cualquier merge que mueva integration obliga revalidación de los otros candidates si la combinación cambió materialmente.
7. No abrir F5 hasta condiciones reales de gate F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-023
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_RESULT_PROCESSED: NIGHT-AAA-022 PENDING; taxonomy demonstrated; cold/warm remains
BBB_RESULT_PROCESSED: NIGHT-BBB-021 WAITING_CI -> 33284981477 FAILURE on 033c2b55
WOZ_RESULT_PROCESSED: NIGHT-WOZ-021 DONE/INTEGRATED -> #67 merge 3ad8f55a
AAA_NEW: NIGHT-AAA-023 ASSIGNED F2/13.1
BBB_NEW: NIGHT-BBB-022 ASSIGNED SAME #63 corrective
WOZ_NEW: NIGHT-WOZ-022 ASSIGNED F3/18.1 software-only
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 023 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-023`, `NIGHT-BBB-022` y `NIGHT-WOZ-022`.
