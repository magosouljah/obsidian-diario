# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 043:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready sobre base exacta `a9d35a3d...`, mergeable y exact-head verde.
- `NIGHT-WOZ-040` revalidó scope + CI + race-check, pero terminó `BLOCKED / MERGE_FLOW_UNAVAILABLE`: el execution layer impidió la transacción antes de aceptación por GitHub. Integration no cambió.
- No recrear, rebasar ni duplicar #73 mientras base/head sigan válidos. El blocker es de flujo de merge, no técnico.
- `NIGHT-WOZ-041` creó PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`, 4 files +156/-0, con observability contract software-only.
- Recheck JOBS: Required CI / Test - Desktop Portability `33323457041` = FAILURE. Supply chain gate falla en `Verify every external GitHub Action is immutable`; el workflow nuevo usa `actions/checkout@v4` y `actions/setup-node@v4`.
- `NIGHT-WOZ-042` corrige únicamente esos dos pins usando los SHAs inmutables canónicos del Required CI y exige fresh exact-head evidence antes de integración.

## Owner actual

**WOZ — `NIGHT-WOZ-042` — F3 / 20.1 SAME #75 supply-chain corrective.**

### PRIMARY

1. Preflight live baseline + SAME #75 exact head/base + duplicate-check; no tocar #73.
2. Reemplazar únicamente las referencias flotantes del workflow F3 20.1 por los pins ya usados por Required CI:
   - `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`;
   - `actions/setup-node@820762786026740c76f36085b0efc47a31fe5020`.
3. Preservar semántica del workflow y no cambiar producto/observability contract salvo lo estrictamente necesario para ese pinning.
4. Focused observability test + fresh exact-head Required CI y workflow F3 20.1.
5. Si todo queda verde y el merge flow está disponible, race-check + merge #75 y verificar merge SHA/post-merge integration HEAD.
6. Si aparece failure no atribuible al pinning o el merge flow vuelve a bloquear, reportar factual y STOP.
7. Provider/on-call/status/retention/tracing/backend durable/product call-site wiring siguen abiertos; no reclamarlos con este slice.

**CI-FALLBACK:** `NONE`.

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
PR #68 integró limits/entitlements server-side, reservation anti-race y subscription-state contract. Merge `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

### 18.2 — `[ 🟡 ] SOFTWARE SLICE READY / GLOBAL OPEN`
- [ 🟡 ] reconciliación Stripe↔BeatGaler + cola de excepciones: PR #73 exact-head verde, `BLOCKED / MERGE_FLOW_UNAVAILABLE` para integración;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund;
- [ ] grace periods aprobados.

No convertir #73 en integrado ni 18.2 en `[x]` sin merge verificable y evidencia literal de tails provider/business.

## Día 19

### 19.1
- [ ] dominio/API/status/support URLs/sender domains;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ ] versión/fecha Terms/Privacy aceptada.

### 19.2
- [ ] Privacy/Terms/refund/cancel/renewal reales;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE`
Gap map WOZ033: logs PARTIAL; metrics GAP; tracing GAP; error reporting PARTIAL/GAP; retention PARTIAL/EXTERNAL; alert routing GAP; backup alert PARTIAL; on-call/status externos; runbook PARTIAL; kill switches GAP.

PR #75 contiene un primer software slice para structured redacted events, bounded counters, explicit alert condition→route mapping, fail-closed kill switches, focused tests y internal runbook. Aún no está integrado y su Required CI está rojo por supply-chain pinning del workflow; `NIGHT-WOZ-042` corrige solo eso.

Aunque #75 llegue a integrarse, permanecen abiertos product call-site wiring, tracing/backend durable de error reporting/metrics, retention, provider alert resources/delivery, on-call/escalation y public status.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
