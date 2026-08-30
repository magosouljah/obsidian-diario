# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 027

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 13.1 Web-only | `NIGHT-AAA-027`: Save All + partial summary + bulk conflict-safe usando durable/CAS existente; server garbage-journal fuera de scope | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-026`: launcher/session corrective mínimo sobre failure `33300992453`; Windows Import literal PASS | `NONE` |
| **WOZ** | F2 / 13.1 server half | `NIGHT-WOZ-026`: garbage journal/orphan reconciliation Web-callable durable, REUSE-FIRST; frontend AAA fuera de scope | `NONE` |

**Holding item:** F3/18.1 PR #68 permanece owned técnicamente por WOZ pero frozen/bloqueado por execution layer después de `NIGHT-WOZ-025`; no existe owner concurrente ni mutación activa sobre #68 en CYCLE 027.

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar roadmap, pero un cambio de owner/scope es explícito.

**Baseline canónico CYCLE 027:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum. F3/16.1 physical staging/prod separation continúa external-only. F3/16.2 software DONE/INTEGRATED con deploy/staging/rollback reales externos. D22/D23 signing/notarization externos. F2/13.1 tiene boundary explícito y owners separados: AAA=Web Save All/bulk; WOZ=server garbage journal/orphan cleanup.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Se puede trabajar cross-phase cuando dependencias reales lo permiten.
2. Cada implementación/pieza material tiene un solo owner por ciclo.
3. Owner hace preflight → implementación/audit → tests → fixes → CI → handoff.
4. Findings de otro agente son input; no transfieren ownership automáticamente.
5. No hopping automático.
6. Si owner queda bloqueado, reporta `BLOCKED/PENDING`; JOBS decide reasignación/ampliación explícita.
7. Revisión independiente adicional solo por orden JOBS/RO o gate literal.
8. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
9. Ningún gate `[x]` sin evidencia verificable.
10. Dependency-ready no equivale a assigned.

## Modo autónomo / turno nocturno

### Preflight factual obligatorio
Verificar asignación, baseline/rama/SHA, Plan Maestro + fase + Registro + Issue #41, dependencias, PR/rama, handoffs, CI y duplicate-check. Dato material no verificable → `STOP / PENDING`. Sin asignación → `WAIT_FOR_ASSIGNMENT`.

### Idempotencia / REUSE-FIRST
Antes de rama/PR/comentario/commit buscar artefacto/evidencia existente; continuar ahí o no-op; nunca duplicar por nuevo ciclo; no repetir drill/CI aceptado solo para recrear evidencia.

### Evidence-before-claim / exact-head
No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff aplicable. Cambio material de head/combinación → refresh + CI aplicable.

### PRIMARY / CI-FALLBACK
- PRIMARY primero.
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente en WAITING_CI/WAITING_EXTERNAL.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias, no adelantar gate, duplicar owner ni ampliar alcance.
- Si no existe fallback seguro: `CI-FALLBACK: NONE`.
- Worker nunca inventa fallback.

### STOP conditions
STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante contradicción material, baseline inesperado, cambio destructivo, secretos fuera de procedimiento, decisión RO, scope creep, CI externo no atribuible, evidencia insuficiente o ausencia de asignación.

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

## Night Shift Ledger — CYCLE 027

```text
JOBS: integration remains 3ad8f55a...; #68 merge attempt blocked by execution layer, no merge; #63 still Windows Import failure
AAA: NIGHT-AAA-026 no result -> superseded; NIGHT-AAA-027 ASSIGNED Web Save All/bulk; fallback NONE
BBB: NIGHT-BBB-025 no result -> superseded; NIGHT-BBB-026 ASSIGNED SAME #63 launcher/session corrective; fallback NONE
WOZ: NIGHT-WOZ-025 BLOCKED/MERGE_TOOL_REJECTED -> NIGHT-WOZ-026 ASSIGNED F2 server garbage-journal half; #68 frozen; fallback NONE
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
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm real; 13.1 con AAA Web + WOZ server, owners explícitos/no-overlap.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1/17.2 integrados; #68 exact-head green pero merge execution blocked, no 18.1 closure.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrado; BBB owner SAME #63 bajo `NIGHT-BBB-026`; Windows Import `NOT_COVERED`; D22/D23 externos; 25.1/25.2 abiertos.
- **JOBS:** coordinación/plan; sin producto/infra.
