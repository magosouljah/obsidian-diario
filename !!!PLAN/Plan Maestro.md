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

## Estado vivo — NIGHT-JOBS-118

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- **Últimos merges materiales procesados:** #92 → `ada77811059a3319b271dcc98dd5d95efe807dec`; #94 → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`; #95 → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3` con parents `08e5802d... + 66f6b18e...`.
- **F2/12.1:** #92/#94/#95 integrados. #95 preserva el bound temporary Web session id y mantiene permanent application credentials fuera del browser. **12.1 sigue NOT_PASS** hasta deploy público exacto post-#95 + signed-out/authenticated startup + worker initialize/activate/verify + authoritative library reload + cold/warm proof y robustness residual aplicable.
- **F2/13.2:** durable Review gap sigue abierto; owner `NIGHT-AAA-114`.
- **F2/15.1:** recent-reauth product seam sigue siendo prerequisito; owner `NIGHT-BBB-113` solo para seam mínima, no Trash UI todavía.
- **F0/0.9:** #89 OPEN @ `daf87da6...`, base registrada `816f946c...`, ahora `mergeable=false` contra `43fdf70e...`; owner `NIGHT-WOZ-117` para bounded refresh/revalidation + conditional expected-head merge de #89 solamente.
- **F4/Windows Auth:** #93 OPEN @ `b2c4eb441...`, base `134a293...`, `mergeable=false`; PARKED / no owner CYCLE118.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7/1.8/1.9 siguen pendientes.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o RO-applicability.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 118

- `NIGHT-AAA-113`: sin RESULTADO DEL TURNO/matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-112`: sin matching result verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-116`: sin matching result verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #95 fue integrado después del snapshot CYCLE117; se procesa como **owner/external factual integration**, no se atribuye a un worker sin matching handoff.
- JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE 118

### AAA — `NIGHT-AAA-114` — F2 / 13.2
PRIMARY: minimum durable Review Save/Save All completion/no-silent-loss corrective; per-item partial/conflict/retry/idempotence; focused Web/no-Tauri tests; bounded candidate. **NO MERGE.**  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-113` — F1/D8 follow-up seam
PRIMARY: expose/reuse the minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; tests; bounded candidate. **No Trash UI/purge this turn. NO MERGE.**  
CI-FALLBACK: only during genuine `WAITING_CI`: F1/1.7 blocker classification READ-ONLY; STOP on mutation/RO/provider action or end of wait.

### WOZ — `NIGHT-WOZ-117` — F0 / 0.9 / #89
PRIMARY: REUSE #89; duplicate-check, history-preserving bounded refresh onto live baseline, exact-head F0/0.9 + applicable CI; if exact/green/race-free, expected-head merge **#89 only** and verify SHA/parents. Maximum claim = bounded DNS-rebinding SSRF P1 corrective integrated; no independent-pentest claim.  
CI-FALLBACK: only during genuine `WAITING_CI`: F4/25.1 #93 blocker classification READ-ONLY; no branch/PR mutation; recheck PRIMARY when CI leaves wait.

**Integration mutation authorization CYCLE118: WOZ117 / PR #89 ONLY, after exact refreshed base/head + applicable CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde GitHub vivo

1. **F2/12.1 runtime post-#95:** code is canonical; public deploy/authenticated worker/library + cold/warm evidence is the highest factual closure gap, but depends on owner/runtime access.
2. **F0/0.9 / #89:** close the known software P1 by safe refresh/revalidation/integration.
3. **F2/13.2:** durable Review completion/no-silent-loss, or explicit RO alpha exclusion.
4. **F1/D8→F2/15.1:** expose bounded recent-reauth seam first; then strong confirmation + durable Trash purge/no-false-success.
5. **F4/25.1 / #93:** refresh/revalidate packaged Windows Auth evidence after current integration lane; global 25.1 still needs other journeys.
6. **F1/1.7:** consolidate blockers and classify F3 18.2/19.2/20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.
7. **F1/1.8:** RO GO/NO-GO for alpha 3–5 accounts; **1.9** only after GO.
8. **Release path paralelo:** F0 1.2/2.2, productive signing/notarization, provider/legal/capacity/testers/hardware remain open.

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

AAA ejecuta `NIGHT-AAA-114`; BBB `NIGHT-BBB-113`; WOZ `NIGHT-WOZ-117` y posee la única conditional integration lane sobre #89. #93 queda parked/unassigned. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE118; GitHub live prevalece si cambia después.
