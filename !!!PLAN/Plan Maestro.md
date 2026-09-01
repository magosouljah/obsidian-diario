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

## Estado vivo — NIGHT-JOBS-104

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** #79 → `816f946c...`.
- **F0:** núcleo técnico interno cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 canónica: **18+**. **0.8 Legal launch review = `[x]` administrativamente: AI-assisted review completed 2026-08-31; independent counsel deferred by explicit RO decision; residual legal risk accepted by RO. Esto cierra la tarea de review, no compliance ni P0/P1.** Nuevo candidate #86 exact-base @ `200474d...` aborda release/provenance governance; no PASS mientras exact-head CI no termine. Nuevo #87 exact-base @ `d5d129c...` aborda security.txt/status software, pero runtime/DNS permanecen UNVERIFIED.
- **F1:** D6–D10.1 PASS. `NIGHT-WOZ-102` terminó `BLOCKED_STOP / D10.2 NOT_READY_FOR_RO_DECISION`; blockers mínimos = F2/12.1, F4/25.1 y cierre/RO applicability de F2/13.2 + 15.1.
- **F2:** 11.1/11.2/12.2 cerrados. Public infra probada por owner, pero apex sigue en `Loading Galer`; `NIGHT-AAA-100` owns F2/12.1. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment external. 19.1 public infra principal PROVEN; legal/support/OAuth/status runtime tails parciales. #76 stale/13+ tooling-blocked. **AI legal review evidence is recorded, but 19.2 remains OPEN with 12 P0 + 14 P1 + P2/P3 + UNVERIFIED implementation/risk backlog.** #83 OPEN/DRAFT tooling-blocked, runtime 160 UNVERIFIED; #85 external/owner-owned; #87 observed candidate, no runtime claim.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 exact `f53d46f...`; Windows Auth run `33449587244` / job `99676242317` = FAILURE. `NIGHT-BBB-099` owns evidence/harness-only causal trace.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 104

- `NIGHT-AAA-099`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result ni matching Issue #41 handoff. PR #86 apareció en rama `aaa/...` pero fuera del scope AAA099; no se acepta como completion y se reasigna explícitamente a WOZ103 para evitar ownership ambiguo.
- `NIGHT-BBB-098`: `NO_RESULT / SUPERSEDED / NOT_PASS`; #84 permanece sin cambio material y el literal packaged auth sigue rojo.
- `NIGHT-WOZ-102`: `BLOCKED_STOP / D10.2 NOT_READY_FOR_RO_DECISION / READ_ONLY_COMPLETE`; Issue #41 `5486382155`; evidencia aceptada como mapa factual, sin mutación.
- PR #86 live: OPEN/Ready/mergeable, exact base `816f946c...`, head `200474d061c63406774da8d21bd22460a8bd0312`; exact-head checks parcialmente in-progress al preflight, por lo que NO PASS todavía.
- PR #87 live: OPEN/Ready/mergeable, exact base `816f946c...`, head `d5d129c578355ca2ff6399bd2e6ec752c9f81618`; software candidate observado, status DNS/deploy/runtime explícitamente UNVERIFIED.
- PR #85 sigue external/owner-owned; no worker nocturno lo toca.
- No BeatGaler merge ni integration mutation procesada por JOBS en CYCLE 104.

## OWNERS — CYCLE 104

### AAA — `NIGHT-AAA-100` — F2 / 12.1
PRIMARY: reproducir `Loading Galer`, aislar primer bootstrap phase irresuelto y hacer mínimo corrective Web-only con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy ⇒ STOP.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-099` — F4 / 25.1
PRIMARY: obtener primer tuple sanitizado `{method, pathname/requestClass}` de #84; si no existe en el output, se permite una única modificación diagnostic-only mínima para emitirlo y rerun. Clasificar causa; harness correction solo si `HARNESS_ONLY_PROVEN`; assertions intactas; **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-103` — F0 / 1.2 / PR #86
PRIMARY: REUSE #86; review exact-base/head/scope + semantics + exact-head CI. Si todo applicable queda SUCCESS y race-free, WOZ es el único autorizado a mergear **#86 solamente**, verificando merge SHA/parents. Maximum claim = release/provenance implementation slice, no cierre global F0.  
CI-FALLBACK: solo si PRIMARY entra genuinamente `WAITING_CI`, inspección READ-ONLY de #87: scope/software evidence vs runtime/DNS/deploy external; **NO MUTATION / NO MERGE**.

**Integration mutation authorization CYCLE 104: WOZ103 / PR #86 ONLY, expected-head and exact-head-green only.**

## Camino crítico global — recalculado CYCLE 104

1. **F2/12.1 public Web startup:** `Loading Galer` debe terminar correctamente; bloquea tester use/browser evidence.
2. **F4/25.1 windows/auth:** sanitized causal trace → literal packaged PASS requerido.
3. **F2/13.2 Review:** durable Save/Save All completion/no-silent-loss + executable Web/no-Tauri evidence.
4. **F2/15.1 Empty Trash:** recent-reauth seam + strong confirmation + deterministic purge o decisión RO explícita de exclusión para alpha.
5. **F0/1.2 release governance:** #86 exact candidate puede cerrar implementación provenance/stable-prerelease si CI + review + merge exactos pasan; external tails siguen.
6. **F3/19.x public/legal:** #76 requiere refresh-capable surface + 18+; #87 puede cubrir software security/status, pero DNS/deploy/runtime y support/OAuth siguen externos. F0/0.8 review ya está `[x]` por excepción AI-assisted RO-approved; **los 12 P0/14 P1 legales sustantivos siguen release-blocking y se rastrean en `Legal launch review - AI-assisted 2026-08-31.md`.**
7. **F3/20.2:** #83 supported Ready tooling debe cambiar materialmente; luego runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin.
8. **F3/18.2:** provider/staging/payment scenarios reales.
9. **F1/D10.2:** reconsiderar readiness solo después de blockers técnicos aplicables y decisiones RO de alcance.
10. **External tails:** GitHub historical cleanup, signing/notarization/hardware/tester execution y revisión de seguridad independiente. **Independent legal counsel is deferred under the explicit F0/0.8 RO governance exception; no attorney review/compliance claim is implied.**

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

AAA ejecuta `NIGHT-AAA-100`; BBB `NIGHT-BBB-099`; WOZ `NIGHT-WOZ-103`. Solo WOZ103 puede mutar integration y únicamente para expected-head #86 después de exact-head applicable CI verde y recheck race-free. #85 permanece external-owned. #87 solo READ-ONLY fallback de WOZ si #86 espera CI. No retry #76/#83 sin cambio material de tooling. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 104; GitHub live prevalece si cambia después.
