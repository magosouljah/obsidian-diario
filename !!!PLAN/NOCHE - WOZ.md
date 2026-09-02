# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-152`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — REUSE PR #98 production Web MTProto cleanup; exact-head validation + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`
- `PREDECESSOR: NIGHT-WOZ-151 = NO_RESULT / SUPERSEDED / NOT_PASS; no RESULTADO DEL TURNO nor Issue #41 worker handoff verified after JOBS CYCLE152.`
- `LIVE_PR_FACT: #98 OPEN/Ready/mergeable, exact base aa4450956579de381e82acf06c660b658c703cd1, head 00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c, one commit / six changed files.`
- `LIVE_CI_FACT_AT_ASSIGNMENT: D6 33575511574 SUCCESS; D7 33575511573 SUCCESS; Web Production Build 33575511615 SUCCESS; Productive Temp Auth Compile 33575511604 SUCCESS; F0 secret scan 33575511622 SUCCESS; Test - Desktop Portability / Required CI run 33575511576 IN_PROGRESS.`
- `SERIALIZATION: WOZ152 exclusively owns PR #98 mutation/integration. AAA149 owns runtime evidence only. BBB148 owns recent-reauth. PR #89 has NO mutation owner this cycle and may only be inspected READ-ONLY as the explicit fallback below. #93 remains mutation-unassigned.`

### PRIMARY

REUSE PR #98 and integrate it only if exact evidence remains sufficient; do not mix startup-performance #97 into the cleanup PR.

1. Fresh preflight integration HEAD, PR #98 base/head/mergeability/changed files, Issue #41, reviews/threads and current exact-head workflow results.
2. Duplicate-check equivalent production MTProto fixes integrated after #96 or newer competing candidate. If equivalent/newer work supersedes #98, STOP with evidence.
3. Verify scope remains exactly the six intended production files: `cloud-server/productive-temp-auth-boundary.js`, `src/App.tsx`, `src/features/cloud/webTransport.worker.ts`, `src/platform/contracts.ts`, `src/platform/desktopAdapter.ts`, `src/platform/webAdapter.ts`; one bounded commit unless factual head movement is justified and revalidated.
4. Treat production claims as evidence requiring exact identity: confirm what can be tied to #98 head versus source-unbound runtime observation. Do not infer a deployed SHA from a successful behavior alone.
5. Wait for exact-head applicable Required CI. Run `33575511576` must finish SUCCESS or be superseded by an exact-head applicable successful run. Existing D6/D7/Web build/temp-auth compile/secret-scan successes remain supporting evidence only.
6. The Strix billing comment is an external auxiliary review failure; do not silently waive a canonical required security gate. Determine whether it is actually required by repository policy. If required, STOP; if not required, record it as `UNVERIFIED_EXTERNAL/AUXILIARY` rather than calling it green.
7. Do **not** implement Issue #97 in PR #98. #97 explicitly requires post-cleanup cross-platform startup/reveal performance work and overlaps `src/App.tsx`; keep it a separate next blocker.
8. Immediately before integration recheck live integration HEAD, exact #98 base/head, changed files, mergeability, review blockers and exact-head applicable CI.
9. If exact/green/race-free and runtime evidence is sufficient for the candidate's claimed functional slice, WOZ152 is authorized to expected-head merge **PR #98 only**, then verify merge SHA + parents + new integration HEAD.
10. Maximum claim after merge: `PR98_PRODUCTION_WEB_MTProto_CLEANUP_INTEGRATED`; F2/12.1 PASS still requires JOBS close review of exact runtime evidence and #97 remains a separate pre-Beta blocker.
11. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** duplicate-check; #98 exact start/end base/head; exact six-file inventory; workflow run IDs/conclusions; review/thread state; deployment-source binding classification; race-check; merge SHA/parents if merged; explicit `UNVERIFIED`.  
**STOP:** Required CI failure/cancel, unresolved required review/security gate, source/head movement not revalidated, baseline race, scope drift into #97/recent-reauth/#89/#93, or any integration mutation other than expected-head #98.

### CI-FALLBACK

**PR #89 / F0 0.9 strictly READ-ONLY refresh-readiness inventory — only while PRIMARY #98 genuinely waits on external CI/review/build.**

- **Independence:** #89 files are disjoint from #98: `.github/workflows/f0-0.9-security-audit.yml`, `cloud-server/outbound-dns-pinning.js`, `cloud-server/server.js`, `cloud-server/tests/outbound-dns-pinning.test.cjs`, and two security audit docs. No shared branch/PR/lock with #98.
- **Scope:** inspect #89 exact base/head/current failed F0/0.9 gate, duplicate-check whether its DNS-pinning fix is already present elsewhere, and prepare a factual minimal refresh/revalidation plan. **No mutation, no rerun, no review, no merge.**
- **Evidence required:** live integration SHA; #89 start/end head; base divergence; current failed run and causal evidence; changed-file inventory; classification `REUSE_REFRESHABLE / SUPERSEDED / SCOPE_CHANGED`.
- **STOP:** any mutation/rerun/review/merge/new PR/gate promotion/head movement/overlap, or as soon as #98 PRIMARY leaves external wait. Return to #98 and recheck PRIMARY before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-151`: no matching final result/handoff verified by JOBS CYCLE153 preflight → `NO_RESULT / SUPERSEDED / NOT_PASS`.
