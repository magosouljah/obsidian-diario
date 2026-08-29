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

## Estado vivo — NIGHT-JOBS-012

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`, merge verificable de PR #60.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS / BLOCKED-UNTIL-CONTROL-PLANE-DELTA`. PR #58 ya **MERGED** como `58a6bf614...` y cerró solo slice A. `NIGHT-AAA-012` demostró que el frontend actual no puede crear un índice ausente de forma atómica: `getLibraryIndex` exige pinned index existente y `replaceLibraryIndex` exige lectura/expected message previo. No hay implementación/PR/CI de atomic empty-index; client-only send+pin no es aceptable. `NIGHT-AAA-013` amplía explícitamente ownership de AAA al control plane/backend para resolver ese primitive sin falsear atomicidad.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE CANDIDATE / NEEDS REFRESH`. SAME PR #61 sigue OPEN/Ready/mergeable, head `aef1cd0b1a26be327e561f344d63dae5d8def7ef`, pero su base snapshot es `58a6bf614...` y el baseline vivo avanzó a `7de7b57a...` por #60. El CI verde previo queda como evidencia histórica, no autoriza merge de la combinación nueva; WOZ debe refrescar SAME #61 + exact-head CI.
- **F4 / 21.1+21.2:** `[x]` PR #51. **24.1:** `[x]` PR #55. **24.2:** `[x]` PR #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. PR #60 exact head `945638c8bb650b0ce0bbe569e48a791a93d80e39` pasó F4 matrix `33265800007`, D6 `33265800004`, D7 `33265800022`, Desktop Portability `33265800008` y fue integrada como `7de7b57a508b3cf05cbded81501fbd3da63922a3`. Este merge **no** convierte `NOT_COVERED`, `PENDING_EXTERNAL` o `PRODUCT_FINDING` en PASS; siguen faltando journeys funcionales explícitos y tails de runner/hardware iPhone, YouTube/billing donde apliquen, signing/notarization y 25.2.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 012

### AAA — `NIGHT-AAA-013` — F2 / 12.1 atomic empty-index vertical slice
La asignación anterior quedó correctamente `BLOCKED`, no fallida. JOBS amplía ownership de esta pieza al control plane/backend: duplicate-check backend-wide; reutilizar primitive existente si hay equivalente; si no existe, implementar el mínimo create-if-absent/CAS/idempotent/fail-closed server-side y cablearlo al Web. Debe probar concurrencia, retry/idempotencia y fallo parcial. No pagination/window/memory/cold-warm ni D13–D15.

### BBB — `NIGHT-BBB-013` — F4 / 25.1 functional coverage residual
PR #60 ya está integrada. BBB conserva ownership exclusivo de los gaps dependency-safe de 25.1: usar la matriz integrada como lista de verdad y cerrar **un slice automatizable real** de journeys core Web/Desktop mediante harnesses existentes, sin inventar iPhone, signing, notarization, billing/YouTube externos ni absorber bugs F2/F3. Findings de producto se reportan, no se roban.

### WOZ — `NIGHT-WOZ-013` — F3 / 16.2 SAME #61 refresh transaction
REUSE-FIRST exclusivamente SAME #61. Refrescar su branch sobre `7de7b57a...` preservando solo el delta F3/16.2; exigir CI aplicable exact-head nuevo y merge protegido con expected-head solo si el race-check sigue válido. Tras merge, reclamar únicamente `SOFTWARE DONE / EXTERNAL TAIL`; no staging/prod físicos ni Stripe.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 012

1. **F2 / 12.1 atomic bootstrap:** es el blocker interno más duro porque el frontend no puede satisfacer atomicidad sin autoridad de control plane. El siguiente movimiento correcto es el primitive backend + wire Web, no otro intento pin-only.
2. **F3 / 16.2:** #61 conserva valor inmediato, pero necesita refresh exact-head tras #60. Integrarla reduce F3 a tails físicos + D17–D20.
3. **F4 / 25.1:** el artifact de matriz ya está integrado; ahora el valor está en convertir `NOT_COVERED` dependency-safe en evidencia funcional real, sin falsear hardware/proveedor externo.
4. **F0/F1:** no usar workers en pruebas repetidas: los gaps activos son externos/RO.

Las asignaciones se recalcularon, no se conservaron por inercia: AAA recibe alcance nuevo porque su auditoría demostró el blocker de autoridad; BBB abandona la transacción #60 ya cerrada y pasa al residual funcional; WOZ permanece en #61 únicamente porque GitHub demuestra que es el candidate único todavía abierto y stale por el merge previo.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; **#60 → `7de7b57a508b3cf05cbded81501fbd3da63922a3`**.

Candidate vivo: **#61 @ `aef1cd0b...` OPEN/mergeable pero stale respecto al baseline `7de7b57a...`; refresh + exact-head CI requerido antes de merge**.

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

**AAA:** `NIGHT-AAA-013` atomic empty-index con scope ampliado explícitamente a control plane/backend + Web wire.  
**BBB:** `NIGHT-BBB-013` 25.1 residual funcional dependency-safe sobre la matriz ya integrada.  
**WOZ:** `NIGHT-WOZ-013` SAME #61 refresh + exact-head CI + protected merge si corresponde.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 012; GitHub prevalece si cambia después de este commit.
