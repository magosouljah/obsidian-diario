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

## Estado vivo — NIGHT-JOBS-009

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`, merge verificable de PR #59.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS`.
- **D7:** `[x] / PASS`.
- **D8:** `[x] / PASS`.
- **D9:** `[x] / PASS`.
- **D10.1:** `[ 🟡 ] / PENDING_EXTERNAL_PROOF` — único blocker literal: copia real fuera del primary provider/account failure domain + read/checksum verification. No repetir drills aceptados.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — PR #58 sigue OPEN con head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`; no existe resultado verificable de `NIGHT-AAA-009` y la combinación vieja quedó invalidada por los avances de integración hasta `be9e58c...`. `NIGHT-AAA-010` ordena refrescar la MISMA PR contra baseline vivo, obtener CI aplicable y mergear solo si queda verde. Atomic empty-index empieza únicamente después de integración verificable de #58.
- **F3 / 16.1:** `[ 🟡 ] / SOFTWARE DONE + EXTERNAL TAIL` — PR #59 exact head `0e0bf188ceb298c5c6846e56576665b50a69e922` quedó integrado como `be9e58c9edc0bb40742e0b91e3f2ebe771ace502`, con parents exactos `f73c9ee...` + `0e0bf188...`. Health/readiness/dependency checks, graceful shutdown, timeouts y proxy trust están DONE/INTEGRATED. Separación física staging/prod permanece `PENDING_EXTERNAL`.
- **F3 / 16.2:** `[ 🟡 ] / IN PROGRESS SOFTWARE-ONLY` — `NIGHT-WOZ-010`; promoción reproducible, origins/TLS/headers fail-closed y smoke/rollback fixtures sin provider resources/costo/deploy real.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55.
- **F4 / 24.2:** `[x] / DONE / INTEGRATED` — PR #57.
- **F4 / 25.1:** `[ 🟡 ] / IN PROGRESS` — PR #60 head `28d9e3819e528ae5ed23435ad39d20ef6c14641b`. F4 25.1 matrix `33260592877`, D6 `33260592860` y D7 `33260592764` SUCCESS, pero **Desktop Portability `33260592774` FAILURE**; además #60 quedó stale tras #59. `NIGHT-BBB-010` exige SAME PR diagnosis + refresh + exact-head CI; no merge mientras un gate aplicable falle.
- **5.1:** `[x]`.
- **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-010`

AAA conserva 12.1. Debe reutilizar exclusivamente PR #58, refrescarla sobre `be9e58c...`, obtener Required CI/merge-candidate aplicable y hacer race-check/merge protegido solo con evidencia verde. No duplicate. Atomic empty-index empieza únicamente tras merge verificable; pagination/window/memory y cold/warm residual quedan fuera de 010.

### BBB — F4 / 25.1 — `NIGHT-BBB-010`

BBB conserva 25.1 y la MISMA PR #60. Debe diagnosticar `Test - Desktop Portability 33260592774` FAILURE, refrescar sobre `be9e58c...`, corregir únicamente el delta F4 mínimo y exigir CI nuevo. Si el fallo corresponde a producto F2/F3, se registra `PRODUCT_FINDING` y no se roba ownership. No 25.2, signing/notarization ni release.

### WOZ — F3 / 16.2 — `NIGHT-WOZ-010`

WOZ procesó #59 correctamente; no reabre 16.1 runtime. Pasa a 16.2 software-only/dependency-safe: auditar/reutilizar deploy assets, contrato PR→preview→staging→production, mismo SHA, origins/TLS/headers fail-closed y smoke/rollback. Sin nueva infraestructura/costo ni deploy real; physical staging/prod sigue externo.

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

Candidates pendientes:
12. #58 / AAA / 12.1 slice A → stale; refresh SAME PR contra `be9e58c...` + CI aplicable requerido.
13. #60 / BBB / 25.1 matrix → exact head `28d9e381...`; matrix/D6/D7 verdes pero Desktop Portability failure y stale base; SAME PR repair/refresh requerido.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head/combinación correspondiente.

## Camino crítico global — recalculado CYCLE 009

- **F0:** solo tails externos/release; no consumir workers técnicos en duplicados.
- **F1:** D10.1 reducido a proof externo off-provider; D10.2 requiere decisión alpha RO. No repetir evidencia aceptada.
- **F2:** refrescar/integrar #58; después atomic empty-index. Pagination/window/memory + cold/warm siguen abiertos; 13.x–15.x permanecen volumen posterior.
- **F3:** 16.1 runtime software ya integrado. El camino interno inmediato es 16.2 software-only; physical separation sigue externa. Después D17–D20 siguen siendo el mayor volumen global y varios tramos requieren Stripe/DNS/legal/provider credentials.
- **F4:** 24.2 cerrado. 25.1 tiene candidate útil pero no pasa todos los gates: arreglar #60 sin ensuciar F2/F3. D22/D23 permanecen externos por signing/notarization.

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

**AAA:** `NIGHT-AAA-010` → SAME #58 refresh sobre `be9e58c...` + exact-head/merge-candidate CI + merge; luego atomic empty-index únicamente.  
**BBB:** `NIGHT-BBB-010` → SAME #60, diagnosticar portability failure, refresh/fix mínimo + CI completo; no merge con gate rojo.  
**WOZ:** `NIGHT-WOZ-010` → F3/16.2 software-only REUSE-FIRST; physical staging/prod queda external.  
**PLAN_HEALTH:** sincronizado al preflight CYCLE 009; GitHub real prevalece si cambia después de este commit.
