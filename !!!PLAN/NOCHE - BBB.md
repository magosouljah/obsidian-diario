# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 / 25.1 — Web auth dedicated journey.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-052`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — dedicated Web auth journey evidence`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `PREDECESSOR: NIGHT-BBB-051 remained ASSIGNED with no final RESULTADO DEL TURNO / Issue #41 handoff observable during JOBS CYCLE 057; SUPERSEDED and MUST NOT execute late.`
- `RECALCULATION: selected again from zero because Web/auth remains the highest-value independent F4 journey while #79 is serialized behind #78; not inherited merely by continuity.`
- `HOLD_PR: #79 @ c6ec2910522370f2506beb71ad5e0fa0317d6a61 — OPEN exact-base; mergeable; prior exact-head CI green; intentionally HOLD_GREEN_PENDING_SERIAL_INTEGRATION while WOZ owns #78 integration.`
- `HOLD_PR: #72 @ 904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c — stale/frozen; DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + duplicate-check F4/25.1 and consume BBB049 read-only residual map instead of repeating it.
2. Take exactly one currently `NOT_COVERED` journey: **Web/auth**. Inspect existing Web auth/session implementation and tests first.
3. Produce the smallest dedicated deterministic journey evidence proving login/session persistence across reload and logout invalidation. Prefer test/harness-only changes if product behavior already satisfies the journey; only make a minimal product fix if the dedicated journey reaches a literal independent defect and ownership does not overlap AAA.
4. Do not promote Windows/macOS/iPhone rows from this work. Do not touch #71/#72/#74 or their branches.
5. Fresh exact-head CI is required for any repository change. If product defect is outside safe independent scope, report `PRODUCT_FINDING + STOP` rather than broadening.
6. Do not merge #79 during this turn. JOBS preserves it for post-#78 reconciliation if integration moves.
7. Do not touch AAA media files, F2 #69/#70, F3 #75/#76/#78, signing/notarization/provider resources.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact live base; literal Web/auth paths and journey assertions; focused tests; fresh exact-head CI for changes; explicit matrix-row recommendation only if dedicated evidence passes; no historical CI reuse.  
**STOP:** overlap with AAA; journey already has dedicated accepted evidence; defect requires broad redesign; unsafe write flow; baseline race; or non-attributable CI red.

### CI-FALLBACK

`NONE`.

**Alcance:** none preauthorized. BBB049 already completed the independent 25.1 residual read-only map, and repeating it would be duplicate work.  
**Evidencia requerida:** n/a.  
**STOP:** if PRIMARY waits externally, do not invent secondary work; recheck PRIMARY once and report factual state.

## RESULTADOS PROCESADOS

- `NIGHT-BBB-051`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS` in CYCLE 057; no dedicated Web/auth evidence accepted.
- `NIGHT-BBB-050`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-BBB-049`: `PENDING / WAITING_CI`; #79 exact-head CI later green; fallback residual map DONE read-only.

## HOLDING / FROZEN

- #79: green exact-base candidate, intentionally serialized behind #78 integration; no mutation in BBB052.
- #72/#74/#71: frozen by prior refresh/integration dependencies.

## HISTORIAL COMPACTO

- `NIGHT-BBB-052`: ASSIGNED — F4/25.1 dedicated Web/auth journey; fallback NONE.
- `NIGHT-BBB-051`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-049`: PENDING/WAITING_CI at close; #79 exact-head CI later green; fallback residual map DONE read-only.
