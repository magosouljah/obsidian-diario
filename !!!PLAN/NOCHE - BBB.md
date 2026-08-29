# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-013`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — dependency-safe functional coverage residual`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`
- `PREDECESSOR: PR #60 CLOSED/MERGED as 7de7b57a508b3cf05cbded81501fbd3da63922a3`
- `SOURCE_OF_TRUTH: integrated F4 25.1 matrix artifact; NOT_COVERED/PENDING_EXTERNAL/PRODUCT_FINDING remain honest gaps.`

### Orden JOBS

1. Preflight factual + duplicate-check contra GitHub vivo, Plan Maestro, F4, Registro, roles, protocolo, este ledger e Issue #41. GitHub manda.
2. REUSE-FIRST: leer la matriz 25.1 ya integrada por #60 y los harnesses existentes. No crear una segunda matriz ni reabrir #60.
3. Elegir **un solo slice automatizable de mayor retorno** entre los journeys core actualmente `NOT_COVERED` que pueda ejecutarse con dependencias ya presentes en Web/Desktop. Prioridad: auth/session → library/import/review/edit/trash/offline/download/update recovery, usando harnesses existentes y evitando duplicar tests ya cubiertos.
4. Debe producir evidencia funcional, no solo otra lista/config. Si el harness existente ya cubre el journey con evidencia reusable, promuévelo con prueba verificable; si falta glue mínimo de test, añadir solo eso.
5. No absorber fixes de producto F2/F3. Si un journey descubre bug real, registrar `PRODUCT_FINDING` con repro/owner y continuar solo si el test slice puede quedar honestamente expresado.
6. No inventar iPhone runner/hardware, signing Windows, notarization macOS, Stripe/billing productivo, YouTube productivo ni provider resources. Esos estados conservan `PENDING_EXTERNAL`/`NOT_COVERED` según evidencia.
7. Tests + CI aplicable exact-head para cualquier candidate. Si baseline cambia por WOZ/AAA, refresh de la misma lineage + CI nuevo antes de merge claim.
8. Integrar solo si el slice queda verificable y race-check limpio. Incluso con merge, **25.1 completo sigue abierto** mientras queden gaps honestos.
9. OUT OF SCOPE: 25.2, signing/notarization/release público, F2/F3 implementation.
10. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-012`  
`TURN_STATUS: DONE`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 58a6bf61441f08bf68aa63673c0d5f2994b220d9`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`  
`PR: #60 CLOSED/MERGED; exact candidate 945638c8bb650b0ce0bbe569e48a791a93d80e39`  
`TESTS/CI: F4 matrix 33265800007 SUCCESS; D6 33265800004 SUCCESS; D7 33265800022 SUCCESS; Desktop Portability 33265800008 SUCCESS; Upgrade 33265800019 SKIPPED/no aplicable.`  
`EVIDENCE: protected expected-head merge returned 7de7b57a...; integration reread confirms parents 58a6bf614... + 945638c8.... Issue #41 comment 5464132337.`  
`UNVERIFIED: NOT_COVERED/PENDING_EXTERNAL/PRODUCT_FINDING remain gaps; iPhone, signing, notarization, dedicated YouTube/billing evidence and 25.2 remain open.`  
`BLOCKERS: none for the completed #60 transaction.`

## HISTORIAL

- `NIGHT-BBB-013`: ASSIGNED — dependency-safe functional coverage residual of 25.1; matrix #60 is source of truth.
- `NIGHT-BBB-012`: DONE — SAME #60 exact-head green merged as `7de7b57a508b3cf05cbded81501fbd3da63922a3`.
- `NIGHT-BBB-011`: PENDING — #60 refreshed to `945638c8...`; CI later green.
- `NIGHT-BBB-010`: PENDING — #60 repaired/refreshed.
- `NIGHT-BBB-009`: PENDING — candidate stale/failure.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`; 24.2 closed.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — PR #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
