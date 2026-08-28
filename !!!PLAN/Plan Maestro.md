# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — MODELO ROMPECABEZAS

Desde 2026-08-28, el trabajo se desbloquea por **dependencia real**, no por número de Día o Fase. JOBS puede reorganizar prioridades, owners, orden operativo, paralelismo y slices cross-phase para maximizar velocidad y calidad.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Un gate controla cierre/promoción de lo que depende de él; no bloquea trabajo futuro realmente independiente.
- Los agentes construyen piezas distintas; no duplican implementación salvo orden explícita de JOBS. Revisión independiente no cuenta como duplicación.
- JOBS puede reordenar fases/tareas, dividir slices, reasignar agentes y mantener varias lanes activas sin pedir permiso adicional al RO.
- JOBS no toca código/infra ni decide cómo resolver técnicamente; WOZ conserva arquitectura, implementación, integración y aceptación técnica.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se rebaja silenciosamente un criterio material de seguridad/release.

## Reglas no negociables

1. No saltar dependencias reales.
2. No marcar `[x]` sin evidencia verificable.
3. Cambio técnico → auditoría read-only previa + pruebas/CI posteriores.
4. Avance relevante → Plan Maestro + fase(s) afectada(s) + Registro.
5. GitHub/Issue #41 conservan diffs, logs y handoffs extensos.
6. Ningún P0/P1 abierto al publicar.
7. Modo autónomo: preflight factual, idempotencia, evidence-before-claim, STOP conditions, gate transaction y watchdog.
8. Si un agente queda bloqueado y existe un slice independiente útil/no conflictivo, JOBS lo reasigna.
9. `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo

- **Critical path:** Fase 1 / Gate D7 — Data plane seguro.
- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[ 🟡 ] / PENDING`.

### WOZ 7.1 actual
- PR #46 `woz/task-7.1-direct-capabilities` @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.
- D7 capability #16 `33201030543` SUCCESS.
- D6 cross-process #26 `33201030559` SUCCESS.
- temp-auth compile #148 `33201030554` SUCCESS.
- Required CI #385 `33201030567` = `IN_PROGRESS` al último preflight JOBS.
- PR #46 declara corregidos los dos revoke-wiring blockers del BBB handoff `5456351308`; **BBB re-review exact-head pendiente**.

### AAA 7.2 actual
- PR #45 `aaa/task-7.2-transport-isolation-adversarial` @ `e29368b4eeaf1641c4f3b9083b166f067bdd6182`.
- Handoff `5456406567`: D7 run #14 `33200605498` FAILURE únicamente por adversarial AAA; unit/PostgreSQL scope/replay = SUCCESS; object substitution/replay/explicit session revoke pasan.
- Findings reproducibles aún pendientes de delta WOZ:
  1. contrato expiry/clock-skew inconsistente memory vs PostgreSQL;
  2. response redaction no universalmente fail-closed en `ok:false` y no-refresh fallback;
  3. capability ACTIVE no queda demostrablemente invalidada por lease expiry / bot quarantine.
- AAA no debe debilitar assertions para volver CI verde.

- **5.1:** `[x]`.
- **5.2:** `[x]` — cierre WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

# LANES SIMULTÁNEAS — AHORA

## LANE A — WOZ / CRITICAL
**F1 / 7.1 — `[ 🟡 ] PRIMARY`**

1. Consumir AAA `5456406567` y reproducir/aceptar/rechazar F1–F3.
2. Si acepta, hacer el delta mínimo en PR #46; no ampliar a 8.x.
3. Mantener scope/deny-by-default/revoke/ceilings ya construido y política shared-bot aceptada.
4. No mergear ni declarar D7 PASS con AAA/BBB pendientes o Required CI exact-head no verde.

## LANE B — AAA / PARALLEL BUILD WHILE BLOCKED
**F2 / 11.1 Design foundations — `[ 🟡 ] ACTIVE PARALLEL`**

AAA está bloqueado para repetir 7.2 hasta que WOZ produzca un nuevo head que responda a F1–F3. Durante ese bloqueo trabaja un slice independiente desde la integración estable:
- tokens, tipografía, focus, buttons, fields, feedback, Dialog, reduced motion;
- AccountGate visual: autofill, contraste, loading y layout 390–430;
- retirar duplicación visual inline solo donde el foundation la sustituya limpiamente;
- tests DOM/a11y afectados.

**Fuera de scope:** APIs Día 8, MFA/reset backend, data plane, YouTube.  
**Artefacto nuevo permitido tras duplicate-check:** `aaa/f2-11.1-design-foundations` desde `23bded948...`.  
**Interrupt rule:** cuando WOZ publique nuevo 7.1 head para F1–F3, AAA deja 11.1 en checkpoint limpio y vuelve a retargetear el PR #45 existente; no crea otro PR 7.2.

## LANE C — BBB / D7 RE-REVIEW NOW, THEN F4
**Immediate:** F1 / 7.1 PR #46 exact head `bd62525...` — READ ONLY re-review únicamente de los dos revoke-wiring blockers `5456351308`.

- comprobar canonical server-side revoke target;
- comprobar fail-closed/durable revoke ante store failure;
- verificar tests HTTP/failure injection pertinentes;
- no reabrir scope ya aceptado sin delta reproducible.

**After handoff:** si WOZ aún no publica otro delta D7, BBB salta automáticamente a **F4 / 21.1 Release manifest readiness audit READ ONLY**: version sources, endpoints/channels/capabilities, runtimes/resources y divergencias. No elige bundle ID ni modifica archivos.

## LANE D — JOBS
Mantener grafo, mover agentes cuando cambian dependencias, preparar administrativamente REUSE D9/D10, procesar handoffs y mantener `WOZ NEXT` en el cuello real.

## Gates bajo el modelo nuevo

- **D7:** exige 0 secretos de infraestructura en cliente y 0 operaciones fuera del scope. Bloquea cierre D7 y trabajo dependiente; no bloquea slices independientes.
- **D8/D9/D10:** conservan aceptación; slices independientes pueden preconstruirse/auditarse antes, nunca `[x]` por adelantado.
- Fases 2–7 conservan sus gates. No se simulan pagos, producción, firma, betas, soak o lanzamiento antes de prerequisitos reales.

## REUSE-FIRST F1 D9/D10

Reutilizar cuando satisfaga literalmente: PostgreSQL autoridad, migrations/versionado/constraints, importer/idempotencia/rollback, durabilidad/restart, fail-closed, PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority. JOBS prepara matriz; WOZ valida equivalencia/GAP; AAA prueba gaps; BBB revisa. No repetir drills solo para recrear evidencia.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementación interna oculta.
- Schema: **Galer T-Library Schema v2**.
- Web pura: sin Tauri ni Desktop helper.
- Media: device ↔ provider directo; Galer Cloud no relaya beats/proyectos.
- Permanent auth/control secrets quedan control-side; cliente usa temporary auth.
- Shared-bot es fallback solo cuando no hay bots libres; exclusividad por vault es camino normal.
- v1 no se publica free-only.
- YouTube debe existir en Desktop/Web; Web no llama Tauri.

## Mapa de fases — trabajo permitido

- **F0:** residual/administrativa.
- **F1:** CRITICAL PATH D7.
- **F2:** PARALLEL BUILD por slices independientes; AAA → 11.1 mientras bloqueado por WOZ.
- **F3:** análisis/prep si no requiere staging/pagos/credenciales inexistentes.
- **F4:** PARALLEL AUDIT/PREP; BBB → 21.1 cuando termine re-review D7 y quede sin delta crítico.
- **F5:** preparación/harness; betas/load real requieren candidato/monitoring.
- **F6:** runbooks/checklists; soft launch/publicación requieren RC/gates.
- **F7:** planificación; operación real requiere lanzamiento/datos.

## WOZ NEXT

PRIMARY: PR #46 — responder AAA F1–F3 y cerrar exact-head CI/reviews.  
READY_FROM_AAA: PR #45 @ `e29368...`, handoff `5456406567`.  
READY_FROM_BBB: handoff `5456351308`; exact-head re-review `bd62525...` pendiente.  
PARALLEL: AAA → F2/11.1 mientras bloqueado; BBB → F4/21.1 después de su re-review si queda sin delta.  
PLAN_HEALTH: CLEAN — dependency-graph model active.

**Principio:** ningún agente espera por un número de Día si existe una pieza independiente, útil y verificable que pueda construir.