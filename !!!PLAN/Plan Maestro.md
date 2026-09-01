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

## Estado vivo — NIGHT-JOBS-111

- **Release público:** 🔴 `NO-GO`.
- **Integración estable al preflight/final assignment:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.
- **Último merge material:** PR #91 → `134a293985c314eb09c238115e3bcb71e79f1810`, parents `78dd55b...` + `35d44a0d...`; exact-head CI aplicable PASS. Claim máximo: F2/12.1 bootstrap Worker deadline integrado; 12.1 no es PASS.
- **Nuevo runtime/candidate F2/12.1:** PR #92 OPEN/Ready/mergeable @ `9947380ce8095b718a400d1e7781d21e67b29be9`, exact base `134a293...`. Evidencia declarada del deployed surface: `.bg-account-gate` ya estaba montado mientras el static `#beatgaler-startup-loader` seguía mostrando `Loading Galer...`. Candidate remueve el loader solo al render signed-out del AccountGate y no pretende alterar authenticated bootstrap. Exact-head Web/shared y otros checks observados verdes; WOZ110 debe verificar todos los required checks antes de cualquier merge.
- **F0/0.20 OAuth rotation:** `[x] DONE` por readiness software #90 + owner-side credential replacement/deploy/fresh production OAuth E2E/old credential removal verificados, sin exponer secretos.
- **F0:** núcleo técnico principal cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 = **18+**. 0.8 review `[x]` administrativamente por AI-assisted review + decisión RO; no implica compliance ni cierre de P0/P1. #88 technical Authenticode seam integrado; production signing `NO-GO`. #89 OPEN/Ready @ `daf87da6...`, stale base `816f946c...`; **PARKED/UNASSIGNED CYCLE111** para no competir con #92.
- **F1:** D6–D10.1 PASS. D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`. 1.7 debe resolver/clasificar blockers; 1.8 decisión RO final; 1.9 solo después de GO.
- **F2:** 11.1/11.2/12.2 cerrados. 12.1 sigue `[🟡]`: #91 integrated + #92 exact-base candidate; después de integración todavía se necesita deployment/runtime aplicable y cold/warm evidence. 13.2 durable Review y 15.1 Trash siguen abiertos.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment real externo. #76 stale/13+ contradice 18+. 19.2 sigue OPEN con 12 P0 + 14 P1 + P2/P3 + UNVERIFIED. #83 OPEN/DRAFT; runtime160 no probado.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. BBB105 ahora probó `HARNESS_ONLY_PROVEN` para la broad fetch interception de #84, pero STOP correcto por refresh/reconstruction inseguro bajo autoridad previa. Windows packaged Auth permanece `NOT_PASS`.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 111

- `NIGHT-AAA-106`: sin RESULTADO DEL TURNO/matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-105`: `BLOCKED_STOP / HARNESS_ONLY_PROVEN_REFRESH_UNSAFE`. Reusable: `POST /plugin%3Awdio%7Cget_window_states` pertenece al tráfico WDIO/Tauri service y el broad fetch interceptor del harness es la frontera implicada. No hubo mutation ni fresh PASS. Successor recibe autoridad bounded para reconstruir el evidence candidate desde live baseline, sin product mutation.
- `NIGHT-WOZ-109`: sin RESULTADO DEL TURNO/matching handoff verificable → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- Cambio concurrente real después de CYCLE110: PR #92 apareció directamente sobre `134a293...`; REUSE-FIRST obliga consumirlo antes de crear otro corrective del mismo runtime gap.
- JOBS no modificó código BeatGaler ni infraestructura.

## D10.2 — mapa de readiness alpha interna

- `PROVEN`: D6–D10.1 y F0/0.20 cerrados.
- `HARD_BLOCKER`: F4/25.1 literal packaged Windows Auth PASS.
- `ACTIVE_RUNTIME_BLOCKER`: F2/12.1 #92 + posterior deployment/runtime/cold-warm proof.
- `CLOSE_OR_RO_EXCLUDE`: F2/13.2 durable Review; F2/15.1 recent-reauth/Empty Trash.
- `SECURITY_RECHECK_BEFORE_RO`: F0/0.9 #89 DNS-rebinding/SSRF P1 debe resolverse/revalidarse antes de 1.8.
- `RO_APPLICABILITY_DECISION`: F3/18.2, 19.2, 20.2 solo pueden salir de alpha 3–5 cuentas mediante decisión explícita de scope; excluir de alpha no marca PASS de release.
- `RELEASE_ONLY/EXTERNAL`: production signing/notarization, hardware/tester matrix amplia y release/admin tails continúan `NO-GO`.

## OWNERS — CYCLE 111

### AAA — `NIGHT-AAA-107` — F2 / 13.2
PRIMARY: minimum durable Review Save/Save All completion/no-silent-loss corrective; visible success only after durable completion; failure/retry/partial Save All; focused Web/no-Tauri tests; bounded candidate. **NO MERGE.**  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-106` — F4 / 25.1 / #84
PRIMARY: using BBB105 `HARNESS_ONLY_PROVEN`, reconstruct a clean live-baseline evidence candidate preserving only authorized lineage, apply minimum WDIO/Tauri IPC bypass in harness/service boundary, keep auth stubs/assertions unchanged, then fresh packaged Windows Auth + exact-head CI. **NO PRODUCT MUTATION / NO MERGE.**  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-110` — F2 / 12.1 / #92
PRIMARY: REUSE #92; verify bounded signed-out loader semantics + exact base/head + all applicable required checks; if exact/green/race-free, expected-head merge **#92 only** and verify merge SHA/parents. Maximum claim remains corrective integrated, not 12.1 PASS.  
CI-FALLBACK: only during genuine `WAITING_CI`: READ-ONLY F1/1.7 blocker-classification prep; no implementation/plan/provider/#89 mutation.

**Integration mutation authorization CYCLE 111: WOZ110 / PR #92 ONLY, after exact-base/head + all applicable required CI SUCCESS + race-free expected-head.**

## Camino crítico global — recalculado desde GitHub vivo

1. **F2/12.1 / #92:** exact-base candidate already exists and directly addresses the observed deployed signed-out loader defect; verify/integrate first, then deployment/runtime proof.
2. **F4/25.1 / #84:** reconstruct current harness evidence candidate, minimum proven IPC-boundary fix, literal packaged Windows Auth PASS.
3. **F2/13.2:** durable Review completion/no-silent-loss, or explicit RO alpha exclusion.
4. **F0/0.9 / #89:** refresh/revalidate DNS-rebinding/SSRF P1 after #92 lane clears.
5. **F2/12.1 runtime tail:** deploy resulting canonical baseline and record applicable signed-out/authenticated + cold/warm evidence.
6. **F2/15.1:** recent-reauth + strong confirmation + durable deterministic purge, or explicit RO alpha exclusion.
7. **F1/1.7:** consolidate/classify remaining blockers and F3 18.2/19.2/20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.
8. **F1/1.8:** RO GO/NO-GO for 3–5 account alpha; **1.9** only after GO.
9. **Release path paralelo:** F0 1.2/2.2, productive signing/notarization, F3 provider/legal/capacity and tester/hardware evidence remain open.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no bot free; normal exclusivity per vault.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-107`; BBB `NIGHT-BBB-106`; WOZ `NIGHT-WOZ-110` y posee la única conditional integration lane sobre #92. #89 queda parked/unassigned este ciclo. #85 sigue external-owned; #76/#83 no se reintentan sin cambio material. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 111; GitHub live prevalece si cambia después.
