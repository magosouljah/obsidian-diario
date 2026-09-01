# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE148

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 runtime proof | `NIGHT-AAA-144`: READ-ONLY exact-deployment runtime evidence inventory post-#96; no deploy/code/infra | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-143`: minimum productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | F3/18.2 READ-ONLY evidence inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-147`: diagnose live F0 audit failure, REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | READ-ONLY PR #93 stale-evidence inventory only while #89 genuinely waits external CI after clean refresh |

**Baseline canónico CYCLE148:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Handoffs/resultados procesados — CYCLE148

- AAA143: no matching final result/handoff verified after CYCLE147 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB142: no matching final result/handoff verified after CYCLE147 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ146: no matching final result/handoff verified after CYCLE147 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Issue #41 fue leído completo; 405 comentarios en preflight y el último era JOBS CYCLE147 (`5500755003`); no había worker handoff posterior.
- PR #96 sigue siendo el último merge material: merge `aa445095...`; final head `6247173...`; Required CI exact-head SUCCESS. Sigue faltando public runtime proof exacto para cerrar F2/12.1.
- PR #89 permanece OPEN/Ready/mergeable @ `daf87da6...`, recorded base `816f946c...`; stale vs live `aa445095...`. F0/0.9 workflow run `33454881387` permanece FAILURE en ese exact head. WOZ147 owns diagnosis + bounded refresh/revalidation/integration; current head is not merge-eligible.
- PR #93 permanece OPEN/Ready/mergeable @ `b2c4eb441...`, base `134a293...`; stale. No mutation owner CYCLE148.
- Duplicate-check de PRs abiertos no mostró un candidate verificable nuevo de recent-reauth que vuelva redundante BBB143.

## Serialización

AAA144 owns only F2/12.1 runtime-proof/evidence READ-ONLY. BBB143 owns only recent-reauth product seam; su fallback F3/18.2 es READ-ONLY y solo existe durante espera externa real. WOZ147 owns only #89 mutation/integration. F2/13.2 Review is `BLOCKED_WRITE_SURFACE / UNASSIGNED`; #93 no tiene mutation owner y solo puede ser inspeccionado READ-ONLY bajo fallback explícito de WOZ147.

**Only integration mutation authorized CYCLE148: WOZ147 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check. #93 no tiene autorización de merge.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is active software P1 lane; live security gate failure must be diagnosed/revalidated, not waived.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; 1.7 se reemitirá con facts frescos tras resultados 12.1/#89/recent-reauth y luego 1.8 RO decision.
- F2/12.1: #92/#94/#95/#96 integrated; exact public runtime proof remains open.
- F2/13.2: factual gap, blocked on safe patch/worktree surface.
- F2/15.1: blocked behind BBB143 recent-reauth seam.
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
