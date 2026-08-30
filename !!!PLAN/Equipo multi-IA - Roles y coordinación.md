# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 024

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 13.1 | `NIGHT-AAA-024`: Save All durable + partial summary; bulk conflict-safe/honest disable; garbage journal | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-023`: current failure causal + corrective mínimo harness + Windows Import literal PASS | `NONE` |
| **WOZ** | F3 / 18.1 software | `NIGHT-WOZ-023`: limits/entitlements server-side + race-safe reservation + portal/subscription-state contract | `NONE` |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar roadmap, pero un cambio de owner/scope es explícito.

**Baseline canónico CYCLE 024:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum. F3/16.1 physical staging/prod separation continúa external-only. F3/16.2 software está DONE/INTEGRATED pero deploy/staging/rollback reales continúan externos. D22/D23 signing/notarization siguen externos.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando las dependencias reales lo permiten.
2. Cada implementación/pieza material tiene un solo owner estable por ciclo.
3. El owner hace preflight → implementación/audit → tests → fixes → CI → handoff.
4. Findings de otro agente son input; no transfieren ownership automáticamente.
5. No hay hopping automático entre tareas.
6. Si un owner queda bloqueado, reporta `BLOCKED`; JOBS decide si reasigna o amplía scope.
7. Revisión independiente adicional existe solo por orden JOBS/RO o gate literal.
8. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
9. Ningún gate se marca `[x]` sin evidencia verificable.
10. Dependency-ready no equivale a assigned.

## Modo autónomo / turno nocturno

### Preflight factual obligatorio
Verificar asignación vigente, baseline/rama/SHA, Plan Maestro + fase + Registro + Issue #41, dependencias, PR/rama existente, handoffs, CI y si el Assignment ID ya fue procesado. Dato material no verificable → `STOP / PENDING`. Sin asignación → `WAIT_FOR_ASSIGNMENT`.

### Idempotencia / REUSE-FIRST
Antes de rama/PR/comentario/commit: buscar artefacto/evidencia existente; continuar ahí o no-op; nunca duplicar por nuevo ciclo; no repetir drill/CI productivo solo para recrear evidencia aceptada.

### Evidence-before-claim / exact-head
No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff aplicable. Si cambia head o combinación material, refresh + CI aplicable sobre la combinación vigente.

### PRIMARY / CI-FALLBACK
- `PRIMARY` siempre se ejecuta primero.
- `CI-FALLBACK` solo existe si JOBS lo preautoriza explícitamente y solo puede empezar cuando PRIMARY entra realmente en `WAITING_CI` o `WAITING_EXTERNAL`.
- Fallback debe ser independiente: distintos archivos/rama/PR/ownership material, no depender del PRIMARY, no adelantar un gate bloqueado, no duplicar otro owner y no ampliar alcance.
- Cada fallback autorizado debe declarar scope exacto, evidencia requerida y STOP condition.
- Si no existe fallback seguro y útil: `CI-FALLBACK: NONE`.
- El worker nunca inventa fallback. Después de usar uno debe releer PRIMARY antes de cerrar el turno.

### STOP conditions
STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante contradicción material, baseline inesperado, cambio destructivo, secretos fuera de procedimiento, decisión RO, scope creep, CI externo no atribuible, evidencia insuficiente o ausencia de asignación.

### Corrective assignment
2 ciclos sin progreso → JOBS precisa la orden dentro de la misma área. 3 ciclos sin progreso → `STALLED`. Progreso parcial real reinicia evaluación. Un blocker de autoridad demostrado puede resolverse con ampliación explícita de scope/owner.

### Handoff mínimo
```text
AI-HANDOFF
ROLE: WOZ | AAA | BBB | JOBS
AREA:
TASK:
BASE_BEFORE:
HEAD_AFTER:
STATUS: DONE | BLOCKED | FINDING | STALLED | PENDING
CHANGES:
TESTS:
CI:
EVIDENCE:
UNVERIFIED:
BLOCKERS:
NEXT_WITHIN_AREA:
END AI-HANDOFF
```

## Night Shift Ledger — CYCLE 024

```text
JOBS: no new product merge since #67; integration remains 3ad8f55a...; prior unprocessed assignments superseded monotonically
AAA: NIGHT-AAA-023 NOT_PROCESSED -> NIGHT-AAA-024 ASSIGNED F2/13.1; CI-FALLBACK NONE
BBB: NIGHT-BBB-022 NOT_PROCESSED -> NIGHT-BBB-023 ASSIGNED SAME #63 corrective; CI-FALLBACK NONE
WOZ: NIGHT-WOZ-022 NOT_PROCESSED -> NIGHT-WOZ-023 ASSIGNED F3/18.1 software; CI-FALLBACK NONE
D10.1: PENDING_EXTERNAL_PROOF only
F2/12.1: cold/warm runtime evidence only
F3/16.1 physical separation: PENDING_EXTERNAL
D22/D23: PENDING_EXTERNAL
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 abierto solo por cold/warm real; AAA owner exclusivo de D13.1 bajo `NIGHT-AAA-024`.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1/17.2 software integrados; WOZ owner exclusivo de 18.1 bajo `NIGHT-WOZ-023`.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrado; BBB owner exclusivo de SAME #63 bajo `NIGHT-BBB-023`; Windows Import sigue `NOT_COVERED`; D22/D23 externos; 25.1/25.2 abiertos.
- **JOBS:** coordinación/plan; sin producto/infra.
