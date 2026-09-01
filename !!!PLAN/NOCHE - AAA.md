# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-104`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — public Web bootstrap runtime blocker (Loading Galer)`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`
- `PREDECESSOR: NIGHT-AAA-103 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff verificable al preflight JOBS CYCLE 108; SUPERSEDED / NOT_PASS.`
- `WHY_ASSIGNED: camino crítico recalculado de cero: F2/12.1 sigue siendo el blocker funcional #1 para browser/tester real; GitHub no contiene candidate/handoff nuevo que lo cierre.`
- `SERIALIZATION: AAA104 owns only F2/12.1 Web bootstrap/runtime. BBB103 owns #84 auth evidence/harness. WOZ107 owns #89 security candidate. Do not touch #74/#84/#89/#90/#88/#83/#76/#85, integration, deploy/provider infra or shared auth/session internals.`

### PRIMARY

**F2 / 12.1 — reproducir y corregir mínimamente el stall público `Loading Galer`.**

1. Fresh preflight del baseline `38517c...`, Issue #41, public symptom y open PRs; duplicate-check antes de mutar.
2. Reproducir el stall en Web y aislar el primer bootstrap phase que no resuelve.
3. Preservar como PROVEN DNS/TLS/deploy público ya evidenciado; no reabrir infraestructura por este síntoma.
4. Aplicar solo el corrective Web mínimo que haga que startup termine determinísticamente en estado válido o error recuperable explícito.
5. No debilitar auth/cloud failure semantics, no timeout cosmético, no Tauri/Desktop dependency.
6. Focused tests para causa + success/failure termination + Web/no-Tauri touched paths.
7. Un solo candidate/PR bounded si duplicate-check sigue limpio; exact base/head + fresh exact-head CI. **NO MERGE.**
8. Maximum claim: `F2/12.1 PUBLIC_WEB_BOOTSTRAP_CANDIDATE_READY`; cold/warm timing real sigue separado.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** reproducción; primer phase irresuelto; archivos/funciones exactos; before/after termination; tests; Web/no-Tauri proof; base/head; PR/CI exact-head; UNVERIFIED explícito.  
**STOP:** shared auth/session product mutation, backend/provider/infra/deploy, secrets, architecture redesign, owner/candidate collision, baseline race o integration mutation.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-103`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 108; no final result/handoff verificable observado al preflight.
- Issue #41 `5485984669`: public infra works; normal Web startup stalls at `Loading Galer`.
- Baseline permanece `38517c...`; revalidar desde ese head antes de cualquier candidate.
