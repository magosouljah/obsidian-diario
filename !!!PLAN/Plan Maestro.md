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

## Estado vivo — NIGHT-JOBS-007

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `f0d65aa66988e3e1a026e237b65c65a56b098aa9`, versión `0.8.0-alpha.1`, confirmado en el preflight del ciclo 007; ninguno de #57/#58/#59 estaba aún merged.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS` — Issue #41 `5455677550` + Required CI/compile/cross-process verdes.
- **D7:** `[x] / PASS` — PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; Issue #41 `5457172823`.
- **D8:** `[x] / PASS` — PRs #49/#52/#53 integrados; Gate Issue #41 `5460381842`.
- **D9:** `[x] / PASS` — REUSE-FIRST Issue #41 `5460959369`.
- **D10.1:** `[ 🟡 ] / PENDING_EXTERNAL_PROOF` — restore/RPO/RTO/core flows PASS; PR #56 integró strategy config+índice/media y backup-failure condition/routing. Merge `f0d65aa66988e3e1a026e237b65c65a56b098aa9`. Único blocker literal restante: copia real fuera del primary provider/account failure domain + read/checksum verification. No repetir drills aceptados.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54 exact head `e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; Required CI `33239731204` SUCCESS; merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — PR #58 `aaa/night-12.1-bootstrap-load` OPEN/Ready/mergeable=true, exact head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`, base `f0d65aa...`; Required CI `33254699647` SUCCESS. Candidate cubre lazy artwork + taxonomy mínima + startup timing/tests del slice A, **no** atomic empty-index ni paginación/ventana/memory/cold-warm residual. `NIGHT-AAA-008` ordena race-check/merge y luego atomic empty-index como único siguiente sub-slice.
- **F3 / 16.1:** `[ 🟡 ] / IN PROGRESS + EXTERNAL TAIL` — PR #59 OPEN/Ready/mergeable=true, exact head `292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`, base `f0d65aa...`; D6 `33256145573`, D7 `33256145614` y compile `33256145521` SUCCESS. Test - Desktop Portability `33256145531` estaba IN_PROGRESS al último preflight. Contrato software dependency-safe candidate; separación física staging/prod sigue PENDING_EXTERNAL. `NIGHT-WOZ-008` cierra #59 solo si exact-head final PASS y después inicia 16.2 software-only.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51 merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55 merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.
- **F4 / 24.2:** `[ 🟡 ] / READY FOR OWNER MERGE` — PR #57 refreshed exact head `4e251cae84ff55116c89c8398e78f04aecb78e3c` sobre base `f0d65aa...`; GitHub reporta OPEN/Ready/mergeable=true; Required CI exact-head SUCCESS; D6 `33255401544` SUCCESS; D7 `33255401512` SUCCESS. `NIGHT-BBB-008` exige race-check + merge protegido y luego 25.1 matrix audit dependency-safe.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-008`

AAA conserva 12.1. Debe reutilizar PR #58; si exact head/base/checks permanecen válidos, race-check + merge protegido. Después inicia únicamente **atomic empty-index** como siguiente sub-slice, con duplicate-check, un candidate, tests y exact-head. No mezcla pagination/window/memory ni cold/warm residual en 008.

### BBB — F4 / 24.2 → 25.1 — `NIGHT-BBB-008`

BBB conserva PR #57. El refreshed head `4e251cae...` ya tiene Required CI/D6/D7 verdes contra baseline `f0d65aa...`; debe race-check y mergear solo si la combinación no cambió. Después inicia 25.1 como REUSE-FIRST matrix audit dependency-safe, separando cobertura automatizada de blockers físicos/externos. No signing/notarization/release/25.2.

### WOZ — F3 / 16.1 → 16.2 — `NIGHT-WOZ-008`

WOZ conserva F3 16.x. Debe finalizar la evidencia exact-head de #59 y mergear únicamente si Desktop Portability/Required CI aplicable queda verde y la combinación sigue vigente. La separación física staging/prod permanece externa. Después avanza 16.2 software-only: pipeline/promoción reproducible, origins/TLS/headers/fail-closed y smoke/rollback fixtures sin crear infraestructura/costo ni ejecutar deploy real.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. No mergea código BeatGaler ni modifica infraestructura. Secuencia, exige evidencia, sincroniza el plan y reasigna explícitamente.

## Secuencia de integración — estado actual

Completado y verificado:
1. #49 / WOZ / 8.1 → `14002b29...`.
2. #47 / AAA / 11.1 → `489d81b...`.
3. #52 / WOZ / 8.2 → `c25ec6a...`.
4. #50 / AAA / 12.2 → `39e894c...`.
5. #53 / WOZ / D8 RO resolutions → `6c4499d...`; D8 PASS.
6. #54 / AAA / 11.2 → `3560dc844...`.
7. #51 / BBB / 21.1+21.2 → `5b05ca845...`.
8. #55 / BBB / 24.1 → `672e133bc...`.
9. #56 / WOZ / D10.1 artifact → merge `f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

Candidates pendientes:
10. #57 / BBB / 24.2 → refreshed head `4e251cae...`, exact-base CI verde; owner race-check/merge pendiente.
11. #58 / AAA / 12.1 slice A → head `d7cc93f...`, Required CI verde; owner race-check/merge pendiente.
12. #59 / WOZ / 16.1 software contract → head `292a7706...`, D6/D7/compile verdes; Desktop Portability final pendiente al último preflight.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head correspondiente.

## Camino crítico global — recalculado CYCLE 007

- **F0:** solo tails externos/release; no bloquear trabajo interno.
- **F1:** D10.1 reducido a un proof externo off-provider; D10.2 requiere decisión alpha RO. No consumir worker técnico repitiendo evidencia aceptada.
- **F2:** integrar #58 primero; después atomic empty-index. Pagination/window/memory + cold/warm siguen abiertos; 13.x–15.x permanecen volumen posterior.
- **F3:** cerrar el candidate software #59 sin falsear physical staging/prod; luego 16.2 dependency-safe. D17–D20 siguen el mayor volumen global y varios tramos requerirán Stripe/DNS/legal/provider credentials.
- **F4:** integrar #57 porque ya tiene exact-head CI verde; después reducir 25.1 por REUSE-FIRST. D22/D23 permanecen externos por signing/notarization.

## REUSE-FIRST F1 D9/D10

Reutilizar cuando satisfaga literalmente: PostgreSQL autoridad, migrations/versionado/constraints, importer/idempotencia/rollback, durabilidad/restart, fail-closed, PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority. No repetir drills solo para recrear evidencia.

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

**AAA:** `NIGHT-AAA-008` → #58 race-check/merge; luego atomic empty-index únicamente.  
**BBB:** `NIGHT-BBB-008` → #57 race-check/merge; luego F4/25.1 matrix audit dependency-safe.  
**WOZ:** `NIGHT-WOZ-008` → #59 exact-head closure; luego F3/16.2 software-only.  
**PLAN_HEALTH:** sincronizado al preflight CYCLE 007; GitHub real sigue prevaleciendo si cualquiera de #57/#58/#59 cambia después de este commit.
