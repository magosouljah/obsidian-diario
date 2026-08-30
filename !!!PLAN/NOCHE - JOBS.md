# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 029`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 029

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- GitHub vivo sigue sin merge posterior a #67.
- PR #69: SAME Web candidate @ `b2ab75ae...`; helper Save All/bulk-safe con D6/D7/Desktop Portability exact-head SUCCESS; product wiring todavía pendiente.
- PR #63: SAME F4 candidate @ `e14a3ab9...`; Windows Import + F4 Matrix + D6 + D7 + Desktop Portability exact-head SUCCESS; promotion/new-head transaction pendiente.
- PR #70: server candidate @ `5a99ebf2...`; focused F2/13.1 workflow `33304798320` SUCCESS; Required CI/Test Desktop Portability `33304798363` FAILURE en PostgreSQL live integration + recovery gate.
- PR #68: OPEN/Ready/mergeable @ `2a988ec2...`; exact-head green histórico; merge execution sigue bloqueado externamente.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos los canónicos requeridos: Plan Maestro; F0–F4; Equipo multi-IA; protocolo nocturno; ledgers JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 + comentarios paginados; GitHub actual. GitHub/runtime fue autoridad.

Hechos verificados:
1. integration continúa exactamente `3ad8f55a...`.
2. AAA `NIGHT-AAA-028` no tiene RESULTADO DEL TURNO observable; #69 no cambió. Se supersede con 029 sin duplicar artifact.
3. BBB `NIGHT-BBB-027` no tiene RESULTADO DEL TURNO observable; #63 no cambió. Se supersede con 028 sin duplicar artifact.
4. WOZ `NIGHT-WOZ-027` sí produjo PR #70 @ `5a99ebf2...`, server-only y sin overlap con AAA.
5. `F2 - 13.1 Orphan Lifecycle` run `33304798320` terminó SUCCESS exact-head.
6. Required CI/Test Desktop Portability run `33304798363` terminó FAILURE exact-head. El job PostgreSQL live integration + recovery falló en `Execute migrations and adversarial persistence checks on PostgreSQL`; Web/shared y Supply chain visibles pasaron.
7. Por evidence-before-claim, #70 NO es PASS ni integration-ready hasta atribuir/resolver ese gate y obtener exact-head green aplicable.
8. #68 sigue frozen y no se reintenta ceremonialmente.
9. F0/F1 external tails no tienen evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-028
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`. No resultado observable ni nuevo artifact. Nueva orden `NIGHT-AAA-029` conserva SAME #69 y exige product wiring factual.

### BBB / NIGHT-BBB-027
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`. No resultado observable ni nuevo artifact. Nueva orden `NIGHT-BBB-028` conserva SAME #63 y la promotion transaction.

### WOZ / NIGHT-WOZ-027
`PENDING / WAITING_CI` procesado. #70 existe y su focused workflow pasó, pero Required CI está rojo en PostgreSQL live/recovery. Nueva orden `NIGHT-WOZ-028` exige attribution-first y prohíbe cambiar producto si el fallo no es atribuible.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / #63:** promotion → fresh exact-head Windows Import/F4/D6/D7/Desktop Portability → race-check/merge.
2. **F2 / 13.1:** AAA #69 product wiring Web + WOZ #70 PG-gate attribution/fix en paralelo, sin overlap.
3. **F3 / 18.1 / #68:** candidate green pero bloqueado por execution layer; preservar frozen.
4. **F2 / 12.1:** cold/warm runtime Web real cuantificado.
5. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20 y F4 25.2/otros gaps. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 029 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 028 sin resultado; #69 unchanged | `NIGHT-AAA-029` — SAME #69 product wiring + final Web integration | `NONE` |
| BBB | 027 sin resultado; #63 unchanged | `NIGHT-BBB-028` — SAME #63 promotion + fresh exact-head gates + merge | `NONE` |
| WOZ | #70 focused PASS / Required CI PG gate FAILURE | `NIGHT-WOZ-028` — SAME #70 attribution/fix + integrate only if green | `NONE` |

No overlap material: AAA=F2 frontend/product wiring; BBB=F4 matrix/harness transaction; WOZ=F2 server orphan lifecycle. #68 permanece frozen.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-029`
PRIMARY: SAME #69; demostrar/wirear Review/Import/Bulk productivo al helper Save All/progreso/resumen/conflict-safe; fresh exact-head CI si cambia head; race-check/merge solo si verde.  
EVIDENCE: wiring real, focused tests, durable/CAS por item, exact-head CI, merge SHA si integra.  
STOP: server/#70, 13.2+, baseline race, CI rojo no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-028`
PRIMARY: SAME #63; promover solo `windows/import` a `AUTOMATED_PASS`; exigir Windows Import + F4 Matrix + D6 + D7 + Desktop Portability fresh exact-head en promotion head; race-check/merge solo si verde.  
EVIDENCE: matrix delta mínimo, new head, fresh gates, race-check, merge SHA/integration HEAD.  
STOP: producto fuera F4, otros matrix gaps, D22/D23/25.2, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-028`
PRIMARY: SAME #70; aceptar focused run `33304798320` SUCCESS; diagnosticar Required CI `33304798363` PostgreSQL live/recovery failure; corregir solo si atribuible; si cambia head, focused + Required CI fresh exact-head; race-check/merge solo si todo aplicable queda green.  
EVIDENCE: failure attribution, logs/repro, tests, exact-head CI, merge SHA si integra.  
STOP: fallo externo/no atribuible, frontend AAA, #68/billing/Desktop/infra, baseline race o evidencia insuficiente.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2/13.1: #69 product wiring/integration + #70 Required CI PG gate attribution/resolution.
7. F3/18.1: #68 merge blocked by execution layer; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: #63 promotion/fresh-CI/merge pendiente; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm; 13.1 ahora tiene #69 Web candidate y #70 server candidate, pero #70 Required CI rojo.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; #68 green pero no merged; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; Windows Import literal PASS ya existe en #63; promotion/integration aún abierta; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 029

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 029;
- `!!!PLAN/Fase 2 - Web y UX.md` → #70 focused PASS + Required CI PG failure, AAA029/WOZ028;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → BBB028;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 029;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-029`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-028`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-028`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 029.

`Registro de avances.md` fue leído; no se añade entrada porque no hubo nuevo merge/PASS de gate estable: #70 es candidate con Required CI rojo. F0/F1/F3 no se modifican porque sus estados no cambiaron. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de claims.
2. Procesar AAA029 / BBB028 / WOZ028 una sola vez.
3. Si #63 o #69/#70 integran y mueven baseline, revalidar candidates restantes por combinación material.
4. No aceptar focused #70 green como sustituto de Required CI.
5. Mantener #68 frozen mientras la execution layer bloquee merge.
6. Mantener 12.1 abierto hasta runtime cold/warm real.
7. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-029
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_028: NO_RESULT -> superseded
BBB_027: NO_RESULT -> superseded
WOZ_027: #70 @ 5a99ebf2; focused F2 33304798320 SUCCESS; Required CI 33304798363 FAILURE at PostgreSQL live/recovery
AAA_NEW: NIGHT-AAA-029 SAME #69
BBB_NEW: NIGHT-BBB-028 SAME #63
WOZ_NEW: NIGHT-WOZ-028 SAME #70 attribution/fix
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 029 completado.
