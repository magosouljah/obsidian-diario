# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 044

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F4 / SAME #74 | `NIGHT-AAA-040`: race-check + integración de #74 usando exact-head green; no #71 todavía | `NONE` |
| BBB | F4 / SAME #72 | `NIGHT-BBB-039`: atribuir/corregir matrix-contract post-promotion; fresh gates + merge solo si verde | `NONE` |
| WOZ | F3 / SAME #75 | `NIGHT-WOZ-043`: pin-only supply-chain corrective; fresh exact-head CI; no #73 | `NONE` |

**Baseline canónico CYCLE 044:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Handoffs procesados

- AAA039: #74 head `14dfba52...`; D6 `33324138675`, D7 `33324138676`, Required CI `33324138689` = SUCCESS; no merge observado. AAA040 emitido para la transacción exacta de integración.
- BBB038: #72 promovió solo `windows/review`; nuevo head `56dc4adf...`; Review/Import/Required CI verdes pero F4 Matrix `33324512174` FAILURE en `Validate dependency-safe matrix contract`. BBB039 emitido attribution-first.
- WOZ042: no resultado, commit ni CI nuevo; #75 permanece en `bb493b37...`. 042 queda `NOT_PROCESSED / SUPERSEDED_BY_JOBS`; 043 reemite el mismo correctivo mínimo para evitar ejecución tardía del ID viejo.

## Holding / blocked items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: holding/stale; coordinator probado, wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #71: regression proof; espera #74 integrado + nueva asignación explícita.
- F3/18.2 #73 @ `fc831172...`: exact-head verde/mergeable, pero `MERGE_FLOW_UNAVAILABLE`; no duplicar ni recrear.
- F3/20.1 #75 @ `bb493b37...`: pin corrective pendiente WOZ043; external/productive tails siguen abiertos.

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
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Si no existe fallback seguro: `CI-FALLBACK: NONE`.
- Worker nunca inventa fallback.

## Night Shift Ledger — CYCLE 044

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA039: WAITING_CI -> exact-head PASS resolved by JOBS; #74 not merged
AAA040: ASSIGNED SAME #74 integration transaction
BBB038: WAITING_CI -> F4 Matrix FAILURE on promoted head 56dc4adf...
BBB039: ASSIGNED SAME #72 attribution/corrective
WOZ042: NOT_PROCESSED / SUPERSEDED_BY_JOBS; #75 unchanged
WOZ043: ASSIGNED SAME #75 pin-only corrective
CI_FALLBACKS: NONE / NONE / NONE
DUPLICATE_WORK: none
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 holding/frozen.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 ready but merge-flow blocked; 20.1 #75 pin corrective pendiente.
- F4: windows/import integrated; windows/auth #74 exact-head green pendiente integración; windows/review #72 dedicated green pero matrix-contract red; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
