# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 012 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`.
- GitHub demuestra que este SHA es merge de PR #60, parents `58a6bf61441f08bf68aa63673c0d5f2994b220d9` + exact candidate `945638c8bb650b0ce0bbe569e48a791a93d80e39`.
- Release público: 🔴 `NO-GO`.
- F0: 1.2 y 2.2 siguen tails externos/administrativos; no hay slice técnico nocturno de mayor retorno.
- F1: D6/D7/D8/D9 PASS; D10.1 external-only por off-provider/off-account copy + read/checksum; D10.2 requiere decisión RO.
- F2: #58 integrado slice A. `NIGHT-AAA-012` quedó BLOCKED con evidencia correcta: Web-only carece de create-if-absent/CAS y pin-only no es atomicidad. Atomic bootstrap sigue abierto.
- F3: #61 sigue OPEN/Ready/mergeable @ `aef1cd0b1a26be327e561f344d63dae5d8def7ef`, pero base snapshot `58a6bf614...` quedó stale tras #60. Protected merge rechazó correctamente el reuse del green viejo; requiere refresh + exact-head CI nuevo.
- F4: #60 está CLOSED/MERGED como `7de7b57a...`. El artifact de matriz 25.1 está integrado, pero sus gaps `NOT_COVERED/PENDING_EXTERNAL/PRODUCT_FINDING` siguen abiertos.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-012`
- `BLOCKED` aceptado como resultado correcto, no como failure.
- No hubo product delta, PR ni CI.
- Evidencia: `getLibraryIndex` requiere pinned index; `replaceLibraryIndex` depende de get+expectedMessageId; un client-only send+pin permitiría races/duplicados.
- Claim conservador: no se afirma inexistencia backend-wide; solo inexistencia en la lineage Web auditada.
- Consecuencia JOBS: 12.1 permanece abierto y el siguiente assignment amplía explícitamente el scope de AAA al control plane/backend mínimo.

### BBB / `NIGHT-BBB-012`
- `DONE` factual.
- SAME PR #60 exact head `945638c8...`; F4 matrix `33265800007`, D6 `33265800004`, D7 `33265800022`, Desktop Portability `33265800008` SUCCESS; Upgrade `33265800019` SKIPPED/no aplicable.
- Protected expected-head merge devolvió `7de7b57a508b3cf05cbded81501fbd3da63922a3`; integration reread confirmó parents exactos.
- Se procesa **artifact integrated**, no cierre total de 25.1.

### WOZ / `NIGHT-WOZ-012`
- `PENDING_CI_REFRESH` aceptado.
- SAME #61 permanece OPEN @ `aef1cd0...`.
- Integration avanzó a `7de7b57a...` por #60; compare previo mostró live delta solo F4, sin overlap semántico con los 3 files F3 de #61.
- Protected merge fue rechazado porque `Required CI` debía renovarse. Esto prueba que el verde anterior no puede autorizar la combinación nueva.
- No merge claim; 16.2 sigue abierto.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 12.1 atomic bootstrap:** blocker interno más duro. La solución correcta requiere autoridad control-plane create-if-absent/CAS/idempotency; repetir pin-only Web sería trabajo falso.
2. **F3 / 16.2:** SAME #61 es el candidate único y requiere refresh exact-head después de #60. Su integración reduce F3 a external tail + D17–D20.
3. **F4 / 25.1:** la matriz ya está integrada; el retorno ahora está en cerrar un slice funcional dependency-safe real entre los `NOT_COVERED`, no en producir otra matriz.
4. **F0/F1:** no repetir drills ni consumir workers técnicos donde solo falta evidencia externa/decisión RO.

No se conservó una asignación por inercia: AAA recibe **scope nuevo** para resolver la causa raíz de su blocker; BBB deja la transacción #60 ya completada y pasa a cobertura funcional; WOZ conserva #61 únicamente porque GitHub demuestra que sigue siendo el único candidate 16.2 y está stale por un movimiento verificable del baseline.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Nueva asignación | Objetivo |
|---|---|---|---|
| AAA | 012: BLOCKED correcto; Web-only no puede atomic create-if-absent | `NIGHT-AAA-013` | atomic bootstrap vertical slice con control-plane/backend explícitamente autorizado + Web wire |
| BBB | 012: #60 MERGED `7de7b57a...`; matrix artifact integrado | `NIGHT-BBB-013` | un slice dependency-safe de functional coverage 25.1 usando harnesses/matrix existentes |
| WOZ | 012: #61 PENDING_CI_REFRESH; old green rechazado post-#60 | `NIGHT-WOZ-013` | refresh SAME #61 sobre `7de7b57a...` + fresh exact-head CI + protected merge si race-check |

Ownership exclusivo: AAA=F2/12.1 atomic vertical slice; BBB=F4/25.1 residual funcional; WOZ=F3/16.2 SAME #61. No overlap material.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-013`
Duplicate-check backend-wide. Reutilizar primitive equivalente si existe; si no, implementar el mínimo ensure-empty-index create-if-absent/CAS/idempotent/fail-closed con autoridad server-side existente y sin nueva infra/costo, luego wire Web. Dos callers concurrentes deben producir un solo ganador; retries mismos resultados; existing no overwrite; fallo parcial no éxito falso. Exact-head obligatorio. No pagination/window/memory/cold-warm ni D13–D15.

### `NIGHT-BBB-013`
Consumir la matriz #60 integrada como source of truth. Elegir un solo journey core `NOT_COVERED` dependency-safe y producir evidencia funcional real reutilizando harnesses; no segunda matriz. Bugs F2/F3 → `PRODUCT_FINDING`, no ownership theft. No iPhone/signing/notarization/Stripe/YouTube productivo inventado; no 25.2.

### `NIGHT-WOZ-013`
REUSE SAME #61. Refresh branch sobre `7de7b57a...`, preservar exclusivamente el delta F3, exact-head CI nuevo y protected expected-head merge solo con race-check limpio. Puede usar Git-data/merge-union de la misma branch si es la forma mínima verificable; no nueva PR ni reconstrucción manual de product code. Tras merge: solo `16.2 SOFTWARE DONE / EXTERNAL TAIL`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia off-provider/off-account real + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: atomic empty-index requiere primitive control-plane real; después quedan pagination/window/memory + cold/warm residual.
6. F3/16.2: SAME #61 requiere refresh + exact-head CI nuevo; physical staging/prod y deploy real siguen externos; D17–D20 abiertos.
7. F4/25.1: matrix artifact integrado, coverage funcional incompleto; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; dos cierres externos/RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58 slice A integrado; atomic bootstrap abierto con blocker causal ya identificado y scope 013 corregido.
- **F3:** 16.1 software integrado; 16.2 candidate existente pero stale; physical tail preservado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix artifact integrado; 25.1 completo no cerrado por gaps honestos.

## PLAN SYNC

Actualizados en este ciclo:
- `!!!PLAN/Plan Maestro.md`
- `!!!PLAN/Fase 2 - Web y UX.md`
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`
- `!!!PLAN/Fase 4 - Desktop y release chain.md`
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`
- `!!!PLAN/NOCHE - AAA.md`
- `!!!PLAN/NOCHE - BBB.md`
- `!!!PLAN/NOCHE - WOZ.md`
- `!!!PLAN/NOCHE - JOBS.md`

F0/F1 no cambiaron factual y no se reescribieron. `Registro de avances.md` fue leído completo como ledger histórico; no se sustituyó con un snapshot parcial. Los estados vivos y los handoffs verificables de este ciclo quedan en Plan Maestro/fases/ledgers + Issue #41; GitHub real sigue siendo autoridad.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de todo claim.
2. Procesar 013 factual, sin asumir que alguna branch/head sigue igual.
3. Si AAA produce atomic candidate: exigir exact-head CI/race-check y cerrar solo atomic sub-slice; luego recalcular pagination/window/memory/cold-warm.
4. Si WOZ refresca #61: no reutilizar CI anterior; consumir solo CI del exact head post-`7de7b57a...` y merge protegido si corresponde.
5. Si BBB produce coverage candidate: aceptar solo los journeys efectivamente demostrados; conservar el resto de matrix gaps.
6. Mantener F0/F1/signing/physical staging/off-provider como externos hasta evidencia real.
7. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-012
INTEGRATION_HEAD: 7de7b57a508b3cf05cbded81501fbd3da63922a3
AAA: NIGHT-AAA-012 BLOCKED validly -> NIGHT-AAA-013 atomic vertical slice with explicit control-plane scope
BBB: NIGHT-BBB-012 DONE -> #60 MERGED 7de7b57a... -> NIGHT-BBB-013 dependency-safe functional coverage residual
WOZ: NIGHT-WOZ-012 PENDING_CI_REFRESH -> old green rejected after #60 -> NIGHT-WOZ-013 SAME #61 refresh + fresh exact-head CI + merge
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 012 terminado. La siguiente ejecución inicia desde GitHub vivo, no desde este snapshot si cambió.
