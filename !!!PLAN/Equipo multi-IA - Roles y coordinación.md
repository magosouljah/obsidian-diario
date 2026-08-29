# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 021

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 12.1 residual | `NIGHT-AAA-021`: cold/warm cuantificado + taxonomy/state residual, REUSE-FIRST | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-020`: refresh a baseline vivo + corrective mínimo session/bootstrap + Windows Import literal PASS/fresh CI | `NONE` |
| **WOZ** | F3 / 17.2 SAME #67 | `NIGHT-WOZ-020`: refresh a baseline vivo + preservar recovery corrective + fresh exact-head CI + merge si verde | `NONE` |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar roadmap, pero un cambio de owner/scope es explícito.

**Baseline canónico CYCLE 021:** `integration-v0.8.0-alpha.1 @ 712b49b6689a31a47902dbe95e98622d001dab40`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum. F3/16.1 physical staging/prod separation continúa external-only. F3/16.2 software está DONE/INTEGRATED por #61 pero deploy/staging/rollback reales continúan externos. D22/D23 signing/notarization siguen externos.

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

## Night Shift Ledger — CYCLE 021

```text
JOBS: integration moved by #66 to 712b49b6689a31a47902dbe95e98622d001dab40; Plan synced and new monotonic assignments emitted
AAA: NIGHT-AAA-020 DONE -> #66 merged 712b49b...; NIGHT-AAA-021 ASSIGNED -> residual 12.1 cold/warm + taxonomy/state; CI-FALLBACK NONE
BBB: NIGHT-BBB-019 PENDING -> baseline STOP + DevToolsActivePort session diagnosis; NIGHT-BBB-020 ASSIGNED -> SAME #63 refresh + F4 corrective + literal PASS/fresh CI; CI-FALLBACK NONE
WOZ: NIGHT-WOZ-019 PENDING/WAITING_CI -> corrective 8a534111...; JOBS recheck found all fresh head CI SUCCESS; NIGHT-WOZ-020 ASSIGNED -> SAME #67 refresh + fresh exact-head CI + merge if green; CI-FALLBACK NONE
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
- **F2:** 11.1/11.2/12.2 cerrados; #66 integrado; AAA owner exclusivo del residual 12.1 bajo `NIGHT-AAA-021`.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1 SOFTWARE DONE/INTEGRATED; WOZ owner exclusivo de SAME #67 bajo `NIGHT-WOZ-020`; 17.2 sigue abierto hasta fresh-base integration.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrado; BBB owner exclusivo de SAME #63 bajo `NIGHT-BBB-020`; D22/D23 externos; 25.1/25.2 abiertos.
- **JOBS:** coordinación/plan; sin producto/infra.
