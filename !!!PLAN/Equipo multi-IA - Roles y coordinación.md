# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 076

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-072`: READ-ONLY audit Web action boundary + silent-loss on live baseline; no #81/#69/#70 mutation | NONE |
| BBB | F4 / 25.2 | `NIGHT-BBB-071`: SAME #79 exact final race-check + expected-head merge only if base/head/delta/CI remain exact | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-075`: SAME #83 exact-head CI/readiness transaction; no code changes while CI runs; no merge | NONE |

**Baseline canónico al inicio CYCLE 076:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA071: no final result/handoff before CYCLE 076; superseded by AAA072 after fresh recalculation, not PASS.
- BBB070: no final result/handoff before CYCLE 076. GitHub real still shows #79 OPEN/non-draft/mergeable at `a3c4d56e...`, exact base live `957f9777...`, one docs-only file, Required CI exact-head SUCCESS. BBB071 is reissued because it remains the highest-value serialized transaction.
- WOZ074: WAITING_CI; PR #83 draft/open/mergeable @ `52b58f56...`; dedicated durable-waitlist workflow PASS. F3/18.2 read-only scenario map completed. CYCLE 076 postcheck still saw PR-wide Test - Desktop Portability in-progress; no merge/readiness promotion.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 076: **BBB/#79**. AAA is read-only. WOZ may change PR metadata only if exact-head CI is green and the authorized Draft→Ready flow succeeds without head/base movement; WOZ MUST NOT merge or move integration. If #79 merges, #83 becomes stale-base and must be reconciled/revalidated in a later explicit assignment.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real-browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F2/14.1 #81: open/stale; safe history-preserving reconcile surface unavailable.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.x #76: open/stale; parked.
- F3/20.1: software observability integrated; external tails remain.
- F3/20.2: #83 durable waitlist candidate WAITING_CI; real 160-runtime + latency/error/queue/recovery + safety margin still missing.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete.
- F4/25.2 #79 exact-head green candidate owned BBB071; beta/tester/signing evidence remains external.
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

## Night Shift Ledger — CYCLE 076

```text
JOBS: baseline-start 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA071: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA072: ASSIGNED F2/13.2 READ_ONLY audit
AAA072 FALLBACK: NONE
BBB070: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB071: ASSIGNED SAME #79 final race-check + expected-head merge
BBB071 FALLBACK: NONE
WOZ074: WAITING_CI / #83 candidate + billing fallback complete -> PROCESSED
WOZ075: ASSIGNED SAME #83 CI/readiness only; NO MERGE
WOZ075 FALLBACK: NONE
ONLY_INTEGRATION_MUTATION: BBB/#79
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
