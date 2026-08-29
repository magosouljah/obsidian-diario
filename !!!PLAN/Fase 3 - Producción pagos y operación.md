# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 012:** baseline vivo `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`. F3 sigue siendo uno de los mayores bloques abiertos de F0–F4.

## Owner actual

**WOZ — F3 / 16.2 software-only — `NIGHT-WOZ-013`.**

PR #59 `woz/night-16.1-runtime-operability` quedó **MERGED / DONE** en su slice software como `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`. Esto integra el contrato runtime dependency-safe de 16.1; **no** satisface la separación física staging/prod.

PR #61 `woz/night-16.2-promotion-contract` sigue OPEN/Ready/mergeable con head `aef1cd0b1a26be327e561f344d63dae5d8def7ef`, pero ese head fue validado sobre snapshot base `58a6bf614...`. El baseline vivo avanzó por #60 a `7de7b57a...`; el protected merge fue rechazado correctamente porque Required CI debía renovarse para la combinación nueva. `NIGHT-WOZ-013` debe REUSE SAME #61, refresh sobre el baseline vivo, exact-head CI nuevo y merge protegido si el race-check queda limpio.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`

- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**; requiere autorización/credenciales/recursos reales.
- [ ] Provider final/ownership real donde aplique.
- [x] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust — **DONE / INTEGRATED** por PR #59.

Integrado por #59:
- `/healthz`;
- `/readyz` con PostgreSQL `SELECT 1`, fail-closed si DB requerida falta/no responde;
- draining durante shutdown;
- trust proxy explícito/acotado;
- request/header/keepalive/socket/dependency timeouts;
- graceful SIGINT/SIGTERM drain;
- `BEATGALER_DEPLOYMENT_ENV=staging|production` obligatorio bajo `NODE_ENV=production`;
- knobs documentados en `.env.example`.

**Regla:** no crear nueva infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO. El merge #59 no convierte 16.1 entero en PASS.

### 16.2 — `[ 🟡 ] SOFTWARE CANDIDATE / NEEDS REFRESH` — WOZ `NIGHT-WOZ-013`

Candidate existente #61 contiene contrato software dependency-safe para:
- PR → preview; tag candidato → staging; aprobación → producción;
- mismo source/artifact SHA;
- API origin público HTTPS, sin localhost/Tailscale fallback;
- headers inyectables;
- smoke `/healthz` + `/readyz`;
- rollback fail-closed al artefacto previo con compatibilidad DB + smoke.

**Evidencia válida histórica:** exact head `aef1cd0...` tuvo D6/temp-auth/D7/Desktop Portability SUCCESS sobre el baseline anterior. **No autoriza merge post-#60.** GitHub ya rechazó usar el estado viejo después del movimiento de integración.

**Orden 013:** refresh de SAME branch/PR #61 sobre `7de7b57a...`, preservar exclusivamente el delta F3, exact-head CI aplicable nuevo y protected merge expected-head solo con race-check limpio. Si integra, declarar únicamente `16.2 SOFTWARE DONE / EXTERNAL TAIL`; deploy/staging/production reales siguen externos.

**Gate completo:** mismo SHA desplegable, smoke y rollback verificables, sin pasos manuales irrepetibles ni secretos compartidos entre entornos.

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
