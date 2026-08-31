# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 092

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-088`: minimum Review Save/Save All durable action-boundary corrective + executable no-silent-loss/Tauri call-spies; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-087`: sole bounded owner of #74/#84 product-auth lineage; minimum token-persistence corrective + exact packaged Windows evidence; NO MERGE | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-091`: #83 dedicated Draft→Ready, exact-head/race recheck and integration if unchanged/green; only integration mutator | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 092

- AAA087: no final result/handoff; superseded; NOT_PASS.
- BBB086: no final result/handoff; superseded; NOT_PASS.
- WOZ090: `BLOCKED_STOP`; existing real-browser harness was verified on exact baseline, but the connected surface cannot execute Vite/WebdriverIO/Chrome, so cold/warm timing remains UNVERIFIED. Issue #41 `5482199628`.
- #83 remains exact at head `803b2143...`, base `816f946c...`, mergeable and exact-head green. Material change: a dedicated `mark_pull_request_ready_for_review` connector action is now available, so the old tooling blocker is no longer assumed permanent.
- #79 remains latest material integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

**Only WOZ091 may mutate integration in CYCLE 092, and only for exact PR #83 after dedicated Ready + same-head/base/scope/CI/race recheck.** Any movement invalidates stale exact-head assumptions and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime needs an execution surface with checkout + Node/npm + Chrome/WebDriver; no owner this cycle.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA088.
- F2/13.2 durable Review Save boundary = AAA088.
- F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails.
- F3/19.1 external canonical web/API/DNS/TLS/status/OAuth/sender/deployment facts required.
- F3/19.2 #76 legal text frozen.
- F3/20.2 #83 process transaction = WOZ091; runtime 160 still independently required after integration.
- F4/25.1 windows/auth product corrective + evidence lineage = BBB087; #72 stale/frozen and overlaps Review work.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 092

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA087: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA088: ASSIGNED F2/13.2 durable Review Save boundary
AAA088 FALLBACK: NONE
BBB086: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB087: ASSIGNED #74/#84 minimum product-auth corrective + exact evidence, NO MERGE
BBB087 FALLBACK: NONE
WOZ090: BLOCKED_STOP -> browser/runtime unavailable
WOZ091: ASSIGNED #83 READY_RECHECK_INTEGRATE
WOZ091 FALLBACK: NONE
INTEGRATION_MUTATION: WOZ091/#83 ONLY
RELEASE: NO-GO
F5: CLOSED
```
