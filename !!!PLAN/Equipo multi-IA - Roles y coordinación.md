# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 026

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 13.1 Web-only | `NIGHT-AAA-026`: Save All + partial summary + bulk conflict-safe usando durable/CAS existente; server garbage-journal fuera de scope | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-025`: launcher/session corrective mínimo sobre failure `33300992453`; Windows Import literal PASS | `NONE` |
| **WOZ** | F3 / 18.1 PR #68 | `NIGHT-WOZ-025`: final exact-head integration transaction for #68 | `NONE` |

RO conserva alcance de producto, riesgo aceptado, decisiones/credenciales externas y go/no-go público. JOBS puede reorganizar roadmap, pero un cambio de owner/scope es explícito.

**Baseline canónico CYCLE 026:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`. GitHub vivo manda si cambia después.

D10.1 permanece external-only por copia real off-provider/off-account + read/checksum. F3/16.1 physical staging/prod separation continúa external-only. F3/16.2 software DONE/INTEGRATED con deploy/staging/rollback reales externos. D22/D23 signing/notarization externos. F2/13.1 tiene boundary explícito: AAA posee carril Web; server half durable orphan-journal queda sin owner técnico asignado en este ciclo y no se falsea como cerrado.

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

## Night Shift Ledger — CYCLE 026

```text
JOBS: integration remains 3ad8f55a...; #68 still exact-head green/open; #63 advanced to ed03b806... but Windows Import 33300992453 failed before assertions
AAA: NIGHT-AAA-025 PENDING/STOP_OWNERSHIP_BOUNDARY -> NIGHT-AAA-026 ASSIGNED Web-only Save All/bulk; server orphan-journal boundary preserved; fallback NONE
BBB: NIGHT-BBB-024 WAITING_CI -> JOBS recheck FAILURE -> NIGHT-BBB-025 ASSIGNED SAME #63 launcher/session corrective; fallback NONE
WOZ: NIGHT-WOZ-024 no result -> superseded; NIGHT-WOZ-025 ASSIGNED SAME #68 final integration; fallback NONE
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
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm real; AAA owner exclusivo de Save All/bulk Web de 13.1 bajo `NIGHT-AAA-026`; server orphan-journal no asignado.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1/17.2 integrados; #68 exact-head green y WOZ owner exclusivo de integración bajo `NIGHT-WOZ-025`.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrado; BBB owner exclusivo SAME #63 bajo `NIGHT-BBB-025`; Windows Import `NOT_COVERED`; D22/D23 externos; 25.1/25.2 abiertos.
- **JOBS:** coordinación/plan; sin producto/infra.
