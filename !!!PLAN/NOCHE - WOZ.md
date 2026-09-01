# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-107`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0/0.9 — REUSE PR #89 AI-assisted adversarial security audit + DNS-rebinding SSRF hardening`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`
- `CANDIDATE: PR #89 OPEN/Ready, head daf87da6ffd604ccac991311036919ae2de9bd7a, stale base_sha 816f946c09d998ee5a045b3e70b2fe4f3a4160d0.`
- `PREDECESSOR: NIGHT-WOZ-106 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff verificable al preflight JOBS CYCLE 108; SUPERSEDED / NOT_PASS. Último WOZ final verificable: NIGHT-WOZ-104 DONE / INTEGRATED PR #87 -> 38517c...; Issue #41 5486854786.`
- `WHY_ASSIGNED: camino crítico recalculado de cero: #89 sigue siendo el P1 software ejecutable independiente; sus checks old-head son verdes pero no autorizan merge contra baseline vivo. #88 permanece bloqueado por inputs/authorization RO.`
- `SERIALIZATION: WOZ107 exclusively owns #89 review/refresh/integration path. AAA104 owns F2/12.1. BBB103 owns #84. PR #85 remains external/owner-owned. #88 and #90 are separate; #90 may only be inspected READ-ONLY under the explicit fallback below.`

### PRIMARY

**F0/0.9 — review, refresh history-preserving, validate and integrate PR #89 only if exact/race-free.**

1. Fresh preflight integration and #89 base/head/scope; duplicate-check and changed-files review.
2. Review exact security semantics in the bounded slice: audit workflow, outbound DNS pinning/server path, focused regression and audit docs.
3. Verify the claimed P1 fix actually pins the already-validated public DNS resolution into the outbound request path and rejects private/reserved rebinding without weakening existing remote-artwork behavior.
4. Preserve audit truth: AI-assisted audit is not an independent pentest; #88 Authenticode remains separate and public release remains NO-GO.
5. Existing green checks on `daf87da6...` are old-base evidence only. Because #89 is stale against live `38517c...`, perform a history-preserving refresh/rebase/union onto the live integration head only if clean and scope-bounded. Conflict/scope drift => STOP.
6. Run/recheck exact-head F0/0.9 security workflow + Required CI and all applicable exact-head checks after refresh.
7. Immediately before integration, recheck exact base/head/mergeability and no competing owner/candidate. If exact-head applicable CI is green and race-free, WOZ is the **only** worker authorized this cycle to merge **PR #89 only** with expected-head protection.
8. Verify merge SHA/parents. Maximum claim: `F0/0.9 AI_ASSISTED_SECURITY_SLICE PASS/INTEGRATED` + DNS-rebinding P1 fixed. Do not claim external pentest, Authenticode, F0 global closure, or release readiness.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 and STOP.

**Required evidence:** pre/post base/head; changed files; refresh method; semantic proof of pinned-DNS request path + regression; exact-head workflow names/conclusions; expected-head merge result/parents if merged; explicit residual P1/#88 and external pentest status.  
**STOP:** conflict/scope drift, unrelated auth/Web startup/provider/deploy changes, external credentials/signing action, failed required CI, base/head race, or any integration mutation other than expected-head #89.

### CI-FALLBACK

**Trigger:** only if PRIMARY reaches genuine `WAITING_CI` after a valid refreshed #89 exact head.

`CI-FALLBACK: READ-ONLY PR #90 readiness map.`

- **Scope:** inspect PR #90 only; software/readiness workflow + operations doc. Compare its claims to live baseline and identify exact owner-only external steps still required.
- **Evidence required:** current base/head/mergeability; changed files; what is software-proven vs owner/deployment/credential evidence; whether refresh would be needed; no secret values.
- **STOP:** no mutation/rebase/merge, no OAuth credential rotation/revocation, no provider/deploy action, no history rewrite. When PRIMARY CI resolves, return to #89 and recheck it before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-106`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 108; no final result/handoff verificable observado al preflight.
- `NIGHT-WOZ-104`: `DONE / INTEGRATED`; PR #87 exact candidate `ba0d7b...` merged as `38517c8065063206fed530028e4e8d20208f3807`; parents verified `b85723e...` + `ba0d7b...`; Issue #41 `5486854786`.
- #89 old-head Required CI is SUCCESS, but base remains stale; no PASS/integration claim until refreshed exact-head evidence exists.
