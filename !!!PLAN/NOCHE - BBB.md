# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-022`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: consumir fallo exact-head y siguiente corrective mínimo`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ 033c2b55a0c46471b7e7ddb3af57b626699ac6e6`
- `PREDECESSOR: NIGHT-BBB-021 PENDING / WAITING_CI — procesado por JOBS; CI ya terminó FAILURE. No repetir 021.`

### PRIMARY

1. Haz preflight GitHub vivo + duplicate-check. Reutiliza exclusivamente SAME PR #63; no replacement PR/branch.
2. Consume la evidencia del Windows Import exact-head run `33284981477`, job `99186491944`, sobre head `033c2b55a0c46471b7e7ddb3af57b626699ac6e6`.
3. Hecho ya aceptado por JOBS: checkout/setup Node/Rust/npm y `Prepare isolated embedded Tauri WebDriver` terminaron SUCCESS; `Run existing Windows import E2E harness` terminó FAILURE. No vuelvas a diagnosticar desde un log anterior como si fuera el actual.
4. Identifica el **primer failure causal del run actual** y aplica únicamente el corrective F4/harness mínimo necesario para llegar a sesión efectiva y ejecutar las assertions existentes de import.
5. No cambies lógica productiva de import salvo que una assertion funcional llegue a ejecutarse y demuestre un `PRODUCT_FINDING`; si eso ocurre, documenta finding y STOP para JOBS en vez de expandir scope.
6. `windows/import` permanece `NOT_COVERED` hasta PASS literal. No promociones la matrix antes de ese PASS.
7. Si el corrective crea head nuevo: exige Windows Import literal PASS y fresh applicable exact-head F4 Matrix + D6 + D7 + Desktop Portability. Race-check contra integration antes de merge; si baseline cambió materialmente, refresh y revalidación.
8. Escribe RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP. No iniciar 25.2/signing/notarization.

**Required evidence:** exact failure causal del job 99186491944; branch/head; delta mínimo; Windows Import assertion/PASS literal o nuevo blocker factual; applicable exact-head CI; matrix permanece honesta; merge SHA solo si autorizado y verde.  
**STOP:** bug productivo fuera de F4 demostrado, scope 25.2/D22/D23, cambio global de packages no justificado, CI rojo no atribuible, baseline no reconciliable o necesidad RO.

### CI-FALLBACK

`NONE`

Reason: 25.2 y otros gaps F4 ampliarían scope; no hay fallback materialmente independiente seguro mientras #63 requiere corrective activo.

## RESULTADO PROCESADO — NIGHT-BBB-021

- `STATUS_AT_WORKER_CLOSE: PENDING / WAITING_CI`
- `BASELINE_LIVE: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `PR: #63 OPEN/Ready / head 033c2b55a0c46471b7e7ddb3af57b626699ac6e6`
- `CI_RECHECK_BY_JOBS: Windows Import 33284981477 = COMPLETED / FAILURE.`
- `JOB 99186491944: setup/checkout/Node/Rust/npm/embedded-prepare SUCCESS; existing Windows import E2E harness FAILURE.`
- `CLAIM: no literal import PASS; windows/import remains NOT_COVERED; no matrix promotion; no merge.`
- `JOBS_ACTION: emitir NIGHT-BBB-022 sobre SAME #63 para consumir exclusivamente el failure actual.`

## HISTORIAL COMPACTO

- `NIGHT-BBB-022`: ASSIGNED — SAME #63 current-run corrective; CI-FALLBACK NONE.
- `NIGHT-BBB-021`: PENDING/WAITING_CI -> JOBS recheck resolved to FAILURE run 33284981477.
- `NIGHT-BBB-020`: PENDING — prior exact-head Windows Import failed before assertions.
- `NIGHT-BBB-019`: PENDING — baseline STOP + DevToolsActivePort diagnosis.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
- `NIGHT-BBB-008`: #57 integrated `f73c9ee...`.
- `NIGHT-BBB-005`: #55 integrated `672e133...`.
- `NIGHT-BBB-003`: #51 integrated `5b05ca845...`.
