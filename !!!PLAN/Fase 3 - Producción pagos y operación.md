# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 025:** baseline vivo `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**WOZ — F3 / 18.1 / PR #68 final integration — `NIGHT-WOZ-024` (ASSIGNED).**

`NIGHT-WOZ-023` produjo PR #68 `woz/night-18.1-entitlements-reservation @ 2a988ec2a25d6ecfa927614fcc32cde689995103` y cerró PENDING/WAITING_CI. JOBS CYCLE 025 verificó que #68 sigue OPEN/Ready/mergeable sobre base exacta `3ad8f55a...` y que toda la CI aplicable del exact head terminó verde.

PR #59 quedó **MERGED / DONE** en su slice software; separación física staging/prod sigue externa. PR #61 quedó **MERGED**; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 quedó **CLOSED / MERGED** como `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. 17.1 está SOFTWARE DONE / INTEGRATED.

PR #67 quedó **CLOSED / MERGED** como `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`. 17.2 está SOFTWARE DONE / INTEGRATED.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — DONE/INTEGRATED por #59.

**Regla:** no crear infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
Integrado por #61 como `55e0d875...`: promoción dependency-safe PR→preview→staging→producción con mismo source/artifact SHA, smoke y rollback fail-closed.

**Pendiente externo:** deploy/staging/production reales, provider ownership, DNS/TLS productivo y rollback real.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
- [x] IDs internos/catalog contract server-owned en software.
- [x] Checkout Session abstraction server-side.
- [x] idempotency key y rechazo de precio/plan/currency/trial controlado por cliente.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
- [x] firma webhook sobre raw-body antes de parse/mutate;
- [x] event ID durable/idempotente + async/retry/failure state;
- [x] duplicados/desorden/timeouts/eventos relevantes con semántica segura.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 — `[ 🟡 ] EXACT-HEAD GREEN / AWAITING OWNER INTEGRATION — WOZ NIGHT-WOZ-024`

PR #68 implementa software-only:
- [x] limits/entitlements server-side antes de reservar recursos;
- [x] transacción/reserva anti-carreras mediante PostgreSQL transaction + advisory xact lock;
- [x] contrato server-side de Billing Portal/cancel/subscription states sin conceder entitlement desde redirect/session.

Exact-head `2a988ec2a25d6ecfa927614fcc32cde689995103`:
- F3 18.1 `33299898356` SUCCESS;
- D6 `33299898222` SUCCESS;
- D7 `33299898232` SUCCESS;
- Productive Temp Auth Compile `33299898207` SUCCESS;
- Desktop Portability `33299898130` SUCCESS;
- Upgrade 21.2 `33299898169` SKIPPED/no aplicable.

No marcar 18.1 `[x]` hasta merge real y post-merge SHA verificado. No afirma Stripe/provider productivo.

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
