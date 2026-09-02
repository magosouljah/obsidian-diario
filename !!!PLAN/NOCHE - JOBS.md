# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 155`.

## BASELINE VIVO / PREFLIGHT

- Lectura completa realizada: Plan Maestro; Fases 0–4; coordinación; protocolo; NOCHE JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo; GitHub vivo.
- Baseline vivo cambió materialmente después de CYCLE154: `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.
- PR #99 `bind Web runtime to exact source SHA` está MERGED. Exact candidate head `6e253c815515624dcfc70cb5d447befa38f19566`; merge/current integration `c2766fb...`; exact-head Required CI `33578074388` = SUCCESS.
- #99 integra fail-closed Web deployment provenance: exact source SHA, dirty-tree rejection, `.well-known/source-sha.txt`, expected-SHA activation/readback y `WEB_RUNTIME_SOURCE_PROOF_OK`.
- Release = `NO-GO`; F5 = CLOSED.

## RESULTADOS PROCESADOS — CYCLE155

- `NIGHT-AAA-150` → sin RESULTADO DEL TURNO/handoff worker posterior a CYCLE154 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-149` → sin RESULTADO DEL TURNO/handoff worker posterior a CYCLE154 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-153` → sin RESULTADO DEL TURNO/handoff worker posterior a CYCLE154 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- GitHub independientemente prueba un outcome nuevo no atribuible a esos handoffs: **PR #99 MERGED + exact-head Required CI SUCCESS + integration advanced to `c2766fb...`**. Se procesa solo como `PR99_WEB_RUNTIME_SOURCE_BINDING_MECHANISM_INTEGRATED`; no como F2/12.1 PASS ni como worker DONE.

## DELTA MATERIAL / GATES

### F2/12.1

#99 cierra la carencia de mecanismo para probar identidad inmutable del Web runtime, pero su propia exit condition exige una **clean production deployment desde canonical integration HEAD** y readback público donde el marker sea exactamente ese SHA. JOBS no observó evidencia literal de esa ejecución para `c2766fb...`; la consulta pública no produjo una prueba verificable durante este run. Por evidence-before-claim, 12.1 queda `NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN`.

### Issue #97

Sigue OPEN, cero comments, y el body dice `Must be addressed before Beta 1`. #99 no es una corrección de startup/reveal; WOZ154 conserva el lane de implementación/integración.

### #89

PR #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, stale versus live. Run F0/0.9 `33454881387` sigue FAILURE. Diagnóstico ya verificable en Issue #41: dependency/DNS/security/TS/cloud checks pasaron; Rust unit contracts falló porque Tauri `frontendDist ../dist` no existía. Sus seis archivos son security workflow/server/DNS-pinning/docs, materialmente separados del startup/App slice de #97. AAA151 recibe ownership exclusivo.

### #93

Sigue OPEN/stale @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base histórica `134a293...`; old-base Windows Auth evidence no es canonical exact-head. Sin mutation owner CYCLE155.

## CAMINO CRÍTICO RECALCULADO DESDE CERO

1. `F2/12.1 clean canonical production deployment/source proof post-#99`.
2. `Issue #97 pre-Beta startup/reveal Web+Desktop`.
3. `F0/0.9 / #89 P1 refresh + exact-green + integration`.
4. `productive recent-reauth seam → F2/15.1 durable Trash`.
5. `F2/13.2 safe write-surface resolution` cuando #97 libere shared surfaces.
6. `F1/1.7 → 1.8` con facts frescos.
7. `#93 / F4 25.1` solo si 1.7 lo mantiene `IN_ALPHA`.
8. En paralelo: F0 1.2/2.2, production signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## TABLERO CYCLE155

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA `NIGHT-AAA-151` | F0/0.9 REUSE #89; history-preserving refresh, mínimo gate-precondition correction, exact-head revalidation y conditional expected-head merge #89 only | NONE |
| BBB `NIGHT-BBB-150` | minimum productive same-provider recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97/#89 | F3/18.2 READ-ONLY applicability inventory only during genuine external wait after clean candidate |
| WOZ `NIGHT-WOZ-154` | exclusive Issue #97 startup/reveal Web+Desktop implementation/integration; conditional expected-head merge candidate #97 only | NONE |

**Integration mutations autorizadas CYCLE155: AAA151 / #89 y WOZ154 / candidate de Issue #97, únicamente dentro de scopes disjuntos y con exact applicable CI SUCCESS + no required review blocker + race-free expected-head. BBB150 NO MERGE. #93 no tiene mutation/merge authorization.**

## FALLBACKS

### AAA151

`CI-FALLBACK: NONE`. F2/12.1 es SHA-dependent y un merge #89 invalidaría cualquier marker del baseline anterior; #93/#97 tienen ownership/dependency risk.

### BBB150 — F3/18.2 READ-ONLY

- Scope: inventario de reconciliation/provider scenarios existentes únicamente mientras PRIMARY espera externamente después de candidate limpio.
- Evidence: refs exactas + unresolved 3DS/rejection/late-payment/renewal/cancel/plan-change/refund/webhook/reconciliation + clasificación `SOFTWARE_PROVEN / UNVERIFIED_EXTERNAL / NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`.
- STOP: provider/payment mutation, new PR, gate promotion, overlap, o PRIMARY deja de esperar.

### WOZ154

`CI-FALLBACK: NONE`. #93 puede solapar Desktop harness/auth y F2/12.1 source proof depende del canonical SHA que #97 podría mover.

## PROGRESO F0–F4

- **F0:** #89 P1 abierto/red pero ahora con owner ejecutable AAA151; 1.2/2.2 + external release tails abiertos.
- **F1:** D6–D10.1 PASS; D10.2 `ALPHA CANDIDATE NOT READY`; 1.7 espera 12.1/#97/#89/recent-reauth facts.
- **F2:** #98/#99 integrados; 12.1 mecanismo de source binding integrado pero clean canonical production proof abierto; #97 active; 13.2 blocked; 15.1 detrás de recent-reauth.
- **F3:** provider/payment, legal implementation y runtime160/capacity abiertos/external o pendientes de explicit alpha applicability.
- **F4:** #93 stale/no owner; 25.1 global open; #97 requiere Desktop+Web validation; production signing/notarization/hardware/tester execution externos.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC

- Asignaciones escritas directamente: AAA151, BBB150, WOZ154.
- Plan Maestro, F0–F4 y `Equipo multi-IA - Roles y coordinación.md` sincronizados a CYCLE155.
- `Registro de avances.md` fue leído completo. No se reescribió whole-file para evitar una sustitución destructiva del ledger histórico; #99 queda registrado canónicamente en Plan/F1/F2/F3/JOBS/Issue #41.
- `Plan Maestro 2208 copy DONT TOUCH .md` untouched.
- JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Procesar AAA151/BBB150/WOZ154.
2. Si aparece clean canonical production deployment proof post-#99, hacer close review literal de F2/12.1 sin inferencias.
3. Si AAA151 deja #89 refreshed exact-green, integrar solo bajo expected-head/race-free authority y procesar merge factual.
4. Si WOZ154 cierra #97 con Web+Desktop evidence, liberar shared App/startup surfaces para F2/13.2.
5. Continuar recent-reauth → F2/15.1 y luego reemitir F1/1.7 cuando facts sean suficientemente frescos.

```text
CYCLE_ID: NIGHT-JOBS-155
INTEGRATION_HEAD_AT_CLOSE_EXPECTED: c2766fb23de5bb837a7fef4080a6aa7a6716f15e
PR99: MERGED / REQUIRED_CI_SUCCESS / PROVENANCE_MECHANISM_ONLY
AAA_NEW: NIGHT-AAA-151
BBB_NEW: NIGHT-BBB-150
WOZ_NEW: NIGHT-WOZ-154
ISSUE97: OPEN / ACTIVE_OWNER_WOZ154 / MUST_BE_ADDRESSED_BEFORE_BETA1
PR89_F0_AUDIT: 33454881387 FAILURE / ACTIVE_OWNER_AAA151
PR93: OPEN_STALE / NO_MUTATION_OWNER
F2_12.1: NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN
F2_13.2: BLOCKED_WRITE_SURFACE / UNASSIGNED
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 155 termina aquí.
