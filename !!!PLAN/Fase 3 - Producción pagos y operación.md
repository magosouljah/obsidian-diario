# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 024:** baseline vivo `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Owner actual

**WOZ — F3 / 18.1 software-only — `NIGHT-WOZ-023` (ASSIGNED).**

`NIGHT-WOZ-022` no produjo RESULTADO DEL TURNO, PR ni handoff observable antes de CYCLE 024 y quedó `NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no debe ejecutarse después de 023.

PR #59 quedó **MERGED / DONE** en su slice software; separación física staging/prod sigue externa. PR #61 quedó **MERGED**; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL.

PR #65 quedó **CLOSED / MERGED** como `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. 17.1 está SOFTWARE DONE / INTEGRATED.

PR #67 `woz/night-17.2-webhook-contract` quedó **CLOSED / MERGED**. Exact tested head `27c2f30007a687a144be289a64ab986451f05c99`; merge/integration SHA `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

Evidencia exact-head final de #67: F3 17.2 `33283532676`, D6 `33283532664`, D7 `33283532679`, productive temp-auth `33283532723`, Required CI/Desktop Portability `33283532696` SUCCESS; Upgrade 21.2 `33283532704` SKIPPED/no aplicable.

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

**Límite de claim:** no prueba Stripe productivo, cuenta/provider real, 18.x, physical staging/prod ni decisiones comerciales externas.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 — `[ 🟡 ] ASSIGNED — WOZ NIGHT-WOZ-023`
- [ ] limits server-side antes de reservar recursos;
- [ ] transacción/reserva anti-carreras;
- [ ] Billing Portal/cancelación y estados subscription.

**Scope 023:** software-only y REUSE-FIRST sobre #65/#67. Una sola rama/PR mínima si hay gaps. Debe probar límites/autoridad server-side, reserva atómica/race-safe y contrato de estados/portal. No Stripe productivo, credenciales/provider, 18.2, grace-period decisions ni infraestructura. CI-FALLBACK `NONE`.

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
