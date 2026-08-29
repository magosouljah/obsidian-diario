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

## Estado vivo — NIGHT-JOBS-015

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ b114111cafb29b4aa50cdce014059c66a75bddf2`, merge verificable de PR #64 sobre parents `55e0d875... + 3e7fd0a0...`.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. Slice A integrada por #58. Atomic empty-index quedó **DONE / INTEGRATED** por PR #64 como `b114111caf...`, Required CI `33272883660` SUCCESS. Residual prioritario: paged/bounded library contract + consumer windowing + measurable memory evidence; `NIGHT-AAA-016` asignado. Cold/warm residual sigue después.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #61 integrado como `55e0d875...`; deploy/staging/rollback reales siguen externos.
- **F3 / 17.1:** PR #65 `woz/night-17.1-checkout-contract @ 584b5cf3...` OPEN/Ready/mergeable sobre base `b114111caf...`. Focal 17.1, D6, D7 y temp-auth SUCCESS; Required CI `33276146715` sigue IN_PROGRESS. No merge todavía.
- **F4 / 21.1+21.2:** `[x]` PR #51. **24.1:** `[x]` PR #55. **24.2:** `[x]` PR #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 está OPEN/Ready/mergeable sobre base `b114111caf...`, head `8768856ff8ea15c7fa164e4b433abccf02852fb1`. F4 Matrix/D6/D7 ya SUCCESS; Windows Import `33276125806` IN_PROGRESS y Desktop Portability `33276125736` PENDING. `windows/import` sigue `NOT_COVERED` hasta PASS literal.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 015

### AAA — `NIGHT-AAA-016` — F2 / 12.1 paged library contract + consumer windowing
#64 ya fue integrado. Implementar un bounded/paged data contract real que evite full-library/global `Beat[]`, coordinar consumers/windowing y producir evidencia medible large-library. No D13–D15.

### BBB — `NIGHT-BBB-015` — F4 / 25.1 SAME #63 corrective
Sigue vigente mientras exact-head Windows Import/CI terminan. No nuevo Assignment ID hasta procesar ese resultado. `AUTOMATED_PASS` solo con PASS literal + applicable CI green + race-check.

### WOZ — `NIGHT-WOZ-015` — F3 / 17.1 SAME #65 candidate
Sigue vigente mientras Required CI `33276146715` termina. No nuevo Assignment ID hasta procesar el resultado. Sin Stripe real/credenciales/costo.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 015

1. **F2 / 12.1 pagination/window/memory:** atomic bootstrap ya integrado; este residual es el siguiente blocker interno de F2.
2. **F3 / 17.1 #65:** candidate software existe; falta Required CI + race-check/merge.
3. **F4 / 25.1 #63:** correction/refresco hechos; falta Windows Import functional PASS + Required CI.
4. **F0/F1:** continúan external/RO tails; no repetir trabajo técnico aceptado.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111cafb29b4aa50cdce014059c66a75bddf2`.

Candidates vivos:
- #63 @ `8768856f...` — OPEN/Ready/mergeable, base `b114111c...`; functional/Required CI aún no cerrados.
- #65 @ `584b5cf3...` — OPEN/Ready/mergeable, base `b114111c...`; focal/D6/D7/temp-auth green, Required CI en progreso.

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

**AAA:** `NIGHT-AAA-016` paged library contract + consumer windowing + large-library evidence.  
**BBB:** mantener `NIGHT-BBB-015` hasta cierre factual de CI de #63.  
**WOZ:** mantener `NIGHT-WOZ-015` hasta cierre factual de Required CI de #65.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 015; GitHub prevalece si cambia después de este commit.
