# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE157

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F0 / 0.9 | `NIGHT-AAA-153`: REUSE #89, refresh/revalidate exact-head; conditional merge #89 only if exact/green/race-free | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-152`: minimum productive recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97/#100/#89 | F3/18.2 READ-ONLY inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | Issue #97 / PR #100 | `NIGHT-WOZ-156`: REUSE #100, measurements Web+Desktop → actual minimum correction on same lineage; conditional merge #100 only after correction + exact evidence | NONE |

**Baseline canónico CYCLE157:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.

## Handoffs/resultados procesados — CYCLE157

- AAA152: sin RESULTADO DEL TURNO/matching worker handoff y #89 sin movimiento → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB151: sin RESULTADO DEL TURNO/matching worker handoff y sin recent-reauth candidate → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ155: sin resultado terminal, pero GitHub live produjo PR #100 durante el preflight → `ACTIVE_PROGRESS / SUPERSEDED_BY_WOZ156 / NOT_PASS`.
- PR #100 es exact-base `c2766fb...` @ `5f0a0727...`, observational instrumentation only y CI in progress; no altera startup/performance y no cierra #97.
- F2/12.1 sigue NOT_PASS; #89 sigue OPEN/stale con dedicated security gate FAILURE; #93 sigue OPEN/stale/no owner.

## Serialización

- AAA153: único owner de mutation/integration de #89.
- BBB152: recent-reauth product seam solamente; NO MERGE.
- WOZ156: único owner de mutation/integration de Issue #97 / PR #100.
- #93: sin owner/mutation/fallback.
- F2/13.2: `BLOCKED_WRITE_SURFACE / UNASSIGNED` mientras #97/#100 ocupe superficies compartidas.
- F2/12.1 exact production deployment/source proof queda blocker factual/SHA-dependent; no fallback que pueda ser invalidado por merges de AAA/WOZ.

**Integration mutations authorized CYCLE157: AAA153 / PR #89 and WOZ156 / PR #100, each only on exact scope + applicable CI SUCCESS + no required review blocker + race-free expected-head. #100 instrumentation-only is not sufficient for merge-as-closure. If either merge moves integration, the other must refresh/revalidate before merge. BBB152 and #93 have no merge authorization.**

## Critical path

`F2/12.1 clean canonical production source proof` → `#97/#100 measurements + correction` + `#89 F0/0.9 P1 refresh/exact-green` + `recent-reauth seam` in parallel where independent → `F2/15.1` → `F2/13.2 safe write surface` → `F1/1.7 → 1.8` → `#93 only if IN_ALPHA`; external F0/F3/F4 tails remain parallel.

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails.
- F0/0.9 #89 P1 unintegrated; red dedicated security gate cannot be waived.
- Productive signing external despite #88 seam.
- F1/D10.2 = `ALPHA CANDIDATE NOT READY`; 1.7 waits fresh facts.
- F2/12.1 not PASS; F2/13.2 blocked; F2/15.1 blocked on recent-reauth; #97 active pre-Beta blocker with #100 instrumentation in progress.
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
