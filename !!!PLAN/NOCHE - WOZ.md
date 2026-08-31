# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-099`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.2 — reuse-first reconciliation of PR #76 legal/public routes`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-098 = BLOCKED_STOP / F3/18.2 EVIDENCE_GAP_MAP_UPDATED; software reconciliation consumed, remaining provider/payment proof is external/staging/RO.`
- `CANDIDATE: PR #76 legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070; OPEN/Ready/mergeable but stale base a9d35a3... and no current exact-head applicability claimed.`
- `NEW FACTUAL GAP: F0 canonical v1 eligibility is 18+, while #76 Privacy/Terms currently say under-13/minimum-age eligibility. #76 therefore MUST NOT be integrated unchanged. PR body also records stale in-app SettingsPanel legal copy/placeholders.`
- `WHY_ASSIGNED: #76 is existing reusable material; reconciling it to current canonical business decisions advances F3/19.2 independently of AAA Review and BBB auth without creating a duplicate legal PR.`
- `SERIALIZATION: WOZ owns #76 only for this cycle. AAA096 owns F2/13.2. BBB095 owns #84/#74 auth evidence. Do not touch #83, Review Save, auth/session, Trash purge, provider/payment config, deployment/DNS or integration.`

### PRIMARY

**F3 / 19.2 — history-preserving refresh/reconciliation of existing #76, no new legal invention.**

1. Fresh preflight integration, #76, Issue #41 and current F0/F3 canonical decisions; duplicate-check before mutation.
2. Reuse #76; do not open a second legal/public-routes PR.
3. Reconcile only explicit already-decided requirements: v1 eligibility **18+**; operator/contact/domain values already canonical; billing/cancel/refund/grace terms only where already RO-approved/current; Cloud-visible language must not expose implementation provider internals.
4. Reconcile the in-app Privacy/Terms surface noted in #76 body so Settings no longer carries placeholder/old legal copy; prefer one canonical source/render path rather than duplicate prose.
5. Preserve `/privacy` and `/terms` public route intent. Do not claim DNS/deployment/SPA fallback works without runtime evidence.
6. Refresh #76 onto the live baseline using history-preserving minimal method; stop on material conflict requiring broad redesign or legal judgment not already decided.
7. Add/adjust only focused tests/build guards needed to prove route rendering/canonical-copy reuse and eligibility consistency. Fresh exact-head applicable CI required after any head change. **NO MERGE.**
8. Maximum claim: `F3/19.2 LEGAL_PUBLIC_ROUTE_CANDIDATE_RECONCILED`; independent legal review/public deployment remain UNVERIFIED and 19.2 stays OPEN.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Required evidence:** exact base/head; exact #76 files changed; explicit 18+ consistency proof; Settings canonical-copy proof; focused tests/build; exact-head CI; explicit external legal review/deployment/DNS UNVERIFIED.  
**STOP:** unresolved legal-policy choice, provider/deployment credentials, DNS/TLS, broad product redesign, overlap with AAA/BBB, integration mutation, or material conflict outside #76 scope.

### CI-FALLBACK

`CI-FALLBACK: F1 / D10.2 ALPHA_READINESS_DECISION_MAP — READ-ONLY`.

**Trigger:** ONLY if PRIMARY reaches genuine `WAITING_CI`/remote build wait after a bounded #76 head has been produced.  
**Scope:** read current F1 D10.2 literal gate, already-proven D2–D10/P0 evidence and open external tails; classify each prerequisite `PROVEN`, `BLOCKED_EXTERNAL`, or `RO_DECISION_REQUIRED`. No code/infra/provider mutations, no alpha launch, no credential use, no re-running accepted restore/cutover drills.  
**Required evidence:** exact references to current plan/Issue/GitHub for every row; one bounded decision-ready gap list.  
**STOP:** once map is complete, or next step needs RO approval/off-provider proof/real alpha execution. Then re-check PRIMARY CI before closing the turn.  
**Maximum claim:** `F1/D10.2 DECISION_MAP_READY`, never PASS/alpha authorization.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-098`: `BLOCKED_STOP / F3/18.2 EVIDENCE_GAP_MAP_UPDATED`; reconciliation core/exception queue = PROVEN_SOFTWARE; provider 3DS/rejection/late payment/renewal/cancel/upgrade/downgrade/refund/webhook/financial outcomes and 100% sandbox reconciliation remain external/unverified; Issue #41 `5485068226`.
- `NIGHT-WOZ-096`: `BLOCKED_STOP / F3/19.1 PUBLIC_SURFACE_EVIDENCE_BOUNDED`; DNS/TLS/HTTP/provider/deployment tails remain external.
- `NIGHT-WOZ-094`: `BLOCKED_STOP / F2-15.1 EMPTY_TRASH_AUDIT`; strong confirmation + bounded recent-reauth seam remain required.
- `NIGHT-WOZ-092`: #83 supported Draft→Ready tooling blocker remains materially unchanged; #83 stays PARKED.
