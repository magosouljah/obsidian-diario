# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 115`.

## BASELINE VIVO

- Preflight GitHub: `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.
- Último merge material: PR #91 → `134a293...`.
- PR #93: OPEN/Ready/mergeable @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`, 3 harness/evidence files only.
- Exact-head CI #93: Windows Auth `33468863393` SUCCESS; D6 `33468863373` SUCCESS; D7 `33468863387` SUCCESS; Desktop Portability `33468863399` SUCCESS; Windows Import `33468863402` SUCCESS; F0 secret scan `33468863418` SUCCESS; Upgrade staging skipped/non-applicable.
- PR #92: OPEN/Ready/mergeable; exact base `134a293...`; live head moved to `bb67f61135f5767b5d7a8220265ff82317020949` since prior plan snapshot. Exact-head Web Production Build `33473295674`, D6 `33473295651`, D7 `33473295616`, Desktop Portability `33473295652`, Temp Auth Compile `33473295563`, secret scan `33473295638` = SUCCESS; staging skipped. PARKED CYCLE115.
- PR #89: OPEN/Ready/mergeable @ `daf87da6...`, stale base `816f946c...`; PARKED CYCLE115.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos/reconciliados completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo disponible en connector y GitHub vivo. GitHub/runtime real prevalece.

- `NIGHT-AAA-110`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-109`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-113`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio factual nuevo: #92 head anterior `9947380...` quedó stale; live head `bb67f611...` con applicable exact-head CI verde. No se promovió PASS ni merge por esto.
- Duplicate-check: no nuevo PR durable Review ni Trash/recent-reauth; #53 solo aporta la seam D8 reutilizable de recent reauth y no duplica 15.1.
- JOBS no modificó código BeatGaler ni infraestructura.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 115

1. **F4/25.1 / #93:** exact-green Windows Auth evidence candidate ya existe; el costo marginal mínimo es exact semantic/CI/race review + integración bounded. Global 25.1 queda abierto.
2. **F2/13.2:** durable Review completion/no-silent-loss o exclusión RO explícita.
3. **F2/15.1:** recent-reauth + strong confirmation + durable purge/no-false-success o exclusión RO explícita.
4. **F0/0.9 / #89:** refresh/revalidate DNS-rebinding/SSRF P1 después de liberar current integration lane.
5. **F2/12.1 / #92:** live candidate ya exact-green sobre baseline actual, pero parked; si #93 mueve baseline, refresh/revalidate antes de integrar. Luego deploy/runtime/cold-warm proof.
6. **F1/1.7 → 1.8 → 1.9:** clasificación blockers, decisión RO alpha y solo después ejecución.
7. **Release tails paralelos:** signing/notarization, F0 1.2/2.2, provider/legal/capacity/tester/hardware.

## TABLERO / ASIGNACIONES EMITIDAS — CYCLE 115

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | `NIGHT-AAA-110 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-AAA-111` — F2/13.2 durable Review Save/Save All completion/no-silent-loss corrective; candidate only; **NO MERGE** | `NONE` |
| BBB | `NIGHT-BBB-109 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-BBB-110` — F2/15.1 Empty Trash recent-reauth + strong confirmation + durable purge; candidate only; **NO MERGE** | only during genuine WAITING_CI: F1/1.7 blocker classification READ-ONLY |
| WOZ | `NIGHT-WOZ-113 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-WOZ-114` — REUSE #93; final exact semantic/CI/race recheck; expected-head merge #93 only if exact/green/race-free | `NONE` |

**INTEGRATION_MUTATION CYCLE 115: WOZ114 / PR #93 ONLY.**

## CI-FALLBACK CONTRACTS

- AAA111: `CI-FALLBACK: NONE`.
- BBB110: solo si PRIMARY está genuinamente `WAITING_CI`: F1/1.7 READ-ONLY blocker matrix. Evidence requerida: cada clasificación ligada a evidence existente. STOP ante implementación, plan mutation, provider call, decisión RO o fin de WAITING_CI; después recheck PRIMARY.
- WOZ114: `CI-FALLBACK: NONE`; #93 CI ya está completado al assignment preflight.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** 0.20 cerrado; #89 P1 software sigue pendiente refresh/revalidation; 1.2/2.2 + release/admin/signing tails mantienen fase global abierta.
- **F1:** D6–D10.1 PASS; D10.2 map complete/NOT_READY. #93 pending canonical evidence integration; durable Review, Trash, #89 y Web runtime bloquean 1.8.
- **F2:** #91 integrado; #92 live head `bb67f611...` exact-base/exact-green pero parked. 12.1 NOT_PASS hasta canonical integration + deploy/runtime/cold-warm proof. 13.2=AAA111. 15.1=BBB110.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o RO-applicability.
- **F4:** Windows packaged Auth literal exact-head SUCCESS demostrado en #93; evidence candidate aún no integrado. 25.1 global continúa abierto por journeys restantes. Production signing/notarization/hardware externos.
- **F5:** CLOSED / NO ABRIR.

## NEXT

AAA111 trabaja F2/13.2; BBB110 trabaja F2/15.1; WOZ114 consume #93 y es el único que puede mutar integración, exclusivamente bajo exact-head/green/race-free. #92 y #89 quedan parked/unassigned hasta el próximo recálculo. Release continúa NO-GO y F5 cerrado.

```text
CYCLE_ID: NIGHT-JOBS-115
INTEGRATION_HEAD_PREFLIGHT: 134a293985c314eb09c238115e3bcb71e79f1810
AAA_RESULT_PROCESSED: NIGHT-AAA-110 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-109 NO_RESULT / SUPERSEDED / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-113 NO_RESULT / SUPERSEDED / NOT_PASS
AAA_NEW: NIGHT-AAA-111 F2_13.2
BBB_NEW: NIGHT-BBB-110 F2_15.1
WOZ_NEW: NIGHT-WOZ-114 F4_25.1_PR93
PR93: OPEN READY exact base 134a293 / head b2c4eb4 / exact-head applicable workflows SUCCESS / conditional integration lane
PR92: OPEN READY exact base 134a293 / head bb67f611 / exact-head applicable workflows SUCCESS / PARKED CYCLE115
PR89: OPEN READY STALE / PARKED CYCLE115
INTEGRATION_MUTATION_AUTHORIZED: WOZ114 PR93 ONLY IF EXACT_GREEN_RACE_FREE
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 115 terminado.
