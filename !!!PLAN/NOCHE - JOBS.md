# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 043`.

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
2. AAA039 sigue ASSIGNED. PR #74 sigue OPEN/Ready/mergeable @ `92058b42e6e455f641e8a494f5c85ae1f2214834`; head sin cambio y Required CI sigue FAILURE por el TS2339 ya conocido. No existe resultado final nuevo del worker; no superseder.
3. BBB038 sigue ASSIGNED. PR #72 sigue OPEN/Ready/mergeable @ `3219996e181ef3f53508b1ea1d272d84b73bc1a4`; head sin cambio. El literal Windows Review PASS previo sigue válido como input, pero la promoción/fresh-post-promotion transaction todavía no fue reportada; no superseder.
4. WOZ041 terminó `PENDING / WAITING_CI` con PR #75 OPEN/Ready/mergeable @ `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`, base exacta `a9d35a3d...`, 4 files +156/-0.
5. JOBS recheck de #75: Required CI / Test - Desktop Portability run `33323457041` terminó FAILURE. El job `Supply chain gate` falló exactamente en `Verify every external GitHub Action is immutable`.
6. Patch del único workflow nuevo confirma `actions/checkout@v4` y `actions/setup-node@v4`; el workflow canónico Required CI ya usa los pins inmutables `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` y `actions/setup-node@820762786026740c76f36085b0efc47a31fe5020`. Failure atribuible y correctivo mínimo claro.
7. #73 sigue congelado/untouched; no nueva evidencia de merge flow capaz.
8. F0/F1 sin evidencia externa nueva; F2 12.1 runtime blocker persiste; #69/#70 holding/frozen.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-039
`NO_NEW_RESULT / KEEP_ASSIGNED`.
- No crear `NIGHT-AAA-040` porque duplicaría SAME #74 antes de procesar 039.
- Assignment actual permanece intacta.

### BBB / NIGHT-BBB-038
`NO_NEW_RESULT / KEEP_ASSIGNED`.
- No crear `NIGHT-BBB-039` porque duplicaría SAME #72 antes de procesar 038.
- Assignment actual permanece intacta.

### WOZ / NIGHT-WOZ-041
`PENDING / WAITING_CI -> FAILURE_RESOLVED_BY_JOBS_RECHECK`.
- SAME #75 es el candidate correcto; no replacement PR.
- Failure atribuible únicamente a floating external Action refs del workflow nuevo.
- Nuevo `NIGHT-WOZ-042` emitido SAME #75 para pin-only corrective + fresh exact-head CI.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 product-auth / #74:** resolver compile exacto y obtener candidate verde; después #71 requiere nueva BBB assignment para Windows Auth literal.
2. **F4 windows/review / #72:** PASS literal ya existe; promotion + fresh gates + integration sigue siendo transacción corta pendiente.
3. **F3/20.1 / #75:** corregir únicamente immutable Action pins; revalidar exact-head; integrar si todo verde y merge flow disponible.
4. **F3/18.2 #73:** integration-ready pero bloqueado por execution layer; no duplicar trabajo.
5. **F2/13.1 #69:** Save All product wiring + refresh; holding hasta liberar owner.
6. **F2/12.1:** real-browser cold/warm bloqueado por runtime ejecutable.
7. **F2/#70:** safe-write + stale baseline frozen.
8. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY vigente/nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 039 sin resultado nuevo | `NIGHT-AAA-039`: SAME #74 compile/type corrective + fresh CI | `NONE` |
| BBB | 038 sin resultado nuevo | `NIGHT-BBB-038`: SAME #72 promotion + fresh post-promotion gates + merge | `NONE` |
| WOZ | 041 WAITING_CI -> Required CI FAILURE atribuible | `NIGHT-WOZ-042`: SAME #75 immutable-action pin corrective + fresh CI | `NONE` |

No overlap material: AAA product runtime/auth; BBB Review F4; WOZ observability F3. #73/#69/#70 quedan holding/frozen.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-039 — CONTINÚA
PRIMARY: SAME #74; arreglar únicamente TS2339 sobre `__TAURI_INTERNALS__` sin cambiar semántica ni contrato auth; focused regression + fresh exact-head D6/D7/Required CI; integrar solo si la autoridad/flujo lo permite y todo queda verde. No tocar #71.  
CI-FALLBACK: `NONE`.

### BBB — NIGHT-BBB-038 — CONTINÚA
PRIMARY: SAME #72; consumir PASS literal `33321799798`, promover solo `windows/review = AUTOMATED_PASS`; exigir después fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Desktop Portability; race-check + merge solo si verde. No auth/#71/#74.  
CI-FALLBACK: `NONE`.

### WOZ — NIGHT-WOZ-042 — NUEVA
PRIMARY: SAME #75; reemplazar solo `actions/checkout@v4` y `actions/setup-node@v4` por los pins inmutables canónicos ya usados por Required CI; no cambiar product/observability semantics; focused test + fresh exact-head Required CI/F3 20.1; race-check + merge solo si todo verde y merge flow disponible. No tocar #73.  
CI-FALLBACK: `NONE`.  
STOP: non-pinning failure, scope drift, baseline race, merge-flow unavailable, provider/RO dependency o necesidad de tocar #73.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: product wiring + refresh; holding/stale.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F3/18.2 #73: software slice exact-head green pero merge-flow unavailable; provider/business tails además abiertos.
9. F3/20.1 #75: Required CI rojo por floating action refs; pin corrective WOZ042; product wiring/backend/external observability tails siguen abiertos.
10. F4/windows-auth: #74 compile-red; #71 waiting corrective integrado + literal rerun.
11. F4/windows-review: literal PASS candidate; matrix promotion/integration pendiente BBB038.
12. F4/25.1: otras rows NOT_COVERED/PENDING_EXTERNAL.
13. F4/25.2 + D22/D23 external signing/notarization.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69/#70 holding/frozen.
- **F3:** 17.1/17.2/18.1 integrated; 18.2 #73 green but merge-flow blocked; 20.1 #75 candidate exists but Required CI pin-failure.
- **F4:** windows/import integrated; windows/auth corrective compile-red; windows/review literal PASS pending promotion/integration; 25.1/25.2 open.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 043

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-042`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 043.

AAA/BBB nocturnos no se reescriben porque sus assignments 039/038 siguen vigentes sin resultado nuevo. F0/F1/F2/F4 y Registro de avances fueron leídos completos; no se cambian sus checkboxes ni Registro porque no hubo merge/PASS estable nuevo integrado. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar AAA039/BBB038/WOZ042 una sola vez.
3. Si cualquiera integra y mueve baseline, revalidar los candidates restantes antes de cualquier integración posterior.
4. #71 solo vuelve a BBB después de #74 verde/integrado y nueva asignación explícita JOBS.
5. #73 queda intacto hasta disponer de merge flow capaz.
6. No hopping automático a #69/#70.
7. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-043
INTEGRATION_HEAD_OBSERVED: a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA_RESULT_PROCESSED: NONE / NIGHT-AAA-039 remains ASSIGNED
BBB_RESULT_PROCESSED: NONE / NIGHT-BBB-038 remains ASSIGNED
WOZ_RESULT_PROCESSED: NIGHT-WOZ-041 WAITING_CI -> Required CI FAILURE / immutable-action attribution
AAA_CURRENT: NIGHT-AAA-039
BBB_CURRENT: NIGHT-BBB-038
WOZ_NEW: NIGHT-WOZ-042
CI_FALLBACKS: NONE/NONE/NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 043 completado.
