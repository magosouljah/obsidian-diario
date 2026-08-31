# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 066:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation MERGED como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; cierra solo software reconciliation/exception-queue slice.
- PR #78 / 20.2 capacity harness MERGED como `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; claim máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- PR #76 sigue OPEN/stale/frozen. Canonical Privacy/Terms + public routes existen; Settings canonical sync sigue pendiente.
- PR #75 `woz/night-20.1-observability @ 40e39393247dbdd506ac01edefa84fd0b0add94c` sigue OPEN/non-draft/mergeable. CYCLE 066 confirma `base_sha = 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`, 4 intended files, sin merge posterior y exact-head CI verde: F3 20.1, D6, D7, Productive Temp Auth Compile y Desktop Portability SUCCESS; Upgrade 21.2 Staging SKIPPED. `NIGHT-WOZ-064` no dejó resultado; `NIGHT-WOZ-065` posee la única transacción exact-head autorizada.
- PR #77 CLOSED/unmerged; superseded por #78.

## Owners actuales

**WOZ — `NIGHT-WOZ-065` — F3 / 20.1 SAME #75.**  
PRIMARY: fresh race-check + exact-head merge transaction de #75; sin workaround ni reimplementación. Solo si GitHub acepta, verificar merge SHA + parents.  
CI-FALLBACK: `NONE`.

**BBB — `NIGHT-BBB-061` — F3 / 20.2 runtime capacity.**  
PRIMARY: reutilizar harness #78 integrado con target canónico **80 usuarios esperados / 160 usuarios de validación**; obtener evidencia runtime materialmente aplicable a 160 para requisitos literales.  
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

### 20.1 — `[ 🟡 ] EXACT-BASE / EXACT-HEAD / ASSIGNED WOZ065`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. CYCLE 066 verificó GitHub real: OPEN/non-draft/mergeable; exact head `40e39393247dbdd506ac01edefa84fd0b0add94c`; `base_sha` exactamente igual al live integration `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`; 4 files; exact-head CI aplicable verde. No existe merge aceptado todavía. WOZ065 posee únicamente la transacción exact-head. External observability tails no se cierran con este PR.

### 20.2 — `[ 🟡 ] HARNESS SOFTWARE INTEGRATED / TARGET APPROVED / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic local/synthetic parameterized harness: PR #78 merged;
- [x] **approved expected peak: 80 simultaneous users** — RO/OWNER Issue #41 `5472774681`;
- [ ] **required validation: 160 simultaneous users (2×)** con runtime evidence aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado en la prueba aplicable;
- [x] admission control + per-bot ceiling software exists;
- [ ] safety margin medida contra 80 expected;
- [ ] durable user waitlist.

`NIGHT-BBB-060` no produjo resultado verificable antes de CYCLE 066 y queda superseded. `NIGHT-BBB-061` fue recalculado desde cero porque el target 80/160 ya está fijado y la evidencia runtime sigue siendo blocker directo. Synthetic/local-only no cierra capacidad. 20.2 solo puede cerrar con evidencia aplicable de 160 + latency/error/queue/recovery + safety margin + durable admission/waitlist, sin data loss ni cross-tenant unauthorized behavior.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
