# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Model: fixed-owner puzzle. GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 079

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-075`: convertir finding AAA071 en executable Web/Tauri call-spy + Save All partial-failure/conflict/retry evidence; solo fix F2 mínimo si el test falla; NO MERGE | NONE |
| BBB | F4 / 25.2 | `NIGHT-BBB-074`: SAME #79 exact final race-check + expected-head merge solo si base/head/file-delta/CI permanecen exactos | NONE |
| WOZ | F3 / 20.2 | `NIGHT-WOZ-078`: SAME #83 readiness/reconcile transaction; history-preserving refresh si integration movió; NO MERGE | F3/19.1 READ-ONLY deployment/domain evidence map solo mientras PRIMARY espera fresh CI tras un head reconciliado |

**Baseline canónico al inicio CYCLE 079:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.

## Handoffs/resultados procesados

- AAA074: no final result/handoff before CYCLE 079; superseded by AAA075, not PASS. REUSE-FIRST consume el handoff AAA071: audit DONE/partial, Save All silent-loss/error-summary gap plausible y executable Web/Tauri call-spy proof faltante.
- BBB073: no final result/handoff before CYCLE 079. GitHub real: #79 OPEN/non-draft @ `a3c4d56e...`, exact base live `957f9777...`, único changed file `docs/beta/0.9.0-beta.1-readiness.md`, Required CI exact-head SUCCESS. BBB074 posee la siguiente transacción.
- WOZ077: no final result/handoff before CYCLE 079. GitHub real: #83 draft/open @ `52b58f56...`, exact base `957f9777...`, tres changed files limitados a waitlist/test/workflow, Required CI exact-head SUCCESS. WOZ078 posee SAME #83 only.

## Serialización de integración

Only one integration mutation is authorized in CYCLE 079: **BBB/#79**. AAA puede crear su propio candidate F2 pero no mergear integration. WOZ owns only #83 and MUST NOT merge or move integration. If #79 merges before WOZ acts, WOZ must treat #83 as stale-base and use only history-preserving reconciliation + fresh exact-head CI. No force-push/rewrite.

## Holding / blocked items

- F0 1.2/2.2: external/administrative.
- F1 D10.1: off-provider/off-account proof; D10.2 RO decision.
- F2/12.1: real-browser cold/warm runtime.
- F2/13.1 #69/#70: frozen.
- F2/13.2: audit consumed; executable evidence/fix slice AAA075 active.
- F2/14.1 #81: open/stale; safe history-preserving reconcile surface unavailable.
- F3/18.2: provider/payment scenarios remain open.
- F3/19.x #76: open/stale; parked; 19.1 only WOZ078 conditional read-only fallback.
- F3/20.1: software observability integrated; external tails remain.
- F3/20.2: #83 durable waitlist candidate; real 160-runtime + latency/error/queue/recovery + safety margin still missing.
- F4/windows-auth #74/#71 and windows-review #72: frozen.
- F4/25.1 incomplete.
- F4/25.2 #79 exact candidate owned BBB074; beta/tester/signing evidence remains external.
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

## Night Shift Ledger — CYCLE 079

```text
JOBS: baseline-start 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA074: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA071: REUSED DONE/AUDIT_ONLY finding
AAA075: ASSIGNED F2/13.2 executable evidence/fix slice
AAA075 FALLBACK: NONE
BBB073: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB074: ASSIGNED SAME #79 final race-check + expected-head merge
BBB074 FALLBACK: NONE
WOZ077: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ078: ASSIGNED SAME #83 readiness/reconcile; NO MERGE
WOZ078 FALLBACK: F3/19.1 READ_ONLY only during genuine WAITING_CI after fresh reconciled head
ONLY_INTEGRATION_MUTATION: BBB/#79
DUPLICATE_WORK: prevented
RELEASE: NO-GO
F5: CLOSED
```
