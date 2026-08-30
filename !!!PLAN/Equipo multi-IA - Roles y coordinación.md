# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 045

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F4 / SAME #74 | `NIGHT-AAA-041`: race-check + integración de #74 usando exact-head green; no #71 todavía | `NONE` |
| BBB | F4 / SAME #72 | `NIGHT-BBB-040`: atribuir/corregir matrix-contract post-promotion; fresh gates + merge solo si verde | F4/25.2 read-only readiness inventory solo si PRIMARY entra WAITING_CI |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-044`: REUSE-FIRST capacity/load readiness audit-only; no #73/#75 writes | `NONE` |

**Baseline canónico CYCLE 045:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Handoffs procesados

- AAA040: no RESULTADO DEL TURNO/handoff nuevo observable. #74 sigue OPEN/Ready, exact head `14dfba52...`, base `a9d35a3d...`, D6/D7/Required CI verdes. 040 queda `NOT_PROCESSED / SUPERSEDED_BY_JOBS`; AAA041 reemite la transacción para impedir ejecución tardía duplicada.
- BBB039: no RESULTADO DEL TURNO/handoff nuevo observable. #72 sigue OPEN/Ready @ `56dc4adf...`; Review/Import/Required CI verdes y F4 Matrix `33324512174` rojo en `Validate dependency-safe matrix contract`. 039 queda `NOT_PROCESSED / SUPERSEDED_BY_JOBS`; BBB040 reemite attribution-first.
- WOZ043: `BLOCKED / WRITE_TOOL_SAFETY`. #75 quedó unchanged @ `bb493b37...`; el corrective exacto de dos immutable Action pins fue verificado pero la escritura fue bloqueada antes de aceptación. Sin fresh head/CI/merge; Issue #41 `5470266322`. Reintentar lo mismo sin cambio del blocker sería duplicación, por lo que WOZ pasa a 20.2 audit-only.

## Holding / blocked items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: holding/stale; coordinator probado, wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #71: regression proof; espera #74 integrado + nueva asignación explícita.
- F3/18.2 #73 @ `fc831172...`: exact-head verde/mergeable, pero `MERGE_FLOW_UNAVAILABLE`; no duplicar ni recrear.
- F3/20.1 #75 @ `bb493b37...`: pin corrective conocido, pero `WRITE_TOOL_SAFETY`; frozen hasta cambio factual del write flow.
- F3/20.2: gap map read-only asignado a WOZ044; no PASS claim.

## Reglas

1. Trabajo cross-phase solo si dependencias reales lo permiten.
2. Una pieza material = un owner.
3. Owner hace preflight → implementation/audit → tests → CI → handoff.
4. Findings no transfieren ownership automáticamente; JOBS lo hace explícitamente.
5. No hopping automático.
6. Bloqueo real → JOBS reasigna explícitamente.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
8. Ningún `[x]` sin evidencia.
9. REUSE-FIRST + duplicate-check obligatorios.
10. Cambio material de baseline/head → refresh + CI aplicable antes de integración.

## PRIMARY / CI-FALLBACK

- PRIMARY siempre primero.
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Si no existe fallback seguro: `CI-FALLBACK: NONE`.
- Worker nunca inventa fallback.
- Tras ejecutar un fallback autorizado, el worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 045

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA040: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA041: ASSIGNED SAME #74 integration transaction
BBB039: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB040: ASSIGNED SAME #72 matrix-contract attribution/corrective
BBB040_FALLBACK: F4/25.2 READ_ONLY only while WAITING_CI
WOZ043: BLOCKED / WRITE_TOOL_SAFETY; #75 unchanged
WOZ044: ASSIGNED F3/20.2 READ_ONLY capacity/load audit
DUPLICATE_WORK: prevented by superseding 040/039 and freezing #75/#73
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 holding/frozen.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 ready but merge-flow blocked; 20.1 #75 write-tool blocked; 20.2 audit-only activo.
- F4: windows/import integrated; windows/auth #74 exact-head green pendiente integración; windows/review #72 dedicated green pero matrix-contract red; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
