# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-106`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.2 — durable Review Save/Save All completion / no silent loss`
- `LIVE_BASE_AT_ASSIGNMENT_REBASED: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-AAA-105 produced PR #91. During JOBS CYCLE 110, #91 was independently merged with exact-head CI as 134a293985c314eb09c238115e3bcb71e79f1810; therefore the original AAA106/#91 PRIMARY became duplicate and was replaced before worker execution.`
- `WHY_ASSIGNED: after #91 integration, F2/12.1 code is integrated but public deploy/auth runtime is owner-key external. The next executable product blocker is F2/13.2 durable Review.`
- `SERIALIZATION: AAA106 owns only F2/13.2 Review durability. BBB105 owns #84. WOZ109 owns #89/integration lane. No #91/deploy/provider/auth-internals/Trash/#89/#84.`

### PRIMARY

**F2 / 13.2 — close the proven durable-completion/no-silent-loss gap with the minimum Web-safe corrective.**

1. Fresh preflight live integration `134a293...` or newer, Issue #41, existing Review paths/tests and any reusable #72 evidence; duplicate-check before mutation.
2. Identify exact Save/Save All path where UI can advance/close before durable cloud completion/failure is known.
3. REUSE existing durable operation/result semantics; do not redesign backend or auth/session.
4. Implement the smallest product correction so visible success/close/advance occurs only after durable completion; failures remain visible/recoverable and no silent loss is possible.
5. Preserve Web pure/no-Tauri behavior. Desktop compatibility may not be weakened.
6. Add focused tests for success completion, failure/no-close, Save All partial/failure semantics and Web/no-Tauri touched paths.
7. One bounded candidate/PR only if duplicate-check is clean; exact base/head + applicable CI. **NO MERGE CYCLE 110.**
8. Maximum claim: `F2/13.2 DURABLE_REVIEW_CANDIDATE_READY`; no PASS until exact-head evidence satisfies the literal gate.
9. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** exact files/functions; before/after completion semantics; tests; Web/no-Tauri proof; branch/base/head/PR; exact-head applicable CI; explicit UNVERIFIED.  
**STOP:** shared auth/session/backend redesign, provider/deploy, Trash, #84/#89, integration mutation, duplicate candidate, or baseline race requiring unsafe refresh.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-105`: corrective #91 was subsequently integrated as `134a293985c314eb09c238115e3bcb71e79f1810` with exact-head CI.
- F2/12.1 now = `INTEGRATED / PUBLIC_DEPLOY + AUTH RUNTIME PENDING`; not PASS because deployed authenticated runtime and cold/warm evidence remain external/unverified.
