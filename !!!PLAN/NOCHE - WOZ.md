# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-104`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0/0.6 + F3/19.1 — REUSE PR #87 public security/status software candidate`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ b85723e1b3016d24bdb943393e796ccdb744247d`
- `CANDIDATE: PR #87 OPEN/Ready/mergeable, exact base live, head ba0d7b689e587da42cc8105b22d0ed0c206bc064.`
- `PREDECESSOR: NIGHT-WOZ-103 no final ledger/handoff observado al preflight, pero GitHub real prueba que su candidate #86 fue merged como b85723e...; JOBS procesa la integración por evidencia GitHub, no inventa worker result.`
- `WHY_ASSIGNED: #86 ya cerró su implementation slice. #87 está refresh-synced al nuevo baseline y sus seis workflows observados en exact head terminaron SUCCESS; es el siguiente candidate reusable que reduce tails F0/F3 sin fabricar runtime.`
- `SERIALIZATION: WOZ104 exclusively owns #87 review/integration path. AAA101 owns F2/12.1. BBB100 owns #84. PR #85 remains external/owner-owned. Do not touch #74/#84/#85/#76/#83 or DNS/TLS/deploy/provider infra.`

### PRIMARY

**F0/0.6 + F3/19.1 — verify and, only if exact/race-free, integrate PR #87 software slice.**

1. Fresh preflight integration and #87 base/head/scope; duplicate-check and changed-files review.
2. Verify exact semantics: RFC9116 security.txt source/expiry/canonical; exact non-SPA serving; low-maintenance status surface; no internal health leakage; deploy script remains fail-safe when status DNS is absent.
3. Separate `PROVEN_SOFTWARE` from `UNVERIFIED_RUNTIME/EXTERNAL`: status DNS, certificate SAN, production deployment and public runtime are not implied by merge.
4. Recheck all applicable exact-head workflows at `ba0d7b...`; observed pre-assignment: D6, D7, Public Operations, Web Production Build, Desktop Portability SUCCESS; Upgrade 21.2 skipped/non-applicable.
5. Recheck base/head immediately before integration. If candidate remains exact `base=b85723e...`, expected head `ba0d7b...`, mergeable and applicable CI green, WOZ is the **only** worker authorized this cycle to merge **PR #87 only**.
6. Verify resulting integration SHA/parents and no race. Maximum claim: F0/0.6 + F3/19.1 **software implementation slice PASS/INTEGRATED**; runtime/DNS/support/legal external tails remain OPEN.
7. Escribir RESULTADO DEL TURNO aquí + Issue #41 and STOP.

**Required evidence:** base/head; changed files; exact-head workflow names/conclusions; semantics/no-leak review; expected-head merge result + parents if merged; explicit runtime/DNS/deploy UNVERIFIED.  
**STOP:** scope drift, owner collision with #85, DNS/TLS/deploy/credentials action, failed/non-applicable ambiguity in required checks, base/head race, or any integration mutation other than expected-head #87.

### CI-FALLBACK

`CI-FALLBACK: NONE` — PRIMARY is already exact-head green at assignment; no independent fallback is needed or safe.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-103`: no final ledger/handoff observed, so no worker-completion claim. GitHub independently proves PR #86 merged as `b85723e1b3016d24bdb943393e796ccdb744247d` with parents old baseline `816f946c...` and candidate `200474d...`.
- JOBS CYCLE 105 promotes only the #86 release/provenance **implementation slice** from that verifiable integration; external/admin release tails remain open.
