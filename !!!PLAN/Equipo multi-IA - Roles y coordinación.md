# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 007

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra |
| **AAA** | F2 / 12.1 | `NIGHT-AAA-008`: cerrar PR #58 si exact-head sigue válido; luego atomic empty-index únicamente |
| **BBB** | F4 / 24.2 → 25.1 | `NIGHT-BBB-008`: cerrar PR #57; luego matrix audit dependency-safe |
| **WOZ** | F3 / 16.1 → 16.2 | `NIGHT-WOZ-008`: cerrar PR #59 solo con exact-head final PASS; luego promotion contract software-only |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar el roadmap, pero **un cambio de owner es una decisión explícita**, no un salto automático por dependencia.

**Baseline canónico al CYCLE 007:** `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9` al preflight JOBS. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum; ningún worker técnico es owner de esa acción externa.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando las dependencias reales lo permiten.
2. Cada implementación/pieza material tiene **un owner estable** por ciclo.
3. El owner hace el ciclo completo de su pieza: preflight → implementación/audit → tests → fixes → CI → handoff.
4. Findings de otro agente son input; no transfieren ownership automáticamente.
5. No hay `interrupt rule` ni hopping automático entre tareas.
6. Si un owner queda bloqueado, reporta `BLOCKED`; JOBS decide explícitamente si reasigna.
7. Revisión independiente adicional existe solo por orden JOBS/RO o gate literal.
8. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
9. Ningún gate se marca `[x]` sin evidencia verificable.
10. **Dependency-ready no equivale a assigned.**

## Invocaciones

- `Eres JOBS. Lee !!!PLAN y continúa.`
- `Eres WOZ. Lee !!!PLAN y continúa tu área asignada.`
- `Eres AAA. Lee !!!PLAN y continúa tu área asignada.`
- `Eres BBB. Lee !!!PLAN y continúa tu área asignada.`

Si un worker no tiene asignación activa explícita en su markdown nocturno, debe hacer preflight y `STOP / WAIT_FOR_ASSIGNMENT`, no escoger trabajo por sí mismo.

## JOBS — rutina

1. Preflight factual de baseline/gates/handoffs/PRs/CI.
2. Leer el resultado más reciente de AAA/BBB/WOZ e Issue #41.
3. Procesar DONE/PASS/integraciones solo con evidencia aplicable.
4. Mantener scope claro y evitar duplicación/overlap.
5. Actualizar estado confirmado en Plan/fases/Registro.
6. Recalcular camino crítico F0→F4 desde cero.
7. Reasignar explícitamente cuando el retorno global sea mayor.
8. Escalar blockers externos sin falsear PASS.

JOBS no toca producto/infra ni mergea código BeatGaler cuando la integración pertenece al owner técnico.

## Owner — paquete mínimo

```text
ROLE: WOZ | AAA | BBB
AREA: <área fija del Assignment ID>
TASK: <tarea exacta>
BASE: <rama/SHA>
SCOPE: <sí>
OUT_OF_SCOPE: <no>
CHANGES: <implementación/audit>
TESTS: <pruebas propias>
CI: <runs/checks>
EVIDENCE: <SHA/PR/runtime>
UNVERIFIED: <lista>
BLOCKERS: <none/lista>
NEXT_WITHIN_AREA: <siguiente paso>
```

Reglas:
- cambio de producto → rama/PR propia o artifact existente reutilizado;
- duplicate-check antes de crear artefacto;
- el owner corrige sus regresiones y añade pruebas de aceptación de su área;
- findings fuera de scope se reportan; JOBS decide owner;
- no mergear/cerrar globalmente sin autoridad aplicable;
- tests propios no bastan si falta requisito literal del gate.

# Modo autónomo / turno nocturno

## 1. Preflight factual obligatorio

Verificar:
- área/tarea exacta vigente en `NOCHE - <ROL>.md`;
- baseline/rama/SHA;
- Plan Maestro + fase aplicable + Registro + Issue #41 reciente;
- dependencias literales;
- PR/rama existente antes de crear otra;
- últimos findings/handoffs;
- CI relevante;
- si el Assignment ID ya fue procesado.

Dato material no verificable → **STOP / PENDING**. Ausencia de asignación activa → **STOP / WAIT_FOR_ASSIGNMENT**.

## 2. Idempotencia / REUSE-FIRST

Antes de rama/PR/comentario/commit:
1. buscar artefacto/evidencia existente de la misma pieza/baseline;
2. continuar ahí o no-op;
3. nunca crear copia por nuevo ciclo;
4. no repetir drill/CI productivo solo para recrear evidencia aceptada.

## 3. Evidence-before-claim / exact-head

No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff aplicable.

Si cambia el head o la combinación material con integración, el verde anterior no prueba la combinación nueva: refresh + CI exact-head aplicable antes de merge/claim.

Lo no probado = `UNVERIFIED` o `PENDING`.

## 4. Owner self-test

El owner es responsable de unit/integration/DOM/runtime que correspondan, regresiones de su cambio y CI exact-head aplicable. Revisiones independientes obligatorias posteriores no desaparecen por self-test.

## 5. STOP conditions

STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante:
- contradicción material Plan/Issue/GitHub/runtime;
- baseline inesperado que invalida evidencia;
- cambio destructivo fuera de scope;
- secretos/credenciales fuera de procedimiento;
- decisión reservada al RO;
- necesidad real de ampliar alcance;
- CI externo no atribuible;
- evidencia insuficiente para gate;
- ausencia de asignación activa explícita.

**BLOCKED no cambia el owner automáticamente.**

## 6. Corrective assignment

2 ciclos sin progreso → JOBS precisa la orden dentro de la misma área. 3 ciclos sin progreso → `STALLED`. Reasignación solo si JOBS/RO lo decide explícitamente. Progreso parcial real reinicia la evaluación de estancamiento, pero no sustituye evidencia de cierre.

## 7. Gate transaction

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
END AI-HANDOFF
```

## Night Shift Ledger — CYCLE 007

```text
JOBS: CYCLE 007 complete; baseline f0d65aa...; assignments 008 issued
AAA: F2/12.1 -> NIGHT-AAA-008; PR #58 d7cc93f mergeable + Required CI green; integrate then atomic empty-index
BBB: F4/24.2 -> NIGHT-BBB-008; PR #57 4e251cae exact-head Required CI/D6/D7 green; integrate then 25.1 audit
WOZ: F3/16.1 -> NIGHT-WOZ-008; PR #59 292a7706 D6/D7/compile green, Desktop Portability still pending at JOBS preflight; then 16.2 software-only
D10.1: PENDING_EXTERNAL_PROOF only; no technical worker overlap
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted to PASS
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; AAA full owner 12.1 bajo `NIGHT-AAA-008`.
- **F3:** WOZ full owner 16.x técnico bajo `NIGHT-WOZ-008`; no nueva infra/costo sin RO.
- **F4:** 21.1/21.2/24.1 cerrados; BBB full owner #57/24.2→25.1 bajo `NIGHT-BBB-008`; D22/D23 externos.
- **JOBS:** coordinación/plan; sin producto/infra.

**Principio:** cada constructor termina y prueba su pieza; al terminar espera una nueva asignación en vez de saltar solo a otra tarea salvo que la misma asignación contenga explícitamente el siguiente sub-slice condicionado.
