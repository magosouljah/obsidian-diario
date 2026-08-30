# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 051:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation **MERGED** como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`, parents `a9d35a3d...` + `fc831172...`. Cierra solo el software slice de reconciliation/exception queue; global 18.2 sigue abierto.
- PR #76 `legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070` sigue OPEN sin cambio de head desde CYCLE 050. Compare contra live integration conserva merge-base `a9d35a3d...`; el candidate sigue stale/diverged. Canonical Privacy/Terms + public routes existen; Settings stale sigue pendiente. `NIGHT-AAA-047` es owner único para narrow refresh + canonical Settings reuse + fresh exact-head CI.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue frozen por corrective/write-flow blocker.
- PR #77 `woz/night-20.2-capacity-harness @ 204a03fc48d161b6943f7b11bea2bfc16bf54b05` sigue CLOSED/unmerged y sin cambio de head. Su ejecución prematura anterior no cuenta como evidencia. `NIGHT-WOZ-050` lo reutiliza explícitamente como PRIMARY; no crear artifact duplicado.

## Owners actuales

**AAA — `NIGHT-AAA-047` — F3 / 19.2 SAME #76 refresh + canonical legal Settings reuse.**  
**WOZ — `NIGHT-WOZ-050` — F3 / 20.2 REUSE SAME #77 harness.**

### AAA PRIMARY — #76

1. Narrow refresh SAME #76 onto `a306e3b3...`.
2. Reuse canonical legal docs and existing Settings legal surfaces; no second UI or policy invention.
3. Replace stale placeholders/old contact only with canonical v1 content/metadata.
4. Focused tests + fresh exact-head applicable CI; merge only if race-clean.

**AAA CI-FALLBACK:** F2/13.2 read-only gap map only while PRIMARY waits CI/review/merge.

### WOZ PRIMARY — #77

1. Confirm #77 remains CLOSED/unmerged and delta is only intended harness/test files.
2. Reuse SAME #77; refresh onto `a306e3b3...`; reopen only if available.
3. Preserve explicit target requirement and synthetic/local-only limitation.
4. Focused deterministic tests + fresh exact-head CI.
5. Maximum claim `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`; no provider/production load and no 20.2 PASS.

**WOZ CI-FALLBACK:** NONE.

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

### 18.2 — `[ 🟡 ] RECONCILIATION SOFTWARE INTEGRATED / GLOBAL OPEN`
- [x] software reconciliation provider↔BeatGaler + exception queue slice: PR #73 merged as `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund con evidencia aplicable;
- [ ] grace periods/productive billing behavior verificados donde corresponda.

No convertir el merge de #73 en full 18.2 PASS.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
- [ ] dominio/API/status/support URLs/sender domains con evidencia productiva;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ 🟡 ] public legal routes `/privacy` y `/terms` existen en #76 pero aún no están integrados/deployed.

### 19.2 — `[ 🟡 ] CANONICAL LEGAL CANDIDATE / REFRESH ASSIGNED`
- [ 🟡 ] Privacy Policy v1.0 + Terms v1.0 owner-approved están en #76, effective/updated 2026-08-30;
- [ 🟡 ] rutas públicas + links de entrada existen en #76;
- [ 🟡 ] #76 sigue stale/diverged tras #73; AAA047 debe refrescar y sincronizar Settings con canonical docs;
- [ ] independent legal review / production publication evidence permanece gate externo;
- [ ] soporte con intake/severidad/SLA/escalación aún abierto.

## Día 20

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE BLOCKED`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido pero write flow previo bloqueado; no fresh PASS, no integración.

### 20.2 — `[ 🟡 ] HARNESS PRIMARY ASSIGNED / NO PASS CLAIM`
Gap map vigente:
- capacity envelope `PARTIAL`;
- approved expected peak `GAP / prerequisite missing`;
- load/stress harness `GAP` hasta que #77 sea legítimamente refrescado/validado;
- 2× peak proof `PENDING_EXTERNAL`;
- latency `GAP`;
- error/queue/recovery measurement `PARTIAL`;
- admission control + per-bot ceiling `EXISTS (software)`;
- safety margin `GAP`;
- durable user waitlist `GAP`.

#77 aporta un harness sintético reusable con target explícito, concurrency/queue/latency/errors/recovery, pero su creación prematura fue invalidada. WOZ050 puede legitimarlo como SAME artifact; aun integrado, resultado máximo `HARNESS_READY`, nunca runtime capacity PASS.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
