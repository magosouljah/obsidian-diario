# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 063

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-059`: REUSE-FIRST media streaming/memory slice mínimo; no merge | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review |
| BBB | F3 / 20.2 | `NIGHT-BBB-058`: runtime capacity proof con target canónico 80 expected / 160 validation | F4/25.2 SAME #79 docs-only refresh + fresh CI solo durante WAITING_EXTERNAL/RUNTIME; no merge |
| WOZ | F3 / 20.1 | `NIGHT-WOZ-062`: SAME #75 exact-head merge transaction after fresh race-check | NONE |

**Baseline canónico CYCLE 063:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Handoffs/resultados procesados

- AAA058: no RESULTADO DEL TURNO / Issue #41 handoff / branch/PR/head change → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB057: no RESULTADO DEL TURNO / Issue #41 handoff / runtime evidence / artifact → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ061: no RESULTADO DEL TURNO / Issue #41 handoff / accepted merge → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- GitHub factual: #75 remains OPEN/non-draft/mergeable at `40e39393247dbdd506ac01edefa84fd0b0add94c`, base SHA exactly `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`, 4 files; applicable exact-head workflows are complete/green.
- #79 remains OPEN/non-draft/mergeable at `c6ec2910522370f2506beb71ad5e0fa0317d6a61`, historical base `a306e3b3...`, exactly one docs-only file.
- RO/OWNER `5472774681`: F3/20.2 target remains **80 simultaneous expected / 160 validation**; not PASS.

## Serialización de integración

Integration remains #78. CYCLE 063 authorizes a single integration mutation: **WOZ/#75**. AAA does not merge. BBB058 does runtime evidence; its #79 fallback also cannot merge.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1: cold/warm real browser runtime.
- F2/13.1 #69/#70: frozen.
- F3/19.2 #76: stale/frozen.
- F3/20.1: #75 integration transaction pendiente; external observability tails remain after software integration.
- F3/20.2: target 80/160 fixed; runtime 160 + latency/error/queue/recovery + safety margin + durable user waitlist faltan.
- F4/windows-auth #74/#71: frozen.
- F4/windows-review #72: frozen.
- F4/25.1: Web/auth and multiple journeys remain NOT_COVERED.
- F4/25.2: #79 stale; fallback preparation only.
- F4 D22/D23: signing/notarization/hardware externos.

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
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL/merge-review equivalente.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Worker nunca inventa fallback.
- Tras fallback, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 063

```text
JOBS: baseline 63c9f8c948b1e05c30b12378ab1f31ceb04259c2
AAA058: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA059: ASSIGNED F2/14.1 minimum media streaming/memory slice; NO MERGE
BBB057: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB058: ASSIGNED F3/20.2 runtime proof @ 80 expected / 160 validation
BBB058 FALLBACK: SAME #79 refresh + fresh CI; NO MERGE
WOZ061: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ062: ASSIGNED SAME #75 exact-head merge transaction; only integration mutation authorized
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA059.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #78 harness integrated; target 80/160 approved; #75 exact-base/exact-head green but unmerged, active WOZ062.
- F4: windows/import integrated; auth/review frozen; #79 fallback-only; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
