# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 042

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F4 product-auth SAME #74 | `NIGHT-AAA-039`: corregir compile/type error exacto, preservar runtime corrective, fresh exact-head CI | `NONE` |
| BBB | F4 / 25.1 SAME #72 | `NIGHT-BBB-038`: promover windows/review tras PASS literal, fresh post-promotion gates + merge si verde | `NONE` |
| WOZ | F3 / 20.1 internal observability | `NIGHT-WOZ-041`: cerrar solo gaps internos software del gap map; external tails quedan abiertos | `NONE` |

**Baseline canónico CYCLE 042:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Holding / blocked items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: holding/stale; coordinator probado, wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #71: regression proof; waiting #74 corrective verde/integrado y luego nueva asignación BBB.
- F3/18.2 #73 @ `fc831172...`: exact-head verde/mergeable, pero `BLOCKED / MERGE_FLOW_UNAVAILABLE`; no duplicar ni recrear.

## Reglas

1. Trabajo cross-phase solo si dependencias reales lo permiten.
2. Una pieza material = un owner.
3. Owner hace preflight → implementation/audit → tests → CI → handoff.
4. Findings no transfieren ownership automáticamente; JOBS lo hace explícito.
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

## Night Shift Ledger — CYCLE 042

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA038: WAITING_CI -> JOBS recheck FAILURE: Required CI 33321752522, TS compile error in src/platform/index.ts; AAA039 emitted SAME #74
BBB037: WAITING_CI -> JOBS recheck SUCCESS: Windows Review 33321799798 literal PASS; BBB038 emitted SAME #72 promotion + fresh gates
WOZ040: BLOCKED/MERGE_FLOW_UNAVAILABLE on #73; technical evidence remains green/race-clean; WOZ041 moved to independent F3/20.1 internal slice
AAA_CURRENT: NIGHT-AAA-039
BBB_CURRENT: NIGHT-BBB-038
WOZ_CURRENT: NIGHT-WOZ-041
CI_FALLBACKS: NONE / NONE / NONE
DUPLICATE_WORK: none
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 holding/frozen.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 integration-ready pero merge-flow blocked; WOZ041 en 20.1 internal.
- F4: windows/import integrated; windows/auth #74 compile-red asignado AAA039; windows/review #72 literal PASS pendiente promotion/integration BBB038; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
