# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 021

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`.
- El baseline avanzó por merge verificado de PR #66.
- Release público: 🔴 `NO-GO`.
- F0: trabajo técnico habilitante cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- F1: D6–D9 PASS; D10.1 external-only por copia off-provider/off-account + read/checksum; D10.2 decisión RO.
- F2: #66 integrado; 12.1 queda solo con cold/warm cuantificado + taxonomy/state residual.
- F3: #67 corrective mínimo ya tiene fresh CI SUCCESS en exact head `8a534111...`, pero esa combinación quedó vieja tras merge #66; refresh requerido antes de merge.
- F4: #63 sigue sin Windows Import literal PASS; failure reducido a WDIO session bootstrap `DevToolsActivePort` antes de assertions y candidate quedó stale tras merge #66.

## PREFLIGHT FACTUAL

Fuentes leídas completas/obligatorias: Plan Maestro, F0–F4, roles/coordinación, protocolo nocturno, cuatro ledgers nocturnos, Registro de avances e Issue #41. GitHub vivo se tomó como autoridad.

Hechos verificados:
1. `integration-v0.8.0-alpha.1` apunta a `712b49b6689a31a47902dbe95e98622d001dab40`, merge #66.
2. AAA `NIGHT-AAA-020` = DONE; PR #66 CLOSED/MERGED; handoff Issue #41 `5465400749`.
3. BBB `NIGHT-BBB-019` = PENDING; no mutation; baseline movement disparó STOP; root diagnosis alcanzó WDIO session creation failure antes de import assertions; handoff `5465407309`.
4. WOZ `NIGHT-WOZ-019` = PENDING/WAITING_CI; corrective `8a534111...` en SAME #67. Al recheck JOBS, todos los workflows fresh de ese head ya terminaron SUCCESS: F3 17.2 `33280134623`, D6 `33280134598`, D7 `33280134660`, temp-auth `33280134648`, Required CI/Desktop Portability `33280134630`.
5. PR #67 sigue OPEN/Ready/mergeable con head `8a534111...`; PR #63 sigue OPEN/Ready con head `ea00d85d...`. Ambos deben reconciliarse contra live integration antes de cualquier claim de merge porque el baseline cambió materialmente.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-020` — DONE
- #66 merge verificado `712b49b6689a31a47902dbe95e98622d001dab40`.
- Pagination/window/memory + navegación productiva bounded quedan integrados.
- 12.1 NO se cierra aún: cold/warm cuantificado y cualquier taxonomy/state residual siguen abiertos.

### BBB / `NIGHT-BBB-019` — PENDING
- SAME #63 preservado; no branch/PR duplicado.
- Failure real no alcanzó producto import: WDIO no creó sesión, `DevToolsActivePort file doesn't exist`.
- Old CI no sirve como merge authorization contra baseline nuevo.
- Se emite `NIGHT-BBB-020` para refresh + corrective F4 mínimo + literal PASS/fresh CI.

### WOZ / `NIGHT-WOZ-019` — PENDING / WAITING_CI resuelto por recheck
- Causa original: recovery verifier hardcodeaba migration ledger 0001..0005; #67 añade 0006.
- Corrective mínimo `8a534111...` deriva expected ledger desde `listMigrations()` y preserva recovery invariants.
- Todos los workflows fresh de ese head ya están SUCCESS.
- No se promueve 17.2 ni se mergea porque #66 movió el baseline después; se emite `NIGHT-WOZ-020` para refresh + fresh exact-head evidence sobre combinación viva.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 / 17.2 / #67:** refresh/race transaction del candidate ya corregido; fresh exact-head sobre live baseline y merge si verde.
2. **F4 / 25.1 / #63:** refresh + minimal session bootstrap corrective hasta Windows Import literal PASS; fresh applicable CI + merge.
3. **F2 / 12.1:** cerrar residual cold/warm + taxonomy/state con REUSE-FIRST; pagination/window/memory ya integrado.
4. **F0/F1:** mantener blockers externos como externos; no repetir drills aceptados.
5. Después: D13–D15, F3 18–20 y F4 25.2/dependencias externas. F5 continúa cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | #66 integrado; residual 12.1 abierto | `NIGHT-AAA-021`: cold/warm cuantificado + taxonomy/state residual | `NONE` |
| BBB | #63 stale; Windows Import sin assertion PASS | `NIGHT-BBB-020`: refresh SAME #63 + minimal session corrective + PASS/fresh CI | `NONE` |
| WOZ | #67 corrective exact-head green en combinación vieja | `NIGHT-WOZ-020`: refresh SAME #67 + fresh exact-head CI + merge si verde | `NONE` |

Ownership exclusivo: AAA=F2/12.1 residual; BBB=#63/F4-25.1; WOZ=#67/F3-17.2. No overlap material.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-021`
- PRIMARY: REUSE-FIRST sobre #58/#66; medir cold/warm de forma reproducible y cerrar únicamente taxonomy/state residual. Si necesita cambios, una sola rama/PR F2 mínima. No D13–D15.
- CI-FALLBACK: `NONE`.
- STOP: scope creep, evidencia no reproducible, CI rojo no atribuible, necesidad de ownership F3/F4 o decisión externa.

### BBB — `NIGHT-BBB-020`
- PRIMARY: SAME #63; refresh onto `712b49b...`; corrective F4 mínimo del WDIO/DevToolsActivePort session bootstrap; Windows Import literal functional PASS + fresh exact-head CI; race-check + merge solo si verde.
- CI-FALLBACK: `NONE`.
- STOP: producto fuera de F4 → `PRODUCT_FINDING`; unrelated delta; CI rojo; scope 25.2/signing/notarization.

### WOZ — `NIGHT-WOZ-020`
- PRIMARY: SAME #67; refresh onto `712b49b...`; preservar corrective `listMigrations()` + recovery invariants; fresh exact-head F3/recovery/Required CI; race-check + merge solo si verde.
- CI-FALLBACK: `NONE`.
- STOP: recovery regression, conflict material, unrelated delta, provider requirement, CI rojo o 18.x scope.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: residual cold/warm + taxonomy/state; D13–D15 abiertos.
6. F3/17.2: refresh/fresh exact-head/merge #67; 18–20 abiertos; 16.x physical/deploy tails externos.
7. F4/25.1: Windows Import session bootstrap + literal PASS; otros matrix gaps; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58/#64/#66 integrados; 12.1 reducido a residual cold/warm/taxonomy; D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 integrado; #67 corrected + old-combination CI all green, pero no integrado; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 sin Windows Import literal PASS; 25.1/25.2 abiertos; D22/D23 externos.

## PLAN SYNC — CYCLE 021

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 2 - Web y UX.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/NOCHE - AAA.md`;
- `!!!PLAN/NOCHE - BBB.md`;
- `!!!PLAN/NOCHE - WOZ.md`;
- `!!!PLAN/NOCHE - JOBS.md`.

F0/F1 no cambiaron materialmente. `Registro de avances.md` fue leído; no se reescribió para evitar una sustitución destructiva del ledger largo cuando Plan Maestro/F2 ya registran el merge #66 con evidencia verificable. JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar AAA-021, BBB-020 y WOZ-020 una sola vez.
3. Si WOZ o BBB integra y mueve baseline, obligar race revalidation/fresh applicable exact-head en el candidate restante.
4. Si AAA prueba ambos residuales 12.1 e integra cualquier cambio necesario, evaluar cierre 12.1 sin adelantar D13.
5. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-021
INTEGRATION_HEAD_OBSERVED: 712b49b6689a31a47902dbe95e98622d001dab40
AAA_RESULT_PROCESSED: NIGHT-AAA-020 DONE / #66 merged
BBB_RESULT_PROCESSED: NIGHT-BBB-019 PENDING / baseline STOP + DevToolsActivePort diagnosis
WOZ_RESULT_PROCESSED: NIGHT-WOZ-019 PENDING; recheck found all fresh head CI SUCCESS
AAA_NEW: NIGHT-AAA-021 ASSIGNED
BBB_NEW: NIGHT-BBB-020 ASSIGNED
WOZ_NEW: NIGHT-WOZ-020 ASSIGNED
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 021 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-021`, `NIGHT-BBB-020` y `NIGHT-WOZ-020`.
