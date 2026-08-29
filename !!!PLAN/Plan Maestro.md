# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por **dependencia real**, incluso cross-phase, pero cada agente conserva **ownership estable de su área asignada** hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- **No hay hopping automático entre tareas.** Una vez asignado un owner, ese agente implementa/audita, corrige, prueba, ejecuta CI aplicable y entrega evidencia de su propia área.
- Findings previos de otros agentes se usan como input; no obligan a devolver el ownership al autor del finding.
- Revisión independiente adicional solo se asigna cuando JOBS/RO la pide explícitamente o un gate externo la exige.
- JOBS puede reorganizar roadmap/owners, pero una reasignación debe ser explícita y quedar en `!!!PLAN`/Issue #41.
- JOBS no toca código/infra ni decide la solución técnica de WOZ.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[x] / PASS` — WOZ Issue #41 `5457172823`; PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`; CI aplicable verde.
- **D8 / 8.1:** `[x] / DONE / INTEGRATED` — PR #49 exact tested head `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff`; merge `14002b29c5101232c0ca8f8b85d808c8214975fb`; WOZ handoff Issue #41 `5458273984`.
- **D8 / 8.2:** `[x] / DONE / INTEGRATED` — PR #52 refreshed exact tested head `f5ae901fb48444b6ea845048fb86f4dd482d75ec`; Required CI #443 `33219253446` SUCCESS; D6 #81 `33219253348` SUCCESS; D7 #53 `33219253320` SUCCESS; compile #171 `33219253332` SUCCESS; merge `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- **D8 decisiones RO:** `[x] / DONE / INTEGRATED` — PR #53 exact tested head `ab952c464f351aac736405c8559f5b85f421bc0c`; Required CI #455 `33234071878` SUCCESS; D6 #91 `33234071860` SUCCESS; D7 #65 `33234071863` SUCCESS; compile #175 `33234071871` SUCCESS; merge `6c4499d124a64d138e791ea4abf0091766dde7e9`.
- **Gate D8:** `[x] / PASS` — WOZ gate transaction Issue #41 `5460381842`. Provider/templates = Amazon SES; account deletion retention = 0 días sin tombstone recuperable; provider-only/OAuth-only reauth = autorización reciente del mismo provider ligada a usuario/sesión.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47 refreshed head `fdc6463e6b81efedc547c97595529d28e0ba2d83`; Required CI #429 `33216364174` SUCCESS; merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **F2 / 12.2:** `[x] / DONE / INTEGRATED` — PR #50 exact tested head `b7a31d686a361f559783b5dc7cb8bebc5aa04e8e`; Required CI #452 `33233250213` SUCCESS; D6 #89 `33233250229` SUCCESS; D7 #62 `33233250210` SUCCESS; compile #173 `33233250206` SUCCESS; merge `39e894c0fcefffa5d3222e3c135a086937a10a8e`; AAA handoff Issue #41 `5460303449`.
- **F4 / 21.1+21.2:** `[ 🟡 ] / PENDING` — PR #51 `bbb/task-21.2-upgrade-matrix` sigue OPEN/DRAFT. Exact head `e9fc4e68fc555357ee470996c51544b879cbae93` tuvo Required CI #451 `33220523143` SUCCESS, Upgrade Staging #8 `33220523159` SUCCESS, D6 #88 `33220523127` SUCCESS y D7 #61 `33220523155` SUCCESS sobre base `c25ec6a...`; esa evidencia ya no prueba integración porque el baseline canónico avanzó a `6c4499d...`. Requiere fresh union/rebase/refresh + exact-head CI/staging antes de integrar. PR #48 sigue OPEN/DRAFT y no se considera superseded/cerrado hasta que #51 aterrice.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### WOZ — D8 CERRADO / SIN NUEVA ASIGNACIÓN ACTIVA

WOZ cerró D8 mediante PRs #49, #52 y #53. Gate D8 = PASS por Issue #41 `5460381842`.

- D9 quedó **habilitado por dependencia**, pero **no está asignado automáticamente**.
- WOZ no inicia D9 hasta nueva asignación explícita JOBS/RO.
- No reabrir D6/D7/D8 sin nueva evidencia material.

### AAA — F2 / 12.2 CERRADO / SIN NUEVA ASIGNACIÓN ACTIVA

AAA cerró 12.2 mediante PR #50 e hizo handoff `STATUS: DONE` en Issue #41 `5460303449`.

- AAA no inicia 11.2, 12.1 ni 15.1 automáticamente.
- Con D8 ya PASS, 11.2 deja de estar bloqueada por ese gate, pero sigue requiriendo asignación explícita.
- Follow-up RO conocido para F2/15.1: acción visible **“Vaciar Trash”** con borrado permanente, confirmación fuerte y recent reauth. Queda en cola de roadmap; no se considera implementado ni asignado por el simple registro.

### BBB — F4 / 21.2 Upgrade Matrix — FULL OWNER

BBB continúa FULL OWNER de 21.2 por Issue #41 `5458104890`; PR #51 es el camino combinado 21.1+21.2.

Estado factual:
- PR #51 = OPEN / DRAFT / no mergeado.
- Head `e9fc4e68fc555357ee470996c51544b879cbae93` tenía exact-head Required CI + Upgrade Staging + D6/D7 verdes sobre base `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- JOBS/BBB encontró blocker de proceso al intentar DRAFT → ready; GitHub rechazó merge mientras seguía draft. Handoff Issue #41 `5460283021`.
- Desde entonces integración avanzó por #50 y #53 hasta `6c4499d...`; por regla exact-head, la evidencia previa no autoriza integración final.

**BBB NEXT dentro del mismo owner:** reutilizar #51; incorporar el baseline `6c4499d...`; repetir Required CI + Upgrade 21.2 Staging + D6/D7 aplicables sobre el nuevo exact head; dejar el PR ready por vía válida; integrar solo con race-check final. #48 no se cierra/supersede hasta integración verificable de #51.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. **No mergea código BeatGaler** ni mueve automáticamente a WOZ/AAA/BBB fuera de su owner vigente. Secuencia, exige evidencia, sincroniza el plan y reasigna únicamente mediante decisión explícita.

## Secuencia de integración — estado actual

Completado y verificado:
1. #49 / WOZ / 8.1 → `14002b29...`.
2. #47 / AAA / 11.1 → `489d81b...`.
3. #52 / WOZ / 8.2 → `c25ec6a...`.
4. #50 / AAA / 12.2 → `39e894c...`.
5. #53 / WOZ / D8 RO resolutions → `6c4499d...`; Gate D8 PASS.

Pendiente:
6. #51 / BBB / 21.1+21.2 — refresh contra `6c4499d...`, exact-head CI/staging, ready-state e integración verificable.
7. **Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head correspondiente.

## Gates y paralelismo

- Fases distintas pueden avanzar a la vez.
- Cada owner prueba su propia área antes de handoff.
- Un gate futuro no recibe `[x]` por trabajo preconstruido.
- Pagos/producción/firma/betas/soft launch siguen requiriendo sus prerequisitos reales.
- Revisión independiente de release/security puede existir como gate separado más adelante sin convertirla en hopping diario entre agentes.

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

## WOZ NEXT

**NO ACTIVE ASSIGNMENT.** D8 quedó cerrado y D9 está dependency-ready, pero WOZ no la inicia automáticamente. JOBS/RO debe emitir una asignación separada antes de trabajo nuevo.  
**AAA:** 12.2 cerrado; sin nueva asignación. F2/15.1 “Vaciar Trash” queda registrado como follow-up RO, no iniciado.  
**BBB:** continúa #51/21.1+21.2 FULL OWNER; baseline actual `6c4499d...` obliga fresh union + exact-head evidence antes de integración.  
**PLAN_HEALTH:** SYNCED con GitHub/Issue #41 al baseline `6c4499d...`; ningún checkbox adelantado.

**Principio:** varios agentes construyen distintas piezas del producto en paralelo; cada uno termina y prueba su propia pieza en vez de pasársela continuamente a otro.