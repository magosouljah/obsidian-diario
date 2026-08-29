# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 018

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.
- Live GitHub reread: sigue siendo merge #65; no apareció merge posterior durante este preflight.
- Release público: 🔴 `NO-GO`.
- F0: 1.2 y 2.2 tails externos/administrativos; trabajo técnico interno habilitante ya cerrado.
- F1: D6/D7/D8/D9 PASS; D10.1 external-only por off-provider/off-account copy + read/checksum; D10.2 decisión RO.
- F2: SAME #66 ya fue refrescado al baseline vivo; paging/windowing avanzó, pero producción React todavía no invoca next/previous/cursor y 12.1 sigue abierto.
- F3: 17.1 SOFTWARE DONE/INTEGRATED; `NIGHT-WOZ-018` continúa ASSIGNED porque no existe todavía un resultado verificable 018 en su ledger/Issue/PR.
- F4: SAME #63 ya fue refrescado al baseline vivo; Windows Import + Required CI siguen en curso; `windows/import` continúa NOT_COVERED hasta PASS literal.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-018` — PENDING
- SAME PR #66 live head `2d9a9ae89f4594b8b72a36dcc835f92b1017bf15`, base `ed6aab7e...`, OPEN/mergeable.
- Implementó `WebLibraryWindowConsumer` bounded current/next/previous/refresh, refresh/invalidation seguro, métricas de materialización y cobertura sintética 10,321 beats sin dup/omission y sin artwork eager.
- Gap material restante: el consumer React productivo aún no invoca next/previous/cursor; current/refresh sí están cableados.
- Exact-head actual: D6 `33277816072` SUCCESS; D7 `33277816068` SUCCESS; Desktop Portability `33277816133` IN_PROGRESS; Upgrade `33277816097` SKIPPED.
- No merge autorizado. Nueva orden: `NIGHT-AAA-019` SAME #66 para production navigation + focused PASS + fresh exact-head/race-check.

### BBB / `NIGHT-BBB-017` — PENDING
- SAME PR #63 live head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`, base `ed6aab7e...`, OPEN/Ready/mergeable.
- Corrigió únicamente bootstrap/tooling: volvió a `driverProvider=official`, `autoInstallTauriDriver=true`, `autoDownloadEdgeDriver=true`; no producto F2/F3.
- Exact-head actual: F4 Matrix `33277733635` SUCCESS; D6 `33277733621` SUCCESS; D7 `33277733651` SUCCESS; Windows Import `33277733650` IN_PROGRESS; Desktop Portability `33277733647` IN_PROGRESS; Upgrade `33277733677` SKIPPED.
- `windows/import` sigue `NOT_COVERED`; no merge autorizado aún.
- Nueva orden: `NIGHT-BBB-018` SAME #63. Reuse runs: PASS→race-check/promote/merge; FAIL→fix mínimo guiado por log. No 25.2.

### WOZ / `NIGHT-WOZ-018` — RESULTADO NO VERIFICABLE AÚN
- Ledger reread mantiene `ASSIGNMENT_STATUS: ASSIGNED` y el último resultado escrito sigue siendo `NIGHT-WOZ-017 DONE`.
- Issue #41 no contiene handoff final de `NIGHT-WOZ-018` al cierre de este preflight.
- No hay PR/branch/commit nuevo observable con lineage 17.2/webhook; búsqueda de branches `woz/*` termina en 17.1 y búsqueda de commits `webhook` no devuelve candidate nuevo.
- Por idempotencia, JOBS **NO emite `NIGHT-WOZ-019` y NO sobreescribe `WOZ-018`**. Se conserva 018 vigente hasta handoff verificable.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 12.1 #66:** cerrar wiring productivo de navegación bounded y exact-head; después queda residual cold/warm si no está demostrado.
2. **F3 / 17.2:** assignment vigente de WOZ; dependency-ready y aún sin resultado compartido verificable.
3. **F4 / 25.1 #63:** esperar evidencia literal de Windows Import/Required CI; cerrar o corregir misma lineage.
4. **F0/F1:** blockers actuales externos/RO; no repetir drills técnicos aceptados.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Asignación vigente | Objetivo |
|---|---|---|---|
| AAA | 018 PENDING — #66 bounded consumer parcial | `NIGHT-AAA-019` | SAME #66 production React next/previous/cursor + focused PASS + fresh exact-head/race-check |
| BBB | 017 PENDING — #63 refreshed; functional CI running | `NIGHT-BBB-018` | SAME #63 reuse runs; PASS→race-check/promote/merge, FAIL→minimal fix |
| WOZ | 018 sin resultado verificable | `NIGHT-WOZ-018` | F3/17.2 webhook raw-body integrity + durable dedupe/idempotency/retry software-only |

Ownership exclusivo: AAA=F2/12.1 #66; BBB=F4/25.1 #63; WOZ=F3/17.2. No overlap material.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia off-provider/off-account real + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: production navigation #66 + exact-head; cold/warm residual después si sigue no demostrado; D13–D15 abiertos.
6. F3: 17.2–20 abiertos; 16.x physical/deploy tails externos; Stripe productivo no probado.
7. F4/25.1: #63 functional conclusion pendiente + otros coverage gaps; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58 + #64 integrados; #66 refreshed y avanzado, todavía PENDING; D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 integrado; 17.2 continúa assignment activo; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 refreshed, functional run pendiente; 25.1/25.2 abiertos; D22/D23 externos.

## PLAN SYNC — CYCLE 018

- Actualizados: `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - JOBS.md`, `Plan Maestro.md`, F2, F4 y roles/coordinación.
- `NOCHE - WOZ.md` se conserva sin mutación porque `NIGHT-WOZ-018` sigue ASSIGNED y no hay resultado final verificable que procesar.
- F0/F1/F3 no cambian materialmente en este ciclo.
- JOBS no modifica código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar `AAA-019`, `BBB-018` y, cuando aparezca, el resultado real `WOZ-018`.
3. No convertir CI en curso en PASS por inferencia.
4. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.
5. Mantener blockers externos como externos hasta evidencia real.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-018
INTEGRATION_HEAD: ed6aab7e964686cdb5fb1b84eac0198ca67f8892
AAA: 018 PENDING -> NIGHT-AAA-019 SAME #66 production navigation/fresh exact-head
BBB: 017 PENDING -> NIGHT-BBB-018 SAME #63 reuse in-flight exact-head evidence
WOZ: 018 still ASSIGNED; no verifiable final handoff -> NO 019 issued
DUPLICATE_WORK: none; #66/#63 same lineages preserved; #62 remains closed/not merged
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 018 procesado con la evidencia visible. El próximo ciclo parte de GitHub vivo.
