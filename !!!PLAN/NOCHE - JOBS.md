# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 030`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 030

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- GitHub vivo sigue sin merge posterior a #67.
- PR #69: OPEN/Ready/mergeable @ `b2ab75ae...`; helper/unit + D6/D7/Desktop Portability green, pero product App path sigue bypassing `saveAllWebItems`.
- PR #63: OPEN/Ready/mergeable @ promotion head `1b957eff...`; Windows Import `33305947664` SUCCESS; Required CI `33305947677` SUCCESS; F4 Matrix `33305947676` FAILURE en `matrix-contract`.
- PR #70: OPEN/Ready/mergeable @ `5a99ebf2...`; focused F2 `33304798320` SUCCESS; Required CI `33304798363` FAILURE en PostgreSQL live/recovery.
- PR #68: OPEN/Ready/mergeable @ `2a988ec2...`; exact-head green histórico; merge execution sigue bloqueado externamente/frozen.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos los canónicos requeridos: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; ledgers JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo vía comentarios; GitHub actual. GitHub/runtime fue autoridad.

Hechos verificados:
1. integration continúa exactamente `3ad8f55a...`.
2. AAA `NIGHT-AAA-029` terminó PENDING/STOP_EVIDENCE_INSUFFICIENT: #69 helper/tests/CI están verdes, pero `App.tsx -> handleReviewedSaveAll` no consume el coordinator productivo; handoff Issue #41 `5468039685`.
3. BBB `NIGHT-BBB-028` creó promotion head `1b957eff...`; su handoff `5468076864` cerró WAITING_CI. Recheck JOBS posterior: Windows Import run `33305947664` SUCCESS y Required CI `33305947677` SUCCESS, pero F4 Functional Matrix `33305947676` FAILURE en `Validate dependency-safe matrix contract`.
4. WOZ `NIGHT-WOZ-028` no tiene RESULTADO DEL TURNO/handoff nuevo observable; #70 sigue sin cambio en `5a99ebf2...`. Se supersede con 029 para ejecución monotónica, conservando el mismo scope.
5. #70 changed-file scope = `.github/workflows/f2-13.1-orphan-lifecycle.yml`, `cloud-server/garbage-reconciliation-worker.js`, `cloud-server/orphan-upload-lifecycle.js`, `cloud-server/tests/orphan-upload-lifecycle.test.cjs`; no migration file.
6. Required CI reciente de #63 contra el mismo integration baseline tuvo `PostgreSQL live integration + recovery gate` SUCCESS; por tanto el rojo de #70 no se clasifica automáticamente provider-wide ni candidate-specific sin logs/repro.
7. #68 sigue frozen y no se reintenta ceremonialmente.
8. F0/F1 external tails no tienen evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-029
`PENDING / STOP_EVIDENCE_INSUFFICIENT` procesado. Nueva orden `NIGHT-AAA-030` mantiene SAME #69 y exige únicamente el wiring productivo mínimo al coordinator existente + focused evidence + fresh CI.

### BBB / NIGHT-BBB-028
`PENDING / WAITING_CI` procesado con recheck final. Promotion head tiene Windows Import y Required CI verdes; F4 Matrix rojo. Nueva orden `NIGHT-BBB-029` reduce el blocker a attribution/corrective del `matrix-contract`; no reabre harness.

### WOZ / NIGHT-WOZ-028
`NO_RESULT / SUPERSEDED_BY_JOBS`. GitHub #70 unchanged. Nueva orden `NIGHT-WOZ-029` conserva SAME #70 y exige attribution-first del PG gate failure.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / #63:** resolver matrix-contract rojo del promotion head → fresh exact-head gates → race-check/merge.
2. **F2 / 13.1:** AAA #69 minimal product wiring + WOZ #70 PG-gate attribution/fix en paralelo sin overlap.
3. **F3 / 18.1 / #68:** candidate green pero bloqueado por execution layer; preservar frozen.
4. **F2 / 12.1:** cold/warm runtime Web real cuantificado.
5. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20 y F4 25.2/otros matrix gaps. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 030 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | #69 helper/CI green; product wiring missing | `NIGHT-AAA-030` — SAME #69 minimal product wiring + focused evidence + fresh CI/merge | `NONE` |
| BBB | #63 promotion head: Windows Import+Required CI green; matrix-contract red | `NIGHT-BBB-029` — SAME #63 matrix-contract attribution/corrective + fresh gates + merge | `NONE` |
| WOZ | 028 no result; #70 focused PASS / Required CI PG failure unchanged | `NIGHT-WOZ-029` — SAME #70 attribution/fix + integrate only if green | `NONE` |

No overlap material: AAA=F2 frontend/product wiring; BBB=F4 matrix transaction; WOZ=F2 server orphan lifecycle. #68 frozen.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-030`
PRIMARY: SAME #69; implementar solo wiring mínimo `App/Review/Import/Bulk -> saveAllWebItems`, demostrar saved/conflict/failed + partial/retry semantics, fresh exact-head CI y race-check/merge si green.  
EVIDENCE: wiring real, focused tests, exact-head CI, merge SHA si integra.  
STOP: server/#70, 13.2+, durable semantics fuera del wiring mínimo, baseline race, CI rojo no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-029`
PRIMARY: SAME #63; atribuir/corregir únicamente F4 `matrix-contract` rojo del promotion head; no reabrir Windows harness. Si cambia head, F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head; race-check/merge solo si todo green.  
EVIDENCE: error/atribución matrix-contract, delta mínimo, fresh gates, race-check, merge SHA/integration HEAD.  
STOP: producto fuera F4, harness sin evidencia, otros matrix gaps/D22/D23/25.2, failure no atribuible, baseline race.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-029`
PRIMARY: SAME #70; aceptar focused run `33304798320` SUCCESS; diagnosticar Required CI `33304798363` PG failure; corregir solo si atribuible; fresh focused + Required CI cuando corresponda; race-check/merge solo si todo aplicable green.  
EVIDENCE: failure attribution, logs/repro, tests, exact-head CI, merge SHA si integra.  
STOP: failure no atribuible/transitorio sin corrective justificado, frontend AAA/#69, #68/billing/Desktop/infra, baseline race.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2/13.1: #69 product wiring + #70 Required CI PG gate attribution/resolution.
7. F3/18.1: #68 merge blocked by execution layer; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: #63 F4 matrix-contract red; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm; 13.1 reducido a product wiring #69 + PG-gate #70.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; #68 green pero no merged; 18.2–20 abiertos.
- **F4:** Windows Import permanece literal PASS incluso en promotion head; el blocker actual es matrix-contract; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 030

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 030;
- `!!!PLAN/Fase 2 - Web y UX.md` → AAA030/WOZ029 + current #69/#70 blockers;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → BBB029 + promotion-head matrix-contract failure;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 030;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-030`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-029`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-029`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 030.

`Registro de avances.md` fue leído; no se añade entrada porque no hubo nuevo merge/PASS de gate estable. F0/F1/F3 no se modifican porque sus estados materiales no cambiaron. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de claims.
2. Procesar AAA030 / BBB029 / WOZ029 una sola vez.
3. Si cualquier PR integra y mueve baseline, revalidar candidates restantes por combinación material.
4. No aceptar Windows Import green como sustituto de F4 Matrix green.
5. No aceptar focused #70 green como sustituto de Required CI.
6. Mantener #68 frozen mientras execution layer bloquee merge.
7. Mantener 12.1 abierto hasta runtime cold/warm real.
8. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-030
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_029: PENDING product-wiring gap; #69 unchanged
BBB_028: promotion head 1b957eff; Windows Import 33305947664 SUCCESS; Required CI 33305947677 SUCCESS; F4 Matrix 33305947676 FAILURE
WOZ_028: NO_RESULT; #70 unchanged; focused F2 SUCCESS + Required CI PG FAILURE carried
AAA_NEW: NIGHT-AAA-030 SAME #69
BBB_NEW: NIGHT-BBB-029 SAME #63 matrix-contract corrective
WOZ_NEW: NIGHT-WOZ-029 SAME #70 attribution/fix
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 030 completado.
