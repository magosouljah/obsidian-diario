# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 048

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-044`: read-only gap map + minimum slices para ReviewShell Import/Edit/Bulk y coverage | `NONE` |
| BBB | F4 / SAME #72 | `NIGHT-BBB-043`: race-check + integración exact-head green | F4/25.2 read-only readiness inventory solo si PRIMARY espera merge/review/queue externo |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-047`: harness parametrizable de capacidad/carga; sin claim 2× ni provider/infra load | `NONE` |

**Baseline canónico CYCLE 048:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Handoffs procesados

- AAA043: `PENDING / STOP_WRITE_SURFACE`; #69 unchanged. Refresh/product wiring requiere superficie patch-capable; fallback no elegible. #69 queda frozen/unowned.
- BBB042: no RESULTADO DEL TURNO/handoff observable antes de CYCLE 048; `NO_RESULT / SUPERSEDED_BY_JOBS`. #72 sigue open/unmerged y exact-head evidence conocida verde.
- WOZ046: no RESULTADO DEL TURNO/handoff observable antes de CYCLE 048; `NO_RESULT / SUPERSEDED_BY_JOBS`. 20.2 sigue abierto.

## Holding / blocked items

- F2/12.1 cold/warm real: runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: frozen/unowned por write surface.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #74 @ `14dfba52...`: candidate green/mergeable pero merge-flow blocker previo; frozen. #71 espera integración real + nueva assignment.
- F4/windows-review #72 @ `904fbf3c...`: exact-head green conocido; owner BBB043.
- F3/18.2 #73 @ `fc831172...`: software slice ready/mergeable, no merge verificable; frozen.
- F3/20.1 #75 @ `bb493b37...`: corrective conocido, previous write-tool blocker; frozen.
- F3/20.2: harness software asignado WOZ047; runtime/target siguen abiertos.

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
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL/merge-review-queue equivalente.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Si no existe fallback seguro: `CI-FALLBACK: NONE`.
- Worker nunca inventa fallback.
- Tras ejecutar fallback autorizado, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 048

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA043: PENDING / STOP_WRITE_SURFACE; #69 frozen
AAA044: ASSIGNED F2/13.2 READ_ONLY gap map; FALLBACK NONE
BBB042: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB043: ASSIGNED SAME #72 exact-head integration transaction
BBB043_FALLBACK: F4/25.2 READ_ONLY only while waiting external merge/review/queue
WOZ046: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ047: ASSIGNED F3/20.2 parameterized capacity harness
DUPLICATE_WORK: prevented by explicit supersede + frozen blocked PRs
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 13.2 audit activo AAA044.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 holding; 20.1 #75 blocked; 20.2 harness software activo WOZ047.
- F4: windows/import integrated; windows/auth #74 holding; windows/review #72 pending BBB043 integration; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
