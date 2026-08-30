# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 038

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | Desktop product-auth finding | `NIGHT-AAA-036`: root cause + corrective mínimo de token/session persistence; no tocar #71 | `NONE` |
| BBB | F4 / 25.1 windows/review | `NIGHT-BBB-035`: slice independiente Review; no tocar auth/#71 | `NONE` |
| WOZ | F3 / 18.1 SAME #68 | `NIGHT-WOZ-037`: exact-head race-check + merge | `NONE` |

**Baseline canónico CYCLE 038:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Holding items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: holding; coordinator probado, product wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #71 @ `29656aa0...`: regression proof intact; waiting product corrective by AAA.
- F3/20.1: gap map WOZ033 válido; holding hasta 18.1.

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

## Night Shift Ledger — CYCLE 038

```text
JOBS: integration remains 02a40564d85284a119281ff79995c9b9bcb5e833
AAA035: no final result -> superseded; #69 moved HOLDING
BBB034: PENDING / PRODUCT_FINDING -> Desktop token persistence assertion failed after real WebDriver session
WOZ036: no final result -> superseded; #68 still OPEN/Ready/mergeable exact-head green
AAA_NEW: NIGHT-AAA-036 -> product-auth root cause/corrective
BBB_NEW: NIGHT-BBB-035 -> independent windows/review row
WOZ_NEW: NIGHT-WOZ-037 -> #68 race-check + merge
CI_FALLBACKS: NONE / NONE / NONE
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 holding/frozen.
- F3: 17.1/17.2 integrated; #68 exact-head green awaiting owner merge; 20.1 holding.
- F4: windows/import integrated; windows/auth blocked by product finding assigned AAA; BBB works windows/review independently; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
