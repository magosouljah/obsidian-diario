# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 103

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 | `NIGHT-AAA-099`: public Web `Loading Galer` bootstrap/runtime blocker; bounded Web-only corrective, tests + no-Tauri + exact-head CI; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-098`: consume exact failed #84 auth diagnostic; classify first sanitized tuple; harness correction only if HARNESS_ONLY_PROVEN; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F1 / D10.2 | `NIGHT-WOZ-102`: refreshed alpha-readiness decision map READ-ONLY; no alpha/provider/infra mutation | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 103

- AAA098: no final result/handoff/candidate → `NO_RESULT / SUPERSEDED / NOT_PASS`; durable Review gap remains open but loses priority this cycle to public startup blocker.
- BBB097: Issue #41 `5486012736` = `WAITING_CI` on diagnostic-only #84 head `f53d46f...`; GitHub post-turn exact run `33449587244` / job `99676242317` finished FAILURE. CI wait resolved; `NOT_PASS`.
- WOZ101: no final result/handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Owner Issue #41 `5485984669`: public Web infra proven (`web-health`, auth-health, www→apex, TLS), but apex stalls at `Loading Galer`; functional bug separated from deploy.
- PR #85 remains external/owner-owned, OPEN/Ready, exact base live; live head `ab25e89570de66189612c7a4677161a73bbe5d5d`. Night workers do not mutate it.
- #83 remains exact OPEN/DRAFT with tooling blocker; #76 remains stale legal candidate blocked on history-preserving refresh surface.

## Serialización

**No worker is authorized to mutate integration in CYCLE 103.** AAA owns only public Web bootstrap/runtime functional slice and must STOP before shared auth/session/provider/deploy ownership. BBB owns only #84 evidence/harness. WOZ102 is READ-ONLY D10.2. #85 external owner remains separate. #76/#83 stay parked.

## Holding / blocked items

- F0 1.2/2.2 external/admin.
- F1 D10.1 CLOSED; D10.2 = WOZ102 READ-ONLY map, RO decision remains authoritative.
- F2/12.1 public startup bug = AAA099; cold/warm real timings remain separate after startup works.
- F2/13.1 #69/#70 frozen.
- F2/13.2 durable Review gap open, unowned CYCLE 103.
- F2/14.1 #81 stale/parked.
- F2/15.1 strong confirmation + recent-reauth + deterministic purge gaps; paused while BBB098 owns auth evidence boundary.
- F3/18.2 provider/payment live/staging proof external.
- F3/19.1 public infra proven; direct legal/public-route/support/OAuth tails remain; #85 external owner.
- F3/19.2 #76 blocked on refresh-capable execution surface.
- F3/20.2 #83 Ready process blocked; runtime 160 required after applicable integration.
- F4/25.1 #74/#84 = BBB098 evidence/harness only; exact packaged Windows Auth red.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 103

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA098: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA099: ASSIGNED F2/12.1 public Loading Galer bootstrap blocker; FALLBACK NONE
BBB097: WAITING_CI -> post-turn exact-head FAILURE / NOT_PASS
BBB098: ASSIGNED #84 first sanitized tuple causal attribution; FALLBACK NONE
WOZ101: NO_RESULT -> SUPERSEDED / NOT_PASS
WOZ102: ASSIGNED F1/D10.2 READ-ONLY decision map; FALLBACK NONE
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
PUBLIC_WEB_INFRA: PROVEN_OWNER_RUNTIME
PUBLIC_WEB_STARTUP: BLOCKED_LOADING_GALER
INTEGRATION_MUTATION: NONE
RELEASE: NO-GO
F5: CLOSED
```
