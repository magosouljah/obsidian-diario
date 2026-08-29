# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 factual y REUSE-FIRST, sin repetir drills aceptados. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-002`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1 / D10.1 — Restore y backup readiness`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 6c4499d124a64d138e791ea4abf0091766dde7e9`
- `CONTEXT: D9 PASS por Issue #41 5460959369`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F1 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real. Confirma que D9 no fue invalidado.
2. Evalúa solo D10.1 con REUSE-FIRST estricto.
3. Matriz literal: (a) backup cifrado/config/media strategy; (b) restore aislado + RPO/RTO + core flows; (c) access/retention/off-provider copy/backup alert.
4. Reutiliza PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority, dump/backup cifrado y evidencia aceptada cuando satisfaga literalmente el requisito.
5. No repitas restore/cutover/rotación/drill productivo solo para recrear evidencia.
6. Si hay gap material de software D10.1, implementa el mínimo por rama/PR propia con tests/CI. Si es externo/operativo, registra exactamente la acción mínima faltante.
7. Decide D10.1 `PASS | FAIL | PENDING` solo con requirement matrix + evidencia y publica handoff Issue #41.
8. Actualiza solo este markdown nocturno y STOP. No iniciar D10.2 alpha en este Assignment ID.

### Fuera de scope

D10.2 alpha; F2/F4; F3 salvo reasignación futura; release público; reabrir D6–D9 sin evidencia material; cualquier `!!!PLAN` salvo este markdown nocturno.

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

- `NIGHT-WOZ-001`: superseded before worker execution by JOBS cycle 001; scope D10.1 retained under new monotonic Assignment ID as required by the hourly orchestration contract.
- D9 closed `DONE / PASS` in Issue #41 `5460959369` via REUSE-FIRST, no new D9 PR.