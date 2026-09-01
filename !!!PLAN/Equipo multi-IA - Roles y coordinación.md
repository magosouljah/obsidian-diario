# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE139

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F1 / 1.7 | `NIGHT-AAA-135`: alpha blocker classification READ-ONLY; incorporar #96 como candidate activo, no RO decision/gate promotion | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-134`: minimum productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-138`: diagnose live F0 audit failure, REUSE #89, bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | READ-ONLY PR #96 stability/evidence inventory only while #89 genuinely waits external CI after clean refresh |

**Baseline canónico CYCLE139:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.

## Handoffs/resultados procesados — CYCLE139

- AAA134: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB133: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ137: no matching final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #96 apareció después de CYCLE138: OPEN/Ready, base exacta `43fdf70e...`; head avanzó durante el preflight hasta `7e7bd5449361b2031c29271e8875de7683ed5af4`, sin check-runs observados en ese exact head. No hay matching worker handoff. Se serializa como `ACTIVE_EXTERNAL_CANDIDATE / NO NIGHT MUTATION OWNER`; nadie lo roba mientras siga activo/cambiante.
- PR #89 remains OPEN @ `daf87da6...`, recorded base `816f946c...`; stale vs live `43fdf70e...`. F0/0.9 workflow run `33454881387` reconsultado = **FAILURE** on that exact head. WOZ138 owns diagnosis + bounded refresh/revalidation/integration; current head is not merge-eligible.
- PR #93 remains OPEN @ `b2c4eb441...`, base `134a293...`; stale. No mutation owner CYCLE139.

## Serialización

AAA135 owns only F1/1.7 READ-ONLY classification. BBB134 owns only recent-reauth product seam. WOZ138 owns only #89 mutation/integration. PR #96 está activo fuera del ownership nocturno y solo puede inspeccionarse READ-ONLY por WOZ138 bajo su fallback. F2/13.2 Review es `BLOCKED_WRITE_SURFACE / UNASSIGNED`; #93 no tiene mutation owner.

**Only integration mutation authorized CYCLE139: WOZ138 / PR #89, conditional on exact refreshed base/head, applicable required CI SUCCESS and race-free expected-head check. #96 y #93 no tienen autorización de merge.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 is active software P1 lane; live security gate failure must be diagnosed/revalidated, not waived.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; 1.7=AAA135 then 1.8 RO decision.
- F2/12.1: #92/#94/#95 integrated; #96 active candidate, exact-head CI/handoff + eventual public runtime proof still required.
- F2/13.2: factual gap, blocked on safe patch/worktree surface.
- F2/15.1: blocked behind BBB134 recent-reauth seam.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending; AAA135 classifies alpha applicability only.
- F4/25.1: #93 needs future refresh/revalidation if in alpha; global 25.1 stays open.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
