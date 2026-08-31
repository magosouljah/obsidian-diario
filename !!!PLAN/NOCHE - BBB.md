# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-090`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — current exact #74/#84 packaged Windows auth causal attribution + minimum corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable; base exact live integration.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; base exact live integration.`
- `AUTHORITATIVE_FAILURE: exact #84 Windows Auth Journey run 33423712589 = FAILURE; broad exact-head Required CI/Desktop Portability 33423712599 = SUCCESS. Literal auth red prevails.`
- `PREDECESSOR: NIGHT-BBB-089 has no final RESULTADO DEL TURNO or matching material Issue #41 handoff and #74/#84 have not moved at CYCLE 095 preflight; superseded / NOT_PASS.`
- `WHY_REASSIGNED: global path was recalculated from live GitHub; this remains the highest-priority executable internal gate because current packaged Windows auth is still literally red.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA091 owns F2/13.2. WOZ094 owns F2/15.1 Trash. #83 is parked and unowned for mutation.`

### PRIMARY

**F4 / 25.1 — identify the first causal boundary on CURRENT #74/#84, then apply at most the smallest attributable correction and regenerate literal evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact workflow state; STOP on duplicate ownership or material lineage movement.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence candidate. Do not fork another PR.
3. Treat `c6c5ecb...` auth red as authoritative; broad green does not satisfy windows/auth.
4. Before product mutation, distinguish the first failure boundary with literal packaged-runner evidence: runtime classification → session write call → storage visibility → AccountGate transition.
5. Only if attribution is conclusive, make the minimum correction inside existing platform/session boundary on #74. No auth/security redesign, backend/provider change, token-policy weakening or unrelated UI work.
6. Refresh #84 history-preservingly onto exact resulting #74 head while preserving harness semantics and record ancestry.
7. Re-run literal packaged Windows auth. Require BOTH `beatgaler:account-session:v1 = e2e-session-token` and AccountGate exit.
8. Any moved head requires fresh applicable exact-head CI and exact run/job IDs.
9. **NO MERGE.** Maximum green claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; global 25.1 remains OPEN for uncovered rows.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** integration/#74/#84 exact pre/post SHAs; compare/ancestry; first-causal assertion/log; changed-file/function map; literal token-persistence and gate-exit result; exact-head CI; explicit NOT_COVERED rows.  
**STOP:** root cause needs auth/security redesign, backend/provider changes, unrelated product files, integration mutation, #72/AAA Review overlap, or remains non-attributable after one bounded diagnostic pass.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** secondary F4 work would share release-chain ownership or broaden scope; signing/hardware/tester work requires external evidence and cannot be truthfully advanced during CI.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-089`: NO_RESULT at CYCLE 095 preflight; no new handoff and no #74/#84 movement; superseded; NOT_PASS.
- `NIGHT-BBB-088`: NO_RESULT at CYCLE 094; superseded; NOT_PASS.
- `NIGHT-BBB-087`: prior blocked/current-lineage evidence only; current literal Windows Auth remains RED.
