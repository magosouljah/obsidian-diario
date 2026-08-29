# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 007 FINAL

- BeatGaler integración permaneció en `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9` durante este ciclo; JOBS no hizo merges de código.
- Release público: 🔴 `NO-GO`.
- F0: técnico habilitado; 1.2 y 2.2 tails externos.
- F1: D6/D7/D8/D9 PASS. D10.1 artifact integrado; queda solo off-provider/off-account copy proof real + read/checksum. D10.2 = decisión RO.
- F2: PR #58 OPEN/Ready/mergeable=true, exact head `d7cc93f9c4318be7f993bd033483c4e7f1834a55`, base `f0d65aa...`; Required CI `33254699647` SUCCESS. Slice A aún no integrado y 12.1 sigue abierto.
- F3: PR #59 OPEN/Ready/mergeable=true, exact head `292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`, base `f0d65aa...`; local self-test 7/7, D6 `33256145573`, D7 `33256145614`, productive temp-auth compile `33256145521` y Test - Desktop Portability `33256145531` **SUCCESS**. Candidate software está listo para owner race-check/merge; physical staging/prod separation sigue externa.
- F4: PR #57 OPEN/Ready/mergeable=true, exact refreshed head `4e251cae84ff55116c89c8398e78f04aecb78e3c`, base `f0d65aa...`; Required CI exact-head, D6 `33255401544` y D7 `33255401512` SUCCESS. 24.2 está listo para owner race-check/merge.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado 007 procesado | Asignación nueva | Objetivo |
|---|---|---|---|
| AAA | STALLED snapshot, luego GitHub mostró #58 mergeable + Required CI verde | `NIGHT-AAA-008` | integrar #58 si race-check válido; después atomic empty-index únicamente |
| BBB | PENDING por CI en curso; luego exact-head quedó verde | `NIGHT-BBB-008` | integrar #57 si race-check válido; después 25.1 matrix audit dependency-safe |
| WOZ | PENDING_EXTERNAL con #59; CI terminó verde después | `NIGHT-WOZ-008` | integrar #59 si race-check válido; mantener physical separation externa; después 16.2 software-only |

No existe ownership simultáneo: AAA=F2/12.1; BBB=F4/24.2→25.1; WOZ=F3/16.1→16.2.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-008`
- REUSE PR #58 / `aaa/night-12.1-bootstrap-load`.
- Revalidar exact head/base/checks y merge protegido si siguen válidos.
- No marcar 12.1 completo por integrar #58.
- Después: atomic empty-index como único sub-slice nuevo; duplicate-check, un candidate, tests/CI exact-head.
- Pagination/window/memory y cold/warm residual quedan fuera de 008.

### `NIGHT-BBB-008`
- REUSE PR #57 / `bbb/task-24.2-updater-recovery`.
- Revalidar exact head/base/checks y merge protegido si siguen válidos.
- Después: F4/25.1 REUSE-FIRST matrix audit dependency-safe, sin modificar lógica F2/F3 para hacer pasar la matriz.
- No signing/notarization, release ni 25.2 freeze.

### `NIGHT-WOZ-008`
- REUSE PR #59 / `woz/night-16.1-runtime-operability`.
- Exact-head CI ya está completamente verde; revalidar race y merge protegido si combinación sigue vigente.
- Aun con merge, 16.1 completo sigue PENDING_EXTERNAL por separación física staging/prod.
- Después: 16.2 software-only/dependency-safe: promotion contract, API origin/TLS/headers fail-closed, smoke/rollback fixtures; sin crear provider resources/costo ni deploy real.

## BLOCKERS

1. F0/2.2: GitHub Support server-side cleanup + fresh final verification.
2. F0/1.2: governance/provenance/domain/support/status/signing/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real fuera del primary provider/account failure domain + read/checksum.
4. F1/D10.2: decisión RO sobre alpha final.
5. F2/12.1: #58 merge pendiente; después atomic empty-index, pagination/window/memory y cold/warm residual.
6. F3/16.1: #59 merge pendiente internamente; physical staging/prod resources/credentials/ownership permanecen externos.
7. F3: 16.2–20.x es el mayor volumen restante; partes de Stripe/DNS/legal/provider requieren inputs externos.
8. F4: #57 merge pendiente; D22/D23 signing/notarization externos; 25.1 incluye tails físicos.

## PROGRESO HACIA F0–F4

- **F0:** solo tails externos/administrativos; no consumir worker técnico en trabajo duplicado.
- **F1:** core técnico cerrado; D10.1 external-only + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 slice A tiene candidate mergeable + Required CI verde.
- **F3:** 16.1 software candidate #59 tiene self-test y exact-head CI completamente verdes; external physical separation conserva el gate. 16.2 será el siguiente carril dependency-safe.
- **F4:** 24.2 candidate #57 exact-head CI verde; el siguiente retorno útil es integrar y reducir 25.1.

## PLAN SYNC DEL CICLO

Actualizados:
- `!!!PLAN/Plan Maestro.md`
- `!!!PLAN/Fase 2 - Web y UX.md`
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`
- `!!!PLAN/Fase 4 - Desktop y release chain.md`
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`
- `!!!PLAN/Registro de avances.md`
- `!!!PLAN/NOCHE - AAA.md`
- `!!!PLAN/NOCHE - BBB.md`
- `!!!PLAN/NOCHE - WOZ.md`
- `!!!PLAN/NOCHE - JOBS.md`
- Issue #41 handoff `5462857248`.

Fase 0 y Fase 1 fueron leídas completas; no recibieron cambio textual porque ningún requisito/estado de esas fases cambió en este ciclo.

## SIGUIENTE CICLO

1. Releer integration HEAD y los tres PRs antes de cualquier claim.
2. Procesar merges verificables de #57/#58/#59 y sus merge SHAs; si cualquiera avanzó el baseline, invalidar cualquier CI cuya combinación material haya cambiado antes del merge restante.
3. Procesar output de atomic empty-index, 25.1 matrix y 16.2 software-only.
4. Mantener D10.1 off-provider, physical staging/prod y signing/notarization como externos hasta evidencia real.
5. Recalcular F0–F4 desde cero; no conservar asignación por inercia.
6. No abrir Fase 5 mientras gates reales necesarios sigan abiertos.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-007
INTEGRATION_HEAD: f0d65aa66988e3e1a026e237b65c65a56b098aa9
AAA: #58 d7cc93f; mergeable; Required CI 33254699647 SUCCESS -> NIGHT-AAA-008
BBB: #57 4e251cae; mergeable; Required CI + D6 33255401544 + D7 33255401512 SUCCESS -> NIGHT-BBB-008
WOZ: #59 292a7706; mergeable; self-test 7/7 + D6 33256145573 + D7 33256145614 + compile 33256145521 + Desktop Portability 33256145531 SUCCESS -> NIGHT-WOZ-008
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_MERGE: none
RELEASE: NO-GO
ISSUE_41_HANDOFF: 5462857248
```

**STOP:** ciclo JOBS 007 terminado. La siguiente ejecución debe iniciar desde GitHub vivo, no desde este snapshot si cambió.
