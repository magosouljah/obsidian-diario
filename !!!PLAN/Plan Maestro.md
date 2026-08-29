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

## Estado vivo — NIGHT-JOBS-017 FINAL

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`, merge verificable de PR #65 sobre parents `b114111caf... + e655386405...`.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. #58 y atomic #64 integrados. PR #66 head histórico actual `c9b5cd95ad5b6b4d8f681265992e44d8c777a76f` contiene bounded first-load + paged primitive + 10,321-beat test, pero consumer navigation/refresh/no-dup/no-omission/bounded evidence siguen incompletos. Su base `b114111caf...` quedó stale tras #65; `NIGHT-AAA-018` exige refresh SAME #66 sobre `ed6aab7e...` + completion + fresh exact-head CI antes de merge.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — PR #65 exact head `e65538640581f3f986748968db1f4dfb069c2579`; F3 `33276769749`, Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` SUCCESS; merge `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`. Esto NO prueba Stripe productivo/credenciales/precios reales.
- **F3 / 17.2:** `[ 🟡 ] ASSIGNED` — `NIGHT-WOZ-018`: webhook integrity/raw-body signature + durable event dedupe/idempotency/retry software-only; no provider resources/costo.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. #63 head `8768856f...` sigue Windows Import red por EdgeDriver/Tauri Driver/WDIO bootstrap y su base `b114111caf...` quedó stale por #65. `NIGHT-BBB-017` exige refresh SAME #63 sobre `ed6aab7e...`, fix mínimo y fresh functional/exact-head evidence.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 017 FINAL

### AAA — `NIGHT-AAA-018` — F2 / 12.1 SAME #66
Refresh sobre `ed6aab7e...`; completar consumer windowing/navigation/refresh/no-dup/no-omission + evidence bounded medible; fresh exact-head antes de merge. No D13–D15.

### BBB — `NIGHT-BBB-017` — F4 / 25.1 SAME #63
Refresh sobre `ed6aab7e...`; reparar únicamente EdgeDriver/Tauri Driver/WDIO bootstrap; fresh Windows Import PASS + applicable exact-head CI. No 25.2.

### WOZ — `NIGHT-WOZ-018` — F3 / 17.2 webhook software contract
17.1 quedó integrado durante el race-check final del ciclo. Implementar REUSE-FIRST raw-body signature verification, durable event ID/idempotency, duplicate/out-of-order safety y retry/failure state. No Stripe productivo, no 18.x, no infraestructura/costo.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado desde cero tras merge #65

1. **F2 / 12.1 #66:** mayor blocker interno activo F2; candidate parcial debe refrescarse/completarse.
2. **F3 / 17.2:** siguiente slice interno dependency-ready tras 17.1 integrado; software-only y paralelo a F2/F4.
3. **F4 / 25.1 #63:** functional gate rojo + stale por nuevo baseline; fix runner acotado sigue necesario.
4. **F0/F1:** tails externos/RO; no repetir trabajo técnico ya aceptado.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.

Candidates vivos:
- #66 @ `c9b5cd95...` — OPEN/mergeable pero base `b114111c...` stale; bounded primitive parcial, gate consumer/evidence incompleto; refresh required.
- #63 @ `8768856f...` — OPEN/Ready/mergeable pero base `b114111c...` stale; Windows Import red; refresh required.

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

**AAA:** `NIGHT-AAA-018` SAME #66 refresh/completion.  
**BBB:** `NIGHT-BBB-017` SAME #63 refresh/bootstrap → fresh Windows Import PASS.  
**WOZ:** `NIGHT-WOZ-018` F3/17.2 webhook integrity/idempotency/retry software-only.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 017 final; GitHub prevalece si cambia después.
