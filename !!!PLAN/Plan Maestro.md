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

## Estado vivo — NIGHT-JOBS-098

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c...`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 requiere decisión RO. No hay trabajo técnico nocturno interno que pueda fabricar esos cierres.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 browser cold/warm sigue abierto y execution-surface-blocked. 13.1 frozen. 13.2 conserva brecha probada Review Save/Save All durable-completion/no-silent-loss; `NIGHT-AAA-094` recibe la mínima slice ejecutable, NO MERGE. 14.1 #81 parked/stale. 15.1 sigue bloqueado: falta strong confirmation, bounded recent-reauth seam reutilizable y action boundary no optimista; no owner mientras BBB093 trabaja auth/session evidence.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global permanece abierto y `NIGHT-WOZ-097` toma únicamente reconciliación factual READ-ONLY de escenarios provider/payment. 19.1 queda `PARTIAL / EXTERNAL` tras `NIGHT-WOZ-096`: la superficie disponible no produjo DNS/TLS/HTTP autoritativos y provider/deployment/OAuth/sender privados siguen UNVERIFIED. 20.1 software integrated. #83 sigue `OPEN/DRAFT`, exact base `816f946c...`, head `803b2143...`, mergeable y exact-head green; supported Draft→Ready path sin cambio material desde blocker WOZ092, por lo que permanece PARKED. Runtime 160 permanece UNVERIFIED y dependency-gated a eventual integración aplicable.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #74 `d1593d3...` y #84 `c6c5ecb...` siguen OPEN/Ready/mergeable sobre base exacta. Exact #84 Windows Auth Journey run `33423712589` continúa `FAILURE`; Desktop Portability y demás gates actuales observados permanecen verdes. `NIGHT-BBB-093` queda diagnostic-only para resolver product auth/session vs mocked Tauri/WDIO-service causal side; NO PRODUCT CORRECTIVE, NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 098

- `NIGHT-AAA-093`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff, candidate PR or material F2/13.2 movement.
- `NIGHT-BBB-092`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final matching handoff, no #74/#84 movement and no fresh literal Windows Auth run. Current exact #84 Windows Auth remains RED.
- `NIGHT-WOZ-096`: `BLOCKED_STOP / F3/19.1 PUBLIC_SURFACE_EVIDENCE_BOUNDED`; consumed as factual evidence. No mutations; authoritative DNS/TLS/HTTP and private provider/deployment/OAuth/sender facts remain UNVERIFIED. 19.1 stays PARTIAL/EXTERNAL.
- No BeatGaler merge, integration mutation or PASS claim occurred in this JOBS cycle; baseline unchanged.

## OWNERS — CYCLE 098

### AAA — `NIGHT-AAA-094` — F2 / 13.2
PRIMARY: minimum Review Save/Save All durable action-boundary correction; per-beat saved/conflict/failed + retry/no-silent-loss + focused executable Web/Tauri call-spies; one bounded candidate/fresh exact-head CI if duplicate-check clean; **NO MERGE**.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-093` — F4 / 25.1 windows/auth
PRIMARY: diagnostic-only instrumentation on exact #84 first post-submit boundary; distinguish `/auth/login` mock/response, `set_cloud_auth_token`, AccountGate/session write/gate transition vs WDIO/Tauri service failure; unchanged literal assertions; one fresh exact packaged Windows run + applicable exact-head CI; **NO PRODUCT CORRECTIVE / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-097` — F3 / 18.2
PRIMARY: provider/payment global scenario evidence map **READ-ONLY**; classify literal current 18.2 scenarios as `PROVEN_SOFTWARE`, `PARTIAL` or `UNVERIFIED_EXTERNAL` with exact existing evidence; no provider/payment/code/infra mutations and no PASS claim.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 098: NONE.**

## Camino crítico global — CYCLE 098

1. **F4/25.1 windows/auth:** exact #74/#84 packaged journey remains RED → resolve first causal side with minimum diagnostic evidence → only then authorize any corrective.
2. **F2/13.2 Review Save/Save All:** durable completion/no-silent-loss correction + executable Web/no-Tauri evidence.
3. **F2/15.1 Empty Trash:** requires bounded reusable recent-reauth seam under proper auth/session ownership; only then strong confirmation + deterministic non-optimistic purge wiring/tests.
4. **F3/20.2 #83:** supported Draft→Ready tooling must materially change before retry; no bypass. After integration, still require materially applicable runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin vs expected 80.
5. **F2/12.1:** real-browser cold/warm evidence requires a surface that can actually run Vite/WebdriverIO/Chrome.
6. **F3/18.2:** reduce global provider/payment unknowns to exact external gaps without confusing software proof with live-provider proof.
7. **F3/19.1:** now external/provider evidence; do not repeat WOZ096 on the same incapable surface.
8. F0/F1 external/RO tails, stale candidates (#81/#76/#72) requiring explicit safe reconciliation, and F4 signing/notarization/hardware/tester execution remain real blockers.

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

AAA executes `NIGHT-AAA-094`; BBB executes `NIGHT-BBB-093`; WOZ executes `NIGHT-WOZ-097`. No worker may mutate integration in CYCLE 098. Do not authorize a Windows-auth corrective until BBB093 resolves causal side or unchanged literal assertions pass. Do not reassign Trash implementation until a bounded reusable recent-reauth seam exists under correct auth/session ownership. Do not retry #83 Ready until the supported path changes materially. Do not repeat F3/19.1 public lookup without a materially better evidence surface. `PLAN_HEALTH`: synced CYCLE 098; GitHub live prevails if it moves afterward.
