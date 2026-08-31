# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 074

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no code/infra | n/a |
| AAA | F2 / 14.1 | `NIGHT-AAA-070`: SAME #81 reconcile to live `957f9777...`, preserve minimal memory-safety slice + consolidated tests, fresh exact-head CI; no merge | F2/12.1 read-only startup readiness map only during genuine CI/review wait |
| BBB | F4 / 25.2 | `NIGHT-BBB-069`: SAME #79 refresh to live `957f9777...`, fresh exact-head CI, final race-check; only worker allowed to merge this cycle | F4/25.1 read-only remaining matrix gap map during genuine CI/merge wait |
| WOZ | F3 / 19.1 | `NIGHT-WOZ-073`: SAME #76 reconcile to live baseline, canonical Settings legal wiring, tests + fresh exact-head CI; no merge this cycle | NONE |

**Baseline canónico CYCLE 074:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA069: no final result/handoff nuevo before CYCLE 074; superseded by JOBS, not PASS.
- BBB068: no final result/handoff nuevo before CYCLE 074; superseded by JOBS, not PASS.
- WOZ072: no final result/handoff nuevo before CYCLE 074; superseded by JOBS, not PASS.
- #79 remains OPEN @ `60c2fb54...`, stale vs live baseline.
- #81 remains OPEN @ `709151082...`, stale vs live baseline.
- #76 remains OPEN @ `36d21860...`, stale vs live baseline and retains Settings canonical legal-copy gap.
- F3/20.2 target remains 80 expected / 160 validation; no runtime PASS implied.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 074: **BBB/#79**, and only after refresh to the current baseline + fresh applicable exact-head CI + final race-check. AAA and WOZ must not merge. If #79 merges, all other candidates require reconciliation to the new baseline before later integration.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.1: #76 active under WOZ073; production DNS/TLS/runtime and counsel evidence remain external.
- F3/20.1: software observability integrated; external observability tails remain.
- F3/20.2: 160 runtime + latency/error/queue/recovery + safety margin + durable user waitlist missing.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete; F4/25.2 #79 active under BBB069; real beta/tester/signing evidence remains external.
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

## Night Shift Ledger — CYCLE 074

```text
JOBS: baseline 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA069: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA070: ASSIGNED SAME #81 reconcile; NO MERGE
AAA070 FALLBACK: F2/12.1 READ_ONLY
BBB068: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB069: ASSIGNED SAME #79 refresh + fresh CI + possible serialized merge
BBB069 FALLBACK: F4/25.1 READ_ONLY
WOZ072: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ073: ASSIGNED SAME #76 reconcile/legal consistency; NO MERGE
WOZ073 FALLBACK: NONE
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
