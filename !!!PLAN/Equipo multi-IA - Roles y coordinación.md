# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 081

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-077`: executable Web/Tauri call-spy + Save All partial-failure/conflict/retry evidence; mínimo F2 fix si literal gap; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-076`: REUSE #71/#74, safe history-preserving refresh + current Windows auth journey/CI; NO MERGE | NONE |
| WOZ | F3 / 20.2 / #83 | `NIGHT-WOZ-080`: reconcile stale #83 onto live base, fresh CI, authorized Ready + exact merge if race-free | REUSE #78 runtime 160 READ-ONLY only during genuine WAITING_CI/external wait |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados

- BBB075: PASS; #79 docs-only readiness artifact merged as `816f946c...`, parents `957f9777...` + `a3c4d56e...`; no global 25.2 closure claim.
- AAA076: no final result/handoff before CYCLE 081; superseded due material integration move, not PASS. AAA071 remains reusable input.
- WOZ079: no final result/handoff before CYCLE 081; superseded due material integration move, not PASS.
- #83 is now stale-base: OPEN/DRAFT, head `52b58f56...`, old base `957f9777...`; must reconcile and re-run exact-head CI before any integration claim.

## Serialización de integración

Only one integration mutation authorized in CYCLE 081: **WOZ/#83**. AAA and BBB may create/update bounded candidates but MUST NOT merge integration. Any integration race invalidates stale exact-head evidence and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime.
- F2/13.1 #69/#70 frozen; F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails; F3/19.x #76 stale/frozen.
- F3/20.2 runtime 160 still independently required even if #83 integrates.
- F4/25.1 windows/auth current evidence BBB076; #72 stale/frozen.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 081

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA076: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA077: ASSIGNED F2/13.2 executable evidence/fix
AAA077 FALLBACK: NONE
BBB075: PASS -> #79 MERGED 816f946c...
BBB076: ASSIGNED F4/25.1 windows/auth current evidence
BBB076 FALLBACK: NONE
WOZ079: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ080: ASSIGNED F3/20.2 #83 reconcile/readiness/integration
WOZ080 FALLBACK: #78 runtime 160 READ_ONLY only during genuine external wait
ONLY_INTEGRATION_MUTATION: WOZ/#83
RELEASE: NO-GO
F5: CLOSED
```
