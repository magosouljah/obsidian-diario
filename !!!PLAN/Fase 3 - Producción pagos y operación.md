# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 049:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 `woz/night-18.2-reconciliation @ fc831172c4c86d97cadb03801a6777777fd345bb` sigue OPEN/Ready/mergeable sobre base exacta `a9d35a3d...`; exact-head F3 reconciliation + D6/D7/compile/Required CI están verdes. `NIGHT-WOZ-048` es owner único para race-check + integración SAME #73.
- PR #76 `legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070` apareció después del CYCLE 048: OPEN/Ready/mergeable sobre base exacta `a9d35a3d...`. Contiene Privacy/Terms v1 owner-approved, rutas públicas `/privacy` y `/terms` y links de entrada; Test - Desktop Portability `33330007495`, D6 `33330007538`, D7 `33330007493` SUCCESS; Upgrade `33330007497` SKIPPED/no aplicable. Sigue faltando reemplazar el copy legal temporal/placeholders/contacto viejo en `SettingsPanel.tsx`. `NIGHT-AAA-045` es owner único de SAME #76 para ese reuse mínimo + fresh CI.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue OPEN/Ready/mergeable. Corrective de immutable pins conocido; previous write flow blocker. Frozen.
- `NIGHT-WOZ-047` no produjo RESULTADO DEL TURNO/handoff observable y queda superseded.
- F3/20.2 harness se conserva únicamente como CI-FALLBACK independiente de WOZ048 si PRIMARY #73 entra realmente en WAITING_CI/review/merge.

## Owners actuales

**WOZ — `NIGHT-WOZ-048` — F3 / 18.2 SAME #73 integration.**  
**AAA — `NIGHT-AAA-045` — F3 / 19.2 SAME #76 canonical legal Settings reuse.**

### WOZ PRIMARY — #73

1. Reuse exact-head green evidence on `fc831172...`.
2. Race-check integration/head/base; merge only if evidence still applies.
3. If baseline moved, narrow refresh + fresh applicable exact-head CI before merge.
4. No claim de 18.2 completo: provider/payment scenario tails remain.

**WOZ CI-FALLBACK:** F3/20.2 separate parameterized harness only while PRIMARY waits an external operation; no target invention, provider/infra load or #73/#75 overlap.

### AAA PRIMARY — #76

1. Reuse canonical `docs/legal/PRIVACY.md` + `docs/legal/TERMS.md` and existing Settings legal surfaces; no second legal UI.
2. Replace temporary August 11 placeholders/old contact in Settings with canonical v1 content/metadata only.
3. Preserve public routes/links from #76; no policy invention.
4. Focused tests + fresh exact-head applicable CI; merge only if race-clean and authorized.

**AAA CI-FALLBACK:** F2/13.2 read-only gap map only while #76 PRIMARY waits CI/review/merge.

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
- [ 🟡 ] reconciliación provider↔BeatGaler + cola de excepciones: PR #73 exact-base/exact-head green, integración asignada WOZ048;
- [ ] 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund con evidencia aplicable;
- [ ] grace periods/productive billing behavior verificados donde corresponda.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
- [ ] dominio/API/status/support URLs/sender domains con evidencia productiva;
- [ ] DNS/TLS/redirects/callbacks OAuth exactos;
- [ 🟡 ] public legal routes `/privacy` y `/terms` existen en candidate #76 pero aún no están integrados/deployed.

### 19.2 — `[ 🟡 ] CANONICAL LEGAL CANDIDATE / IN-APP SYNC ASSIGNED`
- [ 🟡 ] Privacy Policy v1.0 + Terms v1.0 owner-approved están en PR #76, effective/updated 2026-08-30;
- [ 🟡 ] rutas públicas + links de entrada existen en #76 y CI general está verde;
- [ 🟡 ] SettingsPanel mantiene copy temporal viejo/placeholders/contacto anterior; AAA045 debe sustituirlo por los documentos canónicos sin crear UI duplicada;
- [ ] independent legal review / production publication evidence permanece gate externo de release;
- [ ] soporte con intake/severidad/SLA/escalación aún abierto.

No marcar 19.2 `[x]` solo por tener documentos en un PR; falta integración, consistencia in-app y tails externos aplicables.

## Día 20

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE BLOCKED`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido pero write flow previo bloqueado; no fresh PASS, no integración.

### 20.2 — `[ 🟡 ] AUDIT DONE / CONDITIONAL HARNESS FALLBACK / NO PASS CLAIM`
Gap map vigente:
- capacity envelope `PARTIAL`;
- approved expected peak `GAP / prerequisite missing`;
- load/stress harness `GAP`;
- 2× peak proof `PENDING_EXTERNAL`;
- latency `GAP`;
- error/queue/recovery measurement `PARTIAL`;
- admission control + per-bot ceiling `EXISTS (software)`;
- safety margin `GAP`;
- durable user waitlist `GAP`.

WOZ048 puede trabajar el harness solo como CI-FALLBACK independiente después de que PRIMARY #73 entre realmente en espera externa. Resultado máximo: `HARNESS_READY`; no selecciona expected peak ni ejecuta carga productiva.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
