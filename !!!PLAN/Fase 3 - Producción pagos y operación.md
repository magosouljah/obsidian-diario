# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 017:** baseline vivo `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`. F3 sigue siendo uno de los mayores bloques abiertos de F0–F4.

## Owner actual

**WOZ — F3 / 17.1 SAME PR #65 exact-head green race-check/integration — `NIGHT-WOZ-017`.**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`; no satisface separación física staging/prod.

PR #61 quedó **CLOSED / MERGED** como `55e0d8759ec03b23fa8e4f1f35304922dffeb992`; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 `woz/night-17.1-checkout-contract` sigue OPEN/Ready/mergeable sobre base `b114111caf...`, head exacto `e65538640581f3f986748968db1f4dfb069c2579`. Evidencia exact-head: F3 17.1 `33276769749` SUCCESS; Desktop Portability `33276769684` SUCCESS; D6 `33276769695` SUCCESS; D7 `33276769698` SUCCESS; temp-auth `33276769702` SUCCESS; Upgrade `33276769715` SKIPPED/no aplicable. Todavía NO está integrado; `NIGHT-WOZ-017` procesa exclusivamente race-check/merge.

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

### 17.1 — `[ 🟡 ] SOFTWARE CANDIDATE GREEN / NOT INTEGRATED` — WOZ `NIGHT-WOZ-017`
- [ ] productos/precios/trial/currency/tax e IDs internos estables;
- [ ] Checkout Session server-side;
- [ ] idempotency keys y precios no decididos por cliente.

**Estado factual:** candidate #65 está exact-head verde pero no mergeado. Solo después de merge verificable puede promoverse este slice a `SOFTWARE DONE / INTEGRATED`. Eso no prueba Stripe productivo, credenciales reales ni decisiones comerciales reales.

### 17.2
- [ ] firma webhook raw-body;
- [ ] event ID durable + async/retry;
- [ ] duplicados/desorden/timeouts/eventos relevantes.

**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. 17.2 no empieza dentro de `NIGHT-WOZ-017`; requiere nuevo Assignment ID tras 17.1 integrado.

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
