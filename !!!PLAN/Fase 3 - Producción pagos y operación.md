# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Baseline vivo CYCLE 034:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.

## Estado owner / candidates

- PR #68 / 18.1 sigue OPEN @ `2a988ec2...`; exact-head green histórico sobre baseline anterior `3ad8f55a...`, pero no mergeado. El merge #63 movió integration a `02a40564...`; cualquier intento futuro de integrar #68 exige refresh + fresh applicable exact-head CI. Candidate frozen por blocker previo de merge execution; no reintentos ceremoniales.
- PR #70 pertenece a F2/13.1 server y queda fuera del active scope WOZ; frozen por safe-write tooling y baseline viejo.
- `NIGHT-WOZ-032` no dejó resultado observable antes del movimiento de baseline. JOBS lo supersede por `NIGHT-WOZ-033` para evitar usar una combinación vieja.

## Owner actual

**WOZ — `NIGHT-WOZ-033` — F3/20.1 observability REUSE-FIRST.**

PRIMARY:
1. Preflight sobre `02a40564...` + duplicate-check.
2. No tocar #68/#70 ni reutilizar sus ramas.
3. Mapear requisito→evidencia exacta→cobertura→gap para logs/métricas/tracing/error reporting/retention; alerts auth/API/DB/billing/provider/pool/queue/backup/release; on-call/runbook/status/kill-switch.
4. Reutilizar 5.2 observabilidad/alarms/on-call, #59 health/readiness, #61 promotion/rollback y cualquier artifact real existente.
5. Solo si existe un gap literal pequeño, independiente, software-only y safely writable, crear UNA pieza mínima con focused tests + fresh applicable exact-head CI.
6. Provider/dashboard real, recursos pagados, secretos, DNS/status vendor o decisiones RO se registran `PENDING_EXTERNAL`.

CI-FALLBACK: `NONE`.

## Día 16 — Staging y producción reproducibles

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
- [ ] entornos físicamente separados con provider ownership/DB/storage/bots/OAuth/secrets — externo;
- [ ] provider final/ownership real;
- [x] health/readiness/dependency checks; graceful shutdown/timeouts/proxy trust — #59.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe y rollback fail-closed. Deploy/staging/prod reales siguen externos.

## Día 17 — Stripe Checkout y webhooks

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
#65.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
#67 merge `3ad8f55a...`.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 — `[ 🟡 ] CANDIDATE STALE / MERGE BLOCKED`
PR #68 contiene limits/entitlements server-side, reservation anti-race y subscription-state contract. Evidencia histórica exact-head fue green, pero no autoriza merge sobre `02a40564...`. Refresh/revalidación obligatoria cuando se reactive.

### 18.2
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

### 20.1 — `[ 🟡 ] AUDIT ACTIVE` — WOZ `NIGHT-WOZ-033`
- [ ] logs/métricas/tracing/error reporting/retention;
- [ ] dashboards/alerts auth/API/DB/billing/provider/pool/queue/backup/release;
- [ ] on-call/runbook/status/kill switches.

No promover ítems por similitud nominal. Evidence-before-claim literal.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
