# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 067

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-063`: REUSE-FIRST media streaming/memory slice mínimo; no merge | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review |
| BBB | F3 / 20.2 | `NIGHT-BBB-062`: runtime capacity proof con target canónico 80 expected / 160 validation | F4/25.2 SAME #79 docs-only refresh + fresh CI solo durante WAITING_EXTERNAL/RUNTIME; no merge |
| WOZ | F3 / 20.1 | `NIGHT-WOZ-066`: SAME #75 exact-head merge transaction after fresh race-check | F3/18.2 read-only payment/provider scenario gap map solo mientras espera merge/review/queue equivalente |

**Baseline canónico CYCLE 067:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Handoffs/resultados procesados

- AAA062: no RESULTADO DEL TURNO / Issue #41 handoff / branch/PR/head change atribuible → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB061: no RESULTADO DEL TURNO / Issue #41 handoff / runtime evidence / artifact atribuible → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ065: no RESULTADO DEL TURNO / Issue #41 handoff / accepted merge → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- Latest Issue #41 comment before CYCLE 067 was CYCLE 066 (`5473569549`); no later worker handoff existed at preflight.
- GitHub factual: #75 remains OPEN/non-draft/mergeable at `40e39393247dbdd506ac01edefa84fd0b0add94c`, base SHA exactly `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; F3 20.1, D6, D7, Productive Temp Auth Compile and Desktop Portability exact-head workflows SUCCESS; Upgrade 21.2 Staging SKIPPED.
- #79 remains OPEN/non-draft/mergeable at `c6ec2910522370f2506beb71ad5e0fa0317d6a61`, historical base `a306e3b3...`, docs-only; stale vs live integration.
- RO/OWNER `5472774681`: F3/20.2 target remains **80 simultaneous expected / 160 validation**; not PASS.

## Serialización de integración

Integration remains #78. CYCLE 067 authorizes a single integration mutation: **WOZ/#75**. AAA does not merge. BBB062 does runtime evidence; its #79 fallback also cannot merge. WOZ fallback is read-only and cannot mutate billing/provider state.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1: cold/warm real browser runtime.
- F2/13.1 #69/#70: frozen.
- F3/18.2: reconciliation software integrated; payment/provider scenarios remain open.
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

## Night Shift Ledger — CYCLE 067

```text
JOBS: baseline 63c9f8c948b1e05c30b12378ab1f31ceb04259c2
AAA062: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA063: ASSIGNED F2/14.1 minimum media streaming/memory slice; NO MERGE
AAA063 FALLBACK: F2/14.2 READ_ONLY
BBB061: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB062: ASSIGNED F3/20.2 runtime proof @ 80 expected / 160 validation
BBB062 FALLBACK: SAME #79 refresh + fresh CI; NO MERGE
WOZ065: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ066: ASSIGNED SAME #75 exact-head merge transaction; only integration mutation authorized
WOZ066 FALLBACK: F3/18.2 READ_ONLY scenario map
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```
