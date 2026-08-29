# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-014`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F4 / 25.1 — SAME PR #63 Windows import functional journey corrective transaction`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import`
- `KNOWN_HEAD: 9208ead249345d29458a5ae939923dd5c2f47dfb`

### Orden JOBS

1. Preflight factual + duplicate-check contra GitHub vivo, Plan Maestro, F4, Registro, roles, protocolo, este ledger e Issue #41. GitHub manda.
2. REUSE-FIRST exclusivamente SAME #63. PR #62 permanece CLOSED/NOT MERGED y no se reabre.
3. Procesa el gate funcional exact-head `F4 - 25.1 Windows Import Journey` run `33271091186`: terminó `FAILURE`; el step que falló fue `Run existing Windows import E2E harness`. Required CI amplio `33271091123` sí fue SUCCESS, pero NO sustituye este gate específico.
4. Determina la causa mínima verificable del failure. Corrige únicamente workflow/glue/test-harness F4 si el problema pertenece a este slice. Si descubre bug de producto F2/F3, registra `PRODUCT_FINDING` con repro/owner y no robes la implementación.
5. La matriz no puede marcar `windows/import = AUTOMATED_PASS` hasta que el journey exact-head pase realmente. Mantén el estado honesto si el test sigue fallando.
6. Si integration cambia por AAA/WOZ, refresh SAME lineage preservando solo el delta #63 y exige CI funcional + CI aplicable exact-head nuevos.
7. Integra #63 solo con Windows import functional journey PASS + applicable CI green + race-check limpio. Incluso entonces 25.1 completo sigue abierto por los demás gaps.
8. OUT OF SCOPE: segundo slice, segunda matriz, 25.2, iPhone hardware, signing/notarization, Stripe/YouTube productivo, fixes de producto F2/F3.
9. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-014`  
`TURN_STATUS: PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`  
`BRANCH/HEAD: bbb/task-25.1-windows-import @ 9208ead249345d29458a5ae939923dd5c2f47dfb`  
`PR: #63 OPEN / Ready / mergeable; NOT MERGED; SAME lineage.`  
`CAMBIOS: causa mínima del failure 33271091186 aislada a glue/driver F4: build + import harness llegaron al arranque de WDIO pero el proveedor externo tauri-driver/Edge falló antes de ejecutar specs con DevToolsActivePort; además el workflow antiguo hacía checkout del merge-ref de PR pese a llamarse exact source. Se añadió solo scripts/prepare-f4-25.1-embedded-driver.mjs, el workflow ahora hace checkout explícito de github.event.pull_request.head.sha + assert git rev-parse HEAD y prepara driver embebido Tauri para el harness aislado. La matriz volvió honestamente windows/import a NOT_COVERED hasta PASS real. Sin cambios de producto F2/F3.`  
`TESTS: se reutiliza npm run test:e2e:import; no se creó segundo harness productivo. Nuevo gate funcional exact-head: F4 - 25.1 Windows Import Journey run 33272794199 IN_PROGRESS.`  
`CI: exact head 9208ead249345d29458a5ae939923dd5c2f47dfb: F4 Matrix 33272794263 SUCCESS; Windows Import 33272794199 IN_PROGRESS; D6 33272794193 IN_PROGRESS; D7 33272794195 IN_PROGRESS; Desktop Portability 33272794215 PENDING; Upgrade 21.2 Staging 33272794243 SKIPPED/no aplicable.`  
`EVIDENCIA: PR #63 reread OPEN/Ready/mergeable sobre base 7de7b57a... y head 9208ead...; PR #51 revalidada GitHub vivo CLOSED/MERGED, no Ready; integration permanecía 7de7b57a... durante preflight. Matrix exact-head confirma windows/import NOT_COVERED hasta PASS.`  
`UNVERIFIED: windows/import sigue NOT_COVERED; el nuevo driver embebido aún no tiene PASS exact-head; 25.1 completo sigue abierto con todos los demás NOT_COVERED/PENDING_EXTERNAL/PRODUCT_FINDING honestos.`  
`BLOCKERS: gate funcional 33272794199 y CI aplicable exact-head aún no terminaron; merge prohibido.`  
`RECOMMENDATION_TO_JOBS: mantener NIGHT-BBB-014 sobre SAME PR #63/lineage en próximo ciclo; si 33272794199 pasa y gates aplicables quedan verdes con baseline sin mover, promover windows/import a AUTOMATED_PASS en la misma lineage y exigir evidencia exact-head nueva antes de merge. Si integration se mueve, refresh SAME lineage. No asignar segundo slice antes de cerrar/descartar #63.`

## HISTORIAL

- `NIGHT-BBB-014`: PENDING — SAME #63 corregida a head `9208ead249...`; driver/bootstrap F4 corregido, exact-head checkout enforced, matrix vuelve NOT_COVERED; CI nuevo en curso, no merge.
- `NIGHT-BBB-013`: PENDING — PR #63 @ `65a7bf070...`; exact functional run luego FAILURE; PR #62 duplicate CLOSED.
- `NIGHT-BBB-012`: DONE — #60 merged `7de7b57a...`.
- `NIGHT-BBB-011`: PENDING — #60 refreshed.
- `NIGHT-BBB-010`: PENDING — #60 repaired/refreshed.
- `NIGHT-BBB-009`: PENDING — candidate stale/failure.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
