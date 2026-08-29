# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-010`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F3 / 16.2 — software-only reproducible promotion/deploy contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-010`  
`TURN_STATUS: PENDING`  
`GATE: F3/16.2 software contract candidate; full 16.2 remains PENDING until exact-head CI/integration and real provider deployment evidence where required`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`  
`HEAD_AFTER: woz/night-16.2-promotion-contract @ d855b3d259626534650c1a78dae6df58f78cdcb9`  
`PR: #61 OPEN / Ready; base be9e58c9edc0bb40742e0b91e3f2ebe771ace502; exact head d855b3d259626534650c1a78dae6df58f78cdcb9`  
`CHANGES: delta real confirmado tras REUSE-FIRST: no existía deploy/promotion asset 16.2. Candidate mínimo añade cloud-server/deployment-promotion-contract.mjs, tests y post-deploy smoke. Contrato exige PR→preview, candidate_tag→staging, approval explícita→production, artifactSha===sourceSha, origin HTTPS público sin localhost/Tailscale fallback, headers inyectables, smoke /healthz + /readyz y rollback únicamente a artifact previo con DB compatible + smoke PASS.`  
`TESTS: test source añadido con 5 casos contractuales; ejecución local no disponible/verificada desde connector, por lo que no se reclama PASS local.`  
`CI: Test - Desktop Portability run 33263815780 sobre exact head d855b3d... estaba QUEUED al STOP; Required CI completo no verificado todavía.`  
`EVIDENCIA_REUTILIZADA: PR #59 / merge be9e58c... para /healthz, /readyz, deployment env fail-closed, graceful shutdown/timeouts/proxy trust; no se repitió su CI/drill.`  
`EVIDENCIA_NUEVA: PR #61; exact head d855b3d259626534650c1a78dae6df58f78cdcb9; CI run 33263815780 queued.`  
`UNVERIFIED: ejecución de los 5 tests; CI exact-head final; mergeability final; merge SHA; staging/production reales; provider resources; DNS/TLS real; rollback real.`  
`BLOCKERS: CI exact-head pendiente para candidate. Separación física staging/prod y deploy real siguen PENDING_EXTERNAL por provider/RO y no se falsean.`  
`RECOMMENDATION_TO_JOBS: mantener ownership WOZ 16.2 para el próximo ciclo solo para consumir CI/race-check de SAME PR #61 y merge protegido si la combinación vigente queda verde. No crear provider resources ni repetir #59. Tras integración, marcar únicamente SOFTWARE DONE; mantener tail externo de deploy/staging real.`  
`TURN_FINISHED_AT: 2026-08-29T10:47-06:00`

## RESULTADO DEL TURNO ANTERIOR

`LAST_PREVIOUS_ASSIGNMENT: NIGHT-WOZ-009`  
`TURN_STATUS: PENDING_EXTERNAL`  
`PR: #59 / head 0e0bf188ceb298c5c6846e56576665b50a69e922`  
`MERGE: be9e58c9edc0bb40742e0b91e3f2ebe771ace502`  
`RESULT: runtime software 16.1 DONE/INTEGRATED; physical staging/prod external.`

## HISTORIAL

- `NIGHT-WOZ-010`: PENDING — PR #61 candidate software 16.2; exact-head CI queued; external deploy tail preserved.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation remains external.
- `NIGHT-WOZ-008`: PENDING_CI — #59 refreshed; CI terminó verde después.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 + self-test 7/7; physical separation external.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
