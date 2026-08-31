# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 087`.

## BASELINE VIVO

- Final preflight baseline: `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- PR #79 remains latest material integration merge; docs-only F4/25.2 readiness artifact.
- PR #83 remains `OPEN/DRAFT`, mergeable, exact base `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`, exact 3-file durable-waitlist scope; dedicated/applicable exact-head CI remains green. No merge claim.
- PR #74 remains product corrective lineage at `b3468003a80288109e2d537a7aa3f25a7269927c`, exact base `816f946c...`.
- PR #84 is the sole current exact-lineage Windows-auth evidence candidate at `d13a1969aef1ca53ee7fbed0bcba241ceb766d42`, OPEN/Ready, exact base `816f946c...`.
- Exact-head #84 live CI: Required/Desktop Portability run `33407580663` SUCCESS; D6 `33407580862` SUCCESS; D7 `33407580492` SUCCESS; Web Production Build `33407581045` SUCCESS; Windows Import `33407581182` SUCCESS; **F4 - 25.1 Windows Auth Journey `33407580887` / job `99538870371` FAILURE** at `Run isolated Windows auth assertions`.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Read complete for this cycle: Plan Maestro; F0–F4; Equipo; night protocol; JOBS/AAA/BBB/WOZ; Registro ledger surface; Issue #41 complete connector comment surface; live integration, open PRs and exact-head workflow state. GitHub/runtime prevails over stale plan text.

- `NIGHT-AAA-082`: no final RESULTADO DEL TURNO nor matching material Issue #41 handoff observed; no newer open AAA 13.2 candidate observed. `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-081`: worker closed `WAITING_CI` after creating exact-lineage #84. GitHub subsequently resolved the literal auth journey to FAILURE at exact head `d13a1969...`. Processed as `NOT_PASS / CI_FAILURE`; broad green CI does not override the literal failing gate.
- `NIGHT-WOZ-085`: `BLOCKED_STOP`. #83 exact base/head/scope and exact-head CI stayed valid; authorized Ready-for-review connector action failed with GraphQL schema error `Repository.fullDatabaseId`. No workaround, no merge, no integration mutation.
- Duplicate-check: #84 reused for BBB; no new AAA Review candidate; #83 remains unique durable-waitlist candidate; #81/#76/#72 remain stale/frozen; #69/#70 helper/server slices are reuse inputs only where explicitly permitted.
- Two concurrent shared-plan writes were detected by GitHub 409 exact-SHA protection during this JOBS run. Each stale write was abandoned and the live file re-read; no valid concurrent update was overwritten. The already-issued CYCLE 087 assignments were adopted exactly rather than duplicated.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 087

1. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
2. F4/25.1 #84 exact Windows auth failure attribution and bounded correction/evidence.
3. #83 process blocker: candidate is technically exact/green but Draft→Ready cannot proceed through the currently authorized connector action; preserve, do not repeat ceremonial attempts.
4. F3/19.1 real production/public-surface evidence and blocker reduction in parallel.
5. F3/20.2 post-#83 materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
6. F2/12.1 real-browser cold/warm evidence.
7. Frozen stale candidates (#81/#76/#72) only after safe explicit reconciliation.
8. F4 signing/notarization/hardware/tester execution plus F0/F1 external/RO tails remain real blockers.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-083` — F2/13.2 minimum Review Save/Save All durable action-boundary corrective; saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE | F2/12.1 READ-ONLY real-browser cold/warm evidence only while PRIMARY genuinely waits external CI; no code changes; STOP on synthetic/non-attributable evidence, required code change, integration movement without attribution or PRIMARY leaving wait |
| BBB | `NIGHT-BBB-082` — reuse #84; diagnose exact auth-assertion failure. Harness/workflow-only correction allowed iff attributable; if #74 product corrective is implicated, STOP and report exact product finding; fresh exact-head literal Windows auth required; NO MERGE | `NONE` |
| WOZ | `NIGHT-WOZ-086` — F3/19.1 READ-ONLY production/public surface evidence: domain/API/status/support/security-abuse/sender surfaces, DNS/TLS/redirects/OAuth callback destinations and deployment identity only where factually observable; VERIFIED vs MISSING blocker map; no infra/code/#76 mutation | `NONE` |

Ownership is distinct. **No integration mutation is authorized in CYCLE 087.**

## PROGRESO F0–F4 / BLOCKERS

- **F0:** technical core closed; 1.2/2.2 external/admin tails remain.
- **F1:** D6–D9 PASS; D10.1 real off-provider/off-account proof pending; D10.2 RO decision.
- **F2:** 11.1/11.2/12.2 closed; 12.1 browser runtime open; 13.1 frozen; 13.2 proven durable action-boundary gap under AAA083; 14.1 #81 parked; later UX/a11y/YouTube work remains.
- **F3:** 17.1/17.2/18.1 closed; 18.2 global open; F3/19.1 evidence reconciliation under WOZ086; 20.1 software integrated; #83 exact/green but process-blocked; runtime 160 still independently required after integration.
- **F4:** 21.1/21.2/24.1/24.2 closed; #79 readiness artifact integrated; 25.1 remains open because literal exact-lineage Windows auth currently fails on #84; signing/notarization/hardware/tester evidence external.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC / NEXT

CYCLE 087 live assignments are written in `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - WOZ.md`; `Plan Maestro.md` and roles are synchronized to the same baseline/results/ownership. F0–F4 gate semantics were not downgraded; no new BeatGaler merge/PASS occurred, so `Registro de avances.md` receives no ceremonial entry. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS changed no BeatGaler code or infrastructure.

Next cycle: start from live integration and exact worker handoffs. Do not promote #84 unless its literal Windows auth journey passes at the exact current head. Do not reassign #83 merge until Ready-for-review tooling/verified owner flow actually exists. If AAA fallback touches F2/12.1, require explicit genuine WAITING_CI first.

```text
CYCLE_ID: NIGHT-JOBS-087
INTEGRATION_HEAD_FINAL_PREFLIGHT: 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA_RESULT_PROCESSED: NIGHT-AAA-082 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-081 WAITING_CI -> exact Windows auth FAILURE / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-085 BLOCKED_STOP / #83 process blocker / NO_MERGE
AAA_NEW: NIGHT-AAA-083
BBB_NEW: NIGHT-BBB-082
WOZ_NEW: NIGHT-WOZ-086
ONLY_INTEGRATION_MUTATION_AUTHORIZED: NONE
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 087 terminado.
