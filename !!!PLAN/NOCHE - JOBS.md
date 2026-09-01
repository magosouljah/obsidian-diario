# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 117`.

## BASELINE VIVO

- Preflight/postcheck GitHub: `integration-v0.8.0-alpha.1 @ 08e5802d27ad81977b1c2f63ceb0fce398d41e42`.
- PR #92 MERGED → `ada77811059a3319b271dcc98dd5d95efe807dec`.
- PR #94 MERGED → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`, parents `ada77811059a3319b271dcc98dd5d95efe807dec + b245aea738ab111992b1efd874ae7db25cd91aac`.
- F2/12.1 remains NOT_PASS: post-#94 public deployment/authenticated worker/library + cold/warm proof is still required.
- PR #93 OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, recorded base `134a293...`, now stale/non-mergeable; PARKED.
- PR #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`; GitHub currently reports `mergeable=true`, but its recorded base is stale versus `08e5802d...`, so exact refresh/revalidation remains mandatory. Owner WOZ116.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos/reconciliados completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 disponible y GitHub vivo. GitHub/runtime real prevalece.

- `NIGHT-AAA-112`: no matching final result/handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-111`: no matching final result/handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Late `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; accepted factual evidence: Trash UI is optimistic, no strong confirmation, and no consumable recent-reauth product seam was found without widening into auth/session core.
- `NIGHT-WOZ-115`: no matching final result/handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- #92/#94 merges are processed as live GitHub facts; #94 is not attributed to WOZ115 without a matching handoff.
- Duplicate-check: no newer durable Review candidate found; no newer recent-reauth seam candidate observed; #89 remains the existing bounded SSRF candidate and is reused rather than duplicated.
- JOBS modified no BeatGaler code or infrastructure.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE117

1. **F2/12.1 public runtime post-#94:** canonical code now exists; closure requires exact deployed build + authenticated worker/library + cold/warm proof, currently owner/runtime dependent.
2. **F0/0.9 / #89:** known software P1 can advance independently via bounded refresh/revalidation/integration.
3. **F2/13.2:** durable Review completion/no-silent-loss.
4. **F1/D8 → F2/15.1:** first expose bounded recent-reauth product seam; then Trash strong confirmation + durable purge/no-false-success.
5. **F4/25.1 / #93:** refresh/revalidate packaged Windows Auth evidence against new baseline after current integration lane.
6. **F1/1.7 → 1.8 → 1.9:** blocker classification, RO alpha decision, then execution.
7. **Release tails:** signing/notarization, F0 1.2/2.2, provider/legal/capacity/tester/hardware remain open.

## TABLERO / ASIGNACIONES EMITIDAS — CYCLE117

| Worker | Resultado procesado | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | `NIGHT-AAA-112 NO_RESULT / SUPERSEDED / NOT_PASS` | `NIGHT-AAA-113` — F2/13.2 durable Review Save/Save All completion/no-silent-loss; candidate only; **NO MERGE** | `NONE` |
| BBB | `NIGHT-BBB-111 NO_RESULT`; late BBB110 blocker accepted | `NIGHT-BBB-112` — expose minimal productive D8 recent-reauth seam bound to user/session; no Trash UI; **NO MERGE** | only during genuine WAITING_CI: F1/1.7 READ-ONLY blocker classification |
| WOZ | `NIGHT-WOZ-115 NO_RESULT / SUPERSEDED / NOT_PASS`; #94 merge treated external factual | `NIGHT-WOZ-116` — REUSE #89; bounded refresh/revalidate; expected-head merge #89 only if exact/green/race-free | only during genuine WAITING_CI: F1/1.7 READ-ONLY blocker classification |

**INTEGRATION_MUTATION CYCLE117: WOZ116 / PR #89 ONLY.**

## CI-FALLBACK CONTRACTS

- AAA113: `CI-FALLBACK: NONE`.
- BBB112: only during genuine PRIMARY `WAITING_CI`; F1/1.7 READ-ONLY blocker matrix with evidence refs. STOP on code/branch/PR/plan/provider mutation, RO decision or end of wait; then recheck PRIMARY.
- WOZ116: only during genuine #89 `WAITING_CI`; F1/1.7 READ-ONLY blocker classification. STOP on any mutation/RO decision or end of wait; then recheck #89 exact state.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** #89 P1 is active owner lane; 1.2/2.2 + productive signing/legal/tester/admin tails keep F0 global open.
- **F1:** D6–D10.1 PASS; D10.2 map complete/NOT_READY. Runtime 12.1, #89, Review, recent-reauth→Trash and Windows Auth canonical refresh block 1.8.
- **F2:** #92 + #94 integrated; 12.1 still NOT_PASS pending runtime proof. 13.2=AAA113. 15.1 blocked behind BBB112 seam.
- **F3:** provider/payment real, legal implementation and runtime160/capacity remain open/external or RO-applicability.
- **F4:** #93 exact-green historical evidence is stale against live baseline; 25.1 global remains open. Production signing/notarization/hardware external.
- **F5:** CLOSED / NO ABRIR.

## NEXT

AAA113 works F2/13.2; BBB112 works only the recent-reauth seam; WOZ116 consumes #89 and is the only integration mutation owner, exclusively under refreshed exact-head/green/race-free conditions. #93 remains parked. Release remains NO-GO and F5 closed.

```text
CYCLE_ID: NIGHT-JOBS-117
INTEGRATION_HEAD_FINAL: 08e5802d27ad81977b1c2f63ceb0fce398d41e42
AAA_RESULT_PROCESSED: NIGHT-AAA-112 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-111 NO_RESULT / SUPERSEDED / NOT_PASS; BBB110 BLOCKED fact accepted
WOZ_RESULT_PROCESSED: NIGHT-WOZ-115 NO_RESULT / SUPERSEDED / NOT_PASS
AAA_NEW: NIGHT-AAA-113 F2_13.2
BBB_NEW: NIGHT-BBB-112 D8_RECENT_REAUTH_SEAM
WOZ_NEW: NIGHT-WOZ-116 F0_0.9_PR89
PR94: MERGED 08e5802d / runtime proof still pending
PR93: OPEN STALE / PARKED
PR89: OPEN STALE_BASE; mergeable=true at final race-check / WOZ116 refresh lane
INTEGRATION_MUTATION_AUTHORIZED: WOZ116 PR89 ONLY IF REFRESHED_EXACT_GREEN_RACE_FREE
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 117 terminado.
