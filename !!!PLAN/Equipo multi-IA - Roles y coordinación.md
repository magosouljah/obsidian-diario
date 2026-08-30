# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 057

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-053`: REUSE-FIRST media streaming/memory slice mínimo sobre live integration | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review/merge |
| BBB | F4 / 25.1 Web/auth | `NIGHT-BBB-052`: dedicated Web/auth journey; consume BBB049 residual map, prefer harness/tests, no #79 merge this turn | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-056`: SAME #78 exact-head race-check + integration; max claim HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED | NONE |

**Baseline canónico CYCLE 057:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Handoffs/resultados procesados

- AAA052: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 057 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB051: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 057 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ055: no RESULTADO DEL TURNO / Issue #41 handoff observable antes de CYCLE 057 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- #78 continúa OPEN/non-draft/mergeable exact-base en `50aac3f0...`; #79 continúa OPEN/non-draft/mergeable exact-base en `c6ec2910...`.
- Último resultado integrado aceptado: NIGHT-WOZ-048 → #73 merge `a306e3b3...`; solo reconciliation/exception-queue software slice.

## Serialización de integración

#78 y #79 siguen sobre el mismo baseline exacto `a306e3b3...`. CYCLE 057 autoriza una sola mutación de integration: WOZ/#78. #79 queda `HOLD_GREEN_PENDING_SERIAL_INTEGRATION`; tras cualquier movimiento del baseline debe reconciliarse + fresh CI antes de merge.

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
- F4 D22/D23 y la mayoría de 25.1: external/not-covered.
- F4/25.2 #79: internal artifact green/mergeable but not integrated; external beta/tester evidence remains.

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

## Night Shift Ledger — CYCLE 057

```text
JOBS: baseline a306e3b3f6b4a6cf9d678e325b6e529b5344fffe
AAA052: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA053: ASSIGNED F2/14.1 minimum media streaming/memory slice
AAA053_FALLBACK: F2/14.2 READ_ONLY only while waiting external CI/review/merge
BBB051: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB052: ASSIGNED F4/25.1 Web/auth dedicated journey; #79 HOLD_GREEN_PENDING_SERIAL_INTEGRATION
BBB052_FALLBACK: NONE
WOZ055: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ056: ASSIGNED SAME #78 exact-head race-check + integration; only integration mutation authorized this cycle
WOZ056_FALLBACK: NONE
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA053; 14.2 conditional read-only fallback.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #76/#75 frozen; #78 integration assigned WOZ056.
- F4: windows/import integrated; auth/review stale candidates frozen; #79 green hold; 25.1 Web/auth active BBB052; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
