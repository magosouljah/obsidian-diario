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

## Estado vivo — NIGHT-JOBS-130

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- **Últimos merges materiales procesados:** #92 → `ada77811059a3319b271dcc98dd5d95efe807dec`; #94 → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`; #95 → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- **F2/12.1:** #92/#94/#95 integrados; sigue `NOT_PASS` hasta public runtime proof exacto post-#95.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
- **F2/15.1:** recent-reauth product seam sigue prerequisito; owner `NIGHT-BBB-125` solo para seam mínima, no Trash UI todavía.
- **F0/0.9:** #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, `mergeable=true`; stale frente a live. F0 audit run `33454881387` = **FAILURE** sobre ese exact head: Rust unit contracts fallaron porque Tauri `frontendDist=../dist` no existía. El head actual NO está verde. Owner `NIGHT-WOZ-129` para diagnóstico bounded + refresh/revalidation + conditional expected-head merge de #89 solamente.
- **F4/Windows Auth:** #93 OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...`, `mergeable=true`; stale. No mutation owner CYCLE130.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7 owner `NIGHT-AAA-126` READ-ONLY; 1.8/1.9 pendientes.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita de aplicabilidad al alpha.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE130

- `NIGHT-AAA-125`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-124`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-128`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Issue #41 completo y GitHub vivo reconciliados; no apareció candidate nuevo matching ni merge posterior a #95.
- #89 conserva gate rojo exacto; old-head-green no cuenta. #93 conserva evidencia histórica old-base únicamente.
- JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE130

### AAA — `NIGHT-AAA-126` — F1 / 1.7
PRIMARY: blocker classification READ-ONLY para alpha 3–5 cuentas; clasificar evidencia como `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL`, incluyendo el F0/0.9 failure vivo de #89, sin decisión RO ni promoción de gates.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-125` — F1/D8 follow-up seam
PRIMARY: expose/reuse minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; focused tests; bounded candidate. **No Trash UI/purge. NO MERGE.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-129` — F0 / 0.9 / #89
PRIMARY: REUSE #89; diagnose run `33454881387`, duplicate-check, history-preserving bounded refresh onto live baseline, exact-head F0/0.9 + applicable CI; if exact/green/race-free, expected-head merge **#89 only** and verify SHA/parents. El fallo actual no puede omitirse ni rebajarse.  
CI-FALLBACK: while PRIMARY genuinely waits CI/external after a clean refresh only, READ-ONLY #93 applicability/evidence inventory; no mutation, CI rerun, new PR or gate promotion; STOP immediately when PRIMARY ceases waiting and return to #89.

**Integration mutation authorization CYCLE130: WOZ129 / PR #89 ONLY, after exact refreshed base/head + applicable CI SUCCESS + race-free expected-head. El head actual `daf87da6...` NO es elegible por stale base + F0 audit FAILURE.**

## Camino crítico global — recalculado desde cero contra GitHub vivo

1. **F2/12.1 runtime post-#95:** mayor gap factual de cierre; falta deployment/runtime público verificable. No se asigna a un worker sin acceso runtime aplicable.
2. **F0/0.9 / #89:** P1 software conocido; current security gate rojo + base stale. Diagnóstico, refresh y exact-head green son obligatorios antes de integración.
3. **F1/1.7:** clasificación factual necesaria antes de una decisión RO real 1.8.
4. **F1/D8→F2/15.1:** exponer seam recent-reauth bounded; luego strong confirmation + durable Trash purge/no-false-success.
5. **F2/13.2:** hard product gap, pero sigue bloqueado por write surface unsafe; no se fabrica owner inútil.
6. **F4/25.1 / #93:** future refresh/revalidation solo si 1.7 lo mantiene dentro del alpha; ahora mutation-unassigned.
7. **Release path paralelo:** F0 1.2/2.2, productive signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no bot free; normal exclusivity per vault.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-126`; BBB `NIGHT-BBB-125`; WOZ `NIGHT-WOZ-129` y posee la única conditional integration lane sobre #89, actualmente bloqueada hasta resolver/revalidar el F0 audit failure. F2/13.2 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED`. #93 no tiene mutation owner; solo puede ser inspeccionado READ-ONLY bajo el fallback de WOZ129 mientras #89 espera CI. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE130; GitHub live prevalece si cambia después.
