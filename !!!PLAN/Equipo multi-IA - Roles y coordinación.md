# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 110

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-106`: minimum durable Review Save/Save All completion/no-silent-loss corrective; focused Web/no-Tauri tests; candidate only, NO MERGE | NONE |
| BBB | F4 / 25.1 / #84 | `NIGHT-BBB-105`: prove WDIO/Tauri causal attribution; harness correction only if HARNESS_ONLY_PROVEN; refresh to live head; literal packaged Auth; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-109`: REUSE #89; reconcile #88/#90/#91, history-preserving refresh to live head + exact-head security CI; expected-head merge #89 only if exact/green/race-free | READ-ONLY F1/1.7 blocker-classification prep only while #89 genuinely WAITING_CI |

**Baseline canónico final CYCLE 110:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.

## Handoffs/resultados procesados — CYCLE 110

- AAA105: matching Issue #41 handoff → root cause/fix candidate #91. During the same JOBS cycle, #91 finished exact-head portability/Required CI and was independently merged with RO authorization as `134a293985c314eb09c238115e3bcb71e79f1810`, parents `78dd55b...` + `35d44a0d...`. F2/12.1 now = `INTEGRATED / PUBLIC DEPLOY + AUTH RUNTIME PENDING`; not PASS.
- BBB104: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`; last factual BBB099 remains `BLOCKED_STOP / AMBIGUOUS`.
- WOZ108: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #90 previously merged as `78dd55b...`; software/readiness only. Actual OAuth credential rotation/deploy/verify/revoke remains external.
- #89 remains OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; now must reconcile #88/#90/#91 and refresh to `134a293...` or newer.
- #84 literal Windows Auth remains NOT_PASS.

## Serialización

The concurrent #91 merge invalidated the initial AAA106/#91 PRIMARY before worker execution. JOBS kept the same new CYCLE110 ID but rebound its scope to F2/13.2 to prevent duplicate work. AAA106 owns Review durability and NO MERGE. BBB105 owns #84 evidence/harness and NO MERGE. WOZ109 owns #89 and is now **the only integration mutation authorization CYCLE 110**, conditional on refreshed exact-base/head + all applicable exact-head CI SUCCESS + race-free expected-head check. #85 remains external-owned; #76/#83 remain parked unless tooling/surface changes materially.

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain; F0/0.8 administrative AI-assisted review closure does not close legal P0/P1 implementation/compliance.
- F0/0.9 = WOZ109/#89; AI-assisted audit ≠ independent pentest.
- F0 productive signing remains external despite #88 technical seam.
- F0/0.20 readiness software integrated via #90; actual OAuth rotation/deploy/E2E/revoke remains external.
- F1/D10.2 map complete, result `ALPHA CANDIDATE NOT READY`; next governing step 1.7 then 1.8.
- F2/12.1 code integrated via #91; **public deployment needs owner SSH key**, then authenticated runtime + cold/warm evidence. That external tail is not assigned to workers without credential access.
- F2/13.2 = AAA106. F2/15.1 remains open unless explicit RO alpha exclusion.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 runtime160 pending.
- F4/25.1 #84 = BBB105; productive signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 110

```text
JOBS: baseline-start 78dd55b72142e69ea32ba6c1ba6d43e246ac6843
CONCURRENT_PR91: MERGED -> 134a293985c314eb09c238115e3bcb71e79f1810 / EXACT_CI_PASS / PUBLIC_RUNTIME_PENDING
AAA105: CODE_FIX_PROVEN -> #91 INTEGRATED CONCURRENTLY
AAA106: REBOUND_BEFORE_EXECUTION -> F2/13.2 DURABLE_REVIEW; NO MERGE; FALLBACK NONE
BBB104: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
BBB105: ASSIGNED #84 causal attribution/harness-only correction; NO MERGE; FALLBACK NONE
WOZ108: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ109: ASSIGNED #89 refresh/security exact CI + conditional merge; FALLBACK READ_ONLY F1/1.7 WHEN WAITING_CI
PR90: MERGED -> 78dd55b / READINESS_SOFTWARE_ONLY / ACTUAL_ROTATION_EXTERNAL
PR89: OPEN READY STALE_BASE / REFRESH_REQUIRED_TO_134a293_OR_NEWER
PR84: WINDOWS_AUTH_LITERAL_NOT_PASS
INTEGRATION_MUTATION: WOZ109 PR89 ONLY IF REFRESHED_EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
