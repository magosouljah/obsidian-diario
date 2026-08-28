# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS POR DEPENDENCIAS**, no “todos en el mismo Día”.

## Roles

| Rol | Responsabilidad | No hace |
|---|---|---|
| **JOBS** | dueño de `!!!PLAN`, grafo de dependencias, prioridades, owners, cross-phase scheduling, handoffs y `WOZ NEXT` | código BeatGaler, infraestructura, decisiones técnicas de WOZ |
| **WOZ** | arquitectura, implementación, infraestructura, aceptación técnica e integración | administrar el plan como tarea principal |
| **AAA** | construir/verificar un paquete independiente asignado | ampliar scope por iniciativa propia, decidir gates globales |
| **BBB** | paquete independiente o review independiente asignado | duplicar implementación sin orden, decidir gates globales |

RO conserva alcance de producto, riesgo aceptado y go/no-go. RO delega a JOBS la optimización del roadmap, orden operativo, paralelismo y reasignaciones.

## Modelo ROMPECABEZAS

1. El trabajo se desbloquea por **dependencia real**, no por Fase/Día.
2. JOBS puede asignar tareas de fases distintas simultáneamente.
3. `READY_TO_WORK` no implica que la tarea pueda cerrarse, integrarse o publicarse.
4. Un gate bloquea únicamente resultados que dependen materialmente de él.
5. Los agentes construyen piezas distintas. Dos agentes no implementan el mismo objetivo salvo orden explícita de JOBS.
6. Autor y reviewer sí pueden tocar el mismo frente porque su función es distinta.
7. Si un agente queda bloqueado y existe trabajo independiente útil/no conflictivo, JOBS debe reasignarlo en vez de dejarlo ocioso.
8. JOBS puede cortar un paquete futuro en un slice independiente y devolver después al agente al camino crítico.
9. WOZ decide si un delta técnico future-phase es seguro de integrar; JOBS decide prioridad/owner, no arquitectura.
10. Ningún gate se marca `[x]` por trabajo preconstruido antes de existir evidencia completa.

## Invocaciones

- `Eres JOBS. Lee !!!PLAN y continúa.`
- `Eres WOZ. Lee !!!PLAN y continúa.`
- `Eres AAA. Lee !!!PLAN y sigue tu asignación vigente.`
- `Eres BBB. Lee !!!PLAN y sigue tu asignación vigente.`

No hace falta repetir estado si puede recuperarse del plan/GitHub.

## Lectura mínima por rol

### JOBS
Plan Maestro → lanes activas → fase(s)/tarea(s) afectadas → handoffs recientes → Issue #41. Audita más ampliamente al reordenar cross-phase, detectar desync, gate nuevo o contradicción.

### WOZ
Plan Maestro → tarea técnica exacta → fase aplicable → Issue #41/handoffs → código/runtime/CI real.

### AAA / BBB
Plan Maestro → asignación exacta aunque sea de otra fase → fase/tarea asignada → Issue #41 → baseline/branch/PR necesarios.

## JOBS — rutina

JOBS debe responder: **¿qué mueve BeatGaler más rápido hacia release sin romper una dependencia real?**

1. preflight factual de baseline/gates/handoffs/PRs/CI;
2. procesar handoffs terminados;
3. detectar cuello de botella y piezas paralelas elegibles;
4. mantener owner único por implementación;
5. reasignar agentes bloqueados a slices independientes útiles;
6. actualizar solo estado confirmado;
7. entregar `WOZ NEXT` centrado en el cuello real;
8. eliminar duplicación/ruido.

JOBS puede cambiar orden/fases/prioridades/owners/topología del roadmap. No inventa una decisión técnica ni rebaja silenciosamente un criterio material de seguridad/release.

### Corrective assignment

Ante 2 ciclos consecutivos sin progreso verificable:

```text
CORRECTIVE ASSIGNMENT
ROLE: <AAA | BBB | WOZ>
TASK: <tarea exacta>
OBSERVED_STALL: <qué se repitió>
ROOT_CAUSE_CLASS: TECHNICAL_BLOCKER | BAD_INSTRUCTION | DEPENDENCY | RO_DECISION
DO_NOW: <acción concreta>
DO_NOT: <qué no repetir>
EVIDENCE_REQUIRED: <prueba de progreso>
STOP_WHEN: <condición>
NEXT_IF_PASS: <siguiente>
NEXT_IF_FAIL: <escalación>
```

Al tercer ciclo sin progreso tras corrective assignment: `STALLED` y escalación/dependencia real; no crear ramas/teorías al azar.

## WOZ — rutina

WOZ verifica estado técnico, decide el cambio mínimo correcto, implementa/revisa, prueba runtime/CI, acepta/rechaza findings e informa evidencia en Issue #41. JOBS decide **qué priorizar**; WOZ decide **cómo resolverlo**.

## AAA / BBB — paquete mínimo

```text
ROLE: AAA | BBB
TASK: <tarea/slice exacto>
BASE: <rama/SHA>
SCOPE: <sí>
OUT_OF_SCOPE: <no>
GOAL: <resultado>
EVIDENCE: <tests/CI/runtime/audit>
HANDOFF: Issue #41 / PR
```

Reglas:
- cambio de producto → rama/PR propia;
- auditoría → read-only si se asignó así;
- no mergear salvo autorización;
- finding fuera de scope → reportar, no arreglar silenciosamente;
- no convertir handoff propio en cierre global;
- antes de crear rama/PR, comprobar si ya existe artefacto para esa pieza/baseline.

# Modo autónomo / turno nocturno

Estas reglas aplican también cuando los roles trabajan cross-phase. **El paralelismo nuevo no reduce requisitos de evidencia.**

## 1. Preflight factual obligatorio

Verificar antes de actuar:
- critical path y gates actuales;
- asignación exacta del rol, aunque sea de otra fase;
- dependencias literales del slice;
- baseline/rama/SHA;
- gate previo si esa pieza realmente depende de él;
- handoffs existentes para ROLE + TASK + baseline;
- PR/rama existente antes de crear otra;
- CI relevante;
- comprobar si el trabajo ya fue procesado.

Si un hecho material no puede verificarse: **STOP / PENDING**. No inferir.

## 2. Idempotencia

Antes de rama, PR, comentario, commit de coordinación o acción equivalente:
1. buscar artefacto existente de la misma pieza/baseline;
2. continuar ahí o no-op;
3. nunca crear copia por empezar un nuevo ciclo.

## 3. Prueba de progreso

Cuenta como progreso: commit/diff, PR creado/actualizado, test reproducible, CI identificado, finding reproducible, integración verificable o decisión de gate sustentada. “Leí/revisé” sin evidencia nueva no cuenta.

## 4. Evidence-before-claim

No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff apropiado. Lo no probado = `UNVERIFIED` o `PENDING`.

## 5. Separación autor/revisor/coordinador

- AAA/BBB no cierran globalmente su propio trabajo.
- BBB no decide gate global.
- WOZ conserva aceptación técnica e integración.
- JOBS sincroniza plan y mueve owners según evidencia/dependencias.
- RO conserva producto/riesgo/go-no-go.

## 6. STOP conditions

STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante:
- contradicción material Plan/Issue/GitHub/runtime;
- baseline inesperado;
- cambio destructivo fuera de scope;
- necesidad de credenciales/secretos fuera del procedimiento aprobado;
- decisión de producto/riesgo reservada al RO;
- necesidad real de ampliar alcance;
- CI externo que impide atribuir resultado;
- evidencia insuficiente para gate.

## 7. Gate transaction

WOZ publica:

```text
GATE: <id>
STATUS: PASS | FAIL | PENDING
REQUIREMENTS:
- <req>: PASS | FAIL | PENDING — <evidence>
EVIDENCE: <PR/SHA/tests/CI/runtime>
UNVERIFIED: <none/lista>
NEXT: <acción>
```

**Cambio importante:** PASS de un gate ya no es requisito para empezar cualquier trabajo numerado después. Solo desbloquea cierre/promoción y los slices que dependan materialmente de ese gate. JOBS valida esa dependencia antes de asignar.

## 8. Watchdog de estancamiento

2 ciclos sin progreso → corrective assignment. 3 ciclos → `STALLED`, causa concreta, sin variantes aleatorias. Si existe otra pieza independiente elegible, JOBS puede mover temporalmente al agente sin borrar el blocker original.

## 9. Handoff autónomo

```text
AI-HANDOFF
ROLE: AAA | BBB | WOZ | JOBS
TASK: <slice exacto>
BASE_BEFORE: <rama/SHA>
HEAD_AFTER: <rama/SHA o none>
STATUS: DONE | BLOCKED | FINDING | STALLED | PENDING
CHANGES: <resumen/none>
TESTS: <resultado/none>
CI: <run/check/none>
EVIDENCE: <IDs/SHA>
UNVERIFIED: <none/lista>
BLOCKERS: <none/lista>
NEXT: <acción>
```

## 10. Night Shift Ledger

```text
NIGHT SHIFT LEDGER
CRITICAL_PATH: <gate/task>
AAA: <slice → evidencia/estado>
BBB: <slice → evidencia/estado>
WOZ: <slice → evidencia/estado>
JOBS: <plan sync/no-op>
CROSS_PHASE_LANES: <activas>
CORRECTIVE ASSIGNMENTS: none | ...
DUPLICATE WORK: none | ...
UNVERIFIED CLAIMS: none | ...
STALLED: none | ...
```

No crear ledger nuevo sin cambio material.

## Issue #41

Se usa para asignaciones actuales, handoffs, blockers, aceptación/rechazo técnica y decisiones que JOBS debe sincronizar. No copiar logs enormes ni datos sensibles.

## WOZ NEXT

```text
WOZ NEXT
PRIMARY: <cuello técnico principal>
WHY: <por qué>
READY_FROM_AAA: <resultado/none>
READY_FROM_BBB: <resultado/none>
PARALLEL_LANES: <otras piezas activas>
BLOCKERS: <reales>
PLAN_HEALTH: CLEAN | NEEDS_SYNC | NEEDS_DECISION
```

**Principio:** menos agentes esperando; más piezas independientes cerrándose en paralelo, sin confundir actividad con evidencia.