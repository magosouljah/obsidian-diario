# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 045:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready, exact-head verde y holding por `MERGE_FLOW_UNAVAILABLE`. No recrear, rebasar ni tocar mientras siga válido.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue OPEN/Ready/mergeable sobre base exacta `a9d35a3d...`.
- Required CI `33323457041` permanece FAILURE por supply-chain immutable-action gate: el workflow nuevo usa `actions/checkout@v4` y `actions/setup-node@v4`.
- `NIGHT-WOZ-043` verificó el corrective exacto de dos pins pero terminó `BLOCKED / WRITE_TOOL_SAFETY`: la escritura fue rechazada antes de aceptación, por lo que #75 no cambió, no existe fresh CI y no hay merge. Issue #41 `5470266322`.
- Reintentar el mismo write sin cambio del blocker sería duplicación. #75 queda frozen hasta que exista un write flow seguro/capaz; no se transfiere ni recrea automáticamente.

## Owner actual

**WOZ — `NIGHT-WOZ-044` — F3 / 20.2 REUSE-FIRST capacity/load readiness audit — READ ONLY.**

### PRIMARY

1. Confirmar baseline vivo y duplicate-check; #73/#75 permanecen holding y no se mutan.
2. Auditar artefactos/evidencia existente para capacity envelope, 2× expected peak, latency/errors/queue/recovery, admission control, per-bot ceiling, safety margin y waitlist.
3. Separar `EXISTS`, `PARTIAL`, `GAP`, `PENDING_EXTERNAL` y distinguir software de prueba real de capacidad.
4. No inventar expected peak ni números no aprobados; si falta el target, registrarlo como prerequisite.
5. Assignment estrictamente read-only: sin rama/PR/commit/workflow/code/infra, sin load test costoso y sin tocar 20.1/#75 ni 18.2/#73.
6. No cerrar 20.2; dejar gap map + evidencia + blockers a JOBS y STOP.

**CI-FALLBACK:** `NONE`.

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
- [ 🟡 ] reconciliación Stripe↔BeatGaler + cola de excepciones: PR #73 exact-head verde, `BLOCKED / MERGE_FLOW_UNAVAILABLE` para integración;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

No convertir #73 en integrado ni 18.2 en `[x]` sin merge verificable y evidencia literal de tails provider/business.

## Día 19

### 19.1
- [ ] dominio/API/status/support URLs/sender domains;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ ] versión/fecha Terms/Privacy aceptada.

### 19.2
- [ ] Privacy/Terms/refund/cancel/renewal reales;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE BLOCKED`
Gap map: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing GAP; backup alert PARTIAL; on-call/status externos; runbook PARTIAL; kill switches GAP.

PR #75 contiene un primer software slice para structured redacted events, bounded counters, explicit alert condition→route mapping, fail-closed kill switches, focused tests y runbook interno. Su fallo conocido sigue siendo únicamente el supply-chain pinning del workflow, pero el corrective no pudo escribirse bajo `NIGHT-WOZ-043` por `WRITE_TOOL_SAFETY`. No existe head nuevo ni fresh PASS; mantener frozen hasta que cambie ese blocker.

Aunque #75 llegue a integrarse, permanecen abiertos product call-site wiring, tracing/backend durable de error reporting/metrics, retention, provider alert resources/delivery, on-call/escalation y public status.

### 20.2 — `[ 🟡 ] AUDIT ASSIGNED / NO PASS CLAIM`
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

`NIGHT-WOZ-044` hace únicamente REUSE-FIRST/read-only gap map para determinar qué evidencia ya existe y qué es software vs prueba runtime/provider. No selecciona un expected peak si no existe uno aprobado y no ejecuta carga costosa.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
