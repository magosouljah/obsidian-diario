# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-104`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — #84 Windows auth harness/service causal correction`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`
- `EVIDENCE_CANDIDATE: PR #84 OPEN/Ready @ f53d46f39ece94f6de74f2f21a508ce01497ac41; base_sha 816f946c...; stale against live integration.`
- `PREDECESSOR: NIGHT-BBB-103 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff verificable al preflight JOBS CYCLE 109; SUPERSEDED / NOT_PASS. Último resultado factual de la línea: NIGHT-BBB-099 = BLOCKED_STOP / AMBIGUOUS; Issue #41 5486566941.`
- `AUTHORITATIVE_FAILURE: Windows Auth Journey 33449587244 @ f53d46f... = FAILURE; generic exact-head CI on that old head is green but does not replace the literal journey.`
- `KNOWN_CAUSAL_TUPLE: POST /plugin%3Awdio%7Cget_window_states, requestClass=cross-origin; followed by WDIO plugin traffic and /get_settings; Tauri service logged Failed to get window states.`
- `SERIALIZATION: BBB104 owns #84 evidence/harness only. AAA105 owns F2/12.1. WOZ108 owns #89. No tocar #74 product logic, Review, Trash, #88/#89/#90/#83/#76/#85/provider/deploy/integration.`

### PRIMARY

**F4 / 25.1 — prove attribution and correct only harness/service interception if demonstrated.**

1. Fresh preflight integration/#74/#84/Issue #41; account for live baseline `1dbf60e...` after #88.
2. Consume exact sanitized tuple `POST /plugin%3Awdio%7Cget_window_states` / `cross-origin`; no sensitive material in logs.
3. Map it to WDIO/Tauri service and prove whether broad `window.fetch` interception swallows service/mock traffic needed by packaged journey.
4. Classify exactly `HARNESS_ONLY_PROVEN`, `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN`, or `AMBIGUOUS`.
5. Only `HARNESS_ONLY_PROVEN` permits the minimum allowlist/mock-boundary correction on #84 with literal product assertions unchanged. **NO PRODUCT MUTATION.**
6. Before fresh evidence, history-preserving refresh #84 onto live `1dbf60e...` only if clean/safe; conflict or scope drift => STOP.
7. Run fresh packaged Windows Auth + applicable exact-head CI. Required PASS: returned session token persisted and AccountGate exited, assertions unchanged.
8. Product-side/ambiguous attribution => STOP; no new auth PR, no broad harness rewrite, **NO MERGE**.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** live/base/#74/#84 heads; tuple mapping; causal classification; changed files; unchanged literal assertions; refreshed exact base/head; packaged run/job + applicable CI; UNVERIFIED explícito.  
**STOP:** product mutation, sensitive leakage, ambiguous attribution after bounded analysis, unsafe rebase/conflict, unrelated files, integration mutation or auth redesign.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-103`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 109; no final result/handoff verificable observado al preflight.
- `NIGHT-BBB-099`: `BLOCKED_STOP / AMBIGUOUS`; Issue #41 `5486566941`.
- #84 live head sigue `f53d46f...`; Windows Auth literal sigue FAILURE y candidate está stale contra `1dbf60e...`.
