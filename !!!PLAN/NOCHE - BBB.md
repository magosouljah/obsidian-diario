# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-013`
- `ASSIGNMENT_STATUS: PENDING`
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

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-013`  
`TURN_STATUS: PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`  
`BRANCH/HEAD: bbb/task-25.1-windows-import @ 65a7bf07029babfb500d3913226ec8a5ca6e0deb`  
`PR: #63 OPEN/Ready; base exacta 7de7b57a508b3cf05cbded81501fbd3da63922a3; candidate exacto 65a7bf07029babfb500d3913226ec8a5ca6e0deb; 2 archivos cambiados.`  
`CAMBIOS: REUSE-FIRST del harness existente test:e2e:import; añadido solo .github/workflows/f4-25.1-windows-import.yml para ejecutar ese journey en windows-2025 y actualizado release/f4-25.1-functional-matrix.json para que windows/import sea AUTOMATED_PASS únicamente condicionado a PASS exact-head del workflow. No product code F2/F3, no segunda matriz, no 25.2.`  
`TESTS: harness reutilizado npm run test:e2e:import -> scripts/run-import-e2e.mjs -> runner desktop aislado con BEATGALER_E2E_IMPORT=1; nueva ejecución funcional exact-head iniciada como F4 - 25.1 Windows Import Journey run 33271091186.`  
`CI: exact head 65a7bf07029babfb500d3913226ec8a5ca6e0deb: F4 Windows Import 33271091186 IN_PROGRESS; F4 Matrix 33271091128 IN_PROGRESS; D6 33271091122 IN_PROGRESS; D7 33271091147 IN_PROGRESS; Desktop Portability 33271091123 QUEUED; Upgrade 21.2 Staging 33271091125 SKIPPED/no aplicable.`  
`EVIDENCIA: integración seguía en 7de7b57a508b3cf05cbded81501fbd3da63922a3 al crear #63; PR #51 verificada contra GitHub vivo como CLOSED/MERGED, merge 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858; duplicate-check no encontró otra PR BBB abierta para este residual.`  
`UNVERIFIED: windows/import NO se considera cerrado todavía porque el workflow funcional exact-head no había terminado; 25.1 completo sigue abierto y todos los demás NOT_COVERED/PENDING_EXTERNAL/PRODUCT_FINDING permanecen honestamente abiertos.`  
`BLOCKERS: evidencia exact-head aún en ejecución/cola; merge prohibido hasta PASS funcional + CI aplicable + race-check limpio.`  
`RECOMMENDATION_TO_JOBS: mantener NIGHT-BBB-013 sobre la MISMA PR #63/lineage hasta que 33271091186 y gates aplicables terminen; si integration se mueve, refrescar la misma lineage y exigir CI nuevo. No asignar otro slice a BBB antes de cerrar/descartar #63.`

## HISTORIAL

- `NIGHT-BBB-013`: PENDING — PR #63 `bbb/task-25.1-windows-import @ 65a7bf07029babfb500d3913226ec8a5ca6e0deb`; Windows/import residual aislado con harness existente; exact-head CI en curso, no merge.
- `NIGHT-BBB-012`: DONE — SAME #60 exact-head green merged as `7de7b57a508b3cf05cbded81501fbd3da63922a3`.
- `NIGHT-BBB-011`: PENDING — #60 refreshed to `945638c8...`; CI later green.
- `NIGHT-BBB-010`: PENDING — #60 repaired/refreshed.
- `NIGHT-BBB-009`: PENDING — candidate stale/failure.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`; 24.2 closed.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — PR #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
