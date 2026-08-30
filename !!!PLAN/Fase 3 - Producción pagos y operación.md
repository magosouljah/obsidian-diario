# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 047:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready/mergeable, base exacta `a9d35a3d...`; software slice listo pero no existe merge verificable. Mantener frozen bajo el blocker previo de merge-flow; no recrear ni tocar bajo 046.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue OPEN/Ready/mergeable. Required CI conocido falla por floating `actions/checkout@v4` + `actions/setup-node@v4`; corrective exacto conocido pero el último write fue bloqueado por safety. Mantener frozen.
- `NIGHT-WOZ-045` terminó `DONE / AUDIT_ONLY`; no cerró 20.2.
- `NIGHT-WOZ-046` es owner único del siguiente slice: harness parametrizable de capacidad/carga, sin provider/infra/load productivo y sin #73/#75.

## Owner actual

**WOZ — `NIGHT-WOZ-046` — F3 / 20.2 software harness.**

### PRIMARY

1. Reuse-first; confirmar #73/#75 untouched.
2. Crear el mínimo harness reutilizable para una futura prueba 2× peak; target obligatorio se inyecta al ejecutar y no puede inventarse.
3. Sin target aprobado, el harness debe negarse a producir claim 2×/PASS.
4. Medir/reportar attempted concurrency/ops, latencia (p50/p95/p99 donde aplique), errores, queue/wait o ausencia explícita, y recovery timing del path ejercitado.
5. Reutilizar admission control/per-bot ceiling; no rediseñar transport/provider.
6. Preferir nuevos archivos de harness/test/workflow. No tocar #75 observability ni #73 billing; broad product change = STOP.
7. Focused deterministic tests + fresh exact-head CI. Resultado máximo permitido en este turno: `HARNESS_READY`; `RUNTIME_CAPACITY_UNVERIFIED` permanece literal.
8. No cerrar 20.2.

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
- [ 🟡 ] reconciliación provider↔BeatGaler + cola de excepciones: PR #73 exact-head candidate OPEN/Ready/mergeable; no merge verificable;
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
Gap map vigente: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing GAP; backup alert PARTIAL; on-call/status externos; runbook PARTIAL; kill switches GAP.

PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido pero write flow bloqueado; no fresh PASS, no integración.

### 20.2 — `[ 🟡 ] AUDIT DONE / HARNESS ASSIGNED / NO PASS CLAIM`
WOZ045 produjo gap map literal:
- capacity envelope `PARTIAL`;
- approved expected peak `GAP / prerequisite missing`;
- load/stress harness `GAP`;
- 2× peak proof `PENDING_EXTERNAL`;
- latency `GAP`;
- error measurement `PARTIAL`;
- queue measurement `PARTIAL`;
- recovery measurement `PARTIAL`;
- admission control `EXISTS (software)`;
- per-bot ceiling `EXISTS (software)`;
- safety margin `GAP`;
- durable user waitlist `GAP`.

`NIGHT-WOZ-046` puede cerrar únicamente el **gap de harness software** si logra evidencia exact-head. No selecciona expected peak ni ejecuta carga productiva. Después seguirán target aprobado + prueba runtime controlada 2× con latency/errors/queue/recovery.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal o staging real sin evidencia externa/productiva.
