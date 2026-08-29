# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área inicial:** F2 — Web / UX / frontend de producto.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE AAA ESTA NOCHE

Cerrar la mayor cantidad posible de F2 sin invadir otras áreas, comenzando por la asignación vigente y devolviendo el control a JOBS al terminar cada turno.

AAA **no se autoasigna** la siguiente tarea. Un turno = una asignación JOBS.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-001`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 11.2 Auth UI completa`
- `TARGET_ARTIFACT: PR #54`
- `KNOWN_HEAD_AT_ASSIGNMENT: e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 6c4499d124a64d138e791ea4abf0091766dde7e9`

### Orden JOBS

1. Haz preflight factual completo. No asumas que head/base/CI siguen iguales.
2. Reutiliza exclusivamente PR #54 para 11.2; no abras otro artifact.
3. Verifica el estado exact-head de Required CI #459 y checks aplicables.
4. Si CI sigue corriendo o falla por causa externa/no atribuible, registra PENDING/BLOCKED con evidencia y STOP.
5. Si CI pasa y baseline/head siguen compatibles, haz race-check final e integra #54 por el flujo autorizado del owner.
6. Verifica el merge SHA y que integración contiene 11.2.
7. Publica handoff Issue #41 con evidence-before-claim.
8. Actualiza **solo este markdown nocturno** con el resultado del turno.
9. No empieces 12.1, 13.x, 14.x ni 15.x en este turno aunque 11.2 termine. JOBS escogerá el siguiente slice al próximo ciclo.

### Scope 11.2

- login/register/MFA/verify/reset/recovery/error/offline;
- OAuth popup/redirect/blocked/cancel/retry;
- teclado/lector/zoom/móvil/error de red;
- responsive/a11y;
- preservar contratos D8 integrados;
- Web pura, sin introducir dependencia Tauri.

### Fuera de scope

- D9/D10/F1;
- F3;
- F4;
- 12.1/15.1 en este Assignment ID;
- rediseño backend security;
- cambios a decisiones RO de D8;
- cualquier archivo de `!!!PLAN` salvo este markdown nocturno para reportar.

## REGLAS DEL TURNO

- Leer Plan Maestro + F2 + Registro + Equipo multi-IA + protocolo nocturno + este archivo + Issue #41 reciente.
- Duplicate-check obligatorio.
- REUSE-FIRST.
- Evidence-before-claim.
- Si integration avanzó, no uses CI viejo para una combinación nueva sin revalidación aplicable.
- No editar la asignación ni inventar una nueva.
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
RECOMMENDATION_TO_JOBS:
TURN_FINISHED_AT:
```

## HISTORIAL

- Bootstrap: antes del sistema nocturno, handoff Issue #41 `5460950384` registró PR #54 @ `e5aefa9...` como PENDING por finalización de Required CI #459. Este dato debe revalidarse en el turno.
