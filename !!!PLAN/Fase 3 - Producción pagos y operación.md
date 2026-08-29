# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 008:** F3 sigue siendo el mayor bloque abierto de F0–F4. Baseline vivo: `integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`.

## Owner actual

**WOZ — F3 / 16.1 → 16.2 — `NIGHT-WOZ-009`.**

PR #59 `woz/night-16.1-runtime-operability` está OPEN/Ready/mergeable=true, exact head `0e0bf188ceb298c5c6846e56576665b50a69e922`, base `f73c9ee8d058df3c780170c8c2a3fabef975c54d`. Test - Desktop Portability `33258609802`, D6 `33258609811`, D7 `33258609799` y productive temp-auth compile `33258609793` terminaron SUCCESS sobre ese exact head. WOZ debe hacer race-check final y merge protegido si la combinación sigue vigente. Esto puede cerrar el slice software dependency-safe de 16.1, no la separación física staging/prod.

Después del merge verificable, `NIGHT-WOZ-009` autoriza avanzar 16.2 solo en el carril software-only/dependency-safe, REUSE-FIRST y sin crear recursos/costo.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE CANDIDATE READY / EXTERNAL TAIL`

- [ ] Entornos físicamente separados con provider ownership, DB, storage, bots, OAuth callbacks y secretos separados. **PENDING_EXTERNAL**; requiere autorización/credenciales/recursos reales.
- [ ] Provider final/ownership real donde aplique.
- [ 🟡 ] Health/readiness/dependency checks; graceful shutdown, timeouts y proxy trust. Candidate #59 exact-head CI verde; integración pendiente.

Candidate #59 implementa dependency-safe:
- `/healthz`;
- `/readyz` con PostgreSQL `SELECT 1`, fail-closed si DB requerida falta/no responde;
- draining durante shutdown;
- trust proxy explícito/acotado;
- request/header/keepalive/socket/dependency timeouts;
- graceful SIGINT/SIGTERM drain;
- `BEATGALER_DEPLOYMENT_ENV=staging|production` obligatorio bajo `NODE_ENV=production`;
- knobs documentados en `.env.example`.

**Regla:** no crear nueva infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO. Integrar #59 no convierte 16.1 entero en PASS.

### 16.2 — `NEXT SOFTWARE-ONLY AFTER #59`

- [ ] PR → preview; tag candidato → staging; aprobación → producción.
- [ ] API origin público, TLS y headers inyectables; release sin Tailscale/local fallbacks.
- [ ] Smoke post-deploy y rollback al último artefacto/DB compatible.

`NIGHT-WOZ-009` puede cerrar únicamente el contrato software reproducible de esos puntos si existe delta real y puede probarse sin provider resources: auditar/reutilizar workflows/deploy assets existentes; fail-closed release origins; smoke/rollback scripts/fixtures; un único candidate si hace falta. Deploy real/staging real sigue externo.

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
