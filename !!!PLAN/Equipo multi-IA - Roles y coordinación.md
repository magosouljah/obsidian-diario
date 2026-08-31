# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 090

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-086`: minimum Review Save/Save All durable action-boundary corrective + executable no-silent-loss/Tauri call-spies; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-085`: diagnose exact #84 Windows auth assertion failure; harness/workflow-only correction allowed if attributable; product finding => STOP; NO MERGE | NONE |
| WOZ | F2 / 12.1 | `NIGHT-WOZ-089`: READ-ONLY real-browser cold/warm startup evidence on live integration; no code/PR/infra/integration mutation | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 090

- AAA085: no final result/handoff; superseded; NOT_PASS.
- BBB084: no final result/handoff; #84 still exact-lineage candidate with Required CI green but literal Windows auth red; superseded; NOT_PASS.
- WOZ088: `BLOCKED_STOP`; dedicated #83 Draft→Ready action failed again with connector GraphQL `Repository.fullDatabaseId`; postcheck kept OPEN/DRAFT, exact head/base/scope, no merge. Issue #41 `5481554738`.
- #83 remains exact at head `803b2143...`, base `816f946c...`, mergeable and exact-head green, but PARKED/TOOLING_BLOCKED.
- #79 remains latest material integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

**No worker may mutate integration in CYCLE 090.** #83 is intentionally parked until the dedicated Ready path changes or a valid non-bypass human/tooling action exists. Any unexpected integration movement invalidates stale exact-head assumptions and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime = WOZ089 read-only.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA086.
- F2/13.2 durable Review Save boundary = AAA086.
- F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails.
- F3/19.1 external canonical web/API/DNS/TLS/status/OAuth/sender/deployment facts required.
- F3/19.2 #76 legal text frozen.
- F3/20.2 #83 tooling-blocked; runtime 160 still independently required after eventual integration.
- F4/25.1 windows/auth exact failing evidence = BBB085; #72 stale/frozen and overlaps Review work.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 090

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA085: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA086: ASSIGNED F2/13.2 durable Review Save boundary
AAA086 FALLBACK: NONE
BBB084: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB085: ASSIGNED #84 exact failure attribution/correction, NO MERGE
BBB085 FALLBACK: NONE
WOZ088: BLOCKED_STOP -> #83 Ready tooling failure, no merge
WOZ089: ASSIGNED F2/12.1 READ_ONLY_BROWSER_COLD_WARM
WOZ089 FALLBACK: NONE
INTEGRATION_MUTATION: NONE
RELEASE: NO-GO
F5: CLOSED
```
