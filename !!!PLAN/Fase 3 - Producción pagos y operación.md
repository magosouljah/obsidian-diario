# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 062:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation MERGED como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; cierra solo software reconciliation/exception-queue slice.
- PR #78 / 20.2 capacity harness MERGED como `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; claim máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- PR #76 sigue OPEN/stale/frozen. Canonical Privacy/Terms + public routes existen; Settings canonical sync sigue pendiente.
- PR #75 `woz/night-20.1-observability @ 40e39393247dbdd506ac01edefa84fd0b0add94c` sigue OPEN/non-draft/mergeable. WOZ060 confirmó cuatro intended observability files y CI exact-head aplicable verde, pero la transacción de merge fue bloqueada por `MERGE_FLOW_UNAVAILABLE` antes de aceptación GitHub. `NIGHT-WOZ-061` posee el retry exact-head; no reimplementar ni duplicar candidate.
- PR #77 CLOSED/unmerged; superseded por #78.

## Owners actuales

**WOZ — `NIGHT-WOZ-061` — F3 / 20.1 SAME #75.**  
PRIMARY: fresh race-check + retry de la transacción exact-head de #75; sin workaround de código. Solo si GitHub acepta, verificar merge SHA + parents.  
CI-FALLBACK: `NONE`.

**BBB — `NIGHT-BBB-057` — F3 / 20.2 runtime capacity.**  
PRIMARY: reutilizar el harness #78 integrado con target canónico **80 usuarios esperados / 160 usuarios de validación**; obtener evidencia runtime aplicable para 160 y requisitos literales.  
CI-FALLBACK: #79/F4-25.2 refresh docs-only + fresh CI, únicamente si PRIMARY queda esperando runtime/external; no merge.

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

### 20.1 — `[ 🟡 ] EXACT-HEAD GREEN / MERGE-FLOW BLOCKED / ASSIGNED WOZ061`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Immutable pins + history-preserving refresh completados. WOZ060 volvió a confirmar exact-head CI aplicable verde y cuatro-file delta; GitHub no aceptó el merge porque la capa de ejecución bloqueó la transacción antes de llegar al proveedor. WOZ061 solo reintenta el merge exact-head después de fresh race-check. External observability tails no se cierran con este PR.

### 20.2 — `[ 🟡 ] HARNESS SOFTWARE INTEGRATED / TARGET APPROVED / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic local/synthetic parameterized harness: PR #78 merged;
- [x] **approved expected peak: 80 simultaneous users** — RO/OWNER Issue #41 `5472774681`;
- [ ] **required validation: 160 simultaneous users (2×)** con runtime evidence aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado en la prueba aplicable;
- [x] admission control + per-bot ceiling software exists;
- [ ] safety margin medida contra 80 expected;
- [ ] durable user waitlist.

La decisión RO 80/160 fija el target; **no es PASS**. BBB057 posee el carril de evidencia runtime a 160. Si solo existe evidencia local/sintética, debe quedar explícitamente no autoritativa. 20.2 solo puede cerrar con evidencia aplicable de 160 + latency/error/queue/recovery + safety margin + durable admission/waitlist, sin data loss ni cross-tenant unauthorized behavior.

WOZ058 read-only fallback confirmó que la cola existente es fairness/bot-ordering state, no durable user waitlist. #78 por sí solo no autoriza full 20.2 PASS.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
