# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE122

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F1 / 1.7 | `NIGHT-AAA-118`: alpha blocker classification READ-ONLY; no RO decision, no gate promotion | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-117`: minimal productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-121`: REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | READ-ONLY #93 applicability inventory only while #89 genuinely waits CI |

**Baseline canónico CYCLE122:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.

## Handoffs/resultados procesados — CYCLE122

- AAA117: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB116: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ120: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #89 remains OPEN @ `daf87da6...`, recorded base `816f946c...`, mechanical `mergeable=true`; base stale vs live `43fdf70e...`. WOZ121 owns bounded refresh/revalidation/integration.
- PR #93 remains OPEN @ `b2c4eb441...`, base `134a293...`, `mergeable=true`; base stale. It has no mutation owner; WOZ121 may inspect it READ-ONLY only under fallback condition.

## Serialización

AAA118 owns only F1/1.7 READ-ONLY classification. BBB117 owns only the recent-reauth product seam. WOZ121 owns only #89 mutation/integration. F2/13.2 Review is `BLOCKED_WRITE_SURFACE / UNASSIGNED`; #93 has no mutation owner.

**Only integration mutation authorized CYCLE122: WOZ121 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is the active software P1 lane.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; 1.7=AAA118 then 1.8 RO decision.
- F2/12.1: #92/#94/#95 integrated; deployment/runtime proof after #95 still required.
- F2/13.2: factual gap, blocked on safe patch/worktree surface.
- F2/15.1: blocked behind BBB117 recent-reauth seam.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending; AAA118 classifies alpha applicability only.
- F4/25.1: #93 needs future refresh/revalidation if in alpha; global 25.1 stays open.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
