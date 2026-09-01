# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 140`.

## BASELINE VIVO / RACE-CHECK FINAL

- `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`; PR #96 es el último merge material verificable.
- Issue #41 completo reconciliado; no matching final para `NIGHT-AAA-135`, `NIGHT-BBB-134` o `NIGHT-WOZ-138` → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #96: CLOSED/MERGED el `2026-09-01T17:51:40Z`; base `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`, exact final head `6247173ead703f831801fa103ca465fea04e5793`, merge `aa4450956579de381e82acf06c660b658c703cd1`; Required CI exact-head SUCCESS. Esto sustituye el estado viejo WAITING_CI.
- F2/12.1 sigue `NOT_PASS`: no existe todavía evidencia verificada de public runtime exacto descendiente de `aa445095...`.
- #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`; stale. F0/0.9 run `33454881387` = known `completed/failure`; current head no es merge-eligible.
- #93 sigue OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...`; stale y mutation-unassigned.
- Release = `NO-GO`; F5 = CLOSED.

## CAMINO CRÍTICO RECALCULADO

1. F2/12.1: software corrective lineage ya integrada hasta #96; falta exact public runtime proof post-`aa445095...`.
2. F0/0.9: #89 P1, base stale + gate rojo; diagnosis/refresh/exact-head green.
3. D8 recent-reauth seam → F2/15.1 Trash durable.
4. F2/13.2 durable Review: `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
5. F1/1.7→1.8: reemitir clasificación factual después de incorporar resultados frescos de 12.1/#89/recent-reauth.
6. F4/25.1/#93 solo si 1.7 lo mantiene en alpha.
7. Tails externos: F0 1.2/2.2, signing/notarization, provider/payment, legal, runtime160, testers/hardware.

## TABLERO CYCLE140

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA `NIGHT-AAA-136` | F2/12.1 public runtime proof/evidence inventory READ-ONLY post-#96; exact deployment vs older evidence vs UNVERIFIED | NONE |
| BBB `NIGHT-BBB-135` | minimum productive D8 recent-reauth seam; no Trash; candidate only; NO MERGE | NONE |
| WOZ `NIGHT-WOZ-139` | REUSE #89; diagnose current failure, bounded refresh/revalidate on `aa445095...`; expected-head merge #89 only if exact/green/race-free | READ-ONLY #93 stale-evidence inventory únicamente mientras #89 espera CI externo después de clean refresh |

**Única integration mutation autorizada CYCLE140: WOZ139 / PR #89, y solo con refreshed exact base/head + applicable CI SUCCESS + race-free expected-head. #93 no tiene autorización de merge.**

## CI-FALLBACK WOZ139

Scope: inspeccionar #93 base/head/changed-files/existing exact-head checks/divergence vs live y clasificar `REUSE_REFRESHABLE / STALE_INVALIDATED / NO_LONGER_APPLICABLE`.  
Evidence: exact start/end head, live base, existing check conclusions, divergence/material-conflict notes, packaged-current-baseline/runtime `UNVERIFIED`.  
STOP: cualquier mutation/rerun/review/merge/new PR/gate promotion/owner overlap/head movement; volver inmediatamente a #89 cuando PRIMARY deje de esperar.

## PROGRESO F0–F4

- F0: #89 P1 activo; 1.2/2.2 + external release tails abiertos.
- F1: D6–D10.1 PASS; D10.2 NOT_READY; 1.7 se reemitirá tras resultados CYCLE140 para evitar clasificar facts ya superados.
- F2: #92/#94/#95/#96 integrados; 12.1 runtime OPEN; 13.2 blocked; 15.1 detrás de BBB135.
- F3: provider/payment, legal implementation y runtime160/capacity siguen abiertos/external o sujetos a clasificación alpha.
- F4: #93 stale; 25.1 global abierto; production signing/notarization/hardware externos.
- F5: CLOSED / NO ABRIR.

## PLAN SYNC

Plan Maestro, F2, coordinación y NOCHE AAA/BBB/WOZ/JOBS sincronizados a CYCLE140. Registro de avances debe registrar el merge material #96; F0/F1/F3/F4 conservan gates previos y su baseline textual puede quedar detrás hasta el siguiente sync si no se actualiza en esta misma transacción; GitHub live prevalece. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

```text
CYCLE_ID: NIGHT-JOBS-140
INTEGRATION_HEAD_FINAL: aa4450956579de381e82acf06c660b658c703cd1
AAA_NEW: NIGHT-AAA-136
BBB_NEW: NIGHT-BBB-135
WOZ_NEW: NIGHT-WOZ-139
PR96: MERGED / HEAD 6247173ead703f831801fa103ca465fea04e5793 / MERGE aa4450956579de381e82acf06c660b658c703cd1 / REQUIRED_CI SUCCESS
PR89_F0_AUDIT: 33454881387 FAILURE
F2_12.1: NOT_PASS / PUBLIC_RUNTIME_OPEN
F2_13.2: BLOCKED_WRITE_SURFACE / UNASSIGNED
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 140 termina tras handoff Issue #41 y readback.
