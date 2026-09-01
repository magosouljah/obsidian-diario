# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 109

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 12.1 | `NIGHT-AAA-105`: public Web `Loading Galer`; reproduce/isolate/minimum Web-only corrective, tests + no-Tauri + exact-head CI; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-104`: #84 WDIO/Tauri causal attribution; harness correction only if HARNESS_ONLY_PROVEN; refresh exact-base + packaged Auth; NO PRODUCT MUTATION / NO MERGE | NONE |
| WOZ | F0 / 0.9 / #89 | `NIGHT-WOZ-108`: REUSE #89; reconcile #88 merged, security review + history-preserving refresh + exact-head applicable CI; expected-head merge #89 only if green/race-free | READ-ONLY #90 readiness map only while #89 genuinely WAITING_CI |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.

## Handoffs/resultados procesados — CYCLE 109

- AAA104: no final result/handoff verificable => `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB103: no final result/handoff verificable => `NO_RESULT / SUPERSEDED / NOT_PASS`; último factual BBB099 = `BLOCKED_STOP / AMBIGUOUS`.
- WOZ107: no final result/handoff verificable => `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio factual independiente: #88 `MERGED` como `1dbf60e...`, candidate `dcf3e138...`, exact parents `38517c...` + `dcf3e138...`; technical/preparatory seam only, production signing NO-GO.
- #89 live: OPEN/Ready/mergeable @ `daf87da6...`, stale base `816f946c...`; refresh exact-head requerido. Assigned WOZ108.
- #84 live: OPEN/Ready/mergeable @ `f53d46f...`, stale base `816f946c...`; Windows Auth literal sigue FAILURE. Assigned BBB104.
- #90 readiness-only; actual OAuth rotation external. #85 external-owned. #76/#83 parked pending material tooling/surface changes.

## Serialización

AAA105 owns only Web startup. BBB104 owns only #84 evidence/harness. WOZ108 owns #89 review/refresh/integration. **The only integration mutation authorized CYCLE 109 is WOZ108 merging PR #89 after history-preserving refresh to live baseline, exact-head applicable CI SUCCESS + race-free expected-head recheck.** #90 fallback is READ-ONLY only. #85 external owner remains separate.

## Holding / blocked items

- F0/1.2 y 2.2 external/admin tails remain; F0/0.8 review administrative closed but legal P0/P1 backlog remains.
- F0/0.9 = WOZ108/#89; AI-assisted audit does not equal external pentest.
- F0 productive signing = external RO/provider/cert/custody/RFC3161 inputs despite #88 technical seam integrated.
- F0 actual secret rotation = #90 readiness + owner-side action.
- F1/D10.2 not ready; blockers remain F2/12.1, F4/25.1 and closure/RO scope decision for F2/13.2 + 15.1.
- F2/12.1 = AAA105; cold/warm real timings remain separate after startup works.
- F2/13.2 durable Review open/unowned; F2/15.1 recent-reauth/confirmation/purge open/unowned.
- F3/18.2 provider/payment external; F3/19.2 legal implementation open; F3/20.2 #83 + runtime160 pending.
- F4/25.1 #84 = BBB104; productive signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 109

```text
JOBS: baseline-start 1dbf60e58ca970c47d387b303e141e30e2b8eef5
AAA104: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
AAA105: ASSIGNED F2/12.1 Loading Galer; FALLBACK NONE
BBB103: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
BBB104: ASSIGNED #84 causal attribution/harness-only correction; FALLBACK NONE
WOZ107: NO_RESULT_VISIBLE -> SUPERSEDED / NOT_PASS
WOZ108: ASSIGNED F0/#89; FALLBACK READ_ONLY #90 WHEN WAITING_CI
PR88: MERGED -> 1dbf60e / TECHNICAL_PREPARATORY_SIGNING_ONLY / PRODUCTION_NO_GO
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
PR89: OPEN READY STALE_BASE / REFRESH_REQUIRED
PR90: READINESS_ONLY / OWNER_ROTATION_EXTERNAL
INTEGRATION_MUTATION: WOZ108 PR89 ONLY IF REFRESHED_EXACT_GREEN_RACE_FREE
RELEASE: NO-GO
F5: CLOSED
```
