# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` are shared memory. Fixed-owner puzzle; GitHub/runtime live prevails.

## Roles y ownership actual — CYCLE 082

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-078`: minimum Review Save/Save All durable action-boundary corrective slice + executable no-silent-loss/Tauri call-spy; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-077`: REUSE #71/#74, safe refresh + current Windows auth journey/fresh CI; NO MERGE | NONE |
| WOZ | F3 / 20.2 / #83 | `NIGHT-WOZ-081`: exact-head green #83 Draft→Ready + expected-head merge if exact/race-free | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados

- WOZ080: WAITING_CI at close after bounded history-preserving #83 reconciliation. Post-turn dedicated waitlist run `33388377959` and Required CI on `803b2143...` are SUCCESS; PR still Draft/unmerged.
- AAA077: no final result before CYCLE 082; not PASS. Late Issue #41 `5478129410` belongs to AAA074, but materially revalidated on live base the Review Save/Save All fire-and-forget gap and is reusable evidence.
- BBB076: no final result before CYCLE 082; not PASS.
- #79 remains latest integration merge `816f946c...`; docs-only readiness artifact, no global 25.2 closure.

## Serialización de integración

Only one integration mutation authorized in CYCLE 082: **WOZ/#83**. AAA and BBB may create/update bounded candidates but MUST NOT merge integration. Any integration race invalidates stale exact-head evidence and triggers STOP/recheck.

## Holding / blocked items

- F0 1.2/2.2 external/administrative.
- F1 D10.1 off-provider/off-account proof; D10.2 RO decision.
- F2/12.1 real-browser cold/warm runtime.
- F2/13.1 #69/#70 frozen except helper-level reuse explicitly allowed by AAA078; F2/14.1 #81 stale/parked.
- F3/18.2 provider/payment tails; F3/19.x #76 stale/frozen.
- F3/20.2 runtime 160 still independently required even if #83 integrates; #78 local/synthetic-only is insufficient.
- F4/25.1 windows/auth current evidence BBB077; #72 stale/frozen.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + applicable exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback or next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 082

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA077: NO_RESULT -> NOT_PASS
AAA074_LATE_HANDOFF: reusable current-baseline finding only
AAA078: ASSIGNED F2/13.2 durable Review Save boundary
AAA078 FALLBACK: NONE
BBB076: NO_RESULT -> NOT_PASS
BBB077: ASSIGNED F4/25.1 windows/auth current evidence
BBB077 FALLBACK: NONE
WOZ080: WAITING_CI -> post-turn exact-head CI SUCCESS, still Draft/unmerged
WOZ081: ASSIGNED F3/20.2 #83 Ready/merge transaction
WOZ081 FALLBACK: NONE
ONLY_INTEGRATION_MUTATION: WOZ/#83
RELEASE: NO-GO
F5: CLOSED
```
