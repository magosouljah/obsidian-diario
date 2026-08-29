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

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-003`  
`TURN_STATUS: DONE`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 3560dc844fbe6a56b5c2a29008a629f05a9125ce`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`PR: #51 CLOSED/MERGED; exact tested head 0fd9bee8117ca92fb9f713f0d55089f5707a2917; merge SHA 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858. #48 CLOSED/MERGED as superseded.`  
`CI: exact head 0fd9bee... — D7 33243436937 SUCCESS; D6 33243436890 SUCCESS; Required CI 33243436894 SUCCESS; Upgrade 21.2 Staging 33243436914 SUCCESS.`  
`EVIDENCE: race-check matched base 3560dc8... + head 0fd9bee...; merge tree equals tested head tree; integrated manifest/upgrade matrix verified; Issue #41 handoff 5461557463.`  
`BLOCKERS: none para NIGHT-BBB-003.`  
`RECOMMENDATION_TO_JOBS: synchronize 21.1+21.2 and assign next F4 slice.`  
`TURN_FINISHED_AT: 2026-08-29T03:30-06:00`

## HISTORIAL

- `NIGHT-BBB-004`: ASSIGNED — F4/24.1 REUSE-FIRST sobre `5b05ca8...`; provenance/channels/release controls sin signing externo.
- `NIGHT-BBB-003`: DONE — #51 integrado como `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`; exact-head CI verde; #48 superseded/merged; Issue #41 `5461557463`.
- `NIGHT-BBB-002`: PENDING — baseline cambió por #54; #51 refrescada a `0fd9bee...` y nueva tanda exact-head lanzada.
- `NIGHT-BBB-001`: superseded before worker execution.
