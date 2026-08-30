# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 048:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready/mergeable; software slice listo pero no existe merge verificable. Frozen bajo blocker previo de merge-flow.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue OPEN/Ready/mergeable. Corrective de immutable pins conocido; write flow previo bloqueado. Frozen.
- `NIGHT-WOZ-046` no produjo RESULTADO DEL TURNO/handoff observable y queda superseded.
- `NIGHT-WOZ-047` es owner único del harness parametrizable de capacidad/carga; no provider/infra/load productivo y no #73/#75.

## Owner actual

**WOZ — `NIGHT-WOZ-047` — F3 / 20.2 software harness.**

### PRIMARY

1. Reuse-first; confirmar #73/#75 untouched.
2. Crear el mínimo harness reutilizable para una futura prueba 2× peak; target obligatorio se inyecta al ejecutar y no puede inventarse.
3. Sin target aprobado, el harness debe negarse a producir claim 2×/PASS.
4. Medir/reportar attempted concurrency/ops, latencia p50/p95/p99 donde aplique, errores, queue/wait o ausencia explícita, y recovery timing.
5. Reutilizar admission control/per-bot ceiling; no rediseñar transport/provider.
6. Preferir nuevos archivos de harness/test/workflow. Broad product change = STOP.
7. Focused deterministic tests + fresh exact-head CI. Resultado máximo: `HARNESS_READY`; `RUNTIME_CAPACITY_UNVERIFIED` permanece.
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
- [ 🟡 ] reconciliación provider↔BeatGaler + cola de excepciones: PR #73 OPEN/Ready/mergeable; no merge verificable;
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

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE BLOCKED`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido pero write flow bloqueado; no fresh PASS, no integración.

### 20.2 — `[ 🟡 ] AUDIT DONE / HARNESS ASSIGNED / NO PASS CLAIM`
Gap map vigente:
- capacity envelope `PARTIAL`;
- approved expected peak `GAP / prerequisite missing`;
- load/stress harness `GAP`;
- 2× peak proof `PENDING_EXTERNAL`;
- latency `GAP`;
- error/queue/recovery measurement `PARTIAL`;
- admission control + per-bot ceiling `EXISTS (software)`;
- safety margin `GAP`;
- durable user waitlist `GAP`.

`NIGHT-WOZ-047` puede cerrar únicamente el gap de harness software con evidencia exact-head. No selecciona expected peak ni ejecuta carga productiva.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal o staging real sin evidencia externa/productiva.
