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

## Estado vivo — NIGHT-JOBS-119

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- **Últimos merges materiales procesados:** #92 → `ada77811059a3319b271dcc98dd5d95efe807dec`; #94 → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`; #95 → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`, parents `08e5802d... + 66f6b18e...`.
- **F2/12.1:** #92/#94/#95 integrados. Sigue `NOT_PASS` hasta deploy público exacto post-#95 + signed-out/authenticated startup + worker initialize/activate/verify + authoritative library reload + cold/warm proof y robustness residual aplicable.
- **F2/13.2:** gap durable Review confirmado de nuevo por AAA114. `BLOCKED_WRITE_SURFACE / UNASSIGNED` CYCLE119: no candidate, no tests, no CI, no PASS.
- **F2/15.1:** recent-reauth product seam sigue siendo prerequisito; owner `NIGHT-BBB-114` solo para seam mínima, no Trash UI todavía.
- **F0/0.9:** #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`; GitHub ahora reporta `mergeable=true`, pero la base sigue materialmente stale frente a `43fdf70e...`. Owner `NIGHT-WOZ-118` para bounded refresh/revalidation + conditional expected-head merge de #89 solamente.
- **F4/Windows Auth:** #93 OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...`; GitHub ahora reporta `mergeable=true`, pero sigue stale y su old-head exact-green evidence no es canonical integration evidence. PARKED / no owner CYCLE119.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7 owner `NIGHT-AAA-115` READ-ONLY; 1.8/1.9 pendientes.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o requieren clasificación explícita de aplicabilidad al alpha.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE119

- `NIGHT-AAA-114`: `PENDING / STOP_WRITE_SURFACE / NOT_PASS`. Revalidó el gap de Review en el live baseline; no abrió branch/PR porque la superficie disponible solo permitía whole-file replacement inseguro de `src/App.tsx`. Handoff #41 `5490203080`. No DONE/PASS.
- `NIGHT-BBB-113`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-117`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Live GitHub corrigió una observación documental: #89 y #93 actualmente son `mergeable=true`; ambos siguen con base SHA vieja, por lo que exact-head/evidence-before-claim exige refresh/revalidation antes de cualquier canonical integration.
- JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE119

### AAA — `NIGHT-AAA-115` — F1 / 1.7
PRIMARY: blocker classification READ-ONLY para alpha 3–5 cuentas; clasificar evidencia como `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL`, incluyendo F2/F0/F4/F3 blockers, sin tomar decisión RO ni promover gates.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-114` — F1/D8 follow-up seam
PRIMARY: expose/reuse the minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; tests; bounded candidate. **No Trash UI/purge. NO MERGE.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-118` — F0 / 0.9 / #89
PRIMARY: REUSE #89; duplicate-check, history-preserving bounded refresh onto live baseline, exact-head F0/0.9 + applicable CI; if exact/green/race-free, expected-head merge **#89 only** and verify SHA/parents. Maximum claim = bounded DNS-rebinding SSRF P1 corrective integrated; no independent-pentest claim.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE119: WOZ118 / PR #89 ONLY, after exact refreshed base/head + applicable CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde cero contra GitHub vivo

1. **F2/12.1 runtime post-#95:** highest factual closure gap; depends on verified public-runtime/owner access and cannot be fabricated.
2. **F0/0.9 / #89:** close the known software P1 by safe refresh/revalidation/integration; `mergeable=true` does not cure stale base.
3. **F1/1.7:** prepare an evidence-backed alpha blocker classification now, in parallel, so 1.8 can become a real RO decision once hard blockers are resolved/classified.
4. **F1/D8→F2/15.1:** expose bounded recent-reauth seam, then strong confirmation + durable Trash purge/no-false-success.
5. **F2/13.2:** Review durable completion remains a hard product gap but is blocked on a safe patch/worktree-capable write surface; no duplicate assignment while that blocker is unchanged.
6. **F4/25.1 / #93:** future refresh/revalidate packaged Windows Auth evidence against live baseline; global 25.1 still needs other journeys.
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

AAA ejecuta `NIGHT-AAA-115`; BBB `NIGHT-BBB-114`; WOZ `NIGHT-WOZ-118` y posee la única conditional integration lane sobre #89. F2/13.2 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED` hasta cambiar materialmente la superficie de ejecución. #93 queda parked/unassigned. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE119; GitHub live prevalece si cambia después.
