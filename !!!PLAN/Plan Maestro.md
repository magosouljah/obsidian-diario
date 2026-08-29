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

## Estado vivo — NIGHT-JOBS-021

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`; merge verificado de PR #66.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. #58 y #64 integrados. PR #66 quedó CLOSED/MERGED como `712b49b6689a31a47902dbe95e98622d001dab40`; quedan únicamente cold/warm cuantificado y cualquier residual de taxonomy/state no demostrado. `NIGHT-AAA-021` ASSIGNED para cerrar esos residuales con REUSE-FIRST.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65 merge `ed6aab7e...`; no prueba Stripe productivo.
- **F3 / 17.2:** `[ 🟡 ] CANDIDATE / REFRESH REQUIRED`. SAME PR #67 sigue OPEN/Ready, head `8a5341114e00f373bd88553f3f95be53a153b6b8`. El corrective mínimo del stale recovery ledger quedó probado en ese exact head: F3 17.2 `33280134623`, D6 `33280134598`, D7 `33280134660`, temp-auth `33280134648` y Required CI/Desktop Portability `33280134630` terminaron SUCCESS. Pero esa combinación fue creada contra el baseline anterior `ed6aab7e...`; después #66 movió integration a `712b49b...`. `NIGHT-WOZ-020` ASSIGNED para refresh SAME #67 + fresh exact-head CI + merge solo si verde.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 sigue OPEN/Ready, head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`, pero quedó stale frente a `712b49b...`. El failure Windows Import se redujo factual a WDIO session creation `DevToolsActivePort file doesn't exist` después de bootstrap oficial y antes de cualquier import assertion; `windows/import` sigue `NOT_COVERED`. `NIGHT-BBB-020` ASSIGNED para refresh SAME #63 + corrective F4 mínimo + PASS literal/fresh CI.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 021

### AAA — `NIGHT-AAA-021` — F2 / 12.1 residual
PRIMARY: REUSE-FIRST sobre #58/#66; cuantificar cold/warm y cerrar únicamente taxonomy/state residual con evidencia literal. Si requiere cambios, una sola rama/PR F2 mínima; no D13–D15.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-020` — F4 / 25.1 SAME #63
PRIMARY: refresh SAME #63 onto `712b49b...`, corrective mínimo de runner/session guiado por `DevToolsActivePort`, Windows Import literal PASS + fresh applicable exact-head CI, merge solo si race-check verde.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-020` — F3 / 17.2 SAME #67
PRIMARY: refresh SAME #67 onto `712b49b...`; preservar corrective `listMigrations()` y recovery invariants; fresh exact-head CI; merge solo si todo queda verde.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 021

1. **F3 / 17.2 / #67:** ya tiene corrective y CI verde en combinación vieja; refresh/fresh exact-head es la transacción crítica más corta hacia cierre 17.2.
2. **F4 / 25.1 / #63:** refresh + corregir session bootstrap hasta Windows Import literal PASS; no promover `NOT_COVERED` antes.
3. **F2 / 12.1:** cerrar residual cold/warm + taxonomy/state; pagination/window/memory productivo ya integrado por #66.
4. **F0/F1:** blockers externos/RO; no repetir drills técnicos ya aceptados.
5. Después: D13–D15, F3 18–20 y F4 25.2 + D22/D23 externos. F5 no se abre por calendario.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`; #66 → `712b49b6689a31a47902dbe95e98622d001dab40`.

Candidates vivos:
- #67 @ `8a534111...` — OPEN; old-base exact-head CI all green; refresh onto `712b49b...` required before merge.
- #63 @ `ea00d85d...` — OPEN; stale versus live integration; Windows Import still not literal PASS.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-021`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-020`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-020`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh exact-head a los candidates restantes cuando la combinación cambie materialmente.  
**PLAN_HEALTH:** sincronizado al estado GitHub observado en CYCLE 021; GitHub vivo prevalece si cambia después.
