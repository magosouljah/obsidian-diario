# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 024`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 024

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- No existe merge posterior observable al #67.
- Único PR abierto observado: #63 `bbb/task-25.1-windows-import @ 033c2b55a0c46471b7e7ddb3af57b626699ac6e6`, base `3ad8f55a...`.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/obligatorios: Plan Maestro, F0–F4, roles/coordinación, protocolo nocturno, ledgers JOBS/AAA/BBB/WOZ, Registro de avances, Issue #41 y GitHub vivo. GitHub actual se tomó como autoridad.

Hechos materiales:
1. integration sigue `3ad8f55a...`.
2. Issue #41 no recibió handoff worker posterior a CYCLE 023; el último comentario nuevo era el sync JOBS 023.
3. AAA `NIGHT-AAA-023` seguía ASSIGNED sin RESULTADO DEL TURNO, PR ni handoff observable.
4. BBB `NIGHT-BBB-022` seguía ASSIGNED; #63 no cambió de head; Windows Import `33284981477` permanece FAILURE.
5. WOZ `NIGHT-WOZ-022` seguía ASSIGNED sin RESULTADO DEL TURNO, PR ni handoff observable.
6. No replacement PRs para los carriles actuales; no duplicate work observable.
7. F0/F1 tails externos siguen sin nueva evidencia de cierre.

## RESULTADOS PROCESADOS

No apareció un nuevo resultado técnico worker que autorice DONE/PASS/merge/checklist en este ciclo. Por idempotencia y por la regla de Assignment IDs monotónicos:
- AAA 023 = `NOT_PROCESSED / SUPERSEDED_BY_JOBS`;
- BBB 022 = `NOT_PROCESSED / SUPERSEDED_BY_JOBS`;
- WOZ 022 = `NOT_PROCESSED / SUPERSEDED_BY_JOBS`.

No se interpreta esto como fallo del worker ni como progreso técnico. Solo evita que una orden vieja pueda ejecutarse después de que CYCLE 024 emite IDs nuevos.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / SAME #63:** sigue siendo el blocker técnico más concreto: Windows Import no llega a PASS literal.
2. **F3 / 18.1:** 17.2 ya está integrado; limits/entitlements/reserva/subscription-state software es dependency-ready e independiente del provider productivo.
3. **F2 / 13.1:** durability de Save All/bulk/garbage journal avanza F2 sin bloquearse por el residual runtime 12.1.
4. **F2 / 12.1 cold/warm:** sigue abierto hasta startup real comparable; no fabricar benchmark.
5. **F0/F1 + D22/D23:** externos/RO; no repetir drills aceptados.
6. Después: F2 13.2–15, F3 18.2–20, resto F4 25.1/25.2 y tails externos. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 024 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 023 sin resultado observable | `NIGHT-AAA-024` — F2/13.1 | `NONE` |
| BBB | 022 sin resultado; #63 igual, Windows Import rojo | `NIGHT-BBB-023` — SAME #63 corrective | `NONE` |
| WOZ | 022 sin resultado observable | `NIGHT-WOZ-023` — F3/18.1 software-only | `NONE` |

No overlap material: AAA=Web import durability; BBB=F4 Windows E2E harness; WOZ=billing/entitlements server-side.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-024`
PRIMARY: F2/13.1 únicamente — Save All durable con resumen parcial; bulk conflict-safe o deshabilitado honestamente; garbage journal/cleanup de uploads huérfanos. REUSE-FIRST; una sola rama/PR si hay gap.  
EVIDENCE: focused success/partial-failure/conflict/cleanup tests + no silent loss + applicable exact-head CI.  
STOP: 13.2/D14/D15, billing, Desktop, infra, scope creep o CI no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-023`
PRIMARY: SAME #63; consumir run `33284981477`/job `99186491944`, identificar primer failure causal actual y hacer corrective F4/harness mínimo. Windows Import literal PASS antes de promover matrix. Head nuevo → fresh applicable exact-head gates + race-check.  
EVIDENCE: failure causal, exact delta, session/assertion/PASS o blocker factual, CI exact-head.  
STOP: bug productivo fuera de F4, 25.2/D22/D23, package/global change no justificado, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-023`
PRIMARY: F3/18.1 software-only — limits/entitlements server-side antes de reserva; transacción/reserva anti-race; Billing Portal/cancelación/subscription-state contract server-side. REUSE-FIRST #65/#67.  
EVIDENCE: concurrency/limits/state focused tests + applicable exact-head CI; migration evidence si aplica.  
STOP: Stripe/provider real, 18.2+, grace-period/business decision, infra/costo o CI no atribuible.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2: D13–D15 abiertos; D13.1 asignado.
7. F3: 18–20 abiertos; 18.1 asignado; 16.1/16.2 tails externos.
8. F4/25.1: Windows Import `33284981477` FAILURE; #63 no mergeado; otros matrix gaps. D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 reducido a cold/warm runtime; D13.1 activo por assignment; 13.2–15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; 18.1 activo por assignment; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 Windows Import rojo; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 024

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 024 + IDs nuevos;
- `!!!PLAN/Fase 2 - Web y UX.md` → AAA 024;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md` → WOZ 023;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → estado vivo #63 + BBB 023;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 024;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-024`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-023`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-023`;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 024.

`Registro de avances.md` fue leído completo para el preflight; no se añadió entrada porque este ciclo no produjo nuevo merge/PASS/resultado técnico, solo reasignación monotónica y corrección de estado documental. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de cualquier claim.
2. Procesar primero cualquier RESULTADO real de AAA 024 / BBB 023 / WOZ 023.
3. BBB: no aceptar green genérico como sustituto de Windows Import literal PASS.
4. WOZ: software 18.1 no equivale a Stripe/provider productivo.
5. AAA: cero pérdida silenciosa es gate literal de D13.
6. Mantener 12.1 cold/warm abierto hasta evidencia runtime real.
7. Cualquier merge que mueva integration obliga revalidación de candidates afectados.
8. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-024
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
NEW_WORKER_RESULTS: none
AAA_023: NOT_PROCESSED / SUPERSEDED
BBB_022: NOT_PROCESSED / SUPERSEDED
WOZ_022: NOT_PROCESSED / SUPERSEDED
AAA_NEW: NIGHT-AAA-024 ASSIGNED F2/13.1
BBB_NEW: NIGHT-BBB-023 ASSIGNED SAME #63 corrective
WOZ_NEW: NIGHT-WOZ-023 ASSIGNED F3/18.1 software-only
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 024 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-024`, `NIGHT-BBB-023` y `NIGHT-WOZ-023`.
