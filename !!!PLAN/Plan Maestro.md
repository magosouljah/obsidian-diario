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
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `f0d65aa66988e3e1a026e237b65c65a56b098aa9`, versión `0.8.0-alpha.1`.
- **F0:** trabajo técnico necesario para avanzar cerrado; 1.2 y 2.2 conservan tails externos. F0 no recibe `[x]` global todavía.
- **D6:** `[x] / PASS` — Issue #41 `5455677550` + Required CI/compile/cross-process verdes.
- **D7:** `[x] / PASS` — PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; Issue #41 `5457172823`.
- **D8:** `[x] / PASS` — PRs #49/#52/#53 integrados; Gate Issue #41 `5460381842`.
- **D9:** `[x] / PASS` — REUSE-FIRST Issue #41 `5460959369`.
- **D10.1:** `[ 🟡 ] / PENDING_EXTERNAL_PROOF` — restore/RPO/RTO/core flows PASS; PR #56 exact head `0abe39e096d10d992764a2d24874e46529109a70` integró strategy config+índice/media y backup-failure condition/routing con Test - Desktop Portability `33250824435`, D7 `33250824401`, D6 `33250824418` y compile `33250824441` SUCCESS. Merge `f0d65aa66988e3e1a026e237b65c65a56b098aa9`. Único blocker literal restante: copia real fuera del primary provider/account failure domain + read/checksum verification. No repetir drills aceptados.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47 merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **F2 / 11.2:** `[x] / DONE / INTEGRATED` — PR #54 exact head `e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; Required CI `33239731204` SUCCESS; merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`; Issue #41 `5461257322`.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50 merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`.
- **F2 / 12.1:** `[ 🟡 ] / IN PROGRESS` — rama `aaa/night-12.1-bootstrap-load` avanzó a `d7cc93f9c4318be7f993bd033483c4e7f1834a55`: lazy artwork + taxonomy mínima + startup timing + tests añadidos. Ejecución real de tests/CI exact-head sigue UNVERIFIED; no hay PR todavía; atomic empty-index permanece posterior.
- **F3 / 16.1:** `[ 🟡 ] / ASSIGNED` — `NIGHT-WOZ-007`. WOZ fue liberado de D10.1 técnico y reasignado explícitamente a auditar/completar el slice dependency-safe de entornos/operabilidad REUSE-FIRST, sin crear infraestructura/costo no autorizado.
- **F4 / 21.1+21.2:** `[x] / DONE / INTEGRATED` — PR #51 exact tested head `0fd9bee8117ca92fb9f713f0d55089f5707a2917`; merge `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`; Issue #41 `5461557463`.
- **F4 / 24.1:** `[x] / DONE / INTEGRATED` — PR #55 exact head `ba83c87dab8a56163601e913f7764c7f8682b7a6`; Required CI `33248059804`, F4 Release Controls `33248059891`, D6 `33248059823`, D7 `33248059990` SUCCESS; merge `672e133bc9cb8a47a29d4b34e13fc535290e5681`.
- **F4 / 24.2:** `[ 🟡 ] / IN PROGRESS` — PR #57 head histórico `5c74c0948c43d53b2f8d075cd66ba70c953da3c5` tiene Test - Desktop Portability `33252718637`, D6 `33252718614` y D7 `33252718625` SUCCESS; pero fue construido contra `672e133...`. Integración avanzó a `f0d65aa...`, así que debe refrescarse y obtener CI exact-head nuevo antes de merge.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### AAA — F2 / 12.1 — `NIGHT-AAA-007`

AAA conserva 12.1 y la misma lineage `aaa/night-12.1-bootstrap-load`. `NIGHT-AAA-006` produjo `d7cc93f...` con taxonomy + timing + tests, pero sin ejecución/CI/PR verificables. `NIGHT-AAA-007` debe cerrar el corrective slice A: ejecutar/corregir tests, refresh mínimo contra `f0d65aa...` si corresponde, producir/reutilizar un único PR y obtener CI exact-head. Si no logra evidencia verificable y no existe blocker externo, debe reportar `STALLED`. Atomic empty-index sigue como siguiente sub-slice, no se mezcla por conveniencia.

### BBB — F4 / 24.2 — `NIGHT-BBB-007`

BBB conserva PR #57. El candidate histórico `5c74c094...` ya tiene CI aplicable verde, pero el baseline cambió por #56. `NIGHT-BBB-007` ordena refresh mínimo de la misma PR contra `f0d65aa...`, nuevo exact-head CI y, solo si queda verde/Ready/mergeable, race-check + merge protegido. No nueva PR; no signing/notarization/public release.

### WOZ — F3 / 16.1 — `NIGHT-WOZ-007`

Cambio de owner/área explícito: D10.1 quedó external-only y WOZ pasa a F3. Debe auditar REUSE-FIRST assets/runtime existentes y avanzar 16.1 únicamente donde sea dependency-safe: health/readiness/dependency checks, graceful shutdown, timeouts, proxy trust y separación contractual de entornos. No crear nueva RDS/infra pagada/cuentas/provider resources sin aprobación RO. Si staging separado requiere credencial/decisión externa, reducirlo a blocker literal sin falsear PASS.

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
9. #56 / WOZ / D10.1 artifact → exact tested head `0abe39e...`; merge `f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

Candidates pendientes:
10. #57 / BBB / 24.2 → head histórico `5c74c094...`, CI verde sobre base `672e133...`; refresh + nuevo exact-head CI requerido contra baseline vivo.
11. AAA / 12.1 → branch `d7cc93f...`, sin PR/CI exact-head todavía.

**Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head correspondiente.

## Camino crítico global

- **F0:** solo tails externos/release; no bloquear trabajo interno.
- **F1:** D10.1 está reducido a un único proof externo off-provider; D10.2 requiere decisión alpha RO. No consumir worker técnico repitiendo evidencia aceptada.
- **F2:** 12.1 es foundation interno abierto y debe convertirse ya en candidate verificable; después quedan 13.x, 14.x y 15.x.
- **F3:** D16–D20 siguen abiertos y constituyen el mayor volumen restante. WOZ inicia 16.1 dependency-safe ahora; Stripe/DNS/legal/recursos separados pueden requerir credenciales/acciones externas.
- **F4:** 21.x + 24.1 cerrados; 24.2 es el cierre interno más cercano pero necesita refresh exact-head. D22/D23 siguen externos por signing/notarization.

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

**AAA:** `NIGHT-AAA-007` → F2/12.1 cerrar candidate verificable en misma rama: tests + single PR + exact-head CI.  
**BBB:** `NIGHT-BBB-007` → F4/24.2 refrescar PR #57 contra `f0d65aa...`, CI exact-head y merge protegido si PASS.  
**WOZ:** `NIGHT-WOZ-007` → F3/16.1 REUSE-FIRST dependency-safe; no nueva infraestructura/costo sin RO.  
**PLAN_HEALTH:** sincronizado al baseline BeatGaler `f0d65aa66988e3e1a026e237b65c65a56b098aa9`; D10.1 no fue falsamente cerrado y ningún gate externo fue rebajado.
