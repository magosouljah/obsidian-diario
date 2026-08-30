# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-024`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: consumir fallo exact-head y siguiente corrective mínimo`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ 033c2b55a0c46471b7e7ddb3af57b626699ac6e6`
- `PREDECESSOR: NIGHT-BBB-023 ASSIGNED / NOT_PROCESSED / SUPERSEDED_BY_JOBS — no RESULTADO DEL TURNO ni head nuevo observable al CYCLE 025; no ejecutar 023 después de recibir 024.`

### PRIMARY

1. Haz preflight GitHub vivo + duplicate-check. Reutiliza exclusivamente SAME PR #63; no replacement PR/branch.
2. Consume Windows Import exact-head run `33284981477`, job `99186491944`, sobre head `033c2b55a0c46471b7e7ddb3af57b626699ac6e6`.
3. Hecho aceptado: checkout/setup Node/Rust/npm y `Prepare isolated embedded Tauri WebDriver` SUCCESS; `Run existing Windows import E2E harness` FAILURE.
4. Identifica el primer failure causal del run actual y aplica únicamente el corrective F4/harness mínimo necesario para llegar a sesión efectiva y ejecutar las assertions existentes de import.
5. No cambies lógica productiva de import salvo que una assertion funcional demuestre un `PRODUCT_FINDING`; si ocurre, documenta finding y STOP para JOBS.
6. `windows/import` permanece `NOT_COVERED` hasta PASS literal. No promociones matrix antes de ese PASS.
7. Head nuevo => Windows Import literal PASS + fresh applicable exact-head F4 Matrix + D6 + D7 + Desktop Portability; race-check antes de merge.
8. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP. No iniciar 25.2/signing/notarization.

**Required evidence:** exact failure causal del job 99186491944; branch/head; delta mínimo; Windows Import assertion/PASS literal o nuevo blocker factual; applicable exact-head CI; matrix honesta; merge SHA solo si autorizado y verde.  
**STOP:** bug productivo fuera de F4 demostrado, scope 25.2/D22/D23, cambio global de packages no justificado, CI rojo no atribuible, baseline no reconciliable o necesidad RO.

### CI-FALLBACK

`NONE`

Reason: 25.2 y otros gaps F4 ampliarían scope; no hay fallback materialmente independiente seguro mientras #63 requiere corrective activo.

## RESULTADO PROCESADO — NIGHT-BBB-023

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`
- `EVIDENCE: #63 seguía OPEN/Ready @ 033c2b55...; no head nuevo, no RESULTADO DEL TURNO ni handoff 023 observable al CYCLE 025.`
- `ACTION: sustituido por NIGHT-BBB-024 con SAME #63 y mismo corrective crítico.`

## HISTORIAL COMPACTO

- `NIGHT-BBB-024`: ASSIGNED — SAME #63 current-run corrective; CI-FALLBACK NONE.
- `NIGHT-BBB-023`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-022`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-021`: PENDING/WAITING_CI -> FAILURE run 33284981477.
- `NIGHT-BBB-020`: PENDING — prior exact-head Windows Import failed before assertions.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
- `NIGHT-BBB-008`: #57 integrated `f73c9ee...`.
- `NIGHT-BBB-005`: #55 integrated `672e133...`.
- `NIGHT-BBB-003`: #51 integrated `5b05ca845...`.
