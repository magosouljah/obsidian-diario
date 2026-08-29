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

## Estado vivo — NIGHT-JOBS-018

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`; live reread sigue apuntando al merge #65.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. #58 y #64 integrados. SAME PR #66 fue refrescado al baseline vivo y ahora está en `2d9a9ae89f4594b8b72a36dcc835f92b1017bf15`: bounded current/next/previous/refresh consumer + métricas + continuidad 10,321 beats. D6/D7 exact-head están verdes; Required CI sigue en curso. Gap material: el consumer React productivo aún no invoca next/previous/cursor. `NIGHT-AAA-019` continúa SAME #66 para cerrar ese wiring + focused PASS + fresh exact-head/race-check.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65 merge `ed6aab7e...`; no prueba Stripe productivo.
- **F3 / 17.2:** `[ 🟡 ] ASSIGNED` — `NIGHT-WOZ-018`. No existe todavía resultado final verificable en ledger/Issue/PR, por lo que JOBS mantiene el mismo Assignment ID y no emite 019.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 fue refrescado a base `ed6aab7e...` y head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`. F4 Matrix/D6/D7 exact-head están verdes; Windows Import y Desktop Portability siguen en curso. `windows/import` permanece `NOT_COVERED` hasta PASS literal. `NIGHT-BBB-018` reutiliza esos runs y cierra o corrige la misma lineage.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 018

### AAA — `NIGHT-AAA-019` — F2 / 12.1 SAME #66
Cerrar el wiring React productivo de next/previous/cursor sin `Beat[]` global completo; focused tests ejecutados; fresh exact-head CI después del head final; race-check/merge solo si verde. No D13–D15.

### BBB — `NIGHT-BBB-018` — F4 / 25.1 SAME #63
Reutilizar Windows Import `33277733650` y Desktop Portability `33277733647`. Si pasan: race-check, promoción literal de `windows/import` y merge SAME #63. Si falla Windows Import: fix mínimo guiado por ese log y fresh exact-head. No 25.2.

### WOZ — `NIGHT-WOZ-018` — F3 / 17.2 webhook software contract
Assignment permanece vigente y no procesado: raw-body signature verification, durable event ID/idempotency, duplicate/out-of-order safety y retry/failure state. No Stripe productivo, no 18.x, no infraestructura/costo.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 018

1. **F2 / 12.1 #66:** production navigation bounded + exact-head; luego cold/warm residual si sigue no demostrado.
2. **F3 / 17.2:** assignment vigente WOZ; sin resultado compartido verificable todavía.
3. **F4 / 25.1 #63:** conclusión funcional literal de Windows Import + Required CI; misma lineage.
4. **F0/F1:** tails externos/RO; no repetir trabajo técnico ya aceptado.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.

Candidates vivos:
- #66 @ `2d9a9ae...` — OPEN/mergeable, base `ed6aab7e...`; bounded consumer/evidence avanzado; production React navigation + final exact-head pendientes.
- #63 @ `ea00d85d...` — OPEN/Ready/mergeable, base `ed6aab7e...`; Windows Import + Required CI en curso; no AUTOMATED_PASS todavía.

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

**AAA:** `NIGHT-AAA-019` SAME #66 production navigation/focused PASS/fresh exact-head.  
**BBB:** `NIGHT-BBB-018` SAME #63 reuse exact-head runs → close/fix.  
**WOZ:** continuar `NIGHT-WOZ-018`; JOBS no emite 019 hasta resultado verificable.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 018; GitHub prevalece si cambia después.
