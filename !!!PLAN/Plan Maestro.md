# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## Reglas de autoridad

- GitHub/runtime vivo prevalece sobre snapshots viejos.
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Cada pieza material tiene un solo owner.
- JOBS dirige/sincroniza; no modifica código BeatGaler ni infraestructura.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-157

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.
- **PR #99:** `MERGED`; mecanismo fail-closed Web source/runtime binding integrado. F2/12.1 sigue `NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN` porque no existe evidencia literal nueva de clean deployment desde canonical integration HEAD con public marker igual al exact SHA.
- **Issue #97 / PR #100:** #97 sigue OPEN / pre-Beta blocker. Durante CYCLE157 apareció #100 `F2/97: instrument startup and library reveal surfaces`, OPEN/Ready, exact base `c2766fb...`, head `5f0a0727edacbcb404eb4e31571468262744ec95`. Es instrumentation-only: mide startup surfaces/card counts y no cambia performance/startup behavior. CI está en curso; WOZ156 debe REUSE #100, obtener Web+Desktop measurements y convertir esa misma lineage en la correction mínima antes de cualquier merge de cierre.
- **F0/0.9:** PR #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`, stale; dedicated F0/0.9 gate sigue FAILURE. AAA153 posee REUSE/refresh/revalidate e integración condicional.
- **F2/15.1:** bloqueada por seam productiva recent-reauth; BBB152 posee únicamente esa seam mínima, candidate-only, NO MERGE/no Trash.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED` mientras #97/#100 ocupa startup/App surfaces.
- **F4/25.1:** PR #93 sigue OPEN/stale @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`; sin mutation owner; refresh solo si 1.7 lo mantiene `IN_ALPHA`.
- **F1:** D6–D10.1 PASS; D10.2 `MAP COMPLETE / ALPHA CANDIDATE NOT READY`; 1.7 espera facts frescos de 12.1/#97/#89/recent-reauth.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita 1.7→1.8.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global abierto; signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE157

- `NIGHT-AAA-152`: sin RESULTADO DEL TURNO y sin matching worker handoff antes del nuevo ciclo; GitHub #89 no cambió → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-151`: sin RESULTADO DEL TURNO y sin matching worker handoff; no apareció recent-reauth candidate → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-155`: sin resultado terminal, pero GitHub produjo PR #100 durante el preflight → `ACTIVE_PROGRESS / SUPERSEDED_BY_WOZ156 / NOT_PASS`. #100 no cierra #97 porque es observational instrumentation only.
- No se promueve DONE/PASS/integration sin evidencia.

## OWNERS — CYCLE157

### AAA — `NIGHT-AAA-153` — F0/0.9 / PR #89
PRIMARY: REUSE #89; history-preserving refresh sobre live baseline; mínimo gate-precondition correction; exact-head F0/0.9 revalidation; conditional expected-head merge solo si exact/green/race-free.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-152` — recent-reauth seam
PRIMARY: REUSE D8/#53; mínima seam productiva same-provider bound to user/session, fail-closed, focused tests; candidate-only; **NO MERGE / no Trash / no #97/#100/#89**.  
CI-FALLBACK: F3/18.2 READ-ONLY inventory solo durante genuine external wait después de candidate limpio; no provider/payment mutation ni decisión RO.

### WOZ — `NIGHT-WOZ-156` — Issue #97 / PR #100
PRIMARY: REUSE #100; finish instrumentation CI, collect Web+Desktop startup traces/measurements, isolate causal bottleneck, amend/reconstruct same lineage with minimum shared correction, exact-head CI; conditional expected-head merge #100 only after it contains actual bounded correction + literal applicable evidence. Instrumentation-only is not merge-as-closure.  
CI-FALLBACK: NONE.

**Integration mutations autorizadas CYCLE157: AAA153 / #89 y WOZ156 / #100, cada una solo dentro de scope disjunto y condicionada a exact applicable CI SUCCESS + no required review blocker + race-free expected-head. BBB152 NO MERGE. #93 no tiene mutation/merge authorization. Si un merge mueve integración, el otro owner debe refresh/revalidar antes de integrar.**

## Camino crítico global — recalculado desde cero

1. **F2/12.1:** clean canonical production deployment/source proof del live integration SHA; blocker factual externo/SHA-dependent.
2. **Issue #97 / #100:** Web+Desktop factual measurements → minimum shared correction → exact evidence/integration.
3. **F0/0.9 / #89:** P1 DNS-rebinding corrective; refresh + exact-green + integration.
4. **F1/D8→F2/15.1:** productive recent-reauth seam, luego Trash strong confirmation + durable deterministic purge/no-false-success.
5. **F2/13.2:** durable Review write-surface gap cuando #97 libere superficies compartidas.
6. **F1/1.7→1.8:** clasificación factual de remaining alpha blockers y decisión RO.
7. **F4/25.1 / #93:** refresh/revalidate solo si 1.7 lo mantiene IN_ALPHA.
8. **Parallel external/release tails:** F0 1.2/2.2, production signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya payloads.
- Permanent auth/control secrets control-side; clients use temporary auth.
- Shared-bot fallback only when no bot free; normal exclusivity per vault.
- v1 no free-only; eligibility v1 = **18+**.
- YouTube Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-153`; BBB `NIGHT-BBB-152`; WOZ `NIGHT-WOZ-156`. F2/12.1 espera evidencia productiva exacta; #93 queda sin owner; F2/13.2 sigue `BLOCKED_WRITE_SURFACE / UNASSIGNED`. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH: synced CYCLE157`; GitHub/runtime live prevalece si cambia después.
