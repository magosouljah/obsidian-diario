# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE BBB ESTA NOCHE

Cerrar F4 sin invadir otras áreas. Un turno = una asignación JOBS. BBB no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-004`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 24.1 — provenance, channels y release controls`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`
- `CONTEXT: 21.1+21.2 cerrados e integrados por PR #51; #48 quedó superseded/merged. D22/D23 dependen de signing/notarization externos; 24.1 tiene trabajo técnico dependency-safe reutilizable desde 4.2.`

### Orden JOBS

1. Haz preflight factual completo: Plan Maestro + F4 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. Duplicate-check + REUSE-FIRST antes de crear artifact. Audita primero lo ya existente de F0/4.2, workflows de release, SBOM/checksums/provenance, tags/channels/updater y kill-switches.
3. Ejecuta únicamente F4/24.1: cerrar lo que pueda demostrarse/implementarse sin certificado ni notarización: tag protegido = SHA consumido; checksums/SBOM/provenance; channels/rings/minimum version/kill switch. No fabriques un release público ni muevas stable/latest.
4. Si un requisito depende literalmente de certificado/credencial/decisión externa, déjalo PENDING y reduce el blocker; no inventes secretos ni bypass.
5. Si existe gap técnico real, usa un solo artifact mínimo, tests propios y exact-head CI. Preserva manifest/upgrade ya integrados.
6. No iniciar 22.x, 23.x, 24.2 ni 25.x en este Assignment ID.
7. Publica handoff Issue #41 y actualiza solo este markdown; STOP.

### Fuera de scope

Signing Windows, notarización macOS, compra/manejo de certificados, release público, F1/F2/F3, 24.2/25.x y cualquier `!!!PLAN` salvo este markdown nocturno.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-004`  
`TURN_STATUS: PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`HEAD_AFTER: candidate bbb/task-24.1-release-controls @ ba83c87dab8a56163601e913f7764c7f8682b7a6; integration sigue @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`PR: #55 OPEN / Ready / mergeable=true; base_sha 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858; head_sha ba83c87dab8a56163601e913f7764c7f8682b7a6; NO MERGED por Required CI aún in_progress.`  
`CHANGES: REUSE-FIRST conservó binding de release/tag al RELEASE_SOURCE_SHA consumido, provenance runtime y SHA256 existentes. Gap técnico 24.1 cerrado en un solo candidate: release/release-controls.json define alpha/beta/stable, rings únicos, minimum versions, publicationEnabled=false y kill switch global engaged; scripts/release-controls.mjs valida y aplica fail-closed; F4 - Release Controls prueba el bloqueo exact-head; release-desktop-updater consume release_channel/policy antes de publicación y genera/adjunta SBOM SPDX dentro de SHA256SUMS. No release público, no stable/latest, no signing/notarization.`  
`TESTS: F4 - Release Controls run 33248059891 SUCCESS sobre exact head ba83c87...; prueba explícita confirma que la policy comprometida bloquea publicación. D6 run 33248059823 SUCCESS; D7 run 33248059990 SUCCESS. Upgrade 21.2 Staging run 33248059805 SKIPPED por paths/no necesidad de rerun productivo.`  
`CI: exact head ba83c87dab8a56163601e913f7764c7f8682b7a6 — F4 Release Controls SUCCESS; D6 SUCCESS; D7 SUCCESS; Test - Desktop Portability / Required CI run 33248059804 IN_PROGRESS al cierre. No se rebajó ningún gate y no se hizo merge con CI incompleto.`  
`EVIDENCE: PR #51 fue revalidada en GitHub real como CLOSED/MERGED, no asumida Ready; integración race-check sigue exactamente en 5b05ca8...; #55 base/head exactos y mergeable=true; duplicate-check no encontró PR 24.1 paralelo; workflow release existente ya probaba Windows/macOS desde el mismo source SHA, checkout exacto, provenance gitSha y checksums, reutilizados sin repetir drills costosos; Issue #41 reciente no contiene handoff BBB posterior a NIGHT-BBB-003.`  
`UNVERIFIED: resultado final de Required CI 33248059804; ejecución real del workflow de release con publicación (deliberadamente bloqueada por kill switch); certificados Windows, notarización macOS, credenciales y release público — fuera de scope. SBOM se añadió al pipeline y su generación queda sujeta al gate CI/release correspondiente; no se afirma publicación.`  
`BLOCKERS: Required CI 33248059804 aún in_progress. No blocker técnico adicional detectado dentro de 24.1. Signing/notarization/publicación siguen externos y fuera de este assignment.`  
`RECOMMENDATION_TO_JOBS: cuando Required CI 33248059804 cierre SUCCESS, emitir Assignment ID explícito para revalidar exact-head/base y mergear #55 sin rerun ceremonial; si falla, asignar corrección del mismo PR/head family. No iniciar 24.2/25.x automáticamente.`  
`TURN_FINISHED_AT: 2026-08-29T04:34-06:00`

## HISTORIAL

- `NIGHT-BBB-004`: PENDING — PR #55 Ready/mergeable @ `ba83c87...`; F4/D6/D7 verdes, Required CI `33248059804` aún en progreso; no merge; release controls fail-closed + SBOM/provenance candidate listo.
- `NIGHT-BBB-003`: DONE — #51 integrado como `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`; exact-head CI verde; #48 superseded/merged; Issue #41 `5461557463`.
- `NIGHT-BBB-002`: PENDING — baseline cambió por #54; #51 refrescada a `0fd9bee...` y nueva tanda exact-head lanzada.
- `NIGHT-BBB-001`: superseded before worker execution.
