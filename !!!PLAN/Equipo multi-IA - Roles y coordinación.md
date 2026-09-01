# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE140

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 runtime proof | `NIGHT-AAA-136`: READ-ONLY exact-deployment runtime evidence inventory post-#96; no deploy/code/infra | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-135`: minimum productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-139`: diagnose live F0 audit failure, REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | READ-ONLY PR #93 stale-evidence inventory only while #89 genuinely waits external CI after clean refresh |

**Baseline canónico CYCLE140:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Handoffs/resultados procesados — CYCLE140

- AAA135: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB134: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ138: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #96 ya no está WAITING_CI: MERGED el 2026-09-01T17:51:40Z; final head `6247173...`, base `43fdf70e...`, merge `aa445095...`; Required CI exact-head SUCCESS. Sigue faltando public runtime proof exacto para cerrar F2/12.1.
- PR #89 remains OPEN @ `daf87da6...`, recorded base `816f946c...`; stale vs live `aa445095...`. F0/0.9 workflow run `33454881387` remains known FAILURE on that exact head. WOZ139 owns diagnosis + bounded refresh/revalidation/integration; current head is not merge-eligible.
- PR #93 remains OPEN @ `b2c4eb441...`, base `134a293...`; stale. No mutation owner CYCLE140.

## Serialización

AAA136 owns only F2/12.1 runtime-proof/evidence READ-ONLY. BBB135 owns only recent-reauth product seam. WOZ139 owns only #89 mutation/integration. F2/13.2 Review is `BLOCKED_WRITE_SURFACE / UNASSIGNED`; #93 no tiene mutation owner y solo puede ser inspeccionado READ-ONLY bajo fallback explícito de WOZ139.

**Only integration mutation authorized CYCLE140: WOZ139 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check. #93 no tiene autorización de merge.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is active software P1 lane; live security gate failure must be diagnosed/revalidated, not waived.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; 1.7 se reemitirá con facts más frescos tras resultados CYCLE140 y luego 1.8 RO decision.
- F2/12.1: #92/#94/#95/#96 integrated; exact public runtime proof remains open.
- F2/13.2: factual gap, blocked on safe patch/worktree surface.
- F2/15.1: blocked behind BBB135 recent-reauth seam.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending; alpha applicability remains explicit-decision territory.
- F4/25.1: #93 needs future refresh/revalidation if in alpha; global 25.1 stays open.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
