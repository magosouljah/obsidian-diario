# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 012

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra |
| **AAA** | F2 / 12.1 atomic bootstrap vertical slice | `NIGHT-AAA-013`: ownership ampliado explícitamente al control plane/backend mínimo + Web wire; create-if-absent/CAS/idempotency/fail-closed; no pagination/window/memory/cold-warm |
| **BBB** | F4 / 25.1 residual funcional | `NIGHT-BBB-013`: matriz #60 ya integrada; cerrar un slice dependency-safe `NOT_COVERED` con evidencia funcional real; no 25.2 ni fixes F2/F3 |
| **WOZ** | F3 / 16.2 | `NIGHT-WOZ-013`: SAME #61 refresh sobre baseline vivo, exact-head CI nuevo y protected merge si race-check; no Stripe/infra real |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar el roadmap, pero un cambio de owner/scope es una decisión explícita.

**Baseline canónico CYCLE 012 al preflight:** `integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`, merge verificable de PR #60. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum; ningún worker técnico es owner de esa acción externa. F3/16.1 runtime software quedó integrado por #59, pero physical staging/prod separation continúa external-only. D22/D23 signing/notarization siguen externos.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando las dependencias reales lo permiten.
2. Cada implementación/pieza material tiene un owner estable por ciclo.
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

### STOP conditions
STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante contradicción material, baseline inesperado, cambio destructivo, secretos fuera de procedimiento, decisión RO, scope creep, CI externo no atribuible, evidencia insuficiente o ausencia de asignación.

### Corrective assignment
2 ciclos sin progreso → JOBS precisa la orden dentro de la misma área. 3 ciclos sin progreso → `STALLED`. Progreso parcial real reinicia evaluación. Un blocker de autoridad demostrado puede resolverse con ampliación explícita de scope/owner por JOBS, como `NIGHT-AAA-013`.

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

## Night Shift Ledger — CYCLE 012

```text
JOBS: baseline 7de7b57a...; #60 integrated; AAA-012 BLOCKED validly; #61 stale/OPEN after baseline movement; assignments 013 issued
AAA: NIGHT-AAA-012 BLOCKED -> no atomic primitive in Web lineage -> NIGHT-AAA-013 explicit control-plane/backend scope + Web wire
BBB: NIGHT-BBB-012 DONE -> #60 merged 7de7b57a... -> NIGHT-BBB-013 one dependency-safe functional coverage slice
WOZ: NIGHT-WOZ-012 PENDING_CI_REFRESH -> old green invalid for post-#60 combination -> NIGHT-WOZ-013 SAME #61 refresh + fresh exact-head CI + merge
D10.1: PENDING_EXTERNAL_PROOF only; no technical worker overlap
F3/16.1 physical separation: PENDING_EXTERNAL
D22/D23: PENDING_EXTERNAL
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted to PASS
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; AAA owner exclusivo del atomic bootstrap 12.1 bajo `NIGHT-AAA-013` con scope control-plane explícito.
- **F3:** 16.1 runtime software integrado; physical separation external; WOZ owner 16.2 bajo `NIGHT-WOZ-013`; #61 necesita refresh/CI nuevo antes de merge.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix artifact integrado; BBB owner exclusivo de un residual funcional 25.1 bajo `NIGHT-BBB-013`; D22/D23 externos.
- **JOBS:** coordinación/plan; sin producto/infra.
