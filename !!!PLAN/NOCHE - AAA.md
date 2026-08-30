# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** F2 — Web / UX.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-032`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — cerrar residual cold/warm runtime con harness reproducible`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `HOLDING_ITEM: PR #69 remains OPEN/Ready/mergeable @ b2ab75ae... but product wiring is frozen in this assignment after NIGHT-AAA-031 STOP_WRITE_SURFACE.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. No repitas NIGHT-AAA-031 y no toques #69/App wiring en este turno.
2. REUSE-FIRST sobre la instrumentación Web startup ya integrada por #58 y la navegación/windowing #66. No reimplementes library startup.
3. Construye el camino mínimo para producir una comparación **cold vs warm real y reproducible** del startup Web, preferentemente mediante un harness/script/test pequeño y aislado que no requiera reescribir `App.tsx` completo.
4. Mismo escenario y datos para ambas corridas: cold debe limpiar/invalidar explícitamente cache/session aplicable; warm debe preservar la condición warm. Captura métricas de las fases instrumentadas y total comparable; documenta criterio y ambiente.
5. No aceptes timers sintéticos/unit-only como sustituto de startup real. Si la superficie disponible no puede ejecutar navegador/Web real, deja blocker factual y STOP sin fabricar números.
6. Si hace falta cambio, una sola rama/PR F2 mínima limitada a harness/medición/startup instrumentation + tests; no 13.1/13.2/D14/D15, server journal, billing, desktop packaging ni infra.
7. Evidencia requerida: comandos/escenario reproducible, al menos una pareja cold/warm comparable con números, interpretación sin overclaim, focused tests y fresh applicable exact-head CI si cambia código.
8. Si el requisito literal queda demostrado, recomienda a JOBS cerrar únicamente 12.1. No cierres F2 completa.
9. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** baseline/head, cold/warm setup, métricas cuantificadas reales, reproducibilidad, focused tests, exact-head CI si hay cambio, PR/merge si aplica.  
**STOP:** benchmark no real/no reproducible, necesidad de App.tsx full replacement, scope creep a #69/13.x+, baseline race, CI rojo no atribuible o dependencia externa.

### CI-FALLBACK

`NONE`

Reason: #69 está frozen por write-surface y 13.x+ ampliaría scope; no existe fallback independiente seguro.

## RESULTADO PROCESADO — NIGHT-AAA-031

- `STATUS: PENDING / STOP_WRITE_SURFACE`.
- SAME #69 sigue OPEN/Ready/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`.
- Gap reconfirmado: `App.tsx -> handleReviewedSaveAll` no consume `saveAllWebItems`.
- Sin cambio inseguro; handoff Issue #41 `5468306925`.
- JOBS CYCLE 032 mueve AAA a 12.1 runtime para mantener avance independiente y congela #69 hasta una superficie de patch/worktree segura.

## HISTORIAL COMPACTO

- `NIGHT-AAA-032`: ASSIGNED — cold/warm Web runtime reproducible.
- `NIGHT-AAA-031`: PENDING / STOP_WRITE_SURFACE — #69 frozen.
- `NIGHT-AAA-029`: PENDING — helper green, product wiring missing.
- `NIGHT-AAA-027`: #69 created.
- `NIGHT-AAA-022`: taxonomy/state demonstrated; cold/warm real remained open.
- `NIGHT-AAA-020`: #66 merged `712b49b6689...`.
