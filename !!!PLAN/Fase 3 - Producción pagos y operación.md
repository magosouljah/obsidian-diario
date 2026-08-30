# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 039:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 fue MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; candidate exact head `68adaad4a5b1b2b50ba192c1b58325cbba0472e3`, 4 changed files / +178 -0.
- Exact-head evidence previa al merge: 5 workflows `SUCCESS` + 1 `SKIPPED`, 0 failure/pending; dedicated `F3 - 18.1 Entitlements` y Required CI aplicable verdes.
- WOZ037 verificó race-check, merge SHA, parents y new integration HEAD. 18.1 se procesa `[x] SOFTWARE DONE / INTEGRATED`.
- `NIGHT-WOZ-038` toma 18.2 software-only con REUSE-FIRST; no proveedor/credenciales ni decisiones de grace/refund inventadas.
- `NIGHT-WOZ-033` gap map de 20.1 sigue válido; 20.1 permanece holding.

## Owner actual

**WOZ — `NIGHT-WOZ-038` — F3/18.2 reconciliation + exception-queue software contract.**

PRIMARY:
1. Auditar primitives existentes de reconciliation/webhook/event-ledger/subscription/retry/idempotency.
2. No crear recursos Stripe/credenciales/productos/precios ni infraestructura.
3. Si ya está satisfecho literalmente, handoff audit-only; no PR ceremonial.
4. Si hay gap interno, implementar solo reconciliación durable/idempotente + cola de excepciones/retry fail-closed, sin conceder entitlement por redirect/session.
5. Focused tests: replay/idempotencia, divergence, exception/retry y no-grant ambiguo.
6. Fresh applicable exact-head CI para nuevo head.
7. No cerrar 18.2 si faltan casos de negocio/proveedor literales.
8. STOP ante decisión RO/proveedor/credencial, baseline race, scope drift o CI no atribuible.

CI-FALLBACK: `NONE`.

## Día 16

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
Health/readiness/shutdown/timeouts/proxy trust integrado por #59. Separación física provider/DB/storage/bots/OAuth/secrets sigue externa.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe y rollback fail-closed. Deploy/staging/prod reales siguen externos.

## Día 17

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
#65.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
#67 merge `3ad8f55a...`.

## Día 18

### 18.1 — `[x] SOFTWARE DONE / INTEGRATED`
PR #68 integró limits/entitlements server-side, reservation anti-race y subscription-state contract. Merge `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; WOZ037 verificó exact-head/race-check/parents.

### 18.2 — `[ 🟡 ] IN PROGRESS`
- [ ] reconciliación Stripe↔BeatGaler + cola de excepciones;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

## Día 19

### 19.1
- [ ] dominio/API/status/support URLs/sender domains;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ ] versión/fecha Terms/Privacy aceptada.

### 19.2
- [ ] Privacy/Terms/refund/cancel/renewal reales;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] AUDIT DONE / HOLDING`
Gap map WOZ033: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing GAP; backup alert PARTIAL; on-call/status externos; runbook PARTIAL; kill switches GAP.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
