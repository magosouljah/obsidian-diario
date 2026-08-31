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

## Estado vivo — NIGHT-JOBS-097

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 browser cold/warm sigue abierto y execution-surface-blocked. 13.1 frozen. 13.2 conserva brecha Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-093` recibe la slice mínima, NO MERGE. 14.1 #81 parked/stale. 15.1 sigue abierto: audit WOZ094 probó que Beat Empty Trash carece de strong confirmation y de una seam recent-reauth reutilizable; además la UI retira rows optimistamente antes de purge completion. Trash queda sin owner de implementación hasta que auth/session provea una seam bounded reutilizable.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 sigue OPEN/DRAFT, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green; supported Draft→Ready path sigue sin cambio material desde el connector blocker de WOZ092. #83 permanece PARKED sin owner de mutación. Runtime 160 permanece UNVERIFIED. `NIGHT-WOZ-096` toma F3/19.1 public production-surface evidence READ-ONLY.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #74 `d1593d3...` y #84 `c6c5ecb...` siguen OPEN/Ready/mergeable sobre base exacta. Literal Windows Auth run `33423712589` / job `99592060690` sigue FAILURE. Late BBB088 evidence (`5483886991`) acota el primer límite causal: después de Sign in el token nunca es observable en localStorage, pero los logs simultáneos de `@wdio/tauri-service`/DirectEval dejan sin resolver producto vs mock/service. `NIGHT-BBB-092` queda diagnostic-only para resolver ese lado causal; NO MERGE y sin product mutation.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 097

- `NIGHT-AAA-092`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff or new F2/13.2 candidate.
- `NIGHT-BBB-091`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching result/handoff and no #74/#84 movement.
- Late `NIGHT-BBB-088` / Issue #41 `5483886991`: `BLOCKED_STOP / FIRST_CAUSAL_BOUNDARY_ATTRIBUTED`; consumed as factual evidence despite arriving after CYCLE 096. It does not satisfy BBB091 and does not PASS F4/25.1. It proves the next safe step is diagnostic instrumentation, not a speculative corrective.
- `NIGHT-WOZ-095`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result or matching public-surface handoff.
- No BeatGaler merge or PASS claim in this JOBS cycle; integration baseline unchanged.

## OWNERS — CYCLE 097

### AAA — `NIGHT-AAA-093` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Tauri/Desktop call-spies; bounded candidate/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-092` — F4 / 25.1 windows/auth
PRIMARY: diagnostic-only instrumentation on exact #84 submit boundary; prove whether `/auth/login` mock, `set_cloud_auth_token`, product session write/gate transition or WDIO/Tauri service capability fails first; unchanged literal assertions; one fresh exact packaged Windows run + applicable exact-head CI; NO PRODUCT CORRECTIVE, NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-096` — F3 / 19.1
PRIMARY: public production-surface evidence READ-ONLY; verify externally observable DNS/TLS/HTTP/status/support/security-abuse facts, mark provider/private facts UNVERIFIED, STOP before any mutation/credentials/legal work.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 097: NONE.** #83 remains parked until the supported Ready path changes materially.

## Camino crítico global — CYCLE 097

1. F4/25.1 exact #74/#84 packaged-auth failure: resolve product-vs-mock/service causal side via minimum instrumentation; only then authorize a corrective.
2. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
3. F2/15.1 Trash destructive subgate depends on a bounded reusable recent-reauth seam under auth/session ownership; then minimum confirmation + deterministic non-optimistic purge wiring/tests.
4. F3/20.2 #83 process blocker: supported Draft→Ready tooling must materially change before retry; no bypass.
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

AAA executes `NIGHT-AAA-093`; BBB executes `NIGHT-BBB-092`; WOZ executes `NIGHT-WOZ-096`. No worker may mutate integration in CYCLE 097. BBB must resolve the causal side before any further windows/auth corrective. #83 remains parked on a verified connector blocker until that path changes materially. Trash implementation remains paused until a bounded reusable recent-reauth seam exists under the proper auth/session owner. `PLAN_HEALTH`: synced CYCLE 097; GitHub live prevails if it moves afterward.
