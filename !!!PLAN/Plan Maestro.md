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

## Estado vivo — NIGHT-JOBS-154

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.
- **PR #98:** `MERGED`. Candidate exact head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`; Required CI run `33575511576` / check `100081022125` = SUCCESS; merge avanzó integración desde `aa445095...` a `c4e203cf...`. Resultado procesado: `PR98_PRODUCTION_WEB_MTProto_CLEANUP_INTEGRATED`.
- **F2/12.1:** sigue `NOT_PASS / RUNTIME_SOURCE_BINDING_OPEN`. PR #98 reporta production health/library/artwork/playback exitosos, pero JOBS no convierte behavior reportado en exact deployment proof sin identidad inmutable. AAA150 posee close review READ-ONLY.
- **Issue #97:** OPEN, explícitamente `Must be addressed before Beta 1`; #98 ya liberó App/startup surfaces. WOZ153 posee exclusivamente implementación/integración de #97 con Web+Desktop evidence.
- **F2/15.1:** bloqueada por seam productiva recent-reauth; BBB149 posee únicamente esa seam mínima, candidate-only, no Trash todavía.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED`. No owner concurrente mientras #97 pueda tocar App/startup.
- **F0/0.9:** PR #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, base `816f946c...` stale; run `33454881387` = FAILURE. Sin mutation owner CYCLE154; WOZ153 puede inventariarlo READ-ONLY solo durante espera externa real de #97.
- **F4/25.1:** PR #93 sigue stale @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`; sin mutation owner; refresh solo si 1.7 lo mantiene `IN_ALPHA`.
- **F1:** D6–D10.1 PASS; D10.2 `MAP COMPLETE / ALPHA CANDIDATE NOT READY`; 1.7 espera facts frescos de 12.1/#97/#89/recent-reauth.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita 1.7→1.8.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global abierto; signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE154

- `NIGHT-AAA-149`: sin matching worker RESULTADO/handoff posterior a CYCLE153 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-148`: sin matching worker RESULTADO/handoff posterior a CYCLE153 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-152`: no escribió RESULTADO final verificable, pero GitHub independientemente prueba que su único objetivo de integración autorizado se completó: #98 MERGED + Required CI exact-head SUCCESS + integration head `c4e203cf...`. Se procesa **solo** ese outcome como `DONE / INTEGRATED`; no se infiere F2/12.1 PASS.

## OWNERS — CYCLE154

### AAA — `NIGHT-AAA-150` — F2/12.1 close review
PRIMARY: READ-ONLY exact public runtime/deployment-source evidence post-#98; clasificar checklist literal y reducir a `READY_FOR_JOBS_CLOSE_REVIEW` o mínimo `UNVERIFIED`.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-149` — recent-reauth seam
PRIMARY: REUSE D8/#53; mínima seam productiva same-provider bound to user/session, fail-closed, focused tests; candidate-only; **NO MERGE / no Trash / no #97**.  
CI-FALLBACK: F3/18.2 READ-ONLY inventory solo durante genuine external wait después de candidate limpio; no provider/payment mutation ni decisión RO.

### WOZ — `NIGHT-WOZ-153` — Issue #97
PRIMARY: exclusive owner del pre-Beta startup/reveal performance slice; medir causal path, correction cross-platform mínima, Web+Desktop evidence, conditional expected-head merge del candidate #97 only si exact/green/race-free.  
CI-FALLBACK: #89 estrictamente READ-ONLY refresh-readiness solo mientras #97 espera external CI/review/build; STOP ante overlap/mutation/head movement.

**Única integration mutation autorizada CYCLE154: WOZ153 / candidate de Issue #97, condicionada a scope exacto + applicable CI SUCCESS + no required review blocker + race-free expected-head. #89/#93 no tienen mutation/merge authorization.**

## Camino crítico global — recalculado desde cero

1. **F2/12.1:** exact runtime/deployment-source close review post-#98.
2. **Issue #97:** pre-Beta near-instant startup/reveal Web+Desktop; ahora executable porque #98 está integrado.
3. **F0/0.9 / #89:** P1 DNS-rebinding corrective; refresh + exact-green + integration bajo owner explícito futuro.
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

AAA ejecuta `NIGHT-AAA-150`; BBB `NIGHT-BBB-149`; WOZ `NIGHT-WOZ-153`. #97 es la única integration lane. #89/#93 no tienen mutation owner. F2/13.2 sigue `BLOCKED_WRITE_SURFACE / UNASSIGNED`. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH: synced CYCLE154`; GitHub/runtime live prevalece si cambia después.
