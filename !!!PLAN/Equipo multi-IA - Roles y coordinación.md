# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 115

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-111`: minimum durable Review Save/Save All completion/no-silent-loss corrective; focused Web/no-Tauri tests; candidate only, NO MERGE | NONE |
| BBB | F2 / 15.1 | `NIGHT-BBB-110`: Empty Trash recent-reauth + strong confirmation + durable deterministic purge; candidate only, NO MERGE | only during genuine WAITING_CI: F1/1.7 blocker classification READ-ONLY |
| WOZ | F4 / 25.1 / #93 | `NIGHT-WOZ-114`: REUSE #93; final exact semantic/CI/race recheck; expected-head merge #93 only if exact/green/race-free | NONE |

**Baseline canónico CYCLE 115:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.

## Handoffs/resultados procesados — CYCLE 115

- AAA110: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB109: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- WOZ113: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #93 remains OPEN/Ready/mergeable @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`; three harness/evidence files. Exact-head Windows Auth `33468863393` SUCCESS; D6 `33468863373`, D7 `33468863387`, Desktop Portability `33468863399`, Windows Import `33468863402`, secret scan `33468863418` SUCCESS; staging skipped/non-applicable.
- PR #92 changed since prior plan snapshot: OPEN/Ready/mergeable, exact base `134a293...`, live head `bb67f61135f5767b5d7a8220265ff82317020949`; exact-head Web Production Build/D6/D7/Desktop Portability/Temp Auth Compile/secret scan SUCCESS. It remains PARKED/UNASSIGNED while #93 owns the only integration lane.
- PR #89 remains OPEN/Ready/mergeable @ `daf87da6...` on stale base `816f946c...`; parked/unassigned.

## Serialización

AAA111 owns only durable Review. BBB110 owns only Trash/recent-reauth. WOZ114 owns only #93 review/integration. #92 and #89 have **no owner and no merge authority CYCLE115**. #85 remains external-owned; #76/#83 remain parked unless a material condition changes.

**Only integration mutation authorized CYCLE115: WOZ114 / PR #93, conditional on exact base/head, all applicable required CI SUCCESS and race-free expected-head check.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain; F0/0.8 administrative review closure does not close legal P0/P1 implementation/compliance.
- F0/0.9 #89 remains reusable/stale and must be refreshed/revalidated after current integration lane; AI-assisted audit ≠ independent pentest.
- Productive signing remains external despite #88 technical seam.
- F0/0.20 actual OAuth rotation is closed; do not repeat.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; governing steps are 1.7 then 1.8.
- F2/12.1: #91 integrated; #92 now has live exact-head green `bb67f611...` but remains parked; deployment/runtime proof still required after canonical code settles.
- F2/13.2 = AAA111. F2/15.1 = BBB110.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1: Windows Auth has exact-green successor #93, but global 25.1 stays open until all journey evidence is complete; #93 integration = WOZ114.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 115

```text
JOBS: baseline 134a293985c314eb09c238115e3bcb71e79f1810
AAA110: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
AAA111: ASSIGNED F2/13.2 durable Review; NO MERGE; FALLBACK NONE
BBB109: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
BBB110: ASSIGNED F2/15.1 Trash/recent-reauth; NO MERGE; FALLBACK F1/1.7 READ_ONLY only during WAITING_CI
WOZ113: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ114: ASSIGNED PR93 exact semantic/CI/race review + conditional merge
PR93: OPEN READY exact base 134a293 / head b2c4eb4 / exact-head applicable workflows green
PR92: OPEN READY exact base 134a293 / head bb67f611 / exact-head applicable workflows green / PARKED CYCLE115
PR89: OPEN READY STALE / PARKED CYCLE115
INTEGRATION_MUTATION: WOZ114 PR93 ONLY IF EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
