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

## Estado vivo — NIGHT-JOBS-108

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.
- **Último merge material:** #87 → `38517c8065063206fed530028e4e8d20208f3807`, parents exactos `b85723e1b3016d24bdb943393e796ccdb744247d` + `ba0d7b689e587da42cc8105b22d0ed0c206bc064`.
- **F0:** núcleo técnico principal cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 canónica: **18+**. #86/#87 software slices integrados. #89 OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; old-head CI verde no sustituye refresh exact-head. #88 está exact-base `38517c...` pero production signing sigue NO-GO pending RO inputs/authorization. #90 readiness no equivale a rotación real.
- **F1:** D6–D10.1 PASS. D10.2 sigue `NOT_READY_FOR_RO_DECISION`; blockers mínimos = F2/12.1, F4/25.1 y cierre/decisión explícita sobre F2/13.2 + 15.1.
- **F2:** 11.1/11.2/12.2 cerrados. Infra pública principal probada por owner, pero normal apex sigue observado en `Loading Galer`; `NIGHT-AAA-104` owns F2/12.1. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment external. #87 security/status software integrated; DNS/SAN/deployment/public runtime/support/legal/OAuth tails siguen `UNVERIFIED/OPEN`. #76 stale/13+ contradice 18+; #83 OPEN/DRAFT y runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 evidence lineage @ `f53d46f...`, stale; Required CI old-head verde, pero Windows Auth run `33449587244` / job `99676242317` = FAILURE. `NIGHT-BBB-103` owns evidence/harness-only causal correction.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 108

- `NIGHT-AAA-103`: no RESULTADO DEL TURNO ni matching Issue #41 handoff verificable al preflight → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-102`: no RESULTADO DEL TURNO ni matching Issue #41 handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`. Último resultado verificable de la línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- `NIGHT-WOZ-106`: no RESULTADO DEL TURNO ni matching Issue #41 handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`. Último WOZ final verificable: WOZ104 `DONE / INTEGRATED`, Issue #41 `5486854786`.
- PR #89 live: OPEN/Ready, head `daf87da6ffd604ccac991311036919ae2de9bd7a`, base_sha `816f946c...`; Required CI old-head SUCCESS, refresh history-preserving + fresh exact-head CI todavía requeridos.
- PR #84 live: OPEN/Ready, head `f53d46f39ece94f6de74f2f21a508ce01497ac41`, base_sha `816f946c...`; Required CI old-head SUCCESS, literal Windows Auth continúa NOT_PASS.
- PR #88 live: exact current base pero explicit production signing NO-GO / RO inputs required.
- PR #90 readiness-only; rotación real externa. #85 external-owned. #76/#83 parked.
- No PASS nuevo ni integración nueva procesable. JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE 108

### AAA — `NIGHT-AAA-104` — F2 / 12.1
PRIMARY: reproducir `Loading Galer`, aislar primer bootstrap phase irresuelto y hacer mínimo corrective Web-only con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy ⇒ STOP.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-103` — F4 / 25.1
PRIMARY: consumir tuple sanitizado `POST /plugin%3Awdio%7Cget_window_states` / `cross-origin`, demostrar atribución WDIO/Tauri, y corregir solo harness/service interception si queda `HARNESS_ONLY_PROVEN`; refresh history-preserving de #84 al baseline vivo si es seguro; packaged Windows Auth literal + exact-head CI; **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-107` — F0 / 0.9 / PR #89
PRIMARY: REUSE #89; review semántico + refresh history-preserving sobre `38517c...` + fresh exact-head security/Required CI. Si todo applicable queda SUCCESS y race-free, WOZ es el único autorizado a mergear **#89 solamente** con expected-head y verificación de parents. Maximum claim = AI-assisted security software slice + DNS-rebinding P1 fixed; no external pentest/F0 global/release claim.  
CI-FALLBACK: solo si PRIMARY entra genuinamente `WAITING_CI`: inspección **READ-ONLY** de #90, separando software readiness de owner/deployment/credential evidence; **NO MUTATION / NO MERGE / NO ROTATION**. Volver a #89 al resolver CI.

**Integration mutation authorization CYCLE 108: WOZ107 / PR #89 ONLY, después de refresh exact-base, exact-head applicable CI green y race-free expected head.**

## Camino crítico global — recalculado desde cero CYCLE 108

1. **F2/12.1 public Web startup:** `Loading Galer` debe terminar correctamente; bloquea tester/browser evidence.
2. **F4/25.1 windows/auth:** harness/service attribution → literal packaged PASS requerido.
3. **F2/13.2 Review:** durable Save/Save All completion/no-silent-loss + executable Web/no-Tauri evidence.
4. **F2/15.1 Empty Trash:** recent-reauth seam + strong confirmation + deterministic purge o decisión RO explícita de exclusión para alpha.
5. **F0/0.9 security:** #89 debe refresh/revalidar e integrar el P1 DNS-rebinding sin falsear external pentest.
6. **F0 release/admin tails:** #88 Authenticode/RFC3161 requiere provider/cert/publisher/custody/CI/RFC3161/authorization RO; #90 requiere rotación owner real; 2.2 GitHub historical cleanup externo.
7. **F3/19.x public/legal:** #87 software integrated, pero runtime/DNS/SAN/deploy/support/legal/OAuth tails siguen; #76 requiere refresh-capable surface + 18+.
8. **F3/20.2:** #83 tooling + runtime real 160, latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin.
9. **F3/18.2:** provider/staging/payment scenarios reales.
10. **F1/D10.2:** reconsiderar readiness solo después de blockers técnicos aplicables y decisiones RO de alcance.
11. **External tails:** signing/notarization/hardware/tester execution e independent review donde siga requerido.

La secuencia coincide en gran parte con CYCLE 107 porque los hechos vivos relevantes no cambiaron; no se conservó por inercia, se rederivó desde los gates y GitHub actuales.

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

AAA ejecuta `NIGHT-AAA-104`; BBB `NIGHT-BBB-103`; WOZ `NIGHT-WOZ-107`. Solo WOZ107 puede mutar integration y únicamente para expected-head #89 después de refresh al baseline vivo + exact-head applicable CI verde + recheck race-free. #85 permanece external-owned. #88 permanece sin autorización productiva/signing aunque esté exact-base. #90 solo READ-ONLY fallback de WOZ si #89 espera CI. No retry #76/#83 sin cambio material de tooling/surface. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 108; GitHub live prevalece si cambia después.
