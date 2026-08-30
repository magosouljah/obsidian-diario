# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 041:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; candidate exact head `68adaad4a5b1b2b50ba192c1b58325cbba0472e3`.
- WOZ037 verificó exact-head CI, race-check, merge SHA y parents. 18.1 está `[x] SOFTWARE DONE / INTEGRATED`.
- WOZ039 creó PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` desde base exacta `a9d35a3d...`.
- JOBS CYCLE 041 resolvió WAITING_CI: #73 sigue OPEN/Ready, `mergeable=true`, `mergeable_state=clean`; `Required CI` run `33320621865` = SUCCESS; `F3 - 18.2 Reconciliation` run `33320621931` = SUCCESS. No merge todavía.
- `NIGHT-WOZ-040` asignado exclusivamente a race-check + integración SAME #73.
- `NIGHT-WOZ-033` gap map de 20.1 sigue válido; 20.1 permanece holding.

## Owner actual

**WOZ — `NIGHT-WOZ-040` — F3/18.2 SAME PR #73 integration transaction.**

PRIMARY:
1. Recheck live integration/head/base/mergeability y exact-head CI de #73 antes de mutar.
2. Si todo permanece válido, integrar #73 por flujo autorizado.
3. Verificar merge SHA + parents + nuevo integration HEAD.
4. No cerrar 18.2 global: el candidate cubre reconciliation + durable/idempotent exception queue/retry fail-closed, no casos productivos/provider/business restantes.
5. No tocar provider credentials/resources, políticas RO, F2, F4 ni 20.1.
6. Handoff Issue #41 + resultado nocturno y STOP.

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

### 18.1 — `[x] SOFTWARE DONE / INTEGRATED`
PR #68 integró limits/entitlements server-side, reservation anti-race y subscription-state contract. Merge `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

### 18.2 — `[ 🟡 ] SOFTWARE SLICE READY / GLOBAL OPEN`
- [ 🟡 ] reconciliación Stripe↔BeatGaler + cola de excepciones: PR #73 exact-head verde, pendiente integración WOZ040;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

No convertir la integración de #73 en cierre global de 18.2 sin evidencia literal de los tails anteriores.

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
