# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-098`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.2 — Review Save/Save All durable action boundary`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-AAA-097 no dejó RESULTADO DEL TURNO, matching Issue #41 handoff ni candidate material al preflight JOBS CYCLE 102; SUPERSEDED / NOT_PASS.`
- `WHY_ASSIGNED: recalculado desde GitHub vivo; el gap durable Review sigue probado y es la slice F2 técnica ejecutable de mayor valor sin colisión con BBB auth ni WOZ D10.2.`
- `SERIALIZATION: AAA MUST NOT merge or mutate integration. BBB097 owns #84 diagnostics. WOZ101 owns D10.2 READ-ONLY. Do not touch #74/#84/#83/#76/#85/auth/session/Trash/legal/deploy.`

### PRIMARY

**F2 / 13.2 — minimum durable Review Save/Save All candidate.**

1. Fresh preflight integration + Issue #41 + open PRs; duplicate-check antes de mutar.
2. Reuse el gap probado en `src/App.tsx`: single Save y Save All no deben cerrar/avanzar antes de durable `cloudifyImportedBeats(...)` completion.
3. Reuse #69 únicamente como referencia semántica/helper; no revivirlo.
4. Cambiar solo wiring mínimo para esperar persistencia Web durable y exponer por beat `saved/conflict/failed`, retry y cero silent loss.
5. Añadir pruebas enfocadas de single Save y Save All con partial failure/conflict/retry y call-spies que prueben que la ruta Web tocada no invoca APIs Tauri/Desktop-only.
6. Un solo branch/PR bounded si duplicate-check queda limpio; registrar base/head exactos, changed files/functions, tests y fresh exact-head CI. **NO MERGE.**
7. Maximum claim: `F2/13.2 DURABLE_SAVE_BOUNDARY_CANDIDATE_READY`; no cerrar 13.2 global sin cobertura literal suficiente de acciones Web visibles.
8. Escribir RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**Required evidence:** exact base/head; before/after semantics; per-beat result/retry assertions; Web/no-Tauri call-spies; focused tests; exact-head CI; UNVERIFIED explícito.  
**STOP:** duplicate candidate/owner, backend/F3/auth/session ownership needed, material redesign, provider/runtime credentials, baseline movement que invalide scope, integration mutation o broad CI no atribuible.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-097`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 102; no final result, matching Issue #41 handoff ni candidate material.
- `NIGHT-AAA-096`: `NO_RESULT / SUPERSEDED / NOT_PASS` en CYCLE 101.
- Issue #41 `5478129410`: reusable proven Review durable-completion gap.
- `NIGHT-AAA-071`: DONE / AUDIT_ONLY; contexto reusable.
