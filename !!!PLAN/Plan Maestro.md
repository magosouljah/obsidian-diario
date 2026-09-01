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
- **Integración estable final:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.
- **Último merge material:** PR #91 → `134a293985c314eb09c238115e3bcb71e79f1810`, parents `78dd55b72142e69ea32ba6c1ba6d43e246ac6843` + `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`. Exact-head portability/Required CI PASS. Claim máximo: F2/12.1 code corrective integrado; **public deploy + authenticated runtime + cold/warm evidence siguen pendientes**.
- **F0/0.20 OAuth rotation:** `[x] DONE`. #90 readiness software está integrado y RO registró owner-side credential replacement, deploy, fresh production OAuth E2E y eliminación del credential anterior. No se expusieron valores secretos.
- **F0:** núcleo técnico principal cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 = **18+**. 0.8 legal review `[x]` administrativamente por AI-assisted review + decisión RO; no implica compliance ni cierre de P0/P1 legales. #88 technical Authenticode seam integrado; production signing `NO-GO`. #89 OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; requiere refresh a `134a293...` o HEAD posterior + exact-head security CI.
- **F1:** D6–D10.1 PASS. D10.2 `[x] MAP COMPLETE` con resultado `ALPHA CANDIDATE NOT READY`. 1.7 debe resolver/clasificar blockers; 1.8 decisión RO final pendiente; 1.9 solo después de GO.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 code integrado vía #91; deploy público vigente requiere owner SSH key y luego runtime autenticado/cold-warm evidence. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment real externo. #76 stale/13+ contradice 18+. 19.2 sigue OPEN con 12 P0 + 14 P1 + P2/P3 + UNVERIFIED. #83 OPEN/DRAFT; runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 @ `f53d46f...` sigue evidence lineage stale; Windows Auth `33449587244` = FAILURE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 110

- `NIGHT-AAA-105`: handoff verificable → bounded startup corrective #91. Durante el mismo ciclo, #91 completó CI y quedó integrado concurrentemente como `134a293...`; por tanto F2/12.1 pasó a `INTEGRATED / PUBLIC DEPLOY + AUTH RUNTIME PENDING`, no PASS.
- `NIGHT-BBB-104`: sin RESULTADO DEL TURNO/matching handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`; último factual BBB099 `BLOCKED_STOP / AMBIGUOUS`.
- `NIGHT-WOZ-108`: sin RESULTADO DEL TURNO/matching handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio owner-side independiente: F0/0.20 OAuth rotation completada y sincronizada en F0 con credential replacement/deploy/E2E/revocation verificados. No se atribuye a worker nocturno.
- JOBS no modificó código BeatGaler ni infraestructura.

## D10.2 — mapa de readiness de alpha interna

- `PROVEN`: D6–D10.1, prerequisites internos y F0/0.20 OAuth rotation cerrada.
- `EXTERNAL_RUNTIME_BLOCKER`: F2/12.1 deploy del baseline `134a293...` + authenticated public runtime/cold-warm proof; requiere owner key, no worker sin credential.
- `HARD_BLOCKER`: F4/25.1 packaged Windows auth literal PASS.
- `CLOSE_OR_RO_EXCLUDE`: F2/13.2 durable Review y F2/15.1 recent-reauth/Empty Trash.
- `SECURITY_RECHECK_BEFORE_RO`: F0/0.9 #89 DNS-rebinding/SSRF P1 debe resolverse o no existir como P1 conocido al 1.8.
- `RO_APPLICABILITY_DECISION`: F3/18.2, 19.2 y 20.2 pueden quedar fuera de alpha 3–5 cuentas solo mediante decisión explícita de scope; exclusión de alpha no marca PASS de release.
- `RELEASE_ONLY/EXTERNAL`: production signing/notarization, hardware/tester matrix amplia y release/admin tails continúan `NO-GO`.

## OWNERS — CYCLE 110

### AAA — `NIGHT-AAA-106` — F2 / 13.2
PRIMARY: cerrar el gap probado de durable Review Save/Save All con el mínimo corrective: éxito/close/advance solo tras durable completion, failure visible/recoverable, no silent loss, focused Web/no-Tauri tests, un candidate bounded. **NO MERGE CYCLE 110.**  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-105` — F4 / 25.1 / #84
PRIMARY: atribuir tuple WDIO/Tauri; solo `HARNESS_ONLY_PROVEN` permite mínimo harness/service correction; refresh #84 a live head si clean; literal packaged Windows Auth + exact-head CI. **NO PRODUCT MUTATION / NO MERGE.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-109` — F0 / 0.9 / #89
PRIMARY: REUSE #89; reconciliar #88/#90/#91 integrados; history-preserving refresh sobre live `134a293...` o posterior; exact-head F0/0.9 security + Required CI; si exact/green/race-free, expected-head merge **#89 únicamente**.  
CI-FALLBACK: solo durante genuine `WAITING_CI`: **READ-ONLY F1/1.7 blocker-classification prep**; no implementation/plan mutation.

**Integration mutation authorization CYCLE 110 final: WOZ109 / PR #89 ONLY, después de refresh exact-base/head + all applicable CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado tras merge #91 y cierre OAuth

1. **F4/25.1 / #84:** causalidad harness/service → literal packaged Windows Auth PASS.
2. **F2/13.2 Review:** durable completion/no-silent-loss + Web/no-Tauri evidence, o exclusión RO explícita de alpha.
3. **F0/0.9 / #89:** refresh/revalidar/integrar DNS-rebinding P1 sin falsear independent pentest.
4. **F2/12.1 runtime externo:** deploy `134a293...` con owner SSH key + authenticated public startup + cold/warm evidence.
5. **F2/15.1 Empty Trash:** recent-reauth + strong confirmation + durable deterministic purge, o exclusión RO explícita.
6. **F1/1.7:** consolidar blockers y clasificar F3/18.2, 19.2, 20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.
7. **F1/1.8:** decisión RO final GO/NO-GO para 3–5 cuentas.
8. **F1/1.9:** ejecutar alpha solo después del GO.
9. **Release path paralelo:** F0 release/admin tails, F3 public/legal/provider/capacity, production signing/notarization/hardware/12–20 tester execution siguen abiertos.

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

AAA ejecuta `NIGHT-AAA-106` sobre F2/13.2; BBB `NIGHT-BBB-105` sobre #84; WOZ `NIGHT-WOZ-109` sobre #89 y posee la única conditional integration lane. F2/12.1 runtime queda como owner-key external tail. F0/0.20 está cerrado y no se repite. #85 sigue external-owned; #76/#83 no se reintentan sin cambio material. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 110 final; GitHub live prevalece si cambia después.
