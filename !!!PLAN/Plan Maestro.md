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

## Estado vivo — NIGHT-JOBS-026

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo no muestra merge posterior a #67 al preflight CYCLE 026.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`. Taxonomy/state ya está demostrado; queda solo comparación cold/warm Web real, cuantificada y reproducible.
- **F2 / 13.1:** `[ 🟡 ] IN PROGRESS`. NIGHT-AAA-025 verificó que single-save durable + CAS por item y garbage-journal server-side existen, pero faltan Save All productivo/partial summary y bulk orchestration; orphan cleanup tiene boundary Web↔server. `NIGHT-AAA-026` limita AAA al carril Web Save All + bulk conflict-safe sin fingir cierre del server half.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / AWAITING OWNER INTEGRATION`. PR #68 sigue OPEN/Ready/mergeable, base `3ad8f55a...`, head `2a988ec2a25d6ecfa927614fcc32cde689995103`; exact-head F3 18.1/D6/D7/temp-auth/Desktop Portability = SUCCESS. `NIGHT-WOZ-025` es la transacción final de integración; no 18.2.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 sigue OPEN/Ready, base `3ad8f55a...`, head vivo `ed03b806669373758d38bfd211e8f8905c86e269`. Fresh exact-head F4 Matrix/D6/D7/Desktop Portability = SUCCESS, pero Windows Import `33300992453` = **FAILURE** antes de assertions. El primer failure causal observado es launcher/session: Edge driver mismatch, luego `tauri-driver not found`, luego ausencia de browserName/hostname/port. `windows/import` sigue `NOT_COVERED`; `NIGHT-BBB-025` corrective mínimo sobre SAME #63.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 026

### AAA — `NIGHT-AAA-026` — F2 / 13.1 Web-only
PRIMARY: Save All multi-item con resumen parcial + bulk conflict-safe usando durable commits/CAS existentes; no server-side garbage journal.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-025` — F4 / 25.1 SAME #63
PRIMARY: consumir failure `33300992453`/job `99228993010`, corregir launcher/session F4 mínimo hasta session + Windows Import literal PASS; no producto ni matrix promotion prematura.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-025` — F3 / 18.1 PR #68
PRIMARY: revalidar race/base/head y procesar integración exacta de #68; verificar merge SHA e integration post-merge; STOP sin 18.2.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 026

1. **F3 / 18.1 / #68:** candidate exact-head verde y base viva sin carrera observada; integración por WOZ es la transacción más corta.
2. **F4 / 25.1 / #63:** el cuello está reducido a launcher/session Windows antes de assertions; obtener PASS literal, no green genérico.
3. **F2 / 13.1:** avanzar Save All + bulk Web mientras el orphan-journal server half queda separado y explícito.
4. **F2 / 12.1:** cold/warm runtime real sigue abierto; no fabricar benchmark.
5. **F0/F1/D22/D23:** blockers externos/RO; no repetir drills aceptados.
6. Después: server half F2/13.1, 13.2–15, F3 18.2–20, resto F4 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #68 @ `2a988ec2...` — OPEN/Ready/mergeable; exact-head applicable CI green; awaiting owner integration.
- #63 @ `ed03b806...` — OPEN/Ready; fresh Windows Import `33300992453` FAILURE before assertions.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-026`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-025`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-025`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva integration obliga race revalidation/fresh applicable exact-head para candidates afectados.  
**PLAN_HEALTH:** sincronizado al estado GitHub observado en CYCLE 026; GitHub vivo prevalece si cambia después.
