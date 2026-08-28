# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por **dependencia real**, incluso cross-phase, pero cada agente conserva **ownership estable de su área asignada** hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- **No hay hopping automático entre tareas.** Una vez asignado un owner, ese agente implementa/audita, corrige, prueba, ejecuta CI aplicable y entrega evidencia de su propia área.
- Findings previos de otros agentes se usan como input; no obligan a devolver el ownership al autor del finding.
- Revisión independiente adicional solo se asigna cuando JOBS/RO la pide explícitamente o un gate externo la exige; no es requisito automático para cada PR.
- JOBS puede reorganizar roadmap/owners, pero una reasignación debe ser explícita y quedar en `!!!PLAN`/Issue #41.
- JOBS no toca código/infra ni decide la solución técnica de WOZ.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[x] / PASS` — WOZ Issue #41 `5457172823`; PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`; D7 `33205320953`, D6 cross-process `33205320957`, temp-auth compile `33205321000` y Required CI #402 `33205320950` SUCCESS.
- **D8:** `[ 🟡 ] / PENDING` — activo bajo WOZ FULL OWNER. 8.1 candidate = PR #49 `f8ae2d1...`, OPEN/no mergeado; 8.2 pendiente.
- **F2 / 11.1:** `[ 🟡 ]` PR #47 `ddad312...` candidate verde pero OPEN/no mergeado/divergido de integración actual.
- **F2 / 12.2:** `[ 🟡 ]` PR #50 `258017f...` candidate verde, OPEN/no mergeado, apilado sobre #47; dependencia #47 → #50 obligatoria.
- **F4 / 21.1:** `[ 🟡 ]` PR #48 `a3ba448...` `COMPLETE_TECHNICAL`, pero OPEN/DRAFT/no mergeado/divergido; no `[x]`.
- **F4 / 21.2:** `[ 🟡 ]` BBB `ASSIGNED / PRECHECK` por RO `5458104890`; dependencia de integración #48 explícita.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### WOZ — F1 / D8 / 8.1+8.2 — FULL OWNER

Baseline canónico: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

D7 está cerrado; PR #46 está mergeado y no debe reabrirse sin nueva evidencia material.

PR #49 `woz/task-8.1-session-security` @ `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff` está OPEN/no mergeado/no draft. Preflight JOBS verifica que deriva directamente del baseline actual (`ahead_by=7`, `behind_by=0`) y que el exact-head CI aplicable está verde. El propio PR declara que **D8 no es PASS** porque 8.2 sigue pendiente. No se encontró handoff estructurado de WOZ para #49 en Issue #41 al momento del preflight, por lo que JOBS no inventa cierre de owner.

WOZ conserva ownership de **todo D8** hasta cerrarlo. Orden inmediato:
1. recheck final de PR #49/head/CI y duplicación;
2. integrar #49 por el flujo técnico autorizado y publicar handoff estructurado de 8.1;
3. pasar inmediatamente a **8.2 — ciclo de cuenta** dentro del mismo ownership;
4. ejecutar tests/CI exact-head aplicables y corregir regresiones de su área;
5. publicar `GATE D8` estructurado solo cuando 8.1 + 8.2 y el requisito literal estén demostrados.

Si un subitem de 8.2 depende de provider/legal/credencial/decisión RO no verificable, aislarlo como `RO DECISION REQUIRED` o `BLOCKED` y continuar trabajo D8 independiente. No inventar decisiones ni saltar automáticamente a D9.

Gate D8: **usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura**.

### AAA — F2 / 12.2 Biblioteca — FULL OWNER ACTUAL

La reasignación AAA 11.1 → 12.2 fue explícita y está registrada en PR #50/handoff AAA. Eso no cierra 11.1: #47 sigue siendo dependencia canónica de #50.

- PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383`: OPEN/no mergeado; handoff `5456682762` = DONE independent slice; Required CI #392 verde. Contra integración actual `e25c604...` está `diverged`, `behind_by=49` y comparte `AccountGate.tsx` + test DOM con #49.
- PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c`: OPEN/no mergeado; handoff `5458081273` = DONE; Required CI #416 verde; está apilado sobre #47 y también diverge de la integración actual.

**Secuencia obligatoria F2:** después de integrar #49, #47 debe incorporar la integración vigente por el método técnico que corresponda, repetir exact-head CI y quedar integrado. **Solo después** #50 puede quedar basado/validado contra una integración que ya contenga #47, repetir exact-head CI si cambia el head e integrarse.

JOBS no prescribe rebase/merge/cherry-pick ni toca código.

**AAA NEXT después de integrar/cerrar #47 y #50:**
- 11.2 Auth UI solo si sus dependencias F1 reales ya están disponibles. Hoy D8/8.2 sigue pendiente e incluye verification/reset/MFA lifecycle, así que 11.2 completa **no** está dependency-safe todavía.
- Si esa condición sigue igual al cerrar #47/#50, el siguiente slice F2 independiente ya planificado será **12.1 — Bootstrap y load**.
- Si D8/8.2 ya cerró para entonces, JOBS reevalúa 11.2 antes de iniciar 12.1.

### BBB — F4 / 21.2 Upgrade Matrix — FULL OWNER / PRECHECK

RO reasignó explícitamente BBB a 21.2 en Issue #41 `5458104890` con `STATUS: ASSIGNED / PRECHECK`.

PR #48 `bbb/f4-21.1-release-manifest` @ `a3ba448e9ded04f73ee77a3556809dcf72e707f5` tiene handoff BBB `5457967950` = `READY_FOR_INTEGRATION / COMPLETE_TECHNICAL`, identidad RO `Galer` / `com.beatgaler.app` y CI exact-head verde. Sin embargo sigue **OPEN / DRAFT / no mergeado** y, contra `e25c604...`, está `diverged`, `behind_by=49`; además comparte `package.json` con #49.

Por tanto 21.1 continúa `[ 🟡 ]`: después de la integración autorizada de #49, #48 debe incorporar el baseline vigente, resolver cualquier interacción dentro del flujo técnico, salir de Draft por autoridad aplicable, repetir exact-head CI y quedar integrado antes de marcar 21.1 `[x]`.

BBB puede avanzar ahora 21.2 solo en modo dependency-safe: duplicate-check, REUSE/GAP, matriz/casos y trabajo que no falsee la existencia de un manifest 21.1 ya canónico. Validaciones dependientes del manifest integrado esperan #48.

**BBB NEXT:** 21.2 Upgrade Matrix dentro de ese límite; no signing/notarization/release/D24.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. **No mergea código BeatGaler** ni mueve automáticamente a WOZ/AAA/BBB fuera de su owner vigente. Secuencia integración, exige evidencia, sincroniza el plan y reasigna únicamente mediante decisión explícita.

## Secuencia de integración autorizada de esta wave

1. **#49 / WOZ / 8.1 primero.** Es el único candidate verificado que contiene el baseline canónico actual (`behind_by=0`). Integración pertenece al flujo técnico WOZ; JOBS no la ejecuta.
2. **#47 → #50.** Después de #49, #47 necesita revalidación porque comparte AccountGate/tests con #49. #50 permanece detrás de #47 por dependencia literal.
3. **#48 / 21.1.** Necesita incorporar al menos el baseline posterior a #49 y revalidar; puede coordinarse en paralelo con la cadena F2 cuando el mutex técnico lo permita. Solo integración verificable habilita el cierre documental de 21.1.
4. **Regla exact-head:** si cambia un head, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre ese exact head.

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

PRIMARY: **F1 / D8 / 8.1 — procesar/integrar PR #49** sobre `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.  
DO_NOW: recheck exact head `f8ae2d1...` + CI; integrar por flujo WOZ autorizado; publicar handoff 8.1; después iniciar **8.2** dentro del mismo ownership.  
DO_NOT: declarar D8 PASS tras 8.1; saltar D8/D9; reabrir D7 sin nueva evidencia; inventar decisiones provider/legal/credenciales.  
AAA: owner actual F2/12.2; cadena obligatoria #47→#50 pendiente de refresh/revalidación/integración post-#49. NEXT posterior: 11.2 solo si D8/8.2 desbloquea APIs; si no, 12.1.  
BBB: F4/21.2 FULL OWNER/PRECHECK por `5458104890`; #48/21.1 técnico completo pero OPEN/DRAFT, refresh + CI + integración pendientes antes de `[x]`.  
PLAN_HEALTH: CLEAN / PENDING INTEGRATION — estado GitHub más reciente sincronizado; ningún checkbox adelantado.

**Principio:** varios agentes construyen distintas piezas del producto en paralelo; cada uno termina y prueba su propia pieza en vez de pasársela continuamente a otro.