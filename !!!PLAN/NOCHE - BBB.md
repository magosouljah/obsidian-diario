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

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-106`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 112.
- `NIGHT-BBB-105`: `BLOCKED_STOP / HARNESS_ONLY_PROVEN_REFRESH_UNSAFE`; reusable causal evidence preserved.
