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

## Estado vivo — NIGHT-JOBS-011

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 58a6bf61441f08bf68aa63673c0d5f2994b220d9`, merge verificable de PR #58.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. No consumir workers técnicos en duplicados.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO. No repetir drills aceptados.
- **F2 / 11.1:** `[x]` PR #47. **11.2:** `[x]` PR #54. **12.2:** `[x]` PR #50.
- **F2 / 12.1:** `[ 🟡 ] IN PROGRESS`. PR #58 ya **MERGED** como `58a6bf614...`; cerró solo slice A (lazy artwork + taxonomía mínima + startup timing/tests). Atomic empty-index es el siguiente slice y ya existe una sola successor branch `aaa/night-12.1-atomic-empty-index`, sin implementación/PR/CI aún.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado; separación física staging/prod sigue externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE CANDIDATE GREEN` — SAME PR #61 OPEN/Ready/mergeable, exact head `aef1cd0b1a26be327e561f344d63dae5d8def7ef`, base `58a6bf614...`; D6 `33266547956`, temp-auth `33266548019`, D7 `33266548050`, Desktop Portability `33266547963` SUCCESS. No merge aún.
- **F4 / 21.1+21.2:** `[x]` PR #51. **24.1:** `[x]` PR #55. **24.2:** `[x]` PR #57.
- **F4 / 25.1:** `[ 🟡 ] SOFTWARE CANDIDATE GREEN` — SAME PR #60 OPEN/Ready/mergeable, exact head `945638c8bb650b0ce0bbe569e48a791a93d80e39`, base `58a6bf614...`; F4 matrix `33265800007`, D6 `33265800004`, D7 `33265800022`, Desktop Portability `33265800008` SUCCESS. No merge aún; matrix gaps honestos siguen abiertos.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 011

### AAA — `NIGHT-AAA-012` — F2 / 12.1 atomic empty-index
Continuar solo la successor branch existente. Auditar primitives; implementar delta mínimo atómico/idempotente/fail-closed; cubrir race/retry/error parcial; tests + CI exact-head. No pagination/window/memory ni cold/warm residual.

### BBB — `NIGHT-BBB-012` — F4 / 25.1 SAME #60
Race-check e integrar #60 si integration/head siguen exactamente compatibles con el CI verde. Si AAA mueve baseline antes, refresh SAME #60 + CI nuevo. No 25.2/signing/notarization/release.

### WOZ — `NIGHT-WOZ-012` — F3 / 16.2 SAME #61
Race-check e integrar #61 si la combinación sigue válida; si BBB/AAA mueve baseline, refresh SAME #61 + CI nuevo. Tras merge solo `SOFTWARE DONE / EXTERNAL TAIL`. Si integra y queda tiempo, solo audit READ-ONLY REUSE-FIRST de 17.1; no Stripe resources ni implementación.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Camino crítico global — recalculado desde cero CYCLE 011

1. **F2:** atomic empty-index es el siguiente trabajo interno listo; después quedan pagination/window/memory + cold/warm y D13–D15.
2. **F4:** #60 tiene el mayor retorno inmediato: candidate exact-head verde listo para transacción de integración; después quedan gaps funcionales reales + 25.2 y tails de signing/notarization.
3. **F3:** #61 también está exact-head verde; integrarlo cierra el contrato software 16.2 y deja explícitos los tails físicos. Después D17–D20 constituyen el mayor volumen global, con dependencias Stripe/DNS/legal/provider en varias piezas.
4. **F0/F1:** no usar workers en pruebas repetidas: los gaps activos son externos/RO.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; **#58 → `58a6bf61441f08bf68aa63673c0d5f2994b220d9`**.

Candidates vivos: **#60 @ `945638c8...` GREEN**, **#61 @ `aef1cd0b...` GREEN**. Ninguno se considera integrado hasta que GitHub lo demuestre.

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

**AAA:** `NIGHT-AAA-012` atomic empty-index only.  
**BBB:** `NIGHT-BBB-012` SAME #60 race-check/merge; refresh+CI si cambió baseline.  
**WOZ:** `NIGHT-WOZ-012` SAME #61 race-check/merge; luego solo read-only 17.1 readiness si se integra.  
**PLAN_HEALTH:** sincronizado a GitHub vivo CYCLE 011; GitHub prevalece si cambia después de este commit.
