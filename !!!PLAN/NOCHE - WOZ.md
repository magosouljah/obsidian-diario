# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-087`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — PR #83 exact-head Ready→merge transaction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `CANDIDATE: PR #83 OPEN/DRAFT, mergeable, exact base 816f946c..., head 803b2143e6ea03f6549118e9241fee320dfccdee, 3 files.`
- `EXACT_HEAD_CI: F3 20.2 Durable Waitlist run 33388377959 SUCCESS; Test - Desktop Portability 33388377963 SUCCESS; D6 33388377952 SUCCESS; D7 33388377964 SUCCESS.`
- `PREDECESSOR: NIGHT-WOZ-086 BLOCKED_STOP / F3 19.1 evidence reconciled; external domain/provider blocker map processed by JOBS.`
- `PROCESS_CHANGE: current connector surface exposes a dedicated authorized Draft→Ready action; prior Repository.fullDatabaseId failure must not be bypassed or assumed resolved until the direct action succeeds.`
- `SERIALIZATION: WOZ087 is the only worker authorized to mutate integration this cycle, and only for #83 if every exact-head/race condition remains satisfied.`

### PRIMARY

**F3 / 20.2 — finish the bounded #83 process/integration transaction, nothing more.**

1. Fresh preflight integration HEAD, #83 state/base/head/mergeability, changed-file scope, Issue #41 and exact-head workflow state.
2. STOP if integration moved from `816f946c...`, #83 head/base/scope changed, mergeability changed adversely, CI is no longer exact/green, or another owner mutated the candidate.
3. If still OPEN/DRAFT and exact, invoke only the dedicated authorized Draft→Ready action. Do not use GraphQL workarounds or manual bypasses.
4. Re-read #83 after Ready. Require OPEN/non-draft, same head `803b2143...`, same exact base `816f946c...`, mergeable, same 3-file scope and exact-head applicable green CI.
5. If all conditions remain true, merge #83 using exact expected head. No unrelated merge and no force/bypass.
6. Verify resulting integration HEAD/merge SHA and record it in RESULTADO DEL TURNO + Issue #41.
7. Maximum claim: `F3/20.2 DURABLE_WAITLIST_INTEGRATED`. **Do not close 20.2**: runtime 160, latency/error/queue/recovery/no-loss/no-cross-tenant and measured safety margin remain independently required.
8. Do not start runtime-160 work, #76, DNS/provider mutations, payments, AAA/BBB work or any next task after merge. STOP.

**Required evidence:** pre/post integration SHA; #83 exact base/head/draft/mergeable/scope; exact-head workflow IDs/conclusions; Ready transition result; exact expected-head merge result; final integration SHA; explicit runtime-160 UNVERIFIED.  
**STOP:** any race/head/base/scope movement, Ready action failure, CI regression, mergeability conflict, unexpected integration movement or any need for workaround/bypass.

### CI-FALLBACK

`CI-FALLBACK: NONE` — post-#83 runtime 160 materially depends on successful #83 integration and therefore is not independent; F3/19.1 now requires external owner/provider facts.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-086`: BLOCKED_STOP / F3 19.1 evidence reconciled. Intended `beatgaler.com` surface identified from #76 but live DNS/TLS/API/status/OAuth/sender/deployment proof remains MISSING/UNVERIFIED; external owner/provider inventory/action required. No mutation.
- `NIGHT-WOZ-085`: BLOCKED_STOP — #83 exact/green; old Ready action failed on connector GraphQL `Repository.fullDatabaseId`; no merge.
- `NIGHT-WOZ-084`: NO_RESULT; superseded; NOT_PASS.
