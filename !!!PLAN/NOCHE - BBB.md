# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 / 25.1 — Web auth dedicated journey.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-050`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — dedicated Web auth journey evidence`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `PREDECESSOR: NIGHT-BBB-049 = PENDING / WAITING_CI; JOBS CYCLE 055 verified its exact-head CI completed green.`
- `HOLD_PR: #79 @ c6ec2910522370f2506beb71ad5e0fa0317d6a61 — OPEN exact-base; Required CI SUCCESS; intentionally HOLD_GREEN_PENDING_SERIAL_INTEGRATION while WOZ owns #78 integration to avoid two simultaneous integration-baseline races.`
- `HOLD_PR: #72 @ 904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c — stale/frozen; DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + duplicate-check F4/25.1 and consume BBB049 read-only residual map instead of repeating it.
2. Take exactly one currently `NOT_COVERED` journey: **Web/auth**. Inspect existing Web auth/session implementation and tests first.
3. Produce the smallest dedicated deterministic journey evidence proving the literal login/session/reload/logout behavior that already belongs to Web. Prefer test/harness-only changes if product behavior already satisfies the journey; only make a minimal product fix if the dedicated journey reaches a literal existing product defect and ownership does not overlap AAA.
4. Do not promote Windows/macOS/iPhone rows from this work. Do not touch #71/#72/#74 or their branches.
5. Fresh exact-head CI is required for any repository change. If product defect is found outside safe independent scope, report `PRODUCT_FINDING + STOP` rather than broadening.
6. Do not merge #79 during this turn: JOBS serialized integration to WOZ/#78 first to prevent exact-base race. #79 remains evidence-preserved and will be reconciled after baseline movement.
7. Do not touch AAA media files, F2 #69/#70, F3 #75/#76/#78, signing/notarization/provider resources.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact live base; literal Web/auth paths and journey assertions; focused tests; fresh exact-head CI for changes; explicit matrix-row recommendation only if dedicated evidence passes; no historical CI reuse.  
**STOP:** overlap with AAA; journey already has dedicated accepted evidence; defect requires broad redesign; unsafe write flow; baseline race; or non-attributable CI red.

### CI-FALLBACK

`NONE`.

**Alcance:** none preauthorized because BBB049 already completed the independent 25.1 residual read-only map and repeating it would be duplicate work.  
**Evidencia requerida:** n/a.  
**STOP:** if PRIMARY waits externally, do not invent secondary work; recheck PRIMARY once and report factual state.

## RESULTADO PROCESADO — NIGHT-BBB-049

- `STATUS: PENDING / WAITING_CI` at worker close.
- Base `a306e3b3...`; branch `bbb/f4-25.2-beta-readiness`; head `c6ec2910522370f2506beb71ad5e0fa0317d6a61`; PR #79 OPEN/Ready, one docs-only file `docs/beta/0.9.0-beta.1-readiness.md` (+84).
- Artifact contains only compact P2/P3 backlog + beta test script/result form/entry-exit criteria; no product/release/signing/provider mutation.
- JOBS CYCLE 055 later verified exact-head checks complete with no failure/in-progress and `Required CI = SUCCESS`.
- CI-FALLBACK from BBB049 completed the literal 25.1 residual map: Web all 10 NOT_COVERED; Windows import/updater AUTOMATED_PASS and remaining rows NOT_COVERED; macOS updater AUTOMATED_PASS and remaining rows NOT_COVERED; iPhone all PENDING_EXTERNAL.
- #79 is not merged and does not close global 25.2; external beta/tester/signing evidence remains.

## HOLDING / FROZEN

- #79: green exact-base candidate, intentionally serialized behind #78 integration; no mutation in BBB050.
- #72/#74/#71: frozen by prior refresh/integration dependencies.

## HISTORIAL COMPACTO

- `NIGHT-BBB-050`: ASSIGNED — F4/25.1 dedicated Web/auth journey; fallback NONE.
- `NIGHT-BBB-049`: PENDING/WAITING_CI at close; #79 exact-head CI later green; fallback residual map DONE read-only.
- `NIGHT-BBB-048`: NO_RESULT / SUPERSEDED_BY_JOBS.
