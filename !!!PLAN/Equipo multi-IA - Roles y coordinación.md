# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 037

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 13.1 SAME #69 | `NIGHT-AAA-035`: refresh #69 a `02a40564...` + product wiring mínimo si safe-write | `NONE` |
| BBB | F4 / 25.1 SAME #71 | `NIGHT-BBB-034`: attribution-first del Windows Auth FAILURE; corrective F4 mínimo o PRODUCT_FINDING | `NONE` |
| WOZ | F3 / 18.1 SAME #68 | `NIGHT-WOZ-036`: exact-head race-check + merge de #68 ya refreshed/green | `NONE` |

**Baseline canónico CYCLE 037:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Holding items

- F2/12.1 cold/warm real: blocker de runtime navegador; harness localizado, evidencia aún no producida.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write tooling y baseline viejo.
- F3/20.1: audit gap map de WOZ033 sigue válido; software slice queda holding hasta resolver 18.1.
- F3 external half de 20.1: dashboards/alert delivery/on-call/public status/observability retention/tracing backend siguen PENDING_EXTERNAL/UNVERIFIED.

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

## Night Shift Ledger — CYCLE 037

```text
JOBS: integration remains 02a40564d85284a119281ff79995c9b9bcb5e833
AAA034: no final result observed -> superseded by explicit fresh NIGHT-AAA-035; SAME #69 retained
BBB033: no final result observed -> superseded by explicit fresh NIGHT-BBB-034; SAME #71 retained
WOZ035: PENDING/WAITING_CI -> JOBS exact-head recheck resolved 6 workflows = 5 SUCCESS + 1 SKIPPED, zero failure/pending
PR68: OPEN/Ready/mergeable @ 68adaad4..., base 02a40564..., diff 4 files/+178/-0
AAA_NEW: NIGHT-AAA-035 -> F2/13.1 SAME #69
BBB_NEW: NIGHT-BBB-034 -> F4/25.1 SAME #71 corrective
WOZ_NEW: NIGHT-WOZ-036 -> F3/18.1 SAME #68 race-check + merge
CI_FALLBACKS: NONE / NONE / NONE
#70: frozen + stale
F3/20.1: holding; gap map retained
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; 13.1 Web #69 active under AAA035; server #70 frozen.
- F3: 17.1/17.2 integrated; #68 refreshed and fresh exact-head green, active under WOZ036 for race-check+merge; 20.1 audit holding.
- F4: windows/import integrated by #63; #71 Windows Auth red at literal assertion step; BBB034 owns attribution/corrective; 25.1/25.2 remain open.
- JOBS: coordinación/plan; no producto/infra.
