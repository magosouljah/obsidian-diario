# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — órdenes CYCLE 015

| Rol | Owner actual | Responsabilidad |
|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra |
| **AAA** | F2 / 12.1 SAME #64 merge + residual | `NIGHT-AAA-015`: owner race-check/merge de #64 exact-head green; después pagination/window/memory si merge demostrado |
| **BBB** | F4 / 25.1 SAME #63 Windows import | `NIGHT-BBB-015`: corregir marker-safe glue F4, refresh SAME lineage, functional PASS + fresh exact-head CI; no segundo slice |
| **WOZ** | F3 / 17.1 | `NIGHT-WOZ-015`: Stripe Checkout server-side software-only con IDs/precios estables, idempotency y anti-tamper; sin credenciales/costo |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar roadmap, pero un cambio de owner/scope es explícito.

**Baseline canónico al cierre JOBS CYCLE 014:** `integration-v0.8.0-alpha.1 @ 55e0d8759ec03b23fa8e4f1f35304922dffeb992`. GitHub vivo manda si cambia después.

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

## Night Shift Ledger — CYCLE 014

```text
JOBS: baseline advanced to 55e0d875... via verifiable merge #61
AAA: #64 @ 3e7fd0a0... base 55e0d875..., Required CI 33272883660 SUCCESS, mergeable -> NIGHT-AAA-015 owner merge + residual
BBB: #63 @ 9208ead249... Windows Import 33272794199 FAILURE before specs due F4 marker mismatch; stale vs 55e0d875... -> NIGHT-BBB-015 corrective+refresh
WOZ: #61 merged 55e0d875...; 16.2 SOFTWARE DONE / EXTERNAL TAIL -> NIGHT-WOZ-015 F3/17.1 software-only
D10.1: PENDING_EXTERNAL_PROOF only; no technical worker overlap
F3/16.1 physical separation: PENDING_EXTERNAL
D22/D23: PENDING_EXTERNAL
DUPLICATE_WORK: PR #62 remains CLOSED/NOT MERGED; no active duplicate owner
UNVERIFIED_CLAIMS: none promoted to PASS
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; AAA owner exclusivo de #64 transaction bajo `NIGHT-AAA-015`; 12.1 sigue abierto.
- **F3:** 16.1/16.2 software integrado con external tails; WOZ owner exclusivo de 17.1 bajo `NIGHT-WOZ-015`; 17.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrado; BBB owner exclusivo de #63 corrective bajo `NIGHT-BBB-015`; D22/D23 externos; 25.2 abierto.
- **JOBS:** coordinación/plan; sin producto/infra.
