# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-086`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.1 — production surface evidence / blocker reduction, READ-ONLY`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-085 BLOCKED_STOP; #83 remains OPEN/DRAFT at 803b2143... because authorized Ready-for-review connector mutation fails on Repository.fullDatabaseId.`
- `PARKED_DEPENDENCY: #83 remains exact and green but no repeated identical Ready attempt is authorized this turn.`
- `SERIALIZATION: no integration mutation is authorized in CYCLE 087.`

### PRIMARY

**F3 / 19.1 — verify the real production/public surface that can be verified without changing infrastructure.**

1. Fresh preflight live integration, Issue #41, F3 plan and existing #76/public-route evidence; duplicate-check.
2. READ-ONLY only. Do not modify DNS, AWS/provider resources, deployment, OAuth callbacks, sender configuration, GitHub integration, #76 or product code.
3. Inventory the currently intended/observable public surfaces needed by 19.1: product domain, API hostname, status/support/security-abuse endpoints or addresses, sender-domain surface, TLS, redirects and OAuth callback destinations where discoverable.
4. For each real hostname/endpoint that exists, capture attributable current evidence: DNS resolution/record class where visible, HTTPS/TLS availability, certificate/expiry identity where available, HTTP status/redirect chain, and deployment/provider identifier only if already safely readable.
5. Separate VERIFIED from MISSING/UNVERIFIED. Do not infer deployment from configuration files alone and do not claim sender/OAuth validity from mere strings.
6. Produce the minimum blocker map required to make 19.1 executable next: exact missing domain/record/callback/deployment/owner action, without performing it.
7. #76 legal/public routes stays frozen; independent legal review is outside this assignment.
8. Maximum claim: `F3/19.1 PRODUCTION_SURFACE_EVIDENCE_RECONCILED`; 19.1 closes only if every literal production requirement is actually evidenced.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** observation timestamp; exact hostname/endpoint; DNS/TLS/HTTP/redirect evidence; certificate details when available; deployment/provider ID only when safely readable; explicit MISSING/UNVERIFIED matrix; no secrets.  
**STOP:** any mutation/credential is required, only synthetic/local evidence exists, public target cannot be identified factually, scope reaches legal text/#76 mutation, or evidence becomes ambiguous/stale during observation.

### CI-FALLBACK

`CI-FALLBACK: NONE` — PRIMARY is read-only external/runtime reconciliation and does not create a legitimate CI wait lane.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-085`: BLOCKED_STOP — #83 exact/green; authorized Ready action failed on connector GraphQL `Repository.fullDatabaseId`; no merge; runtime 160 remains unverified.
- `NIGHT-WOZ-084`: NO_RESULT; superseded; NOT_PASS.
- `NIGHT-WOZ-082`: prior same process blocker; no merge.
