# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-094`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 15.1 — Trash destructive-action gap, audit-first/minimum corrective`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-093 has no final RESULTADO DEL TURNO or matching material Issue #41 handoff at JOBS CYCLE 095 preflight; superseded / NOT_PASS.`
- `WHY_REASSIGNED: global path was recalculated from live GitHub; the Empty Trash destructive subgate remains a bounded executable product gap with no duplicate candidate and no overlap with AAA/BBB.`
- `DUPLICATE_CHECK: open PR scan found no current Trash/Empty-Trash candidate. Existing SettingsPanel Trash lifecycle/purge path means REUSE-FIRST audit is mandatory before mutation.`
- `SERIALIZATION: WOZ MUST NOT touch #83, #74, #84, #72, #76, #69/#70/#81 or integration. AAA091 owns Review Save/Save All; BBB090 owns Windows auth. No integration mutator is authorized in CYCLE 095.`

### PRIMARY

**F2 / 15.1 — close or sharply reduce the literal “Vaciar Trash” destructive-action gap without widening account/auth/legal scope.**

1. Fresh preflight integration + Issue #41 + open PRs + current `SettingsPanel`/platform Trash contracts. STOP if a duplicate owner/candidate exists.
2. Audit current behavior before changing anything: determine whether permanent beat Trash purge already exists end-to-end and whether the visible action has strong confirmation and a proven recent-reauth gate.
3. REUSE existing platform Trash APIs and existing recent-reauth capability if they already satisfy the contract. Do not create a second purge architecture.
4. If a bounded gap is proven, change only the minimum Trash UI/wiring/tests required for explicit permanent-delete wording, strong confirmation, recent reauth before destructive execution, deterministic success/failure state, and no false-success removal from UI.
5. Scope is limited to `src/components/SettingsPanel.tsx`, existing Trash platform contracts/adapters and focused tests strictly needed by this action. Do not edit Privacy/Terms copy in the same file.
6. Do not modify AccountGate/auth/session implementation. If current recent-reauth API is insufficient and auth changes would be required, STOP with exact blocker/evidence rather than crossing BBB ownership.
7. New bounded WOZ branch/PR only if a real uncovered slice exists and duplicate-check remains clean; fresh exact-head applicable CI. **NO MERGE.**
8. Maximum claim: `F2/15.1 EMPTY_TRASH_DESTRUCTIVE_ACTION_CANDIDATE_READY` or `REUSE_PASS_FOR_THIS_SUBGATE` only if literal existing evidence already proves it. Do not close all 15.1 unless every requirement is covered.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration/base/head; current Trash call chain; confirmation behavior; recent-reauth call/evidence; success/failure UI semantics; changed files/functions if any; focused tests; exact-head CI; explicit UNVERIFIED 15.1 remainder.  
**STOP:** auth/session implementation change needed; server/provider destructive semantics missing; legal copy/#76 touched; AAA/BBB scope overlap; duplicate candidate; broad redesign; integration mutation; or unavailable runtime/provider credential needed for literal proof.

### CI-FALLBACK

**F3 / 19.1 — public production-surface evidence, READ-ONLY only while PRIMARY is genuinely WAITING_CI.**

- **Scope:** verify only externally observable/current public facts for canonical Web/API hostname, DNS/TLS resolution, status/support/security-abuse endpoints and sender-domain/public OAuth callback evidence where directly observable. No provider mutations, no credentials, no legal text edits, no #76 ownership.
- **Evidence required:** dated lookup/source for each fact; explicit `UNVERIFIED` for anything requiring AWS/provider console, secret OAuth configuration, sender verification or deployment credentials.
- **STOP:** any action would change DNS/provider/infra, require credentials/secrets, touch #76/legal copy, infer a private provider fact, or overlap another owner. Return to PRIMARY after the CI wait and recheck its exact head/status before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-093`: NO_RESULT at CYCLE 095 preflight; no material Trash candidate/handoff; superseded; NOT_PASS.
- `NIGHT-WOZ-092`: BLOCKED_STOP / TOOLING_EXTERNAL on #83 supported Draft→Ready connector failure; #83 remains parked and must not be retried absent a material path change.
- `NIGHT-WOZ-090`: BLOCKED_STOP on unavailable real-browser execution surface.
