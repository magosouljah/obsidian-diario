# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.  
**Ciclo:** `CYCLE 096`.

## BASELINE VIVO

- Final preflight baseline: `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- PR #79 sigue siendo el último merge material; F4/25.2 docs-only readiness artifact.
- #83 sigue `OPEN/DRAFT`, merged=false, mergeable=true, exact base `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`; exact-head CI permanece green. Supported Draft→Ready path sin cambio material verificado desde blocker `Repository.fullDatabaseId`; no se repite ni se bypassa.
- #74 sigue `OPEN/Ready/mergeable` @ `d1593d368e1015abb6a25bf98e5fa8586664ac95`, base live integration.
- #84 sigue `OPEN/Ready/mergeable` @ `c6c5ecb17e1efd055cb9a8f2bc42105ef3838d61`, base live integration.
- #84 literal Windows Auth Journey run `33423712589`, job `99592060690` = FAILURE. Exact job reaches `Run isolated Windows auth assertions` after all setup steps pass; literal failure remains `Desktop login did not persist the returned session token.`
- Release público: 🔴 `NO-GO`; F5 `NO ABRIR`.

## PREFLIGHT / RESULTADOS PROCESADOS

Leído para este ciclo: Plan Maestro; F0–F4 completos; Equipo; protocolo nocturno; JOBS/AAA/BBB/WOZ completos; Registro de avances; Issue #41 completo mediante paginated connector fetch; integración viva; open PR scan; #74/#83/#84 live state y exact workflow evidence. GitHub/runtime prevalece sobre texto viejo.

- `NIGHT-AAA-091`: no final RESULTADO DEL TURNO, no matching material Issue #41 handoff y no nuevo F2/13.2 candidate. `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-090`: no final RESULTADO DEL TURNO, no matching material handoff y no movimiento de #74/#84. `NO_RESULT / SUPERSEDED / NOT_PASS`; literal Windows Auth sigue RED.
- `NIGHT-WOZ-094`: final `BLOCKED_STOP / F2-15.1 EMPTY_TRASH_AUDIT`. Existing purge architecture reused. Beat Empty Trash lacks strong confirmation; visible rows are cleared optimistically before purge completion; `PlatformTrashPort` has no recent-reauth seam; satisfying recent reauth requires auth/session implementation outside WOZ authority. No changes/PR/tests/CI; Issue #41 `5483612373`.
- Duplicate-check: #83 sigue único durable-waitlist candidate; #74/#84 única current windows-auth lineage; no new F2/13.2 candidate; no current Trash candidate. #69/#70/#81/#76/#72 remain frozen/parked.

## CAMINO CRÍTICO GLOBAL — RECALCULADO CYCLE 096

1. **F4/25.1 windows/auth:** current exact #74/#84 red → extract first causal boundary from run `33423712589` / job `99592060690` → minimum corrective → literal packaged Windows proof.
2. **F2/13.2 Review Save/Save All:** durable completion/no-silent-loss correction + executable Web/Tauri call-spy evidence.
3. **F2/15.1 Empty Trash:** auth/session owner must expose/reuse a bounded recent-reauth seam; only then minimum strong-confirmation + recent-reauth + deterministic non-optimistic purge wiring/tests.
4. **F3/20.2 #83:** blocked on supported Draft→Ready tooling. No repeat until path changes materially; no bypass.
5. **F3/20.2 after #83 integration:** materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin vs expected 80.
6. **F2/12.1:** real-browser cold/warm evidence requires executable checkout + Node/npm + Chrome/WebDriver surface.
7. **F3/19.1 + F0/F1/F4 tails:** external DNS/TLS/API/OAuth/sender/deployment, off-provider backup, signing/notarization/hardware/tester execution and RO decisions.
8. Frozen stale candidates #81/#76/#72 only after explicit safe reconciliation.

## ASIGNACIONES EMITIDAS

| Worker | PRIMARY | CI-FALLBACK |
|---|---|---|
| AAA | `NIGHT-AAA-092` — F2/13.2 minimum durable Review Save/Save All action-boundary corrective; saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; **NO MERGE** | `NONE` — browser timing surface unavailable; other useful F2 work overlaps/widens scope |
| BBB | `NIGHT-BBB-091` — F4/25.1 current #74/#84 first-causal-boundary attribution from exact failed run/job; only then minimum attributable platform/session corrective, history-preserving #84 refresh and literal token persistence + AccountGate exit with fresh exact-head CI; **NO MERGE** | `NONE` — secondary F4 work shares ownership or requires external signing/hardware/tester evidence; Trash reauth seam is not opportunistic scope |
| WOZ | `NIGHT-WOZ-095` — F3/19.1 public production-surface evidence **READ-ONLY**; verify current DNS/TLS/HTTP/status/support/security-abuse/publicly observable sender/OAuth facts; private/provider facts UNVERIFIED; no mutations | `NONE` — PRIMARY is read-only/no CI; #83/12.1/Trash remain blocked on separate material dependencies |

Ownership is distinct. **INTEGRATION_MUTATION: NONE for CYCLE 096.**

## PROGRESO F0–F4 / BLOCKERS

- **F0:** technical core closed; 1.2/2.2 external/admin tails remain.
- **F1:** D6–D9 PASS; D10.1 real off-provider/off-account proof pending; D10.2 RO decision.
- **F2:** 11.1/11.2/12.2 closed; 12.1 runtime execution-surface-blocked; 13.1 frozen; 13.2 durable Review gap = AAA092; 14.1 #81 parked; 15.1 destructive Empty Trash now factually blocked on missing reusable recent-reauth seam plus confirmation/action-boundary correction; no implementation owner this cycle; remaining 14.x/15.x/YouTube/a11y work open.
- **F3:** 17.1/17.2/18.1 closed; 18.2 global open; 19.1 public external evidence = WOZ095 READ-ONLY; 20.1 software integrated; #83 exact/green but Draft/tooling-blocked; runtime 160 remains required after eventual integration.
- **F4:** 21.1/21.2/24.1/24.2 closed; #79 readiness artifact integrated; 25.1 literal current Windows Auth remains RED, BBB091 owns bounded causal/corrective/evidence transaction; signing/notarization/hardware/testers external.
- **F5:** CLOSED / NO ABRIR.

## PLAN SYNC / NEXT

CYCLE 096 assignments written to `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - WOZ.md`. Plan Maestro, roles, F2, F3 and F4 synchronized to live state. No new BeatGaler merge/PASS occurred, so `Registro de avances.md` receives no ceremonial entry. `Plan Maestro 2208 copy DONT TOUCH .md` untouched. JOBS changed no BeatGaler code or infrastructure.

Next cycle: begin from live GitHub. Promote no F4 claim while literal Windows auth is red. Do not reassign Trash implementation until a bounded recent-reauth seam is available under correct auth/session ownership. Re-open #83 only if the supported Ready path has a material verified change.

```text
CYCLE_ID: NIGHT-JOBS-096
INTEGRATION_HEAD_FINAL_PREFLIGHT: 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA_RESULT_PROCESSED: NIGHT-AAA-091 NO_RESULT / SUPERSEDED / NOT_PASS
BBB_RESULT_PROCESSED: NIGHT-BBB-090 NO_RESULT / SUPERSEDED / NOT_PASS
WOZ_RESULT_PROCESSED: NIGHT-WOZ-094 BLOCKED_STOP / F2-15.1 EMPTY_TRASH_AUDIT
AAA_NEW: NIGHT-AAA-092
BBB_NEW: NIGHT-BBB-091
WOZ_NEW: NIGHT-WOZ-095
INTEGRATION_MUTATION_AUTHORIZED: NONE
DUPLICATE_WORK: prevented
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
F5: CLOSED
```

**STOP:** ciclo JOBS 096 terminado.
