# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 060

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-056`: REUSE-FIRST media streaming/memory slice mínimo; no merge CYCLE 060 | F2/14.2 read-only player-control gap map solo mientras PRIMARY espera CI/review |
| BBB | F4 / 25.2 | `NIGHT-BBB-055`: SAME #79 narrow refresh + fresh exact-head CI; no merge CYCLE 060 | F4/25.1 Web/auth read-only map solo durante WAITING_CI/review |
| WOZ | F3 / 20.1 | `NIGHT-WOZ-059`: SAME #75 exact-head race-check + integration | NONE |

**Baseline canónico CYCLE 060:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Handoffs/resultados procesados

- AAA055: no RESULTADO DEL TURNO / Issue #41 handoff / artifact verificable → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- BBB054: no RESULTADO DEL TURNO / Issue #41 handoff / #79 head change verificable → `NO_RESULT / SUPERSEDED_BY_JOBS`.
- WOZ058: `PENDING / WAITING_CI`; #75 refreshed to `40e3939...`, exact four-file delta; fallback 20.2 audit complete. JOBS later verified all applicable exact-head CI SUCCESS.

## Serialización de integración

Integration sigue en #78. CYCLE 060 autoriza una sola mutación de integration: **WOZ/#75**. BBB puede refresh/validate #79 but MUST NOT merge. AAA tampoco compite por integration.

## Holding / blocked items

- F0 1.2/2.2: externos/administrativos.
- F1 D10.1: off-provider/off-account proof; D10.2 decisión RO.
- F2/12.1: cold/warm real browser runtime.
- F2/13.1 #69/#70: frozen.
- F3/19.2 #76: stale/frozen.
- F3/20.2: harness integrated; approved peak, 2× runtime, latency, safety margin, durable user waitlist remain.
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
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL/merge-review equivalente.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Worker nunca inventa fallback.
- Tras fallback, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 060

```text
JOBS: baseline 63c9f8c948b1e05c30b12378ab1f31ceb04259c2
AAA055: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA056: ASSIGNED F2/14.1 minimum media streaming/memory slice; NO MERGE
BBB054: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB055: ASSIGNED SAME #79 refresh + fresh CI; NO MERGE
WOZ058: PENDING/WAITING_CI -> exact-head CI later all green
WOZ059: ASSIGNED SAME #75 race-check + only integration mutation authorized
DUPLICATE_WORK: prevented
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 14.1 active AAA056.
- F3: 17.1/17.2/18.1 integrated; #73 partial 18.2 integrated; #78 harness integrated; #75 exact-head green active WOZ059; #76 frozen.
- F4: windows/import integrated; auth/review frozen; #79 active BBB055 preparation; remaining rows/external gates open.
- JOBS: coordinación/plan; no producto/infra.
