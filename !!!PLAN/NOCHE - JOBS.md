# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 017 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`.
- Branch reread: #64 sigue siendo el último merge de integración; no hubo avance de baseline durante este ciclo JOBS.
- Release público: 🔴 `NO-GO`.
- F0: 1.2 y 2.2 tails externos/administrativos; trabajo técnico interno habilitante ya cerrado.
- F1: D6/D7/D8/D9 PASS; D10.1 external-only por off-provider/off-account copy + read/checksum; D10.2 decisión RO.
- F2: #66 es progreso real pero incompleto; no se promueve a DONE ni se autoriza merge.
- F3: #65 sigue OPEN/Ready/mergeable y exact-head verde; merge aún no ejecutado.
- F4: #63 sigue OPEN/Ready/mergeable; Windows Import continúa rojo por runner bootstrap.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-017`
- PR #66 `aaa/night-12.1-pagination-windowing` @ `c9b5cd95ad5b6b4d8f681265992e44d8c777a76f`, base `b114111caf...`, OPEN/mergeable.
- Candidate ya limita first-load a 240 rich `Beat` objects, añade `loadWebLibraryPage(offset/pageSize)` y test sintético 10,321 beats.
- Gate incompleto: no consumer next/previous/cursor, refresh/invalidation, no-duplicate/no-omission end-to-end, rendered-card bound ni proxy CPU/network/memory final.
- D6 `33277332289` SUCCESS; D7 `33277332325` SUCCESS; Upgrade `33277332283` SKIPPED; Desktop Portability `33277332334` seguía IN_PROGRESS al preflight.
- Resultado procesado: `PENDING`; DO NOT MERGE.

### BBB / `NIGHT-BBB-016`
- No apareció resultado ejecutado nuevo del worker.
- GitHub real conserva #63 @ `8768856ff8ea15c7fa164e4b433abccf02852fb1`, base `b114111caf...`, OPEN/Ready/mergeable.
- F4 Matrix/D6/D7/Desktop Portability exact-head siguen SUCCESS; Windows Import `33276125806` sigue FAILURE por EdgeDriver/Tauri Driver/WDIO session bootstrap.
- `windows/import` permanece `NOT_COVERED`.
- JOBS supersede 016 before execution y emite 017 únicamente porque el mismo blocker vuelve a estar en el camino crítico fresh.

### WOZ / `NIGHT-WOZ-016`
- No apareció resultado ejecutado nuevo del worker.
- #65 @ `e65538640581f3f986748968db1f4dfb069c2579`, base `b114111caf...`, sigue OPEN/Ready/mergeable.
- F3 17.1 `33276769749`, Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` = SUCCESS; Upgrade `33276769715` SKIPPED/no aplicable.
- No merge, por lo tanto 17.1 sigue `SOFTWARE CANDIDATE GREEN / NOT INTEGRATED`.
- JOBS supersede 016 before execution y emite 017 porque #65 sigue siendo el cierre interno inmediato más barato.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 / 17.1 #65:** candidate exact-head green; depende solo de race-check/merge del owner.
2. **F2 / 12.1 #66:** mayor blocker interno activo F2; bounded primitive parcial necesita consumer windowing/evidence real.
3. **F4 / 25.1 #63:** functional gate rojo por runner bootstrap; arreglo F4 acotado puede convertir Windows/import en evidencia literal.
4. **F0/F1:** blockers actuales son externos/RO; repetir drills o crear infraestructura falsa no aporta progreso legítimo.

No se conservaron asignaciones por inercia: AAA continúa #66 porque hubo progreso material; BBB/WOZ reciben IDs nuevos tras supersede explícito de órdenes no ejecutadas y porque esas mismas piezas volvieron a resultar críticas al recálculo fresh.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Nueva asignación | Objetivo |
|---|---|---|---|
| AAA | 017 PENDING — #66 parcial/incompleto | `NIGHT-AAA-018` | SAME #66 consumer windowing + refresh/no-dup/no-omission + bounded evidence + exact-head |
| BBB | 016 sin ejecución; #63 sigue rojo funcional | `NIGHT-BBB-017` | SAME #63 minimal runner bootstrap fix + fresh Windows Import PASS/exact-head CI |
| WOZ | 016 sin ejecución; #65 exact-head all applicable green | `NIGHT-WOZ-017` | SAME #65 race-check + protected merge; cerrar solo 17.1 software slice |

Ownership exclusivo: AAA=F2/12.1 #66; BBB=F4/25.1 #63; WOZ=F3/17.1 #65. No overlap material.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-018`
SAME #66. Completar consumer navigation/windowing, refresh/invalidation, no duplicados/omisiones y evidencia bounded medible. No D13–D15. Merge solo con exact-head verde y race-check.

### `NIGHT-BBB-017`
SAME #63. Corregir únicamente EdgeDriver/Tauri Driver/WDIO session bootstrap; fresh Windows Import exact-head. `AUTOMATED_PASS` solo con PASS literal. No segundo slice/25.2.

### `NIGHT-WOZ-017`
SAME #65 @ `e6553864...`. Exact-head aplicable observado verde. Race-check/merge solo si head/base siguen exactos y compatibles. Tras merge declarar únicamente `17.1 SOFTWARE DONE / INTEGRATED`. No 17.2 en este ID.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia off-provider/off-account real + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: SAME #66 consumer windowing/evidence + cold/warm residual; D13–D15 aún abiertos después.
6. F3: #65 merge pendiente; luego 17.2–20; 16.x physical/deploy tails externos.
7. F4/25.1: #63 functional red por runner bootstrap; otros coverage gaps; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58 + #64 integrados; #66 partial candidate; 12.1 residual activo; D13–D15 abiertos.
- **F3:** 16.1 y 16.2 software integrados con tails externos; 17.1 candidate exact-head green pero no integrado; 17.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 funcional todavía rojo por bootstrap; 25.1/25.2 abiertos; D22/D23 externos.

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

Leídos completos/preflight: Plan Maestro; Fases 0–4; roles; protocolo; cuatro ledgers nocturnos; Registro de avances por tramos; Issue #41 body + comments; GitHub vivo. `Registro de avances.md` no se reescribió porque este ciclo no produjo merge/gate nuevo; el progreso parcial #66 queda documentado en Plan/F2/JOBS/Issue.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar únicamente resultados nuevos `AAA-018`, `BBB-017`, `WOZ-017`.
3. Si WOZ integra #65, registrar merge SHA/parents y promover solo 17.1 SOFTWARE; después recalcular 17.2.
4. Si BBB logra Windows Import PASS, promover únicamente `windows/import`; conservar el resto de gaps 25.1.
5. Si AAA completa #66, verificar que no sea render-only sobre un global full-library buffer y exigir exact-head green antes de integración.
6. Mantener F0/F1/signing/physical staging/off-provider como externos hasta evidencia real.
7. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-017
INTEGRATION_HEAD: b114111cafb29b4aa50cdce014059c66a75bddf2
AAA: 017 PENDING -> #66 c9b5cd95 partial bounded paging, consumer evidence incomplete -> NIGHT-AAA-018 SAME #66
BBB: 016 unexecuted -> #63 8768856f Windows Import 33276125806 FAILURE unchanged -> superseded -> NIGHT-BBB-017
WOZ: 016 unexecuted -> #65 e6553864 all applicable exact-head CI SUCCESS, no merge -> superseded -> NIGHT-WOZ-017
DUPLICATE_WORK: none; #62 remains closed/not merged; SAME #66/#63/#65 reused
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 017 terminado. La siguiente ejecución inicia desde GitHub vivo, no desde este snapshot si cambió.
