# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE117

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-113`: durable Review Save/Save All completion/no-silent-loss; candidate only, NO MERGE | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-112`: minimal productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | F1/1.7 blocker classification READ-ONLY only during genuine WAITING_CI |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-116`: REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | F1/1.7 READ-ONLY only during genuine WAITING_CI |

**Baseline canónico CYCLE117:** `integration-v0.8.0-alpha.1 @ 08e5802d27ad81977b1c2f63ceb0fce398d41e42`.

## Handoffs/resultados procesados — CYCLE117

- AAA112: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB111: no matching result verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Late BBB110: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; concrete evidence accepted as input for BBB112.
- WOZ115: no matching result verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #92 is merged as `ada77811059a3319b271dcc98dd5d95efe807dec`.
- PR #94 is merged as `08e5802d27ad81977b1c2f63ceb0fce398d41e42`; its merge is factual external/owner integration, not attributed to WOZ115.
- PR #93 remains OPEN @ `b2c4eb441...` but stale/non-mergeable against current integration; parked.
- PR #89 remains OPEN @ `daf87da6...` on stale base `816f946c...`; WOZ116 owns refresh/revalidation/integration.

## Serialización

AAA113 owns only Review durability. BBB112 owns only the recent-reauth product seam. WOZ116 owns only #89. #93 has no owner and no merge authority CYCLE117. #85 remains external-owned; #76/#83 remain parked unless material conditions change.

**Only integration mutation authorized CYCLE117: WOZ116 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is the active software P1 lane.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; governing steps are 1.7 then 1.8.
- F2/12.1: #92/#94 integrated; deployment/runtime proof still required.
- F2/13.2 = AAA113.
- F2/15.1 is blocked behind BBB112 recent-reauth seam.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1: #93 needs future refresh/revalidation; global 25.1 stays open.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
