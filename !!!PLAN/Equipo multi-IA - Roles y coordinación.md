# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**.

## Roles y ownership

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates, `WOZ NEXT` |
| **WOZ** | F1 / D8 / 8.1+8.2 | implementación, fixes, tests, CI, integración y gate técnico de D8 |
| **AAA** | F2 / 11.1 | implementación, tests, CI y evidencia completa de Design Foundations |
| **BBB** | F4 / 21.1 | manifest/release-chain slice 21.1, tests/checks/CI y evidencia de su área |

RO conserva alcance de producto, riesgo aceptado y go/no-go. JOBS puede reorganizar el roadmap, pero **un cambio de owner es una decisión explícita**, no un salto automático por dependencia.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando las dependencias reales lo permiten.
2. Cada implementación tiene **un owner estable**.
3. El owner hace el ciclo completo de su pieza: preflight → implementación/audit → tests → fixes → CI → handoff.
4. Si aparecen findings de otro agente, el owner los consume como input y los reproduce/cierra dentro de su propia área.
5. No se devuelve automáticamente una pieza al autor del finding.
6. No hay `interrupt rule` ni hopping automático entre tareas.
7. Si un owner queda bloqueado, reporta `BLOCKED` y sigue siendo owner; JOBS decide explícitamente si reasigna.
8. Revisión independiente adicional se crea solo por orden JOBS/RO o por un gate que literalmente la requiera.
9. `READY_TO_WORK` no implica `READY_TO_CLOSE` ni `READY_TO_RELEASE`.
10. Ningún gate se marca `[x]` sin evidencia verificable.

## Invocaciones

- `Eres JOBS. Lee !!!PLAN y continúa.`
- `Eres WOZ. Lee !!!PLAN y continúa tu área asignada.`
- `Eres AAA. Lee !!!PLAN y continúa tu área asignada.`
- `Eres BBB. Lee !!!PLAN y continúa tu área asignada.`

No hace falta repetir estado si puede recuperarse del plan/GitHub.

## JOBS — rutina

1. preflight factual de baseline/gates/handoffs/PRs/CI;
2. comprobar que cada owner sigue dentro de su área;
3. procesar handoffs y findings;
4. mantener scope claro y evitar duplicación;
5. actualizar estado confirmado en Plan/fase/Registro;
6. escalar blocker real sin mover al agente automáticamente;
7. reasignar solo con decisión explícita;
8. entregar `WOZ NEXT` centrado en el cuello técnico.

JOBS no toca producto/infra ni decide la solución técnica de WOZ.

## Owner — paquete mínimo

```text
ROLE: WOZ | AAA | BBB
AREA: <área fija>
TASK: <tarea exacta dentro del área>
BASE: <rama/SHA>
SCOPE: <sí>
OUT_OF_SCOPE: <no>
CHANGES: <implementación/audit>
TESTS: <pruebas propias>
CI: <runs/checks>
EVIDENCE: <SHA/PR/runtime>
BLOCKERS: <none/lista>
NEXT_WITHIN_AREA: <siguiente paso del mismo owner>
```

Reglas:
- cambio de producto → rama/PR propia;
- antes de crear artefacto, duplicate-check;
- el owner corrige sus regresiones y añade pruebas de aceptación de su área;
- findings fuera de scope se reportan; JOBS decide si pertenecen al owner o a otra área;
- no mergear/cerrar globalmente sin autoridad aplicable;
- no marcar `[x]` solo porque los tests propios estén verdes si falta un requisito literal del gate.

# Modo autónomo / turno nocturno

## 1. Preflight factual obligatorio

Verificar:
- área fija del rol;
- tarea exacta vigente dentro de esa área;
- baseline/rama/SHA;
- dependencias literales;
- PR/rama existente antes de crear otra;
- últimos findings/handoffs que afecten esa área;
- CI relevante;
- si el trabajo ya fue procesado.

Dato material no verificable → **STOP / PENDING**.

## 2. Idempotencia

Antes de rama/PR/comentario/commit:
1. buscar artefacto existente de la misma pieza/baseline;
2. continuar ahí o no-op;
3. nunca crear copia por nuevo ciclo.

## 3. Evidence-before-claim

No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff. Lo no probado = `UNVERIFIED` o `PENDING`.

## 4. Owner self-test

El owner es responsable de:
- unit/integration/DOM/runtime que correspondan;
- regresiones descubiertas durante su trabajo;
- CI exact-head aplicable;
- reproducir dentro de su área findings previos que materialmente bloqueen su gate.

Los tests propios no eliminan revisiones independientes obligatorias de release/security cuando un gate posterior las exija.

## 5. STOP conditions

STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante:
- contradicción material Plan/Issue/GitHub/runtime;
- baseline inesperado;
- cambio destructivo fuera de scope;
- secretos/credenciales fuera de procedimiento;
- decisión reservada al RO;
- necesidad real de ampliar alcance;
- CI externo no atribuible;
- evidencia insuficiente para gate.

**BLOCKED no cambia el owner automáticamente.**

## 6. Corrective assignment

2 ciclos sin progreso → JOBS precisa la orden dentro de la misma área. 3 ciclos → `STALLED`. Reasignación solo si JOBS/RO lo decide explícitamente.

## 7. Gate transaction

WOZ publica cuando aplique:

```text
GATE: <id>
STATUS: PASS | FAIL | PENDING
REQUIREMENTS:
- <req>: PASS | FAIL | PENDING — <evidence>
EVIDENCE: <PR/SHA/tests/CI/runtime>
UNVERIFIED: <none/lista>
NEXT: <acción>
```

## 8. Handoff

```text
AI-HANDOFF
ROLE: WOZ | AAA | BBB | JOBS
AREA: <owner fijo>
TASK: <tarea exacta>
BASE_BEFORE: <rama/SHA>
HEAD_AFTER: <rama/SHA o none>
STATUS: DONE | BLOCKED | FINDING | STALLED | PENDING
CHANGES: <resumen/none>
TESTS: <resultado/none>
CI: <run/check/none>
EVIDENCE: <IDs/SHA>
UNVERIFIED: <none/lista>
BLOCKERS: <none/lista>
NEXT_WITHIN_AREA: <acción>
```

## Night Shift Ledger

```text
NIGHT SHIFT LEDGER
WOZ: F1/D8 → <estado/evidencia>
AAA: F2/11.1 → <estado/evidencia>
BBB: F4/21.1 → <estado/evidencia>
JOBS: <plan sync/no-op>
OWNER_CHANGES: none | <explícitos>
DUPLICATE_WORK: none | ...
UNVERIFIED_CLAIMS: none | ...
STALLED: none | ...
```

## Estado vigente

- **WOZ:** F1 / D8 / 8.1+8.2 hasta cierre D8. PRIMARY actual: 8.1.
- **AAA:** F2 / 11.1 hasta cierre 11.1; PR #47 open, slice DONE con CI exact-head, cierre global pendiente.
- **BBB:** F4 / 21.1 hasta cierre 21.1; audit FINDING activo, bundle ID final `RO DECISION REQUIRED`.
- **JOBS:** coordinación, sin hopping automático.

**Principio:** tres constructores trabajan tres piezas distintas; cada uno termina y prueba la suya.