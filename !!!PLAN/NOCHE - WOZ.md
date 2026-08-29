# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área inicial:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 de forma factual y reusable, sin repetir drills ya aceptados. Si F1 queda reducido a una decisión RO/externa, devolver control a JOBS para que decida si WOZ cambia de área en el siguiente ciclo.

WOZ **no se autoasigna** la siguiente tarea. Un turno = una asignación JOBS.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-001`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1 / D10.1 — Restore y backup readiness`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 6c4499d124a64d138e791ea4abf0091766dde7e9`
- `CONTEXT: D9 PASS por handoff Issue #41 5460959369`

### Orden JOBS

1. Haz preflight factual completo y verifica que D9 sigue válido/no invalidado por cambios posteriores.
2. Evalúa **solo D10.1** con enfoque REUSE-FIRST.
3. Construye una matriz literal de requisitos:
   - backup cifrado/config/media strategy;
   - restore aislado + RPO/RTO + core flows;
   - access/retention/off-provider copy/backup alert.
4. Reutiliza PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority y demás evidencia aceptada cuando satisfaga literalmente el requisito.
5. No repitas restore/cutover/rotación/productive drill solo para crear evidencia nueva.
6. Si existe un gap material de software dentro de D10.1, implementa el cambio mínimo por rama/PR propia, tests y CI aplicable.
7. Si existe un gap externo/operativo no resoluble sin credencial/decisión RO, registra exactamente cuál y qué acción mínima falta.
8. Decide D10.1 `PASS | FAIL | PENDING` solo con requirement matrix y evidencia.
9. Publica handoff Issue #41.
10. Actualiza **solo este markdown nocturno** con el resultado y STOP.
11. **No iniciar D10.2 alpha** en este Assignment ID. Alpha final conserva decisión RO; JOBS decidirá el siguiente ciclo.

### Evidencia reusable conocida

D9 handoff `5460959369` confirmó, entre otras cosas:
- PostgreSQL autoridad productiva;
- migrations/checksums/transacciones/importer/rollback fail-closed;
- dump/backup cifrado + restore aislado en CI;
- PITR/RPO representativo ~7 min;
- segundo restore con RTO `3643 s <= 7200 s`;
- keyring multiversión y rotación productiva;
- observabilidad, on-call y autoridad de rollback ya aceptados en Task 5.2.

Esto es input reusable; WOZ debe verificar que satisface literalmente D10.1 y no asumir PASS por nombre.

### Fuera de scope

- D10.2 alpha en este assignment;
- F2/F4;
- F3 salvo futura reasignación explícita JOBS;
- release público;
- reabrir D6/D7/D8/D9 sin nueva evidencia material;
- cualquier archivo de `!!!PLAN` salvo este markdown nocturno para reportar.

## REGLAS DEL TURNO

- Leer Plan Maestro + F1 + Registro + Equipo multi-IA + protocolo nocturno + este archivo + Issue #41 reciente.
- Duplicate-check obligatorio.
- REUSE-FIRST estricto.
- Evidence-before-claim.
- Si no hay gap, no crear código ceremonial.
- No editar la asignación ni tomar otra.
- Al finalizar: reportar y STOP.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: none`

```text
TURN_STATUS: NOT_STARTED
BASE_BEFORE:
HEAD_AFTER:
PR:
CHANGES:
TESTS:
CI:
EVIDENCE:
UNVERIFIED:
BLOCKERS:
GATE_OR_REQUIREMENT_DECISION:
RECOMMENDATION_TO_JOBS:
TURN_FINISHED_AT:
```

## HISTORIAL

- Bootstrap: D9 fue cerrado por WOZ como `DONE / PASS` en Issue #41 `5460959369` mediante REUSE-FIRST, sin rama/PR D9 nueva.
