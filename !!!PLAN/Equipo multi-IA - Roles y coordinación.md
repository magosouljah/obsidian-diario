# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE150

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 runtime proof | `NIGHT-AAA-146`: READ-ONLY exact-deployment runtime evidence inventory post-#96; no deploy/code/infra | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-145`: minimum productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | F3/18.2 READ-ONLY evidence inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-149`: diagnose current F0 audit failure, REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | READ-ONLY #93 stale-evidence inventory only while #89 genuinely waits external CI after clean refresh |

**Baseline canónico CYCLE150:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Handoffs/resultados procesados — CYCLE150

- AAA145: no matching final result/handoff verified after CYCLE149 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB144: no matching final result/handoff verified after CYCLE149 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ148: no matching final result/handoff verified after CYCLE149 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Issue #41 fue leído completo y refrescado; el último handoff previo al ciclo seguía siendo JOBS CYCLE149 `5501376377`.
- PR #96 sigue siendo el último merge material; F2/12.1 permanece `PUBLIC_RUNTIME_OPEN`.
- PR #89 sigue OPEN @ `daf87da6...`, recorded base `816f946c...`, stale vs live; run F0/0.9 `33454881387` sigue FAILURE exact-head. Current head is not merge-eligible.
- PR #93 sigue OPEN @ `b2c4eb441...`, base `134a293...`, stale; no mutation owner.
- Duplicate-check no mostró PR nuevo de recent-reauth.

## Serialización

AAA146 owns only F2/12.1 runtime-proof evidence READ-ONLY. BBB145 owns only recent-reauth product seam; its F3/18.2 fallback is READ-ONLY and exists only during genuine external wait. WOZ149 exclusively owns #89 mutation/integration. F2/13.2 remains `BLOCKED_WRITE_SURFACE / UNASSIGNED`; #93 remains mutation-unassigned.

**Only integration mutation authorized CYCLE150: WOZ149 / PR #89, conditional on exact refreshed base/head, applicable security/required CI SUCCESS and race-free expected-head check. #93 has no merge authorization.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 active P1 lane; security failure must be diagnosed/revalidated, never waived.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 = `ALPHA CANDIDATE NOT READY`; 1.7 waits for fresher 12.1/#89/recent-reauth facts before 1.8 RO decision.
- F2/12.1 public runtime proof open; F2/13.2 blocked on safe write surface; F2/15.1 blocked on recent-reauth seam.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1 global open; #93 only future refresh if alpha applicability remains.
- F5 CLOSED / release NO-GO.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
