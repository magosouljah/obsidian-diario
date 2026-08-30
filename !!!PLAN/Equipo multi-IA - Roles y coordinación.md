# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 051

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F3 / 19.2 / SAME #76 | `NIGHT-AAA-047`: narrow refresh + canonical legal Settings reuse + fresh CI | F2/13.2 read-only gap map solo mientras #76 espera CI/review/merge |
| BBB | F4 / SAME #72 | `NIGHT-BBB-046`: narrow refresh + fresh Windows Review/Matrix/Required CI + integración exact-head | F4/25.2 read-only readiness inventory solo mientras PRIMARY espera operación externa |
| WOZ | F3 / 20.2 / REUSE #77 | `NIGHT-WOZ-050`: legitimar/reusar SAME #77 como harness PRIMARY | NONE |

**Baseline canónico CYCLE 051:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Handoffs/resultados procesados

- AAA046: no RESULTADO DEL TURNO / handoff observable; #76 head sigue `36d218609...` → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB045: no RESULTADO DEL TURNO / handoff observable; #72 head sigue `904fbf3c...` → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ049: no RESULTADO DEL TURNO / handoff observable; #77 sigue CLOSED/unmerged en `204a03fc...` → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- Último resultado aceptado WOZ: NIGHT-WOZ-048 `DONE / INTEGRATED`; #73 merge `a306e3b3...`; solo reconciliation/exception-queue software slice. Full 18.2 sigue abierto.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1 cold/warm real: runtime navegador.
- F2/13.1 Web #69: frozen/unowned por write surface.
- F2/13.1 server #70: frozen por safe-write + stale baseline.
- F2/13.2: fallback read-only de AAA047 únicamente durante espera externa del primary.
- F4/windows-auth #74: frozen; #71 espera integración real + nueva assignment.
- F4/windows-review #72: stale/diverged; owner BBB046.
- F3/18.2: #73 software slice integrated; provider/payment scenario tails abiertos.
- F3/19.2 #76: stale/diverged; owner AAA047.
- F3/20.1 #75: corrective conocido, write blocker; frozen.
- F3/20.2 #77: closed/unmerged reusable artifact; owner WOZ050; runtime target/proof sigue abierto.

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
- Worker nunca inventa fallback.
- Tras ejecutar fallback autorizado, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 051

```text
JOBS: baseline remains a306e3b3f6b4a6cf9d678e325b6e529b5344fffe
AAA046: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA047: ASSIGNED SAME #76 narrow refresh + canonical legal Settings reuse
AAA047_FALLBACK: F2/13.2 READ_ONLY only while waiting external CI/review/merge
BBB045: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB046: ASSIGNED SAME #72 narrow refresh + fresh exact-head integration transaction
BBB046_FALLBACK: F4/25.2 READ_ONLY only while waiting external operation
WOZ049: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ050: ASSIGNED REUSE SAME #77 as explicit F3/20.2 harness PRIMARY
WOZ050_FALLBACK: NONE
DUPLICATE_WORK: prevented by explicit supersede + SAME PR reuse
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 13.2 fallback audit queued.
- F3: 17.1/17.2/18.1 integrated; #73 reconciliation slice integrated; #76 active AAA047; #75 frozen; #77 active WOZ050.
- F4: windows/import integrated; windows-auth #74 holding; windows-review #72 active BBB046; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
