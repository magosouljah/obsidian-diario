# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-098`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — consume exact-head #84 diagnostic failure and resolve causal boundary`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 remains the only product-corrective lineage; do not mutate it in this assignment.`
- `EVIDENCE_CANDIDATE: PR #84 OPEN/Ready @ f53d46f39ece94f6de74f2f21a508ce01497ac41; exact base live.`
- `PREDECESSOR: NIGHT-BBB-097 reached WAITING_CI after diagnostic-only sanitized first-request instrumentation; post-turn GitHub authority now shows the exact-head Windows Auth Journey completed FAILURE.`
- `AUTHORITATIVE_RUN: F4 - 25.1 Windows Auth Journey 33449587244 / job 99676242317 @ f53d46f... = FAILURE at Run isolated Windows auth assertions. Other exact-head checks including Desktop Portability, Windows Import, Web Production Build, D6 and D7 are green but do not substitute the literal auth journey.`
- `WHY_ASSIGNED: CI wait is over; the next safe step is to consume the newly generated sanitized first-request evidence and attribute harness vs product/service without speculation.`
- `SERIALIZATION: BBB owns #84 evidence/harness only. AAA099 owns public Web bootstrap functional bug. WOZ102 is D10.2 READ-ONLY. Do not touch public Web bootstrap, Review, Trash, #83/#76/#85/provider/deploy/integration.`

### PRIMARY

**F4 / 25.1 — inspect the exact failed run, identify the first sanitized unexpected request, then make only a causally authorized harness correction.**

1. Fresh preflight integration/#74/#84/Issue #41 and exact run `33449587244`; STOP on head/base race or duplicate owner.
2. Retrieve the sanitized diagnostic output from job `99676242317` and record only `{method, pathname/requestClass}` for the **first** unexpected request. Never record query/body/headers/token/password/secret values.
3. Classify the causal boundary as exactly one of: `HARNESS_ONLY_PROVEN`, `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN`, or `AMBIGUOUS`.
4. If and only if `HARNESS_ONLY_PROVEN`, apply the minimum corresponding allowlist/mock correction on #84; keep literal token-persistence + AccountGate-exit assertions unchanged and run one fresh packaged Windows Auth journey plus applicable exact-head CI.
5. If `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN` or `AMBIGUOUS`, STOP without product changes. JOBS must authorize any subsequent product/service corrective.
6. No third auth PR, no assertion weakening, no broad harness rewrite, **NO PRODUCT MUTATION / NO MERGE**.
7. PASS may be claimed only if the unchanged literal packaged assertions actually succeed on the exact new head.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact base/#74/#84 heads; run/job IDs; first sanitized tuple; causal classification; changed files if any; unchanged assertions; fresh run if correction is authorized; exact-head CI; explicit UNVERIFIED.  
**STOP:** product/service mutation needed; tuple cannot be recovered without sensitive leakage; attribution remains ambiguous; unrelated file needed; integration mutation; auth/security redesign.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-097`: worker handoff `WAITING_CI`; diagnostic-only head `f53d46f39ece94f6de74f2f21a508ce01497ac41`, Issue #41 `5486012736`. Post-turn exact-head GitHub run `33449587244` / job `99676242317` completed **FAILURE**; therefore `NOT_PASS`, CI wait resolved.
- `NIGHT-BBB-095`: `BLOCKED_STOP / HARNESS_SERVICE_BLOCKED`; predecessor trace lacked request identity.
