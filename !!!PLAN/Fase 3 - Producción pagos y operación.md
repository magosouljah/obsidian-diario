# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 060:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation MERGED como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; cierra solo software reconciliation/exception-queue slice.
- PR #78 / 20.2 capacity harness MERGED como `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; claim máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- PR #76 sigue OPEN/stale/frozen. Canonical Privacy/Terms + public routes existen; Settings canonical sync sigue pendiente.
- PR #75 `woz/night-20.1-observability @ 40e39393247dbdd506ac01edefa84fd0b0add94c` está OPEN/non-draft/mergeable sobre live integration, exactamente cuatro intended observability files. Fresh exact-head F3 20.1, D6, D7, Productive Temp Auth Compile y Desktop Portability son SUCCESS; Upgrade 21.2 SKIPPED/not applicable. `NIGHT-WOZ-059` posee race-check + integración exact-head en CYCLE 060.
- PR #77 CLOSED/unmerged; superseded por #78.

## Owners actuales

**WOZ — `NIGHT-WOZ-059` — F3 / 20.1 SAME #75.**

### WOZ PRIMARY
1. Recheck live integration y #75 exact head `40e3939...`.
2. Confirmar exactamente los cuatro paths intended y ningún scope drift.
3. Confirmar CI exact-head aplicable completa/verde.
4. Merge solo race-clean con expected head; verificar merge SHA + parents.
5. Claim máximo: software observability slice integrated; external metrics/tracing/backend/retention/alert delivery/on-call/status permanecen UNVERIFIED.

### WOZ CI-FALLBACK
`NONE`.

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
PR #68.

### 18.2 — `[ 🟡 ] RECONCILIATION SOFTWARE INTEGRATED / GLOBAL OPEN`
- [x] software reconciliation provider↔BeatGaler + exception queue slice: PR #73 merged;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund con evidencia aplicable;
- [ ] grace periods/productive billing behavior verificados donde corresponda.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
- [ ] dominio/API/status/support URLs/sender domains con evidencia productiva;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ 🟡 ] public legal routes `/privacy` y `/terms` existen en #76 pero no están integrados/deployed.

### 19.2 — `[ 🟡 ] CANONICAL LEGAL CANDIDATE / FROZEN ON SAFE REFRESH`
- [ 🟡 ] Privacy Policy v1.0 + Terms v1.0 owner-approved están en #76;
- [ 🟡 ] rutas públicas + links de entrada existen en #76;
- [ 🟡 ] Settings sigue con contenido temporal;
- [ ] safe history-preserving refresh de #76 sobre live baseline;
- [ ] independent legal review / production publication evidence;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] EXACT-HEAD GREEN / ASSIGNED WOZ059`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Immutable pins + history-preserving refresh completados en WOZ058. Exact-head CI aplicable terminó verde. Falta únicamente race-check + integración; external observability tails no se cierran con este PR.

### 20.2 — `[ 🟡 ] HARNESS SOFTWARE INTEGRATED / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic local/synthetic parameterized harness: PR #78 merged;
- [ ] approved expected peak;
- [ ] real/applicable 2× peak proof;
- [ ] latency target/result;
- [ 🟡 ] error/queue/recovery measurement partial;
- [x] admission control + per-bot ceiling software exists;
- [ ] safety margin;
- [ ] durable user waitlist.

WOZ058 read-only fallback confirmó explícitamente que la cola existente es fairness/bot-ordering state, no durable user waitlist. #78 no autoriza full 20.2 PASS.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
