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

## Estado vivo — NIGHT-JOBS-110

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight JOBS:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843`.
- **Último merge material:** PR #90 → `78dd55b72142e69ea32ba6c1ba6d43e246ac6843`, parents `1dbf60e58ca970c47d387b303e141e30e2b8eef5` + `3f2063cf16fe63913dced6d57dc8a6cb46e12169`. Claim máximo: F0/0.20 software/readiness + HEAD secret scan integrated; **actual OAuth credential rotation/deploy/E2E/revoke sigue externo y NOT DONE**.
- **F0:** núcleo técnico principal cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 = **18+**. 0.8 legal review está `[x]` administrativamente por AI-assisted review + decisión RO; no implica compliance ni cierre de P0/P1 legales. #88 technical/preparatory Authenticode seam integrado; production signing `NO-GO`. #89 OPEN/Ready @ `daf87da6...`, base stale `816f946c...`; requiere refresh al live head + exact-head security CI. #90 readiness software integrado; owner rotation real externa.
- **F1:** D6–D10.1 PASS. D10.2 `[x] MAP COMPLETE` con resultado `ALPHA CANDIDATE NOT READY`. 1.7 debe resolver/clasificar blockers; 1.8 decisión RO final pendiente; 1.9 solo después de GO.
- **F2:** 11.1/11.2/12.2 cerrados. `NIGHT-AAA-105` aisló el stall de startup y produjo PR #91 @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`, exact base `78dd55b...`: deadline de 30 s solo para `initialize`/`verify`/`get_index`, sin timeout genérico al loader ni a transfers largos. Estado factual = `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`. Integración + runtime público autenticado + cold/warm timing siguen pendientes. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment real sigue externo. #87 security/status software integrado. #76 stale/13+ contradice 18+. AI legal review está registrada, pero 19.2 sigue OPEN con 12 P0 + 14 P1 + P2/P3 + UNVERIFIED. #83 OPEN/DRAFT; runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 @ `f53d46f...` sigue evidence lineage stale; Windows Auth run `33449587244` = FAILURE. Generic CI viejo no sustituye journey literal.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 110

- `NIGHT-AAA-105`: matching Issue #41 handoff verificable → `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`. Candidate PR #91 @ `35d44a0d...`, base `78dd55b...`. Root cause: `WebTransportWorkerClient.request()` podía quedar pendiente indefinidamente si el Worker no respondía ni fallaba. Corrective bounded: deadline 30 s solo para bootstrap-critical `initialize`/`verify`/`get_index`; silent Worker se termina y retry usa runtime fresco. No PASS de 12.1 todavía.
- `NIGHT-BBB-104`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`. Último factual de línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`.
- `NIGHT-WOZ-108`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio material independiente: PR #90 quedó `MERGED` como `78dd55b...`; F0/0.20 software readiness integrado, owner-side rotation sigue externa.
- PR #91 exact-head CI al momento de asignar AAA106: Web Production Build, D6, D7, temp-auth compile y F0/0.20 secret scan SUCCESS; `Test - Desktop Portability` seguía `in_progress`. No se promueve final green antes de cierre literal de todos los checks aplicables.
- JOBS no modificó código BeatGaler ni infraestructura.

## D10.2 — mapa de readiness de alpha interna

- `PROVEN`: D6–D10.1 y prerequisites internos aceptados.
- `HARD_BLOCKER`: F2/12.1 startup Web hasta integración + runtime público del fix.
- `HARD_BLOCKER`: F4/25.1 packaged Windows auth literal PASS.
- `CLOSE_OR_RO_EXCLUDE`: F2/13.2 durable Review y F2/15.1 recent-reauth/Empty Trash.
- `SECURITY_RECHECK_BEFORE_RO`: F0/0.9 #89 P1 DNS-rebinding/SSRF debe quedar resuelto o no conocido al momento de 1.8.
- `RO_APPLICABILITY_DECISION`: F3/18.2 payments/provider, F3/19.2 legal implementation y F3/20.2 runtime160 pueden quedar fuera de una alpha 3–5 cuentas solo mediante decisión explícita de scope; exclusión de alpha no marca PASS para release.
- `RELEASE_ONLY/EXTERNAL`: production signing/notarization, hardware/tester matrix amplia y release/admin tails siguen `NO-GO`.

## OWNERS — CYCLE 110

### AAA — `NIGHT-AAA-106` — F2 / 12.1 / PR #91
PRIMARY: REUSE #91; terminar exact-head applicable CI y, solo si exact-base/head, scope-bounded, mergeable, green y race-free, mergear **#91 únicamente** con expected-head protection. Maximum post-merge claim = `CODE_FIX_INTEGRATED / PUBLIC_RUNTIME_PENDING`.  
CI-FALLBACK: solo durante genuine `WAITING_CI` en #91: **READ-ONLY F2/13.2 closure map**; no branch/PR/code mutation.

### BBB — `NIGHT-BBB-105` — F4 / 25.1 / #84
PRIMARY: atribuir tuple WDIO/Tauri; solo `HARNESS_ONLY_PROVEN` permite mínimo harness/service correction; refresh #84 a live head si clean; literal packaged Windows Auth + exact-head CI. **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-109` — F0 / 0.9 / #89
PRIMARY: REUSE #89; reconciliar #88/#90 integrados; history-preserving refresh al live head observado en su turno; exact-head F0/0.9 security + Required CI. **NO MERGE CYCLE 110** para no competir con #91.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 110: AAA106 / PR #91 ONLY, exact-base/head + all applicable CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde cero CYCLE 110

1. **F2/12.1 / #91:** completar CI exact-head e integración; luego obtener runtime público autenticado que salga de `Loading Galer` o caiga deterministicamente al estado recuperable existente.
2. **F4/25.1 / #84:** causalidad harness/service → literal packaged Windows Auth PASS.
3. **F2/13.2 Review:** durable Save/Save All completion/no-silent-loss + Web/no-Tauri evidence, o exclusión RO explícita de alpha.
4. **F2/15.1 Empty Trash:** recent-reauth + strong confirmation + durable deterministic purge, o exclusión RO explícita de alpha.
5. **F0/0.9 / #89:** refresh/revalidar DNS-rebinding P1 sin falsear independent pentest.
6. **F1/1.7:** consolidar blockers aplicables y clasificar F3/18.2, 19.2 y 20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.
7. **F1/1.8:** decisión RO final GO/NO-GO para 3–5 cuentas.
8. **F1/1.9:** ejecutar alpha solo después del GO.
9. **Release path paralelo:** F0 release/admin tails; F3 public/legal/provider/capacity; production signing/notarization/hardware/12–20 tester execution siguen abiertos.

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

AAA ejecuta `NIGHT-AAA-106`; BBB `NIGHT-BBB-105`; WOZ `NIGHT-WOZ-109`. Solo AAA106 puede mutar integration y exclusivamente sobre #91 si exact-green/race-free. WOZ109 prepara #89 sin merge; BBB105 no toca producto ni integration. #85 sigue external-owned. #76/#83 no se reintentan sin cambio material. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 110; GitHub live prevalece si cambia después.
