# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 008 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`.
- Cambio factual del ciclo: BBB integró PR #57 / F4 24.2 con exact-head probado y merge verificable.
- Release público: 🔴 `NO-GO`.
- F0: técnico habilitado; 1.2 y 2.2 tails externos.
- F1: D6/D7/D8/D9 PASS. D10.1 external-only por off-provider/off-account copy proof real + read/checksum. D10.2 = decisión RO.
- F2: PR #58 sigue OPEN/Ready/mergeable con head `d7cc93f...`, pero su base observada quedó atrás en `f0d65aa...`; el merge anterior fue rechazado correctamente porque el merge-candidate no tenía Required CI. Debe refrescarse la MISMA PR sobre `f73c9ee...` y obtener CI aplicable antes de merge.
- F3: PR #59 OPEN/Ready/mergeable, exact head `0e0bf188ceb298c5c6846e56576665b50a69e922`, exact base `f73c9ee...`; Test - Desktop Portability `33258609802`, D6 `33258609811`, D7 `33258609799` y temp-auth compile `33258609793` SUCCESS. Listo para owner race-check/merge; physical staging/prod separation sigue externa.
- F4: 24.2 `[x] / DONE / INTEGRATED`; PR #57 exact head `4e251cae...`, CI `33255401498`, D6 `33255401544`, D7 `33255401512` SUCCESS; merge `f73c9ee...`. 25.1 audit REUSE-FIRST completado y ahora es el siguiente carril BBB.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado 008 procesado | Asignación nueva | Objetivo |
|---|---|---|---|
| AAA | STALLED — #58 no pudo mergear por Required CI ausente en merge-candidate; no bypass | `NIGHT-AAA-009` | refresh SAME #58 sobre f73c9ee, CI aplicable, merge; luego atomic empty-index únicamente |
| BBB | DONE — #57 merged f73c9ee; 24.2 cerrable; audit 25.1 completo | `NIGHT-BBB-009` | F4/25.1 matrix/runner dependency-safe sobre harnesses existentes |
| WOZ | PENDING_CI al cierre; JOBS recheck confirmó CI exact-head totalmente verde | `NIGHT-WOZ-009` | integrar #59 si race-check válido; después 16.2 software-only |

No existe ownership simultáneo: AAA=F2/12.1; BBB=F4/25.1; WOZ=F3/16.1→16.2.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-009`
- REUSE SAME PR #58 / `aaa/night-12.1-bootstrap-load`.
- Refrescar contra baseline vivo `f73c9ee...`, preservando #57.
- Obtener Required CI aplicable a la nueva combinación/merge-candidate.
- Race-check + merge protegido solo con evidencia verde.
- Después: atomic empty-index como único sub-slice nuevo.
- No pagination/window/memory ni cold/warm residual en 009.

### `NIGHT-BBB-009`
- 24.2 ya cerrado: no reabrir ni repetir CI.
- F4/25.1 REUSE-FIRST: construir un único matrix/runner dependency-safe sobre harnesses existentes.
- Estados explícitos por requisito: `AUTOMATED_PASS`, `PENDING_EXTERNAL`, `PRODUCT_FINDING`, `NOT_COVERED`.
- No fixes F2/F3, no signing/notarization, no release, no 25.2.

### `NIGHT-WOZ-009`
- REUSE PR #59 / `woz/night-16.1-runtime-operability`.
- Exact-head CI ya verde; revalidar race y merge protegido si base/head siguen vigentes.
- Aun con merge, 16.1 completo sigue PENDING_EXTERNAL por separación física staging/prod.
- Después: 16.2 software-only/dependency-safe; promotion contract, origins/TLS/headers fail-closed, smoke/rollback fixtures; sin provider resources/costo ni deploy real.

## BLOCKERS

1. F0/2.2: GitHub Support server-side cleanup + fresh final verification.
2. F0/1.2: governance/domain/support/status/signing/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real fuera del primary provider/account failure domain + read/checksum.
4. F1/D10.2: decisión RO sobre alpha final.
5. F2/12.1: #58 requiere refresh + CI aplicable + merge; después atomic empty-index, pagination/window/memory y cold/warm residual.
6. F3/16.1: #59 merge pendiente internamente; physical staging/prod resources/credentials/ownership externos.
7. F3: 16.2–20.x es el mayor volumen restante; Stripe/DNS/legal/provider incluyen inputs externos.
8. F4: 24.2 cerrado. D22/D23 signing/notarization externos. 25.1 tiene gaps reales cross-browser/cross-OS/iPhone/YouTube/billing.

## PROGRESO HACIA F0–F4

- **F0:** solo tails externos/administrativos; no consumir worker técnico en duplicados.
- **F1:** core técnico cerrado; D10.1 external-only + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 bloqueado únicamente por refresh/integración del slice A antes del siguiente sub-slice.
- **F3:** 16.1 software candidate #59 tiene exact-head CI verde; external physical separation conserva el gate. 16.2 sigue después.
- **F4:** 24.2 cerrado/integrado; 25.1 audit ya redujo el problema y BBB pasa a matrix/runner dependency-safe.

## PLAN SYNC DEL CICLO

Actualizados:
- `!!!PLAN/Plan Maestro.md`
- `!!!PLAN/Fase 2 - Web y UX.md`
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`
- `!!!PLAN/Fase 4 - Desktop y release chain.md`
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`
- `!!!PLAN/NOCHE - AAA.md`
- `!!!PLAN/NOCHE - BBB.md`
- `!!!PLAN/NOCHE - WOZ.md`
- `!!!PLAN/NOCHE - JOBS.md`

Leídos completos para preflight: F0, F1, protocolo y Registro. F0/F1 no reciben cambio textual porque ningún requisito de esas fases cambió. `Registro de avances.md` no se reescribe en este ciclo: la nueva evidencia factual queda canónicamente sincronizada en Plan Maestro/F4 y en Issue #41, evitando una sustitución parcial del ledger histórico.

## SIGUIENTE CICLO

1. Releer integration HEAD y #58/#59 antes de cualquier claim.
2. Procesar merge verificable de #59 y refresh/CI/merge de #58 si ocurren.
3. Procesar output de 25.1 matrix/runner, atomic empty-index y 16.2 software-only.
4. Mantener D10.1 off-provider, physical staging/prod y signing/notarization como externos hasta evidencia real.
5. Recalcular F0–F4 desde cero; no conservar asignación por inercia.
6. No abrir Fase 5 mientras gates reales necesarios sigan abiertos.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-008
INTEGRATION_HEAD: f73c9ee8d058df3c780170c8c2a3fabef975c54d
AAA: NIGHT-AAA-008 STALLED; #58 stale -> NIGHT-AAA-009 SAME PR refresh + CI + merge, then atomic empty-index
BBB: NIGHT-BBB-008 DONE; #57 merged f73c9ee; 24.2 CLOSED -> NIGHT-BBB-009 F4/25.1 matrix/runner
WOZ: NIGHT-WOZ-008 PENDING_CI; post-turn CI all SUCCESS on 0e0bf188 -> NIGHT-WOZ-009 race-check/merge + 16.2 software-only
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 008 terminado. La siguiente ejecución debe iniciar desde GitHub vivo, no desde este snapshot si cambió.
