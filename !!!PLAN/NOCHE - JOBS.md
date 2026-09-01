# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 139`.

## BASELINE VIVO / RACE-CHECK FINAL

- `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`; #95 sigue último merge material verificable.
- Issue #41 completo reconciliado; no matching final para `NIGHT-AAA-134`, `NIGHT-BBB-133` o `NIGHT-WOZ-137` → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #96 apareció después de CYCLE138. Final del ciclo: OPEN/Ready, base `43fdf70e...`, head `7e7bd5449361b2031c29271e8875de7683ed5af4`. El head cambió durante el preflight y luego se estabilizó. Primera consulta: 0 checks; race-check final: 14 check-runs sobre ese exact head; `Test - Desktop Portability` run `33538653800` = `in_progress`. Estado: `WAITING_CI / ACTIVE_EXTERNAL_CANDIDATE / NOT_PASS / NO NIGHT MUTATION OWNER`.
- F2/12.1 sigue `NOT_PASS`; eventual integración de #96 no sustituye public runtime proof del deployment exacto resultante.
- #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`; stale. F0/0.9 run `33454881387` reconsultado = `completed/failure`; current head no es merge-eligible.
- #93 sigue OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...`; stale y mutation-unassigned.
- Release = `NO-GO`; F5 = CLOSED.

## CAMINO CRÍTICO RECALCULADO

1. F2/12.1: #96 exact-base está `WAITING_CI`; requiere conclusión exact-head + handoff/owner válido; después runtime público exacto.
2. F0/0.9: #89 P1, base stale + gate rojo; diagnosis/refresh/exact-head green.
3. F1/1.7: clasificación factual antes de 1.8, incluyendo #96 como candidate no PASS.
4. D8 recent-reauth seam → F2/15.1 Trash durable.
5. F2/13.2 durable Review: `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
6. F4/25.1/#93 solo si 1.7 lo mantiene en alpha.
7. Tails externos: F0 1.2/2.2, signing/notarization, provider/payment, legal, runtime160, testers/hardware.

## TABLERO CYCLE139

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA `NIGHT-AAA-135` | F1/1.7 blocker classification READ-ONLY; incluir #96/#89/#93 y F3 applicability; sin decisión RO | NONE |
| BBB `NIGHT-BBB-134` | minimum productive D8 recent-reauth seam; no Trash; candidate only; NO MERGE | NONE |
| WOZ `NIGHT-WOZ-138` | REUSE #89; diagnose current failure, bounded refresh/revalidate; expected-head merge #89 solo si exact/green/race-free | READ-ONLY #96 stability/evidence inventory únicamente mientras #89 espera CI externo después de clean refresh |

**Única integration mutation autorizada CYCLE139: WOZ138 / PR #89, y solo con refreshed exact base/head + applicable CI SUCCESS + race-free expected-head. #96 y #93 no tienen autorización de merge.**

## CI-FALLBACK WOZ138

Scope: inspeccionar #96 base/head/changed-files/actividad/checks y matching handoff; clasificar solo `HANDOFF_READY / CI_PENDING / ACTIVE_EXTERNAL / UNSTABLE_ACTIVE_EXTERNAL`.  
Evidence: exact start/end head, live base, checks ligados a ese head, public runtime `UNVERIFIED`.  
STOP: cualquier mutation/rerun/review/merge/new PR/gate promotion/owner overlap, o head movement; volver inmediatamente a #89 cuando PRIMARY deje de esperar.

## PROGRESO F0–F4

- F0: #89 P1 activo; 1.2/2.2 + external release tails abiertos.
- F1: D6–D10.1 PASS; D10.2 NOT_READY; AAA135→1.7; 1.8 posterior.
- F2: #92/#94/#95 integrados; #96 WAITING_CI; 12.1 NOT_PASS; 13.2 blocked; 15.1 detrás de BBB134.
- F3: provider/payment, legal implementation y runtime160/capacity siguen abiertos/external o sujetos a clasificación alpha.
- F4: #93 stale; 25.1 global abierto; production signing/notarization/hardware externos.
- F5: CLOSED / NO ABRIR.

## PLAN SYNC

Plan Maestro, F0–F4, coordinación y NOCHE AAA/BBB/WOZ/JOBS sincronizados a CYCLE139. `Registro de avances.md` leído y dejado sin promoción: no hubo merge/PASS/runtime nuevo. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

```text
CYCLE_ID: NIGHT-JOBS-139
INTEGRATION_HEAD_FINAL: 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3
AAA_NEW: NIGHT-AAA-135
BBB_NEW: NIGHT-BBB-134
WOZ_NEW: NIGHT-WOZ-138
PR96: WAITING_CI / 7e7bd5449361b2031c29271e8875de7683ed5af4 / RUN 33538653800 IN_PROGRESS
PR89_F0_AUDIT: 33454881387 FAILURE
F2_12.1: NOT_PASS
F2_13.2: BLOCKED_WRITE_SURFACE / UNASSIGNED
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 139 termina tras handoff Issue #41 y readback.
