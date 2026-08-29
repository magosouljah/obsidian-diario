# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE BBB ESTA NOCHE

Cerrar F4 sin invadir otras áreas. Un turno = una asignación JOBS. BBB no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-005`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 24.1 — integrar candidate verificado`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`
- `CANDIDATE: PR #55 / bbb/task-24.1-release-controls @ ba83c87dab8a56163601e913f7764c7f8682b7a6`
- `CONTEXT: NIGHT-BBB-004 dejó #55 Ready/mergeable y Required CI estaba in_progress; JOBS verificó después que Required CI run 33248059804 terminó SUCCESS sobre exact head ba83c87...`.

### Orden JOBS

1. Haz preflight factual completo: Plan Maestro + F4 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. Revalida inmediatamente: integration HEAD, PR #55 OPEN/Ready, base/head exactos, mergeability y todos los checks aplicables del head `ba83c87...`.
3. No rerun ceremonial: Required CI `33248059804` ya fue observado SUCCESS por JOBS, junto con F4 Release Controls `33248059891` SUCCESS, D6 `33248059823` SUCCESS y D7 `33248059990` SUCCESS. Si GitHub actual contradice esto, manda GitHub actual.
4. Si integration sigue exactamente `5b05ca845...`, #55 sigue head `ba83c87...` y la evidencia exact-head continúa válida, integra #55 por el flujo autorizado del owner usando expected/exact head cuando aplique.
5. Después verifica merge SHA, integration HEAD resultante y contenido/provenance mínimo. Publica handoff Issue #41.
6. Si baseline/head cambió materialmente, NO uses CI viejo como prueba de la nueva combinación: refresh/revalida dentro de la misma PR family y deja PENDING si no cabe completar.
7. No iniciar 24.2/25.x ni signing/notarization bajo este Assignment ID.
8. Actualiza solo este markdown y STOP.

### Fuera de scope

Signing Windows, notarización macOS, certificados, release público, F1/F2/F3, 24.2/25.x y cualquier `!!!PLAN` salvo este markdown nocturno.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-004`  
`TURN_STATUS: PENDING`  
`CANDIDATE: PR #55 @ ba83c87dab8a56163601e913f7764c7f8682b7a6`  
`TESTS: F4 Release Controls 33248059891 SUCCESS; D6 33248059823 SUCCESS; D7 33248059990 SUCCESS`  
`CI_AT_FINISH: Required CI 33248059804 IN_PROGRESS`  
`JOBS_POSTCHECK: Required CI 33248059804 COMPLETED / SUCCESS on exact head ba83c87...`

## HISTORIAL

- `NIGHT-BBB-005`: ASSIGNED — exact-head/base race-check + merge #55 if unchanged and still authorized.
- `NIGHT-BBB-004`: PENDING — PR #55 Ready/mergeable; F4/D6/D7 green; Required CI later verified SUCCESS by JOBS.
- `NIGHT-BBB-003`: DONE — #51 merged `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`; Issue #41 `5461557463`.
- `NIGHT-BBB-002`: PENDING — #51 refreshed after baseline move.
- `NIGHT-BBB-001`: superseded before execution.
