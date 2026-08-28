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
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[ 🟡 ] / PENDING`.
- **5.1:** `[x]`.
- **5.2:** `[x]` — WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS FIJOS — AHORA

### WOZ — F1 / D7 / 7.1 — FULL OWNER

PR #46 `woz/task-7.1-direct-capabilities` @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.

Evidencia exact-head ya verde:
- D7 capability #16 `33201030543` SUCCESS;
- D6 cross-process #26 `33201030559` SUCCESS;
- temp-auth compile #148 `33201030554` SUCCESS;
- Required CI #385 `33201030567` SUCCESS.

WOZ conserva ownership hasta cerrar D7. Debe:
1. consumir como casos de prueba los findings AAA `5456406567` y BBB `5456351308`;
2. reproducir/aceptar/rechazar técnicamente los findings pendientes;
3. implementar el delta mínimo correcto;
4. mantener/añadir sus propios tests para scope, replay, expiry/skew, response redaction, closed lease/quarantine, revoke y ceilings;
5. ejecutar tests/CI exact-head;
6. integrar cuando corresponda y publicar `GATE D7` estructurado.

**No depende de que AAA vuelva a PR #45 ni de que BBB vuelva a revisar PR #46.** PR #45 y los handoffs previos quedan como evidencia/input histórico para WOZ. No debilitar assertions materiales solo para obtener verde.

Gate D7: **0 secretos de infraestructura en cliente y 0 operaciones fuera del scope concedido**.

### AAA — F2 / 11.1 Design Foundations — FULL OWNER

AAA se queda en **11.1** hasta cerrarla; no vuelve automáticamente a 7.2.

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

Scope:
- inventariar y unificar VERSION/npm/Cargo/Tauri/Settings donde sea técnicamente seguro;
- endpoint/channel/capability sources;
- runtimes/resources Windows/macOS y digests;
- corregir divergencias de manifest dentro de 21.1;
- añadir/verificar tests/checks de consistencia y CI aplicable;
- entregar evidencia de un único manifest coherente desde un SHA.

**RO DECISION REQUIRED:** el bundle ID final no lo inventa BBB. Si falta esa decisión, aísla solo ese subitem y continúa todo lo demás de 21.1.

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

PRIMARY: continuar PR #46 como owner completo de D7; absorber y cerrar técnicamente los findings pendientes con tests/CI propios y gate estructurado.  
AAA: F2 / 11.1 hasta cierre.  
BBB: F4 / 21.1 hasta cierre.  
PLAN_HEALTH: CLEAN — fixed-area ownership active.

**Principio:** varios agentes construyen distintas piezas del producto en paralelo; cada uno termina y prueba su propia pieza en vez de pasársela continuamente a otro.