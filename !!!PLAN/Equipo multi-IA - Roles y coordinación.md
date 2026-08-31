# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 089

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-085`: minimum Review Save/Save All durable action-boundary corrective + executable no-silent-loss/Tauri call-spies; NO MERGE | F2/12.1 READ-ONLY real-browser cold/warm evidence only during genuine external CI wait |
| BBB | F4 / 25.1 | `NIGHT-BBB-084`: diagnose exact #84 Windows auth assertion failure; harness/workflow-only correction allowed if attributable; product finding => STOP; NO MERGE | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-088`: exact/race-free #83 Draft→Ready→merge transaction only; verify final integration SHA; runtime 160 remains open | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 089

- AAA084: no final result/handoff; superseded; NOT_PASS.
- BBB083: no final result/handoff; #84 unchanged; literal Windows auth remains FAILURE; superseded; NOT_PASS.
- WOZ087: no final result/handoff; #83 remains OPEN/DRAFT/unmerged; superseded; NOT_PASS.
- #83 remains exact at head `803b2143...`, base `816f946c...`, mergeable, 3-file scope and previously observed exact-head green CI.
- #74 remains product corrective lineage; #84 remains BBB's sole evidence candidate.
- #79 remains latest material integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

**Only WOZ088 may mutate integration in CYCLE 089**, and only for #83 after exact base/head/scope/CI revalidation and successful direct Draft→Ready transition. AAA/BBB may work bounded candidates but may not merge. Any unexpected integration movement invalidates stale exact-head assumptions and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime; AAA085 fallback only under exact WAITING_CI conditions.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA085; F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails.
- F3/19.1 external canonical web/API/DNS/TLS/status/OAuth/sender/deployment facts required; no active worker mutation.
- F3/19.2 #76 legal text remains frozen.
- F3/20.2 #83 integration = WOZ088; post-merge runtime 160 independently required; #78 local/synthetic-only insufficient.
- F4/25.1 windows/auth exact failing evidence = BBB084; #72 stale/frozen and overlaps active Review surface materially.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 089

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA084: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA085: ASSIGNED F2/13.2 durable Review Save boundary
AAA085 FALLBACK: F2/12.1 READ_ONLY_BROWSER_COLD_WARM during WAITING_CI only
BBB083: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB084: ASSIGNED #84 exact failure attribution/correction, NO MERGE
BBB084 FALLBACK: NONE
WOZ087: NO_RESULT -> SUPERSEDED / NOT_PASS
WOZ088: ASSIGNED #83 exact Ready->merge transaction
WOZ088 FALLBACK: NONE
INTEGRATION_MUTATION: WOZ088 #83 ONLY
RELEASE: NO-GO
F5: CLOSED
```
