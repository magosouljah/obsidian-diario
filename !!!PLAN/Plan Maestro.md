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

## Estado vivo — NIGHT-JOBS-031

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo sigue sin merge posterior a #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`; queda comparación cold/warm Web real cuantificada/reproducible.
- **F2 / 13.1 Web:** `[ 🟡 ] PRODUCT WIRING GAP`. PR #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` sigue OPEN/Ready/mergeable; helper/unit evidence y CI previo están verdes, pero falta wiring productivo App/Review al coordinator `saveAllWebItems`. `NIGHT-AAA-030` no dejó resultado observable y queda superseded por `NIGHT-AAA-031` con el mismo scope mínimo.
- **F2 / 13.1 server:** `[ 🟡 ] ATTRIBUTED CORRECTIVE`. PR #70 `woz/night-13.1-orphan-lifecycle @ 5a99ebf2...` sigue OPEN/Ready/mergeable. Focused F2 `33304798320` = SUCCESS. Required CI `33304798363` falló de forma determinista porque el fixture `cloud-server/tests/postgres-live.integration.cjs` no proporciona el nuevo guard `isObjectStillOrphan`; PostgreSQL estuvo sano. JOBS autoriza explícitamente ese quinto path de test como corrective mínimo, sin cambiar el comportamiento productivo fail-closed.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`. PR #68 sigue OPEN/Ready/mergeable @ `2a988ec2...`; no existe merge SHA aceptado. Candidate frozen.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] WINDOWS IMPORT PROMOTED / MATRIX CONTRACT RED`. SAME #63 @ `1b957eff...` sigue OPEN/Ready/mergeable. Windows Import `33305947664` = SUCCESS y Required CI `33305947677` = SUCCESS; F4 Functional Matrix `33305947676` = FAILURE en `Validate dependency-safe matrix contract`. `NIGHT-BBB-029` no dejó resultado observable y queda superseded por `NIGHT-BBB-030` con el mismo corrective reducido.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 031

### AAA — `NIGHT-AAA-031` — F2 / 13.1 Web SAME #69
PRIMARY: reutilizar SAME #69 e implementar únicamente el wiring productivo mínimo App/Review/Import/Bulk al coordinator existente `saveAllWebItems`; demostrar saved/conflict/failed + partial/retry semantics; fresh exact-head CI y merge solo si todo aplicable queda verde. No tocar #70/server journal.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-030` — F4 / 25.1 SAME #63
PRIMARY: reutilizar SAME #63 y atribuir/corregir únicamente el `matrix-contract` rojo del promotion head `1b957eff...`; no reabrir Windows import harness. Tras cualquier head nuevo exigir F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head; merge solo si todo verde.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-030` — F2 / 13.1 server SAME #70
PRIMARY: corrective mínimo ya atribuido. JOBS autoriza añadir `cloud-server/tests/postgres-live.integration.cjs` al scope de #70 exclusivamente para actualizar el fixture ETIMEDOUT con un guard positivo `isObjectStillOrphan` (o equivalente autoritativo), preservando el fail-closed productivo. Después focused F2 + Required CI fresh exact-head; merge solo si todo aplicable queda verde. No tocar frontend/#69, #68, infra ni producto fuera del corrective.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 031

1. **F2 / 13.1 server / #70:** aplicar el único corrective de fixture ya atribuido → fresh focused + Required CI → race-check/merge.
2. **F4 / 25.1 / #63:** matrix-contract corrective → fresh gates → race-check/merge.
3. **F2 / 13.1 Web / #69:** product wiring mínimo → focused evidence + fresh CI → merge.
4. **F3 / 18.1 / #68:** candidate técnicamente listo pero bloqueado por execution layer; conservar frozen.
5. **F2 / 12.1:** cold/warm runtime Web real sigue abierto; no fabricar benchmark.
6. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
7. Después: F2 13.2–15, F3 18.2–20 y resto F4 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #69 @ `b2ab75ae...` — product wiring pendiente.
- #70 @ `5a99ebf2...` — focused PASS; Required CI failure atribuida a fixture legacy; corrective de test autorizado.
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

**AAA:** ejecutar una sola vez `NIGHT-AAA-031`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-030`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-030`; corrective de fixture autorizado, no tocar #68.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva integration obliga revalidación fresh de candidates restantes cuando la combinación sea material.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 031; GitHub vivo prevalece si cambia después.
