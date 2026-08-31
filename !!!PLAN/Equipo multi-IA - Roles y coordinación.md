# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 058

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-054`: REUSE-FIRST media streaming/memory slice mínimo sobre live integration | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review/merge |
| BBB | F4 / 25.2 | `NIGHT-BBB-053`: SAME #79 narrow refresh + fresh exact-head CI + race-clean integration | F4/25.1 Web/auth read-only map solo durante WAITING_CI/review/merge |
| WOZ | F3 / 20.1 | `NIGHT-WOZ-057`: SAME #75 corrective immutable pins + history-preserving refresh; no merge this cycle | F3/20.2 read-only residual capacity gap map solo durante WAITING_CI |

**Baseline canónico CYCLE 058:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Handoffs/resultados procesados

- AAA053: no RESULTADO DEL TURNO / Issue #41 handoff verificable antes de CYCLE 058 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB052: no RESULTADO DEL TURNO / Issue #41 handoff verificable antes de CYCLE 058 → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ056: no handoff estructurado observable, pero GitHub real prueba PR #78 MERGED exact-head `50aac3f0...` como `63c9f8c9...` → accepted `DONE / INTEGRATED`, claim máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.

## Serialización de integración

PR #78 movió el baseline. #79 quedó divergido (`ahead 1 / behind 3`) y requiere refresh + fresh CI. CYCLE 058 autoriza una sola mutación de integration: **BBB/#79**. WOZ puede preparar #75 pero no mergearlo; AAA tampoco compite por integration hasta un próximo ciclo/race-check.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1: cold/warm real browser runtime.
- F2/13.1 #69: frozen por write surface; #70 frozen safe-write + stale.
- F3/19.2 #76: stale/frozen.
- F3/20.2: harness integrated; runtime capacity proof + durable waitlist remain.
- F4/windows-auth #74/#71: frozen.
- F4/windows-review #72: frozen.
- F4/25.1: Web/auth y múltiples journeys siguen NOT_COVERED.
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
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL/merge-review-queue equivalente.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Worker nunca inventa fallback.
- Tras fallback, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 058

```text
JOBS: baseline 63c9f8c948b1e05c30b12378ab1f31ceb04259c2
AAA053: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA054: ASSIGNED F2/14.1 minimum media streaming/memory slice
AAA054_FALLBACK: F2/14.2 READ_ONLY only while waiting external CI/review/merge
BBB052: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB053: ASSIGNED SAME #79 refresh + fresh CI + only integration mutation authorized
BBB053_FALLBACK: F4/25.1 WEB_AUTH READ_ONLY only while waiting external operation
WOZ056: GITHUB-VERIFIED DONE/INTEGRATED #78 -> 63c9f8c9...
WOZ057: ASSIGNED SAME #75 corrective + refresh; NO MERGE this cycle
WOZ057_FALLBACK: F3/20.2 READ_ONLY residual capacity gap map
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA054.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #78 harness integrated; #75 active WOZ057; #76 frozen.
- F4: windows/import integrated; auth/review frozen; #79 refresh/integration active BBB053; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
