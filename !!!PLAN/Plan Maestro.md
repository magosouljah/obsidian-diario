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
- **D8:** `[ 🟡 ] / PENDING` — activo bajo WOZ full owner.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### WOZ — F1 / D8 / 8.1+8.2 — FULL OWNER

Baseline de entrada: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

D7 está cerrado; PR #46 está mergeado y no debe reabrirse sin nueva evidencia material.

WOZ conserva ownership de **todo D8** hasta cerrarlo. Orden de trabajo inmediato:
1. preflight/duplicate-check de D8 sobre el baseline exacto;
2. comenzar por **8.1 — sesión y seguridad de sesión**: cookie HttpOnly/Secure/SameSite o equivalente, CSRF explícito, distinguir 401/expiry de offline/timeout, session inventory, revoke-one/revoke-all y rotación sensible;
3. ejecutar tests/CI exact-head aplicables y corregir regresiones de su propia área;
4. continuar dentro del mismo ownership con **8.2 — ciclo de cuenta**: verification/reset one-shot/expiry/anti-enumeración, MFA recovery/reauth/notifications, export/delete + revocation/provider cleanup/retention/receipt;
5. publicar `GATE D8` estructurado solo cuando el requisito literal esté demostrado.

Si un subitem de 8.2 depende de provider/legal/credencial/decisión RO no verificable, aislarlo como `RO DECISION REQUIRED` o `BLOCKED` y continuar trabajo D8 independiente. No inventar decisiones ni saltar automáticamente a D9.

Gate D8: **usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura**.

### AAA — F2 / 11.1 Design Foundations — FULL OWNER

AAA se queda en **11.1** hasta cierre explícito; no vuelve automáticamente a 7.2.

PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383` está **OPEN / no mergeado**. El slice asignado tiene handoff DONE y Required CI #392 `33202493998` SUCCESS, pero **11.1 global no recibe `[x]` todavía** hasta integración/secuenciación verificable.

Scope:
- tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog, reduced motion;
- AccountGate: autofill, contraste, loading y layout 390–430;
- retirar duplicación visual inline donde el foundation la sustituya limpiamente;
- documentación/estados aplicables;
- tests DOM/a11y, build y CI afectados;
- corregir sus propias regresiones hasta entregar evidencia completa.

Fuera de scope: APIs de cuenta F1/D8, MFA/reset backend, data plane, YouTube.

### BBB — F4 / 21.1 Release Manifest — FULL OWNER

BBB se queda en **21.1** hasta cerrarla; no vuelve automáticamente a D7.

Audit READ ONLY `5456640788` sobre `23bded948c4377b28fc48a72378816968d4cd413` dejó REUSE fuerte y cinco gaps: bundle ID final sin decisión; updater endpoint duplicado; channel/feed sin fuente canónica; FFmpeg omitido del packaging Windows; manifest tooling no fijado al mismo SHA de artefactos.

BBB debe continuar 21.1 dentro de su área, reutilizando version/provenance/shared-SHA ya verdes y corrigiendo solo gaps técnicamente autorizados. **RO DECISION REQUIRED:** el bundle ID final no lo inventa BBB. Endpoint/channel semantics que requieran decisión de producto/arquitectura se escalan sin bloquear el resto seguro de 21.1.

Fuera de scope: 21.2 upgrade matrix, signing, notarization, release, certificados/credenciales.

### JOBS

JOBS mantiene prioridades, `!!!PLAN`, handoffs y gates. **No mueve automáticamente a WOZ/AAA/BBB a otra tarea al bloquearse.** Si un owner queda bloqueado, permanece dueño y reporta el blocker; JOBS solo reasigna mediante decisión explícita.

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

PRIMARY: **F1 / D8 / 8.1 — sesión y seguridad de sesión**, sobre `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.  
DO_NOW: preflight REUSE/GAP + duplicate-check; implementar solo requisitos literales de 8.1; tests/CI exact-head; mantener ownership de D8 y continuar luego 8.2 sin hopping.  
DO_NOT: reabrir D7 sin nueva evidencia; iniciar D9 por conveniencia; inventar decisiones provider/legal/credenciales; rebajar Gate D8.  
AAA: F2 / 11.1 continúa owner; PR #47 open, slice DONE/CI verde, cierre global pendiente de integración/secuenciación.  
BBB: F4 / 21.1 continúa owner; audit FINDING activo y bundle ID = `RO DECISION REQUIRED`.  
PLAN_HEALTH: CLEAN — D7 closed; D8 active; fixed-area ownership active.

**Principio:** varios agentes construyen distintas piezas del producto en paralelo; cada uno termina y prueba su propia pieza en vez de pasársela continuamente a otro.