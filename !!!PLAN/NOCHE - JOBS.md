# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 027`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 027

- BeatGaler integración verificada: `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.
- GitHub vivo no muestra merge posterior al #67.
- PR #68: OPEN/Ready/mergeable, base `3ad8f55a...`, head `2a988ec2a25d6ecfa927614fcc32cde689995103`; exact-head applicable CI verde; `NIGHT-WOZ-025` intentó merge pero execution layer bloqueó la mutación antes de GitHub.
- PR #63: OPEN/Ready/mergeable, base `3ad8f55a...`, head `ed03b806669373758d38bfd211e8f8905c86e269`; Windows Import `33300992453` sigue FAILURE antes de assertions; matrix/D6/D7/Desktop Portability verdes.
- Release público: 🔴 `NO-GO`.

## PREFLIGHT FACTUAL

Leídos completos/obligatorios: Plan Maestro, F0–F4, Equipo multi-IA, protocolo nocturno, ledgers JOBS/AAA/BBB/WOZ, Registro de avances e Issue #41 completo. GitHub actual fue autoridad.

Hechos verificados:
1. integration sigue exactamente `3ad8f55a...`.
2. AAA `NIGHT-AAA-026` no tiene RESULTADO DEL TURNO nuevo, branch/PR ni handoff observable; se supersede con 027 para monotonicidad.
3. BBB `NIGHT-BBB-025` no tiene RESULTADO DEL TURNO nuevo ni head posterior; #63 sigue `ed03b806...`; se supersede con 026.
4. WOZ `NIGHT-WOZ-025` sí produjo resultado: `BLOCKED / MERGE_TOOL_REJECTED`.
5. WOZ revalidó #68 base/head/race y exact-head CI; el merge con expected-head guard fue bloqueado por la execution/safety layer antes de que GitHub aceptara mutación. Recheck: integration sin cambio; no merge SHA.
6. #68 continúa OPEN/Ready/mergeable; no corresponde recrear candidate ni marcar 18.1 integrado.
7. Windows Import #63 sigue exactamente FAILURE en run `33300992453`, job `99228993010`; no evidencia nueva de bug productivo porque falla antes de assertions.
8. F0/F1 tails externos no tienen evidencia nueva de cierre.

## RESULTADOS PROCESADOS

### AAA / NIGHT-AAA-026
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`. No resultado nuevo observable. Se emite `NIGHT-AAA-027` sobre el mismo carril Web dependency-safe.

### BBB / NIGHT-BBB-025
`NOT_PROCESSED / SUPERSEDED_BY_JOBS`. GitHub conserva #63/head/failure. Se emite `NIGHT-BBB-026` SAME #63.

### WOZ / NIGHT-WOZ-025
`BLOCKED / MERGE_TOOL_REJECTED` procesado. No merge, no 18.1 closure. #68 queda frozen/holding item; el blocker es capacidad de ejecución de merge, no falta de CI/código observada. Para no desperdiciar ciclos, WOZ se mueve explícitamente a un slice independiente: F2/13.1 server garbage-journal/orphan reconciliation.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F4 / 25.1 / #63:** trabajo ejecutable inmediato; resolver launcher/session hasta Windows Import literal PASS.
2. **F2 / 13.1:** paralelizar los dos halves reales sin overlap: AAA=Web Save All/bulk; WOZ=server garbage journal/orphan cleanup.
3. **F3 / 18.1 / #68:** candidate exact-head green, pero merge bloqueado por execution layer; preservar y no repetir intento ceremonial.
4. **F2 / 12.1:** cold/warm runtime Web real sigue pendiente; no fabricar benchmark.
5. **F0/F1 + F3 external tails + D22/D23:** externos/RO.
6. Después: 13.2–15, F3 18.2–20, resto 25.1/25.2. F5 sigue cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual CYCLE 027 | PRIMARY nuevo | CI-FALLBACK |
|---|---|---|---|
| AAA | 026 sin resultado | `NIGHT-AAA-027` — Save All + bulk Web-only | `NONE` |
| BBB | 025 sin resultado; #63 Windows Import FAILURE | `NIGHT-BBB-026` — SAME #63 launcher/session corrective | `NONE` |
| WOZ | 025 BLOCKED / MERGE_TOOL_REJECTED | `NIGHT-WOZ-026` — F2/13.1 server garbage-journal/orphan cleanup | `NONE` |

No overlap material: AAA=F2 frontend orchestration; BBB=F4 Windows harness; WOZ=F2 server journal/reconciliation. #68 queda frozen sin owner concurrente activo.

## PRIMARY / CI-FALLBACK EMITIDOS

### AAA — `NIGHT-AAA-027`
PRIMARY: usar durable commit/CAS existente para Save All multi-item con progreso/resumen parcial y bulk conflict-safe; no tocar server journal/cleanup de WOZ ni afirmar 13.1 cerrado.  
EVIDENCE: total/partial/conflict/retry tests, zero silent loss, exact-head CI si hay candidate.  
STOP: server-side journal/cleanup, overlap con WOZ, 13.2/D14/D15, billing/Desktop/infra, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-026`
PRIMARY: SAME #63; consumir failure `33300992453`/job `99228993010`; verificar config/provider/session realmente consumido; corregir primer failure causal F4 mínimo; obtener session + Windows Import literal PASS antes de matrix promotion.  
EVIDENCE: failure causal, delta mínimo, provider/session efectiva, PASS literal o blocker, fresh exact-head gates.  
STOP: bug productivo fuera de F4, 25.2/D22/D23, package/global change injustificado, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-026`
PRIMARY: REUSE-FIRST sobre `garbage-journal-repository.js` / `garbage-reconciliation-worker.js` y contratos relacionados; demostrar o implementar solo el server contract mínimo Web-callable durable para registrar/reconciliar orphans, con persistencia/retry/idempotencia y protección contra borrar uploads válidos/committed.  
EVIDENCE: artifact reutilizado, gap exacto, tests focused, exact-head CI si hay candidate, UNVERIFIED explícito.  
STOP: tocar frontend AAA, decisión RO/policy no definida, #68/18.2/billing/Desktop/infra, baseline race o CI no atribuible.  
CI-FALLBACK: `NONE`.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: cold/warm runtime real cuantificado.
6. F2/13.1: ambos halves ahora asignados; cierre depende de evidencia real AAA 027 + WOZ 026.
7. F3/18.1: #68 exact-head green pero merge bloqueado por execution layer; 18.2–20 abiertos; 16.1/16.2 tails externos.
8. F4/25.1: Windows Import `33300992453` FAILURE antes de assertions; #63 no mergeado; otros matrix gaps; D22/D23 externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 solo cold/warm; 13.1 ahora trabaja Web y server en paralelo con ownership separado; 13.2–15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1/17.2 integrados; #68 técnicamente green pero no mergeable por execution layer disponible; 18.2–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 Windows harness rojo; 25.1/25.2 abiertos; D22/D23 externos.
- **F5:** `NO ABRIR` todavía.

## PLAN SYNC — CYCLE 027

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md` → CYCLE 027;
- `!!!PLAN/Fase 2 - Web y UX.md` → AAA 027 + WOZ 026 split 13.1;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md` → #68 merge execution blocker;
- `!!!PLAN/Fase 4 - Desktop y release chain.md` → BBB 026 / #63 unchanged failure;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md` → CYCLE 027;
- `!!!PLAN/NOCHE - AAA.md` → `NIGHT-AAA-027`;
- `!!!PLAN/NOCHE - BBB.md` → `NIGHT-BBB-026`;
- `!!!PLAN/NOCHE - WOZ.md` → `NIGHT-WOZ-026` + processed WOZ 025;
- `!!!PLAN/NOCHE - JOBS.md` → CYCLE 027.

`Registro de avances.md` fue leído completo; no se añade entrada porque este ciclo no produjo nuevo merge/PASS de gate. F0/F1 no se modifican: no existe evidencia nueva de sus tails externos. JOBS no modificó código BeatGaler ni infraestructura. `Plan Maestro 2208 copy DONT TOUCH .md` no fue tocado.

## SIGUIENTE CICLO

1. Releer integration HEAD antes de claims.
2. Procesar resultados AAA 027 / BBB 026 / WOZ 026 una sola vez.
3. Si algún candidate mueve integration, revalidar base/head/CI de #63/#68 antes de cualquier integración futura.
4. #68: no retry ceremonial; solo reabrir transacción si existe capacidad autorizada de merge y entonces race-check exacto.
5. BBB: Windows Import literal PASS obligatorio; no green genérico.
6. Mantener 12.1 abierto hasta runtime cold/warm real.
7. No abrir F5 hasta condiciones reales F0–F4.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-027
INTEGRATION_HEAD_OBSERVED: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af
AAA_026: NOT_PROCESSED -> superseded
BBB_025: NOT_PROCESSED -> superseded; #63 failure unchanged
WOZ_025: BLOCKED / MERGE_TOOL_REJECTED -> processed; #68 frozen
AAA_NEW: NIGHT-AAA-027 ASSIGNED F2/13.1 Web-only
BBB_NEW: NIGHT-BBB-026 ASSIGNED SAME #63 launcher/session corrective
WOZ_NEW: NIGHT-WOZ-026 ASSIGNED F2/13.1 server half
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 027 completado. El próximo ciclo parte de GitHub vivo y de los resultados de `NIGHT-AAA-027`, `NIGHT-BBB-026` y `NIGHT-WOZ-026`.
