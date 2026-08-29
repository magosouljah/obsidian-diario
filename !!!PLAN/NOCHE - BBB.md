# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE BBB ESTA NOCHE

Cerrar F4 sin invadir otras áreas. Un turno = una asignación JOBS. BBB no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-006`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 24.2 — updater recovery / rollback`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`
- `CONTEXT: NIGHT-BBB-005 cerró e integró 24.1 mediante PR #55. D22/D23 siguen externos; 24.2 es dependency-safe y distinto de AAA/WOZ.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F4 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST sobre updater, upgrade matrix, release-controls, tests/workflows existentes. Duplicate-check antes de nueva rama/PR.
3. Ejecuta 24.2 únicamente:
   - update N-1 y fallos de red/disco/firma/manifest con comportamiento seguro;
   - recovery/rollback verificable;
   - mecanismo/runbook para retirar artefacto malo y comunicar sin publicar release real.
4. No inventes signing/notarization/certificados. Los fallos de firma pueden probarse con fixtures/validación existente, no con credenciales falsas.
5. Preserva 24.1 integrado: channels/rings/minimum version/kill switch y provenance.
6. Candidate mínimo + tests aplicables + CI exact-head. No publicar stable/latest ni mutar releases públicos.
7. Si algún requisito literal depende de certificado/credencial externa, separa exactamente ese blocker y completa lo dependency-safe.
8. Actualiza solo este markdown con DONE/BLOCKED/PENDING/STALLED y STOP.

### Fuera de scope

D22/D23 signing/notarization reales; 25.x; F1/F2/F3; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-006`  
`TURN_STATUS: PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 permanece @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`BRANCH_HEAD: bbb/task-24.2-updater-recovery @ 5c74c0948c43d53b2f8d075cd66ba70c953da3c5`  
`PR: #57 OPEN/Ready; no merge mientras CI exact-head no cierre verde.`  
`CHANGES: REUSE-FIRST sobre updater/upgrade-matrix/release-controls existentes; policy fail-closed de recovery para red/disco/firma/manifest; fixtures N-1; planner no destructivo de retiro ligado a tag + source SHA + SHA-256; runbook de rollback/recuperación/comunicación; test conectado a packaging static. Una deriva accidental de @types/react-dom detectada por diff-check fue revertida antes del cierre.`  
`TESTS: test:updater-recovery queda integrado en test:packaging:static y test:mac-portability:static; ejecución independiente local UNVERIFIED porque el runtime no pudo clonar GitHub, por lo que evidence-before-claim depende de CI exact-head.`  
`CI: exact head 5c74c094... disparó Test - Desktop Portability run 33252718637 PENDING, D6 run 33252718614 QUEUED, D7 run 33252718625 PENDING; Upgrade 21.2 Staging run 33252718609 SKIPPED por scope. No reruns ceremoniales.`  
`EVIDENCIA: PR #57 base exacta 672e133...; release-desktop-updater existente ya demuestra build-runs→same source SHA→VERSION/tag→provenance/checksum→signed updater entry; candidate 24.2 añade recovery/withdrawal sin publicar ni mutar release.`  
`UNVERIFIED: conclusión final de Required CI/Test - Desktop Portability, D6 y D7; ejecución real de signing/notarization/publicación (fuera de scope); retiro real de artefacto público (intencionalmente no ejecutado).`  
`BLOCKERS: CI exact-head aún no concluido. No hay blocker técnico dependency-safe conocido; D22/D23 credenciales siguen externos y fuera de 24.2.`  
`RECOMMENDATION_TO_JOBS: si los checks del exact head 5c74c094... cierran SUCCESS, emitir nuevo Assignment ID para race-check base/head y merge de #57 sin rerun ceremonial; si falla un check, asignar corrección sobre la misma PR. No auto-iniciar 25.x.`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-BBB-006`: PENDING — PR #57 head `5c74c094...`; 24.2 candidate completo dependency-safe, CI exact-head en curso.
- `NIGHT-BBB-005`: DONE — PR #55 head `ba83c87...` merged as `672e133...`; exact-head checks green.
- `NIGHT-BBB-004`: PENDING — PR #55 ready; CI luego verde.
- `NIGHT-BBB-003`: DONE — #51 merged `5b05ca845...`.
- `NIGHT-BBB-002`: PENDING — #51 refreshed.
- `NIGHT-BBB-001`: superseded.
