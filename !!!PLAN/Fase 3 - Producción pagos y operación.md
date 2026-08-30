# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 042:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready sobre base exacta `a9d35a3d...`, mergeable y exact-head verde.
- `NIGHT-WOZ-040` revalidó scope + CI + race-check, pero terminó `BLOCKED / MERGE_FLOW_UNAVAILABLE`: el execution layer impidió la transacción antes de aceptación por GitHub. Integration no cambió.
- No recrear, rebasar ni duplicar #73 mientras base/head sigan válidos. El blocker es de flujo de merge, no técnico.
- `NIGHT-WOZ-033` dejó gap map 20.1 válido. JOBS asigna `NIGHT-WOZ-041` para avanzar solo los gaps internos software de 20.1 mientras #73 espera canal de merge capaz.

## Owner actual

**WOZ — `NIGHT-WOZ-041` — F3 / 20.1 internal observability slice.**

### PRIMARY

1. Preflight live baseline + duplicate-check; no tocar #73.
2. REUSE-FIRST sobre gap map WOZ033 y evidencia ya integrada de 5.2/16.x/17.x/18.x.
3. Cerrar únicamente gaps internos software verificables de 20.1: logging estructurado útil, métricas internas donde falten, error reporting interno, routing/conditions de alerts, runbook software y kill switches fail-closed.
4. No crear provider resources, dashboards productivos pagados, on-call externo, status page, DNS, credentials ni retention policy externa.
5. Si ya existe evidencia suficiente para un subrequisito, documentarla y no hacer cambio ceremonial.
6. Si hacen falta cambios, una sola rama/PR F3 mínima desde baseline vivo; focused tests + fresh applicable exact-head CI.
7. Reportar exactamente qué queda `PENDING_EXTERNAL` y STOP.

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

`NIGHT-WOZ-041` trabaja solo lo interno y dependency-safe. Provider/on-call/status/retention externos permanecen abiertos aunque el software slice mejore.

### 20.2
- [ ] capacity envelope + load al doble del pico;
- [ ] medir latency/errors/queue/recovery;
- [ ] admission control/per-bot ceiling/margen/waitlist.

**Principio:** no falsear proveedor, capacidad, Stripe, DNS, legal o staging real sin evidencia externa/productiva.
