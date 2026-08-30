# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 028`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 028

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- GitHub vivo no muestra merge posterior a #67.
- PR #69: OPEN/Ready/mergeable, base `3ad8f55a...`, head `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`; D6/D7/Desktop Portability exact-head SUCCESS. Helper Save All/bulk-safe probado; product wiring no reclamado aún.
- PR #63: OPEN/Ready/mergeable, base `3ad8f55a...`, head `e14a3ab9a284484cace9b8fa98c293c7c15b5dce`; F4 Matrix/D6/D7/Desktop Portability y **Windows Import exact-head SUCCESS**.
- PR #68: OPEN/Ready/mergeable, base `3ad8f55a...`, head `2a988ec2a25d6ecfa927614fcc32cde689995103`; exact-head applicable CI verde histórico aceptado; merge execution sigue bloqueado externamente.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/obligatorios: Plan Maestro, F0–F4, Equipo multi-IA, protocolo nocturno, ledgers JOBS/AAA/BBB/WOZ, Registro de avances e Issue #41 completo mediante fetch paginado. GitHub actual fue autoridad.

Hechos verificados:
1. integration sigue exactamente `3ad8f55a...`.
2. AAA `NIGHT-AAA-027` cerró PENDING/WAITING_CI sobre SAME #69 @ `b2ab75ae...`; JOBS recheck confirmó D6 `33303237410`, D7 `33303237375`, Desktop Portability `33303237401` SUCCESS; Upgrade no aplicable.
3. #69 continúa OPEN/Ready/mergeable. El artifact helper está probado; product Review/Import/Bulk wiring quedó UNVERIFIED por el propio worker.
4. BBB `NIGHT-BBB-026` cerró PENDING/WAITING_CI sobre SAME #63 @ `e14a3ab9...` después de restaurar auto provisioning del launcher.
5. JOBS recheck #63 exact-head confirmó F4 Matrix `33303300262`, D6 `33303300263`, D7 `33303300298`, Desktop Portability `33303300278` y **Windows Import `33303300259` = SUCCESS**.
6. Windows Import SUCCESS demuestra el journey funcional existente en ese candidate head; matrix promotion todavía no ocurrió y cualquier promotion crea head nuevo que exige fresh exact-head CI.
7. WOZ `NIGHT-WOZ-026` no tiene RESULTADO DEL TURNO ni artifact/handoff nuevo observable; se supersede con 027 para monotonicidad.
8. #68 sigue OPEN/Ready/mergeable y frozen; no merge SHA nuevo.
9. F0/F1 tails externos no tienen evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-027
`PENDING / WAITING_CI` procesado. CI exact-head terminó verde. Se emite `NIGHT-AAA-028` SAME #69 para comprobar/wirear el flujo productivo real y completar la integración Web sin tocar server journal.

### BBB / NIGHT-BBB-026
`PENDING / WAITING_CI` procesado. Fresh exact-head Windows Import y todos los gates aplicables terminaron SUCCESS. Se emite `NIGHT-BBB-027` SAME #63 para promover únicamente `windows/import` a `AUTOMATED_PASS`, obtener fresh exact-head CI en el nuevo head y merge solo si race-check verde.

### WOZ / NIGHT-WOZ-026
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`. No resultado observable. Se reemite la misma pieza independiente como `NIGHT-WOZ-027`; #68 continúa frozen.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / #63:** Windows Import ya pasó literalmente. La acción de mayor retorno inmediato es promotion → fresh exact-head gates → race-check/merge del mismo PR.
2. **F2 / 13.1:** AAA termina product wiring/integración de #69 y WOZ trabaja server garbage-journal/orphan cleanup en paralelo, sin overlap.
3. **F3 / 18.1 / #68:** candidate técnicamente listo pero bloqueado por execution layer; preservar frozen hasta capacidad autorizada real.
4. **F2 / 12.1:** cold/warm runtime Web real sigue pendiente; no fabricar benchmark.
5. **F0/F1 + F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20 y resto F4 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 028 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | #69 exact-head applicable CI green; product wiring unverified | `NIGHT-AAA-028` — SAME #69 product wiring + final Web integration | `NONE` |
| BBB | #63 exact-head Windows Import + gates SUCCESS | `NIGHT-BBB-027` — SAME #63 matrix promotion + fresh CI + merge | `NONE` |
| WOZ | 026 sin resultado | `NIGHT-WOZ-027` — F2/13.1 server garbage-journal/orphan cleanup | `NONE` |

No overlap material: AAA=F2 frontend/product wiring; BBB=F4 matrix/harness transaction; WOZ=F2 server journal/reconciliation. #68 queda frozen sin owner concurrente activo.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-028`
PRIMARY: SAME #69; reutilizar helper probado; confirmar/wirear el flujo productivo Review/Import/Bulk a Save All/progreso/resumen parcial/conflict-safe; fresh exact-head CI si cambia head; race-check/merge solo si verde. No cerrar 13.1 completo.  
EVIDENCE: wiring real, focused tests, durable/CAS por item, exact-head CI, merge SHA si integra.  
STOP: server journal/WOZ overlap, scope 13.2+, baseline race, CI rojo no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-027`
PRIMARY: SAME #63; usar Windows Import literal PASS del head `e14a3ab9...`; promover solo `windows/import` a `AUTOMATED_PASS`; exigir Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head en promotion head; race-check/merge solo si verde.  
EVIDENCE: matrix delta mínimo, promotion-head exact SHA, fresh gates, race-check, merge SHA/integration HEAD si integra.  
STOP: producto fuera de F4, otros matrix gaps, D22/D23/25.2, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-027`
PRIMARY: REUSE-FIRST sobre garbage journal/reconciliation; demostrar o implementar el server contract mínimo Web-callable durable para registrar/reconciliar orphans, con persistencia/retry/idempotencia/fail-closed y protección committed/valid.  
EVIDENCE: artifact reutilizado, gap exacto, focused tests, exact-head CI si hay candidate.  
STOP: tocar frontend AAA, decisión RO/policy no definida, #68/billing/Desktop/infra, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2/13.1: AAA product wiring/integration + WOZ server orphan cleanup.
7. F3/18.1: #68 exact-head green pero merge bloqueado por execution layer; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: Windows Import ya PASS; promotion/fresh-CI/merge pendiente; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm; 13.1 tiene helper Web green pero product wiring/integration y server cleanup aún abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; #68 green pero no merged; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; Windows Import literal PASS ya obtenido en #63; promotion/integration aún abierta; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 028

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 028;
- `!!!PLAN/Fase 2 - Web y UX.md` → #69 green + AAA 028 / WOZ 027;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → Windows Import SUCCESS + BBB 027 promotion transaction;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 028;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-028`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-027`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-027`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 028.

`Registro de avances.md` fue leído completo; no se añade entrada porque todavía no hubo nuevo merge/PASS de gate estable, solo candidatos exact-head green. F0/F1/F3 no se modifican porque no hay evidencia nueva que cambie sus estados. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de claims.
2. Procesar resultados AAA 028 / BBB 027 / WOZ 027 una sola vez.
3. BBB: exigir fresh promotion-head Windows Import + applicable CI; si #63 integra, sincronizar baseline y revalidar #69/#68 por race/combinación material.
4. AAA: no aceptar helper green como sustituto de product wiring; integrar #69 solo cuando el flujo real esté demostrado.
5. WOZ: cerrar solo server half; no tocar #68 en 027.
6. Mantener 12.1 abierto hasta runtime cold/warm real.
7. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-028
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_027: PENDING/WAITING_CI -> applicable exact-head CI SUCCESS; #69 OPEN
BBB_026: PENDING/WAITING_CI -> Windows Import 33303300259 SUCCESS + applicable gates SUCCESS
WOZ_026: NOT_PROCESSED -> superseded
AAA_NEW: NIGHT-AAA-028 ASSIGNED SAME #69 product wiring/final Web integration
BBB_NEW: NIGHT-BBB-027 ASSIGNED SAME #63 promotion/fresh-CI/merge
WOZ_NEW: NIGHT-WOZ-027 ASSIGNED F2/13.1 server half
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 028 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-028`, `NIGHT-BBB-027` y `NIGHT-WOZ-027`.
