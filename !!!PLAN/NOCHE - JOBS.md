# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 022`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 022

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`.
- Release público: 🔴 `NO-GO`.
- No hubo nuevo merge/PASS integrable en este ciclo: #63 y #67 siguen OPEN / NOT MERGED; 12.1 sigue sin cierre factual.
- F0: trabajo técnico habilitante cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- F1: D6–D9 PASS; D10.1 external-only por copia off-provider/off-account + read/checksum; D10.2 decisión RO.
- F2: #66 integrado; 12.1 queda con cold/warm cuantificado + taxonomy/state residual.
- F3: #67 ya fue refrescado sobre `712b49b...` y casi todo exact-head está verde; Desktop Portability aún corría al último recheck.
- F4: #63 ya fue refrescado sobre `712b49b...`; Windows Import exact-head terminó FAILURE antes de assertions.

## PREFLIGHT FACTUAL

Fuentes leídas completas/obligatorias: Plan Maestro, F0–F4, roles/coordinación, protocolo nocturno, cuatro ledgers nocturnos, Registro de avances e Issue #41 completo. GitHub vivo se tomó como autoridad.

Hechos verificados:
1. `integration-v0.8.0-alpha.1` sigue en `712b49b6689a31a47902dbe95e98622d001dab40`, merge #66.
2. AAA: último resultado final verificable `NIGHT-AAA-020 DONE`; `NIGHT-AAA-021` no tenía RESULTADO DEL TURNO ni artifact/handoff observable al iniciar este ciclo.
3. BBB: PR #63 OPEN/Ready/mergeable, base `712b49b...`, head `2a5853209669f7b50b51126f0aa4572383492c26`.
4. WOZ: PR #67 OPEN/Ready/mergeable, base `712b49b...`, head `27c2f30007a687a144be289a64ab986451f05c99`.
5. Duplicate-check: no replacement PR para #63/#67; búsqueda de `NIGHT-AAA-021` en BeatGaler no encontró artifact nuevo.
6. Ownership exclusivo: AAA=F2/12.1; BBB=#63/F4-25.1; WOZ=#67/F3-17.2.

## RESULTADOS PROCESADOS

### AAA

- `NIGHT-AAA-020 = DONE`; #66 merge verificado `712b49b6689a31a47902dbe95e98622d001dab40`.
- 12.1 NO se cierra: faltan cold/warm cuantificado y cierre factual de taxonomy/state residual.
- `NIGHT-AAA-021`: `NOT_PROCESSED / SUPERSEDED_BY_JOBS` para impedir ejecución tardía/duplicada; se emite 022.

### BBB / `NIGHT-BBB-020`

- Worker cerró `PENDING / WAITING_CI`; JOBS resolvió la espera con recheck final.
- Exact head `2a5853209669f7b50b51126f0aa4572383492c26`:
  - D6 `33281787207` SUCCESS;
  - D7 `33281787235` SUCCESS;
  - Desktop Portability `33281787208` SUCCESS;
  - F4 Functional Matrix `33281787222` SUCCESS;
  - Upgrade 21.2 `33281787228` SKIPPED/no aplicable;
  - Windows Import Journey `33281787254` **FAILURE**.
- Failure literal: embedded-prep + E2E build terminaron; después `@wdio/tauri-service` cayó al launcher legacy, reportó Edge `151.0.4129.101` vs driver `unknown`, `tauri-driver not found`, y finalmente `No "browserName" defined in capabilities nor hostname or port found`.
- `0 passed / 1 failed`; no assertion de import alcanzada.
- `windows/import` continúa `NOT_COVERED`; no AUTOMATED_PASS; no merge.

### WOZ / `NIGHT-WOZ-020`

- Worker cerró `PENDING / WAITING_CI` sobre refreshed head `27c2f30007a687a144be289a64ab986451f05c99`.
- Recheck exact head:
  - F3 17.2 `33283532676` SUCCESS;
  - D6 `33283532664` SUCCESS;
  - D7 `33283532679` SUCCESS;
  - productive temp-auth `33283532723` SUCCESS;
  - Upgrade 21.2 `33283532704` SKIPPED/no aplicable;
  - Desktop Portability `33283532696` **IN_PROGRESS** al último recheck.
- #67 permanece NOT MERGED; 17.2 no se promueve todavía.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 / 17.2 / #67:** terminar el último exact-head gate, race-check e integrar SAME #67 si todo queda verde. Es el candidato más cercano al cierre y da base confiable a 18.x.
2. **F4 / 25.1 / #63:** corregir la selección efectiva del provider WDIO y obtener Windows Import literal PASS; el fallo actual es harness/session antes de assertions, no evidencia de bug productivo.
3. **F2 / 12.1:** producir cold/warm cuantificado + verificar/cerrar taxonomy/state residual; no reimplementar lo ya integrado en #58/#66.
4. **F0/F1:** mantener external tails como externos; no repetir drills aceptados ni fabricar evidencia.
5. Después de estos carriles: D13–D15, F3 18–20, F4 25.2 y release-chain restante según dependencias/gates vivos. F5 continúa cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | #66 integrado; 12.1 residual abierto; 021 sin resultado | `NIGHT-AAA-022`: cold/warm cuantificado + taxonomy/state residual | `NONE` |
| BBB | #63 refreshed; Windows Import exact-head FAILURE antes de assertions | `NIGHT-BBB-021`: SAME #63, activar realmente embedded WDIO y alcanzar literal PASS | `NONE` |
| WOZ | #67 refreshed; focused gates SUCCESS; Desktop Portability aún corriendo | `NIGHT-WOZ-021`: SAME #67 final exact-head gate + race/merge | `NONE` |

Ownership exclusivo: AAA=F2/12.1 residual; BBB=#63/F4-25.1; WOZ=#67/F3-17.2. No overlap material.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-022`
- PRIMARY: REUSE-FIRST sobre #58/#66; medir cold/warm de forma reproducible y cerrar únicamente taxonomy/state residual. Si necesita cambios, una sola rama/PR F2 mínima. No D13–D15.
- Evidencia requerida: comparación cold/warm cuantificada/reproducible; separación literal empty/no-results/offline/auth/cloud-failure; focused tests; exact-head CI/race/merge solo si hay cambio.
- CI-FALLBACK: `NONE`.
- STOP: scope creep, evidencia no reproducible, CI rojo no atribuible, necesidad de ownership F3/F4 o decisión externa.

### BBB — `NIGHT-BBB-021`
- PRIMARY: SAME #63; diagnosticar por qué `driverProvider=embedded` preparado no fue consumido por la config WDIO efectiva; corregir únicamente esa causa F4/harness; obtener session efectiva + import assertions literal PASS antes de promover matrix.
- Evidencia requerida: log de provider/session efectiva; literal PASS; tras cualquier promoción/head nuevo, fresh exact-head Windows Import + F4 Matrix + D6 + D7 + Desktop Portability; race-check + merge solo si verde.
- CI-FALLBACK: `NONE`.
- STOP: tocar lógica productiva antes de assertion fallida, scope 25.2/signing/notarization, package/global changes no justificadas o CI rojo no atribuible.

### WOZ — `NIGHT-WOZ-021`
- PRIMARY: SAME #67; recheck final exact head `27c2f300...`; si Desktop Portability completa SUCCESS y integration sigue `712b49b...`, verificar 5-path scope, race-check e integrar SAME #67 por flujo técnico autorizado.
- Evidencia requerida: final applicable exact-head CI, exact base/head, changed-file scope, race-check, merge SHA + integration HEAD.
- Si CI falla o baseline mueve: no usar evidencia stale; corrective/refresco mínimo y fresh exact-head CI.
- CI-FALLBACK: `NONE`.
- STOP: recovery regression, unrelated delta, baseline race no reconciliable, provider externo, CI rojo o expansión a 18.x.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: residual cold/warm + taxonomy/state; D13–D15 abiertos.
6. F3/17.2: Desktop Portability `33283532696` seguía IN_PROGRESS; #67 aún no integrado; 18–20 abiertos.
7. F4/25.1: Windows Import `33281787254` FAILURE antes de assertions; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58/#64/#66 integrados; 12.1 reducido a residual cold/warm/taxonomy; D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 integrado; #67 refreshed y casi totalmente verde, pero no integrado; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 sin Windows Import literal PASS; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 022

Actualizados por JOBS:
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-022`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-021`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-021`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 022.

No se cambió ningún checkbox/gate estable de Plan Maestro/Fases 0–4 porque este ciclo no produjo merge/PASS/cierre nuevo. El delta transitorio vivo (#63 FAILURE; #67 partial-green/WAITING_CI) queda en los ledgers y se promoverá al plan estable solo cuando cambie un estado material confirmado. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar `NIGHT-WOZ-021`; si #67 integra, sincronizar F3/17.2 y recalcular 18.x.
3. Procesar `NIGHT-BBB-021`; exigir Windows Import literal PASS, no aceptar green genérico como sustituto.
4. Procesar `NIGHT-AAA-022`; cerrar 12.1 solo con cold/warm + taxonomy/state demostrados.
5. Si cualquier merge mueve integration, obligar race revalidation/fresh applicable exact-head en candidatos restantes.
6. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-022
INTEGRATION_HEAD_OBSERVED: 712b49b6689a31a47902dbe95e98622d001dab40
AAA_RESULT_PROCESSED: NIGHT-AAA-020 DONE; NIGHT-AAA-021 no-result -> superseded
BBB_RESULT_PROCESSED: NIGHT-BBB-020 PENDING at worker close; recheck Windows Import 33281787254 FAILURE
WOZ_RESULT_PROCESSED: NIGHT-WOZ-020 PENDING/WAITING_CI; focused exact-head gates SUCCESS; Desktop Portability 33283532696 IN_PROGRESS
AAA_NEW: NIGHT-AAA-022 ASSIGNED
BBB_NEW: NIGHT-BBB-021 ASSIGNED
WOZ_NEW: NIGHT-WOZ-021 ASSIGNED
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 022 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-022`, `NIGHT-BBB-021` y `NIGHT-WOZ-021`.
