# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 034

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 13.1 SAME #69 | `NIGHT-AAA-033`: refresh #69 a `02a40564...` + product wiring mínimo si safe-write | `NONE` |
| BBB | F4 / 25.1 windows/auth | `NIGHT-BBB-032`: harness/evidencia Windows auth, single-row promotion only after literal PASS | `NONE` |
| WOZ | F3 / 20.1 observability | `NIGHT-WOZ-033`: REUSE-FIRST gap map sobre baseline vivo; una pieza mínima solo si gap literal/safe-write | `NONE` |

**Baseline canónico CYCLE 034:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Holding items

- F2/12.1 cold/warm real: blocker de runtime navegador; harness localizado, evidencia aún no producida.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write tooling y baseline viejo.
- F3/18.1 #68 @ `2a988ec2...`: frozen por merge execution blocker y baseline viejo; necesita refresh/fresh CI si se reactiva.

## Reglas

1. Trabajo cross-phase solo si dependencias reales lo permiten.
2. Una pieza material = un owner.
3. Owner hace preflight → implementation/audit → tests → CI → handoff.
4. Findings no transfieren ownership automáticamente.
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

## Night Shift Ledger — CYCLE 034

```text
JOBS: #63 merged; integration -> 02a40564d85284a119281ff79995c9b9bcb5e833
AAA032: PENDING/STOP_RUNTIME_UNAVAILABLE; harness real-browser localizado, cold/warm no demostrado
BBB031: DONE/INTEGRATED; #63 merge 02a40564...; windows/import slice integrated
WOZ032: no result observable before baseline move -> superseded by JOBS
AAA_NEW: NIGHT-AAA-033 -> F2/13.1 SAME #69 refresh + safe minimal product wiring
BBB_NEW: NIGHT-BBB-032 -> F4/25.1 windows/auth
WOZ_NEW: NIGHT-WOZ-033 -> F3/20.1 observability gap map on new baseline
CI_FALLBACKS: NONE / NONE / NONE
#68/#70: frozen + stale after #63 baseline move
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; 13.1 Web #69 active under AAA033; server #70 frozen.
- F3: 17.1/17.2 integrated; #68 stale/frozen; WOZ033 on 20.1.
- F4: windows/import integrated by #63; BBB032 advances windows/auth; 25.1/25.2 remain open.
- JOBS: coordinación/plan; no producto/infra.
