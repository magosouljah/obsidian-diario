# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 107

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 | `NIGHT-AAA-103`: public Web `Loading Galer`; reproduce/isolate/minimum Web-only corrective, tests + no-Tauri + exact-head CI; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-102`: #84 WDIO/Tauri causal attribution from sanitized tuple; harness correction only if HARNESS_ONLY_PROVEN; refresh exact-base + packaged Auth; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-106`: REUSE #89; security review + history-preserving refresh + exact-head applicable CI; expected-head merge #89 only if green/race-free | READ-ONLY #90 readiness map only while #89 genuinely WAITING_CI |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Handoffs/resultados procesados — CYCLE 107

- AAA102: no final result/handoff => `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB101: no final result/handoff => `NO_RESULT / SUPERSEDED / NOT_PASS`. Último factual BBB099 = `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- WOZ105: no final result/handoff => `NO_RESULT / SUPERSEDED / NOT_PASS`. Último final verificable WOZ104 = `DONE / INTEGRATED`, Issue #41 `5486854786`.
- PR #89: OPEN/Ready al preflight, head `daf87da6ffd604ccac991311036919ae2de9bd7a`, stale base `816f946c...`; AI-assisted audit + DNS-rebinding hardening candidate. Assigned WOZ106.
- PR #84: OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, stale base `816f946c...`; packaged Auth literal remains red. Assigned BBB102.
- PR #90: readiness-only; owner rotation external. Read-only fallback only.
- PR #88: Authenticode/RFC3161 candidate; production signing explicitly NO-GO pending RO inputs/authorization.
- PR #85 remains external/owner-owned; do not collide.
- #76/#83 remain parked pending material tooling/surface changes.

## Serialización

AAA103 owns only Web startup. BBB102 owns only #84 evidence/harness. WOZ106 owns #89 review/refresh/integration. **The only integration mutation authorized CYCLE 107 is WOZ106 merging PR #89 after a history-preserving refresh to live baseline, exact-head applicable CI SUCCESS + race-free expected-head recheck.** #90 is fallback READ-ONLY only. #85 external owner remains separate. #88 has no nocturnal integration authorization.

## Holding / blocked items

- F0/1.2 external tails remain after #86/#87; F0/2.2 external/admin tail remains.
- F0/0.9 P1 DNS-rebinding candidate = WOZ106/#89; AI-assisted audit does not equal external pentest.
- F0 signing = #88 + RO/provider/cert/custody/RFC3161 inputs external.
- F0 secret rotation = #90 software readiness; actual rotation owner-side external.
- F1/D10.2 not ready; no owner this cycle because its technical blockers are assigned elsewhere.
- F2/12.1 = AAA103; cold/warm real timings remain separate after startup works.
- F2/13.2 durable Review open/unowned; F2/15.1 recent-reauth/confirmation/purge open/unowned.
- F3/18.2 provider/payment external.
- F3/19.1 #87 software integrated; DNS/SAN/deploy/runtime/support/OAuth/legal tails remain.
- F3/19.2 #76 tooling/surface-blocked; F3/20.2 #83 tooling-blocked + runtime160 pending.
- F4/25.1 #84 = BBB102; signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 107

```text
JOBS: baseline-start 38517c8065063206fed530028e4e8d20208f3807
AAA102: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA103: ASSIGNED F2/12.1 Loading Galer; FALLBACK NONE
BBB101: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB102: ASSIGNED #84 causal attribution/harness-only correction; FALLBACK NONE
WOZ105: NO_RESULT -> SUPERSEDED / NOT_PASS
WOZ106: ASSIGNED F0/#89; FALLBACK READ_ONLY #90 WHEN WAITING_CI
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
PR88: PRODUCTION_SIGNING_NO_GO / RO_INPUTS_REQUIRED
PR89: OPEN READY STALE_BASE / REFRESH_REQUIRED
PR90: READINESS_ONLY / OWNER_ROTATION_EXTERNAL
INTEGRATION_MUTATION: WOZ106 PR89 ONLY IF REFRESHED_EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
