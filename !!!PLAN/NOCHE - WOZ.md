# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-100`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.2 — reuse-first reconciliation of PR #76 legal/public routes`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-099 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff y #76 no se movió al preflight CYCLE 101; SUPERSEDED / NOT_PASS.`
- `CANDIDATE: PR #76 @ 36d218609cf2488997755312fa2dafd0a019d070; OPEN/Ready/mergeable; stale base a9d35a3...; reusable but unsafe unchanged.`
- `FACTUAL GAP: #76 eligibility 13+/minimum age contradice requisito canónico v1 18+; PR body además reconoce SettingsPanel legal copy/placeholders viejos.`
- `WHY_ASSIGNED: recalculado desde cero; #76 es el único candidate reusable para 19.2 y su reconciliación es independiente de AAA Review y BBB auth.`
- `SERIALIZATION: WOZ owns #76 only. AAA097 owns F2/13.2. BBB096 owns #84 diagnostics. Do not touch #83, auth/session, Trash purge, provider/payment config, DNS/deployment or integration.`

### PRIMARY

**F3 / 19.2 — reconcile existing #76 to canonical current decisions; no legal invention.**

1. Fresh preflight integration/#76/Issue #41/F0-F3 decisions; duplicate-check antes de mutar.
2. Reuse #76; no segundo legal/public-routes PR.
3. Reconcile only explicit decided requirements: eligibility **18+**, operator/contact/domain values already canonical, and owner-approved billing/cancel/refund/grace terms. Do not invent policy.
4. Reconcile Settings Privacy/Terms surface to reuse one canonical copy/source instead of stale placeholders/duplicate prose.
5. Preserve `/privacy` and `/terms` route intent; no claim of DNS/deployment/SPA fallback without runtime evidence.
6. History-preserving refresh #76 onto live baseline. STOP on broad conflicts or unresolved legal judgment.
7. Focused route/render/canonical-copy/18+ consistency tests + fresh exact-head applicable CI after any head change. **NO MERGE.**
8. Maximum claim: `F3/19.2 LEGAL_PUBLIC_ROUTE_CANDIDATE_RECONCILED`; external legal review and production deployment remain UNVERIFIED.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/head, #76 changed files, 18+ consistency, Settings canonical-copy reuse, focused tests/build, exact-head CI, external legal/deployment/DNS UNVERIFIED.  
**STOP:** unresolved policy/legal choice, provider/deployment credentials, DNS/TLS, broad redesign, overlap with AAA/BBB, integration mutation or conflict beyond #76 scope.

### CI-FALLBACK

`CI-FALLBACK: F1 / D10.2 ALPHA_READINESS_DECISION_MAP — READ-ONLY`.

**Trigger:** ONLY if PRIMARY reaches genuine `WAITING_CI` after producing a bounded #76 head.  
**Scope:** D10.1 is now factual PASS; map D10.2 remaining prerequisites against current D2–D10/P0 evidence and classify each `PROVEN`, `BLOCKED_EXTERNAL`, or `RO_DECISION_REQUIRED`. No alpha launch, provider/infra mutation, credential use or repeated accepted drills.  
**Required evidence:** exact plan/Issue/GitHub reference per row; bounded decision-ready gap list.  
**STOP:** map complete or next step needs RO/real-alpha/external action; then recheck PRIMARY CI.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-099`: `NO_RESULT / SUPERSEDED / NOT_PASS` at CYCLE 101; no final result/handoff and #76 remained exact `36d2186...` on stale base.
- `NIGHT-WOZ-098`: `BLOCKED_STOP / F3/18.2 EVIDENCE_GAP_MAP_UPDATED`; Issue #41 `5485068226`.
- `NIGHT-WOZ-094`: Empty Trash audit proved confirmation/recent-reauth/action-boundary gaps.
- `NIGHT-WOZ-092`: #83 supported Draft→Ready tooling blocker; #83 remains PARKED.
