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

## Estado vivo — NIGHT-JOBS-156

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.
- **PR #99:** `MERGED`. Exact candidate head `6e253c815515624dcfc70cb5d447befa38f19566`; merge/current integration `c2766fb...`. Exact-head Required CI `33578074388` = SUCCESS. Integra fail-closed Web deployment provenance: package/source SHA, `.well-known/source-sha.txt`, expected-SHA activation/readback y `WEB_RUNTIME_SOURCE_PROOF_OK`.
- **F2/12.1:** `NOT_PASS / CLEAN_CANONICAL_PRODUCTION_DEPLOYMENT_PROOF_OPEN`. #99 aporta el mecanismo, pero falta una clean production deployment desde canonical integration HEAD y public marker igual al exact integrated SHA. CYCLE156 no pudo observar esa evidencia runtime literal; DNS externo tampoco fue verificable desde la superficie JOBS.
- **Issue #97:** OPEN, cero comments, `Must be addressed before Beta 1`; WOZ155 posee exclusivamente implementación/integración Web+Desktop.
- **F0/0.9:** PR #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c...`, stale; run `33454881387` = FAILURE sobre ese exact head. AAA152 posee REUSE/refresh/revalidate e integración condicional.
- **F2/15.1:** bloqueada por seam productiva recent-reauth; BBB151 posee únicamente esa seam mínima, candidate-only, NO MERGE/no Trash.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED` mientras #97 ocupa startup/App surfaces.
- **F4/25.1:** PR #93 sigue OPEN/stale @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base histórica `134a293...`; sin mutation owner; refresh solo si 1.7 lo mantiene `IN_ALPHA`.
- **F1:** D6–D10.1 PASS; D10.2 `MAP COMPLETE / ALPHA CANDIDATE NOT READY`; 1.7 espera facts frescos de 12.1/#97/#89/recent-reauth.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita 1.7→1.8.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global abierto; signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE156

- `NIGHT-AAA-151`: sin RESULTADO DEL TURNO en su ledger y sin matching worker handoff en Issue #41 antes de CYCLE156 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-150`: sin RESULTADO DEL TURNO en su ledger y sin matching worker handoff en Issue #41 antes de CYCLE156 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-154`: sin RESULTADO DEL TURNO en su ledger y sin matching worker handoff en Issue #41 antes de CYCLE156 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- GitHub no muestra PR/candidate nuevo posterior a #99 para #97 o recent-reauth; #89 conserva el mismo stale/red head. No se promueve DONE/PASS por ausencia de evidencia.

## OWNERS — CYCLE156

### AAA — `NIGHT-AAA-152` — F0/0.9 / PR #89
PRIMARY: REUSE #89; history-preserving refresh sobre live baseline; resolver únicamente el gate precondition conocido o probar que refresh ya lo cubre; exact-head security CI; conditional expected-head merge solo si exact/green/race-free.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-151` — recent-reauth seam
PRIMARY: REUSE D8/#53; mínima seam productiva same-provider bound to user/session, fail-closed, focused tests; candidate-only; **NO MERGE / no Trash / no #97/#89**.  
CI-FALLBACK: F3/18.2 READ-ONLY inventory solo durante genuine external wait después de candidate limpio; no provider/payment mutation ni decisión RO.

### WOZ — `NIGHT-WOZ-155` — Issue #97
PRIMARY: exclusive owner del pre-Beta startup/reveal performance slice; medir causal path, correction cross-platform mínima, Web+Desktop evidence, conditional expected-head merge del candidate #97 only si exact/green/race-free.  
CI-FALLBACK: NONE.

**Integration mutations autorizadas CYCLE156: AAA152 / PR #89 y WOZ155 / candidate de Issue #97, cada una solo dentro de su scope disjunto y condicionada a exact applicable CI SUCCESS + no required review blocker + race-free expected-head. BBB151 NO MERGE. #93 no tiene mutation/merge authorization. Si un merge mueve integración, el otro owner debe refresh/revalidar antes de integrar.**

## Camino crítico global — recalculado desde cero

1. **F2/12.1:** clean canonical production deployment/source proof de `c2766fb...` o de un SHA canónico posterior; es blocker factual externo/SHA-dependent y no se duplica como worker fallback.
2. **Issue #97:** pre-Beta near-instant startup/reveal Web+Desktop.
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

AAA ejecuta `NIGHT-AAA-152`; BBB `NIGHT-BBB-151`; WOZ `NIGHT-WOZ-155`. F2/12.1 espera evidencia productiva exacta posterior a #99; #93 queda sin owner. F2/13.2 sigue `BLOCKED_WRITE_SURFACE / UNASSIGNED`. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH: synced CYCLE156`; GitHub/runtime live prevalece si cambia después.
