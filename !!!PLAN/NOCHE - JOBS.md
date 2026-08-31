# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 079`.

## BASELINE VIVO

- Final preflight baseline: `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- PR #82 sigue siendo el último merge material observado; parents `5e117d69...` + `eb817223...`.
- PR #79: OPEN/non-draft, exact base live `957f9777...`, head `a3c4d56e8317d7711832154ecc72afe581d2b309`; changed files = solo `docs/beta/0.9.0-beta.1-readiness.md`; Required CI exact-head COMPLETED/SUCCESS. No merge claim en este ciclo JOBS.
- PR #83: draft/open, exact base live `957f9777...`, head `52b58f56d66430db1ecdce9f572680c61d5d9fe3`; changed files = `.github/workflows/f3-20.2-durable-waitlist.yml`, `cloud-server/durable-user-waitlist.js`, `cloud-server/tests/durable-user-waitlist.test.cjs`; Required CI exact-head COMPLETED/SUCCESS. No readiness/merge claim nuevo en este ciclo JOBS.
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leídos completos: Plan Maestro; F0–F4; Equipo; protocolo; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 completo; GitHub vivo para integration y candidates críticos. GitHub/runtime prevalece.

- `NIGHT-AAA-074`: no RESULTADO DEL TURNO ni handoff nuevo antes de CYCLE 079. Se supersede, no PASS. Duplicate-check detectó que `NIGHT-AAA-071` ya había completado la auditoría F2/13.2: no repetirla. AAA071 dejó un gap concreto y accionable: falta executable Web-visible Tauri/Desktop call-spy coverage y Save All conserva una brecha plausible de partial-failure/conflict summary + retry/no-silent-loss.
- `NIGHT-BBB-073`: no RESULTADO DEL TURNO ni handoff nuevo. GitHub real conserva #79 exacto y verde; se emite BBB074 por ser la transacción serializada de mayor valor.
- `NIGHT-WOZ-077`: no RESULTADO DEL TURNO ni handoff nuevo. GitHub real conserva #83 draft/open sobre exact base/head con Required CI exact-head verde; se emite WOZ078 para SAME #83 sin merge.
- Duplicate-check: #78 ya posee capacity harness; #83 solo durable waitlist; #79 solo docs F4; AAA075 se deriva del finding AAA071 y no toca #69/#70/#81. Ownership sin overlap material.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 079

1. F4/25.2 #79: final exact integration transaction BBB074.
2. F3/20.2 #83: readiness/reconcile sin carrera con #79; si #79 mueve integration, history-preserving refresh + fresh exact-head CI.
3. F2/13.2: convertir finding AAA071 en executable evidence y, solo si el test lo demuestra, corregir el menor gap F2.
4. F3/20.2: posteriormente integrar durable waitlist y completar runtime aplicable 160 + latency/error/queue/recovery + measured safety margin.
5. F2/14.1 #81: parked hasta superficie segura de reconciliation.
6. F2/12.1: real-browser cold/warm evidence.
7. F3/19.x #76 y F2/13.1 #69/#70: frozen/parked hasta cambio factual.
8. F4/25.1 journeys restantes + signing/notarization/hardware external.
9. F0/F1 y provider/legal/operational external tails.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-075` — F2/13.2: REUSE AAA071; mínimo browser/component journey con Tauri/Desktop `invoke`/`listen` call-spies + Save All partial-failure/conflict/retry/no-silent-loss; solo fix F2 mínimo si test falla; fresh CI; NO MERGE | `NONE` |
| BBB | `NIGHT-BBB-074` — SAME #79 final exact race-check; si integration/base/head/file-delta/CI siguen exactos, expected-head merge + verify merge SHA/parents | `NONE` |
| WOZ | `NIGHT-WOZ-078` — SAME #83 readiness/reconcile; si #79 movió integration, history-preserving reconcile #83 + fresh exact-head CI; **NO MERGE** | F3/19.1 READ-ONLY deployment/domain evidence map solo si PRIMARY entra genuinamente en WAITING_CI tras un fresh/reconciled head |

Ownership distinto: AAA=F2 evidence/fix slice, BBB=#79/F4, WOZ=#83/F3. Solo BBB/#79 puede mutar integration en CYCLE 079.

## PRIMARY / CI-FALLBACK — CONDICIONES

- **AAA075 fallback:** NONE. STOP si la evidencia requiere tocar #69/#70/#81, redesign material, provider credential/runtime externo o overlap.
- **BBB074 fallback:** NONE. STOP ante cualquier race, scope drift, CI no verde/concluido, expected-head mismatch o rechazo del merge flow.
- **WOZ078 fallback:** únicamente si PRIMARY ya estableció un head fresh/reconciled y está realmente `WAITING_CI`. Scope read-only F3/19.1: public domain/API/status/support URLs, DNS/TLS, redirects/callbacks, sender domains. Evidence PASS/GAP/UNVERIFIED + menor acción externa. STOP ante provider mutation/credential, overlap, unsafe visibility o cuando PRIMARY CI termine. No cierra 19.1.

## PROGRESO F0–F4 / BLOCKERS

- **F0:** technical core closed; 1.2 external release governance y 2.2 GitHub-side cleanup verification siguen administrativos/externos.
- **F1:** D6–D9 PASS; D10.1 requiere real off-provider/off-account copy + read/checksum; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 closed; 12.1 real-browser runtime open; 13.1 frozen; 13.2 audit consumido y AAA075 trabaja evidence/fix mínimo; 14.1 #81 parked/stale; 14.2/15.x pending.
- **F3:** 17.1/17.2/18.1 closed; 18.2 global open; 19.x #76 parked; 20.1 software integrated; 20.2 #83 durable waitlist candidate draft/not integrated, exact-head CI green, más real 160/safety-margin evidence missing.
- **F4:** 21.1/21.2 y 24.1/24.2 closed; 25.1 incomplete; #79 exact + green owned BBB074; tester/signing/notarization evidence external.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC / NEXT

Updated on `obsidian-diario/main`: `NOCHE - AAA.md` → AAA075; `NOCHE - BBB.md` → BBB074; `NOCHE - WOZ.md` → WOZ078; `Fase 2 - Web y UX.md` consumed AAA071 and now records the executable 13.2 gap; `Plan Maestro.md` → CYCLE 079; `Equipo multi-IA - Roles y coordinación.md` → CYCLE 079; this file → CYCLE 079. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. `Registro de avances.md` was read completely; no new integration/PASS/runtime evidence justified adding a product-advance entry in this cycle. JOBS changed no BeatGaler code or infrastructure.

Next cycle: read integration first. If BBB074 merges #79, record new merge SHA/parents and require #83 reconciliation + fresh exact-head evidence before any readiness/integration claim. Process AAA075/BBB074/WOZ078 only with verifiable results/handoffs. Keep F3/20.2 runtime, F2/12.1 and external tails open until literal proof.

```text
CYCLE_ID: NIGHT-JOBS-079
INTEGRATION_HEAD_FINAL_PREFLIGHT: 957f97771b7a15554cf6e002fe9eb215c71a65cc
AAA_RESULT_PROCESSED: NIGHT-AAA-074 NO_RESULT / SUPERSEDED_BY_JOBS
AAA_REUSED_EVIDENCE: NIGHT-AAA-071 DONE_AUDIT_ONLY
BBB_RESULT_PROCESSED: NIGHT-BBB-073 NO_RESULT / SUPERSEDED_BY_JOBS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-077 NO_RESULT / SUPERSEDED_BY_JOBS
AAA_NEW: NIGHT-AAA-075
BBB_NEW: NIGHT-BBB-074
WOZ_NEW: NIGHT-WOZ-078
ONLY_INTEGRATION_MUTATION_AUTHORIZED: BBB / #79
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 079 terminado.
