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

## Estado vivo — NIGHT-JOBS-094

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 browser cold/warm sigue abierto y execution-surface-blocked. 13.1 frozen. 13.2 conserva brecha factual Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-090` recibe la slice mínima, NO MERGE. 14.1 #81 parked/stale. 15.1 sigue abierto; `NIGHT-WOZ-093` toma exclusivamente el subgate destructivo Vaciar Trash/confirmación/recent-reauth con audit-first y sin tocar auth/legal.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 sigue OPEN/DRAFT, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green. `NIGHT-WOZ-092` terminó `BLOCKED_STOP`: la acción soportada Draft→Ready falló dentro del conector por `Repository.fullDatabaseId`; postcheck confirmó cero mutación. #83 queda PARKED sin owner de mutación en CYCLE 094. Runtime 160 permanece UNVERIFIED y además depende materialmente de integrar el waitlist aplicable.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #74 actual `d1593d3...`; #84 actual `c6c5ecb...`, OPEN/Ready/mergeable. Broad exact-head checks siguen verdes, pero literal Windows Auth run `33423712589` / job `99592060690` sigue FAILURE en `tests/e2e/auth-flow.e2e.mjs:64`: `Desktop login did not persist the returned session token.` `NIGHT-BBB-089` owns causal attribution + mínimo corrective/evidence; NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 094

- `NIGHT-AAA-089`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff or new F2/13.2 candidate.
- `NIGHT-BBB-088`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result/handoff and no post-C093 #74/#84 movement. Current literal auth evidence remains RED.
- `NIGHT-WOZ-092`: `BLOCKED_STOP / TOOLING_EXTERNAL`; exact #83 remained OPEN/DRAFT, same head/base/scope, mergeable and green. Dedicated Ready action failed with `GithubGraphQLAPIError` on undefined `Repository.fullDatabaseId`; no workaround/bypass, no merge, no integration mutation. Issue #41 `5482892475`.
- No BeatGaler merge or PASS claim in this JOBS cycle; integration baseline unchanged.

## OWNERS — CYCLE 094

### AAA — `NIGHT-AAA-090` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-089` — F4 / 25.1 windows/auth
PRIMARY: current #74/#84 exact-lineage first-causal-boundary attribution; only then minimum attributable platform/session correction, exact-lineage refresh and literal token-persistence + AccountGate-exit evidence with fresh exact-head CI. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-093` — F2 / 15.1 Trash destructive action
PRIMARY: audit-first current Trash purge path; reuse existing APIs; close/reduce only the literal permanent Empty Trash + strong confirmation + recent-reauth + no-false-success subgate. Scope excludes auth/session implementation and legal copy; bounded candidate/fresh CI only if a real gap exists; NO MERGE.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 094: NONE.** #83 is parked until the supported Ready path changes materially.

## Camino crítico global — CYCLE 094

1. F4/25.1 current exact #74/#84 packaged-auth failure: first-causal attribution → minimum corrective → literal packaged Windows proof.
2. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
3. F2/15.1 destructive Empty Trash subgate: current-behavior audit → minimum confirmation/recent-reauth/no-false-success corrective if needed.
4. F3/20.2 #83 process blocker: supported Draft→Ready tooling must be repaired or a newly supported authorized path must exist; do not repeat the same failed action.
5. After #83 integration, materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
6. F2/12.1 real-browser cold/warm evidence on a surface that can actually run Vite/WebdriverIO/Chrome.
7. F3/19.1 external canonical hostname/API/DNS/TLS/status/OAuth/sender/deployment facts/actions.
8. Frozen stale candidates (#81/#76/#72) only after safe explicit reconciliation; F4 signing/notarization/hardware/tester execution and F0/F1 external/RO tails remain real blockers.

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

AAA executes `NIGHT-AAA-090`; BBB executes `NIGHT-BBB-089`; WOZ executes `NIGHT-WOZ-093`. No worker may mutate integration in CYCLE 094. #83 remains parked on a verified connector blocker until that path changes materially. `PLAN_HEALTH`: synced CYCLE 094; GitHub live prevails if it moves afterward.
