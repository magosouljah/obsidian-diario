# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 017 FINAL:** baseline vivo `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.

## Owner actual

**WOZ — F3 / 17.2 webhook integrity/idempotency/retry software-only — `NIGHT-WOZ-018`.**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9...`; separación física staging/prod sigue externa. PR #61 quedó **MERGED** como `55e0d875...`; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 quedó **CLOSED / MERGED** como `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`, parents `b114111caf... + e655386405...`. Exact-head previo: F3 17.1 `33276769749`, Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` = SUCCESS; Upgrade skipped/no aplicable.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — **DONE / INTEGRATED** por #59.

**Regla:** no crear infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
Integrado por #61 como `55e0d875...`: promoción dependency-safe PR→preview→staging→producción con mismo source/artifact SHA, smoke y rollback fail-closed.

**Pendiente externo:** deploy/staging/production reales, provider ownership, DNS/TLS productivo y rollback real.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
- [x] IDs internos/catalog contract server-owned en software.
- [x] Checkout Session abstraction server-side.
- [x] idempotency key y rechazo de precio/plan/currency/trial controlado por cliente.

**Evidencia:** PR #65 head `e65538640581f3f986748968db1f4dfb069c2579`, exact-head CI verde, merge `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. El cierre es **software**: no prueba cuenta Stripe productiva, credenciales, products/prices reales ni decisiones comerciales reales.

### 17.2 — `[ 🟡 ] ASSIGNED` — WOZ `NIGHT-WOZ-018`
- [ ] firma webhook sobre raw-body antes de parse/mutate;
- [ ] event ID durable/idempotente + async/retry/failure state;
- [ ] duplicados/desorden/timeouts/eventos relevantes con semántica segura.

**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. `NIGHT-WOZ-018` es software-only, REUSE-FIRST y no autoriza recursos/credenciales Stripe reales.

## Día 18 — Entitlements, portal y reconciliación

### 18.1
- [ ] limits server-side antes de reservar recursos;
- [ ] transacción/reserva anti-carreras;
- [ ] Billing Portal/cancelación y estados subscription.

### 18.2
- [ ] reconciliación Stripe↔BeatGaler + cola de excepciones;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

## Día 19 — Dominio, identidad, legal y soporte

### 19.1
- [ ] dominio/API/status/support URLs/sender domains;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ ] versión/fecha Terms/Privacy aceptada.

### 19.2
- [ ] Privacy/Terms/refund/cancel/renewal reales;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20 — Observabilidad, capacidad y recovery

### 20.1
- [ ] logs/métricas/tracing/error reporting/retention;
- [ ] dashboards/alerts auth/API/DB/billing/provider/pool/queue/backup/release;
- [ ] on-call/runbook/status/kill switches.

### 20.2
- [ ] capacity envelope y load al doble del pico esperado;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia productiva/externa correspondiente.
