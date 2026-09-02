# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE154

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 close review | `NIGHT-AAA-150`: READ-ONLY exact runtime/deployment-source evidence post-#98 | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-149`: minimum productive recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97 | F3/18.2 READ-ONLY inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | Issue #97 | `NIGHT-WOZ-153`: exclusive pre-Beta startup/reveal Web+Desktop implementation/integration; conditional merge candidate #97 only | #89 strictly READ-ONLY refresh-readiness only while #97 genuinely waits external CI/review/build |

**Baseline canónico CYCLE154:** `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.

## Handoffs/resultados procesados — CYCLE154

- AAA149 y BBB148: sin matching worker final result/handoff posterior a CYCLE153 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ152: no final handoff escrito, pero GitHub prueba directamente el outcome autorizado: PR #98 MERGED, exact candidate head `00da0ab...`, Required CI `33575511576` SUCCESS, integration `c4e203cf...`. Procesado solo como `PR98_PRODUCTION_WEB_MTProto_CLEANUP_INTEGRATED`; no implica F2/12.1 PASS.
- Issue #97 continúa OPEN / pre-Beta blocker; ahora sí recibe owner porque #98 liberó App/startup surfaces.
- #89 sigue OPEN @ `daf87da6...`, stale base `816f946c...`, F0/0.9 `33454881387` FAILURE; sin mutation owner.
- #93 sigue stale @ `b2c4eb441...`; sin mutation owner.

## Serialización

- AAA150: evidencia runtime/deployment READ-ONLY solamente.
- BBB149: recent-reauth product seam solamente.
- WOZ153: único owner de mutation/integration de Issue #97.
- #89: solo fallback READ-ONLY de WOZ153 durante espera externa genuina; cualquier overlap factual invalida fallback.
- #93: sin owner/mutation/fallback.
- F2/13.2: `BLOCKED_WRITE_SURFACE / UNASSIGNED`.

**Only integration mutation authorized CYCLE154: WOZ153 / candidate de Issue #97, conditional on exact scope + applicable CI SUCCESS + no required review blocker + race-free expected-head. #89/#93 have no merge authorization.**

## Critical path

`F2/12.1 exact runtime-source close review` → `#97 pre-Beta startup/reveal` → `#89 F0/0.9 P1 refresh/exact-green` → `recent-reauth seam → F2/15.1` → `F2/13.2 safe write surface` → `F1/1.7 → 1.8` → `#93 only if IN_ALPHA`; external F0/F3/F4 tails remain parallel.

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails.
- F0/0.9 #89 P1 unintegrated; red security gate cannot be waived.
- Productive signing external despite #88 seam.
- F1/D10.2 = `ALPHA CANDIDATE NOT READY`; 1.7 waits fresh facts.
- F2/12.1 not PASS; F2/13.2 blocked; F2/15.1 blocked on recent-reauth; #97 active pre-Beta blocker.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1 global open; #93 future refresh only if alpha applicable.
- F5 CLOSED / release NO-GO.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
