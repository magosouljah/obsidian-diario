# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 154`.

## BASELINE VIVO / PREFLIGHT

- Lectura completa realizada: Plan Maestro; Fases 0–4; coordinación; protocolo; NOCHE JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41; GitHub vivo.
- Baseline vivo cambió materialmente desde CYCLE153: `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.
- PR #98 es ahora MERGED; exact candidate head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`; Required CI run `33575511576` / check `100081022125` = SUCCESS. Merge commit/head `c4e203cf...` tiene como parent previo `aa445095...` y candidate `00da0ab...`.
- Release = `NO-GO`; F5 = CLOSED.

## RESULTADOS PROCESADOS — CYCLE154

- `NIGHT-AAA-149` → sin RESULTADO DEL TURNO/handoff worker posterior a CYCLE153 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-148` → sin RESULTADO DEL TURNO/handoff worker posterior a CYCLE153 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-152` → sin final handoff escrito, pero GitHub independientemente prueba que su único integration outcome autorizado ocurrió: **PR #98 MERGED + exact-head Required CI SUCCESS + integration advanced to `c4e203cf...`**. Se procesa como `DONE / PR98_PRODUCTION_WEB_MTProto_CLEANUP_INTEGRATED` únicamente; no como F2/12.1 PASS.

## DELTA MATERIAL / GATES

### F2/12.1

#98 ya está integrado y su body reporta clean production deployment, public/local health PASS, library materialization, artwork y playback success. Aun así, deployment-source identity exacta no está demostrada por evidencia inmutable observada por JOBS; por evidence-before-claim, 12.1 sigue `NOT_PASS / RUNTIME_SOURCE_BINDING_OPEN`.

### Issue #97

OPEN: `Pre-Beta 1: make library reveal near-instant across Web/Desktop`; body dice `Must be addressed before Beta 1`. #98 ya liberó las superficies startup/App, así que #97 pasa a execution lane prioritaria.

### #89 / #93

- #89: OPEN @ `daf87da6...`, recorded base `816f946c...`, stale; F0/0.9 run `33454881387` = FAILURE. Sin mutation owner CYCLE154.
- #93: OPEN/stale @ `b2c4eb441...`, base `134a293...`; sin mutation owner; refresh solo si 1.7 lo mantiene IN_ALPHA.

## CAMINO CRÍTICO RECALCULADO DESDE CERO

1. `F2/12.1 exact runtime/deployment-source close review post-#98`.
2. `Issue #97 pre-Beta startup/reveal Web+Desktop`.
3. `F0/0.9 / #89 P1 refresh + exact-green + integration` bajo owner futuro explícito.
4. `productive recent-reauth seam → F2/15.1 durable Trash`.
5. `F2/13.2 safe write-surface resolution`.
6. `F1/1.7 → 1.8` con facts frescos.
7. `#93 / F4 25.1` solo si 1.7 lo mantiene `IN_ALPHA`.
8. En paralelo: F0 1.2/2.2, production signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## TABLERO CYCLE154

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA `NIGHT-AAA-150` | F2/12.1 post-#98 exact runtime/deployment-source close review, strictly READ-ONLY | NONE |
| BBB `NIGHT-BBB-149` | minimum productive same-provider recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97 | F3/18.2 READ-ONLY applicability inventory only during genuine external wait after clean candidate |
| WOZ `NIGHT-WOZ-153` | exclusive Issue #97 startup/reveal Web+Desktop implementation/integration; conditional expected-head merge candidate #97 only | #89 strictly READ-ONLY refresh-readiness only while #97 genuinely waits external CI/review/build |

**Única integration mutation autorizada CYCLE154: WOZ153 / candidate de Issue #97, solo con exact scope + applicable CI SUCCESS + no required review blocker + race-free expected-head. #89/#93 no tienen mutation/merge authorization.**

## FALLBACKS

### BBB149 — F3/18.2 READ-ONLY

- Scope: inventario de reconciliation/provider scenarios existentes únicamente mientras PRIMARY espera externamente.
- Evidence: refs exactas + unresolved 3DS/rejection/late-payment/renewal/cancel/plan-change/refund/webhook/reconciliation + clasificación `SOFTWARE_PROVEN / UNVERIFIED_EXTERNAL / NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`.
- STOP: provider/payment mutation, new PR, gate promotion, overlap, o PRIMARY deja de esperar.

### WOZ153 — #89 READ-ONLY

- Scope: exact base/head/failed F0 gate/divergence/duplicate-check/refresh-readiness únicamente durante genuine external wait de #97.
- Evidence: live integration SHA; #89 start/end head; run `33454881387`; changed-file/divergence/duplicate classification `REUSE_REFRESHABLE / SUPERSEDED / SCOPE_CHANGED`.
- STOP: any mutation/rerun/review/merge/new PR/gate promotion/head movement/dependency overlap, o #97 deja de esperar.

## PROGRESO F0–F4

- **F0:** #89 P1 abierto/no merge-eligible; 1.2/2.2 + external release tails abiertos.
- **F1:** D6–D10.1 PASS; D10.2 `ALPHA CANDIDATE NOT READY`; 1.7 espera 12.1/#97/#89/recent-reauth facts.
- **F2:** #98 integrado; 12.1 exact runtime-source proof abierto; #97 active; 13.2 blocked; 15.1 detrás de recent-reauth.
- **F3:** provider/payment, legal implementation y runtime160/capacity abiertos/external o pendientes de explicit alpha applicability.
- **F4:** #93 stale/no owner; 25.1 global open; #97 requiere Desktop+Web validation; production signing/notarization/hardware/tester execution externos.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC

- Asignaciones escritas directamente: AAA150, BBB149, WOZ153.
- Plan Maestro, F0–F4 y `Equipo multi-IA - Roles y coordinación.md` sincronizados a CYCLE154.
- `Registro de avances.md` fue leído completo. No se reescribió whole-file para evitar una sustitución destructiva del ledger histórico; el nuevo merge #98 queda canónicamente registrado en Plan Maestro/F2/JOBS/Issue #41.
- `Plan Maestro 2208 copy DONT TOUCH .md` untouched.
- JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Procesar AAA150/BBB149/WOZ153.
2. Si AAA150 liga literalmente production evidence a immutable deployment identity y cubre checklist, revisar cierre F2/12.1.
3. Si WOZ153 cierra #97 con Web+Desktop evidence, reasignar owner de #89 como siguiente P1 técnico.
4. Continuar recent-reauth → F2/15.1; después 13.2 cuando shared surfaces queden libres.
5. Reemitir F1/1.7 cuando facts sean suficientemente frescos.

```text
CYCLE_ID: NIGHT-JOBS-154
INTEGRATION_HEAD_AT_CLOSE: c4e203cf5e44cf93c0c017c0120f097473fe91b2
PR98: MERGED / REQUIRED_CI_SUCCESS
AAA_NEW: NIGHT-AAA-150
BBB_NEW: NIGHT-BBB-149
WOZ_NEW: NIGHT-WOZ-153
ISSUE97: OPEN / ACTIVE_OWNER_WOZ153 / MUST_BE_ADDRESSED_BEFORE_BETA1
PR89_F0_AUDIT: 33454881387 FAILURE / NO_MUTATION_OWNER
F2_12.1: NOT_PASS / RUNTIME_SOURCE_BINDING_OPEN
F2_13.2: BLOCKED_WRITE_SURFACE / UNASSIGNED
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 154 termina aquí.
