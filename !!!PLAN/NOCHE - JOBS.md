# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 042`.

## META

Terminar F0–F4 o reducirlos al mínimo factual de blockers externos. Prioridad: F0–F4 → sencillez → limpieza. Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head obligatorios.

## BASELINE VIVO

- `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- Último merge material: PR #68 → `a9d35a3d...`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/revisados: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo; GitHub vivo. GitHub/runtime prevaleció.

Hechos verificados:
1. Integration sigue exactamente `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; no hubo merge posterior a #68.
2. AAA038 terminó `PENDING / WAITING_CI` con PR #74 OPEN/Ready/mergeable @ `92058b42e6e455f641e8a494f5c85ae1f2214834`, base exacta `a9d35a3d...`.
3. JOBS recheck de #74: D6 `33321752555` SUCCESS; D7 `33321752537` SUCCESS; Upgrade 21.2 SKIPPED; `Test - Desktop Portability / Required CI` `33321752522` FAILURE. Root cause literal: TypeScript `src/platform/index.ts(10,22)` no reconoce `__TAURI_INTERNALS__` sobre el tipo unión actual. No #74 PASS/merge y #71 no se revalida todavía.
4. BBB037 terminó `PENDING / WAITING_CI` sobre SAME #72 head `3219996e181ef3f53508b1ea1d272d84b73bc1a4` después de corregir solo expectativa de key normalizada `F#m -> f#m` en harness.
5. JOBS recheck de #72: Windows Review `33321799798` SUCCESS literal; Windows Import `33321799800`, Desktop Portability `33321799802`, D6 `33321799792`, D7 `33321799819` SUCCESS; Upgrade 21.2 SKIPPED. Matrix aún no promovida; PR no merged.
6. WOZ040 terminó `BLOCKED / MERGE_FLOW_UNAVAILABLE`: #73 OPEN/Ready/mergeable, base `a9d35a3d...`, head `fc831172...`, exact-head CI verde y race-check limpio; execution layer bloqueó merge antes de aceptación por GitHub. Integration no cambió.
7. F0/F1 sin evidencia externa nueva; F2 12.1 runtime blocker persiste; #69/#70 holding/frozen.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-038
`PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- SAME #74 continúa candidate correcto; no replacement PR.
- Failure atribuible a compile/type issue en el corrective, no a D6/D7 ni a provider externo.
- Nuevo `NIGHT-AAA-039` emitido sobre SAME #74 para correctivo mínimo + fresh CI.

### BBB / NIGHT-BBB-037
`PENDING / WAITING_CI -> PASS_RESOLVED_BY_JOBS_RECHECK`.
- SAME #72 dedicated Review tiene literal PASS sobre exact head `3219996e...`.
- Matrix row aún no cambió; no merge.
- Nuevo `NIGHT-BBB-038` emitido para promotion-only + fresh post-promotion exact-head gates + merge si green/race-clean.

### WOZ / NIGHT-WOZ-040
`BLOCKED / MERGE_FLOW_UNAVAILABLE`.
- #73 technical evidence sigue válida y exact-head green, pero no integrada.
- No repetir/recrear/rebasear #73 mientras base/head sigan válidos.
- Para maximizar avance global, WOZ se mueve explícitamente a pieza independiente F3/20.1 bajo `NIGHT-WOZ-041`.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 product-auth / #74:** corregir compile exacto y obtener candidate verde; después #71 requiere nueva BBB assignment para Windows Auth literal.
2. **F4 windows/review / #72:** PASS literal ya existe; promotion + fresh gates + integration es la transacción ejecutable más corta.
3. **F3/20.1:** cerrar gaps internos software mientras #73 espera un canal de merge funcional.
4. **F3/18.2 #73:** integration-ready pero bloqueado por execution layer; no duplicar trabajo.
5. **F2/13.1 #69:** Save All product wiring + refresh; holding hasta liberar owner.
6. **F2/12.1:** real-browser cold/warm sigue bloqueado por runtime ejecutable.
7. **F2/#70:** safe-write + stale baseline frozen.
8. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 038 WAITING_CI -> Required CI FAILURE atribuible | `NIGHT-AAA-039`: SAME #74 compile/type corrective + fresh CI | `NONE` |
| BBB | 037 WAITING_CI -> Windows Review literal PASS | `NIGHT-BBB-038`: SAME #72 promotion + fresh post-promotion gates + merge | `NONE` |
| WOZ | 040 BLOCKED / MERGE_FLOW_UNAVAILABLE | `NIGHT-WOZ-041`: F3/20.1 internal observability slice | `NONE` |

No overlap material: AAA product runtime/auth; BBB Review F4; WOZ observability F3. #73/#69/#70 quedan holding/frozen.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-039
PRIMARY: SAME #74; arreglar únicamente TS2339 sobre `__TAURI_INTERNALS__` sin cambiar semántica ni contrato auth; focused regression + fresh exact-head D6/D7/Required CI; integrar solo si la autoridad/flujo lo permite y todo queda verde. No tocar #71.  
CI-FALLBACK: `NONE`.  
STOP: semantic drift, auth contract change, baseline race, CI rojo no atribuible, merge-flow unavailable o necesidad de tocar #71.

### BBB — NIGHT-BBB-038
PRIMARY: SAME #72; consumir PASS literal `33321799798`, promover solo `windows/review = AUTOMATED_PASS`; exigir después fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Desktop Portability; race-check + merge solo si verde. No auth/#71/#74.  
CI-FALLBACK: `NONE`.  
STOP: failure nuevo, matrix contract failure no atribuible, baseline race, merge-flow unavailable, scope drift o auth overlap.

### WOZ — NIGHT-WOZ-041
PRIMARY: F3/20.1; REUSE-FIRST del gap map WOZ033; cerrar solo gaps internos software de observability/alerts/runbook/kill-switch. No tocar #73 ni crear provider/on-call/status/retention externos; no 20.2.  
CI-FALLBACK: `NONE`.  
STOP: provider/RO decision, overlap, scope creep, external evidence requirement, CI rojo no atribuible o baseline race.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: product wiring + refresh; holding/stale.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F3/18.2 #73: software slice exact-head green pero merge-flow unavailable; provider/business tails además abiertos.
9. F3/20.1: internal gaps en trabajo WOZ041 + external observability/on-call/status tails.
10. F4/windows-auth: #74 compile-red; #71 waiting corrective integrado + literal rerun.
11. F4/windows-review: literal PASS candidate; matrix promotion/integration pendiente BBB038.
12. F4/25.1: otras rows NOT_COVERED/PENDING_EXTERNAL.
13. F4/25.2 + D22/D23 external signing/notarization.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69/#70 holding/frozen.
- **F3:** 17.1/17.2/18.1 integrated; 18.2 #73 green but merge-flow blocked; 20.1 internal slice assigned.
- **F4:** windows/import integrated; windows/auth corrective compile-red; windows/review literal PASS pending promotion/integration; 25.1/25.2 open.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 042

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-039`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-038`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-041`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 042.

F0/F1/F2 y Registro de avances fueron leídos completos. No se cambian sus checkboxes ni Registro porque no hubo merge/PASS estable nuevo integrado. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar AAA039/BBB038/WOZ041 una sola vez.
3. Si BBB038 integra #72 y mueve baseline, revalidar #74/#73 antes de cualquier integración posterior.
4. #71 solo vuelve a BBB después de #74 verde/integrado y nueva asignación explícita JOBS.
5. #73 queda intacto hasta disponer de merge flow capaz; no gastar worker repitiendo el mismo bloqueo.
6. No hopping automático a #69/#70.
7. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-042
INTEGRATION_HEAD_OBSERVED: a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA_RESULT_PROCESSED: NIGHT-AAA-038 WAITING_CI -> Required CI FAILURE / TS compile attribution
BBB_RESULT_PROCESSED: NIGHT-BBB-037 WAITING_CI -> Windows Review literal PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-040 BLOCKED / MERGE_FLOW_UNAVAILABLE
AAA_NEW: NIGHT-AAA-039
BBB_NEW: NIGHT-BBB-038
WOZ_NEW: NIGHT-WOZ-041
CI_FALLBACKS: NONE/NONE/NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 042 completado.
