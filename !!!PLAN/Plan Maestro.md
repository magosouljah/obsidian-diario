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

## Estado vivo — NIGHT-JOBS-020

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`; GitHub vivo sigue apuntando al merge #65.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. #58 y #64 integrados. SAME PR #66 está OPEN sobre base `ed6aab7e...`, head `86f9659b0341107496332ada546312611e40ddaa`. El candidate ya contiene navegación React Previous/Next por cursor bounded sin materializar un `Beat[]` global; conserva continuidad sintética 10,321 beats, lazy artwork y materialización bounded. Required CI/Desktop Portability `33278321854`, D6 `33278321859` y D7 `33278321867` terminaron SUCCESS sobre exact head. Falta race-check + integración; después siguen abiertos cold/warm cuantificado y cualquier residual de taxonomy no demostrado. `NIGHT-AAA-020` está ASSIGNED para esa transacción.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65 merge `ed6aab7e...`; no prueba Stripe productivo.
- **F3 / 17.2:** `[ 🟡 ] CANDIDATE / REQUIRED CI RED`. SAME PR #67 está OPEN sobre base `ed6aab7e...`, head `22550152e9960c5dad328711b3a8b150301a8c4f`. Focal 17.2 `33278423859`, D6 `33278423854`, D7 `33278423851` y temp-auth `33278423880` están SUCCESS, pero Required CI/Desktop Portability `33278423879` terminó FAILURE porque `PostgreSQL live integration + recovery gate` falló en restored-state verification después de dump/encrypt/restore. `NIGHT-WOZ-019` está ASSIGNED para corrective mínimo SAME #67; no 18.x.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME #63 sigue OPEN/Ready sobre base `ed6aab7e...`, head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`. F4 Matrix `33277733635`, D6 `33277733621`, D7 `33277733651` y Desktop Portability/Required CI `33277733647` están SUCCESS; Windows Import `33277733650` terminó FAILURE. El job `99167313710` pasó setup/exact checkout/official Tauri+Edge bootstrap y falló dentro de `Run existing Windows import E2E harness`; por tanto `windows/import` continúa `NOT_COVERED`. `NIGHT-BBB-019` está ASSIGNED para corrective mínimo SAME #63.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 020

### AAA — `NIGHT-AAA-020` — F2 / 12.1 SAME #66
PRIMARY vigente: race-check exact head/base + focused evidence y protected merge de SAME #66 si la combinación sigue válida. Reclamar solo pagination/window/memory + navegación productiva demostrada.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-019` — F4 / 25.1 SAME #63
PRIMARY vigente: inspeccionar failure real del Windows Import, aplicar corrective mínimo solo si pertenece a F4, obtener PASS literal + fresh exact-head CI y merge solo si todos los gates aplicables quedan verdes.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-019` — F3 / 17.2 SAME #67
PRIMARY vigente: diagnosticar restored-state mismatch del recovery gate, corregir lo mínimo sin debilitar invariantes D9/D10, focal tests + fresh Required CI y merge solo con race-check verde.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 020

1. **F2 / 12.1 / #66:** cerrar transacción de integración del candidate exact-head verde; luego reducir residual cold/warm/taxonomy con evidencia.
2. **F3 / 17.2 / #67:** corregir restored-state verification sin debilitar recovery; integrar únicamente con Required CI verde.
3. **F4 / 25.1 / #63:** lograr Windows Import PASS literal y cierre de SAME lineage; `NOT_COVERED` no se promociona antes.
4. **F0/F1:** blockers externos/RO; no repetir drills técnicos ya aceptados.
5. Después: reevaluar D13–D15, F3 18–20 y F4 25.2 + D22/D23 externos. F5 no se abre por calendario.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.

Candidates vivos:
- #66 @ `86f9659b...` — OPEN; base `ed6aab7e...`; exact-head applicable CI verde; falta race-check/merge.
- #63 @ `ea00d85d...` — OPEN; base `ed6aab7e...`; Required CI general verde, Windows Import rojo; no AUTOMATED_PASS.
- #67 @ `22550152...` — OPEN; base `ed6aab7e...`; focal/D6/D7/temp-auth verdes, Required CI rojo por PostgreSQL recovery verification.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-020`; no superseder mientras siga ASSIGNED sin resultado.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-019`; no superseder mientras siga ASSIGNED sin resultado.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-019`; no superseder mientras siga ASSIGNED sin resultado.  
**JOBS:** siguiente ciclo procesa resultados reales; si una integración mueve baseline, obliga refresh/fresh exact-head a los candidates restantes.  
**PLAN_HEALTH:** sincronizado al estado GitHub observado en CYCLE 020; GitHub vivo prevalece si cambia después.
