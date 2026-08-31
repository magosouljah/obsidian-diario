# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 085

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-081`: minimum Review Save/Save All durable action-boundary corrective + executable no-silent-loss/Tauri call-spies; NO MERGE | F2/12.1 READ-ONLY real-browser cold/warm evidence only during genuine external CI wait |
| BBB | F4 / 25.1 | `NIGHT-BBB-080`: reuse #71 harness on exact #74 `b3468003...` via bounded test/workflow-only lineage; prove literal packaged Windows auth; NO MERGE | NONE |
| WOZ | F3 / 20.2 / #83 | `NIGHT-WOZ-084`: exact #83 Ready-for-review + expected-head merge if exact/race-free | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados

- AAA080: no final result/handoff at CYCLE 085; superseded; NOT_PASS.
- BBB079: BLOCKED_STOP accepted. #71 old harness cannot prove refreshed #74 because histories diverge; generic #74 CI is not auth proof.
- WOZ083: no final result/handoff at CYCLE 085; superseded; NOT_PASS.
- #83 remains OPEN/DRAFT, mergeable, exact base `816f946c...`, head `803b2143...`, dedicated waitlist + applicable exact-head CI green.
- #74 remains OPEN/Ready/mergeable at `b3468003...`, base exact `816f946c...`.
- #79 remains latest integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

Only one integration mutation authorized in CYCLE 085: **WOZ/#83**. AAA and BBB may create/update bounded candidates but MUST NOT merge integration. Any integration race invalidates stale exact-head evidence and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime; may be AAA081 fallback only under exact conditions.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA081; F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails; F3/19.x #76 stale/frozen.
- F3/20.2 runtime 160 independently required even if #83 integrates; #78 local/synthetic-only insufficient.
- F4/25.1 windows/auth current proof BBB080; #72 stale/frozen and overlaps active Review surface materially.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 085

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA080: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA081: ASSIGNED F2/13.2 durable Review Save boundary
AAA081 FALLBACK: F2/12.1 READ_ONLY_BROWSER_COLD_WARM during WAITING_CI only
BBB079: BLOCKED_STOP / HARNESS_ATTRIBUTION_GAP / NOT_PASS
BBB080: ASSIGNED F4/25.1 exact-lineage packaged Windows auth proof
BBB080 FALLBACK: NONE
WOZ083: NO_RESULT -> SUPERSEDED / NOT_PASS
WOZ084: ASSIGNED F3/20.2 #83 Ready/merge transaction
WOZ084 FALLBACK: NONE
ONLY_INTEGRATION_MUTATION: WOZ/#83
RELEASE: NO-GO
F5: CLOSED
```
