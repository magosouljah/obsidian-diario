# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 075`.

## BASELINE VIVO

- Final race-check: `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- #82 sigue siendo el último merge material observado; parents `5e117d69...` + `eb817223...`.
- PR #79 está preparado sobre ese baseline a exact head `a3c4d56e8317d7711832154ecc72afe581d2b309`; no se reclama merge en este ciclo JOBS.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro; Issue #41 y GitHub vivo. GitHub/runtime prevalece.

- `NIGHT-AAA-070`: `PENDING / STOP_HISTORY_RECONCILE_UNAVAILABLE`. #81 quedó OPEN @ `709151082...`, no mutation/no merge. Compare contra live: 4 ahead / 13 behind, dos paths materiales. La CI previa es stale. El handoff del worker no pudo publicarse; JOBS lo replicó en Issue #41 comment `5475866952`.
- `NIGHT-BBB-069`: `WAITING_CI`. Reutilizó SAME #79 y lo reconcilió history-preservingly a `a3c4d56e...` sobre live `957f9777...`; behind=0, exactamente un archivo docs-only. Fallback F4/25.1 read-only completado; Windows playback quedó como menor journey futuro no-frozen.
- Post-handoff BBB: JOBS verificó check-runs exact-head de `a3c4d56e...`: `Required CI = SUCCESS`; no se observaron checks exact-head `in_progress` ni `failure`. Upgrade 21.2 staging sigue `SKIPPED`/no aplicable. Esto habilita race-check final del owner, no un merge claim de JOBS.
- `NIGHT-WOZ-073`: sin RESULTADO DEL TURNO/handoff nuevo antes del ciclo; superseded por WOZ074 después de recalcular desde cero, no por PASS.
- Duplicate-check: #78 ya contiene harness/capacity software; Issue #41 sigue registrando durable user waitlist como GAP y la búsqueda repo actual no encontró implementación separada equivalente.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 075

1. F4/25.2 #79: exact-head green candidate; queda una transacción final serializada y factual.
2. F3/20.2 durable waitlist: cerrar el gap interno más claro sin mezclarlo con runtime capacity.
3. F2/13.2: auditoría Web boundary/silent-loss para determinar el siguiente write slice sin reactivar frozen work a ciegas.
4. F3/20.2: runtime aplicable 160 + latency/error/queue/recovery + safety margin medida.
5. F2/14.1 #81: abierto pero aparcado por falta de superficie segura de history-preserving reconciliation.
6. F2/12.1: cold/warm Web en browser real.
7. F3/19.x #76 y F2/13.1 #69/#70: aparcados/frozen hasta cambio factual de blocker.
8. F4/25.1 journeys restantes; signing/notarization/hardware externos.
9. F0/F1 y provider/legal/operational tails externos/RO.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-071` — F2/13.2 READ-ONLY audit de Web-visible action boundary + silent-loss sobre live baseline; sin writes ni #81/#69/#70 | `NONE` |
| BBB | `NIGHT-BBB-070` — SAME #79 final race-check; si integration/base/head/delta/CI siguen exactos, expected-head merge y verificación de merge SHA + parents | `NONE` |
| WOZ | `NIGHT-WOZ-074` — F3/20.2 minimal durable user-waitlist persistence/recovery/isolation + tests + fresh CI; **NO MERGE** | F3/18.2 READ-ONLY billing scenario evidence map solo durante genuine WAITING_CI/review |

Ownership: AAA=F2/13.2 audit; BBB=#79/F4; WOZ=F3/20.2 durable waitlist. Solo BBB/#79 puede mutar integration. Si #79 integra, cualquier candidate posterior necesita reconciliación/fresh evidence contra el nuevo baseline.

## PRIMARY / CI-FALLBACK EMITIDOS — CONDICIONES

- **AAA071 fallback:** NONE; PRIMARY es read-only y no debe fabricar una espera CI.
- **BBB070 fallback:** NONE; BBB069 ya consumió el único audit fallback útil. STOP ante race, CI no-green, scope drift, expected-head mismatch o merge-flow reject.
- **WOZ074 fallback:** solo si PRIMARY queda code-complete en WAITING_CI/review. Scope F3/18.2 live read-only, sin writes/provider calls; evidencia scenario→code/test/provider-proof + GAP classification; STOP ante cualquier provider mutation, overlap o cuando PRIMARY deje de esperar.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** núcleo técnico cerrado; 1.2 release governance/dependencias externas y 2.2 GitHub-side cleanup verification siguen abiertos administrativamente.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account copy + read/checksum real; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 runtime real abierto; 13.1 frozen; 13.2 ahora activo AAA071; 14.1 #81 abierto/aparcado; 14.2/15.x pendientes.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 19.x #76 aparcado; 20.1 software integrado; 20.2 activo en dos capas: waitlist interno WOZ074 + runtime 160/safety margin todavía sin evidencia.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto; #79 está exact-head green pero no integrado todavía; beta/testers/signing/notarization reales siguen externos.
- **F5:** cerrado/no abrir.

## PLAN SYNC / ISSUE #41 / NEXT

Actualizados en `obsidian-diario/main`: `NOCHE - AAA.md` → AAA071; `NOCHE - BBB.md` → BBB070; `NOCHE - WOZ.md` → WOZ074; `Plan Maestro.md` → CYCLE 075; `Equipo multi-IA - Roles y coordinación.md` → CYCLE 075; este `NOCHE - JOBS.md` → CYCLE 075. F0/F1/Registro fueron leídos pero no se promovió ningún gate nuevo. `Plan Maestro 2208 copy DONT TOUCH .md` untouched.

Issue #41 actualizado con handoff JOBS CYCLE 075: comment `5475866952`, incluyendo el resultado AAA070 que el worker no pudo publicar.

Siguiente ciclo: leer integration primero. Si BBB070 integra #79, registrar el nuevo SHA/parents y tratar cualquier head/base previo como stale. Procesar AAA071/BBB070/WOZ074 solo con evidencia real. Mantener F3/20.2 runtime, F2/12.1 y tails externos abiertos hasta prueba literal. No abrir F5.

```text
CYCLE_ID: NIGHT-JOBS-075
INTEGRATION_HEAD_FINAL_RACECHECK: 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA_RESULT_PROCESSED: NIGHT-AAA-070 PENDING / STOP_HISTORY_RECONCILE_UNAVAILABLE
BBB_RESULT_PROCESSED: NIGHT-BBB-069 WAITING_CI; JOBS_POSTCHECK_CI=GREEN
WOZ_RESULT_PROCESSED: NIGHT-WOZ-073 NO_RESULT / SUPERSEDED_BY_JOBS
AAA_NEW: NIGHT-AAA-071
BBB_NEW: NIGHT-BBB-070
WOZ_NEW: NIGHT-WOZ-074
ONLY_INTEGRATION_MUTATION_AUTHORIZED: BBB / #79
ISSUE41_HANDOFF: 5475866952
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 075 terminado.
