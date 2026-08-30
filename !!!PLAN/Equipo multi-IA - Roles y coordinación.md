# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 054

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-050`: REUSE-FIRST media streaming/memory slice mínimo sobre live integration | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review/merge |
| BBB | F4 / 25.2 | `NIGHT-BBB-049`: materializar únicamente beta backlog + test script/form/criteria faltantes reutilizando foundations/release evidence | F4/25.1 residual journey map read-only solo mientras PRIMARY espera operación externa |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-053`: SAME #78 exact-head race-check + integration; max claim HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED | NONE |

**Baseline canónico CYCLE 054:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Handoffs/resultados procesados

- AAA049: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 054 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB048: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 054 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ052: `PENDING / WAITING_CI`; abrió replacement #78 exact-base desde existing branch `50aac3f0...`, compare ahead2/behind0, dos archivos/+139, sin duplicar implementación. En preflight CYCLE 054 el CI ya materializó 13 check-runs sin failure/pending/null; `Required CI = SUCCESS`; #78 sigue OPEN/non-draft/mergeable=true, head/base unchanged.
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
- F3/18.2 external/payment/business-policy tails permanecen.
- F3/20.2 runtime capacity proof remains open even if #78 merges.
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

## Night Shift Ledger — CYCLE 054

```text
JOBS: baseline remains a306e3b3f6b4a6cf9d678e325b6e529b5344fffe
AAA049: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA050: ASSIGNED F2/14.1 minimum media streaming/memory slice
AAA050_FALLBACK: F2/14.2 READ_ONLY only while waiting external CI/review/merge
BBB048: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB049: ASSIGNED F4/25.2 missing readiness artifacts only
BBB049_FALLBACK: F4/25.1 residual journey map READ_ONLY
WOZ052: PENDING / WAITING_CI; #78 opened exact-base
WOZ053: ASSIGNED SAME #78 exact-head race-check + integration
WOZ053_FALLBACK: NONE
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA050; 14.2 conditional read-only fallback.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #76/#75 frozen; #78 green/integration assigned WOZ053.
- F4: windows/import integrated; auth/review stale candidates frozen; 25.2 active BBB049; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
