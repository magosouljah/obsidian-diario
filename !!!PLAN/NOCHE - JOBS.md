# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 074`.

## BASELINE VIVO

- `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- GitHub live confirma que #82 sigue siendo el último merge material observado en integration; parents `5e117d69...` + `eb817223...`.
- #79, #81 y #76 siguen OPEN/non-draft/mergeable sobre bases stale; ningún resultado nuevo justificó promover gate o merge.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro; Issue #41; GitHub vivo. GitHub/runtime prevalece.

- `NIGHT-AAA-069`: no RESULTADO DEL TURNO ni handoff nuevo visible antes del ciclo; #81 sigue `709151082...`, base PR `5e117d69...` vs live `957f9777...`. Superseded por nueva orden, no por PASS.
- `NIGHT-BBB-068`: no RESULTADO DEL TURNO ni handoff nuevo visible; #79 sigue `60c2fb54...`, base PR `5e117d69...` vs live `957f9777...`. Superseded por nueva orden, no por PASS.
- `NIGHT-WOZ-072`: no RESULTADO DEL TURNO ni handoff nuevo visible; #76 sigue `36d21860...`, base PR `a9d35a3...` vs live `957f9777...`. Superseded por nueva orden, no por PASS.
- Duplicate-check: no PR nuevo necesario para ninguno; REUSE-FIRST conserva #81/#79/#76.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 074

1. F4/25.2 #79: docs-only candidate, refresh exacto + fresh CI + única posible integración serializada.
2. F2/14.1 #81: memory-safety bounded candidate, reconcile + exact-head CI; no merge este ciclo.
3. F3/19.1 #76: legal canonical in-app consistency candidate, reconcile + exact-head CI; no merge este ciclo.
4. F3/20.2: falta runtime aplicable 160 + latency/error/queue/recovery + safety margin + durable user waitlist.
5. F2/12.1: cold/warm Web en browser real.
6. F2/13.1 #69/#70: frozen hasta cambio factual de write-surface blocker.
7. F4/25.1: auth/review y journeys restantes; signing/notarization/hardware externos.
8. F0/F1: tails externos/RO permanecen; no falsificar cierre.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-070` — SAME #81; history-preserving reconcile a `957f9777...`; mínimo memory-safety slice + tests; fresh exact-head CI; **NO MERGE** | F2/12.1 READ-ONLY startup readiness map solo durante genuine WAITING_CI/review |
| BBB | `NIGHT-BBB-069` — SAME #79; refresh a `957f9777...`; docs-only proof; fresh exact-head CI; final race-check; única posible merge transaction | F4/25.1 READ-ONLY matrix gap map durante genuine WAITING_CI/merge wait |
| WOZ | `NIGHT-WOZ-073` — SAME #76; reconcile a `957f9777...`; canonical Settings legal wiring + tests + fresh exact-head CI; **NO MERGE** | `NONE` |

Ownership: AAA=#81/F2; BBB=#79/F4; WOZ=#76/F3. Solo BBB/#79 puede mutar integration en CYCLE 074. Si integration cambia, #81/#76 requieren nueva reconciliation + CI antes de cualquier integración futura.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** núcleo técnico cerrado; 1.2 release governance/external dependencies y 2.2 GitHub-side cleanup verification siguen abiertos administrativamente.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account copy + read/checksum real; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 runtime real abierto; 13.1 frozen; 14.1 activo #81; 14.2/15.x pendientes.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 19.1 candidato #76; 20.1 software integrado; 20.2 runtime/waitlist bloqueante.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto; 25.2 artifact #79 pendiente; beta/testers/signing/notarization reales siguen externos.
- **F5:** cerrado/no abrir.

## PLAN SYNC / NEXT

Actualizados: `NOCHE - AAA.md` → AAA070; `NOCHE - BBB.md` → BBB069; `NOCHE - WOZ.md` → WOZ073; este `NOCHE - JOBS.md` → CYCLE 074. No se modificó código BeatGaler ni infraestructura.

Siguiente ciclo: revalidar integration primero; procesar AAA070/BBB069/WOZ073 una sola vez; si #79 integra, invalidar bases exactas de #81/#76; mantener 20.2 y 12.1 abiertos hasta evidencia runtime aplicable; no abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-074
INTEGRATION_HEAD: 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA_RESULT_PROCESSED: NIGHT-AAA-069 NO_RESULT / SUPERSEDED_BY_JOBS
BBB_RESULT_PROCESSED: NIGHT-BBB-068 NO_RESULT / SUPERSEDED_BY_JOBS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-072 NO_RESULT / SUPERSEDED_BY_JOBS
AAA_NEW: NIGHT-AAA-070
BBB_NEW: NIGHT-BBB-069
WOZ_NEW: NIGHT-WOZ-073
ONLY_INTEGRATION_MUTATION_AUTHORIZED: BBB / #79
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 074 terminado.
