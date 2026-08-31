# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 058:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation MERGED como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; cierra solo software reconciliation/exception-queue slice.
- PR #78 / 20.2 capacity harness MERGED como `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`, parents `a306e3b3...` + `50aac3f0...`; claim máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- PR #76 `legal/privacy-terms-v1 @ 36d218609...` sigue OPEN/stale/frozen. Canonical Privacy/Terms + public routes existen; Settings canonical sync sigue pendiente.
- PR #75 `woz/night-20.1-observability @ bb493b375...` sigue OPEN/stale. Delta observado contra live integration: 4 intended files, ahead 4 / behind 8, merge-base `a9d35a3d...`. Corrective conocido: immutable Action pins. `NIGHT-WOZ-057` es owner único para refresh/corrective; no merge este ciclo mientras BBB/#79 posee integration.
- PR #77 CLOSED/unmerged; superseded por #78.

## Owners actuales

**WOZ — `NIGHT-WOZ-057` — F3 / 20.1 SAME #75.**

### WOZ PRIMARY
1. Recheck live integration y duplicate-check #75.
2. REUSE-FIRST: conservar únicamente los 4 files intended de observability software.
3. Aplicar solo el corrective conocido de immutable pins y un history-preserving refresh al live baseline si el flujo seguro lo permite.
4. Focused tests + fresh exact-head CI; no external observability claims.
5. **No mergear en CYCLE 058**: BBB/#79 es la única mutación de integration autorizada. Dejar candidate listo para el próximo race-check.

### WOZ CI-FALLBACK
F3/20.2 READ-ONLY residual gap map únicamente si PRIMARY queda genuinamente `WAITING_CI`/review: approved peak, 2× runtime, latency, safety margin, durable waitlist. Sin writes, sin provider load, sin PASS claim. STOP ante overlap y recheck PRIMARY.

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
- [x] software reconciliation provider↔BeatGaler + exception queue slice: PR #73 merged as `a306e3b3...`;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund con evidencia aplicable;
- [ ] grace periods/productive billing behavior verificados donde corresponda.

No convertir #73 en full 18.2 PASS.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
- [ ] dominio/API/status/support URLs/sender domains con evidencia productiva;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ 🟡 ] public legal routes `/privacy` y `/terms` existen en #76 pero no están integrados/deployed.

### 19.2 — `[ 🟡 ] CANONICAL LEGAL CANDIDATE / FROZEN ON SAFE REFRESH`
- [ 🟡 ] Privacy Policy v1.0 + Terms v1.0 owner-approved están en #76, effective/updated 2026-08-30;
- [ 🟡 ] rutas públicas + links de entrada existen en #76;
- [ 🟡 ] Settings sigue con contenido temporal; sincronización canónica pendiente;
- [ ] safe history-preserving refresh de #76 sobre live baseline;
- [ ] independent legal review / production publication evidence;
- [ ] soporte con intake/severidad/SLA/escalación.

## Día 20

### 20.1 — `[ 🟡 ] IN PROGRESS / ASSIGNED WOZ057`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido; candidate stale. No fresh PASS ni integración todavía.

### 20.2 — `[ 🟡 ] HARNESS SOFTWARE INTEGRATED / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic local/synthetic parameterized harness: PR #78 merged `63c9f8c9...`;
- [ ] approved expected peak;
- [ ] real/applicable 2× peak proof;
- [ ] latency target/result;
- [ 🟡 ] error/queue/recovery measurement partial;
- [x] admission control + per-bot ceiling software exists;
- [ ] safety margin;
- [ ] durable user waitlist.

#78 no autoriza full 20.2 PASS.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
