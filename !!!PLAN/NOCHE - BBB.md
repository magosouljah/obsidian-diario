# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-089`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — current exact #74/#84 packaged Windows auth causal attribution + minimum corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95; OPEN/Ready/mergeable.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; base exact live integration.`
- `AUTHORITATIVE_FAILURE: exact #84 Windows Auth Journey run 33423712589 / job 99592060690 = FAILURE at tests/e2e/auth-flow.e2e.mjs:64: Desktop login did not persist the returned session token.`
- `BROAD_EXACT_HEAD: Required CI / Desktop Portability 33423712599 = SUCCESS; broad green does not override literal auth red.`
- `PREDECESSOR: NIGHT-BBB-088 has no final RESULTADO DEL TURNO or matching material Issue #41 handoff and #74/#84 have not moved since CYCLE 093 facts; superseded / NOT_PASS.`
- `WHY_REASSIGNED: recalculated path makes this the highest-priority executable internal gate after #83 became tooling-blocked; retained because live evidence demands it, not because prior assignment existed.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA090 owns F2/13.2. WOZ093 owns F2/15.1 Trash only. #83 parked; no integration mutator this cycle.`

### PRIMARY

**F4 / 25.1 — identify the first causal boundary on CURRENT #74/#84, then apply at most the smallest attributable correction and regenerate literal evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact workflow state; STOP on duplicate ownership or material lineage movement.
2. Reuse #74 as sole product-corrective lineage and #84 as sole packaged-Windows evidence candidate. Do not fork another PR.
3. Treat `c6c5ecb...` red as authoritative. Do not repeat the disproven stale-head hypothesis; #84 already contains current #74.
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

**Reason:** a secondary F4 mutation would share release-chain ownership or broaden scope while #74/#84 is active; external signing/hardware work cannot be truthfully advanced without credentials/provider evidence.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-088`: NO_RESULT at CYCLE 094 preflight; no new handoff or post-C093 lineage movement; superseded; NOT_PASS.
- `NIGHT-BBB-087`: PARTIAL_LIVE_EVIDENCE / NOT_PASS; produced current lineage facts, later exact Windows Auth resolved RED.
- `NIGHT-BBB-085`: BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED; older evidence only.
