# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 factual y REUSE-FIRST, sin repetir drills aceptados. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-005`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1 / D10.1 — backup readiness / minimal verifiable artifact`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`
- `CONTEXT: NIGHT-WOZ-004 confirmó que PITR/RPO/RTO/core flows/cifrado/retention/least-privilege siguen PASS y que solo faltan tres gaps literales: cobertura config+índice/media, copia off-provider y backup-failure alert específica.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F1 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub/runtime actual.
2. REUSE-FIRST estricto. No repetir restore, cutover, restart, migrations ni rotation ya aceptados.
3. Construye/reutiliza **un solo artifact mínimo** que convierta los tres gaps restantes en evidencia verificable sin aprovisionar costo/credenciales por inferencia:
   - matriz/contrato ejecutable de cobertura de backup para config + índice/media como conjunto;
   - mecanismo/contrato de copia off-provider con dry-run o verificación local segura si puede demostrarse sin proveedor nuevo; si el requisito literal exige un destino externo real, deja exactamente ese punto como EXTERNAL_BLOCKER;
   - backup-failure alert específica: config/test/validator que pruebe la condición y el routing esperado sin inventar delivery productivo si no existe.
4. Duplicate-check antes de crear rama/PR. Si ya existe artifact que satisface literalmente, úsalo y no dupliques.
5. Si hay cambio técnico/documental versionado necesario, artifact mínimo + tests/CI aplicables. Si requiere credencial, proveedor o costo real, no lo ejecutes por inferencia: reduce a una sola acción externa concreta.
6. Emite matriz D10.1 `PASS | PENDING | FAIL` requirement por requirement y handoff Issue #41.
7. No iniciar D10.2 ni F3 bajo este Assignment ID.
8. Actualiza solo este markdown y STOP.

### Fuera de scope

D10.2 alpha; F2/F3/F4; release público; nueva infraestructura de costo; repetir drills 5.2; cualquier `!!!PLAN` salvo este markdown nocturno.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-004`  
`TURN_STATUS: PENDING`  
`GATE: D10.1 / PENDING`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`  
`PR: none`  
`EVIDENCE_NEW: Issue #41 5461893650; no artifact nuevo`  
`PASS_REUSED: isolated PITR restore; RPO ~7 min; RTO 3643 s; core flows; encryption; retention; least privilege`  
`PENDING: config+index/media strategy; off-provider copy; backup-failure alert específica/equivalencia literal`.

## HISTORIAL

- `NIGHT-WOZ-005`: ASSIGNED — un solo artifact mínimo/verificable para los tres gaps; external blocker reducido si aplica.
- `NIGHT-WOZ-004`: PENDING — tres gaps literales siguen abiertos; Issue #41 `5461893650`.
- `NIGHT-WOZ-003`: SUPERSEDED_UNPROCESSED.
- `NIGHT-WOZ-002`: PENDING — D10.1 audit REUSE-FIRST; Issue #41 `5461379758`.
- `NIGHT-WOZ-001`: superseded before execution.
- D9: DONE/PASS — Issue #41 `5460959369`.
