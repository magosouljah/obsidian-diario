# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 032

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 12.1 runtime evidence | `NIGHT-AAA-032`: harness cold/warm Web real reproducible; #69 frozen | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-031`: final exact-head race/merge transaction on green head `7a6b7443...` | `NONE` |
| **WOZ** | F2 / 13.1 server SAME #70 | `NIGHT-WOZ-031`: live-PG fixture corrective autorizado + fresh focused/Required CI + merge if green | `NONE` |

**Holding items:**
- F2/13.1 Web PR #69 permanece owned por AAA pero frozen por `STOP_WRITE_SURFACE`; no reemplazar ni duplicar.
- F3/18.1 PR #68 permanece owned técnicamente por WOZ pero frozen/bloqueado por execution layer; no mutación activa en CYCLE 032.

**Baseline canónico CYCLE 032:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

## Modelo ROMPECABEZAS CON OWNER FIJO

1. Trabajo cross-phase permitido cuando dependencias reales lo permiten.
2. Cada pieza material tiene un solo owner por ciclo.
3. Owner hace preflight → implementación/audit → tests → fixes → CI → handoff.
4. Findings no transfieren ownership automáticamente.
5. No hopping automático.
6. Bloqueo real → worker reporta; JOBS reasigna/amplía explícitamente.
7. Revisión independiente solo por orden JOBS/RO o gate literal.
8. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
9. Ningún `[x]` sin evidencia verificable.
10. Dependency-ready no equivale a assigned.

## Modo autónomo / turno nocturno

### Preflight factual obligatorio
Verificar asignación, baseline/rama/SHA, Plan Maestro + fase + Registro + Issue #41, dependencias, PR/rama, handoffs, CI y duplicate-check. Dato material no verificable → `STOP / PENDING`. Sin asignación → `WAIT_FOR_ASSIGNMENT`.

### Idempotencia / REUSE-FIRST
Antes de rama/PR/comentario/commit buscar artifact/evidencia existente; continuar ahí o no-op; nunca duplicar por nuevo ciclo; no repetir drill/CI aceptado solo para recrear evidencia.

### Evidence-before-claim / exact-head
No afirmar DONE/PASS/corregido/integrado/cerrado sin SHA/PR/test/CI/runtime/handoff aplicable. Cambio material de head/combinación → refresh + CI aplicable.

### PRIMARY / CI-FALLBACK
- PRIMARY primero.
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente en WAITING_CI/WAITING_EXTERNAL.
- Debe ser independiente en archivos/rama/PR/ownership/dependencias, no adelantar gate, duplicar owner ni ampliar alcance.
- Si no existe fallback seguro: `CI-FALLBACK: NONE`.
- Worker nunca inventa fallback.

### STOP conditions
STOP/BLOCKED/STALLED/RO DECISION REQUIRED ante contradicción material, baseline inesperado, cambio destructivo, secretos fuera de procedimiento, decisión RO, scope creep, CI externo no atribuible, evidencia insuficiente o ausencia de asignación.

## Night Shift Ledger — CYCLE 032

```text
JOBS: integration sigue 3ad8f55a...; release NO-GO
AAA: NIGHT-AAA-031 PENDING/STOP_WRITE_SURFACE; #69 frozen; NIGHT-AAA-032 -> 12.1 cold/warm runtime harness; fallback NONE
BBB: NIGHT-BBB-030 PENDING/WAITING_CI -> JOBS recheck resolved all fresh exact-head gates green on 7a6b7443...; NIGHT-BBB-031 final race/merge; fallback NONE
WOZ: NIGHT-WOZ-030 no result observable; #70 unchanged; NIGHT-WOZ-031 SAME attributed fixture corrective; fallback NONE
F3/18.1: #68 frozen exact-head green / external merge execution blocker
D10.1: PENDING_EXTERNAL_PROOF only
F2/12.1: AAA active on cold/warm runtime evidence
F2/13.1 Web: #69 frozen; server #70 active
F3/16.1+16.2: external tails
D22/D23: PENDING_EXTERNAL
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 AAA runtime residual; 13.1 Web #69 frozen + server #70 corrective activo.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1/17.2 integrados; #68 exact-head green pero merge execution blocked.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #63 exact-head green y pendiente solo de race/merge; otros gaps permanecen honestos.
- **JOBS:** coordinación/plan; sin producto/infra.
