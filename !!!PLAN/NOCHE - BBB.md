# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-030`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: matrix-contract corrective after successful Windows Import promotion head`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ 1b957eff98271f78809c6eeb5fd79fed311b3286`
- `PREDECESSOR: NIGHT-BBB-029 had no RESULTADO DEL TURNO observable at JOBS CYCLE 031; superseded monotonically with SAME scope.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reutiliza SAME #63; no replacement branch/PR.
2. Estado aceptado del promotion head `1b957eff...`: Windows Import `33305947664` SUCCESS; Required CI `33305947677` SUCCESS; F4 Functional Matrix `33305947676` FAILURE en `Validate dependency-safe matrix contract`.
3. No vuelvas a tocar Windows import harness salvo evidencia nueva que lo invalide. El blocker activo es únicamente el contrato de matriz.
4. Atribuye el `matrix-contract` rojo. Si es causado por la promoción `windows/import -> AUTOMATED_PASS` o su `evidenceCatalog`, corrige solo el mínimo en `release/f4-25.1-functional-matrix.json` y/o validator F4 estrictamente necesario dentro del SAME #63. Si es externo/no atribuible, no cambies producto/config para apaciguarlo: documenta y STOP/PENDING.
5. Tras cualquier head nuevo, exige F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head.
6. Si todo aplicable queda verde e integration sigue compatible, race-check + merge SAME #63; verifica merge SHA e integration HEAD.
7. Cierra solo el slice `windows/import`; 25.1 completo, 25.2 y D22/D23 permanecen abiertos salvo evidencia separada.
8. Reporta RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** error/atribución exacta del matrix-contract, delta correctivo mínimo si aplica, fresh gates tras cambio, race-check, merge SHA/integration HEAD si integra.  
**STOP:** producto fuera de F4, reabrir harness sin evidencia, otros matrix gaps, D22/D23/25.2, baseline race, fallo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: otros gaps F4 dependen de signing/hardware o amplían scope; no hay carril independiente seguro mientras #63 espera CI.

## RESULTADO PROCESADO — NIGHT-BBB-028

- `STATUS: PENDING / WAITING_CI`.
- Promotion commit `1b957eff98271f78809c6eeb5fd79fed311b3286`.
- Windows Import `33305947664` SUCCESS; Required CI `33305947677` SUCCESS; F4 Functional Matrix `33305947676` FAILURE en `matrix-contract`.
- PR #63 OPEN/Ready/mergeable; no merge.

## HISTORIAL COMPACTO

- `NIGHT-BBB-030`: ASSIGNED — SAME #63 matrix-contract attribution/corrective + fresh gates + merge if green; fallback NONE.
- `NIGHT-BBB-029`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-BBB-028`: PENDING — promotion head created; Windows Import + Required CI green, matrix-contract red.
- `NIGHT-BBB-026`: exact-head Windows Import + applicable gates SUCCESS before promotion.
- `NIGHT-BBB-024`: prior Windows Import FAILURE before assertions.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
