# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 046

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / SAME #69 | `NIGHT-AAA-042`: refresh + wiring productivo Save All; fresh focused tests/CI | `NONE` |
| BBB | F4 / SAME #72 | `NIGHT-BBB-041`: race-check + integración exact-head green | F4/25.2 read-only readiness inventory solo si PRIMARY espera operación externa de merge/review/queue |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-045`: REUSE-FIRST capacity/load readiness audit-only; no #73/#75 writes | `NONE` |

**Baseline canónico CYCLE 046:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Handoffs procesados

- AAA041: `PENDING / STOP_MERGE_FLOW_BLOCKED`. #74 sigue OPEN/Ready/mergeable @ `14dfba52...`, exact-head green; merge expected-head bloqueado antes de mutación. #74 frozen; #71 espera integración real.
- BBB040: `WAITING_CI -> PASS_RESOLVED_BY_JOBS_RECHECK`. #72 final head `904fbf3c...`; Windows Review/F4 Matrix/D6/D7/Required CI/Windows Import SUCCESS; Upgrade skipped. BBB041 integra solo si race-clean.
- WOZ044: no RESULTADO DEL TURNO/handoff observable antes de CYCLE 046; `NOT_PROCESSED / SUPERSEDED_BY_JOBS`. WOZ045 reemite la misma auditoría read-only para impedir late duplicate.

## Holding / blocked items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: owner AAA042; stale base, wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #74: exact-head green/mergeable pero `MERGE_FLOW_BLOCKED`; frozen. #71 espera integración real + nueva asignación.
- F3/18.2 #73 @ `fc831172...`: exact-head green/mergeable, `MERGE_FLOW_UNAVAILABLE`; no duplicar.
- F3/20.1 #75 @ `bb493b37...`: pin corrective conocido, `WRITE_TOOL_SAFETY`; frozen.
- F3/20.2: audit read-only asignado a WOZ045; no PASS claim.

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
- Tras ejecutar un fallback autorizado, el worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 046

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA041: PENDING / STOP_MERGE_FLOW_BLOCKED; #74 unchanged
AAA042: ASSIGNED SAME #69 refresh + product wiring
BBB040: WAITING_CI -> PASS_RESOLVED_BY_JOBS_RECHECK
BBB041: ASSIGNED SAME #72 integration transaction
BBB041_FALLBACK: F4/25.2 READ_ONLY only while waiting external merge/review/queue
WOZ044: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ045: ASSIGNED F3/20.2 READ_ONLY capacity/load audit
DUPLICATE_WORK: prevented by freezing #74/#73/#75 and superseding 044
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69 activo con AAA042; #70 frozen.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 merge-flow blocked; 20.1 #75 write-tool blocked; 20.2 audit-only activo.
- F4: windows/import integrated; windows/auth #74 green but merge-flow blocked; windows/review #72 exact-head fully green pending integration; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
