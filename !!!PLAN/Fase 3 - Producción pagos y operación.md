# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Baseline vivo CYCLE 037:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado owner / candidates

- PR #68 / 18.1 sigue OPEN / Ready / mergeable @ `68adaad4a5b1b2b50ba192c1b58325cbba0472e3`, ya refrescado sobre `02a40564...` con exactamente 4 changed files / +178 -0.
- Fresh exact-head CI de #68 ya resolvió: 6 workflow runs totales = 5 `SUCCESS` + 1 `SKIPPED`; 0 `FAILURE`, 0 `IN_PROGRESS`, 0 `QUEUED`. Dedicated `F3 - 18.1 Entitlements` y Required CI aplicable están verdes.
- PR #70 pertenece a F2/13.1 server y queda fuera del active scope WOZ; frozen por safe-write tooling y baseline viejo.
- `NIGHT-WOZ-033` terminó `DONE / AUDIT_ONLY`: produjo gap map literal de 20.1 sin código/PR. 20.1 permanece abierto.

## Owner actual

**WOZ — `NIGHT-WOZ-036` — F3/18.1 SAME PR #68 race-check + merge.**

PRIMARY:
1. Preflight sobre integration vivo + duplicate-check; reutilizar SAME #68, sin replacement PR.
2. Verificar exact base/head: base `02a40564...`, head `68adaad4...`, PR OPEN/Ready/mergeable, 4 files/+178/-0.
3. Reutilizar fresh exact-head CI ya terminado: 5 SUCCESS + 1 SKIPPED, cero failure/pending; no rerun ceremonial salvo que cambie head/base o aparezca un gate nuevo aplicable.
4. Race-check final: integration debe seguir exactamente `02a40564...`.
5. Si permanece compatible, integrar SAME #68 por flujo autorizado del owner y verificar merge SHA + integration HEAD post-merge.
6. Si baseline/head cambia, CI se invalida o reaparece process tooling blocker, STOP; no duplicate PR/bypass.
7. No iniciar 18.2/20.1 automáticamente; no Stripe productivo/provider resources/grace periods/F2/F4/costos/secretos.

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

### 18.1 — `[ 🟡 ] READY_FOR_OWNER_MERGE` — WOZ `NIGHT-WOZ-036`
PR #68 contiene limits/entitlements server-side, reservation anti-race y subscription-state contract. Candidate refrescado a baseline vivo y fresh exact-head CI verde/skipped aplicable. Falta únicamente race-check e integración autorizada del owner; no marcar `[x]` antes de merge SHA real.

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

El software slice 20.1 sigue holding hasta procesar 18.1. No cerrar 20.1 hasta evidencia literal de sus componentes internos/externos aplicables.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
