# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 008

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra |
| **AAA** | F2 / 12.1 | `NIGHT-AAA-009`: refresh SAME PR #58 sobre baseline vivo, CI exact-head/merge-candidate, merge protegido; luego atomic empty-index únicamente |
| **BBB** | F4 / 25.1 | `NIGHT-BBB-009`: matrix/runner dependency-safe reutilizando harnesses existentes; no fixes F2/F3 |
| **WOZ** | F3 / 16.1 → 16.2 | `NIGHT-WOZ-009`: cerrar #59 con exact-head verde; luego promotion contract software-only |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar el roadmap, pero un cambio de owner es una decisión explícita.

**Baseline canónico CYCLE 008:** `integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum; ningún worker técnico es owner de esa acción externa.

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

## Night Shift Ledger — CYCLE 008

```text
JOBS: CYCLE 008 complete; baseline f73c9ee...; assignments 009 issued
AAA: NIGHT-AAA-008 STALLED on stale #58 merge-candidate Required CI; -> NIGHT-AAA-009 refresh SAME PR against f73c9ee, CI, merge, then atomic empty-index
BBB: NIGHT-BBB-008 DONE; #57 merged f73c9ee...; 24.2 CLOSED; -> NIGHT-BBB-009 F4/25.1 matrix/runner dependency-safe
WOZ: NIGHT-WOZ-008 PENDING_CI; after turn CI completed SUCCESS on #59 head 0e0bf188...; -> NIGHT-WOZ-009 race-check/merge then 16.2 software-only
D10.1: PENDING_EXTERNAL_PROOF only; no technical worker overlap
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted to PASS
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; AAA full owner 12.1 bajo `NIGHT-AAA-009`.
- **F3:** WOZ full owner 16.x técnico bajo `NIGHT-WOZ-009`; no nueva infra/costo sin RO.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; BBB full owner 25.1 bajo `NIGHT-BBB-009`; D22/D23 externos.
- **JOBS:** coordinación/plan; sin producto/infra.
