# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 044`.

## META

Terminar F0–F4 o reducirlos al mínimo factual de blockers externos. Prioridad: F0–F4 → sencillez → limpieza. Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head obligatorios.

## BASELINE VIVO

- `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- Último merge material verificado: PR #68 → `a9d35a3d...`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/revisados: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo y comentarios actuales; GitHub vivo. GitHub/runtime prevaleció.

Hechos verificados:
1. Integration sigue exactamente `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; no hubo merge posterior a #68.
2. AAA039 sí dejó handoff nuevo `5470062487`. SAME #74 está OPEN/Ready/mergeable @ `14dfba52775f40f1956e3d1dcb343b07b147ba0c`, base exacta `a9d35a3d...`.
3. JOBS resolvió su WAITING_CI: D6 `33324138675` SUCCESS, D7 `33324138676` SUCCESS y Required CI `33324138689` SUCCESS sobre ese exact head. No merge observado.
4. BBB038 sí dejó handoff nuevo `5470100644`. SAME #72 promovió únicamente `windows/review` a `AUTOMATED_PASS`; nuevo head vivo `56dc4adf206cc53f5260c71952f84ae67d994279`, base exacta `a9d35a3d...`.
5. En #72, Windows Review `33324512156` SUCCESS, Windows Import `33324512159` SUCCESS y Required CI `33324512153` SUCCESS; pero F4 Functional Matrix `33324512174` terminó FAILURE. El único job es `matrix-contract` y el paso fallido literal es `Validate dependency-safe matrix contract`. No merge y no integración del row.
6. WOZ042 no dejó resultado. PR #75 sigue OPEN/Ready/mergeable @ `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`, base `a9d35a3d...`, sin commit nuevo ni CI nuevo atribuible a 042. Para impedir ejecución tardía, 042 queda superseded y el mismo corrective mínimo se reemite como 043.
7. #73 sigue holding exact-head green / merge-flow blocked; no se recrea.
8. F0/F1 no recibieron evidencia externa nueva; F2 mantiene runtime/#69/#70 blockers.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-039
`PENDING / WAITING_CI -> PASS_RESOLVED_BY_JOBS_RECHECK`.
- Candidate #74 exact-head green.
- No integración aún.
- Nuevo `NIGHT-AAA-040` emitido para race-check + integración exacta únicamente.

### BBB / NIGHT-BBB-038
`PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- Promotion ocurrió en SAME #72 y dedicated Review sigue verde.
- F4 Matrix está rojo en dependency-safe matrix contract.
- Nuevo `NIGHT-BBB-039` emitido attribution-first; no se presume bug de producto ni se revierte/promueve nada sin causa literal.

### WOZ / NIGHT-WOZ-042
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- #75 head/base sin cambio; no evidencia de ejecución.
- Nuevo `NIGHT-WOZ-043` reemite el mismo pin-only corrective bajo ID vigente único.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 #74 / product-auth prerequisite:** candidate exact-head green; integrar. Después #71 requiere nueva asignación para revalidación literal Windows Auth.
2. **F4 #72 / windows-review:** dedicated journey y Required CI verdes, pero matrix-contract rojo; atribuir/corregir y revalidar antes de integración.
3. **F3 #75 / 20.1:** pin-only corrective pendiente; fresh exact-head CI y merge si disponible.
4. **F3 #73 / 18.2:** software slice listo, bloqueado por merge execution layer; no duplicar.
5. **F2 #69 / 13.1:** Save All product wiring + refresh, holding hasta liberar owner.
6. **F2 / 12.1:** real-browser cold/warm bloqueado por runtime ejecutable.
7. **F2 #70:** safe-write + stale baseline frozen.
8. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 039 WAITING_CI → exact-head PASS | `NIGHT-AAA-040`: SAME #74 race-check + integración solo si evidencia sigue válida | `NONE` |
| BBB | 038 WAITING_CI → F4 Matrix FAILURE | `NIGHT-BBB-039`: SAME #72 attribution/corrective + fresh gates | `NONE` |
| WOZ | 042 sin resultado/head change | `NIGHT-WOZ-043`: SAME #75 immutable-action pin corrective + fresh CI | `NONE` |

No overlap material: AAA #74 product runtime/auth prerequisite; BBB #72 Review/matrix; WOZ #75 observability workflow. #71/#73/#69/#70 quedan holding.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-040
PRIMARY: SAME #74; consumir D6/D7/Required CI exact-head SUCCESS; race-check integration y merge únicamente si base/head siguen compatibles. Si baseline movió, refresh + fresh applicable CI antes de integrar. No tocar #71.  
CI-FALLBACK: `NONE`.  
STOP: fresh red, merge-flow unavailable, baseline race que requiera broad conflict work, cambio semántico o necesidad de tocar #71.

### BBB — NIGHT-BBB-039
PRIMARY: SAME #72; atribuir literalmente `Validate dependency-safe matrix contract`; correctivo mínimo solo si es inconsistencia acotada de matrix/workflow/test dentro de #72. Luego fresh Windows Review + F4 Matrix + D6 + D7 + Required CI; merge solo si todo verde/race-clean. No auth/#71/#74.  
CI-FALLBACK: `NONE`.  
STOP: product finding, unrelated row/gate change, auth overlap, baseline race amplio, non-attributable red o merge-flow unavailable.

### WOZ — NIGHT-WOZ-043
PRIMARY: SAME #75; reemplazar únicamente `actions/checkout@v4` y `actions/setup-node@v4` por pins canónicos inmutables; fresh Required CI + F3 20.1; race-check/merge solo si todo verde y flow disponible. No tocar #73.  
CI-FALLBACK: `NONE`.  
STOP: non-pinning failure, semantic scope drift, provider/RO expansion, baseline race amplio, merge-flow unavailable o necesidad de tocar #73.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: product wiring + refresh; holding/stale.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F3/18.2 #73: exact-head green pero merge-flow unavailable; provider/business tails abiertos.
9. F3/20.1 #75: pin corrective aún no ejecutado; product wiring/backend/external observability tails abiertos.
10. F4/windows-auth: #74 exact-head green pero no integrado; #71 espera merge + nueva assignment.
11. F4/windows-review: #72 dedicated green pero matrix-contract rojo.
12. F4/25.1: otras rows NOT_COVERED/PENDING_EXTERNAL.
13. F4/25.2 + D22/D23 external signing/notarization.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69/#70 holding/frozen.
- **F3:** 17.1/17.2/18.1 integrated; 18.2 #73 green but merge-flow blocked; 20.1 #75 candidate exists, pin corrective pendiente.
- **F4:** windows/import integrated; windows/auth #74 green pending merge; windows/review #72 dedicated green but matrix-contract red; 25.1/25.2 open.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 044

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-040`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-039`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-043`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 044.

F0/F1/F2 y Registro de avances fueron leídos completos; no se cambian sus checkboxes ni Registro porque no hubo merge estable nuevo ni PASS integrado que lo amerite. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar AAA040/BBB039/WOZ043 una sola vez.
3. Si AAA040 integra #74 y mueve baseline, #72/#75 deberán refresh/revalidar antes de cualquier merge posterior.
4. #71 solo vuelve a un owner mediante nueva asignación JOBS después de #74 realmente integrado.
5. #73 queda intacto hasta disponer de merge flow capaz.
6. No hopping automático a #69/#70.
7. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-044
INTEGRATION_HEAD_OBSERVED: a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA_RESULT_PROCESSED: NIGHT-AAA-039 WAITING_CI -> PASS / #74 not merged
BBB_RESULT_PROCESSED: NIGHT-BBB-038 WAITING_CI -> F4 Matrix FAILURE
WOZ_RESULT_PROCESSED: NIGHT-WOZ-042 NO_RESULT -> SUPERSEDED
AAA_NEW: NIGHT-AAA-040
BBB_NEW: NIGHT-BBB-039
WOZ_NEW: NIGHT-WOZ-043
CI_FALLBACKS: NONE/NONE/NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 044 completado.
