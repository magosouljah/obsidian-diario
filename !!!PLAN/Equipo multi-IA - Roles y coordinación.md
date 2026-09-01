# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 113

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-109`: minimum durable Review Save/Save All completion/no-silent-loss corrective; focused Web/no-Tauri tests; candidate only, NO MERGE | NONE |
| BBB | F2 / 15.1 | `NIGHT-BBB-108`: Empty Trash recent-reauth + strong confirmation + durable deterministic purge; candidate only, NO MERGE | only during genuine WAITING_CI: F1/1.7 blocker classification READ-ONLY |
| WOZ | F4 / 25.1 / #93 | `NIGHT-WOZ-112`: REUSE #93; final exact semantic/CI/race recheck; expected-head merge #93 only if exact/green/race-free | NONE |

**Baseline canónico CYCLE 113:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.

## Handoffs/resultados procesados — CYCLE 113

- AAA108: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB107: PR #93 exact-head candidate @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`; only three harness/evidence files; Windows Auth run `33468863393` SUCCESS, job `99734302105` SUCCESS including isolated auth assertions; D6/D7/Desktop Portability/Windows Import/secret scan SUCCESS. Result processed as `CANDIDATE_EXACT_GREEN / NO_MERGE`.
- WOZ111: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #92 remains OPEN/Ready/mergeable @ `9947380...`, exact base `134a293...`, exact-head workflows observed green; parked CYCLE113 because the higher-priority integration lane is #93.

## Serialización

AAA109 owns only durable Review. BBB108 owns only Trash/recent-reauth. WOZ112 owns only #93 review/integration. #92 and #89 have **no owner and no merge authority CYCLE113**. #85 remains external-owned; #76/#83 remain parked unless a material condition changes.

**Only integration mutation authorized CYCLE113: WOZ112 / PR #93, conditional on exact base/head, all applicable required CI SUCCESS and race-free expected-head check.**

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain; F0/0.8 administrative review closure does not close legal P0/P1 implementation/compliance.
- F0/0.9 #89 remains reusable/stale and must be refreshed/revalidated after current integration lane; AI-assisted audit ≠ independent pentest.
- Productive signing remains external despite #88 technical seam.
- F0/0.20 actual OAuth rotation is closed; do not repeat.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; governing steps are 1.7 then 1.8.
- F2/12.1: #91 integrated; #92 remains exact-base signed-out corrective candidate but parked CYCLE113; deployment/runtime proof still required after canonical code settles.
- F2/13.2 = AAA109. F2/15.1 = BBB108.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1: Windows Auth now has exact-green successor #93, but global 25.1 stays open until all journey evidence is complete; #93 integration = WOZ112.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => clean history-preserving refresh/reconstruction + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 113

```text
JOBS: baseline 134a293985c314eb09c238115e3bcb71e79f1810
AAA108: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
AAA109: ASSIGNED F2/13.2 durable Review; NO MERGE; FALLBACK NONE
BBB107: PR93 EXACT_GREEN / NO_MERGE
BBB108: ASSIGNED F2/15.1 Trash/recent-reauth; NO MERGE; FALLBACK F1/1.7 READ_ONLY only during WAITING_CI
WOZ111: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ112: ASSIGNED PR93 exact semantic/CI/race review + conditional merge
PR93: OPEN READY exact base 134a293 / head b2c4eb4 / Windows Auth + applicable exact-head CI green
PR92: OPEN READY exact base 134a293 / PARKED CYCLE113
PR89: OPEN READY STALE / PARKED CYCLE113
INTEGRATION_MUTATION: WOZ112 PR93 ONLY IF EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
