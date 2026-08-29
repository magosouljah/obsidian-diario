# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 013 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`.
- GitHub reread confirma que sigue siendo merge de PR #60; no hubo nueva integración durante este ciclo JOBS.
- Release público: 🔴 `NO-GO`.
- F0: 1.2 y 2.2 tails externos/administrativos; no hay slice técnico nocturno de mayor retorno.
- F1: D6/D7/D8/D9 PASS; D10.1 external-only por off-provider/off-account copy + read/checksum; D10.2 RO.
- F2: #64 existe/mergeable pero su exact-head Required CI/Test Desktop Portability `33271187072` terminó FAILURE. Tests focales atomic bootstrap quedaron UNVERIFIED en AAA-013. No merge/no PASS.
- F3: #61 refreshed exact head `d254b294cf8fe78d93025271360dd73ed594898f`, OPEN/Ready/mergeable=true; Required CI `33271019389` SUCCESS y D6 `33271019493` SUCCESS; no failure/in-progress exact-head observado. No integración reclamada: owner transaction pendiente.
- F4: #63 exact head `65a7bf07029babfb500d3913226ec8a5ca6e0deb`, OPEN/Ready/mergeable. Required CI `33271091123` SUCCESS, pero Windows import functional journey `33271091186` terminó FAILURE en el harness existente. No merge/no functional PASS.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-013`
- Resultado del worker: `PENDING`, PR #64 OPEN/Ready/NOT MERGED @ `86ea14ad...`.
- Candidate reutilizó advisory locks PostgreSQL + `commitIndexCopyOnWrite`; añadió `/transport/index/ensure`, Web wire y tests de race/retry/existing/provider/pointer-failure.
- El handoff dejó ejecución de tests focales y CI final como UNVERIFIED.
- GitHub posterior resolvió el CI de forma negativa: run `33271187072` FAILURE exact-head. Jobs visibles: Web+shared Chrome smoke FAILURE; Portable Windows FAILURE; native macOS arm64/x86_64 FAILURE.
- Consecuencia: no se promueve atomic bootstrap; SAME #64 pasa a corrective assignment 014.

### BBB / `NIGHT-BBB-013`
- Resultado del worker: `PENDING`, PR #63 OPEN/Ready/mergeable @ `65a7bf070...`.
- Reutilizó `test:e2e:import` y añadió únicamente workflow Windows + promotion condicionada en la matriz.
- Required CI amplio terminó SUCCESS, pero el gate literal creado para esta cobertura `33271091186` terminó FAILURE en `Run existing Windows import E2E harness`.
- Consecuencia: `windows/import` sigue no demostrado; la matriz no se promueve falsamente; SAME #63 recibe corrective 014.
- Duplicate-check: PR #62 quedó CLOSED/NOT MERGED y no se reabre.

### WOZ / `NIGHT-WOZ-013`
- Resultado del worker: `PENDING_CI`, SAME #61 refreshed a `d254b294...` preservando solo delta F3/16.2 sobre `7de7b57a...`.
- GitHub posterior: PR OPEN/Ready/mergeable=true; Required CI exact-head `33271019389` SUCCESS; D6 `33271019493` SUCCESS; no failure/in-progress exact-head observado.
- Consecuencia: blocker CI quedó resuelto; candidate pasa a owner race-check/protected merge bajo 014. JOBS no bypassa la integración técnica del owner.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 12.1 #64 exact-head red:** candidate existe, pero el gate amplio falló y sus tests focales siguen sin ejecución demostrada. Resolver ese failure es el movimiento interno más crítico antes de abrir más slices F2.
2. **F3 / 16.2 #61 exact-head green:** retorno inmediato máximo; el owner puede integrar si race-check sigue limpio. Si otro merge mueve baseline antes, debe refresh + fresh CI.
3. **F4 / 25.1 #63 functional red:** la evidencia negativa real tiene prioridad sobre empezar otra cobertura. Fix mínimo o PRODUCT_FINDING; ningún false PASS.
4. **F0/F1:** blockers activos son externos/RO; no repetir drills ni consumir workers técnicos.

Las nuevas asignaciones no se conservaron por inercia. Cada candidate fue revaluado desde GitHub actual: AAA permanece por failure real #64; BBB permanece por failure real #63; WOZ permanece porque #61 cambió de PENDING_CI a integration-ready subject to race-check.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Nueva asignación | Objetivo |
|---|---|---|---|
| AAA | 013: #64 candidate, CI final FAILURE | `NIGHT-AAA-014` | SAME #64: causa mínima/fix atribuible + ejecutar focal tests + fresh exact-head CI; merge solo si verde |
| BBB | 013: #63 candidate; Required CI green pero functional journey FAILURE | `NIGHT-BBB-014` | SAME #63: resolver gate Windows/import; no false matrix PASS ni segundo slice |
| WOZ | 013: #61 refreshed; exact-head CI ahora green/mergeable | `NIGHT-WOZ-014` | SAME #61 race-check + protected merge; refresh/fresh CI si baseline cambia |

Ownership exclusivo: AAA=F2/12.1 #64; BBB=F4/25.1 #63; WOZ=F3/16.2 #61. No overlap material.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-014`
REUSE SAME #64. Procesar `33271187072` FAILURE sin esconderlo tras D6/D7 verdes. Verificar los tests atomic bootstrap añadidos. Fix solo atribuible al slice; finding ajeno → reportar. Fresh exact-head CI tras cambios/baseline movement. Integrar únicamente con tests + applicable CI green + race-check. Cerrar solo atomic sub-slice, no 12.1 entero.

### `NIGHT-BBB-014`
REUSE SAME #63. `33271091186` functional FAILURE manda aunque Required CI sea green. Diagnosticar/fijar solo workflow/glue/harness F4; bug producto → PRODUCT_FINDING. No promover matrix windows/import hasta PASS exact-head. No segundo slice/25.2.

### `NIGHT-WOZ-014`
REUSE SAME #61. Si integration sigue `7de7b57a...`, race-check + protected expected-head merge de `d254b294...`; si baseline se mueve, refresh SAME #61 + fresh applicable CI. Tras merge reclamar solo 16.2 SOFTWARE DONE / EXTERNAL TAIL. Después solo audit READ-ONLY de 17.1 si hay tiempo, sin implementar Stripe sin nueva orden.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia off-provider/off-account real + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: #64 exact-head CI FAILURE + focal tests unverified; después quedan pagination/window/memory + cold/warm residual.
6. F3/16.2: owner merge transaction; physical staging/prod y deploy real siguen externos; D17–D20 abiertos.
7. F4/25.1: #63 Windows/import functional FAILURE; otros coverage gaps; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; dos cierres externos/RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58 slice A integrado; atomic bootstrap candidate existe pero está rojo y no integrado; D13–D15 abiertos.
- **F3:** 16.1 software integrado; 16.2 candidate verde a nivel exact-head y pendiente transacción owner; physical tail + D17–D20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; matrix #60 integrada; #63 reveló failure funcional real; 25.1/25.2 siguen abiertos; D22/D23 externos.

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

F0/F1 no cambiaron factual y no se reescribieron. `Registro de avances.md` se leyó completo por tramos; no se reescribe porque este ciclo no produjo un nuevo merge/gate cerrado y los findings/candidates vivos quedan en Plan/fases/ledgers + Issue #41.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar resultados 014, no snapshots 013.
3. Si WOZ integra #61, registrar merge SHA exacto y 16.2 SOFTWARE DONE / EXTERNAL TAIL; después recalcular 17.1 software-only vs blockers externos.
4. Si AAA corrige #64, exigir focal tests + applicable exact-head green; tras merge cerrar solo atomic sub-slice y recalcular pagination/window/memory/cold-warm.
5. Si BBB corrige #63, aceptar Windows/import solo con run funcional exact-head PASS; conservar todos los demás gaps.
6. Mantener F0/F1/signing/physical staging/off-provider como externos hasta evidencia real.
7. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-013
INTEGRATION_HEAD: 7de7b57a508b3cf05cbded81501fbd3da63922a3
AAA: NIGHT-AAA-013 PENDING -> #64 exact-head Required CI FAILURE -> NIGHT-AAA-014 SAME #64 corrective
BBB: NIGHT-BBB-013 PENDING -> #63 functional Windows import FAILURE -> NIGHT-BBB-014 SAME #63 corrective
WOZ: NIGHT-WOZ-013 PENDING_CI -> #61 exact-head CI green/mergeable -> NIGHT-WOZ-014 owner race-check + protected merge
DUPLICATE_WORK: PR #62 CLOSED/NOT MERGED; no active duplicate
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 013 terminado. La siguiente ejecución inicia desde GitHub vivo, no desde este snapshot si cambió.
