# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 020:** baseline vivo `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.

## Owner actual

**WOZ — F3 / 17.2 SAME #67 PostgreSQL recovery-gate corrective — `NIGHT-WOZ-019` (ASSIGNED).**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9...`; separación física staging/prod sigue externa. PR #61 quedó **MERGED** como `55e0d875...`; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 quedó **CLOSED / MERGED** como `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. 17.1 está SOFTWARE DONE / INTEGRATED.

PR #67 `woz/night-17.2-webhook-contract` está OPEN/Ready sobre base `ed6aab7e...`, head `22550152e9960c5dad328711b3a8b150301a8c4f`.

Candidate 17.2 software-only ya contiene raw-body verifier, ledger durable PostgreSQL `billing_webhook_events`, dedupe/idempotency por event ID, ordering watermark, retry/failure state, out-of-order safe ignore, unsupported-event safe no-op y `entitlementGranted=false`. Tests focales cubren firma válida/inválida, body mutado, duplicados, reordering, failure+retry, timeout/error, unsupported y concurrencia.

Evidencia exact-head:
- F3 17.2 `33278423859` — SUCCESS;
- D6 `33278423854` — SUCCESS;
- D7 `33278423851` — SUCCESS;
- temp-auth `33278423880` — SUCCESS;
- Required CI / Desktop Portability `33278423879` — **FAILURE**.

Causa factual disponible: el job `99169258638` `PostgreSQL live integration + recovery gate` superó migrations/adversarial persistence y dump/encrypt/restore, pero falló en `Verify restored constraints, secrets, reconciliation and rollback state`. No se infiere todavía si migration 0006, webhook durable state o expectation de recovery es la causa exacta.

`NIGHT-WOZ-019` debe reutilizar SAME #67, diagnosticar esa discrepancia y aplicar solo el corrective mínimo sin debilitar recovery/D9/D10. Fresh applicable Required CI es obligatorio antes de merge. CI-FALLBACK: `NONE`; 18.x comparte billing/PostgreSQL ownership y no es independiente de 17.2.

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

**Evidencia:** PR #65 merge `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. El cierre es **software**: no prueba cuenta Stripe productiva, credenciales, products/prices reales ni decisiones comerciales reales.

### 17.2 — `[ 🟡 ] CANDIDATE / REQUIRED CI RED` — WOZ `NIGHT-WOZ-019`
- [ 🟡 ] firma webhook sobre raw-body antes de parse/mutate — implementada en candidate #67, no integrada;
- [ 🟡 ] event ID durable/idempotente + async/retry/failure state — implementado en candidate #67, no integrado;
- [ 🟡 ] duplicados/desorden/timeouts/eventos relevantes con semántica segura — cubierto por candidate/tests focales, no integrado.

**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. No marcar 17.2 `[x]` hasta merge exact-head verde. No Stripe productivo, no 18.x, no infraestructura/costo.

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
