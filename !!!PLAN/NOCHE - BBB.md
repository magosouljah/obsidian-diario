# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área inicial:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE BBB ESTA NOCHE

Cerrar la mayor cantidad posible de F4 sin invadir otras áreas, empezando por el camino combinado 21.1+21.2 y devolviendo el control a JOBS al finalizar cada turno.

BBB **no se autoasigna** la siguiente tarea. Un turno = una asignación JOBS.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-001`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 21.1 + 21.2`
- `TARGET_ARTIFACT: PR #51`
- `KNOWN_HEAD_AT_ASSIGNMENT: 362d69811da112c3b73f68c2e736455b05ed5dc4`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 6c4499d124a64d138e791ea4abf0091766dde7e9`

### Orden JOBS

1. Haz preflight factual completo. Revalida PR #51, integration, Issue #41 y CI exact-head.
2. Reutiliza exclusivamente PR #51; no abras PR alterno para evitar el Draft.
3. Si #51 ya está **Ready** y head/base siguen correspondiendo a la combinación exact-head probada, no repitas CI innecesariamente: haz race-check, integra por el flujo autorizado y verifica el merge SHA.
4. Después de integración verificable, procesa #48 únicamente como superseded-for-integration conforme al plan y publica handoff final de 21.1/21.2.
5. Si #51 sigue **Draft**, no rerunees CI verde solo para ocupar tiempo. Registra `BLOCKED_HUMAN_ACTION`, confirma exactamente la acción mínima requerida y STOP.
6. Si head/base cambiaron, aplica la regla exact-head: refresh/union + evidencia aplicable antes de integración.
7. Actualiza **solo este markdown nocturno** con el resultado.
8. No empieces Día 22/23/24/25 dentro de este Assignment ID. JOBS decidirá el siguiente slice en el próximo ciclo.

### Evidencia conocida a revalidar

Handoff BBB Issue #41 `5460933229`:
- PR #51 OPEN / DRAFT / mergeable / not merged;
- exact head `362d69811da112c3b73f68c2e736455b05ed5dc4`;
- base/integration `6c4499d124a64d138e791ea4abf0091766dde7e9`;
- Required CI #458 / `33236730894` SUCCESS;
- Upgrade 21.2 Staging #9 / `33236730864` SUCCESS;
- D6 #93 / `33236730854` SUCCESS;
- D7 #68 / `33236730901` SUCCESS;
- Windows/macOS staging artifacts ligados al exact head.

Este snapshot no sustituye el preflight.

### Fuera de scope

- signing Windows en este assignment;
- notarización macOS;
- certificados/credenciales;
- D24/D25 en este assignment;
- release/beta pública;
- F1/F2/F3;
- cualquier archivo de `!!!PLAN` salvo este markdown nocturno para reportar.

## REGLAS DEL TURNO

- Leer Plan Maestro + F4 + Registro + Equipo multi-IA + protocolo nocturno + este archivo + Issue #41 reciente.
- Duplicate-check obligatorio.
- REUSE-FIRST.
- Evidence-before-claim.
- No bypass de Draft mediante ref update directo/PR duplicado.
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
RECOMMENDATION_TO_JOBS:
TURN_FINISHED_AT:
```

## HISTORIAL

- Bootstrap: #51 tiene evidencia técnica exact-head verde pero el último estado factual conocido sigue Draft. Si el RO lo cambia a Ready antes del turno, BBB debe detectarlo factual y continuar sin esperar una nueva orden.
