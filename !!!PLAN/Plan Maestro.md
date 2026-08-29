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

## Estado vivo — NIGHT-JOBS-013

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`, merge verificable de PR #60. GitHub reread del ciclo confirma que no hubo nueva integración antes de emitir las órdenes 014.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. Slice A está integrada por #58. `NIGHT-AAA-013` produjo PR #64 `aaa/night-12.1-atomic-empty-index @ 86ea14ad04357d86d4140f17621bd3a835435350`, OPEN/Ready/mergeable, con primitive server-side `/transport/index/ensure` + Web wire y tests focales añadidos. Sin embargo el exact-head `Test - Desktop Portability / Required CI` run `33271187072` terminó **FAILURE**: Web+shared falló en Chrome smoke, Portable Windows falló y ambos native macOS smoke fallaron. Los tests focales del atomic bootstrap también quedaron UNVERIFIED en el handoff 013. No merge/no PASS. `NIGHT-AAA-014` reutiliza SAME #64 para causa mínima + fixes atribuibles + ejecución de tests + fresh exact-head CI.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE CANDIDATE / READY_FOR_OWNER_RACE_CHECK`. SAME PR #61 fue refrescada sobre el baseline vivo mediante head `d254b294cf8fe78d93025271360dd73ed594898f`. GitHub actual: OPEN/Ready/mergeable=true; Required CI exact-head run `33271019389` SUCCESS; D6 `33271019493` SUCCESS; no failure/in-progress observado en el set exact-head. No se reclama integración: `NIGHT-WOZ-014` ejecuta race-check + protected merge, o refresh/fresh CI si integration se mueve antes.
- **F4 / 21.1+21.2:** `[x]` PR #51. **24.1:** `[x]` PR #55. **24.2:** `[x]` PR #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. PR #60 integró la matriz. `NIGHT-BBB-013` produjo PR #63 `bbb/task-25.1-windows-import @ 65a7bf07029babfb500d3913226ec8a5ca6e0deb`, OPEN/Ready/mergeable. Required CI `33271091123` fue SUCCESS, pero el gate funcional específico `F4 - 25.1 Windows Import Journey` run `33271091186` terminó **FAILURE** en `Run existing Windows import E2E harness`. Por tanto `windows/import` NO puede promoverse a AUTOMATED_PASS ni #63 integrarse todavía. `NIGHT-BBB-014` corrige/explica SAME #63 sin robar fixes F2/F3.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 013 → órdenes 014

### AAA — `NIGHT-AAA-014` — F2 / 12.1 SAME #64 corrective transaction
Procesar el failure exact-head de #64 y ejecutar los tests focales que 013 dejó UNVERIFIED. Fixes solo atribuibles al atomic bootstrap/harness de su slice. Fresh CI exact-head tras cambio material. Integrar únicamente con tests + applicable CI green + race-check. No pagination/window/memory/cold-warm ni D13–D15 hasta resolver #64.

### BBB — `NIGHT-BBB-014` — F4 / 25.1 SAME #63 Windows import corrective transaction
El Required CI amplio verde no sustituye el journey funcional rojo. Diagnosticar/fijar únicamente workflow/glue/harness F4; product bug ajeno → `PRODUCT_FINDING`. La matriz no marca PASS antes de un run funcional exact-head verde. No segundo slice ni 25.2.

### WOZ — `NIGHT-WOZ-014` — F3 / 16.2 SAME #61 merge transaction
El CI exact-head de `d254b294...` ya está verde y #61 mergeable. Owner debe hacer race-check + protected merge si integration aún es `7de7b57a...`; si otro owner mueve baseline primero, refresh SAME #61 + fresh CI. Tras merge, solo `SOFTWARE DONE / EXTERNAL TAIL`. Puede hacer audit READ-ONLY de 17.1 después, sin implementar Stripe sin nueva orden.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 013

1. **F2 / 12.1 #64 rojo:** el atomic bootstrap ya tiene candidate, pero el gate amplio exact-head falló. Resolver ese failure y probar los tests focales es el camino interno más crítico de F2 antes de avanzar pagination/window/memory/cold-warm o D13–D15.
2. **F3 / 16.2 #61 verde:** es el retorno inmediato más alto; candidate está exact-head green/mergeable y solo falta la transacción del owner, sujeta a race-check. Después F3 sigue con physical tail + D17–D20.
3. **F4 / 25.1 #63 rojo funcional:** el journey Windows/import produjo evidencia negativa real. Corregirlo es más útil que iniciar otro residual y evita falsa cobertura.
4. **F0/F1:** continúan external/RO tails; no repetir trabajo técnico aceptado.

No se conservó trabajo por inercia: AAA permanece en #64 porque existe un failure atribuible pendiente en su candidate; BBB permanece en #63 porque su gate funcional reveló un failure real; WOZ permanece en #61 porque GitHub ya convirtió el blocker de CI en candidate listo para race-check. Son tres piezas distintas y sin ownership simultáneo.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a508b3cf05cbded81501fbd3da63922a3`.

Candidates vivos:
- #64 @ `86ea14ad...` — OPEN/mergeable, **Required CI FAILURE**, no merge.
- #63 @ `65a7bf070...` — OPEN/mergeable, Required CI green pero **Windows import functional FAILURE**, no merge.
- #61 @ `d254b294...` — OPEN/mergeable, applicable exact-head CI observado verde; owner race-check/merge pendiente.

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

**AAA:** `NIGHT-AAA-014` SAME #64 CI failure + focal tests + corrective exact-head transaction.  
**BBB:** `NIGHT-BBB-014` SAME #63 Windows import functional failure; no false PASS.  
**WOZ:** `NIGHT-WOZ-014` SAME #61 race-check/protected merge; refresh+fresh CI si baseline se mueve.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 013; GitHub prevalece si cambia después de este commit.
