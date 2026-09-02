# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-151`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimum productive recent-reauth seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`
- `PREDECESSOR: NIGHT-BBB-150 = NO_RESULT / SUPERSEDED / NOT_PASS; no RESULTADO DEL TURNO in this ledger and no matching Issue #41 handoff before CYCLE156.`
- `DUPLICATE_CHECK_START: no newer PR/candidate is visible for this bounded product seam; merged #53 remains the D8 decision/reuse authority.`
- `SERIALIZATION: BBB151 owns only recent-reauth seam. AAA152 owns #89. WOZ155 owns Issue #97. Do not touch Trash implementation, Review, #89/#93, Issue #97 or deployment/provenance surfaces.`

### PRIMARY

REUSE D8/#53 and expose only the minimum productive same-provider recent-reauth contract required by destructive callers.

1. Fresh preflight: live integration + Issue #41 + #53/D8 lineage + duplicate-check.
2. Reuse the decided invariant literally: fresh same-provider authorization bound to the correct BeatGaler user/session; no password/MFA/new-provider redesign.
3. If an existing production primitive already satisfies the bounded caller contract, STOP with exact reusable evidence rather than duplicate implementation.
4. If a gap remains, expose the smallest fail-closed boundary granting/verifying recent reauth for destructive callers.
5. Cover wrong user, wrong session, expired/not-fresh authorization, replay where applicable and provider failure.
6. Add focused tests. Preserve D6/D7 and Web/Desktop auth contracts.
7. One candidate/PR only if duplicate-check remains clean; exact-head applicable CI. **NO MERGE CYCLE156.**
8. Maximum claim: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; do not implement Empty Trash yet.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Evidence required:** reused D8 primitive/decision; exact functions/files; semantics; focused tests; base/head/branch/PR; exact-head CI; explicit `UNVERIFIED`; clean duplicate-check.  
**STOP:** architecture redesign, provider/payment mutation, Trash, Review, Issue #97 overlap, #89/#93 mutation, merge, duplicate candidate or widened scope.

### CI-FALLBACK

**F3 / 18.2 alpha-applicability inventory — READ-ONLY, only while PRIMARY genuinely waits on external CI/build/review after a clean candidate exists.**

- **Scope:** inventory existing reconciliation/provider evidence and unresolved 3DS/rejection/late-payment/renewal/cancel/plan-change/refund/webhook/reconciliation scenarios. Classify only `SOFTWARE_PROVEN`, `UNVERIFIED_EXTERNAL`, `NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`.
- **Evidence required:** exact PR/merge/runtime refs and explicit unresolved scenario list; state that F1/1.7→1.8 owns the eventual applicability decision.
- **STOP:** any mutation, payment/provider state change, new PR, gate promotion, overlap, or PRIMARY leaves external wait. Return to PRIMARY and recheck before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-150`: no RESULTADO DEL TURNO in this ledger and no matching Issue #41 worker handoff before CYCLE156 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; causal evidence remains reusable.
