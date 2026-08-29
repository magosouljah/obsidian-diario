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

## Estado vivo — NIGHT-JOBS-017

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`, merge verificable de PR #64.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. Slice A #58 integrada y atomic empty-index #64 integrado. PR #66 head `c9b5cd95ad5b6b4d8f681265992e44d8c777a76f`, base `b114111caf...`, OPEN/mergeable: bounded first-load + paged primitive + 10,321-beat test existen, pero consumer next/previous, refresh/invalidation, no-duplicate/no-omission y measurable rendered/memory/network evidence siguen incompletos. D6/D7 exact-head SUCCESS; Desktop Portability `33277332334` seguía IN_PROGRESS al preflight JOBS. `NIGHT-AAA-018` continúa SAME #66; DO NOT MERGE hasta cerrar el gate.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales siguen externos.
- **F3 / 17.1:** `[ 🟡 ] SOFTWARE CANDIDATE GREEN / NOT INTEGRATED`. PR #65 head exacto `e65538640581f3f986748968db1f4dfb069c2579`, base `b114111caf...`, OPEN/Ready/mergeable. F3 `33276769749`, Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` = SUCCESS; Upgrade skipped/no aplicable. `NIGHT-WOZ-017` = race-check/merge SAME #65; no 17.2 todavía.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 head `8768856ff8ea15c7fa164e4b433abccf02852fb1`, base `b114111caf...`, OPEN/Ready/mergeable. F4 Matrix/D6/D7/Desktop Portability SUCCESS. Windows Import `33276125806` FAILURE por EdgeDriver/Tauri Driver/WDIO bootstrap; `windows/import` sigue `NOT_COVERED`. `NIGHT-BBB-017` corrige únicamente tooling/harness mínimo.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 017

### AAA — `NIGHT-AAA-018` — F2 / 12.1 SAME #66 consumer windowing
Continuar SAME #66. Completar consumer navigation/windowing, refresh/invalidation, no duplicados/omisiones y evidencia bounded medible. No D13–D15.

### BBB — `NIGHT-BBB-017` — F4 / 25.1 SAME #63 runner bootstrap
`NIGHT-BBB-016` no fue ejecutado antes de este recálculo; se supersede explícitamente. SAME #63; reparar EdgeDriver/Tauri Driver/WDIO bootstrap, fresh Windows Import PASS exact-head antes de cualquier promoción.

### WOZ — `NIGHT-WOZ-017` — F3 / 17.1 SAME #65 integration transaction
`NIGHT-WOZ-016` no fue ejecutado antes de este recálculo; se supersede explícitamente. Exact-head sigue verde. Race-check/merge solo si head/base siguen exactos y compatibles. Tras merge declarar únicamente 17.1 SOFTWARE DONE/INTEGRATED; 17.2 requiere ID nuevo.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 017

1. **F3 / 17.1 #65:** candidato exact-head verde; cierre interno inmediato depende solo de race-check/merge del owner.
2. **F2 / 12.1 #66:** progreso real pero incompleto; consumer windowing/evidence es el mayor blocker interno F2 activo.
3. **F4 / 25.1 #63:** functional gate rojo por bootstrap/tooling concreto; necesario para convertir Windows/import en evidencia real.
4. **F0/F1:** tails externos/RO; no repetir trabajo técnico ya aceptado.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111cafb29b4aa50cdce014059c66a75bddf2`.

Candidates vivos:
- #66 @ `c9b5cd95...` — OPEN/mergeable, base `b114111c...`; bounded primitive parcial, gate consumer/evidence incompleto; Desktop Portability aún en curso al preflight.
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

**AAA:** `NIGHT-AAA-018` SAME #66 consumer windowing/evidence.  
**BBB:** `NIGHT-BBB-017` SAME #63 runner bootstrap → fresh Windows Import PASS.  
**WOZ:** `NIGHT-WOZ-017` SAME #65 exact-head green race-check/merge.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 017; GitHub prevalece si cambia después de este commit.
