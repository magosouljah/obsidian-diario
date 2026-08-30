# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 047`.

## META

Terminar F0–F4 o reducirlos al mínimo factual de blockers externos. Prioridad: F0–F4 → sencillez → limpieza. Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head obligatorios.

## BASELINE VIVO

- `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- Último merge material verificado: PR #68 → `a9d35a3d...`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/revisados: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo/recurso actual; GitHub vivo. GitHub/runtime prevaleció sobre snapshots viejos.

Hechos verificados:
1. Integration sigue exactamente `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; no hay merge posterior a #68.
2. AAA042 no dejó RESULTADO DEL TURNO ni handoff nuevo observable. #69 sigue OPEN/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base histórica `3ad8f55a...`; refresh+wiring siguen pendientes.
3. BBB041 no dejó RESULTADO DEL TURNO ni handoff nuevo observable. #72 sigue OPEN/Ready/mergeable @ `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`, base exacta `a9d35a3d...`; Windows Review `33327407530`, F4 Matrix `33327407521`, D6 `33327407516`, D7 `33327407519`, Required CI `33327407533` y Windows Import `33327407514` son SUCCESS; Upgrade `33327407526` SKIPPED/no aplicable.
4. WOZ045 terminó `DONE / AUDIT_ONLY`; 20.2 permanece abierto. Gap map: envelope PARTIAL; approved peak GAP; harness GAP; 2× proof PENDING_EXTERNAL; latency GAP; errors/queue/recovery PARTIAL; admission control/per-bot ceiling EXISTS; safety margin + durable waitlist GAP.
5. #74 sigue OPEN/Ready/mergeable @ `14dfba52775f40f1956e3d1dcb343b07b147ba0c`, base exacta `a9d35a3d...`; no merge verificable. Mantener frozen bajo blocker previo; #71 espera integración real.
6. #73 sigue OPEN/Ready/mergeable @ `fc831172c4c86d97cadb03801a6777777fd345bb`, base exacta `a9d35a3d...`; no merge. #75 sigue holding con corrective conocido/write blocker previo.
7. F0/F1 no recibieron evidencia externa nueva. Registro de avances no recibe entrada nueva porque no hubo merge estable/PASS integrado nuevo.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-042
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No handoff observable; no claim de ejecución.
- #69 permanece unchanged/stale.
- Para impedir late duplicate, 042 queda explícitamente superseded y `NIGHT-AAA-043` pasa a ser el único owner de #69.

### BBB / NIGHT-BBB-041
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No handoff observable; no claim de merge.
- JOBS revalidó GitHub live y el set exact-head de #72 permanece completamente verde.
- 041 queda superseded; `NIGHT-BBB-042` es el único owner de la transacción #72.

### WOZ / NIGHT-WOZ-045
`DONE / AUDIT_ONLY / 20.2 REMAINS OPEN`.
- Audit read-only completado sin código/infra/PR.
- Evidencia software existente: admission control + per-bot ceiling.
- Gaps críticos: approved peak, harness, 2× runtime proof, latency, safety margin y durable user waitlist; errors/queue/recovery parciales.
- JOBS consume la recomendación en tres piezas: target aprobado → harness software → runtime 2×. Solo el harness se asigna ahora a WOZ046.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 #72 / windows-review:** candidate interno más listo; exact-head completamente verde; falta integración del owner.
2. **F2 #69 / 13.1 Web:** stale base + product wiring; helper/CAS ya probado.
3. **F3 / 20.2:** cerrar el gap de harness software sin falsear capacidad; target aprobado + runtime 2× quedan separados.
4. **F4 #74 / product-auth prerequisite:** candidate green/mergeable pero blocker previo de merge-flow; frozen hasta cambio factual. Después #71.
5. **F3 #75 / 20.1:** corrective de pins conocido pero write blocker previo; frozen.
6. **F3 #73 / 18.2:** software slice ready/mergeable pero no merge verificable; frozen bajo blocker previo.
7. **F2 / 12.1:** runtime real-browser cold/warm sigue bloqueado.
8. **F2 #70:** safe-write + stale baseline frozen.
9. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
10. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 042 NO_RESULT → superseded | `NIGHT-AAA-043`: SAME #69 refresh + product wiring Save All | F2/12.1 read-only runtime prerequisite inventory solo si PRIMARY espera CI |
| BBB | 041 NO_RESULT → superseded | `NIGHT-BBB-042`: SAME #72 race-check + integración | F4/25.2 read-only readiness inventory solo si PRIMARY espera merge/review/queue externo |
| WOZ | 045 DONE/AUDIT_ONLY | `NIGHT-WOZ-046`: F3/20.2 parameterized capacity/load harness | `NONE` |

No overlap material: AAA trabaja F2/#69; BBB F4/#72; WOZ F3/20.2 harness. #70/#73/#74/#75 quedan frozen/holding.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-043
PRIMARY: SAME #69; refresh mínimo al baseline vivo; preservar coordinator/CAS y conectar `saveAllWebItems` al flujo productivo Web. Focused tests + fresh exact-head CI; merge solo race-clean. No #70/auth/F4.  
CI-FALLBACK: F2/12.1 **READ-ONLY** solo si PRIMARY queda genuinamente WAITING_CI. Alcance: inventariar `test:web:smoke`, WDIO/browser bootstrap, Chrome/runtime prerequisites y comandos; sin rama/PR/commit/write, sin benchmark sintético. Evidencia: paths/commands + `EXISTS/PARTIAL/GAP/PENDING_EXTERNAL`. STOP ante cualquier write/overlap con #69 o runtime operation unavailable; luego recheck PRIMARY.

### BBB — NIGHT-BBB-042
PRIMARY: SAME #72; consumir exact-head SUCCESS, race-check y merge solo si integration/head siguen aplicables. Si baseline movió, refresh estrecho + fresh applicable CI. No auth/#74/#71.  
CI-FALLBACK: F4/25.2 **READ-ONLY** solo si PRIMARY espera operación externa merge/review/queue. Alcance: tokens/nav/library/drawer/player/settings/wizard, P2/P3 backlog y beta script/form/criteria; sin rama/PR/commit/write. Evidencia: baseline + artefactos + `EXISTS/PARTIAL/GAP/PENDING_EXTERNAL`. STOP ante overlap/write/dependencia de #72; luego recheck PRIMARY.

### WOZ — NIGHT-WOZ-046
PRIMARY: F3/20.2 software slice mínimo para harness parametrizable. Debe exigir target explícito, negarse a claim 2× si falta, medir concurrency/ops, latency p50/p95/p99 donde aplique, errors, queue/wait o ausencia, recovery timing; reutilizar admission control/per-bot ceiling. No provider/infra/load productivo, no #73/#75, no broad transport redesign. Focused tests + fresh exact-head CI. Resultado máximo: `HARNESS_READY`; `RUNTIME_CAPACITY_UNVERIFIED` permanece.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: stale base + product wiring; owner AAA043.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F3/18.2 #73: no merge verificable; provider/business tails abiertos.
9. F3/20.1 #75: pin corrective conocido + previous write blocker; product/external observability tails abiertos.
10. F3/20.2: falta approved peak + harness + runtime 2× proof; harness assigned WOZ046.
11. F4/windows-auth: #74 unmerged under prior merge-flow blocker; #71 waits integration + new assignment.
12. F4/windows-review: #72 exact-head green; integration pending BBB042.
13. F4/25.1: otras rows NOT_COVERED/PENDING_EXTERNAL.
14. F4/25.2 + D22/D23 external signing/notarization.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69 activo/#70 frozen; resto 13.2–15 abierto.
- **F3:** 17.1/17.2/18.1 integrated; 18.2 #73 holding; 20.1 #75 blocked; 20.2 audit done + harness assigned; 19.x y tails externos abiertos.
- **F4:** windows/import integrated; windows/auth #74 holding; windows/review #72 fully green pending integration; 25.1/25.2 open; D22/D23 externos.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 047

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 2 - Web y UX.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-043`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-042`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-046`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 047.

F0/F1 y Registro de avances fueron leídos; no se cambian sus checkboxes ni Registro porque no hubo merge estable nuevo ni PASS integrado nuevo. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar AAA043/BBB042/WOZ046 una sola vez.
3. Si BBB042 integra #72 y mueve baseline, #69/#74/#73/#75 deberán reconciliar exact-head antes de integración futura.
4. #71 solo vuelve a un owner mediante nueva asignación JOBS después de #74 realmente integrado.
5. #74/#73/#75 no se reintentan mientras sus blockers no cambien factual.
6. Si AAA/BBB usan fallback, procesar solo como audit evidence; no promover checkbox.
7. No hopping automático a #70.
8. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-047
INTEGRATION_HEAD_OBSERVED: a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA_RESULT_PROCESSED: NIGHT-AAA-042 NO_RESULT -> SUPERSEDED
BBB_RESULT_PROCESSED: NIGHT-BBB-041 NO_RESULT -> SUPERSEDED
WOZ_RESULT_PROCESSED: NIGHT-WOZ-045 DONE/AUDIT_ONLY
AAA_NEW: NIGHT-AAA-043
BBB_NEW: NIGHT-BBB-042
WOZ_NEW: NIGHT-WOZ-046
CI_FALLBACKS: F2-12.1-READ_ONLY / F4-25.2-READ_ONLY / NONE
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 047 completado.
