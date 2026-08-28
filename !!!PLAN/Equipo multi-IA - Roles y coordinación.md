# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**.

## Roles y ownership

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates, `WOZ NEXT` |
| **WOZ** | F1 / D8 / 8.2 | implementación, fixes, tests, CI, integración y gate técnico de D8 |
| **AAA** | F2 / 12.2 | artifact Biblioteca #50; tests/CI/evidencia e integración de su área |
| **BBB** | F4 / 21.2 | PR #51 camino combinado 21.1+21.2; upgrade matrix y evidencia |

RO conserva alcance de producto, riesgo aceptado y go/no-go. JOBS puede reorganizar el roadmap, pero **un cambio de owner es una decisión explícita**, no un salto automático por dependencia.

Estado de owner verificado:
- WOZ: 8.1 cerrado/integrado; continúa el mismo FULL OWNER de D8 en 8.2 / PR #52.
- AAA: 11.1 cerrado/integrado; continúa FULL OWNER de 12.2 / PR #50.
- BBB: continúa FULL OWNER de 21.2 por Issue #41 `5458104890`; PR #51 es el camino combinado 21.1+21.2.

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

JOBS no toca producto/infra ni decide la solución técnica de WOZ. En particular, JOBS **no mergea código BeatGaler** cuando esa integración pertenece al owner/integrador técnico; JOBS secuencia, exige evidencia y sincroniza el plan.

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
WOZ: F1/D8/8.2 + PR #52 → <estado/evidencia>
AAA: F2/12.2 + PR #50 → <estado/evidencia>
BBB: F4/21.2 + PR #51 → <estado/evidencia>
JOBS: <plan sync/no-op>
OWNER_CHANGES: none | <explícitos>
DUPLICATE_WORK: none | ...
UNVERIFIED_CLAIMS: none | ...
STALLED: none | ...
```

## Estado vigente

- **Baseline canónico:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- **WOZ:** F1 / D8 / 8.2 FULL OWNER. 8.1/#49 ya está integrado. PR #52 `ef0d6b1...` tiene candidate técnico + Required CI verde sobre baseline `14002b29...`, pero debe refresh/revalidarse contra `489d81b...`. Gate D8 sigue PENDING por email provider/templates, retención y provider-only reauth; no D9.
- **AAA:** F2 / 12.2 FULL OWNER. 11.1/#47 refreshed e integrado como `489d81b...`. PR #50 `258017f...` sigue OPEN/no mergeado y debe refresh/revalidarse contra el baseline canónico posterior a la secuencia WOZ.
- **BBB:** F4 / 21.2 FULL OWNER. PR #51 es camino combinado 21.1+21.2, OPEN/DRAFT; current head observado `f70f17e...`, CI actual en curso al preflight y fresh baseline requerido antes de integración final.
- **JOBS:** coordinación, secuenciación y plan; sin hopping automático y sin código BeatGaler.

## Secuencia de integración vigente

1. #49 / 8.1 — **DONE / INTEGRATED** `14002b29...`.
2. #47 / 11.1 — **DONE / INTEGRATED** `489d81b...`.
3. #52 / 8.2 — siguiente cuello técnico: refresh contra `489d81b...`, exact-head CI, integración técnica; Gate D8 puede permanecer PENDING por decisiones externas.
4. #50 / 12.2 — refresh final después del movimiento #52 para evitar doble revalidación; exact-head CI + integración.
5. #51 / 21.1+21.2 — puede continuar pruebas en paralelo; integración final usa baseline vigente y exact-head evidence.
6. Cualquier cambio material de head/combinación invalida el uso del CI anterior como prueba de la nueva combinación hasta nuevo CI exact-head.

**Principio:** tres constructores trabajan tres piezas distintas; cada uno termina y prueba la suya.