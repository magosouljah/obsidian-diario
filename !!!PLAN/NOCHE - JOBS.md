# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 157`.

## BASELINE VIVO / PREFLIGHT

- Lectura completa realizada: Plan Maestro; Fases 0–4; coordinación; protocolo; NOCHE JOBS/AAA/BBB/WOZ; Registro de avances completo; Issue #41 completo; GitHub vivo.
- Baseline vivo: `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.
- PR #99 sigue MERGED y aporta fail-closed Web deployment/source SHA binding; no equivale a clean canonical production deployment proof.
- Release = `NO-GO`; F5 = CLOSED.

## RESULTADOS PROCESADOS — CYCLE157

- `NIGHT-AAA-152` → no RESULTADO DEL TURNO en NOCHE-AAA, no matching worker handoff posterior y GitHub #89 sin movimiento → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-151` → no RESULTADO DEL TURNO, no matching worker handoff y no recent-reauth candidate nuevo → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-155` → no resultado terminal, pero durante este preflight GitHub produjo PR #100 para Issue #97 → `ACTIVE_PROGRESS / SUPERSEDED_BY_WOZ156 / NOT_PASS`.
- No se infiere DONE/PASS por ausencia de resultado.

## DELTA MATERIAL / GATES

### PR #100 / Issue #97

PR #100 `F2/97: instrument startup and library reveal surfaces` apareció durante CYCLE157. Estado al cierre operativo: OPEN/Ready, exact base `c2766fb23de5bb837a7fef4080a6aa7a6716f15e`, head `5f0a0727edacbcb404eb4e31571468262744ec95`.

Scope literal de #100: observational instrumentation only. Añade startup trace shared Web/Desktop, visible-surface taxonomy y beat-card counts; no cambia startup UX/routing/library truth/performance behavior. Por tanto es progreso de WOZ155, no closure de #97.

CI exact-head observable:
- Web - Production Build `33583643161` SUCCESS.
- D6 `33583643150` SUCCESS.
- D7 `33583643244` SUCCESS.
- F0 0.20 HEAD Secret Scan `33583643258` SUCCESS.
- Upgrade 21.2 Staging `33583643339` SKIPPED.
- Test - Desktop Portability `33583643291` sigue `in_progress` al último recheck.

WOZ156 debe REUSE #100, capturar factual Web+Desktop startup traces/measurements, aislar causal bottleneck y convertir esa misma lineage en actual minimum correction antes de merge de cierre. Instrumentation-only no puede marcar #97 PASS.

### F2/12.1

#99 aporta el mecanismo para probar identidad inmutable del Web runtime, pero exit condition sigue exigiendo clean production deployment desde canonical integration HEAD y public readback marker exactamente igual al SHA. No apareció evidencia literal nueva para `c2766fb...`. Estado: `NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN`.

### #89

PR #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`, stale versus live. Required CI genérico histórico es SUCCESS pero el dedicated F0/0.9 security gate de ese exact stale head continúa FAILURE; no waiver. AAA153 recibe ownership exclusivo de REUSE/refresh/revalidation/integration condicional.

### #93

Sigue OPEN/stale @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`; old-base Windows Auth evidence no es canonical exact-head. Sin mutation owner CYCLE157.

## CAMINO CRÍTICO RECALCULADO DESDE CERO

1. `F2/12.1 clean canonical production deployment/source proof` — blocker factual externo/SHA-dependent.
2. `Issue #97 / PR #100`: measurements Web+Desktop → causal finding → minimum shared correction → exact evidence/integration.
3. `F0/0.9 / #89`: P1 refresh + exact-green + integration.
4. `productive recent-reauth seam → F2/15.1 durable Trash`.
5. `F2/13.2 safe write-surface resolution` cuando #97 libere shared surfaces.
6. `F1/1.7 → 1.8` con facts frescos.
7. `#93 / F4 25.1` solo si 1.7 lo mantiene `IN_ALPHA`.
8. En paralelo: F0 1.2/2.2, production signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## TABLERO CYCLE157

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA `NIGHT-AAA-153` | F0/0.9 REUSE #89; history-preserving refresh, mínimo gate-precondition correction, exact-head revalidation y conditional expected-head merge #89 only | NONE |
| BBB `NIGHT-BBB-152` | minimum productive same-provider recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97/#100/#89 | F3/18.2 READ-ONLY applicability inventory only during genuine external wait after clean candidate |
| WOZ `NIGHT-WOZ-156` | REUSE #100; finish instrumentation CI, obtain Web+Desktop measurements, isolate cause, amend same lineage with actual minimum shared correction; conditional expected-head merge #100 only after correction + exact evidence | NONE |

**Integration mutations autorizadas CYCLE157: AAA153 / #89 y WOZ156 / #100, únicamente dentro de scopes disjuntos y con exact applicable CI SUCCESS + no required review blocker + race-free expected-head. #100 instrumentation-only no autoriza closure merge. Si uno mueve integración, el otro debe refresh/revalidar. BBB152 NO MERGE. #93 no tiene mutation/merge authorization.**

## FALLBACKS

### AAA153

`CI-FALLBACK: NONE`. F2/12.1 es SHA-dependent; #97/#100 y recent-reauth ya tienen owners; #93 espera 1.7.

### BBB152 — F3/18.2 READ-ONLY

- Scope: inventario de reconciliation/provider scenarios existentes únicamente mientras PRIMARY espera externamente después de candidate limpio.
- Evidence: refs exactas + unresolved 3DS/rejection/late-payment/renewal/cancel/plan-change/refund/webhook/reconciliation + clasificación `SOFTWARE_PROVEN / UNVERIFIED_EXTERNAL / NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`.
- STOP: provider/payment mutation, new PR, gate promotion, overlap, o PRIMARY deja de esperar. Volver al PRIMARY y recheck antes de cierre.

### WOZ156

`CI-FALLBACK: NONE`. El trabajo seguro durante wait de #100 sigue siendo el mismo PRIMARY de medición/causalidad; F2/12.1 depende del canonical SHA y #93/recent-reauth tienen constraints separados.

## PROGRESO F0–F4

- **F0:** #89 P1 sigue abierto/red pero tiene owner ejecutable AAA153; 1.2/2.2 + external release tails abiertos.
- **F1:** D6–D10.1 PASS; D10.2 `ALPHA CANDIDATE NOT READY`; 1.7 espera 12.1/#97/#89/recent-reauth facts.
- **F2:** 12.1 source-binding mechanism integrado pero clean canonical production proof abierto; #97 ahora tiene instrumentation candidate #100 pero actual correction sigue abierta; 13.2 blocked; 15.1 detrás de recent-reauth.
- **F3:** provider/payment, legal implementation y runtime160/capacity abiertos/external o pendientes de explicit alpha applicability.
- **F4:** #93 stale/no owner; 25.1 global open; #97 requiere Desktop+Web correction/validation; production signing/notarization/hardware/tester execution externos.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC

- Asignaciones escritas directamente: AAA153, BBB152, WOZ156.
- Plan Maestro, F0–F4 y `Equipo multi-IA - Roles y coordinación.md` sincronizados a CYCLE157.
- `Registro de avances.md` fue leído completo; no se reescribió porque no hubo nuevo merge/PASS/runtime canónico que promover.
- `Plan Maestro 2208 copy DONT TOUCH .md` untouched.
- JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Procesar AAA153/BBB152/WOZ156.
2. Recheck #100 exact-head CI and real Web/Desktop traces; no closure until actual correction evidence exists.
3. Si aparece clean canonical production deployment proof, hacer close review literal de F2/12.1.
4. Si AAA153 deja #89 refreshed exact-green, integrar solo bajo expected-head/race-free authority y procesar merge factual.
5. Cuando #97 libere shared surfaces, abrir F2/13.2; continuar recent-reauth → F2/15.1; después reemitir F1/1.7.

```text
CYCLE_ID: NIGHT-JOBS-157
INTEGRATION_HEAD_AT_CLOSE_EXPECTED: c2766fb23de5bb837a7fef4080a6aa7a6716f15e
AAA_NEW: NIGHT-AAA-153
BBB_NEW: NIGHT-BBB-152
WOZ_NEW: NIGHT-WOZ-156
ISSUE97: OPEN / PR100 ACTIVE_INSTRUMENTATION / OWNER_WOZ156 / NOT_PASS
PR100_HEAD: 5f0a0727edacbcb404eb4e31571468262744ec95
PR89: OPEN_STALE / DEDICATED_SECURITY_GATE_FAILURE / OWNER_AAA153
PR93: OPEN_STALE / NO_MUTATION_OWNER
F2_12.1: NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN
F2_13.2: BLOCKED_WRITE_SURFACE / UNASSIGNED
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 157 termina aquí.
