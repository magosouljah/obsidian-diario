# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE153

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 runtime proof | `NIGHT-AAA-149`: READ-ONLY exact production/deployment evidence around PR #98; classify source-bound vs source-unbound; keep #97 separate | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-148`: minimum productive recent-reauth seam bound to user/session; no Trash UI; candidate only, NO MERGE; no PR #98 files | F3/18.2 READ-ONLY evidence inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | F2 / 12.1 / PR #98 | `NIGHT-WOZ-152`: exclusive #98 validation/mutation/integration; exact-head Required CI + race-free expected-head merge #98 only | #89 strictly READ-ONLY refresh-readiness inventory only while #98 genuinely waits external CI/review/build |

**Baseline canónico CYCLE153:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Handoffs/resultados procesados — CYCLE153

- Issue #41 CYCLE152 (`5502310629`) was newer than the vault nightlies and therefore authoritative for consecutive IDs.
- AAA148, BBB147, WOZ151: no matching worker final result/handoff after CYCLE152 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #98 appeared after CYCLE152: OPEN/Ready/mergeable, exact base `aa445095...`, head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`, 1 commit / 6 files. Supporting exact-head workflows were green except Test - Desktop Portability / Required CI `33575511576`, still in progress at assignment time.
- PR #98 reports production health/library/artwork/playback success, but exact deployment-source binding remains a literal evidence requirement.
- Issue #97 is OPEN and explicitly `Must be addressed before Beta 1`; it overlaps #98 startup/App surfaces and is not assigned concurrently.
- PR #89 remains OPEN @ `daf87da6...`, stale base `816f946c...`, F0/0.9 run `33454881387` FAILURE. No mutation owner CYCLE153.
- PR #93 remains OPEN @ `b2c4eb441...`, stale base `134a293...`; no mutation owner.

## Serialización

- AAA149 owns runtime/deployment evidence only; it cannot mutate PR #98.
- WOZ152 exclusively owns PR #98 mutation/integration.
- BBB148 owns only recent-reauth product seam and is explicitly barred from the six #98 files.
- #89 may only be inspected READ-ONLY by WOZ152 while #98 is genuinely waiting externally; its changed files are disjoint from #98.
- #93 has no owner/mutation/fallback this cycle.
- F2/13.2 remains `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
- Issue #97 has no implementation owner until #98 releases overlapping startup/App surfaces.

**Only integration mutation authorized CYCLE153: WOZ152 / PR #98, conditional on exact base/head, applicable Required CI SUCCESS, no required review blocker and race-free expected-head check. #89/#93 have no merge authorization.**

## Critical path

`#98 exact CI + integration + runtime-source proof` → `#97 pre-Beta startup/reveal` → `#89 F0/0.9 P1 refresh/exact-green` → `recent-reauth seam → F2/15.1` → `F2/13.2 safe write surface` → `F1/1.7 → 1.8` → `#93 only if IN_ALPHA`; external F0/F3/F4 tails remain parallel.

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain.
- F0/0.9 #89 P1 remains unintegrated; red security gate cannot be waived.
- Productive signing remains external despite #88 technical seam.
- F1/D10.2 = `ALPHA CANDIDATE NOT READY`; 1.7 waits for fresher #98/#97/#89/recent-reauth facts.
- F2/12.1 not PASS yet; F2/13.2 blocked; F2/15.1 blocked on recent-reauth; #97 is new explicit pre-Beta performance blocker.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1 global open; #93 future refresh only if alpha applicability remains.
- F5 CLOSED / release NO-GO.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
