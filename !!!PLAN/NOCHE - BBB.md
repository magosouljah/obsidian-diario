# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-099`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — exact #84 Windows auth causal trace`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`
- `PRODUCT_LINEAGE: PR #74 remains the only product-corrective lineage; do not mutate it in this assignment.`
- `EVIDENCE_CANDIDATE: PR #84 OPEN/Ready/mergeable @ f53d46f39ece94f6de74f2f21a508ce01497ac41, exact live base.`
- `PREDECESSOR: NIGHT-BBB-098 no dejó RESULTADO DEL TURNO ni matching Issue #41 handoff al preflight JOBS CYCLE 104; SUPERSEDED / NOT_PASS.`
- `AUTHORITATIVE_FAILURE: Windows Auth Journey 33449587244 / job 99676242317 @ f53d46f... = FAILURE at isolated auth assertions.`
- `SERIALIZATION: BBB099 owns #84 evidence/harness only. AAA100 owns public Web startup. WOZ103 owns #86. Do not touch #74 product logic, Review, Trash, #83/#76/#85/#86/#87/provider/deploy/integration.`

### PRIMARY

**F4 / 25.1 — obtener la primera request inesperada sanitizada y resolver causalidad sin especular.**

1. Fresh preflight integration/#74/#84/Issue #41 y exact failure; STOP en base/head race o duplicate owner.
2. Intentar recuperar del run/job exacto solo el primer tuple `{method, pathname/requestClass}`; nunca query/body/headers/token/password/secrets.
3. Si el tuple no fue emitido/recuperable, se autoriza **una** modificación diagnostic-only mínima sobre #84 que registre únicamente ese primer tuple y una fresh packaged Windows Auth run; assertions literales permanecen intactas.
4. Clasificar exactamente: `HARNESS_ONLY_PROVEN`, `PRODUCT_SIDE_PROVEN`, `SERVICE_BOUNDARY_PROVEN` o `AMBIGUOUS`.
5. Solo si `HARNESS_ONLY_PROVEN`, aplicar el mínimo allowlist/mock correction sobre #84 y ejecutar fresh packaged auth + applicable exact-head CI. Token-persistence y AccountGate-exit assertions no se debilitan.
6. Product/service/ambiguous => STOP sin product mutation. No tercer auth PR, no broad harness rewrite, **NO PRODUCT MUTATION / NO MERGE**.
7. PASS solo si las assertions literales unchanged pasan realmente en exact new head.
8. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** exact base/#74/#84 heads; run/job; sanitized tuple; causal classification; changed files; unchanged assertions; fresh run/CI si aplica; UNVERIFIED explícito.  
**STOP:** product/service mutation, sensitive leakage required, ambiguous attribution after bounded trace, unrelated files, integration mutation o auth redesign.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-098`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 104; #84 sigue exact `f53d46f...` y el literal Windows Auth sigue rojo.
- `NIGHT-BBB-097`: diagnostic-only handoff `WAITING_CI`; post-turn run `33449587244` / job `99676242317` = FAILURE.
