# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-080`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.2 — Review Save/Save All durable action-boundary corrective slice`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-AAA-079 had no RESULTADO DEL TURNO nor matching Issue #41 handoff at JOBS CYCLE 084; superseded, not PASS.`
- `REUSE_EVIDENCE: Issue #41 5478129410 + NIGHT-AAA-071. Do not repeat broad audit.`
- `SERIALIZATION: AAA MUST NOT merge or mutate integration. WOZ/#83 owns the only integration mutation.`

### PRIMARY

**F2 / 13.2 — implement the minimum proven durable-completion/no-silent-loss fix.**

1. Fresh preflight live integration + Issue #41 + duplicate-check; stop if another candidate already owns this exact slice.
2. REUSE the proven finding: Review single Save / Save All can advance/close before `cloudifyImportedBeats(...)` durable completion.
3. Reuse helper/semantics from #69 only as bounded input; do not revive or take ownership of #69.
4. Change only the minimum F2 Review Save/Save All product wiring so visible success/advance waits for durable Web persistence.
5. Surface per-beat `saved/conflict/failed` sufficient for retry and zero silent loss.
6. Add focused executable evidence for single Save + Save All partial failure/conflict/retry, plus call-spies proving touched Web paths never call Tauri/Desktop-only APIs.
7. New bounded AAA branch/PR, exact scope map, focused tests and fresh exact-head applicable CI. NO MERGE.
8. Maximum claim: `F2/13.2 DURABLE_SAVE_BOUNDARY_CANDIDATE_READY`; global 13.2 remains OPEN unless every literal Web-action family is evidenced.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head; changed files/functions; before/after semantics; per-beat result/retry assertions; Tauri/Desktop call-spies; focused tests; exact-head CI; explicit UNVERIFIED families.  
**STOP:** backend/F3 ownership required, #70/#81 overlap, material redesign, provider/runtime credentials, existing duplicate candidate, scope expansion, or non-attributable broad CI failure.

### CI-FALLBACK

**F2 / 12.1 — READ-ONLY real-browser cold/warm evidence on untouched integration baseline.**

Execute ONLY if PRIMARY is genuinely `WAITING_CI`/remote-build wait. Do not change code, branch, PR or ownership. Reuse the existing `npm run test:web:smoke`/current Web smoke path and capture attributable real-browser cold vs warm startup evidence from the live integration baseline, including environment/browser/build identity and observed timings. This fallback does not authorize synthetic substitution or performance claims from static inspection.

**Required evidence:** exact integration SHA; browser/runtime identity; cold/warm run outputs/timings; command/harness used; explicit limitations.  
**STOP:** browser/runtime unavailable, evidence would be synthetic/non-attributable, any code change becomes necessary, or PRIMARY leaves external wait. Return to PRIMARY state before closing the turn.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-079`: NO_RESULT at CYCLE 084; superseded; not PASS.
- Late `NIGHT-AAA-074` Issue #41 `5478129410`: reusable current-baseline finding only.
- `NIGHT-AAA-071`: DONE / AUDIT_ONLY; reusable context.
