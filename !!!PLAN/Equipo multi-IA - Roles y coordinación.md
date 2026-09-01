# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 108

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 | `NIGHT-AAA-104`: public Web `Loading Galer`; reproduce/isolate/minimum Web-only corrective, tests + no-Tauri + exact-head CI; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-103`: #84 WDIO/Tauri causal attribution; harness correction only if HARNESS_ONLY_PROVEN; refresh exact-base + packaged Auth; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-107`: REUSE #89; security review + history-preserving refresh + exact-head applicable CI; expected-head merge #89 only if green/race-free | READ-ONLY #90 readiness map only while #89 genuinely WAITING_CI |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Handoffs/resultados procesados — CYCLE 108

- AAA103: no final result/handoff verificable al preflight => `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB102: no final result/handoff verificable al preflight => `NO_RESULT / SUPERSEDED / NOT_PASS`. Último factual BBB099 = `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- WOZ106: no final result/handoff verificable al preflight => `NO_RESULT / SUPERSEDED / NOT_PASS`. Último final verificable WOZ104 = `DONE / INTEGRATED`, Issue #41 `5486854786`.
- PR #89 live: OPEN/Ready @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, stale base `816f946c...`; old-head Required CI SUCCESS no sustituye refresh al baseline vivo. Assigned WOZ107.
- PR #84 live: OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, stale base `816f946c...`; Required CI old-head SUCCESS pero Windows Auth literal `33449587244` / `99676242317` continúa FAILURE. Assigned BBB103.
- PR #88 live: exact current base `38517c...`, pero production signing explícitamente NO-GO pending RO/provider/cert/custody/RFC3161 inputs; no nocturnal merge authorization.
- PR #90: readiness-only; owner rotation external. Read-only fallback only.
- PR #85 external/owner-owned; do not collide. #76/#83 parked pending material tooling/surface changes.

## Serialización

AAA104 owns only Web startup. BBB103 owns only #84 evidence/harness. WOZ107 owns #89 review/refresh/integration. **The only integration mutation authorized CYCLE 108 is WOZ107 merging PR #89 after history-preserving refresh to live baseline, exact-head applicable CI SUCCESS + race-free expected-head recheck.** #90 is fallback READ-ONLY only. #85 external owner remains separate. #88 has no nocturnal integration authorization.

## Holding / blocked items

- F0/1.2 external tails remain after #86/#87; F0/2.2 external/admin tail remains.
- F0/0.9 P1 DNS-rebinding candidate = WOZ107/#89; AI-assisted audit does not equal external pentest.
- F0 signing = #88 + RO/provider/cert/custody/RFC3161 inputs external.
- F0 secret rotation = #90 software readiness; actual rotation owner-side external.
- F1/D10.2 not ready; its minimum technical blockers remain F2/12.1, F4/25.1 and closure/RO scope decision for F2/13.2 + 15.1.
- F2/12.1 = AAA104; cold/warm real timings remain separate after startup works.
- F2/13.2 durable Review open/unowned; F2/15.1 recent-reauth/confirmation/purge open/unowned.
- F3/18.2 provider/payment external.
- F3/19.1 #87 software integrated; DNS/SAN/deploy/runtime/support/OAuth/legal tails remain.
- F3/19.2 #76 tooling/surface-blocked; F3/20.2 #83 tooling-blocked + runtime160 pending.
- F4/25.1 #84 = BBB103; signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 108

```text
JOBS: baseline-start 38517c8065063206fed530028e4e8d20208f3807
AAA103: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
AAA104: ASSIGNED F2/12.1 Loading Galer; FALLBACK NONE
BBB102: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
BBB103: ASSIGNED #84 causal attribution/harness-only correction; FALLBACK NONE
WOZ106: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ107: ASSIGNED F0/#89; FALLBACK READ_ONLY #90 WHEN WAITING_CI
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
PR88: EXACT_BASE_BUT_PRODUCTION_SIGNING_NO_GO / RO_INPUTS_REQUIRED
PR89: OPEN READY STALE_BASE / OLD_HEAD_CI_GREEN / REFRESH_REQUIRED
PR90: READINESS_ONLY / OWNER_ROTATION_EXTERNAL
INTEGRATION_MUTATION: WOZ107 PR89 ONLY IF REFRESHED_EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
