# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 035

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no código/infra | n/a |
| AAA | F2 / 13.1 SAME #69 | `NIGHT-AAA-033`: refresh #69 a `02a40564...` + product wiring mínimo si safe-write | `NONE` |
| BBB | F4 / 25.1 windows/auth | `NIGHT-BBB-032`: harness/evidencia Windows auth, single-row promotion only after literal PASS | `NONE` |
| WOZ | F3 / 20.1 observability contract | `NIGHT-WOZ-034`: software contract A — canonical event/metric/alert taxonomy; no external observability claims | `NONE` |

**Baseline canónico CYCLE 035:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Holding items

- F2/12.1 cold/warm real: blocker de runtime navegador; harness localizado, evidencia aún no producida.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write tooling y baseline viejo.
- F3/18.1 #68 @ `2a988ec2...`: frozen por merge execution blocker y baseline viejo; necesita refresh/fresh CI si se reactiva.
- F3/20.1 external half: dashboards/alert delivery/on-call/public status/observability retention/tracing backend siguen PENDING_EXTERNAL/UNVERIFIED.

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

## Night Shift Ledger — CYCLE 035

```text
JOBS: integration remains 02a40564d85284a119281ff79995c9b9bcb5e833
AAA033: still ASSIGNED / no new final result observed; retained to avoid duplicate work
BBB032: still ASSIGNED / no new final result observed; retained to avoid duplicate work
WOZ033: DONE/AUDIT_ONLY; 20.1 gap map produced, no code/PR, 20.1 remains open
WOZ_NEW: NIGHT-WOZ-034 -> F3/20.1 software event/metric/alert taxonomy contract
AAA_CURRENT: NIGHT-AAA-033 -> F2/13.1 SAME #69
BBB_CURRENT: NIGHT-BBB-032 -> F4/25.1 windows/auth
CI_FALLBACKS: NONE / NONE / NONE
#68/#70: frozen + stale
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; 13.1 Web #69 active under AAA033; server #70 frozen.
- F3: 17.1/17.2 integrated; #68 stale/frozen; WOZ033 audit processed; WOZ034 owns the bounded 20.1 software contract slice.
- F4: windows/import integrated by #63; BBB032 advances windows/auth; 25.1/25.2 remain open.
- JOBS: coordinación/plan; no producto/infra.
