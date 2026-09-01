# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-102`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 Windows auth harness/service causal correction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`
- `EVIDENCE_CANDIDATE: PR #84 OPEN/Ready @ f53d46f39ece94f6de74f2f21a508ce01497ac41; base_sha 816f946c...; stale against live integration.`
- `PREDECESSOR: NIGHT-BBB-101 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff al preflight JOBS CYCLE 107; SUPERSEDED / NOT_PASS. Último resultado factual procesado: NIGHT-BBB-099 = BLOCKED_STOP / AMBIGUOUS; Issue #41 5486566941.`
- `AUTHORITATIVE_FAILURE: Windows Auth Journey 33449587244 / job 99676242317 @ f53d46f... = FAILURE.`
- `KNOWN_CAUSAL_TUPLE: POST /plugin%3Awdio%7Cget_window_states, requestClass=cross-origin; followed by WDIO plugin traffic and /get_settings; Tauri service also logged Failed to get window states.`
- `SERIALIZATION: BBB102 owns #84 evidence/harness only. AAA103 owns F2/12.1. WOZ106 owns #89. Do not touch #74 product logic, Review, Trash, #88/#89/#90/#83/#76/#85/provider/deploy/integration.`

### PRIMARY

**F4 / 25.1 — prove attribution and correct only harness/service interception if demonstrated.**

1. Fresh preflight integration/#74/#84/Issue #41; account for #84 stale base after #86/#87 merges.
2. Consume the exact sanitized tuple `POST /plugin%3Awdio%7Cget_window_states` / `cross-origin`; no sensitive material may be logged.
3. Map it to the WDIO/Tauri test service and prove whether the test's broad `window.fetch` interception is swallowing service/mock traffic required by the real packaged journey.
4. Classify exactly `HARNESS_ONLY_PROVEN`, `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN`, or `AMBIGUOUS`.
5. Only if failure is proven harness/service-interception-side and product assertions remain literal, apply the minimum allowlist/mock-boundary correction on #84. **NO PRODUCT MUTATION.**
6. Before fresh evidence, refresh/rebase #84 history-preserving onto live `38517c...` if safe; otherwise STOP on conflict/race.
7. Run fresh packaged Windows Auth + all applicable exact-head CI. Required PASS remains returned session token persisted and AccountGate exited, assertions unchanged.
8. Product-side/ambiguous attribution => STOP; no new auth PR, no broad harness rewrite, **NO MERGE**.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** live/base/#74/#84 heads; exact tuple mapping; causal classification; changed files; unchanged literal assertions; refreshed exact base/head; packaged run/job + applicable CI; UNVERIFIED explícito.  
**STOP:** product mutation, sensitive leakage, ambiguous attribution after bounded analysis, unsafe rebase/conflict, unrelated files, integration mutation or auth redesign.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-101`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 107; no final result/handoff observado.
- `NIGHT-BBB-099`: `BLOCKED_STOP / AMBIGUOUS`; Issue #41 `5486566941`.
- Exact tuple ya recuperado por JOBS desde el failed job log; ahora el trabajo permitido sigue siendo atribución causal bounded + harness-only correction si se demuestra.
