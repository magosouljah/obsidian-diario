# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE156

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F0 / 0.9 | `NIGHT-AAA-152`: REUSE #89, refresh/revalidate exact-head; conditional merge #89 only if exact/green/race-free | NONE |
| BBB | F1/D8 follow-up | `NIGHT-BBB-151`: minimum productive recent-reauth seam bound to user/session; candidate only; NO MERGE; no Trash/#97/#89 | F3/18.2 READ-ONLY inventory only while PRIMARY genuinely waits external CI/build/review |
| WOZ | Issue #97 | `NIGHT-WOZ-155`: exclusive pre-Beta startup/reveal Web+Desktop implementation/integration; conditional merge candidate #97 only | NONE |

**Baseline canónico CYCLE156:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.

## Handoffs/resultados procesados — CYCLE156

- AAA151, BBB150 y WOZ154: sin RESULTADO DEL TURNO en sus ledgers y sin matching worker handoff en Issue #41 antes del nuevo ciclo → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- No aparece PR/candidate nuevo posterior a #99 para #97 o recent-reauth.
- #99 sigue integrado y solo aporta el mecanismo de source binding; no prueba por sí mismo clean canonical production deployment desde current SHA. F2/12.1 sigue NOT_PASS.
- Issue #97 continúa OPEN / pre-Beta blocker, cero comments.
- #89 sigue OPEN @ `daf87da6...`, stale base `816f946c...`, F0/0.9 `33454881387` FAILURE; owner exclusivo AAA152.
- #93 sigue OPEN/stale @ `b2c4eb441...`; sin mutation owner.

## Serialización

- AAA152: único owner de mutation/integration de #89.
- BBB151: recent-reauth product seam solamente; NO MERGE.
- WOZ155: único owner de mutation/integration de Issue #97.
- #93: sin owner/mutation/fallback.
- F2/13.2: `BLOCKED_WRITE_SURFACE / UNASSIGNED` mientras #97 ocupe superficies compartidas.
- F2/12.1 exact production deployment/source proof queda como blocker factual/SHA-dependent; no se asigna fallback que pueda ser invalidado por merges de AAA/WOZ.

**Integration mutations authorized CYCLE156: AAA152 / PR #89 and WOZ155 / Issue #97 candidate, each only on exact scope + applicable CI SUCCESS + no required review blocker + race-free expected-head. If either merge moves integration, the other must refresh/revalidate before merge. BBB151 and #93 have no merge authorization.**

## Critical path

`F2/12.1 clean canonical production source proof post-#99` → `#97 pre-Beta startup/reveal` + `#89 F0/0.9 P1 refresh/exact-green` + `recent-reauth seam` in parallel where independent → `F2/15.1` → `F2/13.2 safe write surface` → `F1/1.7 → 1.8` → `#93 only if IN_ALPHA`; external F0/F3/F4 tails remain parallel.

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
