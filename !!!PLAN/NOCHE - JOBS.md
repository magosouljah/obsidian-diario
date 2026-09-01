# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 114`.

## BASELINE VIVO

- Preflight GitHub: `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.
- Final race-check: sigue `134a293985c314eb09c238115e3bcb71e79f1810`; no merge nuevo durante JOBS114.
- Último merge material: PR #91 → `134a293...`.
- PR #93: OPEN/Ready/mergeable @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`, three harness/evidence files only.
- Exact-head CI #93: Windows Auth `33468863393` SUCCESS; D6 `33468863373` SUCCESS; D7 `33468863387` SUCCESS; Desktop Portability `33468863399` SUCCESS; Windows Import `33468863402` SUCCESS; F0 secret scan `33468863418` SUCCESS; Upgrade staging skipped/non-applicable.
- PR #92: OPEN/Ready/mergeable @ `9947380ce8095b718a400d1e7781d21e67b29be9`, exact base `134a293...`; parked CYCLE114.
- #89: OPEN/Ready @ `daf87da6...`, stale base histórica; parked/unassigned CYCLE114.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos/reconciliados completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo disponible en connector y GitHub vivo. GitHub/runtime real prevalece.

- `NIGHT-AAA-109`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-108`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-112`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Recalculo desde cero mantiene #93 primero porque ya es exact-green y solo falta integration/evidence promotion; no se conserva por inercia de assignment.
- Duplicate-check final: AAA110=F2/13.2; BBB109=F2/15.1; WOZ113=#93. No overlap material.
- JOBS no modificó código BeatGaler ni infraestructura.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 114

1. **F4/25.1 / #93:** exact-green Windows Auth candidate ya existe; WOZ debe hacer exact semantic/CI/race review y merge condicional. Global 25.1 queda abierto para journeys restantes.
2. **F2/13.2:** durable Review completion/no-silent-loss o exclusión RO explícita.
3. **F2/15.1:** recent-reauth + strong confirmation + durable purge/no-false-success o exclusión RO explícita.
4. **F0/0.9 / #89:** refresh/revalidate DNS-rebinding/SSRF P1 después de liberar la current integration lane.
5. **F2/12.1 / #92:** refresh/revalidate si baseline cambia, integrar candidate y luego deployment/runtime/cold-warm proof.
6. **F1/1.7 → 1.8 → 1.9:** clasificación blockers, decisión RO alpha y solo después ejecución.
7. **Release tails paralelos:** signing/notarization, F0 1.2/2.2, provider/legal/capacity/tester/hardware.

## TABLERO / ASIGNACIONES EMITIDAS — CYCLE 114

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | `NIGHT-AAA-109 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-AAA-110` — F2/13.2 durable Review Save/Save All completion/no-silent-loss corrective; candidate only; **NO MERGE** | `NONE` |
| BBB | `NIGHT-BBB-108 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-BBB-109` — F2/15.1 Empty Trash recent-reauth + strong confirmation + durable purge; candidate only; **NO MERGE** | only during genuine WAITING_CI: F1/1.7 blocker classification READ-ONLY |
| WOZ | `NIGHT-WOZ-112 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-WOZ-113` — REUSE #93; final exact semantic/CI/race recheck; expected-head merge #93 only if exact/green/race-free | `NONE` |

**INTEGRATION_MUTATION CYCLE 114: WOZ113 / PR #93 ONLY.**

## CI-FALLBACK CONTRACTS

- AAA110: `CI-FALLBACK: NONE`.
- BBB109: solo si PRIMARY está genuinamente `WAITING_CI`: F1/1.7 READ-ONLY blocker matrix. Evidence requerida: cada clasificación ligada a evidence existente. STOP inmediato ante implementación, plan mutation, provider call, decisión RO o fin de WAITING_CI; después recheck PRIMARY.
- WOZ113: `CI-FALLBACK: NONE`; #93 CI ya está completado al assignment preflight.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** 0.20 cerrado; #89 P1 software sigue pendiente refresh/revalidation; 1.2/2.2 + release/admin/signing tails mantienen fase global abierta.
- **F1:** D6–D10.1 PASS; D10.2 map complete/NOT_READY. #93 pending canonical evidence integration; durable Review, Trash, #89 y Web runtime aún bloquean 1.8.
- **F2:** #91 integrado; #92 exact-base candidate parked CYCLE114. 12.1 NOT_PASS hasta canonical candidate + deploy/runtime/cold-warm proof. 13.2=AAA110. 15.1=BBB109.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o RO-applicability.
- **F4:** Windows packaged Auth literal exact-head SUCCESS demostrado en #93; evidence candidate aún no integrado. 25.1 global continúa abierto por journeys restantes. Production signing/notarization/hardware externos.
- **F5:** CLOSED / NO ABRIR.

## NEXT

AAA110 trabaja F2/13.2; BBB109 trabaja F2/15.1; WOZ113 consume #93 y es el único que puede mutar integración, exclusivamente bajo exact-head/green/race-free. #92 y #89 quedan parked/unassigned hasta el próximo recálculo. Release continúa NO-GO y F5 cerrado.

```text
CYCLE_ID: NIGHT-JOBS-114
INTEGRATION_HEAD_PREFLIGHT: 134a293985c314eb09c238115e3bcb71e79f1810
INTEGRATION_HEAD_FINAL_RACECHECK: 134a293985c314eb09c238115e3bcb71e79f1810
AAA_RESULT_PROCESSED: NIGHT-AAA-109 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-108 NO_RESULT / SUPERSEDED / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-112 NO_RESULT / SUPERSEDED / NOT_PASS
AAA_NEW: NIGHT-AAA-110 F2_13.2
BBB_NEW: NIGHT-BBB-109 F2_15.1
WOZ_NEW: NIGHT-WOZ-113 F4_25.1_PR93
PR93: OPEN READY exact base 134a293 / head b2c4eb4 / exact-head applicable workflows SUCCESS / conditional integration lane
PR92: OPEN READY exact base 134a293 / PARKED CYCLE114
PR89: OPEN READY STALE / PARKED CYCLE114
INTEGRATION_MUTATION_AUTHORIZED: WOZ113 PR93 ONLY IF EXACT_GREEN_RACE_FREE
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 114 terminado.
