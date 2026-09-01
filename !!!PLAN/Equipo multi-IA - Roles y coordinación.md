# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 110

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 / #91 | `NIGHT-AAA-106`: REUSE #91; finish exact-head CI and conditionally merge #91 only if exact/race-free; public runtime remains separate | READ-ONLY F2/13.2 closure map only while #91 genuinely WAITING_CI |
| BBB | F4 / 25.1 / #84 | `NIGHT-BBB-105`: prove WDIO/Tauri causal attribution; harness correction only if HARNESS_ONLY_PROVEN; refresh to live head; literal packaged Auth; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-109`: REUSE #89; reconcile #88/#90, history-preserving refresh to live head + exact-head security CI; NO MERGE this cycle | NONE |

**Baseline canónico CYCLE 110:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843` at JOBS preflight. GitHub live prevails if AAA106 changes it by authorized #91 merge.

## Handoffs/resultados procesados — CYCLE 110

- AAA105: matching Issue #41 handoff verified → `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`; candidate PR #91 @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`, exact base `78dd55b...`. Root cause: bootstrap-critical `WebTransportWorkerClient.request()` could wait forever on a silent Worker. Bounded 30 s deadline added only for `initialize` / `verify` / `get_index`; no generic loader timeout; long transfers remain unbounded.
- BBB104: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`; last factual BBB099 remains `BLOCKED_STOP / AMBIGUOUS`.
- WOZ108: no final result/handoff verified → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Independent material change: PR #90 merged as `78dd55b72142e69ea32ba6c1ba6d43e246ac6843`, candidate `3f2063cf16fe63913dced6d57dc8a6cb46e12169`; software/readiness slice only. Actual OAuth credential rotation + deploy/verify/revoke remains owner-side external.
- #91 exact-head CI at assignment: Web Production Build, D6, D7, temp-auth compile and F0/0.20 secret scan SUCCESS; Test Desktop Portability still in progress. No final green claim until complete.
- #89 remains OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; needs current refresh. #84 remains evidence lineage and literal Windows Auth remains NOT_PASS.

## Serialización

AAA106 owns #91 and **the only integration mutation authorization CYCLE 110**. BBB105 owns #84 evidence/harness only. WOZ109 owns #89 review/refresh branch only and may not merge. This prevents #89 from racing the higher-priority #91 integration. #85 remains external-owned; #76/#83 remain parked unless tooling/surface changes materially.

## Holding / blocked items

- F0/1.2 + 2.2 external/admin tails remain; F0/0.8 administrative AI-assisted review closure does not close legal P0/P1 implementation/compliance.
- F0/0.9 = WOZ109/#89; AI-assisted audit ≠ independent pentest.
- F0 productive signing remains external despite #88 technical seam.
- F0/0.20 readiness software is integrated via #90; actual OAuth rotation/deploy/E2E/revoke remains external.
- F1/D10.2 map = complete, outcome `ALPHA CANDIDATE NOT READY`; next governing step is 1.7 blocker closure/classification, then 1.8 RO GO/NO-GO.
- F2/12.1 = AAA106/#91; integration + public authenticated runtime evidence + cold/warm timing remain.
- F2/13.2 durable Review open; F2/15.1 recent-reauth/confirmation/purge open unless explicit RO alpha exclusion.
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
AAA105: CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING -> PROCESSED
AAA106: ASSIGNED PR91 exact-head validation + conditional merge; FALLBACK READ_ONLY F2/13.2 while WAITING_CI
BBB104: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
BBB105: ASSIGNED #84 causal attribution/harness-only correction; NO MERGE; FALLBACK NONE
WOZ108: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ109: ASSIGNED #89 review/refresh/exact-head CI; NO MERGE; FALLBACK NONE
PR90: MERGED -> 78dd55b / READINESS_SOFTWARE_ONLY / ACTUAL_ROTATION_EXTERNAL
PR91: OPEN READY EXACT_BASE @ 35d44a0d / CI_PARTIAL_GREEN_WAITING_PORTABILITY
PR89: OPEN READY STALE_BASE / REFRESH_REQUIRED
PR84: WINDOWS_AUTH_LITERAL_NOT_PASS
INTEGRATION_MUTATION: AAA106 PR91 ONLY IF EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
