# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 031`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 031

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- GitHub vivo sigue sin merge posterior a #67.
- PR #69: OPEN/Ready/mergeable @ `b2ab75ae...`; helper/unit + D6/D7/Desktop Portability green, pero product App path sigue bypassing `saveAllWebItems`.
- PR #63: OPEN/Ready/mergeable @ `1b957eff...`; Windows Import `33305947664` SUCCESS; Required CI `33305947677` SUCCESS; F4 Matrix `33305947676` FAILURE en `matrix-contract`.
- PR #70: OPEN/Ready/mergeable @ `5a99ebf2...`; focused F2 `33304798320` SUCCESS; Required CI `33304798363` FAILURE ya atribuida a fixture live-PG legacy que omite `isObjectStillOrphan`; PostgreSQL/provider no fue la causa.
- PR #68: OPEN/Ready/mergeable @ `2a988ec2...`; exact-head green histórico; merge execution sigue bloqueado externamente/frozen.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; ledgers JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 y GitHub actual. GitHub/runtime fue autoridad.

Hechos verificados:
1. Integration continúa exactamente `3ad8f55a...`.
2. AAA `NIGHT-AAA-030` no dejó RESULTADO DEL TURNO observable antes de este ciclo; #69 permanece sin head movement.
3. BBB `NIGHT-BBB-029` no dejó RESULTADO DEL TURNO observable antes de este ciclo; #63 permanece en `1b957eff...` con Windows Import + Required CI verdes y F4 Matrix rojo.
4. WOZ `NIGHT-WOZ-029` sí dejó handoff verificable `5468213443`: Required CI #70 falló en `postgres-live.integration.cjs:159` con actual `REQUIRED`, expected `ETIMEDOUT` porque el fixture de `reason='orphan_upload'` no provee el nuevo guard `isObjectStillOrphan`.
5. WOZ verificó PostgreSQL containers sanos; failure determinista/candidate-specific, no outage provider-wide.
6. El corrective mínimo correcto es de test: añadir guard autoritativo positivo al fixture ETIMEDOUT; cambiar producto fail-closed sería incorrecto.
7. El quinto path `cloud-server/tests/postgres-live.integration.cjs` estaba fuera del scope explícito anterior; JOBS lo autoriza ahora solo para ese corrective.
8. #68 sigue frozen y no se reintenta ceremonialmente.
9. F0/F1 external tails no tienen evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-030
`NO_RESULT / SUPERSEDED_BY_JOBS`. GitHub #69 unchanged. Nueva orden `NIGHT-AAA-031` conserva SAME #69 y mismo wiring productivo mínimo.

### BBB / NIGHT-BBB-029
`NO_RESULT / SUPERSEDED_BY_JOBS`. GitHub #63 unchanged. Nueva orden `NIGHT-BBB-030` conserva SAME #63 y mismo matrix-contract corrective.

### WOZ / NIGHT-WOZ-029
`PENDING / ATTRIBUTED_CORRECTIVE_BLOCKED_BY_SCOPE_TOOLING` procesado. El failure ya está atribuido; nueva orden `NIGHT-WOZ-030` autoriza exclusivamente el quinto server-test path para corregir el fixture, preservar fail-closed productivo y ejecutar fresh focused + Required CI.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 13.1 server / #70:** corrective de fixture autorizado → fresh focused + Required CI → race-check/merge.
2. **F4 / 25.1 / #63:** matrix-contract rojo → corrective mínimo → fresh gates → race-check/merge.
3. **F2 / 13.1 Web / #69:** minimal product wiring → focused evidence + fresh exact-head CI → race-check/merge.
4. **F3 / 18.1 / #68:** candidate green pero bloqueado por execution layer; preservar frozen.
5. **F2 / 12.1:** cold/warm runtime Web real cuantificado.
6. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
7. Después: F2 13.2–15, F3 18.2–20 y F4 25.2/otros matrix gaps. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 031 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 030 sin resultado; #69 unchanged; product wiring missing | `NIGHT-AAA-031` — SAME #69 minimal product wiring + focused evidence + fresh CI/merge | `NONE` |
| BBB | 029 sin resultado; #63 unchanged; matrix-contract red | `NIGHT-BBB-030` — SAME #63 matrix-contract attribution/corrective + fresh gates + merge | `NONE` |
| WOZ | 029 atribuyó #70 red a live-PG fixture legacy | `NIGHT-WOZ-030` — autorizar quinto test path, corrective mínimo + fresh focused/Required CI + merge | `NONE` |

No overlap material: AAA=F2 frontend/product wiring; BBB=F4 matrix transaction; WOZ=F2 server test/corrective. #68 frozen.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-031`
PRIMARY: SAME #69; wiring mínimo `App/Review/Import/Bulk -> saveAllWebItems`, demostrar saved/conflict/failed + partial/retry semantics, fresh exact-head CI y merge si green.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-030`
PRIMARY: SAME #63; atribuir/corregir únicamente F4 `matrix-contract` rojo; no reabrir Windows harness. Si cambia head, F4 Matrix + Windows Import + D6 + D7 + Desktop Portability/Required CI fresh exact-head; merge solo si todo green.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-030`
PRIMARY: SAME #70; JOBS autoriza `cloud-server/tests/postgres-live.integration.cjs` como quinto path únicamente para añadir guard positivo `isObjectStillOrphan` (o equivalente) al fixture ETIMEDOUT. No cambiar fail-closed productivo. Fresh focused F2 + Required CI; race-check/merge solo si todo green.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2/13.1: #69 product wiring + #70 corrective/fresh CI.
7. F3/18.1: #68 merge blocked by execution layer; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: #63 F4 matrix-contract red; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm; 13.1 reducido a wiring #69 + corrective de fixture #70.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; #68 green pero no merged; 18.2–20 abiertos.
- **F4:** Windows Import literal PASS en promotion head; blocker actual matrix-contract; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 031

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 031;
- `!!!PLAN/Fase 2 - Web y UX.md` → AAA031/WOZ030 y corrective #70 autorizado;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → BBB030;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 031;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-031`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-030`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-030`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 031.

`Registro de avances.md` fue leído; no se añade entrada porque no hubo nuevo merge/PASS de gate estable. F0/F1/F3 no se modifican porque sus estados materiales no cambiaron. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de claims.
2. Procesar AAA031 / BBB030 / WOZ030 una sola vez.
3. Si cualquier PR integra y mueve baseline, revalidar candidates restantes por combinación material.
4. No aceptar focused #70 green como sustituto de Required CI fresh.
5. No aceptar Windows Import green como sustituto de F4 Matrix green.
6. Mantener #68 frozen mientras execution layer bloquee merge.
7. Mantener 12.1 abierto hasta runtime cold/warm real.
8. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-031
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_030: NO_RESULT; #69 unchanged
BBB_029: NO_RESULT; #63 unchanged; matrix-contract red remains
WOZ_029: PENDING but failure attributed to missing isObjectStillOrphan guard in PG-live ETIMEDOUT fixture
AAA_NEW: NIGHT-AAA-031 SAME #69
BBB_NEW: NIGHT-BBB-030 SAME #63
WOZ_NEW: NIGHT-WOZ-030 SAME #70 + fifth server-test path authorized
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 031 completado.
