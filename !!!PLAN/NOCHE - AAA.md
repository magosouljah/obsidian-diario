# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-106`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — REUSE PR #91, exact-head validation + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843`
- `PREDECESSOR: NIGHT-AAA-105 = CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING; matching Issue #41 handoff verified. Candidate PR #91 @ 35d44a0dd5ee380f802b3a80b139ca1ca741d5f9.`
- `WHY_ASSIGNED: F2/12.1 remains the first hard blocker for alpha readiness. #91 is the existing bounded corrective and is exact-base against the live integration head at JOBS CYCLE 110 preflight.`
- `SERIALIZATION: AAA106 owns PR #91 and is the only integration mutation owner in CYCLE 110. BBB105 owns #84 evidence/harness. WOZ109 owns #89 review/refresh only. Do not touch #84/#89/#76/#83/#85/provider/deploy/shared auth internals.`

### PRIMARY

**F2 / 12.1 — finish REUSE-first validation of #91 and integrate only if exact/race-free.**

1. Fresh preflight integration HEAD, PR #91 base/head/mergeability, changed files and Issue #41; duplicate-check.
2. Preserve the bounded semantics already proven by AAA105: 30 s deadline only for bootstrap-critical Worker requests `initialize`, `verify`, `get_index`; no generic loader timeout; long transfers unaffected; Web/no-Tauri invariant preserved.
3. Recheck all applicable exact-head workflows for `35d44a0d...`. At assignment time Web Production Build, D6, D7, temp-auth compile and F0/0.20 scan were successful; `Test - Desktop Portability` was still in progress. Do not infer final green until every applicable required check is complete.
4. If integration HEAD changed before merge, STOP and history-preserving refresh/re-run exact-head applicable CI; no stale-green merge.
5. If #91 remains exact-base, scope-bounded, mergeable and all applicable exact-head CI is SUCCESS, AAA106 is authorized to merge **PR #91 only** with expected-head/race protection and verify merge SHA + parents.
6. Maximum claim after merge: `F2/12.1 CODE_FIX_INTEGRATED / PUBLIC_RUNTIME_PENDING`. Do **not** mark 12.1 PASS until authenticated public Web on the deployed artifact containing the fix proves deterministic exit from `Loading Galer` or existing recoverable fallback, plus cold/warm timing evidence as applicable.
7. Record RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** live integration before/after; #91 exact base/head; changed files; applicable workflow names/conclusions; merge SHA/parents if merged; public runtime explicitly UNVERIFIED unless actually observed.  
**STOP:** failed/pending required CI at turn close, base/head race, scope drift, shared auth/backend/provider/deploy mutation, duplicate candidate, or any integration mutation other than #91.

### CI-FALLBACK

**Trigger:** only while PRIMARY is genuinely `WAITING_CI` on unchanged exact head `35d44a0d...`.

`CI-FALLBACK: READ-ONLY F2/13.2 durable Review closure map.`

- **Scope:** inspect current integrated Review Save/Save All paths and existing #72/evidence only to identify the minimum durable-completion/no-silent-loss acceptance seam. No branch, PR, code or integration mutation.
- **Evidence required:** exact files/functions involved; existing reusable tests/candidates; smallest closure criterion; Web/no-Tauri boundary; explicit conflicts/owners.
- **STOP:** no implementation, no #72 refresh, no auth/session/backend mutation, no claim of PASS. As soon as #91 CI resolves, return to PRIMARY before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-105`: `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`.
- Root cause: `WebTransportWorkerClient.request()` could remain pending forever when the data-plane Worker neither replied nor crashed during bootstrap-critical operations.
- Candidate: PR #91 `aaa/12.1-web-bootstrap-deadline` @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`, base `78dd55b72142e69ea32ba6c1ba6d43e246ac6843`.
- Public runtime remains pending; no PASS claim yet.
