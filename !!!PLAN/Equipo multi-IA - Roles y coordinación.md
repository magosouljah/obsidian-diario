# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE118

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-114`: durable Review Save/Save All completion/no-silent-loss; candidate only, NO MERGE | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-113`: minimal productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | F1/1.7 blocker classification READ-ONLY only during genuine WAITING_CI |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-117`: REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | F4/25.1 #93 blocker classification READ-ONLY only during genuine WAITING_CI |

**Baseline canónico CYCLE118:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.

## Handoffs/resultados procesados — CYCLE118

- AAA113: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB112: no matching result verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ116: no matching result verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #95 merged after CYCLE117 as `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`, parents `08e5802d... + 66f6b18e...`; treated as factual owner/external integration, not attributed to any missing worker handoff.
- PR #95 exact-head observed workflows include Web Production Build, Desktop Portability, D6, D7, productive temp-auth compile and F0/0.20 secret scan SUCCESS; 12.1 still requires post-merge public runtime proof.
- PR #93 remains OPEN @ `b2c4eb441...`, base `134a293...`, `mergeable=false`; parked.
- PR #89 remains OPEN @ `daf87da6...`, base `816f946c...`, now `mergeable=false`; WOZ117 owns bounded refresh/revalidation/integration.

## Serialización

AAA114 owns only Review durability. BBB113 owns only the recent-reauth product seam. WOZ117 owns only #89. #93 has no owner and no merge authority CYCLE118.

**Only integration mutation authorized CYCLE118: WOZ117 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is the active software P1 lane.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; governing steps are 1.7 then 1.8.
- F2/12.1: #92/#94/#95 integrated; deployment/runtime proof after #95 still required.
- F2/13.2 = AAA114.
- F2/15.1 is blocked behind BBB113 recent-reauth seam.
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
