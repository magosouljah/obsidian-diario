# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 094`.

## BASELINE VIVO

- Final preflight baseline: `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- PR #79 sigue siendo el último merge material; F4/25.2 docs-only readiness artifact.
- #83 sigue `OPEN/DRAFT`, merged=false, mergeable=true, exact base `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`, 3 archivos; exact-head Required CI permanece SUCCESS.
- WOZ092 ejecutó únicamente la acción dedicada soportada Draft→Ready. Falló dentro del conector con `GithubGraphQLAPIError` por `Repository.fullDatabaseId` undefined; postcheck inmediato confirmó #83 sin cambio. No workaround/bypass, no merge.
- #74 sigue `OPEN/Ready/mergeable` @ `d1593d368e1015abb6a25bf98e5fa8586664ac95`, base live integration.
- #84 sigue `OPEN/Ready/mergeable` @ `c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61`, base live integration; contiene current #74.
- #84 exact-head Required CI / Desktop Portability `33423712599` = SUCCESS; literal Windows Auth Journey `33423712589` / job `99592060690` = FAILURE at `tests/e2e/auth-flow.e2e.mjs:64`: `Desktop login did not persist the returned session token.`
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leído para este ciclo: Plan Maestro; F0–F4; Equipo; protocolo nocturno; JOBS/AAA/BBB/WOZ; Registro de avances; Issue #41 body + comentarios completos; integración viva; open PR scan; #74/#83/#84 live state y exact checks. GitHub/runtime prevalece sobre texto viejo.

- `NIGHT-AAA-089`: no final RESULTADO DEL TURNO, no matching material Issue #41 handoff y no nuevo F2/13.2 candidate. `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-088`: no final RESULTADO DEL TURNO, no matching material handoff y no movimiento posterior de #74/#84 respecto al estado ya procesado. `NO_RESULT / SUPERSEDED / NOT_PASS`; literal Windows Auth sigue RED.
- `NIGHT-WOZ-092`: `BLOCKED_STOP / TOOLING_EXTERNAL`. Exact #83 unchanged after supported Ready action failed; Issue #41 `5482892475`. No integration mutation.
- Duplicate-check: #83 sigue único durable-waitlist candidate; #74/#84 única lineage windows-auth actual; no open PR de Trash/Empty Trash; #69/#70/#81/#76/#72 siguen frozen/parked según ownership actual.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 094

1. **F4/25.1 windows/auth:** current exact #74/#84 red → first-causal-boundary attribution → mínimo corrective → literal packaged Windows proof.
2. **F2/13.2 Review Save/Save All:** durable completion/no-silent-loss correction + executable Web/Tauri call-spy evidence.
3. **F2/15.1 Empty Trash:** audit current existing purge path → mínimo strong-confirmation/recent-reauth/no-false-success correction only if gap literal exists.
4. **F3/20.2 #83:** blocked on supported Draft→Ready tooling. No repeat until path changes materially; no bypass.
5. **F3/20.2 after #83 integration:** materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin vs expected 80.
6. **F2/12.1:** real-browser cold/warm evidence requires executable checkout + Node/npm + Chrome/WebDriver surface.
7. **F3/19.1 + F0/F1/F4 tails:** external DNS/TLS/API/OAuth/sender/deployment, off-provider backup, signing/notarization/hardware/tester execution and RO decisions.
8. Frozen stale candidates #81/#76/#72 only after explicit safe reconciliation.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-090` — F2/13.2 minimum durable Review Save/Save All action-boundary corrective; saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; **NO MERGE** | `NONE` — browser timing surface unavailable; other useful F2 work overlaps/fattens scope |
| BBB | `NIGHT-BBB-089` — F4/25.1 current #74/#84 first-causal-boundary attribution; only then minimum attributable platform/session corrective, history-preserving #84 refresh and literal token persistence + AccountGate exit with fresh exact-head CI; **NO MERGE** | `NONE` — secondary F4 mutations share release-chain ownership; signing/hardware needs external evidence |
| WOZ | `NIGHT-WOZ-093` — F2/15.1 audit-first Empty Trash destructive-action subgate using existing Trash/recent-reauth APIs; minimum bounded confirmation/reauth/no-false-success correction only if proven missing; auth/legal/server excluded; **NO MERGE** | `NONE` — #83 remains verified tooling-blocked and runtime 160 depends on its integration; no safe independent fallback |

Ownership is distinct. **INTEGRATION_MUTATION: NONE for CYCLE 094.**

## PROGRESO F0–F4 / BLOCKERS

- **F0:** technical core closed; 1.2/2.2 external/admin tails remain.
- **F1:** D6–D9 PASS; D10.1 real off-provider/off-account proof pending; D10.2 RO decision.
- **F2:** 11.1/11.2/12.2 closed; 12.1 runtime execution-surface-blocked; 13.1 frozen; 13.2 durable Review gap = AAA090; 14.1 #81 parked; 15.1 destructive Empty Trash subgate = WOZ093; remaining 14.x/15.x/YouTube/a11y work still open.
- **F3:** 17.1/17.2/18.1 closed; 18.2 global open; 19.1 external/provider facts; 20.1 software integrated; #83 exact/green but Draft and now explicitly tooling-blocked after supported action failure; runtime 160 remains required after eventual integration.
- **F4:** 21.1/21.2/24.1/24.2 closed; #79 readiness artifact integrated; 25.1 literal current Windows Auth remains RED, BBB089 owns bounded causal/corrective/evidence transaction; signing/notarization/hardware/testers external.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC / NEXT

CYCLE 094 assignments written to `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - WOZ.md`. Plan Maestro, roles, F2, F3 and F4 synchronized to live state. No new BeatGaler merge/PASS occurred, so `Registro de avances.md` receives no ceremonial entry. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS changed no BeatGaler code or infrastructure.

Next cycle: begin from live GitHub, not these snapshots. If #83 supported Ready path is repaired or replaced by a newly supported authorized action, re-evaluate it from scratch; otherwise do not burn another worker turn on the same connector error. Promote no F4 claim while literal Windows auth is red; promote no F2/15.1 claim from UI inspection without destructive/recent-reauth evidence.

```text
CYCLE_ID: NIGHT-JOBS-094
INTEGRATION_HEAD_FINAL_PREFLIGHT: 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA_RESULT_PROCESSED: NIGHT-AAA-089 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-088 NO_RESULT / SUPERSEDED / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-092 BLOCKED_STOP / SUPPORTED_READY_CONNECTOR_FAILURE
AAA_NEW: NIGHT-AAA-090
BBB_NEW: NIGHT-BBB-089
WOZ_NEW: NIGHT-WOZ-093
INTEGRATION_MUTATION_AUTHORIZED: NONE
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 094 terminado.
