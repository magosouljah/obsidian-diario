# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-012`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.2 — integrate SAME PR #61; then READ-ONLY 17.1 readiness if merge succeeds`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 58a6bf61441f08bf68aa63673c0d5f2994b220d9`
- `REUSE_PR: #61 / woz/night-16.2-promotion-contract`
- `KNOWN_CANDIDATE_HEAD: aef1cd0b1a26be327e561f344d63dae5d8def7ef`
- `JOBS_PRECHECK: exact-head D6 33266547956 SUCCESS; temp-auth 33266548019 SUCCESS; D7 33266548050 SUCCESS; Test - Desktop Portability 33266547963 SUCCESS; Upgrade 21.2 Staging skipped/no aplicable.`

### Orden JOBS

1. Preflight factual + race-check GitHub vivo; REUSE-FIRST exclusivamente SAME #61 para 16.2.
2. BBB corre antes en cadencia. Si integration sigue `58a6bf614...` y head `aef1cd0...`, usa CI exact-head verde y merge protegido expected-head.
3. Si integration cambió por #60 u otro owner, refresca la MISMA #61 sobre baseline vivo, preservando exclusivamente los 3 archivos F3, y exige CI aplicable nuevo.
4. Tras merge verificable, declarar solo `16.2 SOFTWARE DONE / EXTERNAL TAIL`; no fingir staging/prod físicos, provider resources, DNS/TLS o deploy/rollback real.
5. Solo si #61 queda integrado con evidencia y queda tiempo: READ-ONLY REUSE-FIRST audit de 17.1 (qué existe vs gaps de Stripe products/prices/Checkout/idempotency). No crear Stripe resources, costo ni implementación 17.1 en 012.
6. No tocar F2/F4 ni infraestructura real. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-011`  
`TURN_STATUS: PENDING`  
`RESULT: SAME #61 fue refrescada sobre baseline 58a6bf614... a head aef1cd0b1a26be327e561f344d63dae5d8def7ef preservando 3-file delta F3. El turno terminó con CI pendiente; GitHub posterior confirma todos los gates aplicables SUCCESS.`  
`EVIDENCE_NEW_BY_JOBS: runs 33266547956/48019/48050/47963 SUCCESS; #61 OPEN/Ready/mergeable; no merge todavía.`

## HISTORIAL

- `NIGHT-WOZ-012`: ASSIGNED — integrar SAME #61; luego solo audit read-only 17.1 si mergea.
- `NIGHT-WOZ-011`: PENDING — #61 refreshed a `aef1cd0...`; CI luego verde.
- `NIGHT-WOZ-010`: PENDING — #61 candidate software 16.2.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation external.
- `NIGHT-WOZ-008`: PENDING_CI.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
