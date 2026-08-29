# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 014:** baseline vivo `integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`. F3 sigue siendo uno de los mayores bloques abiertos de F0–F4.

## Owner actual

**WOZ — F3 / 17.1 Stripe Checkout server-side software-only — `NIGHT-WOZ-015`.**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`; no satisface separación física staging/prod.

PR #61 `woz/night-16.2-promotion-contract` quedó **CLOSED / MERGED** como `55e0d8759ec03b23fa8e4f1f35304922dffeb992`, candidate exact head `d254b294cf8fe78d93025271360dd73ed594898f`; Required CI `33271019389`, D6 `33271019493`, D7 `33271019399`, temp-auth `33271019373` y F4 matrix `33271019370` SUCCESS. Declaración limitada: 16.2 SOFTWARE DONE / EXTERNAL TAIL.

Duplicate-check previo a `NIGHT-WOZ-015`: búsqueda visible por `stripe checkout idempotency webhook price` no encontró implementación reutilizable en BeatGaler; WOZ debe repetir búsqueda precisa antes de crear artifact.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`

- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**; requiere autorización/credenciales/recursos reales.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — **DONE / INTEGRATED** por PR #59.

Integrado por #59: `/healthz`; `/readyz` PostgreSQL fail-closed; draining; proxy trust acotado; timeouts; graceful shutdown; `BEATGALER_DEPLOYMENT_ENV`; knobs documentados.

**Regla:** no crear infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`

Integrado por PR #61 como `55e0d875...`: software dependency-safe para PR→preview; tag candidato→staging; aprobación→producción; mismo source/artifact SHA; API origin HTTPS sin localhost/Tailscale fallback; headers inyectables; smoke `/healthz` + `/readyz`; rollback fail-closed al artifact previo con compatibilidad DB + smoke.

**Pendiente externo:** deploy/staging/production reales, provider ownership, DNS/TLS productivo y rollback real. No falsear evidencia física/productiva.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[ 🟡 ] ASSIGNED / SOFTWARE-ONLY` — WOZ `NIGHT-WOZ-015`
- [ ] productos/precios/trial/currency/tax e IDs internos estables;
- [ ] Checkout Session server-side;
- [ ] idempotency keys y precios no decididos por cliente.

**Orden 015:** implementar el contrato software mínimo con boundary de provider y tests deterministas; rechazar tampering de price/plan del cliente; retry/idempotency; unsupported product/currency; provider timeout/error fail-closed; identidad/metadata ligadas al usuario. Sin Stripe real, credenciales/costo ni claims productivos.

### 17.2
- [ ] firma webhook raw-body;
- [ ] event ID durable + async/retry;
- [ ] duplicados/desorden/timeouts/eventos relevantes.

**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado.

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
