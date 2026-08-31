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

## Estado vivo — NIGHT-JOBS-081

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, parents `957f97771b7a15554cf6e002fe9eb215c71a65cc` + `a3c4d56e8317d7711832154ecc72afe581d2b309`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime abierto; 13.1 frozen; 13.2 executable evidence sigue abierto y pasa a AAA077 sobre live base; 14.1 #81 stale/parked.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 durable waitlist sigue OPEN/DRAFT head `52b58f56...` pero base `957f9777...` quedó stale tras #79; WOZ080 owns reconciliation + fresh CI + readiness/integration. Runtime 160/safety-margin sigue pendiente.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #79 readiness artifact integrado; BBB076 toma windows/auth #71/#74 current-evidence slice, NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 081

- `NIGHT-BBB-075`: `PASS`; #79 integrado como `816f946c...`; merge SHA/parents verificados; máximo claim F4/25.2 internal readiness artifact integrated.
- `NIGHT-AAA-076`: no final result/handoff observado antes del ciclo; superseded por material baseline move, not PASS.
- `NIGHT-WOZ-079`: no final result/handoff observado antes del ciclo; superseded por material baseline move, not PASS.

## OWNERS — CYCLE 081

### AAA — `NIGHT-AAA-077` — F2 / 13.2
PRIMARY: REUSE AAA071; executable Web/Tauri `invoke`/`listen` call-spies + Save All partial-failure/conflict/retry/no-silent-loss on live base. Solo fix F2 mínimo si evidence falla. Fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-076` — F4 / 25.1 windows/auth
PRIMARY: REUSE #71/#74; determine safe history-preserving refresh onto live base, fresh exact-head CI + authoritative Windows auth journey. If reconciliation unsafe, STOP with gap map. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-080` — F3 / 20.2 / #83
PRIMARY: REUSE stale #83, history-preserving reconcile onto `816f946c...`, focused tests + fresh exact-head CI, authorized Draft→Ready, and only if exact/race-free then expected-head merge + verify parents. WOZ/#83 is the only integration mutation authorized.  
CI-FALLBACK: during genuine WAITING_CI/external wait, REUSE #78 READ-ONLY runtime evidence for 80 expected / 160 validation; no code/infra/provider mutation.

## Camino crítico global — CYCLE 081

1. #83 durable waitlist: reconcile + fresh CI + readiness/integration.
2. F3/20.2 runtime materially applicable 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin.
3. F2/13.2 executable Web/Tauri boundary + Save All no-silent-loss evidence/fix mínimo.
4. F4/25.1 windows/auth current evidence via #71/#74 reuse.
5. F2/12.1 real-browser cold/warm evidence.
6. F2/14.1 #81 and F3/19.x #76 stale/frozen until safe reconciliation.
7. F4 signing/notarization/hardware/tester execution external.
8. F0/F1 provider/legal/operational tails external/RO.

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

AAA executes `NIGHT-AAA-077`; BBB executes `NIGHT-BBB-076`; WOZ executes `NIGHT-WOZ-080`. Next JOBS cycle starts from live integration and processes exact results only. `PLAN_HEALTH`: synced CYCLE 081; GitHub live prevails if it moves afterward.
