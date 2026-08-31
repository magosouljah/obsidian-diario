# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-085`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — exact-lineage Windows auth failure triage/correction on PR #84`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_CORRECTIVE: PR #74 @ b3468003a80288109e2d537a7aa3f25a7269927c.`
- `EVIDENCE_CANDIDATE: PR #84 @ d13a1969aef1ca53ee7fbed0bcba241ceb766d42; OPEN/Ready/mergeable; harness/workflow-only delta from exact #74 lineage.`
- `PREDECESSOR: NIGHT-BBB-084 had no final RESULTADO DEL TURNO nor material Issue #41 handoff at JOBS CYCLE 090 preflight; superseded, NOT_PASS.`
- `KNOWN_CI: Windows auth functional journey run 33407580887 / job 99538870371 = FAILURE at Run isolated Windows auth assertions; Required CI 33407580663 = SUCCESS.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. No worker is authorized to mutate integration in CYCLE 090.`

### PRIMARY

**F4 / 25.1 — isolate and correct the exact #84 Windows auth failure without widening product scope.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact check status; duplicate-check before mutation.
2. Reuse #84 as the sole BBB evidence candidate; do not open a duplicate PR.
3. Diagnose `Run isolated Windows auth assertions` using workflow/job/log evidence on exact current head.
4. If and only if failure is attributable to harness/workflow/test plumbing, apply the minimum harness/workflow-only correction on #84. Preserve #74 product files/logic unchanged.
5. Re-run the literal packaged Windows/Tauri auth journey and require attributable assertions for returned token persistence into `beatgaler:account-session:v1` and AccountGate exit.
6. Any moved #84 head requires fresh exact-head applicable CI. Record run/job IDs and exact failing/passing assertion evidence.
7. If #74 product corrective is insufficient, **STOP** and report the exact product finding to JOBS; do not modify #74 product logic under this assignment.
8. **NO MERGE.** Do not touch #83, AAA F2/13.2, WOZ F2/12.1, #72, signing/notarization or provider resources.
9. Maximum claim if green: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; never global 25.1 closure.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact #74 product head; exact #84 pre/post head; changed-file map; failure root attribution; packaged Windows runner; literal auth assertions; run/job IDs; exact-head CI; explicit remaining NOT_COVERED journeys.  
**STOP:** product code change outside #74 required, root cause cannot be attributed, external hardware/credential dependency, duplicate owner/candidate, integration mutation required, overlap with AAA/WOZ work, or scope expansion.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-084`: NO_RESULT at CYCLE 090 preflight; superseded; NOT_PASS.
- `NIGHT-BBB-083`: NO_RESULT at CYCLE 089; superseded; NOT_PASS.
- `NIGHT-BBB-081`: #84 exact head `d13a1969...`; Required CI SUCCESS, literal Windows auth run `33407580887` / job `99538870371` FAILURE. NOT_PASS; no merge.
