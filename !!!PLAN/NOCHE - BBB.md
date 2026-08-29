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

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-005`  
`TURN_STATUS: DONE`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`BRANCH_HEAD: bbb/task-24.1-release-controls @ ba83c87dab8a56163601e913f7764c7f8682b7a6`  
`PR: #55 CLOSED/MERGED; merge SHA 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`CHANGES: 24.1 release controls integrado; rings/minimum versions, fail-closed publication, kill switch, SPDX SBOM y SHA/provenance/checksum binding.`  
`TESTS: F4 Release Controls 33248059891 SUCCESS; D6 33248059823 SUCCESS; D7 33248059990 SUCCESS.`  
`CI: Required CI 33248059804 SUCCESS on exact head ba83c87...`  
`BLOCKERS: none para 24.1; signing/notarization siguen externos.`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-BBB-006`: ASSIGNED — F4/24.2 updater recovery/rollback, REUSE-FIRST.
- `NIGHT-BBB-005`: DONE — PR #55 head `ba83c87...` merged as `672e133...`; exact-head checks green.
- `NIGHT-BBB-004`: PENDING — PR #55 ready; CI luego verde.
- `NIGHT-BBB-003`: DONE — #51 merged `5b05ca845...`.
- `NIGHT-BBB-002`: PENDING — #51 refreshed.
- `NIGHT-BBB-001`: superseded.
