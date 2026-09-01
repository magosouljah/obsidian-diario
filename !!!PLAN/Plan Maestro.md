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

## Estado vivo — NIGHT-JOBS-113

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight/final assignment:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.
- **Último merge material:** PR #91 → `134a293985c314eb09c238115e3bcb71e79f1810`.
- **F4/Windows Auth cambio material:** BBB107 abrió PR #93 exact-base `134a293...` @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, harness/evidence-only. Windows Auth run `33468863393` SUCCESS, job `99734302105` SUCCESS incluyendo isolated auth assertions; D6/D7/Desktop Portability/Windows Import/secret scan también SUCCESS. Claim procesado: `WINDOWS_AUTH_CANDIDATE_EXACT_GREEN / NO_MERGE`. WOZ112 recibe la única integration lane sobre #93.
- **F2/12.1:** #91 integrated; #92 OPEN/Ready/mergeable @ `9947380...`, exact base `134a293...`, exact-head checks observados verdes. Se parquea CYCLE113 para priorizar #93; 12.1 sigue NOT_PASS y necesita luego #92/equivalente + deploy/runtime/cold-warm proof.
- **F2/13.2:** durable Review sigue gap probado; AAA109.
- **F2/15.1:** Empty Trash recent-reauth/strong confirmation/durable purge pasa a BBB108; no false success.
- **F0/0.9:** #89 OPEN/Ready @ `daf87da6...`, stale y parked; debe refresh/revalidate antes de 1.8.
- **F1:** D6–D10.1 PASS; D10.2 map complete/NOT_READY. Windows Auth ya tiene exact-green candidate pero aún no evidence-integrated en canonical baseline.
- **F3:** 18.2 provider/payment real externo; 19.2 legal implementation sigue abierto; #83/runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto pese al candidate verde de Windows Auth; production signing/notarization/hardware/tester execution continúan externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 113

- `NIGHT-AAA-108`: sin RESULTADO DEL TURNO/matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-107`: `CANDIDATE_EXACT_GREEN / NO_MERGE`; PR #93 exact base/head y literal Windows Auth SUCCESS verificados; no product mutation. Transferencia de ownership de #93 a WOZ112 para integración condicional.
- `NIGHT-WOZ-111`: sin RESULTADO DEL TURNO/matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- JOBS no modificó código BeatGaler ni infraestructura.

## D10.2 — mapa de readiness alpha interna

- `PROVEN`: D6–D10.1 y F0/0.20 cerrados.
- `ACTIVE_EVIDENCE_BLOCKER`: #93 Windows packaged Auth exact-green candidate pendiente integration review.
- `ACTIVE_RUNTIME_BLOCKER`: F2/12.1 #92/equivalente + posterior deployment/runtime/cold-warm proof.
- `CLOSE_OR_RO_EXCLUDE`: F2/13.2 durable Review y F2/15.1 Empty Trash.
- `SECURITY_RECHECK_BEFORE_RO`: F0/0.9 #89 DNS-rebinding/SSRF P1.
- `RO_APPLICABILITY_DECISION`: F3/18.2, 19.2, 20.2 solo pueden salir de alpha 3–5 cuentas mediante decisión explícita de scope; excluir de alpha no marca PASS de release.
- `RELEASE_ONLY/EXTERNAL`: production signing/notarization, hardware/tester matrix amplia y release/admin tails continúan `NO-GO`.

## OWNERS — CYCLE 113

### AAA — `NIGHT-AAA-109` — F2 / 13.2
PRIMARY: minimum durable Review Save/Save All completion/no-silent-loss corrective; visible success only after durable completion; failure/retry/partial Save All; focused Web/no-Tauri tests; bounded candidate. **NO MERGE.**  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-108` — F2 / 15.1
PRIMARY: Empty Trash strong confirmation + canonical recent-reauth reuse + durable deterministic purge/no-false-success; bounded candidate, **NO MERGE**. STOP if auth/session core redesign is required.  
CI-FALLBACK: only during genuine `WAITING_CI`: F1/1.7 blocker classification READ-ONLY, evidence-backed, no plan/code/provider mutation or RO decision.

### WOZ — `NIGHT-WOZ-112` — F4 / 25.1 / #93
PRIMARY: REUSE #93; verify bounded harness-only semantics + exact base/head + literal Windows Auth job + all applicable required checks; if exact/green/race-free, expected-head merge **#93 only** and verify merge SHA/parents. Maximum claim does not close global 25.1.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 113: WOZ112 / PR #93 ONLY, after exact-base/head + all applicable required CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde GitHub vivo

1. **F4/25.1 / #93:** exact-green Windows Auth candidate ya existe; integrar evidencia bounded primero.
2. **F2/13.2:** durable Review completion/no-silent-loss, o explicit RO alpha exclusion.
3. **F2/15.1:** recent-reauth + strong confirmation + durable deterministic purge, o explicit RO alpha exclusion.
4. **F0/0.9 / #89:** refresh/revalidate DNS-rebinding/SSRF P1 después de liberar current integration lane.
5. **F2/12.1 / #92:** refresh/revalidate si baseline cambia, integrar candidate signed-out loader y después deployment/runtime proof signed-out/authenticated + cold/warm.
6. **F1/1.7:** consolidar blockers y F3 18.2/19.2/20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.
7. **F1/1.8:** RO GO/NO-GO para alpha 3–5 cuentas; **1.9** solo después de GO.
8. **Release path paralelo:** F0 1.2/2.2, productive signing/notarization, F3 provider/legal/capacity y tester/hardware evidence permanecen abiertos.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no bot free; normal exclusivity per vault.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-109`; BBB `NIGHT-BBB-108`; WOZ `NIGHT-WOZ-112` y posee la única conditional integration lane sobre #93. #92 y #89 quedan parked/unassigned CYCLE113. #85 sigue external-owned; #76/#83 no se reintentan sin cambio material. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 113; GitHub live prevalece si cambia después.
