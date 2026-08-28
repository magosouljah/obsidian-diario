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

- **Critical path:** Fase 1 / Día 7 / Gate D7 — Data plane seguro.
- **Release público:** 🔴 `NO-GO`.
- **Integración:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`, versión `0.8.0-alpha.1`.
- **D6:** `[x] / PASS` — WOZ Issue #41 `5455677550`; Required CI #363 `33194215450` SUCCESS; compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS.
- **D7:** `[ 🟡 ] / PENDING`.
- **BBB 7.1:** finding `5455758175`: gaps en capability/deny-by-default, lifecycle revoke, ceilings bot/tenant y revocación inmediata control-side.
- **AAA 7.2 parcial:** PR #45 @ `1d923c467922231df157bdc42f9aad62405d34ea`; Required CI #364 `33195699165` SUCCESS; finding boundary fail-closed `5455777574`. No cierra 7.2/D7.
- **5.1:** `[x]`.
- **5.2:** `[x]` — cierre WOZ/RO `5448976400`; no repetir drills aceptados salvo invalidación.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante.
- **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

# LANES SIMULTÁNEAS

## LANE A — WOZ / CRITICAL
**F1 / 7.1 — `[ 🟡 ] PRIMARY`**

Resolver técnicamente el delta mínimo de D7: capability corta scope `user/vault/operation/object`, allowlist/deny-by-default, lifecycle revoke, revocación inmediata control-side, ceilings bot/tenant y el finding fail-closed AAA si lo reproduce/acepta. Mantener la política shared-bot aceptada. Salida: PR/head exacto + tests/CI + handoff.

## LANE B — AAA / PARALLEL BUILD
**F2 / 11.1 Design foundations — `READY_TO_WORK`**

Mientras la parte restante de 7.2 espera contrato 7.1, AAA trabaja un slice frontend independiente:
- tokens, tipografía, focus, buttons, fields, feedback, Dialog, reduced motion;
- AccountGate visual: autofill, contraste, loading y layout 390–430;
- retirar duplicación visual inline solo donde el foundation la sustituya limpiamente;
- tests/DOM/a11y afectados.

**Fuera de scope:** APIs Día 8, MFA/reset backend, data plane, YouTube. PR #45 queda intacto. Cuando WOZ publique delta 7.1, JOBS decide el checkpoint/retorno de AAA a 7.2.

## LANE C — BBB / PARALLEL AUDIT
**F4 / 21.1 Release manifest readiness — `READY_TO_WORK / READ ONLY`**

Auditar VERSION/npm/Cargo/Tauri/Settings, endpoints/channels/capabilities, runtimes/resources Windows/macOS y divergencias que impedirían un manifest único desde un SHA. Entregar `REUSE | GAP | DEPENDENCY | NEXT` con evidencia.

**Fuera de scope:** elegir bundle ID final, modificar código/config, firmar/notarizar/generar release.

## LANE D — JOBS
Mantener grafo, mover agentes cuando cambian dependencias, preparar administrativamente REUSE de D9/D10, procesar handoffs y mantener `WOZ NEXT` en el cuello real.

## Gates bajo el modelo nuevo

- **D7:** exige 0 secretos de infraestructura en cliente y 0 operaciones fuera del scope. Bloquea cierre D7 y trabajo que dependa técnicamente de ese contrato; **no** bloquea slices independientes de otras fases.
- **D8/D9/D10:** conservan sus requisitos de aceptación; slices independientes pueden preconstruirse/auditarse antes, nunca marcarse `[x]` por adelantado.
- Fases 2–7 conservan sus gates. No se simulan pagos, producción, firma, betas, soak o lanzamiento antes de sus prerequisitos reales.

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
- **F2:** PARALLEL BUILD permitido por slices independientes; AAA → 11.1.
- **F3:** análisis/prep permitido cuando no requiera staging/pagos/credenciales aún inexistentes.
- **F4:** PARALLEL AUDIT/PREP permitido; BBB → 21.1 readiness.
- **F5:** preparación/harness permitido; betas/load real requieren candidato/monitoring.
- **F6:** runbooks/checklists permitidos; soft launch/publicación requieren RC/gates.
- **F7:** planificación permitida; operación real requiere lanzamiento/datos.

## WOZ NEXT

PRIMARY: F1 / 7.1.  
READY_FROM_AAA: PR #45 + CI #364 + boundary finding.  
READY_FROM_BBB: 7.1 gap review `5455758175`.  
PARALLEL: AAA → F2/11.1; BBB → F4/21.1 audit.  
PLAN_HEALTH: CLEAN — dependency-graph model active.

**Principio:** ningún agente espera por un número de Día si existe una pieza independiente, útil y verificable que pueda construir.