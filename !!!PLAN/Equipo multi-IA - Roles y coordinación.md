# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son la memoria compartida. El modelo operativo es **ROMPECABEZAS CON OWNER FIJO**. GitHub/runtime más reciente prevalece sobre snapshots viejos.

## Roles y ownership actual — CYCLE 029

| Rol | Owner actual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| **JOBS** | coordinación | `!!!PLAN`, prioridades, owners, handoffs, gates; no código BeatGaler/infra | n/a |
| **AAA** | F2 / 13.1 Web-only SAME #69 | `NIGHT-AAA-029`: confirmar/wirear Save All productivo y merge solo con evidencia/fresh CI si cambia head | `NONE` |
| **BBB** | F4 / 25.1 SAME #63 | `NIGHT-BBB-028`: promover windows/import, fresh exact-head gates, race-check/merge | `NONE` |
| **WOZ** | F2 / 13.1 server SAME #70 | `NIGHT-WOZ-028`: atribuir/fijar Required CI PostgreSQL failure y integrar solo si exact-head green | `NONE` |

**Holding item:** F3/18.1 PR #68 permanece técnicamente owned por WOZ pero frozen/bloqueado por execution layer; no mutación activa sobre #68 en este ciclo.

**Baseline canónico CYCLE 029:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

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

## Night Shift Ledger — CYCLE 029

```text
JOBS: integration sigue 3ad8f55a...; release NO-GO
AAA: NIGHT-AAA-028 no result observable -> superseded; NIGHT-AAA-029 SAME #69 product wiring; fallback NONE
BBB: NIGHT-BBB-027 no result observable -> superseded; NIGHT-BBB-028 SAME #63 promotion/fresh-CI/merge; fallback NONE
WOZ: NIGHT-WOZ-027 produced #70 @ 5a99ebf2...; focused F2 run 33304798320 SUCCESS; Required CI 33304798363 FAILURE in PostgreSQL live/recovery gate; NIGHT-WOZ-028 assigned attribution/fix; fallback NONE
F3/18.1: #68 frozen exact-head green / external merge execution blocker
D10.1: PENDING_EXTERNAL_PROOF only
F2/12.1: cold/warm runtime evidence only
F3/16.1+16.2: external tails
D22/D23: PENDING_EXTERNAL
DUPLICATE_WORK: none
UNVERIFIED_CLAIMS: none promoted
RELEASE: NO-GO
```

## Estado vigente

- **F0:** técnico habilitado; 1.2/2.2 tails externos `[ 🟡 ]`.
- **F1:** D6–D9 PASS; D10.1 external-only; D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm real; 13.1 AAA #69 + WOZ #70 sin overlap; #70 focused PASS pero Required CI rojo.
- **F3:** 16.1/16.2 software integrado con external tails; 17.1/17.2 integrados; #68 exact-head green pero merge execution blocked.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; Windows Import literal PASS existe en #63; promotion/fresh-CI/merge pendiente; otros gaps siguen honestos.
- **JOBS:** coordinación/plan; sin producto/infra.
