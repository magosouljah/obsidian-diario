# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-091`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — current exact #74/#84 packaged Windows auth first-causal-boundary attribution + minimum corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; base exact live integration.`
- `AUTHORITATIVE_FAILURE: exact #84 Windows Auth Journey run 33423712589 / job 99592060690 = FAILURE at step Run isolated Windows auth assertions; broad green does not satisfy windows/auth.`
- `PREDECESSOR: NIGHT-BBB-090 has no final RESULTADO DEL TURNO or matching material Issue #41 handoff at JOBS CYCLE 096 preflight; superseded / NOT_PASS.`
- `WHY_ASSIGNED: recalculated path still puts the literal packaged Windows auth failure on the global critical path. This is not retained by inertia; current GitHub evidence remains red and uniquely owned by #74/#84.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA092 owns F2/13.2. WOZ095 owns F3/19.1 READ-ONLY. F2/15.1 Trash is blocked on a reusable recent-reauth seam and has no implementation owner this cycle.`

### PRIMARY

**F4 / 25.1 — identify the first causal boundary on CURRENT #74/#84, then apply at most the smallest attributable correction and regenerate literal evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and run `33423712589` / job `99592060690`; STOP on duplicate ownership or material lineage movement.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence candidate. Do not fork another PR.
3. Treat exact `c6c5ecb...` auth red as authoritative; Required CI green is insufficient.
4. Before any product mutation, extract the first causal failure/log boundary from the exact packaged runner: runtime classification → session write call → storage visibility → AccountGate transition.
5. Only if attribution is conclusive, make the minimum correction inside the existing platform/session boundary on #74. No auth/security redesign, backend/provider change, token-policy weakening or unrelated UI work.
6. Refresh #84 history-preservingly onto the exact resulting #74 head while preserving harness semantics and record ancestry.
7. Re-run literal packaged Windows auth. Require BOTH `beatgaler:account-session:v1 = e2e-session-token` and AccountGate exit.
8. Any moved head requires fresh applicable exact-head CI and exact run/job IDs.
9. **NO MERGE.** Maximum green claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; global 25.1 remains OPEN for uncovered rows.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** integration/#74/#84 exact pre/post SHAs; compare/ancestry; first-causal log/assertion; changed-file/function map if corrective; literal token-persistence and gate-exit result; exact-head CI; explicit NOT_COVERED rows.  
**STOP:** root cause requires auth/security redesign, backend/provider changes, unrelated product files, integration mutation, #72/AAA Review overlap, or remains non-attributable after one bounded diagnostic pass.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** secondary F4 work shares release-chain ownership or needs external signing/hardware/tester evidence. Trash recent-reauth would overlap auth/session ownership and must not be opportunistically added to this assignment.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-090`: NO_RESULT at CYCLE 096 preflight; no matching material handoff and no #74/#84 movement; superseded; NOT_PASS.
- `NIGHT-BBB-089`: NO_RESULT at CYCLE 095; superseded; NOT_PASS.
- Current literal #84 Windows Auth remains RED on exact `c6c5ecb...`; run `33423712589`, job `99592060690`.
