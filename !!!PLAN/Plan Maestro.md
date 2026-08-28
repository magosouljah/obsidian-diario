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
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[x] / PASS` — WOZ Issue #41 `5457172823`; PR #46 merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`; CI aplicable verde.
- **D8 / 8.1:** `[x] / DONE / INTEGRATED` — PR #49 exact tested head `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff`; merge `14002b29c5101232c0ca8f8b85d808c8214975fb`; WOZ handoff Issue #41 `5458273984`.
- **D8 / 8.2:** `[ 🟡 ] / TECHNICAL CANDIDATE / PENDING` — PR #52 `ef0d6b142a92cdb88b2a3111e144ba6a9f15df9c`, OPEN/no mergeado. Required CI `33216990412` SUCCESS sobre ese head, pero el PR parte de `14002b29...` y la integración ya avanzó a `489d81b...`; requiere refresh/revalidación exact-head antes de integración. Gate D8 además conserva decisiones provider/legal.
- **D8 global:** `[ 🟡 ] / PENDING` — no PASS hasta 8.2 integrado/revalidado + resolución/aceptación explícita de email provider/templates, retención y reauth provider-only + gate transaction WOZ.
- **F2 / 11.1:** `[x] / DONE / INTEGRATED` — PR #47 refreshed head `fdc6463e6b81efedc547c97595529d28e0ba2d83`; Required CI #429 `33216364174` SUCCESS; D6 #68 `33216364104` SUCCESS; D7 #39 `33216364074` SUCCESS; merge de integración `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **F2 / 12.2:** `[ 🟡 ] / CANDIDATE DONE / INTEGRACIÓN PENDIENTE` — PR #50 `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c`, OPEN/no mergeado. Su CI #416 fue verde sobre el stack anterior, pero debe quedar validado contra integración que ya contiene #47 y contra cualquier integración previa que JOBS secuencie antes de su cierre.
- **F4 / 21.1+21.2:** `[ 🟡 ]` — BBB consolidó el camino técnico en PR #51 `bbb/task-21.2-upgrade-matrix`; PR sigue OPEN/DRAFT. Head actual observado `f70f17ea41cd26bd833bf7ee91949a3e4d752d4e`; Required CI del head actual estaba QUEUED al preflight. #48 no recibe cierre separado mientras el camino combinado #51 no esté integrado y verificable.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### WOZ — F1 / D8 / 8.2 — FULL OWNER

Baseline canónico vivo: `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

8.1 está cerrado e integrado. No reabrir D7 ni 8.1 sin nueva evidencia material.

PR #52 `woz/task-8.2-account-lifecycle` @ `ef0d6b142a92cdb88b2a3111e144ba6a9f15df9c` implementa el lifecycle técnico de 8.2: verification/reset one-shot y anti-enumeración, MFA recovery, reauth, notifications, export, delete/cleanup/receipt y revocación fail-closed. Required CI sobre ese exact head pasó. Sin embargo ese head fue construido sobre `14002b29...`; desde entonces #47 fue integrado y el baseline canónico es `489d81b...`. Evidence-before-claim exige nueva combinación exact-head antes de integrar/cerrar 8.2.

**WOZ NEXT dentro del mismo owner:**
1. reutilizar PR #52; no crear duplicado;
2. incorporar el baseline canónico `489d81b...` por el método técnico que WOZ determine;
3. corregir solo regresiones propias y repetir Required CI + D6/D7/compile aplicables sobre el nuevo exact head;
4. integrar 8.2 por el flujo técnico autorizado cuando la combinación quede demostrada;
5. publicar handoff estructurado de 8.2;
6. mantener `GATE D8 = PENDING` hasta que las decisiones externas abajo estén resueltas/aceptadas y publicar entonces la transacción de gate.

**RO / provider / legal decisions todavía necesarias para Gate D8:**
- proveedor y templates productivos para email verification/reset;
- duración explícita de retención/tombstone para account deletion;
- contrato aprobado de reauth sensible para cuentas provider-only/OAuth-only.

Mientras esas decisiones no existan, WOZ no las inventa y **no salta a D9**.

Gate D8 literal: **usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura**.

### AAA — F2 / 12.2 Biblioteca — FULL OWNER ACTUAL

11.1 ya está cerrado: PR #47 fue actualizado sobre el baseline post-#49, pasó exact-head CI e ingresó a integración como `489d81b...`.

PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c` conserva el slice técnico 12.2 y su CI #416 verde histórico, pero sigue OPEN/no mergeado. Ese CI no es evidencia de la combinación actual que ya contiene el refreshed #47 y puede volver a moverse por D8.2.

**AAA NEXT dentro del mismo owner:**
1. reutilizar #50; no crear artifact duplicado;
2. esperar/seguir la secuencia de integración fijada por JOBS para evitar refresh inútil;
3. incorporar el baseline canónico que corresponda al momento de cierre por el método técnico de su owner/integrador;
4. repetir CI exact-head si cambia el head;
5. integrar/cerrar 12.2 solo con evidencia verificable.

Después de #50 integrado/cerrado:
- si D8 ya está cerrado y sus APIs están disponibles, JOBS reevalúa **11.2 Auth UI**;
- si D8 sigue pendiente, el siguiente slice F2 independiente planificado es **12.1 — Bootstrap y load**.

### BBB — F4 / 21.2 Upgrade Matrix — FULL OWNER

BBB continúa en 21.2 por reasignación RO `5458104890`.

PR #51 es ahora el camino combinado de integración para 21.1+21.2. Su body declara que contiene el manifest 21.1 y el Upgrade Matrix 21.2, preservando upgrade 0.7.4, settings/SQLite/offline/cache, clean install/recovery y staging same-SHA. Sigue OPEN/DRAFT y no está cerrado. El head actual observado `f70f17e...` lanzó nueva CI; Required CI seguía QUEUED al preflight JOBS. Además la integración canónica ya avanzó a `489d81b...`, por lo que el propio contrato de #51 exige fresh union + CI si el baseline se mueve.

BBB mantiene owner y puede continuar sus pruebas/CI dependency-safe. No signing/notarization/release/D24 y no `[x]` hasta integración verificable.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. **No mergea código BeatGaler** ni mueve automáticamente a WOZ/AAA/BBB fuera de su owner vigente. Secuencia integración, exige evidencia, sincroniza el plan y reasigna únicamente mediante decisión explícita.

## Secuencia de integración autorizada — estado post #49/#47

Ya completado:
1. **#49 / WOZ / 8.1** → integrado como `14002b29...`.
2. **#47 / AAA / 11.1** → refreshed, CI exact-head verde e integrado como `489d81b...`.

Siguiente cuello técnico:
3. **#52 / WOZ / 8.2 primero para cierre técnico.** Debe incorporar `489d81b...`, repetir exact-head CI aplicable e integrarse. D8 seguirá PENDING si persisten decisiones RO/provider/legal.
4. **#50 / AAA / 12.2 después del movimiento de integración de #52**, para evitar validar dos veces el mismo stack. Refresh sobre la integración resultante, exact-head CI e integración.
5. **#51 / BBB / 21.1+21.2** continúa trabajo/CI en paralelo, pero su integración final debe usar el baseline vigente y repetir evidencia si ese baseline cambió.
6. **Regla exact-head:** si cambia un head o la combinación material bajo prueba, el CI verde anterior no prueba la nueva combinación hasta que el CI aplicable vuelva a pasar sobre el exact head correspondiente.

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

PRIMARY: **F1 / D8 / 8.2 — continuar PR #52**, no crear duplicado.  
BASELINE: `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.  
DO_NOW: refresh/revalidar #52 contra baseline vivo; CI exact-head; integrar 8.2 técnico; publicar handoff.  
STOP/GATE: email provider/templates, retención y provider-only reauth requieren autoridad aplicable; mientras tanto D8 = PENDING y no D9.  
AAA: #47/11.1 cerrado; #50/12.2 permanece owner actual y se refresca después del movimiento #52 para evitar CI desperdiciado.  
BBB: #51/21.1+21.2 continúa FULL OWNER, OPEN/DRAFT, CI del current head en curso; integración final requiere baseline vigente.  
PLAN_HEALTH: SYNCED / PENDING D8 + INTEGRATION — ningún checkbox adelantado.

**Principio:** varios agentes construyen distintas piezas del producto en paralelo; cada uno termina y prueba su propia pieza en vez de pasársela continuamente a otro.