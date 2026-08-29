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

## Estado vivo — NIGHT-JOBS-014

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`, merge verificable de PR #61 sobre parents `7de7b57a... + d254b294...`.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. Slice A está integrada por #58. Atomic empty-index SAME PR #64 está ahora OPEN/Ready/mergeable sobre base viva `55e0d875...`, exact head `3e7fd0a0d7db6f7f423de47c86e643c36d6bcd24`. El Required CI/Test Desktop Portability `33272883660` terminó **SUCCESS** exact-head; Web+shared, Portable Windows y native macOS observados SUCCESS. No se reclama integración hasta owner race-check/merge. `NIGHT-AAA-015` procesa merge y, solo después, residual pagination/window/memory.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #61 protegido/integrado como `55e0d875...`; deploy/staging/rollback reales siguen externos. `NIGHT-WOZ-015` pasa explícitamente a F3/17.1 software-only Stripe Checkout server-side, sin credenciales/costo.
- **F4 / 21.1+21.2:** `[x]` PR #51. **24.1:** `[x]` PR #55. **24.2:** `[x]` PR #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. PR #60 integró la matriz. SAME PR #63 está OPEN/Ready/mergeable pero stale respecto a `55e0d875...`; exact head `9208ead249345d29458a5ae939923dd5c2f47dfb`. F4 Matrix/D6/D7/Desktop Portability verdes, pero Windows Import `33272794199` terminó **FAILURE** antes de specs porque el bootstrap `prepare-f4-25.1-embedded-driver.mjs` no encontró el marker esperado. `windows/import` sigue `NOT_COVERED`. `NIGHT-BBB-015` corrige solo glue/harness, refresh y exige functional PASS + fresh exact-head CI.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 014 → órdenes 015

### AAA — `NIGHT-AAA-015` — F2 / 12.1 SAME #64 merge + residual
Race-check + protected merge de #64 si GitHub sigue exactamente compatible; si baseline/head cambia, refresh SAME lineage + fresh CI. Después de merge, cerrar solo atomic sub-slice y avanzar pagination/window/memory como siguiente residual pequeño y dependency-safe. No D13–D15.

### BBB — `NIGHT-BBB-015` — F4 / 25.1 SAME #63 corrective
Fix mínimo marker-safe del bootstrap, refresh SAME lineage sobre baseline vivo y functional Windows Import exact-head. `AUTOMATED_PASS` solo con PASS literal; bug producto ajeno → `PRODUCT_FINDING`. No segundo slice/25.2.

### WOZ — `NIGHT-WOZ-015` — F3 / 17.1 Stripe Checkout software-only
16.2 ya cerró su slice software. Duplicate-check no encontró implementación Stripe reutilizable. Implementar server-side Checkout contract con IDs/precios estables, idempotency y rechazo de precio/plan controlado por cliente; adapter/mocks permitidos. Sin Stripe real, credenciales, costo, 17.2 completo ni D18–D20.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 014

1. **F2 / 12.1 #64 exact-head verde:** es el retorno inmediato más alto; merge del atomic bootstrap desbloquea el residual pagination/window/memory sin rehacer trabajo.
2. **F3 / 17.1:** 16.2 software quedó integrado; F3 D17–D20 es ahora el mayor volumen técnico abierto. Stripe Checkout server-side software-only puede avanzar sin esperar physical staging ni credenciales reales.
3. **F4 / 25.1 #63 functional red:** failure reproducible y atribuible a glue F4; corregirlo antes de ampliar cobertura evita falsa matriz y deuda.
4. **F0/F1:** continúan external/RO tails; no repetir trabajo técnico aceptado.

No se conservó trabajo por inercia: AAA sigue en #64 porque el candidate pasó a merge-ready; BBB sigue en #63 por failure específico demostrado; WOZ cambia de 16.2 ya integrado a 17.1 porque ese es ahora el siguiente bloque técnico independiente de mayor retorno.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d8759ec03b23fa8e4f1f35304922dffeb992`.

Candidates vivos:
- #64 @ `3e7fd0a0...` — OPEN/Ready/mergeable, base `55e0d875...`, Required CI `33272883660` SUCCESS; owner merge transaction pendiente.
- #63 @ `9208ead249...` — OPEN/Ready/mergeable, stale vs `55e0d875...`; Windows Import `33272794199` FAILURE en bootstrap; no merge.

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

**AAA:** `NIGHT-AAA-015` SAME #64 owner merge; después pagination/window/memory.  
**BBB:** `NIGHT-BBB-015` SAME #63 marker-safe fix + refresh + functional exact-head.  
**WOZ:** `NIGHT-WOZ-015` F3/17.1 server-side Stripe Checkout software-only.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 014; GitHub prevalece si cambia después de este commit.
