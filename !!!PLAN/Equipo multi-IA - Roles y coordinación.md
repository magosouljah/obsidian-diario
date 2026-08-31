# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 075

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-071`: READ-ONLY audit Web action boundary + silent-loss on live baseline; no #81/#69/#70 mutation | NONE |
| BBB | F4 / 25.2 | `NIGHT-BBB-070`: SAME #79 exact final race-check + expected-head merge only if base/head/delta/CI remain exact | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-074`: minimal durable user-waitlist persistence/recovery/isolation + tests + fresh CI; no merge | F3/18.2 read-only billing scenario evidence map only during genuine CI/review wait |

**Baseline canónico al inicio CYCLE 075:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA070: `PENDING / STOP_HISTORY_RECONCILE_UNAVAILABLE`; #81 remains OPEN @ `709151082...`; no mutation/merge. Worker could not post its handoff; JOBS carries it to Issue #41.
- BBB069: `WAITING_CI`; #79 refreshed history-preservingly to `a3c4d56e8317d7711832154ecc72afe581d2b309`, base exact `957f9777...`, behind=0, one docs-only file. F4/25.1 read-only fallback completed.
- JOBS postcheck after BBB069: exact-head Required CI is `SUCCESS`; no in-progress or failed exact-head check observed. #79 still needs final fresh race-check + merge by BBB070; no merge claim yet.
- WOZ073: no final result/handoff before CYCLE 075; superseded by WOZ074 after recalculation, not PASS.
- F3/20.2 target remains 80 expected / 160 validation; durable waitlist remains a documented GAP and runtime PASS is not implied.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 075: **BBB/#79**. AAA is read-only. WOZ may create/update its own candidate branch/PR but MUST NOT merge or move integration. If #79 merges, all other candidates must rebase/reconcile against the new live baseline and obtain applicable fresh evidence before later integration.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real-browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F2/14.1 #81: open/stale; safe history-preserving reconcile surface unavailable to AAA070.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.x #76: open/stale; parked this cycle.
- F3/20.1: software observability integrated; external tails remain.
- F3/20.2: durable waitlist now owned by WOZ074; 160 runtime + latency/error/queue/recovery + safety margin still missing regardless of software progress.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete; Windows playback is the smallest independent desktop journey identified by BBB069, but is not assigned this cycle.
- F4/25.2 #79: exact-head green candidate owned BBB070; real beta/tester/signing evidence remains external.
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

## Night Shift Ledger — CYCLE 075

```text
JOBS: baseline-start 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA070: PENDING STOP_HISTORY_RECONCILE_UNAVAILABLE -> PROCESSED
AAA071: ASSIGNED F2/13.2 READ_ONLY audit
AAA071 FALLBACK: NONE
BBB069: WAITING_CI -> postcheck exact-head CI GREEN; no merge yet
BBB070: ASSIGNED SAME #79 final race-check + expected-head merge
BBB070 FALLBACK: NONE
WOZ073: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ074: ASSIGNED F3/20.2 durable waitlist; NO MERGE
WOZ074 FALLBACK: F3/18.2 READ_ONLY only during genuine wait
ONLY_INTEGRATION_MUTATION: BBB/#79
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
