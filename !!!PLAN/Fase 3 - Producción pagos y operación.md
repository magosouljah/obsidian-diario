# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Baseline vivo CYCLE 036:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado owner / candidates

- PR #68 / 18.1 sigue OPEN @ `2a988ec2...`; exact-head green histórico sobre baseline anterior `3ad8f55a...`, pero no mergeado. Tras #63 cualquier integración exige refresh + fresh applicable exact-head CI.
- PR #70 pertenece a F2/13.1 server y queda fuera del active scope WOZ; frozen por safe-write tooling y baseline viejo.
- `NIGHT-WOZ-033` terminó `DONE / AUDIT_ONLY`: produjo gap map literal de 20.1 sin código/PR. 20.1 permanece abierto.
- `NIGHT-WOZ-034` no produjo resultado final observable antes de CYCLE 036 y fue superseded por JOBS; no ejecutar 034 después de recibir 035.

## Owner actual

**WOZ — `NIGHT-WOZ-035` — F3/18.1 SAME PR #68 refresh + exact-head revalidation.**

PRIMARY:
1. Preflight sobre `02a40564...` + duplicate-check; reutilizar SAME #68, sin replacement PR.
2. Reconcile/refresh el candidate desde su baseline viejo `3ad8f55a...` al baseline vivo preservando solo el delta 18.1 autorizado.
3. Mantener server-side subscription-state authority, limits antes de reservar, PostgreSQL advisory-lock transaction anti-race y Billing Portal contract que nunca concede entitlement desde redirect/session.
4. REUSE-FIRST: preservar implementación/tests ya existentes; no reescribir billing ni abrir 18.2.
5. Focused tests + fresh applicable exact-head CI sobre el head refrescado; old green CI es histórico y no autoriza merge.
6. Race-check antes de merge; integrar SAME #68 solo si head/base/scope exactos y gates aplicables verdes.
7. Si reaparece merge/process tooling blocker, registrar error exacto y STOP sin duplicate PR/bypass.
8. No Stripe productivo, provider resources, grace-period decisions, F2/F4, #70, 20.1 implementation, costos o secretos.

CI-FALLBACK: `NONE` — 18.2 depende materialmente de 18.1 y 20.1 es una pieza separada, no fallback independiente dentro del mismo turno.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
- [ ] entornos físicamente separados con provider ownership/DB/storage/bots/OAuth/secrets — externo;
- [ ] provider final/ownership real;
- [x] health/readiness/dependency checks; graceful shutdown/timeouts/proxy trust — #59.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe y rollback fail-closed. Deploy/staging/prod reales siguen externos.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
#65.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
#67 merge `3ad8f55a...`.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 — `[ 🟡 ] REACTIVATED / REFRESH REQUIRED` — WOZ `NIGHT-WOZ-035`
PR #68 contiene limits/entitlements server-side, reservation anti-race y subscription-state contract. Evidencia histórica exact-head fue green, pero no autoriza merge sobre `02a40564...`. Refresh/revalidación obligatoria y race-check antes de integración.

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

Gap map literal procesado de WOZ033:
- logs: PARTIAL; no structured service-wide production logging + retention demostrados;
- metrics: GAP;
- tracing: GAP;
- error reporting: PARTIAL/GAP;
- retention: PARTIAL/EXTERNAL;
- alert routing matrix auth/API/DB/billing/provider/pool/queue/release: GAP; backup alert contract: PARTIAL;
- on-call: GAP/PENDING_EXTERNAL;
- runbook: PARTIAL;
- public status: GAP/PENDING_EXTERNAL;
- kill switches: GAP.

Evidencia ya existente reutilizable: `cloud-server/runtime-operability.js`, `cloud-server/server.js`, `cloud-server/deployment-promotion-contract.mjs`, `cloud-server/d10-backup-readiness-contract.mjs`.

El primer software slice de 20.1 vuelve a holding en CYCLE 036 porque 18.1 es anterior y más crítico. No cerrar 20.1 hasta evidencia literal de sus componentes internos/externos aplicables.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
