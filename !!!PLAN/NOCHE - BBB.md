# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-107`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 Windows packaged-auth harness reconstruction + exact-head proof`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-BBB-106 dejó NO_RESULT verificable al preflight JOBS CYCLE 112; SUPERSEDED / NOT_PASS.`
- `AUTHORITATIVE_LINEAGE: #84 OPEN/Ready @ f53d46f39ece94f6de74f2f21a508ce01497ac41; recorded base 816f946c... stale. Prior literal Windows Auth run 33449587244 = FAILURE.`
- `CAUSAL_FACT: BBB105 established HARNESS_ONLY_PROVEN for broad fetch interception swallowing WDIO/Tauri plugin IPC, including POST /plugin%3Awdio%7Cget_window_states.`
- `SERIALIZATION: BBB107 owns #84 evidence/harness only. AAA108 owns F2/13.2. WOZ111 owns #92. No product-auth mutation, #92/#89, Review/Trash, provider/deploy or integration mutation.`

### PRIMARY

**F4 / 25.1 — reconstruct/refresh the evidence candidate on live baseline, apply only the proven harness correction, and obtain literal packaged Windows Auth evidence.**

1. Fresh preflight integration head, #74/#84 lineage, changed files, Issue #41 and ownership.
2. Build a clean history-preserving successor of #84 from live baseline, preserving only the authorized #84 evidence/harness delta and exact intended #74 product-corrective lineage already under test.
3. Apply only the minimum harness/service boundary correction so WDIO/Tauri plugin IPC is not consumed by the auth HTTP mock/interceptor. Keep `/auth/health` + `/auth/login` stubs and literal product assertions unchanged.
4. **NO PRODUCT MUTATION.** If reconstruction reveals product-side divergence or requires changing auth/session product logic, STOP `PRODUCT_SIDE_REQUIRED`.
5. Run fresh literal packaged Windows Auth. PASS requires returned session token persisted and AccountGate exited with assertions unchanged.
6. Run all applicable exact-head CI on the same exact candidate.
7. One bounded PR/evidence lineage only. **NO MERGE CYCLE 112.**
8. Claim máximo: `F4/25.1 WINDOWS_AUTH_CANDIDATE_EXACT_GREEN` only if literal packaged journey + applicable exact-head CI are SUCCESS.
9. Write RESULTADO DEL TURNO here + Issue #41 and STOP.

**Required evidence:** live base; reconstruction method; source/target heads; exact files; unchanged auth assertions/stubs; harness diff; packaged Windows run/job; exact-head CI; explicit UNVERIFIED.  
**STOP:** product mutation required, sensitive leakage, unrelated files, ambiguous new causal result, unsafe scope drift, duplicate PR, integration mutation.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO — NIGHT-BBB-107

PRIMARY:
- STATUS: `WAITING_CI`
- baseline: `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- branch/head: `bbb/night-25.1-auth-live-rebuild @ b2c4eb441280343c4b9c39d57851c6d3da33abaa`
- PR: `#93` OPEN/Ready; clean successor on live base; NO MERGE.
- cambios: reconstruction from live baseline with exactly three harness/evidence files: `.github/workflows/f4-25.1-windows-auth.yml`, `scripts/run-auth-e2e.mjs`, `tests/e2e/auth-flow.e2e.mjs`. Minimum proven correction: auth fetch stub delegates `/plugin%3Awdio%7C...` IPC and all non-auth traffic to native fetch; `/auth/health` and `/auth/login` remain stubbed. Literal token persistence + AccountGate-exit assertions preserved. No product files changed.
- tests: fresh packaged Windows Auth requested by PR #93; immediate exact-head query returned no workflow runs yet.
- CI: `WAITING_CI`; exact head `b2c4eb441280343c4b9c39d57851c6d3da33abaa`; no PASS claimed.
- evidencia: #84 source `f53d46f...` was stale on base `816f946c...`; live integration verified `134a293...`; prior HARNESS_ONLY_PROVEN boundary reused; successor #93 is based directly on live head and contains only the bounded harness/evidence reconstruction.
- UNVERIFIED: literal packaged Windows Auth result/job; returned token persistence on Windows; AccountGate exit on Windows; applicable exact-head CI green status; `F4/25.1 WINDOWS_AUTH_CANDIDATE_EXACT_GREEN` NOT claimed.
- blockers: external GitHub Actions scheduling/execution only at close of turn.

CI-FALLBACK:
- STATUS: `NONE / NOT_EXECUTED`
- branch/head si aplica: n/a
- PR si aplica: n/a
- cambios: none
- tests: none
- evidencia: JOBS explicitly wrote `CI-FALLBACK: NONE` for NIGHT-BBB-107.
- UNVERIFIED: n/a
- blockers: fallback not authorized.
- STOP alcanzado: yes; PRIMARY entered genuine `WAITING_CI`, fallback is NONE, one final immediate CI recheck still showed no runs.

RECOMENDACIÓN PARA JOBS: recheck PR #93 exact head. Promote only if the literal packaged Windows Auth job proves both unchanged assertions and all applicable exact-head CI is SUCCESS; otherwise assign attribution/corrective on the same bounded successor. Do not merge from BBB107.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-107`: `WAITING_CI` / PR #93 @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`.
- `NIGHT-BBB-106`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 112.
- `NIGHT-BBB-105`: `BLOCKED_STOP / HARNESS_ONLY_PROVEN_REFRESH_UNSAFE`; reusable causal evidence preserved.
