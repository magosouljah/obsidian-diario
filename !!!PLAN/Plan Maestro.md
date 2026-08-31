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

## Estado vivo — NIGHT-JOBS-093

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 browser cold/warm sigue abierto y execution-surface-blocked. 13.1 frozen. 13.2 conserva brecha factual Review Save/Save All durable-completion/no-silent-loss; AAA088 no produjo candidato verificable y `NIGHT-AAA-089` recibe la slice mínima; NO MERGE. 14.1 #81 parked/stale.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 sigue OPEN/DRAFT, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green. `NIGHT-WOZ-092` es único owner para supported Draft→Ready→exact/race recheck→expected-head merge. Runtime 160 permanece UNVERIFIED aun si #83 integra.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #74 actual `d1593d3...`; #84 actual `c6c5ecb...`. Compare exacto prueba que #84 contiene #74 y está 3 commits ahead. Fresh exact-head broad checks son verdes, pero literal Windows Auth run `33423712589` / job `99592060690` sigue FAILURE en `tests/e2e/auth-flow.e2e.mjs:64`: `Desktop login did not persist the returned session token.` `NIGHT-BBB-088` owns causal attribution + mínimo corrective/evidence; NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 093

- `NIGHT-AAA-088`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching final result/handoff or new material F2/13.2 PR.
- `NIGHT-BBB-087`: no correctly labelled final night result; live bounded branch work exists. #74 moved to `d1593d3...`, #84 to `c6c5ecb...`; current exact packaged Windows Auth resolved RED. Processed `PARTIAL_LIVE_EVIDENCE / NOT_PASS`; any earlier WAITING_CI is obsolete.
- `NIGHT-WOZ-091`: `NO_RESULT / SUPERSEDED / NOT_PASS`; #83 remains unchanged OPEN/DRAFT.
- No BeatGaler merge or PASS claim in this JOBS cycle; integration baseline unchanged.

## OWNERS — CYCLE 093

### AAA — `NIGHT-AAA-089` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-088` — F4 / 25.1 windows/auth
PRIMARY: sole bounded owner of current #74/#84 lineage. Attribute the first causal boundary of the current exact packaged-auth failure before modifying product; only then apply the minimum attributable platform/session correction, refresh #84 exact lineage, and require literal token persistence + AccountGate exit plus fresh exact-head CI. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-092` — F3 / 20.2 #83 integration transaction
PRIMARY: dedicated Draft→Ready on exact #83; same-head/base/scope/mergeability + exact CI/race postcheck; expected-head merge only if unchanged/green. Do not claim 20.2 PASS; runtime 160 remains separate.  
CI-FALLBACK: NONE.

## Camino crítico global — CYCLE 093

1. F3/20.2 #83 supported Ready→exact-head/race recheck→integration; prerequisite for meaningful durable-waitlist capacity validation.
2. F4/25.1 current exact #74/#84 failure: causal attribution → minimum corrective → literal packaged Windows proof.
3. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
4. F3/20.2 post-#83 materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
5. F2/12.1 real-browser cold/warm evidence on a surface that can actually run Vite/WebdriverIO/Chrome.
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

AAA executes `NIGHT-AAA-089`; BBB executes `NIGHT-BBB-088`; WOZ executes `NIGHT-WOZ-092`. Only WOZ092 may mutate integration, and only for exact #83 under stated race/exact-head gates. `PLAN_HEALTH`: synced CYCLE 093; GitHub live prevails if it moves afterward.
