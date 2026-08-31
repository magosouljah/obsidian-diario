# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-090`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — real-browser cold/warm startup evidence`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PREDECESSOR: NIGHT-WOZ-089 had no final RESULTADO DEL TURNO nor matching material Issue #41 handoff at JOBS CYCLE 091 preflight; superseded, NOT_PASS.`
- `SERIALIZATION: PR #83 remains PARKED/TOOLING_BLOCKED; WOZ090 has NO integration mutation authorization.`
- `DISTINCT_OWNERSHIP: AAA087 owns F2/13.2 product wiring; BBB086 owns F4/#74+#84 product-auth slice; WOZ090 is read-only F2/12.1 runtime evidence.`

### PRIMARY

**F2 / 12.1 — obtain attributable real-browser cold/warm startup evidence without code mutation.**

1. Fresh preflight live integration and Issue #41; confirm exact baseline before measurement.
2. REUSE-FIRST the existing Web smoke/browser harness (`npm run test:web:smoke` or the canonical equivalent already present on the exact baseline).
3. Run only real browser/runtime evidence; do not substitute static inspection or synthetic microbenchmarks.
4. Capture cold-start and warm-start timings with browser/runtime/build identity and exact integration SHA.
5. Record observed result, methodology, repeat count if available, limitations and whether the evidence is materially attributable to current Web startup/library behavior.
6. Do not change code, branch, PR, infra, provider resources or integration.
7. Maximum claim: `F2/12.1 REAL_BROWSER_RUNTIME_EVIDENCE_OBTAINED` only if literal runtime evidence exists; otherwise BLOCKED/PENDING with exact missing dependency.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact integration SHA; browser/runtime/build identity; command/harness; cold/warm timing outputs; attributable runtime logs; limitations.  
**STOP:** browser/runtime unavailable, evidence synthetic/non-attributable, any code change required, integration moves during measurement without attribution, provider credentials required, or overlap with AAA087.

### CI-FALLBACK

`CI-FALLBACK: NONE` — PRIMARY is itself independent read-only runtime work; no safe secondary lane is necessary.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-089`: NO_RESULT at CYCLE 091 preflight; superseded; NOT_PASS.
- `NIGHT-WOZ-088`: BLOCKED_STOP. #83 exact/green remained OPEN/DRAFT; dedicated Draft→Ready action failed with connector GraphQL `Repository.fullDatabaseId`; no workaround/bypass, no merge. Issue #41 `5481554738`.
- #83 remains parked until the dedicated Ready path materially changes; runtime 160 remains UNVERIFIED and materially depends on integration of the durable waitlist candidate.
