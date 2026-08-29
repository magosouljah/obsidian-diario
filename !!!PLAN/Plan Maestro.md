# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por dependencia real, incluso cross-phase, pero cada agente conserva ownership estable de su pieza hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- GitHub real prevalece sobre snapshots viejos del plan.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- JOBS dirige/sincroniza; no toca código BeatGaler ni infraestructura.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-016

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`, merge verificable de PR #64 sobre parents `55e0d875... + 3e7fd0a0...`.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. Slice A #58 integrada y atomic empty-index #64 integrado como `b114111caf...`. Residual prioritario: bounded/paged library contract + consumer windowing + evidencia medible de no-global-buffer; `NIGHT-AAA-017`. Cold/warm residual sigue después.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado como `55e0d875...`; deploy/staging/rollback reales siguen externos.
- **F3 / 17.1:** `[ 🟡 ] SOFTWARE CANDIDATE GREEN / NOT INTEGRATED`. PR #65 head exacto `e65538640581f3f986748968db1f4dfb069c2579`, base `b114111caf...`, OPEN/Ready/mergeable. Exact-head: F3 `33276769749`, Required CI/Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` = SUCCESS; Upgrade `33276769715` SKIPPED/no aplicable. `NIGHT-WOZ-016` = owner race-check/merge; no 17.2 todavía.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 head `8768856ff8ea15c7fa164e4b433abccf02852fb1`, base `b114111caf...`, OPEN/Ready/mergeable. F4 Matrix `33276125761`, D6 `33276125754`, D7 `33276125735`, Desktop Portability `33276125736` SUCCESS. Windows Import `33276125806` FAILURE después de prepare PASS por runner bootstrap: EdgeDriver mismatch, `tauri-driver` missing y WDIO sin browser/session. `windows/import` sigue `NOT_COVERED`; `NIGHT-BBB-016` corrige solo ese tooling/harness.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 016

### AAA — `NIGHT-AAA-017` — F2 / 12.1 bounded pagination/window/memory
Assignment 016 quedó superseded before execution únicamente para emitir el nuevo ID del ciclo. El área se conserva por fresh critical-path recalculation: sigue siendo el blocker interno prioritario de F2. No D13–D15.

### BBB — `NIGHT-BBB-016` — F4 / 25.1 SAME #63 runner bootstrap
SAME #63; reparar únicamente EdgeDriver/Tauri Driver/session bootstrap y exigir fresh functional PASS exact-head. No product fix F2/F3 ni segundo slice.

### WOZ — `NIGHT-WOZ-016` — F3 / 17.1 SAME #65 integration transaction
Exact-head ya verde. Race-check/merge solo si head/base siguen exactos y compatibles. Tras merge declarar únicamente 17.1 SOFTWARE DONE/INTEGRATED; 17.2 requiere ID nuevo.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 016

1. **F3 / 17.1 #65:** candidato exact-head verde; cierre inmediato depende solo de race-check/merge del owner.
2. **F2 / 12.1 pagination/window/memory:** mayor blocker interno restante de F2; no hay candidato aún.
3. **F4 / 25.1 #63:** functional gate rojo por bootstrap/tooling concreto; arreglo acotado puede convertir `windows/import` en evidencia real.
4. **F0/F1:** tails externos/RO; no repetir trabajo técnico ya aceptado.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111cafb29b4aa50cdce014059c66a75bddf2`.

Candidates vivos:
- #63 @ `8768856f...` — OPEN/Ready/mergeable, base `b114111c...`; Windows Import red por runner bootstrap; demás applicable exact-head CI green.
- #65 @ `e6553864...` — OPEN/Ready/mergeable, base `b114111c...`; todos los applicable exact-head gates observados green.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementación interna oculta.
- Schema: **Galer T-Library Schema v2**.
- Web pura: sin Tauri ni Desktop helper.
- Media: device ↔ provider directo; Galer Cloud no relaya beats/proyectos.
- Permanent auth/control secrets quedan control-side; cliente usa temporary auth.
- Shared-bot fallback solo cuando no hay bots libres; exclusividad por vault es camino normal.
- v1 no se publica free-only.
- YouTube existe en Desktop/Web; Web no llama Tauri.

## NEXT

**AAA:** `NIGHT-AAA-017` bounded pagination/window/memory.  
**BBB:** `NIGHT-BBB-016` SAME #63 runner bootstrap → fresh Windows Import PASS.  
**WOZ:** `NIGHT-WOZ-016` SAME #65 exact-head green race-check/merge.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 016; GitHub prevalece si cambia después de este commit.
