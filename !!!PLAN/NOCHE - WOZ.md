# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-093`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 15.1 — Trash destructive-action gap, audit-first/minimum corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-092 = BLOCKED_STOP. PR #83 remains exact/open/draft/green; the explicitly supported Draft→Ready action failed inside connector on Repository.fullDatabaseId. Do not retry the same operation this cycle.`
- `DUPLICATE_CHECK: open PR scan found no current Trash/Empty-Trash candidate. SettingsPanel already contains Trash lifecycle/purge state, so REUSE-FIRST audit is mandatory before any mutation.`
- `SERIALIZATION: WOZ MUST NOT touch #83, #74, #84, #72, #76, #69/#70/#81 or integration. AAA090 owns Review Save/Save All; BBB089 owns Windows auth. No integration mutator is authorized in CYCLE 094.`

### PRIMARY

**F2 / 15.1 — close or sharply reduce the literal “Vaciar Trash” destructive-action gap without widening account/auth/legal scope.**

1. Fresh preflight integration + Issue #41 + open PRs + current `SettingsPanel`/platform Trash contracts. STOP if a duplicate owner/candidate exists.
2. Audit current behavior before changing anything: determine whether permanent beat Trash purge already exists end-to-end and whether the visible action has strong confirmation and a proven recent-reauth gate.
3. REUSE existing platform Trash APIs and existing recent-reauth capability if they already satisfy the contract. Do not create a second purge architecture.
4. If a bounded gap is proven, change only the minimum Trash UI/wiring/tests required for: explicit permanent-delete wording, strong confirmation, recent reauth before destructive execution, deterministic success/failure state, and no false-success removal from UI.
5. Scope is limited to `src/components/SettingsPanel.tsx`, existing Trash platform contracts/adapters and focused tests strictly needed by this action. Do not edit Privacy/Terms copy in the same file.
6. Do not modify AccountGate/auth/session implementation. If current recent-reauth API is insufficient and auth changes would be required, STOP with exact blocker/evidence rather than crossing BBB ownership.
7. New bounded WOZ branch/PR only if a real uncovered slice exists and duplicate-check remains clean; fresh exact-head applicable CI. **NO MERGE.**
8. Maximum claim: `F2/15.1 EMPTY_TRASH_DESTRUCTIVE_ACTION_CANDIDATE_READY` or `REUSE_PASS_FOR_THIS_SUBGATE` only if literal existing evidence already proves it. Do not close all 15.1 unless every requirement is actually covered.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration/base/head; current Trash call chain; confirmation behavior; recent-reauth call/evidence; success/failure UI semantics; changed files/functions if any; focused tests; exact-head CI; explicit UNVERIFIED 15.1 remainder.  
**STOP:** auth/session implementation change needed; server/provider destructive semantics missing; legal copy/#76 touched; AAA/BBB scope overlap; duplicate candidate; broad redesign; integration mutation; or unavailable runtime/provider credential needed for literal proof.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

**Reason:** #83 remains materially blocked on the broken supported Ready transition and runtime-160 depends on its integration; retry/readiness mutation would repeat a verified blocker. Other F2/F3 work would broaden ownership or depend on external execution surfaces.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

### `NIGHT-WOZ-092` — `BLOCKED_STOP`

- Integration before/postcheck: `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; no mutation.
- PR #83: OPEN/DRAFT, merged=false, mergeable=true, base exact `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`, exact 3-file scope.
- Exact-head Required CI remains SUCCESS.
- Dedicated `mark_pull_request_ready_for_review` was attempted exactly once as authorized and failed with `GithubGraphQLAPIError` because `Repository.fullDatabaseId` is undefined; immediate postcheck showed no state/head/base/scope change.
- No workaround/bypass and no merge. Issue #41 `5482892475`.
- F3/20.2 runtime 160, latency/error/queue/recovery, no-loss/no-cross-tenant and measured margin vs expected 80 remain UNVERIFIED.

Earlier relevant: `NIGHT-WOZ-090` BLOCKED_STOP on unavailable real-browser execution surface.
