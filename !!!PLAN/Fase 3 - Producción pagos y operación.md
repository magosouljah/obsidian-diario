# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 038:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado owner / candidates

- PR #68 / 18.1 sigue OPEN / Ready / mergeable @ `68adaad4a5b1b2b50ba192c1b58325cbba0472e3`, base exacta `02a40564...`, 4 changed files / +178 -0.
- Fresh exact-head workflows: 6 totales = 5 `SUCCESS` + 1 `SKIPPED`; 0 `FAILURE`, 0 `IN_PROGRESS`, 0 `QUEUED`. Dedicated `F3 - 18.1 Entitlements` y Required CI aplicable están verdes.
- No hubo merge nuevo en CYCLE 038; 18.1 no se marca `[x]` todavía.
- `NIGHT-WOZ-037` sustituye la orden 036 no procesada y conserva SAME #68 para race-check + merge, sin nueva implementación.
- `NIGHT-WOZ-033` gap map de 20.1 sigue válido; 20.1 permanece holding.

## Owner actual

**WOZ — `NIGHT-WOZ-037` — F3/18.1 SAME PR #68 race-check + merge.**

PRIMARY:
1. Preflight + duplicate-check; revalidar integration vivo y exact head.
2. Verificar #68 OPEN/Ready/mergeable, base `02a40564...`, head `68adaad4...`, 4 files/+178/-0.
3. Reutilizar exact-head CI ya terminado; no rerun ceremonial salvo cambio material.
4. Si race-check permanece limpio, integrar SAME #68 por flujo autorizado del owner.
5. Verificar merge SHA + integration HEAD post-merge.
6. Si baseline/head/CI cambia o aparece blocker de proceso, STOP; no bypass/replacement PR.
7. No iniciar 18.2/20.1 automáticamente.

CI-FALLBACK: `NONE`.

## Día 16

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
Health/readiness/shutdown/timeouts/proxy trust integrado por #59. Separación física provider/DB/storage/bots/OAuth/secrets sigue externa.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe y rollback fail-closed. Deploy/staging/prod reales siguen externos.

## Día 17

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
#65.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
#67 merge `3ad8f55a...`.

## Día 18

### 18.1 — `[ 🟡 ] READY_FOR_OWNER_MERGE`
PR #68 contiene limits/entitlements server-side, reservation anti-race y subscription-state contract. Candidate refreshed + exact-head green; falta merge SHA real.

### 18.2
- [ ] reconciliación Stripe↔BeatGaler + cola de excepciones;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

## Día 19

### 19.1
- [ ] dominio/API/status/support URLs/sender domains;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ ] versión/fecha Terms/Privacy aceptada.

### 19.2
- [ ] Privacy/Terms/refund/cancel/renewal reales;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] AUDIT DONE / HOLDING`
Gap map WOZ033: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing GAP; backup alert PARTIAL; on-call/status externos; runbook PARTIAL; kill switches GAP.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
