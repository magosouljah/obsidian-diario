# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-088`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — attribute and correct current exact #74/#84 packaged Windows auth failure`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 @ d1593d368e1015abb6a25bf98e5fa8586664ac95.`
- `EVIDENCE_CANDIDATE: PR #84 @ c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61; OPEN/Ready/mergeable; compare proves #84 contains exact current #74 head and is 3 commits ahead.`
- `PREDECESSOR: NIGHT-BBB-087 has no correctly labelled final RESULTADO DEL TURNO in the night ledger. Live GitHub nevertheless proves its bounded lineage moved and fresh CI resolved; process as factual partial evidence, NOT_PASS.`
- `AUTHORITATIVE_FAILURE: exact #84 Windows Auth Journey run 33423712589, job 99592060690, FAILURE at tests/e2e/auth-flow.e2e.mjs:64: Desktop login did not persist the returned session token.`
- `OTHER_EXACT_HEAD_CHECKS: Desktop Portability 33423712599 SUCCESS; D6 33423712621 SUCCESS; D7 33423712587 SUCCESS; Web Production Build 33423712565 SUCCESS; Windows Import Journey 33423712584 SUCCESS.`
- `SERIALIZATION: BBB MUST NOT merge or mutate integration. AAA089 owns F2/13.2. WOZ092 exclusively owns #83 Ready/exact-head/integration transaction.`

### PRIMARY

**F4 / 25.1 — identify the first causal failure on the CURRENT corrective, then make at most the minimum attributable product correction and regenerate exact-lineage evidence.**

1. Fresh preflight integration, #74, #84, Issue #41 and exact workflow state; STOP on duplicate ownership or unexpected lineage movement.
2. Reuse #74 as the sole product-corrective lineage and #84 as the sole packaged-Windows evidence candidate. Do not fork another PR.
3. Treat `c6c5ecb...` failure as authoritative current evidence: #84 already contains #74 `d1593d3...`; do not repeat the stale-head hypothesis.
4. Attribute the first causal boundary before changing product: packaged runtime classification, session write path, storage visibility, or AccountGate transition. Capture a literal assertion/log that distinguishes them.
5. Only if attribution is conclusive, apply the smallest correction within the existing platform/session boundary on #74. No auth/security contract redesign, backend change, token-policy weakening, or unrelated surface change.
6. Refresh #84 history-preservingly onto the resulting exact #74 head while keeping the isolated Windows auth harness semantics stable; record ancestry/head mapping.
7. Re-run the literal packaged Windows/Tauri journey. Require BOTH `beatgaler:account-session:v1 = e2e-session-token` and AccountGate exit.
8. Any moved #74/#84 head requires fresh applicable exact-head CI; record exact run/job IDs and literal assertion results.
9. **NO MERGE.** Maximum green claim: `F4/25.1 WINDOWS_AUTH_CURRENT_EVIDENCE_READY`; global 25.1 remains OPEN for uncovered journeys.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration/#74/#84 pre/post heads; compare/ancestry; first causal assertion from the packaged runner; changed-file/function map if any; literal token-persistence + AccountGate-exit result; exact-head CI run/job IDs; explicit NOT_COVERED rows.  
**STOP:** root cause requires auth/security redesign, backend/provider changes, unrelated product files, integration mutation, #72/AAA Review overlap, or cannot be attributed after one bounded diagnostic pass.

### CI-FALLBACK

`CI-FALLBACK: NONE` — no independent release-chain work is safe while the same #74/#84 ownership and packaged-evidence transaction is active.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-087`: no correctly labelled final night result; live bounded work observed. #74 moved to `d1593d3...`, #84 to `c6c5ecb...`; exact #84 Windows auth run `33423712589` / job `99592060690` failed on missing persisted session token. Processed PARTIAL_LIVE_EVIDENCE / NOT_PASS; superseded by BBB088.
- Late Issue #41 WAITING_CI handoff on this lineage recorded `c6c5ecb...`; CI has since resolved red, so WAITING_CI is no longer current.
- `NIGHT-BBB-085`: BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED; older exact-lineage failure only.
