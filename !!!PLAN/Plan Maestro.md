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

## Estado vivo — NIGHT-JOBS-029

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo sigue sin merge posterior a #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`; queda comparación cold/warm Web real cuantificada/reproducible.
- **F2 / 13.1 Web:** `[ 🟡 ] IN PROGRESS`. PR #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` mantiene helper Save All/bulk conflict-safe con D6/D7/Desktop Portability exact-head SUCCESS; product Review/Import/Bulk wiring e integración siguen pendientes.
- **F2 / 13.1 server:** PR #70 `woz/night-13.1-orphan-lifecycle @ 5a99ebf2...` OPEN/Ready. Focused `F2 - 13.1 Orphan Lifecycle` run `33304798320` = SUCCESS. Required CI/Test Desktop Portability run `33304798363` = FAILURE en `PostgreSQL live integration + recovery gate`, paso `Execute migrations and adversarial persistence checks on PostgreSQL`; no PASS/merge hasta atribución y exact-head green.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`. PR #68 sigue OPEN/Ready/mergeable, base `3ad8f55a...`, head `2a988ec2...`; no existe merge SHA aceptado.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] WINDOWS IMPORT PROVEN / PROMOTION PENDING`. SAME #63 @ `e14a3ab9...`: F4 Matrix `33303300262`, D6 `33303300263`, D7 `33303300298`, Desktop Portability `33303300278`, Windows Import `33303300259` = SUCCESS; promotion/new-head fresh CI todavía pendiente.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 029

### AAA — `NIGHT-AAA-029` — F2 / 13.1 Web-only
PRIMARY: SAME #69. Confirmar/wirear el flujo productivo Review/Import/Bulk al helper Save All/progreso/resumen parcial/conflict-safe; fresh exact-head CI si cambia head; race-check/merge solo si verde. No tocar #70/server journal.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-028` — F4 / 25.1 SAME #63
PRIMARY: promover únicamente `windows/import` a `AUTOMATED_PASS`; nuevo head exige Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head; race-check/merge solo si verde.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-028` — F2 / 13.1 server SAME #70
PRIMARY: procesar el Required CI rojo de #70: atribuir el failure PostgreSQL live/recovery; corregir solo si atribuible al candidate; fresh exact-head tests/CI tras cualquier cambio; integrar #70 solo si todo aplicable queda verde y baseline compatible. No tocar #68 ni frontend AAA.  
CI-FALLBACK: `NONE`.

**Holding item WOZ:** PR #68 / F3 18.1 permanece exact-head green pero bloqueado por execution layer; no se recrea ni se reintenta ceremonialmente.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 029

1. **F4 / 25.1 / #63:** promotion → fresh exact-head gates → race-check/merge sigue siendo el cierre técnico más corto disponible.
2. **F2 / 13.1:** AAA #69 completa product wiring Web mientras WOZ #70 aísla/corrige Required CI PostgreSQL en server lane, sin overlap.
3. **F3 / 18.1 / #68:** candidate técnicamente listo pero bloqueado por execution layer; conservar frozen.
4. **F2 / 12.1:** cold/warm runtime Web real sigue abierto; no fabricar benchmark.
5. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20, resto F4 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #69 @ `b2ab75ae...` — Web helper green; product wiring/integration pendiente.
- #70 @ `5a99ebf2...` — focused F2 workflow SUCCESS; Required CI PostgreSQL gate FAILURE; no merge.
- #68 @ `2a988ec2...` — exact-head applicable CI green; merge execution blocked externally.
- #63 @ `e14a3ab9...` — Windows Import + applicable CI exact-head SUCCESS; matrix promotion transaction pendiente.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-029`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-028`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-028`; no tocar #68.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva integration obliga revalidación fresh de candidates restantes cuando el cambio sea material.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 029; GitHub vivo prevalece si cambia después.
