# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 027:** baseline vivo `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Estado owner / bloqueo actual

PR #68 / F3 18.1 conserva ownership técnico de WOZ pero queda **HOLDING / BLOCKED_EXTERNAL_MERGE_EXECUTION** después de `NIGHT-WOZ-025`. El candidate no se recrea ni se modifica en `NIGHT-WOZ-026`; WOZ usa ese turno en el server half independiente de F2/13.1.

NIGHT-WOZ-025 revalidó #68 OPEN/Ready/mergeable sobre base exacta `3ad8f55a...`, head `2a988ec2a25d6ecfa927614fcc32cde689995103`, exact-head CI verde y race-check limpio. El intento de merge con expected-head guard fue bloqueado por la execution/safety layer antes de que GitHub aceptara la mutación. Recheck posterior: integration siguió exactamente `3ad8f55a...`. No existe merge SHA; 18.1 NO está integrado.

PR #59 está MERGED/DONE en su slice software; separación física staging/prod sigue externa. PR #61 está MERGED; 16.2 permanece SOFTWARE DONE / EXTERNAL TAIL. PR #65 está MERGED; 17.1 SOFTWARE DONE / INTEGRATED. PR #67 está MERGED como `3ad8f55a...`; 17.2 SOFTWARE DONE / INTEGRATED.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados — PENDING_EXTERNAL.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — #59.

No crear infraestructura pagada/proyectos/buckets/bots/OAuth ni recursos con costo sin aprobación RO.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe PR→preview→staging→producción con mismo source/artifact SHA, smoke y rollback fail-closed.

**Pendiente externo:** deploy/staging/production reales, provider ownership, DNS/TLS productivo y rollback real.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
- [x] IDs internos/catalog contract server-owned.
- [x] Checkout Session abstraction server-side.
- [x] Idempotency y rechazo de precio/plan/currency/trial controlado por cliente.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
- [x] firma webhook raw-body;
- [x] event ID durable/idempotente + retry/failure state;
- [x] duplicados/desorden/timeouts/eventos relevantes seguros.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 — `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`

PR #68 software-only implementa:
- [x] limits/entitlements server-side antes de reservar recursos;
- [x] transacción/reserva anti-carreras mediante PostgreSQL transaction + advisory xact lock;
- [x] contrato server-side Billing Portal/cancel/subscription states sin conceder entitlement desde redirect/session.

Exact-head `2a988ec2a25d6ecfa927614fcc32cde689995103`:
- F3 18.1 `33299898356` SUCCESS;
- D6 `33299898222` SUCCESS;
- D7 `33299898232` SUCCESS;
- Productive Temp Auth Compile `33299898207` SUCCESS;
- Desktop Portability `33299898130` SUCCESS;
- Upgrade 21.2 SKIPPED/no aplicable.

`NIGHT-WOZ-025`: race-check limpio + intento de merge bloqueado por execution layer; no mutación aceptada por GitHub. Candidate queda frozen. No marcar 18.1 `[x]` hasta merge real + post-merge integration SHA verificado. No afirmar Stripe/provider productivo.

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

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia productiva/externa.
