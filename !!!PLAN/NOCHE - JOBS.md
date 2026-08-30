# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 025`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 025

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- No existe merge posterior observable al #67.
- PRs abiertos materiales observados: #63 y #68.
- #68 `woz/night-18.1-entitlements-reservation @ 2a988ec2a25d6ecfa927614fcc32cde689995103`, base `3ad8f55a...`, OPEN/Ready/mergeable, exact-head CI aplicable verde.
- #63 `bbb/task-25.1-windows-import @ 033c2b55a0c46471b7e7ddb3af57b626699ac6e6`, base `3ad8f55a...`, OPEN/Ready; Windows Import sigue FAILURE.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/obligatorios: Plan Maestro, F0–F4, roles/coordinación, protocolo nocturno, ledgers JOBS/AAA/BBB/WOZ, Registro de avances, Issue #41 y GitHub vivo. GitHub actual se tomó como autoridad.

Hechos materiales:
1. integration sigue `3ad8f55a...`.
2. WOZ `NIGHT-WOZ-023` sí produjo resultado: PR #68 + handoff Issue #41 `5467454128`, cerrado por worker como `PENDING / WAITING_CI`.
3. Recheck JOBS del exact head #68 `2a988ec2...`: F3 18.1 `33299898356`, D6 `33299898222`, D7 `33299898232`, Productive Temp Auth Compile `33299898207` y Desktop Portability `33299898130` = SUCCESS; Upgrade 21.2 `33299898169` = SKIPPED/no aplicable.
4. #68 sigue OPEN/Ready/mergeable y base exacta sigue `3ad8f55a...`; no carrera material observable al preflight.
5. AAA `NIGHT-AAA-024` seguía ASSIGNED sin RESULTADO DEL TURNO, PR ni handoff observable.
6. BBB `NIGHT-BBB-023` seguía ASSIGNED; #63 no cambió de head y Windows Import no obtuvo PASS nuevo.
7. F0/F1 tails externos siguen sin evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### WOZ 023
`PENDING / WAITING_CI` fue resuelto factual por JOBS: la CI aplicable exact-head completó verde. No se declara 18.1 integrado porque #68 no está mergeado. Se emite `NIGHT-WOZ-024` para la transacción final de integración por el owner técnico.

### AAA 024
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`: no resultado/artifact/handoff observable; se emite 025 con el mismo scope crítico.

### BBB 023
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`: #63 permanece igual; se emite 024 con SAME PR y mismo corrective crítico.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F3 / 18.1 / PR #68:** CI ya verde; el camino más corto es la integración exacta por WOZ.
2. **F4 / 25.1 / SAME #63:** Windows Import sigue rojo; resolver primer failure causal hasta assertion/PASS literal.
3. **F2 / 13.1:** durability de Save All/bulk/garbage journal sigue dependency-safe.
4. **F2 / 12.1 cold/warm:** abierto hasta startup real comparable; no fabricar benchmark.
5. **F0/F1 + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20, resto F4 25.1/25.2 y tails externos. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 025 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 024 sin resultado observable | `NIGHT-AAA-025` — F2/13.1 | `NONE` |
| BBB | 023 sin resultado; #63 igual, Windows Import rojo | `NIGHT-BBB-024` — SAME #63 corrective | `NONE` |
| WOZ | 023 produjo #68; WAITING_CI resuelto GREEN | `NIGHT-WOZ-024` — #68 final integration transaction | `NONE` |

No overlap material: AAA=Web import durability; BBB=F4 Windows E2E harness; WOZ=billing/entitlements PR #68 integration.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-025`
PRIMARY: F2/13.1 únicamente — Save All durable con resumen parcial; bulk conflict-safe o deshabilitado honestamente; garbage journal/cleanup de uploads huérfanos. REUSE-FIRST; una sola rama/PR si hay gap.  
EVIDENCE: focused success/partial-failure/conflict/cleanup tests + no silent loss + applicable exact-head CI.  
STOP: 13.2/D14/D15, billing, Desktop, infra, scope creep o CI no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-024`
PRIMARY: SAME #63; consumir run `33284981477`/job `99186491944`, identificar primer failure causal actual y hacer corrective F4/harness mínimo. Windows Import literal PASS antes de promover matrix. Head nuevo → fresh applicable exact-head gates + race-check.  
EVIDENCE: failure causal, exact delta, session/assertion/PASS o blocker factual, CI exact-head.  
STOP: bug productivo fuera de F4, 25.2/D22/D23, package/global change no justificado, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-024`
PRIMARY: PR #68 final integration transaction. Revalidar integration HEAD y exact head; si sigue base `3ad8f55a...` sin carrera material, integrar por flujo autorizado del owner; verificar merge SHA/post-merge integration SHA; reportar handoff. No iniciar 18.2.  
EVIDENCE: live baseline, exact-head green already observed, race-check, merge SHA, integration SHA post-merge.  
STOP: baseline materialmente distinto, conflicto/merge rechazado, CI no aplicable, 18.2/provider real/grace decisions/infra.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2: D13–D15 abiertos; D13.1 asignado.
7. F3: #68 awaiting owner integration; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: Windows Import `33284981477` FAILURE; #63 no mergeado; otros matrix gaps. D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 reducido a cold/warm runtime; D13.1 activo por assignment; 13.2–15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; 18.1 candidate #68 exact-head green esperando integración; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 Windows Import rojo; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 025

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 025 + #68 exact-head green + IDs nuevos;
- `!!!PLAN/Fase 2 - Web y UX.md` → AAA 025;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md` → #68 green / WOZ 024 integration;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → BBB 024;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 025;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-025`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-024`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-024`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 025.

`Registro de avances.md` fue leído completo para el preflight; no se añadió entrada porque #68 todavía no está integrado y este ciclo no produjo nuevo merge/PASS de gate. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de cualquier claim.
2. Procesar primero cualquier RESULTADO real de AAA 025 / BBB 024 / WOZ 024.
3. Si WOZ integra #68, actualizar baseline y revalidar candidates afectados antes de cualquier merge posterior.
4. BBB: no aceptar green genérico como sustituto de Windows Import literal PASS.
5. AAA: cero pérdida silenciosa es gate literal de D13.
6. Mantener 12.1 cold/warm abierto hasta evidencia runtime real.
7. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-025
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
WOZ_023: PENDING/WAITING_CI -> EXACT_HEAD_CI_GREEN / PR68 NOT_MERGED
AAA_024: NOT_PROCESSED / SUPERSEDED
BBB_023: NOT_PROCESSED / SUPERSEDED
AAA_NEW: NIGHT-AAA-025 ASSIGNED F2/13.1
BBB_NEW: NIGHT-BBB-024 ASSIGNED SAME #63 corrective
WOZ_NEW: NIGHT-WOZ-024 ASSIGNED PR68 final integration
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 025 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-025`, `NIGHT-BBB-024` y `NIGHT-WOZ-024`.
