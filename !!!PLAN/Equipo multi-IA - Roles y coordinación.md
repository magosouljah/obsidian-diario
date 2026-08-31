# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 080

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-076`: executable Web/Tauri call-spy + Save All partial-failure/conflict/retry evidence; solo fix F2 mínimo si test prueba gap; NO MERGE | NONE |
| BBB | F4 / 25.2 | `NIGHT-BBB-075`: SAME #79 exact final race-check + expected-head merge solo si base/head/file-delta/CI permanecen exactos | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-079`: REUSE #78; runtime materially aplicable 160 + latency/error/queue/recovery/safety margin; no code/infra y no tocar #83 | F3/19.1 READ-ONLY evidence map solo durante genuine WAITING_EXTERNAL_RUNTIME tras operación externa iniciada |

**Baseline canónico al inicio CYCLE 080:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA075: no final result/handoff before CYCLE 080; superseded by AAA076, not PASS. AAA071 remains reusable evidence; no repeat broad audit.
- BBB074: no final result/handoff before CYCLE 080. GitHub: #79 OPEN/non-draft/mergeable @ `a3c4d56e...`, exact base live `957f9777...`, one docs-only file, exact-head applicable workflows concluded green where required. BBB075 owns the next transaction.
- WOZ078: `BLOCKED_STOP`; #83 OPEN/DRAFT @ `52b58f56...`, exact base `957f9777...`, scoped 3-file delta and exact-head CI success. Draft→Ready connector path failed on `Repository.fullDatabaseId`; no mutation; fallback not eligible. JOBS moves WOZ to independent runtime evidence rather than repeating the same tooling blocker.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 080: **BBB/#79**. AAA may create its own bounded F2 candidate but cannot merge integration. WOZ performs runtime/read-only evidence only and MUST NOT mutate #83 or integration. If #79 merges, #83 becomes stale-base and requires a future explicit history-preserving reconciliation assignment + fresh exact-head CI.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real-browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F2/13.2: executable evidence/fix AAA076 active.
- F2/14.1 #81: open/stale; safe reconciliation unavailable.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.x #76: open/stale; parked; 19.1 only WOZ079 conditional read-only fallback.
- F3/20.1: software observability integrated; external tails remain.
- F3/20.2: #83 durable waitlist candidate parked Draft due tooling; runtime 160 evidence WOZ079 active.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete.
- F4/25.2 #79 exact candidate owned BBB075; beta/tester/signing evidence remains external.
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

## Night Shift Ledger — CYCLE 080

```text
JOBS: baseline-start 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA075: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA076: ASSIGNED F2/13.2 executable evidence/fix slice
AAA076 FALLBACK: NONE
BBB074: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB075: ASSIGNED SAME #79 final race-check + expected-head merge
BBB075 FALLBACK: NONE
WOZ078: BLOCKED_STOP Draft->Ready connector tooling; no mutation
WOZ079: ASSIGNED F3/20.2 applicable 160 runtime evidence; no #83 mutation
WOZ079 FALLBACK: F3/19.1 READ_ONLY only during genuine WAITING_EXTERNAL_RUNTIME
ONLY_INTEGRATION_MUTATION: BBB/#79
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
