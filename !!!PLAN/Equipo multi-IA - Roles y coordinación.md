# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 041

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F4 product-auth finding | `NIGHT-AAA-038`: root cause + corrective mínimo token/session persistence; no tocar #71 | `NONE` |
| BBB | F4 / 25.1 SAME #72 | `NIGHT-BBB-037`: attribution-first Windows Review failure; corrective harness o PRODUCT_FINDING + STOP | `NONE` |
| WOZ | F3 / 18.2 SAME #73 | `NIGHT-WOZ-040`: exact-head race-check + integración de #73; verificar merge SHA/parents; no cerrar tails provider/business | `NONE` |

**Baseline canónico CYCLE 041:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Holding items

- F2/12.1 cold/warm real: blocker runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: holding/stale; coordinator probado, wiring/refresh pendientes.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F4/windows-auth #71: regression proof; waiting product corrective AAA038 y luego refresh/revalidation por nueva asignación.
- F3/20.1: gap map WOZ033 válido; holding.

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

## Night Shift Ledger — CYCLE 041

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA038: still ASSIGNED; no new final result/handoff observed -> retain, do not duplicate
BBB037: still ASSIGNED; no new final result/handoff observed -> retain, do not duplicate
WOZ039: PENDING/WAITING_CI -> JOBS recheck green: PR #73 fc831172, Required CI SUCCESS, F3 18.2 Reconciliation SUCCESS, mergeable clean
AAA_CURRENT: NIGHT-AAA-038
BBB_CURRENT: NIGHT-BBB-037
WOZ_NEW: NIGHT-WOZ-040 SAME #73 integration transaction
CI_FALLBACKS: NONE / NONE / NONE
DUPLICATE_WORK: none
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 holding/frozen.
- F3: 17.1/17.2/18.1 integrated; 18.2 #73 exact-head green pending WOZ040 integration; 20.1 holding.
- F4: windows/import integrated; windows/auth product finding assigned AAA038; windows/review #72 red assigned BBB037; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
