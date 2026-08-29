# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 021:** baseline vivo `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`.

## Owner actual

**WOZ — F3 / 17.2 SAME #67 refresh + final integration transaction — `NIGHT-WOZ-020` (ASSIGNED).**

PR #59 quedó **MERGED / DONE** en su slice software como `be9e58c9...`; separación física staging/prod sigue externa. PR #61 quedó **MERGED** como `55e0d875...`; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 quedó **CLOSED / MERGED** como `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. 17.1 está SOFTWARE DONE / INTEGRATED.

PR #67 `woz/night-17.2-webhook-contract` sigue OPEN/Ready. Head actual observado: `8a5341114e00f373bd88553f3f95be53a153b6b8`.

Candidate 17.2 software-only contiene raw-body verifier, ledger durable PostgreSQL `billing_webhook_events`, dedupe/idempotency por event ID, ordering watermark, retry/failure state, out-of-order safe ignore, unsupported-event safe no-op y `entitlementGranted=false`.

El failure anterior de recovery fue reducido y corregido: `postgres-restore.verify.cjs` tenía ledger hardcodeado 0001..0005 mientras #67 añadió migration 0006. El corrective mínimo `8a534111...` cambió el verifier para derivar versiones desde `listMigrations()` preservando checks de checksum, secrets, reconciliation, rotation/rollback y constraints.

Evidencia exact-head sobre `8a534111...`:
- F3 17.2 `33280134623` — SUCCESS;
- D6 `33280134598` — SUCCESS;
- D7 `33280134660` — SUCCESS;
- temp-auth `33280134648` — SUCCESS;
- Required CI / Desktop Portability `33280134630` — SUCCESS.

Sin embargo, #66 movió integration después a `712b49b...`. Por evidence-before-claim, esa evidencia no autoriza merge contra la combinación nueva. `NIGHT-WOZ-020` debe refresh SAME #67 onto live baseline, obtener fresh applicable exact-head CI y solo entonces integrar.

CI-FALLBACK: `NONE`; 18.x comparte billing/PostgreSQL ownership y depende de 17.2.

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

### 17.2 — `[ 🟡 ] CANDIDATE / REFRESH REQUIRED` — WOZ `NIGHT-WOZ-020`
- [ 🟡 ] firma webhook sobre raw-body antes de parse/mutate — candidate probado, no integrado;
- [ 🟡 ] event ID durable/idempotente + async/retry/failure state — candidate probado, no integrado;
- [ 🟡 ] duplicados/desorden/timeouts/eventos relevantes con semántica segura — candidate/tests verdes en combinación previa, no integrado.

**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. No marcar 17.2 `[x]` hasta merge exact-head verde sobre baseline vivo. No Stripe productivo, no 18.x, no infraestructura/costo.

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
