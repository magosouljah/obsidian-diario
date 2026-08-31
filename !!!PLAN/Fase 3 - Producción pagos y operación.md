# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 080:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED.
- PR #73 / 18.2 software reconciliation MERGED; no cierra escenarios provider/payment globales.
- PR #75 / 20.1 software observability MERGED; external observability tails permanecen.
- PR #78 / 20.2 capacity harness MERGED; claim máximo histórico `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- PR #83 / durable waitlist: OPEN/DRAFT/mergeable, exact base `957f9777...`, exact head `52b58f56...`, 3-file bounded scope. Exact-head F3 20.2 Durable Waitlist + Test Desktop Portability + D6/D7/temp-auth compile observados SUCCESS. `NIGHT-WOZ-078` intentó Draft→Ready y el conector falló antes de mutar por `Repository.fullDatabaseId`; #83 queda parked, no integrado.
- PR #76 legal/public routes sigue OPEN/stale/frozen.

## Owner CYCLE 080

**WOZ — `NIGHT-WOZ-079` — F3 / 20.2 runtime capacity evidence.**  
PRIMARY: REUSE #78 ya integrado; obtener evidencia runtime materialmente aplicable al target canónico **80 usuarios esperados / 160 usuarios de validación**, incluyendo latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin. Sin code/infra/provider mutation y sin tocar #83.  
CI-FALLBACK: F3/19.1 READ-ONLY evidence map solo si PRIMARY entra genuinamente en `WAITING_EXTERNAL_RUNTIME` tras iniciar una espera externa verificable.

## Día 16

### 16.1 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
Health/readiness/shutdown/timeouts/proxy trust integrado por #59. Separación física provider/DB/storage/bots/OAuth/secrets sigue externa.

### 16.2 — `[ 🟡 ] SOFTWARE DONE / EXTERNAL TAIL`
#61 integró promoción dependency-safe y rollback fail-closed. Deploy/staging/prod reales siguen externos.

## Día 17

### 17.1 — `[x] SOFTWARE DONE / INTEGRATED`
#65.

### 17.2 — `[x] SOFTWARE DONE / INTEGRATED`
#67.

## Día 18

### 18.1 — `[x] SOFTWARE DONE / INTEGRATED`
#68.

### 18.2 — `[ 🟡 ] RECONCILIATION SOFTWARE INTEGRATED / GLOBAL OPEN`
- [x] software reconciliation provider↔BeatGaler + exception queue slice: #73 merged;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund con evidencia aplicable;
- [ ] grace periods/productive billing behavior verificados donde corresponda.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
- [ ] dominio/API/status/support URLs/sender domains con evidencia productiva;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ 🟡 ] public legal routes `/privacy` y `/terms` existen en #76 pero no están integrados/deployed.

`NIGHT-WOZ-079` puede mapear evidencia solo READ-ONLY como fallback condicional; no cierra 19.1.

### 19.2 — `[ 🟡 ] CANONICAL LEGAL CANDIDATE / FROZEN ON SAFE REFRESH`
- [ 🟡 ] Privacy Policy v1.0 + Terms v1.0 owner-approved están en #76;
- [ 🟡 ] rutas públicas + links de entrada existen en #76;
- [ 🟡 ] Settings sigue con contenido temporal;
- [ ] safe history-preserving refresh de #76 sobre live baseline;
- [ ] independent legal review / production publication evidence;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno integrados por #75. External observability tails no se cierran con ese merge.

### 20.2 — `[ 🟡 ] HARNESS INTEGRATED / DURABLE WAITLIST CANDIDATE / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic parameterized harness: #78 merged;
- [x] approved expected peak: **80 simultaneous users** — RO/OWNER Issue #41 `5472774681`;
- [ ] required validation: **160 simultaneous users (2×)** con runtime evidence aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado en la prueba aplicable;
- [x] admission control + per-bot ceiling software exists;
- [ ] safety margin medida contra 80 expected;
- [ 🟡 ] durable user waitlist candidate #83 exact/scoped/CI-green pero Draft y no integrado; Draft→Ready tooling blocker confirmado por WOZ078.

**Owner runtime CYCLE 080:** WOZ079. Local/synthetic-only no cierra capacidad si no es materialmente aplicable. Incluso un runtime PASS no cierra 20.2 mientras #83 siga sin integrar. Si #79 mueve integration, #83 requerirá futura reconciliation history-preserving + fresh exact-head CI antes de readiness/integration.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
