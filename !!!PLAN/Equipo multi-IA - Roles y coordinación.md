# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 009

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra |
| **AAA** | F2 / 12.1 | `NIGHT-AAA-010`: SAME PR #58 refresh sobre baseline vivo, CI exact-head/merge-candidate, merge protegido; luego atomic empty-index únicamente |
| **BBB** | F4 / 25.1 | `NIGHT-BBB-010`: SAME PR #60; diagnosticar Desktop Portability failure, refresh/fix mínimo, CI completo; no fixes F2/F3 |
| **WOZ** | F3 / 16.2 | `NIGHT-WOZ-010`: promotion/deploy contract software-only REUSE-FIRST; no provider resources/costo/deploy real |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar el roadmap, pero un cambio de owner es una decisión explícita.

**Baseline canónico CYCLE 009:** `integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum; ningún worker técnico es owner de esa acción externa. F3/16.1 runtime software quedó integrado por #59, pero physical staging/prod separation continúa external-only.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando las dependencias reales lo permiten.
2. Cada implementación/pieza material tiene un owner estable por ciclo.
3. El owner hace preflight → implementación/audit → tests → fixes → CI → handoff.
4. Findings de otro agente son input; no transfieren ownership automáticamente.
5. No hay hopping automático entre tareas.
6. Si un owner queda bloqueado, reporta `BLOCKED`; JOBS decide si reasigna.
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
2 ciclos sin progreso → JOBS precisa la orden dentro de la misma área. 3 ciclos sin progreso → `STALLED`. Progreso parcial real reinicia evaluación.

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

## Night Shift Ledger — CYCLE 009

```text
JOBS: CYCLE 009 preflight complete; baseline be9e58c...; #59 processed integrated; assignments 010 issued
AAA: NIGHT-AAA-009 had no verified result; integration advanced -> NIGHT-AAA-010 SAME #58 refresh + CI + merge, then atomic empty-index
BBB: NIGHT-BBB-009 produced #60; matrix/D6/D7 green but Desktop Portability 33260592774 FAILURE and base stale -> NIGHT-BBB-010 SAME #60 diagnose/refresh/fix/CI
WOZ: NIGHT-WOZ-009 PENDING_EXTERNAL; #59 merged be9e58c...; runtime software 16.1 integrated -> NIGHT-WOZ-010 F3/16.2 software-only
D10.1: PENDING_EXTERNAL_PROOF only; no technical worker overlap
F3/16.1 physical separation: PENDING_EXTERNAL
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted to PASS
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; AAA full owner 12.1 bajo `NIGHT-AAA-010`.
- **F3:** 16.1 runtime software integrado; physical separation external; WOZ full owner 16.2 técnico bajo `NIGHT-WOZ-010`; no nueva infra/costo sin RO.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; BBB full owner 25.1 bajo `NIGHT-BBB-010`; #60 no está integration-ready por portability failure + stale base; D22/D23 externos.
- **JOBS:** coordinación/plan; sin producto/infra.
