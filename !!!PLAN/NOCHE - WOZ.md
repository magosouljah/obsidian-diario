# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 factual y REUSE-FIRST, sin repetir drills aceptados. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-003`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1 / D10.1 — cerrar gaps literales de backup readiness`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3560dc844fbe6a56b5c2a29008a629f05a9125ce`
- `CONTEXT: D9 PASS; D10.1 handoff 5461379758 = PENDING`

### Orden JOBS

1. Haz preflight factual completo: Plan Maestro + F1 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub/runtime real. Confirma que D9 y la evidencia Task 5.2 siguen válidos.
2. Trabaja únicamente los gaps literales restantes de D10.1 identificados en `5461379758`: (a) evidencia/estrategia completa para backup de config + índice/media; (b) evidencia de copia off-provider; (c) backup-failure alert específica o demostración literal de que el mecanismo existente satisface ese requisito.
3. REUSE-FIRST estricto: reutiliza PITR/RPO/RTO, restore aislado, keyring multiversión, alarmas/on-call/rotation/rollback authority, cifrado/retention/least-privilege ya aceptados. NO repitas restore, cutover, restart ni rotación para fabricar evidencia.
4. Antes de implementar, duplicate-check. Si el gap es únicamente documental/operativo y puede cerrarse con evidencia ya existente, documenta y cierra sin PR ceremonial.
5. Si existe un gap técnico real de software, implementa el mínimo por artifact propio con tests/CI. Si la única forma de satisfacerlo requiere credencial, proveedor, costo nuevo o decisión RO, NO aprovisiones ni amplíes costo: registra la acción externa mínima exacta y deja PENDING/BLOCKED.
6. Decide D10.1 `PASS | FAIL | PENDING` mediante requirement matrix literal y publica handoff Issue #41.
7. Actualiza solo este markdown nocturno y STOP. No inicies D10.2 ni F3 en este Assignment ID.

### Fuera de scope

D10.2 alpha; F2/F3/F4; release público; repetir drills 5.2; nueva infraestructura de costo; cualquier `!!!PLAN` salvo este markdown nocturno.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-002`

Pendiente de ejecución de `NIGHT-WOZ-003`.

## HISTORIAL

- `NIGHT-WOZ-002`: PENDING — D10.1 auditado REUSE-FIRST; restore/RPO/RTO/core flows = PASS; gaps literales en config/index/media strategy, off-provider copy y backup-failure alert; Issue #41 `5461379758`; sin PR ni drill repetido.
- `NIGHT-WOZ-001`: superseded before worker execution; scope D10.1 conservado bajo 002.
- D9: DONE/PASS por Issue #41 `5460959369`, sin PR ceremonial.
