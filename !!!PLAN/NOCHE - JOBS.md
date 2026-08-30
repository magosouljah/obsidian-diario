# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 049`.

## META

Terminar F0–F4 o reducirlos al mínimo factual de blockers externos. Prioridad: F0–F4 → sencillez → limpieza. Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head obligatorios.

## BASELINE VIVO

- Preflight: `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- Último merge material verificado al preflight: PR #68 → `a9d35a3d...`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/revisados: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo vía recurso paginado; GitHub vivo. GitHub/runtime prevaleció sobre snapshots viejos.

Hechos verificados:
1. Integration seguía exactamente `a9d35a3d69dd9127029fb851d189f9bd3079d03b` al preflight; commit = merge PR #68.
2. AAA044 no dejó RESULTADO DEL TURNO ni handoff observable; no se acepta audit/PASS. AAA043 sigue siendo el último resultado factual: `PENDING / STOP_WRITE_SURFACE`, #69 unchanged/frozen.
3. BBB043 no dejó RESULTADO DEL TURNO ni handoff observable. #72 sigue OPEN, draft=false, mergeable=true, merged=false, base exacta `a9d35a3d...`, head `904fbf3c...`; exact-head Windows Review/Matrix/D6/D7/Required CI/Windows Import conocidos verdes.
4. WOZ047 no dejó RESULTADO DEL TURNO ni handoff observable. No `HARNESS_READY` aceptado.
5. #73 sigue OPEN/Ready/mergeable, base exacta `a9d35a3d...`, head `fc831172...`; exact-head F3 Reconciliation `33320621931`, D7 `33320621893`, D6 `33320621877`, compile `33320621868`, Test Desktop Portability `33320621865` SUCCESS; Upgrade `33320621863` SKIPPED.
6. Nuevo hecho material: PR #76 OPEN/Ready/mergeable, base exacta `a9d35a3d...`, head `36d218609cf2488997755312fa2dafd0a019d070`. Contiene Privacy/Terms v1 owner-approved, rutas `/privacy` `/terms`, links públicos; Test Desktop Portability `33330007495`, D6 `33330007538`, D7 `33330007493` SUCCESS; Upgrade `33330007497` SKIPPED. Issue #41 deja handoff explícito: `SettingsPanel.tsx` aún contiene copy legal temporal/placeholders/contacto viejo y debe reutilizar los documentos canónicos, no crear UI duplicada.
7. #69 sigue OPEN/Ready/mergeable @ `b2ab75ae...` con base histórica `3ad8f55a...`; blocker de write surface no cambió.
8. F0/F1 no recibieron evidencia externa nueva. Registro de avances se leyó y no recibe entrada nueva: no hubo merge estable/PASS integrado nuevo procesado en este ciclo.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-044
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No claim de audit ni de 13.2.
- El audit read-only se conserva solo como fallback de AAA045 mientras el nuevo PRIMARY espere una operación externa.

### BBB / NIGHT-BBB-043
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No claim de merge.
- #72 sigue candidate exact-base/head green y pasa a BBB044.

### WOZ / NIGHT-WOZ-047
`NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No claim de harness/CI.
- El harness 20.2 pasa a fallback condicional de WOZ048; el PRIMARY cambia a #73 por estar más arriba en F3 y listo para integrar.

### RO/OWNER / PR #76
`NEW MATERIAL FACT / ACCEPTED AS CANDIDATE, NOT AS INTEGRATED PASS`.
- Canonical legal docs/public routes/entry links existen en exact-base candidate con CI general verde.
- In-app Settings legal copy sigue stale; AAA045 recibe owner explícito para reuse mínimo.
- No se marca 19.2 `[x]` ni se afirma deploy/productive legal publication.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 #73 / 18.2 reconciliation:** exact-base/head green; software slice anterior a 19/20 y listo para integration transaction.
2. **F4 #72 / windows-review:** exact-base/head green; integration puede promover una journey literal ya probada.
3. **F3 #76 / 19.2 legal:** canonical docs/public routes green; falta consistency mínima in-app antes de integración ideal.
4. **F2 #69 / 13.1 Web:** crítico pero bloqueado por write surface; no repetir PRIMARY ciego.
5. **F2 / 13.2:** audit mínimo solo como fallback AAA durante wait externo de #76.
6. **F4 #74 → #71 / windows-auth:** frozen bajo merge-flow blocker previo.
7. **F3 #75 / 20.1:** frozen bajo write-flow blocker.
8. **F3 / 20.2:** harness puede avanzar como fallback WOZ; approved peak + runtime 2× siguen separados.
9. **F2 / 12.1:** runtime real-browser cold/warm.
10. **F2 #70:** safe-write + stale baseline frozen.
11. **F0/F1/F3 external tails + F4 D22/D23 + resto F2/F4:** externos/RO o todavía abiertos. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 044 NO_RESULT → superseded | `NIGHT-AAA-045`: SAME #76 canonical legal Settings reuse + tests/CI | F2/13.2 READ-ONLY gap map solo mientras #76 espera CI/review/merge |
| BBB | 043 NO_RESULT → superseded | `NIGHT-BBB-044`: SAME #72 race-check + integración | F4/25.2 READ-ONLY readiness inventory solo mientras PRIMARY espera merge/review/queue |
| WOZ | 047 NO_RESULT → superseded | `NIGHT-WOZ-048`: SAME #73 race-check + integración | F3/20.2 separate parameterized harness solo mientras PRIMARY espera CI/review/merge |

No overlap material: AAA #76/Settings+legal; BBB #72/F4 review harness; WOZ #73/billing reconciliation. Los fallbacks excluyen explícitamente los archivos/PRs de sus PRIMARY y de otros owners.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — NIGHT-AAA-045
PRIMARY: SAME #76. Reuse canonical Privacy/Terms docs and existing Settings legal surfaces; replace only stale in-app legal copy/placeholders/contact with canonical v1. Preserve public routes/links. Focused tests + fresh exact-head CI. No second legal UI, no policy invention, no #69/#70, no infra/DNS/deploy.  
CI-FALLBACK: F2/13.2 READ-ONLY only after PRIMARY code-complete WAITING_CI/review/merge. Evidence = baseline + requirement matrix + paths/symbols/tests/minimum slices. STOP on any write/overlap/dependency abuse. Recheck PRIMARY before close.

### BBB — NIGHT-BBB-044
PRIMARY: SAME #72; consume exact-head green set, race-check and merge only if integration/head remain applicable. Baseline move → narrow refresh + fresh applicable CI. No auth/legal/other PRs.  
CI-FALLBACK: F4/25.2 READ-ONLY only while waiting external merge/review/queue; no writes; recheck PRIMARY before close.

### WOZ — NIGHT-WOZ-048
PRIMARY: SAME #73; consume exact-head green set, race-check and integrate reconciliation/exception-queue software slice. Baseline move → narrow refresh + fresh applicable CI. Do not close full 18.2.  
CI-FALLBACK: F3/20.2 on separate branch/PR only while PRIMARY waits external operation. Target explicit; absent approved target no 2×/PASS claim. No provider/infra load and no #73/#75 overlap. Result max `HARNESS_READY`; runtime remains UNVERIFIED. Recheck PRIMARY before close.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: off-provider/off-account copy + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: runtime real browser cold/warm.
6. F2/13.1 #69: patch-capable write surface + refresh/product wiring.
7. F2/13.1 #70: safe-write blocker + stale baseline.
8. F2/13.2: audit no ejecutado; solo fallback AAA045.
9. F3/18.2 #73: integration pending WOZ048; provider/payment scenario tails remain after software slice.
10. F3/19.1/19.2: #76 candidate not integrated; Settings stale; production DNS/deploy/support/legal-review tails remain.
11. F3/20.1 #75: pin corrective + write blocker; external observability tails abiertos.
12. F3/20.2: approved peak + harness + runtime 2× proof; harness only conditional fallback WOZ048.
13. F4/windows-auth: #74 unmerged under prior blocker; #71 waits integration + new assignment.
14. F4/windows-review: #72 exact-head green; integration pending BBB044.
15. F4/25.1: otras rows NOT_COVERED/PENDING_EXTERNAL.
16. F4/25.2 + D22/D23: readiness/signing/notarization externos.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 12.1 runtime residual; 13.1 #69/#70 frozen; 13.2 fallback audit; resto 14–15 abierto.
- **F3:** 17.1/17.2/18.1 integrated; 18.2 #73 now active; 19.2 gained new canonical legal candidate #76 but remains open; 20.1 #75 blocked; 20.2 harness conditional fallback.
- **F4:** windows/import integrated; windows/auth #74 holding; windows-review #72 green pending integration; 25.1/25.2 open; D22/D23 externos.
- **F5:** `NO ABRIR`.

## PLAN SYNC — CYCLE 049

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 2 - Web y UX.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-045`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-044`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-048`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 049.

F0/F1 y Registro de avances fueron leídos; no se cambian sus checkboxes ni Registro porque no hubo merge estable nuevo ni PASS integrado nuevo procesado. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Releer integration HEAD.
2. Procesar AAA045/BBB044/WOZ048 una sola vez.
3. El primer merge entre #72/#73/#76 que mueva baseline obliga a los otros candidates a race-check y, si su evidencia deja de aplicar, narrow refresh + fresh exact-head CI.
4. #69 solo vuelve a PRIMARY de implementación cuando cambie factual el blocker de write surface.
5. #74/#75/#70 no se reintentan mientras blockers no cambien factual.
6. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-049
INTEGRATION_HEAD_PREFLIGHT: a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA_RESULT_PROCESSED: NIGHT-AAA-044 NO_RESULT -> SUPERSEDED
BBB_RESULT_PROCESSED: NIGHT-BBB-043 NO_RESULT -> SUPERSEDED
WOZ_RESULT_PROCESSED: NIGHT-WOZ-047 NO_RESULT -> SUPERSEDED
NEW_MATERIAL_FACT: PR #76 exact-base legal candidate + owner handoff
AAA_NEW: NIGHT-AAA-045
BBB_NEW: NIGHT-BBB-044
WOZ_NEW: NIGHT-WOZ-048
CI_FALLBACKS: F2-13.2-READ_ONLY / F4-25.2-READ_ONLY / F3-20.2-SEPARATE_HARNESS
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 049 completado después del race-check final y publicación del handoff de coordinación.
