# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 091

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-087`: minimum Review Save/Save All durable action-boundary corrective + executable no-silent-loss/Tauri call-spies; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-086`: sole bounded owner of #74/#84 product-auth lineage; minimum token-persistence corrective + exact packaged Windows evidence; NO MERGE | NONE |
| WOZ | F2 / 12.1 | `NIGHT-WOZ-090`: READ-ONLY real-browser cold/warm startup evidence on live integration; no code/PR/infra/integration mutation | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 091

- AAA086: no final result/handoff; superseded; NOT_PASS.
- BBB085: `BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED`. Exact #84 Windows auth run `33407580887` / job `99538870371` reached the real packaged test and failed because Desktop login did not persist the returned session token. No harness-only correction justified. Issue #41 `5481842956`.
- WOZ089: no final result/handoff; superseded; NOT_PASS.
- #83 remains exact at head `803b2143...`, base `816f946c...`, mergeable and exact-head green, but PARKED/TOOLING_BLOCKED after the dedicated Ready action failed on `Repository.fullDatabaseId`.
- #79 remains latest material integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

**No worker may mutate integration in CYCLE 091.** #83 remains intentionally parked until the Ready path materially changes or a valid non-bypass human/tooling action exists. Any unexpected integration movement invalidates stale exact-head assumptions and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime = WOZ090 read-only.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA087.
- F2/13.2 durable Review Save boundary = AAA087.
- F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails.
- F3/19.1 external canonical web/API/DNS/TLS/status/OAuth/sender/deployment facts required.
- F3/19.2 #76 legal text frozen.
- F3/20.2 #83 tooling-blocked; runtime 160 still independently required after eventual integration.
- F4/25.1 windows/auth product corrective + evidence lineage = BBB086; #72 stale/frozen and overlaps Review work.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 091

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA086: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA087: ASSIGNED F2/13.2 durable Review Save boundary
AAA087 FALLBACK: NONE
BBB085: BLOCKED_STOP -> PRODUCT_LOGIC_IMPLICATED / #84 auth red
BBB086: ASSIGNED #74/#84 minimum product-auth corrective + exact evidence, NO MERGE
BBB086 FALLBACK: NONE
WOZ089: NO_RESULT -> SUPERSEDED / NOT_PASS
WOZ090: ASSIGNED F2/12.1 READ_ONLY_BROWSER_COLD_WARM
WOZ090 FALLBACK: NONE
INTEGRATION_MUTATION: NONE
RELEASE: NO-GO
F5: CLOSED
```
