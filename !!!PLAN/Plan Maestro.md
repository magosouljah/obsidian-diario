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

## Estado vivo — NIGHT-JOBS-028

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo no muestra merge posterior a #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`; queda solo comparación cold/warm Web real cuantificada/reproducible.
- **F2 / 13.1:** `[ 🟡 ] IN PROGRESS`. PR #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` está OPEN/Ready/mergeable y sus gates exact-head D6/D7/Desktop Portability están SUCCESS. El helper Save All/bulk conflict-safe existe; falta confirmar/wirear el flujo productivo real y luego integrar por el owner. El server half garbage-journal/orphan cleanup sigue separado y owned por WOZ.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`. PR #68 sigue OPEN/Ready/mergeable, base `3ad8f55a...`, head `2a988ec2...`; no existe merge SHA aceptado.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] WINDOWS IMPORT PROVEN / PROMOTION PENDING`. SAME #63 OPEN/Ready/mergeable, base `3ad8f55a...`, head `e14a3ab9...`. Fresh exact-head F4 Matrix `33303300262`, D6 `33303300263`, D7 `33303300298`, Desktop Portability `33303300278` y **Windows Import `33303300259`** terminaron SUCCESS. `windows/import` no se promueve a `AUTOMATED_PASS` hasta que BBB actualice la matrix en un nuevo head y vuelva a obtener el set fresh exact-head requerido.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 028

### AAA — `NIGHT-AAA-028` — F2 / 13.1 Web-only
PRIMARY: SAME #69. Reutilizar helper ya probado, comprobar si está realmente wired al flujo productivo Review/Import/Bulk; si falta, conectar únicamente Save All/progreso/resumen parcial/conflict-safe sin tocar server journal. Fresh exact-head CI y merge solo si todo verde/race-check limpio.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-027` — F4 / 25.1 SAME #63
PRIMARY: aceptar Windows Import literal SUCCESS sobre `e14a3ab9...`; promover únicamente `windows/import` a `AUTOMATED_PASS`, creando nuevo head; exigir Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head en ese nuevo head; race-check y merge solo si verde.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-027` — F2 / 13.1 server half
PRIMARY: reemitir el server half no procesado: REUSE-FIRST sobre garbage journal/reconciliation; demostrar o implementar contrato Web-callable durable para registrar/reconciliar orphans, idempotente/fail-closed y sin borrar committed/valid. No tocar #68 ni frontend AAA.  
CI-FALLBACK: `NONE`.

**Holding item WOZ:** PR #68 / F3 18.1 permanece exact-head green pero bloqueado por execution layer; no se recrea ni se reintenta ceremonialmente.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 028

1. **F4 / 25.1 / #63:** Windows Import ya pasó; cerrar la transacción de promoción + fresh exact-head + merge es el camino más corto a reducir un gap funcional real.
2. **F2 / 13.1:** AAA completa wiring/integración Web de #69 mientras WOZ trabaja server garbage-journal/orphan cleanup en paralelo sin overlap.
3. **F3 / 18.1 / #68:** candidate técnicamente listo pero bloqueado por execution layer; conservar frozen.
4. **F2 / 12.1:** cold/warm runtime Web real sigue abierto; no fabricar benchmark.
5. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: 13.2–15, F3 18.2–20, resto F4 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #69 @ `b2ab75ae...` — OPEN/Ready/mergeable; exact-head applicable CI green; product wiring todavía no reclamado.
- #68 @ `2a988ec2...` — OPEN/Ready/mergeable; exact-head applicable CI green; merge execution blocked externally.
- #63 @ `e14a3ab9...` — OPEN/Ready/mergeable; Windows Import + applicable CI exact-head SUCCESS; matrix promotion transaction pendiente.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-028`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-027`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-027`; no tocar #68 durante este assignment.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva integration obliga revalidación fresh de candidates restantes cuando el cambio sea material.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 028; GitHub vivo prevalece si cambia después.
