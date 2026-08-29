# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por dependencia real, incluso cross-phase, pero cada agente conserva ownership estable de su pieza hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- No hay hopping automático entre tareas.
- JOBS puede reorganizar roadmap/owners, pero la reasignación debe ser explícita.
- JOBS no toca código/infra ni decide la solución técnica de WOZ.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-010

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`, merge verificable de PR #59. GitHub real seguía en este SHA durante preflight CYCLE 010.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS`.
- **D7:** `[x] / PASS`.
- **D8:** `[x] / PASS`.
- **D9:** `[x] / PASS`.
- **D10.1:** `[ 🟡 ] / PENDING_EXTERNAL_PROOF` — único blocker literal: copia real fuera del primary provider/account failure domain + read/checksum verification. No repetir drills aceptados.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — SAME PR #58 OPEN/Ready/mergeable, refreshed head `61e38f8a9c89aaa2e308e1e93bbbf4a7de22f741` sobre base exacta `be9e58c...`; Test - Desktop Portability `33262586452`, D6 `33262586456` y D7 `33262586450` terminaron SUCCESS. `NIGHT-AAA-011` ordena race-check + merge protegido si la combinación sigue intacta; si cambia baseline, refresh SAME PR + CI. Atomic empty-index solo después del merge verificable.
- **F3 / 16.1:** `[ 🟡 ] / SOFTWARE DONE + EXTERNAL TAIL` — PR #59 integrado como `be9e58c...`; runtime software DONE/INTEGRATED; separación física staging/prod permanece `PENDING_EXTERNAL`.
- **F3 / 16.2:** `[ 🟡 ] / SOFTWARE CANDIDATE GREEN` — SAME PR #61 OPEN/Ready/mergeable, head `d855b3d259626534650c1a78dae6df58f78cdcb9`; Test - Desktop Portability `33263815780`, D6 `33263815813`, D7 `33263815852` y temp-auth compile `33263815854` SUCCESS. `NIGHT-WOZ-011` integra solo con race-check/refresh exact-head. Deploy real/staging real continúa externo.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55.
- **F4 / 24.2:** `[x] / DONE / INTEGRATED` — PR #57.
- **F4 / 25.1:** `[ 🟡 ] / SOFTWARE CANDIDATE GREEN` — SAME PR #60 OPEN/Ready/mergeable, head `f8773d5f3f0a93d5e1a0a338cd3e5db6c1f574c4`; F4 matrix `33263350498`, D6 `33263350489`, D7 `33263350490` y Desktop Portability `33263350496` SUCCESS. El failure previo quedó diagnosticado/corregido sin tocar F2/F3. `NIGHT-BBB-011` hace race-check; si AAA mueve integration primero, refresh SAME #60 + CI nuevo antes de merge.
- **5.1:** `[x]`.
- **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-011`

AAA conserva 12.1 y exclusivamente SAME PR #58. Con exact-head CI verde sobre `be9e58c...`, debe race-check/merge protegido si la combinación sigue válida. Si integration cambia, refresh SAME lineage + CI aplicable. Tras merge, atomic empty-index únicamente; no pagination/window/memory ni cold/warm residual en 011.

### BBB — F4 / 25.1 — `NIGHT-BBB-011`

BBB conserva 25.1 y SAME PR #60. Candidate actual está verde sobre `be9e58c...`, pero AAA ejecuta antes; por tanto BBB debe revalidar baseline. Si cambió, refresh SAME #60 + CI exact-head. Integrar matrix no convierte `NOT_COVERED`/`PENDING_EXTERNAL` en PASS. No 25.2/signing/notarization/release.

### WOZ — F3 / 16.2 — `NIGHT-WOZ-011`

WOZ conserva 16.2 y SAME PR #61. Candidate actual está verde sobre `be9e58c...`, pero AAA/BBB ejecutan antes; revalidar baseline, refrescar SAME PR y exigir CI si la combinación cambió. Tras integración solo SOFTWARE DONE; physical staging/prod, provider/DNS/TLS y deploy/rollback reales siguen externos.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura.

## Secuencia de integración — estado actual

Completado y verificado:
1. #49 / WOZ / 8.1 → `14002b29...`.
2. #47 / AAA / 11.1 → `489d81b...`.
3. #52 / WOZ / 8.2 → `c25ec6a...`.
4. #50 / AAA / 12.2 → `39e894c...`.
5. #53 / WOZ / D8 → `6c4499d...`.
6. #54 / AAA / 11.2 → `3560dc844...`.
7. #51 / BBB / 21.1+21.2 → `5b05ca845...`.
8. #55 / BBB / 24.1 → `672e133bc...`.
9. #56 / WOZ / D10.1 artifact → `f0d65aa66988e3e1a026e237b65c65a56b098aa9`.
10. #57 / BBB / 24.2 → `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.
11. #59 / WOZ / 16.1 software runtime → `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`.

Candidates pendientes, los tres verdes sobre el mismo baseline al cierre CYCLE 010:
12. #58 / AAA / 12.1 slice A → head `61e38f8a...`; portability/D6/D7 SUCCESS; AAA ejecuta primero y puede integrar si exact-head/base siguen intactos.
13. #60 / BBB / 25.1 matrix → head `f8773d5...`; matrix/portability/D6/D7 SUCCESS; si #58 integra antes, refresh SAME PR + CI requerido.
14. #61 / WOZ / 16.2 software contract → head `d855b3d...`; portability/D6/D7/temp-auth compile SUCCESS; si #58/#60 cambian baseline, refresh SAME PR + CI requerido.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head/combinación correspondiente.

## Camino crítico global — recalculado CYCLE 010

- **F0:** solo tails externos/release; no consumir workers técnicos en duplicados.
- **F1:** D10.1 reducido a proof externo off-provider; D10.2 requiere decisión alpha RO. No repetir evidencia aceptada.
- **F2:** cerrar #58; después atomic empty-index. Pagination/window/memory + cold/warm siguen abiertos; 13.x–15.x permanecen volumen posterior.
- **F3:** 16.1 runtime software integrado; 16.2 tiene candidate verde. Cerrar software contract y preservar physical separation externa. Después D17–D20 siguen siendo el mayor volumen global y varios tramos requieren Stripe/DNS/legal/provider credentials.
- **F4:** 25.1 candidate ya reparado y verde. Integrar con race-check/refresh si cambia baseline; después 25.2 y gaps funcionales reales. D22/D23 siguen externos por signing/notarization.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementación interna oculta.
- Schema: **Galer T-Library Schema v2**.
- Web pura: sin Tauri ni Desktop helper.
- Media: device ↔ provider directo; Galer Cloud no relaya beats/proyectos.
- Permanent auth/control secrets quedan control-side; cliente usa temporary auth.
- Shared-bot es fallback solo cuando no hay bots libres; exclusividad por vault es camino normal.
- v1 no se publica free-only.
- YouTube debe existir en Desktop/Web; Web no llama Tauri.

## NEXT

**AAA:** `NIGHT-AAA-011` → SAME #58 exact-head race-check/merge; si baseline cambia, refresh + CI; luego atomic empty-index únicamente.  
**BBB:** `NIGHT-BBB-011` → SAME #60 race-check; probable refresh + CI si AAA integra primero; no 25.2.  
**WOZ:** `NIGHT-WOZ-011` → SAME #61 race-check; refresh + CI si baseline cambió por integraciones previas; tras merge solo SOFTWARE DONE, external tails preservados.  
**PLAN_HEALTH:** sincronizado al preflight CYCLE 010; GitHub real prevalece si cambia después de este commit.
