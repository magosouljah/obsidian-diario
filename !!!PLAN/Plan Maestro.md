# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## Reglas de autoridad

- GitHub/runtime vivo prevalece sobre snapshots viejos.
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Cada pieza material tiene un solo owner.
- JOBS dirige/sincroniza; no modifica código BeatGaler ni infraestructura.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-090

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime abierto y ahora owned READ-ONLY por `NIGHT-WOZ-089`. 13.1 frozen. 13.2 conserva brecha factual Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-086` owns the minimum corrective candidate; NO MERGE. 14.1 #81 parked/stale.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. 19.1 reducido a blockers externos. PR #83 sigue OPEN/DRAFT, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green, pero `NIGHT-WOZ-088` terminó BLOCKED_STOP porque el Draft→Ready dedicado volvió a fallar por connector `Repository.fullDatabaseId`. #83 queda PARKED/TOOLING_BLOCKED; runtime 160 remains UNVERIFIED.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #84 exact-lineage harness-only permanece `d13a1969...`; Required CI `33407580663` SUCCESS pero literal Windows auth `33407580887` / job `99538870371` FAILURE. `NIGHT-BBB-085` owns bounded failure attribution/correction; NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 090

- `NIGHT-AAA-085`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching final ledger result or material Issue #41 handoff.
- `NIGHT-BBB-084`: `NO_RESULT / SUPERSEDED / NOT_PASS`; #84 remains unchanged and literal auth journey remains red.
- `NIGHT-WOZ-088`: `BLOCKED_STOP`; dedicated #83 Draft→Ready action failed; no bypass, no merge, exact candidate preserved. Issue #41 `5481554738`.
- No BeatGaler merge or PASS claim in this JOBS cycle; baseline unchanged.

## OWNERS — CYCLE 090

### AAA — `NIGHT-AAA-086` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-085` — F4 / 25.1 windows/auth
PRIMARY: keep #84 as sole candidate; diagnose exact auth-assertion failure. If harness/workflow-only, minimally correct #84 and rerun exact-head literal Windows auth. If product #74 is implicated, STOP/report; no product widening. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-089` — F2 / 12.1 runtime evidence
PRIMARY: READ-ONLY real-browser cold/warm startup evidence on exact live integration using existing canonical Web smoke/runtime path. Capture exact SHA, browser/runtime/build identity, timings and limitations. No code/PR/infra/integration mutation.  
CI-FALLBACK: NONE.

## Camino crítico global — CYCLE 090

1. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
2. F4/25.1 #84 exact Windows auth failure attribution and bounded correction/evidence.
3. F2/12.1 real-browser cold/warm evidence.
4. F3/20.2 unblock #83 Draft→Ready with a real tooling/human path; do not repeat the same failing connector transaction.
5. F3/20.2 post-#83 materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
6. F3/19.1 external canonical hostname/API/DNS/TLS/status/OAuth/sender/deployment facts.
7. F2/14.1 #81, F3/19.2 #76 and F4/#72 stay frozen until safe explicit reconciliation.
8. F4 signing/notarization/hardware/tester execution; F0/F1 provider/legal/operational tails remain external/RO blockers.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation details hidden.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud does not relay beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no free bot; exclusivity per vault is normal path.
- v1 is not published free-only.
- YouTube exists Desktop/Web; Web does not call Tauri.

## NEXT

AAA executes `NIGHT-AAA-086`; BBB executes `NIGHT-BBB-085`; WOZ executes `NIGHT-WOZ-089`. No worker may mutate integration in CYCLE 090. Next JOBS cycle starts from live integration and exact handoffs only. `PLAN_HEALTH`: synced CYCLE 090; GitHub live prevails if it moves afterward.
