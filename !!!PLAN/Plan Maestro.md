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

## Estado vivo — NIGHT-JOBS-091

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime abierto y owned READ-ONLY por `NIGHT-WOZ-090`. 13.1 frozen. 13.2 conserva brecha factual Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-087` owns the minimum corrective candidate; NO MERGE. 14.1 #81 parked/stale.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. 19.1 reducido a blockers externos. PR #83 sigue OPEN/DRAFT, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green, pero el último Draft→Ready dedicado falló por connector `Repository.fullDatabaseId`. #83 queda PARKED/TOOLING_BLOCKED; runtime 160 remains UNVERIFIED.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #84 exact-lineage permanece `d13a1969...`; Required CI `33407580663` SUCCESS pero literal Windows auth `33407580887` / job `99538870371` FAILURE. `NIGHT-BBB-085` verified the failing assertion is product-facing: `Desktop login did not persist the returned session token.` `NIGHT-BBB-086` now exclusively owns the minimum #74/#84 product-auth corrective/evidence lineage; NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 091

- `NIGHT-AAA-086`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching final ledger result or material Issue #41 handoff.
- `NIGHT-BBB-085`: `BLOCKED_STOP / PRODUCT_LOGIC_IMPLICATED`; exact packaged Windows auth reached the real test and failed on session-token persistence; no harness/workflow-only correction justified. Issue #41 `5481842956`.
- `NIGHT-WOZ-089`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching final ledger result or material Issue #41 handoff.
- No BeatGaler merge or PASS claim in this JOBS cycle; baseline unchanged.

## OWNERS — CYCLE 091

### AAA — `NIGHT-AAA-087` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-086` — F4 / 25.1 windows/auth
PRIMARY: sole bounded owner of #74/#84 product-auth lineage. Correct only the minimum product logic behind missing packaged-Tauri session-token persistence, refresh #84 onto the corrected exact #74 lineage, then require exact-head packaged Windows assertions for token persistence and AccountGate exit. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-090` — F2 / 12.1 runtime evidence
PRIMARY: READ-ONLY real-browser cold/warm startup evidence on exact live integration using existing canonical Web smoke/runtime path. Capture exact SHA, browser/runtime/build identity, timings and limitations. No code/PR/infra/integration mutation.  
CI-FALLBACK: NONE.

## Camino crítico global — CYCLE 091

1. F4/25.1 minimum #74 product-auth correction + refreshed #84 exact packaged Windows evidence, because the current literal journey is red on session-token persistence.
2. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
3. F2/12.1 real-browser cold/warm evidence.
4. F3/20.2 unblock #83 Draft→Ready only with a materially changed real tooling/human path; do not repeat the same failing connector transaction.
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

AAA executes `NIGHT-AAA-087`; BBB executes `NIGHT-BBB-086`; WOZ executes `NIGHT-WOZ-090`. No worker may mutate integration in CYCLE 091. Next JOBS cycle starts from live integration and exact handoffs only. Do not retry #83 until Ready tooling materially changes. `PLAN_HEALTH`: synced CYCLE 091; GitHub live prevails if it moves afterward.
