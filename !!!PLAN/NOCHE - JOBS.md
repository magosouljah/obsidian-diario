# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 089`.

## BASELINE VIVO

- Final preflight baseline: `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- PR #79 remains latest material integration merge; docs-only F4/25.2 readiness artifact.
- PR #83 remains `OPEN/DRAFT`, mergeable, exact base `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`, exact 3-file durable-waitlist scope.
- Exact-head #83 evidence retained from live verified state: F3 20.2 Durable Waitlist `33388377959` SUCCESS; Test - Desktop Portability `33388377963` SUCCESS; D6 `33388377952` SUCCESS; D7 `33388377964` SUCCESS.
- Current connector surface exposes a dedicated authorized Draft→Ready action; WOZ088 owns the only authorized transaction.
- PR #74 remains OPEN/Ready/mergeable product corrective lineage at `b3468003a80288109e2d537a7aa3f25a7269927c`, exact base `816f946c...`.
- PR #84 remains OPEN/Ready/mergeable sole exact-lineage Windows-auth evidence candidate at `d13a1969aef1ca53ee7fbed0bcba241ceb766d42`, exact base `816f946c...`.
- #84 Required CI `33407580663` = SUCCESS; literal Windows auth run `33407580887` / job `99538870371` = FAILURE at `Run isolated Windows auth assertions`.
- Issue #41 remained open; no material handoff for AAA084/BBB083/WOZ087 appeared by CYCLE 089 preflight.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Read complete for this cycle: Plan Maestro; F0–F4; Equipo; night protocol; JOBS/AAA/BBB/WOZ; Registro ledger surface; Issue #41 full connector comment surface; live integration branch; exact #83/#84/#74 PR state and duplicate checks. GitHub/runtime prevails over stale plan text.

- `NIGHT-AAA-084`: no final RESULTADO DEL TURNO nor matching material Issue #41 handoff observed. No newer open AAA 13.2 candidate observed. Processed `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-083`: no final RESULTADO DEL TURNO nor material Issue #41 handoff observed. #84 remains unchanged at `d13a1969...`; literal auth journey remains red. Processed `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-087`: no final RESULTADO DEL TURNO nor matching material Issue #41 handoff observed. #83 remains OPEN/DRAFT/unmerged at exact head/base. Processed `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Duplicate-check: #84 remains sole BBB evidence candidate; no AAA 13.2 candidate found; #83 remains unique durable-waitlist candidate; #81/#76/#72 remain frozen; #69 helper semantics reusable only inside AAA scope.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 089

1. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
2. F4/25.1 #84 exact Windows auth failure attribution and bounded correction/evidence.
3. F3/20.2 #83 direct Draft→Ready→exact-head merge transaction.
4. F3/20.2 post-#83 materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
5. F2/12.1 real-browser cold/warm evidence.
6. F3/19.1 external canonical hostname/API/DNS/TLS/status/OAuth/sender/deployment facts/actions.
7. Frozen stale candidates (#81/#76/#72) only after safe explicit reconciliation.
8. F4 signing/notarization/hardware/tester execution plus F0/F1 external/RO tails remain real blockers.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-085` — F2/13.2 minimum Review Save/Save All durable action-boundary corrective; saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE | F2/12.1 READ-ONLY real-browser cold/warm evidence only while PRIMARY genuinely waits external CI; no code changes; STOP on synthetic/non-attributable evidence, required code change, integration movement without attribution or PRIMARY leaving wait |
| BBB | `NIGHT-BBB-084` — reuse #84; diagnose/correct exact auth assertion failure only if harness/workflow attributable; product #74 finding => STOP/report; fresh exact-head literal Windows auth required; NO MERGE | `NONE` |
| WOZ | `NIGHT-WOZ-088` — recheck exact #83 base/head/scope/CI; use dedicated Draft→Ready action; re-read; if unchanged and green, merge with exact expected head; verify final integration SHA; STOP. Runtime 160 remains open | `NONE` |

Ownership is distinct. **Only WOZ088 may mutate integration in CYCLE 089, and only for #83 under exact/race-free conditions.**

## PROGRESO F0–F4 / BLOCKERS

- **F0:** technical core closed; 1.2/2.2 external/admin tails remain.
- **F1:** D6–D9 PASS; D10.1 real off-provider/off-account proof pending; D10.2 RO decision.
- **F2:** 11.1/11.2/12.2 closed; 12.1 browser runtime open; 13.1 frozen; 13.2 durable action-boundary gap under AAA085; 14.1 #81 parked; later UX/a11y/YouTube work remains.
- **F3:** 17.1/17.2/18.1 closed; 18.2 global open; 19.1 external/provider facts only; 20.1 software integrated; #83 exact/green/draft under WOZ088 transaction; runtime 160 still independently required after integration.
- **F4:** 21.1/21.2/24.1/24.2 closed; #79 readiness artifact integrated; 25.1 remains open because literal exact-lineage Windows auth currently fails on #84; signing/notarization/hardware/tester evidence external.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC / NEXT

CYCLE 089 assignments are written in `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - WOZ.md`. Plan Maestro, roles, F2, F3 and F4 are synchronized to the same baseline/results/ownership. F0/F1 semantics unchanged. No new BeatGaler merge/PASS occurred during JOBS execution, so Registro de avances receives no ceremonial entry. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS changed no BeatGaler code or infrastructure.

Next cycle: start from live integration and exact worker handoffs. If WOZ088 merges #83, verify resulting integration SHA before assigning runtime-160 work. Do not promote #84 unless literal Windows auth passes on exact current candidate. F3/19.1 should not receive another read-only discovery turn until canonical provider/domain facts exist.

```text
CYCLE_ID: NIGHT-JOBS-089
INTEGRATION_HEAD_FINAL_PREFLIGHT: 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA_RESULT_PROCESSED: NIGHT-AAA-084 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-083 NO_RESULT / SUPERSEDED / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-087 NO_RESULT / SUPERSEDED / NOT_PASS
AAA_NEW: NIGHT-AAA-085
BBB_NEW: NIGHT-BBB-084
WOZ_NEW: NIGHT-WOZ-088
ONLY_INTEGRATION_MUTATION_AUTHORIZED: WOZ088 PR #83 exact-head transaction
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 089 terminado.
