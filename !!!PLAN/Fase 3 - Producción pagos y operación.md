# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo `Plan Maestro.md`.

**Baseline vivo CYCLE 053:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

## Estado owner / candidates

- PR #68 / 18.1 MERGED como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- PR #73 / 18.2 reconciliation MERGED como `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`; cierra solo software reconciliation/exception-queue slice.
- PR #76 `legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070` sigue OPEN/Ready/mergeable con base snapshot `a9d35a3d...`, stale contra live integration. AAA048 no produjo resultado; #76 queda frozen hasta disponer de refresh history-preserving seguro. Canonical Privacy/Terms + public routes existen; Settings canonical sync sigue pendiente.
- PR #75 `woz/night-20.1-observability @ bb493b3755ba1a42b4c5cfe7f3b885edc544c61f` sigue frozen por corrective/write-flow blocker.
- PR #77 sigue CLOSED/unmerged y no puede reabrirse. Source branch `woz/night-20.2-capacity-harness @ 50aac3f0c700a88e1f058372c23ee1d96ecf247a` fue verificado previamente exact-base, ahead 2 / behind 0, dos archivos harness/test. No replacement PR apareció antes de CYCLE 053. `NIGHT-WOZ-052` es owner único para una sola replacement PR autorizada.

## Owners actuales

**WOZ — `NIGHT-WOZ-052` — F3 / 20.2 one authorized replacement PR from existing source artifact.**

### WOZ PRIMARY

1. Fresh compare de live integration contra `50aac3f0...`; no asumir el snapshot anterior si cambió algo.
2. Reutilizar exclusivamente ese branch; crear exactamente una replacement PR si duplicate-check sigue limpio.
3. Preservar delta de dos archivos harness/test, target explícito y limitación synthetic/local-only.
4. Focused deterministic tests + fresh exact-head CI.
5. Merge solo si exact-head green/race-clean; máximo claim `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.

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

### 20.1 — `[ 🟡 ] IN PROGRESS / INTERNAL SLICE BLOCKED`
PR #75 contiene structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno. Corrective de immutable pins conocido; write-flow blocker persiste. No fresh PASS ni integración.

### 20.2 — `[ 🟡 ] REPLACEMENT CONTINUATION ASSIGNED / NO PASS CLAIM`
Gap map vigente:
- capacity envelope `PARTIAL`;
- approved expected peak `GAP / prerequisite missing`;
- load/stress harness source artifact `50aac3f0...` listo para una replacement PR si compare sigue limpio;
- 2× peak proof `PENDING_EXTERNAL`;
- latency `GAP` hasta ejecución aplicable;
- error/queue/recovery measurement `PARTIAL`;
- admission control + per-bot ceiling `EXISTS (software)`;
- safety margin `GAP`;
- durable user waitlist `GAP`.

Aun integrado el harness, resultado máximo `HARNESS_READY`; nunca runtime capacity PASS sin target aprobado + ejecución real aplicable.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
