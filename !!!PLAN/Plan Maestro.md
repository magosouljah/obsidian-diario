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

## Estado vivo — NIGHT-JOBS-122

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight y race-check:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- **Últimos merges materiales procesados:** #92 → `ada77811059a3319b271dcc98dd5d95efe807dec`; #94 → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`; #95 → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`, parents `08e5802d... + 66f6b18e...`.
- **F2/12.1:** #92/#94/#95 integrados. Sigue `NOT_PASS` hasta deploy público exacto post-#95 + signed-out/authenticated startup + worker initialize/activate/verify + authoritative library reload + cold/warm proof y robustness residual aplicable.
- **F2/13.2:** durable Review gap confirmado por AAA114. `BLOCKED_WRITE_SURFACE / UNASSIGNED`: no candidate, tests, CI ni PASS.
- **F2/15.1:** recent-reauth product seam sigue prerequisito; owner `NIGHT-BBB-117` solo para seam mínima, no Trash UI todavía.
- **F0/0.9:** #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`, mechanical `mergeable=true`; base materialmente stale frente a `43fdf70e...`. Owner `NIGHT-WOZ-121` para bounded refresh/revalidation + conditional expected-head merge de #89 solamente.
- **F4/Windows Auth:** #93 OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...`, `mergeable=true`; stale y old-head exact-green evidence no es canonical integration evidence. No mutation owner CYCLE122.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7 owner `NIGHT-AAA-118` READ-ONLY; 1.8/1.9 pendientes.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o requieren clasificación explícita de aplicabilidad al alpha.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE122

- `NIGHT-AAA-117`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-116`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-120`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Issue #41 completo fue reconciliado; no apareció candidate nuevo para recent-reauth ni resultado final nuevo de esos Assignment IDs.
- Live GitHub mantiene integration en #95; #89/#93 siguen OPEN y stale-base. Mechanical mergeability no sustituye refresh/exact-head evidence.
- JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE122

### AAA — `NIGHT-AAA-118` — F1 / 1.7
PRIMARY: blocker classification READ-ONLY para alpha 3–5 cuentas; clasificar evidencia como `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL`, incluyendo F2/F0/F4/F3 blockers, sin tomar decisión RO ni promover gates.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-117` — F1/D8 follow-up seam
PRIMARY: expose/reuse the minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; focused tests; bounded candidate. **No Trash UI/purge. NO MERGE.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-121` — F0 / 0.9 / #89
PRIMARY: REUSE #89; duplicate-check, history-preserving bounded refresh onto live baseline, exact-head F0/0.9 + applicable CI; if exact/green/race-free, expected-head merge **#89 only** and verify SHA/parents. Maximum claim = bounded DNS-rebinding SSRF P1 corrective integrated; no independent-pentest claim.  
CI-FALLBACK: while PRIMARY is genuinely WAITING_CI/WAITING_EXTERNAL only, perform READ-ONLY #93 applicability/evidence inventory; no mutation, CI rerun, new PR or gate promotion; STOP fallback immediately when PRIMARY ceases waiting and return to #89 recheck.

**Integration mutation authorization CYCLE122: WOZ121 / PR #89 ONLY, after exact refreshed base/head + applicable CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde cero contra GitHub vivo

1. **F2/12.1 runtime post-#95:** highest factual closure gap; currently lacks verified production-runtime evidence/authority.
2. **F0/0.9 / #89:** known software P1; independently executable refresh/revalidation/integration.
3. **F1/1.7:** blocker classification required before a real 1.8 RO decision.
4. **F1/D8→F2/15.1:** expose bounded recent-reauth seam, then strong confirmation + durable Trash purge/no-false-success.
5. **F2/13.2:** hard product gap but blocked on safe patch/worktree-capable write surface; do not duplicate unsafe whole-file mutation.
6. **F4/25.1 / #93:** future mutation only after alpha applicability classification; READ-ONLY inventory allowed solely as WOZ fallback while #89 waits.
7. **Release path paralelo:** F0 1.2/2.2, productive signing/notarization, provider/legal/capacity/testers/hardware remain open.

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

AAA ejecuta `NIGHT-AAA-118`; BBB `NIGHT-BBB-117`; WOZ `NIGHT-WOZ-121` y posee la única conditional integration lane sobre #89. F2/13.2 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED` hasta cambiar materialmente la superficie de ejecución. #93 no tiene mutation owner; solo puede ser inspeccionado READ-ONLY bajo el fallback de WOZ121 mientras #89 espera CI. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE122; GitHub live prevalece si cambia después.
