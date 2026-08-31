# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## Reglas de autoridad

- GitHub/runtime vivo prevalece sobre snapshots viejos.
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Cada pieza material tiene un solo owner.
- JOBS dirige/sincroniza; no modifica código BeatGaler ni infraestructura.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-102

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** #79 → `816f946c...`.
- **F0:** núcleo técnico interno cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 canónica: **18+**.
- **F1:** D6–D10.1 PASS. D10.2 sigue `[ 🟡 ] RO / ALPHA DECISION`; `NIGHT-WOZ-101` recibe mapa READ-ONLY de readiness para reducir el blocker sin lanzar alpha.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime bloqueado por execution surface; 13.1 frozen; 13.2 durable Review gap = `NIGHT-AAA-098`, NO MERGE; 14.1 #81 parked; 15.1 bloqueado por recent-reauth seam + strong confirmation/action boundary.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment external; 19.1 partial/external. PR #85 apareció owner-owned @ `5225fae856ac8e5e094bc76f4a70383296fa224b`, exact base live, corrigiendo el deploy PowerShell que falló en owner-machine; no worker nocturno lo toca mientras ese ownership externo esté activo. #76 sigue stale y contradice 18+; WOZ100 quedó BLOCKED porque su superficie no soporta el refresh history-preserving requerido. #83 sigue OPEN/DRAFT/tooling-blocked; runtime 160 UNVERIFIED.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #74 exact `d1593d3...`; #84 exact `28c3810c...`; Windows Auth literal sigue FAILURE. `NIGHT-BBB-097` recibe únicamente causal diagnostic sanitizado, NO PRODUCT MUTATION / NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 102

- `NIGHT-AAA-097`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff ni candidate 13.2 material.
- `NIGHT-BBB-096`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result ni matching Issue #41 handoff; #84 permanece unchanged/red.
- `NIGHT-WOZ-100`: `BLOCKED_STOP / PREFLIGHT_COMPLETE / NO_MUTATION`; Issue #41 `5485787222`. #76 no puede completarse safely desde la superficie soportada porque falta branch refresh/history-preserving operation.
- PR #85 es un cambio factual nuevo externo/owner-owned; exact base `816f946c...`, head `5225fae...`, un archivo `scripts/deploy-web-production.ps1`; CI empezó sobre ese exact head. No se reclama PASS global ni integración.
- No BeatGaler merge ni integration mutation en este ciclo.

## OWNERS — CYCLE 102

### AAA — `NIGHT-AAA-098` — F2 / 13.2
PRIMARY: mínimo Review Save/Save All durable action-boundary correction; per-beat `saved/conflict/failed`, retry/no-silent-loss, focused Web/no-Tauri call-spies; one bounded candidate + fresh exact-head CI; **NO MERGE**.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-097` — F4 / 25.1
PRIMARY: diagnostic-only primer `unexpected-request` sanitizado en #84; unchanged literal assertions + fresh packaged Windows run. Minimum harness correction solo si la traza prueba `HARNESS_ONLY`; product-side ⇒ STOP. **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-101` — F1 / D10.2
PRIMARY: mapa READ-ONLY de readiness alpha interna 3–5 cuentas; clasificar `PROVEN / BLOCKED_EXTERNAL / RO_DECISION_REQUIRED / BLOCKED_BY_F2/F3/F4` con evidencia exacta; no lanzar alpha ni mutar infra/provider.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 102: NONE.**

## Camino crítico global — recalculado CYCLE 102

1. **F4/25.1 windows/auth:** identificar primer unexpected request → atribuir harness/service/product → literal packaged PASS requerido.
2. **F2/13.2 Review:** durable completion/no-silent-loss + executable Web/no-Tauri evidence.
3. **F3/19.1 deploy:** dejar terminar/validar owner-owned #85 sin doble ownership; luego comprobar deployment real, SPA fallback y public surface.
4. **F3/19.2 #76:** requiere superficie capaz de history-preserving refresh antes de reconciliar 18+ + Settings canonical legal copy.
5. **F2/15.1 Empty Trash:** bounded recent-reauth seam bajo owner auth/session correcto, luego strong confirmation + deterministic purge.
6. **F3/20.2 #83/runtime:** supported Ready tooling debe cambiar materialmente; después runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin.
7. **F2/12.1:** real-browser cold/warm requiere surface ejecutable.
8. **F3/18.2:** provider/staging/payment scenarios reales.
9. **F1/D10.2 + F0/F4 external/RO tails:** alpha decision, signing/notarization/hardware/tester execution.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets permanecen control-side; clients usan temporary auth.
- Shared-bot fallback solo cuando no hay bot libre; exclusivity per vault normal.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-098`; BBB `NIGHT-BBB-097`; WOZ `NIGHT-WOZ-101`. Nadie puede mutar integration. No tocar PR #85 mientras siga owner-owned activo. No retry #76 con la misma superficie incapaz de refresh. No retry #83 sin material supported-tooling change. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 102; GitHub live prevalece si cambia después.
