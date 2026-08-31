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

## Estado vivo — NIGHT-JOBS-100

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos. Requisito canónico v1: **18+**.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 requiere decisión RO. WOZ099 puede producir únicamente un decision map READ-ONLY si su PRIMARY #76 entra realmente en WAITING_CI.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 browser cold/warm sigue abierto y execution-surface-blocked. 13.1 frozen. 13.2 conserva brecha probada Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-096` recibe la mínima slice ejecutable, NO MERGE. 14.1 #81 parked/stale. 15.1 sigue bloqueado: falta strong confirmation, bounded recent-reauth seam reutilizable y action boundary no optimista; no owner mientras BBB095 trabaja auth/session evidence.
- **F3:** 17.1/17.2/18.1 cerrados. `NIGHT-WOZ-098` redujo 18.2 a reconciliation core/exception queue `PROVEN_SOFTWARE` vs provider/payment staging/financial/RO rows aún externas; 18.2 global permanece abierto. 19.1 queda `PARTIAL / EXTERNAL`. 19.2 tiene ahora un gap factual ejecutable: #76 es reusable pero stale y sus Privacy/Terms dicen 13+/minimum age, contradiciendo el requisito canónico v1 18+; además su propio PR reconoce copy legal viejo/placeholders en Settings. `NIGHT-WOZ-099` reconcilia #76, NO MERGE. 20.1 software integrated. #83 sigue `OPEN/DRAFT`, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green; supported Draft→Ready path sin cambio material desde blocker WOZ092, por lo que permanece PARKED. Runtime 160 permanece UNVERIFIED y dependency-gated a eventual integración aplicable.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #74 `d1593d3...` y #84 `28c3810c...` siguen OPEN/Ready/mergeable sobre base exacta. Exact #84 Windows Auth Journey run `33439899177` / job `99645269221` continúa `FAILURE`; trace reusable = repeated `boundary=unexpected-request`, `gatePresent=true`, `tokenPresent=false`. `NIGHT-BBB-095` queda diagnostic-only para atribuir la primera request inesperada; solo harness-only permite corrección mínima del harness. NO PRODUCT CORRECTIVE especulativo, NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 100

- `NIGHT-AAA-095`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff, candidate PR or material F2/13.2 movement.
- `NIGHT-BBB-094`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result/handoff or material #84 movement. Current exact #84 Windows Auth remains RED.
- `NIGHT-WOZ-098`: `BLOCKED_STOP / F3/18.2 EVIDENCE_GAP_MAP_UPDATED`; consumed as factual evidence. Reconciliation core/exception queue software is proven; real/staging provider/payment scenario closure remains external/unverified. Issue #41 `5485068226`.
- New factual duplicate/reuse finding: #76 already owns the legal/public-route material but is not safe unchanged because its eligibility conflicts with canonical 18+ and its in-app Settings copy remains stale. Reuse #76; do not create duplicate legal PR.
- No BeatGaler merge, integration mutation or PASS claim occurred in this JOBS cycle; baseline unchanged.

## OWNERS — CYCLE 100

### AAA — `NIGHT-AAA-096` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Web/Tauri call-spies; one bounded candidate/fresh exact-head CI if duplicate-check clean; **NO MERGE**.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-095` — F4 / 25.1 windows/auth
PRIMARY: identify/attribute first exact `unexpected-request` on #84; preserve #74/#84 as sole lineages; only if `HARNESS_ONLY` may minimally fix #84 harness and rerun unchanged literal assertions; if product implicated STOP `PRODUCT_SIDE_PROVEN`; **NO PRODUCT CORRECTIVE / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-099` — F3 / 19.2
PRIMARY: REUSE-FIRST #76 history-preserving reconciliation against live baseline; align canonical **18+** eligibility, current approved legal/business terms and Settings canonical-copy reuse; focused route/build evidence + fresh exact-head CI; **NO MERGE**. Independent legal review/deployment remain UNVERIFIED.  
CI-FALLBACK: only if PRIMARY is genuinely `WAITING_CI`: F1/D10.2 `ALPHA_READINESS_DECISION_MAP` READ-ONLY; classify prerequisites PROVEN/BLOCKED_EXTERNAL/RO_DECISION_REQUIRED; no alpha execution or external mutations; STOP before RO/off-provider action and recheck PRIMARY CI.

**Integration mutation authorization CYCLE 100: NONE.**

## Camino crítico global — CYCLE 100

1. **F4/25.1 windows/auth:** exact #84 packaged journey remains RED → attribute first unexpected request → only proven harness-only correction may run; product side requires new JOBS authorization later.
2. **F2/13.2 Review Save/Save All:** durable completion/no-silent-loss correction + executable Web/no-Tauri evidence.
3. **F3/19.2 #76:** reconcile existing stale candidate to canonical 18+ + current Settings legal copy; do not duplicate or integrate before exact-head evidence; independent legal review/deployment remain separate.
4. **F2/15.1 Empty Trash:** requires bounded reusable recent-reauth seam under proper auth/session ownership; only then strong confirmation + deterministic non-optimistic purge wiring/tests.
5. **F3/20.2 #83:** supported Draft→Ready tooling must materially change before retry; no bypass. After integration, still require materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
6. **F2/12.1:** real-browser cold/warm evidence requires a surface that can actually run Vite/WebdriverIO/Chrome.
7. **F3/18.2:** remaining rows require authorized provider/staging/payment/RO evidence; software inspection is exhausted for current useful proof.
8. **F3/19.1:** external canonical DNS/TLS/API/status/OAuth/sender/deployment evidence; do not repeat incapable surface.
9. F0/F1 external/RO tails, stale candidates requiring explicit safe reconciliation, and F4 signing/notarization/hardware/tester execution remain real blockers.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation details hidden.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud does not relay beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no free bot; exclusivity per vault is normal path.
- v1 is not published free-only; eligibility canónica v1 = **18+**.
- YouTube exists Desktop/Web; Web does not call Tauri.

## NEXT

AAA executes `NIGHT-AAA-096`; BBB executes `NIGHT-BBB-095`; WOZ executes `NIGHT-WOZ-099`. No worker may mutate integration in CYCLE 100. Do not authorize a Windows-auth product corrective until BBB095 proves product-side causality; do not reassign Trash implementation until a bounded reusable recent-reauth seam exists under correct auth/session ownership. Do not retry #83 Ready until the supported path changes materially. Do not claim F3/18.2 provider/payment PASS from software tests. Reuse and reconcile #76 instead of opening a second legal candidate. `PLAN_HEALTH`: synced CYCLE 100; GitHub live prevails if it moves afterward.
