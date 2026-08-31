# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-082`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — exact-lineage Windows auth failure triage/correction on PR #84`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_CORRECTIVE: PR #74 @ b3468003a80288109e2d537a7aa3f25a7269927c.`
- `EVIDENCE_CANDIDATE: PR #84 @ d13a1969aef1ca53ee7fbed0bcba241ceb766d42; OPEN/Ready; harness/workflow-only delta from exact #74 lineage.`
- `PREDECESSOR: NIGHT-BBB-081 WAITING_CI is now resolved factually as CI FAILURE, not PASS.`
- `LIVE_CI: Windows auth functional journey run 33407580887 / job 99538870371 = FAILURE at step Run isolated Windows auth assertions; Required CI run 33407580663 = SUCCESS.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration; no integration mutation is authorized in CYCLE 087.`

### PRIMARY

**F4 / 25.1 — isolate and correct the exact #84 Windows auth failure without widening product scope.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact check status; duplicate-check before mutation.
2. Reuse #84 as the sole BBB evidence candidate; do not open a duplicate PR.
3. Diagnose the failed `Run isolated Windows auth assertions` step on exact head `d13a1969...` using workflow/job/log evidence available to the worker.
4. If and only if the failure is attributable to the transplanted harness/workflow/test plumbing, apply the minimum harness/workflow-only correction on #84. Preserve #74 product files/logic unchanged.
5. Re-run the literal packaged Windows/Tauri auth journey and require attributable assertions for returned token persistence into `beatgaler:account-session:v1` and AccountGate exit; include any encoded reauth/session assertions actually executed.
6. Any moved #84 head requires fresh exact-head applicable CI. Record run/job IDs and exact failing/passing assertion evidence.
7. If evidence indicates the #74 product corrective itself is insufficient, **STOP** and report the exact product finding to JOBS; do not modify #74 product logic under this assignment.
8. **NO MERGE.** Do not touch #83, AAA F2/13.2, #72, signing/notarization or provider resources.
9. Maximum claim if green: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; never global 25.1 closure.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact #74 product head; exact #84 pre/post head; changed-file map; failure root attribution; packaged Windows runner; literal auth assertions; run/job IDs; exact-head CI; explicit remaining NOT_COVERED journeys.  
**STOP:** product code change outside #74 required, root cause cannot be attributed, external hardware/credential dependency, duplicate owner/candidate, integration mutation required, overlap with AAA Review/#72, or scope expansion.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent F4 lane is both useful and non-overlapping while windows/auth is active; #72 Review materially overlaps active AAA Review work.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-081`: processed CYCLE 087. #84 exact head `d13a1969...`; Required CI SUCCESS, but `Windows auth functional journey` run `33407580887` / job `99538870371` = FAILURE at isolated auth assertions. NOT_PASS; no merge.
- `NIGHT-BBB-080`: NO_RESULT; superseded; NOT_PASS.
- `NIGHT-BBB-079`: BLOCKED_STOP; old #71 harness lineage not attributable to refreshed #74.
