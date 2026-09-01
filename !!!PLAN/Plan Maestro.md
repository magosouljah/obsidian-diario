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

## Estado vivo — NIGHT-JOBS-109

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.
- **Último merge material:** #88 → `1dbf60e58ca970c47d387b303e141e30e2b8eef5`, parents exactos `38517c8065063206fed530028e4e8d20208f3807` + `dcf3e13864d02cd4ffc958dc3a31b7411af6145a`.
- **F0:** núcleo técnico principal cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 = **18+**. **0.8 Legal launch review = `[x]` administrativamente por AI-assisted review + decisión RO de deferir counsel; no implica compliance ni cierre de P0/P1 legales.** #88 cerró únicamente F0/0.7 technical/preparatory Authenticode+RFC3161; production signing sigue `NO-GO`. #89 OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; requiere refresh a `1dbf60e...` + fresh exact-head CI. #90 readiness-only; rotación real externa.
- **F1:** D6–D10.1 PASS. **D10.2 `[x] MAP COMPLETE`** sobre `1dbf60e...`; resultado factual = `ALPHA CANDIDATE NOT READY`. 1.7 hereda resolución: hard blockers F2/12.1 + F4/25.1; F2/13.2 y 15.1 requieren cierre o exclusión RO explícita. F0/0.9 P1 debe revalidarse antes de 1.8. F3/18.2, 19.2 y 20.2 requieren decisión explícita `IN_ALPHA`/`EXCLUDED_FROM_ALPHA` sin alterar sus gates de release. **1.8 decisión RO final sigue pendiente.**
- **F2:** 11.1/11.2/12.2 cerrados. Infra pública principal probada, pero normal apex sigue sin evidencia nueva de salida de `Loading Galer`. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment external. #87 security/status software integrado. #76 stale/13+ contradice 18+. AI legal review está registrada, pero 19.2 sigue OPEN con 12 P0 + 14 P1 + P2/P3 + implementación/riesgos UNVERIFIED. #83 OPEN/DRAFT y runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 evidence lineage @ `f53d46f...`, stale base `816f946c...`; generic old-head CI green, pero Windows Auth run `33449587244` = FAILURE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 109

- `NIGHT-AAA-104`: no RESULTADO DEL TURNO ni matching Issue #41 handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-103`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`. Último resultado verificable de línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- `NIGHT-WOZ-107`: no RESULTADO DEL TURNO ni matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio factual independiente de esos resultados: PR #88 fue `MERGED` con autorización RO como `1dbf60e...`; candidate `dcf3e138...` tuvo Test Desktop Portability, F4 Release Controls, F4 Functional Matrix, Windows Authenticode seam, D6, D7, Web Production Build y Windows Import en SUCCESS. Claim máximo: technical/preparatory signing seam integrado; production signing continúa NO-GO.
- PR #89 live: OPEN/Ready/mergeable, head `daf87da6...`, stale base `816f946c...`; refresh exact-head obligatorio.
- PR #84 live: OPEN/Ready/mergeable, head `f53d46f...`, stale base `816f946c...`; literal Windows Auth continúa NOT_PASS.
- No otro PASS nuevo procesable. JOBS no modificó código BeatGaler ni infraestructura.

## D10.2 — mapa de readiness de alpha interna

**Snapshot:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.

- `PROVEN`: D6–D10.1 y prerequisites internos ya aceptados.
- `HARD_BLOCKER`: F2/12.1 startup Web normal (`Loading Galer`).
- `HARD_BLOCKER`: F4/25.1 packaged Windows auth literal PASS.
- `CLOSE_OR_RO_EXCLUDE`: F2/13.2 durable Review y F2/15.1 recent-reauth/Empty Trash.
- `SECURITY_RECHECK_BEFORE_RO`: F0/0.9 #89 P1 DNS-rebinding/SSRF debe quedar resuelto o no existir como P1 conocido al momento de 1.8.
- `RO_APPLICABILITY_DECISION`: F3/18.2 payments/provider, F3/19.2 legal implementation y F3/20.2 runtime160 pueden quedar fuera de una alpha 3–5 cuentas solo mediante decisión explícita de scope; su exclusión de alpha no los marca PASS para release.
- `RELEASE_ONLY/EXTERNAL`: production signing/notarization, amplia hardware/tester matrix y release/admin tails continúan `NO-GO` y no impiden que el mapa D10.2 esté completo.

**Salida:** D10.2 está cerrado como mapa; 1.7 resuelve/clasifica los blockers. 1.8 autoriza o rechaza la alpha. 1.9 ejecuta solo después de 1.8.

## OWNERS — CYCLE 109

### AAA — `NIGHT-AAA-105` — F2 / 12.1
PRIMARY: reproducir `Loading Galer`, aislar primer bootstrap phase irresuelto y hacer mínimo corrective Web-only con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy ⇒ STOP.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-104` — F4 / 25.1
PRIMARY: consumir tuple sanitizado `POST /plugin%3Awdio%7Cget_window_states` / `cross-origin`, demostrar atribución WDIO/Tauri y corregir solo harness/service interception si queda `HARNESS_ONLY_PROVEN`; refresh history-preserving de #84 al baseline vivo si es seguro; packaged Windows Auth literal + exact-head CI; **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-108` — F0 / 0.9 / PR #89
PRIMARY: REUSE #89; reconciliar audit con #88 ya integrado, refresh history-preserving sobre `1dbf60e...` + fresh exact-head security/Required CI. Si todo applicable queda SUCCESS y race-free, WOZ es el único autorizado a mergear **#89 solamente** con expected-head y verificación de parents. Maximum claim = AI-assisted security software slice + DNS-rebinding P1 fixed; no external pentest/F0 global/release claim.  
CI-FALLBACK: solo si PRIMARY entra genuinamente `WAITING_CI`: inspección **READ-ONLY** de #90, separando software readiness de owner/deployment/credential evidence; **NO MUTATION / NO MERGE / NO ROTATION**. Volver a #89 al resolver CI.

**Integration mutation authorization CYCLE 109: WOZ108 / PR #89 ONLY, después de refresh exact-base, exact-head applicable CI green y race-free expected head.**

## Camino crítico global — recalculado desde cero CYCLE 109

1. **F2/12.1 public Web startup:** `Loading Galer` debe terminar correctamente; bloquea tester/browser evidence y readiness de alpha.
2. **F4/25.1 windows/auth:** harness/service attribution → literal packaged PASS requerido.
3. **F2/13.2 Review:** durable Save/Save All completion/no-silent-loss + executable Web/no-Tauri evidence, o decisión RO explícita de excluirlo de la alpha.
4. **F2/15.1 Empty Trash:** recent-reauth seam + strong confirmation + deterministic purge, o decisión RO explícita de exclusión para alpha.
5. **F0/0.9 security:** #89 debe refresh/revalidar e integrar el P1 DNS-rebinding sin falsear external pentest; recheck obligatorio antes de 1.8.
6. **F1/1.7:** cerrar blockers aplicables y producir clasificación final `IN_ALPHA` / `EXCLUDED_FROM_ALPHA` para F3/18.2, 19.2 y 20.2.
7. **F1/1.8:** decisión RO final GO/NO-GO para 3–5 cuentas.
8. **F1/1.9:** ejecutar alpha únicamente después del GO.
9. **Release path paralelo:** F0 release/admin tails; F3 public/legal/provider/capacity; signing/notarization/hardware/12–20 tester execution y demás gates siguen abiertos y no se marcan PASS por una alpha acotada.

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

AAA ejecuta `NIGHT-AAA-105`; BBB `NIGHT-BBB-104`; WOZ `NIGHT-WOZ-108`. **D10.2 no necesita otro turno de mapeo salvo invalidación factual; el siguiente trabajo de F1 es 1.7.** Solo WOZ108 puede mutar integration y únicamente para expected-head #89 después de refresh al baseline vivo + exact-head applicable CI verde + recheck race-free. #85 permanece external-owned. #90 solo READ-ONLY fallback de WOZ si #89 espera CI. No retry #76/#83 sin cambio material de tooling/surface. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 109; GitHub live prevalece si cambia después.
