# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Baseline vivo CYCLE 035:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado owner / candidates

- PR #68 / 18.1 sigue OPEN @ `2a988ec2...`; exact-head green histórico sobre baseline anterior `3ad8f55a...`, pero no mergeado. Tras #63 cualquier integración exige refresh + fresh applicable exact-head CI. Candidate frozen por blocker previo de merge execution; no reintentos ceremoniales.
- PR #70 pertenece a F2/13.1 server y queda fuera del active scope WOZ; frozen por safe-write tooling y baseline viejo.
- `NIGHT-WOZ-033` terminó `DONE / AUDIT_ONLY`: produjo gap map literal de 20.1 sin código/PR. 20.1 permanece abierto.

## Owner actual

**WOZ — `NIGHT-WOZ-034` — F3/20.1 software observability contract A.**

PRIMARY:
1. Preflight sobre `02a40564...` + duplicate-check.
2. Reutilizar el gap map WOZ033 y superficies integradas (`runtime-operability`, backup readiness, promotion/rollback).
3. Cerrar únicamente el contrato software de taxonomía operativa eventos/métricas/alerts: fuente canónica pequeña que mapee auth/API/DB/billing/provider/pool/queue/backup/release a señal/severidad y referencia de respuesta/runbook cuando aplique.
4. Reusar `backup.failure` y naming existente; evitar segundo sistema/renames ceremoniales.
5. Una pieza aditiva pequeña + focused tests/fresh applicable CI solo si existe gap literal y safe-write. Si evidencia existente basta, audit-only y STOP.
6. No provider dashboard, real alert delivery, tracing backend, public status, on-call, retention provider, secretos/costes, #68/#70, F2 o F4.
7. No cerrar 20.1 completo con este slice.

CI-FALLBACK: `NONE`.

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

### 18.1 — `[ 🟡 ] CANDIDATE STALE / MERGE BLOCKED`
PR #68 contiene limits/entitlements server-side, reservation anti-race y subscription-state contract. Evidencia histórica exact-head fue green, pero no autoriza merge sobre `02a40564...`. Refresh/revalidación obligatoria cuando se reactive.

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

### 20.1 — `[ 🟡 ] AUDIT DONE / SOFTWARE SLICE ACTIVE` — WOZ `NIGHT-WOZ-034`

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

`NIGHT-WOZ-034` toma solo el primer slice software: contrato canónico pequeño de eventos/métricas/alerts. Provider dashboards/delivery/on-call/status/retention/tracing backend siguen fuera de este assignment y no pueden promoverse sin evidencia real.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
