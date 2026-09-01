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

## Estado vivo — NIGHT-JOBS-139

- **Release público:** 🔴 `NO-GO`.
- **Integración estable, incluido race-check final:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`; #95 continúa como último merge material verificable.
- **F2/12.1:** #92/#94/#95 integrados. PR #96 `F2/12.1: continue bound Web MTProto session state` apareció después de CYCLE138, OPEN/Ready sobre base exacta `43fdf70e...`, head estable en race-check final `7e7bd5449361b2031c29271e8875de7683ed5af4`. Durante el preflight inicial todavía no había check-runs; en el race-check final ya existen **14 check-runs** sobre ese exact head y `Test - Desktop Portability` run `33538653800` sigue **in_progress**. Por tanto #96 = `WAITING_CI / ACTIVE_EXTERNAL_CANDIDATE / NOT_PASS`; no hay autorización nocturna de mutation/merge. Incluso si CI queda verde y luego se integra por un owner válido, sigue faltando public runtime proof del exact deployment resultante.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
- **F2/15.1:** recent-reauth product seam sigue prerequisito; owner `NIGHT-BBB-134` solo para seam mínima, no Trash UI todavía.
- **F0/0.9:** #89 OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; stale frente a live. F0 audit run `33454881387` reconsultado = `completed/failure` sobre ese exact head. Owner `NIGHT-WOZ-138` para diagnóstico bounded + refresh/revalidation + conditional expected-head merge de #89 solamente.
- **F4/Windows Auth:** #93 OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293985c314eb09c238115e3bcb71e79f1810`; stale. No mutation owner CYCLE139.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7 owner `NIGHT-AAA-135` READ-ONLY; 1.8/1.9 pendientes.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita de aplicabilidad al alpha.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE139

- `NIGHT-AAA-134`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-133`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-137`: sin matching RESULTADO DEL TURNO/handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- GitHub vivo sí cambió después de CYCLE138: apareció PR #96 en F2/12.1. Su existencia invalida el claim anterior de “sin candidate nuevo”, pero no satisface ningún gate. El race-check final lo deja con exact-head CI en progreso, no verde/mergeado/runtime-proven.
- #89 conserva gate rojo exacto; old-head-green no cuenta. #93 conserva evidencia histórica old-base únicamente.
- JOBS no modificó código BeatGaler ni infraestructura.

## OWNERS — CYCLE139

### AAA — `NIGHT-AAA-135` — F1 / 1.7
PRIMARY: blocker classification READ-ONLY para alpha 3–5 cuentas; clasificar evidencia como `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL`, incorporando #96 como `WAITING_CI` sin adjudicarse ese PR, el F0/0.9 failure vivo de #89 y el resto de blockers materiales. Sin decisión RO ni promoción de gates.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-134` — F1/D8 follow-up seam
PRIMARY: REUSE/expose minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; focused tests; bounded candidate. **No Trash UI/purge. NO MERGE. No tocar #96/#89/#93.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-138` — F0 / 0.9 / #89
PRIMARY: REUSE #89; diagnose run `33454881387`, duplicate-check, history-preserving bounded refresh onto live baseline, exact-head F0/0.9 + applicable CI; if exact/green/race-free, expected-head merge **#89 only** and verify SHA/parents. El fallo actual no puede omitirse ni rebajarse.  
CI-FALLBACK: mientras PRIMARY esté genuinamente `WAITING_CI/WAITING_EXTERNAL` después de un clean refresh, hacer inventario **READ-ONLY de PR #96**: base/head/changed-files/actividad/CI exact-head y si ya existe handoff estable. No mutar, no rerun, no merge, no promover 12.1; si el head cambia durante la inspección, marcar `UNSTABLE_ACTIVE_EXTERNAL` y STOP fallback. Volver a #89 en cuanto PRIMARY deje de esperar.

**Integration mutation authorization CYCLE139: WOZ138 / PR #89 ONLY, after exact refreshed base/head + applicable CI SUCCESS + race-free expected-head. Ni #96 ni #93 tienen autorización de integración nocturna.**

## Camino crítico global — recalculado desde cero contra GitHub vivo

1. **F2/12.1 / PR #96 + runtime:** #96 está en `WAITING_CI` sobre exact head `7e7bd544...`; requiere conclusión exact-head + handoff/ownership válido antes de cualquier integración. Incluso integrado, 12.1 seguirá necesitando public runtime proof del exact deployment resultante.
2. **F0/0.9 / #89:** P1 software conocido; current security gate rojo + base stale. Diagnóstico, refresh y exact-head green son obligatorios antes de integración.
3. **F1/1.7:** clasificación factual necesaria antes de una decisión RO real 1.8; debe incorporar #96 como candidate, no como PASS.
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

AAA ejecuta `NIGHT-AAA-135`; BBB `NIGHT-BBB-134`; WOZ `NIGHT-WOZ-138` y posee la única conditional integration lane sobre #89. PR #96 queda `WAITING_CI / ACTIVE_EXTERNAL_CANDIDATE / NO NIGHT MUTATION OWNER`; WOZ solo puede inspeccionarlo READ-ONLY bajo su fallback. F2/13.2 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED`. #93 no tiene mutation owner. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE139 final race-check; GitHub live prevalece si cambia después.
