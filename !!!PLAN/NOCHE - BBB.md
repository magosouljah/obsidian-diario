# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-100`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 Windows auth harness/service causal correction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ b85723e1b3016d24bdb943393e796ccdb744247d`
- `EVIDENCE_CANDIDATE: PR #84 OPEN/Ready but non-mergeable/stale-base @ f53d46f39ece94f6de74f2f21a508ce01497ac41; base_sha 816f946c...`
- `PREDECESSOR: NIGHT-BBB-099 = BLOCKED_STOP / AMBIGUOUS; Issue #41 5486566941.`
- `AUTHORITATIVE_FAILURE: Windows Auth Journey 33449587244 / job 99676242317 @ f53d46f... = FAILURE.`
- `NEW_CAUSAL_EVIDENCE: exact job log exposes first unexpected tuple POST /plugin%3Awdio%7Cget_window_states, requestClass=cross-origin, followed by repeated WDIO plugin traffic and /get_settings; Tauri service also logs Failed to get window states.`
- `SERIALIZATION: BBB100 owns #84 evidence/harness only. AAA101 owns F2/12.1. WOZ104 owns #87. Do not touch #74 product logic, Review, Trash, #83/#76/#85/#87/provider/deploy/integration.`

### PRIMARY

**F4 / 25.1 — consume the exact tuple, prove attribution, and correct only harness/service interception if demonstrated.**

1. Fresh preflight integration/#74/#84/Issue #41; account for #84 stale base after #86 merge.
2. Treat the exact first tuple as factual: `POST /plugin%3Awdio%7Cget_window_states` / `cross-origin`; no sensitive material may be logged.
3. Map that request to the WDIO/Tauri test service and prove whether the test's broad `window.fetch` interception is swallowing service/mock traffic required by the real packaged journey.
4. Classify exactly `HARNESS_ONLY_PROVEN`, `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN`, or `AMBIGUOUS`.
5. Only if the failure is proven harness/service-interception-side and product assertions stay literal, apply the minimum allowlist/mock-boundary correction on #84. **NO PRODUCT MUTATION.**
6. Before fresh evidence, refresh/rebase #84 history-preserving onto live `b85723e...` if safe; otherwise STOP on conflict/race.
7. Run fresh packaged Windows Auth + all applicable exact-head CI. Required PASS remains returned session token persisted and AccountGate exited, assertions unchanged.
8. Product-side/ambiguous attribution => STOP; no new auth PR, no broad harness rewrite, **NO MERGE**.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** live/base/#74/#84 heads; exact tuple mapping; causal classification; changed files; unchanged literal assertions; refreshed exact base/head; packaged run/job + applicable CI; UNVERIFIED explícito.  
**STOP:** product mutation, sensitive leakage, ambiguous attribution after bounded analysis, unsafe rebase/conflict, unrelated files, integration mutation or auth redesign.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-099`: `BLOCKED_STOP / AMBIGUOUS`; Issue #41 `5486566941`.
- JOBS CYCLE 105 recovered the exact failed job log: first unexpected request is WDIO service traffic (`POST /plugin%3Awdio%7Cget_window_states`, cross-origin); this narrows attribution but does not itself constitute a Windows Auth PASS.
