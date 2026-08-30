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

## Estado vivo — NIGHT-JOBS-030

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo sigue sin merge posterior a #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`; queda comparación cold/warm Web real cuantificada/reproducible.
- **F2 / 13.1 Web:** `[ 🟡 ] PRODUCT WIRING GAP`. PR #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` está OPEN/Ready y su helper/unit evidence + D6/D7/Desktop Portability exact-head están verdes, pero `App.tsx` todavía usa `handleReviewedSaveAll` como ruta productiva separada y no consume el coordinator `saveAllWebItems`; no merge hasta wiring/focused evidence/fresh CI.
- **F2 / 13.1 server:** `[ 🟡 ] FOCUSED PASS / REQUIRED CI RED`. PR #70 `woz/night-13.1-orphan-lifecycle @ 5a99ebf2...` OPEN/Ready/mergeable. Focused run `33304798320` = SUCCESS; Required CI `33304798363` = FAILURE en `PostgreSQL live integration + recovery gate`. #70 cambia cuatro archivos server/F2 y ningún migration file; atribución sigue pendiente.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`. PR #68 sigue OPEN/Ready/mergeable @ `2a988ec2...`; no existe merge SHA aceptado. Candidate frozen.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] WINDOWS IMPORT PROMOTED / MATRIX CONTRACT RED`. SAME #63 @ `1b957eff...` está OPEN/Ready/mergeable. En este promotion head Windows Import run `33305947664` = SUCCESS y Required CI `33305947677` = SUCCESS, pero F4 Functional Matrix run `33305947676` = FAILURE en `Validate dependency-safe matrix contract`; no merge hasta attribution/corrective + fresh exact-head green.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 030

### AAA — `NIGHT-AAA-030` — F2 / 13.1 Web SAME #69
PRIMARY: implementar únicamente el wiring productivo mínimo App/Review/Import/Bulk al coordinator existente `saveAllWebItems`, demostrar summary saved/conflict/failed + partial/retry semantics, fresh exact-head CI tras cambio y merge solo si verde. No tocar #70/server journal.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-029` — F4 / 25.1 SAME #63
PRIMARY: atribuir/corregir únicamente el `matrix-contract` rojo del promotion head `1b957eff...`; Windows Import/Required CI ya son green en ese head. Tras cualquier corrective, exigir F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head; race-check/merge solo si todo verde.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-029` — F2 / 13.1 server SAME #70
PRIMARY: attribution-first del Required CI PostgreSQL failure; corregir solo si #70 es causa; fresh focused + Required CI si cambia head; integrar solo si todo aplicable queda green. #68 sigue frozen y fuera de este assignment.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 030

1. **F4 / 25.1 / #63:** matrix-contract corrective → fresh gates → race-check/merge. Windows Import ya no es el blocker.
2. **F2 / 13.1:** AAA #69 product wiring y WOZ #70 PG-gate attribution/fix avanzan en paralelo sin overlap.
3. **F3 / 18.1 / #68:** candidate técnicamente listo pero bloqueado por execution layer; conservar frozen.
4. **F2 / 12.1:** cold/warm runtime Web real sigue abierto; no fabricar benchmark.
5. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20 y resto F4 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #69 @ `b2ab75ae...` — helper/tests/CI green; product wiring faltante.
- #70 @ `5a99ebf2...` — focused F2 PASS; Required CI PostgreSQL gate FAILURE.
- #68 @ `2a988ec2...` — exact-head green; merge execution blocked/frozen.
- #63 @ `1b957eff...` — Windows Import + Required CI SUCCESS; F4 matrix-contract FAILURE.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-030`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-029`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-029`; no tocar #68.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva integration obliga revalidación fresh de candidates restantes cuando la combinación sea material.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 030; GitHub vivo prevalece si cambia después.
