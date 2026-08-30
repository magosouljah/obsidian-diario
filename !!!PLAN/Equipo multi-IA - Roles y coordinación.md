# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 053

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-049`: REUSE-FIRST media streaming/memory slice mínimo sobre live integration | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review/merge |
| BBB | F4 / 25.2 | `NIGHT-BBB-048`: materializar únicamente beta backlog + test script/form/criteria faltantes reutilizando foundations/release evidence | F4/25.1 residual journey map read-only solo mientras PRIMARY espera operación externa |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-052`: una replacement PR autorizada desde existing branch `50aac3f0...` si fresh compare sigue narrow/exact-base | NONE |

**Baseline canónico CYCLE 053:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Handoffs/resultados procesados

- AAA048: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 053; #76 head sigue `36d218609...` → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB047: `WAITING_EXTERNAL / STOP_MERGE_FLOW_UNAVAILABLE`; #72 permanece `904fbf3c...` sobre snapshot stale. No fresh CI/merge. Su fallback F4/25.2 completó inventario read-only: design foundations/component artifacts EXISTS; complete design-freeze PARTIAL; beta backlog GAP; beta script/form/criteria GAP.
- WOZ051: no RESULTADO DEL TURNO / replacement PR observable antes de CYCLE 053; source branch sigue siendo el único artifact conocido → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- Último resultado integrado aceptado: NIGHT-WOZ-048 → #73 merge `a306e3b3...`; solo reconciliation/exception-queue software slice.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1: cold/warm real browser runtime.
- F2/13.1 #69: frozen por write surface; #70 frozen safe-write + stale.
- F3/19.2 #76: stale; frozen hasta safe history-preserving refresh.
- F3/20.1 #75: frozen por corrective/write flow.
- F4/windows-auth #74/#71: frozen por integration/refresh dependency.
- F4/windows-review #72: frozen por falta de safe update-branch/history-preserving refresh.
- F3/18.2 y 20.2: external/runtime/business-policy tails permanecen.
- F4 D22/D23 y parte de 25.1: external/not-covered.

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
- Tras fallback, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 053

```text
JOBS: baseline remains a306e3b3f6b4a6cf9d678e325b6e529b5344fffe
AAA048: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA049: ASSIGNED F2/14.1 minimum media streaming/memory slice
AAA049_FALLBACK: F2/14.2 READ_ONLY only while waiting external CI/review/merge
BBB047: WAITING_EXTERNAL / STOP_MERGE_FLOW_UNAVAILABLE; #72 frozen
BBB047_FALLBACK: 25.2 inventory completed read-only; backlog + beta script/form/criteria GAP
BBB048: ASSIGNED F4/25.2 missing readiness artifacts only
BBB048_FALLBACK: F4/25.1 residual journey map READ_ONLY
WOZ051: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ052: ASSIGNED one authorized replacement PR from existing #77 branch
WOZ052_FALLBACK: NONE
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA049; 14.2 conditional read-only fallback.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #76/#75 frozen; 20.2 continuation active WOZ052.
- F4: windows/import integrated; auth/review stale candidates frozen; 25.2 active BBB048; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
