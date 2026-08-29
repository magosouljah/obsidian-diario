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

## Estado vivo — NIGHT-JOBS-008

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `f73c9ee8d058df3c780170c8c2a3fabef975c54d`, merge verificable de PR #57.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS`.
- **D7:** `[x] / PASS`.
- **D8:** `[x] / PASS`.
- **D9:** `[x] / PASS`.
- **D10.1:** `[ 🟡 ] / PENDING_EXTERNAL_PROOF` — único blocker literal: copia real fuera del primary provider/account failure domain + read/checksum verification. No repetir drills aceptados.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — PR #58 sigue OPEN/Ready/mergeable, head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`, pero quedó stale frente al baseline `f73c9ee...`. El intento anterior fue bloqueado correctamente porque el merge-candidate no tenía Required CI. `NIGHT-AAA-009` ordena refrescar la MISMA PR contra baseline vivo, obtener exact-head/merge-candidate CI aplicable y mergear solo si queda verde. Atomic empty-index empieza únicamente después de integración verificable de #58.
- **F3 / 16.1:** `[ 🟡 ] / SOFTWARE CANDIDATE READY + EXTERNAL TAIL` — PR #59 OPEN/Ready/mergeable, base vivo `f73c9ee...`, head `0e0bf188ceb298c5c6846e56576665b50a69e922`; Test - Desktop Portability `33258609802`, D6 `33258609811`, D7 `33258609799` y temp-auth compile `33258609793` SUCCESS. `NIGHT-WOZ-009` ordena race-check/merge protegido. Separación física staging/prod sigue PENDING_EXTERNAL aun después del merge. Luego 16.2 software-only.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55.
- **F4 / 24.2:** `[x] / DONE / INTEGRATED` — PR #57 exact head `4e251cae84ff55116c89c8398e78f04aecb78e3c`; Test - Desktop Portability/Required CI `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee8d058df3c780170c8c2a3fabef975c54d`.
- **F4 / 25.1:** `[ 🟡 ] / IN PROGRESS` — audit REUSE-FIRST de BBB confirmó cobertura reutilizable amplia; faltan matriz funcional explícita cross-OS/browser, iPhone, YouTube y billing. `NIGHT-BBB-009` limita el trabajo a un único matrix/runner dependency-safe reutilizando harnesses existentes; hardware/credentials externos permanecen separados.
- **5.1:** `[x]`.
- **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-009`

AAA conserva 12.1. Debe refrescar exclusivamente PR #58 sobre `f73c9ee...`, obtener Required CI aplicable a la combinación vigente y hacer race-check/merge protegido solo con evidencia verde. No abrir duplicate. Atomic empty-index comienza únicamente tras merge verificable; pagination/window/memory y cold/warm residual quedan fuera de 009.

### BBB — F4 / 25.1 — `NIGHT-BBB-009`

BBB pasa de 24.2 cerrado a 25.1. Debe reutilizar los harnesses ya inventariados y construir únicamente una matriz/runner F4 dependency-safe que componga cobertura existente y haga explícitos los gaps. No modifica producto F2/F3. iPhone/hardware/credenciales reales quedan PENDING_EXTERNAL si no pueden ejecutarse.

### WOZ — F3 / 16.1 → 16.2 — `NIGHT-WOZ-009`

WOZ conserva F3 16.x. #59 ya tiene exact-head CI aplicable verde sobre el refreshed head `0e0bf188...`; debe race-check y merge protegido si base/head siguen vigentes. Después avanza 16.2 software-only: promoción reproducible, origins/TLS/headers fail-closed y smoke/rollback fixtures, sin crear infraestructura/costo ni deploy real.

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

Candidates pendientes:
11. #58 / AAA / 12.1 slice A → stale base; refresh same PR + exact-head/merge-candidate Required CI requerido.
12. #59 / WOZ / 16.1 software contract → head `0e0bf188...`, exact-head workflows verdes; owner race-check/merge pendiente.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head/combinación correspondiente.

## Camino crítico global — recalculado CYCLE 008

- **F0:** solo tails externos/release; no bloquear trabajo interno.
- **F1:** D10.1 reducido a proof externo off-provider; D10.2 requiere decisión alpha RO. No consumir worker técnico repitiendo evidencia aceptada.
- **F2:** refrescar/integrar #58; después atomic empty-index. Pagination/window/memory + cold/warm siguen abiertos; 13.x–15.x permanecen volumen posterior.
- **F3:** integrar #59 con CI ya verde si race-check se mantiene; luego 16.2 dependency-safe. D17–D20 siguen el mayor volumen global y varios tramos requerirán Stripe/DNS/legal/provider credentials.
- **F4:** 24.2 ya cerrado. 25.1 debe convertir el audit existente en matriz/runner reutilizable y separar evidencia interna de hardware/credenciales externas. D22/D23 permanecen externos por signing/notarization.

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

**AAA:** `NIGHT-AAA-009` → refresh #58 sobre baseline vivo + exact-head/merge-candidate CI + merge; luego atomic empty-index únicamente.  
**BBB:** `NIGHT-BBB-009` → F4/25.1 matrix/runner dependency-safe reutilizando harnesses existentes.  
**WOZ:** `NIGHT-WOZ-009` → #59 race-check/merge; luego F3/16.2 software-only.  
**PLAN_HEALTH:** sincronizado al preflight CYCLE 008; GitHub real prevalece si cambia después de este commit.
