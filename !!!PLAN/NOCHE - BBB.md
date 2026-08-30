# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-029`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #63: matrix-contract corrective after successful Windows Import promotion head`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `REUSE_PR: #63 / bbb/task-25.1-windows-import @ 1b957eff98271f78809c6eeb5fd79fed311b3286`
- `PREDECESSOR: NIGHT-BBB-028 PENDING / WAITING_CI — processed by JOBS CYCLE 030.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. Reutiliza SAME #63; no replacement branch/PR.
2. Procesa el promotion head `1b957eff...`: Windows Import functional journey `33305947664` terminó SUCCESS y Required CI `33305947677` terminó SUCCESS; el check específico F4 Functional Matrix run `33305947676`, job `matrix-contract`, terminó FAILURE en `Validate dependency-safe matrix contract`.
3. No vuelvas a tocar el Windows import harness salvo evidencia nueva que lo invalide. El blocker activo es únicamente el contrato de matriz del promotion head.
4. Atribuye el `matrix-contract` rojo. Si es causado por el delta de promoción `windows/import -> AUTOMATED_PASS` o su evidenceCatalog, corrige solo el mínimo en `release/f4-25.1-functional-matrix.json` y/o validator F4 estrictamente necesario dentro del SAME #63. Si el rojo es externo/no atribuible, no cambies producto/config para apaciguarlo: documenta y STOP/PENDING.
5. Tras cualquier head nuevo, exige F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head. No uses el SUCCESS anterior como autorización para el nuevo head.
6. Si todo aplicable queda verde e integration sigue compatible, race-check + merge SAME #63; verifica merge SHA e integration HEAD.
7. Cierra solo el slice `windows/import`; 25.1 completo, 25.2 y D22/D23 permanecen abiertos salvo evidencia separada.
8. Reporta RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** error/atribución exacta del matrix-contract, delta correctivo mínimo si aplica, fresh promotion-head gates tras cambio, race-check, merge SHA/integration HEAD si integra.  
**STOP:** producto fuera de F4, reabrir harness sin evidencia, otros matrix gaps, D22/D23/25.2, baseline race, fallo no atribuible o evidencia insuficiente.

### CI-FALLBACK

`NONE`

Reason: otros gaps F4 dependen de signing/hardware o amplían scope; no hay carril independiente seguro mientras #63 espera CI.

## RESULTADO PROCESADO — NIGHT-BBB-028

- `STATUS: PENDING / WAITING_CI`.
- Promotion commit: `1b957eff98271f78809c6eeb5fd79fed311b3286`; solo `windows/import` fue promovido a `AUTOMATED_PASS` con evidencia previa exact-head.
- GitHub recheck por JOBS: Windows Import functional journey run `33305947664` = SUCCESS; Required CI run `33305947677` = SUCCESS.
- F4 Functional Matrix run `33305947676` = FAILURE; job `matrix-contract` falla en `Validate dependency-safe matrix contract`.
- PR #63 sigue OPEN/Ready/mergeable, base `3ad8f55a...`, head `1b957eff...`; no merge.
- Issue #41 handoff `5468076864` registró el estado WAITING_CI antes del cierre de esos checks.

## HISTORIAL COMPACTO

- `NIGHT-BBB-029`: ASSIGNED — SAME #63 matrix-contract attribution/corrective + fresh gates + merge if green; fallback NONE.
- `NIGHT-BBB-028`: PENDING — promotion head created; later JOBS observed Windows Import + Required CI SUCCESS but matrix-contract FAILURE.
- `NIGHT-BBB-026`: exact-head Windows Import + applicable gates SUCCESS before promotion.
- `NIGHT-BBB-024`: prior Windows Import FAILURE before assertions.
- `NIGHT-BBB-012`: #60 matrix integrated `7de7b57a...`.
