# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 009 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`.
- Cambio factual principal: WOZ integró PR #59 / F3 16.1 runtime software contract. Merge exacto `be9e58c9...`, parents `f73c9ee...` + `0e0bf188...`.
- Release público: 🔴 `NO-GO`.
- F0: técnico habilitado; 1.2 y 2.2 tails externos.
- F1: D6/D7/D8/D9 PASS. D10.1 external-only por off-provider/off-account copy proof real + read/checksum. D10.2 = decisión RO.
- F2: PR #58 sigue OPEN con head `d7cc93f...`; no hay resultado verificable de AAA-009 y su combinación quedó stale frente a `be9e58c...`.
- F3: 16.1 runtime/software slice de #59 DONE/INTEGRATED; physical staging/prod separation sigue PENDING_EXTERNAL. 16.2 software-only queda ahora dependency-ready.
- F4: PR #60 OPEN/Ready, head `28d9e381...`; F4 matrix `33260592877`, D6 `33260592860` y D7 `33260592764` SUCCESS, pero Desktop Portability `33260592774` = FAILURE. Además su base `f73c9ee...` quedó stale tras #59. No integración.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Asignación nueva | Objetivo |
|---|---|---|---|
| AAA | 009 sin resultado verificable; #58 no refrescada y baseline avanzó | `NIGHT-AAA-010` | SAME #58 refresh a be9e58c, CI aplicable, merge; luego atomic empty-index únicamente |
| BBB | 009 PENDING — #60 creado; matrix/D6/D7 verdes, Desktop Portability rojo | `NIGHT-BBB-010` | SAME #60 diagnosticar failure, refresh/fix mínimo, CI completo; merge solo si todo aplicable queda verde |
| WOZ | 009 PENDING_EXTERNAL — #59 merged be9e58c; runtime 16.1 integrado | `NIGHT-WOZ-010` | F3/16.2 software-only REUSE-FIRST; physical separation permanece external |

No existe ownership simultáneo: AAA=F2/12.1; BBB=F4/25.1; WOZ=F3/16.2.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-010`
- REUSE SAME PR #58 / `aaa/night-12.1-bootstrap-load`.
- Refresh contra baseline vivo `be9e58c...` preservando toda integración previa.
- CI aplicable exact-head/merge-candidate; no reutilizar verde viejo para combinación nueva.
- Race-check + merge protegido solo con evidencia verde.
- Después: atomic empty-index como único sub-slice nuevo.
- No pagination/window/memory ni cold/warm residual en 010.

### `NIGHT-BBB-010`
- REUSE SAME PR #60 / `bbb/task-25.1-functional-matrix`.
- Inspeccionar failure exacto `Test - Desktop Portability 33260592774`.
- Refresh sobre `be9e58c...`; corregir únicamente delta F4 mínimo si corresponde.
- Si el failure pertenece a F2/F3, registrar `PRODUCT_FINDING`; no robar ownership.
- Exigir nuevo Desktop Portability/Required CI + F4 matrix + D6/D7 aplicables sobre exact head.
- No merge mientras quede gate rojo. No 25.2/signing/notarization/release.

### `NIGHT-WOZ-010`
- #59 ya integrado: no reabrir 16.1 runtime ni repetir CI/drills.
- F3/16.2 software-only/dependency-safe, REUSE-FIRST.
- Auditar assets existentes antes de candidate.
- Contrato PR→preview, candidate tag→staging, approval→production; mismo source SHA.
- Origins/TLS/headers inyectables y fail-closed; smoke/rollback fixtures.
- Sin provider resources/costo/deploy real. Physical staging/prod sigue PENDING_EXTERNAL.

## BLOCKERS

1. F0/2.2: GitHub Support server-side cleanup + fresh final verification.
2. F0/1.2: governance/domain/support/status/signing/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real fuera del primary provider/account failure domain + read/checksum.
4. F1/D10.2: decisión RO sobre alpha final.
5. F2/12.1: #58 requiere refresh + CI aplicable + merge; después atomic empty-index, pagination/window/memory y cold/warm residual.
6. F3/16.1: runtime software integrado; physical staging/prod resources/credentials/ownership externos.
7. F3: 16.2–20.x es el mayor volumen restante; Stripe/DNS/legal/provider incluyen inputs externos.
8. F4/25.1: #60 tiene failure real en Desktop Portability y stale base; matrix verde no compensa el gate rojo.
9. F4: D22/D23 signing/notarization externos; iPhone/YouTube/billing/cross-platform functional gaps siguen honestamente sin PASS.

## PROGRESO HACIA F0–F4

- **F0:** solo tails externos/administrativos; no consumir worker técnico en duplicados.
- **F1:** core técnico cerrado; D10.1 external-only + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 sigue crítico, ahora con orden correctiva 010 sobre la misma PR.
- **F3:** avance material: 16.1 runtime software integrado. Physical separation permanece externo; 16.2 software-only ahora tiene owner activo.
- **F4:** 24.2 cerrado. 25.1 ya tiene matrix candidate, pero no puede integrarse hasta corregir/explicar el portability failure y revalidar contra baseline vivo.

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

Leídos completos también: F0, F1, protocolo y Registro. F0/F1 no reciben mutación porque ningún requisito de esas fases cambió factual en este ciclo. GitHub real e Issue #41 prevalecieron sobre los snapshots nocturnos stale.

## SIGUIENTE CICLO

1. Releer integration HEAD y #58/#60 antes de cualquier claim.
2. Procesar output de AAA-010, BBB-010 y WOZ-010; no conservar assignment por inercia.
3. Si #58 se integra, avanzar atomic empty-index; si no, corregir misma lineage.
4. Si #60 queda verde tras refresh/fix, permitir owner race-check/merge; si failure es product finding, replanificar sin ownership overlap.
5. Procesar 16.2 y después recalcular el siguiente slice F3 de mayor retorno.
6. Mantener D10.1 off-provider, physical staging/prod y signing/notarization como externos hasta evidencia real.
7. No abrir Fase 5 mientras los gates reales necesarios sigan abiertos.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-009
INTEGRATION_HEAD: be9e58c9edc0bb40742e0b91e3f2ebe771ace502
AAA: NIGHT-AAA-009 no verified result; stale -> NIGHT-AAA-010 SAME #58 refresh + CI + merge, then atomic empty-index
BBB: NIGHT-BBB-009 PENDING; #60 matrix/D6/D7 green, portability 33260592774 FAILURE -> NIGHT-BBB-010 SAME #60 diagnose/refresh/fix/CI
WOZ: NIGHT-WOZ-009 PENDING_EXTERNAL; #59 merged be9e58c, runtime 16.1 software integrated -> NIGHT-WOZ-010 F3/16.2 software-only
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 009 terminado. La siguiente ejecución debe iniciar desde GitHub vivo, no desde este snapshot si cambió.
