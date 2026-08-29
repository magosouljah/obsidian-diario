# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 013:** baseline vivo `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`. F3 sigue siendo uno de los mayores bloques abiertos de F0–F4.

## Owner actual

**WOZ — F3 / 16.2 SAME PR #61 merge transaction — `NIGHT-WOZ-014`.**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`; no satisface separación física staging/prod.

PR #61 `woz/night-16.2-promotion-contract` fue refrescada en `NIGHT-WOZ-013` a exact head `d254b294cf8fe78d93025271360dd73ed594898f`, preservando el delta F3 sobre `7de7b57a...`. GitHub actual: OPEN/Ready/mergeable=true; Required CI `33271019389` SUCCESS; D6 `33271019493` SUCCESS; no failure/in-progress observado en el set exact-head. Sigue NO MERGED hasta race-check/merge del owner.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`

- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**; requiere autorización/credenciales/recursos reales.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — **DONE / INTEGRATED** por PR #59.

Integrado por #59: `/healthz`; `/readyz` PostgreSQL fail-closed; draining; proxy trust acotado; timeouts; graceful shutdown; `BEATGALER_DEPLOYMENT_ENV`; knobs documentados.

**Regla:** no crear infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO.

### 16.2 — `[ 🟡 ] SOFTWARE CANDIDATE / READY_FOR_OWNER_RACE_CHECK` — WOZ `NIGHT-WOZ-014`

Candidate #61 cubre software dependency-safe para PR→preview; tag candidato→staging; aprobación→producción; mismo source/artifact SHA; API origin HTTPS sin localhost/Tailscale fallback; headers inyectables; smoke `/healthz` + `/readyz`; rollback fail-closed al artifact previo con compatibilidad DB + smoke.

**Orden 014:** si integration sigue en `7de7b57a...`, protected merge con expected head `d254b294...` tras race-check; si otro owner mueve integration, refresh SAME #61 + fresh applicable CI antes de merge. Tras integración declarar solo `16.2 SOFTWARE DONE / EXTERNAL TAIL`. Puede hacer audit READ-ONLY de 17.1 después, sin implementar Stripe sin nueva orden.

**Gate completo:** mismo SHA desplegable, smoke y rollback verificables, sin pasos manuales irrepetibles ni secretos compartidos entre entornos. Deploy/staging/production reales siguen externos.

## Día 17 — Stripe Checkout y webhooks

### 17.1
- [ ] productos/precios/trial/currency/tax e IDs internos estables;
- [ ] Checkout Session server-side;
- [ ] idempotency keys y precios no decididos por cliente.

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
