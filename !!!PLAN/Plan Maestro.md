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

## Estado vivo

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `672e133bc9cb8a47a29d4b34e13fc535290e5681`, versión `0.8.0-alpha.1`.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS` — Issue #41 `5455677550` + Required CI/compile/cross-process verdes.
- **D7:** `[x] / PASS` — PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; Issue #41 `5457172823`.
- **D8:** `[x] / PASS` — PRs #49/#52/#53 integrados; Gate Issue #41 `5460381842`.
- **D9:** `[x] / PASS` — REUSE-FIRST Issue #41 `5460959369`.
- **D10.1:** `[ 🟡 ] / PENDING` — restore/RPO/RTO/core flows PASS; `NIGHT-WOZ-005` produjo PR #56 exact head `0abe39e096d10d992764a2d24874e46529109a70`. Strategy config+índice/media y backup-failure condition/routing están PASS en candidate; Test - Desktop Portability `33250824435`, D7 `33250824401`, D6 `33250824418` y compile `33250824441` SUCCESS. Único blocker literal restante: evidencia de copia real fuera del primary provider/account failure domain. `NIGHT-WOZ-006` debe integrar #56 sin repetir drills.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54 exact head `e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; Required CI `33239731204` SUCCESS; merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`; Issue #41 `5461257322`.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — `NIGHT-AAA-005` produjo commit `51232744a6cd4bc2af67de901e09beb70c91f4fc` retirando eager artwork hydration. Taxonomy observable, startup instrumentation, tests/CI y atomic empty-index siguen abiertos; AAA continúa `NIGHT-AAA-006` en la misma rama.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51 exact tested head `0fd9bee8117ca92fb9f713f0d55089f5707a2917`; merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`; Issue #41 `5461557463`.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55 exact head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`. Publication remains fail-closed; signing/notarization not bypassed.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-006`

AAA conserva 12.1. `NIGHT-AAA-005` produjo progreso productivo en `aaa/night-12.1-bootstrap-load @ 51232744...`: artwork dejó de hidratarse eager durante la carga inicial. `NIGHT-AAA-006` completa taxonomy + startup instrumentation + tests + exact-head candidate en esa misma lineage. Atomic empty-index permanece requisito posterior de 12.1.

### BBB — F4 / 24.2 — `NIGHT-BBB-006`

24.1 quedó integrado por PR #55. BBB avanza explícitamente a 24.2 porque es dependency-safe mientras D22/D23 siguen condicionados por signing/notarization externos.

Scope 24.2: REUSE-FIRST de updater N-1, fallos red/disco/firma/manifest, recovery/rollback y retiro/comunicación de artefacto malo. No publicar stable/latest ni inventar certificados.

### WOZ — F1 / D10.1 — `NIGHT-WOZ-006`

PR #56 `0abe39e...` contiene el artifact mínimo de backup readiness y ya tiene exact-head CI aplicable verde. WOZ debe hacer race-check + integración si sigue compatible con baseline `672e133...`, dejar D10.1 PENDING únicamente por off-provider proof real y STOP. No repetir PITR/cutover/restart/migrations/rotation ni iniciar D10.2/F3 bajo este Assignment ID.

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

Candidate pendiente:
9. #56 / WOZ / D10.1 artifact → exact head `0abe39e...`; exact-head CI aplicable verde; falta integración owner-authorized.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head correspondiente.

## Camino crítico global

- **F0:** solo tails externos/release; no bloquear trabajo interno.
- **F1:** D10.1 está reducido a off-provider proof externo + integración #56; D10.2 requiere decisión alpha RO.
- **F2:** 12.1 es foundation real abierto; después quedan 13.x, 14.x, 15.x.
- **F3:** D16–D20 siguen abiertos y constituyen el mayor volumen restante; Stripe/DNS/legal/producción pueden requerir credenciales/acciones externas. WOZ debe moverse a F3 en un ciclo posterior si D10.1 queda external-only integrado.
- **F4:** 21.x + 24.1 cerrados; 24.2 activo en paralelo mientras signing/notarization externos limitan 22.x/23.x.

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

**AAA:** `NIGHT-AAA-006` → F2/12.1 completar corrective slice A en misma rama + exact-head evidence.  
**BBB:** `NIGHT-BBB-006` → F4/24.2 updater recovery/rollback, REUSE-FIRST.  
**WOZ:** `NIGHT-WOZ-006` → integrar PR #56 exact-head y dejar D10.1 external-only factual.  
**PLAN_HEALTH:** sincronizado al baseline BeatGaler `672e133bc9cb8a47a29d4b34e13fc535290e5681`; ningún gate externo fue rebajado ni checkbox adelantado.
