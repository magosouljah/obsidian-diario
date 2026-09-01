# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 104

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 | `NIGHT-AAA-100`: public Web `Loading Galer` bootstrap/runtime blocker; minimum Web-only corrective, tests + no-Tauri + exact-head CI; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-099`: #84 sanitized first-request causal trace; diagnostic-only rerun if needed; harness correction only if HARNESS_ONLY_PROVEN; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 1.2 / #86 | `NIGHT-WOZ-103`: REUSE #86; exact review + exact-head applicable CI; expected-head merge #86 only if green/race-free | READ-ONLY #87 evidence map only while #86 genuinely WAITING_CI |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 104

- AAA099: no final result/handoff => `NO_RESULT / SUPERSEDED / NOT_PASS`. PR #86 appeared on `aaa/...` outside its F2/12.1 scope; not accepted as AAA099 completion and explicitly transferred to WOZ103.
- BBB098: no final result/handoff => `NO_RESULT / SUPERSEDED / NOT_PASS`; #84 remains exact `f53d46f...`, auth run `33449587244` / job `99676242317` FAILURE.
- WOZ102: Issue #41 `5486382155` => `BLOCKED_STOP / D10.2 NOT_READY_FOR_RO_DECISION / READ_ONLY_COMPLETE`; D6–D10.1 remain proven; blockers reduced to F2/12.1, F4/25.1 and applicability/cierre of F2/13.2 + 15.1.
- PR #86: OPEN/Ready/mergeable, exact base live, head `200474d061c63406774da8d21bd22460a8bd0312`; applicable CI still in progress at final JOBS preflight; not PASS yet.
- PR #87: OPEN/Ready/mergeable, exact base live, head `d5d129c578355ca2ff6399bd2e6ec752c9f81618`; software security/status candidate with DNS/deploy/runtime explicitly UNVERIFIED.
- PR #85 remains external/owner-owned; do not collide.
- #76/#83 remain parked pending material tooling changes.

## Serialización

AAA100 owns only Web startup. BBB099 owns only #84 evidence/harness. WOZ103 owns #86 review/integration only. **The only integration mutation authorized CYCLE 104 is WOZ103 merging PR #86 after exact-head applicable CI SUCCESS + race-free recheck.** #87 is fallback READ-ONLY only. #85 external owner remains separate.

## Holding / blocked items

- F0/1.2 external tails remain even if #86 implementation lands; F0/2.2 external/admin tail remains.
- F1/D10.2 not ready; no owner this cycle because its technical blockers are assigned elsewhere.
- F2/12.1 = AAA100; cold/warm real timings remain separate after startup works.
- F2/13.2 durable Review open/unowned; F2/15.1 recent-reauth/confirmation/purge open/unowned.
- F3/18.2 provider/payment external.
- F3/19.1 public infra proven; #87 software candidate does not prove status/runtime/support/OAuth tails.
- F3/19.2 #76 tooling-blocked; F3/20.2 #83 tooling-blocked + runtime160 pending.
- F4/25.1 #84 = BBB099; signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 104

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA099: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA100: ASSIGNED F2/12.1 Loading Galer; FALLBACK NONE
BBB098: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB099: ASSIGNED #84 causal trace; FALLBACK NONE
WOZ102: BLOCKED_STOP / D10.2 NOT_READY_FOR_RO_DECISION / READ_ONLY_COMPLETE
WOZ103: ASSIGNED F0/#86; FALLBACK READ_ONLY #87 WHEN WAITING_CI
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
PR86: OPEN READY EXACT_BASE / CI_IN_PROGRESS
PR87: OPEN READY EXACT_BASE / RUNTIME_UNVERIFIED
INTEGRATION_MUTATION: WOZ103 PR86 ONLY IF EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
