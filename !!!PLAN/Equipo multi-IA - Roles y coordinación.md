# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 078

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-074`: READ-ONLY audit Web action boundary + silent-loss on live baseline; no #81/#69/#70 mutation | NONE |
| BBB | F4 / 25.2 | `NIGHT-BBB-073`: SAME #79 exact final race-check + expected-head merge only if base/head/delta/CI remain exact | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-077`: SAME #83 readiness/reconcile transaction; history-preserving refresh if integration moved; NO MERGE | F3/19.1 READ-ONLY deployment/domain evidence map only while PRIMARY waits fresh CI |

**Baseline canónico al inicio CYCLE 078:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA073: no final result/handoff before CYCLE 078; superseded by AAA074 after fresh recalculation, not PASS.
- BBB072: no final result/handoff before CYCLE 078. GitHub real still shows #79 OPEN/non-draft at `a3c4d56e...`, exact base live `957f9777...`; BBB073 owns the next exact transaction.
- WOZ076: no final result/handoff before CYCLE 078. GitHub real still shows #83 draft/open at `52b58f56...`, exact base `957f9777...`; WOZ077 owns SAME #83 only.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 078: **BBB/#79**. AAA is read-only. WOZ owns only #83 and MUST NOT merge or move integration. If #79 merges before WOZ acts, WOZ must treat #83 as stale-base and use only history-preserving reconciliation + fresh exact-head CI. No force-push/rewrite.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real-browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F2/14.1 #81: open/stale; safe history-preserving reconcile surface unavailable.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.x #76: open/stale; parked; 19.1 may be audited read-only only as WOZ077 fallback.
- F3/20.1: software observability integrated; external tails remain.
- F3/20.2: #83 durable waitlist candidate; real 160-runtime + latency/error/queue/recovery + safety margin still missing.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete.
- F4/25.2 #79 exact candidate owned BBB073; beta/tester/signing evidence remains external.
- F4 D22/D23: signing/notarization/hardware external.

## Reglas

1. Cross-phase work only when real dependencies allow it.
2. One material piece = one owner.
3. Owner does preflight → implementation/audit → tests → CI → handoff.
4. Findings do not transfer ownership automatically; JOBS does so explicitly.
5. No automatic hopping.
6. Real blocker → JOBS explicitly reassigns.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
8. No `[x]` without evidence.
9. REUSE-FIRST + duplicate-check mandatory.
10. Material base/head change → refresh + applicable CI before integration.

## PRIMARY / CI-FALLBACK

- PRIMARY always first.
- CI-FALLBACK only if JOBS preauthorizes it and PRIMARY genuinely enters WAITING_CI/WAITING_EXTERNAL/merge-review equivalent.
- Fallback must be independent in files/branch/PR/ownership/dependencies; no scope expansion or blocked-gate leap.
- Worker never invents fallback.
- After fallback, worker rechecks PRIMARY before closing.

## Night Shift Ledger — CYCLE 078

```text
JOBS: baseline-start 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA073: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA074: ASSIGNED F2/13.2 READ_ONLY audit
AAA074 FALLBACK: NONE
BBB072: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB073: ASSIGNED SAME #79 final race-check + expected-head merge
BBB073 FALLBACK: NONE
WOZ076: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ077: ASSIGNED SAME #83 readiness/reconcile; NO MERGE
WOZ077 FALLBACK: F3/19.1 READ_ONLY only during WAITING_CI
ONLY_INTEGRATION_MUTATION: BBB/#79
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
