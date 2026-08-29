# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** F2 — Web / UX / frontend de producto.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE AAA ESTA NOCHE

Cerrar la mayor cantidad posible de F2 sin invadir otras áreas. Un turno = una asignación JOBS. AAA no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-005`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 12.1 — Bootstrap y load / corrective slice A`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`
- `REUSE_BRANCH: aaa/night-12.1-bootstrap-load`
- `CONTEXT: NIGHT-AAA-003=PENDING y NIGHT-AAA-004=STALLED sin product commit. Corrective assignment obligatorio: reducir alcance ejecutable sin abandonar ownership 12.1.`

### Orden JOBS

1. Preflight factual: Plan Maestro + F2 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. Reutiliza exclusivamente `aaa/night-12.1-bootstrap-load`; no abras otra rama/PR 12.1.
3. Este turno NO intenta cerrar todo 12.1. Produce un candidate mínimo y coherente para **slice A**:
   - retirar la hidratación eager de artwork del camino de carga inicial y dejar artwork lazy/on-demand o thumbnail-safe;
   - introducir taxonomía observable mínima que distinga `empty`, `no-results`, `offline`, `auth-failure` y `cloud-failure` donde el flujo actual los colapsa;
   - instrumentar fases de startup suficientes para medir cold/warm sin inventar números.
4. Añade/ajusta tests afectados. No reclames mejora de performance sin medición reproducible.
5. No tocar atomic empty-index bootstrap salvo que sea estrictamente necesario para compilar este slice; queda como requisito 12.1 posterior.
6. Preserva D8/11.2/12.2; Web pura sin Tauri/helper; no reabras auth/session fuera del mapping de estados.
7. Candidate head + tests + CI exact-head. Si el artifact queda listo, abre/reutiliza un solo PR y reporta; no auto-integres otra tarea.
8. Actualiza solo este markdown con DONE/BLOCKED/PENDING/STALLED y STOP.

### Fuera de scope

F1/F3/F4; pagos; signing/release; YouTube 15.3; 13.x/14.x/15.x; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-AAA-004`  
`TURN_STATUS: STALLED`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`HEAD_AFTER: aaa/night-12.1-bootstrap-load @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858 — branch created; no product commit`  
`PR: none`  
`EVIDENCE: eager artwork hydration y failure genérico reconfirmados; atomic empty-index/bootstrap taxonomy/startup measurements siguen UNVERIFIED.`

## HISTORIAL

- `NIGHT-AAA-005`: ASSIGNED — corrective narrow slice A sobre rama existente; candidate+tests/CI exigidos.
- `NIGHT-AAA-004`: STALLED — rama creada, sin product commit/PR/CI.
- `NIGHT-AAA-003`: PENDING — no reusable artifact; gaps 12.1 confirmados.
- `NIGHT-AAA-002`: DONE — PR #54 exact head `e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; Required CI #459 SUCCESS; merge `3560dc844fbe6a56b5c2a29008a629f05a9125ce`; Issue #41 `5461257322`.
- `NIGHT-AAA-001`: superseded before execution.
