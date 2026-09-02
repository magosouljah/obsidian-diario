# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-153`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89, refresh/revalidate DNS-rebinding corrective on live baseline`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`
- `PREDECESSOR: NIGHT-AAA-152 = NO_RESULT / SUPERSEDED / NOT_PASS; no RESULTADO DEL TURNO in this ledger and no matching worker handoff before CYCLE157.`
- `LIVE_FACT: PR #89 remains OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a on recorded base 816f946c..., while live integration remains c2766fb...; old exact-head Required CI is green but the dedicated F0/0.9 security gate on that stale head remains FAILURE and cannot be waived.`
- `SERIALIZATION: AAA153 exclusively owns #89 mutation/integration. BBB152 owns recent-reauth. WOZ156 owns Issue #97 / PR #100. Do not touch #93, #97/#100, recent-reauth/Trash/Review, or production deployment/source-proof execution.`

### PRIMARY

REUSE PR #89 and close the smallest real F0/0.9 P1 lane without a duplicate PR.

1. Fresh preflight: live integration, #89 base/head/files/checks, Issue #41 and duplicate-check whether the DNS-pinning corrective is already integrated elsewhere.
2. Preserve #89 lineage/history. If still needed, reconcile it onto the live baseline without widening the security/server/DNS/docs slice.
3. Do not waive the red security gate. Resolve only the minimum in-scope precondition behind the known Rust `frontendDist ../dist` failure, or prove the refreshed baseline already supplies it; no Tauri/product redesign.
4. Run applicable exact-head F0/0.9 security CI after refresh. DNS rebinding regression plus applicable dependency/security/TS/cloud/Rust contracts must be green.
5. Conditional expected-head merge of #89 is authorized only if refreshed scope is exact, applicable CI is SUCCESS, no required review blocker exists and integration race-check is clean. If WOZ156 moves integration first, refresh/revalidate before merge.
6. After merge verify resulting integration SHA/parents. Maximum claim: `F0_0.9_PR89_INTEGRATED`; do not claim external pentest/public-release readiness.
7. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Evidence required:** live integration SHA; #89 start/end base+head; duplicate/divergence classification; exact changed files; exact-head run/check IDs; dedicated gate result; failure resolution; review/merge state; merge SHA/parents if merged; explicit `UNVERIFIED`.  
**STOP:** duplicate PR, scope drift outside #89/security gate, any #93/#97/#100/recent-reauth/Trash/Review mutation, merge without exact-green/race-free evidence, or unsupported gate promotion.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

Reason: F2/12.1 runtime proof is SHA-dependent on canonical integration; #97/#100 and recent-reauth already have owners; #93 awaits 1.7 applicability. No independent fallback is safe.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-152`: no RESULTADO DEL TURNO in this ledger and no matching worker handoff before CYCLE157 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-AAA-114`: durable Review gap remains reusable evidence only; F2/13.2 stays open.
